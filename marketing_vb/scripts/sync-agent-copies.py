#!/usr/bin/env python3
"""sync-agent-copies.py — DEV is the source, the other two copies are generated.

WHY
---
Agent definitions live in three places (`check-agent-copies.py` calls them ROOTS):

    claude_code/DEV/marketing_vb/plugins/<plugin>/agents/<name>.md   DEV source (marketplace)
    marketing_vb/.claude/plugins/<plugin>/<version>/agents/<name>.md installed plugin
    marketing_vb/.claude/agents/<group>/<name>.md                    project copy

`check-agent-copies.py` tells you when they have diverged. It cannot stop them diverging, and
divergence is not rare: on 2026-09-02 a one-sentence rule change ("positioned as" for the
medical-device boundary) had to be applied to twelve files by hand, and the same day's audit
found the agent prompts still carrying `DEXA` after the review had corrected it to `DXA`, so
`seo-writer` had to be told mid-run to override its own prompt.

Three copies edited by hand means a rule change ships partially. So: edit DEV, run this.

The pattern is already in this repo. `scripts/split-linkedin-prompts.py` generates the six
LinkedIn profile briefs from one master and fails `--check` with exit 1 on divergence; the
master stays the source of truth. This does the same for agents.

HOW IT DECIDES WHERE A FILE GOES
--------------------------------
By agent NAME, not by path, because the three roots are laid out differently: DEV groups by
plugin, the installed plugin adds a version directory, and the project copy groups into
`seo/`, `_shared/`, `social/`, `outbound/` with four writers sitting loose at the top level.
So for an agent that already exists, its current location is respected and only the content is
replaced. For an agent that is new in DEV, PLUGIN_TO_GROUP below decides, and if that mapping
does not cover its plugin the script reports it instead of guessing a path.

USAGE
    scripts/sync-agent-copies.py             # write the derived copies from DEV
    scripts/sync-agent-copies.py --check     # exit 1 if any derived copy differs from DEV
    scripts/sync-agent-copies.py --dry-run   # show what would change, write nothing
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))          # .../marketing_vb
OUTER = os.path.dirname(REPO)                                                # .../3dlook-marketing

DEV = os.path.join(OUTER, "claude_code", "DEV", "marketing_vb", "plugins")
PLUGINS = os.path.join(REPO, ".claude", "plugins")
PROJECT = os.path.join(REPO, ".claude", "agents")

# Only used for an agent that does not exist in a target root yet.
PLUGIN_TO_GROUP = {
    "mvb-core": "_shared",
    "mvb-seo": "seo",
    "mvb-social": "social",
    "mvb-outbound": "outbound",
}

SKIP_SUFFIXES = (".bak", ".orig")


def digest(path: str) -> str:
    with open(path, "rb") as fh:
        return hashlib.md5(fh.read()).hexdigest()


def is_skippable(name: str) -> bool:
    return any(s in name for s in SKIP_SUFFIXES) or ".bak-" in name


def dev_agents() -> dict[str, tuple[str, str]]:
    """{agent_name: (dev_path, plugin)} for every agent definition in DEV."""
    out = {}
    if not os.path.isdir(DEV):
        return out
    for plugin in sorted(os.listdir(DEV)):
        adir = os.path.join(DEV, plugin, "agents")
        if not os.path.isdir(adir):
            continue
        for fn in sorted(os.listdir(adir)):
            if not fn.endswith(".md") or is_skippable(fn):
                continue
            out[fn[:-3]] = (os.path.join(adir, fn), plugin)
    return out


def find_existing(root: str, name: str) -> str | None:
    """Where this agent currently lives under `root`, if anywhere. Respecting the existing
    location is what keeps the four loose writers at `.claude/agents/*.md` where they are."""
    for dirpath, _dirs, files in os.walk(root):
        for fn in files:
            if fn == f"{name}.md" and not is_skippable(fn):
                return os.path.join(dirpath, fn)
    return None


def plugin_version(plugin: str) -> str | None:
    d = os.path.join(PLUGINS, plugin)
    if not os.path.isdir(d):
        return None
    versions = [v for v in os.listdir(d) if re.fullmatch(r"\d+\.\d+\.\d+", v)]
    return sorted(versions)[-1] if versions else None


def targets_for(name: str, plugin: str) -> tuple[list[str], list[str]]:
    """(paths to write, problems). Existing locations win; PLUGIN_TO_GROUP is the fallback."""
    paths, problems = [], []

    # installed plugin copy
    existing = find_existing(PLUGINS, name)
    if existing:
        paths.append(existing)
    else:
        ver = plugin_version(plugin)
        if ver:
            paths.append(os.path.join(PLUGINS, plugin, ver, "agents", f"{name}.md"))
        else:
            problems.append(
                f"{name}: plugin {plugin!r} is not installed under .claude/plugins and has no "
                f"version directory, so there is nowhere to put the plugin copy"
            )

    # project copy
    existing = find_existing(PROJECT, name)
    if existing:
        paths.append(existing)
    else:
        group = PLUGIN_TO_GROUP.get(plugin)
        if group:
            paths.append(os.path.join(PROJECT, group, f"{name}.md"))
        else:
            problems.append(
                f"{name}: plugin {plugin!r} is not in PLUGIN_TO_GROUP, so the project copy's "
                f"directory is unknown. Add the mapping rather than letting the script guess."
            )
    return paths, problems


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="exit 1 if any derived copy differs from DEV")
    ap.add_argument("--dry-run", action="store_true", help="show what would change, write nothing")
    args = ap.parse_args()

    agents = dev_agents()
    if not agents:
        print(f"FAIL: no agents found under {DEV}", file=sys.stderr)
        print("DEV is the source of truth for agent definitions. If it is gone, do NOT sync "
              "from a derived copy: that would make whichever copy drifted the new source.",
              file=sys.stderr)
        return 2

    stale, missing, problems, written = [], [], [], []

    for name, (src, plugin) in agents.items():
        paths, probs = targets_for(name, plugin)
        problems.extend(probs)
        src_d = digest(src)
        for dst in paths:
            rel = os.path.relpath(dst, OUTER)
            if not os.path.exists(dst):
                missing.append(rel)
                if not (args.check or args.dry_run):
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    with open(src, "rb") as a, open(dst, "wb") as b:
                        b.write(a.read())
                    written.append(rel)
                continue
            if digest(dst) != src_d:
                stale.append(rel)
                if not (args.check or args.dry_run):
                    with open(src, "rb") as a, open(dst, "wb") as b:
                        b.write(a.read())
                    written.append(rel)

    n = len(agents)
    if args.check:
        if stale or missing or problems:
            print(f"FAIL: derived agent copies do not match DEV ({n} agents in DEV)", file=sys.stderr)
            for r in stale:
                print(f"  differs from DEV: {r}", file=sys.stderr)
            for r in missing:
                print(f"  missing:          {r}", file=sys.stderr)
            for p in problems:
                print(f"  unplaceable:      {p}", file=sys.stderr)
            print("\nEdit DEV, then run scripts/sync-agent-copies.py", file=sys.stderr)
            return 1
        print(f"all derived copies match DEV ({n} agents x 2 derived locations)")
        return 0

    if args.dry_run:
        print(f"{n} agents in DEV")
        for r in stale:
            print(f"  would overwrite: {r}")
        for r in missing:
            print(f"  would create:    {r}")
        for p in problems:
            print(f"  UNPLACEABLE:     {p}")
        if not (stale or missing):
            print("  nothing to do, everything already matches DEV")
        return 1 if problems else 0

    print(f"{n} agents in DEV, {len(written)} derived file(s) written")
    for r in written:
        print(f"  wrote {r}")
    for p in problems:
        print(f"  UNPLACEABLE: {p}", file=sys.stderr)
    if not written and not problems:
        print("  everything already matched DEV")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
