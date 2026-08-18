/**
 * Hermes Orchestrator — conductor state access (SQLite via better-sqlite3).
 *
 * DATABASE_URL points at a local file, and only at a local file:
 *   file:./ho.db · file:/abs/path/ho.db · ./ho.db
 *
 * It used to accept `libsql://…` and `http://…` too, through @libsql/client, so the queue could
 * move to a libSQL server or Turso Cloud by changing one variable. That option was never used,
 * and on 2026-08-14 it cost a production outage: the driver's local mode never closed the
 * connection it handed to `transaction()`, so 24 h of polling an EMPTY queue orphaned 33 021
 * connections — 66 081 fds, 5.4 GB RSS, 1.3 GB of swap — and drove a shared 15 GB box into swap
 * thrashing until the kernel OOM-killer fired. Still unfixed upstream in 0.17.4 (see RUNBOOK).
 *
 * better-sqlite3 is the same SQLite, and barely a different API: @libsql/client's local mode was
 * itself built on a better-sqlite3-COMPATIBLE fork. What it does not have is the connection
 * handoff that leaked, nor the statement that a lost BEGIN leaves unreset — verified against the
 * same harness that reproduced both. If the queue ever does need to live on a server, that is a
 * deliberate project, not a URL change.
 *
 * SQLite is single-writer, so the claim/next-step/recover logic runs inside a
 * write transaction and is race-free by construction — no FOR UPDATE SKIP LOCKED,
 * no stored procedures (those lived in the old Postgres schema).
 *
 * Minimal by design: queue + runs (session_id for DURABLE RESUME) + escalations +
 * steps + interview questions. No cost ledger (cost not tracked; loops caught in-memory).
 * Array/JSON columns (tags, depends_on, acceptance, quality_bar, *_report, context)
 * are stored as JSON TEXT and (de)serialized here.
 *
 * The driver is SYNCHRONOUS. Every method here stays async regardless: the public shape must not
 * change under its callers, and retryBusy still has to await between attempts.
 */
import Database from 'better-sqlite3';

/** A row as SQLite hands it back: column name → value. */
type Row = Record<string, unknown>;
/** What may be bound to a `?` placeholder. */
type Arg = string | number | bigint | Buffer | null;

/**
 * DATABASE_URL → filesystem path.
 *
 * A remote URL is rejected loudly instead of being quietly taken for a filename. Silence is the
 * dangerous option here: a conductor that created `./libsql:/host.db` and then polled an empty
 * queue would look perfectly healthy while doing nothing at all.
 */
function dbPath(url: string): string {
  const scheme = /^(libsql|wss?|https?):/i.exec(url)?.[1];
  if (scheme) {
    throw new Error(
      `DATABASE_URL points at a remote server (${scheme}:) — this store is local-file only since ` +
      'the move off @libsql/client. Use file:/path/to/ho.db.',
    );
  }
  return url.replace(/^file:(\/\/)?/i, '');
}

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

/** Knobs for waitEscalation — see that method for what each one is for. */
export interface WaitEscalationOpts {
  /** Job whose heartbeat to keep beating while a human thinks. */
  jobId?: number;
  /** Give up waiting after this long and return 'timeout' (the row stays open). */
  timeoutMs?: number;
  /** How often to re-read the escalation row. */
  pollMs?: number;
  /** Called every `remindMs` while the escalation is still unanswered. */
  onReminder?: (waitedMs: number) => Promise<void>;
  remindMs?: number;
}

export class Store {
  private db: Database.Database;
  /** Attempts (including the first) for a statement that comes back SQLITE_BUSY. */
  private readonly busyRetries: number;
  /**
   * Compiled statements, keyed by their SQL. NOT merely an optimization.
   *
   * `prepare()` allocates a native statement that only a GC pass reclaims, and V8 cannot see what
   * it is holding: measured on this driver, 59 000 prepare-and-run calls grew RSS by 202 MB and
   * gave none of it back, while the same 59 000 calls through one cached statement grew it by
   * exactly 0. That is the same shape as the leak this store just moved away from — native memory
   * pinned by garbage nothing feels pressure to collect — and a 24/7 poll loop is exactly where it
   * surfaces. The transaction wrapper is free by comparison: 39 000 transactions built fresh each
   * time cost 0 KB, so only the statements needed caching.
   *
   * Bounded as a backstop, not because the bound is expected to bite: the SQL here is static apart
   * from three shapes — claimJob's attempts cap, nextStep's `in (?,…)` widening with a step's
   * dependency count, and finishStep's column list — so the live key count is a few dozen. If a
   * future caller ever builds SQL out of data, this resets rather than growing forever. A
   * recompile is cheap; an unbounded map is the thing being avoided.
   */
  private readonly stmts = new Map<string, Database.Statement>();

  constructor(url = process.env.DATABASE_URL) {
    if (!url) throw new Error('DATABASE_URL required (e.g. file:./ho.db)');
    // KEEP THIS SMALL, AND DO NOT "FIX" CONTENTION BY RAISING IT.
    //
    // The driver is SYNCHRONOUS: while it sits out a busy_timeout it blocks the whole Node event
    // loop. Measured — a 5000ms lock wait let exactly 0 timers fire in that window. So a generous
    // timeout does not buy patience, it buys a process-wide freeze: set to 30s here, the
    // escalation webhook never even reached `listen()` because the three worker loops contending
    // at startup froze the loop, and every heartbeat stalled with it.
    //
    // Correct split: a SHORT in-driver wait absorbs the millisecond-scale overlap that is the
    // common case, and anything longer is retried at the application level below, where the
    // sleep is async and the event loop keeps breathing.
    const ms = Number(process.env.HO_BUSY_TIMEOUT_MS ?? 500);
    const timeout = Number.isFinite(ms) && ms > 0 ? Math.round(ms) : 500;
    const retries = Number(process.env.HO_BUSY_RETRIES ?? 6);
    this.busyRetries = Number.isFinite(retries) && retries >= 1 ? Math.round(retries) : 6;
    // The busy timeout is a CONSTRUCTOR option now, so it is in force on the connection's very
    // first statement. Under the old async driver it was a pragma fired from the constructor and
    // awaited through a `ready` promise, because a writer that started before the pragma landed
    // met busy_timeout=0 and failed instantly instead of waiting. That whole race is gone: there
    // is no window between opening the connection and the timeout being set.
    this.db = new Database(dbPath(url), { timeout });
    // WAL, and not only because it is faster.
    //
    // In the default rollback-journal mode a writer's COMMIT needs an EXCLUSIVE lock, so any
    // concurrent READER blocks it — with several workers polling, the holder of the write lock
    // can be unable to commit while the pollers are unable to write, and nobody makes progress
    // until someone gives up. WAL removes that class of stall outright (reproduced in
    // test/contention.test.ts: identical scenario, deadlocks without WAL, passes with it).
    //
    // conductor-run.sh already sets this on the ho.db it manages, but `npm start` and every test
    // and script that constructs a Store directly bypass that script — the guarantee belongs
    // with the code that depends on it.
    try { this.db.pragma('journal_mode = WAL'); }
    catch (e) { console.warn(`store: could not enable WAL — ${String(e).slice(0, 120)}`); }
  }

  /**
   * Run a DB operation, retrying SQLITE_BUSY with an async backoff.
   *
   * This is where waiting for a lock belongs: `await sleep()` yields, so the webhook still
   * answers and other workers still make progress while this one waits. Total patience is
   * ~0.1+0.2+0.4+0.8+1.6s ≈ 3s on top of the in-driver wait per attempt — far more than the
   * few milliseconds a queue transaction actually takes, and the caller (workerLoop) already
   * survives a throw by retrying on its next poll.
   */
  private async retryBusy<T>(what: string, op: () => Promise<T>): Promise<T> {
    let delay = 100;
    for (let attempt = 1; ; attempt++) {
      try {
        return await op();
      } catch (e) {
        const busy = /SQLITE_BUSY|database is locked/i.test(String(e));
        if (!busy || attempt >= this.busyRetries) throw e;
        await new Promise((r) => setTimeout(r, Math.round(delay * (0.5 + Math.random()))));
        delay *= 2;
        if (attempt === this.busyRetries - 1) console.warn(`store: ${what} still busy after ${attempt} tries`);
      }
    }
  }

  private async q<T = any>(sql: string, args: Arg[] = []): Promise<T[]> {
    const res = await this.exec({ sql, args });
    return res.rows as unknown as T[];
  }

  /** Same gate as q(), for the callers that need the raw result (lastInsertRowid). */
  private async exec(stmt: { sql: string; args: Arg[] }) {
    return this.retryBusy(
      stmt.sql.trim().split(/\s+/).slice(0, 3).join(' '),
      async () => this.step(stmt),
    );
  }

  /**
   * One statement, in the result shape the rest of this file already expects.
   *
   * `reader` is how the driver reports whether a statement returns rows, and the split matters:
   * `.all()` throws on a statement that returns none, and `.run()` cannot report rows.
   */
  /** Compile once, reuse forever — see `stmts` for why that is not optional here. */
  private prep(sql: string): Database.Statement {
    let st = this.stmts.get(sql);
    if (!st) {
      if (this.stmts.size >= 256) this.stmts.clear();
      st = this.db.prepare(sql);
      this.stmts.set(sql, st);
    }
    return st;
  }

  private step(stmt: { sql: string; args: Arg[] }): {
    rows: Row[]; lastInsertRowid: number | bigint; rowsAffected: number;
  } {
    const st = this.prep(stmt.sql);
    if (st.reader) return { rows: st.all(...stmt.args) as Row[], lastInsertRowid: 0, rowsAffected: 0 };
    const info = st.run(...stmt.args);
    // `changes` is this driver's name for what the old one called rowsAffected. It is not
    // cosmetic: decideEscalation() tells 'applied' from 'already-decided' by nothing else.
    return { rows: [], lastInsertRowid: info.lastInsertRowid, rowsAffected: info.changes };
  }

  /** Sync helpers for transaction bodies, which are not allowed to await. */
  private one(sql: string, ...args: Arg[]): Row | undefined {
    return this.prep(sql).get(...args) as Row | undefined;
  }
  private many(sql: string, ...args: Arg[]): Row[] {
    return this.prep(sql).all(...args) as Row[];
  }
  private write(sql: string, ...args: Arg[]): void {
    this.prep(sql).run(...args);
  }

  /**
   * Run `fn` inside an IMMEDIATE write transaction.
   *
   * The body is SYNCHRONOUS, and that is the feature. It cannot await, so nothing can interleave
   * between its statements: BEGIN IMMEDIATE takes the write lock up front, the driver commits on
   * return and rolls back on throw, and there is nothing to serialize by hand.
   *
   * The previous driver forced the opposite shape — an async body on a shared connection — which
   * had to be hand-serialized against itself AND leaked a connection per call, because its
   * `transaction()` handed the connection away and never closed it. Two problems that only ever
   * existed because the transaction body was allowed to await.
   *
   * Deliberately NOT wrapped in retryBusy: the three callers wrap their WHOLE transaction
   * instead. Retrying here as well nests two ladders, multiplying the wait and making the
   * failure logs meaningless.
   */
  private inWriteTx<T>(fn: () => T): T {
    return this.db.transaction(fn).immediate();
  }

  async close(): Promise<void> { this.stmts.clear(); this.db.close(); }

  /** Atomically claim the next pickable job. Single-writer tx replaces FOR UPDATE SKIP LOCKED.
   *
   *  `maxAttempts` retires a job that keeps killing its worker. Without it a
   *  poison job cycles forever: recoverStale bumps attempts and sets
   *  not_before=now, so it is immediately pickable again, burns a full agent run,
   *  dies, repeats — and blocks the queue behind it while doing so.
   */
  async claimJob(worker: string, maxAttempts = 0): Promise<Job | null> {
    return this.retryBusy('claimJob', async () => this.inWriteTx(() => {
      const cap = maxAttempts > 0 ? 'and attempts < ?' : '';
      const row = this.one(
        `select * from ho_jobs
           where status in ('queued','deferred')
             and (not_before is null or not_before <= datetime('now'))
             ${cap}
           order by priority, created_at limit 1`,
        ...(maxAttempts > 0 ? [maxAttempts] : []),
      );
      // Nothing to claim — the common case on an idle queue. Returning commits a transaction that
      // wrote nothing, which costs no more than a rollback and leaves one exit path.
      if (!row) return null;
      this.write(
        `update ho_jobs set status='claimed', claimed_by=?, claimed_at=datetime('now') where id=?`,
        worker, row.id as number,
      );
      return mapJob(this.one('select * from ho_jobs where id=?', row.id as number) as Row);
    }));
  }

  /** Requeue jobs whose worker died mid-run, carrying their session_id so they resume. */
  async recoverStale(staleSecs: number): Promise<number> {
    return this.retryBusy('recoverStale', async () => this.inWriteTx(() => {
      // 'verifying' and 'escalated' were missing, and both are states a job can
      // sit in for a long time: setJobStatus('verifying') is set immediately
      // BEFORE runStep, the longest call in the loop, and 'escalated' spans the
      // human approval window. A worker dying in either left the job in a status
      // no recovery pass looked at — stuck forever. Both are heartbeat-covered,
      // so a live worker cannot be recovered out from under itself.
      const stale = this.many(
        `select id from ho_jobs
           where status in ('running','claimed','verifying','escalated')
             and coalesce(claimed_at, created_at) < datetime('now', ?)`,
        `-${staleSecs} seconds`,
      );
      let n = 0;
      for (const j of stale) {
        const jobId = j.id as number;
        const sidRow = this.one('select session_id from ho_runs where job_id=? order by id desc limit 1', jobId);
        const sid = (sidRow?.session_id as string | null) ?? null;
        this.write(
          `update ho_runs set status='failed', stop_reason='stale_recovered', ended_at=datetime('now')
            where job_id=? and status in ('running','paused')`,
          jobId,
        );
        // The STEP the dead worker was holding has to come back too. Recovery
        // used to touch only ho_runs and ho_jobs, so the step stayed 'running'
        // while nextStep() selects 'pending' only — that step was never picked up
        // again, everything depending on it stayed blocked, and the requeued job
        // ran straight to "no runnable step left" and closed itself as failed.
        // The work was silently lost rather than retried.
        this.write(
          `update ho_steps set status='pending', updated_at=datetime('now')
            where job_id=? and status in ('running','verifying')`,
          jobId,
        );
        this.write(
          `update ho_jobs
              set status='deferred', not_before=datetime('now'), claimed_by=null,
                  resume_session_id=coalesce(?, resume_session_id), attempts=attempts+1
            where id=?`,
          sid, jobId,
        );
        n++;
      }
      return n;
    }));
  }

  /** Bump claimed_at so a LIVE worker's long-running job isn't falsely stale-recovered
   *  by a sibling worker (recoverStale is time-based). Called while a job actively streams. */
  async heartbeat(jobId: number): Promise<void> {
    // 'escalated' belongs here as much as the rest: a job waiting on a human is
    // being tended by a LIVE worker inside waitEscalation, and recoverStale now
    // covers that status. Without a beat during the wait, a legitimate 30-minute
    // approval window would look exactly like a dead worker.
    await this.q(
      "update ho_jobs set claimed_at=datetime('now') where id=? and status in ('claimed','running','verifying','escalated')",
      [jobId],
    );
  }

  async startRun(jobId: number, attempt = 1): Promise<number> {
    await this.q("update ho_jobs set status='running', error=null where id=?", [jobId]);
    const res = await this.exec({ sql: 'insert into ho_runs(job_id, attempt) values(?,?)', args: [jobId, attempt] });
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

  /**
   * How many runs IMMEDIATELY before `beforeRunId` ended paused on a rate limit without making
   * real progress. The streak resets the moment any run got somewhere or ended for another
   * reason, so a job that is genuinely inching forward is never penalised. Feeds the pause
   * backoff ladder in conductor.ts.
   *
   * WHY: a flat backoff re-claims a limited job every ~60s. Anthropic's windows are hours long,
   * so that produced 193 zero-turn runs over 3h22m on job 30 (2026-07-27) — pure API hammering
   * with no work done, and no record of why. DB-backed so it survives a conductor restart; the
   * 50-row window is far above any sane streak.
   *
   * `progressTurns` is the number of turns a run must have made to count as REAL progress. It is
   * not 1 by accident of history: on an exhausted usage window an agent still gets a couple of
   * turns through before the limit bites, so "made any turn at all" is a false signal for "the
   * window is open" — it pinned the streak at 0, held the backoff at ~50s and made every pause
   * look like a first pause (job 41, 2026-07-28: 6 pauses in 7 minutes, all streak 0, one
   * Telegram message each). Callers pass the real threshold; 1 keeps the original
   * turns-must-be-zero meaning.
   */
  async noProgressPauseStreak(jobId: number, beforeRunId: number, progressTurns = 1): Promise<number> {
    return this.trailingPausedStreak(beforeRunId, 'ratelimit', jobId, progressTurns);
  }

  /** How many times this job has already been paused by a rate limit. 0 → this pause is its first. */
  async ratelimitPauseCount(jobId: number, beforeRunId: number): Promise<number> {
    const rows = await this.q<{ n: number }>(
      "select count(*) as n from ho_runs where job_id=? and id<? and status='paused' and stop_reason='ratelimit'",
      [jobId, beforeRunId],
    );
    return Number(rows[0]?.n ?? 0);
  }

  /**
   * Same count, but ACROSS ALL JOBS. A usage window is an ACCOUNT-level resource, so the
   * per-job streak understates it: on 2026-07-28 job 35 proved the window was shut (streak 1),
   * then job 36 was claimed and started its own ladder from scratch at 56s, burning five more
   * pointless attempts. Callers take max(per-job, global) so a fresh job inherits what the
   * previous one already learned.
   */
  async globalNoProgressPauseStreak(beforeRunId: number, progressTurns = 1): Promise<number> {
    return this.trailingPausedStreak(beforeRunId, 'ratelimit', null, progressTurns);
  }

  /**
   * How many runs of this job, immediately before `beforeRunId`, parked waiting on the same
   * unanswered human decision. Bounds the ask→park→ask cycle so an escalation nobody answers
   * eventually settles instead of nagging forever.
   */
  async awaitHumanStreak(jobId: number, beforeRunId: number): Promise<number> {
    return this.trailingPausedStreak(beforeRunId, 'await_human', jobId, null);
  }

  /**
   * Count the unbroken tail of paused runs matching `stopReason` (optionally scoped to one job).
   * `progressTurns`: a run with `turns >= progressTurns` made real progress and breaks the streak;
   * `null` means ignore turns entirely.
   */
  private async trailingPausedStreak(
    beforeRunId: number, stopReason: string, jobId: number | null, progressTurns: number | null,
  ): Promise<number> {
    const rows = await this.q<{ status: string; stop_reason: string | null; turns: number }>(
      jobId === null
        ? 'select status, stop_reason, turns from ho_runs where id<? order by id desc limit 50'
        : 'select status, stop_reason, turns from ho_runs where id<? and job_id=? order by id desc limit 50',
      jobId === null ? [beforeRunId] : [beforeRunId, jobId],
    );
    let n = 0;
    for (const r of rows) {
      const noProgress = progressTurns === null || Number(r.turns) < progressTurns;
      if (r.status === 'paused' && r.stop_reason === stopReason && noProgress) n += 1;
      else break;
    }
    return n;
  }

  async openEscalation(runId: number, jobId: number, reason: string, question: string, context: unknown): Promise<number> {
    await this.q("update ho_jobs set status='escalated' where id=?", [jobId]);
    const res = await this.exec({
      sql: 'insert into ho_escalations(run_id, job_id, reason, question, context) values(?,?,?,?,?)',
      args: [runId, jobId, reason, question, JSON.stringify(context ?? null)],
    });
    return Number(res.lastInsertRowid);
  }

  /**
   * Record a human's decision on an open escalation. Returns 'applied' when this call won the race,
   * 'already-decided' when someone got there first, or 'missing' when there is no such row.
   *
   * THIS BELONGS IN THE STORE, and that is the whole point of the method existing. The escalation
   * webhook used to open its OWN libSQL client and fire a bare UPDATE: no WAL, no busy_timeout
   * (a fresh connection defaults to 0 — fail instantly), no retry. With three conductor workers
   * writing the same file, that UPDATE throws SQLITE_BUSY, the exception reaches the webhook's
   * catch, it answers HTTP 500 — and the human's Approve/Deny/ABORT tap is gone. No log says a
   * decision was lost; the button simply did nothing and the job stayed parked.
   *
   * Going through Store means it inherits the connection settings (WAL + a short busy_timeout)
   * and the async retry ladder, which is exactly what the queue's own writers use.
   *
   * `and status='open'` keeps the FIRST decision: two taps, or a tap racing waitEscalation, must not
   * overwrite each other.
   */
  async decideEscalation(id: number, decision: string, who: string): Promise<'applied' | 'already-decided' | 'missing'> {
    const res = await this.exec({
      sql: "update ho_escalations set status=?, decided_by=?, decided_at=datetime('now') where id=? and status='open'",
      args: [decision, who, id],
    });
    if (Number(res.rowsAffected ?? 0) > 0) return 'applied';
    const rows = await this.q<{ n: number }>('select count(*) as n from ho_escalations where id=?', [id]);
    return Number(rows[0]?.n ?? 0) > 0 ? 'already-decided' : 'missing';
  }

  /**
   * Poll an escalation until decided or the wait runs out. Returns the recorded decision, or
   * the sentinel `'timeout'`.
   *
   * IT DOES NOT MARK THE ROW 'expired'. It used to, and that broke the buttons: handleCallback
   * only writes `where status='open'`, so once a row expired the Approve/Deny taps in Telegram
   * silently did nothing and the job was already gone. Leaving the row OPEN means a late answer
   * still lands, and the caller parks the job instead of failing it (4 of the first 11
   * escalations died as silent 'expired').
   *
   * `opts.jobId` keeps the job's heartbeat going while a human thinks — see heartbeat(); without
   * it a legitimate 30-minute approval window looks exactly like a dead worker to recoverStale.
   * `opts.onReminder` fires every `remindMs` while nobody answers — silence reads as a dead
   * conductor.
   *
   * Options are an object, not positionals: this call now carries five independent knobs, and
   * the two lineages that grew it disagreed on their order.
   */
  async waitEscalation(id: number, opts: WaitEscalationOpts = {}): Promise<string> {
    const { jobId, timeoutMs = 1000 * 60 * 30, pollMs = 5000, onReminder, remindMs = 1000 * 60 * 10 } = opts;
    const startedAt = Date.now();
    const deadline = startedAt + timeoutMs;
    let nextReminder = startedAt + remindMs;
    for (;;) {
      const rows = await this.q<{ status: string }>('select status from ho_escalations where id=?', [id]);
      const st = rows[0]?.status ?? 'open';
      if (st !== 'open') return st;
      if (Date.now() > deadline) return 'timeout';
      if (onReminder && Date.now() >= nextReminder) {
        nextReminder = Date.now() + remindMs;
        await onReminder(Date.now() - startedAt).catch(() => {});
      }
      if (jobId !== undefined) await this.heartbeat(jobId);
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
    return this.retryBusy('nextStep', async () => this.inWriteTx(() => {
      const pend = this.many(`select * from ho_steps where job_id=? and status='pending' order by step_no`, jobId);
      // find first whose dependencies are all 'done'
      let chosen: Row | null = null;
      for (const st of pend) {
        const deps = parseJson<number[]>(st.depends_on, []);
        if (deps.length === 0) { chosen = st; break; }
        const q = `select count(*) as n from ho_steps
                     where job_id=? and step_no in (${deps.map(() => '?').join(',')}) and status<>'done'`;
        const undone = this.one(q, jobId, ...deps);
        if (Number(undone?.n) === 0) { chosen = st; break; }
      }
      if (!chosen) return null;
      this.write(
        `update ho_steps set status='running', attempts=attempts+1, updated_at=datetime('now') where id=?`,
        chosen.id as number,
      );
      return mapStep(this.one('select * from ho_steps where id=?', chosen.id as number) as Row);
    }));
  }

  async recordAttempt(stepId: number): Promise<void> {
    await this.q("update ho_steps set attempts=attempts+1, updated_at=datetime('now') where id=?", [stepId]);
  }

  async setStepStatus(stepId: number, status: string): Promise<void> {
    await this.q("update ho_steps set status=?, updated_at=datetime('now') where id=?", [status, stepId]);
  }

  /** Update only the fields the caller actually passed.
   *
   * It used to write every column on every call, so an omitted field was stored
   * as NULL rather than left alone. runStep saves the reviewer and runtime
   * reports first and then calls this again with just {status, score, error} —
   * which wiped both. Every finished step in the database ended up with empty
   * reports: the entire evidence trail the verification protocol exists to
   * produce, gone, and no postmortem possible on any step.
   *
   * Presence is tested with `in`, not `!== undefined`, so a caller CAN still
   * clear a column by passing the key explicitly as undefined — which is how a
   * successful finish clears a previous error.
   */
  async finishStep(stepId: number, f: { status: string; score?: number; reviewer_report?: unknown; runtime_report?: unknown; error?: string }): Promise<void> {
    const sets: string[] = ['status=?'];
    const args: Arg[] = [f.status];
    if ('score' in f) { sets.push('score=?'); args.push(f.score ?? null); }
    if ('reviewer_report' in f) {
      sets.push('reviewer_report=?');
      args.push(f.reviewer_report === undefined ? null : JSON.stringify(f.reviewer_report));
    }
    if ('runtime_report' in f) {
      sets.push('runtime_report=?');
      args.push(f.runtime_report === undefined ? null : JSON.stringify(f.runtime_report));
    }
    if ('error' in f) { sets.push('error=?'); args.push(f.error ?? null); }
    sets.push("updated_at=datetime('now')");
    await this.q(`update ho_steps set ${sets.join(', ')} where id=?`, [...args, stepId]);
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

  /** Record an answer, and release the job once nothing is left open.
   *
   * askQuestions parks the job in 'awaiting-input' and NOTHING brought it back:
   * no code path cleared the status, recoverStale did not cover it, and the
   * documented `ho_answer_question(id, text)` procedure that was supposed to do
   * the releasing is a leftover of the Postgres schema — it does not exist in
   * SQLite. A job that ever asked a question could therefore never run again.
   *
   * Returns true when this answer was the last one and the job was released, so
   * a caller can report "back in the queue" rather than guess.
   */
  async answerQuestion(qid: number, answer: string): Promise<boolean> {
    const rows = await this.q<{ job_id: number }>('select job_id from ho_questions where id=?', [qid]);
    const jobId = rows[0]?.job_id;
    await this.q("update ho_questions set answer=?, status='answered', answered_at=datetime('now') where id=?", [answer, qid]);
    if (jobId === undefined) return false;
    const left = await this.q<{ n: number }>(
      "select count(*) as n from ho_questions where job_id=? and status='open'", [jobId]);
    if (Number(left[0]?.n ?? 0) > 0) return false;
    // Only release a job that is actually parked — never yank one that has since
    // moved on (aborted, failed, or picked up by something else).
    await this.q(
      "update ho_jobs set status='queued', not_before=datetime('now') where id=? and status='awaiting-input'",
      [jobId]);
    return true;
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
