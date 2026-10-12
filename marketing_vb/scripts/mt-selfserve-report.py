#!/usr/bin/env python3
"""mt-selfserve-report.py — monthly Mobile Tailor self-serve sign-up report (HubSpot -> Google Sheet).

WHY THIS EXISTS
---------------
Whitney asked (2026-10-12) how many customers sign up for Mobile Tailor self-serve every month and
what kind of business they are. Nobody had a dashboard for it. This script pulls the MT app users
from HubSpot and fills the Google Sheet "Mobile Tailor self-serve sign-ups" once a month.

WHO COUNTS
  Every HubSpot contact that has a Mobile Tailor app account: `product_signed_up_in` = "smb"
  (self-serve) or "smb_enterprise" (enterprise sign-up). The app writes this field together with
  the admin link `django_customer_s_link` (.../customcustomer/<account id>/change/).
  Dropped: 3DLOOK's own domains, mailinator / example / mail-tester, and test-looking emails.
  `lead_source` = "MT Self-serv" is NOT the filter: ~12% of app users were already in HubSpot from
  a contact form, kept that lead source and would be missed (with ~100 active subscriptions).

SIGN-UP DATE
  HubSpot has no sign-up date field. Two sources:
  * the contact's create date, when the contact was created by the sign-up itself;
  * otherwise an estimate from the app account id. Account ids grow with time from ~6,250
    (mid-2023); the id -> date curve is built from contacts that the app integration or the
    sign-up form created, so it is exact to a few days.
  Rule: create date if it is within 14 days of the id estimate, else the estimate (the contact
  existed before the sign-up). Accounts with id < 6,250 signed up before mid-2023: when HubSpot
  created their contact later (bulk syncs in 2023), the sign-up date is unknown and the month is
  "Before 2023-07". The monthly series starts at 2023-07: from 2021-07 to 2023-05 the app barely
  synced to HubSpot, so those months are not comparable.

STARTED WITH (Data column; Monthly / Summary columns)
  "$1 trial" = initial or current plan smb_free7_dollar (every one has the $1 payment recorded);
  "Paid plan (no trial)" = a paid plan as the initial or current plan without the $1 trial;
  "Free plan / other" = some other subscription record (free plan, free trial); "Nothing yet" = registered
  only, no subscription record.

PAYING TODAY
  subscription_status = active, on a paid plan (not smb_free*, which covers the $1 / 7-day trial
  and free plans), and the current period has not ended more than 7 days before the data date.
  A few "active" records with periods that ended in 2023-2024 are stale and do not count.

SHEET
  Data tab = one row per account; every other tab is COUNTIFS formulas over Data, so a person can
  add tabs or charts. `refresh` (monthly cron) rewrites Data, the month rows of Monthly / By type,
  the By country block, the "Data as of" cell and the chart range. It does not touch Summary text
  or anything outside those ranges. `build` re-creates every tab from scratch (layout changes only).

READ-ONLY BY RULE
  HubSpot is read-only for us: the only HubSpot call is the MCP tool search_crm_objects through
  `oo connector proxy hubspot`. The only writes are to the report sheet.

COMMANDS
  refresh [--notify] [--dry-run]   monthly update (cron: 1st of the month, 06:15 UTC)
  build   [--dry-run]              full re-layout of the sheet
  stats                            print the numbers without writing anything
"""

from __future__ import annotations

import argparse
import datetime as _dt
import importlib.util
import json
import os
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path
from zoneinfo import ZoneInfo

MCP_URL = "https://mcp.hubspot.com/"
SHEETS_URL = "https://sheets.googleapis.com/v4/spreadsheets"
OO = shutil.which("oo") or str(Path.home() / ".local" / "bin" / "oo")
SHEET = "1m4DNHM0LX7_dmwo0TgQq7ujTsV9AcQUl4Zg1-qSdSbY"   # "Mobile Tailor self-serve sign-ups"
PORTAL = 6014382
TZ = ZoneInfo("Europe/Kyiv")
START = "2023-07"
MIN_CURVE_ID = 6250
PIPE = Path(__file__).with_name("outbound-pipeline.py")

PROPS = ["email", "hs_email_domain", "company", "createdate", "lifecyclestage", "your_business",
         "subscription_status", "subscription_plan_nickname", "initial_product_plan",
         "subscription_current_period_end", "first_payment_date", "last_payment_date",
         "product_signed_up_in", "django_customer_s_link", "ip_country", "hs_analytics_source",
         "hs_object_source_label", "hs_object_source_detail_1", "num_associated_deals"]

TYPE_MAP = {  # your_business, lower-cased without spaces/dashes -> (Type, Segment)
    "madetomeasure": ("Made-to-Measure", "Custom clothing"),
    "individualtailor": ("Individual Tailor", "Custom clothing"),
    "personaltailor": ("Individual Tailor", "Custom clothing"),
    "bespokebrand": ("Bespoke Brand", "Custom clothing"),
    "apparelmonobrand": ("Apparel Monobrand", "Apparel brands & retail"),
    "apparelmultibrand": ("Apparel Multibrand", "Apparel brands & retail"),
    "marketplace": ("Marketplace", "Apparel brands & retail"),
    "retailplatform": ("Retail platform", "Apparel brands & retail"),
    "rental": ("Rental", "Apparel brands & retail"),
    "apparelmanufacturer": ("Apparel Manufacturer", "Manufacturing & uniforms"),
    "uniformcompany": ("Uniform company", "Manufacturing & uniforms"),
    "uniformmanufacturer": ("Uniform company", "Manufacturing & uniforms"),
    "uniformmanufacturer/retailer": ("Uniform company", "Manufacturing & uniforms"),
    "uniforms": ("Uniform company", "Manufacturing & uniforms"),
    "beddingandmattresses": ("Bedding & mattresses", "Manufacturing & uniforms"),
    "bedding": ("Bedding & mattresses", "Manufacturing & uniforms"),
    "fashion/technicaldesigner": ("Fashion / Technical Designer", "Designers & studios"),
    "designstudio": ("Design Studio", "Designers & studios"),
    "university/student": ("University / Student", "Students & education"),
    "softwaredeveloper/integrator": ("Software developer / integrator", "Software & tech"),
    "softwaredevelopment/integrator": ("Software developer / integrator", "Software & tech"),
    "softwaredevelopment": ("Software developer / integrator", "Software & tech"),
    "developer": ("Software developer / integrator", "Software & tech"),
    "2d/3ddesignsoftware": ("2D/3D design software", "Software & tech"),
    "2dand3ddesignsoftware": ("2D/3D design software", "Software & tech"),
    "health&fitness": ("Health & Fitness", "Health & Fitness"),
    "healthandfitness": ("Health & Fitness", "Health & Fitness"),
    "marketingagency": ("Marketing agency", "Other"),
    "clientelling/customersupport": ("Clientelling / Customer support", "Other"),
    "insurance": ("Insurance", "Other"),
    "other": ("Other", "Other"),
    "": ("Not specified", "Not specified"),
}
SEGMENTS = ["Custom clothing", "Apparel brands & retail", "Manufacturing & uniforms", "Designers & studios",
            "Students & education", "Software & tech", "Health & Fitness", "Other", "Not specified"]
SOURCES = {"ORGANIC_SEARCH": "Organic search", "DIRECT_TRAFFIC": "Direct", "OFFLINE": "Offline (app integration)",
           "REFERRALS": "Referrals", "AI_REFERRALS": "AI assistants", "SOCIAL_MEDIA": "Social",
           "EMAIL_MARKETING": "Email", "OTHER_CAMPAIGNS": "Other campaigns", "PAID_SEARCH": "Paid search",
           "PAID_SOCIAL": "Paid social"}
LIFECYCLE = {"subscriber": "Subscriber", "44205152": "Contact", "lead": "Lead", "marketingqualifiedlead": "MQL",
             "salesqualifiedlead": "SQL", "opportunity": "Opportunity", "customer": "Customer",
             "evangelist": "Evangelist", "other": "Other", "54977858": "Disqualified", "56837266": "Churned"}
COUNTRIES = {"Iran (Islamic Republic Of)": "Iran", "Taiwan Province Of China": "Taiwan",
             "Russian Federation": "Russia", "Viet Nam": "Vietnam", "Korea, Republic Of": "South Korea",
             "Slovakia (Slovak Republic)": "Slovakia", "Syrian Arab Republic": "Syria",
             "Moldova, Republic Of": "Moldova", "Tanzania, United Republic Of": "Tanzania"}
TIERS = ["Starter", "Basic", "Individual", "Growing", "Premium", "Business", "Enterprise"]
ACCOUNT = {"smb": "Self-serve", "smb_enterprise": "Enterprise"}
TEST_DOMAIN = re.compile(r"3dlook\.|mailinator\.com$|example\.com$|mail-tester\.com$", re.I)
TEST_LOCAL = re.compile(r"^(test|testing)(\d|[._+-]|$)|\+test", re.I)
REL_SOURCE = re.compile(r"signup-form|MT Trial Sign up form|complete-profile", re.I)

DATA_HEAD = ["Sign-up date", "Month", "Quarter", "Date source", "Account type", "Company", "Email domain",
             "Type of business (as entered)", "Type", "Segment", "Country", "Original source", "Starting plan",
             "Subscription status", "Current plan", "Plan tier", "Billing", "Started with", "Paying today", "First payment",
             "Last payment", "Lifecycle stage", "Deals", "HubSpot record"]
COL = {h: chr(65 + i) for i, h in enumerate(DATA_HEAD)}   # header -> Data column letter (A..X)
LAST = COL[DATA_HEAD[-1]]
STARTED = ["$1 trial", "Paid plan (no trial)", "Free plan / other", "Nothing yet"]
TABS = ["Summary", "Monthly", "By type", "By country", "Data"]


class Broken(RuntimeError):
    pass


# ------------------------------------------------------------------ transport

def oo(args: list[str], timeout: int = 300) -> dict:
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


def search(groups: list[dict]) -> list[dict]:
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
        total = int(page.get("total") or 0)
        if not batch or offset in (None, "") or len(rows) >= total:
            if len(rows) < total:
                raise Broken(f"search returned {len(rows)} of {total} rows")
            return rows


def pull_app_users() -> list[dict]:
    """Every contact with product_signed_up_in set, in create-date windows (search caps at 10k)."""
    out: dict[str, dict] = {}
    edges = ["1970-01-01", "2023-01-01", "2024-07-01", "2026-01-01", "2100-01-01"]
    for a, b in zip(edges, edges[1:]):
        f = [{"propertyName": "product_signed_up_in", "operator": "HAS_PROPERTY"},
             {"propertyName": "createdate", "operator": "GTE", "value": f"{a}T00:00:00Z"},
             {"propertyName": "createdate", "operator": "LT", "value": f"{b}T00:00:00Z"}]
        for r in search([{"filters": f}]):
            out[r["_id"]] = r
    return list(out.values())


def sheets_batch(requests: list[dict]) -> dict:
    return oo(["connector", "proxy", "googlesheets", "--method", "POST",
               "--endpoint", f"{SHEETS_URL}/{SHEET}:batchUpdate",
               "--headers", json.dumps({"Content-Type": "application/json"}),
               "--body", json.dumps({"requests": requests})])


def sheets_run(action: str, payload: dict) -> dict:
    # values go through a file: the Data tab is ~1.5 MB, too big for one argv string
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(payload, f, ensure_ascii=False)
        path = f.name
    try:
        return oo(["connector", "run", "googlesheets", "--action", action, "--data", "@" + path], timeout=600)
    finally:
        os.unlink(path)


def sheet_meta() -> dict:
    d = oo(["connector", "proxy", "googlesheets", "--method", "GET",
            "--endpoint", f"{SHEETS_URL}/{SHEET}?fields=sheets(properties,charts(chartId))"])
    d = d.get("data") or d
    return {s["properties"]["title"]: s for s in d["sheets"]}


# ------------------------------------------------------------------ model

def account_id(p: dict) -> int | None:
    m = re.search(r"/(\d+)/change", p.get("django_customer_s_link") or "")
    return int(m.group(1)) if m else None


def local_day(iso: str) -> _dt.date:
    return _dt.datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(TZ).date()


def created_by_signup(p: dict) -> bool:
    src = p.get("hs_object_source_label")
    return src == "INTEGRATION" or (src == "FORM" and bool(REL_SOURCE.search(p.get("hs_object_source_detail_1") or "")))


def id_curve(users: list[dict]) -> list[tuple[int, int]]:
    """(account id, date ordinal) points: rolling median of create dates of sign-up-created contacts,
    made monotonic. Used to date the sign-ups of contacts that existed before signing up."""
    pts = sorted((account_id(p), local_day(p["createdate"]).toordinal()) for p in users
                 if account_id(p) and account_id(p) >= MIN_CURVE_ID and created_by_signup(p))
    if len(pts) < 100:
        raise Broken(f"only {len(pts)} points for the id -> date curve")
    w, out, top = 20, [], 0
    for i, (aid, _) in enumerate(pts):
        med = int(statistics.median(d for _, d in pts[max(0, i - w): i + w + 1]))
        top = max(top, med)
        out.append((aid, top))
    return out


def estimate(curve: list[tuple[int, int]], aid: int) -> _dt.date:
    if aid <= curve[0][0]:
        return _dt.date.fromordinal(curve[0][1])
    if aid >= curve[-1][0]:
        return _dt.date.fromordinal(curve[-1][1])
    lo, hi = 0, len(curve) - 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if curve[mid][0] <= aid:
            lo = mid
        else:
            hi = mid
    (a0, d0), (a1, d1) = curve[lo], curve[hi]
    return _dt.date.fromordinal(round(d0 + (d1 - d0) * (aid - a0) / max(1, a1 - a0)))


def type_seg(raw: str | None) -> tuple[str, str]:
    return TYPE_MAP.get(re.sub(r"[\s\-]", "", (raw or "").strip().lower()), ("Other", "Other"))


def tier(nick: str) -> str:
    n = nick.lower()
    if not n:
        return ""
    if "free" in n:
        return "Free / trial"
    for t, keys in [("Enterprise", ["enterprise"]), ("Business", ["business", "bussines"]),
                    ("Premium", ["premium"]), ("Growing", ["growing"]), ("Individual", ["individual"]),
                    ("Basic", ["basic"]), ("Starter", ["startet", "starter"])]:
        if any(k in n for k in keys):
            return t
    return "Other"


def billing(nick: str) -> str:
    n = nick.lower()
    if not n or "free" in n:
        return ""
    return "Annual" if ("annual" in n or "yearly" in n) else "Monthly"


def is_test(p: dict) -> bool:
    email = (p.get("email") or "").lower()
    dom = (p.get("hs_email_domain") or email.split("@")[-1]).lower()
    return bool(TEST_DOMAIN.search(dom) or TEST_LOCAL.search(email.split("@")[0]))


def build_rows(users: list[dict], as_of: _dt.date) -> tuple[list[dict], dict]:
    users = [p for p in users if p.get("product_signed_up_in") in ACCOUNT]
    curve = id_curve(users)
    rows, stats = [], Counter()
    for p in users:
        if is_test(p):
            stats["excluded: internal or test"] += 1
            continue
        created = local_day(p["createdate"])
        aid = account_id(p)
        if aid is None:
            day, src = created, "Contact create date (no app account id)"
        elif aid < MIN_CURVE_ID:
            if created.strftime("%Y-%m") >= START:
                day, src = None, "Before Jul 2023 (contact synced later)"
            else:
                day, src = created, "Contact create date"
        else:
            est = estimate(curve, aid)
            if abs((created - est).days) <= 14:
                day, src = created, "Contact create date"
            else:
                day, src = est, "Estimated from app account id"
        stats[src] += 1
        typ, seg = type_seg(p.get("your_business"))
        status = p.get("subscription_status") or ""
        nick = p.get("subscription_plan_nickname") or ""
        t = tier(nick)
        end = p.get("subscription_current_period_end") or ""
        fresh = not end or _dt.date.fromisoformat(end[:10]) >= as_of - _dt.timedelta(days=7)
        paying = status == "active" and t not in ("", "Free / trial") and fresh
        start_plan = p.get("initial_product_plan") or ""
        if "free7_dollar" in start_plan or "free7_dollar" in nick:
            started = "$1 trial"
        elif tier(start_plan) not in ("", "Free / trial") or t not in ("", "Free / trial"):
            started = "Paid plan (no trial)"
        elif status or start_plan:
            started = "Free plan / other"
        else:
            started = "Nothing yet"
        if status == "active" and t not in ("", "Free / trial") and not fresh:
            stats["active but period ended (stale, not paying)"] += 1
        country = (p.get("ip_country") or "").strip().title()
        country = COUNTRIES.get(country, country.replace(" And ", " and ").replace(" Of ", " of ")) or "Unknown"
        month = day.strftime("%Y-%m") if day else "Before 2023-07"
        if day and month < START:
            month = "Before 2023-07"
        rows.append({
            "Sign-up date": (day - _dt.date(1899, 12, 30)).days if day else None,
            "Month": month,
            "Quarter": f"{day.year}-Q{(day.month - 1) // 3 + 1}" if day and month != "Before 2023-07" else "Before 2023-Q3",
            "Date source": src,
            "Account type": ACCOUNT[p["product_signed_up_in"]],
            "Company": (p.get("company") or "").strip() or None,
            "Email domain": p.get("hs_email_domain") or None,
            "Type of business (as entered)": (p.get("your_business") or "").strip() or None,
            "Type": typ, "Segment": seg, "Country": country,
            "Original source": SOURCES.get(p.get("hs_analytics_source"), p.get("hs_analytics_source") or "Unknown"),
            "Starting plan": p.get("initial_product_plan") or None,
            "Subscription status": status or None,
            "Current plan": nick or None,
            "Plan tier": t or None,
            "Billing": billing(nick) or None,
            "Started with": started,
            "Paying today": "Yes" if paying else "No",
            "First payment": (p.get("first_payment_date") or "")[:10] or None,
            "Last payment": (p.get("last_payment_date") or "")[:10] or None,
            "Lifecycle stage": LIFECYCLE.get(p.get("lifecyclestage"), p.get("lifecyclestage") or None),
            "Deals": int(p.get("num_associated_deals") or 0),
            "HubSpot record": f'=HYPERLINK("https://app.hubspot.com/contacts/{PORTAL}/record/0-1/{p["_id"]}","Open")',
            "_sort": (day or _dt.date(1900, 1, 1)).toordinal(), "_id": p["_id"]})
    rows.sort(key=lambda r: (-r["_sort"], r["_id"]))
    return rows, stats


def months_until(as_of: _dt.date) -> list[str]:
    y, m, out = int(START[:4]), int(START[5:]), []
    while (y, m) <= (as_of.year, as_of.month):
        out.append(f"{y}-{m:02d}")
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)
    return out


# ------------------------------------------------------------------ sheet layout

def col(i: int) -> str:
    s, i = "", i + 1
    while i:
        i, r = divmod(i - 1, 26)
        s = chr(65 + r) + s
    return s


def D(header: str) -> str:
    c = COL[header]
    return f"Data!${c}:${c}"


MONTHLY_HEAD = (["Month", "Registrations", "Self-serve", "Enterprise"] + SEGMENTS +
                ["$1 trial sign-ups", "Paid plan sign-ups (no trial)", "Paying today", "% paying today",
                 "Organic search", "Direct", "Offline (app integration)", "Other sources"])


def monthly_values(months: list[str]) -> list[list]:
    h = MONTHLY_HEAD
    c = {name: col(i) for i, name in enumerate(h)}
    out = [h]
    for i, mk in enumerate(months):
        r, M = i + 2, f"$A{i + 2}"
        row = [f"'{mk}", f"=COUNTIF({D('Month')},{M})",
               f'=COUNTIFS({D("Month")},{M},{D("Account type")},"Self-serve")',
               f'=COUNTIFS({D("Month")},{M},{D("Account type")},"Enterprise")']
        row += [f"=COUNTIFS({D('Month')},{M},{D('Segment')},{c[s]}$1)" for s in SEGMENTS]
        row += [f'=COUNTIFS({D("Month")},{M},{D("Started with")},"$1 trial")',
                f'=COUNTIFS({D("Month")},{M},{D("Started with")},"Paid plan (no trial)")',
                f'=COUNTIFS({D("Month")},{M},{D("Paying today")},"Yes")',
                f'=IF(B{r}>0,{c["Paying today"]}{r}/B{r},"")']
        row += [f"=COUNTIFS({D('Month')},{M},{D('Original source')},{c[s]}$1)"
                for s in ("Organic search", "Direct", "Offline (app integration)")]
        row.append(f'=B{r}-{c["Organic search"]}{r}-{c["Direct"]}{r}-{c["Offline (app integration)"]}{r}')
        out.append(row)
    return out


def bytype_values(months: list[str], types: list[str]) -> list[list]:
    out = [["Month"] + types + ["Total"]]
    for i, mk in enumerate(months):
        r = i + 2
        out.append([f"'{mk}"] + [f"=COUNTIFS({D('Month')},$A{r},{D('Type')},{col(1 + j)}$1)" for j in range(len(types))]
                   + [f"=SUM(B{r}:{col(len(types))}{r})"])
    return out


def bycountry_values(quarters: list[str], top: list[str]) -> list[list]:
    last = col(len(quarters))
    out = [["Country"] + quarters + ["Total"]]
    for i, c in enumerate(top):
        r = i + 2
        out.append([c] + [f"=COUNTIFS({D('Country')},$A{r},{D('Quarter')},{col(1 + j)}$1)" for j in range(len(quarters))]
                   + [f"=SUM(B{r}:{last}{r})"])
    ro, ru, rt = len(top) + 2, len(top) + 3, len(top) + 4
    out.append(["Other countries"] + [f"={col(1 + j)}{rt}-SUM({col(1 + j)}2:{col(1 + j)}{ro - 1})-{col(1 + j)}{ru}"
                                      for j in range(len(quarters))] + [f"=SUM(B{ro}:{last}{ro})"])
    out.append(["Unknown"] + [f"=COUNTIFS({D('Country')},$A{ru},{D('Quarter')},{col(1 + j)}$1)"
                              for j in range(len(quarters))] + [f"=SUM(B{ru}:{last}{ru})"])
    out.append(["Total"] + [f"=COUNTIF({D('Quarter')},{col(1 + j)}$1)" for j in range(len(quarters))]
               + [f"=SUM(B{rt}:{last}{rt})"])
    return out


SUMMARY_NOTES = [
    "Mobile Tailor self-serve sign-ups",
    "Source: HubSpot only. One row per Mobile Tailor app account (self-serve and enterprise sign-ups) on the Data tab; "
    "every other tab is formulas over Data. 3DLOOK staff and test accounts are excluded. Registration = an MT account "
    "was created. $1 trial sign-up = started the $1 trial (Initial product plan smb_free7_dollar). Paid plan sign-up = "
    "chose a paid plan without the $1 trial.",
    "Registration date: the HubSpot contact create date when the registration created the contact; for people who were already "
    "in HubSpot, an estimate from the app account number (accurate to a few days). Monthly figures start in Jul 2023.",
    "Type and segment: \"Type of business\" that the user picks at sign-up; the Type → Segment mapping is on the Data "
    "tab (columns H–J). Paying today: active subscription on a paid plan whose billing period has not ended "
    "(the $1 trial and free plans do not count). It is a snapshot by registration month, not the month payment started.",
]


def summary_values() -> tuple[list[dict], dict]:
    S = []

    def put(rng, vals):
        S.append({"range": f"Summary!{rng}", "values": vals})

    for i, t in enumerate(SUMMARY_NOTES):
        put(f"A{i + 1}", [[t]])
    put("A6", [["Data as of"]])
    put("A8:G8", [["", "Last full month", "Previous month", "Same month last year", "Last 12 months",
                   "Previous 12 months", "12m vs previous 12m"]])
    put("A9:F10", [["From", "=EOMONTH($B$6,-2)+1", "=EOMONTH($B$6,-3)+1", "=EOMONTH($B$6,-14)+1",
                    "=EOMONTH($B$6,-13)+1", "=EOMONTH($B$6,-25)+1"],
                   ["To", "=EOMONTH($B$6,-1)", "=EOMONTH($B$6,-2)", "=EOMONTH($B$6,-13)",
                    "=EOMONTH($B$6,-1)", "=EOMONTH($B$6,-13)"]])

    def per(c):
        return f'{D("Sign-up date")},">="&{c}$9,{D("Sign-up date")},"<="&{c}$10'

    metrics = [("Registrations (account created)", ""), ("   of which self-serve", f',{D("Account type")},"Self-serve"'),
               ("   of which enterprise sign-ups", f',{D("Account type")},"Enterprise"'),
               ("$1 trial sign-ups", f',{D("Started with")},"$1 trial"'),
               ("Paid plan sign-ups (no trial)", f',{D("Started with")},"Paid plan (no trial)"'),
               ("Registered, started nothing yet", f',{D("Started with")},"Nothing yet"'),
               ("Paying today", f',{D("Paying today")},"Yes"'), ("% paying today (of registrations)", None),
               ("From organic search", f',{D("Original source")},"Organic search"'),
               ("From direct traffic", f',{D("Original source")},"Direct"'),
               ("Offline (created by the app integration)", f',{D("Original source")},"Offline (app integration)"')]
    first = 11
    block = []
    for k, (name, crit) in enumerate(metrics):
        r = first + k
        if crit is None:
            pr = first + 6
            block.append([name] + [f'=IF({c}{first}>0,{c}{pr}/{c}{first},"")' for c in "BCDEF"]
                         + [f'=IF(AND(ISNUMBER(E{r}),ISNUMBER(F{r})),(E{r}-F{r})*100,"")'])
        else:
            block.append([name] + [f"=COUNTIFS({per(c)}{crit})" for c in "BCDEF"] + [f'=IF(F{r}>0,E{r}/F{r}-1,"")'])
    last = first + len(metrics) - 1
    put(f"A{first}:G{last}", block)
    pct_row = first + 7

    r0 = last + 2
    put(f"A{r0}:G{r0}", [["Registrations by segment", "Last full month", "Previous month", "Same month last year",
                          "Last 12 months", "Previous 12 months", "Share of last 12 months"]])
    seg = [[s] + [f"=COUNTIFS({per(c)},{D('Segment')},$A{r0 + 1 + i})" for c in "BCDEF"]
           + [f'=IF(E${first}>0,E{r0 + 1 + i}/E${first},"")'] for i, s in enumerate(SEGMENTS)]
    rt = r0 + 1 + len(SEGMENTS)
    seg.append(["Total"] + [f"=SUM({c}{r0 + 1}:{c}{rt - 1})" for c in "BCDEF"] + [f"=SUM(G{r0 + 1}:G{rt - 1})"])
    put(f"A{r0 + 1}:G{rt}", seg)

    p0 = rt + 2
    put(f"A{p0}:D{p0}", [["Paying today by plan (all accounts on the Data tab)", "Monthly", "Annual", "Total"]])
    pl = [[t, f'=COUNTIFS({D("Paying today")},"Yes",{D("Plan tier")},$A{p0 + 1 + i},{D("Billing")},B${p0})',
           f'=COUNTIFS({D("Paying today")},"Yes",{D("Plan tier")},$A{p0 + 1 + i},{D("Billing")},C${p0})',
           f"=B{p0 + 1 + i}+C{p0 + 1 + i}"] for i, t in enumerate(TIERS)]
    pt = p0 + 1 + len(TIERS)
    pl.append(["Total", f"=SUM(B{p0 + 1}:B{pt - 1})", f"=SUM(C{p0 + 1}:C{pt - 1})", f"=SUM(D{p0 + 1}:D{pt - 1})"])
    put(f"A{p0 + 1}:D{pt}", pl)

    q0 = pt + 2
    put(f"A{q0}:E{q0}", [["Paying today by segment (all accounts on the Data tab)", "Accounts", "Paying today",
                          "% paying", "Of paying: self-serve"]])
    ps = [[s, f"=COUNTIF({D('Segment')},$A{q0 + 1 + i})",
           f'=COUNTIFS({D("Segment")},$A{q0 + 1 + i},{D("Paying today")},"Yes")',
           f'=IF(B{q0 + 1 + i}>0,C{q0 + 1 + i}/B{q0 + 1 + i},"")',
           f'=COUNTIFS({D("Segment")},$A{q0 + 1 + i},{D("Paying today")},"Yes",{D("Account type")},"Self-serve")']
          for i, s in enumerate(SEGMENTS)]
    qt = q0 + 1 + len(SEGMENTS)
    ps.append(["Total", f"=SUM(B{q0 + 1}:B{qt - 1})", f"=SUM(C{q0 + 1}:C{qt - 1})",
               f'=IF(B{qt}>0,C{qt}/B{qt},"")', f"=SUM(E{q0 + 1}:E{qt - 1})"])
    put(f"A{q0 + 1}:E{qt}", ps)
    return S, {"first": first, "last": last, "pct_row": pct_row, "r0": r0, "rt": rt, "p0": p0, "pt": pt,
               "q0": q0, "qt": qt}


# ------------------------------------------------------------------ writes

GRAY = {"red": 0.93, "green": 0.93, "blue": 0.93}


def rng(sid, r1, r2, c1, c2):
    return {"sheetId": sid, "startRowIndex": r1, "endRowIndex": r2, "startColumnIndex": c1, "endColumnIndex": c2}


def fmt(sid, r1, r2, c1, c2, f, fields):
    return {"repeatCell": {"range": rng(sid, r1, r2, c1, c2), "cell": {"userEnteredFormat": f}, "fields": fields}}


def header(sid, r, c2):
    return fmt(sid, r, r + 1, 0, c2, {"textFormat": {"bold": True}, "backgroundColor": GRAY,
                                      "wrapStrategy": "WRAP", "verticalAlignment": "MIDDLE"},
               "userEnteredFormat(textFormat,backgroundColor,wrapStrategy,verticalAlignment)")


def number(sid, r1, r2, c1, c2, kind, pattern):
    return fmt(sid, r1, r2, c1, c2, {"numberFormat": {"type": kind, "pattern": pattern}}, "userEnteredFormat.numberFormat")


def width(sid, c1, c2, px):
    return {"updateDimensionProperties": {"range": {"sheetId": sid, "dimension": "COLUMNS", "startIndex": c1,
                                                    "endIndex": c2}, "properties": {"pixelSize": px},
                                          "fields": "pixelSize"}}


def height(sid, r1, r2, px):
    return {"updateDimensionProperties": {"range": {"sheetId": sid, "dimension": "ROWS", "startIndex": r1,
                                                    "endIndex": r2}, "properties": {"pixelSize": px},
                                          "fields": "pixelSize"}}


def grid(sid, rows, cols, frozen_rows=0, frozen_cols=0):
    return {"updateSheetProperties": {"properties": {"sheetId": sid, "gridProperties": {
        "rowCount": rows, "columnCount": cols, "frozenRowCount": frozen_rows, "frozenColumnCount": frozen_cols}},
        "fields": "gridProperties(rowCount,columnCount,frozenRowCount,frozenColumnCount)"}}


def chart_spec(sid_monthly: int, n_months: int) -> dict:
    first_seg = MONTHLY_HEAD.index(SEGMENTS[0])
    series = [{"series": {"sourceRange": {"sources": [rng(sid_monthly, 0, n_months + 1, first_seg + j, first_seg + j + 1)]}},
               "targetAxis": "LEFT_AXIS"} for j in range(len(SEGMENTS))]
    return {"title": "Registrations per month by segment", "basicChart": {
        "chartType": "COLUMN", "stackedType": "STACKED", "legendPosition": "RIGHT_LEGEND", "headerCount": 1,
        "axis": [{"position": "BOTTOM_AXIS"}, {"position": "LEFT_AXIS", "title": "Registrations"}],
        "domains": [{"domain": {"sourceRange": {"sources": [rng(sid_monthly, 0, n_months + 1, 0, 1)]}}}],
        "series": series}}


def write_data(rows: list[dict], meta: dict) -> None:
    sid = meta["Data"]["properties"]["sheetId"]
    gp = meta["Data"]["properties"]["gridProperties"]
    if gp["rowCount"] < len(rows) + 200 or gp["columnCount"] < len(DATA_HEAD):
        sheets_batch([grid(sid, max(gp["rowCount"], len(rows) + 200), max(gp["columnCount"], len(DATA_HEAD)), 1)])
    sheets_run("clear_values", {"spreadsheetId": SHEET, "range": f"Data!A2:{LAST}"})
    vals = [[r[h] for h in DATA_HEAD[:-1]] for r in rows]
    links = [[r["HubSpot record"]] for r in rows]
    sheets_run("update_values_batch", {"spreadsheetId": SHEET, "valueInputOption": "RAW", "data": [
        {"range": f"Data!A1:{LAST}1", "values": [DATA_HEAD]},
        {"range": f"Data!A2:{COL[DATA_HEAD[-2]]}{len(rows) + 1}", "values": vals}]})
    sheets_run("update_values_batch", {"spreadsheetId": SHEET, "valueInputOption": "USER_ENTERED", "data": [
        {"range": f"Data!{LAST}2:{LAST}{len(rows) + 1}", "values": links}]})
    sheets_batch([{"setBasicFilter": {"filter": {"range": rng(sid, 0, len(rows) + 1, 0, len(DATA_HEAD))}}},
                  number(sid, 1, len(rows) + 1, 0, 1, "DATE", "yyyy-mm-dd")])


def layout_inputs(rows: list[dict], as_of: _dt.date):
    months = months_until(as_of)
    tc = Counter(r["Type"] for r in rows)
    types = [t for t, _ in tc.most_common() if t not in ("Other", "Not specified")] + ["Other", "Not specified"]
    quarters = []
    for mk in months:
        q = f"{mk[:4]}-Q{(int(mk[5:]) - 1) // 3 + 1}"
        if q not in quarters:
            quarters.append(q)
    cc = Counter(r["Country"] for r in rows if r["Country"] != "Unknown" and r["Month"] != "Before 2023-07")
    top = [c for c, _ in cc.most_common(25)]
    return months, types, quarters, top


def write_tabs(rows: list[dict], as_of: _dt.date, meta: dict, full: bool) -> None:
    months, types, quarters, top = layout_inputs(rows, as_of)
    ids = {t: meta[t]["properties"]["sheetId"] for t in TABS}
    n = len(months)
    # grids big enough, then clear the blocks this script owns
    reqs = [grid(ids["Monthly"], max(n + 40, 80), len(MONTHLY_HEAD) + 4, 1, 1),
            grid(ids["By type"], max(n + 40, 80), len(types) + 4, 1, 1),
            grid(ids["By country"], len(top) + 10, len(quarters) + 6, 1, 1)]
    if full:
        reqs.append(grid(ids["Summary"], 120, 12))
        for t in ("Summary", "Monthly", "By type", "By country"):
            reqs.append({"updateCells": {"range": {"sheetId": ids[t]}, "fields": "userEnteredValue,userEnteredFormat,note"}})
        for t in TABS:
            for ch in meta[t].get("charts") or []:
                reqs.append({"deleteEmbeddedObject": {"objectId": ch["chartId"]}})
    else:
        reqs += [{"updateCells": {"range": rng(ids["Monthly"], 1, max(n + 40, 80), 0, len(MONTHLY_HEAD)),
                                  "fields": "userEnteredValue,note"}},
                 {"updateCells": {"range": rng(ids["By type"], 0, max(n + 40, 80), 0, len(types) + 4),
                                  "fields": "userEnteredValue,note"}},
                 {"updateCells": {"range": {"sheetId": ids["By country"]}, "fields": "userEnteredValue,note"}}]
    sheets_batch(reqs)
    data = [{"range": f"Monthly!A1:{col(len(MONTHLY_HEAD) - 1)}{n + 1}", "values": monthly_values(months)},
            {"range": f"'By type'!A1:{col(len(types) + 1)}{n + 1}", "values": bytype_values(months, types)},
            {"range": f"'By country'!A1:{col(len(quarters) + 1)}{len(top) + 4}", "values": bycountry_values(quarters, top)}]
    lay = None
    if full:
        summary, lay = summary_values()
        data += summary
    data.append({"range": "Summary!B6", "values": [[(as_of - _dt.date(1899, 12, 30)).days]]})
    sheets_run("update_values_batch", {"spreadsheetId": SHEET, "valueInputOption": "USER_ENTERED", "data": data})

    m = ids["Monthly"]
    note = "Month in progress: data as of the date on the Summary tab."
    pct_col = MONTHLY_HEAD.index("% paying today")
    reqs = [header(m, 0, len(MONTHLY_HEAD)), number(m, 1, n + 1, pct_col, pct_col + 1, "PERCENT", "0.0%"),
            width(m, 1, len(MONTHLY_HEAD), 100), height(m, 0, 1, 60),
            {"updateCells": {"range": rng(m, n, n + 1, 0, 1), "rows": [{"values": [{"note": note}]}], "fields": "note"}},
            header(ids["By type"], 0, len(types) + 2), width(ids["By type"], 1, len(types) + 2, 100),
            height(ids["By type"], 0, 1, 60),
            fmt(ids["By type"], 0, n + 1, len(types) + 1, len(types) + 2, {"textFormat": {"bold": True}}, "userEnteredFormat.textFormat"),
            {"updateCells": {"range": rng(ids["By type"], n, n + 1, 0, 1), "rows": [{"values": [{"note": note}]}], "fields": "note"}},
            header(ids["By country"], 0, len(quarters) + 2), width(ids["By country"], 0, 1, 170),
            fmt(ids["By country"], len(top) + 3, len(top) + 4, 0, len(quarters) + 2, {"textFormat": {"bold": True}}, "userEnteredFormat.textFormat"),
            fmt(ids["By country"], 0, len(top) + 4, len(quarters) + 1, len(quarters) + 2, {"textFormat": {"bold": True}}, "userEnteredFormat.textFormat"),
            {"updateCells": {"range": rng(ids["By country"], 0, 1, 0, 1), "rows": [{"values": [{"note":
                "Country = IP country in HubSpot; empty for about half of the sign-ups (Unknown). "
                "Quarters by sign-up date; accounts from before Jul 2023 are not shown here."}]}], "fields": "note"}}]
    if full:
        s = ids["Summary"]
        grey = {"red": 0.4, "green": 0.4, "blue": 0.4}
        reqs += [fmt(s, 0, 1, 0, 1, {"textFormat": {"bold": True, "fontSize": 14}}, "userEnteredFormat.textFormat"),
                 fmt(s, 1, 4, 0, 1, {"textFormat": {"italic": True, "foregroundColor": grey}}, "userEnteredFormat.textFormat"),
                 fmt(s, 5, 6, 0, 1, {"textFormat": {"bold": True}}, "userEnteredFormat.textFormat"),
                 number(s, 5, 6, 1, 2, "DATE", "d mmm yyyy"), number(s, 8, 10, 1, 6, "DATE", "d mmm yyyy"),
                 fmt(s, 8, 10, 0, 6, {"textFormat": {"foregroundColor": grey, "fontSize": 9}}, "userEnteredFormat.textFormat"),
                 header(s, 7, 7), header(s, lay["r0"] - 1, 7), header(s, lay["p0"] - 1, 4), header(s, lay["q0"] - 1, 5),
                 number(s, lay["first"] - 1, lay["last"], 6, 7, "PERCENT", "+0%;-0%;0%"),
                 number(s, lay["pct_row"] - 1, lay["pct_row"], 1, 6, "PERCENT", "0.0%"),
                 number(s, lay["pct_row"] - 1, lay["pct_row"], 6, 7, "NUMBER", '+0.0" pp";-0.0" pp";0.0" pp"'),
                 number(s, lay["r0"], lay["rt"], 6, 7, "PERCENT", "0%"),
                 number(s, lay["q0"], lay["qt"], 3, 4, "PERCENT", "0.0%"),
                 fmt(s, lay["rt"] - 1, lay["rt"], 0, 7, {"textFormat": {"bold": True}}, "userEnteredFormat.textFormat"),
                 fmt(s, lay["pt"] - 1, lay["pt"], 0, 4, {"textFormat": {"bold": True}}, "userEnteredFormat.textFormat"),
                 fmt(s, lay["qt"] - 1, lay["qt"], 0, 5, {"textFormat": {"bold": True}}, "userEnteredFormat.textFormat"),
                 width(s, 0, 1, 340), width(s, 1, 7, 125), height(s, 7, 8, 40), height(s, lay["r0"] - 1, lay["r0"], 40),
                 header(ids["Data"], 0, len(DATA_HEAD)),
                 {"addChart": {"chart": {"spec": chart_spec(m, n), "position": {"overlayPosition": {
                     "anchorCell": {"sheetId": s, "rowIndex": lay["qt"] + 1, "columnIndex": 0},
                     "widthPixels": 1000, "heightPixels": 400}}}}}]
    else:
        for t in TABS:
            for ch in meta[t].get("charts") or []:
                reqs.append({"updateChartSpec": {"chartId": ch["chartId"], "spec": chart_spec(m, n)}})
    sheets_batch(reqs)
    if full:
        sheets_batch([{"autoResizeDimensions": {"dimensions": {"sheetId": ids["Data"], "dimension": "COLUMNS",
                                                               "startIndex": 0, "endIndex": len(DATA_HEAD)}}}])


# ------------------------------------------------------------------ commands

def summarize(rows: list[dict], stats: Counter, as_of: _dt.date) -> str:
    last_end = as_of.replace(day=1) - _dt.timedelta(days=1)
    last_month = last_end.strftime("%Y-%m")
    l12_start = (last_end.replace(day=1) - _dt.timedelta(days=330)).replace(day=1)
    in_l12 = [r for r in rows if r["Sign-up date"] is not None and r["Month"] != "Before 2023-07"
              and l12_start.strftime("%Y-%m") <= r["Month"] <= last_month]
    lm = [r for r in rows if r["Month"] == last_month]
    seg = Counter(r["Segment"] for r in lm)
    lines = [f"MT self-serve report, data as of {as_of}",
             f"{last_month}: {len(lm)} registrations ({sum(r['Account type'] == 'Self-serve' for r in lm)} self-serve), "
             f"{sum(r['Started with'] == '$1 trial' for r in lm)} $1 trials, "
             f"{sum(r['Started with'] == 'Paid plan (no trial)' for r in lm)} paid plan sign-ups, "
             f"{sum(r['Paying today'] == 'Yes' for r in lm)} paying today",
             f"Last 12 months: {len(in_l12)} registrations, {sum(r['Started with'] == '$1 trial' for r in in_l12)} $1 trials, "
             f"{sum(r['Started with'] == 'Paid plan (no trial)' for r in in_l12)} paid plan sign-ups, "
             f"{sum(r['Paying today'] == 'Yes' for r in in_l12)} paying today",
             "Top segments last month: " + ", ".join(f"{k} {v}" for k, v in seg.most_common(4)),
             f"All accounts: {len(rows)}, paying today {sum(r['Paying today'] == 'Yes' for r in rows)}",
             "Date sources: " + ", ".join(f"{k} {v}" for k, v in stats.items())]
    return "\n".join(lines)


def send(msg: str) -> bool:
    spec = importlib.util.spec_from_file_location("outbound_pipeline", PIPE)
    op = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(op)
    return op.telegram_send(msg)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("refresh", "build", "stats"):
        p = sub.add_parser(name)
        p.add_argument("--dry-run", action="store_true")
        p.add_argument("--notify", action="store_true", help="Telegram summary (refresh)")
        p.add_argument("--as-of", help="data date, default today (Kyiv)")
    args = ap.parse_args()
    as_of = _dt.date.fromisoformat(args.as_of) if args.as_of else _dt.datetime.now(TZ).date()
    try:
        rows, stats = build_rows(pull_app_users(), as_of)
        text = summarize(rows, stats, as_of)
        print(text)
        if args.cmd == "stats" or args.dry_run:
            return 0
        meta = sheet_meta()
        missing = [t for t in TABS if t not in meta]
        if missing:
            raise Broken(f"sheet tabs missing: {missing}")
        write_data(rows, meta)
        write_tabs(rows, as_of, sheet_meta(), full=args.cmd == "build")
        print(f"sheet updated: https://docs.google.com/spreadsheets/d/{SHEET}")
        if args.notify:
            send(text + f"\nhttps://docs.google.com/spreadsheets/d/{SHEET}")
        return 0
    except Broken as e:
        print(f"FAILED: {e}", file=sys.stderr)
        if args.notify:
            send(f"MT self-serve report FAILED: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
