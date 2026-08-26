/**
 * Liveness test.
 *
 * REGRESSION GUARD for a double-execution bug. runJobAsSteps beat ONCE per step and then blocked in
 * runStep — an SDK query plus gate() calls capped at 10 minutes each, routinely longer than
 * HO_STALE_RUN_SECS (900s). The job sits in 'verifying' throughout, recoverStale covers 'verifying',
 * so a sibling worker requeued a LIVE job and a second worker re-ran the same steps in the same
 * work_dir. Two agents, one tree.
 *
 * The property under test is the one that prevents it: while a long step runs, claimed_at keeps
 * moving, so a time-based recovery pass cannot mistake the job for abandoned.
 */
import { readFileSync, rmSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createClient } from './_client';
import { Store } from '../src/core/store';

const HERE = dirname(fileURLToPath(import.meta.url));
const DB_PATH = join(HERE, `.heartbeat-test-${process.pid}.db`);
const URL = `file:${DB_PATH}`;

let pass = 0, fail = 0;
function check(name: string, cond: boolean) {
  if (cond) { pass++; console.log(`  ok  ${name}`); }
  else { fail++; console.log(`  FAIL ${name}`); }
}

async function main() {
  const schema = readFileSync(join(HERE, '..', 'sql', 'schema.sql'), 'utf8');
  const boot = createClient({ url: URL });
  await boot.executeMultiple(schema);
  await boot.execute("insert into ho_jobs(kind,title,prompt,profile,work_dir) values('feature','beat','p','dev','/tmp')");
  boot.close();

  const store = new Store(URL);
  const raw = createClient({ url: URL });
  const job = await store.claimJob('ho-beat-test');
  const id = job!.id;

  // The state a long step leaves behind: 'verifying', and claimed_at pushed into the past.
  await store.setJobStatus(id, 'verifying');
  await raw.execute({ sql: "update ho_jobs set claimed_at=datetime('now','-1 hour') where id=?", args: [id] });

  // WITHOUT a beat, a stale sweep takes the job away from its live owner.
  check('a sibling worker recovers the job when nothing beats', (await store.recoverStale(900)) === 1);

  // Put it back in the mid-step state and beat the way runJobAsSteps now does.
  await raw.execute({ sql: "update ho_jobs set status='verifying', claimed_by='ho-beat-test', claimed_at=datetime('now','-1 hour') where id=?", args: [id] });
  const beat = setInterval(() => { store.heartbeat(id).catch(() => {}); }, 50);
  await new Promise((r) => setTimeout(r, 220));            // a "long step" elapses
  clearInterval(beat);

  const fresh = await raw.execute({
    sql: "select (claimed_at > datetime('now','-30 seconds')) as fresh from ho_jobs where id=?", args: [id] });
  check('the beat moved claimed_at back into the present', Number(fresh.rows[0].fresh) === 1);
  check('so a stale sweep now leaves the live job alone', (await store.recoverStale(900)) === 0);

  // heartbeat() must cover 'verifying' — the status a step-running job actually holds. It updates
  // only claimed/running/verifying/escalated, so a missing status here would make the interval a
  // no-op and the whole fix silent.
  await raw.execute({ sql: "update ho_jobs set status='verifying', claimed_at=datetime('now','-1 hour') where id=?", args: [id] });
  await store.heartbeat(id);
  const covered = await raw.execute({
    sql: "select (claimed_at > datetime('now','-30 seconds')) as fresh from ho_jobs where id=?", args: [id] });
  check("heartbeat() applies to a job in 'verifying'", Number(covered.rows[0].fresh) === 1);

  raw.close();
  await store.close();
  for (const sfx of ['', '-wal', '-shm']) rmSync(`${DB_PATH}${sfx}`, { force: true });
  console.log(`\nheartbeat.test: ${pass} passed, ${fail} failed`);
  if (fail) process.exit(1);
}
main().catch((e) => { console.error(e); process.exit(1); });
