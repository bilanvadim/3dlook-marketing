/**
 * Fullstack agents Orchestrator — main control loop.
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
import { query } from '@anthropic-ai/claude-agent-sdk';
import { Store, Job, Step } from './store';
import { evaluate, initState, BreakerState, BreakerLimits, DEFAULT_LIMITS, Event } from './breaker';
import { runStep, StepRecord } from './steprunner';
import { makeSdkDeps } from './agent-runner';
import { resolveProfilePlugins } from './profiles';
import { tgConfigFromEnv, notifyEscalation, notifyDone, TelegramConfig } from '../escalation/telegram';

const WORKER_ID = process.env.HO_WORKER_ID ?? `ho-${process.pid}`;
const RESUME_BACKOFF_SECS = Number(process.env.HO_RESUME_BACKOFF_SECS ?? 3600); // wait when limit gives no retry-after
const STALE_RUN_SECS = Number(process.env.HO_STALE_RUN_SECS ?? 900);            // requeue runs stuck this long
const HERMES_SYSTEM_PROMPT =
  'You are the Fullstack-agents orchestrator described in this project\'s CLAUDE.md. Plan, delegate to ' +
  'the specialized subagents, coordinate via the scratchpad protocol, and run the quality gate ' +
  '(qa-engineer then security-auditor) before declaring done. Never run production-affecting ' +
  'commands without an explicit ask — they are gated.';

function limitsForJob(j: Job): BreakerLimits {
  return {
    maxTurns: j.max_turns ?? DEFAULT_LIMITS.maxTurns,
    maxWallSecs: j.max_wall_secs ?? DEFAULT_LIMITS.maxWallSecs,
    stuckRepeats: DEFAULT_LIMITS.stuckRepeats,
  };
}

/** Heuristic: does this error look like a token/quota/rate limit we should pause-and-resume on? */
function isLimitError(detail: string): boolean {
  return /rate.?limit|quota|usage limit|too many requests|overloaded|429|insufficient|credit/i.test(detail);
}

/** Map a raw SDK message to our normalized breaker Event(s) + a log record. THE ONLY SDK-coupling point. */
function mapSdkMessage(msg: any): { events: Event[]; type: string; toolName?: string; signature?: string } {
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
      const target = tu.input?.file_path ?? tu.input?.path ?? tu.input?.command ?? '';
      signature = `${tu.name}:${String(target).slice(0, 80)}`;
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

  try {
    const stream = query({
      prompt: job.prompt,
      options: {
        settingSources: ['project'],        // inherit our .claude/ marketplace, CLAUDE.md, settings.json, hooks
        plugins,                            // profile-selected system (dev|seo|marketing|security), loaded by absolute path
        permissionMode: job.permission_mode as any, // 'acceptEdits' recommended for autonomy
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
        const escId = await store.openEscalation(runId, job.id, 'ask_gate',
          `Agent wants to run a gated action: ${gated}. Approve?`, { command: gated });
        if (tg) await notifyEscalation(tg, { escalationId: escId, jobTitle: job.title, reason: 'ask_gate', question: gated, context: { command: gated } });
        const decision = await store.waitEscalation(escId);
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
          // token/rate limit → defer WITH session id; a later claim resumes it
          await store.deferJob(job.id, d.backoffSecs);
          await store.finishRun(runId, 'paused', 'ratelimit', state.turns);
          if (tg) await notifyDone(tg, job.title, 'paused',
            `rate/token limit — will resume in ~${Math.round(d.backoffSecs / 60)} min`);
          return true;
        }
        if (d.action === 'escalate') {
          const escId = await store.openEscalation(runId, job.id, d.reason, d.detail, { turns: state.turns });
          if (tg) await notifyEscalation(tg, { escalationId: escId, jobTitle: job.title, reason: d.reason, question: d.detail });
          const decision = await store.waitEscalation(escId);
          finalStatus = decision === 'approved' ? 'done' : decision === 'aborted' ? 'aborted' : 'escalated';
          stopReason = d.reason;
          summary = `${d.reason}: ${d.detail} — human ${decision}`;
          throw new BreakStop();
        }
        if (d.action === 'stop') {
          stopReason = d.reason;
          finalStatus = d.reason === 'completed' ? 'done' : 'failed';
          summary = d.detail || stopReason;
          throw new BreakStop();
        }
      }
    }
  } catch (err) {
    if (!(err instanceof BreakStop)) {
      const detail = String(err).slice(0, 500);
      if (isLimitError(detail)) {
        // thrown limit error → pause + resume rather than fail
        await store.deferJob(job.id, RESUME_BACKOFF_SECS);
        await store.finishRun(runId, 'paused', 'ratelimit', state.turns, detail);
        if (tg) await notifyDone(tg, job.title, 'paused',
          `limit hit — will resume in ~${Math.round(RESUME_BACKOFF_SECS / 60)} min`);
        return true;
      }
      finalStatus = 'failed'; stopReason = 'error'; summary = detail;
    }
  }

  await store.finishRun(runId,
    finalStatus === 'done' ? 'done' : finalStatus === 'aborted' ? 'aborted' : 'failed',
    stopReason, state.turns, finalStatus === 'failed' ? summary : undefined);
  await store.finishJob(job.id, finalStatus, summary, finalStatus === 'failed' ? summary : undefined);
  if (tg) await notifyDone(tg, job.title, finalStatus, summary || stopReason);
  return true;
}

class BreakStop extends Error {}

/** Long-running worker loop: recover stale runs, poll for jobs, sleep when idle. */
export async function workerLoop() {
  const store = new Store();
  const idleMs = Number(process.env.HO_IDLE_MS ?? 10000);
  console.log(`[${WORKER_ID}] orchestrator up. polling…`);
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

if (process.argv[1] && process.argv[1].endsWith('orchestrator.ts')) {
  workerLoop().catch((e) => { console.error(e); process.exit(1); });
}
