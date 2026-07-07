import { evaluate, initState, DEFAULT_LIMITS, BreakerLimits } from '../src/core/breaker';

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

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
