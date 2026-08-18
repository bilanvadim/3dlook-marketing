#!/usr/bin/env bash
# migrate-db.sh [profile] [--check] [--yes] — bring a live ho.db's CONSTRAINTS up to the schema.
#
# WHY THIS HAS TO EXIST
#
# sql/schema.sql is applied with `create table if not exists`, which does exactly nothing to a
# table that is already there. So every schema change since the database was created is present in
# git and absent from the running system, and nothing says so: reads and writes keep working, right
# up to the one insert that trips an old CHECK.
#
# It bit hard. Renaming the systems (dev-sm → dev, and so on) updated schema.sql, and sergiy_prod's
# live ho_jobs kept `check (profile in ('dev-sm','seo-sm','marketing-sm','security-sm',…))` — so the
# conductor rejected EVERY job submitted under the profile names the system actually uses, with a
# bare "CHECK constraint failed" and no clue that the constraint was simply out of date.
# vadim_prod's copy had the renamed values but was missing 'sandbox' and 'test'.
#
# validate.sh did not catch it because it checks the schema FILE against the shipped profiles. The
# file was right. doctor.sh now checks the LIVE database, which is the thing that decides.
#
# WHAT IT DOES: rebuilds ho_jobs with the shipped definition, preserving every row. SQLite cannot
# ALTER a CHECK constraint, so a rebuild is the only route — new table, copy, drop, rename,
# recreate indexes, verify. Nothing else in the schema is touched.
set -uo pipefail
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"

CHECK=0; YES=0; PROFILE_ARG=""; DB_OVERRIDE=""
while [ $# -gt 0 ]; do
  case "$1" in
    --check) CHECK=1; shift;;
    --yes|-y) YES=1; shift;;
    # --db exists so this can be REHEARSED on a copy before it touches the queue. The first version
    # had no such option, so its only test was the live database — and it emptied ho_jobs.
    --db) DB_OVERRIDE="${2:?--db needs a path}"; shift 2;;
    -*) die "unknown option: $1";;
    *) PROFILE_ARG="$1"; shift;;
  esac
done
load_profile "$PROFILE_ARG"
[ "$CHECK" = 1 ] || [ -n "$DB_OVERRIDE" ] || require_own_profile

DB="${DB_OVERRIDE:-$CONDUCTOR_DB_FILE}"
[ -f "$DB" ] || die "no database at $DB"
SCHEMA="$CONDUCTOR_DIR/sql/schema.sql"
[ -f "$SCHEMA" ] || die "no schema at $SCHEMA"

# The profiles the system can actually run, taken from the files rather than from a list someone
# has to remember to update.
shopt -s nullglob
shipped=()
for f in "$PROFILES_DIR"/*.json; do shipped+=("$(basename "$f" .json)"); done
[ "${#shipped[@]}" -gt 0 ] || die "no profiles found in $PROFILES_DIR"

live_check="$(sqlite_q "$DB" "select sql from sqlite_master where name='ho_jobs';" | tr -d '\n' | grep -oE "profile in \([^)]*\)" || true)"
# What the SHIPPED schema will accept — used both to decide whether a migration is needed and to
# refuse one that would reject existing rows.
new_expected="$(tr -d '\n' < "$SCHEMA" | grep -oE "profile[[:space:]]+text not null default 'dev'[^)]*\)" | grep -oE "profile in \([^)]*\)" || true)"
[ -n "$new_expected" ] || die "could not read the shipped profile CHECK from $SCHEMA"

hdr "ho_jobs profile constraint"
info "live    ${live_check:-<none found>}"
info "shipped ${shipped[*]}"

missing=()
for p in "${shipped[@]}"; do
  case "$live_check" in *"'$p'"*) : ;; *) missing+=("$p");; esac
done

if [ "${#missing[@]}" -eq 0 ]; then
  ok "every shipped profile is accepted by the live database — nothing to migrate"
  exit 0
fi
bad "the live database REJECTS: ${missing[*]}"
info "a job submitted under any of those fails with a bare CHECK error"
[ "$CHECK" = 1 ] && exit 1

# ── migrate ──────────────────────────────────────────────────────────────────
hdr "migrate"
if [ "$YES" != 1 ]; then
  printf '  %srebuild ho_jobs in %s?%s [type yes] ' "$_C_Y" "$DB" "$_C_0"
  read -r a; [ "$a" = yes ] || die "aborted"
fi

# A copy first, always. This rewrites the table that holds the queue's entire history.
BK="$DB.pre-migrate-$(date -u +%Y%m%d-%H%M%S)"
sqlite3 "$DB" ".backup '$BK'" 2>/dev/null || die "could not back up to $BK"
ok "backed up → $BK ($(sqlite_q "$BK" 'select count(*) from ho_jobs;') jobs)"

before_jobs="$(sqlite_q "$DB" 'select count(*) from ho_jobs;')"

# The conductor must not be writing while the table is swapped.
was_active=0
if [ -n "$DB_OVERRIDE" ]; then
  info "rehearsal on $DB — the live conductor is left running"
elif svc_active hermes-conductor; then
  was_active=1; sc hermes-conductor stop >/dev/null; ok "conductor stopped"
fi

# Extract the shipped ho_jobs definition straight from schema.sql, so this script never carries a
# second copy of the column list that could go stale — the exact failure mode it exists to fix.
defn="$(sed -n '/^create table if not exists ho_jobs (/,/^);/p' "$SCHEMA" \
        | sed '1s/create table if not exists ho_jobs (/create table ho_jobs_migrated (/')"
[ -n "$defn" ] || die "could not extract the ho_jobs definition from $SCHEMA"

cols="$(sqlite_q "$DB" "select group_concat(name, ', ') from pragma_table_info('ho_jobs');")"
[ -n "$cols" ] || die "could not read the live column list"

# EXISTING ROWS MUST SATISFY THE NEW CONSTRAINT, and on this box they did not: every job predating
# the rename carries profile='dev-sm', which the new CHECK rejects. The first version of this script
# copied rows verbatim, the insert failed on row one, and — because sqlite3 keeps going after an
# error unless told otherwise — the DROP and the COMMIT ran anyway. ho_jobs came out EMPTY.
#
# So: map the retired names, and refuse to start if anything is left that the new constraint would
# reject. Guessing a mapping for an unknown value would be worse than stopping.
declare -A RENAMED=( [dev-sm]=dev [seo-sm]=seo [marketing-sm]=marketing [security-sm]=security )
map_sql="profile"
for old_p in "${!RENAMED[@]}"; do
  map_sql="case $map_sql when '$old_p' then '${RENAMED[$old_p]}' else $map_sql end"
done
mapped_cols="$(printf '%s' "$cols" | sed "s/\bprofile\b/$map_sql/")"

unmappable="$(sqlite_q "$DB" "select distinct profile from ho_jobs;" | while read -r v; do
  [ -n "$v" ] || continue
  mapped="${RENAMED[$v]:-$v}"
  case "$new_expected" in *"'$mapped'"*) : ;; *) printf '%s ' "$v";; esac
done)"
if [ -n "$unmappable" ]; then
  bad "these profile values exist in the data and are not accepted by the new constraint: $unmappable"
  info "add them to the CHECK in $SCHEMA, or fix the rows, then re-run. Nothing was changed."
  [ "$was_active" = 1 ] && sc hermes-conductor start >/dev/null
  exit 1
fi
info "columns carried over: $(printf '%s' "$cols" | tr -cd ',' | wc -c | tr -d ' ') + 1"
for old_p in "${!RENAMED[@]}"; do
  n="$(sqlite_q "$DB" "select count(*) from ho_jobs where profile='$old_p';")"
  [ "${n:-0}" -gt 0 ] && info "remapping $n row(s): $old_p → ${RENAMED[$old_p]}"
done

# .bail on is the difference between a failed migration and a destroyed table. Without it sqlite3
# runs every remaining statement after an error — including the DROP and the COMMIT.
#
# The dependent views must be dropped first: they reference ho_jobs by name, so the DROP invalidates
# them and any later statement touching one fails. They are recreated from schema.sql afterwards.
views_sql="$(sed -n '/^create view if not exists /,/;$/p' "$SCHEMA")"
if sqlite3 "$DB" <<SQL
.bail on
PRAGMA foreign_keys=OFF;
BEGIN;
drop view if exists ho_job_progress;
drop view if exists ho_project_status;
$defn
insert into ho_jobs_migrated ($cols) select $mapped_cols from ho_jobs;
drop table ho_jobs;
alter table ho_jobs_migrated rename to ho_jobs;
create index if not exists ho_jobs_pickable on ho_jobs (priority, created_at)
  where status in ('queued','deferred');
create unique index if not exists ho_jobs_one_active_per_title
  on ho_jobs (title, work_dir)
  where status in ('queued','deferred','claimed','running','planning','verifying','awaiting-input');
$views_sql
COMMIT;
SQL
then
  ok "table rebuilt"
  # The detection stage called bad() to report the stale constraint, which is right for --check but
  # would otherwise make a SUCCESSFUL migration end with "1 failed". The finding is now resolved.
  FAILS=0
else
  bad "migration failed — .bail on stopped it before the destructive statements"
  info "restore from $BK if anything looks wrong"
  [ "$was_active" = 1 ] && sc hermes-conductor start >/dev/null
  exit 1
fi

# ── verify ───────────────────────────────────────────────────────────────────
hdr "verify"
after_jobs="$(sqlite_q "$DB" 'select count(*) from ho_jobs;')"
[ "$before_jobs" = "$after_jobs" ] && ok "$after_jobs job(s) preserved" \
  || bad "row count changed: $before_jobs → $after_jobs"
[ "$(sqlite_q "$DB" 'pragma integrity_check;')" = ok ] && ok "integrity ok" || bad "integrity_check failed"
new_check="$(sqlite_q "$DB" "select sql from sqlite_master where name='ho_jobs';" | tr -d '\n' | grep -oE "profile in \([^)]*\)" || true)"
still=()
for p in "${shipped[@]}"; do case "$new_check" in *"'$p'"*) : ;; *) still+=("$p");; esac; done
[ "${#still[@]}" -eq 0 ] && ok "every shipped profile is now accepted" || bad "still rejected: ${still[*]}"
idx="$(sqlite_q "$DB" "select count(*) from sqlite_master where type='index' and tbl_name='ho_jobs' and name like 'ho_jobs%';")"
[ "${idx:-0}" -ge 2 ] && ok "$idx index(es) recreated" || bad "indexes missing after the rebuild"

[ "$was_active" = 1 ] && { sc hermes-conductor start >/dev/null; sleep 8
  svc_active hermes-conductor && ok "conductor back up" || bad "conductor did not restart"; }

finish
