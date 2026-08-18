#!/usr/bin/env bash
# update.sh [profile] [--force] [--no-restart] [--dry-run] — pull, re-render, verify, restart.
#
# The sequence, and why it is this sequence:
#
#   backup → reset → pull → render → deps → VERIFY → restart → doctor
#                                              ↑
#                              a failure here rolls back and stops
#
# `git reset --hard` is in there deliberately, and it is safe for one specific reason: the local
# modifications in a deployed tree are RENDER OUTPUT, which render.sh regenerates from the
# profile. Discarding them is not data loss, it is how the clean-clone → render model updates.
# diff.sh is what proves that claim before this runs — it separates render from drift, and this
# script REFUSES to discard actual drift unless you pass --force.
#
# `git clean` is NOT used, at any point, in any form. Untracked files here are the runtime:
# conductor/.env holds this profile's DB path and its Telegram credentials, and node_modules is
# 300 MB of installed dependencies. `reset --hard` leaves both alone; `clean -fd` would delete
# them and there is no version of this script where that is what someone wanted.
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"

PROFILE_ARG=""; FORCE=0; NO_RESTART=0; DRY=0; RESUMED=0
for a in "$@"; do
  case "$a" in
    --force) FORCE=1;;
    --no-restart) NO_RESTART=1;;
    --dry-run) DRY=1;;
    # Internal: set when this process IS the re-exec of a freshly pulled update.sh. Everything
    # up to and including the render has already happened; BEFORE comes in via the environment.
    --resumed-after-pull) RESUMED=1;;
    -*) die "unknown option: $a";;
    *) PROFILE_ARG="$a";;
  esac
done
load_profile "$PROFILE_ARG"
require_own_profile

run(){ if [ "$DRY" = 1 ]; then printf '  [dry-run] %s\n' "$*"; else "$@"; fi; }

git -C "$PROFILE_DEST" rev-parse --git-dir >/dev/null 2>&1 \
  || die "$PROFILE_DEST is not a git checkout — use deploy.sh for a first install"

# A SELF-UPDATING SCRIPT CANNOT DELIVER THE FIX FOR ITS OWN BUG.
#
# This happened twice in one afternoon: a bug in update.sh's drift detection made it abort on a
# clean tree, and the fix was in the very commit it refused to pull. Both times the way out was
# to run reset/pull/render by hand — which is the one path this whole script exists to remove.
#
# So after the pull, if update.sh itself changed, we hand control to the NEW copy and it finishes
# the run. That makes the tool able to repair itself, and it means a broken update.sh is only ever
# one commit away from being fixed rather than a manual intervention.
if [ "$RESUMED" = 1 ]; then
  BEFORE="${UPDATE_BEFORE:?--resumed-after-pull requires UPDATE_BEFORE}"
  BK="${UPDATE_BACKUP:-}"
  # AFTER is normally computed by the pull stage, which a resume skips — and every later stage
  # needs it: the dependency check, the restart decision and the summary all diff BEFORE..AFTER.
  # Without it the resumed process died on `set -u` at the dependency stage, AFTER the render had
  # already succeeded. The tree was left correct and the services untouched, but the update
  # stopped halfway with an unbound-variable message, which is not a failure mode anyone should
  # have to interpret. HEAD is exactly what the pull would have recorded.
  AFTER="$(git -C "$PROFILE_DEST" rev-parse HEAD)"
  # The render already ran in the process that handed off; do not re-arm the template-form trap.
  RENDER_DONE=1
  ok "resumed in the freshly pulled update.sh ($(git_head))"
else

hdr "1/8  pre-flight"
BEFORE="$(git -C "$PROFILE_DEST" rev-parse HEAD)"
info "current $(git_head)"

set +e; "$REPO_ROOT/scripts/check-update.sh" "$PROFILE_NAME" --quiet; CU=$?; set -e
case "$CU" in
  0) if [ "$FORCE" = 0 ]; then ok "already up to date — nothing to do"; exit 0; fi
     info "already up to date, but --force given: re-rendering and re-verifying";;
  3) ok "updates available";;
  *) die "cannot determine update state (network? upstream? see check-update.sh)";;
esac

# A consumer tree must not carry commits: `reset --hard` would silently destroy them.
ahead="$(git -C "$PROFILE_DEST" rev-list --count '@{u}..HEAD' 2>/dev/null || echo 0)"
if [ "${ahead:-0}" -gt 0 ] && [ "${PROFILE_ROLE:-consumer}" != author ]; then
  bad "$ahead local commit(s) in a consumer tree — they would be DESTROYED by the reset below"
  info "push them somewhere or drop them deliberately, then re-run"
  exit 1
fi

# Real drift must not be thrown away without the operator saying so.
# Read the COUNTERS, not the prose: grepping for "drift:" also matched the success line
# "no drift: every local modification is explained by the render", so a clean tree aborted
# its own update.
set +e; drift_line="$("$REPO_ROOT/scripts/diff.sh" "$PROFILE_NAME" --porcelain 2>/dev/null)"; set -e
drift_files="$(printf '%s' "$drift_line" | sed -n 's/.*DRIFT=\([0-9]*\).*/\1/p')"
drift_files="${drift_files:-0}"
if [ "${drift_files:-0}" -gt 0 ] && [ "$FORCE" = 0 ]; then
  bad "$drift_files locally modified file(s) are NOT explained by the render — real drift"
  "$REPO_ROOT/scripts/diff.sh" "$PROFILE_NAME" 2>&1 | grep -E '✗ drift:' | sed 's/^/    /'
  info "inspect with: scripts/diff.sh $PROFILE_NAME --full"
  info "then re-run with --force to discard it, or commit it upstream first"
  exit 1
fi
[ "${drift_files:-0}" -gt 0 ] && warn "--force: discarding $drift_files drifted file(s)"

# A job mid-flight survives a restart (durable resume re-claims it with its session id), but say
# so rather than let it be a surprise.
if [ -f "$CONDUCTOR_DB_FILE" ]; then
  busy="$(sqlite_q "$CONDUCTOR_DB_FILE" "select count(*) from ho_jobs where status in ('claimed','running','planning','verifying');")"
  [ "${busy:-0}" -gt 0 ] && warn "$busy job(s) in flight — they will be requeued and resumed after the restart"
fi

hdr "2/8  backup"
if [ "$DRY" = 1 ]; then info "[dry-run] backup.sh --label pre-update"
else
  "$REPO_ROOT/scripts/backup.sh" "$PROFILE_NAME" --label pre-update >/dev/null || die "backup failed — refusing to update without one"
  BK="$(cat "$HERMES_HOME/backups/.last" 2>/dev/null)"
  ok "backed up to $BK"
fi

hdr "3/8  discard render output, pull"
# FROM HERE UNTIL THE RENDER, THE TREE IS NOT USABLE.
#
# `reset --hard` restores the tracked files to their TEMPLATE form, which since §4 means they carry
# @DEST@ / @HOME@ / @USER@ instead of real paths — and this tree is live: Claude Code resolves
# plugin marketplaces out of it by absolute path on its next call. A tokenised tree is not
# "slightly stale", it is broken.
#
# The window is a second or two, but a failed pull would leave it open indefinitely, so an EXIT
# trap re-renders on ANY exit path until the render below clears it. Better a tree back on the old
# commit and rendered than one sitting in template form.
if [ "$DRY" = 0 ]; then
  trap 'st=$?; [ "${RENDER_DONE:-0}" = 1 ] || { echo "  re-rendering: the tree must not be left in template form" >&2
    "$REPO_ROOT/scripts/render.sh" "$PROFILE_NAME" --tree "$PROFILE_DEST" >/dev/null 2>&1; }; exit $st' EXIT
fi
run git -C "$PROFILE_DEST" reset -q --hard HEAD
run git -C "$PROFILE_DEST" pull -q --ff-only origin "$(git -C "$PROFILE_DEST" rev-parse --abbrev-ref HEAD)" \
  || { bad "pull failed (not a fast-forward?)"; exit 1; }
AFTER="$(git -C "$PROFILE_DEST" rev-parse HEAD)"
if [ "$DRY" = 0 ]; then
  ok "$(git -C "$PROFILE_DEST" rev-parse --short "$BEFORE") → $(git_head)"
  git -C "$PROFILE_DEST" log --oneline "$BEFORE..$AFTER" 2>/dev/null | head -10 | sed 's/^/      /'
fi

hdr "4/8  render"
run "$REPO_ROOT/scripts/render.sh" "$PROFILE_NAME" --tree "$PROFILE_DEST" || die "render failed"
RENDER_DONE=1
if [ "$DRY" = 0 ]; then trap - EXIT; fi

# Hand off to the new copy if this script (or its library) is part of what we just pulled.
if [ "$DRY" = 0 ] && ! git -C "$PROFILE_DEST" diff --quiet "$BEFORE" "$AFTER" -- \
     'scripts/update.sh' 'scripts/lib.sh' 'scripts/diff.sh' 2>/dev/null; then
  hdr "hand-off"
  ok "update.sh changed in this pull — continuing in the new version"
  UPDATE_BEFORE="$BEFORE" UPDATE_BACKUP="${BK:-}" \
    exec "$PROFILE_DEST/scripts/update.sh" "$PROFILE_NAME" --resumed-after-pull \
      $([ "$NO_RESTART" = 1 ] && echo --no-restart)
fi
fi   # end of the pre-render phase skipped on resume

rollback_now(){
  bad "$1"
  if [ "$DRY" = 1 ]; then info "[dry-run] would roll back to $(git -C "$PROFILE_DEST" rev-parse --short "$BEFORE")"; exit 1; fi
  hdr "rolling back"
  git -C "$PROFILE_DEST" reset -q --hard "$BEFORE" && ok "tree back at $(git -C "$PROFILE_DEST" rev-parse --short "$BEFORE")"
  "$REPO_ROOT/scripts/render.sh" "$PROFILE_NAME" --tree "$PROFILE_DEST" >/dev/null && ok "re-rendered"
  if [ -f "$CONDUCTOR_DIR/package-lock.json" ] && [ "$DEPS" = 1 ]; then
    ( cd "$CONDUCTOR_DIR" && npm ci --silent >/dev/null 2>&1 ) && ok "dependencies restored"
  fi
  info "config and queue are untouched; the backup is at ${BK:-<none>}"
  exit 1
}

hdr "5/8  dependencies"
DEPS=0
if [ "$DRY" = 0 ] && ! git -C "$PROFILE_DEST" diff --quiet "$BEFORE" "$AFTER" -- \
     'agents-ai/telegram-bot-agent/claude-code-agent/DEV/dev/conductor/package-lock.json' 2>/dev/null; then
  DEPS=1
  info "package-lock.json changed — npm ci"
  ( cd "$CONDUCTOR_DIR" && npm ci --silent ) || rollback_now "npm ci failed"
  ok "dependencies installed"
else
  ok "unchanged"
fi

hdr "6/8  verify BEFORE restarting anything"
# The point of doing this here: a broken conductor that is still running is a far better place
# to be than a broken conductor that has just been restarted into a crash loop.
if [ "$DRY" = 1 ]; then info "[dry-run] typecheck + tests"
elif [ -d "$CONDUCTOR_DIR/node_modules" ]; then
  ( cd "$CONDUCTOR_DIR" && npx --no-install tsc --noEmit ) || rollback_now "typecheck failed on the new code"
  ok "typecheck clean"
  ( cd "$CONDUCTOR_DIR" && npm test >/tmp/.upd-tests.$$ 2>&1 ) || {
    grep -E 'FAIL' /tmp/.upd-tests.$$ | head -8 | sed 's/^/      /'; rm -f /tmp/.upd-tests.$$
    rollback_now "tests failed on the new code"; }
  ok "tests pass ($(grep -c 'ok  ' /tmp/.upd-tests.$$) assertions)"; rm -f /tmp/.upd-tests.$$
else
  warn "no node_modules — cannot verify the conductor before restart"
fi

hdr "7/8  restart what the change touched"
if [ "$NO_RESTART" = 1 ]; then
  warn "--no-restart: services still run the OLD code until you restart them"
elif [ "$DRY" = 1 ]; then
  info "[dry-run] would restart affected services"
else
  touched="$(git -C "$PROFILE_DEST" diff --name-only "$BEFORE" "$AFTER" 2>/dev/null)"
  restarted=0
  if printf '%s\n' "$touched" | grep -q 'DEV/dev/conductor/'; then
    sc hermes-conductor restart >/dev/null && { ok "hermes-conductor restarted"; restarted=1; }
  fi
  if printf '%s\n' "$touched" | grep -qE 'hermes-agent/(SOUL\.md|skills/|ops/|CONFIG)'; then
    sc hermes-gateway restart >/dev/null && { ok "hermes-gateway restarted"; restarted=1; }
  fi
  [ "$restarted" = 0 ] && ok "nothing that requires a restart"
  [ "$restarted" = 1 ] && { sleep 12; for u in hermes-conductor hermes-gateway; do
      svc_active "$u" && ok "$u active" || bad "$u did NOT come back — see rollback.sh"
    done; }
fi

hdr "8/8  post-update health"
if [ "$DRY" = 1 ]; then info "[dry-run] doctor.sh"
else
  set +e; "$REPO_ROOT/scripts/doctor.sh" "$PROFILE_NAME" >/tmp/.upd-doc.$$ 2>&1; dc=$?; set -e
  case "$dc" in
    0) ok "doctor: clean";;
    2) warn "doctor: warnings only"; grep -E '^  !' /tmp/.upd-doc.$$ | head -6 | sed 's/^/    /';;
    *) bad "doctor reports failures AFTER the update"; grep -E '^  ✗' /tmp/.upd-doc.$$ | head -8 | sed 's/^/    /'
       info "roll back with: scripts/rollback.sh $PROFILE_NAME";;
  esac
  rm -f /tmp/.upd-doc.$$
  printf '%s updated %s → %s\n' "$(date -u '+%F %T')" "$(git -C "$PROFILE_DEST" rev-parse --short "$BEFORE")" "$(git_head)" \
    >> "$HERMES_HOME/update-history.log"
fi

finish
