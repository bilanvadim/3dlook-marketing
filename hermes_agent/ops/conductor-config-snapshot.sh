#!/usr/bin/env bash
# conductor-config-snapshot.sh — versioned snapshots of the LIVE conductor config tree.
#
# WHY THIS EXISTS
# ---------------
# `/srv/vadim_prod/ai-agents-config` stopped being a git checkout somewhere around
# 2026-08-18 08:48 (its `.git` is simply gone; `git rev-parse` there fails). Two
# things broke at once, and only one of them is fixable from this account:
#
#   1. UPSTREAM IS UNREACHABLE. scripts/update.sh dies at its first check
#      ("not a git checkout"), so the conductor takes no upstream changes at all.
#      The canonical repo is the PRIVATE github.com/SergeMiro/ai-agents-config,
#      and nothing on this box can see it: vadim's gh token and the PAT in
#      secrets.env are both `bilanvadim` (2 repos, neither is it), and ~/.ssh/hop
#      is an internal hop key GitHub rejects. Restoring that link needs Sergiy to
#      grant access. This script does NOT pretend to fix it.
#
#   2. THE TREE LOST ITS ONLY BACKUP. This is the part that IS fixable, and it is
#      the one that can actually lose work. scripts/backup.sh snapshots
#      "everything that is NOT in git" ON PURPOSE — secrets, the ho.db queue,
#      systemd units, vector memory — because git was holding the config. Git is
#      not holding it any more, so since 2026-08-18 the config tree has had NO
#      restore point of any kind.
#
# WHY A GIT DIR OUTSIDE THE TREE, AND NOT `git init` INSIDE IT
# ------------------------------------------------------------
# Because an in-tree repo would LIE. The upstream repo stores TEMPLATES carrying
# @DEST@ / @HOME@ / @USER@ tokens; render.sh expands them, so every file in the
# deployed tree legitimately differs from its committed form. diff.sh exists to
# split that difference into "explained by the render" and "real drift", and
# update.sh refuses to reset when real drift is present. Committing the RENDERED
# state as HEAD would make diff.sh report a permanently clean tree — drift
# detection silently disabled, with the reassuring output intact.
#
# So the history lives at $SNAP_GIT with GIT_WORK_TREE pointed at the tree. The
# tree itself stays exactly as it is: no .git, update.sh keeps failing early and
# honestly, and nothing here can be mistaken for the checkout.
#
# The tree's own .gitignore is honoured (it is read from the work tree), which is
# what keeps this cheap: 586 files / ~3.2 MiB tracked, with 350 MB of node_modules
# and every *.db / .env / secret excluded by the same rules upstream uses.
#
# USAGE
#   conductor-config-snapshot.sh            # snapshot if changed; alert once if the checkout is gone
#   conductor-config-snapshot.sh --dry-run  # report what would happen, write and send nothing
#   conductor-config-snapshot.sh --log      # show snapshot history
#   conductor-config-snapshot.sh --show     # what changed in the latest snapshot
#   conductor-config-snapshot.sh --restore <file>   # print a file as of the last snapshot
# Exit: 0 ok (with or without changes) · 1 setup broken.
set -uo pipefail

TREE="${CONDUCTOR_CONFIG_TREE:-/srv/vadim_prod/ai-agents-config}"
SNAP_GIT="${CONDUCTOR_SNAP_GIT:-$HOME/.hermes/config-snapshots/tree.git}"
STATE="${CONDUCTOR_SNAP_STATE:-$HOME/.hermes/.config-snapshot-state}"
ENVF="${HERMES_ENV_FILE:-$HOME/.hermes/.env}"
MODE="${1:-run}"

[ -d "$TREE" ] || { echo "snapshot: no tree at $TREE" >&2; exit 1; }

# Never let this script's own git calls pick up ambient repo state.
export GIT_DIR="$SNAP_GIT" GIT_WORK_TREE="$TREE"
unset GIT_INDEX_FILE

g() { git -c core.fileMode=false -c gc.auto=0 "$@"; }

if [ ! -d "$SNAP_GIT" ]; then
  [ "$MODE" = "--dry-run" ] && { echo "[dry-run] would create snapshot store $SNAP_GIT"; exit 0; }
  mkdir -p "$(dirname "$SNAP_GIT")" || { echo "snapshot: cannot create store dir" >&2; exit 1; }
  chmod 700 "$(dirname "$SNAP_GIT")" 2>/dev/null
  # `git init` refuses to run with GIT_WORK_TREE in the environment ("not allowed
  # without specifying GIT_DIR"), so create the store in a clean subshell first
  # and only then let the exported pair drive the staging calls below.
  ( unset GIT_DIR GIT_WORK_TREE; git init -q --bare "$SNAP_GIT" ) \
    || { echo "snapshot: git init failed" >&2; exit 1; }
  # Bare layout, but staging needs a work tree — so core.bare must be off. The
  # work tree comes from GIT_WORK_TREE per call, never from core.worktree, so the
  # store stays portable if the path ever moves.
  g config core.bare false
  g config user.name  "conductor-config-snapshot"
  g config user.email "noreply@localhost"
fi

case "$MODE" in
  --log)  exec git --git-dir="$SNAP_GIT" log --format='%h  %ad  %s' --date=iso-local ;;
  --show) exec git --git-dir="$SNAP_GIT" show --stat --format='%h %ad%n%s' --date=iso-local ;;
  --restore)
    # Prints to stdout; it never writes into the live tree. Restoring is a
    # deliberate `> file` by a human who has read the diff first — a script that
    # silently overwrites conductor config is how you turn one bad file into two.
    # The ref defaults to HEAD but the realistic case is recovering something
    # already deleted or clobbered, which lives an earlier snapshot back.
    f="${2:?usage: --restore <path-relative-to-tree> [ref, default HEAD]}"
    exec git --git-dir="$SNAP_GIT" show "${3:-HEAD}:$f" ;;
esac

# ── the alert half: say ONCE that upstream is severed ────────────────────────
# Deduped like conductor-monitor.sh — this is a standing condition, not news
# every 24 hours. If the checkout is ever restored the key changes back and a
# later regression alerts again on its own.
notify() {
  local key="$1" text="$2"
  grep -qxF "$key" "$STATE" 2>/dev/null && return 0
  if [ "$MODE" = "--dry-run" ]; then printf '[dry-run] would alert:\n%s\n' "$text"; return 0; fi
  local bot chat
  bot=$(grep -hE '^TELEGRAM_BOT_TOKEN=' "$ENVF" 2>/dev/null | head -1 | sed 's/^TELEGRAM_BOT_TOKEN=//')
  chat=$(grep -hE '^TELEGRAM_ALLOWED_USERS=' "$ENVF" 2>/dev/null | head -1 | sed 's/^TELEGRAM_ALLOWED_USERS=//' | cut -d, -f1)
  [ -n "$bot" ] && [ -n "$chat" ] || { echo "snapshot: no telegram creds in $ENVF" >&2; return 1; }
  # --config -: keep the bot token out of argv (this runs from cron; ps is world-readable).
  # -f: without it curl exits 0 on HTTP 400/429 and the alert is marked sent forever.
  printf 'url = "https://api.telegram.org/bot%s/sendMessage"\n' "$bot" |
    curl -sf -m 15 --config - --data-urlencode "chat_id=$chat" \
         --data-urlencode "text=$text" >/dev/null || return 1
  printf '%s\n' "$key" >> "$STATE"
}
touch "$STATE" 2>/dev/null

if git -C "$TREE" rev-parse --git-dir >/dev/null 2>&1; then
  # Checkout is back — record it so a future regression alerts again.
  notify "checkout:present" "✅ Конфиг диригента снова git-чекаут: $TREE
scripts/update.sh и diff.sh опять работают. Снапшоты продолжаю вести — они дешёвые и не мешают."
else
  notify "checkout:missing" "⚠️ $TREE — НЕ git-чекаут (.git отсутствует).
scripts/update.sh падает на первой проверке, diff.sh не работает: диригент не получает upstream-изменений.
Репо github.com/SergeMiro/ai-agents-config приватное, доступа с этой машины нет ни у одного ключа — нужен доступ от Сергия.
Снапшоты конфига я веду отдельно (~/.hermes/config-snapshots), так что дерево хотя бы восстановимо."
fi

# ── the snapshot half ────────────────────────────────────────────────────────
g add -A 2>/dev/null
if g diff --cached --quiet 2>/dev/null; then
  [ "$MODE" = "--dry-run" ] && echo "[dry-run] no changes since last snapshot"
  exit 0
fi
n=$(g diff --cached --numstat | wc -l)
if [ "$MODE" = "--dry-run" ]; then
  echo "[dry-run] would snapshot $n changed file(s):"
  g diff --cached --numstat | sed 's/^/    /' | head -20
  g reset -q 2>/dev/null
  exit 0
fi
g commit -q -m "snapshot $(date -u '+%Y-%m-%d %H:%M:%S')Z — $n file(s) changed" || {
  echo "snapshot: commit failed" >&2; exit 1; }
echo "snapshot: $n file(s) — $(git --git-dir="$SNAP_GIT" rev-parse --short HEAD)"
exit 0
