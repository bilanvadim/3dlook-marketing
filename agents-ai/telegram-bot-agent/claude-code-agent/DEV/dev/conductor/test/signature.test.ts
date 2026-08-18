/**
 * Turn-signature test.
 *
 * REGRESSION GUARD for the 2026-07-28 false-positive loop. The signature used to be
 * `${tool}:${target.slice(0, 80)}`, and the campaign paths this conductor works in are 128
 * chars whose first 80 end exactly at `campaigns/2026`:
 *
 *   /home/vadim_prod/3dlook-marketing/marketing_vb/workspace/outbound/campaigns/2026-…/<file>
 *   ^------------------------------ first 80 chars are IDENTICAL -----------------^
 *
 * So six Reads of six DIFFERENT files collapsed to one signature, the breaker called it a loop,
 * and job 37 ("AU Telehealth v3: message-sequencer") was escalated and closed with zero work.
 * 8 of the first 11 escalations ever raised were this bug. The signature must discriminate on
 * the WHOLE input, not on a prefix.
 */
import { buildSignature, mapSdkMessage } from '../src/core/conductor';

let pass = 0, fail = 0;
function check(name: string, cond: boolean) {
  if (cond) { pass++; console.log(`  ok  ${name}`); }
  else { fail++; console.log(`  FAIL ${name}`); }
}

const CAMPAIGN = '/home/vadim_prod/3dlook-marketing/marketing_vb/workspace/outbound/campaigns/2026-07-27-australia-telehealth';
const FILES = [
  'people-validated.csv', 'hypothesis.md', 'icp-validation-summary.md',
  'people-raw-batch2.csv', 'people-raw-batch3.csv', 'generate_v3.py',
];

// ---- the exact job-37 shape ----
{
  // sanity: the paths really do share their first 80 chars, or this test proves nothing
  const prefixes = new Set(FILES.map((f) => `${CAMPAIGN}/${f}`.slice(0, 80)));
  check('precondition: the six paths DO share their first 80 chars', prefixes.size === 1);

  const sigs = FILES.map((f) => buildSignature('Read', { file_path: `${CAMPAIGN}/${f}` }));
  check('six different files in one campaign dir → six DIFFERENT signatures',
        new Set(sigs).size === FILES.length);
}

// ---- determinism ----
{
  const a = buildSignature('Read', { file_path: `${CAMPAIGN}/hypothesis.md` });
  const b = buildSignature('Read', { file_path: `${CAMPAIGN}/hypothesis.md` });
  check('same call → same signature (a real loop is still detectable)', a === b);
}
{
  // key order must not matter, or an identical repeated call could hash differently and hide a loop
  const a = buildSignature('Read', { file_path: '/x/y.md', offset: 1, limit: 20 });
  const b = buildSignature('Read', { limit: 20, file_path: '/x/y.md', offset: 1 });
  check('key order does not change the signature', a === b);
}

// ---- fields beyond the path still discriminate ----
{
  const a = buildSignature('Read', { file_path: '/x/y.md', offset: 1 });
  const b = buildSignature('Read', { file_path: '/x/y.md', offset: 500 });
  check('same file, different offset → different signature', a !== b);
}
{
  const long = 'x'.repeat(300);
  const a = buildSignature('Bash', { command: `grep ${long} a.txt` });
  const b = buildSignature('Bash', { command: `grep ${long} b.txt` });
  check('two 300-char commands differing only at the END → different signatures', a !== b);
}
{
  const a = buildSignature('WebSearch', { query: 'australia telehealth providers' });
  const b = buildSignature('WebSearch', { query: 'australia telehealth regulation' });
  check('WebSearch queries discriminate', a !== b);
}
{
  const a = buildSignature('WebFetch', { urls: ['https://a.example/one'] });
  const b = buildSignature('WebFetch', { urls: ['https://a.example/two'] });
  check('WebFetch urls-array discriminates', a !== b);
}
{
  const a = buildSignature('Read', { file_path: '/x/y.md' });
  const b = buildSignature('Grep', { path: '/x/y.md' });
  check('different tools on the same target → different signatures', a !== b);
}
{
  // an empty / unrecognised input must not collapse every such call into one signature
  const a = buildSignature('Task', { subagent_type: 'seo-writer', description: 'write section 1' });
  const b = buildSignature('Task', { subagent_type: 'seo-writer', description: 'write section 2' });
  check('unrecognised input shapes still discriminate (hash covers everything)', a !== b);
}

// ---- readability: the breaker's detail string goes straight to Telegram ----
{
  const sig = buildSignature('Read', { file_path: `${CAMPAIGN}/people-validated.csv` });
  check('signature keeps the tool name', sig.startsWith('Read:'));
  check('signature keeps a readable tail (basename survives)', sig.includes('people-validated.csv'));
  check('signature carries a digest', /#[0-9a-f]{12}$/.test(sig));
}

// ---- the breaker threshold keys off the tool prefix, so it must survive mapSdkMessage ----
{
  const m = mapSdkMessage({
    type: 'assistant',
    message: { content: [{ type: 'tool_use', name: 'Read', input: { file_path: `${CAMPAIGN}/hypothesis.md` } }] },
  });
  check('mapSdkMessage emits one turn event', m.events.length === 1 && m.events[0].kind === 'turn');
  check('mapSdkMessage signature is tool-prefixed', !!m.signature?.startsWith('Read:'));
  check('mapSdkMessage reports the tool name', m.toolName === 'Read');
}
{
  const m = mapSdkMessage({ type: 'assistant', message: { content: [{ type: 'text', text: 'thinking' }] } });
  check('a text-only assistant turn keeps the assistant:text signature', m.signature === 'assistant:text');
}

console.log(`\nsignature.test: ${pass} passed, ${fail} failed`);
if (fail) process.exit(1);
