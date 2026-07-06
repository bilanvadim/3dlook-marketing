-- Fullstack agents Conductor — state schema (plain PostgreSQL, no Supabase layer)
-- Apply: psql "$DATABASE_URL" -f sql/schema.sql  (or any Postgres migration tool).
-- The conductor connects directly as a privileged Postgres role (its own DB/schema), so the
-- RLS enable_row_level_security lines below are belt-and-suspenders; there are no public policies.
--
-- Minimal by design: queue + runs (with session_id for DURABLE RESUME) + escalations.
-- No cost ledger and no full event audit — cost is not tracked; loops are caught in-memory.

-- ============ jobs: the work queue ============
create table if not exists hc_jobs (
  id            bigint generated always as identity primary key,
  kind          text not null default 'feature'
                check (kind in ('feature','fix','scout','review','custom')),
  title         text not null,
  prompt        text not null,                       -- the goal handed to the agent
  priority      int  not null default 100,           -- lower = sooner
  status        text not null default 'queued'
                check (status in ('queued','claimed','running','paused','planning','awaiting-input','verifying','done','failed','deferred','escalated','aborted')),
  -- per-job circuit-breaker overrides (null = use conductor defaults). NO budget cap by design.
  max_turns      int,
  max_wall_secs  int,
  permission_mode text default 'acceptEdits'
                check (permission_mode in ('default','acceptEdits','bypassPermissions')),
  work_dir      text not null default '.',           -- repo path mounted into the container
  resume_session_id text,                            -- SDK session to resume; set while running, cleared on finish
  attempts      int  not null default 0,
  created_at    timestamptz not null default now(),
  not_before    timestamptz,                          -- for 'deferred' backoff (can be hours, for resume)
  claimed_by    text,                                  -- worker id
  claimed_at    timestamptz,
  finished_at   timestamptz,
  result_summary text,
  error         text
);
create index if not exists hc_jobs_pickable on hc_jobs (priority, created_at)
  where status in ('queued','deferred');

-- ============ runs: one execution attempt of a job ============
create table if not exists hc_runs (
  id            bigint generated always as identity primary key,
  job_id        bigint not null references hc_jobs(id) on delete cascade,
  attempt       int not null default 1,
  session_id    text,                                  -- SDK session id, for durable resume
  status        text not null default 'running'
                check (status in ('running','paused','done','failed','escalated','aborted')),
  turns         int not null default 0,
  stop_reason   text,                                  -- turns|timeout|stuck|ratelimit|ask_gate|completed|error|stale_recovered
  error         text,
  started_at    timestamptz not null default now(),
  ended_at      timestamptz
);
create index if not exists hc_runs_job on hc_runs(job_id);

-- ============ escalations: open questions to the human ============
create table if not exists hc_escalations (
  id            bigint generated always as identity primary key,
  run_id        bigint not null references hc_runs(id) on delete cascade,
  job_id        bigint not null references hc_jobs(id) on delete cascade,
  reason        text not null,                         -- ask_gate|turns|stuck|manual
  question      text not null,
  context       jsonb,                                 -- the proposed command / diff / state
  status        text not null default 'open'
                check (status in ('open','approved','denied','aborted','expired')),
  decided_by    text,
  decision_note text,
  created_at    timestamptz not null default now(),
  decided_at    timestamptz
);
create index if not exists hc_escalations_open on hc_escalations(status) where status='open';

-- ============ atomic claim: one worker grabs one job, no double-pickup ============
create or replace function hc_claim_job(worker text)
returns hc_jobs language plpgsql as $$
declare j hc_jobs;
begin
  select * into j from hc_jobs
   where status in ('queued','deferred')
     and (not_before is null or not_before <= now())
   order by priority, created_at
   for update skip locked
   limit 1;
  if not found then return null; end if;
  update hc_jobs
     set status='claimed', claimed_by=worker, claimed_at=now()
   where id = j.id
   returning * into j;
  return j;
end $$;

-- ============ durable resume: requeue jobs whose worker died mid-run ============
-- A job left 'running'/'claimed' past p_secs (default 15 min) is assumed crashed.
-- It is re-queued as 'deferred' carrying the latest run's session_id, so the next
-- claim resumes that SDK session instead of starting over.
create or replace function hc_recover_stale(p_secs int default 900)
returns int language plpgsql as $$
declare n int := 0; rec record;
begin
  for rec in
    select j.id as job_id,
           (select session_id from hc_runs where job_id = j.id order by id desc limit 1) as sid
      from hc_jobs j
     where j.status in ('running','claimed')
       and coalesce(j.claimed_at, j.created_at) < now() - make_interval(secs => p_secs)
  loop
    update hc_runs set status='failed', stop_reason='stale_recovered', ended_at=now()
     where job_id = rec.job_id and status in ('running','paused');
    update hc_jobs
       set status='deferred', not_before=now(), claimed_by=null,
           resume_session_id = coalesce(rec.sid, resume_session_id),
           attempts = attempts + 1
     where id = rec.job_id;
    n := n + 1;
  end loop;
  return n;
end $$;

-- ============ steps: per-step state machine under a job (migration 002) ============
create table if not exists hc_steps (
  id           bigint generated always as identity primary key,
  job_id       bigint not null references hc_jobs(id) on delete cascade,
  step_no      int not null,
  title        text not null,
  agent        text,
  tags         text[] not null default '{}',
  description  text,
  acceptance   jsonb not null default '[]'::jsonb,     -- [{id,text,status,evidence}]
  quality_bar  jsonb,                                  -- {tests,e2e,perf}
  depends_on   int[] not null default '{}',
  status       text not null default 'pending'
               check (status in ('pending','running','awaiting-input','verifying','needs_review','blocked','done')),
  attempts     int not null default 0,
  score        int,
  reviewer_report jsonb,
  runtime_report  jsonb,
  session_id   text,
  error        text,
  created_at   timestamptz not null default now(),
  updated_at   timestamptz not null default now(),
  unique (job_id, step_no)
);
create index if not exists hc_steps_job on hc_steps(job_id, step_no);

-- ============ questions: async interview channel ============
create table if not exists hc_questions (
  id           bigint generated always as identity primary key,
  job_id       bigint not null references hc_jobs(id) on delete cascade,
  step_no      int,
  seq          int not null,
  layer        text,
  question     text not null,
  answer       text,
  status       text not null default 'open' check (status in ('open','answered','skipped')),
  asked_at     timestamptz not null default now(),
  answered_at  timestamptz
);
create index if not exists hc_questions_open on hc_questions(job_id) where status='open';

-- ============ progress + status surfaces (read by Hermes) ============
create or replace view hc_job_progress as
select j.id as job_id,
       count(s.*)                                   as total_steps,
       count(s.*) filter (where s.status='done')    as done_steps,
       case when count(s.*)=0 then 0
            else round(100.0*count(s.*) filter (where s.status='done')/count(s.*)) end as percent
from hc_jobs j left join hc_steps s on s.job_id=j.id
group by j.id;

create or replace view hc_project_status as
select j.id as job_id, j.title, j.kind, j.status as job_status,
       p.total_steps, p.done_steps, p.percent,
       (select count(*) from hc_questions q  where q.job_id=j.id and q.status='open') as open_questions,
       (select count(*) from hc_escalations e where e.job_id=j.id and e.status='open') as open_escalations,
       j.not_before,
       coalesce((select max(s.updated_at) from hc_steps s where s.job_id=j.id), j.created_at) as last_activity
from hc_jobs j join hc_job_progress p on p.job_id=j.id;

-- ============ claim next runnable step (deps satisfied), atomic ============
create or replace function hc_next_step(p_job_id bigint)
returns hc_steps language plpgsql as $$
declare s hc_steps;
begin
  select st.* into s from hc_steps st
   where st.job_id = p_job_id and st.status='pending'
     and not exists (
       select 1 from unnest(st.depends_on) d
       join hc_steps dep on dep.job_id = p_job_id and dep.step_no = d
       where dep.status <> 'done'
     )
   order by st.step_no
   for update skip locked
   limit 1;
  if not found then return null; end if;
  update hc_steps set status='running', attempts=attempts+1, updated_at=now()
   where id = s.id returning * into s;
  return s;
end $$;

-- ============ answer a question (Hermes calls this from Telegram) ============
create or replace function hc_answer_question(p_qid bigint, p_answer text)
returns void language sql as $$
  update hc_questions set answer=p_answer, status='answered', answered_at=now() where id=p_qid;
$$;

alter table hc_jobs        enable row level security;
alter table hc_runs        enable row level security;
alter table hc_escalations enable row level security;
alter table hc_steps       enable row level security;
alter table hc_questions   enable row level security;
-- intentionally no policies: service-role only
