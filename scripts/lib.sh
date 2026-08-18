#!/usr/bin/env bash
# lib.sh — shared plumbing for the scripts in this directory. Sourced, never executed.
#
#   . "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
#   load_profile "$@"        # resolves the profile and exports its values + derived paths
#
# Everything here exists because the two runtimes on this box are NOT symmetrical, and a
# script that assumes they are reports confident nonsense. The differences that actually bite:
#
#   - systemd SCOPE differs per service per profile. The conductor is a system unit for
#     sergiy_prod and a user unit for vadim_prod, so `systemctl --user is-active
#     hermes-conductor` answers "inactive" about a service that is running fine.
#   - `systemctl --user` needs XDG_RUNTIME_DIR. Without it every query fails silently and
#     empty output reads as "not running".
#   - the conductor's DB is resolved from THREE places (unit drop-in Environment, the
#     conductor's own .env, conductor-run.sh's default), and the gateway resolves its own
#     copy independently. When they disagree nothing errors — the two halves just operate on
#     different files, which is how every escalation button on vadim_prod wrote "approved"
#     into a database no conductor was reading.
set -uo pipefail

# ── output ───────────────────────────────────────────────────────────────────
if [ -t 1 ] && [ -z "${NO_COLOR:-}" ]; then
  _C_R=$'\033[31m'; _C_G=$'\033[32m'; _C_Y=$'\033[33m'; _C_B=$'\033[1m'; _C_0=$'\033[0m'
else
  _C_R=''; _C_G=''; _C_Y=''; _C_B=''; _C_0=''
fi
FAILS=0; WARNS=0
say(){ printf '%s\n' "$*"; }
hdr(){ printf '\n%s%s%s\n' "$_C_B" "$*" "$_C_0"; }
ok(){   printf '  %s✓%s %s\n' "$_C_G" "$_C_0" "$*"; }
warn(){ printf '  %s!%s %s\n' "$_C_Y" "$_C_0" "$*"; WARNS=$((WARNS+1)); }
bad(){  printf '  %s✗%s %s\n' "$_C_R" "$_C_0" "$*"; FAILS=$((FAILS+1)); }
info(){ printf '  · %s\n' "$*"; }
die(){ printf '%s%s%s\n' "$_C_R" "error: $*" "$_C_0" >&2; exit 1; }

# Exit 0 clean, 1 if anything failed, 2 if only warnings. Cron and CI read these.
finish(){
  hdr "result"
  if [ "$FAILS" -gt 0 ]; then say "  $FAILS failed, $WARNS warning(s)"; exit 1; fi
  if [ "$WARNS" -gt 0 ]; then say "  ok with $WARNS warning(s)"; exit 2; fi
  say "  all checks passed"; exit 0
}

# ── profile ──────────────────────────────────────────────────────────────────
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Resolve the profile: explicit argument, then $AI_PROFILE, then the current account name.
# Defaulting to the account is what makes every script safe to run with no arguments as
# either user, and impossible to point at the wrong runtime by forgetting one.
load_profile(){
  local p="${1:-${AI_PROFILE:-$(id -un)}}"
  PROFILE_NAME="$p"
  PROFILE_FILE="$REPO_ROOT/config/profiles/$p.vars"
  [ -f "$PROFILE_FILE" ] || die "no profile for '$p' (looked for $PROFILE_FILE)"
  # shellcheck disable=SC1090
  set -a; . "$PROFILE_FILE"; set +a
  for v in PROFILE_USER PROFILE_HOME PROFILE_DEST PROFILE_CONDUCTOR_DB PROFILE_HO_WEBHOOK_PORT; do
    [ -n "${!v:-}" ] || die "$PROFILE_FILE is missing $v"
  done

  # Derived paths — computed once, so no script re-hardcodes the seven-level tree walk.
  CONDUCTOR_DIR="$PROFILE_DEST/agents-ai/telegram-bot-agent/claude-code-agent/DEV/dev/conductor"
  OPS_DIR="$PROFILE_DEST/agents-ai/telegram-bot-agent/hermes-agent/ops"
  PROFILES_DIR="$PROFILE_DEST/agents-ai/telegram-bot-agent/claude-code-agent/DEV/profiles"
  HERMES_HOME="$PROFILE_HOME/.hermes"
  SECRETS_FILE="$PROFILE_HOME/.config/ai-agent-stack/secrets.env"
  CONDUCTOR_DB_FILE="${PROFILE_CONDUCTOR_DB}"
  export PROFILE_NAME CONDUCTOR_DIR OPS_DIR PROFILES_DIR HERMES_HOME SECRETS_FILE CONDUCTOR_DB_FILE

  # systemctl --user is useless without this, and its failure is SILENT.
  [ -n "${XDG_RUNTIME_DIR:-}" ] || export XDG_RUNTIME_DIR="/run/user/$(id -u)"
}

# Refuse to touch another account's runtime. Every mutating script calls this: the paths in a
# profile are absolute, so running deploy/update with the wrong profile name would happily
# rewrite the other user's tree — the one thing this whole setup exists to prevent.
require_own_profile(){
  [ "$(id -un)" = "$PROFILE_USER" ] || die \
    "profile '$PROFILE_NAME' belongs to $PROFILE_USER; you are $(id -un). Run it as that user."
}

# ── rendering ────────────────────────────────────────────────────────────────
# A MIRROR of render.sh's substitution table, for the read-only scripts that source this file.
#
# render.sh owns the definition and does NOT source lib.sh: it must run on a bare clone with
# nothing else in place, and it is the one script whose failure leaves a tree unusable. Making it
# call in here proved that — an undefined function, an empty table, and a cheerful
# "fully rendered — nothing to do" over a live tree that had just been reset to template form.
#
# Before this mirror existed diff.sh had its own private copy, which silently went stale when the
# template switched to tokens: it re-rendered each pristine blob with the old rules and reported all
# 30 files as DRIFT, so update.sh refused to run. Two copies is the compromise; validate.sh asserts
# they stay byte-identical, which is what makes it a mirror rather than a second source of truth.
#
# @DEST@ FIRST: it is the longest token and its expansion contains the others' expansions.
render_sed_script(){
  printf '%s\n' \
    "s|@DEST@|$PROFILE_DEST|g" \
    "s|@HOME@|$PROFILE_HOME|g" \
    "s|@USER@|$PROFILE_USER|g"
}

# Files carrying a path token, excluding *.example — those are copied by hand, so a token there
# must survive to be replaced by the person copying it.
render_candidates(){
  grep -rlI --exclude='*.example' -e '@DEST@' -e '@HOME@' -e '@USER@' "${1:?tree}/agents-ai" 2>/dev/null | sort
}

# ── services ─────────────────────────────────────────────────────────────────
# The full set, in start order. Names only; scope is resolved per name below.
ALL_SERVICES=(hermes-qdrant llm-failover-proxy llm-failover-proxy-strong hermes-gateway hermes-conductor)

unit_scope(){
  case "$1" in
    hermes-conductor) printf '%s' "${PROFILE_UNIT_SCOPE_CONDUCTOR:-user}";;
    *)                printf '%s' "${PROFILE_UNIT_SCOPE_DEFAULT:-user}";;
  esac
}

# systemctl for one unit, in ITS scope. System-scope actions that change state need sudo;
# queries do not, so a read-only script never prompts.
sc(){
  local unit="$1"; shift
  if [ "$(unit_scope "$unit")" = system ]; then
    case "${1:-}" in
      is-active|is-enabled|show|cat|status) systemctl "$@" "$unit" 2>&1;;
      *) sudo systemctl "$@" "$unit" 2>&1;;
    esac
  else
    systemctl --user "$@" "$unit" 2>&1
  fi
}

svc_active(){ [ "$(sc "$1" is-active)" = active ]; }

# ── small helpers ────────────────────────────────────────────────────────────
port_listening(){ ss -ltn 2>/dev/null | awk '{print $4}' | grep -qE "[:.]$1\$"; }

# Read one KEY=value from a dotenv-ish file without sourcing it (never execute a secrets file).
env_get(){
  local file="$1" key="$2"
  [ -f "$file" ] || return 1
  sed -n "s/^${key}=//p" "$file" | head -1 | sed 's/^"//; s/"$//'
}

# Short hash of a secret, for comparing two values without ever printing either.
hash8(){ printf '%s' "${1:-}" | sha256sum | cut -c1-8; }

sqlite_q(){ sqlite3 "$1" "$2" 2>/dev/null; }

git_head(){ git -C "${1:-$PROFILE_DEST}" rev-parse --short HEAD 2>/dev/null; }
