#!/usr/bin/env python3
"""apollo-pull.py — step 3 people from Apollo, as a second source next to Sales Navigator.

WHY THIS EXISTS
---------------
Step 3 was always Vadim exporting Sales Navigator by hand into `sales-nav-raw/`. Since
2026-10-01 Apollo can fill the same folder: free people search by company domain and the
hypothesis titles, then paid enrichment for the LinkedIn URL. Vadim cleared the use of Apollo
data for LinkedIn outreach with Apollo on 2026-10-01 (their API terms list "using any API with
LinkedIn automations" as prohibited by default, so that clearance is the precondition).

Both sources live side by side. The file this writes, `sales-nav-raw/apollo-<date>.csv`, has
the Sales Navigator export's columns, so `extract-people`, `compact` and the validator read
it unchanged. When one person is in both, the Sales Navigator row wins (it carries Bio and
Skills, Apollo has neither): `extract-people` and `raw_index` read apollo-* files last.

WHAT IT COSTS (docs.apollo.io, read 2026-10-01)
----------------------------------------------
    people search   POST /api/v1/mixed_people/api_search    0 credits, no LinkedIn URL,
                    last name obfuscated ("Hu***n"), 100 per page
    enrichment      POST /api/v1/people/bulk_match          1 credit per matched person
                    (10 per call), never with personal emails, phones or waterfall: those
                    cost 8-45 credits and are useless for LinkedIn outreach

`search` is free and writes `apollo-candidates.csv` with a credit estimate. `enrich` spends
credits and refuses to go past `--max-credits`. `pull` is both.

THE PREVIOUS-EMPLOYER TRAP
--------------------------
`q_organization_domains_list[]` matches a person's CURRENT OR PREVIOUS employer. A search for
one clinic returns its alumni too. Two filters handle it: before enrichment, candidates whose
current organisation name is neither the shortlist name nor the name most people at that
domain carry are dropped (free); after enrichment, the person's current organisation must
own the domain (`organization.primary_domain`) or they go to the skipped log, not the CSV.

Credentials, two transports, same endpoints:
  * oo (default since 2026-10-01): Apollo is connected in OOMOL (team bilanvadim_team), and
    calls go through `oo connector proxy apollo` with the endpoint URL. No key on this box,
    and the oo Apollo connection is read-only. `oo connector proxy` rejects array values
    in --query, so the query string rides in the endpoint URL.
  * key: APOLLO_API_KEY in the environment or ~/.hermes/.env wins when it is set. A SCOPED
    key with mixed_people/api_search + people/bulk_match is enough; never a master key (it
    can send email and buy mailboxes). The key is never printed.
APOLLO_TRANSPORT=key|oo forces one.

    apollo-pull.py health
    apollo-pull.py search --campaign <slug> [--all-functions] [--strict-titles]
    apollo-pull.py enrich --campaign <slug> --max-credits 60 [--dry-run]
    apollo-pull.py pull   --campaign <slug> --max-credits 60 [--dry-run]
"""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import difflib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


PIPE = _load("outbound_pipeline", HERE / "outbound-pipeline.py")
PACK = _load("outbound_pack", HERE / "outbound_pack.py")

BASE = (os.environ.get("APOLLO_BASE_URL") or "https://api.apollo.io/api/v1").rstrip("/")
HERMES_ENV = Path.home() / ".hermes" / ".env"
PAUSE = float(os.environ.get("APOLLO_PAUSE", "0.4"))   # seconds between calls
PER_PAGE = 100
CANDIDATES = "apollo-candidates.csv"

# The Sales Navigator export's columns, in its order, then Apollo's own.
SALES_NAV_COLUMNS = [
    "Linkedin_url", "First_name", "Last_name", "Photo_url", "Job_title", "Company_name",
    "Location", "Skills", "Experience", "Education", "Headline", "Industry", "Bio",
    "Connections", "Followers", "Company linkedin_url", "Company website_url",
    "Company description", "Company foundation_year", "Company staff_in_li",
    "Company specialities", "Company headquarter_city", "Company headquarter_country",
    "Company headquarter_geographic_area", "Company location_city",
    "Company location_country", "Company location_geographic_area",
]
APOLLO_COLUMNS = ["Source", "Apollo_id", "Apollo_last_refreshed_at", "Role_started"]
CANDIDATE_COLUMNS = ["apollo_id", "first_name", "last_name_obfuscated", "title",
                     "apollo_org", "domain", "company_name", "last_refreshed_at", "status"]


# --------------------------------------------------------------------- credentials / http

def _env(name: str) -> str:
    """Value from the process env, else from ~/.hermes/.env. Never logged."""
    v = os.environ.get(name)
    if v:
        return v.strip()
    if HERMES_ENV.exists():
        try:
            for line in HERMES_ENV.read_text(encoding="utf-8", errors="replace").splitlines():
                m = re.match(rf"^\s*{re.escape(name)}\s*=\s*(.+)$", line)
                if m:
                    return m.group(1).strip().strip('"').strip("'")
        except OSError:
            pass
    return ""


class ApolloError(Exception):
    pass


def _query(params: dict) -> str:
    """Apollo's array params go as `key[]=a&key[]=b`, scalars as plain pairs."""
    pairs = []
    for k, v in params.items():
        if isinstance(v, (list, tuple)):
            pairs += [(k, x) for x in v]
        elif v is not None:
            pairs.append((k, str(v).lower() if isinstance(v, bool) else v))
    return urllib.parse.urlencode(pairs)


def transport() -> str:
    forced = os.environ.get("APOLLO_TRANSPORT", "").strip().lower()
    if forced in ("key", "oo"):
        return forced
    if _env("APOLLO_API_KEY"):
        return "key"
    return "oo" if shutil.which("oo") else "key"


def _wait_of(det: dict, retry_after: str | None, attempt: int) -> int:
    wait = next((s.get("retry_after_seconds") for s in det.get("suggestions", [])
                 if s.get("retry_after_seconds")), None) or int(retry_after or 0)
    return min(int(wait or 30 * (attempt + 1)), 300)


def _refusal(status: int, path: str, err: dict, raw: str) -> ApolloError:
    det = err.get("error_details") or {}
    code = det.get("code") or err.get("error_code") or ""
    msg = det.get("message") or err.get("error") or err.get("message") or raw[:200]
    hint = {401: "the key is wrong or revoked",
            403: "the key lacks this endpoint: add it to the scoped key in Apollo "
                 "(Settings > Integrations > API Keys)"}.get(status, "")
    return ApolloError(f"HTTP {status} on {path}: {code} {msg}".strip()
                       + (f" ({hint})" if hint else ""))


def call_oo(path: str, params: dict | None, body: dict | None, retries: int) -> dict:
    """The same endpoint through `oo connector proxy apollo`; OOMOL injects the auth."""
    url = f"{BASE}{path}" + (f"?{_query(params)}" if params else "")
    for attempt in range(retries + 1):
        try:
            r = subprocess.run(["oo", "connector", "proxy", "apollo", "--endpoint", url,
                                "--method", "POST", "--body", json.dumps(body or {}),
                                "--json"], capture_output=True, text=True, timeout=180)
        except (OSError, subprocess.TimeoutExpired) as e:
            raise ApolloError(f"oo connector proxy apollo: {e}")
        out = (r.stdout or "") + (r.stderr or "")
        try:
            env = json.loads(out[out.index("{"):])
            res = env["data"]
            status, data = int(res.get("status") or 0), res.get("data")
        except (ValueError, KeyError, TypeError):
            hint = (" (connect Apollo at https://console.oomol.com/team/bilanvadim_team/"
                    "connections/apollo)") if "connect" in out.lower() else ""
            raise ApolloError(f"oo connector proxy apollo: {out.strip()[:300]}{hint}")
        if 200 <= status < 300:
            time.sleep(PAUSE)
            return data if isinstance(data, dict) else {}
        err = data if isinstance(data, dict) else {}
        if status == 429 and attempt < retries:
            wait = _wait_of(err.get("error_details") or {},
                            (res.get("headers") or {}).get("retry-after"), attempt)
            print(f"  … 429 rate limit, waiting {wait}s", file=sys.stderr)
            time.sleep(wait)
            continue
        raise _refusal(status, path, err, json.dumps(data)[:200])
    raise ApolloError(f"{path}: gave up after {retries} retries")


def call(path: str, params: dict | None = None, body: dict | None = None,
         retries: int = 4) -> dict:
    if transport() == "oo":
        return call_oo(path, params, body, retries)
    key = _env("APOLLO_API_KEY")
    if not key:
        raise ApolloError("APOLLO_API_KEY is not set (environment or ~/.hermes/.env), and "
                          "`oo` is not on PATH")
    url = f"{BASE}{path}" + (f"?{_query(params)}" if params else "")
    data = json.dumps(body or {}).encode()
    for attempt in range(retries + 1):
        req = urllib.request.Request(url, data=data, method="POST", headers={
            "x-api-key": key, "Content-Type": "application/json",
            "Cache-Control": "no-cache", "Accept": "application/json",
            "User-Agent": "3dlook-marketing-outbound/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                time.sleep(PAUSE)
                return json.loads(r.read().decode() or "{}")
        except urllib.error.HTTPError as e:
            raw = e.read().decode(errors="replace")
            try:
                err = json.loads(raw)
            except ValueError:
                err = {}
            if e.code == 429 and attempt < retries:
                wait = _wait_of(err.get("error_details") or {}, e.headers.get("Retry-After"),
                                attempt)
                print(f"  … 429 rate limit, waiting {wait}s", file=sys.stderr)
                time.sleep(wait)
                continue
            raise _refusal(e.code, path, err, raw)
        except urllib.error.URLError as e:
            if attempt < retries:
                time.sleep(5 * (attempt + 1))
                continue
            raise ApolloError(f"{path}: {e.reason}")
    raise ApolloError(f"{path}: gave up after {retries} retries")


# --------------------------------------------------------------------- campaign helpers

def domain_of(url: str) -> str:
    u = (url or "").strip().lower()
    if not u:
        return ""
    if "://" not in u:
        u = "http://" + u
    host = urllib.parse.urlparse(u).hostname or ""
    return host[4:] if host.startswith("www.") else host


def primary_name(name: str) -> str:
    """'FlyteHealth (Intellihealth)' -> 'FlyteHealth'; extract-people joins on it."""
    return re.sub(r"\s*\(.*$", "", name or "").strip()


def targets(cdir: Path, profile: str) -> tuple[list[dict], list[str]]:
    """The shortlist rows extract-people would keep, each with its domain."""
    rows = PACK.shortlist(cdir)
    out, skipped = [], []
    for r in rows:
        name = PIPE.pick(r, "company_name", "company")
        if not name:
            continue
        owner = PIPE.geo_profile(PIPE.pick(r, "hq_country", "country", "hq"))
        if profile and owner and owner != profile:
            continue
        f = PIPE.fit_of(r)
        if f and f not in PIPE.FIT_OK:
            continue
        dom = domain_of(PIPE.pick(r, "website", "website_url", "domain"))
        if not dom:
            skipped.append(name)
            continue
        out.append({"company_name": primary_name(name), "domain": dom, "row": r})
    return out, skipped


def similar(a: str, b: str) -> float:
    na, nb = PIPE.norm_company(a or ""), PIPE.norm_company(b or "")
    if not na or not nb:
        return 0.0
    if na in nb or nb in na:
        return 1.0
    return difflib.SequenceMatcher(None, na, nb).ratio()


def already_in_raw(cdir: Path, company: str) -> list[tuple[str, str]]:
    """(first, last) of people the Sales Navigator export already has at this company."""
    out = []
    raw = cdir / "sales-nav-raw"
    for f in sorted(raw.glob("*.csv")) if raw.exists() else []:
        if f.name.startswith("apollo"):
            continue
        for r in PIPE.read_csv(f):
            if similar(PIPE.pick(r, "Company_name", "company_name"), company) >= 0.85:
                out.append((PIPE.pick(r, "First_name", "first_name").lower(),
                            PIPE.pick(r, "Last_name", "last_name").lower()))
    return out


def matches_known(first: str, obf: str, known: list[tuple[str, str]]) -> bool:
    """'Hu***n' against a full last name: same first name, same visible head and tail."""
    m = re.match(r"^(.*?)\*+(.*)$", obf or "")
    head, tail = (m.group(1), m.group(2)) if m else (obf or "", "")
    for kf, kl in known:
        if kf == (first or "").lower() and kl.startswith(head.lower()) \
                and kl.endswith(tail.lower()):
            return True
    return False


def append_log(cdir: Path, lines: list[str]) -> None:
    p = cdir / "apollo-log.md"
    head = "" if p.exists() else (
        f"# Apollo pulls — {cdir.name}\n\nWritten by `scripts/apollo-pull.py`. "
        "Credits are Apollo's own `credits_consumed`.\n")
    with p.open("a", encoding="utf-8") as fh:
        fh.write(head + "\n" + "\n".join(lines) + "\n")


# --------------------------------------------------------------------- commands

def cmd_health(args) -> int:
    """One free search (per_page=1). Proves the key and the search scope, spends nothing."""
    try:
        res = call("/mixed_people/api_search",
                   {"q_organization_domains_list[]": ["apollo.io"], "per_page": 1})
    except ApolloError as e:
        print(f"✗ {e}", file=sys.stderr)
        return 1
    print(f"✓ Apollo answers via {transport()}: people search returned "
          f"{res.get('total_entries', '?')} people at apollo.io. Enrichment is checked on "
          "the first `enrich`.")
    return 0


def cmd_search(args) -> int:
    cdir = PIPE.campaign_dir(args.campaign)
    hyp = cdir / "hypothesis.md"
    if not hyp.exists():
        print(f"✗ no hypothesis.md in {PIPE.rel(cdir)}", file=sys.stderr)
        return 2
    text = hyp.read_text(encoding="utf-8")
    profile = PACK.frontmatter(text).get("profile") or PIPE.infer_profile(args.campaign) or ""
    titles: list[str] = []
    if not args.all_functions:
        titles, src = PACK.titles_from_hypothesis(text)
        if not titles:
            print("✗ the hypothesis names no titles (```titles block). Add them, or pass "
                  "--all-functions to pull everyone at the companies, as a Sales Navigator "
                  "pull by company would.", file=sys.stderr)
            return 2
    tg, no_domain = targets(cdir, profile)
    if not tg:
        print("✗ no shortlisted company with a website: run step 2 first", file=sys.stderr)
        return 2

    print(f"→ {len(tg)} companies · "
          + (f"{len(titles)} titles from the hypothesis" if titles else "all functions")
          + (" (strict titles)" if args.strict_titles else ""))
    rows: list[dict] = []
    for t in tg:
        params = {"q_organization_domains_list[]": [t["domain"]], "per_page": PER_PAGE}
        if titles:
            params["person_titles[]"] = titles
            if args.strict_titles:
                params["include_similar_titles"] = False
        people, page, total = [], 1, 0
        try:
            while True:
                params["page"] = page
                res = call("/mixed_people/api_search", params)
                batch = res.get("people") or []
                total = res.get("total_entries") or len(batch)
                people += batch
                if len(batch) < PER_PAGE or len(people) >= min(total, args.max_per_company):
                    break
                page += 1
        except ApolloError as e:
            print(f"✗ {t['company_name']}: {e}", file=sys.stderr)
            return 1
        people = people[: args.max_per_company]

        # The previous-employer trap, free half: keep people whose current organisation is
        # the shortlist company or the name most people at this domain carry.
        orgs = collections.Counter((p.get("organization") or {}).get("name", "") for p in people)
        dominant = orgs.most_common(1)[0][0] if orgs else ""
        known = already_in_raw(cdir, t["company_name"])
        kept = alumni = dup = 0
        for p in people:
            org = (p.get("organization") or {}).get("name", "")
            ok = similar(org, t["company_name"]) >= 0.72 or \
                (org and org == dominant and orgs[dominant] > 1)
            status = "candidate" if ok else "other-employer"
            if ok and matches_known(p.get("first_name", ""), p.get("last_name_obfuscated", ""),
                                    known):
                status = "in-sales-nav"
            kept += status == "candidate"
            alumni += status == "other-employer"
            dup += status == "in-sales-nav"
            rows.append({"apollo_id": p.get("id", ""), "first_name": p.get("first_name", ""),
                         "last_name_obfuscated": p.get("last_name_obfuscated", ""),
                         "title": p.get("title", ""), "apollo_org": org,
                         "domain": t["domain"], "company_name": t["company_name"],
                         "last_refreshed_at": p.get("last_refreshed_at", ""),
                         "status": status})
        print(f"  {t['company_name'][:34]:<34} {t['domain']:<28} found {len(people):>3}"
              f" · candidates {kept:>3}" + (f" · other employer {alumni}" if alumni else "")
              + (f" · already in Sales Nav {dup}" if dup else ""))

    PIPE.write_csv(cdir / CANDIDATES, rows, CANDIDATE_COLUMNS)
    n = sum(r["status"] == "candidate" for r in rows)
    print(f"\n✓ {PIPE.rel(cdir / CANDIDATES)}: {n} candidates to enrich "
          f"≈ {n} credits (1 per matched person; search itself was free)")
    if no_domain:
        print(f"⚠ skipped, no website in companies.csv: {', '.join(no_domain)}")
    append_log(cdir, [f"## {dt.date.today()} search",
                      f"- companies {len(tg)}, " + (f"{len(titles)} titles" if titles
                                                    else "all functions"),
                      f"- candidates {n}, other employer "
                      f"{sum(r['status'] == 'other-employer' for r in rows)}, already in "
                      f"Sales Nav {sum(r['status'] == 'in-sales-nav' for r in rows)}"])
    return 0


def experience_of(m: dict) -> str:
    hist = sorted(m.get("employment_history") or [],
                  key=lambda h: (not h.get("current"), -(int((h.get("start_date") or "0")[:4]
                                                             or 0))))
    return ", ".join(f"{h.get('title') or '?'} at {h.get('organization_name') or '?'}"
                     for h in hist if h.get("title") or h.get("organization_name"))


def sales_nav_row(m: dict, cand: dict) -> dict:
    org = m.get("organization") or {}
    cur = next((h for h in m.get("employment_history") or [] if h.get("current")), {})
    loc = ", ".join(x for x in (m.get("city"), m.get("state"), m.get("country")) if x)
    return {
        "Linkedin_url": PIPE.norm_linkedin(m.get("linkedin_url", "")) or m.get("linkedin_url", ""),
        "First_name": m.get("first_name", ""), "Last_name": m.get("last_name", ""),
        "Photo_url": "", "Job_title": m.get("title", "") or cur.get("title", ""),
        "Company_name": cand["company_name"], "Location": loc, "Skills": "",
        "Experience": experience_of(m), "Education": "", "Headline": m.get("headline", ""),
        "Industry": org.get("industry", ""), "Bio": "", "Connections": "", "Followers": "",
        "Company linkedin_url": org.get("linkedin_url", ""),
        "Company website_url": org.get("website_url", ""),
        "Company description": "", "Company foundation_year": org.get("founded_year", "") or "",
        "Company staff_in_li": org.get("estimated_num_employees", "") or "",
        "Company specialities": "", "Company headquarter_city": org.get("city", ""),
        "Company headquarter_country": org.get("country", ""),
        "Company headquarter_geographic_area": org.get("state", ""),
        "Company location_city": "", "Company location_country": "",
        "Company location_geographic_area": "",
        "Source": "apollo", "Apollo_id": m.get("id", ""),
        "Apollo_last_refreshed_at": cand.get("last_refreshed_at", ""),
        "Role_started": cur.get("start_date", "") or "",
    }


def cmd_enrich(args) -> int:
    cdir = PIPE.campaign_dir(args.campaign)
    src = cdir / CANDIDATES
    if not src.exists():
        print(f"✗ no {CANDIDATES}: run `apollo-pull.py search --campaign {args.campaign}` "
              "first", file=sys.stderr)
        return 2
    cands = [r for r in PIPE.read_csv(src) if r.get("status") == "candidate"]
    if not cands:
        print("✗ no candidates to enrich", file=sys.stderr)
        return 1
    if len(cands) > args.max_credits:
        print(f"✗ {len(cands)} candidates need up to {len(cands)} credits, over "
              f"--max-credits {args.max_credits}. Raise it, or narrow the search "
              "(--strict-titles, fewer titles).", file=sys.stderr)
        return 1
    if args.dry_run:
        print(f"(dry run) would enrich {len(cands)} people in {-(-len(cands) // 10)} calls, "
              f"≤ {len(cands)} credits")
        return 0

    out, skipped, credits = [], [], 0.0
    for i in range(0, len(cands), 10):
        chunk = cands[i:i + 10]
        try:
            res = call("/people/bulk_match",
                       {"reveal_personal_emails": False, "reveal_phone_number": False},
                       {"details": [{"id": c["apollo_id"]} for c in chunk]})
        except ApolloError as e:
            print(f"✗ {e}", file=sys.stderr)
            break
        credits += float(res.get("credits_consumed") or 0)
        by_id = {c["apollo_id"]: c for c in chunk}
        matches = res.get("matches") or []
        for c, m in zip(chunk, matches):
            if not m:
                skipped.append((c, "no match"))
                continue
            c = by_id.get(m.get("id"), c)
            org = m.get("organization") or {}
            dom = domain_of(org.get("primary_domain") or org.get("website_url") or "")
            if dom != c["domain"] and similar(org.get("name", ""), c["company_name"]) < 0.85:
                skipped.append((c, f"current employer is {org.get('name') or '?'} ({dom or '?'})"))
                continue
            if not m.get("linkedin_url"):
                skipped.append((c, "no LinkedIn URL"))
                continue
            out.append(sales_nav_row(m, c))

    if not out:
        print(f"✗ nothing to write ({len(skipped)} skipped, {credits:g} credits spent)",
              file=sys.stderr)
        return 1
    raw = cdir / "sales-nav-raw"
    raw.mkdir(exist_ok=True)
    dst = raw / f"apollo-{dt.date.today()}.csv"
    n = 2
    while dst.exists():
        dst = raw / f"apollo-{dt.date.today()}-{n}.csv"
        n += 1
    PIPE.write_csv(dst, out, SALES_NAV_COLUMNS + APOLLO_COLUMNS)
    per = collections.Counter(r["Company_name"] for r in out)
    print(f"✓ {PIPE.rel(dst)}: {len(out)} people · {credits:g} credits")
    for name, k in per.most_common():
        print(f"    {name[:40]:<40} {k}")
    if skipped:
        print(f"⚠ {len(skipped)} skipped:")
        for c, why in skipped[:8]:
            print(f"    {c['first_name']} {c['last_name_obfuscated']} ({c['title'][:40]}): {why}")
    append_log(cdir, [f"## {dt.date.today()} enrich → {dst.name}",
                      f"- written {len(out)}, skipped {len(skipped)}, credits {credits:g}"]
               + [f"  - skipped {c['first_name']} {c['last_name_obfuscated']}: {why}"
                  for c, why in skipped])
    print(f"\nnext: scripts/outbound-pipeline.py extract-people --campaign {args.campaign} "
          "--dry-run")
    return 0


def cmd_pull(args) -> int:
    rc = cmd_search(args)
    return rc if rc else cmd_enrich(args)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("health", help="free check that the key works").set_defaults(func=cmd_health)

    def search_opts(p):
        p.add_argument("--campaign", required=True)
        p.add_argument("--all-functions", action="store_true",
                       help="no title filter: everyone at the companies")
        p.add_argument("--strict-titles", action="store_true",
                       help="exact titles only (include_similar_titles=false)")
        p.add_argument("--max-per-company", type=int, default=100)

    def enrich_opts(p, need_campaign=True):
        if need_campaign:
            p.add_argument("--campaign", required=True)
        p.add_argument("--max-credits", type=int, default=100)
        p.add_argument("--dry-run", action="store_true")

    s = sub.add_parser("search", help="free: candidates + credit estimate")
    search_opts(s)
    s.set_defaults(func=cmd_search)
    e = sub.add_parser("enrich", help="paid: candidates -> sales-nav-raw/apollo-<date>.csv")
    enrich_opts(e)
    e.set_defaults(func=cmd_enrich)
    p = sub.add_parser("pull", help="search, then enrich")
    search_opts(p)
    enrich_opts(p, need_campaign=False)
    p.set_defaults(func=cmd_pull)
    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
