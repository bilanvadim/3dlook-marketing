-- Align ho_jobs.profile's CHECK list with the manifests that actually exist.
--
-- WHY: the list had drifted in both directions. It accepted 'sandbox' and 'test' (no
-- manifest on disk — a job against either passed validation and ran with zero plugins)
-- and rejected 'sandbox_sm' (which does ship).
--
-- ⚠️ RUN THIS WITH `sqlite3 -bail`, AND DROP THE VIEWS FIRST.
--
-- Both of those are lessons from doing it wrong on 2026-08-28:
--
--  1. `ALTER TABLE ho_jobs_new RENAME TO ho_jobs` FAILS while any view still references
--     ho_jobs, because SQLite re-validates every view during a rename and ho_jobs has
--     just been dropped:  "error in view ho_job_progress: no such table: main.ho_jobs".
--
--  2. `sqlite3` WITHOUT `-bail` does not stop on that error. It carried on to COMMIT, so
--     the DROP was committed and the table was gone from the live queue — recovered only
--     because ho_jobs_new still held all 100 rows and a `sqlite3 .backup` had been taken
--     minutes earlier. A migration script that cannot fail cleanly is not a migration.
--
-- Take a backup with `sqlite3 <db> ".backup <path>"` (never cp: WAL) and stop the
-- conductor before running this.
PRAGMA foreign_keys=OFF;
BEGIN;

DROP VIEW IF EXISTS ho_job_progress;
DROP VIEW IF EXISTS ho_project_status;

CREATE TABLE ho_jobs_migrated AS SELECT * FROM ho_jobs;   -- data parking, schema-less
DROP TABLE ho_jobs;

-- Recreate with the corrected CHECK. Keep this in sync with sql/schema.sql.
CREATE TABLE ho_jobs (
  id            integer primary key autoincrement,
  kind          text not null default 'feature'
                check (kind in ('feature','fix','scout','review','custom')),
  title         text not null,
  prompt        text not null,
  priority      integer not null default 100,
  status        text not null default 'queued'
                check (status in ('queued','claimed','running','paused','planning','awaiting-input','verifying','done','failed','deferred','escalated','aborted')),
  max_turns      integer,
  max_wall_secs  integer,
  permission_mode text default 'acceptEdits'
                check (permission_mode in ('default','acceptEdits','bypassPermissions')),
  work_dir      text not null default '.',
  resume_session_id text,
  attempts      integer not null default 0,
  profile       text not null default 'dev'
                check (profile in ('dev','marketing','marketing_vb','marketing_vb_sm',
                                   'sandbox_sm','security','seo')),
  created_at    text not null default (datetime('now')),
  not_before    text,
  claimed_by    text,
  claimed_at    text,
  finished_at   text,
  result_summary text,
  error         text
);
INSERT INTO ho_jobs SELECT * FROM ho_jobs_migrated;
DROP TABLE ho_jobs_migrated;

CREATE INDEX ho_jobs_pickable on ho_jobs (priority, created_at)
  where status in ('queued','deferred');
CREATE UNIQUE INDEX ho_jobs_one_active_per_title
  on ho_jobs (title, work_dir)
  where status in ('queued','deferred','claimed','running','planning','verifying','awaiting-input');

-- Recreate the views AFTER the table exists again.
CREATE VIEW ho_job_progress as
select j.id as job_id,
       count(s.id)                                     as total_steps,
       count(case when s.status='done' then 1 end)     as done_steps,
       case when count(s.id)=0 then 0
            else round(100.0*count(case when s.status='done' then 1 end)/count(s.id)) end as percent
from ho_jobs j left join ho_steps s on s.job_id = j.id
group by j.id;

CREATE VIEW ho_project_status as
select j.id, j.kind, j.title, j.status, j.profile, j.work_dir, j.attempts,
       j.created_at, j.finished_at, j.result_summary, j.error,
       p.total_steps, p.done_steps, p.percent
from ho_jobs j left join ho_job_progress p on p.job_id = j.id;

COMMIT;
PRAGMA foreign_keys=ON;

-- Afterwards, assert rather than assume:
--   pragma integrity_check;                     -- ok
--   select count(*) from ho_jobs;               -- unchanged
--   select type,name from sqlite_master;        -- 2 views, both ho_jobs indexes back
--   select count(*) from ho_project_status;     -- the views must actually query
