-- 003_profiles.sql — per-job "profile" (which Claude Code system to run under).
-- Additive & safe: nullable-with-default column; existing rows/logic unaffected.
-- Idempotent: re-apply to widen the allowed set on an already-migrated DB.
-- Apply: psql "$DATABASE_URL" -f sql/003_profiles.sql
--
-- A profile selects a mutually-exclusive plugin set (see
-- claude_code/DEV/profiles/<name>.json + switch-profile.sh). The conductor,
-- when it starts an Agent SDK session for a job, should activate this profile
-- so only that system's agents/skills/commands load. Hermes sets it at intake
-- (explicit "переключись на marketing_vb_sm" or intent-routing). NULL/'dev' = default.

alter table hc_jobs
  add column if not exists profile text not null default 'dev';

-- (Re)define the allowed set as a NAMED constraint so this migration can widen
-- it on a DB that was created with the older 4-profile check.
alter table hc_jobs drop constraint if exists hc_jobs_profile_check;
alter table hc_jobs add constraint hc_jobs_profile_check
  check (profile in ('dev','seo','marketing','security','marketing_vb','marketing_vb_sm'));

comment on column hc_jobs.profile is
  'Claude Code system/profile to run this job under: dev|seo|marketing|security|marketing_vb|marketing_vb_sm. Maps to claude_code/DEV/profiles/<profile>.json.';
