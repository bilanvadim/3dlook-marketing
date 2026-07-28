/**
 * Fullstack agents Conductor — circuit breaker.
 * Pure decision logic, no SDK/network deps, so it is unit-testable in isolation.
 * The core loop feeds it every event; it returns whether to continue, pause, or stop.
 *
 * SCOPE (deliberately narrow): we do NOT cap spend — cost is not optimized here.
 * The only thing the agent can't reason its way out of is SPINNING IN A LOOP, so
 * that is the primary control. Turn/wall-clock caps are generous runaway backstops,
 * not budget controls. Rate-limit pause feeds durable resume; ask-gate feeds Telegram.
 */

export interface BreakerLimits {
  maxTurns: number;              // generous runaway backstop (NOT a budget)
  maxWallSecs: number;           // generous per-run wall-clock backstop
  stuckRepeats: number;          // identical-signature turns before declaring a loop (mutating tools)
  stuckRepeatsReadOnly: number;  // ditto for read-only research tools — see READ_ONLY_TOOLS
}

export const DEFAULT_LIMITS: BreakerLimits = {
  maxTurns: 300,
  maxWallSecs: 4 * 60 * 60,  // 4h per contiguous run; longer waits handled by resume
  stuckRepeats: 6,
  stuckRepeatsReadOnly: 15,
};

/**
 * Tools whose repetition is normal research rather than a spin. An agent gathering context
 * legitimately calls Read/Grep dozens of times in a row, and re-reads a file after editing it;
 * only a MUTATING or EXECUTING tool repeating in place is a real runaway. Read-only calls
 * therefore get a much longer rope (stuckRepeatsReadOnly).
 *
 * WHY: on 2026-07-28 job 37 was killed as "stuck" after 6 Reads of six DIFFERENT files in one
 * campaign directory. The signature bug that made them look identical is fixed in conductor.ts,
 * but a 6-repeat threshold on reads was the other half of the false positive.
 */
export const READ_ONLY_TOOLS = new Set([
  'Read', 'Grep', 'Glob', 'NotebookRead', 'WebFetch', 'WebSearch', 'TodoWrite', 'Task',
]);

/** How many identical turns in a row it takes to call THIS signature a loop. */
export function repeatsForSignature(sig: string, lim: BreakerLimits): number {
  const i = sig.indexOf(':');
  const tool = i < 0 ? sig : sig.slice(0, i);
  return READ_ONLY_TOOLS.has(tool) ? lim.stuckRepeatsReadOnly : lim.stuckRepeats;
}

/**
 * Per-job-kind minimum turn limits. Some job kinds (content pipelines, features)
 * need more turns than a simple fix or daily scout. When the DB value is lower than
 * this floor, the conductor uses the floor instead. Set to 0 to use DB value as-is.
 */
export const KIND_MIN_TURNS: Record<string, number> = {
  feature: 80,    // content pipeline + full implementation
  fix: 40,        // targeted fix
  scout: 40,      // daily scan
  review: 60,     // full code review
  custom: 60,     // user-defined — be generous
};

export type Decision =
  | { action: 'continue' }
  | { action: 'pause'; reason: 'ratelimit'; backoffSecs: number }   // → defer + durable resume
  | { action: 'escalate'; reason: 'ask_gate' | 'turns' | 'stuck'; detail: string }
  | { action: 'stop'; reason: 'timeout' | 'completed' | 'error'; detail: string };

export interface BreakerState {
  startedAtMs: number;
  turns: number;
  recentSignatures: string[]; // rolling window of turn signatures for loop-detection
}

export function initState(): BreakerState {
  return { startedAtMs: Date.now(), turns: 0, recentSignatures: [] };
}

/** A "turn signature" = what the agent did this turn (tool + target). Repeated identical
 * signatures with no new files/results = spinning. Caller builds it from the event. */
export function pushSignature(s: BreakerState, sig: string): void {
  s.recentSignatures.push(sig);
  // Window must stay comfortably above the largest threshold, or a raised
  // stuckRepeatsReadOnly could never be reached because the tail got trimmed away.
  if (s.recentSignatures.length > 200) s.recentSignatures.shift();
}

/** Repeat count that tripped, or null when the tail is not a loop. */
function stuckAfter(s: BreakerState, lim: BreakerLimits): number | null {
  const last = s.recentSignatures[s.recentSignatures.length - 1];
  if (!last) return null;
  const repeats = repeatsForSignature(last, lim);
  if (repeats <= 1 || s.recentSignatures.length < repeats) return null;
  const tail = s.recentSignatures.slice(-repeats);
  return tail.every((x) => x === tail[0] && x !== '') ? repeats : null;
}

export type Event =
  | { kind: 'turn'; signature: string }
  | { kind: 'rate_limit'; status: 'allowed' | 'allowed_warning' | 'rejected'; retryAfterSecs?: number }
  | { kind: 'ask'; detail: string }            // agent requested an ask/deny-gated action
  | { kind: 'result'; ok: boolean; detail?: string };

/** Evaluate one event against the limits. Caller persists state between calls. */
export function evaluate(s: BreakerState, ev: Event, lim: BreakerLimits): Decision {
  // 1. terminal result from the agent
  if (ev.kind === 'result') {
    return ev.ok
      ? { action: 'stop', reason: 'completed', detail: ev.detail ?? '' }
      : { action: 'stop', reason: 'error', detail: ev.detail ?? '' };
  }

  // 2. rate limit / quota exhausted — pause + backoff (feeds durable resume)
  if (ev.kind === 'rate_limit') {
    if (ev.status === 'rejected') {
      return { action: 'pause', reason: 'ratelimit', backoffSecs: ev.retryAfterSecs ?? 60 };
    }
    return { action: 'continue' }; // allowed_warning logged by caller, lower concurrency
  }

  // 3. ask-gated action → human in the loop (Telegram)
  if (ev.kind === 'ask') {
    return { action: 'escalate', reason: 'ask_gate', detail: ev.detail };
  }

  // 4. turn → count, loop-detection (primary), wall-clock + turn-cap backstops
  if (ev.kind === 'turn') {
    s.turns += 1;
    pushSignature(s, ev.signature);
    const repeats = stuckAfter(s, lim);
    if (repeats !== null) {
      return { action: 'escalate', reason: 'stuck',
               detail: `loop: repeated ${repeats}x: ${s.recentSignatures[s.recentSignatures.length - 1]}` };
    }
    const wall = (Date.now() - s.startedAtMs) / 1000;
    if (wall >= lim.maxWallSecs) {
      return { action: 'stop', reason: 'timeout', detail: `wall ${Math.round(wall)}s >= ${lim.maxWallSecs}s` };
    }
    if (s.turns >= lim.maxTurns) {
      return { action: 'escalate', reason: 'turns', detail: `turn backstop ${lim.maxTurns} hit` };
    }
    return { action: 'continue' };
  }

  return { action: 'continue' };
}
