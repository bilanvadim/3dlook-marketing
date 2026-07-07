#!/usr/bin/env bash
# install.sh — set up the Sergiy config (6 Claude Code systems + Hermes orchestrator)
# on THIS machine. Safe & idempotent: it never runs sudo or touches /etc itself —
# it prepares everything and PRINTS the privileged commands for you to review & run.
#
# Usage:
#   ./install.sh                      # checks + prepare orchestrator + render systemd units
#   ./install.sh --profile <name>     # also activate a Claude Code system now
#   ./install.sh --no-orchestrator       # skip orchestrator npm/test (Claude Code side only)
#   ./install.sh --user <u> --home <h>                      # values baked into systemd units
#
# Orchestrator state is SQLite/libSQL (default local file); no Postgres/Supabase needed.
# Profiles: dev | seo | marketing | security | marketing_vb | marketing_vb_sm
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEV_DIR="$REPO_ROOT/claude_code/DEV"
ORCHESTRATOR_DIR="$REPO_ROOT/claude_code/DEV/full_stack_sm/orchestrator"
SYSTEMD_SRC="$REPO_ROOT/hermes_agent/ops/systemd"
GEN_DIR="$SYSTEMD_SRC/generated"

PROFILE=""
DO_ORCHESTRATOR=1
SVC_USER="${SUDO_USER:-$USER}"
SVC_HOME="$HOME"

while [ $# -gt 0 ]; do
  case "$1" in
    --profile) PROFILE="$2"; shift 2 ;;
    --no-orchestrator) DO_ORCHESTRATOR=0; shift ;;
    --user) SVC_USER="$2"; shift 2 ;;
    --home) SVC_HOME="$2"; shift 2 ;;
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
for bin in node npm sqlite3; do
  have "$bin" && ok "$bin: $(command -v "$bin")" || warn "$bin NOT found (needed for the Hermes orchestrator / libSQL state)"
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
if [ "$DO_ORCHESTRATOR" = 1 ]; then
  say "3) Hermes orchestrator (autonomous worker)"
  if [ -d "$ORCHESTRATOR_DIR" ]; then
    if have npm; then
      info "installing deps (npm ci)…"
      ( cd "$ORCHESTRATOR_DIR" && (npm ci --no-audit --no-fund 2>/dev/null || npm install --no-audit --no-fund) ) && ok "deps installed"
      info "running core tests (no API/network)…"
      ( cd "$ORCHESTRATOR_DIR" && npm test >/dev/null 2>&1 ) && ok "orchestrator tests pass" || warn "orchestrator tests failed — inspect: (cd $ORCHESTRATOR_DIR && npm test)"
    else
      warn "npm missing — skipping orchestrator build"
    fi
    if [ ! -f "$ORCHESTRATOR_DIR/.env" ]; then
      cp "$ORCHESTRATOR_DIR/.env.example" "$ORCHESTRATOR_DIR/.env"
      warn "created orchestrator/.env from example — default DATABASE_URL=file:./ho.db (edit for ANTHROPIC auth / Telegram / Turso)"
    else
      ok "orchestrator/.env present"
    fi
    # create the local libSQL schema (file: mode) so the queue is ready
    if have sqlite3; then
      ( cd "$ORCHESTRATOR_DIR" && sqlite3 ho.db < sql/schema.sql ) && ok "libSQL schema applied → $ORCHESTRATOR_DIR/ho.db"
    else
      warn "sqlite3 missing — create state later: (cd $ORCHESTRATOR_DIR && sqlite3 ho.db < sql/schema.sql)"
    fi
  else
    warn "orchestrator dir not found: $ORCHESTRATOR_DIR"
  fi
else
  say "3) Hermes orchestrator — skipped (--no-orchestrator)"
fi

# ---------------------------------------------------------------------------
say "4) Render systemd units from templates"
mkdir -p "$GEN_DIR"
render() {
  local tpl="$1" out="$GEN_DIR/$(basename "${1%.template}")"
  sed -e "s#@REPO_ROOT@#$REPO_ROOT#g" \
      -e "s#@USER@#$SVC_USER#g" \
      -e "s#@HOME@#$SVC_HOME#g" \
      "$tpl" > "$out"
  ok "rendered $(basename "$out")"
}
for t in "$SYSTEMD_SRC"/*.template; do [ -e "$t" ] && render "$t"; done
info "units written to: $GEN_DIR"
info "user=$SVC_USER home=$SVC_HOME"

# ---------------------------------------------------------------------------
say "Next steps (privileged / manual) — see INSTALL.md for detail"
cat <<EOF
  # A. (done above for file: mode) orchestrator state = SQLite/libSQL. Networked/Turso
  #    instead? set DATABASE_URL=libsql://… in orchestrator/.env and load the schema:
  #      turso db shell <db> < "$ORCHESTRATOR_DIR/sql/schema.sql"

  # B. Install the orchestrator service (review the rendered unit first):
  sudo cp "$GEN_DIR/hermes-orchestrator.service" /etc/systemd/system/
  sudo systemctl daemon-reload && sudo systemctl enable --now hermes-orchestrator

  # C. Orchestrator push-notifier (open questions/escalations/done → Telegram), cron every 5 min:
  ( crontab -l 2>/dev/null; echo "*/5 * * * * $REPO_ROOT/hermes_agent/ops/orchestrator-monitor.sh >> \$HOME/.hermes/orchestrator-monitor.log 2>&1" ) | crontab -

  # D. Enqueue a job (profile ∈ the 6 systems):
  sqlite3 "$ORCHESTRATOR_DIR/ho.db" "insert into ho_jobs(kind,title,prompt,profile,work_dir) values('feature','smoke','say hi','marketing_vb_sm','$REPO_ROOT');"
EOF
ok "install.sh done"
