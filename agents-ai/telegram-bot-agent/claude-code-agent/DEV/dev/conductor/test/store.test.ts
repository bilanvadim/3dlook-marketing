/**
 * Store smoke test — exercises the real libSQL Store against a throwaway file DB.
 * Covers the logic that moved OUT of Postgres stored procedures into store.ts:
 * atomic job claim, dependency-aware nextStep, stale recovery, questions, escalations.
 */
import { readFileSync, rmSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createClient } from './_client';
import { Store } from '../src/core/store';

const HERE = dirname(fileURLToPath(import.meta.url));
const DB_PATH = join(HERE, `.store-test-${process.pid}.db`);
const URL = `file:${DB_PATH}`;

let pass = 0, fail = 0;
function check(name: string, cond: boolean) {
  if (cond) { pass++; console.log(`  ok  ${name}`); }
  else { fail++; console.log(`  FAIL ${name}`); }
}

async function main() {
  // fresh schema
  const schema = readFileSync(join(HERE, '..', 'sql', 'schema.sql'), 'utf8');
  const boot = createClient({ url: URL });
  await boot.executeMultiple(schema);
  boot.close();

  const store = new Store(URL);
  const raw = createClient({ url: URL });

  // seed a job
  await raw.execute({
    sql: "insert into ho_jobs(kind,title,prompt,profile,work_dir) values('feature','t','p','marketing_vb_sm','/tmp')",
    args: [],
  });

  // claim
  const j = await store.claimJob('ho-test');
  check('claimJob returns the job', !!j && j.title === 't');
  check('claimJob carries profile', j?.profile === 'marketing_vb_sm');
  check('claim is idempotent-safe (nothing left to claim)', (await store.claimJob('ho-test')) === null);

  const jobId = j!.id;

  // steps with a dependency: step 2 depends on step 1
  await store.insertSteps(jobId, [
    { step_no: 1, title: 's1', agent: 'backend-engineer', tags: ['backend'], depends_on: [] },
    { step_no: 2, title: 's2', depends_on: [1] },
  ]);
  check('hasSteps true', await store.hasSteps(jobId));

  const s1 = await store.nextStep(jobId);
  check('nextStep picks step 1 first (dep blocks step 2)', s1?.step_no === 1);
  check('nextStep parses tags JSON', Array.isArray(s1?.tags) && s1?.tags[0] === 'backend');

  // step 2 must NOT be runnable until step 1 is done
  const blocked = await store.nextStep(jobId);
  check('nextStep withholds step 2 while dep unfinished', blocked === null);

  await store.finishStep(s1!.id, { status: 'done', score: 90 });
  const s2 = await store.nextStep(jobId);
  check('nextStep releases step 2 after dep done', s2?.step_no === 2);

  // questions
  await store.askQuestions(jobId, null, [{ seq: 1, question: 'q1?' }]);
  const open = await store.openQuestions(jobId);
  check('openQuestions returns the asked one', open.length === 1 && open[0].question === 'q1?');
  await store.answerQuestion(open[0].id, 'a1');
  check('answerQuestion clears it', (await store.openQuestions(jobId)).length === 0);
  // The half of the feature that was missing: askQuestions parks the job in
  // 'awaiting-input' and nothing used to bring it back, so a job that ever asked
  // a question could never run again.
  check('answering the last question releases the job',
    (await store.projectStatus(jobId))?.job_status === 'queued');

  // escalation round-trip
  const runId = await store.startRun(jobId);
  const escId = await store.openEscalation(runId, jobId, 'ask_gate', 'deploy?', { cmd: 'vercel deploy' });
  const st = await store.waitEscalation(escId, { timeoutMs: 100, pollMs: 20 });
  check('waitEscalation returns the timeout sentinel when undecided', st === 'timeout');
  // It must NOT mark the row expired: handleCallback only writes `where status='open'`, so an
  // expired row makes the Telegram buttons silently dead while the job is already gone.
  const stillOpen = await raw.execute({ sql: 'select status from ho_escalations where id=?', args: [escId] });
  check('waitEscalation leaves the row OPEN so a late button tap still lands',
        String(stillOpen.rows[0].status) === 'open');

  // reminders fire while nobody answers — silence reads as a dead conductor
  let reminders = 0;
  await store.waitEscalation(escId, { timeoutMs: 260, pollMs: 20, onReminder: async () => { reminders++; }, remindMs: 50 });
  check('waitEscalation nudges via onReminder while waiting', reminders >= 2);

  // the heartbeat must keep beating while a human thinks, or recoverStale requeues a job
  // that is merely waiting on an approval — a live worker recovered out from under itself
  await raw.execute({ sql: "update ho_jobs set status='escalated', claimed_at=datetime('now','-1 hour') where id=?", args: [jobId] });
  await store.waitEscalation(escId, { jobId, timeoutMs: 60, pollMs: 20 });
  const beat = await raw.execute({
    sql: "select (claimed_at > datetime('now','-30 seconds')) as fresh from ho_jobs where id=?", args: [jobId] });
  check('waitEscalation heartbeats the job while the human is away', Number(beat.rows[0].fresh) === 1);

  // a decision recorded mid-wait is picked up
  await raw.execute({ sql: "update ho_escalations set status='approved' where id=?", args: [escId] });
  check('waitEscalation returns the recorded decision',
        (await store.waitEscalation(escId, { timeoutMs: 100, pollMs: 20 })) === 'approved');
  await raw.execute({ sql: "update ho_jobs set status='running' where id=?", args: [jobId] });

  // project status surface
  const ps = await store.projectStatus(jobId);
  check('projectStatus reports 2 total steps', ps?.total_steps === 2);
  check('projectStatus reports 1 done step', ps?.done_steps === 1);
  check('projectStatus percent = 50', ps?.percent === 50);

  // stale recovery: force a running job old, then recover
  await raw.execute({ sql: "update ho_jobs set status='running', claimed_at=datetime('now','-1 hour') where id=?", args: [jobId] });
  const n = await store.recoverStale(900);
  check('recoverStale requeues the crashed job', n === 1);

  // ---- noProgressPauseStreak: drives the rate-limit backoff ladder in conductor.ts ----
  // Regression guard for the 2026-07-27 loop (job 30: 193 zero-turn paused runs in 3h22m).
  await raw.execute({
    sql: "insert into ho_jobs(kind,title,prompt,profile,work_dir) values('feature','streak','p','marketing','/tmp')",
    args: [],
  });
  const streakJob = Number((await raw.execute('select max(id) as id from ho_jobs')).rows[0].id as number);
  const addRun = async (status: string, stop: string | null, turns: number): Promise<number> => {
    const r = await raw.execute({
      sql: 'insert into ho_runs(job_id,attempt,status,stop_reason,turns) values(?,1,?,?,?)',
      args: [streakJob, status, stop, turns],
    });
    return Number(r.lastInsertRowid);
  };

  check('streak is 0 with no history', (await store.noProgressPauseStreak(streakJob, 1)) === 0);

  await addRun('paused', 'ratelimit', 0);   // older — must NOT be counted…
  await addRun('paused', 'ratelimit', 13);  // …because this run made progress, breaking the streak
  await addRun('paused', 'ratelimit', 0);
  await addRun('paused', 'ratelimit', 0);
  const cursor = await addRun('running', null, 0);
  check('streak counts only the trailing zero-turn pauses',
        (await store.noProgressPauseStreak(streakJob, cursor)) === 2);

  await addRun('done', 'completed', 5);
  const afterSuccess = await addRun('running', null, 0);
  check('streak resets after a run that succeeded',
        (await store.noProgressPauseStreak(streakJob, afterSuccess)) === 0);

  await addRun('failed', 'error', 0);
  const afterError = await addRun('running', null, 0);
  check('a non-ratelimit failure does not extend the streak',
        (await store.noProgressPauseStreak(streakJob, afterError)) === 0);

  // ---- globalNoProgressPauseStreak: a usage window is an ACCOUNT resource ----
  // 2026-07-28: job 35 proved the window was shut, then job 36 was claimed and restarted its
  // ladder from 56s, burning five more attempts. The global streak carries that knowledge over.
  await raw.execute({
    sql: "insert into ho_jobs(kind,title,prompt,profile,work_dir) values('feature','other','p','marketing','/tmp')",
    args: [],
  });
  const otherJob = Number((await raw.execute('select max(id) as id from ho_jobs')).rows[0].id as number);
  const addRunFor = async (job: number, status: string, stop: string | null, turns: number): Promise<number> => {
    const r = await raw.execute({
      sql: 'insert into ho_runs(job_id,attempt,status,stop_reason,turns) values(?,1,?,?,?)',
      args: [job, status, stop, turns],
    });
    return Number(r.lastInsertRowid);
  };
  await addRunFor(streakJob, 'paused', 'ratelimit', 0);
  await addRunFor(streakJob, 'paused', 'ratelimit', 0);
  await addRunFor(streakJob, 'paused', 'ratelimit', 0);
  const freshCursor = await addRunFor(otherJob, 'running', null, 0);
  check('a freshly claimed job sees a per-job streak of 0',
        (await store.noProgressPauseStreak(otherJob, freshCursor)) === 0);
  check('…but inherits the account-wide streak of 3',
        (await store.globalNoProgressPauseStreak(freshCursor)) === 3);

  await addRunFor(otherJob, 'done', 'completed', 12);
  const afterGlobalProgress = await addRunFor(otherJob, 'running', null, 0);
  check('any run that made progress clears the global streak',
        (await store.globalNoProgressPauseStreak(afterGlobalProgress)) === 0);

  // ---- progress threshold: "any turn at all" is NOT proof the window opened ----
  // 2026-07-28 job 41: each retry pushed 2–5 turns through before the limit bit again, which under
  // the old turns>0 rule reset the streak every time — backoff pinned at ~50s and a Telegram
  // message on every pause. A couple of turns is the run-up to the same wall, not progress.
  await raw.execute({
    sql: "insert into ho_jobs(kind,title,prompt,profile,work_dir) values('feature','partial','p','marketing','/tmp')",
    args: [],
  });
  const partialJob = Number((await raw.execute('select max(id) as id from ho_jobs')).rows[0].id as number);
  await addRunFor(partialJob, 'paused', 'ratelimit', 0);
  await addRunFor(partialJob, 'paused', 'ratelimit', 2);
  await addRunFor(partialJob, 'paused', 'ratelimit', 5);
  const partialCursor = await addRunFor(partialJob, 'running', null, 0);
  check('threshold 1 (old behaviour): the trailing 5-turn pause zeroes the streak',
        (await store.noProgressPauseStreak(partialJob, partialCursor, 1)) === 0);
  check('threshold 10: partial-progress pauses keep the streak climbing',
        (await store.noProgressPauseStreak(partialJob, partialCursor, 10)) === 3);

  await addRunFor(partialJob, 'paused', 'ratelimit', 40);
  const realProgressCursor = await addRunFor(partialJob, 'running', null, 0);
  check('threshold 10: a genuinely productive run still resets the streak',
        (await store.noProgressPauseStreak(partialJob, realProgressCursor, 10)) === 0);

  // ---- ratelimitPauseCount: drives "is this the first pause worth announcing" ----
  check('ratelimitPauseCount is 0 before a job has ever paused',
        (await store.ratelimitPauseCount(otherJob, 1)) === 0);
  check('ratelimitPauseCount counts this job\'s rate-limit pauses only',
        (await store.ratelimitPauseCount(partialJob, realProgressCursor)) === 4);

  // ---- awaitHumanStreak: bounds the ask → park → ask cycle ----
  await addRunFor(streakJob, 'paused', 'await_human', 0);
  await addRunFor(streakJob, 'paused', 'await_human', 7);   // turns must NOT reset this one
  const parkCursor = await addRunFor(streakJob, 'running', null, 0);
  check('awaitHumanStreak counts parks regardless of turns made',
        (await store.awaitHumanStreak(streakJob, parkCursor)) === 2);
  check('awaitHumanStreak ignores rate-limit pauses',
        (await store.awaitHumanStreak(otherJob, afterGlobalProgress)) === 0);

  raw.close();
  await store.close();
  rmSync(DB_PATH, { force: true });
  rmSync(`${DB_PATH}-wal`, { force: true });
  rmSync(`${DB_PATH}-shm`, { force: true });

  console.log(`\nstore.test: ${pass} passed, ${fail} failed`);
  if (fail) process.exit(1);
}

main().catch((e) => { console.error(e); process.exit(1); });
