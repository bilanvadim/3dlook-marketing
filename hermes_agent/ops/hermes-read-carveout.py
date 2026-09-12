#!/usr/bin/env python3
"""Let Hermes READ the marketing repo again, without letting it write.

WHY THIS EXISTS
---------------
2026-09-12: Vadim dropped a Sales Navigator export into a campaign directory and asked
Hermes to pick it up. Hermes could not read `outbound-pipeline.py` to find out what the
pipeline does — `approvals.deny` in ~/.hermes/config.yaml blocks grep, find, sed and awk
across the whole of ~/3dlook-marketing. So it improvised: it wrote its own people CSVs,
its own "validation", and 218 message files for 109 people, none of it through a real
script or agent. All of it was thrown away. It also silently lost 19 real people, because
the export calls NowPatient "Infohealth Ltd" and only the real extract-people knows the
alias.

The carve-out for this ALREADY EXISTS — it was written on 2026-09-02 — but it lives in
`approvals.smart_policy`, which is the soft layer. `approvals.deny` is the hard layer and
fires first, so the policy never gets consulted and the carve-out has been dead since the
day it was written. That is the bug this fixes: right intent, wrong layer.

WHAT IT CHANGES
---------------
Removes deny rules for ~/3dlook-marketing whose command is READ-ONLY:
    grep, egrep, fgrep, rg, ag, ack, awk, find, sed (without -i)

KEEPS every rule that can write:
    sed -i, tee, vim, vi, nvim, nano, emacs, and every `* > path` / `* >> path` redirect

Does NOT touch ~/workspaces rules, or anything else in the file.

After this, reads are decided by `smart_policy`, which is already explicit: reads under
marketing_vb/workspace/ are approved, and every write escalates to Vadim. The
`block-destructive-terminal.py` agent hook remains as the second line.

Reading was never the risk. Editors and redirects were, and they stay denied.

USAGE
-----
    python3 hermes-read-carveout.py              # dry run, prints the diff, writes nothing
    python3 hermes-read-carveout.py --apply      # takes a backup, then writes
    python3 hermes-read-carveout.py --revert     # restore the newest backup this made

A restart is needed for the gateway to pick it up:
    systemctl --user restart hermes-gateway
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import shutil
import sys
from pathlib import Path

CONFIG = Path.home() / ".hermes" / "config.yaml"
TREE = "3dlook-marketing"
READ_TOOLS = ("grep", "egrep", "fgrep", "rg", "ag", "ack", "awk", "find", "sed")
BACKUP_TAG = "bak-readcarveout"


def leading_tool(rule: str) -> str:
    """The command a deny pattern actually gates, across the four shapes used in the file.

    The list writes each tool four ways: bare (`grep *<tree>/*`), after a cd
    (`cd <tree> && grep*`), after a cd into a subdir, and piped (`* | grep *<tree>/*`).
    """
    s = rule.strip()
    if s.startswith("sed -i"):
        return "sed -i"
    if ">" in s:
        return "redirect"
    if s.startswith("*") and "|" in s:
        m = re.search(r"\|\s*([a-z]+)", s)
        return m.group(1) if m else ""
    tok = s.split()[0].strip()
    if tok == "cd":
        m = re.search(r"&&\s*([a-z]+)", s)
        return m.group(1) if m else ""
    return tok


def is_read_only_marketing(rule: str) -> bool:
    return TREE in rule and leading_tool(rule) in READ_TOOLS


def slice_deny_block(lines: list[str]) -> tuple[int, int]:
    """(first, last+1) index of the deny list's ITEM lines, by indentation.

    Parsed by hand rather than through yaml.safe_load + yaml.dump: a round-trip would
    reformat the whole 27KB file, drop its comments, and rewrite blocks this has no
    business touching.
    """
    start = next((i for i, l in enumerate(lines) if l.rstrip() == "  deny:"), -1)
    if start < 0:
        sys.exit("✗ no `  deny:` key at two-space indent — the file's shape changed. "
                 "Stopping rather than guessing.")
    i = start + 1
    while i < len(lines) and (not lines[i].strip() or lines[i].startswith("    ")):
        i += 1
    return start + 1, i


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--apply", action="store_true", help="write the change (takes a backup first)")
    g.add_argument("--revert", action="store_true", help="restore the newest backup this made")
    g.add_argument("--check", action="store_true",
                   help="exit 0 if the carve-out holds, 1 if read-only denies are back "
                        "(for hermes-config-guard)")
    args = ap.parse_args()

    if not CONFIG.exists():
        sys.exit(f"✗ no {CONFIG}")

    if args.revert:
        backups = sorted(CONFIG.parent.glob(f"config.yaml.{BACKUP_TAG}-*"))
        if not backups:
            sys.exit(f"✗ no {BACKUP_TAG} backup to revert to")
        shutil.copy2(backups[-1], CONFIG)
        print(f"✓ restored {backups[-1].name}")
        print("  systemctl --user restart hermes-gateway")
        return 0

    lines = CONFIG.read_text(encoding="utf-8").split("\n")
    lo, hi = slice_deny_block(lines)
    block = lines[lo:hi]

    if args.check:
        back = [l for l in block if l.strip()
                and is_read_only_marketing(l.strip().lstrip("- ").strip('"\''))]
        if back:
            print(f"✗ {len(back)} read-only deny rule(s) are back — the carve-out was reverted")
            return 1
        print("✓ carve-out holds")
        return 0

    dropped = [l for l in block if l.strip() and is_read_only_marketing(l.strip().lstrip("- ").strip('"\''))]
    kept = [l for l in block if l not in dropped]

    marketing_kept = [l for l in kept if TREE in l]
    print(f"deny rules: {len([l for l in block if l.strip()])}")
    print(f"  removing (read-only, {TREE}): {len(dropped)}")
    print(f"  keeping  (writes, {TREE}):    {len(marketing_kept)}")
    print(f"  keeping  (other trees):       {len([l for l in kept if l.strip() and TREE not in l])}")
    print()
    print("  first few removed:")
    for l in dropped[:6]:
        print(f"    - {l.strip()}")
    print("  ...")
    print("  write rules that REMAIN denied (sample):")
    for l in marketing_kept[:6]:
        print(f"    - {l.strip()}")

    if not dropped:
        print("\n✓ nothing to do — already carved out")
        return 0

    if not args.apply:
        print("\n(dry run — nothing written. Re-run with --apply)")
        return 0

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup = CONFIG.with_suffix(f".yaml.{BACKUP_TAG}-{stamp}")
    shutil.copy2(CONFIG, backup)
    lines[lo:hi] = kept
    CONFIG.write_text("\n".join(lines), encoding="utf-8")
    print(f"\n✓ backup  {backup.name}")
    print(f"✓ written {CONFIG}")
    print("\nNow restart the gateway for it to take effect:")
    print("  systemctl --user restart hermes-gateway")
    print("\n⚠ `hermes update` rewrites config.yaml. If reads start being blocked again,")
    print("  that is what happened — re-run this script.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
