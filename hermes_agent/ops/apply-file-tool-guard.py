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

0.21 moved `_check_sensitive_path` out of tools/file_tools.py into
tools/file_tools_write_guards.py AND rewrote its body: the `resolved` /
`normalized` locals became one `candidates` tuple and the refusal strings lost
their hanging close-paren. Both the file and the anchor are probed, so one kit
installs on either layout.
"""
import os
import shutil
import sys
import tempfile

AGENT = os.path.expanduser("~/.hermes/hermes-agent")
# >=0.21: the write guards live in their own module; <=0.20: still in file_tools.
_CANDIDATE_TARGETS = (
    os.path.join(AGENT, "tools", "file_tools_write_guards.py"),
    os.path.join(AGENT, "tools", "file_tools.py"),
)
MARKER = "[hermes-mechanic]"

# Anchor = the tail of _check_sensitive_path: its config-file refusal plus the
# final `return None`. 0.21 folded the close-paren onto the last string line.
ANCHOR_021 = (
    "            \"Agent cannot modify security-sensitive configuration. \"\n"
    "            \"Edit ~/.hermes/config.yaml directly or use 'hermes config' instead.\")\n"
    "    return None\n"
)
ANCHOR_019 = (
    "            \"Edit ~/.hermes/config.yaml directly or use 'hermes config' instead.\"\n"
    "        )\n"
    "    return None\n"
)

_HEAD = (
    "    # [hermes-mechanic] Manager-not-coder: block file-tool WRITES to project\n"
    "    # code under /srv/vadim_prod (Claude Code / OpenCode own that); the Second\n"
    "    # Brain wiki lives inside that zone and is carved out. Fires under mode:off too.\n"
    "    _PZ = \"/srv/vadim_prod/\"\n"
    "    _WIKI = \"/home/vadim_prod/3dlook-marketing/hermes_agent/AI-Second-Brain\"\n"
)
_TAILBODY = (
    "        if _cand.startswith(_PZ) and not _cand.startswith(_WIKI) and not _cand.endswith(\"/.hermes-handoff.md\"):\n"
    "            return (\n"
    "                \"Refusing (hermes-mechanic): Hermes is the manager, not the coder. \"\n"
    "                \"Project code under /srv/vadim_prod must be written by Claude Code / \"\n"
    "                \"OpenCode, not Hermes's file tool. Delegate it (claude-code skill / conductor).\"\n"
    "            )\n"
    "    return None\n"
)
# The candidate paths are upstream's own already-resolved values — realpath AND
# normpath, so neither a symlink into the zone nor a `..` walk out of it escapes.
# Deriving them again here would resolve relative paths against the WRONG cwd.
GUARD_BODY_021 = _HEAD + "    for _cand in candidates:\n" + _TAILBODY
GUARD_BODY_019 = _HEAD + "    for _cand in (resolved, normalized):\n" + _TAILBODY

GUARD_HEAD = "    # [hermes-mechanic] Manager-not-coder"
GUARD_TAIL = "    return None\n"


def _resolve():
    """(target path, anchor, guard body) for whichever layout is installed."""
    for path in _CANDIDATE_TARGETS:
        try:
            s = open(path, encoding="utf-8").read()
        except OSError:
            continue
        if "def _check_sensitive_path" not in s:
            continue
        # Pick the body by the local the function actually exposes, so a REFRESH
        # of an already-patched file writes the shape that file can execute.
        body = GUARD_BODY_021 if "candidates = (" in s else GUARD_BODY_019
        anchor = ANCHOR_021 if ANCHOR_021 in s else ANCHOR_019
        return path, s, anchor, body
    return None, None, None, None


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
    target, s, anchor, body = _resolve()
    if target is None:
        # Exit 2, not 0: an upstream refactor that moves _check_sensitive_path
        # leaves the guard uninstalled, and hermes-update.py only alerts on 2.
        # Reporting success for "target vanished" is the case worth shouting about.
        print("MISSING_TARGET: _check_sensitive_path found in none of "
              + ", ".join(_CANDIDATE_TARGETS) + " — file-tool guard NOT applied")
        return 2
    where = os.path.basename(target)
    if MARKER in s:
        # Marker present is NOT the same as "current". The guard's carve-out path
        # moved when the repo was restructured; the repo was updated, the patched
        # file was not, and an early return meant it never could be. The stale copy
        # pointed at a directory that no longer existed, so writing notes into the
        # Second Brain wiki was refused for weeks.
        if body in s:
            print(f"OK: file-tool guard already applied, current ({where})")
            return 0
        start = s.find(GUARD_HEAD)
        end = s.find(GUARD_TAIL, start) if start >= 0 else -1
        if start < 0 or end < 0:
            print("MISSING_ANCHOR: applied guard found but its bounds moved — "
                  "file-tool guard NOT refreshed")
            return 2
        _write_atomic(target, s[:start] + body + s[end + len(GUARD_TAIL):])
        print(f"REFRESHED: stale file-tool guard replaced with the current one ({where})")
        return 0
    if anchor not in s:
        print("MISSING_ANCHOR: _check_sensitive_path shape changed — file-tool guard NOT applied")
        return 2
    guard = anchor[:anchor.rindex(GUARD_TAIL)] + body
    _write_atomic(target, s.replace(anchor, guard, 1))
    print(f"APPLIED: file-tool project-code write guard ({where})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
