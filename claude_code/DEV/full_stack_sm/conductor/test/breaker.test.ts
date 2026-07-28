import { evaluate, initState, DEFAULT_LIMITS, BreakerLimits, repeatsForSignature } from '../src/core/breaker';

let pass = 0, fail = 0;
function check(name: string, cond: boolean) {
  if (cond) { pass++; console.log(`  ok  ${name}`); }
  else { fail++; console.log(`  FAIL ${name}`); }
}

const L: BreakerLimits = { ...DEFAULT_LIMITS, maxTurns: 5, maxWallSecs: 999, stuckRepeats: 3 };

// 1. loop detection escalates (primary control)
{
  const s = initState();
  let d: any;
  for (let i = 0; i < 3; i++) d = evaluate(s, { kind: 'turn', signature: 'Edit:foo.ts' }, L);
  check('stuck: 3x same signature -> escalate', d.action === 'escalate' && d.reason === 'stuck');
}
// 2. varied work does NOT trigger loop detection
{
  const s = initState();
  let d: any;
  ['a','b','c'].forEach(sig => d = evaluate(s, { kind: 'turn', signature: sig }, L));
  check('not-stuck: varied work continues', d.action === 'continue');
}
// 3. turn-cap backstop escalates
{
  const s = initState();
  let d: any;
  for (let i = 0; i < 5; i++) d = evaluate(s, { kind: 'turn', signature: `t${i}` }, L);
  check('turns: backstop -> escalate', d.action === 'escalate' && d.reason === 'turns');
}
// 4. rate limit rejected -> pause with backoff (durable resume)
{
  const s = initState();
  const d: any = evaluate(s, { kind: 'rate_limit', status: 'rejected', retryAfterSecs: 30 }, L);
  check('ratelimit: rejected -> pause', d.action === 'pause' && d.backoffSecs === 30);
}
// 5. rate limit warning -> continue
{
  const s = initState();
  const d = evaluate(s, { kind: 'rate_limit', status: 'allowed_warning' }, L);
  check('ratelimit: warning -> continue', d.action === 'continue');
}
// 6. ask gate -> escalate
{
  const s = initState();
  const d: any = evaluate(s, { kind: 'ask', detail: 'gh pr merge' }, L);
  check('ask: gated action -> escalate', d.action === 'escalate' && d.reason === 'ask_gate');
}
// 7. wall-clock timeout backstop -> stop
{
  const s = initState(); s.startedAtMs = Date.now() - 1000 * 1000;
  const d: any = evaluate(s, { kind: 'turn', signature: 'x' }, { ...L, maxWallSecs: 60 });
  check('timeout: wall exceeded -> stop', d.action === 'stop' && d.reason === 'timeout');
}
// 8. clean completion
{
  const s = initState();
  const d: any = evaluate(s, { kind: 'result', ok: true, detail: 'done' }, L);
  check('result: ok -> stop completed', d.action === 'stop' && d.reason === 'completed');
}
// 9. error result -> stop error
{
  const s = initState();
  const d: any = evaluate(s, { kind: 'result', ok: false, detail: 'boom' }, L);
  check('result: error -> stop error', d.action === 'stop' && d.reason === 'error');
}

// ---- read-only tools get a longer rope (2026-07-28 job 37 false positive) ----
// Reading files IS how an agent gathers context; six reads in a row is research, not a spin.
const RO: BreakerLimits = { ...DEFAULT_LIMITS, maxTurns: 500, maxWallSecs: 999, stuckRepeats: 3, stuckRepeatsReadOnly: 10 };

// 10. threshold is chosen per tool, from the signature prefix
check('repeatsFor: Read uses the read-only threshold', repeatsForSignature('Read:a.md#deadbeef', RO) === 10);
check('repeatsFor: Grep uses the read-only threshold', repeatsForSignature('Grep:foo#deadbeef', RO) === 10);
check('repeatsFor: Edit uses the mutating threshold', repeatsForSignature('Edit:a.ts#deadbeef', RO) === 3);
check('repeatsFor: Bash uses the mutating threshold', repeatsForSignature('Bash:rm -rf x#deadbeef', RO) === 3);
check('repeatsFor: a signature with no colon still resolves', repeatsForSignature('weird', RO) === 3);

// 11. the mutating threshold must NOT be applied to reads
{
  const s = initState();
  let d: any;
  for (let i = 0; i < 9; i++) d = evaluate(s, { kind: 'turn', signature: 'Read:same.md#deadbeef' }, RO);
  check('read-only: 9 identical reads still continue (mutating limit is 3)', d.action === 'continue');
  d = evaluate(s, { kind: 'turn', signature: 'Read:same.md#deadbeef' }, RO);
  check('read-only: the 10th identical read escalates', d.action === 'escalate' && d.reason === 'stuck');
  check('read-only: detail reports the threshold that tripped', /repeated 10x/.test(d.detail));
}

// 12. a mutating tool spinning in place is still caught fast — that is the control we keep
{
  const s = initState();
  let d: any;
  for (let i = 0; i < 3; i++) d = evaluate(s, { kind: 'turn', signature: 'Edit:a.ts#deadbeef' }, RO);
  check('mutating: 3 identical edits escalate', d.action === 'escalate' && d.reason === 'stuck');
  check('mutating: detail reports the mutating threshold', /repeated 3x/.test(d.detail));
}

// 13. distinct reads never trip, however many — the job-37 shape
{
  const s = initState();
  let d: any;
  for (let i = 0; i < 60; i++) d = evaluate(s, { kind: 'turn', signature: `Read:file${i}.md#hash${i}` }, RO);
  check('read-only: 60 DIFFERENT reads never trip loop detection', d.action === 'continue');
}

// 14. an interleaved read breaks a mutating streak (tail-based, not count-based)
{
  const s = initState();
  let d: any;
  evaluate(s, { kind: 'turn', signature: 'Edit:a.ts#1' }, RO);
  evaluate(s, { kind: 'turn', signature: 'Edit:a.ts#1' }, RO);
  evaluate(s, { kind: 'turn', signature: 'Read:b.md#2' }, RO);
  d = evaluate(s, { kind: 'turn', signature: 'Edit:a.ts#1' }, RO);
  check('tail-based: an interleaved turn breaks the streak', d.action === 'continue');
}

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
