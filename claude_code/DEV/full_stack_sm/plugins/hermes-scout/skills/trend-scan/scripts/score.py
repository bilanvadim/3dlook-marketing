#!/usr/bin/env python3
"""Hermes trend-scout scorer. Deterministic scoring so the LLM does not have to do arithmetic.

Input:  JSON from collect.py (current run) on stdin OR --current <file>.
Optional --previous <file>: a prior run's collect.py output, to compute velocity (star deltas).
Optional --enrich <file>: JSON dict keyed by full_name with extra signals the agent gathered
        via WebFetch, e.g. {"obra/superpowers": {"installs": 752120, "hn_points": 240,
        "sources": ["github","hn","devto"], "in_official_dir": true, "awesome_listed": true}}

Output: JSON list of scored candidates (score 0..1), sorted desc, only score >= threshold.

Scoring (mirrors trend-scan SKILL.md):
  score = 0.30*velocity + 0.20*liveness + 0.25*cross_source + 0.15*adoption + 0.10*author_trust
"""
import argparse, json, sys
from datetime import datetime, timezone

TRUSTED_OWNERS = {
    "anthropics", "modelcontextprotocol", "trailofbits", "obra", "wshobson",
    "voltagent", "supabase", "cloudflare", "vercel", "getsentry", "redis",
    "microsoft", "googleapis", "pulumi", "upstash", "punkpeye", "hesreallyhim",
}

def parse_dt(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        return None

def days_since(s):
    dt = parse_dt(s)
    if not dt:
        return 9999
    return (datetime.now(timezone.utc) - dt).days

def velocity_score(stars_now, stars_prev):
    if stars_prev is None:
        return None  # unknown — handled by caller (cold start)
    delta = max(0, stars_now - stars_prev)  # weekly assumption (runs daily, diff vs ~7d ago ideally)
    pct = (delta / stars_prev) if stars_prev else 0
    if delta >= 150 or pct >= 0.15:
        return 1.0
    if delta >= 30 or pct >= 0.03:
        return 0.5
    return 0.0

def liveness_score(pushed_at, contributors):
    d = days_since(pushed_at)
    if d <= 14 and (contributors is None or contributors >= 3):
        return 1.0
    if d <= 60:
        return 0.5
    return 0.0

def cross_source_score(n_sources):
    if n_sources >= 3:
        return 1.0
    if n_sources == 2:
        return 0.6
    if n_sources == 1:
        return 0.2
    return 0.0

def adoption_score(enrich):
    if enrich.get("in_official_dir") or enrich.get("installs"):
        return 1.0
    if enrich.get("awesome_listed"):
        return 0.6
    return 0.0

def author_trust_score(full_name, owner_type, enrich):
    if "author_trust" in enrich:  # agent may override with judgment
        return float(enrich["author_trust"])
    owner = full_name.split("/", 1)[0].lower()
    if owner in TRUSTED_OWNERS or owner_type == "Organization":
        return 1.0
    return 0.2  # unknown individual; agent can bump to 0.5 via enrich if they recognize other popular repos

def score_item(it, prev_stars, enrich):
    e = enrich.get(it["full_name"], {})
    sources = set(e.get("sources", []))
    if it.get("discovered_via"):
        sources.add("github")
    vel = velocity_score(it["stars"], prev_stars)
    cold = vel is None
    vel = 0.3 if cold else vel  # cold-start neutral-ish prior so day-1 isn't all zeros
    parts = {
        "velocity": vel,
        "liveness": liveness_score(it.get("pushed_at"), e.get("contributors")),
        "cross_source": cross_source_score(len(sources)),
        "adoption": adoption_score(e),
        "author_trust": author_trust_score(it["full_name"], it.get("owner_type"), e),
    }
    score = (0.30*parts["velocity"] + 0.20*parts["liveness"] + 0.25*parts["cross_source"]
             + 0.15*parts["adoption"] + 0.10*parts["author_trust"])
    return {
        "full_name": it["full_name"], "url": it["url"], "category": it.get("category"),
        "stars": it["stars"], "license": it.get("license"),
        "score": round(score, 3), "cold_start": cold,
        "components": {k: round(v, 2) for k, v in parts.items()},
        "sources": sorted(sources),
        "description": it.get("description", "")[:200],
    }

def load(path):
    return json.load(open(path)) if path else json.load(sys.stdin)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--current"); ap.add_argument("--previous"); ap.add_argument("--enrich")
    ap.add_argument("--threshold", type=float, default=0.5)
    a = ap.parse_args()
    cur = load(a.current)
    prev = json.load(open(a.previous)) if a.previous else None
    enrich = json.load(open(a.enrich)) if a.enrich else {}
    prev_stars = {x["full_name"]: x["stars"] for x in prev["items"]} if prev else {}
    scored = [score_item(it, prev_stars.get(it["full_name"]), enrich) for it in cur["items"]]
    scored = [s for s in scored if s["score"] >= a.threshold]
    scored.sort(key=lambda x: -x["score"])
    print(json.dumps({"scored_at": datetime.now(timezone.utc).isoformat(),
                      "threshold": a.threshold, "count": len(scored),
                      "any_cold_start": any(s["cold_start"] for s in scored),
                      "items": scored}, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    main()
