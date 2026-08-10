#!/usr/bin/env python3
"""Idempotent, anchor-based installer for the Hermes per-turn vision switch.

Mirrors ops/claude-switcher/apply-claude-switcher-patch.py: MARKER-guarded no-op
if already applied, fail-loud (exit 2) if any anchor moved so hermes-update.py
can alert. Re-run after every `hermes update` — an upstream reinstall overwrites
the vendored gateway files and takes the patch with it.

What it does:
  1. Copies vision_switch.py into the vendored gateway/ package.
  2. Inserts TWO call-outs in gateway/run.py:
       * ENGAGE, inside _prepare_inbound_message_text at the moment inbound
         images are found — and crucially BEFORE _decide_image_input_mode, which
         resolves the session override to decide whether the model gets pixels
         or a text description. Insert after that call and the borrow is
         pointless.
       * RELEASE, in the finally of the message-handling path, next to the
         existing MoA and one-turn restores, so the everyday model comes back on
         success, exception and interrupt alike.

Exit codes: 0 = applied or already-present · 2 = an anchor is missing (upstream
moved it — the switch is NOT active and needs a code fix).
"""
import os
import shutil
import sys

HERMES_AGENT = os.environ.get(
    "HERMES_AGENT_DIR",
    os.path.join(os.environ.get("HERMES_HOME") or os.path.expanduser("~/.hermes"), "hermes-agent"),
)
GATEWAY = os.path.join(HERMES_AGENT, "gateway")
RUN_PY = os.path.join(GATEWAY, "run.py")
SRC_MODULE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vision_switch.py")
DST_MODULE = os.path.join(GATEWAY, "vision_switch.py")

MARKER = "[hermes-vision-switch]"

# --- run.py: borrow the reader the moment inbound images are found ----------
# The comment lines are part of the anchor on purpose: `if image_paths:` alone
# appears more than once in run.py, and patching the wrong one would put the
# borrow somewhere it does nothing.
ENGAGE_ANCHOR = (
    "            if image_paths:\n"
    "                # Decide routing: native (attach pixels) vs text (vision_analyze\n"
    "                # pre-run + prepend description).  See agent/image_routing.py.\n"
)
ENGAGE_INSERT = (
    "            if image_paths:\n"
    "                # [hermes-vision-switch] borrow today's proven image reader for\n"
    "                # THIS turn. Must run before _decide_image_input_mode below: that\n"
    "                # call resolves this session's override, so with the reader\n"
    "                # already in place it answers \"native\" and the reader sees the\n"
    "                # actual pixels instead of someone else's description of them.\n"
    "                try:\n"
    "                    from gateway import vision_switch as _vsw\n"
    "                    _vsw.engage(self, session_key)\n"
    "                except Exception:\n"
    "                    logger.debug(\"vision-switch engage failed\", exc_info=True)\n"
    "                # Decide routing: native (attach pixels) vs text (vision_analyze\n"
    "                # pre-run + prepend description).  See agent/image_routing.py.\n"
)

# --- run.py: hand it back when the turn ends, however it ends --------------
# Inserted BEFORE the upstream restores, not after, and the order matters in one
# rare combination: `/model X --once` plus an image in the same turn. Our snapshot
# was taken while the one-turn override was live, so restoring it AFTER
# _restore_pending_one_turn_model_override would put that one-turn model straight
# back and leave it on for good. Releasing first unwinds the two in the order they
# were applied.
RELEASE_ANCHOR = (
    "            self._restore_moa_one_shot(event, _quick_key)\n"
    "            self._restore_pending_one_turn_model_override(_quick_key)\n"
)
RELEASE_INSERT = (
    "            # [hermes-vision-switch] give the image reader back. Same finally as\n"
    "            # the MoA restore and for the same reason: a leaked override would\n"
    "            # pin the session to the weakest model of the day, silently.\n"
    "            # (The upstream comment above belongs to the MoA restore two lines\n"
    "            # below — this block was inserted between them deliberately, see the\n"
    "            # ordering note in ops/vision-switch/apply-vision-switch-patch.py.)\n"
    "            try:\n"
    "                from gateway import vision_switch as _vsw\n"
    "                _vsw.release(self, _quick_key)\n"
    "            except Exception:\n"
    "                logger.debug(\"vision-switch release failed\", exc_info=True)\n"
    "\n"
)


def _patch_file(path, edits):
    """Apply anchor edits. Returns "patched" / "already" / [missing names].

    Idempotency is decided PER EDIT, not per file, so a later addition still
    reaches an install an earlier version of this script already patched.
    """
    with open(path, "r", encoding="utf-8") as f:
        s = f.read()
    todo, missing = [], []
    for name, anchor, replacement, present_test in edits:
        if present_test in s:
            continue
        if anchor not in s:
            missing.append(name)
        else:
            todo.append((name, anchor, replacement))
    if missing:
        return missing
    if not todo:
        return "already"
    for _name, anchor, replacement in todo:
        s = s.replace(anchor, replacement, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)
    return "patched"


def main():
    if not os.path.isdir(GATEWAY):
        print(f"MISSING_TARGET gateway dir not found: {GATEWAY}")
        return 2
    if not os.path.exists(SRC_MODULE):
        print(f"MISSING_TARGET source module not found: {SRC_MODULE}")
        return 2

    # 1. Copy the module into the vendored package (always refresh it).
    shutil.copyfile(SRC_MODULE, DST_MODULE)

    # 2. run.py — engage + release.
    r = _patch_file(RUN_PY, [
        ("engage", ENGAGE_ANCHOR, ENGAGE_INSERT, "_vsw.engage(self, session_key)"),
        ("release", RELEASE_ANCHOR, RELEASE_INSERT + RELEASE_ANCHOR,
         "_vsw.release(self, _quick_key)"),
    ])
    if isinstance(r, list):
        print("MISSING_ANCHOR " + ", ".join(f"run.py:{m}" for m in r))
        return 2
    print(f"run.py: {r}")
    print("OK vision-switch patch applied (module + run.py engage/release)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
