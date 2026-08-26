/**
 * Ask-gate test.
 *
 * REGRESSION GUARD for a gate that could be walked past with a long path. `asksForGatedAction` used
 * to match ASK_PATTERNS against the SIGNATURE, whose readable half is only the last 56 characters of
 * the target — so `rm -rf <78-char path>` had its `rm -rf` truncated away and executed with no
 * Telegram gate, while the identical command on a short path gated correctly. A `DROP TABLE` in a
 * long psql command survived only by luck, when the keyword happened to fall inside the tail.
 *
 * Second half of the same bug: only the FIRST tool_use block of an assistant message produced a
 * signature, so a gated action in the second block was never checked at all.
 */
import { mapSdkMessage } from '../src/core/conductor';

let pass = 0, fail = 0;
function check(name: string, cond: boolean) {
  if (cond) { pass++; console.log(`  ok  ${name}`); }
  else { fail++; console.log(`  FAIL ${name}`); }
}

// Mirror of the conductor's ASK_PATTERNS, applied the way the conductor applies them.
const ASK = [
  /wrangler\s+(deploy|publish)/i, /terraform\s+(apply|destroy)/i,
  /supabase\s+db\s+push/i, /gh\s+pr\s+merge/i,
  /\brm\s+-[a-z]*r[a-z]*/i, /\bgit\s+reset\s+--hard\b/i,
  /\bgit\s+clean\s+-[a-z]*f/i, /\b(DROP\s+(TABLE|DATABASE|SCHEMA)|TRUNCATE)\b/i,
];
const gated = (msg: any) => mapSdkMessage(msg).gateTexts.some((t) => ASK.some((p) => p.test(t)));
const bash = (command: string) => ({ type: 'assistant', message: { content: [{ type: 'tool_use', name: 'Bash', input: { command } }] } });

// ---- the length that used to decide whether a gate fired ----
const LONG = '/srv/app/workspace/outbound/campaigns/2026/data/exports/old-batch-files';
check('short rm -rf is gated', gated(bash('rm -rf ./build')));
check(`rm -rf on a ${LONG.length}-char path is gated (was NOT)`, gated(bash(`rm -rf ${LONG}`)));
check('rm -rf with flags before a long path is gated', gated(bash(`rm -rf --no-preserve-root ${LONG}`)));
check('git reset --hard is gated at any length', gated(bash(`git reset --hard origin/main # ${LONG}`)));
check('DROP TABLE early in a long command is gated (survived only by luck before)',
      gated(bash(`psql -h localhost -U app -c "DROP TABLE events" --set=x=${LONG}`)));

// ---- every tool_use block, not just the first ----
check('a gated action in the SECOND tool_use block is caught', gated({
  type: 'assistant',
  message: { content: [
    { type: 'tool_use', name: 'Read', input: { file_path: '/tmp/a.md' } },
    { type: 'tool_use', name: 'Bash', input: { command: `rm -rf ${LONG}` } },
  ] },
}));
check('three blocks, gated one last', gated({
  type: 'assistant',
  message: { content: [
    { type: 'tool_use', name: 'Read', input: { file_path: '/tmp/a.md' } },
    { type: 'tool_use', name: 'Grep', input: { pattern: 'x' } },
    { type: 'tool_use', name: 'Bash', input: { command: 'terraform destroy -auto-approve' } },
  ] },
}));

// ---- and it must not fire on innocent work, or the Telegram gate becomes noise ----
check('a plain build is not gated', !gated(bash('npm run build')));
check('git push (not force) is not gated', !gated(bash('git push origin main')));
// `DROP` alone is not a gated pattern — only DROP TABLE/DATABASE/SCHEMA and TRUNCATE are, so
// searching source for the word must stay silent.
check('grep for the word DROP in source is not gated', !gated(bash('grep -rn "DROP" src/')));
check('a text-only assistant turn yields no gate text', mapSdkMessage({ type: 'assistant', message: { content: [{ type: 'text', text: 'thinking' }] } }).gateTexts.length === 0);
check('a non-assistant message yields no gate text', mapSdkMessage({ type: 'result', subtype: 'success' }).gateTexts.length === 0);

console.log(`\naskgate.test: ${pass} passed, ${fail} failed`);
if (fail) process.exit(1);
