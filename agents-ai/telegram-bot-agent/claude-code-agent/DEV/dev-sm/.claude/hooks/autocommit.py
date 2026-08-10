#!/usr/bin/env python3
"""Hermes auto-commit hook (Stop event).

After every agent turn that left changes, commit + push the current branch.
Push triggers Vercel's Git integration → automatic deploy. Never merges.

Safety rails:
  - Skips the default branches main/master (never auto-push there).
  - Skips when there are no changes.
  - Skips if a `.git/HERMES_NO_AUTOPUSH` flag file exists (manual escape hatch).
  - Force-push stays blocked by guard.py; this only does a plain push.

Hook contract: reads JSON from stdin (ignored), exit 0 always (never break the
session on a git hiccup — a failed push is logged to stderr, not fatal).
"""
import json, os, subprocess, sys

def run(*args):
    return subprocess.run(args, capture_output=True, text=True)

def main():
    try:
        json.load(sys.stdin)  # consume payload; we don't need fields from it
    except Exception:
        pass

    proj = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    os.chdir(proj)

    # not a git repo? nothing to do
    if run("git", "rev-parse", "--is-inside-work-tree").returncode != 0:
        sys.exit(0)

    # escape hatch
    git_dir = run("git", "rev-parse", "--git-dir").stdout.strip() or ".git"
    if os.path.exists(os.path.join(git_dir, "HERMES_NO_AUTOPUSH")):
        sys.exit(0)

    branch = run("git", "rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    if branch in ("main", "master", "HEAD"):
        print(f"[autocommit] skip protected branch '{branch}'", file=sys.stderr)
        sys.exit(0)

    # any changes?
    if not run("git", "status", "--porcelain").stdout.strip():
        sys.exit(0)

    run("git", "add", "-A")
    # short summary of what changed for the message
    stat = run("git", "diff", "--cached", "--shortstat").stdout.strip() or "changes"
    msg = f"chore(hermes): auto-commit — {stat}\n\nCo-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>"
    c = run("git", "commit", "-m", msg)
    if c.returncode != 0:
        print(f"[autocommit] commit failed: {c.stderr.strip()}", file=sys.stderr)
        sys.exit(0)

    p = run("git", "push", "origin", branch)
    if p.returncode != 0:
        # try to set upstream on first push of a new branch
        p2 = run("git", "push", "-u", "origin", branch)
        if p2.returncode != 0:
            print(f"[autocommit] push failed: {p2.stderr.strip()}", file=sys.stderr)
    sys.exit(0)

if __name__ == "__main__":
    main()
