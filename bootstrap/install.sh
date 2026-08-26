#!/usr/bin/env bash
# install.sh — bring a machine to the state this repository describes.
#
#   git clone <repo> && cd 3dlook-marketing && ./bootstrap/install.sh
#
# Idempotent: run it as often as you like. Every step checks before it acts, and
# re-running a healthy machine changes nothing. That matters more than it sounds —
# this is also the repair tool, so it has to be safe to point at a system that is
# half-broken in an unknown way.
#
# WHAT IT DELIBERATELY DOES NOT DO
#   * It does not write secrets. It creates ~/.config/ai-agent-stack/secrets.env
#     from the example and stops if required keys are blank. Filling them is a
#     human step, on purpose.
#   * It does not log you into Claude Code. `claude` needs an interactive OAuth
#     login against a Max/Pro subscription; a script cannot do that honestly.
#   * It does not touch ~/.hermes/ho.db. Queue state belongs to the machine, not
#     the repo, and clobbering a live queue during a "repair" would be the worst
#     possible failure mode.
#
# Usage: bootstrap/install.sh [--dry-run] [--skip-deps]
set -uo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DRY=0; SKIP_DEPS=0
for a in "$@"; do
  case "$a" in
    --dry-run)   DRY=1 ;;
    --skip-deps) SKIP_DEPS=1 ;;
    *) echo "unknown option: $a"; exit 2 ;;
  esac
done

step()  { printf '\n▶ %s\n' "$1"; }
info()  { printf '  %s\n' "$1"; }
ok()    { printf '  ✅ %s\n' "$1"; }
warn()  { printf '  ⚠️  %s\n' "$1"; }
die()   { printf '  ❌ %s\n' "$1"; exit 1; }
run()   { if [ "$DRY" = 1 ]; then printf '  [dry-run] %s\n' "$*"; else "$@"; fi; }

# ── 0. sanity ────────────────────────────────────────────────────────────────
step "Environment"
[ "$(uname -s)" = "Linux" ] || die "this installer targets Linux (found $(uname -s))"
command -v systemctl >/dev/null || die "systemd is required (systemctl not found)"
systemctl --user show-environment >/dev/null 2>&1 \
  || die "no systemd --user session. Enable lingering: sudo loginctl enable-linger $USER"
ok "Linux + systemd --user session"
info "repo: $REPO"
info "user: $USER   home: $HOME"

# ── 1. dependencies ──────────────────────────────────────────────────────────
step "Dependencies"
missing=()
for c in git python3 node npm sqlite3 curl jq; do
  command -v "$c" >/dev/null || missing+=("$c")
done
if [ ${#missing[@]} -gt 0 ]; then
  if [ "$SKIP_DEPS" = 1 ]; then
    warn "missing: ${missing[*]} (--skip-deps given, continuing)"
  elif command -v apt-get >/dev/null; then
    info "installing: ${missing[*]}"
    run sudo apt-get update -qq
    run sudo apt-get install -y "${missing[@]}"
  else
    die "missing: ${missing[*]} — install them and re-run"
  fi
else
  ok "git python3 node npm sqlite3 curl jq all present"
fi
command -v claude >/dev/null && ok "claude CLI present" \
  || warn "claude CLI missing → sudo npm i -g @anthropic-ai/claude-code, then run 'claude' and /login"
command -v hermes >/dev/null && ok "hermes CLI present" \
  || warn "hermes CLI missing → install the hermes-agent package, then 'hermes auth'"

# ── 2. directories ───────────────────────────────────────────────────────────
step "Directories"
for d in "$HOME/.hermes" "$HOME/.hermes/logs" "$HOME/.config/ai-agent-stack" \
         "$HOME/.config/systemd/user"; do
  if [ -d "$d" ]; then ok "exists: ${d/#$HOME/\~}"; else run mkdir -p "$d"; ok "created: ${d/#$HOME/\~}"; fi
done
run chmod 700 "$HOME/.config/ai-agent-stack"

# ── 3. secrets ───────────────────────────────────────────────────────────────
# Created from the example, never overwritten: a re-run must not wipe live keys.
step "Secrets"
SEC="$HOME/.config/ai-agent-stack/secrets.env"
if [ -f "$SEC" ]; then
  ok "secrets.env exists (left untouched)"
else
  run cp "$REPO/secrets.env.example" "$SEC"
  run chmod 600 "$SEC"
  warn "created secrets.env from the example — FILL IT IN, then re-run this script"
fi
if [ -f "$SEC" ] && [ "$DRY" = 0 ]; then
  blanks=()
  for k in TELEGRAM_BOT_TOKEN TELEGRAM_ALLOWED_USERS; do
    v="$(grep -E "^${k}=" "$SEC" 2>/dev/null | head -1 | cut -d= -f2- | tr -d '"'"'"' ')"
    [ -z "$v" ] && blanks+=("$k")
  done
  if [ ${#blanks[@]} -gt 0 ]; then
    warn "required keys still blank: ${blanks[*]} — Telegram will not connect until they are set"
  else
    ok "required Telegram keys present"
  fi
fi

# ── 4. conductor application ─────────────────────────────────────────────────
step "Conductor"
CDIR="$REPO/claude_code/DEV/full_stack_sm/conductor"
[ -f "$CDIR/package.json" ] || die "conductor package.json missing — incomplete clone?"
if [ -d "$CDIR/node_modules/better-sqlite3" ]; then
  ok "node_modules installed (better-sqlite3 present)"
else
  info "npm install (better-sqlite3 builds a native module, this takes a minute)"
  if [ "$DRY" = 1 ]; then info "[dry-run] (cd $CDIR && npm install)"
  else (cd "$CDIR" && npm install --no-audit --no-fund) || die "npm install failed"; fi
fi

# ── 5. systemd units ─────────────────────────────────────────────────────────
# Copied, not symlinked: a `git checkout` of a branch without these files would
# otherwise pull the unit out from under a running service.
step "systemd units"
UD="$HOME/.config/systemd/user"
SRC="$REPO/hermes_agent/ops/systemd/vadim-user"
if [ -d "$SRC" ]; then
  while IFS= read -r -d '' f; do
    rel="${f#$SRC/}"
    dst="$UD/$rel"
    run mkdir -p "$(dirname "$dst")"
    if [ -f "$dst" ] && cmp -s "$f" "$dst"; then info "unchanged: $rel"
    else run cp "$f" "$dst"; ok "installed: $rel"; fi
  done < <(find "$SRC" -type f \( -name '*.service' -o -name '*.conf' -o -name '*.timer' \) -print0)
  run systemctl --user daemon-reload
else
  warn "no unit sources at $SRC"
fi

# ── 6. cron ──────────────────────────────────────────────────────────────────
# Rewritten from scratch each run so the repo, not history, decides what is
# scheduled — but only OUR lines. Anything else in the crontab is preserved.
step "cron"
MARK="# --- 3dlook-marketing (managed by bootstrap/install.sh) ---"
NEW_CRON="$(mktemp)"
crontab -l 2>/dev/null | awk -v m="$MARK" '
  $0 == m {skip=1; next}
  skip && /^# --- end 3dlook-marketing ---$/ {skip=0; next}
  !skip {print}' > "$NEW_CRON"
{
  echo "$MARK"
  echo "*/5 * * * * HO_DB=$HOME/.hermes/ho.db $REPO/hermes_agent/ops/conductor-monitor.sh >> $HOME/.hermes/conductor-monitor.log 2>&1"
  echo "55 5 * * * $REPO/marketing_vb/scripts/check-agent-copies.py --notify --quiet >> $HOME/.hermes/logs/agent-copies.log 2>&1"
  echo "# --- end 3dlook-marketing ---"
} >> "$NEW_CRON"
if crontab -l 2>/dev/null | diff -q - "$NEW_CRON" >/dev/null 2>&1; then
  ok "crontab already correct"
else
  run crontab "$NEW_CRON"
  ok "crontab updated (managed block only; your other entries kept)"
fi
rm -f "$NEW_CRON"

# ── 7. executable bits ───────────────────────────────────────────────────────
step "Permissions"
for f in hermes_agent/ops/*.sh hermes_agent/ops/*.py bootstrap/*.sh \
         marketing_vb/scripts/*.py marketing_vb/brand-assets/style-guides/scripts/*.py; do
  for p in $REPO/$f; do [ -f "$p" ] && [ ! -x "$p" ] && run chmod +x "$p"; done
done
ok "scripts executable"

# ── 8. start ─────────────────────────────────────────────────────────────────
step "Services"
for u in hermes-gateway hermes-conductor; do
  # `systemctl … | grep -q` is wrong here: grep exits at the first match, systemctl
  # takes SIGPIPE, and under `pipefail` the whole test reads as "unit not found" —
  # which is exactly what it reported for a gateway that was running at the time.
  if systemctl --user cat "${u}.service" >/dev/null 2>&1; then
    if systemctl --user is-active --quiet "$u"; then
      run systemctl --user restart "$u"; ok "$u restarted"
    else
      run systemctl --user enable --now "$u" 2>/dev/null; ok "$u started"
    fi
  else
    warn "$u.service not installed on this machine"
  fi
done

# ── 9. health check ──────────────────────────────────────────────────────────
step "Health check"
if [ "$DRY" = 1 ]; then
  info "[dry-run] bootstrap/verify.sh"
  echo; echo "Dry run complete — nothing was changed."
  exit 0
fi
sleep 5
"$REPO/bootstrap/verify.sh"
rc=$?
echo
case $rc in
  0) echo "Install complete. System ready." ;;
  2) echo "Install complete, with warnings above. Usually: fill in secrets, or log into Claude Code." ;;
  *) echo "Install finished but the health check FAILED — read the [FAIL] lines above." ;;
esac
exit $rc
