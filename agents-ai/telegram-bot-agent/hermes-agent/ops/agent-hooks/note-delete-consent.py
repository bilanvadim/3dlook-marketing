#!/usr/bin/env python3
"""pre_llm_call hook: turn Sergiy's own "удали" into a one-turn deletion permit.

The deletion fuse (block-destructive-terminal.py) cannot tell "Sergiy asked for
this" from "the model decided on its own" — a pre_tool_call hook sees the tool
call and nothing else. So the consent is captured one layer up: pre_llm_call is
handed ``user_message``, i.e. the text that actually arrived from the human this
turn, before any skill or memory injection.

If that text carries an explicit deletion instruction, a permit is written; if it
does not, any previous permit is REMOVED. Consent therefore lives exactly as long
as the turn that expressed it and never leaks into the next one.

What deliberately does NOT grant a permit:

* **Forwarded client messages.** They reach the model as user text, so a client
  writing "удалите все старые файлы" would otherwise authorise a deletion. The
  switcher prefixes forwards with a marker, and those are refused here.
* **Vague tidying** ("приведи в порядок", "почисти") — that is the exact request
  that made the agent delete files unasked on 2026-08-05. The agent should come
  back and ask instead.
* Anything about Hermes' own control files, and destructive SQL / git history
  rewrites / container teardown: those are never unlocked from a chat, permit or
  not (see the fuse itself).

The permit is written to ~/.hermes/.delete-consent.json and is bound to the
session id plus a short TTL. The file is itself on the fuse's protected list, so
the agent cannot forge one.

Returns ``{}`` — this hook never injects context.
"""

import json
import os
import re
import sys
import time

PERMIT = os.path.expanduser("~/.hermes/.delete-consent.json")
TTL_SECONDS = 600  # a slow free model can take minutes between turn start and rm

# Explicit enough that it cannot be mistaken for "tidy this up".
INTENT = re.compile(
    r"(?:^|\W)(?:"
    r"удали(?:те|ть|шь)?|удаляй|снеси|снести|сотри|стереть|затри"
    r"|delete|remove|purge|wipe|unlink"
    r"|rm\s+-|rm\s+/|rm\s+~"
    r")(?:\W|$)",
    re.I,
)
# Markers the switcher puts on relayed content — never a source of consent.
RELAYED = (
    "Пересланное сообщение",
    "[Replying to:",
    "[Приложенные файлы",
    "forwarded message",
)


def read_payload():
    try:
        return json.load(sys.stdin)
    except Exception:
        return {}


def main():
    payload = read_payload()
    extra = payload.get("extra") or {}
    message = extra.get("user_message") or payload.get("user_message") or ""
    session = payload.get("session_id") or extra.get("session_id") or ""

    granted = False
    if isinstance(message, str) and message.strip():
        if not any(marker in message for marker in RELAYED):
            granted = bool(INTENT.search(message))

    try:
        if granted:
            tmp = PERMIT + ".tmp"
            with open(tmp, "w", encoding="utf-8") as fh:
                json.dump({
                    "ts": time.time(),
                    "session_id": session,
                    # Excerpt only: enough to audit why a deletion was allowed.
                    "asked": message.strip()[:200],
                }, fh, ensure_ascii=False)
            os.replace(tmp, PERMIT)
            os.chmod(PERMIT, 0o600)
        elif os.path.exists(PERMIT):
            os.remove(PERMIT)
    except OSError:
        pass  # never break a turn over the permit file

    print("{}")


if __name__ == "__main__":
    main()
