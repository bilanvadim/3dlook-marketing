#!/usr/bin/env bash
# deploy.sh [profile] [--tree DIR] [--dry-run] — put a profile's runtime tree in place.
#
# This is the first-install / re-deploy path: clone → render → dependencies → conductor .env →
# verify. It is what turns "a profile exists in git" into "this account has a runtime", and it is
# the script that did not exist when vadim_prod was set up — which is exactly why his tree was a
# plain COPY with no git remote and no update path at all.
#
# IDEMPOTENT: run it on an existing deployment and it fetches instead of clones, re-renders, and
# reinstalls dependencies only if the lock file moved. It does NOT touch secrets, the queue, or
# any live service beyond what it must — updating an existing deployment is update.sh's job.
#
# It deliberately does NOT install unit files or write secrets. install.sh owns the machine-level
# setup (services, linger, venvs) and secrets are the account owner's to provide; this script
# owns the TREE.
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"

PROFILE_ARG=""; TREE=""; DRY=0
while [ $# -gt 0 ]; do
  case "$1" in
    --tree) TREE="${2:-}"; shift 2;;
    --dry-run) DRY=1; shift;;
    -*) die "unknown option: $1";;
    *) PROFILE_ARG="$1"; shift;;
  esac
done
load_profile "$PROFILE_ARG"
require_own_profile
[ -n "$TREE" ] || TREE="$PROFILE_DEST"
run(){ if [ "$DRY" = 1 ]; then printf '  [dry-run] %s\n' "$*"; else "$@"; fi; }

# The remote is read from THIS repo, so a deploy cannot be pointed at a different origin by
# accident — one source of truth means one URL.
ORIGIN="$(git -C "$REPO_ROOT" remote get-url origin 2>/dev/null)"
[ -n "$ORIGIN" ] || die "cannot determine the canonical remote from $REPO_ROOT"

hdr "deploy $PROFILE_NAME → $TREE"
info "origin  $ORIGIN"
info "role    ${PROFILE_ROLE:-consumer}"

# ── 1. tree ──────────────────────────────────────────────────────────────────
hdr "1/6  checkout"
if [ -d "$TREE/.git" ]; then
  ok "already a git checkout at $(git -C "$TREE" rev-parse --short HEAD 2>/dev/null)"
  run git -C "$TREE" fetch -q origin || warn "fetch failed — continuing with what is on disk"
elif [ -d "$TREE" ] && [ -n "$(ls -A "$TREE" 2>/dev/null)" ]; then
  # A non-git directory with content is the vadim_prod situation. Never overwrite it in place:
  # clone alongside, then swap, so a failure at any point leaves the old tree intact.
  warn "$TREE exists and is NOT a git checkout — cloning alongside and swapping"
  NEW="$TREE.newclone-$(date -u +%Y%m%d-%H%M%S)"
  OLD="$TREE.oldcopy-$(date -u +%Y%m%d-%H%M%S)"
  run git clone -q "$ORIGIN" "$NEW" || die "clone failed"
  if [ "$DRY" = 0 ]; then
    # Anything the old tree has that the clone does not is either runtime state or drift; report
    # it BEFORE the swap rather than discovering it afterwards.
    extra="$(diff -rq --exclude=.git --exclude=node_modules "$NEW" "$TREE" 2>/dev/null | grep "^Only in $TREE" | wc -l)"
    [ "${extra:-0}" -gt 0 ] && warn "$extra path(s) exist only in the old tree — check them in $OLD after the swap"
    mv "$TREE" "$OLD" && mv "$NEW" "$TREE" || die "swap failed — old tree is at $OLD"
    ok "swapped; previous tree kept at $OLD"
  fi
else
  run git clone -q "$ORIGIN" "$TREE" || die "clone failed"
  ok "cloned"
fi

# ── 1b. make the runtime refuse commits ──────────────────────────────────────
# A consumer tree is a read-only replica. Committing in it produces work that no other runtime can
# see and that the next `update.sh` discards with its reset — and the mistake is easy, because the
# runtime tree is where you happen to be standing when you notice something wrong.
#
# Hooks are not tracked by git, so installing one is a deployment step. It is advisory by design:
# `--no-verify` still works for the rare case where you know what you are doing.
if [ "${PROFILE_ROLE:-consumer}" = consumer ] && [ "$DRY" = 0 ] && [ -d "$TREE/.git" ]; then
  hdr "1b/6  commit guard"
  hook="$TREE/.git/hooks/pre-commit"
  mkdir -p "$(dirname "$hook")"
  # Two different messages, because the right advice differs. A profile WITH a dev tree has
  # somewhere local to put the change; one without it (a read-only clone on a deploy key) does
  # not, and telling its owner to "commit in the dev checkout" would name a path they do not have.
  if [ -n "${PROFILE_DEV_TREE:-}" ]; then
    advice="Commit in the development checkout instead:

    $PROFILE_DEV_TREE

then push, and run ./scripts/update.sh here to pull it in."
  else
    advice="This clone is read-only (deploy key). Changes belong in the canonical repository:
open a pull request there, then run ./scripts/update.sh here to pull it in."
  fi
  # The message is expanded NOW, at install time, and written as a literal heredoc inside the
  # hook — so the hook itself needs no variables and cannot mis-expand at commit time.
  {
    printf '%s\n' '#!/bin/sh' \
      '# Installed by scripts/deploy.sh. This tree is a RUNTIME replica, not a working copy.' \
      "cat >&2 <<'MSG'" \
      "refusing to commit: $TREE is a runtime replica, not a working copy." \
      "" \
      "A commit here is invisible to the other runtime and is discarded by the next update.sh" \
      "reset, which resets the tree to origin before re-rendering it." \
      ""
    printf '%s\n' "$advice" ""
    printf '%s\n' "(--no-verify overrides this if you really mean it.)" 'MSG' 'exit 1'
  } > "$hook"
  chmod +x "$hook"
  ok "pre-commit guard installed (${PROFILE_DEV_TREE:+dev tree: $PROFILE_DEV_TREE})"
fi

# ── 2. render ────────────────────────────────────────────────────────────────
hdr "2/6  render"
run "$REPO_ROOT/scripts/render.sh" "$PROFILE_NAME" --tree "$TREE" || die "render failed"

# ── 3. dependencies ──────────────────────────────────────────────────────────
# The single reason the canonical tree could not be started on vadim_prod: no node_modules, so
# `npm start` exited 127 and a drop-in was added to pin the unit back to the old tree instead.
hdr "3/6  conductor dependencies"
CD="$TREE/agents-ai/telegram-bot-agent/claude-code-agent/DEV/dev/conductor"
[ -d "$CD" ] || die "no conductor directory in the tree: $CD"
if [ "$DRY" = 1 ]; then info "[dry-run] npm ci in $CD"
else
  ( cd "$CD" && npm ci --silent ) || ( cd "$CD" && npm install --silent ) || die "dependency install failed"
  ok "installed ($(du -sh "$CD/node_modules" 2>/dev/null | cut -f1))"
fi

# ── 4. conductor .env ────────────────────────────────────────────────────────
# Rendered from the profile, never copied from another account. Existing files are left ALONE:
# this one holds Telegram credentials, and silently rewriting it is how one account ends up
# holding another's bot token.
hdr "4/6  conductor .env"
if [ -f "$CD/.env" ]; then
  ok "exists — left untouched (it holds credentials)"
  for k in DATABASE_URL HO_WEBHOOK_PORT HO_WEBHOOK_SECRET HO_SNAPSHOT_SH; do
    v="$(env_get "$CD/.env" "$k" || true)"
    [ -n "$v" ] && info "$k=$v" || warn "$k is not set in $CD/.env"
  done
  want_db="file:$PROFILE_CONDUCTOR_DB"
  have_db="$(env_get "$CD/.env" DATABASE_URL || true)"
  [ -n "$have_db" ] && [ "$have_db" != "$want_db" ] \
    && warn "DATABASE_URL is $have_db but the profile says $want_db"
  want_port="$PROFILE_HO_WEBHOOK_PORT"
  have_port="$(env_get "$CD/.env" HO_WEBHOOK_PORT || true)"
  [ -n "$have_port" ] && [ "$have_port" != "$want_port" ] \
    && warn "HO_WEBHOOK_PORT is $have_port but the profile assigns $want_port"
elif [ "$DRY" = 1 ]; then
  info "[dry-run] would write $CD/.env from the profile (without secrets)"
else
  umask 077
  cat > "$CD/.env" <<EOF
# Hermes conductor — $PROFILE_NAME runtime. Generated by scripts/deploy.sh from
# config/profiles/$PROFILE_NAME.vars. NOT in git.
#
# Queue state lives outside any project checkout: a project repo gets cloned, moved and cleaned,
# and the job history must not travel with it.
DATABASE_URL=file:$PROFILE_CONDUCTOR_DB

# Escalation callbacks. This port is assigned per profile — both runtimes bind the same
# loopback, so a shared value gives the port to whoever starts first and the loser's
# Approve/Deny taps go nowhere. Loopback only: an open escalation endpoint would let anyone
# on the network approve a gated action.
HO_WEBHOOK_PORT=$PROFILE_HO_WEBHOOK_PORT
HO_WEBHOOK_HOST=127.0.0.1

# Shared secret for the callback endpoint, sent as X-Telegram-Bot-Api-Secret-Token (Telegram's own
# header, so a directly-registered webhook works too). The endpoint decides gated actions for any
# escalation id, so it is CLOSED without this — loopback alone does not separate the other accounts
# on a shared box, and a forged callback used to be accepted with {"ok":true}.
HO_WEBHOOK_SECRET=$(python3 -c 'import secrets;print(secrets.token_urlsafe(32))' 2>/dev/null || openssl rand -hex 24)

# Pre-run recovery point (refs/hermes/snapshots/job-<id>). autocommit skips main/master and
# these repos work on main, so without this an autonomous run has nothing to roll back to.
HERMES_REPO_ROOT=$TREE
HO_SNAPSHOT_SH=$TREE/agents-ai/telegram-bot-agent/hermes-agent/ops/conductor-snapshot.sh

# TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID are NOT written here by deploy: they are this account's
# own credentials. Add them yourself, or let install.sh take them from
# ~/.config/ai-agent-stack/secrets.env. Never copy them from another account.
EOF
  chmod 600 "$CD/.env"
  ok "written (no credentials — add TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID yourself)"
fi

# ── 5. verify ────────────────────────────────────────────────────────────────
hdr "5/6  verify"
if [ "$DRY" = 1 ]; then info "[dry-run] typecheck + tests + doctor"
else
  ( cd "$CD" && npx --no-install tsc --noEmit ) && ok "typecheck clean" || bad "typecheck failed"
  if ( cd "$CD" && npm test >/tmp/.dep-tests.$$ 2>&1 ); then
    ok "tests pass ($(grep -c 'ok  ' /tmp/.dep-tests.$$) assertions)"
  else
    bad "tests failed"; grep -E 'FAIL' /tmp/.dep-tests.$$ | head -6 | sed 's/^/      /'
  fi
  rm -f /tmp/.dep-tests.$$
  set +e; "$REPO_ROOT/scripts/render.sh" "$PROFILE_NAME" --tree "$TREE" --check >/dev/null 2>&1; rc=$?; set -e
  [ "$rc" = 0 ] && ok "tree fully rendered" || bad "tree is not fully rendered"
fi

hdr "next"
info "1. secrets:   $SECRETS_FILE (0600) — this account's own keys only"
info "2. services:  install.sh installs units, venvs and linger"
info "3. check:     scripts/doctor.sh $PROFILE_NAME"
finish
