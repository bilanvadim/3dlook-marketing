/**
 * Fullstack agents Conductor — Postgres state access (direct `pg`, no Supabase layer).
 *
 * Talks straight to PostgreSQL via a connection pool — no PostgREST / Supabase client.
 * The DB engine is plain Postgres (the hc_* schema in schema.sql). Point DATABASE_URL at
 * any Postgres (a dedicated container, or the existing self-hosted instance).
 *
 * Minimal by design: queue + runs (session_id for DURABLE RESUME) + escalations + steps +
 * interview questions. No cost ledger / event audit (cost not tracked; loops caught in-memory).
 */
import pg from 'pg';

const { Pool, types } = pg;
// bigint (int8, oid 20) → JS number (our ids/counts fit well within Number.MAX_SAFE_INTEGER)
types.setTypeParser(20, (v: string | null) => (v === null ? null : Number(v)));

export interface Job {
  id: number; kind: string; title: string; prompt: string; priority: number;
  status: string; max_turns: number | null; max_wall_secs: number | null;
  permission_mode: string; work_dir: string;
  resume_session_id: string | null;   // set → resume an earlier SDK session instead of starting fresh
  attempts: number;
  profile: string;                     // which Claude Code system to run under: dev|seo|marketing|security
}

// ---- steps, questions, status surfaces ----
export interface PlanStepInput {
  step_no: number; title: string; agent?: string; tags?: string[]; description?: string;
  acceptance?: unknown; quality_bar?: unknown; depends_on?: number[];
}
export interface Step {
  id: number; job_id: number; step_no: number; title: string; agent: string | null;
  tags: string[]; description: string | null; acceptance: unknown; quality_bar: unknown;
  depends_on: number[]; status: string; attempts: number; score: number | null;
}
export interface Question {
  id: number; job_id: number; step_no: number | null; seq: number; layer: string | null;
  question: string; answer: string | null; status: string;
}
export interface ProjectStatus {
  job_id: number; title: string; kind: string; job_status: string;
  total_steps: number; done_steps: number; percent: number;
  open_questions: number; open_escalations: number; last_activity: string;
}

export class Store {
  private pool: pg.Pool;
  constructor(connectionString = process.env.DATABASE_URL) {
    if (!connectionString) throw new Error('DATABASE_URL required (postgres connection string)');
    this.pool = new Pool({ connectionString, max: Number(process.env.HC_PG_POOL ?? 4) });
  }

  private async q<T = any>(text: string, params: unknown[] = []): Promise<T[]> {
    const res = await this.pool.query(text, params as any[]);
    return res.rows as T[];
  }

  async close(): Promise<void> { await this.pool.end(); }

  /** Atomically claim the next pickable job (FOR UPDATE SKIP LOCKED inside the function). */
  async claimJob(worker: string): Promise<Job | null> {
    const rows = await this.q<Job>('select * from hc_claim_job($1)', [worker]);
    const j = rows[0];
    return j && j.id != null ? j : null;
  }

  /** Requeue jobs whose worker died mid-run, carrying their session_id so they resume. */
  async recoverStale(staleSecs: number): Promise<number> {
    const rows = await this.q<{ n: number }>('select hc_recover_stale($1) as n', [staleSecs]);
    return Number(rows[0]?.n ?? 0);
  }

  async startRun(jobId: number, attempt = 1): Promise<number> {
    await this.q("update hc_jobs set status='running', error=null where id=$1", [jobId]);
    const rows = await this.q<{ id: number }>('insert into hc_runs(job_id, attempt) values($1,$2) returning id', [jobId, attempt]);
    return rows[0].id;
  }

  /** Persist the SDK session id on BOTH the run and the job, so resume survives a crash. */
  async setSession(runId: number, jobId: number, sessionId: string): Promise<void> {
    await this.q('update hc_runs set session_id=$1 where id=$2', [sessionId, runId]);
    await this.q('update hc_jobs set resume_session_id=$1 where id=$2', [sessionId, jobId]);
  }

  async finishRun(runId: number, status: string, stopReason: string, turns: number, error?: string): Promise<void> {
    await this.q(
      'update hc_runs set status=$1, stop_reason=$2, turns=$3, error=$4, ended_at=now() where id=$5',
      [status, stopReason, turns, error ?? null, runId],
    );
  }

  async finishJob(jobId: number, status: string, summary?: string, error?: string): Promise<void> {
    await this.q(
      'update hc_jobs set status=$1, result_summary=$2, error=$3, resume_session_id=null, finished_at=now() where id=$4',
      [status, summary ?? null, error ?? null, jobId],
    );
  }

  /** Pause a job for `backoffSecs` (can be hours) but KEEP its resume_session_id. */
  async deferJob(jobId: number, backoffSecs: number): Promise<void> {
    await this.q(
      "update hc_jobs set status='deferred', not_before = now() + make_interval(secs => $2), claimed_by=null where id=$1",
      [jobId, backoffSecs],
    );
  }

  async openEscalation(runId: number, jobId: number, reason: string, question: string, context: unknown): Promise<number> {
    await this.q("update hc_jobs set status='escalated' where id=$1", [jobId]);
    const rows = await this.q<{ id: number }>(
      'insert into hc_escalations(run_id, job_id, reason, question, context) values($1,$2,$3,$4,$5::jsonb) returning id',
      [runId, jobId, reason, question, JSON.stringify(context ?? null)],
    );
    return rows[0].id;
  }

  /** Poll an escalation until decided or timeout (ms). Returns final status. */
  async waitEscalation(id: number, timeoutMs = 1000 * 60 * 30, pollMs = 5000): Promise<string> {
    const deadline = Date.now() + timeoutMs;
    for (;;) {
      const rows = await this.q<{ status: string }>('select status from hc_escalations where id=$1', [id]);
      const st = rows[0]?.status ?? 'open';
      if (st !== 'open') return st;
      if (Date.now() > deadline) {
        await this.q("update hc_escalations set status='expired' where id=$1", [id]);
        return 'expired';
      }
      await new Promise((r) => setTimeout(r, pollMs));
    }
  }

  // ---------- steps ----------
  async hasSteps(jobId: number): Promise<boolean> {
    const rows = await this.q<{ n: number }>('select count(*)::int as n from hc_steps where job_id=$1', [jobId]);
    return (rows[0]?.n ?? 0) > 0;
  }

  async insertSteps(jobId: number, steps: PlanStepInput[]): Promise<void> {
    for (const s of steps) {
      await this.q(
        `insert into hc_steps(job_id, step_no, title, agent, tags, description, acceptance, quality_bar, depends_on)
         values($1,$2,$3,$4,$5,$6,$7::jsonb,$8::jsonb,$9)`,
        [jobId, s.step_no, s.title, s.agent ?? null, s.tags ?? [], s.description ?? null,
         JSON.stringify(s.acceptance ?? []), JSON.stringify(s.quality_bar ?? null), s.depends_on ?? []],
      );
    }
  }

  /** Atomically claim the next runnable step (deps done). Returns null when none ready. */
  async nextStep(jobId: number): Promise<Step | null> {
    const rows = await this.q<Step>('select * from hc_next_step($1)', [jobId]);
    const s = rows[0];
    return s && s.id != null ? s : null;
  }

  async recordAttempt(stepId: number): Promise<void> {
    await this.q('update hc_steps set attempts=attempts+1, updated_at=now() where id=$1', [stepId]);
  }

  async setStepStatus(stepId: number, status: string): Promise<void> {
    await this.q('update hc_steps set status=$1, updated_at=now() where id=$2', [status, stepId]);
  }

  async finishStep(stepId: number, f: { status: string; score?: number; reviewer_report?: unknown; runtime_report?: unknown; error?: string }): Promise<void> {
    await this.q(
      `update hc_steps set status=$1, score=$2, reviewer_report=$3::jsonb, runtime_report=$4::jsonb, error=$5, updated_at=now() where id=$6`,
      [f.status, f.score ?? null,
       f.reviewer_report === undefined ? null : JSON.stringify(f.reviewer_report),
       f.runtime_report === undefined ? null : JSON.stringify(f.runtime_report),
       f.error ?? null, stepId],
    );
  }

  // ---------- interview questions ----------
  async askQuestions(jobId: number, stepNo: number | null, questions: { seq: number; layer?: string; question: string }[]): Promise<void> {
    for (const qq of questions) {
      await this.q(
        'insert into hc_questions(job_id, step_no, seq, layer, question) values($1,$2,$3,$4,$5)',
        [jobId, stepNo, qq.seq, qq.layer ?? null, qq.question],
      );
    }
    await this.setJobStatus(jobId, 'awaiting-input');
  }

  async openQuestions(jobId: number): Promise<Question[]> {
    return this.q<Question>("select * from hc_questions where job_id=$1 and status='open' order by seq", [jobId]);
  }

  async answerQuestion(qid: number, answer: string): Promise<void> {
    await this.q('select hc_answer_question($1,$2)', [qid, answer]);
  }

  async setJobStatus(jobId: number, status: string): Promise<void> {
    await this.q('update hc_jobs set status=$1 where id=$2', [status, jobId]);
  }

  // ---------- status surface (Hermes reads this) ----------
  async projectStatus(jobId: number): Promise<ProjectStatus | null> {
    const rows = await this.q<any>('select * from hc_project_status where job_id=$1', [jobId]);
    const r = rows[0];
    if (!r) return null;
    return {
      job_id: Number(r.job_id), title: r.title, kind: r.kind, job_status: r.job_status,
      total_steps: Number(r.total_steps), done_steps: Number(r.done_steps), percent: Number(r.percent),
      open_questions: Number(r.open_questions), open_escalations: Number(r.open_escalations),
      last_activity: r.last_activity,
    };
  }
}
