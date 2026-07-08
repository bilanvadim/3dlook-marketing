#!/usr/bin/env python3
"""Hermes trend-scout → Supabase upsert. Persists scored items + per-run metrics so velocity
can be computed across runs (see scout_velocity view in sql/schema.sql).

Uses Supabase REST (PostgREST) with the SERVICE ROLE key (scout tables are RLS deny-by-default,
service role bypasses RLS). NEVER expose this key client-side; this runs server-side only (n8n/cron).

Env:
  SUPABASE_URL          e.g. https://xxxx.supabase.co
  SUPABASE_SERVICE_KEY  service_role key
Input: scored JSON (from score.py) on stdin or --scored <file>.

Idempotent: scout_items upserted on unique full_name; one scout_metrics row appended per run.
"""
import json, os, sys, argparse, urllib.request, urllib.error

URL = os.environ.get("SUPABASE_URL", "").rstrip("/")
KEY = os.environ.get("SUPABASE_SERVICE_KEY", "")

def req(method, path, body=None, prefer=None):
    if not URL or not KEY:
        raise SystemExit("SUPABASE_URL / SUPABASE_SERVICE_KEY not set — skipping DB write "
                         "(agent memory seen.md still works as fallback).")
    headers = {
        "apikey": KEY, "Authorization": f"Bearer {KEY}",
        "Content-Type": "application/json",
    }
    if prefer:
        headers["Prefer"] = prefer
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(f"{URL}/rest/v1/{path}", data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(r, timeout=30) as resp:
            txt = resp.read().decode()
            return json.loads(txt) if txt else []
    except urllib.error.HTTPError as e:
        raise SystemExit(f"Supabase {method} {path} failed: {e.code} {e.read().decode()[:300]}")

CAT_MAP = {"skill": "skill", "agent": "agent", "plugin": "plugin", "mcp": "mcp",
           "framework": "framework"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scored")
    a = ap.parse_args()
    data = json.load(open(a.scored)) if a.scored else json.load(sys.stdin)
    items = data["items"]
    if not items:
        print("nothing to upsert (empty scored set)"); return

    # 1. upsert scout_items (on_conflict=full_name). Returns rows with ids.
    item_rows = [{
        "full_name": s["full_name"],
        "category": CAT_MAP.get(s.get("category"), "other"),
        "layer": s.get("layer"),
        "url": s["url"],
        "description": s.get("description"),
        "license": s.get("license"),
        "author_trust": s["components"]["author_trust"],
    } for s in items]
    returned = req("POST", "scout_items?on_conflict=full_name",
                   item_rows, prefer="resolution=merge-duplicates,return=representation")
    id_by_name = {r["full_name"]: r["id"] for r in returned}

    # 2. append scout_metrics (one row per item per run)
    metric_rows = [{
        "item_id": id_by_name[s["full_name"]],
        "stars": s.get("stars"),
        "pushed_at": None,  # available in collect output if needed; metrics view uses stars deltas
        "sources": s.get("sources"),
        "score": s["score"],
    } for s in items if s["full_name"] in id_by_name]
    req("POST", "scout_metrics", metric_rows, prefer="return=minimal")

    print(f"upserted {len(item_rows)} items, {len(metric_rows)} metric rows")

if __name__ == "__main__":
    main()
