/**
 * Fullstack agents Conductor — main control loop.
 *
 * Wires the Agent SDK to the circuit breaker, Supabase state, and Telegram escalation.
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
import { query } from '@anthropic-ai/claude-agent-sdk';
import { Store, Job, Step } from './store';
import { evaluate, initState, BreakerState, BreakerLimits, DEFAULT_LIMITS, KIND_MIN_TURNS, Event } from './breaker';
import { runStep, StepRecord } from './steprunner';
import { makeSdkDeps } from './agent-runner';
import { resolveProfilePlugins } from './profiles';
import { tgConfigFromEnv, notifyEscalation, notifyDone, TelegramConfig } from '../escalation/telegram';
import { startWebhookServer, startTelegramPolling } from '../escalation/bot-callback';

const WORKER_ID = process.env.HO_WORKER_ID ?? `ho-${process.pid}`;
const RESUME_BACKOFF_SECS = Number(process.env.HO_RESUME_BACKOFF_SECS ?? 3600); // result-shaped / thrown limit errors
const STALE_RUN_SECS = Number(process.env.HO_STALE_RUN_SECS ?? 900);            // requeue runs stuck this long
/**
 * Turns a run must make before we treat it as REAL progress against a usage window.
 *
 * WHY NOT 1: on an exhausted window the agent still pushes 2–5 turns through before the limit
 * bites. Treating "any turn at all" as progress reset the streak to 0 on every pause, which held
 * the backoff at its first rung (~50s) and re-armed the "first pause" Telegram notice each time —
 * job 41 on 2026-07-28 produced 6 pauses in 7 minutes, all streak 0, one message each. A couple of
 * turns is not the window opening, it is the run-up to the same wall.
 */
const MIN_PROGRESS_TURNS = Number(process.env.HO_MIN_PROGRESS_TURNS ?? 10);
/**
 * Only announce a rate-limit pause when the wait is long enough to be worth a human's attention
 * (or when it is this job's first). Throttling on the STREAK could never work: the streak is
 * exactly the thing that breaks when the signal is wrong.
 */
const PAUSE_NOTIFY_MIN_SECS = Number(process.env.HO_PAUSE_NOTIFY_MIN_SECS ?? 600);
/** Extra turns granted when the human waves a `turns` escalation through. */
const TURN_GRANT = Number(process.env.HO_TURN_GRANT ?? 60);
/** How many times ONE run may be resumed by a human "continue" before we stop asking. */
const MAX_CONTINUES = Number(process.env.HO_MAX_CONTINUES ?? 5);
/** How long to wait for a human decision before parking the job (escalation stays open). */
const ESC_WAIT_SECS = Number(process.env.HO_ESC_WAIT_SECS ?? 1800);
/** Re-ping Telegram this often while an escalation sits unanswered. */
const ESC_REMIND_SECS = Number(process.env.HO_ESC_REMIND_SECS ?? 600);
/** How long a job sleeps after an unanswered escalation before it asks again. */
const ESC_PARK_SECS = Number(process.env.HO_ESC_PARK_SECS ?? 1800);
/** Give up (leave the job 'escalated') after this many unanswered park cycles. */
const MAX_ESC_PARKS = Number(process.env.HO_MAX_ESC_PARKS ?? 8);

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
const PAUSE_LADDER = [60, 300, 900, Number(process.env.HO_PAUSE_MAX_BACKOFF_SECS ?? 1800)];

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
    stuckRepeats: Number(process.env.HO_STUCK_REPEATS ?? DEFAULT_LIMITS.stuckRepeats),
    stuckRepeatsReadOnly: Number(process.env.HO_STUCK_REPEATS_READONLY ?? DEFAULT_LIMITS.stuckRepeatsReadOnly),
  };
}

/** Heuristic: does this error look like a token/quota/rate limit we should pause-and-resume on? */
function isLimitError(detail: string): boolean {
  return /rate.?limit|quota|usage limit|too many requests|overloaded|429|insufficient|credit/i.test(detail);
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
 *   /home/vadim_prod/3dlook-marketing/marketing_vb/workspace/outbound/campaigns/<slug>/…
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

/** Map a raw SDK message to our normalized breaker Event(s) + a log record. THE ONLY SDK-coupling point. */
export function mapSdkMessage(msg: any): { events: Event[]; type: string; toolName?: string; signature?: string } {
  const events: Event[] = [];
  let type = msg?.type ?? 'system';
  let toolName: string | undefined;
  let signature: string | undefined;

  if (type === 'assistant') {
    // a turn happened; build a signature from the first tool_use if present
    const blocks = msg?.message?.content ?? [];
    const tu = Array.isArray(blocks) ? blocks.find((b: any) => b.type === 'tool_use') : null;
    if (tu) {
      toolName = tu.name;
      signature = buildSignature(tu.name, tu.input);
    } else {
      signature = 'assistant:text';
    }
    events.push({ kind: 'turn', signature });
  } else if (type === 'rate_limit' || msg?.rate_limit_info) {
    const status = msg?.rate_limit_info?.status ?? msg?.status ?? 'allowed';
    events.push({ kind: 'rate_limit', status, retryAfterSecs: msg?.rate_limit_info?.retry_after });
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
  return { events, type, toolName, signature };
}

/** Detect an ask-gated tool call the agent is proposing (mirror of guard.py ASK patterns).
 * Note: plain `git push` is NO LONGER gated (auto commit+push is the desired flow); only merge
 * and irreversible infra/db actions are. */
const ASK_PATTERNS = [
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
];
function asksForGatedAction(signature?: string): string | null {
  if (!signature) return null;
  for (const p of ASK_PATTERNS) if (p.test(signature)) return signature;
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
    const step: Step | null = await store.nextStep(job.id);
    if (!step) break; // no runnable step left
    await store.setJobStatus(job.id, 'verifying');
    try {
      const outcome = await runStep(step as StepRecord, deps, store);
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
        const decision = await store.waitEscalation(escId);
        if (decision === 'approved') { await store.finishStep(step.id, { status: 'done', score: outcome.lastScore }); continue; }
        if (decision === 'aborted') { finalStatus = 'aborted'; summary = `aborted at step ${step.step_no}`; break loop; }
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
  tg: ReturnType<typeof tgConfigFromEnv>, job: Job, streak: number, waitSecs: number, isFirstPause: boolean,
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

export async function runOneJob(store: Store): Promise<boolean> {
  const job = await store.claimJob(WORKER_ID);
  if (!job) return false; // nothing to do

  // PHASE 2: if the job was decomposed into steps, run the per-step verified loop.
  if (await store.hasSteps(job.id)) {
    await runJobAsSteps(store, job, tgConfigFromEnv());
    return true;
  }

  const tg = tgConfigFromEnv();
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

  /** Ask the human, reminding them while they are away. Returns the decision or 'timeout'. */
  const askHuman = async (reason: string, detail: string, context: unknown): Promise<{ id: number; decision: string }> => {
    const escId = await store.openEscalation(runId, job.id, reason, detail, context);
    if (tg) await notifyEscalation(tg, { escalationId: escId, jobTitle: job.title, reason, question: detail, context });
    const decision = await store.waitEscalation(
      escId, ESC_WAIT_SECS * 1000, 5000,
      (waited) => notifyEscalationWaiting(tg, job, escId, reason, waited),
      ESC_REMIND_SECS * 1000,
    );
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
        // do NOT set bypassPermissions: it would disable our guard for all subagents
      } as any,
    });

    for await (const msg of stream) {
      const { events, signature } = mapSdkMessage(msg);
      // capture the session id the moment the SDK emits it → enables resume on crash/limit
      const sid = (msg as any)?.session_id;
      if (sid) await store.setSession(runId, job.id, sid);

      // intercept ask-gated actions BEFORE they execute
      const gated = asksForGatedAction(signature);
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
        // approved → let the loop continue (the gate is enforced by Claude Code itself on resume)
      }

      for (const ev of events) {
        const d = evaluate(state, ev, lim);
        if (d.action === 'continue') continue;
        if (d.action === 'pause') {
          // Token/rate limit → defer WITH session id; a later claim resumes it.
          // We take the wait from the ladder rather than d.backoffSecs: when the server
          // supplies retry_after the two agree, but when it does not the breaker falls
          // back to a flat 60s, which is what produced the hammering loop.
          // A run that made REAL progress (>= MIN_PROGRESS_TURNS) proves the window is open, so
          // its streak restarts at 0. A run that only managed a turn or two hit the same wall and
          // must keep climbing. Otherwise take the WORSE of this job's streak and the account-wide
          // one: the usage window is shared, so a freshly claimed job must not restart the ladder
          // at 60s after another job just proved the window is shut.
          const madeProgress = state.turns >= MIN_PROGRESS_TURNS;
          const streak = madeProgress ? 0 : Math.max(
            await store.noProgressPauseStreak(job.id, runId, MIN_PROGRESS_TURNS),
            await store.globalNoProgressPauseStreak(runId, MIN_PROGRESS_TURNS),
          );
          const isFirstPause = (await store.ratelimitPauseCount(job.id, runId)) === 0;
          const serverRetry = ev.kind === 'rate_limit' ? ev.retryAfterSecs : undefined;
          const wait = backoffForStreak(streak, serverRetry);
          const detail = `rate limit — streak ${streak}, turns this run ${state.turns}, retry in ${wait}s`;
          console.warn(`[${WORKER_ID}] job ${job.id} paused: ${detail}`);
          await store.deferJob(job.id, wait);
          await store.finishRun(runId, 'paused', 'ratelimit', state.turns, detail);
          await notifyPauseProgress(tg, job, streak, wait, isFirstPause);
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
        const streak = state.turns >= MIN_PROGRESS_TURNS ? 0 : Math.max(
          await store.noProgressPauseStreak(job.id, runId, MIN_PROGRESS_TURNS),
          await store.globalNoProgressPauseStreak(runId, MIN_PROGRESS_TURNS),
        );
        const isFirstPause = (await store.ratelimitPauseCount(job.id, runId)) === 0;
        const wait = backoffForStreak(streak);
        console.warn(`[${WORKER_ID}] job ${job.id} paused on thrown limit: streak ${streak}, retry in ${wait}s — ${detail}`);
        await store.deferJob(job.id, wait);
        await store.finishRun(runId, 'paused', 'ratelimit', state.turns, `${detail} (streak ${streak}, retry in ${wait}s)`);
        await notifyPauseProgress(tg, job, streak, wait, isFirstPause);
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
export async function workerLoop() {
  const store = new Store();
  const idleMs = Number(process.env.HO_IDLE_MS ?? 10000);
  console.log(`[${WORKER_ID}] conductor up. polling…`);
  for (;;) {
    let worked = false;
    try {
      const recovered = await store.recoverStale(STALE_RUN_SECS);
      if (recovered) console.log(`[${WORKER_ID}] recovered ${recovered} stale job(s) for resume`);
      worked = await runOneJob(store);
    } catch (e) { console.error('worker error:', e); }
    if (!worked) await new Promise((r) => setTimeout(r, idleMs));
  }
}

if (process.argv[1] && process.argv[1].endsWith('conductor.ts')) {
  startWebhookServer();
  // getUpdates polling collides with the gateway, which owns @dlookmarketing_bot's
  // single allowed getUpdates consumer. Escalation callbacks arrive via the gateway,
  // which forwards ho:* callback_query updates to our :3001 webhook. Opt-in only
  // (set HO_TELEGRAM_POLLING=1) for standalone runs where the conductor owns the bot.
  if (process.env.HO_TELEGRAM_POLLING === '1') startTelegramPolling();
  workerLoop().catch((e) => { console.error(e); process.exit(1); });
}
