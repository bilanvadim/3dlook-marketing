#!/usr/bin/env python3
"""pack-cost.py — what one social pack actually cost, from the session transcripts.

WHY
---
The 2026-09-01 optimisation was sized from a measurement of one real pack, and the
claim it makes ("42.9M tokens down to single-digit millions") is only worth
something if the next pack can be measured the same way. This is that measurement,
so nobody has to trust the estimate.

It reads `~/.claude/projects/*/**.jsonl` — the main session transcripts and the
`subagents/` transcripts beside them — and reports context tokens, output tokens
and list-price cost per stage.

TWO THINGS IT GETS RIGHT, and both change the answer by more than 2x:

1. **Deduplication by message id.** A streamed assistant message is written to the
   transcript several times (partial content blocks, each carrying the same usage
   block). Summing every record counted the 2026-08-28 pack at 133.7M tokens; the
   real figure is 42.9M. Records are grouped by `message.id` and the record with
   the largest `output_tokens` wins, because the early partials report out=1-4.

2. **Cache classes priced separately.** Cache reads are a tenth of input price and
   cache writes are above it, so a token count alone ranks the levers wrong: by raw
   tokens the coordinator was 59% of the pack, by dollars 42%, and the cache-write
   line that looked negligible in tokens was $29.

Stages are identified from each subagent's first user message, so a renamed prompt
opener shows up as `other:` rather than being silently misfiled.

USAGE
    scripts/pack-cost.py <session-id-or-prefix>
    scripts/pack-cost.py --list [n]        # recent sessions that ran a social pack
    scripts/pack-cost.py <session> --hours # split the main session by hour, to
                                           # separate a pack from other work in it
"""
from __future__ import annotations

import argparse
import collections
import glob
import json
import os
import sys

PROJECTS = os.path.expanduser("~/.claude/projects")

# USD per million tokens: (input, cache write, cache read, output).
PRICE = {
    "opus":   (15.0, 18.75, 1.50, 75.0),
    "sonnet": (3.0, 3.75, 0.30, 15.0),
    "haiku":  (0.80, 1.00, 0.08, 4.0),
}

STAGES = (
    ("post-drafter", ("write the social post", "write one social post")),
    ("post-brand-checker", ("brand-voice check", "brand voice check")),
    ("post-quality-controller", ("score one social post",)),
    ("quality-controller", ("20-point", "quality-rubric")),
)


def family(model: str) -> str:
    m = (model or "").lower()
    for k in PRICE:
        if k in m:
            return k
    return "opus"


def usage(path: str, hour_prefix: str = None, window: tuple = None):
    """(counter, cost) for one transcript, deduplicated by message id.

    `window` is an inclusive (first, last) ISO-timestamp pair. It exists because a
    session outlives the pack: session 1ee1d21a ran the 2026-08-28 pack and was
    then resumed on 08-31 for unrelated work, and counting the whole file put the
    pack at 56.4M tokens instead of its real 42.9M. The window is derived from the
    pack's own subagent activity, so it needs no guessing."""
    best = {}
    for line in open(path, errors="replace"):
        try:
            o = json.loads(line)
        except ValueError:
            continue
        msg = o.get("message") or {}
        u = msg.get("usage") or {}
        if not u:
            continue
        ts = o.get("timestamp") or ""
        if hour_prefix and not ts.startswith(hour_prefix):
            continue
        if window and ts and not (window[0] <= ts <= window[1]):
            continue
        mid = msg.get("id") or o.get("uuid")
        rec = (u.get("input_tokens", 0), u.get("cache_creation_input_tokens", 0),
               u.get("cache_read_input_tokens", 0), u.get("output_tokens", 0),
               family(msg.get("model")))
        if mid not in best or rec[3] > best[mid][3]:
            best[mid] = rec
    c, cost = collections.Counter(), 0.0
    for i, cw, cr, ot, fam in best.values():
        c["in"] += i; c["cw"] += cw; c["cr"] += cr; c["out"] += ot; c["calls"] += 1
        p = PRICE[fam]
        cost += (i * p[0] + cw * p[1] + cr * p[2] + ot * p[3]) / 1e6
    return c, cost


def first_user_text(path: str) -> str:
    for line in open(path, errors="replace"):
        try:
            o = json.loads(line)
        except ValueError:
            continue
        if o.get("type") != "user":
            continue
        c = (o.get("message") or {}).get("content")
        return (c if isinstance(c, str) else json.dumps(c)).lower()
    return ""


def stage_of(text: str) -> str:
    for name, needles in STAGES:
        if any(n in text for n in needles):
            return name
    return "other: " + text[:48].replace("\n", " ")


def find_session(token: str):
    hits = [p for p in glob.glob(os.path.join(PROJECTS, "*", "*.jsonl"))
            if os.path.basename(p).startswith(token)]
    if len(hits) == 1:
        return hits[0]
    if not hits:
        print(f"✗ no session transcript starting with {token!r}", file=sys.stderr)
        return None
    print(f"✗ {len(token)} chars match {len(hits)} sessions; use a longer prefix:",
          file=sys.stderr)
    for h in hits:
        print("   " + os.path.basename(h)[:-6], file=sys.stderr)
    return None


def list_recent(n: int):
    rows = []
    for p in glob.glob(os.path.join(PROJECTS, "*", "*", "subagents", "*.jsonl")):
        t = first_user_text(p)
        if stage_of(t).startswith("other"):
            continue
        sess = p.split("/subagents/")[0] + ".jsonl"
        rows.append((os.path.getmtime(p), sess))
    seen, out = set(), []
    for mt, sess in sorted(rows, reverse=True):
        if sess in seen:
            continue
        seen.add(sess)
        out.append((mt, sess))
    import datetime
    for mt, sess in out[:n]:
        print(f"{datetime.datetime.fromtimestamp(mt).isoformat()[:16]}  "
              f"{os.path.basename(sess)[:-6]}")
    if not out:
        print("(no session with social-pack subagents found)")


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("session", nargs="?", help="session id or a unique prefix of it")
    p.add_argument("--list", nargs="?", const=10, type=int, metavar="N")
    p.add_argument("--hours", action="store_true",
                   help="also break the main session down by hour")
    p.add_argument("--whole-session", action="store_true",
                   help="count the entire main session, not just the pack window "
                        "(a session resumed days later for other work inflates it)")
    a = p.parse_args(argv)

    if a.list:
        list_recent(a.list)
        return 0
    if not a.session:
        p.print_help()
        return 2
    main_path = find_session(a.session)
    if not main_path:
        return 2
    subdir = main_path[:-6] + "/subagents"

    rows = collections.defaultdict(lambda: [collections.Counter(), 0.0, 0])
    first = last = None
    for sp in sorted(glob.glob(subdir + "/*.jsonl")):
        stage = stage_of(first_user_text(sp))
        c, cost = usage(sp)
        rows[stage][0].update(c); rows[stage][1] += cost; rows[stage][2] += 1
        for line in open(sp, errors="replace"):
            try:
                t = (json.loads(line).get("timestamp") or "")
            except ValueError:
                continue
            if not t:
                continue
            first = t if first is None else min(first, t)
            last = t if last is None else max(last, t)
    # Give the coordinator an hour of slack either side of the pack's own subagent
    # activity: it resolves the source and fills the run brief before the first
    # drafter starts, and writes the digest after the last one finishes.
    window = None
    if first and last and not a.whole_session:
        window = (first[:11] + "00:00:00", last[:13] + ":59:59")
        import datetime
        try:
            lo = datetime.datetime.fromisoformat(first.replace("Z", "+00:00"))
            hi = datetime.datetime.fromisoformat(last.replace("Z", "+00:00"))
            window = ((lo - datetime.timedelta(hours=1)).isoformat(),
                      (hi + datetime.timedelta(hours=1)).isoformat())
        except ValueError:
            pass
    c, cost = usage(main_path, window=window)
    rows["MAIN session"][0].update(c); rows["MAIN session"][1] += cost
    rows["MAIN session"][2] = 1

    print(f"session {os.path.basename(main_path)[:-6]}")
    if window:
        print(f"pack window {window[0][:16]} .. {window[1][:16]} "
              f"(main session outside it is excluded; --whole-session to include)")
    print()
    print(f"{'stage':28}{'runs':>5}{'reqs':>6}{'cacheW':>11}{'cacheR':>13}"
          f"{'output':>9}{'ctx':>13}{'$':>9}")
    tt = tc = 0
    for stage, (cc, cost_, n) in sorted(rows.items(), key=lambda x: -x[1][1]):
        ctx = cc["in"] + cc["cw"] + cc["cr"]
        print(f"{stage[:28]:28}{n:>5}{cc['calls']:>6}{cc['cw']:>11,}{cc['cr']:>13,}"
              f"{cc['out']:>9,}{ctx:>13,}{cost_:>9.2f}")
        tt += ctx + cc["out"]; tc += cost_
    print(f"\nTOTAL {tt:,} tokens · ~${tc:.2f}")
    posts = rows["post-drafter"][2]
    if posts:
        print(f"      {tt // posts:,} tokens · ~${tc / posts:.2f} per post "
              f"({posts} posts)")
    print("\nBaseline, as this script reads it (glp-1-market-hub, session 1ee1d21a,"
          "\n2026-08-28, before the optimisation):"
          "\n      42,787,229 tokens · ~$133.05 · ~$14.78 per post"
          "\n      MAIN 25.4M / $55.43 · drafter 7.5M / $36.78 · "
          "QC 7.1M / $36.35 · checker 2.2M / $4.49")

    if a.hours:
        print("\nMAIN session by hour (to separate the pack from other work):")
        stamps = set()
        for line in open(main_path, errors="replace"):
            try:
                o = json.loads(line)
            except ValueError:
                continue
            t = o.get("timestamp") or ""
            if t:
                stamps.add(t[:13])
        for h in sorted(stamps):
            cc, cost_ = usage(main_path, h)
            if not cc["calls"]:
                continue
            ctx = cc["in"] + cc["cw"] + cc["cr"]
            print(f"  {h}  reqs={cc['calls']:>4} ctx={ctx:>12,} ${cost_:>7.2f}  "
                  f"avg ctx/req={ctx // cc['calls']:>8,}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
