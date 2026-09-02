#!/usr/bin/env python3
"""web-verify.py — verify a companies.csv against the live web, without a vendor key.

WHY
---
`web_extract` in Hermes needs a paid backend (firecrawl / tavily / keenable / exa /
parallel). None is configured — `~/.hermes/.env` has EXA_API_KEY and FIRECRAWL_API_KEY
commented out — and SearXNG is search-only, so every `web_extract` call on 2026-09-02
came back:

    SearXNG is a search-only backend and cannot extract URL content.

The consequence was not an error the run stopped on. It was 26 company rows all carrying
`verification=unverified-desk`: nobody had checked a single HQ, app or subscription claim
against a live source. A shortlist that has never touched the web is indistinguishable
from one the model remembered.

Fetching a public marketing site does not need a vendor. It needs a browser User-Agent
and an honest three-way answer. That is this script.

THE THREE OUTCOMES (measured 2026-09-02 on the UK campaign)
-----------------------------------------------------------
    verified-live   200 + a <title>. Evidence columns are filled from the page.
    blocked         403 / 429 / a JS challenge. secondnature.io and numan.com answer
                    curl fine; joinvoy.com returns 429 "Vercel Security Checkpoint" to
                    curl AND to a real headless Chrome from this VPS — the datacenter IP
                    is the problem, not the fetcher. Retrying it through a browser is
                    wasted work, so `blocked` is a terminal state here and the row is
                    listed for a human or a residential proxy.
    dead            DNS failure, 404, timeout. A company with no reachable site is a
                    finding, not a blank.

`blocked` is deliberately NOT folded into `unverified`. "We could not look" and "we
looked and the door was shut" send a researcher to different next actions.

APP-STORE EVIDENCE IS A NEGATIVE-ONLY SIGNAL
--------------------------------------------
Homepages often carry no store links even when the app exists: myjuniper.co.uk renders
zero apps.apple.com links in a real browser, yet Juniper ships an iOS app. So a hit is
evidence of an app; a miss is recorded as `none-on-homepage`, never as "no app". The
column name says so, to stop the next reader over-reading it.

USAGE
    scripts/web-verify.py verify --campaign 2026-09-01-uk-erakulis-similar
    scripts/web-verify.py verify --campaign <slug> --limit 5      # smoke-test
    scripts/web-verify.py verify --campaign <slug> --in companies-glp1-telehealth.csv
    scripts/web-verify.py verify --url https://www.numan.com/     # one-off, no CSV

Writes `<in-stem>-verified.csv` next to the input and prints a summary. Never edits the
input in place: the unverified list stays on disk as the record of what was claimed.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import csv
import html
import http.cookiejar
import ipaddress
import re
import socket
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/147.0.0.0 Safari/537.36"
)
# A bare urllib request is refused or throttled by a lot of marketing stacks. These are
# the headers a real Chrome sends that actually change the answer; measured against
# myjuniper.co.uk, secondnature.io and numan.com.
HEADERS = {
    "User-Agent": UA,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-GB,en;q=0.9",
    "Accept-Encoding": "identity",
}

MAX_BYTES = 3_000_000          # numan.com's homepage is ~1 MB; 3 MB is headroom, not a cap we hit
DEFAULT_TIMEOUT = 25
DEFAULT_WORKERS = 6            # polite: these are real companies, not a load test

CHALLENGE_MARKERS = (
    "security checkpoint",
    "just a moment",
    "checking your browser",
    "attention required",
    "cf-browser-verification",
    "captcha-delivery",
    "px-captcha",
)

SUBSCRIPTION_WORDS = (
    "per month", "a month", "/month", "monthly", "subscription", "cancel anytime",
    "billed monthly", "per week", "plan",
)

GEO_WORDS = (
    "United Kingdom", "England", "London", "Scotland", "Wales", "Manchester",
    "United States", "USA", "New York", "San Francisco", "Australia", "Sydney",
    "Melbourne", "Israel", "Tel Aviv", "Sweden", "Stockholm", "Germany", "Berlin",
)

# "Registered in England and Wales" is the standard Companies House formula on every UK
# site's footer. Left alone it makes `evidence_geo` report Wales for a London company —
# numan.com did exactly that on 2026-09-02, cross-checked in a real browser. The phrase
# is boilerplate, not a location, so it is removed before geo keywords are counted.
GEO_BOILERPLATE = (
    re.compile(r"registered\s+in\s+england\s+and\s+wales", re.I),
    re.compile(r"england\s*(?:&|and)\s*wales", re.I),
)

# The legal-registration disclosure is the most reliable HQ evidence a marketing site
# carries: it is filed text, not copy. Two shapes cover the UK/EU sites in this pipeline,
# tried in this order — numan.com carries the first, myjuniper.co.uk only the second.
#
# What is deliberately NOT here: the shape `registered in <Place>`. It reads like a
# company registration and is not one. On myjuniper.co.uk it matched "prescribers are
# registered in the United Kingdom with the General Pharmaceutical Council" — a
# professional-body registration, which says nothing about where the company sits.
# Cross-checked in a real browser on 2026-09-02; the pattern was removed, not narrowed,
# because every variant of it collides with regulator wording in this vertical.
REGISTERED_OFFICE = (
    re.compile(r"registered\s+(?:office|address)[^.<]{0,160}", re.I),
    re.compile(
        r"(?:company|registration)\s+(?:number|no\.?|reg\.?)\s*:?\s*([A-Z]{0,2}[0-9]{6,10})",
        re.I,
    ),
)

VERIFY_HEADERS = [
    "verification", "source_url", "http_status", "evidence_title",
    "evidence_app_store", "evidence_subscription", "evidence_geo",
    "evidence_registered_office", "checked_at",
]


# --------------------------------------------------------------------------- paths

def repo_root() -> Path:
    """marketing_vb/, resolved from this file — never from cwd.

    Same rule as outbound-registry.py: `oo`/OpenCode launch subprocesses from the
    parent's directory, so anything derived from cwd silently writes to the wrong tree.
    """
    return Path(__file__).resolve().parent.parent


def campaign_dir(slug: str) -> Path:
    return repo_root() / "workspace" / "outbound" / "campaigns" / slug


# --------------------------------------------------------------------------- fetching

def _is_public_http_url(url: str) -> tuple[bool, str]:
    """Reject anything that is not a public http(s) URL.

    A companies.csv is model-written, so a `website` cell can hold anything. Resolving
    a hostname that points at 127.0.0.1 or 169.254.169.254 would turn this script into
    an SSRF tool against our own VPS and its cloud metadata endpoint.
    """
    try:
        p = urllib.parse.urlsplit(url)
    except ValueError:
        return False, "unparseable-url"
    if p.scheme not in ("http", "https"):
        return False, f"scheme-not-http:{p.scheme or 'none'}"
    if not p.hostname:
        return False, "no-host"
    host = p.hostname.lower()
    if host in ("localhost",) or host.endswith(".localhost") or host.endswith(".internal"):
        return False, "private-host"
    try:
        infos = socket.getaddrinfo(host, None)
    except socket.gaierror:
        return False, "dns-failure"
    for info in infos:
        try:
            ip = ipaddress.ip_address(info[4][0])
        except ValueError:
            continue
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved:
            return False, "private-address"
    return True, ""


def _opener() -> urllib.request.OpenerDirector:
    """A fresh opener with its own cookie jar, per fetch.

    Without cookies, puregym.com answers the first GET with `302 -> itself` plus a
    Set-Cookie, urllib re-requests without the cookie and gets the same 302 forever, and
    the site looks dead. It is not: a real browser renders "Cheap 24 Hour Gym
    Memberships UK | No Contract | PureGym" (checked 2026-09-02). One cookie round-trip
    is the whole difference, so every fetch carries a jar.

    The jar is per-call, not shared: these are unrelated companies and a shared jar would
    leak one site's session into another's request.
    """
    jar = http.cookiejar.CookieJar()
    return urllib.request.build_opener(urllib.request.HTTPCookieProcessor(jar))


def fetch(url: str, timeout: int = DEFAULT_TIMEOUT) -> dict:
    """One page. Returns a dict with status/body/final_url/error — never raises."""
    ok, why = _is_public_http_url(url)
    if not ok:
        return {"status": 0, "body": "", "final_url": url, "error": why}
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with _opener().open(req, timeout=timeout) as resp:
            raw = resp.read(MAX_BYTES)
            charset = resp.headers.get_content_charset() or "utf-8"
            return {
                "status": resp.status,
                "body": raw.decode(charset, errors="replace"),
                "final_url": resp.geturl(),
                "error": "",
            }
    except urllib.error.HTTPError as e:
        # A 403/429 body still carries the challenge marker we want to report.
        try:
            body = e.read(MAX_BYTES).decode("utf-8", errors="replace")
        except Exception:
            body = ""
        return {"status": e.code, "body": body, "final_url": url, "error": f"http-{e.code}"}
    except urllib.error.URLError as e:
        return {"status": 0, "body": "", "final_url": url, "error": f"urlerror:{e.reason}"}
    except (TimeoutError, socket.timeout):
        return {"status": 0, "body": "", "final_url": url, "error": "timeout"}
    except Exception as e:  # noqa: BLE001 — one bad row must not kill the batch
        return {"status": 0, "body": "", "final_url": url, "error": f"{type(e).__name__}:{e}"}


# --------------------------------------------------------------------------- parsing

def _title(body: str) -> str:
    m = re.search(r"<title[^>]*>(.*?)</title>", body, re.I | re.S)
    if not m:
        return ""
    return re.sub(r"\s+", " ", html.unescape(m.group(1))).strip()[:200]


def _visible_text(body: str) -> str:
    """Crude tag-strip. Enough for keyword presence; not for reading prose."""
    t = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", body)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", html.unescape(t))


def _app_store(body: str) -> str:
    apple = bool(re.search(r"(apps|itunes)\.apple\.com", body, re.I))
    play = bool(re.search(r"play\.google\.com", body, re.I))
    if apple and play:
        return "ios+android"
    if apple:
        return "ios"
    if play:
        return "android"
    # See the module docstring: a miss is not "no app".
    return "none-on-homepage"


def _keywords(text: str, words: tuple[str, ...], limit: int) -> str:
    low = text.lower()
    hits = [w for w in words if w.lower() in low]
    return "; ".join(hits[:limit])


def _geo(text: str) -> str:
    """Geo keywords with the Companies House boilerplate stripped first.

    WEAK EVIDENCE ON PURPOSE. A keyword hit means the word is somewhere on the page, not
    that the company sits there: myjuniper.co.uk reports "Australia" because a team
    member's bio says "Global Clinical Director for Australia" (verified in a browser,
    2026-09-02). Anything deciding geo — the filter in outbound-pipeline.py — must read
    `evidence_registered_office` first and treat this column as a hint for a human.
    """
    cleaned = text
    for pat in GEO_BOILERPLATE:
        cleaned = pat.sub(" ", cleaned)
    return _keywords(cleaned, GEO_WORDS, 4)


def _registered_office(text: str) -> str:
    """The legal-disclosure HQ line, if the page carries one."""
    for pat in REGISTERED_OFFICE:
        m = pat.search(text)
        if m:
            return re.sub(r"\s+", " ", m.group(0)).strip()[:180]
    return ""


def classify(res: dict) -> tuple[str, str]:
    """(verification, note) from a fetch result."""
    status, body, err = res["status"], res["body"], res["error"]
    low = body[:20000].lower()
    if any(m in low for m in CHALLENGE_MARKERS):
        return "blocked", "js-challenge"
    if status in (401, 403, 429):
        return "blocked", f"http-{status}"
    if status == 404 or status == 410:
        return "dead", f"http-{status}"
    if 300 <= status < 400:
        # Followed redirects already; still on a 3xx means a cookie/consent gate we
        # did not satisfy. Not dead — a browser gets through.
        return "blocked", f"http-{status}-redirect-gate"
    if status >= 500:
        return "dead", f"http-{status}"
    if err.startswith("dns-failure"):
        return "dead", "dns-failure"
    if err in ("timeout",) or err.startswith("urlerror"):
        return "dead", err
    if err:
        return "dead", err
    if status == 200 and not _title(body):
        # 200 with no title is usually a JS shell that never rendered server-side.
        return "blocked", "no-title-js-shell"
    if status == 200:
        return "verified-live", ""
    return "dead", f"http-{status}"


def verify_one(company: str, url: str, timeout: int) -> dict:
    """Fetch + classify one company. Returns the VERIFY_HEADERS payload."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    if not url.strip():
        return {
            "verification": "unverified-no-website", "source_url": "", "http_status": "",
            "evidence_title": "", "evidence_app_store": "", "evidence_subscription": "",
            "evidence_geo": "", "evidence_registered_office": "", "checked_at": now,
        }
    res = fetch(url.strip(), timeout=timeout)
    verdict, note = classify(res)
    body = res["body"]
    text = _visible_text(body) if body else ""
    title = _title(body)
    return {
        "verification": verdict if not note else f"{verdict}:{note}",
        "source_url": res["final_url"],
        "http_status": str(res["status"] or res["error"]),
        "evidence_title": title,
        "evidence_app_store": _app_store(body) if verdict == "verified-live" else "",
        "evidence_subscription": _keywords(text, SUBSCRIPTION_WORDS, 4) if verdict == "verified-live" else "",
        "evidence_geo": _geo(text) if verdict == "verified-live" else "",
        "evidence_registered_office": _registered_office(text) if verdict == "verified-live" else "",
        "checked_at": now,
    }


# --------------------------------------------------------------------------- commands

def cmd_verify(args) -> int:
    if args.url:
        out = verify_one("(ad-hoc)", args.url, args.timeout)
        width = max(len(k) for k in out)
        for k, v in out.items():
            print(f"  {k:<{width}}  {v}")
        return 0 if out["verification"].startswith("verified") else 1

    cdir = campaign_dir(args.campaign)
    src = cdir / args.infile
    if not src.exists():
        print(f"✗ not found: {src}", file=sys.stderr)
        return 2

    with src.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        print(f"✗ empty: {src}", file=sys.stderr)
        return 2

    name_col = next((c for c in rows[0] if c and c.lower() in ("company_name", "company")), None)
    site_col = next((c for c in rows[0] if c and c.lower() in ("website", "url", "domain")), None)
    if not site_col:
        print(f"✗ {src.name} has no website/url column — nothing to verify", file=sys.stderr)
        return 2

    todo = rows[: args.limit] if args.limit else rows
    print(f"→ {src.name}: verifying {len(todo)} of {len(rows)} rows "
          f"({DEFAULT_WORKERS} workers, {args.timeout}s timeout)\n")

    results: dict[int, dict] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=DEFAULT_WORKERS) as pool:
        futures = {
            pool.submit(verify_one, r.get(name_col, ""), r.get(site_col, "") or "", args.timeout): i
            for i, r in enumerate(todo)
        }
        for fut in concurrent.futures.as_completed(futures):
            i = futures[fut]
            results[i] = fut.result()
            v = results[i]["verification"]
            mark = "✓" if v.startswith("verified") else ("⊘" if v.startswith("blocked") else "✗")
            nm = (todo[i].get(name_col, "") or "?")[:34]
            print(f"  {mark} {nm:<34} {v}")

    # Merge: verified rows keep every original column, verification columns overwritten.
    fieldnames = [c for c in rows[0] if c] + [h for h in VERIFY_HEADERS if h not in rows[0]]
    for i, r in enumerate(rows):
        if i in results:
            r.update(results[i])
        else:
            r.setdefault("verification", r.get("verification", "unverified-desk"))

    dst = src.with_name(f"{src.stem}-verified.csv")
    with dst.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    counts: dict[str, int] = {}
    for r in results.values():
        counts[r["verification"].split(":")[0]] = counts.get(r["verification"].split(":")[0], 0) + 1
    print(f"\n{'-' * 62}")
    for k in ("verified-live", "blocked", "dead", "unverified-no-website"):
        if counts.get(k):
            print(f"  {k:<22} {counts[k]}")
    print(f"\n→ wrote {dst.relative_to(repo_root())}")

    blocked = [todo[i].get(name_col, "?") for i, r in results.items() if r["verification"].startswith("blocked")]
    if blocked:
        print("\n⚠ blocked from this VPS — needs a human or a residential proxy, "
              "NOT a browser retry:")
        for b in blocked:
            print(f"    · {b}")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        prog="web-verify.py",
        description="Verify companies.csv rows against the live web (no vendor key needed).",
    )
    sub = ap.add_subparsers(dest="cmd", required=True)

    v = sub.add_parser("verify", help="fetch every company website and classify it")
    v.add_argument("--campaign", help="campaign slug under workspace/outbound/campaigns/")
    v.add_argument("--in", dest="infile", default="companies.csv",
                   help="input CSV inside the campaign dir (default: companies.csv)")
    v.add_argument("--url", help="verify one URL and exit; ignores --campaign")
    v.add_argument("--limit", type=int, default=0, help="only the first N rows (smoke test)")
    v.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    v.set_defaults(func=cmd_verify)

    args = ap.parse_args(argv)
    if args.cmd == "verify" and not args.url and not args.campaign:
        ap.error("verify needs --campaign or --url")
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
