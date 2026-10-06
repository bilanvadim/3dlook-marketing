#!/usr/bin/env python3
"""hubspot-handraisers.py — count FitXpress B2B hand-raisers in HubSpot for the Q4'26 Growth OKR.

WHY THIS EXISTS
---------------
The Q4'26 Growth OKR sheet has a KR "FitXpress B2B hand-raisers" (O3 KR2). It is the purely
marketing step between traffic and deals: did landings, AEO and content turn into people who asked
to talk? The first baseline (121 for Q3'26, from the 2026-09-25 HubSpot review) counted every
product, eBook downloads and outbound meetings. Most of the shared "Contact us" traffic is Mobile
Tailor (made-to-measure, uniforms), so that number said little about FitXpress. This script keeps
one written definition and fills the KR's "Current" cell every week.

WHAT COUNTS (a "hand-raiser")
  A company (one per email domain, however many people wrote) whose contact, from a business
  email and inside the quarter:
  * filled a FitXpress-only form: FX pricing (Starter / Pro / Talk to sales) or an FX landing form
    (Telehealth & Weight Loss, Connected & Digital Fitness, Health & Fitness LP, FX | LP | Demo); or
  * wrote through the shared "Contact us & Partnership" form, or booked through a HubSpot Meetings
    link, and the message / company / email domain / first page reads as FitXpress (health,
    fitness, weight, insurance, clinic ...) more than as Mobile Tailor (tailoring, uniforms, apparel).
  An FX form filled by a company that clearly reads as fashion counts as MT.

  Not counted, but shown: Mobile Tailor; new directions (wrist, head, rings: they belong to O1);
  eBook downloads (content leads); meetings booked from outbound (lead_source VB outreach / Apollo /
  Outbound: they count in the outbound KR); spam and vendors; unclassified.
  Dropped silently: consumer email domains, 3DLOOK's own domains, the homepage popup, MT app forms,
  careers, support, newsletter.

LIMITS
  * HubSpot keeps only the FIRST and the MOST RECENT conversion of a contact (plus the date of the
    last Meetings-link booking). A conversion in between is invisible to the API.
  * The FX/MT split on shared forms is a keyword classifier. `count --list` prints every row so a
    person can check it. Fix a wrong row with an override, not by editing the keywords for one
    company: ~/.hermes/handraisers-overrides.json  {"example.com": "FX" | "MT" | "exclude"}.
    It lives outside the repo because the repo is public and domains are lead data.

LEDGER
  ~/.hermes/.handraisers-ledger.json. Once a company counts as FX for a quarter it stays counted,
  so a later homepage-popup visit (which replaces "most recent conversion") cannot erase an October
  demo request. An "MT"/"exclude" override still removes it.

READ-ONLY BY RULE
  HubSpot is read-only for us. The only HubSpot call is the MCP tool search_crm_objects, through
  `oo connector proxy hubspot` (the `oo connector run hubspot search_contacts` action caps at 200
  rows and returns no paging cursor). The only write is the OKR Google Sheet cell.

COMMANDS
  count [--from D --to D] [--list]     buckets for a window (default: current quarter)
  quarters [--n 4]                     FX hand-raisers per quarter, for baselines
  update-sheet [--notify] [--dry-run]  current quarter -> the KR's "Current" cell (+ a cell note),
                                       Telegram summary with --notify. Cron: Mon 07:05 UTC.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

MCP_URL = "https://mcp.hubspot.com/"
SHEETS_URL = "https://sheets.googleapis.com/v4/spreadsheets"
# cron has no ~/.local/bin on PATH, hence the fallback (same as hubspot-aeo.py)
OO = shutil.which("oo") or str(Path.home() / ".local" / "bin" / "oo")
OKR_SHEET = "1Qd5MjTQwQfdDL3Dicd3lzsCZIn46VlAOgjki8sGEWCI"   # Q4'26 OKRs — Growth (Marketing)
OKR_TAB, OKR_TAB_ID = "Main Panel", 1021869658
KR_MARKER = re.compile(r"^KR\d+:.*hand-raisers", re.I)        # finds the KR row in column F
LEDGER = Path.home() / ".hermes" / ".handraisers-ledger.json"
OVERRIDES = Path.home() / ".hermes" / "handraisers-overrides.json"
PIPE = Path(__file__).with_name("outbound-pipeline.py")
TG_LIMIT = 3800

PROPS = ["email", "hs_email_domain", "company", "jobtitle", "lead_source", "hs_analytics_first_url",
         "first_conversion_event_name", "first_conversion_date",
         "recent_conversion_event_name", "recent_conversion_date", "engagements_last_meeting_booked",
         "message", "please_describe_the_problem_you_expect_to_solve_with_3dlook_solutions",
         "contact_with_the_sales_team_message"]
TEXT_PROPS = PROPS[-3:] + ["company", "jobtitle"]

CONSUMER = set("""
gmail.com googlemail.com yahoo.com yahoo.co.uk yahoo.co.in yahoo.fr ymail.com rocketmail.com
hotmail.com hotmail.co.uk hotmail.fr outlook.com live.com msn.com icloud.com me.com mac.com aol.com
proton.me protonmail.com gmx.com gmx.de gmx.net web.de mail.ru bk.ru inbox.ru list.ru yandex.ru
yandex.com ukr.net i.ua meta.ua qq.com 163.com 126.com sina.com rediffmail.com zoho.com zohomail.com
zohomail.in mail.com email.com hey.com fastmail.com tutanota.com libero.it virgilio.it orange.fr
free.fr laposte.net wanadoo.fr t-online.de seznam.cz wp.pl o2.pl interia.pl onet.pl naver.com
daum.net hanmail.net btinternet.com sky.com comcast.net verizon.net att.net sbcglobal.net
bellsouth.net cox.net charter.net shaw.ca rogers.com bigpond.com optusnet.com.au
""".split())
OWN = {"3dlook.me", "3dlook.ai", "3dlook.com"}

FX_FORMS = re.compile(r"FX Starter|FX Pricing - Talk to sales|FX Pro\b|Telehealth & Weight Loss|"
                      r"Connected & Digital Fitness|Health & Fitness LP|FX \| LP \| Demo", re.I)
SHARED_FORM = re.compile(r"Contact us & Partnership form", re.I)
MEETING_SLUG = re.compile(r"^[a-z]+(-[a-z]+)+$")          # Meetings-link conversions: "first-last"
CONTENT_FORM = re.compile(r"Downloadable content", re.I)
OUTBOUND_LS = re.compile(r"VB outreach|Apollo|Outbound|Sales Nav", re.I)

FX_KW = re.compile(r"\b(weight|glp|obes\w*|bmi|tele ?health|telemed\w*|patients?|clinics?|clinical|"
                   r"health\w*|medical|fitness|gyms?|workouts?|body ?composition|body ?fat|fat loss|"
                   r"muscles?|dexa|dxa|inbody|wellness|nutrition\w*|diet\w*|coach\w*|insur\w*|"
                   r"underwrit\w*|occupational|bariatric|pharmac\w*|longevity|physio\w*|rehab\w*|"
                   r"metabolic|fitxpress|personal trainers?|trainers?|strength)", re.I)
MT_KW = re.compile(r"\b(tailor\w*|made[- ]to[- ](measure|order)|mtm|bespoke|suits?|uniforms?|apparel|"
                   r"cloth(ing|es)|garments?|fashion|dress(es)?|shirts?|trousers?|sewing|patternmaking|"
                   r"patronaje|workwear|boutique|size recommendations?|virtual try[- ]?on|try[- ]on|"
                   r"mobile tailor|textiles?|jeans|bridal|bedding|footwear|shoes?|lingerie|bras?|"
                   r"collars?|harness(es)?|e-?commerce|rental platform)\b", re.I)
NEW_KW = re.compile(r"(wrist|watch|bracelet|jewel|ring siz|finger|helmet|\bheads?\b|\bhats?\b|\bwigs?\b)", re.I)
SPAM_KW = re.compile(r"(domain name|attendee|database|website creation|seo services|backlink|guest post|"
                     r"investment|asset management|awards?\b|lead generation|outsourc|development company|"
                     r"app development|we provide|agency\b|magazine|conference|science park|"
                     r"technical partnership|\bstudent\b|\bintern\b|конференц)", re.I)
FX_DOMAIN = re.compile(r"health|fitness|clinic|medic|weight|slim|nutri|gym|wellness|pharm|physio|diet|"
                       r"sweat|longevity|obes|bariatr|telemed|care|doctor|vitality|metabol", re.I)
MT_DOMAIN = re.compile(r"cloth|dress|tailor|suit|fashion|apparel|wear|style|textile|uniform|shoe|bridal|"
                       r"bespoke|garment|couture|denim|jeans", re.I)
FX_URL = re.compile(r"3dlook\.ai/(fitxpress|for-)|telehealth|glp|weight|bariatric|fitness|health|obes|"
                    r"bmi|patient|clinic|wellness|insurance|underwrit|occupational|dexa|dxa|"
                    r"body-composition", re.I)
MT_URL = re.compile(r"/mobile-tailor|apparel|fashion|\?mt", re.I)

COUNTED = "FX"
SHOWN = ["MT", "new", "content", "meeting-outbound", "spam", "mixed", "unknown"]
LABELS = {"MT": "Mobile Tailor", "new": "нові напрямки", "content": "eBook", "meeting-outbound":
          "зустрічі з аутбаунду", "spam": "спам/вендори", "mixed": "змішані", "unknown": "нерозпізнані"}
LABELS_EN = {"MT": "Mobile Tailor", "new": "new directions", "content": "eBook", "meeting-outbound":
             "outbound meetings", "spam": "spam/vendors", "mixed": "mixed", "unknown": "unclassified"}


class Broken(Exception):
    """oo, HubSpot or Sheets failed. Exit 3."""


# ------------------------------------------------------------------ transport

def oo(args: list[str], timeout: int = 180) -> dict:
    if not Path(OO).exists():
        raise Broken(f"`oo` CLI not found (looked on PATH and at {OO})")
    try:
        proc = subprocess.run([OO, *args, "--json"], capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        raise Broken(f"oo timed out after {timeout}s: {' '.join(args[:4])}")
    if proc.returncode != 0:
        raise Broken(f"oo exit {proc.returncode}: {(proc.stderr or proc.stdout).strip()[:500]}")
    try:
        return json.loads(proc.stdout)["data"]
    except (ValueError, KeyError):
        raise Broken(f"unexpected oo output: {proc.stdout[:500]}")


def search_contacts(start: str, end: str) -> list[dict]:
    """Contacts with a first/recent conversion or a Meetings booking in [start, end). Read-only."""
    def window(prop: str) -> dict:
        return {"filters": [{"propertyName": prop, "operator": "GTE", "value": f"{start}T00:00:00Z"},
                            {"propertyName": prop, "operator": "LT", "value": f"{end}T00:00:00Z"}]}
    groups = [window(p) for p in ("first_conversion_date", "recent_conversion_date",
                                  "engagements_last_meeting_booked")]
    rows, offset = [], None
    while True:
        args = {"objectType": "CONTACT", "properties": PROPS, "limit": 200, "filterGroups": groups}
        if offset is not None:
            args["offset"] = offset
        body = {"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                "params": {"name": "search_crm_objects", "arguments": args}}
        data = oo(["connector", "proxy", "hubspot", "--method", "POST", "--endpoint", MCP_URL,
                   "--headers", json.dumps({"Content-Type": "application/json",
                                            "Accept": "application/json, text/event-stream"}),
                   "--body", json.dumps(body)])
        rpc = data.get("data") or {}
        if "error" in rpc:
            raise Broken(f"MCP error: {json.dumps(rpc['error'])[:500]}")
        result = rpc.get("result") or {}
        text = "".join(c.get("text", "") for c in result.get("content", []) if c.get("type") == "text")
        if result.get("isError"):
            raise Broken(f"search_crm_objects: {text[:500]}")
        page = json.loads(text)
        batch = page.get("results") or []
        for r in batch:
            props = dict(r.get("properties") or {})
            props["_id"] = str(r.get("id"))
            rows.append(props)
        offset = page.get("offset")
        if not batch or offset in (None, "") or len(rows) >= int(page.get("total") or 0):
            return rows


# ------------------------------------------------------------------ classification

def domain(p: dict) -> str:
    return (p.get("hs_email_domain") or (p.get("email") or "@").split("@")[-1]).strip().lower()


def text(p: dict) -> str:
    return " ".join(filter(None, (p.get(k) for k in TEXT_PROPS)))


def form(event: str | None) -> str:
    return (event or "").split(": ", 1)[-1].strip()


def lean(p: dict) -> tuple[int, int]:
    t, d = text(p), domain(p)
    fx = len(FX_KW.findall(t)) + bool(FX_DOMAIN.search(d))
    mt = len(MT_KW.findall(t)) + bool(MT_DOMAIN.search(d))
    return fx, mt


def hits(p: dict, start: str, end: str) -> list[tuple[str, str, str]]:
    """Qualifying touches inside [start, end): (kind, form name, date)."""
    out = []
    for k in ("first", "recent"):
        name = form(p.get(f"{k}_conversion_event_name"))
        day = (p.get(f"{k}_conversion_date") or "")[:10]
        if not name or not start <= day < end:
            continue
        if FX_FORMS.search(name):
            out.append(("fx_form", name, day))
        elif SHARED_FORM.search(name):
            out.append(("shared", name, day))
        elif MEETING_SLUG.match(name):
            out.append(("meeting", "Meetings link", day))
        elif CONTENT_FORM.search(name):
            out.append(("content", name, day))
    booked = (p.get("engagements_last_meeting_booked") or "")[:10]
    if booked and start <= booked < end and not any(h[0] == "meeting" for h in out):
        out.append(("meeting", "Meetings link", booked))
    return sorted(out, key=lambda h: h[2])


def classify_by_content(p: dict) -> str:
    t, url = text(p), p.get("hs_analytics_first_url") or ""
    if SPAM_KW.search(t):
        return "spam"
    if NEW_KW.search(t):
        return "new"
    fx, mt = lean(p)
    if fx > mt:
        return "FX"
    if mt > fx:
        return "MT"
    if fx:
        return "mixed"
    if MT_URL.search(url):
        return "MT"
    if FX_URL.search(url):
        return "FX"
    return "unknown"


def bucket(p: dict, start: str, end: str, overrides: dict) -> tuple[str | None, list]:
    """(bucket, hits). bucket None = not a B2B hand-raise in the window at all."""
    h = hits(p, start, end)
    if not h:
        return None, h
    dom = domain(p)
    if dom in OWN or not dom or dom in CONSUMER:
        return None, h
    if dom in overrides:
        o = overrides[dom]
        return (None if o == "exclude" else o), h
    kinds = {k for k, _, _ in h}
    if "fx_form" in kinds:
        fx, mt = lean(p)
        return ("MT" if mt > fx else "FX"), h
    if "shared" in kinds:
        return classify_by_content(p), h
    if "meeting" in kinds:
        if OUTBOUND_LS.search(p.get("lead_source") or ""):
            return "meeting-outbound", h
        return classify_by_content(p), h
    return "content", h


# ------------------------------------------------------------------ periods, ledger, overrides

def quarter_of(day: _dt.date) -> tuple[str, str, str]:
    q = (day.month - 1) // 3
    start = _dt.date(day.year, 3 * q + 1, 1)
    end = _dt.date(day.year + (q == 3), (3 * q + 3) % 12 + 1, 1)
    return f"{day.year}-Q{q + 1}", start.isoformat(), end.isoformat()


def load_json(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    os.chmod(tmp, 0o600)
    tmp.replace(path)


def load_overrides() -> dict:
    raw = load_json(OVERRIDES, {})
    bad = {d: v for d, v in raw.items() if v not in ("FX", "MT", "exclude")}
    if bad:
        raise Broken(f"{OVERRIDES}: values must be FX / MT / exclude, got {bad}")
    return {d.lower(): v for d, v in raw.items()}


PRIORITY = [COUNTED, "new", "MT", "meeting-outbound", "content", "mixed", "spam", "unknown"]


def tally(start: str, end: str, overrides: dict) -> tuple[Counter, list[dict]]:
    """One row per company (email domain): two people from one company are one hand-raise.
    A company takes its strongest bucket (FX first), then its earliest touch in that bucket."""
    best: dict[str, dict] = {}
    for p in search_contacts(start, end):
        b, h = bucket(p, start, end, overrides)
        if b is None:
            continue
        row = {"bucket": b, "domain": domain(p), "form": h[0][1], "kind": h[0][0], "date": h[0][2]}
        cur = best.get(row["domain"])
        if cur is None or (PRIORITY.index(b), row["date"]) < (PRIORITY.index(cur["bucket"]), cur["date"]):
            best[row["domain"]] = row
    rows = list(best.values())
    return Counter(r["bucket"] for r in rows), rows


def with_ledger(qkey: str, rows: list[dict], overrides: dict, save: bool) -> tuple[list[dict], list[dict]]:
    """FX rows for the quarter, sticky across runs. Returns (all FX entries, entries new this run)."""
    ledger = load_json(LEDGER, {})
    q = ledger.setdefault(qkey, {})
    new = []
    for r in rows:
        if r["bucket"] == COUNTED and r["domain"] not in q:
            q[r["domain"]] = {k: r[k] for k in ("form", "kind", "date")}
            new.append(r)
    for dom in [d for d in q if overrides.get(d) in ("MT", "exclude")]:
        del q[dom]
    if save:
        save_json(LEDGER, ledger)
    return [dict(v, domain=k) for k, v in q.items()], new


# ------------------------------------------------------------------ sheet

def find_kr_row() -> tuple[int, str]:
    data = oo(["connector", "run", "googlesheets", "--action", "batch_get", "--data", json.dumps(
        {"spreadsheetId": OKR_SHEET, "ranges": [f"{OKR_TAB}!A1:F80", f"{OKR_TAB}!B1:B3"],
         "valueRenderOption": "UNFORMATTED_VALUE"})])
    vr = data["valueRanges"]
    for i, row in enumerate(vr[0].get("values") or [], start=1):
        if len(row) >= 6 and KR_MARKER.search(str(row[5])):
            label = str((vr[1].get("values") or [[""]])[0][0])
            return i, label
    raise Broken("hand-raisers KR row not found in the OKR sheet (column F, 'KR…: … hand-raisers')")


def sheet_quarter_ok(label: str, qkey: str) -> bool:
    """Sheet B1 is like Q4'26; refuse to write a quarter the sheet is not about."""
    m = re.match(r"Q(\d)'(\d\d)", label.strip())
    return bool(m) and qkey == f"20{m.group(2)}-Q{m.group(1)}"


def write_sheet(row: int, value: int, note: str) -> None:
    oo(["connector", "run", "googlesheets", "--action", "update_values_batch", "--data", json.dumps(
        {"spreadsheetId": OKR_SHEET, "valueInputOption": "RAW",
         "data": [{"range": f"{OKR_TAB}!K{row}", "values": [[value]]}]})])
    req = {"requests": [{"updateCells": {
        "range": {"sheetId": OKR_TAB_ID, "startRowIndex": row - 1, "endRowIndex": row,
                  "startColumnIndex": 10, "endColumnIndex": 11},
        "rows": [{"values": [{"note": note}]}], "fields": "note"}}]}
    oo(["connector", "proxy", "googlesheets", "--method", "POST",
        "--endpoint", f"{SHEETS_URL}/{OKR_SHEET}:batchUpdate", "--body", json.dumps(req)])


# ------------------------------------------------------------------ output

def by_kind(entries: list[dict]) -> str:
    c = Counter({"fx_form": "FX forms", "shared": "Contact us", "meeting": "Meetings"}.get(e["kind"], e["kind"])
                for e in entries)
    return ", ".join(f"{k} {v}" for k, v in c.most_common())


def others_line(counts: Counter, labels: dict = LABELS) -> str:
    return " · ".join(f"{labels[b]} {counts[b]}" for b in SHOWN if counts.get(b))


def send(msg: str) -> bool:
    spec = importlib.util.spec_from_file_location("outbound_pipeline", PIPE)
    op = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(op)
    return op.telegram_send(msg)


# ------------------------------------------------------------------ commands

def cmd_count(args) -> int:
    today = _dt.date.today()
    _, qs, qe = quarter_of(today)
    start, end = args.date_from or qs, args.date_to or qe
    counts, rows = tally(start, end, load_overrides())
    print(f"B2B hand-raisers {start} … {end} (end exclusive)")
    print(f"  FitXpress (counted): {counts.get(COUNTED, 0)}")
    for b in SHOWN:
        print(f"  {b:17s} {counts.get(b, 0)}")
    if args.list:
        print("\nbucket | domain | first qualifying touch | date")
        for r in sorted(rows, key=lambda r: (r["bucket"], r["date"])):
            print(f"{r['bucket']:16s} | {r['domain'][:32]:32s} | {r['form'][:45]:45s} | {r['date']}")
    return 0


def cmd_quarters(args) -> int:
    overrides = load_overrides()
    today = _dt.date.today()
    qs = []
    day = today
    for _ in range(args.n):
        qs.append(quarter_of(day))
        day = _dt.date.fromisoformat(qs[-1][1]) - _dt.timedelta(days=1)
    print("quarter  | FX | " + " | ".join(SHOWN))
    for key, start, end in reversed(qs):
        counts, _ = tally(start, end, overrides)
        part = " (to date)" if end > today.isoformat() else ""
        print(f"{key}{part} | {counts.get(COUNTED, 0)} | " + " | ".join(str(counts.get(b, 0)) for b in SHOWN))
    return 0


def cmd_update_sheet(args) -> int:
    stamp = _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    try:
        overrides = load_overrides()
        qkey, start, end = quarter_of(_dt.date.today())
        counts, rows = tally(start, end, overrides)
        entries, new = with_ledger(qkey, rows, overrides, save=not args.dry_run)
        row, label = find_kr_row()
        if not sheet_quarter_ok(label, qkey):
            msg = f"OKR sheet is for {label!r}, today is {qkey}: not writing. Point OKR_SHEET at the new quarter."
            print(f"[{stamp}] SKIP {msg}")
            if args.notify:
                send(f"🙋 Hand-raisers: {msg}")
            return 0
        value = len(entries)
        note = (f"Auto: hubspot-handraisers.py, {stamp}. {qkey}: {value} FitXpress hand-raisers "
                f"({by_kind(entries) or 'none yet'}). Not counted: {others_line(counts, LABELS_EN) or 'nothing'}.")
        print(f"[{stamp}] {qkey} FX={value} new={len(new)} row=K{row} | {others_line(counts)}")
        if args.dry_run:
            print("dry run: sheet and ledger untouched")
            return 0
        write_sheet(row, value, note)
    except Broken as e:
        print(f"[{stamp}] FAIL {e}")
        if args.notify:
            send(f"⚠️ hubspot-handraisers.py не оновив OKR: {e}"[:TG_LIMIT])
        return 3
    if args.notify:
        lines = [f"🙋 FitXpress hand-raisers · {qkey}: {value} (+{len(new)} за тиждень)"]
        for r in new[:10]:
            lines.append(f"· {r['domain']} — {r['form']} ({r['date']})")
        if len(new) > 10:
            lines.append(f"· …ще {len(new) - 10}")
        if others_line(counts):
            lines.append(f"Не пораховано: {others_line(counts)}")
        lines.append(f"OKR оновлено (K{row}). Перевірити рядки: hubspot-handraisers.py count --list")
        send("\n".join(lines)[:TG_LIMIT])
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("count", help="buckets for a window (default: current quarter)")
    c.add_argument("--from", dest="date_from", help="YYYY-MM-DD, inclusive")
    c.add_argument("--to", dest="date_to", help="YYYY-MM-DD, exclusive")
    c.add_argument("--list", action="store_true", help="print every row (stdout only)")
    c.set_defaults(fn=cmd_count)
    q = sub.add_parser("quarters", help="FX hand-raisers per quarter")
    q.add_argument("--n", type=int, default=4)
    q.set_defaults(fn=cmd_quarters)
    u = sub.add_parser("update-sheet", help="current quarter -> OKR sheet")
    u.add_argument("--notify", action="store_true", help="Telegram summary")
    u.add_argument("--dry-run", action="store_true", help="compute only; no sheet, no ledger")
    u.set_defaults(fn=cmd_update_sheet)
    args = ap.parse_args()
    try:
        return args.fn(args)
    except Broken as e:
        print(f"FAIL {e}", file=sys.stderr)
        return 3


if __name__ == "__main__":
    sys.exit(main())
