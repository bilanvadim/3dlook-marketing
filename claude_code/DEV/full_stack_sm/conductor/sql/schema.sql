-- Hermes Orchestrator — conductor state schema (SQLite / libSQL).
-- Apply: sqlite3 ho.db < sql/schema.sql   (or via @libsql/client / Turso `turso db shell`).
-- Single-file, single-writer store. For a networked/shared DB point the same code
-- at a libSQL server or Turso (DATABASE_URL=libsql://…) — identical schema.
--
-- Prefix `ho_` = Hermes Orchestrator. Consolidated (jobs + runs + escalations +
-- steps + questions + profile + views) — no separate migrations, no stored
-- procedures: the atomic claim/next-step/recover/answer logic lives in store.ts
-- (SQLite is single-writer, so a write transaction is race-free by construction).

pragma journal_mode = wal;
pragma foreign_keys = on;

-- ============ jobs: the work queue ============
create table if not exists ho_jobs (
  id            integer primary key autoincrement,
  kind          text not null default 'feature'
                check (kind in ('feature','fix','scout','review','custom')),
  title         text not null,
  prompt        text not null,                       -- the goal handed to the agent
  priority      integer not null default 100,        -- lower = sooner
  status        text not null default 'queued'
                check (status in ('queued','claimed','running','paused','planning','awaiting-input','verifying','done','failed','deferred','escalated','aborted')),
  -- per-job circuit-breaker overrides (null = use conductor defaults). NO budget cap by design.
  max_turns      integer,
  max_wall_secs  integer,
  permission_mode text default 'acceptEdits'
                check (permission_mode in ('default','acceptEdits','bypassPermissions')),
  work_dir      text not null default '.',           -- repo path the agent runs in
  resume_session_id text,                            -- SDK session to resume; set while running, cleared on finish
  attempts      integer not null default 0,
  -- which Claude Code system to run under (maps to claude_code/DEV/profiles/<profile>.json)
  profile       text not null default 'dev'
                check (profile in ('dev','seo','marketing','security','marketing_vb','marketing_vb_sm')),
  created_at    text not null default (datetime('now')),
  not_before    text,                                 -- for 'deferred' backoff (can be hours, for resume)
  claimed_by    text,                                 -- worker id
  claimed_at    text,
  finished_at   text,
  result_summary text,
  error         text
);
create index if not exists ho_jobs_pickable on ho_jobs (priority, created_at)
  where status in ('queued','deferred');

-- ============ runs: one execution attempt of a job ============
create table if not exists ho_runs (
  id            integer primary key autoincrement,
  job_id        integer not null references ho_jobs(id) on delete cascade,
  attempt       integer not null default 1,
  session_id    text,                                  -- SDK session id, for durable resume
  status        text not null default 'running'
                check (status in ('running','paused','done','failed','escalated','aborted')),
  turns         integer not null default 0,
  stop_reason   text,                                  -- turns|timeout|stuck|ratelimit|ask_gate|completed|error|stale_recovered
  error         text,
  started_at    text not null default (datetime('now')),
  ended_at      text
);
create index if not exists ho_runs_job on ho_runs(job_id);

-- ============ escalations: open questions to the human ============
create table if not exists ho_escalations (
  id            integer primary key autoincrement,
  run_id        integer not null references ho_runs(id) on delete cascade,
  job_id        integer not null references ho_jobs(id) on delete cascade,
  reason        text not null,                         -- ask_gate|turns|stuck|manual
  question      text not null,
  context       text,                                  -- JSON: the proposed command / diff / state
  status        text not null default 'open'
                check (status in ('open','approved','denied','aborted','expired')),
  decided_by    text,
  decision_note text,
  created_at    text not null default (datetime('now')),
  decided_at    text
);
create index if not exists ho_escalations_open on ho_escalations(status) where status='open';

-- ============ steps: per-step state machine under a job ============
create table if not exists ho_steps (
  id           integer primary key autoincrement,
  job_id       integer not null references ho_jobs(id) on delete cascade,
  step_no      integer not null,
  title        text not null,
  agent        text,
  tags         text not null default '[]',             -- JSON array of strings
  description  text,
  acceptance   text not null default '[]',             -- JSON: [{id,text,status,evidence}]
  quality_bar  text,                                   -- JSON: {tests,e2e,perf}
  depends_on   text not null default '[]',             -- JSON array of step_no ints
  status       text not null default 'pending'
               check (status in ('pending','running','awaiting-input','verifying','needs_review','blocked','done')),
  attempts     integer not null default 0,
  score        integer,
  reviewer_report text,                                -- JSON
  runtime_report  text,                                -- JSON
  session_id   text,
  error        text,
  created_at   text not null default (datetime('now')),
  updated_at   text not null default (datetime('now')),
  unique (job_id, step_no)
);
create index if not exists ho_steps_job on ho_steps(job_id, step_no);

-- ============ questions: async interview channel ============
create table if not exists ho_questions (
  id           integer primary key autoincrement,
  job_id       integer not null references ho_jobs(id) on delete cascade,
  step_no      integer,
  seq          integer not null,
  layer        text,
  question     text not null,
  answer       text,
  status       text not null default 'open' check (status in ('open','answered','skipped')),
  asked_at     text not null default (datetime('now')),
  answered_at  text
);
create index if not exists ho_questions_open on ho_questions(job_id) where status='open';

-- ============ progress + status surfaces (read by Hermes) ============
create view if not exists ho_job_progress as
select j.id as job_id,
       count(s.id)                                     as total_steps,
       count(case when s.status='done' then 1 end)     as done_steps,
       case when count(s.id)=0 then 0
            else round(100.0*count(case when s.status='done' then 1 end)/count(s.id)) end as percent
from ho_jobs j left join ho_steps s on s.job_id=j.id
group by j.id;

create view if not exists ho_project_status as
select j.id as job_id, j.title, j.kind, j.status as job_status,
       p.total_steps, p.done_steps, p.percent,
       (select count(*) from ho_questions q  where q.job_id=j.id and q.status='open') as open_questions,
       (select count(*) from ho_escalations e where e.job_id=j.id and e.status='open') as open_escalations,
       j.not_before,
       coalesce((select max(s.updated_at) from ho_steps s where s.job_id=j.id), j.created_at) as last_activity
from ho_jobs j join ho_job_progress p on p.job_id=j.id;
