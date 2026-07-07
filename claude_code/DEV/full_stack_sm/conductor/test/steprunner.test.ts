import { runStep, StepRecord, StepRunnerDeps, StepStore } from '../src/core/steprunner';
import { DEFAULT_STEPLOOP } from '../src/core/steploop';

let pass = 0, fail = 0;
function check(name: string, cond: boolean) {
  if (cond) { pass++; console.log(`  ok  ${name}`); }
  else { fail++; console.log(`  FAIL ${name}`); }
}

const cfg = { ...DEFAULT_STEPLOOP, maxAttempts: 3, minProgressDelta: 3, passScore: 85, needsReviewScore: 70 };
const step = (qb: unknown = { e2e: true }): StepRecord =>
  ({ id: 1, job_id: 1, step_no: 1, title: 't', agent: 'backend-engineer', tags: ['backend'], description: 'd', acceptance: [], quality_bar: qb, attempts: 1, status: 'running' });

function fakeStore() {
  const calls: string[] = [];
  const store: StepStore = {
    async recordAttempt() { calls.push('attempt'); },
    async setStepStatus(_id, s) { calls.push('status:' + s); },
    async finishStep(_id, f) { calls.push('finish:' + f.status); },
  };
  return { store, calls };
}

// scripted deps: arrays indexed by attempt
function deps(script: {
  exec?: boolean[]; gates?: boolean[]; review?: { score: number; crit?: number; verdict?: 'approve'|'request_changes'|'block' }[]; runtime?: boolean[];
}): StepRunnerDeps {
  let e = 0, g = 0, r = 0, t = 0;
  return {
    async runExecutor() { return { ok: script.exec ? script.exec[e++] : true }; },
    async runGates() { return { passed: script.gates ? script.gates[g++] : true, detail: 'x' }; },
    async runReviewer() { const s = script.review![r++]; return { score: s.score, criticalIssues: s.crit ?? 0, verdict: s.verdict ?? (s.score >= 85 ? 'approve' : 'request_changes'), reportJson: {}, retryInstructions: 'fix it' }; },
    async runRuntime() { return { passed: script.runtime ? script.runtime[t++] : true, reportJson: {} }; },
  };
}

await (async () => {
  // 1. pass on first try
  { const { store, calls } = fakeStore();
    const o = await runStep(step(), deps({ review: [{ score: 90 }], runtime: [true] }), store, cfg);
    check('pass first try -> done, 1 attempt', o.decision.action === 'done' && o.attempts === 1);
    check('  finished done', calls.includes('finish:done')); }

  // 2. retry then pass
  { const { store } = fakeStore();
    const o = await runStep(step(), deps({ review: [{ score: 60 }, { score: 90 }], runtime: [true] }), store, cfg);
    check('retry then pass -> done, 2 attempts', o.decision.action === 'done' && o.attempts === 2); }

  // 3. gates fail then pass
  { const { store } = fakeStore();
    const o = await runStep(step(), deps({ gates: [false, true], review: [{ score: 90 }], runtime: [true] }), store, cfg);
    check('gates fail then pass -> done, 2 attempts', o.decision.action === 'done' && o.attempts === 2); }

  // 4. plateau -> blocked at attempt 2
  { const { store } = fakeStore();
    const o = await runStep(step(), deps({ review: [{ score: 80 }, { score: 81 }] }), store, cfg);
    check('plateau -> blocked', o.decision.action === 'blocked' && o.attempts === 2); }

  // 5. monotonic growth, capped -> needs_review
  { const { store } = fakeStore();
    const o = await runStep(step(), deps({ review: [{ score: 70 }, { score: 75 }, { score: 80 }] }), store, cfg);
    check('cap monotonic close -> needs_review, 3 attempts', o.decision.action === 'needs_review' && o.attempts === 3); }

  // 6. approved but runtime fails -> retry then runtime pass -> done
  { const { store } = fakeStore();
    const o = await runStep(step(), deps({ review: [{ score: 90 }, { score: 90 }], runtime: [false, true] }), store, cfg);
    check('runtime fail then pass -> done', o.decision.action === 'done' && o.attempts === 2); }

  // 7. step with no e2e quality_bar -> approved without runtime call -> done
  { const { store } = fakeStore();
    const o = await runStep(step({ e2e: false }), deps({ review: [{ score: 88 }] }), store, cfg);
    check('no-e2e step -> done without runtime', o.decision.action === 'done' && o.attempts === 1); }

  console.log(`\n${pass} passed, ${fail} failed`);
  process.exit(fail ? 1 : 0);
})();
