/**
 * Fullstack agents Conductor — main control loop.
 *
 * Wires the Agent SDK to the circuit breaker, SQLite/libSQL state, and Telegram escalation.
 * One worker process can run several of these; jobs are claimed atomically so they don't collide.
 *
 * DURABLE RESUME: every run records its SDK session_id on the job. If the run is paused by a
 * token/rate limit, or the process dies mid-flight, the job is requeued (deferred) WITH that
 * session_id; a later claim passes `resume: <session_id>` to query() and continues where it
 * left off — minutes or many hours later. Cost is NOT tracked or capped; the only runaway
 * control is loop-detection (see breaker.ts).
 *
 * NOTE ON THE SDK SURFACE: the @anthropic-ai/claude-agent-sdk `query()` streams messages of
 * several shapes (assistant, tool_use, tool_result, result, plus rate-limit notifications).
 * The SDK is moving fast (TS V2 in preview as of 2026-06), so the exact field names below are
 * mapped in ONE place — `mapSdkMessage()` — adjust there if the shape drifts. Everything else
 * depends only on our normalized Event type, which is unit-tested.
 */
import { createHash } from 'node:crypto';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import { query } from '@anthropic-ai/claude-agent-sdk';
import { Store, Job, Step } from './store';
import { evaluate, initState, BreakerState, BreakerLimits, DEFAULT_LIMITS, KIND_MIN_TURNS, Event } from './breaker';
import { runStep, StepRecord } from './steprunner';
import { makeSdkDeps } from './agent-runner';
import { resolveProfilePlugins, resolveWorkDir } from './profiles';
import { tgConfigFromEnv, withJobThread, notifyEscalation, notifyDone, TelegramConfig } from '../escalation/telegram';
import { startWebhookServer, startTelegramPolling } from '../escalation/bot-callback';

/** Positive number from env, or the default. `Number('')` is 0, and .env.example
 *  itself ships empty values (`HO_WORKER_ID=`), so a blank line in .env used to
 *  become a real 0 with real consequences: HO_STALE_RUN_SECS=0 made every LIVE
 *  claimed job look stale on every poll (endless requeue + double-running the
 *  same job), HO_RESUME_BACKOFF_SECS=0 turned a rate-limit pause into a hot loop
 *  against the provider, HO_HEARTBEAT_MS=0 wrote to the DB on every stream event.
 *  Every tunable below goes through this — a blank line in .env must never be a setting. */
function posEnv(name: string, dflt: number): number {
  const raw = process.env[name];
  if (raw === undefined || raw.trim() === '') return dflt;
  const n = Number(raw);
  if (!Number.isFinite(n) || n <= 0) {
    console.warn(`${name}=${JSON.stringify(raw)} не является положительным числом — беру ${dflt}`);
    return dflt;
  }
  return n;
}

const WORKER_ID = (process.env.HO_WORKER_ID || '').trim() || `ho-${process.pid}`;
const RESUME_BACKOFF_SECS = posEnv('HO_RESUME_BACKOFF_SECS', 3600); // wait when limit gives no retry-after
const STALE_RUN_SECS = posEnv('HO_STALE_RUN_SECS', 900);            // requeue runs stuck this long
const HEARTBEAT_MS = posEnv('HO_HEARTBEAT_MS', 60000);              // bump claimed_at while a job streams, so parallel workers don't stale-recover a live job
const CONDUCTOR_WORKERS = Math.max(1, Math.floor(posEnv('CONDUCTOR_WORKERS', 1))); // parallel worker loops in this process (each claims jobs independently; claim is atomic)
/** A job that reliably kills its worker must not be retried forever: recoverStale
 *  requeues with not_before=now and no backoff, so a poison job spins on the
 *  queue burning tokens and starving everything behind it. */
const MAX_ATTEMPTS = posEnv('HO_MAX_ATTEMPTS', 5);
/**
 * Turns a run must make before we treat it as REAL progress against a usage window.
 *
 * WHY NOT 1: on an exhausted window the agent still pushes 2–5 turns through before the limit
 * bites. Treating "any turn at all" as progress reset the streak to 0 on every pause, which held
 * the backoff at its first rung (~50s) and re-armed the "first pause" Telegram notice each time —
 * job 41 on 2026-07-28 produced 6 pauses in 7 minutes, all streak 0, one message each. A couple of
 * turns is not the window opening, it is the run-up to the same wall.
 */
const MIN_PROGRESS_TURNS = posEnv('HO_MIN_PROGRESS_TURNS', 10);
/**
 * Only announce a rate-limit pause when the wait is long enough to be worth a human's attention
 * (or when it is this job's first). Throttling on the STREAK could never work: the streak is
 * exactly the thing that breaks when the signal is wrong.
 */
const PAUSE_NOTIFY_MIN_SECS = posEnv('HO_PAUSE_NOTIFY_MIN_SECS', 600);
/** Extra turns granted when the human waves a `turns` escalation through. */
const TURN_GRANT = posEnv('HO_TURN_GRANT', 60);
/** How many times ONE run may be resumed by a human "continue" before we stop asking. */
const MAX_CONTINUES = posEnv('HO_MAX_CONTINUES', 5);
/** How long to wait for a human decision before parking the job (escalation stays open). */
const ESC_WAIT_SECS = posEnv('HO_ESC_WAIT_SECS', 1800);
/** Re-ping Telegram this often while an escalation sits unanswered. */
const ESC_REMIND_SECS = posEnv('HO_ESC_REMIND_SECS', 600);
/** How long a job sleeps after an unanswered escalation before it asks again. */
const ESC_PARK_SECS = posEnv('HO_ESC_PARK_SECS', 1800);
/** Give up (leave the job 'escalated') after this many unanswered park cycles. */
const MAX_ESC_PARKS = posEnv('HO_MAX_ESC_PARKS', 8);

/**
 * Backoff ladder for CONSECUTIVE no-progress rate-limit pauses, in seconds.
 * The last entry repeats forever.
 *
 * WHY A LADDER: the structured `rate_limit` SDK message usually carries no `retry_after`,
 * so breaker.ts falls back to a flat 60s. Anthropic's usage windows are measured in HOURS,
 * so 60s retries can never clear one — on 2026-07-27 job 30 burned 193 zero-turn runs over
 * 3h22m waiting out a 5-hour window. The ladder waits out the same window in ~8 attempts.
 * Capped at 30 min so a job never idles longer than that once the window actually clears.
 */
const PAUSE_LADDER = [60, 300, 900, posEnv('HO_PAUSE_MAX_BACKOFF_SECS', 1800)];

/** Pick the wait before re-claiming a rate-limited job. A server-supplied retry_after always wins. */
export function backoffForStreak(streak: number, retryAfterSecs?: number): number {
  if (retryAfterSecs && retryAfterSecs > 0) return retryAfterSecs;
  const base = PAUSE_LADDER[Math.min(Math.max(streak, 0), PAUSE_LADDER.length - 1)];
  return Math.max(30, Math.round(base * (0.8 + Math.random() * 0.4))); // ±20% jitter, de-synchronises workers
}

const HERMES_SYSTEM_PROMPT =
  'You are the Fullstack-agents orchestrator described in this project\'s CLAUDE.md. Plan, delegate to ' +
  'the specialized subagents, coordinate via the scratchpad protocol, and run the quality gate ' +
  '(qa-engineer then security-auditor) before declaring done. Never run production-affecting ' +
  'commands without an explicit ask — they are gated.';

function limitsForJob(j: Job): BreakerLimits {
  const kindMin = KIND_MIN_TURNS[j.kind] ?? 0;
  const dbMax = j.max_turns ?? DEFAULT_LIMITS.maxTurns;
  return {
    maxTurns: Math.max(dbMax, kindMin),  // floor from kind, but never reduce a higher DB value
    maxWallSecs: j.max_wall_secs ?? DEFAULT_LIMITS.maxWallSecs,
    stuckRepeats: posEnv('HO_STUCK_REPEATS', DEFAULT_LIMITS.stuckRepeats),
    stuckRepeatsReadOnly: posEnv('HO_STUCK_REPEATS_READONLY', DEFAULT_LIMITS.stuckRepeatsReadOnly),
  };
}

/** Heuristic: does this error look like a token/quota/rate limit we should pause-and-resume on? */
function isLimitError(detail: string): boolean {
  return /rate.?limit|quota|usage limit|too many requests|overloaded|429|insufficient|credit/i.test(detail);
}

/**
 * `HO_PAUSE_ON_OVERAGE=1` restores the pre-2026-09-04 behaviour: pause on ANY rejected
 * window, even one overage is paying for. Set it to stop autonomous runs at the plan
 * boundary instead of spending overage credit.
 */
const PAUSE_ON_OVERAGE = (process.env.HO_PAUSE_ON_OVERAGE || '').trim() === '1';

/**
 * What a `rate_limit_event` REALLY means for this run.
 *
 * `status: 'rejected'` alone does not mean requests are refused. On a plan with overage
 * billing enabled the SDK reports the *included* window as rejected while the API keeps
 * serving every request out of overage — measured 2026-09-04:
 *
 *   {"status":"rejected","rateLimitType":"five_hour","resetsAt":1788530400,
 *    "overageStatus":"allowed","isUsingOverage":true,"overageInUse":true}
 *
 * and the very next assistant message in that same stream completed normally. Reading
 * `status` on its own cost the whole 2026-09-04 social fan-out: 32 rate-limit pauses
 * between 09:08 and 13:53, 0-3 turns each, and 31 of them pushed to Telegram, while
 * interactive sessions on the same account ran fine. Vadim saw nothing but limit notices.
 *
 * So a rejection counts only when nothing is carrying it: overage not allowed (disabled,
 * or its own monthly budget spent). If this call is wrong the run is not stranded — the
 * SDK's `result` still comes back limit-shaped and isLimitError() pauses it properly.
 */
export function effectiveLimitStatus(info: any): 'allowed' | 'allowed_warning' | 'rejected' {
  const status = info?.status ?? 'allowed';
  if (status !== 'rejected') return status;
  const overageCarrying = info?.overageStatus === 'allowed';
  if (overageCarrying && !PAUSE_ON_OVERAGE) return 'allowed_warning';
  return 'rejected';
}

/**
 * Seconds to wait out a REAL rejection. `retry_after` is what the ladder wants but the
 * five-hour message never carries one; `resetsAt` (epoch seconds) is the same number
 * stated as a deadline, and using it means the job wakes when the window actually opens
 * instead of climbing 60s → 30min guesses at it. Clamped: a stale/bogus deadline must not
 * park a job for a day, and a deadline already in the past must not mean "retry instantly".
 */
export function retryAfterFromLimitInfo(info: any): number | undefined {
  const direct = Number(info?.retry_after ?? info?.retryAfter);
  if (Number.isFinite(direct) && direct > 0) return Math.round(direct);
  const resetsAt = Number(info?.resetsAt ?? info?.resets_at);
  if (!Number.isFinite(resetsAt) || resetsAt <= 0) return undefined;
  const secs = resetsAt - Date.now() / 1000;
  if (secs <= 0) return undefined;                       // window already open → use the ladder
  return Math.min(Math.round(secs) + 15, 6 * 3600);      // +15s so we wake just after it opens
}

/** One-line, log-safe rendering of a rate_limit_info, for the pause record. */
export function describeLimitInfo(info: any): string {
  if (!info || typeof info !== 'object') return '';
  const bits: string[] = [];
  if (info.rateLimitType) bits.push(String(info.rateLimitType));
  if (info.status) bits.push(`status=${info.status}`);
  if (info.overageStatus) bits.push(`overage=${info.overageStatus}`);
  if (info.isUsingOverage || info.overageInUse) bits.push('overage-in-use');
  const resetsAt = Number(info.resetsAt ?? info.resets_at);
  if (Number.isFinite(resetsAt) && resetsAt > 0) {
    bits.push(`resets=${new Date(resetsAt * 1000).toISOString().replace('.000Z', 'Z')}`);
  }
  return bits.join(' ');
}

/** Return the first non-empty string value found in an object (shallow). */
function firstStringValue(obj: Record<string, unknown>): string | undefined {
  for (const v of Object.values(obj)) {
    if (typeof v === 'string' && v.length > 0) return v;
  }
  return undefined;
}

/**
 * Deterministic JSON. Key order must not change a digest, otherwise the SAME repeated tool
 * call could hash differently and hide a genuine loop.
 */
function stableStringify(v: unknown): string {
  if (v === null || typeof v !== 'object') return JSON.stringify(v) ?? 'null';
  if (Array.isArray(v)) return `[${v.map(stableStringify).join(',')}]`;
  const o = v as Record<string, unknown>;
  return `{${Object.keys(o).sort().map((k) => `${JSON.stringify(k)}:${stableStringify(o[k])}`).join(',')}}`;
}

/** Chars of the target kept in the signature for human readability (the tail, so the basename survives). */
const SIG_HINT_CHARS = 56;

/**
 * Build the turn signature: `<Tool>:<readable tail>#<digest of the whole input>`.
 *
 * THE DIGEST IS THE CORRECTNESS PART. The previous version truncated the target to its FIRST
 * 80 chars, which is not a discriminator at all for deep paths: every file inside
 *   …/marketing_vb/workspace/outbound/campaigns/<slug>/…
 * shares its first 80 chars (they end exactly at `campaigns/2026`), so six Reads of six
 * DIFFERENT files collapsed to one signature and read as a loop. That killed job 37 on
 * 2026-07-28 and accounted for 8 of the first 11 escalations ever raised.
 *
 * Hashing the full input is exact and fixed-length, and makes no assumption about which field
 * happens to be the distinguishing one. The readable tail exists only so the Telegram
 * escalation message still says something a human can act on.
 */
export function buildSignature(toolName: string, input: unknown): string {
  const i = (input ?? {}) as Record<string, unknown>;
  const target = i.file_path ?? i.path ?? i.url ?? i.command
    ?? i.query                                              // WebSearch
    ?? (Array.isArray(i.urls) ? i.urls[0] : undefined)      // WebFetch (urls array)
    ?? firstStringValue(i)
    ?? '';
  const hint = String(target).slice(-SIG_HINT_CHARS);
  const digest = createHash('sha1').update(stableStringify(input ?? null)).digest('hex').slice(0, 12);
  return `${toolName}:${hint}#${digest}`;
}

/** Map a raw SDK message to our normalized breaker Event(s) + a log record. THE ONLY SDK-coupling point.
 *
 * `gateTexts` carries the FULL text of EVERY tool_use in the message, and exists separately from
 * `signature` because the two have opposite requirements. A signature must be short and stable (it
 * is compared for loop detection and shown to a human); a gate must see everything.
 *
 * Both halves of that were wrong, and both let a destructive command through the Telegram gate:
 *   - the gate was matched against the SIGNATURE, whose readable part is only the last 56 chars of
 *     the target — so `rm -rf /srv/app/workspace/outbound/campaigns/2026/data/exports/old-batch`
 *     had its `rm -rf` truncated away and executed ungated. Verified: gated=false on a 78-char
 *     command, while the same command at 14 chars gated correctly.
 *   - only the FIRST tool_use block produced a signature, so a gated action placed in the second or
 *     later block of one assistant message was never checked at all.
 */
export function mapSdkMessage(msg: any): { events: Event[]; type: string; toolName?: string; signature?: string; gateTexts: string[] } {
  const events: Event[] = [];
  let type = msg?.type ?? 'system';
  let toolName: string | undefined;
  let signature: string | undefined;
  const gateTexts: string[] = [];

  if (type === 'assistant') {
    const blocks = msg?.message?.content ?? [];
    const tus = Array.isArray(blocks) ? blocks.filter((b: any) => b?.type === 'tool_use') : [];
    // EVERY tool_use is gate-checked, in full.
    for (const b of tus) gateTexts.push(`${b.name}:${stableStringify(b.input ?? null)}`);
    const tu = tus[0];
    if (tu) {
      // The signature still comes from the first tool_use only: it feeds loop detection, and
      // counting one turn per assistant message is what the breaker's thresholds are calibrated to.
      toolName = tu.name;
      signature = buildSignature(tu.name, tu.input);
    } else {
      signature = 'assistant:text';
    }
    events.push({ kind: 'turn', signature });
  } else if (type === 'rate_limit' || type === 'rate_limit_event' || msg?.rate_limit_info) {
    const info = msg?.rate_limit_info ?? msg ?? {};
    const status = effectiveLimitStatus(info);
    events.push({
      kind: 'rate_limit', status,
      retryAfterSecs: retryAfterFromLimitInfo(info),
      detail: describeLimitInfo(info),
    });
    type = 'rate_limit';
  } else if (type === 'result') {
    const detail = String(msg?.result ?? msg?.subtype ?? '');
    const ok = msg?.subtype === 'success' || msg?.is_error === false;
    // a limit-shaped failure becomes a pause (→ durable resume), not a hard error
    if (!ok && isLimitError(detail)) {
      events.push({ kind: 'rate_limit', status: 'rejected', retryAfterSecs: RESUME_BACKOFF_SECS });
      type = 'rate_limit';
    } else {
      events.push({ kind: 'result', ok, detail });
    }
  }
  return { events, type, toolName, signature, gateTexts };
}

/** Detect an ask-gated tool call the agent is proposing (mirror of guard.py ASK patterns).
 * Note: plain `git push` is NO LONGER gated (auto commit+push is the desired flow); only merge
 * and irreversible infra/db actions are. */
// Exported ONLY so test/askgate.test.ts can apply the real list. It used to keep a
// hand-written "mirror of the conductor's ASK_PATTERNS" instead, which is a test that
// cannot fail: the mirror and the real list drift apart silently, and on 2026-08-27 two
// newly-added patterns were proven "not gated" by a suite that was never looking at them.
export const ASK_PATTERNS = [
  /wrangler\s+(deploy|publish)/i, /terraform\s+(apply|destroy)/i,
  /supabase\s+db\s+push/i, /gh\s+pr\s+merge/i,
  // Data loss was not represented here at all: a recursive delete, a hard reset or a
  // DROP proposed mid-run went straight to Claude Code's own permission layer, which is
  // only as strict as the work_dir's settings. These four put a Telegram gate in front of
  // them for every profile and every work_dir, regardless of project settings.
  /\brm\s+-[a-z]*r[a-z]*/i,
  /\bgit\s+reset\s+--hard\b/i,
  /\bgit\s+clean\s+-[a-z]*f/i,
  /\b(DROP\s+(TABLE|DATABASE|SCHEMA)|TRUNCATE)\b/i,
  // Self-approval. guard.py blocks this too, but only when the job's work_dir
  // happens to load THIS repo's .claude/settings.json — a job pointed anywhere
  // else runs with no such hook, and `sqlite3` is a perfectly ordinary command.
  // The queue is the human gate's storage, so a run that edits it is editing the
  // decision it is waiting for. Gated here, it reaches Telegram as an escalation
  // a human can refuse, for every profile and every work_dir.
  /\b(update|replace\s+into|delete\s+from|drop\s+table)\s+(ho_escalations|ho_questions|ho_jobs|ho_runs|ho_steps)\b/i,
  /\bsqlite3\b[\s\S]{0,200}?\bho\.db\b[\s\S]{0,400}?\b(update|delete\s+from|drop|replace\s+into|attach)\b/i,
];
/** Undo JSON string escaping before pattern-matching.
 *
 * gateTexts are built as `Tool:{"command":"…"}` — i.e. the tool input passed through
 * JSON.stringify — so a real newline in the command arrives as the TWO characters
 * backslash and n. Every ASK_PATTERNS rule that joins words with \s+ is therefore blind
 * to a multi-line command, and a heredoc is the most natural way for an agent to write
 * one. Measured 2026-08-27: `sqlite3 ho.db <<'X'\nupdate\n ho_escalations …` matched
 * nothing, and neither would `DROP\nTABLE x` or an `rm -rf` broken over a continuation.
 *
 * Fixing it here rather than in each regex means every existing rule gains the coverage
 * too, and a rule added later cannot forget about it. Matching only — the ORIGINAL text
 * is what gets shown to the human, so the escalation message still quotes the command
 * exactly as the agent proposed it. */
export function unescapeForGate(t: string): string {
  return t
    // JSON-escaped newline / CR / tab -> real whitespace. MUST run first: doing the
    // bare-backslash pass first would turn `\n` into ` n` and glue a stray letter onto
    // the next word.
    .replace(/\\[nrt]/g, ' ')
    // What is left is a shell line-continuation, which JSON.stringify wrote as `\\`.
    // Semantically it joins two lines, so whitespace is the right substitution — and
    // without it `rm \<newline> -rf /path` still slips the rm rule.
    .replace(/\\+/g, ' ')
    .replace(/\\"/g, '"');
}

/** First gated pattern found in ANY of this message's tool calls, or null.
 *
 * Takes the full tool text — never the signature. See mapSdkMessage for why that distinction is
 * load-bearing. The returned string is truncated only for the human-facing message. */
function asksForGatedAction(gateTexts: string[]): string | null {
  for (const t of gateTexts) {
    const probe = unescapeForGate(t);
    for (const p of ASK_PATTERNS) {
      if (p.test(probe)) return t.length > 200 ? `${t.slice(0, 200)}…` : t;
    }
  }
  return null;
}

/** PHASE 2 — run a job that was decomposed into ho_steps: per-step verified loop with
 * progress, escalation and durable step state. The agent SDK calls live in agent-runner.ts
 * (integration seam); the loop decisions in steprunner.ts/steploop.ts are unit-tested. */
async function runJobAsSteps(store: Store, job: Job, tg: TelegramConfig | null): Promise<void> {
  const runId = await store.startRun(job.id); // anchors escalations (ho_escalations.run_id FK)
  await store.setJobStatus(job.id, 'running');
  const deps = makeSdkDeps(job.work_dir, job.profile);
  let finalStatus = 'done';
  let summary = '';

  loop: for (;;) {
    await store.heartbeat(job.id);   // keep this job "alive" between steps for parallel-worker safety
    const step: Step | null = await store.nextStep(job.id);
    if (!step) break; // no runnable step left
    await store.setJobStatus(job.id, 'verifying');
    try {
      // BEAT FOR THE WHOLE STEP, not once before it.
      //
      // One beat per step was a double-execution bug, not a rough edge. runStep builds an executor,
      // runs an SDK query (maxTurns 150) and up to three gate() calls each capped at 10 MINUTES,
      // plus reviewer and runtime passes — routinely far longer than HO_STALE_RUN_SECS (900s). The
      // job sits in 'verifying' throughout, and recoverStale covers 'verifying', so a SIBLING worker
      // saw a live job as abandoned: it flipped it to 'deferred', cleared claimed_by, reset the
      // step running→pending, and a second worker claimed and re-ran the SAME steps in the SAME
      // work_dir while the first was still executing. Two agents editing one tree, duplicated
      // commits and pushes.
      //
      // An interval belongs here rather than inside runStep: liveness is a property of the WORKER
      // holding the job, and threading a callback through the step machinery would put that
      // knowledge in the wrong place. Cleared in `finally`, so a throw cannot leak the timer or keep
      // beating for a job this worker no longer owns.
      const beat = setInterval(() => { store.heartbeat(job.id).catch(() => {}); }, HEARTBEAT_MS);
      let outcome;
      try { outcome = await runStep(step as StepRecord, deps, store); }
      finally { clearInterval(beat); }
      await store.setJobStatus(job.id, 'running');
      const act = outcome.decision.action;
      if (act === 'blocked' || act === 'needs_review') {
        const reason = (outcome.decision as { reason: string }).reason;
        const escId = await store.openEscalation(
          runId, job.id, act,
          `Step ${step.step_no} "${step.title}" → ${act} (score ${outcome.lastScore}): ${reason}. Approve / deny / abort?`,
          { step_no: step.step_no, score: outcome.lastScore, decision: act },
        );
        if (tg) await notifyEscalation(tg, { escalationId: escId, jobTitle: job.title, reason: act, question: `Step ${step.step_no}: ${reason}` });
        const decision = await store.waitEscalation(escId, {
          jobId: job.id,
          timeoutMs: ESC_WAIT_SECS * 1000,
          onReminder: (waited) => notifyEscalationWaiting(tg, job, escId, act, waited),
          remindMs: ESC_REMIND_SECS * 1000,
        });
        // Back to 'running' before continuing: openEscalation left the job flagged
        // 'escalated', bridge.py maps that to "failed", and heartbeat() skips it.
        if (decision === 'approved') {
          await store.finishStep(step.id, { status: 'done', score: outcome.lastScore });
          await store.setJobStatus(job.id, 'running');
          continue;
        }
        if (decision === 'aborted') { finalStatus = 'aborted'; summary = `aborted at step ${step.step_no}`; break loop; }
        // 'timeout' lands here too: the escalation row stays OPEN, so a late tap still
        // resolves it and the job can be re-run from where it stopped.
        finalStatus = 'escalated'; summary = `step ${step.step_no} ${act}, human ${decision}`; break loop;
      }
      // done → next step
    } catch (err) {
      await store.finishStep(step.id, { status: 'blocked', error: String(err).slice(0, 300) });
      finalStatus = 'failed'; summary = `step ${step.step_no} crashed: ${String(err).slice(0, 200)}`;
      break loop;
    }
  }

  if (finalStatus === 'done') {
    const ps = await store.projectStatus(job.id);
    if (ps && ps.total_steps > 0 && ps.done_steps < ps.total_steps) {
      finalStatus = 'failed';
      summary = `stalled: ${ps.done_steps}/${ps.total_steps} steps done (a step is blocked or has unmet deps)`;
    } else {
      summary = `all ${ps?.total_steps ?? 0} steps done`;
    }
  }

  await store.finishRun(runId, finalStatus === 'done' ? 'done' : finalStatus === 'aborted' ? 'aborted' : 'failed', 'steps', 0, finalStatus === 'done' ? undefined : summary);
  await store.finishJob(job.id, finalStatus, summary, finalStatus === 'done' ? undefined : summary);
  if (tg) await notifyDone(tg, job.title, finalStatus, summary);
}

/**
 * Push the "job paused — will resume" notice when it carries information: the job's FIRST
 * rate-limit pause, or any wait long enough that silence would read as a dead conductor.
 * Short retries stay quiet.
 *
 * This used to key off the streak (`first pause, then every Nth`), which inverted under load:
 * with the streak wrongly pinned at 0 every pause looked like a first pause, so a job retrying
 * every ~50s sent a Telegram message every ~50s. Gating on the WAIT WE ARE ABOUT TO TAKE is
 * self-limiting — the ladder caps at 30 min, so a genuine hours-long outage reports every rung
 * and a fast retry loop reports nothing.
 */
export function shouldNotifyPause(waitSecs: number, isFirstPause: boolean): boolean {
  return isFirstPause || waitSecs >= PAUSE_NOTIFY_MIN_SECS;
}

async function notifyPauseProgress(
  tg: TelegramConfig | null, job: Job, streak: number, waitSecs: number, isFirstPause: boolean,
): Promise<void> {
  if (!tg) return;
  if (!shouldNotifyPause(waitSecs, isFirstPause)) return; // short retry → stay quiet
  const mins = Math.max(1, Math.round(waitSecs / 60));
  await notifyDone(tg, job.title, 'paused', streak === 0
    ? `rate/token limit — will resume in ~${mins} min`
    : `still rate-limited (${streak} tries, no progress) — next try in ~${mins} min`);
}

/** Nudge Telegram about an escalation nobody has answered yet. The buttons on the ORIGINAL
 * message still work — the row stays 'open' — so this is a reminder, not a new question. */
async function notifyEscalationWaiting(
  tg: TelegramConfig | null, job: Job, escId: number, reason: string, waitedMs: number,
): Promise<void> {
  if (!tg) return;
  const mins = Math.max(1, Math.round(waitedMs / 60000));
  await notifyDone(tg, job.title, 'paused',
    `still waiting on escalation #${escId} (${reason}) — ${mins} min, buttons above still work`);
}

/** Pre-run recovery point. autocommit.py deliberately skips main/master and these repos work on
 * main, so an autonomous run had nothing to roll back to. The pattern guards stop an `rm -rf`,
 * but a delete inside an allowed python3 script is invisible to them — only a snapshot taken
 * before the agent starts covers that. Never fatal: a job must still run if the snapshot fails.
 *
 * THE ATTEMPT NUMBER IS PART OF THE REF, and that is the whole point. The ref used to be
 * refs/hermes/snapshots/job-<id> alone, so every resume OVERWROTE it with the tree as it
 * stood AFTER the previous attempt's work. For a job that defers on a rate limit and
 * resumes — the normal case on a free-tier chain, and precisely the long job you would
 * want to roll back — the pre-job tree was gone, replaced by a "rollback point" that
 * already contains the changes you are trying to undo. It reported success each time.
 *
 * One ref per attempt keeps the original as -a1 and makes each attempt's work readable:
 *   git diff refs/hermes/snapshots/job-42-a1 refs/hermes/snapshots/job-42-a2
 */
async function snapshotWorkTree(job: Job): Promise<void> {
  const script = process.env.HO_SNAPSHOT_SH
    ?? (process.env.HERMES_REPO_ROOT ? `${process.env.HERMES_REPO_ROOT}/hermes_agent/ops/conductor-snapshot.sh` : '');
  if (!script) { console.warn(`[snapshot] job ${job.id}: no HERMES_REPO_ROOT / HO_SNAPSHOT_SH — skipped`); return; }
  try {
    const { stdout } = await promisify(execFile)(
      script, [job.work_dir, String(job.id), String(job.attempts ?? 1)], { timeout: 120_000 });
    const line = stdout.trim();
    if (line) console.log(line);
  } catch (e) {
    console.warn(`[snapshot] job ${job.id}: ${String(e).slice(0, 200)}`);
  }
}

export async function runOneJob(store: Store): Promise<boolean> {
  const claimed = await store.claimJob(WORKER_ID, MAX_ATTEMPTS);
  if (!claimed) return false; // nothing to do

  // A profile bound to a directory (`runFrom`) overrides the enqueued work_dir —
  // see resolveWorkDir. Done once, here, so the snapshot, the step deps and the
  // SDK cwd below can never disagree about where this job runs.
  const job: Job = { ...claimed, work_dir: resolveWorkDir(claimed.profile, claimed.work_dir) };

  await snapshotWorkTree(job);

  // PHASE 2: if the job was decomposed into steps, run the per-step verified loop —
  // but ONLY for profiles whose work that loop can actually verify.
  //
  // The step loop is a SOFTWARE pipeline: runExecutor tells the agent to "implement
  // step N from .claude/scratchpad/*/plan.md" (the job's own prompt is never passed),
  // and runGates re-runs `npx ultracite lint`, `npm run typecheck`, `npm test`. In a
  // content repo none of that exists, so every attempt scores 0 and every step ends
  // 'blocked' → a Telegram escalation whose Approve means "skip the step".
  //
  // That is not theory: job 88 (2026-08-17, profile marketing_vb_sm) had two step rows
  // inserted by hand alongside it, ran the dev loop 3× per step against a tree with no
  // package.json, escalated twice, was approved twice, and closed as `done — all 2 steps
  // done` having written zero posts. A content pipeline already carries its own gate
  // (quality-controller / post-brand-checker, then Vadim approving the digest), so for
  // these profiles the steps are IGNORED and the job runs as one prompt — the prompt is
  // the thing that carries the actual brief.
  const stepProfiles = (process.env.HO_STEP_PROFILES ?? 'dev,security')
    .split(',').map((s) => s.trim()).filter(Boolean);
  if (await store.hasSteps(job.id)) {
    if (stepProfiles.includes(job.profile)) {
      await runJobAsSteps(store, job, withJobThread(tgConfigFromEnv(), job.id));
      return true;
    }
    console.warn(`[${WORKER_ID}] job ${job.id} has ho_steps but profile='${job.profile}' is not `
      + `step-verifiable (HO_STEP_PROFILES=${stepProfiles.join(',')}) — running the job prompt `
      + 'as ONE run; steps left untouched');
  }

  // Bound to the job's ORIGIN topic once, so every push below (escalation, pause,
  // done) answers where the work was asked for instead of the DM's General lane.
  const tg = withJobThread(tgConfigFromEnv(), job.id);
  const lim = limitsForJob(job);
  const attempt = (job.attempts ?? 0) + 1;
  const runId = await store.startRun(job.id, attempt);
  const resuming = !!job.resume_session_id;
  if (resuming) console.log(`[${WORKER_ID}] resuming job ${job.id} from session ${job.resume_session_id}`);
  const plugins = resolveProfilePlugins(job.profile);
  console.log(`[${WORKER_ID}] job ${job.id} profile='${job.profile}' → ${plugins.length} plugin(s)`);

  const state: BreakerState = initState();
  let stopReason = 'completed';
  let finalStatus = 'done';
  let summary = '';
  /** Set ONLY by an SDK `result` event saying the agent finished. Guards against reporting
   * success because the stream merely ended or a human waved an escalation through. */
  let sawCompletion = false;
  let continues = 0;
  let loggedLimitWarning = false;

  /** Ask the human, reminding them while they are away. Returns the decision or 'timeout'. */
  const askHuman = async (reason: string, detail: string, context: unknown): Promise<{ id: number; decision: string }> => {
    const escId = await store.openEscalation(runId, job.id, reason, detail, context);
    if (tg) await notifyEscalation(tg, { escalationId: escId, jobTitle: job.title, reason, question: detail, context });
    const decision = await store.waitEscalation(escId, {
      jobId: job.id,                                   // keep beating: a human thinking is not a dead worker
      timeoutMs: ESC_WAIT_SECS * 1000,
      onReminder: (waited) => notifyEscalationWaiting(tg, job, escId, reason, waited),
      remindMs: ESC_REMIND_SECS * 1000,
    });
    return { id: escId, decision };
  };

  /**
   * Nobody answered. Park the job (durable resume, escalation row left OPEN so a late tap still
   * lands) rather than killing it. Returns false once we have parked too many times, so the
   * caller settles the job as 'escalated' instead of nagging forever.
   */
  const parkAwaitingHuman = async (escId: number, reason: string): Promise<boolean> => {
    const parks = await store.awaitHumanStreak(job.id, runId);
    if (parks >= MAX_ESC_PARKS) return false;
    const detail = `awaiting human on escalation #${escId} (${reason}) — park ${parks + 1}/${MAX_ESC_PARKS}`;
    console.warn(`[${WORKER_ID}] job ${job.id} ${detail}`);
    await store.deferJob(job.id, ESC_PARK_SECS);
    await store.finishRun(runId, 'paused', 'await_human', state.turns, detail);
    if (tg) await notifyDone(tg, job.title, 'paused',
      `${detail} — will ask again in ~${Math.round(ESC_PARK_SECS / 60)} min`);
    return true;
  };

  /** Wait out a rate limit on the ladder, record it, and resume later. */
  const pauseOnLimit = async (serverRetrySecs: number | undefined, detailPrefix: string): Promise<void> => {
    // A run that made REAL progress (>= MIN_PROGRESS_TURNS) proves the window is open, so its
    // streak restarts at 0. A run that only managed a turn or two hit the same wall and must keep
    // climbing. Otherwise take the WORSE of this job's streak and the account-wide one: the usage
    // window is shared, so a freshly claimed job must not restart the ladder at 60s after another
    // job just proved the window is shut.
    const madeProgress = state.turns >= MIN_PROGRESS_TURNS;
    const streak = madeProgress ? 0 : Math.max(
      await store.noProgressPauseStreak(job.id, runId, MIN_PROGRESS_TURNS),
      await store.globalNoProgressPauseStreak(runId, MIN_PROGRESS_TURNS),
    );
    const isFirstPause = (await store.ratelimitPauseCount(job.id, runId)) === 0;
    const wait = backoffForStreak(streak, serverRetrySecs);
    const detail = `${detailPrefix}streak ${streak}, turns this run ${state.turns}, retry in ${wait}s`;
    console.warn(`[${WORKER_ID}] job ${job.id} paused: ${detail}`);
    await store.deferJob(job.id, wait);
    await store.finishRun(runId, 'paused', 'ratelimit', state.turns, detail);
    await notifyPauseProgress(tg, job, streak, wait, isFirstPause);
  };

  try {
    const stream = query({
      prompt: job.prompt,
      options: {
        settingSources: ['project'],        // inherit our .claude/ marketplace, CLAUDE.md, settings.json, hooks
        plugins,                            // profile-selected system (dev|seo|marketing|security), loaded by absolute path
        permissionMode: job.permission_mode as any, // 'acceptEdits' recommended for autonomy
        // Pre-approve read-only web tools: acceptEdits auto-denies them in headless
        // ("you haven't granted it yet"), which blocks the outbound/SEO research flows.
        // allowedTools is ADDITIVE (auto-allow only these) — it does NOT restrict other
        // tools and does NOT bypass the ask-gate below. Applies to subagents too.
        allowedTools: ['WebSearch', 'WebFetch'],
        systemPrompt: HERMES_SYSTEM_PROMPT,
        cwd: job.work_dir,
        ...(job.resume_session_id ? { resume: job.resume_session_id } : {}),
        // do NOT set bypassPermissions: it would disable the work_dir's deny rules and
        // its PreToolUse guard for this run and every subagent it spawns
      } as any,
    });

    let _hbAt = Date.now();
    for await (const msg of stream) {
      // heartbeat while streaming so a sibling worker's recoverStale won't requeue this live job
      if (Date.now() - _hbAt > HEARTBEAT_MS) { await store.heartbeat(job.id); _hbAt = Date.now(); }
      const { events, signature, gateTexts } = mapSdkMessage(msg);
      // capture the session id the moment the SDK emits it → enables resume on crash/limit
      const sid = (msg as any)?.session_id;
      if (sid) await store.setSession(runId, job.id, sid);

      // intercept ask-gated actions BEFORE they execute
      const gated = asksForGatedAction(gateTexts);
      if (gated) {
        const { id: escId, decision } = await askHuman(
          'ask_gate', `Agent wants to run a gated action: ${gated}. Approve?`, { command: gated });
        if (decision === 'timeout') {
          if (await parkAwaitingHuman(escId, 'ask_gate')) return true;
          stopReason = 'ask_gate'; finalStatus = 'escalated';
          summary = `gated action (${gated}) unanswered after ${MAX_ESC_PARKS} reminders`;
          break;
        }
        if (decision !== 'approved') {
          stopReason = 'ask_gate'; finalStatus = decision === 'aborted' ? 'aborted' : 'escalated';
          summary = `stopped at gated action (${gated}): human ${decision}`;
          break;
        }
        // approved → let the loop continue (the gate is enforced by Claude Code itself on resume).
        // Put the status back: openEscalation set 'escalated' and nothing cleared it, so a
        // run could continue for hours flagged as escalated — bridge.py maps that to
        // "failed", so MV-Link/Hermes showed a live job as a failure, and heartbeat()
        // skipped it for the rest of the run.
        await store.setJobStatus(job.id, 'running');
      }

      for (const ev of events) {
        const d = evaluate(state, ev, lim);
        // A limit we deliberately ran THROUGH must leave a trace: this run is billing to
        // overage, not to the plan, and "the pipeline kept going" should be explainable
        // from the log alone. Once per run — the SDK repeats the event on every request.
        if (ev.kind === 'rate_limit' && ev.status === 'allowed_warning' && !loggedLimitWarning) {
          loggedLimitWarning = true;
          console.warn(`[${WORKER_ID}] job ${job.id} continuing through a limit warning: ${ev.detail || '(no detail)'}`);
        }
        if (d.action === 'continue') continue;
        if (d.action === 'pause') {
          // Token/rate limit → defer WITH session id; a later claim resumes it.
          // We take the wait from the ladder rather than d.backoffSecs: when the server
          // supplies retry_after the two agree, but when it does not the breaker falls
          // back to a flat 60s, which is what produced the hammering loop.
          const why = ev.kind === 'rate_limit' && ev.detail ? `rate limit [${ev.detail}] — ` : 'rate limit — ';
          await pauseOnLimit(ev.kind === 'rate_limit' ? ev.retryAfterSecs : undefined, why);
          return true;
        }
        if (d.action === 'escalate') {
          const { id: escId, decision } = await askHuman(d.reason, d.detail, { turns: state.turns });

          if (decision === 'timeout') {
            if (await parkAwaitingHuman(escId, d.reason)) return true;
            stopReason = d.reason; finalStatus = 'escalated';
            summary = `${d.reason}: ${d.detail} — unanswered after ${MAX_ESC_PARKS} reminders`;
            throw new BreakStop();
          }

          // "Approve" on a BREAKER escalation means CONTINUE — "no, it is not really stuck, keep
          // going" — NOT "the job is finished". It used to mean the latter: job 37 (2026-07-28)
          // was closed as `done` with a zero-work result_summary five seconds after the tap.
          // There is no "mark done" decision on purpose: only the agent's own result event may
          // declare success (see the sawCompletion guard below).
          if (decision === 'approved') {
            if (++continues > MAX_CONTINUES) {
              stopReason = d.reason; finalStatus = 'escalated';
              summary = `${d.reason}: ${d.detail} — continued ${MAX_CONTINUES}x already, stopping`;
              throw new BreakStop();
            }
            // Clear the loop window, or the very same tail re-trips on the next turn.
            state.recentSignatures.length = 0;
            if (d.reason === 'turns') lim.maxTurns = state.turns + TURN_GRANT;
            await store.setJobStatus(job.id, 'running');
            console.log(`[${WORKER_ID}] job ${job.id} continued by human after ${d.reason} `
              + `(${continues}/${MAX_CONTINUES}, turns ${state.turns}, cap ${lim.maxTurns})`);
            continue;
          }

          finalStatus = decision === 'aborted' ? 'aborted' : 'escalated';
          stopReason = d.reason;
          summary = `${d.reason}: ${d.detail} — human ${decision}`;
          throw new BreakStop();
        }
        if (d.action === 'stop') {
          stopReason = d.reason;
          if (d.reason === 'completed') { finalStatus = 'done'; sawCompletion = true; }
          else finalStatus = 'failed';
          summary = d.detail || stopReason;
          throw new BreakStop();
        }
      }
    }
  } catch (err) {
    if (!(err instanceof BreakStop)) {
      const detail = String(err).slice(0, 500);
      if (isLimitError(detail)) {
        // Thrown limit error → pause + resume rather than fail. Same ladder as the
        // structured path: isLimitError also matches transient "overloaded", which clears
        // in seconds, so a flat RESUME_BACKOFF_SECS (1h) idled the job far longer than needed.
        await pauseOnLimit(undefined, `${detail} — `);
        return true;
      }
      finalStatus = 'failed'; stopReason = 'error'; summary = detail;
    }
  }

  /**
   * NEVER report success the agent did not claim. `finalStatus` starts at 'done', so any path
   * that leaves it untouched — a stream that just ends, an escalation waved through — used to
   * write a false success into result_summary and clear the resume session, making the job
   * indistinguishable from real work (job 37, 2026-07-28). Only an SDK `result` event counts.
   */
  if (finalStatus === 'done' && !sawCompletion) {
    finalStatus = 'escalated';
    if (stopReason === 'completed') stopReason = 'no_result';
    summary = summary
      ? `${summary} — NOT marked done: no SDK result event`
      : 'stream ended without an SDK result event — nothing proves the work finished';
    console.warn(`[${WORKER_ID}] job ${job.id} withheld 'done': ${summary}`);
  }

  const runStatus = finalStatus === 'done' ? 'done'
    : finalStatus === 'aborted' ? 'aborted'
    : finalStatus === 'escalated' ? 'escalated' : 'failed';
  const errText = finalStatus === 'done' || finalStatus === 'aborted' ? undefined : summary;
  await store.finishRun(runId, runStatus, stopReason, state.turns, errText);
  await store.finishJob(job.id, finalStatus, summary, errText);
  if (tg) await notifyDone(tg, job.title, finalStatus, summary || stopReason);
  return true;
}

class BreakStop extends Error {}

/** Long-running worker loop: recover stale runs, poll for jobs, sleep when idle. */
export async function workerLoop(idx = 0) {
  const store = new Store();
  const idleMs = posEnv('HO_IDLE_MS', 10000);
  const tag = `${WORKER_ID}#${idx}`;
  console.log(`[${tag}] conductor up. polling…`);
  for (;;) {
    let worked = false;
    try {
      // Only one worker runs the global stale-recovery sweep — avoids N writers colliding.
      if (idx === 0) {
        const recovered = await store.recoverStale(STALE_RUN_SECS);
        if (recovered) console.log(`[${tag}] recovered ${recovered} stale job(s) for resume`);
      }
      worked = await runOneJob(store);
    } catch (e) { console.error('worker error:', e); }
    if (!worked) await new Promise((r) => setTimeout(r, idleMs));
  }
}

if (process.argv[1] && process.argv[1].endsWith('conductor.ts')) {
  // One webhook server for the process, not one per worker — see bot-callback.ts for why the
  // port is per-user rather than a shared default.
  startWebhookServer();
  // getUpdates polling collides with the Hermes gateway, which owns the bot's single allowed
  // getUpdates consumer. Escalation callbacks normally arrive via the gateway, which forwards
  // ho:* callback_query updates to our webhook. Opt-in only (HO_TELEGRAM_POLLING=1) for
  // standalone runs where the conductor owns the bot outright.
  if (process.env.HO_TELEGRAM_POLLING === '1') startTelegramPolling();
  // Run CONDUCTOR_WORKERS loops concurrently — each claims jobs atomically, so N
  // different projects (topics/systems) run in parallel instead of one at a time.
  console.log(`conductor: starting ${CONDUCTOR_WORKERS} worker(s)`);
  Promise.all(Array.from({ length: CONDUCTOR_WORKERS }, (_, i) => workerLoop(i)))
    .catch((e) => { console.error(e); process.exit(1); });
}
