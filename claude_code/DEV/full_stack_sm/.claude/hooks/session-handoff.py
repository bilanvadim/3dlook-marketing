#!/usr/bin/env python3
"""Native session handoff — save context before compaction/clear, restore on session start.

Two events, one script:
  • PreCompact / SessionEnd → snapshot the recent transcript to .claude/scratchpad/_handoff/.
  • SessionStart (after compact|clear|resume) → inject the latest snapshot as additionalContext.

This is the RELIABLE safety-net (mechanical capture of recent messages) — it can't be lost
even if you /clear or the context auto-compacts. For a RICH structured handoff (Goal / done /
tried / decisions / next), run /sm-handoff, which overwrites latest.md with the better version.

Never breaks the session: any error → exit 0. Files live under the gitignored scratchpad.
"""
import json, os, sys, time

MAX_MSGS = 20
MAX_CHARS = 1200

def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    event = payload.get("hook_event_name", "")
    proj = os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd()
    hdir = os.path.join(proj, ".claude", "scratchpad", "_handoff")
    latest = os.path.join(hdir, "latest.md")

    # ---- restore on a fresh/compacted/cleared session ----
    if event == "SessionStart":
        if payload.get("source") not in ("compact", "clear", "resume"):
            sys.exit(0)
        if not os.path.exists(latest):
            sys.exit(0)
        try:
            txt = open(latest, encoding="utf-8").read()[:6000]
        except Exception:
            sys.exit(0)
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": "↩️ Восстановлен последний session-handoff (контекст был сжат/очищен). "
                                 "Свежее рабочее состояние фич — в .claude/scratchpad/<feature>/.\n\n" + txt,
        }}))
        sys.exit(0)

    # ---- snapshot before compaction / on session end ----
    tpath = payload.get("transcript_path")
    msgs = []
    if tpath and os.path.exists(tpath):
        try:
            with open(tpath, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        o = json.loads(line)
                    except Exception:
                        continue
                    t, m = o.get("type"), o.get("message", {}) or {}
                    if t == "user":
                        c = m.get("content")
                        if isinstance(c, str):
                            msgs.append(("user", c))
                        elif isinstance(c, list):
                            for b in c:
                                if isinstance(b, dict) and b.get("type") == "text":
                                    msgs.append(("user", b.get("text", "")))
                    elif t == "assistant":
                        for b in (m.get("content") or []):
                            if isinstance(b, dict) and b.get("type") == "text":
                                msgs.append(("assistant", b.get("text", "")))
        except Exception:
            pass

    msgs = [(r, x.strip()) for r, x in msgs if x and x.strip()][-MAX_MSGS:]
    if not msgs:
        sys.exit(0)

    out = [
        "# Session handoff (auto-snapshot)",
        "",
        "> Авто-снимок перед сжатием/очисткой контекста. Это safety-net (последние сообщения). "
        "Рабочее состояние фич — в `.claude/scratchpad/<feature>/`. Структурный handoff: `/sm-handoff`.",
        "",
        "## Последние сообщения",
    ]
    for role, text in msgs:
        who = "🧑 You" if role == "user" else "🤖 Claude"
        out.append(f"\n**{who}:** {text[:MAX_CHARS]}")
    body = "\n".join(out)

    try:
        os.makedirs(hdir, exist_ok=True)
        ts = time.strftime("%Y%m%d-%H%M%S")
        with open(os.path.join(hdir, f"session-{ts}.md"), "w", encoding="utf-8") as f:
            f.write(body)
        with open(latest, "w", encoding="utf-8") as f:
            f.write(body)
    except Exception:
        pass
    sys.exit(0)

if __name__ == "__main__":
    main()
