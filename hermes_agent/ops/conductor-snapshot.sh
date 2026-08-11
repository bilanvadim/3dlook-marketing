#!/usr/bin/env bash
# conductor-snapshot.sh <work_dir> <job_id>
#
# Capture the work tree as a real, recoverable commit before an autonomous run —
# WITHOUT touching HEAD, the current branch, the index or the working tree.
#
# Why this and not autocommit.py: that hook deliberately skips main/master, and this
# repo works on main, so a Conductor run on main had no recovery point at all. Pattern
# guards stop `rm -rf`, but a delete inside an allowed python3 script is invisible to
# them — the only real answer is a snapshot taken before the agent starts.
#
# The snapshot is written to refs/hermes/snapshots/job-<id> using a throwaway index,
# so nothing about the checked-out state changes and main's history stays clean.
#
# Recover a file:   git show refs/hermes/snapshots/job-42:path/to/file
# Restore a file:   git checkout refs/hermes/snapshots/job-42 -- path/to/file
# See what a run changed:  git diff refs/hermes/snapshots/job-42 -- .
# List snapshots:   git for-each-ref refs/hermes/snapshots
# Drop one:         git update-ref -d refs/hermes/snapshots/job-42
#
# Exits 0 in every path on purpose: a failed snapshot must never keep a job from running.
set -uo pipefail

WORK_DIR="${1:-}"
JOB_ID="${2:-}"
if [ -z "$WORK_DIR" ] || [ -z "$JOB_ID" ]; then
  echo "conductor-snapshot: usage: conductor-snapshot.sh <work_dir> <job_id>" >&2
  exit 0
fi

cd "$WORK_DIR" 2>/dev/null || { echo "conductor-snapshot: work_dir unreadable: $WORK_DIR" >&2; exit 0; }
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || { echo "conductor-snapshot: $WORK_DIR is not a git work tree — no snapshot"; exit 0; }

TOP="$(git rev-parse --show-toplevel 2>/dev/null)" || exit 0
cd "$TOP" || exit 0

HEAD_SHA="$(git rev-parse --verify HEAD 2>/dev/null)" || { echo "conductor-snapshot: no HEAD yet — no snapshot"; exit 0; }

IDX="$(mktemp "${TMPDIR:-/tmp}/hermes-snapshot-index-XXXXXX")" || exit 0
trap 'rm -f "$IDX"' EXIT
export GIT_INDEX_FILE="$IDX"

git read-tree HEAD 2>/dev/null || exit 0
git add -A 2>/dev/null || exit 0            # honors .gitignore, so no node_modules / .env
TREE="$(git write-tree 2>/dev/null)" || exit 0

if [ "$TREE" = "$(git rev-parse "HEAD^{tree}" 2>/dev/null)" ]; then
  echo "conductor-snapshot: work tree matches HEAD — nothing to snapshot for job $JOB_ID"
  exit 0
fi

SHA="$(git commit-tree "$TREE" -p "$HEAD_SHA" -m "conductor: pre-run snapshot for job $JOB_ID" 2>/dev/null)" || exit 0
git update-ref "refs/hermes/snapshots/job-$JOB_ID" "$SHA" 2>/dev/null || exit 0
echo "conductor-snapshot: job $JOB_ID → refs/hermes/snapshots/job-$JOB_ID ($SHA)"
exit 0
