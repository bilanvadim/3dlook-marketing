/**
 * Connection-leak guard for the write path.
 *
 * THE INCIDENT (2026-08-14). The conductor sat on an EMPTY queue for 24 hours and grew to
 * 33 021 open connections to ho.db — 66 081 file descriptors, 5.4 GB of anonymous RSS and 1.3 GB
 * of swap. It never ran a job; polling alone did that. On a 15 GB box shared with a second
 * account it meant swap thrashing for everyone: a neighbouring service's watchdog thread was
 * starved so badly it needed 24 minutes to reach its own os._exit(), and the kernel OOM-killer
 * fired.
 *
 * THE CAUSE. `client.transaction()` in @libsql/client's local driver handed its connection to the
 * transaction object and dropped its own reference, and neither commit(), rollback() nor close()
 * ever called db.close(). One orphan per transaction — ~170 KB of native page cache and two fds
 * each, invisible to V8, so no heap limit bounded it and GC had no reason to collect it.
 *
 * THE FIX WAS TO LEAVE THAT DRIVER. store.ts now uses better-sqlite3, which has no such handoff:
 * one Store owns one connection for its whole life, and transactions run on it. This test is what
 * keeps that true — it does not care which driver is underneath, only that N transactions cost 0
 * file descriptors.
 *
 * The control run at the end is what stops the test passing vacuously: it deliberately leaks
 * connections and asserts the counter noticed. If that ever fails, this file has stopped
 * measuring anything and its green result means nothing.
 */
import Database from 'better-sqlite3';
import { readFileSync, readdirSync, rmSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { Store } from '../src/core/store';

const HERE = dirname(fileURLToPath(import.meta.url));
const DB_PATH = join(HERE, `.fdleak-test-${process.pid}.db`);
const URL = `file:${DB_PATH}`;
/** Enough iterations that a per-transaction fd leak is unmistakable, still under a second. */
const ROUNDS = 200;
/** Native memory moves in far smaller steps than a file descriptor, so it needs a longer run. */
const RSS_ROUNDS = 20000;

let pass = 0, fail = 0;
function check(name: string, cond: boolean) {
  if (cond) { pass++; console.log(`  ok  ${name}`); }
  else { fail++; console.log(`  FAIL ${name}`); }
}

/** Live fd count for this process. Linux-only, which is where the conductor runs. */
function fds(): number {
  return readdirSync('/proc/self/fd').length;
}

async function main() {
  if (!process.platform.startsWith('linux')) {
    console.log('fdleak.test: skipped — needs /proc/self/fd');
    return;
  }

  const schema = readFileSync(join(HERE, '..', 'sql', 'schema.sql'), 'utf8');
  const boot = new Database(DB_PATH);
  boot.exec(schema);
  boot.close();

  const store = new Store(URL);
  // Warm up first: the first call settles WAL and the connection itself, and those fds are setup,
  // not leakage. The baseline has to be taken after they exist.
  await store.claimJob('fdleak-warmup');
  const before = fds();

  // The exact production shape: claim against an empty queue. Every round still opens a write
  // transaction and commits it — this is the loop that burned 5.4 GB doing nothing.
  for (let i = 0; i < ROUNDS; i++) {
    const claimed = await store.claimJob('fdleak-probe');
    if (claimed !== null) throw new Error('queue was supposed to be empty');
  }
  const after = fds();

  // A per-transaction leak shows up as ~2 fds per round (the db and its -wal). A couple of fds of
  // slack is generous; anything proportional to ROUNDS does not fit under it.
  check(`${ROUNDS} write transactions did not leak connections (fds ${before} → ${after})`, after - before <= 4);

  const step = await store.nextStep(1);
  check('nextStep on an empty plan still returns null', step === null);
  check(`nextStep/recoverStale did not leak either (fds ${fds()})`, fds() - before <= 4);

  // Second leak, same family, that the fd counter cannot see: `prepare()` allocates a native
  // statement which only a GC pass reclaims, and V8 does not know it is expensive. Preparing per
  // call measured +202 MB over 59 000 calls with nothing given back; the same calls through a
  // cached statement measured +0. The store caches, and this is what keeps it caching.
  const rssBefore = process.memoryUsage.rss();
  for (let i = 0; i < RSS_ROUNDS; i++) await store.claimJob('fdleak-rss');
  const grewMb = Math.round((process.memoryUsage.rss() - rssBefore) / 1024 / 1024);
  // A regression costs ~2.7 KB per transaction, i.e. ~54 MB at this count. The threshold sits
  // far below that and far above the noise of a loop that allocates nothing per round.
  check(`${RSS_ROUNDS} transactions did not grow native memory (+${grewMb} MB)`, grewMb < 30);

  await store.close();
  check('closing the store gives its fds back', fds() < before);

  // Control: leak on purpose, and confirm the counter sees it. Two fds per connection — the file
  // and its -wal — which is exactly the shape the incident had.
  const leaked: Database.Database[] = [];
  const rawBefore = fds();
  for (let i = 0; i < ROUNDS; i++) {
    const db = new Database(DB_PATH);
    db.prepare('select count(*) as n from ho_jobs').get();
    leaked.push(db);
  }
  const rawGrew = fds() - rawBefore;
  check(`control: ${ROUNDS} unclosed connections were detected (+${rawGrew} fds)`, rawGrew >= ROUNDS);
  if (rawGrew < ROUNDS) {
    console.log('  → the fd counter stopped measuring anything; a green run above proves nothing.');
  }
  for (const db of leaked) db.close();

  for (const suffix of ['', '-wal', '-shm']) rmSync(`${DB_PATH}${suffix}`, { force: true });

  console.log(`\nfdleak.test: ${pass} passed, ${fail} failed`);
  if (fail) process.exit(1);
}

main().catch((e) => { console.error(e); process.exit(1); });
