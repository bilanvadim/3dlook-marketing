#!/usr/bin/env python3
"""yt-research.py — YouTube search for SEO research.

WHY
---
On 2026-09-26 we looked at Agent Reach (Panniantong/Agent-Reach) for web/social research.
The only piece worth keeping for us was YouTube: what videos exist in the niche
(occ-health, telehealth, GLP-1), whose channels, how many views. Agent Reach does that with
plain yt-dlp underneath, so we install yt-dlp alone (~/.local/share/yt-dlp venv, linked
into ~/.local/bin) and skip the wrapper and the account-bound scrapers.

Search only, by decision. YouTube blocks this VPS's datacenter IP for transcripts and
comments ("Sign in to confirm you're not a bot"); getting past that needs cookies from a
Google account, and Vadim chose not to (2026-09-26). Search works without them.

USAGE
    scripts/yt-research.py "occupational health intake" -n 15

EXIT
    0 results · 1 no results · 3 yt-dlp missing or failed
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("query")
    ap.add_argument("-n", type=int, default=10)
    a = ap.parse_args()

    exe = shutil.which("yt-dlp") or str(Path("~/.local/bin/yt-dlp").expanduser())
    if not Path(exe).exists():
        print("yt-dlp not found (expected ~/.local/bin/yt-dlp)", file=sys.stderr)
        return 3
    p = subprocess.run([exe, "--no-warnings", "--ignore-config", "--flat-playlist", "--dump-json",
                        f"ytsearch{a.n}:{a.query}"], capture_output=True, text=True)
    if p.returncode:
        print(p.stderr.strip()[-800:], file=sys.stderr)
        return 3
    rows = [json.loads(l) for l in p.stdout.splitlines() if l.strip()]
    for r in rows:
        views = r.get("view_count")
        print(f"{r['id']} | {r.get('channel') or r.get('uploader') or '?'} | "
              f"{views if views is not None else '?'} views | {r.get('title', '')}")
    return 0 if rows else 1


if __name__ == "__main__":
    sys.exit(main())
