/**
 * Profile resolution test.
 *
 * REGRESSION GUARD for a silent failure, not a crash. resolveProfilePlugins() used to
 * console.warn "no manifest for '<x>' — falling back to project settings" and return [],
 * so a job whose profile has no manifest ran with NONE of its plugins. For a
 * marketing_vb_sm job that is the entire marketing system absent: no error, no failed
 * step, nothing in ho_project_status, and an agent producing output with no idea what it
 * was meant to be. 88 of the jobs in the live queue are marketing_vb_sm.
 *
 * And it was reachable without a typo: ho_jobs' CHECK constraint accepts 'sandbox' and
 * 'test', neither of which has a manifest on disk, so such a job passed every validation
 * that exists and then ran empty.
 *
 * The plugin COUNTS are asserted too, not just "some plugins": a manifest that resolves to
 * 1 plugin instead of 12 also loads successfully.
 */
import { resolveProfilePlugins } from '../src/core/profiles';

let pass = 0, fail = 0;
function check(name: string, cond: boolean, detail = '') {
  if (cond) { pass++; console.log(`  ok  ${name}`); }
  else { fail++; console.log(`  FAIL ${name}${detail ? ' — ' + detail : ''}`); }
}

// Minimum plugin count per real profile. Lower bounds, so adding a plugin does not break
// the test, while a manifest silently resolving to nothing does.
const REAL: [string, number][] = [
  ['dev', 11], ['seo', 7], ['marketing', 7], ['security', 4],
  ['marketing_vb', 4], ['marketing_vb_sm', 12], ['sandbox_sm', 2],
];
for (const [name, min] of REAL) {
  try {
    const n = resolveProfilePlugins(name).length;
    check(`${name} resolves to >= ${min} plugin(s)`, n >= min, `got ${n}`);
  } catch (e) {
    check(`${name} resolves`, false, String(e).split('\n')[0]);
  }
}

// Names the CHECK constraint allows but no manifest backs — must THROW, never return [].
for (const ghost of ['sandbox', 'test', 'definitely-not-a-profile']) {
  let threw = false, msg = '';
  try { resolveProfilePlugins(ghost); } catch (e) { threw = true; msg = String(e); }
  check(`'${ghost}' throws instead of running with no plugins`, threw);
  if (threw) {
    check(`'${ghost}' error names the profile and lists the alternatives`,
          msg.includes(ghost) && msg.includes('Available profiles'));
  }
}

// An empty/absent profile must fall to 'dev', which is a real manifest — not to nothing.
check("empty profile falls back to 'dev' and still loads plugins",
      resolveProfilePlugins('').length >= 11);
check("null profile falls back to 'dev' and still loads plugins",
      resolveProfilePlugins(null).length >= 11);

console.log(`\nprofiles.test: ${pass} passed, ${fail} failed`);
if (fail) process.exit(1);
