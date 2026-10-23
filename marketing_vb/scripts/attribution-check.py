#!/usr/bin/env python3
"""attribution-check.py — follow-up on the cookie-banner attribution break (found 2026-10-23).

WHY THIS EXISTS
---------------
Since 2026-02-04 the WebToffee cookie banner shows the GDPR opt-in banner worldwide, and HubSpot tracks a
visitor only after Accept. Someone who accepts on a later page gets HubSpot original source Direct, with
the first page view referred by our own site. Work-email Direct contacts like that went from ~13 a month
(Jul 2024 – Jan 2026) to ~26 (Mar – Sep 2026). On 2026-10-23 Asel was asked to geo-target the GDPR
banner to EU & UK. This script tells whether the change happened and whether the count went back down.

COMMANDS
  watch [--notify]    fetch the banner config from the live page; the first time it differs from the
                      2026-10-23 state (GDPR and US State Laws both "ALL"), record the date and send one
                      Telegram message. Silent otherwise. Cron: daily.
  report [--notify]   weekly counts from HubSpot for the last 8 full weeks (work-email inbound contacts,
                      the same exclusions as organic-dashboard.py) plus the banner state; Telegram with
                      --notify. Cron: once, 2026-11-13.

STATE (outside the repo; the repo is public)
  ~/.hermes/.attribution-check-state.json: banner config last seen, the date it changed.

Exit: 0 ok · 3 broken (the page, oo or HubSpot failed).
"""
from __future__ import annotations

import argparse
import datetime as _dt
import importlib.util
import json
import re
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
STATE = Path.home() / ".hermes" / ".attribution-check-state.json"
PAGE = "https://3dlook.ai/contact-us/"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
OLD = {"gdpr": '"ALL"', "ccpa": '"ALL"'}         # the 2026-10-23 state: both laws worldwide
OWN_REF = re.compile(r"^https?://([a-z0-9-]+\.)?3dlook\.(ai|me)", re.I)
BASELINE, BROKEN = 13, 26                        # Direct with an internal first referrer, per month


class Broken(Exception):
    pass


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
    STATE.write_text(json.dumps(state, indent=1), encoding="utf-8")


def banner() -> dict:
    """Per law: selected region (raw JSON), plus the Analytics category defaults and the renew stamp."""
    try:
        req = urllib.request.Request(PAGE, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=60) as r:
            html = r.read().decode("utf-8", "replace")
    except OSError as e:
        raise Broken(f"{PAGE}: {e}")
    out = {law: region for law, region in
           re.findall(r'"applicableLaw":"(gdpr|ccpa)"[^{}]*?"selectedRegion":(\[[^\]]*\]|"[^"]*")', html)}
    m = re.search(r'"name":"Analytics","slug":"analytics".{0,20000}?"defaultConsent":(\{[^}]*\})', html, re.S)
    out["analytics_default"] = m.group(1) if m else None
    m = re.search(r'"_gdprAllowedRegions":(\[[^\]]*\])', html)
    out["gdpr_regions"] = m.group(1) if m else None   # the GDPR banner shows only to these countries (or is_eu)
    m = re.search(r'"_renewConsent":"(\d+)"', html)
    out["renew"] = _dt.datetime.fromtimestamp(int(m.group(1)) / 1000, _dt.timezone.utc).strftime("%Y-%m-%d %H:%M")\
        if m else None
    if "gdpr" not in out and "ccpa" not in out:
        raise Broken("banner config not found on the page (WebToffee removed or markup changed)")
    return out


def describe(b: dict) -> str:
    regions = b.get("gdpr_regions") or "[]"
    uk = "UK є" if '"GB"' in regions else "⚠️ UK немає (британці не in_eu → без банера)" if regions != "[]" else "список порожній"
    return (f"GDPR: {b.get('gdpr', 'вимкнено')} ({uk}) · US State Laws: {b.get('ccpa', 'вимкнено')} · "
            f"Analytics за замовчуванням: {b.get('analytics_default')} · renew consent: {b.get('renew')}")


def changed(b: dict) -> bool:
    return any(b.get(k) != v for k, v in OLD.items())


def send(msg: str) -> bool:
    return load_module("outbound_pipeline", HERE / "outbound-pipeline.py").telegram_send(msg)


def cmd_watch(args) -> int:
    state = load_state()
    b = banner()
    state["last_seen"], state["last_checked"] = b, _dt.date.today().isoformat()
    if changed(b) and not state.get("changed_on"):
        state["changed_on"] = _dt.date.today().isoformat()
        msg = ("🍪 Налаштування cookie-банера на 3dlook.ai змінились.\n" + describe(b) +
               "\n\nПопроси Claude перевірити з німецького IP, що GDPR-банер для EU лишився, а Асель — "
               "через VPN зі США, що hubspotutk ставиться без Accept. Підсумок по HubSpot прийде 13.11.")
        print(msg)
        if args.notify:
            send(msg)
    save_state(state)
    return 0


def weekly(end: _dt.date) -> list[dict]:
    """Last 8 full Mon–Sun weeks up to `end`: work-email inbound contacts by source bucket."""
    od = load_module("organic_dashboard", HERE / "organic-dashboard.py")
    hr = load_module("hubspot_handraisers", HERE / "hubspot-handraisers.py")
    last_monday = end - _dt.timedelta(days=end.weekday() + 7)
    weeks = [last_monday - _dt.timedelta(days=7 * i) for i in range(7, -1, -1)]
    lo, hi = weeks[0], last_monday + _dt.timedelta(days=7)
    props = sorted(set(hr.PROPS) | {"createdate", "hs_analytics_source", "hs_analytics_first_referrer", "icp_segment"})
    window = [{"propertyName": "createdate", "operator": "GTE", "value": f"{lo.isoformat()}T00:00:00Z"},
              {"propertyName": "createdate", "operator": "LT", "value": f"{hi.isoformat()}T00:00:00Z"},
              {"propertyName": "first_conversion_event_name", "operator": "HAS_PROPERTY"}]
    try:
        contacts = od.hubspot_search("CONTACT", [{"filters": window}], props)
    except od.Broken as e:
        raise Broken(str(e))
    W = {wk: defaultdict(int) for wk in weeks}
    for p in contacts:
        form, dom = hr.form(p.get("first_conversion_event_name")), hr.domain(p)
        if (od.MT_APP_FORM.search(p.get("first_conversion_event_name") or "") or od.CAREERS.search(form)
                or p.get("icp_segment") == "Job seeker" or od.NEWSLETTER.search(form) or dom in hr.OWN
                or hr.OUTBOUND_LS.search(p.get("lead_source") or "")):
            continue
        if not dom or dom in hr.CONSUMER or od.PERSONAL_PREFIX.match(dom):
            continue
        day = _dt.date.fromisoformat(p["createdate"][:10])
        a = W[od.monday(day)]
        src = p.get("hs_analytics_source") or ""
        a["work"] += 1
        a["organic"] += src == "ORGANIC_SEARCH"
        a["ai"] += src == "AI_REFERRALS"
        a["direct_internal"] += src == "DIRECT_TRAFFIC" and bool(OWN_REF.match(p.get("hs_analytics_first_referrer") or ""))
    return [{"week": wk, **W[wk]} for wk in weeks]


def cmd_report(args) -> int:
    state = load_state()
    b = banner()
    rows = weekly(_dt.date.today())
    since = state.get("changed_on")
    lines = ["🍪 Атрибуція HubSpot після зміни cookie-банера",
             f"Банер зараз: {describe(b)}",
             f"Зміна помічена: {since}" if since else
             ("⚠️ Налаштування банера НЕ змінились (GDPR і US State Laws досі на весь світ)." if not changed(b) else
              "Банер змінено, але дату зміни watch не зафіксував."), "",
             "Робочі контакти по тижнях: усього · Direct з внутрішньої сторінки · органіка · AI"]
    for r in rows:
        mark = " ←після зміни" if since and r["week"] >= _dt.date.fromisoformat(since) else ""
        lines.append(f"{r['week'].strftime('%d.%m')}: {r['work']} · {r['direct_internal']} · {r['organic']} · {r['ai']}{mark}")
    after = [r for r in rows if since and r["week"] >= _dt.date.fromisoformat(since) + _dt.timedelta(days=7)]
    if after:
        per_month = sum(r["direct_internal"] for r in after) / len(after) * 30.4 / 7
        verdict = ("повернулось до норми" if per_month <= (BASELINE + BROKEN) / 2 else "досі зламано")
        lines += ["", f"Direct з внутрішньої сторінки після зміни: ~{per_month:.0f}/міс (норма ~{BASELINE}, "
                      f"зламано ~{BROKEN}) → {verdict}. Повних тижнів після зміни: {len(after)}."]
    lines += ["", "Контекст: пам'ять project_hubspot_attribution_consent_break; застереження на вкладці About "
                  "в Organic Dashboard прибрати, коли норма повернеться."]
    msg = "\n".join(lines)
    print(msg)
    if args.notify:
        send(msg)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("watch", "report"):
        sub.add_parser(name).add_argument("--notify", action="store_true")
    args = ap.parse_args()
    try:
        return {"watch": cmd_watch, "report": cmd_report}[args.cmd](args)
    except Broken as e:
        print(f"attribution-check: {e}", file=sys.stderr)
        if getattr(args, "notify", False):
            send(f"⚠️ attribution-check ({args.cmd}) не спрацював: {str(e)[:400]}")
        return 3


if __name__ == "__main__":
    sys.exit(main())
