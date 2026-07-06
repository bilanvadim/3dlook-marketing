#!/usr/bin/env bash
# install.sh — set up the Sergiy config (6 Claude Code systems + Hermes orchestrator)
# on THIS machine. Safe & idempotent: it never runs sudo or touches /etc itself —
# it prepares everything and PRINTS the privileged commands for you to review & run.
#
# Usage:
#   ./install.sh                      # checks + prepare conductor + render systemd units
#   ./install.sh --profile <name>     # also activate a Claude Code system now
#   ./install.sh --no-conductor       # skip conductor npm/test (Claude Code side only)
#   ./install.sh --user <u> --home <h> --stack-env <path>   # values baked into systemd units
#
# Profiles: dev | seo | marketing | security | marketing_vb | marketing_vb_sm
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEV_DIR="$REPO_ROOT/claude_code/DEV"
CONDUCTOR_DIR="$REPO_ROOT/claude_code/DEV/full_stack_sm/conductor"
SYSTEMD_SRC="$REPO_ROOT/hermes_agent/ops/systemd"
GEN_DIR="$SYSTEMD_SRC/generated"

PROFILE=""
DO_CONDUCTOR=1
SVC_USER="${SUDO_USER:-$USER}"
SVC_HOME="$HOME"
STACK_ENV="${STACK_ENV:-/path/to/supabase/stack/.env}"

while [ $# -gt 0 ]; do
  case "$1" in
    --profile) PROFILE="$2"; shift 2 ;;
    --no-conductor) DO_CONDUCTOR=0; shift ;;
    --user) SVC_USER="$2"; shift 2 ;;
    --home) SVC_HOME="$2"; shift 2 ;;
    --stack-env) STACK_ENV="$2"; shift 2 ;;
    -h|--help) grep '^#' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

say()  { printf '\n\033[1m== %s\033[0m\n' "$*"; }
ok()   { printf '  \033[32m✓\033[0m %s\n' "$*"; }
warn() { printf '  \033[33m!\033[0m %s\n' "$*"; }
info() { printf '    %s\n' "$*"; }

say "Repo root: $REPO_ROOT"

# ---------------------------------------------------------------------------
say "1) Dependency check"
have() { command -v "$1" >/dev/null 2>&1; }
for bin in claude python3; do
  have "$bin" && ok "$bin: $(command -v "$bin")" || warn "$bin NOT found (required for Claude Code systems)"
done
for bin in node npm docker psql; do
  have "$bin" && ok "$bin: $(command -v "$bin")" || warn "$bin NOT found (needed for the Hermes conductor)"
done

# ---------------------------------------------------------------------------
say "2) Claude Code systems (6 profiles)"
if [ -x "$DEV_DIR/switch-profile.sh" ]; then
  ok "switcher: $DEV_DIR/switch-profile.sh"
  info "available: $(ls "$DEV_DIR/profiles"/*.json | xargs -n1 basename | sed 's/\.json//' | tr '\n' ' ')"
  if [ -n "$PROFILE" ]; then
    say "   activating profile: $PROFILE"
    "$DEV_DIR/switch-profile.sh" "$PROFILE"
  else
    info "activate later: $DEV_DIR/switch-profile.sh <profile>   (then restart Claude Code)"
  fi
else
  warn "switch-profile.sh not found/executable at $DEV_DIR"
fi

# ---------------------------------------------------------------------------
if [ "$DO_CONDUCTOR" = 1 ]; then
  say "3) Hermes conductor (autonomous worker)"
  if [ -d "$CONDUCTOR_DIR" ]; then
    if have npm; then
      info "installing deps (npm ci)…"
      ( cd "$CONDUCTOR_DIR" && (npm ci --no-audit --no-fund 2>/dev/null || npm install --no-audit --no-fund) ) && ok "deps installed"
      info "running core tests (no API/network)…"
      ( cd "$CONDUCTOR_DIR" && npm test >/dev/null 2>&1 ) && ok "conductor tests pass" || warn "conductor tests failed — inspect: (cd $CONDUCTOR_DIR && npm test)"
    else
      warn "npm missing — skipping conductor build"
    fi
    if [ ! -f "$CONDUCTOR_DIR/.env" ]; then
      cp "$CONDUCTOR_DIR/.env.example" "$CONDUCTOR_DIR/.env"
      warn "created conductor/.env from example — EDIT IT (DATABASE_URL, ANTHROPIC auth, Telegram)"
    else
      ok "conductor/.env present"
    fi
  else
    warn "conductor dir not found: $CONDUCTOR_DIR"
  fi
else
  say "3) Hermes conductor — skipped (--no-conductor)"
fi

# ---------------------------------------------------------------------------
say "4) Render systemd units from templates"
mkdir -p "$GEN_DIR"
render() {
  local tpl="$1" out="$GEN_DIR/$(basename "${1%.template}")"
  sed -e "s#@REPO_ROOT@#$REPO_ROOT#g" \
      -e "s#@USER@#$SVC_USER#g" \
      -e "s#@HOME@#$SVC_HOME#g" \
      -e "s#@STACK_ENV@#$STACK_ENV#g" \
      "$tpl" > "$out"
  ok "rendered $(basename "$out")"
}
for t in "$SYSTEMD_SRC"/*.template; do [ -e "$t" ] && render "$t"; done
info "units written to: $GEN_DIR"
info "user=$SVC_USER home=$SVC_HOME stack-env=$STACK_ENV"
[ "$STACK_ENV" = "/path/to/supabase/stack/.env" ] && warn "STACK_ENV is a placeholder — re-run with --stack-env <path> or set DATABASE_URL in conductor/.env"

# ---------------------------------------------------------------------------
say "Next steps (privileged / manual) — see INSTALL.md for detail"
cat <<EOF
  # A. Apply the conductor DB schema (hc_* tables) to your Postgres:
  psql "\$DATABASE_URL" -f "$CONDUCTOR_DIR/sql/schema.sql"
  psql "\$DATABASE_URL" -f "$CONDUCTOR_DIR/sql/002_steps_questions.sql"
  psql "\$DATABASE_URL" -f "$CONDUCTOR_DIR/sql/003_profiles.sql"

  # B. Install the conductor service (review the rendered unit first):
  sudo cp "$GEN_DIR/hermes-conductor.service" /etc/systemd/system/
  sudo systemctl daemon-reload && sudo systemctl enable --now hermes-conductor

  # C. Conductor push-notifier (open questions/escalations/done → Telegram), cron every 5 min:
  ( crontab -l 2>/dev/null; echo "*/5 * * * * $REPO_ROOT/hermes_agent/ops/conductor-monitor.sh >> \$HOME/.hermes/conductor-monitor.log 2>&1" ) | crontab -

  # D. Enqueue a job (profile ∈ the 6 systems):
  psql "\$DATABASE_URL" -c "insert into hc_jobs(kind,title,prompt,profile,work_dir) values('feature','smoke','say hi','marketing_vb_sm','$REPO_ROOT');"
EOF
ok "install.sh done"
