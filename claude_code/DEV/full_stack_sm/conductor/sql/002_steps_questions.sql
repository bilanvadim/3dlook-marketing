-- Migration 002 — step-level state, interview questions, progress/status surfaces.
-- Additive over the v1 schema (schema.sql). Safe to re-run (idempotent where possible).

-- ── extend job status vocabulary ────────────────────────────────────────────
alter table hc_jobs drop constraint if exists hc_jobs_status_check;
alter table hc_jobs add constraint hc_jobs_status_check
  check (status in ('queued','claimed','running','paused','planning','awaiting-input',
                    'verifying','done','failed','deferred','escalated','aborted'));

-- ── steps: per-step state machine under a job ───────────────────────────────
create table if not exists hc_steps (
  id           bigint generated always as identity primary key,
  job_id       bigint not null references hc_jobs(id) on delete cascade,
  step_no      int not null,
  title        text not null,
  agent        text,                                  -- which specialist (frontend-engineer, …)
  tags         text[] not null default '{}',          -- → policy packs
  description  text,
  acceptance   jsonb not null default '[]'::jsonb,     -- [{id,text,status,evidence}]
  quality_bar  jsonb,                                  -- {tests,e2e,perf}
  depends_on   int[] not null default '{}',            -- step_no list
  status       text not null default 'pending'
               check (status in ('pending','running','awaiting-input','verifying','needs_review','blocked','done')),
  attempts     int not null default 0,
  score        int,
  reviewer_report jsonb,
  runtime_report  jsonb,
  session_id   text,                                   -- step-level resume hint (best-effort)
  error        text,
  created_at   timestamptz not null default now(),
  updated_at   timestamptz not null default now(),
  unique (job_id, step_no)
);
create index if not exists hc_steps_job on hc_steps(job_id, step_no);

-- ── questions: async interview channel (Hermes relays these to the human) ────
create table if not exists hc_questions (
  id           bigint generated always as identity primary key,
  job_id       bigint not null references hc_jobs(id) on delete cascade,
  step_no      int,                                    -- null = planning-phase question
  seq          int not null,
  layer        text,                                   -- 'product' | 'L2-data' | ...
  question     text not null,
  answer       text,
  status       text not null default 'open' check (status in ('open','answered','skipped')),
  asked_at     timestamptz not null default now(),
  answered_at  timestamptz
);
create index if not exists hc_questions_open on hc_questions(job_id) where status='open';

-- ── progress view: % done per job ───────────────────────────────────────────
create or replace view hc_job_progress as
select j.id as job_id,
       count(s.*)                                   as total_steps,
       count(s.*) filter (where s.status='done')    as done_steps,
       case when count(s.*)=0 then 0
            else round(100.0*count(s.*) filter (where s.status='done')/count(s.*)) end as percent
from hc_jobs j left join hc_steps s on s.job_id=j.id
group by j.id;

-- ── project status view: the single read for a Telegram update ───────────────
create or replace view hc_project_status as
select j.id as job_id, j.title, j.kind, j.status as job_status,
       p.total_steps, p.done_steps, p.percent,
       (select count(*) from hc_questions q  where q.job_id=j.id and q.status='open') as open_questions,
       (select count(*) from hc_escalations e where e.job_id=j.id and e.status='open') as open_escalations,
       j.not_before,
       coalesce((select max(s.updated_at) from hc_steps s where s.job_id=j.id), j.created_at) as last_activity
from hc_jobs j join hc_job_progress p on p.job_id=j.id;

-- ── claim next runnable step (deps satisfied), atomic ───────────────────────
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

-- ── answer a question (Hermes calls this from Telegram) ──────────────────────
create or replace function hc_answer_question(p_qid bigint, p_answer text)
returns void language sql as $$
  update hc_questions set answer=p_answer, status='answered', answered_at=now() where id=p_qid;
$$;

alter table hc_steps     enable row level security;
alter table hc_questions enable row level security;
-- service-role only, no public policies (consistent with v1)
