#!/usr/bin/env python3
"""Idempotently patch Hermes' file_tools so its WRITE tools (write_file/patch)
refuse to touch project code under /srv/vadim_prod — the file-tool half of the
"Hermes is the manager, not the coder" barrier (the terminal half is
approvals.deny in config.yaml). The Second Brain wiki lives inside that zone and
is carved out so note-taking keeps working.

Vendored upstream code is overwritten by `hermes update`, so this runs now AND
from hermes-update.py after every update. Idempotent: no-op if already patched;
fail-LOUD (prints MISSING_ANCHOR) if upstream moved the anchor so the lapse is
visible rather than silent.
"""
import os
import shutil
import sys
import tempfile

TARGET = "/home/vadim_prod/.hermes/hermes-agent/tools/file_tools.py"
MARKER = "[hermes-mechanic]"
# Anchor = the final `return None` of _check_sensitive_path (unique 3-line block).
ANCHOR = (
    "            \"Edit ~/.hermes/config.yaml directly or use 'hermes config' instead.\"\n"
    "        )\n"
    "    return None\n"
)
# The inserted body on its own, so a STALE previously-applied body can be cut out
# and replaced without re-deriving it from GUARD by string surgery.
GUARD_BODY = (
    "    # [hermes-mechanic] Manager-not-coder: block file-tool WRITES to project\n"
    "    # code under /srv/vadim_prod (Claude Code / OpenCode own that); the Second\n"
    "    # Brain wiki lives inside that zone and is carved out. Fires under mode:off too.\n"
    "    _PZ = \"/srv/vadim_prod/\"\n"
    "    _WIKI = \"/home/vadim_prod/3dlook-marketing/hermes_agent/AI-Second-Brain\"\n"
    "    for _cand in (resolved, normalized):\n"
    "        if _cand.startswith(_PZ) and not _cand.startswith(_WIKI) and not _cand.endswith(\"/.hermes-handoff.md\"):\n"
    "            return (\n"
    "                \"Refusing (hermes-mechanic): Hermes is the manager, not the coder. \"\n"
    "                \"Project code under /srv/vadim_prod must be written by Claude Code / \"\n"
    "                \"OpenCode, not Hermes's file tool. Delegate it (claude-code skill / conductor).\"\n"
    "            )\n"
    "    return None\n"
)
# What actually gets written on a fresh install: the anchor's own two lines, then
# the body in place of the plain `return None` that used to follow them.
GUARD = ANCHOR[:ANCHOR.rindex("    return None\n")] + GUARD_BODY
GUARD_HEAD = "    # [hermes-mechanic] Manager-not-coder"
GUARD_TAIL = "    return None\n"


def _write_atomic(path, text):
    """Temp file + os.replace. `open(path,"w")` truncates first, so an interrupt
    mid-write leaves the vendored module half-written and Hermes' file tools
    dead — the one failure this script must not be able to cause itself."""
    d = os.path.dirname(path) or "."
    fd, tmp = tempfile.mkstemp(dir=d, prefix=".ftg-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
        shutil.copymode(path, tmp)
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def main():
    try:
        s = open(TARGET, encoding="utf-8").read()
    except FileNotFoundError:
        # Exit 2, not 0: an upstream refactor that moves file_tools.py leaves the
        # guard uninstalled, and hermes-update.py only alerts on 2. Reporting
        # success for "target vanished" is exactly the case worth shouting about.
        print(f"MISSING_TARGET: {TARGET} not found — file-tool guard NOT applied")
        return 2
    if MARKER in s:
        # Marker present is NOT the same as "current". The guard's carve-out path
        # moved when the repo was restructured (hermes_agent/ →
        # agents-ai/telegram-bot-agent/hermes-agent/); the repo was updated, the
        # patched file was not, and this early return meant it could never be.
        # The stale copy pointed at a directory that no longer exists, so writing
        # notes into the Second Brain wiki was refused for weeks.
        if GUARD_BODY in s:
            print("OK: file-tool guard already applied (current)")
            return 0
        start = s.find(GUARD_HEAD)
        end = s.find(GUARD_TAIL, start) if start >= 0 else -1
        if start < 0 or end < 0:
            print("MISSING_ANCHOR: applied guard found but its bounds moved — "
                  "file-tool guard NOT refreshed")
            return 2
        _write_atomic(TARGET, s[:start] + GUARD_BODY + s[end + len(GUARD_TAIL):])
        print("REFRESHED: stale file-tool guard replaced with the current one")
        return 0
    if ANCHOR not in s:
        print("MISSING_ANCHOR: _check_sensitive_path shape changed — file-tool guard NOT applied")
        return 2
    _write_atomic(TARGET, s.replace(ANCHOR, GUARD, 1))
    print("APPLIED: file-tool project-code write guard")
    return 0


if __name__ == "__main__":
    sys.exit(main())
