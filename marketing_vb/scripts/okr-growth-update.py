#!/usr/bin/env python3
"""okr-growth-update.py — fill the measurable KRs of the Q4'26 Growth OKR sheet and send a weekly digest.

WHY THIS EXISTS
---------------
The Q4'26 Growth (Marketing) OKR sheet has a "Current" column that nobody updates by hand on time.
Four KRs can be read from systems we already have. hubspot-handraisers.py fills the hand-raisers KR
(its own cron, 07:05). This script fills the other three and then sends Vadim one Telegram digest
of the whole sheet, manual KRs included, so a stale "Current" is visible every Monday.

  KR (found by text in column F)          source                                       value
  "visibility in AI assistants"           HubSpot AEO SUMMARY.averageVisibility,        fraction, e.g. 0.37
                                          last 28 days ending yesterday
  "new FitXpress deals"                   HubSpot deals, Health & Fitness pipeline,     count
                                          created this quarter, Deal Source Inbound
                                          or Outbound (warm intros and events excluded)
  "interested replies"                    workspace/outbound/campaigns/*/               count
                                          responses-classified.csv, category
                                          "interested", response_date this quarter,
                                          one per person

The definitions are written in column Q of the sheet as well. If a definition changes, change both.

READ-ONLY BY RULE
  HubSpot is read-only for us (AEO via hubspot-aeo.py's read allowlist; deals via the search
  action). The only writes are the "Current" cells of those three rows plus a cell note each.

COMMANDS
  update [--notify] [--dry-run]   fill the three cells; --notify sends the digest
  digest [--notify]               only read the sheet and print/send the digest
Cron: Mon 07:10 UTC `update --notify`, after hubspot-handraisers.py (07:05).
"""
from __future__ import annotations

import argparse
import csv
import datetime as _dt
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
CAMPAIGNS = REPO / "workspace" / "outbound" / "campaigns"
FX_PIPELINE = "67834452"                     # HubSpot deal pipeline "Health & Fitness" = FitXpress
DEAL_SOURCES = {"Inbound", "Outbound"}       # deal property deal_status, label "Deal Source"
AEO_DAYS = 28


def load(name: str, file: str):
    spec = importlib.util.spec_from_file_location(name, HERE / file)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


hr = load("hubspot_handraisers", "hubspot-handraisers.py")   # oo(), quarter_of(), sheet I/O, send()
aeo = load("hubspot_aeo", "hubspot-aeo.py")                   # metrics()
Broken = hr.Broken

MARKERS = {
    "aeo": re.compile(r"^KR\d+:.*visibility in AI assistants", re.I),
    "deals": re.compile(r"^KR\d+:.*new FitXpress deals", re.I),
    "outbound": re.compile(r"^KR\d+:.*interested replies", re.I),
}


# ------------------------------------------------------------------ metrics

def aeo_visibility(today: _dt.date) -> tuple[float, str]:
    end = today - _dt.timedelta(days=1)
    start = end - _dt.timedelta(days=AEO_DAYS - 1)
    try:
        data = aeo.metrics(["SUMMARY"], start.isoformat(), end.isoformat())
    except (aeo.Broken, aeo.Refused) as e:
        raise Broken(f"AEO: {e}")
    s = data.get("summary") or {}
    if s.get("averageVisibility") is None:
        raise Broken(f"AEO summary has no averageVisibility: {json.dumps(s)[:200]}")
    value = round(float(s["averageVisibility"]) / 100, 4)
    return value, (f"{start:%b %d}–{end:%b %d} average {s['averageVisibility']:.1f}% over "
                   f"{s.get('totalPrompts')} prompts, {s.get('totalResponses')} AI answers")


def fx_deals(start: str, end: str) -> tuple[int, str]:
    data = hr.oo(["connector", "run", "hubspot", "--action", "search_deals", "--data", json.dumps({
        "filterGroups": [{"filters": [
            {"propertyName": "pipeline", "operator": "EQ", "value": FX_PIPELINE},
            {"propertyName": "createdate", "operator": "GTE", "value": f"{start}T00:00:00Z"},
            {"propertyName": "createdate", "operator": "LT", "value": f"{end}T00:00:00Z"}]}],
        "properties": ["dealname", "createdate", "deal_status"], "limit": 200})])
    deals = [d.get("properties") or {} for d in data.get("results") or []]
    if len(deals) >= 200:   # the oo action returns no paging cursor; a quarter is ~10-25 deals
        raise Broken("200+ FX deals in one quarter: the oo search action cannot page, switch to the MCP proxy")
    by_source: dict[str, int] = {}
    for d in deals:
        src = d.get("deal_status") or "not set"
        by_source[src] = by_source.get(src, 0) + 1
    value = sum(by_source.get(s, 0) for s in DEAL_SOURCES)
    detail = ", ".join(f"{k} {v}" for k, v in sorted(by_source.items(), key=lambda kv: -kv[1])) or "none"
    return value, f"created {start}…{end}: {detail}; counted Inbound + Outbound"


def outbound_interested(start: str, end: str) -> tuple[int, str]:
    people, per_campaign = set(), {}
    for f in sorted(CAMPAIGNS.glob("*/responses-classified.csv")):
        with f.open(encoding="utf-8", newline="") as fh:
            for r in csv.DictReader(fh):
                day = (r.get("response_date") or "")[:10]
                if r.get("category") != "interested" or not start <= day < end:
                    continue
                key = r.get("person_id") or r.get("linkedin_url") or r.get("full_name")
                if key in people:
                    continue
                people.add(key)
                per_campaign[f.parent.name] = per_campaign.get(f.parent.name, 0) + 1
    detail = ", ".join(f"{k} {v}" for k, v in sorted(per_campaign.items())) or "none yet"
    return len(people), f"{detail}"


# ------------------------------------------------------------------ sheet

def read_panel() -> tuple[str, list[list]]:
    data = hr.oo(["connector", "run", "googlesheets", "--action", "batch_get", "--data", json.dumps(
        {"spreadsheetId": hr.OKR_SHEET, "ranges": [f"{hr.OKR_TAB}!A1:B3", f"{hr.OKR_TAB}!A1:Q40"]})])
    vr = data["valueRanges"]
    first = (vr[0].get("values") or [[]])[0]
    label = str(first[1]) if len(first) > 1 else ""
    return label, vr[1].get("values") or []


def find_rows(rows: list[list]) -> dict[str, int]:
    found = {}
    for i, row in enumerate(rows, start=1):
        cell = str(row[5]) if len(row) > 5 else ""
        for key, rx in MARKERS.items():
            if rx.search(cell):
                found[key] = i
    missing = set(MARKERS) - set(found)
    if missing:
        raise Broken(f"KR rows not found in column F: {', '.join(sorted(missing))}")
    return found


def digest(rows: list[list], label: str, auto: dict[str, str]) -> str:
    """One line per KR from the sheet itself, so manual KRs show their staleness too."""
    cell = lambda r, c: str(r[c]).strip() if len(r) > c else ""   # noqa: E731
    lines = [f"🎯 OKR {label} · Growth · {_dt.date.today():%d.%m}"]
    for r in rows:
        company, division, obj, kr = cell(r, 0), cell(r, 1), cell(r, 4), cell(r, 5)
        if company.startswith("O1:") and not division:
            lines.append(f"Загалом: {cell(r, 11)} · {cell(r, 14)}")
        elif division != "Growth":
            continue
        elif obj:
            lines.append(f"\n{obj.split(':')[0]} · {cell(r, 11)} — {obj.split(':', 1)[-1].strip()[:70]}")
        elif kr:
            name = kr.split(":")[0]
            what = kr.split(":", 1)[-1].strip()
            what = what.split(":")[0] if len(what.split(":")[0]) < 40 else what[:40] + "…"
            status = cell(r, 14).split(" ")[0:2]
            lines.append(f"· {name} {what}: {cell(r, 10) or '0'} / {cell(r, 9)} ({cell(r, 11)}) · "
                         f"до {cell(r, 12)} · {' '.join(status)}")
    if auto:
        lines.append("\nАвтоматично: " + " · ".join(f"{k} {v}" for k, v in auto.items()))
    lines.append("Решту «Current» оновлюють руками в таблиці.")
    return "\n".join(lines)[:hr.TG_LIMIT]


# ------------------------------------------------------------------ commands

def cmd_update(args) -> int:
    stamp = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    today = _dt.date.today()
    qkey, start, end = hr.quarter_of(today)
    try:
        label, rows = read_panel()
        if not hr.sheet_quarter_ok(label, qkey):
            msg = f"OKR sheet is for {label!r}, today is {qkey}: not writing."
            print(f"[{stamp}] SKIP {msg}")
            if args.notify:
                hr.send(f"🎯 okr-growth-update: {msg}")
            return 0
        where = find_rows(rows)
        results = {"aeo": aeo_visibility(today), "deals": fx_deals(start, end),
                   "outbound": outbound_interested(start, end)}
        auto = {}
        for key, (value, detail) in results.items():
            row = where[key]
            shown = f"{value:.1%}" if key == "aeo" else str(value)
            auto[{"aeo": "AEO", "deals": "угоди FX", "outbound": "interested"}[key]] = shown
            print(f"[{stamp}] {key}: K{row} = {shown} | {detail}")
            if not args.dry_run:
                hr.write_sheet(row, value, f"Auto: okr-growth-update.py, {stamp}. {detail}.")
        if args.dry_run:
            print("dry run: sheet untouched")
            return 0
        if args.notify:
            label, rows = read_panel()
            hr.send(digest(rows, label, auto))
    except Broken as e:
        print(f"[{stamp}] FAIL {e}")
        if args.notify:
            hr.send(f"⚠️ okr-growth-update.py не оновив OKR: {e}"[:hr.TG_LIMIT])
        return 3
    return 0


def cmd_digest(args) -> int:
    label, rows = read_panel()
    text = digest(rows, label, {})
    print(text)
    if args.notify:
        hr.send(text)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    u = sub.add_parser("update", help="fill AEO, deals and outbound KRs")
    u.add_argument("--notify", action="store_true", help="send the weekly digest to Telegram")
    u.add_argument("--dry-run", action="store_true", help="compute only, write nothing")
    u.set_defaults(fn=cmd_update)
    d = sub.add_parser("digest", help="read the sheet and print the digest")
    d.add_argument("--notify", action="store_true")
    d.set_defaults(fn=cmd_digest)
    args = ap.parse_args()
    try:
        return args.fn(args)
    except Broken as e:
        print(f"FAIL {e}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    sys.exit(main())
