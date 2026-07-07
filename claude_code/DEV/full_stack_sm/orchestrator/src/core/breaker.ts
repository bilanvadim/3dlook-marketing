/**
 * Fullstack agents Orchestrator — circuit breaker.
 * Pure decision logic, no SDK/network deps, so it is unit-testable in isolation.
 * The core loop feeds it every event; it returns whether to continue, pause, or stop.
 *
 * SCOPE (deliberately narrow): we do NOT cap spend — cost is not optimized here.
 * The only thing the agent can't reason its way out of is SPINNING IN A LOOP, so
 * that is the primary control. Turn/wall-clock caps are generous runaway backstops,
 * not budget controls. Rate-limit pause feeds durable resume; ask-gate feeds Telegram.
 */

export interface BreakerLimits {
  maxTurns: number;          // generous runaway backstop (NOT a budget)
  maxWallSecs: number;       // generous per-run wall-clock backstop
  stuckRepeats: number;      // identical-signature turns before declaring a loop
}

export const DEFAULT_LIMITS: BreakerLimits = {
  maxTurns: 300,
  maxWallSecs: 4 * 60 * 60,  // 4h per contiguous run; longer waits handled by resume
  stuckRepeats: 6,
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
  if (s.recentSignatures.length > 50) s.recentSignatures.shift();
}

function isStuck(s: BreakerState, repeats: number): boolean {
  if (s.recentSignatures.length < repeats) return false;
  const tail = s.recentSignatures.slice(-repeats);
  return tail.every((x) => x === tail[0] && x !== '');
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
    if (isStuck(s, lim.stuckRepeats)) {
      return { action: 'escalate', reason: 'stuck',
               detail: `loop: repeated ${lim.stuckRepeats}x: ${s.recentSignatures.slice(-1)[0]}` };
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
