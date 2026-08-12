#!/usr/bin/env bash
# hermes-conductor-guard
# ----------------------------------------------------------------------------
# Kills ROGUE conductor.ts processes that are NOT managed by the systemd
# `hermes-conductor.service` unit. Rogues get spawned when an autonomous agent
# self-restarts the conductor via nohup/terminal (instead of `systemctl --user
# restart hermes-conductor`). They reparent to init or live under the gateway
# cgroup, squat TCP :3001, and make the managed unit crash-loop with EADDRINUSE
# (+ SQLITE_BUSY from two conductors fighting the DB).
# See memory: project_hermes_gateway_wedge_dup_conductor
#
# SAFETY (triple guard — a false kill of the legit conductor must be impossible):
#   1. path   : only conductor.ts under Vadim's conductor dir (never /srv/sergiy_prod/*)
#   2. owner  : only processes owned by uid 1006 (vadim_prod)
#   3. cgroup : SKIP any pid whose cgroup contains `hermes-conductor.service`
#               (that IS the systemd-managed one — the whole point is to keep it)
#
# Dry run: DRY_RUN=1 /home/vadim_prod/.hermes/conductor-guard/hermes-conductor-guard.sh
# ----------------------------------------------------------------------------
set -uo pipefail

# 2026-08-12: the managed conductor moved to the CANONICAL tree, so the path guard has to
# cover BOTH — the old project checkout (where a stray nohup could still be started from) and
# the new runtime dir. Left as only the old path, this guard silently stopped catching anything:
# a rogue from /srv/vadim_prod/... failed the path test and kept squatting :3001.
# The cgroup test below is what protects the LEGIT managed process in either location.
VADIM_CONDUCTOR_DIRS=(
  "/srv/vadim_prod/ai-agents-config/agents-ai/telegram-bot-agent/claude-code-agent/DEV/dev/conductor"
  "/home/vadim_prod/3dlook-marketing/claude_code/DEV/full_stack_sm/conductor"
)
VADIM_UID=1006
DRY_RUN="${DRY_RUN:-0}"
ts() { date -u '+%Y-%m-%dT%H:%M:%SZ'; }

rogues=()
for pid in $(pgrep -f "src/core/conductor.ts" 2>/dev/null); do
  [ -d "/proc/$pid" ] || continue

  # (0) exe guard — must be an actual node process, not a shell/editor/grep that
  # merely mentions the path (pgrep -f matches any cmdline containing the string)
  [ "$(cat "/proc/$pid/comm" 2>/dev/null)" = "node" ] || continue

  # (1) path guard — must be Vadim's conductor, never Sergiy's (/srv/sergiy_prod/*)
  cmdline="$(tr '\0' ' ' < "/proc/$pid/cmdline" 2>/dev/null)" || continue
  match=0
  for d in "${VADIM_CONDUCTOR_DIRS[@]}"; do
    case "$cmdline" in *"$d"*) match=1; break ;; esac
  done
  [ "$match" = 1 ] || continue

  # (2) owner guard — must be uid 1006
  puid="$(awk '/^Uid:/{print $2; exit}' "/proc/$pid/status" 2>/dev/null)"
  [ "$puid" = "$VADIM_UID" ] || continue

  # (3) cgroup guard — the systemd-managed conductor lives in hermes-conductor.service; keep it
  cg="$(cat "/proc/$pid/cgroup" 2>/dev/null)" || continue
  case "$cg" in
    *hermes-conductor.service*) continue ;;   # legit — leave alone
  esac

  rogues+=("$pid")
done

if [ "${#rogues[@]}" -eq 0 ]; then
  echo "$(ts) conductor-guard: OK — no rogue conductor (managed unit only)"
  exit 0
fi

echo "$(ts) conductor-guard: found ${#rogues[@]} rogue conductor pid(s): ${rogues[*]}"
if [ "$DRY_RUN" = "1" ]; then
  for pid in "${rogues[@]}"; do
    echo "  [dry-run] would kill pid=$pid cgroup=$(cat /proc/$pid/cgroup 2>/dev/null)"
  done
  exit 0
fi

# TERM first, then KILL survivors after a grace period
for pid in "${rogues[@]}"; do kill -TERM "$pid" 2>/dev/null && echo "  TERM $pid"; done
sleep 3
for pid in "${rogues[@]}"; do
  if [ -d "/proc/$pid" ]; then kill -KILL "$pid" 2>/dev/null && echo "  KILL $pid (survived TERM)"; fi
done

# Port freed — make sure the managed unit is up (systemd auto-restarts within 5s,
# but nudge it in case it had given up / was stopped).
sleep 2
systemctl --user reset-failed hermes-conductor.service 2>/dev/null
systemctl --user start hermes-conductor.service 2>/dev/null
echo "$(ts) conductor-guard: cleaned ${#rogues[@]} rogue(s); ensured hermes-conductor.service is up"
exit 0
