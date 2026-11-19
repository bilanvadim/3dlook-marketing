#!/usr/bin/env python3
"""content-plan-render.py — render the sheet rows of content-plan.md from content-plan.csv.

WHY
---
`content-plan-sync.py --sync` rewrites `content-plan.csv` but never `content-plan.md`, because the
md also carries hand-written text the sheet does not have (what changed, the gate legend, hub
preambles, repo notes). Until 2026-11-19 the row tables were retyped by hand after every sync,
which is how the md drifted two months behind the sheet in September and how the v3.0 sync
would have meant retyping 102 rows.

So the md is split: prose is hand-written, and every block between

    <!-- BEGIN rows:hub=N -->  ...  <!-- END rows:hub=N -->
    <!-- BEGIN published -->    ...  <!-- END published -->

is generated from the CSV, verbatim (Recommendations and guardrails are not shortened: seo-planner
quotes the guardrail word for word). Edit the sheet, sync, then run this; never edit inside the
markers.

USAGE
    scripts/content-plan-render.py            # rewrite the generated blocks in content-plan.md
    scripts/content-plan-render.py --check    # exit 1 if the md is behind the CSV
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIR = ROOT / "brand-assets" / "content-strategy"
CSV = DIR / "content-plan.csv"
MD = DIR / "content-plan.md"


def cell(s: str) -> str:
    s = (s or "").strip().replace("|", "\\|")
    return re.sub(r"\s*\n\s*", "<br>", s)


def load():
    rows = list(csv.reader(CSV.open(encoding="utf-8")))
    head = rows[0]
    hubs: dict[str, dict] = {}
    order: list[str] = []
    cur = None
    for r in rows[1:]:
        if not any(c.strip() for c in r):
            continue
        d = dict(zip(head, r))
        num = d.get("#", "").strip()
        if num:
            cur = num
            hubs[cur] = {"title": d["Main hub topic"].strip(), "rule": None, "rows": []}
            order.append(cur)
        if cur is None:
            raise SystemExit("content-plan.csv: first row has no hub number in column '#'")
        if not d.get("Cluster section", "").strip() and not d.get("Supporting articles", "").strip() \
                and not d.get("Action Type", "").strip():
            hubs[cur]["rule"] = d          # hub-wide rule row (Hub 9 has one)
            continue
        hubs[cur]["rows"].append(d)
    return hubs, order


def live_title(d: dict) -> str:
    """The sheet's `Published article` without its URL ('Title - https://…'); '' if only a date."""
    t = re.sub(r"\s*-?\s*https://\S+", "", d.get("Published article", "")).strip()
    return "" if re.match(r"^Published\b", t) else t


def pages(s: str) -> str:
    urls = re.findall(r"https://\S+?(?=[,\s]|$)", s)
    return "<br>".join(u.rstrip(",;") for u in urls) if urls else cell(s)


def article(d: dict) -> str:
    title = d.get("Supporting articles", "").strip() or d.get("Main hub topic", "").strip()
    pub = live_title(d)
    out = cell(title)
    if pub and pub != title:
        out += "<br>**Live as:** " + cell(pub)
    when = d.get("Published / Updated", "").strip()
    if when:
        out += f"<br>*Sheet date:* {cell(when)}"
    return out


def render_hub(h: dict) -> str:
    lines = []
    if h["rule"]:
        rule = h["rule"]
        lines.append("> **Sheet rule for every row of this hub:** " + cell(rule.get("Recommendations", "")))
        if rule.get("Cannibalization Guardrail", "").strip():
            lines.append(">")
            lines.append("> **Guardrail for every row:** " + cell(rule["Cannibalization Guardrail"]))
        lines.append("")
    lines.append("| Cluster | Article | Intent | Action | Pri | Pages | Recommendation | Cannibalization guardrail | Demand / KD |")
    lines.append("|---|---|---|---|---|---|---|---|---|")
    for d in h["rows"]:
        urls = d.get("URL of already published articles", "").strip()
        lines.append("| " + " | ".join([
            cell(d.get("Cluster section", "")),
            article(d),
            cell(d.get("Intent", "")),
            cell(d.get("Action Type", "")) or "—",
            cell(d.get("Execution Priority", "")) or "—",
            pages(urls) if urls else "—",
            cell(d.get("Recommendations", "")),
            cell(d.get("Cannibalization Guardrail", "")),
            cell(d.get("Спрос / KD", "")),
        ]) + " |")
    return "\n".join(lines)


def render_published(hubs: dict, order: list[str]) -> str:
    lines = ["| Hub | Cluster | Live page (sheet title) | Sheet date | Pri | URL |", "|---|---|---|---|---|---|"]
    for n in order:
        for d in hubs[n]["rows"]:
            if "published" not in d.get("Execution Priority", "").lower():
                continue
            title = live_title(d) or d.get("Supporting articles", "").strip()
            url = d.get("URL of already published articles", "").strip()
            lines.append("| " + " | ".join([
                f"Hub {n}", cell(d.get("Cluster section", "")), cell(title),
                cell(d.get("Published / Updated", "")), cell(d.get("Execution Priority", "")),
                pages(url) if url else "—",
            ]) + " |")
    return "\n".join(lines)


def replace_block(text: str, tag: str, body: str) -> str:
    pat = re.compile(rf"(<!-- BEGIN {re.escape(tag)} -->)\n.*?(<!-- END {re.escape(tag)} -->)", re.S)
    if not pat.search(text):
        raise SystemExit(f"content-plan.md: markers for '{tag}' not found")
    return pat.sub(lambda m: m.group(1) + "\n" + body + "\n" + m.group(2), text, count=1)


def main(argv: list[str]) -> int:
    hubs, order = load()
    text = MD.read_text(encoding="utf-8")
    new = replace_block(text, "published", render_published(hubs, order))
    for n in order:
        new = replace_block(new, f"rows:hub={n}", render_hub(hubs[n]))
    stray = set(re.findall(r"<!-- BEGIN rows:hub=(\w+) -->", new)) - set(order)
    if stray:
        print(f"⚠️  md has blocks for hubs the CSV no longer has: {sorted(stray)}")
    if "--check" in argv:
        if new != text:
            print("content-plan.md is behind content-plan.csv: run scripts/content-plan-render.py")
            return 1
        print("content-plan.md matches content-plan.csv")
        return 0
    MD.write_text(new, encoding="utf-8")
    total = sum(len(hubs[n]["rows"]) for n in order)
    print(f"✅ content-plan.md: {len(order)} hubs, {total} rows rendered from content-plan.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
