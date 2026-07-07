/**
 * Hermes Orchestrator — orchestrator state access (SQLite / libSQL via @libsql/client).
 *
 * DATABASE_URL selects the backend with ONE code path:
 *   file:./ho.db            local single-file SQLite (default, zero infra)
 *   libsql://<host>[?authToken=…] / http://…  a libSQL server or Turso Cloud
 * SQLite is single-writer, so the claim/next-step/recover logic runs inside a
 * write transaction and is race-free by construction — no FOR UPDATE SKIP LOCKED,
 * no stored procedures (those lived in the old Postgres schema).
 *
 * Minimal by design: queue + runs (session_id for DURABLE RESUME) + escalations +
 * steps + interview questions. No cost ledger (cost not tracked; loops caught in-memory).
 * Array/JSON columns (tags, depends_on, acceptance, quality_bar, *_report, context)
 * are stored as JSON TEXT and (de)serialized here.
 */
import { createClient, type Client, type InArgs, type Row } from '@libsql/client';

export interface Job {
  id: number; kind: string; title: string; prompt: string; priority: number;
  status: string; max_turns: number | null; max_wall_secs: number | null;
  permission_mode: string; work_dir: string;
  resume_session_id: string | null;   // set → resume an earlier SDK session instead of starting fresh
  attempts: number;
  profile: string;                     // Claude Code system: dev|seo|marketing|security|marketing_vb|marketing_vb_sm
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

const num = (v: unknown): number | null => (v == null ? null : Number(v));
const parseJson = <T>(v: unknown, fallback: T): T => {
  if (v == null) return fallback;
  try { return JSON.parse(String(v)) as T; } catch { return fallback; }
};

function mapJob(r: Row): Job {
  return {
    id: Number(r.id), kind: String(r.kind), title: String(r.title), prompt: String(r.prompt),
    priority: Number(r.priority), status: String(r.status),
    max_turns: num(r.max_turns), max_wall_secs: num(r.max_wall_secs),
    permission_mode: String(r.permission_mode), work_dir: String(r.work_dir),
    resume_session_id: (r.resume_session_id as string | null) ?? null,
    attempts: Number(r.attempts), profile: String(r.profile ?? 'dev'),
  };
}
function mapStep(r: Row): Step {
  return {
    id: Number(r.id), job_id: Number(r.job_id), step_no: Number(r.step_no), title: String(r.title),
    agent: (r.agent as string | null) ?? null,
    tags: parseJson<string[]>(r.tags, []), description: (r.description as string | null) ?? null,
    acceptance: parseJson<unknown>(r.acceptance, []), quality_bar: parseJson<unknown>(r.quality_bar, null),
    depends_on: parseJson<number[]>(r.depends_on, []), status: String(r.status),
    attempts: Number(r.attempts), score: num(r.score),
  };
}

export class Store {
  private db: Client;
  constructor(url = process.env.DATABASE_URL) {
    if (!url) throw new Error('DATABASE_URL required (e.g. file:./ho.db or libsql://…)');
    this.db = createClient({ url });
  }

  private async q<T = any>(sql: string, args: InArgs = []): Promise<T[]> {
    const res = await this.db.execute({ sql, args });
    return res.rows as unknown as T[];
  }

  async close(): Promise<void> { this.db.close(); }

  /** Atomically claim the next pickable job. Single-writer tx replaces FOR UPDATE SKIP LOCKED. */
  async claimJob(worker: string): Promise<Job | null> {
    const tx = await this.db.transaction('write');
    try {
      const sel = await tx.execute({
        sql: `select * from ho_jobs
                where status in ('queued','deferred')
                  and (not_before is null or not_before <= datetime('now'))
                order by priority, created_at limit 1`,
        args: [],
      });
      const row = sel.rows[0];
      if (!row) { await tx.rollback(); return null; }
      await tx.execute({
        sql: `update ho_jobs set status='claimed', claimed_by=?, claimed_at=datetime('now') where id=?`,
        args: [worker, row.id as number],
      });
      const after = await tx.execute({ sql: 'select * from ho_jobs where id=?', args: [row.id as number] });
      await tx.commit();
      return mapJob(after.rows[0]);
    } catch (e) { await tx.rollback(); throw e; }
  }

  /** Requeue jobs whose worker died mid-run, carrying their session_id so they resume. */
  async recoverStale(staleSecs: number): Promise<number> {
    const tx = await this.db.transaction('write');
    try {
      const stale = await tx.execute({
        sql: `select id from ho_jobs
                where status in ('running','claimed')
                  and coalesce(claimed_at, created_at) < datetime('now', ?)`,
        args: [`-${staleSecs} seconds`],
      });
      let n = 0;
      for (const j of stale.rows) {
        const jobId = j.id as number;
        const sidRow = await tx.execute({
          sql: 'select session_id from ho_runs where job_id=? order by id desc limit 1', args: [jobId],
        });
        const sid = (sidRow.rows[0]?.session_id as string | null) ?? null;
        await tx.execute({
          sql: `update ho_runs set status='failed', stop_reason='stale_recovered', ended_at=datetime('now')
                 where job_id=? and status in ('running','paused')`,
          args: [jobId],
        });
        await tx.execute({
          sql: `update ho_jobs
                   set status='deferred', not_before=datetime('now'), claimed_by=null,
                       resume_session_id=coalesce(?, resume_session_id), attempts=attempts+1
                 where id=?`,
          args: [sid, jobId],
        });
        n++;
      }
      await tx.commit();
      return n;
    } catch (e) { await tx.rollback(); throw e; }
  }

  async startRun(jobId: number, attempt = 1): Promise<number> {
    await this.q("update ho_jobs set status='running', error=null where id=?", [jobId]);
    const res = await this.db.execute({ sql: 'insert into ho_runs(job_id, attempt) values(?,?)', args: [jobId, attempt] });
    return Number(res.lastInsertRowid);
  }

  /** Persist the SDK session id on BOTH the run and the job, so resume survives a crash. */
  async setSession(runId: number, jobId: number, sessionId: string): Promise<void> {
    await this.q('update ho_runs set session_id=? where id=?', [sessionId, runId]);
    await this.q('update ho_jobs set resume_session_id=? where id=?', [sessionId, jobId]);
  }

  async finishRun(runId: number, status: string, stopReason: string, turns: number, error?: string): Promise<void> {
    await this.q(
      "update ho_runs set status=?, stop_reason=?, turns=?, error=?, ended_at=datetime('now') where id=?",
      [status, stopReason, turns, error ?? null, runId],
    );
  }

  async finishJob(jobId: number, status: string, summary?: string, error?: string): Promise<void> {
    await this.q(
      "update ho_jobs set status=?, result_summary=?, error=?, resume_session_id=null, finished_at=datetime('now') where id=?",
      [status, summary ?? null, error ?? null, jobId],
    );
  }

  /** Pause a job for `backoffSecs` (can be hours) but KEEP its resume_session_id. */
  async deferJob(jobId: number, backoffSecs: number): Promise<void> {
    await this.q(
      "update ho_jobs set status='deferred', not_before=datetime('now', ?), claimed_by=null where id=?",
      [`+${backoffSecs} seconds`, jobId],
    );
  }

  async openEscalation(runId: number, jobId: number, reason: string, question: string, context: unknown): Promise<number> {
    await this.q("update ho_jobs set status='escalated' where id=?", [jobId]);
    const res = await this.db.execute({
      sql: 'insert into ho_escalations(run_id, job_id, reason, question, context) values(?,?,?,?,?)',
      args: [runId, jobId, reason, question, JSON.stringify(context ?? null)],
    });
    return Number(res.lastInsertRowid);
  }

  /** Poll an escalation until decided or timeout (ms). Returns final status. */
  async waitEscalation(id: number, timeoutMs = 1000 * 60 * 30, pollMs = 5000): Promise<string> {
    const deadline = Date.now() + timeoutMs;
    for (;;) {
      const rows = await this.q<{ status: string }>('select status from ho_escalations where id=?', [id]);
      const st = rows[0]?.status ?? 'open';
      if (st !== 'open') return st;
      if (Date.now() > deadline) {
        await this.q("update ho_escalations set status='expired' where id=?", [id]);
        return 'expired';
      }
      await new Promise((r) => setTimeout(r, pollMs));
    }
  }

  // ---------- steps ----------
  async hasSteps(jobId: number): Promise<boolean> {
    const rows = await this.q<{ n: number }>('select count(*) as n from ho_steps where job_id=?', [jobId]);
    return Number(rows[0]?.n ?? 0) > 0;
  }

  async insertSteps(jobId: number, steps: PlanStepInput[]): Promise<void> {
    for (const s of steps) {
      await this.q(
        `insert into ho_steps(job_id, step_no, title, agent, tags, description, acceptance, quality_bar, depends_on)
         values(?,?,?,?,?,?,?,?,?)`,
        [jobId, s.step_no, s.title, s.agent ?? null, JSON.stringify(s.tags ?? []), s.description ?? null,
         JSON.stringify(s.acceptance ?? []), JSON.stringify(s.quality_bar ?? null), JSON.stringify(s.depends_on ?? [])],
      );
    }
  }

  /** Atomically claim the next runnable step (all deps done). Returns null when none ready. */
  async nextStep(jobId: number): Promise<Step | null> {
    const tx = await this.db.transaction('write');
    try {
      const pend = await tx.execute({
        sql: `select * from ho_steps where job_id=? and status='pending' order by step_no`,
        args: [jobId],
      });
      // find first whose dependencies are all 'done'
      let chosen: Row | null = null;
      for (const st of pend.rows) {
        const deps = parseJson<number[]>(st.depends_on, []);
        if (deps.length === 0) { chosen = st; break; }
        const q = `select count(*) as n from ho_steps
                     where job_id=? and step_no in (${deps.map(() => '?').join(',')}) and status<>'done'`;
        const undone = await tx.execute({ sql: q, args: [jobId, ...deps] });
        if (Number(undone.rows[0].n) === 0) { chosen = st; break; }
      }
      if (!chosen) { await tx.rollback(); return null; }
      await tx.execute({
        sql: `update ho_steps set status='running', attempts=attempts+1, updated_at=datetime('now') where id=?`,
        args: [chosen.id as number],
      });
      const after = await tx.execute({ sql: 'select * from ho_steps where id=?', args: [chosen.id as number] });
      await tx.commit();
      return mapStep(after.rows[0]);
    } catch (e) { await tx.rollback(); throw e; }
  }

  async recordAttempt(stepId: number): Promise<void> {
    await this.q("update ho_steps set attempts=attempts+1, updated_at=datetime('now') where id=?", [stepId]);
  }

  async setStepStatus(stepId: number, status: string): Promise<void> {
    await this.q("update ho_steps set status=?, updated_at=datetime('now') where id=?", [status, stepId]);
  }

  async finishStep(stepId: number, f: { status: string; score?: number; reviewer_report?: unknown; runtime_report?: unknown; error?: string }): Promise<void> {
    await this.q(
      `update ho_steps set status=?, score=?, reviewer_report=?, runtime_report=?, error=?, updated_at=datetime('now') where id=?`,
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
        'insert into ho_questions(job_id, step_no, seq, layer, question) values(?,?,?,?,?)',
        [jobId, stepNo, qq.seq, qq.layer ?? null, qq.question],
      );
    }
    await this.setJobStatus(jobId, 'awaiting-input');
  }

  async openQuestions(jobId: number): Promise<Question[]> {
    return this.q<Question>("select * from ho_questions where job_id=? and status='open' order by seq", [jobId]);
  }

  async answerQuestion(qid: number, answer: string): Promise<void> {
    await this.q("update ho_questions set answer=?, status='answered', answered_at=datetime('now') where id=?", [answer, qid]);
  }

  async setJobStatus(jobId: number, status: string): Promise<void> {
    await this.q('update ho_jobs set status=? where id=?', [status, jobId]);
  }

  // ---------- status surface (Hermes reads this) ----------
  async projectStatus(jobId: number): Promise<ProjectStatus | null> {
    const rows = await this.q<any>('select * from ho_project_status where job_id=?', [jobId]);
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
