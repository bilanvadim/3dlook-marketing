-- 003_profiles.sql — per-job "profile" (which Claude Code system to run under).
-- Additive & safe: nullable column with a default; existing rows/logic unaffected.
-- Apply: psql "$DATABASE_URL" -f sql/003_profiles.sql
--
-- A profile selects a mutually-exclusive plugin set (see
-- claude_code/DEV/profiles/<name>.json + switch-profile.sh). The conductor,
-- when it starts an Agent SDK session for a job, should activate this profile
-- so only that system's agents/skills/commands load. Hermes sets it at intake
-- (explicit "переключись на SEO" or intent-routing). NULL/'dev' = default dev.

alter table hc_jobs
  add column if not exists profile text not null default 'dev'
  check (profile in ('dev','seo','marketing','security'));

comment on column hc_jobs.profile is
  'Claude Code system/profile to run this job under: dev|seo|marketing|security. Maps to claude_code/DEV/profiles/<profile>.json.';
