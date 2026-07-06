import { decideStep, DEFAULT_STEPLOOP, AttemptResult, StepLoopConfig } from '../src/core/steploop';

let pass = 0, fail = 0;
function check(name: string, cond: boolean) {
  if (cond) { pass++; console.log(`  ok  ${name}`); }
  else { fail++; console.log(`  FAIL ${name}`); }
}
const C: StepLoopConfig = { ...DEFAULT_STEPLOOP, passScore: 85, needsReviewScore: 70, minProgressDelta: 3, maxAttempts: 3 };
const A = (gatesPassed: boolean, score: number, criticalIssues = 0, runtimePassed: boolean | null = null): AttemptResult =>
  ({ gatesPassed, score, criticalIssues, runtimePassed });

// 1. clean pass → done
check('done: gates+score+runtime ok', decideStep([A(true, 90, 0, true)], C).action === 'done');

// 2. high score but runtime failed → retry (attempt 1)
check('runtime fail -> retry', decideStep([A(true, 90, 0, false)], C).action === 'retry');

// 3. high score but a critical issue → not done → retry
check('critical -> not done', decideStep([A(true, 90, 1, true)], C).action !== 'done');

// 4. gates fail attempt 1 → retry
check('gates fail -> retry', decideStep([A(false, 0)], C).action === 'retry');

// 5. gates fail at cap → blocked
check('gates fail at cap -> blocked', decideStep([A(false,0),A(false,0),A(false,0)], C).action === 'blocked');

// 6. regression between gate-passing attempts → blocked (sub-pass scores → runtime not run → null)
{ const d = decideStep([A(true,80), A(true,70)], C); check('regression -> blocked', d.action === 'blocked' && /regression/.test((d as any).reason)); }

// 7. plateau (delta < 3) → blocked
{ const d = decideStep([A(true,80), A(true,81)], C); check('plateau -> blocked', d.action === 'blocked' && /plateau/.test((d as any).reason)); }

// 8. monotonic growth, below pass, at cap, >= needsReview → needs_review
check('cap+close+monotonic -> needs_review', decideStep([A(true,70),A(true,75),A(true,80)], C).action === 'needs_review');

// 9. growth but below needsReview at cap → blocked
check('cap+low -> blocked', decideStep([A(true,40),A(true,45),A(true,50)], C).action === 'blocked');

// 10. low score attempt 1 (room to retry) → retry
check('low score early -> retry', decideStep([A(true,60)], C).action === 'retry');

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
