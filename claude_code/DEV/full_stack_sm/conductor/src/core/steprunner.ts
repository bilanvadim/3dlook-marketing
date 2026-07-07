/**
 * Fullstack agents Conductor — per-step runner (orchestration).
 *
 * Runs ONE plan step through the verification loop: executor → independent gates →
 * reviewer (score) → runtime (when approved) → decideStep → persist. Retries with
 * cumulative critiques until decideStep says done / needs_review / blocked.
 *
 * Testable: the agent calls and the store are injected (interfaces). The real SDK
 * adapter lives in agent-runner.ts; the real store in store.ts.
 */
import { decideStep, AttemptResult, StepLoopConfig, DEFAULT_STEPLOOP, StepDecision } from './steploop';

export interface StepRecord {
  id: number; job_id: number; step_no: number; title: string; agent: string | null;
  tags: string[]; description: string | null; acceptance: unknown; quality_bar: unknown;
  attempts: number; status: string;
}

export interface ExecutorResult { ok: boolean; detail?: string; }
export interface GateResult { passed: boolean; detail: string; }
export interface ReviewResult {
  score: number; criticalIssues: number;
  verdict: 'approve' | 'request_changes' | 'block';
  reportJson: unknown; retryInstructions?: string;
}
export interface RuntimeResult { passed: boolean; reportJson: unknown; }

export interface StepRunnerDeps {
  runExecutor(step: StepRecord, critiques: string[]): Promise<ExecutorResult>; // builds the step (baseline-reset inside)
  runGates(step: StepRecord): Promise<GateResult>;       // ultracite+typecheck+test+build, re-run independently
  runReviewer(step: StepRecord): Promise<ReviewResult>;
  runRuntime(step: StepRecord): Promise<RuntimeResult>;  // only when reviewer approves & quality_bar wants it
}

export interface StepStore {
  recordAttempt(stepId: number): Promise<void>;
  setStepStatus(stepId: number, status: string): Promise<void>;
  finishStep(stepId: number, fields: { status: string; score?: number; reviewer_report?: unknown; runtime_report?: unknown; error?: string }): Promise<void>;
}

export interface StepOutcome { decision: StepDecision; attempts: number; lastScore: number; }

function wantsRuntime(step: StepRecord): boolean {
  const qb = step.quality_bar as { e2e?: unknown } | null | undefined;
  return !!qb && (qb.e2e === true || qb.e2e === 'yes');
}

export async function runStep(
  step: StepRecord,
  deps: StepRunnerDeps,
  store: StepStore,
  cfg: StepLoopConfig = DEFAULT_STEPLOOP,
): Promise<StepOutcome> {
  const history: AttemptResult[] = [];
  const critiques: string[] = [];
  let attempt = 0;

  for (;;) {
    attempt++;
    if (attempt > 1) await store.recordAttempt(step.id); // claim already counted attempt 1

    const exec = await deps.runExecutor(step, critiques);
    let result: AttemptResult;

    if (!exec.ok) {
      result = { gatesPassed: false, score: 0, criticalIssues: 0, runtimePassed: null };
      critiques.push(`attempt ${attempt}: executor failed — ${exec.detail ?? 'no detail'}`);
    } else {
      const gates = await deps.runGates(step);
      if (!gates.passed) {
        // preflight short-circuit: skip the (expensive) reviewer on a broken build
        result = { gatesPassed: false, score: 0, criticalIssues: 0, runtimePassed: null };
        critiques.push(`attempt ${attempt}: gates failed — ${gates.detail}`);
      } else {
        await store.setStepStatus(step.id, 'verifying');
        const rev = await deps.runReviewer(step);
        let runtimePassed: boolean | null = null;
        const approved = rev.verdict === 'approve' && rev.criticalIssues === 0 && rev.score >= cfg.passScore;
        if (approved && wantsRuntime(step)) {
          const rt = await deps.runRuntime(step);
          runtimePassed = rt.passed;
          await store.finishStep(step.id, { status: 'verifying', score: rev.score, reviewer_report: rev.reportJson, runtime_report: rt.reportJson });
        } else if (approved) {
          runtimePassed = true; // no runtime gate required for this step
          await store.finishStep(step.id, { status: 'verifying', score: rev.score, reviewer_report: rev.reportJson });
        } else {
          await store.finishStep(step.id, { status: 'verifying', score: rev.score, reviewer_report: rev.reportJson });
        }
        result = { gatesPassed: true, score: rev.score, criticalIssues: rev.criticalIssues, runtimePassed };
        if (!approved && rev.retryInstructions) critiques.push(`attempt ${attempt} (score ${rev.score}): ${rev.retryInstructions}`);
      }
    }

    history.push(result);
    const decision = decideStep(history, cfg);
    if (decision.action !== 'retry') {
      const status = decision.action === 'done' ? 'done' : decision.action; // needs_review|blocked
      const reason = decision.action === 'done' ? undefined : (decision as { reason: string }).reason;
      await store.finishStep(step.id, { status, score: result.score, error: reason });
      return { decision, attempts: attempt, lastScore: result.score };
    }
    // retry: executor adapter resets the working tree to the step baseline before rebuilding
  }
}
