#!/usr/bin/env python3
"""Re-apply the stream-failover patch after `hermes update` wipes it.

WHAT THE PATCH DOES
-------------------
A provider that dies mid-stream (429 quota, 502 all_providers_failed, read timeout)
arrives in the conversation loop as a `finish_reason=length` stub with NOTHING
recovered. Untouched, Hermes reads that as "the model ran long", spends its four
continuation attempts re-asking the same dead chain, never consults the fallback
providers, and finally tells the user:

    Response remained truncated after 4 continuation attempts

— a message about output length that says nothing about the quota that actually
caused it. The patch teaches the loop to tell the two apart (via error_classifier,
the single source of truth) and to escalate a provider death to the fallback chain
exactly as it already escalates a content filter. A non-empty partial keeps the old
behaviour: a stream that delivered real text IS worth resuming.

WHY THIS FILE EXISTS AT ALL
---------------------------
The patch was live in the tree on 2026-08-27 and its patcher was not: the previous
one lived only at /srv/vadim_prod/…/ops/apply-stream-failover-patch.py, and the
2026-08-26 repo-independence move emptied that tree. hermes-update.py still pointed
there and guarded the call with os.path.exists(), so the next `hermes update` would
have wiped the patch, found no patcher, and skipped re-applying it WITHOUT A WORD.
The symptom would have come back looking like a truncation bug.

WHY `git apply` AND NOT AN ANCHOR PATCHER
-----------------------------------------
The switcher's patcher matches text anchors because it INSERTS calls at named seams
that move between releases. This patch is five ordinary hunks, so a unified diff is
both smaller and stricter: `git apply --check` refuses on ANY context drift, which is
precisely the fail-loud behaviour wanted here. The base commit the diff was cut
against is recorded in stream-failover.base so a future drift can be read as
"upstream moved" rather than guessed at.

CONTRACT
--------
exit 0 — applied, or already present (idempotent; safe to run every morning)
exit 2 — could NOT apply. hermes-update.py turns this into a Telegram alert. Never
         exit 0 on failure: a silent skip is how the patch went missing in the first
         place.
"""
from __future__ import annotations

import os
import subprocess
import sys

AGENT = os.path.expanduser("~/.hermes/hermes-agent")
HERE = os.path.dirname(os.path.abspath(__file__))
PATCH = os.path.join(HERE, "patches", "stream-failover.patch")
BASE = os.path.join(HERE, "patches", "stream-failover.base")
MARKER = "[hermes-mechanic:stream-failover]"
# 0.21 extracted the whole truncation-recovery chain out of conversation_loop.py
# into agent/turn_truncation.py (a _Trunc state object + one function per phase) and
# rewrote the streaming stub builder into a _StreamingCall method. The patch was
# re-cut against that shape on 2026-09-06; the old two-file target list is gone with
# the code it named.
TARGETS = ("agent/chat_completion_helpers.py", "agent/turn_truncation.py")
# What a fully-applied patch looks like, so a HALF-applied tree is an error rather
# than a pass. Counted from the shipped patch, verified 2026-09-06.
EXPECTED = {"agent/chat_completion_helpers.py": 1, "agent/turn_truncation.py": 2}


def markers() -> dict[str, int]:
    out = {}
    for rel in TARGETS:
        try:
            with open(os.path.join(AGENT, rel), encoding="utf-8") as fh:
                out[rel] = fh.read().count(MARKER)
        except OSError:
            out[rel] = -1
    return out


def main() -> int:
    if not os.path.isdir(os.path.join(AGENT, ".git")):
        print(f"stream-failover: {AGENT} is not a git checkout — cannot apply", file=sys.stderr)
        return 2
    if not os.path.exists(PATCH):
        print(f"stream-failover: patch missing at {PATCH}", file=sys.stderr)
        return 2

    found = markers()
    if any(v < 0 for v in found.values()):
        missing = [k for k, v in found.items() if v < 0]
        print(f"stream-failover: target file(s) unreadable: {missing}", file=sys.stderr)
        return 2
    if found == EXPECTED:
        print("stream-failover: already")
        return 0
    if any(found.values()):
        # Half-applied is worse than not applied: `git apply` will refuse, and a
        # partial patch means the classifier exists while the loop that reads it
        # does not (or the reverse). Say so instead of trying to paper over it.
        print(f"stream-failover: PARTIALLY applied {found}, expected {EXPECTED} — "
              f"refusing to patch on top. Restore the two files from upstream "
              f"(git -C {AGENT} checkout -- {' '.join(TARGETS)}) and re-run.",
              file=sys.stderr)
        return 2

    chk = subprocess.run(["git", "-C", AGENT, "apply", "--check", PATCH],
                         capture_output=True, text=True)
    if chk.returncode != 0:
        base = ""
        try:
            base = open(BASE, encoding="utf-8").read().strip()
        except OSError:
            pass
        print(f"stream-failover: MISSING_ANCHOR — patch no longer applies.\n"
              f"  cut against: {base or 'unknown'}\n"
              f"  git says: {(chk.stderr or chk.stdout).strip()[:400]}", file=sys.stderr)
        return 2

    app = subprocess.run(["git", "-C", AGENT, "apply", PATCH],
                         capture_output=True, text=True)
    if app.returncode != 0:
        print(f"stream-failover: apply failed after a clean --check: "
              f"{(app.stderr or app.stdout).strip()[:400]}", file=sys.stderr)
        return 2

    after = markers()
    if after != EXPECTED:
        print(f"stream-failover: applied but markers are {after}, expected {EXPECTED}",
              file=sys.stderr)
        return 2
    print("stream-failover: applied")
    return 0


if __name__ == "__main__":
    sys.exit(main())
