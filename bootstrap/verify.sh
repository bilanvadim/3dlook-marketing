#!/usr/bin/env bash
# verify.sh — is this machine's Hermes/Claude-Code ecosystem actually healthy,
# and is it independent of /srv/…/ai-agents-config?
#
# Run it after a bootstrap, after `hermes update`, and any time something feels
# wrong. It only READS: nothing here starts, stops, installs or edits anything, so
# it is safe to run against production at any moment.
#
# WHY THE INDEPENDENCE CHECKS ARE IN A HEALTH SCRIPT AT ALL
# --------------------------------------------------------
# /srv/vadim_prod/ai-agents-config is a different system (Sergiy's). Until
# 2026-08-26 this repo's conductor, its cron monitor and its DAILY UPDATE all
# reached into that tree. The update was the dangerous one: it re-copied SOUL.md,
# the vendored patch appliers and the model-router out of /srv every morning, so
# the dependency came BACK on its own after any manual cleanup. A one-time audit
# cannot hold that; a check that runs regularly can.
#
# Usage: bootstrap/verify.sh [--quiet]
# Exit:  0 all green · 1 at least one FAIL · 2 warnings only.
set -uo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LEGACY_TREE="/srv/vadim_prod/ai-agents-config"
QUIET=0; [ "${1:-}" = "--quiet" ] && QUIET=1

fails=0; warns=0
ok()   { [ "$QUIET" = 1 ] || printf '[OK]   %s\n' "$1"; }
warn() { printf '[WARN] %s\n' "$1"; warns=$((warns+1)); }
fail() { printf '[FAIL] %s\n' "$1"; fails=$((fails+1)); }
hdr()  { [ "$QUIET" = 1 ] || printf '\n── %s\n' "$1"; }

# ── 1. services ──────────────────────────────────────────────────────────────
hdr "Services"
for u in hermes-gateway hermes-conductor; do
  if systemctl --user is-active --quiet "$u"; then ok "$u active"
  else fail "$u NOT active (systemctl --user status $u)"; fi
done

# ── 2. the conductor must be OUR conductor ───────────────────────────────────
# Checking the unit file is not enough: a drop-in can override WorkingDirectory,
# which is exactly how the runtime ended up in /srv while the base unit still
# named this repo. Ask the RUNNING process where it actually is.
hdr "Conductor runs from this repo"
CPID="$(systemctl --user show hermes-conductor -p MainPID --value 2>/dev/null)"
if [ -n "${CPID:-}" ] && [ "$CPID" != "0" ] && [ -e "/proc/$CPID/cwd" ]; then
  cwd="$(readlink -f "/proc/$CPID/cwd" 2>/dev/null)"
  case "$cwd" in
    "$REPO"/*) ok "conductor cwd inside repo (${cwd#$REPO/})" ;;
    *)         fail "conductor cwd is OUTSIDE this repo: $cwd" ;;
  esac
else
  fail "conductor has no running main process"
fi

# ── 3. independence from the legacy tree ─────────────────────────────────────
hdr "Independence from ai-agents-config"
if [ -e "$LEGACY_TREE" ]; then
  warn "$LEGACY_TREE still exists — presence alone is fine, the checks below are what matter"
else
  ok "$LEGACY_TREE absent"
fi

# systemd: only LIVE directives count, comments explaining the history are fine.
live_srv=0
for f in "$HOME"/.config/systemd/user/*.service "$HOME"/.config/systemd/user/*.d/*.conf; do
  [ -f "$f" ] || continue
  if grep -v '^[[:space:]]*#' "$f" 2>/dev/null | grep -q "$LEGACY_TREE"; then
    fail "live systemd directive points at legacy tree: $f"; live_srv=1
  fi
done
[ "$live_srv" = 0 ] && ok "no systemd unit or drop-in points at the legacy tree"

if crontab -l 2>/dev/null | grep -v '^[[:space:]]*#' | grep -q "$LEGACY_TREE"; then
  fail "crontab still runs something from the legacy tree"
else
  ok "crontab free of the legacy tree"
fi

# The daily update is the one that used to re-acquire the dependency.
if grep -v '^[[:space:]]*#' "$REPO/hermes_agent/ops/hermes-update.py" 2>/dev/null | grep -q "$LEGACY_TREE"; then
  fail "hermes-update.py still pulls from the legacy tree — it would come back tomorrow 06:01"
else
  ok "hermes-update.py sources everything from this repo"
fi

if find "$HOME" -maxdepth 4 -type l -lname "${LEGACY_TREE}*" 2>/dev/null | grep -q .; then
  fail "symlink(s) under \$HOME point into the legacy tree"
else
  ok "no symlinks into the legacy tree"
fi

# ── 4. the pieces the pipelines shell out to ─────────────────────────────────
hdr "Executables the pipelines depend on"
for f in \
  "hermes_agent/ops/mvb-run.py" \
  "hermes_agent/ops/conductor-monitor.sh" \
  "hermes_agent/ops/conductor-run.sh" \
  "hermes_agent/ops/mvb-verify-job.py" \
  "marketing_vb/scripts/ahrefs-keywords.py" \
  "marketing_vb/scripts/check-agent-copies.py" \
  "marketing_vb/brand-assets/style-guides/scripts/detect-ai-tells.py" ; do
  if [ -x "$REPO/$f" ]; then ok "$f"
  elif [ -f "$REPO/$f" ]; then warn "$f present but not executable"
  else fail "$f MISSING"; fi
done

# ── 5. conductor app is installed and buildable ──────────────────────────────
hdr "Conductor application"
CDIR="$REPO/claude_code/DEV/full_stack_sm/conductor"
[ -f "$CDIR/package.json" ] && ok "package.json present" || fail "conductor package.json missing"
[ -d "$CDIR/node_modules" ] && ok "node_modules installed" || fail "node_modules missing — run: (cd $CDIR && npm install)"
if [ -d "$CDIR/node_modules/better-sqlite3" ]; then ok "better-sqlite3 present"
else fail "better-sqlite3 missing — the source needs it (@libsql/client leaked and OOM-killed the box 2026-08-14)"; fi

# ── 6. agent copies must not have drifted ────────────────────────────────────
hdr "Agent definitions"
if [ -x "$REPO/marketing_vb/scripts/check-agent-copies.py" ]; then
  if out="$("$REPO/marketing_vb/scripts/check-agent-copies.py" --quiet 2>&1)"; then
    ok "every agent identical across its copies"
  else
    fail "agent copies have drifted — run marketing_vb/scripts/check-agent-copies.py"
  fi
fi

# ── 7. secrets present but NOT in git ────────────────────────────────────────
hdr "Secrets"
SEC="$HOME/.config/ai-agent-stack/secrets.env"
if [ -f "$SEC" ]; then
  perm="$(stat -c '%a' "$SEC" 2>/dev/null)"
  [ "$perm" = "600" ] && ok "secrets.env present, mode 600" || warn "secrets.env mode is $perm, expected 600"
else
  fail "secrets.env missing — copy config/secrets.env.example and fill it in"
fi
if git -C "$REPO" ls-files --error-unmatch "$SEC" >/dev/null 2>&1; then
  fail "secrets.env is TRACKED IN GIT"
else
  ok "no secrets file tracked in git"
fi

# ── 8. repository shape ──────────────────────────────────────────────────────
hdr "Repository"
br="$(git -C "$REPO" rev-parse --abbrev-ref HEAD 2>/dev/null)"
[ "$br" = "main" ] && ok "on branch main" || warn "on branch '$br', expected main"
# `branch -r` prints "origin/HEAD -> origin/main" as a row; without stripping the
# arrow form it reads as a phantom branch called "origin".
extra="$(git -C "$REPO" branch -r --format='%(refname:short)' 2>/dev/null \
          | grep -vE '^origin/HEAD$|^origin$|^origin/main$' | tr '\n' ' ')"
[ -z "$extra" ] && ok "no extra remote branches" || warn "extra remote branches: $extra"

# ── verdict ──────────────────────────────────────────────────────────────────
echo
if [ "$fails" -gt 0 ]; then
  echo "SYSTEM NOT READY — $fails failure(s), $warns warning(s)"; exit 1
elif [ "$warns" -gt 0 ]; then
  echo "SYSTEM READY (with $warns warning(s))"; exit 2
fi
echo "SYSTEM READY"
