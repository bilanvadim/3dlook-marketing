/**
 * Fullstack agents Conductor — per-step loop decision logic (pure, unit-tested).
 *
 * Given the history of attempts on ONE plan step (each: did gates pass, reviewer score,
 * critical-issue count, did runtime pass), decide what to do next:
 *   done | retry | needs_review | blocked
 *
 * Ports the OrchestrAgent run-step discipline: progress-delta gating, plateau/regression
 * stop, needs-review soft-block. NO SDK/network here — the runner feeds it results.
 */

export interface StepLoopConfig {
  passScore: number;        // reviewer score to pass (default 85)
  needsReviewScore: number; // "close enough → hand to human" floor (default 70)
  minProgressDelta: number; // min reviewer-score improvement between gate-passing attempts (default 3)
  maxAttempts: number;      // hard cap on executor↔reviewer rounds (default 3)
}

export const DEFAULT_STEPLOOP: StepLoopConfig = {
  passScore: 85,
  needsReviewScore: 70,
  minProgressDelta: 3,
  maxAttempts: 3,
};

export interface AttemptResult {
  gatesPassed: boolean;          // ultracite + typecheck + tests + build all green (independent re-run)
  score: number;                 // reviewer 0-100 (0 if gates failed / reviewer blocked)
  criticalIssues: number;        // count of critical issues from the reviewer
  runtimePassed: boolean | null; // runtime/e2e verdict; null = not run (only run after reviewer approves)
}

export type StepDecision =
  | { action: 'done' }
  | { action: 'retry'; reason: string }
  | { action: 'needs_review'; reason: string }
  | { action: 'blocked'; reason: string };

/** Decide the next move after the latest attempt. `history` is oldest→newest, non-empty. */
export function decideStep(history: AttemptResult[], cfg: StepLoopConfig = DEFAULT_STEPLOOP): StepDecision {
  const n = history.length;
  const last = history[n - 1];
  const atCap = n >= cfg.maxAttempts;

  // success: gates green, score high, no criticals, runtime proven
  if (last.gatesPassed && last.score >= cfg.passScore && last.criticalIssues === 0 && last.runtimePassed === true) {
    return { action: 'done' };
  }

  // gates failing → keep retrying (that's what retries fix); cap → blocked
  if (!last.gatesPassed) {
    return atCap ? { action: 'blocked', reason: 'max_attempts: gates still failing' }
                 : { action: 'retry', reason: 'gates failed (preflight)' };
  }

  // gates green but runtime proven to fail → retry; cap → blocked
  if (last.runtimePassed === false) {
    return atCap ? { action: 'blocked', reason: 'max_attempts: runtime still failing' }
                 : { action: 'retry', reason: 'runtime failed' };
  }

  // gates green, reviewer score insufficient → progress-delta over gate-passing attempts
  const scored = history.filter((h) => h.gatesPassed).map((h) => h.score);
  if (scored.length >= 2) {
    const delta = scored[scored.length - 1] - scored[scored.length - 2];
    if (delta < 0) return { action: 'blocked', reason: `regression (${delta})` };
    if (delta < cfg.minProgressDelta) return { action: 'blocked', reason: `plateau (delta ${delta} < ${cfg.minProgressDelta})` };
  }

  if (atCap) {
    const monotonic = scored.every((v, i) => i === 0 || v >= scored[i - 1]);
    if (last.score >= cfg.needsReviewScore && monotonic) {
      return { action: 'needs_review', reason: `max attempts, close (${last.score})` };
    }
    return { action: 'blocked', reason: `max_attempts (score ${last.score})` };
  }

  return { action: 'retry', reason: `score ${last.score} < ${cfg.passScore}` };
}
