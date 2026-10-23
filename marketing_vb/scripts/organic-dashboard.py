#!/usr/bin/env python3
"""organic-dashboard.py — the site-wide organic dashboard for 3dlook.ai (FitXpress, Mobile Tailor,
Wrist Measurement) and weekly keyword tracking. SEO plan phase 0, items 0.6 and 0.7.

WHY THIS EXISTS
---------------
Phase 0 of the FitXpress SEO plan (workspace/research/seo-fitxpress-2026-09/) fixed the measurement:
GA4 lead events since 2026-10-07, UTM and first-touch fields in HubSpot, the source copied onto deals.
Items 0.6 and 0.7 are the read-out: one place where the team and leadership see whether the later
phases (/fitxpress/, vertical landings, refreshes) move clicks, contacts and deals, plus a weekly
check of the keywords. On 2026-10-16 Vadim widened it from FitXpress to the whole site (Mobile Tailor
and Wrist Measurement too). Looker Studio can't create reports in his region, so the dashboard is a
Google Sheet with native charts, filled by this script.

WHAT IT WRITES (one Google Sheet, owned by vadim.bilan@3dlook.me; sharing is done by hand)
  Dashboard     last 4 weeks vs previous 4, quarters vs the plan's targets, key keywords, six charts
                (chart data lives in the hidden tab _chart)
  Weekly        one row per week (Mon-Sun) since 2025-09-29
  Monthly       the same per calendar month, plus FitXpress deals by first-touch source, work-email
                contacts by original source (AI assistants apart from organic) and deals from AI
  Leads by form GA4 generate_lead by form_name, weekly, since the event exists (2026-10-07)
  Contacts by page  work-email contacts by first page seen, last 12 months: top 30 pages, source split, forms
  Recent contacts   every work-email contact of the last 90 days: source, first page, first form, fx_vertical,
                    a link to the HubSpot record (no names or emails: the Sheet is open to the whole domain)
  Rankings      keyword x country: Ahrefs position now, change, Google avg position, last 12 weeks
  Rank history  every keyword x country x week (long format)
  Top pages     last 4 weeks, top 50 pages by Google clicks, with GA4 organic sessions
  About         definitions

SOURCES AND DEFINITIONS
  * Google Search Console (sc-domain:3dlook.ai), final data only. Clicks by page are summed from
    [date, page] rows, so anonymised queries are included. Pages are grouped by URL (PAGE RULES) and
    each group belongs to a product (PRODUCT_OF_GROUP).
  * GA4 property 251675969. Traffic tagged by the "Internal Traffic" and "Developer Traffic" data
    filters (Testing mode since 2026-10-01) is excluded. Organic = session default channel group
    "Organic Search". AI assistants = session source matching AI_SOURCE.
  * HubSpot, read-only (MCP search_crm_objects through `oo connector proxy hubspot`).
    Inbound contact = created in the window with a first conversion, minus Mobile Tailor app forms
    (they are counted as MT sign-ups instead), careers and job seekers, the newsletter, 3DLOOK's own
    domains and outbound-sourced meetings. Work email = not a consumer domain.
    Product of a work-email contact: the form (FX…/MT…/WM…), else the handraisers classifier
    (message text, company, domain, first page; overrides in ~/.hermes/handraisers-overrides.json),
    so the split matches hubspot-handraisers.py.
    MT self-serve sign-ups come from mt-selfserve-report.py (product_signed_up_in, sign-up date
    estimated from the app account id), so they match the sheet Whitney and Kate read.
    Deals: product = pipeline (PIPELINES); source = original_traffic_source copied from the contact
    by the deal workflow (runbook 0.4).
    The two contact tabs replace spec B6 (a HubSpot dashboard), dropped 2026-10-23: HubSpot reports can't
    apply the exclusions and the product classifier above, so they would show other numbers.
  * Ahrefs API v3 site-explorer/organic-keywords for 3dlook.ai on the Sunday of each week (top 100;
    "—" = not in the top 100). ~50 units per country per week, cached in the state file, so only new
    weeks are paid for. Volume and KD from keywords-explorer/overview, refreshed every 30 days.
  * Keywords: workspace/research/seo-fitxpress-2026-09/rank-keywords.csv (tier, keyword, countries,
    target). Edit the CSV, not this file.

WEEKS
  A week is Monday-Sunday. The newest week shown is the last one whose Sunday Search Console already
  has as final data (about two days' lag), so the cron runs on Tuesday morning, again on Wednesday.

STATE (outside the repo; the repo is public)
  ~/.hermes/.organic-dashboard-state.json: spreadsheet id, Ahrefs cache, last reported week.

COMMANDS
  update [--notify] [--dry-run] [--no-ahrefs]   rebuild every tab from the sources; Telegram summary
                                               with --notify (once per week). Cron: Tue and Wed 06:20 UTC;
                                               Wed only reports if GSC had not finalised Sunday on Tue.
  report [--no-ahrefs]                         print the Telegram text, write and send nothing

Exit: 0 ok · 3 broken (oo, an API or the Sheet failed).
"""
from __future__ import annotations

import argparse
import csv
import datetime as _dt
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
KEYWORDS_CSV = HERE.parent / "workspace/research/seo-fitxpress-2026-09/rank-keywords.csv"
STATE = Path.home() / ".hermes" / ".organic-dashboard-state.json"
HANDRAISERS = HERE / "hubspot-handraisers.py"
MT_SELFSERVE = HERE / "mt-selfserve-report.py"
PIPE = HERE / "outbound-pipeline.py"
OO = shutil.which("oo") or str(Path.home() / ".local" / "bin" / "oo")
SECRETS = Path.home() / ".config" / "ai-agent-stack" / "secrets.env"

GA4_PROPERTY = "251675969"
GSC_SITE = "sc-domain:3dlook.ai"
SITE = "https://3dlook.ai"
SHEETS = "https://sheets.googleapis.com/v4/spreadsheets"
MCP_URL = "https://mcp.hubspot.com/"
AHREFS = "https://api.ahrefs.com"
HISTORY_START = _dt.date(2025, 9, 29)          # Monday; Q4 2025 starts that week
Q_START = _dt.date(2025, 10, 1)                # first full quarter shown
GA4_LEADS_SINCE = _dt.date(2026, 10, 7)        # generate_lead went live (runbook 0.2)
# GA4 page tracking was dead 2026-02-05 → 2026-06-25 (data/ga4-findings.md §0.1): ~10-20 sessions/day
# instead of 500-700. Any GA4 figure for a period touching it is shown as a gap, never as a low number.
GA4_GAP = (_dt.date(2026, 2, 5), _dt.date(2026, 6, 25))
TITLE = "3DLOOK Organic Dashboard"
RANK_WEEKS = 12                                 # heat-map columns on the Rankings tab
OVERVIEW_TTL_DAYS = 30

INTERNAL_FILTERS = ["Internal Traffic", "Developer Traffic"]
AI_SOURCE = (r"(chatgpt|openai|perplexity|claude\.ai|anthropic|gemini\.google|bard\.google|copilot|deepseek|"
             r"grok|you\.com|meta\.ai|mistral)")

PRODUCTS = ["FitXpress", "Mobile Tailor", "Wrist Measurement"]
SHORT = {"FitXpress": "FX", "Mobile Tailor": "MT", "Wrist Measurement": "WM"}
PORTAL = 6014382                                # HubSpot account, for record links
PIPELINES = {"67834452": "FitXpress",          # Health & Fitness
             "2491523": "Mobile Tailor", "1666823": "Mobile Tailor", "41462559": "Mobile Tailor",
             "942531392": "Wrist Measurement"}

# ------------------------------------------------------------------ page rules

GROUPS = ["Homepage", "FitXpress pages", "Health & fitness content", "Mobile Tailor pages", "Apparel content",
          "Wrist Measurement", "Body scanning content", "Other pages"]
PRODUCT_OF_GROUP = {"FitXpress pages": "FitXpress", "Health & fitness content": "FitXpress",
                    "Mobile Tailor pages": "Mobile Tailor", "Apparel content": "Mobile Tailor",
                    "Wrist Measurement": "Wrist Measurement",
                    "Homepage": "General", "Body scanning content": "General", "Other pages": "General"}
SITE_PRODUCTS = [*PRODUCTS, "General"]          # "General" = homepage, general body-scanning content, rest

FX_PATH = re.compile(r"^/(fitxpress|for-|structured-body-data-for-telehealth)")
MT_PATH = re.compile(r"^/(mobile-tailor|yourfit|uniform|top-50-sustainable-fashion)")
WRIST = re.compile(r"wrist")
SLUG_OVERRIDES = {   # content-hub slugs the keyword rules get wrong
    "the-enormous-impact-of-daily-physiological-changes-on-the-accuracy-of-our-body-measurements":
        "Body scanning content",
    "fit3d-vs-3dlook": "Body scanning content",
}
APPAREL_SLUG = re.compile(r"cloth|apparel|fashion|garment|tailor|uniform|retail|ecommerce|e-commerce|returns|"
                          r"try-on|fitting-room|dressing|siz(e|ing)|nft|metaverse|sustainab|swim|armor|"
                          r"dickies|burlington|tmall|influencer|made-to-measure|bespoke|manufactur|brand|"
                          r"\bdress|jeans|bridal|footwear|shoe|lingerie|textile|on-demand")
HEALTH_SLUG = re.compile(r"health|fitness|fit-|weight|glp|obes|bmi|body-fat|abs\b|abs-|skinny|lean|muscle|"
                         r"dexa|inbody|bia\b|bia-|body-composition|telehealth|telemed|patient|clinic|"
                         r"bariatric|insur|underwrit|occupational|wellness|pharmac|fitxpress|calorie|"
                         r"nutrition|diet|gym|workout|exercise|medical|rpm|clinical|trial|biometric|"
                         r"smart-scale|longevity|mounjaro|ozempic|wegovy")
BODYSCAN_SLUG = re.compile(r"3d-body|body-scan|scanner|measur|virtual-body|scan-app|body-data|two-photos|"
                           r"take-photos|mobile-body|accuracy|3dlook-turns")


def norm_path(url: str) -> str:
    p = urllib.parse.urlsplit(url).path if "://" in url else url.split("?")[0].split("#")[0]
    p = "/" + p.strip("/")
    return p if p == "/" else p + "/"


def page_group(path: str) -> str:
    if path == "/":
        return "Homepage"
    if WRIST.search(path):
        return "Wrist Measurement"
    if FX_PATH.match(path):
        return "FitXpress pages"
    if MT_PATH.match(path):
        return "Mobile Tailor pages"
    m = re.match(r"^/content-hub/([^/]+)/$", path)
    if not m:
        return "Other pages"
    slug = m.group(1)
    if slug in SLUG_OVERRIDES:
        return SLUG_OVERRIDES[slug]
    if APPAREL_SLUG.search(slug):
        return "Apparel content"
    if HEALTH_SLUG.search(slug):
        return "Health & fitness content"
    if BODYSCAN_SLUG.search(slug):
        return "Body scanning content"
    return "Other pages"


def page_product(path: str) -> str:
    return PRODUCT_OF_GROUP[page_group(path)]


# ------------------------------------------------------------------ dates

def monday(d: _dt.date) -> _dt.date:
    return d - _dt.timedelta(days=d.weekday())


def quarter_key(d: _dt.date) -> str:
    return f"Q{(d.month - 1) // 3 + 1} {d.year}"


def quarter_start(d: _dt.date) -> _dt.date:
    return _dt.date(d.year, 3 * ((d.month - 1) // 3) + 1, 1)


def next_month(d: _dt.date) -> _dt.date:
    return (d.replace(day=1) + _dt.timedelta(days=32)).replace(day=1)


def fmt_day(d: _dt.date) -> str:
    return f"{d.day} {d.strftime('%b')}"


def iso_monday(code: str) -> _dt.date:
    return _dt.date.fromisocalendar(int(code[:4]), int(code[4:]), 1)


def ga4_ok(first: _dt.date, last: _dt.date) -> bool:
    """False when [first, last] touches the GA4 tracking gap."""
    return last < GA4_GAP[0] or first > GA4_GAP[1]


GA4_KEYS = ("org_", "ai_sessions", "leads", "demo_clicks")


# ------------------------------------------------------------------ transport

class Broken(Exception):
    """oo, an API or the Sheet failed. Exit 3."""


def oo(args: list[str], timeout: int = 240) -> dict:
    if not Path(OO).exists():
        raise Broken(f"`oo` CLI not found (looked on PATH and at {OO})")
    try:
        proc = subprocess.run([OO, *args, "--json"], capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        raise Broken(f"oo timed out after {timeout}s: {' '.join(args[:5])}")
    if proc.returncode != 0:
        raise Broken(f"oo exit {proc.returncode}: {(proc.stderr or proc.stdout).strip()[:600]}")
    try:
        return json.loads(proc.stdout)["data"]
    except (ValueError, KeyError):
        raise Broken(f"unexpected oo output: {proc.stdout[:600]}")


def sheets(method: str, path: str, body: dict | None = None) -> dict:
    """Sheets API through the oo proxy. Only absolute URLs work there (memory: reference_google_drive_mcp).

    The request goes in a file (`-d @file`): a few thousand rows overflow the argv limit."""
    req = {"method": method, "endpoint": f"{SHEETS}{path}"}
    if body is not None:
        req["body"] = body
    with tempfile.NamedTemporaryFile("w", suffix=".json", encoding="utf-8") as f:
        json.dump(req, f)
        f.flush()
        data = oo(["connector", "proxy", "googlesheets", "-d", f"@{f.name}"])
    status = data.get("status") or data.get("statusCode")
    payload = data.get("data")
    if (status and int(status) >= 400) or (isinstance(payload, dict) and "error" in payload):
        raise Broken(f"Sheets {method} {path[:80]}: {json.dumps(payload)[:600]}")
    return payload or {}


def ga4(body: dict) -> list[dict]:
    """GA4 Data API run_report; pages through offset until rowCount."""
    rows, offset = [], 0
    while True:
        req = {"propertyId": GA4_PROPERTY, "limit": 100000, **body}
        if offset:
            req["offset"] = offset
        rep = oo(["connector", "run", "google_analytics", "--action", "run_report", "--data", json.dumps(req)])["report"]
        batch = rep.get("rows") or []
        rows += batch
        offset += len(batch)
        if not batch or offset >= int(rep.get("rowCount") or 0):
            return rows


def ga4_filter(*extra: dict) -> dict:
    exprs = [{"notExpression": {"filter": {"fieldName": "testDataFilterName",
                                           "inListFilter": {"values": INTERNAL_FILTERS}}}}, *extra]
    return {"andGroup": {"expressions": exprs}}


def gsc(start: _dt.date, end: _dt.date, dims: list[str], filters: list[dict] | None = None) -> list[dict]:
    rows, start_row = [], 0
    while True:
        req = {"siteUrl": GSC_SITE, "startDate": start.isoformat(), "endDate": end.isoformat(),
               "dimensions": dims, "rowLimit": 25000, "startRow": start_row}
        if filters:
            req["dimensionFilterGroups"] = [{"groupType": "and", "filters": filters}]
        batch = oo(["connector", "run", "google_search_console", "--action", "query_search_analytics",
                    "--data", json.dumps(req)]).get("rows") or []
        rows += batch
        if len(batch) < 25000:
            return rows
        start_row += len(batch)


def hubspot_search(object_type: str, groups: list[dict], props: list[str]) -> list[dict]:
    rows, offset = [], None
    while True:
        args = {"objectType": object_type, "properties": props, "limit": 200, "filterGroups": groups}
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
            raise Broken(f"HubSpot MCP error: {json.dumps(rpc['error'])[:500]}")
        result = rpc.get("result") or {}
        text = "".join(c.get("text", "") for c in result.get("content", []) if c.get("type") == "text")
        if result.get("isError"):
            raise Broken(f"search_crm_objects: {text[:500]}")
        page = json.loads(text)
        batch = page.get("results") or []
        rows += [dict(r.get("properties") or {}, _id=str(r.get("id"))) for r in batch]
        offset = page.get("offset")
        total = int(page.get("total") or 0)
        if not batch or offset in (None, "") or len(rows) >= total:
            if len(rows) < total:
                raise Broken(f"HubSpot search returned {len(rows)} of {total} {object_type} rows")
            return rows


def ahrefs_key() -> str:
    key = os.environ.get("AHREFS_API_KEY", "")
    if not key and SECRETS.exists():
        for line in SECRETS.read_text(encoding="utf-8").splitlines():
            if line.startswith("AHREFS_API_KEY="):
                key = line.split("=", 1)[1].strip().strip('"').strip("'")
    if not key:
        raise Broken("no AHREFS_API_KEY (env or ~/.config/ai-agent-stack/secrets.env)")
    return key


def ahrefs(path: str, params: dict) -> dict:
    url = f"{AHREFS}{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {ahrefs_key()}",
                                               "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise Broken(f"Ahrefs {path} HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:400]}")
    except urllib.error.URLError as e:
        raise Broken(f"Ahrefs {path}: {e}")


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_state() -> dict:
    try:
        return json.loads(STATE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def save_state(state: dict) -> None:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding="utf-8")
    os.chmod(tmp, 0o600)
    tmp.replace(STATE)


# ------------------------------------------------------------------ keywords

TIER_ORDER = {"Brand": 0, "A": 1, "B": 2, "C": 3, "MT": 4, "WM": 5}
GSC_COUNTRY = {"us": "usa", "gb": "gbr"}
COUNTRY_LABEL = {"us": "US", "gb": "UK"}


def load_keywords() -> list[dict]:
    out = []
    with KEYWORDS_CSV.open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            kw = r["keyword"].strip().lower()
            for c in r["countries"].split("|"):
                out.append({"tier": r["tier"].strip(), "keyword": kw, "country": c.strip(),
                            "target": (r.get("target") or "").strip(), "note": (r.get("note") or "").strip()})
    return sorted(out, key=lambda k: (TIER_ORDER.get(k["tier"], 9), k["keyword"], k["country"]))


def re2_escape(s: str) -> str:
    return re.sub(r"([.^$*+?()\[\]{}|\\])", r"\\\1", s)


# ------------------------------------------------------------------ collection

def last_final_sunday() -> _dt.date:
    """Newest Sunday that Search Console already has as final data."""
    today = _dt.date.today()
    rows = gsc(today - _dt.timedelta(days=12), today, ["date"])
    if not rows:
        raise Broken("Search Console returned no final data for the last 12 days")
    last = max(_dt.date.fromisoformat(r["keys"][0]) for r in rows)
    return last - _dt.timedelta(days=(last.weekday() + 1) % 7)


def month_chunks(start: _dt.date, end: _dt.date):
    d = start
    while d <= end:
        nxt = next_month(d)
        yield d, min(end, nxt - _dt.timedelta(days=1))
        d = nxt


def collect_gsc_pages(start: _dt.date, end: _dt.date) -> list[tuple]:
    """(day, path, clicks, impressions, position*impressions)."""
    out = []
    for a, b in month_chunks(start, end):
        for r in gsc(a, b, ["date", "page"]):
            out.append((_dt.date.fromisoformat(r["keys"][0]), norm_path(r["keys"][1]), r["clicks"],
                        r["impressions"], r["position"] * r["impressions"]))
    return out


def collect_gsc_keywords(start: _dt.date, end: _dt.date, kws: list[dict]) -> list[tuple]:
    """(day, query, country, clicks, impressions, position*impressions) for the tracked keywords."""
    words = sorted({k["keyword"] for k in kws})
    filters = [{"dimension": "query", "operator": "includingRegex",
                "expression": "^(" + "|".join(re2_escape(w) for w in words) + ")$"},
               {"dimension": "country", "operator": "includingRegex", "expression": "^(usa|gbr)$"}]
    out = []
    for a, b in month_chunks(start, end):
        for r in gsc(a, b, ["date", "query", "country"], filters):
            out.append((_dt.date.fromisoformat(r["keys"][0]), r["keys"][1].lower(), r["keys"][2],
                        r["clicks"], r["impressions"], r["position"] * r["impressions"]))
    return out


def collect_ga4(start: _dt.date, end: _dt.date) -> dict:
    rng = [{"startDate": start.isoformat(), "endDate": end.isoformat()}]
    organic = {"filter": {"fieldName": "sessionDefaultChannelGroup",
                          "stringFilter": {"matchType": "EXACT", "value": "Organic Search"}}}
    ai = {"filter": {"fieldName": "sessionSource",
                     "stringFilter": {"matchType": "PARTIAL_REGEXP", "value": AI_SOURCE, "caseSensitive": False}}}
    events = {"filter": {"fieldName": "eventName", "inListFilter": {"values": ["generate_lead", "demo_click"]}}}
    res = {}
    # daily rows: one dataset serves weeks, months and quarters exactly
    res["landing"] = [(_dt.date.fromisoformat(f"{r['dimensions']['date'][:4]}-{r['dimensions']['date'][4:6]}-"
                                              f"{r['dimensions']['date'][6:]}"),
                       norm_path(r["dimensions"]["landingPage"]), int(r["metrics"]["sessions"]),
                       int(r["metrics"]["engagedSessions"]), int(float(r["metrics"]["keyEvents"])))
                      for r in ga4({"dateRanges": rng, "dimensions": ["date", "landingPage"],
                                    "metrics": ["sessions", "engagedSessions", "keyEvents"],
                                    "dimensionFilter": ga4_filter(organic)})]
    res["ai"] = [(_dt.date.fromisoformat(f"{r['dimensions']['date'][:4]}-{r['dimensions']['date'][4:6]}-"
                                         f"{r['dimensions']['date'][6:]}"), int(r["metrics"]["sessions"]))
                 for r in ga4({"dateRanges": rng, "dimensions": ["date"], "metrics": ["sessions"],
                               "dimensionFilter": ga4_filter(ai)})]
    res["events"] = [(_dt.date.fromisoformat(f"{r['dimensions']['date'][:4]}-{r['dimensions']['date'][4:6]}-"
                                             f"{r['dimensions']['date'][6:]}"), r["dimensions"]["eventName"],
                      r["dimensions"].get("customEvent:form_name") or "(not set)", int(r["metrics"]["eventCount"]))
                     for r in ga4({"dateRanges": rng, "dimensions": ["date", "eventName", "customEvent:form_name"],
                                   "metrics": ["eventCount"], "dimensionFilter": ga4_filter(events)})]
    return res


PERSONAL_PREFIX = re.compile(r"^(gmail|googlemail|yahoo|ymail|hotmail|outlook|live|msn|icloud|aol|yandex|"
                             r"mail|proton|protonmail|gmx|zoho|rediffmail)\.")
MT_APP_FORM = re.compile(r"MTM|MT log in form|MT Trial Sign up|^\.(signup-form|login)|\.ng-", re.I)
CAREERS = re.compile(r"career|^HR \|", re.I)
NEWSLETTER = re.compile(r"newsletter|subscribe", re.I)
FORM_FX = re.compile(r"^FX\b|FX Starter|FX Pricing|FX Pro\b|Telehealth & Weight Loss|Connected & Digital Fitness|"
                     r"Health & Fitness LP|Downloadable content", re.I)
FORM_MT = re.compile(r"^MT\b|Pricing page \(Entreprise|Enterprise plan", re.I)
FORM_WM = re.compile(r"^WM\b|\bWM Landing|wrist", re.I)
WRIST_TEXT = re.compile(r"wrist|watch|bracelet", re.I)
SOURCE_LABEL = {"ORGANIC_SEARCH": "Organic search", "AI_REFERRALS": "AI assistants", "DIRECT_TRAFFIC": "Direct",
                "REFERRALS": "Referrals", "SOCIAL_MEDIA": "Social", "PAID_SEARCH": "Paid", "PAID_SOCIAL": "Paid",
                "EMAIL_MARKETING": "Email & campaigns", "OTHER_CAMPAIGNS": "Email & campaigns", "OFFLINE": "Offline"}
SOURCES = ["Organic search", "AI assistants", "Direct", "Referrals", "Social", "Paid", "Email & campaigns",
           "Offline", "Not set"]


def page_label(url: str | None) -> str | None:
    """First page seen as a path on 3dlook.ai, or host + path elsewhere (the MT app, old domains)."""
    if not url:
        return None
    host = urllib.parse.urlsplit(url).netloc.lower().removeprefix("www.") if "://" in url else ""
    return norm_path(url) if host in ("", "3dlook.ai") else host + norm_path(url).rstrip("/")


def collect_hubspot(start: _dt.date, end: _dt.date) -> dict:
    hr = load_module("hubspot_handraisers", HANDRAISERS)
    overrides = hr.load_overrides()
    lo, hi = f"{start.isoformat()}T00:00:00Z", f"{(end + _dt.timedelta(days=1)).isoformat()}T00:00:00Z"
    window = [{"propertyName": "createdate", "operator": "GTE", "value": lo},
              {"propertyName": "createdate", "operator": "LT", "value": hi}]
    props = sorted(set(hr.PROPS) | {"createdate", "hs_analytics_source", "hs_analytics_source_data_1",
                                     "icp_segment", "fx_vertical"})
    contacts = hubspot_search("CONTACT", [{"filters": window + [{"propertyName": "first_conversion_event_name",
                                                                  "operator": "HAS_PROPERTY"}]}], props)
    inbound, dropped = [], defaultdict(int)
    for p in contacts:
        form = hr.form(p.get("first_conversion_event_name"))
        dom = hr.domain(p)
        reason = ("mt_app" if MT_APP_FORM.search(p.get("first_conversion_event_name") or "") else
                  "careers" if CAREERS.search(form) or p.get("icp_segment") == "Job seeker" else
                  "newsletter" if NEWSLETTER.search(form) else
                  "own" if dom in hr.OWN else
                  "outbound" if hr.OUTBOUND_LS.search(p.get("lead_source") or "") else None)
        if reason:
            dropped[reason] += 1
            continue
        work = bool(dom) and dom not in hr.CONSUMER and not PERSONAL_PREFIX.match(dom)
        product = None
        if work:
            if dom in overrides and overrides[dom] in ("FX", "MT"):
                product = {"FX": "FitXpress", "MT": "Mobile Tailor"}[overrides[dom]]
            elif FORM_WM.search(form):
                product = "Wrist Measurement"
            elif FORM_FX.search(form):
                fx, mt = hr.lean(p)
                product = "Mobile Tailor" if mt > fx else "FitXpress"
            elif FORM_MT.search(form):
                product = "Mobile Tailor"
            else:
                c = hr.classify_by_content(p)
                product = ("FitXpress" if c == "FX" else "Mobile Tailor" if c == "MT" else
                           "Wrist Measurement" if c == "new" and WRIST_TEXT.search(hr.text(p)) else
                           page_product(norm_path(p.get("hs_analytics_first_url") or "/x"))
                           if c == "unknown" else "Not assigned")
                if product == "General":
                    product = "Not assigned"
        src = p.get("hs_analytics_source") or ""
        inbound.append({"day": _dt.date.fromisoformat(p["createdate"][:10]), "work": work, "product": product,
                        "organic": src in ("ORGANIC_SEARCH", "AI_REFERRALS"),
                        "source": SOURCE_LABEL.get(src, "Not set"), "source_detail": p.get("hs_analytics_source_data_1"),
                        "page": page_label(p.get("hs_analytics_first_url")), "form": form or None,
                        "fx_vertical": p.get("fx_vertical"), "id": p["_id"]})

    deals = []
    for d in hubspot_search("DEAL", [{"filters": window}],
                            ["createdate", "pipeline", "original_traffic_source", "hs_is_closed_won"]):
        ots = d.get("original_traffic_source") or ""
        src = ("Organic search & AI" if ots in ("Organic Search", "AI Referrals") else
               "Direct" if ots == "Direct Traffic" else
               "Offline & outbound" if ots == "Offline Sources" else "Other")
        deals.append({"day": _dt.date.fromisoformat(d["createdate"][:10]),
                      "product": PIPELINES.get(d.get("pipeline") or "", "Other"),
                      "source": src, "ai": ots == "AI Referrals", "won": d.get("hs_is_closed_won") == "true"})

    mt = load_module("mt_selfserve_report", MT_SELFSERVE)
    rows, _stats = mt.build_rows(mt.pull_app_users(), end)
    signups = []
    for r in rows:
        if r["Sign-up date"] is None:
            continue
        day = _dt.date(1899, 12, 30) + _dt.timedelta(days=r["Sign-up date"])
        if start <= day <= end:
            signups.append({"day": day, "organic": r["Original source"] in ("Organic search", "AI assistants")})
    return {"contacts": inbound, "deals": deals, "signups": signups, "raw_contacts": len(contacts),
            "dropped": dict(dropped)}


def collect_ahrefs(kws: list[dict], sundays: list[_dt.date], state: dict, use_api: bool) -> dict:
    """{(sunday, country): {keyword: [position, url]}}; only weeks missing from the cache hit the API.

    A cached week is re-fetched when the keyword list gained words since (the CSV changed)."""
    cache = state.setdefault("ahrefs", {})
    asked = state.setdefault("ahrefs_asked", {})
    by_country = defaultdict(set)
    for k in kws:
        by_country[k["country"]].add(k["keyword"])
    out = {}
    for sun in sundays:
        for c, ws in by_country.items():
            ck = f"{sun.isoformat()}|{c}"
            if use_api and (ck not in cache or not ws <= set(asked.get(ck, []))):
                where = {"or": [{"field": "keyword", "is": ["eq", w]} for w in sorted(ws)]}
                data = ahrefs("/v3/site-explorer/organic-keywords",
                              {"target": "3dlook.ai", "mode": "subdomains", "country": c, "date": sun.isoformat(),
                               "select": "keyword,best_position,best_position_url", "where": json.dumps(where),
                               "limit": 1000})
                cache[ck] = {r["keyword"].lower(): [r.get("best_position"), r.get("best_position_url")]
                             for r in data.get("keywords") or []}
                asked[ck] = sorted(ws)
            if ck in cache:
                out[(sun, c)] = cache[ck]
    ov = state.setdefault("overview", {})
    fetched = ov.get("fetched")
    stale = not fetched or (_dt.date.today() - _dt.date.fromisoformat(fetched)).days >= OVERVIEW_TTL_DAYS
    if use_api and (stale or any(k["keyword"] not in ov.get(k["country"], {}) for k in kws)):
        for c, ws in by_country.items():
            data = ahrefs("/v3/keywords-explorer/overview",
                          {"country": c, "keywords": ",".join(sorted(ws)), "select": "keyword,volume,difficulty"})
            ov[c] = {r["keyword"].lower(): [r.get("volume"), r.get("difficulty")] for r in data.get("keywords") or []}
            for w in ws:                 # no row = Ahrefs has no figure; keep it explicit, never 0
                ov[c].setdefault(w, [None, None])
        ov["fetched"] = _dt.date.today().isoformat()
    return out


# ------------------------------------------------------------------ aggregation

class Agg:
    """Sums keyed by metric name, per week, month and quarter, from dated facts."""

    def __init__(self, weeks: list[_dt.date], end: _dt.date):
        self.end = end
        self.W = {wk: defaultdict(float) for wk in weeks}
        self.M: dict[str, defaultdict] = {}
        d = Q_START
        while d <= end:
            self.M[d.strftime("%Y-%m")] = defaultdict(float)
            d = next_month(d)
        self.Q: dict[str, defaultdict] = defaultdict(lambda: defaultdict(float))

    def add(self, day: _dt.date, key: str, value: float = 1) -> None:
        if day > self.end:
            return
        wk = self.W.get(monday(day))
        if wk is not None:
            wk[key] += value
        if day >= Q_START:
            self.M[day.strftime("%Y-%m")][key] += value
            self.Q[quarter_key(day)][key] += value


def build(end: _dt.date, gsc_pages, gsc_kw, ga, hs, ahr, kws, state) -> dict:
    weeks = []
    w = HISTORY_START
    while w + _dt.timedelta(days=6) <= end:
        weeks.append(w)
        w += _dt.timedelta(days=7)
    A = Agg(weeks, end)
    for day, path, clicks, impr, _ in gsc_pages:
        g = page_group(path)
        A.add(day, "clicks", clicks)
        A.add(day, f"clicks|{g}", clicks)
        A.add(day, f"clicks|{PRODUCT_OF_GROUP[g]}", clicks)
        A.add(day, "impr", impr)
    for day, path, s, e, _ in ga["landing"]:
        p = page_product(path)
        A.add(day, "org_sessions", s)
        A.add(day, "org_engaged", e)
        A.add(day, f"org_engaged|{p}", e)
    for day, s in ga["ai"]:
        A.add(day, "ai_sessions", s)
    forms = defaultdict(lambda: defaultdict(int))
    for day, ev, form, cnt in ga["events"]:
        if ev == "generate_lead":
            A.add(day, "leads", cnt)
            if monday(day) in A.W:
                forms[monday(day)][form] += cnt
        else:
            A.add(day, "demo_clicks", cnt)
    for c in hs["contacts"]:
        if c["work"]:
            A.add(c["day"], "work")
            A.add(c["day"], f"work|{c['product']}")
            A.add(c["day"], f"work_src|{c['source']}")
            if c["organic"]:
                A.add(c["day"], "work_organic")
                A.add(c["day"], f"work_organic|{c['product']}")
        else:
            A.add(c["day"], "personal")
    for d in hs["deals"]:
        A.add(d["day"], f"deals|{d['product']}")
        if d["source"] == "Organic search & AI":
            A.add(d["day"], f"deals_organic|{d['product']}")
        if d["ai"]:
            A.add(d["day"], "deals_ai")
        if d["won"]:
            A.add(d["day"], f"won|{d['product']}")
        if d["product"] == "FitXpress":
            A.add(d["day"], f"fx_src|{d['source']}")
    for s in hs["signups"]:
        A.add(s["day"], "mt_signups")
        if s["organic"]:
            A.add(s["day"], "mt_signups_organic")

    since = weeks[-4]
    top = defaultdict(lambda: defaultdict(float))
    for day, path, clicks, impr, posw in gsc_pages:
        if since <= day <= end:
            top[path]["clicks"] += clicks
            top[path]["impr"] += impr
            top[path]["posw"] += posw
    for day, path, s, e, k in ga["landing"]:
        if since <= day <= end:
            top[path]["sessions"] += s
            top[path]["engaged"] += e
            top[path]["key_events"] += k

    gkw = defaultdict(lambda: defaultdict(float))
    rev_country = {v: k for k, v in GSC_COUNTRY.items()}
    for day, q, ctry, clicks, impr, posw in gsc_kw:
        c = rev_country.get(ctry)
        if c and monday(day) in A.W:
            a = gkw[(monday(day), q, c)]
            a["clicks"] += clicks
            a["impr"] += impr
            a["posw"] += posw
    return {"weeks": weeks, "A": A, "forms": forms, "top": top, "gkw": gkw, "ahr": ahr, "kws": kws,
            "end": end, "overview": state.get("overview", {}), "work": [c for c in hs["contacts"] if c["work"]]}


# ------------------------------------------------------------------ sheet values

TABS = ["Dashboard", "Weekly", "Monthly", "Leads by form", "Contacts by page", "Recent contacts", "Rankings",
        "Rank history", "Top pages", "About", "_chart"]
PAGE_DAYS, PAGE_TOP, RECENT_DAYS = 365, 30, 90
BLUE, ORANGE, AQUA, YELLOW, MAGENTA, GRAY = "#143DFF", "#EB6834", "#1BAF7A", "#EDA100", "#E87BA4", "#A8A8A8"
NAVY, INK, MUTED, LINE = "#050F40", "#1A1A1A", "#666666", "#E5E5E5"
PRODUCT_COLOR = {"FitXpress": BLUE, "Mobile Tailor": ORANGE, "Wrist Measurement": AQUA, "General": GRAY,
                 "Not assigned": GRAY}
FORM_GROUPS = [("FitXpress pricing", lambda f: f.startswith("fx_"), BLUE),
               ("Mobile Tailor pricing", lambda f: f == "pricing_enterprise", ORANGE),
               ("Contact us", lambda f: f == "contact_us", YELLOW),
               ("Homepage popup", lambda f: f == "home_popup", MAGENTA)]


def n(x):
    """Whole numbers as int; None stays an empty cell."""
    if x is None:
        return None
    return int(round(x)) if abs(x - round(x)) < 1e-9 else round(x, 1)


def pct_change(cur, prev):
    if not prev or cur is None:
        return None
    return (cur - prev) / prev


def tab_values(r: dict) -> dict:
    weeks, A, end, kws = r["weeks"], r["A"], r["end"], r["kws"]
    W, M, Q = A.W, A.M, A.Q
    out = {}
    lead_weeks = [wk for wk in weeks if wk + _dt.timedelta(days=6) >= GA4_LEADS_SINCE]

    def metric_cols(a, lead_ok, ga_ok=True):
        g = (lambda x: n(x)) if ga_ok else (lambda x: None)
        return [n(a["clicks"]), *[n(a[f"clicks|{p}"]) for p in SITE_PRODUCTS], *[n(a[f"clicks|{g_}"]) for g_ in GROUPS],
                n(a["impr"]), g(a["org_sessions"]), g(a["org_engaged"]),
                *[g(a[f"org_engaged|{p}"]) for p in SITE_PRODUCTS], g(a["ai_sessions"]),
                n(a["leads"]) if lead_ok else None, n(a["demo_clicks"]) if lead_ok else None,
                n(a["work"]), *[n(a[f"work|{p}"]) for p in [*PRODUCTS, "Not assigned"]], n(a["work_organic"]),
                *[n(a[f"work_organic|{p}"]) for p in PRODUCTS], n(a["personal"]),
                n(a["mt_signups"]), n(a["mt_signups_organic"]),
                *[v for p in PRODUCTS for v in (n(a[f"deals|{p}"]), n(a[f"deals_organic|{p}"]))]]

    metric_hdr = ["Google clicks: whole site", *[f"Google clicks: {p}" for p in SITE_PRODUCTS],
                  *[f"Google clicks: {g}" for g in GROUPS], "Google impressions: whole site",
                  "GA4 organic sessions", "GA4 engaged organic sessions",
                  *[f"Engaged organic sessions: {p}" for p in SITE_PRODUCTS], "Sessions from AI assistants",
                  "Website leads (GA4 generate_lead)", "Demo clicks (GA4 demo_click)",
                  "Inbound contacts, work email: all", *[f"Inbound contacts, work email: {p}" for p in PRODUCTS],
                  "Inbound contacts, work email: not assigned", "Work-email contacts from organic search or AI: all",
                  *[f"Work-email contacts from organic search or AI: {p}" for p in PRODUCTS],
                  "Inbound contacts, personal email", "Mobile Tailor self-serve sign-ups",
                  "MT sign-ups from organic search or AI",
                  *[h for p in PRODUCTS for h in (f"New deals: {p}", f"New deals from organic search or AI: {p}")]]
    out["Weekly"] = [["Week (Mon)", *metric_hdr, "Note"]] + [
        [wk.isoformat(), *metric_cols(W[wk], wk + _dt.timedelta(days=6) >= GA4_LEADS_SINCE,
                                      ga4_ok(wk, wk + _dt.timedelta(days=6))),
         "GA4 not recording" if not ga4_ok(wk, wk + _dt.timedelta(days=6)) else None] for wk in weeks]

    srcs = ["Organic search & AI", "Direct", "Offline & outbound", "Other"]
    rows = [["Month", *metric_hdr, *[f"FitXpress deals: {s}" for s in srcs],
             *[f"Deals won so far: {p}" for p in PRODUCTS],
             *[f"Work-email contacts by source: {s}" for s in SOURCES], "New deals from AI assistants: all products",
             "Note"]]
    for ym, a in M.items():
        first = _dt.date.fromisoformat(ym + "-01")
        last = next_month(first) - _dt.timedelta(days=1)
        ok = ga4_ok(first, last)
        note = "; ".join(x for x in (f"to {fmt_day(end)}" if end < last else "",
                                     "" if ok else "GA4 not recording 5 Feb – 25 Jun 2026") if x)
        rows.append([first.isoformat(), *metric_cols(a, next_month(first) > GA4_LEADS_SINCE, ok),
                     *[n(a[f"fx_src|{s}"]) for s in srcs], *[n(a[f"won|{p}"]) for p in PRODUCTS],
                     *[n(a[f"work_src|{s}"]) for s in SOURCES], n(a["deals_ai"]), note or None])
    out["Monthly"] = rows

    totals = defaultdict(int)
    for wk in lead_weeks:
        for f, c in r["forms"].get(wk, {}).items():
            totals[f] += c
    forms = sorted(totals, key=lambda f: (-totals[f], f))
    out["Leads by form"] = [["Week (Mon)", *forms, "Total", "Demo clicks"]] + [
        [wk.isoformat(), *[r["forms"].get(wk, {}).get(f, 0) for f in forms], sum(r["forms"].get(wk, {}).values()),
         n(W[wk]["demo_clicks"])] for wk in lead_weeks]

    # ---- work-email contacts by first page and the recent ones one by one (spec B6, reports 2, 4 and 5)
    year_ago, recent = end - _dt.timedelta(days=PAGE_DAYS - 1), end - _dt.timedelta(days=RECENT_DAYS - 1)
    pages = defaultdict(lambda: {"all": 0, "organic": 0, "ai": 0, "recent": 0, "forms": defaultdict(int),
                                 "last": None})
    for c in r["work"]:
        if not year_ago <= c["day"] <= end:
            continue
        a = pages[c["page"] or "(not set)"]
        a["all"] += 1
        a["organic"] += c["source"] == "Organic search"
        a["ai"] += c["source"] == "AI assistants"
        a["recent"] += c["day"] >= recent
        a["forms"][c["form"] or "(none)"] += 1
        a["last"] = max(a["last"] or c["day"], c["day"])
    ranked = sorted(pages.items(), key=lambda kv: (-kv[1]["all"], -kv[1]["organic"] - kv[1]["ai"], kv[0]))
    rows = [["First page seen", "Product of the page", f"Work-email contacts, {fmt_day(year_ago)} {year_ago.year} – "
             f"{fmt_day(end)} {end.year}", "From organic search", "From AI assistants", "From other sources",
             f"Last {RECENT_DAYS} days", "First form (contacts)", "Latest contact"]]
    for page, a in ranked[:PAGE_TOP]:
        forms_txt = "; ".join(f"{f} ×{k}" for f, k in sorted(a["forms"].items(), key=lambda fk: (-fk[1], fk[0]))[:4])
        rows.append([page, page_product(page) if page.startswith("/") else None if page == "(not set)" else
                     "Other site", a["all"], a["organic"],
                     a["ai"], a["all"] - a["organic"] - a["ai"], a["recent"], forms_txt, a["last"].isoformat()])
    rest = [a for _, a in ranked[PAGE_TOP:]]
    if rest:
        rows.append([f"Other pages ({len(rest)})", None, *[sum(a[k] for a in rest) for k in ("all", "organic", "ai")],
                     sum(a["all"] - a["organic"] - a["ai"] for a in rest), sum(a["recent"] for a in rest), None, None])
    out["Contacts by page"] = rows
    out["Recent contacts"] = [["Created", "Product", "Original source", "Source detail", "First page seen",
                               "First form", "FX vertical", "HubSpot"]] + [
        [c["day"].isoformat(), c["product"], c["source"], c["source_detail"], c["page"], c["form"], c["fx_vertical"],
         f'=HYPERLINK("https://app.hubspot.com/contacts/{PORTAL}/record/0-1/{c["id"]}","Open")']
        for c in sorted(r["work"], key=lambda c: (c["day"], c["id"]), reverse=True) if recent <= c["day"] <= end]

    # ---- keywords
    sundays = [wk + _dt.timedelta(days=6) for wk in weeks]
    heat = sundays[-RANK_WEEKS:]
    ov = r["overview"]

    def apos(sun, k):
        snap = r["ahr"].get((sun, k["country"]))
        if snap is None:
            return None, None
        hit = snap.get(k["keyword"])
        return (hit[0], hit[1]) if hit and hit[0] is not None else ("—", None)

    def gpos(wks, k):
        """Impression-weighted Google position over one or more weeks: (position, impressions, clicks)."""
        imp = clk = posw = 0.0
        for wk in wks:
            a = r["gkw"].get((wk, k["keyword"], k["country"]))
            if a:
                imp += a["impr"]
                clk += a["clicks"]
                posw += a["posw"]
        return (round(posw / imp, 1), n(imp), n(clk)) if imp else (None, None, None)

    def delta(now, then):
        if isinstance(now, (int, float)) and isinstance(then, (int, float)):
            return round(then - now, 1)
        if isinstance(now, (int, float)) and then in ("—", None):
            return "new"
        if now in ("—", None) and isinstance(then, (int, float)):
            return "lost"
        return None

    last4w, prev4w = weeks[-4:], weeks[-8:-4]
    hdr = ["Tier", "Keyword", "Country", "Volume (Ahrefs)", "KD", "Target",
           "Google avg position, last 4 weeks", "Google avg position, previous 4 weeks", "Change",
           "Google impressions, last 4 weeks", "Google clicks, last 4 weeks", "Ahrefs position (latest week)",
           "Ahrefs ranking URL", *[s.isoformat() for s in heat]]
    rows = [hdr]
    for k in kws:
        g_now, g_imp, g_clk = gpos(last4w, k)
        g_prev = gpos(prev4w, k)[0]
        a_now, url = apos(sundays[-1], k)
        vol, kd = ov.get(k["country"], {}).get(k["keyword"]) or [None, None]
        rows.append([k["tier"], k["keyword"], COUNTRY_LABEL[k["country"]], vol, kd,
                     int(k["target"]) if k["target"] else None, g_now, g_prev,
                     delta(g_now, g_prev) if (g_now or g_prev) else None, g_imp, g_clk, a_now,
                     (url or "").replace(SITE, "") or None,
                     *[gpos([s - _dt.timedelta(days=6)], k)[0] for s in heat]])
    out["Rankings"] = rows

    # week-on-week moves for Telegram: Google (5+ impressions in both weeks) and Ahrefs
    alerts = []

    def crossed(a, b):
        return [t for t in (3, 10) if (b <= t < a) or (a <= t < b)]
    for k in kws:
        label = f"{k['keyword']} ({COUNTRY_LABEL[k['country']]})"
        g1, i1, _ = gpos([weeks[-1]], k)
        g0, i0, _ = gpos([weeks[-2]], k)
        if g1 is not None and g0 is not None and i1 >= 5 and i0 >= 5:
            c = crossed(g0, g1)
            if abs(g0 - g1) >= 3 or c:
                up = g1 < g0
                tag = f" · {'в' if up else 'з'} топ-{c[0]}" if c else ""
                alerts.append((0 if up else 1, f"{'⬆️' if up else '⬇️'} Google: {label} {g0:g} → {g1:g}{tag}"))
        a1, a0 = apos(sundays[-1], k)[0], apos(sundays[-2], k)[0]
        if isinstance(a1, (int, float)) and isinstance(a0, (int, float)):
            c = crossed(a0, a1)
            if abs(a0 - a1) >= 3 or c:
                up = a1 < a0
                tag = f" · {'в' if up else 'з'} топ-{c[0]}" if c else ""
                alerts.append((0 if up else 1, f"{'⬆️' if up else '⬇️'} Ahrefs: {label} {a0} → {a1}{tag}"))
        elif isinstance(a1, (int, float)) and a0 == "—" and a1 <= 20:
            alerts.append((0, f"🆕 Ahrefs: {label} → {a1}"))
        elif a1 == "—" and isinstance(a0, (int, float)) and a0 <= 20:
            alerts.append((1, f"⬇️ Ahrefs: {label} {a0} → поза топ-100"))
    out["_alerts"] = [m for _, m in sorted(alerts)]
    rows = [["Week ending (Sun)", "Tier", "Keyword", "Country", "Position (Ahrefs)", "Ranking URL",
             "Google avg position", "Google impressions", "Google clicks"]]
    for wk, sun in zip(weeks, sundays):
        for k in kws:
            p, url = apos(sun, k)
            gp, gi, gc = gpos([wk], k)
            rows.append([sun.isoformat(), k["tier"], k["keyword"], COUNTRY_LABEL[k["country"]], p,
                         (url or "").replace(SITE, "") or None, gp, gi, gc])
    out["Rank history"] = rows

    top = sorted(r["top"].items(), key=lambda kv: (-kv[1]["clicks"], kv[0]))[:50]
    out["Top pages"] = [["Page", "Group", "Product", "Google clicks", "Google impressions", "Google avg position",
                         "GA4 organic sessions", "GA4 engaged organic sessions", "GA4 key events (organic)"]] + [
        [path, page_group(path), page_product(path), n(a["clicks"]), n(a["impr"]),
         round(a["posw"] / a["impr"], 1) if a["impr"] else None, n(a["sessions"]), n(a["engaged"]),
         n(a["key_events"])] for path, a in top]

    # ---- Dashboard
    last4, prev4 = weeks[-4:], weeks[-8:-4]

    def kpi(label, key, lead=False):
        cur = sum(W[wk][key] for wk in last4)
        if key.startswith(GA4_KEYS) and not all(ga4_ok(wk, wk + _dt.timedelta(days=6)) for wk in last4):
            return [label, "GA4 gap", "—", None]
        if (lead and prev4[0] < monday(GA4_LEADS_SINCE)) or (
                key.startswith(GA4_KEYS) and not all(ga4_ok(wk, wk + _dt.timedelta(days=6)) for wk in prev4)):
            return [label, n(cur), "—", None]
        prev = sum(W[wk][key] for wk in prev4)
        return [label, n(cur), n(prev), pct_change(cur, prev)]

    d = [[TITLE],
         [f"FitXpress · Mobile Tailor · Wrist Measurement. Weeks run Monday to Sunday; data through Sunday "
          f"{fmt_day(end)} {end.year}; updated {_dt.date.today().isoformat()}. Sources: Google Search Console, "
          f"GA4 (internal traffic excluded), HubSpot, Ahrefs. Definitions: tab About."],
         [],
         ["Last 4 weeks vs previous 4", f"{fmt_day(last4[0])} – {fmt_day(end)}",
          f"{fmt_day(prev4[0])} – {fmt_day(prev4[-1] + _dt.timedelta(days=6))}", "Change"],
         kpi("Organic Google clicks, whole site", "clicks"),
         *[kpi(f"   {p} pages and content", f"clicks|{p}") for p in PRODUCTS],
         kpi("   Homepage and general pages", "clicks|General"),
         kpi("Engaged organic sessions, whole site (GA4)", "org_engaged"),
         kpi("Sessions from AI assistants (ChatGPT, Perplexity, Gemini …)", "ai_sessions"),
         kpi("Inbound contacts with a work email", "work"),
         *[kpi(f"   {p}", f"work|{p}") for p in PRODUCTS],
         kpi("   not assigned to a product", "work|Not assigned"),
         kpi("   of all work-email contacts: from organic search or AI", "work_organic"),
         kpi("Mobile Tailor self-serve sign-ups", "mt_signups"),
         kpi("   of them from organic search or AI", "mt_signups_organic"),
         *[kpi(f"New deals: {p}", f"deals|{p}") for p in PRODUCTS],
         kpi("Website leads (GA4, tracked since 7 Oct 2026)", "leads", lead=True)]
    kpi_rows = (4, len(d) - 1)
    d.append([])
    qs = []
    q = Q_START
    while q <= end:
        qs.append(q)
        q = next_month(next_month(next_month(q)))
    q_hdr_row = len(d)
    d.append(["By quarter", *[quarter_key(x) + (" to date" if quarter_start(end) == x else "") for x in qs],
              "Target (FitXpress plan)"])

    def qrow(label, key, target="", since=None):
        def cell(x):
            last = next_month(next_month(next_month(x))) - _dt.timedelta(days=1)
            if since is not None and last < since:
                return "—"
            if key.startswith(GA4_KEYS) and not ga4_ok(x, min(last, end)):
                return "GA4 gap"
            return n(Q[quarter_key(x)][key])
        return [label, *[cell(x) for x in qs], target]
    d += [qrow("FitXpress deals from organic search or AI", "deals_organic|FitXpress", "6–8 per quarter"),
          *[qrow(f"New deals: {p}", f"deals|{p}") for p in PRODUCTS],
          qrow("Work-email contacts from organic search or AI, all products", "work_organic", "120+ per quarter"),
          *[qrow(f"   {p}", f"work_organic|{p}") for p in PRODUCTS],
          qrow("Mobile Tailor self-serve sign-ups from organic search or AI", "mt_signups_organic"),
          *[qrow(f"Organic Google clicks: {p} pages and content", f"clicks|{p}",
                 "×2–3" if p == "FitXpress" else "") for p in PRODUCTS],
          qrow("Sessions from AI assistants", "ai_sessions", "×2"),
          qrow("Website leads (GA4)", "leads", "> 0 every month", since=GA4_LEADS_SINCE)]
    q_rows = (q_hdr_row + 1, len(d) - 1)
    d.append([])
    cat_hdr_row = len(d)
    d.append(["Key keywords, US (Google avg position)", "Last 4 weeks", "Previous 4 weeks", "Ahrefs, latest week",
              "Target"])
    cat = [k for k in kws if k["country"] == "us" and
           (k["tier"] == "B" or k["keyword"] in ("fitxpress", "bmi verification", "ai body measurement", "ai tailor",
                                                 "mobile tailor", "wrist measurement", "wrist size"))]
    for k in cat:
        d.append([k["keyword"], gpos(last4w, k)[0] or "—", gpos(prev4w, k)[0] or "—", apos(sundays[-1], k)[0],
                  f"top {k['target']}" if k["target"] else None])
    cat_rows = (cat_hdr_row + 1, len(d) - 1)
    out["Dashboard"] = d
    out["_layout"] = {"kpi": (3, *kpi_rows, 4), "q": (q_hdr_row, *q_rows, len(qs) + 2),
                      "cat": (cat_hdr_row, *cat_rows, 5), "charts_row": len(d) + 2}

    # ---- chart data (hidden tab), one block per chart, side by side
    chart: list[list] = []
    blocks = {}

    def add_block(name, header, data_rows):
        col = max((len(rw) for rw in chart), default=0) + (1 if chart else 0)
        blocks[name] = (col, len(header), len(data_rows))
        for i, row in enumerate([header, *data_rows]):
            while len(chart) <= i:
                chart.append([])
            chart[i] += [None] * (col - len(chart[i])) + row

    add_block("clicks", ["Week", *SITE_PRODUCTS[:3], "Homepage & general"],
              [[wk.isoformat(), *[n(W[wk][f"clicks|{p}"]) for p in SITE_PRODUCTS]] for wk in weeks])
    add_block("ai", ["Week", "Sessions from AI assistants"],
              [[wk.isoformat(), n(W[wk]["ai_sessions"]) if ga4_ok(wk, wk + _dt.timedelta(days=6)) else None]
               for wk in weeks])
    add_block("contacts", ["Week", *PRODUCTS, "Not assigned"],
              [[wk.isoformat(), *[n(W[wk][f"work|{p}"]) for p in [*PRODUCTS, "Not assigned"]]] for wk in weeks])
    add_block("signups", ["Week", "Organic search & AI", "Other sources"],
              [[wk.isoformat(), n(W[wk]["mt_signups_organic"]), n(W[wk]["mt_signups"] - W[wk]["mt_signups_organic"])]
               for wk in weeks])
    add_block("deals", ["Month", *PRODUCTS],
              [[ym + "-01", *[n(a[f"deals|{p}"]) for p in PRODUCTS]]
               for ym, a in M.items()])
    lead_rows = []
    for wk in lead_weeks:
        fw = r["forms"].get(wk, {})
        vals = [sum(c for f, c in fw.items() if fn(f)) for _, fn, _ in FORM_GROUPS]
        lead_rows.append([wk.isoformat(), *vals, sum(fw.values()) - sum(vals)])
    add_block("leads", ["Week", *[g for g, _, _ in FORM_GROUPS], "Other forms"], lead_rows)
    out["_chart"] = chart
    out["_blocks"] = blocks
    return out


ABOUT = [
    ["About this dashboard"],
    ["What it is", "Organic search read-out for the whole of 3dlook.ai: FitXpress, Mobile Tailor and Wrist "
                   "Measurement. Is organic search turning into contacts, sign-ups and deals, and where do our "
                   "keywords rank? Rebuilt every Tuesday morning by a script (marketing repo, "
                   "scripts/organic-dashboard.py). Manual edits to these tabs are overwritten."],
    ["Weeks", "Monday to Sunday. The newest week is the last one Google Search Console has as final data "
              "(about two days' lag)."],
    ["Google clicks", "Google Search Console, sc-domain:3dlook.ai, web search, all countries. Summed by page, so "
                      "anonymised queries are included."],
    ["Page groups and products", "FitXpress = /fitxpress/…, /for-…, the telehealth page and Content Hub articles on "
                                 "health, fitness, GLP-1, body composition, insurance, occupational health. Mobile "
                                 "Tailor = /mobile-tailor/…, YourFit and apparel/fashion articles. Wrist Measurement "
                                 "= any URL with “wrist”. Homepage & general = the homepage, general body-scanning "
                                 "articles, pricing, contact, about, careers, technology and the rest."],
    ["GA4", "Property 251675969. Organic = default channel group Organic Search. Traffic tagged by the Internal "
            "Traffic and Developer Traffic filters is excluded. Engaged session = 10+ seconds, 2+ pages or a key "
            "event. GA4 recorded almost nothing from 5 Feb to 25 Jun 2026 (the page tag was broken: 10–20 "
            "sessions a day instead of 500–700), so every GA4 figure for a period touching those dates is left "
            "empty or marked “GA4 gap”. Search Console and HubSpot are not affected."],
    ["AI assistants", "GA4 sessions whose source is ChatGPT/OpenAI, Perplexity, Claude, Gemini, Copilot, DeepSeek, "
                      "Grok, You.com, Meta AI or Mistral."],
    ["Website leads", "GA4 event generate_lead (a submitted HubSpot form, careers excluded), tracked since "
                      "7 Oct 2026; earlier weeks are empty, not zero. Forms without a name in the GTM lookup "
                      "(the Wrist landing form among them) fall under Other forms. Demo clicks = GA4 demo_click."],
    ["Inbound contacts", "HubSpot contacts created in the period with a first conversion (a form or a meeting "
                         "link). Not counted: Mobile Tailor app sign-ups and logins (they are the MT sign-ups row), "
                         "careers and job seekers, the newsletter, 3DLOOK's own domains, meetings booked from "
                         "outbound. Work email = not a consumer domain (Gmail, Yahoo, Outlook …). Organic = HubSpot "
                         "original source Organic Search or AI Referrals."],
    ["Product of a contact", "Work-email contacts only. The form decides when it is product-specific (FX…, MT…, "
                             "WM…). For the shared Contact us form, the popup, meetings and eBooks, the message "
                             "text, company and email domain decide (the same rules as the hand-raisers KR), then "
                             "the first page seen. Not assigned = no signal, spam or vendors."],
    ["MT self-serve sign-ups", "Mobile Tailor app accounts (self-serve and enterprise sign-up), test and internal "
                               "accounts excluded; the same definition as the “Mobile Tailor self-serve sign-ups” "
                               "sheet. Accounts the app created through its integration show HubSpot source "
                               "Offline, so “from organic search or AI” is a lower bound."],
    ["Contact sources", "Monthly tab, “Work-email contacts by source”: the HubSpot original source of the same "
                        "work-email inbound contacts, with AI assistants (ChatGPT, Perplexity …) apart from organic "
                        "search. Not set = HubSpot has no source (mostly meetings and imports)."],
    ["Contacts by page", "Work-email inbound contacts of the last 12 months by the first page HubSpot saw them on "
                         "(any source), top 30 pages. First form = the first form or meeting they converted on. "
                         "A page outside 3dlook.ai is shown with its host. Small numbers: read it as a list of "
                         "what brought people in, not as conversion rates."],
    ["Recent contacts", "Every work-email inbound contact of the last 90 days, newest first. Source detail = "
                        "HubSpot's drill-down (the AI assistant's site, the referring domain, the import type). FX "
                        "vertical is set by the shared FitXpress landing form. No names or emails here; HubSpot = a "
                        "link to the record (needs HubSpot access)."],
    ["Deals", "HubSpot deals created in the period. FitXpress = pipeline Health & Fitness; Mobile Tailor = Mobile "
              "Tailor, Mobile Tailor Enterprise and MT self-serve pipelines; Wrist Measurement = Wrist Measurement "
              "pipeline. Source = the contact's original traffic source, copied onto the deal. Won = closed won "
              "as of today."],
    ["Keywords", "Main figure: Google average position from Search Console for that exact query and country, "
                 "weighted by impressions. Shown over 4 weeks because single weeks with a handful of impressions "
                 "are noisy; empty = no impressions (we are not on the pages people saw). Change: +3.0 = moved up "
                 "three places. The weekly columns on the Rankings tab are the same figure per week. Ahrefs "
                 "position = Ahrefs organic keywords for 3dlook.ai on the Sunday of the week, top 100, “—” = not "
                 "in Ahrefs' top 100; Ahrefs tracks only some of our keywords, so Google is the main source. "
                 "Volume and KD = Ahrefs, monthly, US or UK. Keyword list: rank-keywords.csv in the marketing repo."],
    ["Targets", "From the FitXpress SEO plan (2026-09-25), section 6. Mobile Tailor and Wrist have no targets yet."],
]


# ------------------------------------------------------------------ sheet writing

def rgb(hexstr: str) -> dict:
    h = hexstr.lstrip("#")
    return {"red": int(h[0:2], 16) / 255, "green": int(h[2:4], 16) / 255, "blue": int(h[4:6], 16) / 255}


def sheet_meta(sid: str) -> dict:
    return sheets("GET", f"/{sid}?fields=sheets(properties(sheetId,title),charts(chartId,spec(title)),"
                         f"conditionalFormats)")


def ensure_sheet(state: dict) -> tuple[str, dict]:
    sid = state.get("spreadsheet_id")
    if not sid:
        body = {"properties": {"title": TITLE, "locale": "en_US", "timeZone": "Europe/Kyiv"},
                "sheets": [{"properties": {"title": t, "index": i}} for i, t in enumerate(TABS)]}
        sid = sheets("POST", "", body)["spreadsheetId"]
        state["spreadsheet_id"] = sid
        save_state(state)
    meta = sheet_meta(sid)
    have = {s["properties"]["title"] for s in meta.get("sheets", [])}
    missing = [t for t in TABS if t not in have]
    if missing:
        sheets("POST", f"/{sid}:batchUpdate", {"requests": [{"addSheet": {"properties": {"title": t}}} for t in missing]})
        meta = sheet_meta(sid)
    return sid, meta


def write_sheet(sid: str, meta: dict, v: dict) -> None:
    tabs = {s["properties"]["title"]: s["properties"]["sheetId"] for s in meta.get("sheets", [])}
    # a new tab is 1000 x 26; Weekly is wider and Rank history longer, so size every grid first
    size = {}
    for t in TABS:
        values = ABOUT if t == "About" else v[t]
        rows = len(values) + 20
        if t == "Dashboard":
            rows = v["_layout"]["charts_row"] + 3 * 19 + 10
        size[t] = (max(rows, 60), max(max((len(r) for r in values), default=1) + 2, 10))
    sheets("POST", f"/{sid}:batchUpdate", {"requests": [
        {"updateSheetProperties": {"properties": {"sheetId": tabs[t], "gridProperties": {
            "rowCount": size[t][0], "columnCount": size[t][1]}},
            "fields": "gridProperties(rowCount,columnCount)"}} for t in TABS]})
    sheets("POST", f"/{sid}/values:batchClear", {"ranges": [f"'{t}'" for t in TABS]})
    chunk = 2000
    for t in TABS:
        values = ABOUT if t == "About" else v[t]
        for i in range(0, max(len(values), 1), chunk):
            sheets("POST", f"/{sid}/values:batchUpdate", {"valueInputOption": "USER_ENTERED", "data": [
                {"range": f"'{t}'!A{i + 1}", "values": values[i:i + chunk]}]})

    reqs: list[dict] = []
    # conditional formats are re-created every run: drop the old ones first
    for s in meta.get("sheets", []):
        for _ in s.get("conditionalFormats", []) or []:
            reqs.append({"deleteConditionalFormatRule": {"sheetId": s["properties"]["sheetId"], "index": 0}})

    def rng(sheet, r0, r1, c0, c1):
        return {"sheetId": sheet, "startRowIndex": r0, "endRowIndex": r1, "startColumnIndex": c0, "endColumnIndex": c1}

    def fmt(sheet, r0, r1, c0, c1, f, fields):
        reqs.append({"repeatCell": {"range": rng(sheet, r0, r1, c0, c1), "cell": {"userEnteredFormat": f},
                                    "fields": fields}})

    def width(sheet, c0, c1, px):
        reqs.append({"updateDimensionProperties": {"range": {"sheetId": sheet, "dimension": "COLUMNS",
                                                             "startIndex": c0, "endIndex": c1},
                                                   "properties": {"pixelSize": px}, "fields": "pixelSize"}})

    def cond(ranges, ctype, value, color):
        reqs.append({"addConditionalFormatRule": {"index": 0, "rule": {"ranges": ranges, "booleanRule": {
            "condition": {"type": ctype, "values": [{"userEnteredValue": value}]},
            "format": {"textFormat": {"foregroundColor": rgb(color), "bold": True}}}}}})

    font = {"fontFamily": "Arial"}
    hdr_fmt = {"textFormat": {**font, "bold": True, "fontSize": 9, "foregroundColor": rgb("#FFFFFF")},
               "backgroundColor": rgb(NAVY), "wrapStrategy": "WRAP", "verticalAlignment": "MIDDLE"}
    hdr_fields = "userEnteredFormat(textFormat,backgroundColor,wrapStrategy,verticalAlignment)"

    # ---- Dashboard
    D = tabs["Dashboard"]
    lay = v["_layout"]
    reqs.append({"updateCells": {"range": rng(D, 0, size["Dashboard"][0], 0, size["Dashboard"][1]), "fields": "userEnteredFormat"}})
    reqs.append({"updateSheetProperties": {"properties": {"sheetId": D, "gridProperties": {"hideGridlines": True}},
                                           "fields": "gridProperties.hideGridlines"}})
    width(D, 0, 1, 430)
    width(D, 1, 8, 120)
    fmt(D, 0, 1, 0, 1, {"textFormat": {**font, "bold": True, "fontSize": 18, "foregroundColor": rgb(NAVY)}},
        "userEnteredFormat.textFormat")
    fmt(D, 1, 2, 0, 1, {"textFormat": {**font, "fontSize": 9, "foregroundColor": rgb(MUTED)},
                        "wrapStrategy": "OVERFLOW_CELL"}, "userEnteredFormat(textFormat,wrapStrategy)")
    for key in ("kpi", "q", "cat"):
        h, r0, r1, ncol = lay[key]
        fmt(D, h, h + 1, 0, ncol, {**hdr_fmt, "textFormat": {**hdr_fmt["textFormat"], "fontSize": 10},
                                   "horizontalAlignment": "RIGHT"}, hdr_fields.replace(")", ",horizontalAlignment)"))
        fmt(D, h, h + 1, 0, 1, {"horizontalAlignment": "LEFT"}, "userEnteredFormat.horizontalAlignment")
        fmt(D, r0, r1 + 1, 0, ncol,
            {"textFormat": {**font, "fontSize": 10, "foregroundColor": rgb(INK)}, "horizontalAlignment": "RIGHT",
             "borders": {"bottom": {"style": "SOLID", "colorStyle": {"rgbColor": rgb(LINE)}}},
             "numberFormat": {"type": "NUMBER", "pattern": "#,##0"}},
            "userEnteredFormat(textFormat,horizontalAlignment,borders,numberFormat)")
        fmt(D, r0, r1 + 1, 0, 1, {"horizontalAlignment": "LEFT"}, "userEnteredFormat.horizontalAlignment")
    # sub-rows (indented with spaces) in muted ink
    for key in ("kpi", "q"):
        _, r0, r1, _ = lay[key]
        for i in range(r0, r1 + 1):
            if str(v["Dashboard"][i][0]).startswith("   "):
                fmt(D, i, i + 1, 0, 1, {"textFormat": {**font, "fontSize": 10, "foregroundColor": rgb(MUTED)}},
                    "userEnteredFormat.textFormat")
    _, k0, k1, _ = lay["kpi"]
    fmt(D, k0, k1 + 1, 3, 4, {"numberFormat": {"type": "PERCENT", "pattern": "▲ 0%;▼ 0%;0%"}},
        "userEnteredFormat.numberFormat")
    cond([rng(D, k0, k1 + 1, 3, 4)], "NUMBER_GREATER", "0", "#1A7F37")
    cond([rng(D, k0, k1 + 1, 3, 4)], "NUMBER_LESS", "0", "#C62828")
    _, c0, c1, _ = lay["cat"]
    fmt(D, c0, c1 + 1, 1, 3, {"numberFormat": {"type": "NUMBER", "pattern": "0.0"}}, "userEnteredFormat.numberFormat")
    fmt(D, c0, c1 + 1, 3, 4, {"numberFormat": {"type": "NUMBER", "pattern": "0"}}, "userEnteredFormat.numberFormat")

    # ---- data tabs
    nweekly = len(v["Weekly"][0])
    widths = {"Weekly": (100, nweekly, 105), "Monthly": (120, len(v["Monthly"][0]), 105),
              "Leads by form": (100, len(v["Leads by form"][0]), 115),
              "Contacts by page": None, "Recent contacts": None,
              "Rank history": None, "Rankings": None, "Top pages": None}
    for t, spec in widths.items():
        sh = tabs[t]
        reqs.append({"updateSheetProperties": {"properties": {"sheetId": sh, "gridProperties": {"frozenRowCount": 1}},
                                               "fields": "gridProperties.frozenRowCount"}})
        reqs.append({"updateDimensionProperties": {"range": {"sheetId": sh, "dimension": "ROWS", "startIndex": 0,
                                                             "endIndex": 1}, "properties": {"pixelSize": 54},
                                                   "fields": "pixelSize"}})
        fmt(sh, 0, 1, 0, max(len(v[t][0]), 1), hdr_fmt, hdr_fields)
        if spec:
            first, ncol, px = spec
            width(sh, 0, 1, first)
            width(sh, 1, ncol, px)
            reqs.append({"updateSheetProperties": {"properties": {"sheetId": sh,
                                                                  "gridProperties": {"frozenColumnCount": 1}},
                                                   "fields": "gridProperties.frozenColumnCount"}})
    for t in ("Weekly", "Leads by form"):
        fmt(tabs[t], 1, size[t][0], 0, 1, {"numberFormat": {"type": "DATE", "pattern": "d mmm yyyy"}},
            "userEnteredFormat.numberFormat")
    fmt(tabs["Weekly"], 1, size["Weekly"][0], 1, nweekly, {"numberFormat": {"type": "NUMBER", "pattern": "#,##0"}},
        "userEnteredFormat.numberFormat")
    fmt(tabs["Monthly"], 1, size["Monthly"][0], 1, len(v["Monthly"][0]), {"numberFormat": {"type": "NUMBER", "pattern": "#,##0"}},
        "userEnteredFormat.numberFormat")
    fmt(tabs["Monthly"], 1, size["Monthly"][0], 0, 1, {"numberFormat": {"type": "DATE", "pattern": "mmm yyyy"}},
        "userEnteredFormat.numberFormat")
    RH = tabs["Rank history"]
    for i, px in enumerate([110, 50, 260, 60, 90, 300, 110, 110, 100]):
        width(RH, i, i + 1, px)
    fmt(RH, 1, size["Rank history"][0], 0, 1, {"numberFormat": {"type": "DATE", "pattern": "d mmm yyyy"}}, "userEnteredFormat.numberFormat")
    TP = tabs["Top pages"]
    for i, px in enumerate([440, 180, 130, 100, 110, 100, 110, 120, 110]):
        width(TP, i, i + 1, px)
    fmt(TP, 1, size["Top pages"][0], 3, 9, {"numberFormat": {"type": "NUMBER", "pattern": "#,##0.#"}}, "userEnteredFormat.numberFormat")
    CP = tabs["Contacts by page"]
    for i, px in enumerate([420, 130, 130, 100, 100, 100, 90, 420, 100]):
        width(CP, i, i + 1, px)
    fmt(CP, 1, size["Contacts by page"][0], 8, 9, {"numberFormat": {"type": "DATE", "pattern": "d mmm yyyy"}},
        "userEnteredFormat.numberFormat")
    RC = tabs["Recent contacts"]
    for i, px in enumerate([100, 130, 120, 180, 420, 260, 150, 80]):
        width(RC, i, i + 1, px)
    fmt(RC, 1, size["Recent contacts"][0], 0, 1, {"numberFormat": {"type": "DATE", "pattern": "d mmm yyyy"}},
        "userEnteredFormat.numberFormat")
    AB = tabs["About"]
    width(AB, 0, 1, 190)
    width(AB, 1, 2, 900)
    fmt(AB, 0, 1, 0, 1, {"textFormat": {**font, "bold": True, "fontSize": 14, "foregroundColor": rgb(NAVY)}},
        "userEnteredFormat.textFormat")
    fmt(AB, 1, len(ABOUT), 0, 2, {"wrapStrategy": "WRAP", "verticalAlignment": "TOP",
                                  "textFormat": {**font, "fontSize": 10}},
        "userEnteredFormat(wrapStrategy,verticalAlignment,textFormat)")
    fmt(AB, 1, len(ABOUT), 0, 1, {"textFormat": {**font, "bold": True, "fontSize": 10}}, "userEnteredFormat.textFormat")
    CH = tabs["_chart"]
    fmt(CH, 1, size["_chart"][0], 0, size["_chart"][1], {"numberFormat": {"type": "NUMBER", "pattern": "#,##0"}},
        "userEnteredFormat.numberFormat")
    for name, (c0, _w, _n) in v["_blocks"].items():
        fmt(CH, 1, size["_chart"][0], c0, c0 + 1,
            {"numberFormat": {"type": "DATE", "pattern": "mmm yy" if name == "deals" else "d mmm yy"}},
            "userEnteredFormat.numberFormat")

    # ---- Rankings: heat map in one blue hue, darker = better
    R = tabs["Rankings"]
    nrows = len(v["Rankings"])
    heat0 = 13
    for i, px in enumerate([50, 250, 60, 90, 50, 60, 110, 110, 80, 110, 100, 100, 300]):
        width(R, i, i + 1, px)
    width(R, heat0, heat0 + RANK_WEEKS, 70)
    reqs.append({"updateSheetProperties": {"properties": {"sheetId": R, "gridProperties": {"frozenColumnCount": 3}},
                                           "fields": "gridProperties.frozenColumnCount"}})
    reqs.append({"addConditionalFormatRule": {"index": 0, "rule": {
        "ranges": [rng(R, 1, nrows, 6, 8), rng(R, 1, nrows, 11, 12), rng(R, 1, nrows, heat0, heat0 + RANK_WEEKS)],
        "gradientRule": {"minpoint": {"colorStyle": {"rgbColor": rgb("#8A9CFF")}, "type": "NUMBER", "value": "1"},
                         "midpoint": {"colorStyle": {"rgbColor": rgb("#D8DEFF")}, "type": "NUMBER", "value": "10"},
                         "maxpoint": {"colorStyle": {"rgbColor": rgb("#FFFFFF")}, "type": "NUMBER", "value": "50"}}}}})
    fmt(R, 1, nrows, 2, heat0 + RANK_WEEKS, {"horizontalAlignment": "CENTER"}, "userEnteredFormat.horizontalAlignment")
    fmt(R, 1, nrows, 12, 13, {"horizontalAlignment": "LEFT"}, "userEnteredFormat.horizontalAlignment")
    fmt(R, 1, nrows, 6, 8, {"numberFormat": {"type": "NUMBER", "pattern": "0.0"}}, "userEnteredFormat.numberFormat")
    fmt(R, 1, nrows, heat0, heat0 + RANK_WEEKS, {"numberFormat": {"type": "NUMBER", "pattern": "0.0"}},
        "userEnteredFormat.numberFormat")
    fmt(R, 0, 1, heat0, heat0 + RANK_WEEKS, {**hdr_fmt, "numberFormat": {"type": "DATE", "pattern": "d mmm"}},
        hdr_fields.replace(")", ",numberFormat)"))
    fmt(R, 1, nrows, 8, 9, {"numberFormat": {"type": "NUMBER", "pattern": "+0.0;-0.0;0"}}, "userEnteredFormat.numberFormat")
    cond([rng(R, 1, nrows, 8, 9)], "NUMBER_GREATER", "0", "#1A7F37")
    cond([rng(R, 1, nrows, 8, 9)], "NUMBER_LESS", "0", "#C62828")

    reqs.append({"updateSheetProperties": {"properties": {"sheetId": tabs["_chart"], "hidden": True},
                                           "fields": "hidden"}})
    for i, t in enumerate(TABS):
        reqs.append({"updateSheetProperties": {"properties": {"sheetId": tabs[t], "index": i}, "fields": "index"}})
    sheets("POST", f"/{sid}:batchUpdate", {"requests": reqs})
    write_charts(sid, meta, tabs, v)


CHARTS = [  # (title, data block, colors in series order, grid row, grid column)
    ("Organic Google clicks by product, weekly", "clicks", [BLUE, ORANGE, AQUA, GRAY], 0, 0),
    ("Sessions from AI assistants, weekly (GA4 recorded almost nothing 5 Feb – 25 Jun 2026)", "ai", [BLUE], 0, 1),
    ("Inbound contacts with a work email, by product, weekly", "contacts", [BLUE, ORANGE, AQUA, GRAY], 1, 0),
    ("Mobile Tailor self-serve sign-ups, weekly", "signups", [ORANGE, GRAY], 1, 1),
    ("New deals by product, monthly", "deals", [BLUE, ORANGE, AQUA], 2, 0),
    ("Website leads by form, weekly (tracked since 7 Oct 2026)", "leads", [BLUE, ORANGE, YELLOW, MAGENTA, GRAY], 2, 1),
]


def write_charts(sid: str, meta: dict, tabs: dict, v: dict) -> None:
    C, D = tabs["_chart"], tabs["Dashboard"]
    existing = {}
    for s in meta.get("sheets", []):
        for ch in s.get("charts", []) or []:
            existing[(ch.get("spec") or {}).get("title", "")] = ch["chartId"]
    known = {t for t, *_ in CHARTS}
    reqs = [{"deleteEmbeddedObject": {"objectId": cid}} for t, cid in existing.items() if t not in known]
    top = v["_layout"]["charts_row"]
    for title, block, colors, grow, gcol in CHARTS:
        c0, width, nrows = v["_blocks"][block]

        def src(c):
            return {"sourceRange": {"sources": [{"sheetId": C, "startRowIndex": 0, "endRowIndex": nrows + 1,
                                                 "startColumnIndex": c, "endColumnIndex": c + 1}]}}
        series = [{"series": src(c0 + 1 + i), "targetAxis": "LEFT_AXIS",
                   "colorStyle": {"rgbColor": rgb(colors[i])}} for i in range(width - 1)]
        multi = width > 2
        spec = {"title": title, "fontName": "Arial",
                "titleTextFormat": {"fontFamily": "Arial", "fontSize": 12, "bold": True,
                                    "foregroundColorStyle": {"rgbColor": rgb(INK)}},
                "basicChart": {"chartType": "COLUMN", "legendPosition": "BOTTOM_LEGEND" if multi else "NO_LEGEND",
                               "stackedType": "STACKED" if multi else "NOT_STACKED", "headerCount": 1,
                               "axis": [{"position": "BOTTOM_AXIS"}, {"position": "LEFT_AXIS"}],
                               "domains": [{"domain": src(c0)}], "series": series}}
        if title in existing:
            reqs.append({"updateChartSpec": {"chartId": existing[title], "spec": spec}})
            reqs.append({"updateEmbeddedObjectPosition": {"objectId": existing[title], "fields": "*", "newPosition": {
                "overlayPosition": {"anchorCell": {"sheetId": D, "rowIndex": top + grow * 19, "columnIndex": 0},
                                    "offsetXPixels": 10 + gcol * 700, "widthPixels": 680, "heightPixels": 350}}}})
        else:
            reqs.append({"addChart": {"chart": {"spec": spec, "position": {"overlayPosition": {
                "anchorCell": {"sheetId": D, "rowIndex": top + grow * 19, "columnIndex": 0},
                "offsetXPixels": 10 + gcol * 700, "widthPixels": 680, "heightPixels": 350}}}}})
    sheets("POST", f"/{sid}:batchUpdate", {"requests": reqs})


# ------------------------------------------------------------------ Telegram

def report_text(r: dict, v: dict, sid: str) -> str:
    weeks, W = r["weeks"], r["A"].W
    wk = weeks[-1]
    prev = weeks[-5:-1]

    def val(key):
        cur = W[wk][key]
        avg = sum(W[p][key] for p in prev) / len(prev)
        ch = f" ({'+' if cur >= avg else ''}{(cur - avg) / avg:.0%} до сер. 4 тижнів)" if avg else ""
        return f"{n(cur)}{ch}"

    lines = [f"📊 Органіка 3dlook.ai · тиждень {fmt_day(wk)} – {fmt_day(wk + _dt.timedelta(days=6))}",
             f"• Кліки з Google, весь сайт: {val('clicks')}",
             f"  FitXpress {n(W[wk]['clicks|FitXpress'])} · MT {n(W[wk]['clicks|Mobile Tailor'])} · "
             f"Wrist {n(W[wk]['clicks|Wrist Measurement'])} · головна і загальні {n(W[wk]['clicks|General'])}",
             f"• Сесії з AI-асистентів: {val('ai_sessions')}",
             f"• Заявки на сайті (GA4): {n(W[wk]['leads'])} · demo-кліки: {n(W[wk]['demo_clicks'])}",
             f"• Контакти з робочою поштою: {n(W[wk]['work'])} (FX {n(W[wk]['work|FitXpress'])} · "
             f"MT {n(W[wk]['work|Mobile Tailor'])} · WM {n(W[wk]['work|Wrist Measurement'])} · "
             f"без продукту {n(W[wk]['work|Not assigned'])}), з органіки/AI: {n(W[wk]['work_organic'])}",
             f"• MT self-serve sign-ups: {n(W[wk]['mt_signups'])}, з органіки/AI: {n(W[wk]['mt_signups_organic'])}",
             f"• Нові угоди: FX {n(W[wk]['deals|FitXpress'])} · MT {n(W[wk]['deals|Mobile Tailor'])} · "
             f"WM {n(W[wk]['deals|Wrist Measurement'])}"]
    moves = v["_alerts"]
    lines.append("")
    if moves:
        lines.append("Позиції за тиждень:")
        lines += moves[:15]
        if len(moves) > 15:
            lines.append(f"…ще {len(moves) - 15}, див. вкладку Rankings")
    else:
        lines.append("Позиції: за тиждень ніщо не зрушило на 3+ місця (Google при 5+ показах, Ahrefs).")
    lines += ["", f"https://docs.google.com/spreadsheets/d/{sid}/edit"]
    return "\n".join(lines)


def send(msg: str) -> bool:
    return load_module("outbound_pipeline", PIPE).telegram_send(msg)


# ------------------------------------------------------------------ commands

def run(args) -> int:
    state = load_state()
    kws = load_keywords()
    end = last_final_sunday()
    weeks_n = ((end - HISTORY_START).days + 1) // 7
    sundays = [HISTORY_START + _dt.timedelta(days=7 * i + 6) for i in range(weeks_n)]
    print(f"window {HISTORY_START} … {end} ({weeks_n} weeks)", file=sys.stderr)
    gsc_pages = collect_gsc_pages(HISTORY_START, end)
    gsc_kw = collect_gsc_keywords(HISTORY_START, end, kws)
    ga = collect_ga4(HISTORY_START, end)
    hs = collect_hubspot(HISTORY_START, end)
    ahr = collect_ahrefs(kws, sundays, state, use_api=not args.no_ahrefs)
    save_state(state)                            # keep the paid-for Ahrefs snapshots even if the Sheet fails
    r = build(end, gsc_pages, gsc_kw, ga, hs, ahr, kws, state)
    v = tab_values(r)
    print(f"gsc page rows {len(gsc_pages)}, keyword rows {len(gsc_kw)}, ga4 landing rows {len(ga['landing'])}, "
          f"hubspot contacts {hs['raw_contacts']} → inbound {len(hs['contacts'])} (dropped {hs['dropped']}), "
          f"deals {len(hs['deals'])}, MT sign-ups {len(hs['signups'])}, ahrefs snapshots {len(ahr)}", file=sys.stderr)
    if args.dry_run:
        print(report_text(r, v, state.get("spreadsheet_id", "<not created>")))
        return 0
    sid, meta = ensure_sheet(state)
    write_sheet(sid, meta, v)
    print(f"https://docs.google.com/spreadsheets/d/{sid}/edit")
    if args.notify:
        wk = r["weeks"][-1].isoformat()
        if state.get("last_reported_week") == wk and not args.force_notify:
            print(f"week {wk} already reported, not sending", file=sys.stderr)
        elif send(report_text(r, v, sid)):
            state["last_reported_week"] = wk
            save_state(state)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    u = sub.add_parser("update", help="rebuild the Sheet")
    u.add_argument("--notify", action="store_true", help="Telegram summary for the newest week (once per week)")
    u.add_argument("--force-notify", action="store_true", help="send even if this week was already reported")
    u.add_argument("--dry-run", action="store_true", help="collect and print the report, write nothing")
    u.add_argument("--no-ahrefs", action="store_true", help="use only cached Ahrefs snapshots")
    rp = sub.add_parser("report", help="print the Telegram text, write and send nothing")
    rp.add_argument("--no-ahrefs", action="store_true")
    args = ap.parse_args()
    if args.cmd == "report":
        args.dry_run, args.notify, args.force_notify = True, False, False
    try:
        return run(args)
    except Broken as e:
        print(f"organic-dashboard: {e}", file=sys.stderr)
        if getattr(args, "notify", False):
            send(f"⚠️ organic-dashboard не оновився: {str(e)[:500]}")
        return 3


if __name__ == "__main__":
    sys.exit(main())
