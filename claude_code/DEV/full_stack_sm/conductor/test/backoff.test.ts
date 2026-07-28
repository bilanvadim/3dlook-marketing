/**
 * Rate-limit backoff ladder test.
 *
 * REGRESSION GUARD for the 2026-07-27 hammering loop: the structured `rate_limit` SDK
 * message carries no retry_after, breaker.ts fell back to a flat 60s, and job 30 burned
 * 193 zero-turn runs over 3h22m re-claiming itself every ~63s against a 5-hour window.
 * The ladder must grow, must cap, and must always yield to a server-supplied retry_after.
 */
import { backoffForStreak } from '../src/core/conductor';

let pass = 0, fail = 0;
function check(name: string, cond: boolean) {
  if (cond) { pass++; console.log(`  ok  ${name}`); }
  else { fail++; console.log(`  FAIL ${name}`); }
}

const SAMPLES = 500;
/** Jitter is ±20%, so assert on the band rather than an exact value. */
function inBand(streak: number, base: number): boolean {
  for (let i = 0; i < SAMPLES; i++) {
    const v = backoffForStreak(streak);
    if (v < Math.max(30, Math.floor(base * 0.8)) || v > Math.ceil(base * 1.2)) return false;
  }
  return true;
}
const median = (streak: number): number => {
  const xs = Array.from({ length: SAMPLES }, () => backoffForStreak(streak)).sort((a, b) => a - b);
  return xs[Math.floor(xs.length / 2)];
};

// ladder shape: 60s → 5min → 15min → 30min
check('streak 0 → ~60s', inBand(0, 60));
check('streak 1 → ~5min', inBand(1, 300));
check('streak 2 → ~15min', inBand(2, 900));
check('streak 3 → ~30min', inBand(3, 1800));

// the last rung repeats forever — a long limit must never fall off the end or grow unbounded
check('streak 4 stays at the cap', inBand(4, 1800));
check('streak 50 stays at the cap', inBand(50, 1800));
check('negative streak clamps to the first rung', inBand(-3, 60));

// strictly growing: this is the whole point — a flat ladder is the bug
check('backoff grows with the streak', median(0) < median(1) && median(1) < median(2) && median(2) < median(3));

// a server-supplied retry_after always wins, verbatim and un-jittered
check('retry_after wins over the ladder', backoffForStreak(0, 42) === 42);
check('retry_after wins even deep in the streak', backoffForStreak(9, 7) === 7);
check('zero/absent retry_after falls back to the ladder', inBand(0, 60) && backoffForStreak(0, 0) !== 0);

// jitter must actually vary, or every worker retries in lockstep
check('jitter de-synchronises retries', new Set(Array.from({ length: 50 }, () => backoffForStreak(2))).size > 1);

// the ladder must clear a 5-hour window in a sane number of attempts (the original bug: 194)
let waited = 0, attempts = 0;
while (waited < 5 * 3600 && attempts < 100) { waited += backoffForStreak(attempts); attempts++; }
check(`clears a 5h window in <15 attempts (took ${attempts})`, attempts < 15);

console.log(`\nbackoff.test: ${pass} passed, ${fail} failed`);
if (fail) process.exit(1);
