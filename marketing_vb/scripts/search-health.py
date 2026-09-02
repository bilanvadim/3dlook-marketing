#!/usr/bin/env python3
"""search-health.py — is the web-search backend actually answering?

WHY
---
On 2026-09-02 SearXNG returned 10 results per query up to 03:50:06 and **zero results to
every query from 03:50:10 until at least 05:08** — nineteen in a row, including the
control query `weather London` that the agent itself tried. Nothing in the pipeline
noticed. `company-researcher` kept going and produced a 26-company shortlist with every
row marked `unverified-desk`, i.e. a list assembled from model memory and presented as
research.

The instance was not down: it answered normally again later the same day. A blackout that
heals itself is worse than one that stays broken, because the only trace it leaves is a
quietly worse artifact.

So: a query whose answer we already know, run before a research round and every ~10
queries inside one. Exit code is the whole contract.

    exit 0   backend answered at least one control query with results — search away
    exit 1   backend returned nothing, errored, or is unreachable — STOP the run

A zero here is never "the sub-segment is narrow". It is the backend. Do not reformulate
the query; re-run this, and if it still fails, stop and tell Vadim.

USAGE
    scripts/search-health.py                  # exit 0/1, one summary line
    scripts/search-health.py --verbose        # per-query detail
    scripts/search-health.py --json           # machine-readable, for a runner
    scripts/search-health.py --url http://127.0.0.1:8888
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

# Queries with a guaranteed non-empty answer on any working general-web index. Two, not
# one: a single query can legitimately go empty if an engine de-indexes something, and a
# false "backend is dead" would stop a good run.
CONTROL_QUERIES = ("weather London", "wikipedia")

HERMES_ENV = Path.home() / ".hermes" / ".env"
DEFAULT_TIMEOUT = 20


def searxng_url(override: str | None = None) -> tuple[str, str]:
    """(url, where-it-came-from). Env wins, then ~/.hermes/.env, then the default.

    Only the SEARXNG_URL line is read out of the .env — that file also holds API keys and
    this script has no business touching them, let alone printing them.
    """
    if override:
        return override.rstrip("/"), "--url"
    env = os.environ.get("SEARXNG_URL")
    if env:
        return env.rstrip("/"), "$SEARXNG_URL"
    if HERMES_ENV.exists():
        try:
            for line in HERMES_ENV.read_text(encoding="utf-8", errors="replace").splitlines():
                m = re.match(r"^\s*SEARXNG_URL\s*=\s*(\S+)", line)
                if m:
                    return m.group(1).strip().rstrip("/"), "~/.hermes/.env"
        except OSError:
            pass
    return "http://127.0.0.1:8888", "default"


def probe(base: str, query: str, timeout: int) -> dict:
    """One control query. Returns {query, ok, count, error}."""
    url = f"{base}/search?" + urllib.parse.urlencode({"q": query, "format": "json"})
    req = urllib.request.Request(url, headers={"User-Agent": "search-health/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            if resp.status != 200:
                return {"query": query, "ok": False, "count": 0, "error": f"http-{resp.status}", "unresponsive_engines": []}
            payload = json.loads(resp.read().decode("utf-8", errors="replace"))
    except urllib.error.HTTPError as e:
        # 403 here usually means format=json is not in the instance's `formats:` list —
        # a config regression, not a network problem. Worth naming precisely.
        hint = "-json-format-disabled?" if e.code == 403 else ""
        return {"query": query, "ok": False, "count": 0, "error": f"http-{e.code}{hint}", "unresponsive_engines": []}
    except urllib.error.URLError as e:
        return {"query": query, "ok": False, "count": 0, "error": f"unreachable:{e.reason}", "unresponsive_engines": []}
    except json.JSONDecodeError:
        return {"query": query, "ok": False, "count": 0, "error": "non-json-response", "unresponsive_engines": []}
    except Exception as e:  # noqa: BLE001
        return {"query": query, "ok": False, "count": 0, "error": f"{type(e).__name__}:{e}", "unresponsive_engines": []}

    results = payload.get("results") or []
    # SearXNG answers 200 with an EMPTY results list when its upstream engines are
    # suspended, and names them in `unresponsive_engines`. Measured 2026-09-02 16:36 UTC,
    # while the instance looked perfectly healthy from the outside:
    #
    #   [['brave','Suspended: too many requests'], ['duckduckgo','HTTP connection error'],
    #    ['google cse','Suspended: too many requests'], ['startpage','Suspended: CAPTCHA']]
    #
    # This is THE reason the morning run went blind, and nothing surfaced it: the
    # provider's own log line ("0 results (from 0 raw, limit 10)") never mentions engines.
    # "All four engines are rate-limited, wait for the cooldown" and "the index has
    # nothing" demand opposite responses, so the field is reported, not swallowed.
    engines = [
        f"{name}: {reason}"
        for name, reason in (payload.get("unresponsive_engines") or [])
    ]
    return {
        "query": query,
        "ok": bool(results),
        "count": len(results),
        "error": "",
        "unresponsive_engines": engines,
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        prog="search-health.py",
        description="Exit 0 if the web-search backend returns results; exit 1 if it is blind.",
    )
    ap.add_argument("--url", help="SearXNG base URL (default: $SEARXNG_URL or ~/.hermes/.env)")
    ap.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    ap.add_argument("--verbose", action="store_true", help="one line per control query")
    ap.add_argument("--json", dest="as_json", action="store_true", help="machine-readable output")
    ap.add_argument("--wait", type=int, default=0, metavar="SECONDS",
                    help="poll until the backend recovers, up to SECONDS (checks every 60s)")
    args = ap.parse_args(argv)

    base, source = searxng_url(args.url)
    probes = [probe(base, q, args.timeout) for q in CONTROL_QUERIES]
    healthy = any(p["ok"] for p in probes)

    # A suspension is a cooldown, not an outage: measured 2026-09-02, the instance went
    # blind at 03:50, answered again by 17:04, and was suspended again by 19:00 under
    # nothing heavier than a dozen probes. Waiting it out beats failing a research run,
    # so --wait turns a hard stop into a delay. Polling is every 60s and no faster:
    # hammering a rate-limited engine is what extends the ban.
    if not healthy and args.wait > 0:
        import time
        deadline = time.monotonic() + args.wait
        attempt = 0
        while not healthy and time.monotonic() < deadline:
            attempt += 1
            left = int(deadline - time.monotonic())
            print(f"  … backend blind, waiting for the cooldown "
                  f"(attempt {attempt}, {left}s left)", file=sys.stderr)
            time.sleep(min(60, max(1, left)))
            probes = [probe(base, q, args.timeout) for q in CONTROL_QUERIES]
            healthy = any(p["ok"] for p in probes)

    if args.as_json:
        print(json.dumps(
            {"healthy": healthy, "backend": base, "source": source, "probes": probes},
            ensure_ascii=False,
        ))
        return 0 if healthy else 1

    if args.verbose:
        print(f"backend: {base}  (from {source})")
        for p in probes:
            mark = "✓" if p["ok"] else "✗"
            detail = f"{p['count']} results" if p["ok"] else (p["error"] or "0 results")
            print(f"  {mark} {p['query']!r:<20} {detail}")
            for eng in p.get("unresponsive_engines", []):
                print(f"      ⊘ {eng}")
        print()

    if healthy:
        best = max(p["count"] for p in probes)
        print(f"✓ search backend healthy — control query returned {best} results")
        return 0

    reasons = "; ".join(p["error"] or "0 results" for p in probes)
    suspended = sorted({e for p in probes for e in p.get("unresponsive_engines", [])})
    msg = [f"✗ SEARCH BACKEND BLIND — {base} ({reasons})."]
    if suspended:
        msg.append("  Upstream engines are refusing, so the index is not the problem:")
        msg += [f"    ⊘ {e}" for e in suspended]
        if any("too many requests" in e.lower() or "captcha" in e.lower() for e in suspended):
            msg.append("  This is a rate-limit / CAPTCHA cooldown. Waiting is the fix; retrying")
            msg.append("  faster makes it longer. Re-run this check before searching again.")
    msg.append("  STOP the research round. Do not reformulate the query: on 2026-09-02 this")
    msg.append("  state ate 19 queries and produced an unverifiable 26-company list. Tell Vadim.")
    print("\n".join(msg), file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
