#!/usr/bin/env python3
"""Hermes prompt counter (UserPromptSubmit event).

Goal: cut token usage by clearing context every 5th prompt.

HARD LIMITATION (verified): Claude Code hooks CANNOT run /clear or any slash
command — there is no hook output that resets the context window. So this hook
does the only thing it can: on every 5th prompt it injects a visible reminder
to run /clear (your context lives in .claude/scratchpad/, so clearing is safe).

For the AUTONOMOUS conductor, the real periodic reset is done in code
(fresh SDK session every N turns) — see conductor/src/core/conductor.ts.

Counter is per-session, stored under the git dir. Exit 0 always.
"""
import json, os, subprocess, sys

EVERY = 5

def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    session = str(payload.get("session_id") or "default")[:64].replace("/", "_")
    proj = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()

    git_dir = subprocess.run(["git", "rev-parse", "--git-dir"], cwd=proj,
                             capture_output=True, text=True).stdout.strip()
    base = os.path.join(proj, git_dir) if git_dir else "/tmp"
    state = os.path.join(base, f"hermes-prompt-count-{session}")

    try:
        n = int(open(state).read().strip()) + 1
    except Exception:
        n = 1
    try:
        open(state, "w").write(str(n))
    except Exception:
        pass

    if n % EVERY == 0:
        msg = (f"🧹 Hermes: это {n}-й запрос в сессии. Контекст вырос — для экономии токенов "
               f"запусти `/clear` (всё рабочее состояние сохранено в .claude/scratchpad/, "
               f"оркестратор поднимет его с диска). Хук не может сделать /clear сам.")
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": msg
            }
        }))
    sys.exit(0)

if __name__ == "__main__":
    main()
