/**
 * Store smoke test — exercises the real libSQL Store against a throwaway file DB.
 * Covers the logic that moved OUT of Postgres stored procedures into store.ts:
 * atomic job claim, dependency-aware nextStep, stale recovery, questions, escalations.
 */
import { readFileSync, rmSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { createClient } from '@libsql/client';
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

  // escalation round-trip
  const runId = await store.startRun(jobId);
  const escId = await store.openEscalation(runId, jobId, 'ask_gate', 'deploy?', { cmd: 'vercel deploy' });
  const st = await store.waitEscalation(escId, 100, 20); // will time out → 'expired'
  check('waitEscalation times out to expired when undecided', st === 'expired');

  // project status surface
  const ps = await store.projectStatus(jobId);
  check('projectStatus reports 2 total steps', ps?.total_steps === 2);
  check('projectStatus reports 1 done step', ps?.done_steps === 1);
  check('projectStatus percent = 50', ps?.percent === 50);

  // stale recovery: force a running job old, then recover
  await raw.execute({ sql: "update ho_jobs set status='running', claimed_at=datetime('now','-1 hour') where id=?", args: [jobId] });
  const n = await store.recoverStale(900);
  check('recoverStale requeues the crashed job', n === 1);

  raw.close();
  await store.close();
  rmSync(DB_PATH, { force: true });
  rmSync(`${DB_PATH}-wal`, { force: true });
  rmSync(`${DB_PATH}-shm`, { force: true });

  console.log(`\nstore.test: ${pass} passed, ${fail} failed`);
  if (fail) process.exit(1);
}

main().catch((e) => { console.error(e); process.exit(1); });
