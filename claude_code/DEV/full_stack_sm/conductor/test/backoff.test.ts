/**
 * Rate-limit backoff ladder test.
 *
 * REGRESSION GUARD for the 2026-07-27 hammering loop: the structured `rate_limit` SDK
 * message carries no retry_after, breaker.ts fell back to a flat 60s, and job 30 burned
 * 193 zero-turn runs over 3h22m re-claiming itself every ~63s against a 5-hour window.
 * The ladder must grow, must cap, and must always yield to a server-supplied retry_after.
 */
import { backoffForStreak, shouldNotifyPause, effectiveLimitStatus, retryAfterFromLimitInfo,
         describeLimitInfo, mapSdkMessage } from '../src/core/conductor';

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

// ---- Telegram pause notice gating ----
// REGRESSION GUARD for the 2026-07-28 spam: job 41 ("Telehealth Hub — Full Publish Pack v3")
// paused 6 times in 7 minutes, every one at streak 0, and the old streak-parity gate read every
// one as a "first pause" → a Telegram message every ~50s. The gate now keys off the WAIT.
check('first pause always reports', shouldNotifyPause(50, true));
check('a short retry stays quiet', !shouldNotifyPause(50, false));
check('a 5-min retry still stays quiet', !shouldNotifyPause(300, false));
check('a 10-min wait reports', shouldNotifyPause(600, false));
check('a capped 30-min wait reports', shouldNotifyPause(1800, false));
// the whole point: a fast retry loop must be silent at EVERY rung the ladder can produce below 10 min
check('no rung under 10 min ever spams', ![0, 1].some((s) => shouldNotifyPause(backoffForStreak(s), false)));
check('the upper rungs do report', [2, 3, 50].every((s) => shouldNotifyPause(backoffForStreak(s), false)));

// ---- what counts as a REAL rejection ----
// REGRESSION GUARD for 2026-09-04: the SDK reported the five-hour window as `rejected` while
// overage billing kept serving every request, and reading `status` alone paused the whole social
// fan-out 23 times (jobs 112-120, 0-3 turns each, 09:47→13:34) on an account that was working.
// This is the exact payload measured that day.
const OVERAGE_CARRIED = {
  status: 'rejected', resetsAt: 1788530400, rateLimitType: 'five_hour',
  overageStatus: 'allowed', isUsingOverage: true, overageInUse: true,
};
check('a window overage is paying for is NOT a rejection',
      effectiveLimitStatus(OVERAGE_CARRIED) === 'allowed_warning');
check('a rejection with overage refused IS a rejection',
      effectiveLimitStatus({ ...OVERAGE_CARRIED, overageStatus: 'rejected' }) === 'rejected');
check('a rejection with no overage field at all IS a rejection',
      effectiveLimitStatus({ status: 'rejected', rateLimitType: 'five_hour' }) === 'rejected');
check('allowed stays allowed', effectiveLimitStatus({ status: 'allowed' }) === 'allowed');
check('a warning is passed through', effectiveLimitStatus({ status: 'allowed_warning' }) === 'allowed_warning');
check('an empty info defaults to allowed', effectiveLimitStatus({}) === 'allowed');

// the SDK's real message type is `rate_limit_event`; it must reach the breaker as a rate_limit
const mapped = mapSdkMessage({ type: 'rate_limit_event', rate_limit_info: OVERAGE_CARRIED });
check('rate_limit_event maps to one rate_limit event',
      mapped.type === 'rate_limit' && mapped.events.length === 1 && mapped.events[0].kind === 'rate_limit');
check('the mapped event carries the downgraded status',
      mapped.events[0].kind === 'rate_limit' && mapped.events[0].status === 'allowed_warning');
check('the mapped event carries a readable detail',
      /five_hour/.test((mapped.events[0] as any).detail ?? ''));

// ---- resetsAt is the wait, when there is a real rejection ----
// The five-hour message never carries retry_after, which is what made the ladder guess at it.
check('retry_after wins when present', retryAfterFromLimitInfo({ retry_after: 90 }) === 90);
const inAnHour = Math.floor(Date.now() / 1000) + 3600;
const fromReset = retryAfterFromLimitInfo({ resetsAt: inAnHour });
check(`resetsAt becomes the wait (${fromReset}s)`, fromReset !== undefined && fromReset > 3600 && fromReset <= 3630);
check('a past resetsAt falls back to the ladder', retryAfterFromLimitInfo({ resetsAt: 1 }) === undefined);
check('a bogus resetsAt falls back to the ladder',
      retryAfterFromLimitInfo({ resetsAt: 'soon' }) === undefined && retryAfterFromLimitInfo({}) === undefined);
check('an absurd resetsAt is capped at 6h',
      retryAfterFromLimitInfo({ resetsAt: Math.floor(Date.now() / 1000) + 30 * 86400 }) === 6 * 3600);
check('the wait from resetsAt beats the ladder verbatim',
      backoffForStreak(0, retryAfterFromLimitInfo({ resetsAt: inAnHour })) === fromReset);

// the pause record must say WHY, or the next incident is another blind re-run of the SDK by hand
check('describeLimitInfo names the window, the overage and the reset',
      /five_hour/.test(describeLimitInfo(OVERAGE_CARRIED))
      && /overage=allowed/.test(describeLimitInfo(OVERAGE_CARRIED))
      && /resets=2026-09-04T14:00:00Z/.test(describeLimitInfo(OVERAGE_CARRIED)));

console.log(`\nbackoff.test: ${pass} passed, ${fail} failed`);
if (fail) process.exit(1);
