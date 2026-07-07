#!/usr/bin/env bash
# dispatch-in-profile.sh — switch to a profile, VERIFY it, then run a command
# under it, holding a lock so concurrent ad-hoc switches can't race the global
# ~/.claude/settings.json. This makes the "switch" step mechanical: it cannot be
# silently skipped, and a failed/wrong switch aborts before the task runs.
#
# Usage:
#   dispatch-in-profile.sh <profile> -- <command...>   # switch+verify, then run command
#   dispatch-in-profile.sh <profile>                   # switch+verify only (e.g. prep interactive)
#
# Example (Hermes headless):
#   dispatch-in-profile.sh marketing -- claude -p 'plan a launch campaign' \
#       --output-format json --max-turns 30 --dangerously-skip-permissions
#
# Notes:
# - Headless `claude -p` is a fresh process, so no restart is needed — this
#   switch takes effect for the command run here.
# - For the human's interactive TUI, use switch-profile.sh + restart instead.
# - For concurrent multi-profile work, use the orchestrator (ho_jobs.profile), NOT
#   this global toggle.
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOCK="${TMPDIR:-/tmp}/hermes-profile-switch.lock"

profile="${1:-}"
[[ -n "$profile" ]] || { echo "usage: $0 <profile> [-- <command...>]" >&2; exit 2; }
shift || true
[[ -f "$DIR/profiles/$profile.json" ]] || { echo "ERROR: unknown profile '$profile' (see: $DIR/switch-profile.sh --list)" >&2; exit 2; }

# strip a leading '--' separator if present
[[ "${1:-}" == "--" ]] && shift || true

# Serialize global-settings switches. Hold the lock across switch+verify+run so a
# second dispatch waits rather than clobbering settings mid-task.
exec 9>"$LOCK"
if ! flock -w 900 9; then
  echo "ERROR: could not acquire profile lock within 900s ($LOCK)" >&2; exit 1
fi

echo "[dispatch] switching → $profile" >&2
"$DIR/switch-profile.sh" "$profile" >&2

active="$("$DIR/switch-profile.sh" --current)"
if [[ "$active" != "$profile" ]]; then
  echo "ERROR: profile verify failed — active='$active', expected '$profile'. Aborting before dispatch." >&2
  exit 1
fi
echo "[dispatch] verified active profile: $active" >&2

# No command → switch+verify only.
if (( $# == 0 )); then
  echo "[dispatch] no command given; profile is set. (interactive: restart Claude Code)" >&2
  exit 0
fi

echo "[dispatch] running under '$profile': $*" >&2
"$@"   # lock released on exit
