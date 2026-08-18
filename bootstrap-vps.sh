#!/usr/bin/env bash
# =============================================================================
# bootstrap-vps.sh — stand up the whole Telegram-bot AI agent on a fresh VPS.
#
#   Hermes Agent (orchestrator + Telegram bot)  +  Claude Code Agent (systems).
#
# Idempotent. Does every MECHANICAL step; STOPS with a checklist for the parts
# only a human can do (fill secrets, enroll Telegram/MTProto/userbot, hermes auth).
#
#   bash bootstrap-vps.sh              # LIVE — actually installs
#   bash bootstrap-vps.sh --dry-run    # preview only: prints what it WOULD do
#                                       # + the TODO checklist, mutates NOTHING
#
# Full manual reference: agents-ai/telegram-bot-agent/hermes-agent/SETUP.md
#                        agents-ai/telegram-bot-agent/claude-code-agent/INSTALL.md
# =============================================================================
set -uo pipefail

DRY=false
# SKIP_CLAUDE exists because install.sh --skip-claude has to reach section 7 —
# that is where ~/.mcp.json and the whole ~/.claude tree get scaffolded. install.sh
# computed a flag for this and then never passed it anywhere, so the documented
# "don't scaffold the Claude Code side" did nothing.
SKIP_CLAUDE=false
while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run|-n) DRY=true ;;
    --skip-claude) SKIP_CLAUDE=true ;;
    --help|-h) sed -n '2,18p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    "") ;;
    *) echo "unknown arg: $1 (use --dry-run, --skip-claude or --help)"; exit 2 ;;
  esac
  shift
done

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BOT="$REPO_ROOT/agents-ai/telegram-bot-agent"
HSRC="$BOT/hermes-agent"
CSRC="$BOT/claude-code-agent"
HHOME="${HERMES_HOME:-$HOME/.hermes}"
TODO=()

c(){ printf '\n\033[1;36m▶ %s\033[0m\n' "$*"; }
ok(){ printf '  \033[1;32m✓\033[0m %s\n' "$*"; }
warn(){ printf '  \033[1;33m⚠\033[0m %s\n' "$*"; }
todo(){ TODO+=("$*"); }
# run — execute in LIVE mode, print-only in DRY mode. Mutating ops go through this.
run(){ if $DRY; then printf '  \033[2m[would] %s\033[0m\n' "$*"; else "$@"; fi; }
copy_if_absent(){ # src dst — copy template to real config only if real is missing
  if [ -e "$2" ]; then ok "exists, kept: ${2/#$HOME/~}"
  else
    if $DRY; then printf '  \033[2m[would] create %s from %s\033[0m\n' "${2/#$HOME/~}" "$(basename "$1")"
    else cp "$1" "$2"; warn "created from template — FILL IT: ${2/#$HOME/~}"; fi
    todo "Fill ${2/#$HOME/~} (from $(basename "$1"))"
  fi
}

if $DRY; then printf '\033[1;33m===== DRY-RUN — no changes will be made =====\033[0m\n'
else printf '\033[1;32m===== LIVE install =====\033[0m\n'; fi
echo "repo:  $REPO_ROOT"
echo "hermes home: $HHOME"

# --- 0. prereqs -------------------------------------------------------------
c "0. Prereqs"
for bin in python3 git; do command -v "$bin" >/dev/null && ok "$bin" || { echo "MISSING: $bin"; exit 1; }; done
command -v npx >/dev/null && ok "node/npx" || { warn "node/npx missing — needed for MCP + Claude Code"; todo "Install Node.js (npx)"; }
command -v claude >/dev/null && ok "claude CLI" || { warn "claude CLI missing"; todo "sudo npm i -g @anthropic-ai/claude-code"; }
run mkdir -p "$HHOME"

# --- 1. upstream hermes-agent ----------------------------------------------
c "1. Upstream hermes-agent"
if [ -d "$HHOME/hermes-agent" ] && [ -x "$HHOME/hermes-agent/venv/bin/python" ]; then
  ok "hermes-agent present at ~/.hermes/hermes-agent"
else
  warn "hermes-agent not installed — follow SETUP.md §2 (install upstream into ~/.hermes/hermes-agent), then re-run"
  todo "Install upstream hermes-agent per hermes-agent/SETUP.md §2"
fi

# --- 2. config scaffolding (never clobber real secrets) ---------------------
c "2. Config (templates -> real, only if missing)"
copy_if_absent "$HSRC/.env.example"          "$HHOME/.env"
copy_if_absent "$HSRC/config.yaml.example"   "$HHOME/config.yaml"
copy_if_absent "$HSRC/mem0.json.example"     "$HHOME/mem0.json"
run cp "$HSRC/SOUL.md" "$HHOME/SOUL.md"; $DRY || ok "SOUL.md (canonical persona) copied"
$DRY || for f in "$HHOME/.env" "$HHOME/config.yaml" "$HHOME/mem0.json"; do [ -e "$f" ] && chmod 600 "$f"; done

# --- 3. ops into runtime ----------------------------------------------------
c "3. Ops scripts -> ~/.hermes"
run mkdir -p "$HHOME/model-router" "$HHOME/scripts"
run cp -t "$HHOME/model-router/" "$HSRC/ops/model-router/refresh.py" "$HSRC/ops/model-router/router_lib.py" "$HSRC/ops/model-router/model-strength.json"
run cp -t "$HHOME/" "$HSRC/ops/vault-sync.sh" "$HSRC/ops/hermes-update.py"
run cp -t "$HHOME/scripts/" "$HSRC/ops/scripts/cleanup_hanging_procs.py"
$DRY || ok "model-router + vault-sync + hermes-update + maintenance staged"
# runtime helpers — CODE only (secrets stay templates; enroll separately)
for comp in conductor-bridge mtproto telegram-userbot; do
  run mkdir -p "$HHOME/$comp"
  for py in "$HSRC/ops/$comp/"*.py; do [ -e "$py" ] && run cp "$py" "$HHOME/$comp/"; done
  [ -f "$HSRC/ops/$comp/search.sh" ] && run cp "$HSRC/ops/$comp/search.sh" "$HHOME/$comp/"
  for ex in "$HSRC/ops/$comp/"*.example; do [ -e "$ex" ] || continue; copy_if_absent "$ex" "$HHOME/$comp/$(basename "${ex%.example}")"; done
done
$DRY || ok "conductor-bridge / mtproto / telegram-userbot code staged"

# --- 4. skills --------------------------------------------------------------
c "4. Skills -> ~/.hermes/skills"
run mkdir -p "$HHOME/skills/autonomous-ai-agents" "$HHOME/skills/devops"
run cp -r "$HSRC/skills/vps-orchestration" "$HHOME/skills/autonomous-ai-agents/"
for s in telegram-userbot-vps vps-maintenance; do run cp -r "$HSRC/skills/$s" "$HHOME/skills/devops/"; done
run cp -r "$HSRC/skills/claude-code-hermes" "$HHOME/skills/"
$DRY || ok "vps-orchestration, telegram-userbot-vps, vps-maintenance, claude-code-hermes"

# --- 5. patchers (require hermes-agent installed) ---------------------------
c "5. Apply switcher + file-tool-guard patches"
if [ -d "$HHOME/hermes-agent/gateway" ]; then
  run python3 "$HSRC/ops/claude-switcher/apply-claude-switcher-patch.py"
  run python3 "$HSRC/ops/apply-file-tool-guard.py"
  $DRY || ok "patches applied (re-run is idempotent)"
else
  warn "skipping patches — hermes-agent not installed yet"; todo "After installing hermes-agent, re-run to apply patches"
fi

# --- 6. systemd user units + crontab ---------------------------------------
c "6. systemd user units + crontab"
run mkdir -p "$HOME/.config/systemd/user"
for u in "$HSRC/ops/systemd/"*.service "$HSRC/ops/systemd/"*.timer; do [ -e "$u" ] && run cp "$u" "$HOME/.config/systemd/user/"; done
warn "Review units in ~/.config/systemd/user/ (paths must match this checkout), then:"
echo "     systemctl --user daemon-reload && systemctl --user enable --now hermes-gateway model-router-refresh.timer hermes-update.timer vault-sync.timer"
todo "daemon-reload + enable systemd units (gateway/model-router/update/vault-sync[/conductor])"
MON="$HSRC/ops/conductor-monitor.sh"
if crontab -l 2>/dev/null | grep -qF "$MON"; then ok "conductor-monitor cron present"
else warn "conductor-monitor cron not present"; todo "crontab: */5 * * * * $MON >> $HHOME/conductor-monitor.log 2>&1"; fi

# --- 7. Claude Code side ----------------------------------------------------
if $SKIP_CLAUDE; then
  c "7. Claude Code agent — ПРОПУЩЕНО (--skip-claude)"
else
c "7. Claude Code agent (systems / MCP / settings)"
run mkdir -p "$HOME/.claude"
copy_if_absent "$CSRC/config/project-mcp.json.example"       "$HOME/.mcp.json"
copy_if_absent "$CSRC/config/settings.json.example"          "$HOME/.claude/settings.json"
copy_if_absent "$CSRC/config/settings.local.json.example"    "$HOME/.claude/settings.local.json"
if [ -e "$HOME/.claude/.active-profile" ]; then ok "exists, kept: ~/.claude/.active-profile"
else run bash -c "printf 'dev\n' > '$HOME/.claude/.active-profile'"; fi
command -v codebase-memory-mcp >/dev/null && ok "codebase-memory binary present" || \
  todo "Install codebase-memory: curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh | bash -s -- --skip-config (then config set auto_index true / auto_watch false)"
todo "Run: claude-code-agent/DEV/switch-profile.sh dev   (systems: dev|seo|marketing|security|test), restart Claude Code"
todo "Replace 'YOUR_USER' in ~/.claude/settings.json + fill token placeholders in ~/.mcp.json / user-mcp"
fi   # end --skip-claude

# --- 8. human checklist -----------------------------------------------------
c "8. REMAINING — human steps (secrets & enrollment)"
todo "hermes auth   (provider OAuth -> ~/.hermes/auth.json)"
todo "Enroll MTProto session (forward-picker): ops/mtproto/README.md"
todo "Enroll Telegram userbot session: ops/telegram-userbot/README.md ; chmod 600 session.session"
todo "Recreate Hermes cron jobs: cron/jobs.json.example -> ~/.hermes/cron/jobs.json (chmod 600)"

printf '\n\033[1;35m==== TODO ( %d ) ====\033[0m\n' "${#TODO[@]}"
i=1; for t in "${TODO[@]}"; do printf '  %2d. %s\n' "$i" "$t"; i=$((i+1)); done
if $DRY; then printf '\n\033[1;33mDRY-RUN complete — nothing changed.\033[0m Re-run without --dry-run to install.\n'
else printf '\n\033[1;32mMechanical bootstrap done.\033[0m Finish the TODO list, then verify per SETUP.md.\n'; fi
