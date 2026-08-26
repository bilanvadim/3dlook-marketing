/**
 * Escalation-callback test.
 *
 * REGRESSION GUARD for a lost human decision. The webhook used to open its OWN libSQL client — no
 * WAL, no busy_timeout (a fresh connection defaults to 0: fail instantly), no retry — and fire a
 * bare UPDATE. With conductor workers writing the same file, that throws SQLITE_BUSY, the webhook
 * answers HTTP 500, and the Approve/Deny/ABORT tap is gone with nothing in any log saying so.
 */
import { readFileSync, rmSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createClient } from './_client';
import { Store } from '../src/core/store';

const HERE = dirname(fileURLToPath(import.meta.url));
const DB_PATH = join(HERE, `.callback-test-${process.pid}.db`);
const URL = `file:${DB_PATH}`;
let pass = 0, fail = 0;
const check = (n: string, c: boolean) => { c ? (pass++, console.log(`  ok  ${n}`)) : (fail++, console.log(`  FAIL ${n}`)); };

async function main() {
  const boot = createClient({ url: URL });
  await boot.execute('PRAGMA journal_mode = WAL');
  await boot.executeMultiple(readFileSync(join(HERE, '..', 'sql', 'schema.sql'), 'utf8'));
  await boot.execute("insert into ho_jobs(kind,title,prompt,profile,work_dir) values('fix','cb','p','dev','/tmp')");
  await boot.execute('insert into ho_runs(job_id,attempt,status) values(1,1,\'running\')');
  await boot.execute("insert into ho_escalations(run_id,job_id,reason,question,context,status) values(1,1,'ask_gate','deploy?','{}','open')");
  boot.close();

  const store = new Store(URL);
  check('a decision on an open escalation applies', (await store.decideEscalation(1, 'approved', 'tester')) === 'applied');
  check('the first decision wins — a second tap is reported, not overwritten',
        (await store.decideEscalation(1, 'denied', 'other')) === 'already-decided');
  const st = await new Store(URL).waitEscalation(1, { timeoutMs: 100, pollMs: 20 });
  check('the recorded decision is the FIRST one', st === 'approved');
  check('a callback for a row that never existed says so', (await store.decideEscalation(999, 'approved', 'tester')) === 'missing');

  // THE point: a decision arriving while another writer holds the lock must survive.
  const boot2 = createClient({ url: URL });
  await boot2.execute("insert into ho_escalations(run_id,job_id,reason,question,context,status) values(1,1,'turns','more?','{}','open')");
  const eid = Number((await boot2.execute('select max(id) as id from ho_escalations')).rows[0].id);
  const blocker = createClient({ url: URL });
  await blocker.execute('PRAGMA busy_timeout = 0');
  const held = await blocker.transaction('write');
  await held.execute("update ho_jobs set error='holding the write lock' where id=1");
  setTimeout(() => { held.commit().catch(() => {}); }, 700);        // released mid-retry
  const outcome = await store.decideEscalation(eid, 'aborted', 'tester');
  check('a decision landing during a write lock is still recorded', outcome === 'applied');
  blocker.close(); boot2.close();

  await store.close();
  for (const sfx of ['', '-wal', '-shm']) rmSync(`${DB_PATH}${sfx}`, { force: true });
  console.log(`\ncallback.test: ${pass} passed, ${fail} failed`);
  if (fail) process.exit(1);
}
main().catch((e) => { console.error(e); process.exit(1); });
