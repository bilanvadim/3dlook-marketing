/**
 * Write-contention test.
 *
 * REGRESSION GUARD for a fix that made things worse. SQLITE_BUSY in the worker loop looked like
 * "the writer isn't patient enough", so busy_timeout was raised to 30s. The local libSQL driver
 * is SYNCHRONOUS: while it sits out that timeout it blocks the whole Node event loop. The errors
 * disappeared and the conductor froze instead — the escalation webhook never reached listen(),
 * and every heartbeat stalled with it.
 *
 * So there are two things to prove, and the first one is the one that bites:
 *   1. waiting for a lock must NOT freeze the event loop, and
 *   2. a contended write must still eventually succeed.
 */
import { rmSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createClient } from './_client';
import { Store } from '../src/core/store';

const HERE = dirname(fileURLToPath(import.meta.url));
const DB_PATH = join(HERE, `.contention-test-${process.pid}.db`);
const URL = `file:${DB_PATH}`;

let pass = 0, fail = 0;
function check(name: string, cond: boolean) {
  if (cond) { pass++; console.log(`  ok  ${name}`); }
  else { fail++; console.log(`  FAIL ${name}`); }
}

async function main() {
  const boot = createClient({ url: URL });
  // WAL, exactly as conductor-run.sh sets up the real ho.db. It is not a detail: in the default
  // rollback-journal mode a writer's COMMIT needs an EXCLUSIVE lock and any concurrent reader
  // blocks it, so the *blocker* in this test could not commit and the lock was never released —
  // the test failed for a reason production does not have.
  await boot.execute('PRAGMA journal_mode = WAL');
  await boot.executeMultiple(`
    create table if not exists ho_jobs (
      id integer primary key autoincrement, kind text, title text, prompt text,
      priority integer not null default 5, status text not null default 'queued',
      max_turns integer, max_wall_secs integer,
      permission_mode text default 'acceptEdits', work_dir text not null default '.',
      resume_session_id text, attempts integer not null default 0,
      profile text not null default 'dev',
      created_at text not null default (datetime('now')), not_before text,
      claimed_by text, claimed_at text, finished_at text, result_summary text, error text
    );
  `);
  await boot.execute("insert into ho_jobs(kind,title,prompt) values('fix','contended','p')");
  boot.close();

  const store = new Store(URL);
  // An UNRELATED writer holds the write lock — stands in for a sibling worker or the ingest
  // bridge mid-transaction.
  const blocker = createClient({ url: URL });
  await blocker.execute('PRAGMA busy_timeout = 0');
  const held = await blocker.transaction('write');
  await held.execute("insert into ho_jobs(kind,title,prompt) values('fix','blocker','p')");

  // Release the lock shortly — well inside the retry ladder, well past the in-driver wait.
  const HOLD_MS = 900;
  setTimeout(() => { held.commit().catch(() => {}); }, HOLD_MS);

  // THE POINT: count timer ticks while the claim waits. A frozen event loop scores ~0.
  let ticks = 0;
  const iv = setInterval(() => { ticks++; }, 50);
  const t0 = Date.now();
  const job = await store.claimJob('ho-contention-test', 5).catch((e) => {
    console.log(`  (claimJob threw: ${String(e).slice(0, 80)})`);
    return null;
  });
  const waited = Date.now() - t0;
  clearInterval(iv);

  check(`the claim waited for the lock rather than failing instantly (${waited}ms)`, waited >= HOLD_MS * 0.5);
  check(`the event loop kept running while waiting (${ticks} ticks in ${waited}ms)`, ticks >= 5);
  check('the contended claim eventually succeeded', job !== null);

  blocker.close();
  await store.close();
  for (const suffix of ['', '-wal', '-shm']) rmSync(`${DB_PATH}${suffix}`, { force: true });

  console.log(`\ncontention.test: ${pass} passed, ${fail} failed`);
  if (fail) process.exit(1);
}

main().catch((e) => { console.error(e); process.exit(1); });
