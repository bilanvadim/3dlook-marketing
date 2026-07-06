#!/usr/bin/env python3
"""Hermes trend-scout collector. GitHub-only (no key needed; GITHUB_TOKEN env raises rate limits).
Outputs JSON to stdout (and optionally a file): candidates with raw metrics for scoring.
Other sources (HN, dev.to, registries) are fetched by the agent via WebFetch — they need
no auth but live outside this script so the agent can degrade gracefully per-source.
"""
import json, os, sys, time, urllib.request, urllib.parse
from datetime import datetime, timedelta, timezone

GH = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
QUERIES = [
    # (label, github search query)
    ("skills",  'topic:claude-skills OR topic:claude-code-skills OR "claude code skill" in:name,description'),
    ("agents",  'topic:claude-code-subagents OR "claude code agent" in:name,description'),
    ("plugins", 'topic:claude-code-plugin OR "claude code plugin" in:name,description'),
    ("mcp",     'topic:mcp-server'),
]
WINDOW_DAYS = int(os.environ.get("SCOUT_WINDOW_DAYS", "14"))
MIN_STARS  = int(os.environ.get("SCOUT_MIN_STARS", "15"))
PER_QUERY  = int(os.environ.get("SCOUT_PER_QUERY", "20"))

def gh_get(url):
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "hermes-trend-scout",
        **({"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}),
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())

def search(label, q):
    since = (datetime.now(timezone.utc) - timedelta(days=WINDOW_DAYS)).date().isoformat()
    out = []
    # "updated" mode caps stars at 30k: mega-repos are not "trends"
    for sort_mode, qualifier in (("stars", f"created:>{since}"), ("updated", f"pushed:>{since} stars:{MIN_STARS}..30000")):
        full_q = urllib.parse.quote(f"{q} {qualifier}")
        url = f"{GH}/search/repositories?q={full_q}&sort={sort_mode}&order=desc&per_page={PER_QUERY}"
        try:
            data = gh_get(url)
        except Exception as e:
            print(f"WARN search failed [{label}/{sort_mode}]: {e}", file=sys.stderr)
            continue
        for it in data.get("items", []):
            out.append({
                "category": label,
                "full_name": it["full_name"],
                "url": it["html_url"],
                "description": (it.get("description") or "")[:300],
                "stars": it["stargazers_count"],
                "created_at": it["created_at"],
                "pushed_at": it["pushed_at"],
                "license": (it.get("license") or {}).get("spdx_id"),
                "owner_type": it["owner"]["type"],
                "discovered_via": f"github-search/{sort_mode}",
            })
        time.sleep(2 if TOKEN else 8)  # unauthenticated search API: 10 req/min
    return out

def main():
    seen, items = set(), []
    for label, q in QUERIES:
        for it in search(label, q):
            if it["full_name"] in seen:
                continue
            seen.add(it["full_name"])
            items.append(it)
    result = {
        "run_at": datetime.now(timezone.utc).isoformat(),
        "window_days": WINDOW_DAYS,
        "count": len(items),
        "items": sorted(items, key=lambda x: -x["stars"]),
        "note": "velocity needs a previous run to diff against: store runs and compare stars by full_name",
    }
    out_path = os.environ.get("SCOUT_OUT")
    payload = json.dumps(result, ensure_ascii=False, indent=1)
    if out_path:
        open(out_path, "w").write(payload)
        print(f"wrote {out_path} ({len(items)} items)")
    else:
        print(payload)

if __name__ == "__main__":
    main()
