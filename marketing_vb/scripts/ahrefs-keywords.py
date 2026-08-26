#!/usr/bin/env python3
"""ahrefs-keywords.py — pull real keyword data for an SEO topic and write the
`keywords_raw` input the pipeline has always declared but never had.

WHY THIS EXISTS
---------------
`seo-planner` declares an input `keywords_raw` ("CSV or raw key list from
Ahrefs/SEMrush") and Phase 1 opens with "read the raw keys from the context
pack". No copy of `context-pack-builder` ever emitted that field, so Phase 1 read
nothing on every run and every article shipped with volume/difficulty as TBD. The
2026-08-25 article is the proof: its chosen primary keyword, "remote body
measurement for online fitness coaching", returns NO Ahrefs data at all, while
"online fitness coaching" is 800/mo at KD 76. Nobody could see that, because the
number never existed.

This is the producer. It writes one YAML file per topic; the context pack reads
it into `keywords_raw` and the planner clusters against real figures.

DATA NOTES, LEARNED FROM THE API RATHER THAN ASSUMED
  * `keywords` is COMMA-separated. Newline-separated silently returns zero rows
    (a 200 with an empty list), which reads exactly like "no data for this topic".
    A seed containing a comma cannot be expressed; the script refuses one instead
    of quietly truncating.
  * Any of volume / difficulty / cpc can come back null for a real keyword. Null
    means "Ahrefs has no figure", NOT zero, and the two must not be conflated when
    a planner is choosing a head term. Nulls are written as `null`, never 0.
  * A long-tail phrase having no row is a finding, not an error: it means the
    exact phrase has no measured demand. Recorded as `no_data: true`.

UNITS: plan is Standard 2022, 400,000 units/month shared with Ahrefs MCP and
Connect. Every billable request costs at least 50 units, then rows x fields. One
run is two requests. The script reports units consumed by diffing the account's
usage counter, so the cost is visible rather than assumed.

USAGE
    scripts/ahrefs-keywords.py "<seed topic>" [--slug <slug>] [--country us]
                               [--limit 40] [--out <path>] [--dry-run] [--json]
Exit: 0 ok · 2 refused (reason on stdout) · 3 broken setup / API error.
"""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.ahrefs.com"
SECRETS = os.path.expanduser("~/.config/ai-agent-stack/secrets.env")
OVERVIEW_COLS = "keyword,volume,difficulty,cpc,traffic_potential,parent_topic,intents"
IDEA_COLS = "keyword,volume,difficulty,cpc"


def load_key() -> str:
    """Env first, then the canonical secrets file (SECRETS.md calls it the source
    of truth; the five files install.sh writes are generated copies)."""
    k = os.environ.get("AHREFS_API_KEY")
    if k:
        return k.strip()
    try:
        for line in open(SECRETS, encoding="utf-8"):
            if line.startswith("AHREFS_API_KEY="):
                return line.split("=", 1)[1].strip().strip("\"'")
    except OSError:
        pass
    sys.exit("⚠️ нет AHREFS_API_KEY (ни в env, ни в ~/.config/ai-agent-stack/secrets.env).\n"
             "Ключ создаётся в Ahrefs → Account settings → API keys. Скажи Вадиму, не выдумывай цифры.")


def call(key: str, path: str, params: dict):
    url = f"{API}{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(
        url, headers={"Authorization": f"Bearer {key}", "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")[:300]
        if e.code == 401:
            sys.exit("⚠️ Ahrefs: 401 Unauthorized — ключ недействителен или отозван.")
        if e.code == 429:
            sys.exit("⚠️ Ahrefs: 429 — юниты за месяц исчерпаны или слишком часто. "
                     "Повтори позже; цифры НЕ выдумывай.")
        sys.exit(f"⚠️ Ahrefs {e.code}: {body}")
    except Exception as e:                                  # network / timeout
        sys.exit(f"⚠️ Ahrefs недоступен: {type(e).__name__}: {e}")


def units_used(key: str):
    d = call(key, "/v3/subscription-info/limits-and-usage", {})
    lu = d.get("limits_and_usage", {})
    return lu.get("units_usage_workspace"), lu.get("units_limit_workspace"), lu.get("subscription")


def variants(seed: str):
    """Seed plus a few honest shortenings, so a zero-data long tail is visible
    NEXT TO the head term that does have demand. Deliberately mechanical: the
    judgement about which to target belongs to seo-planner, not to this script."""
    words = seed.split()
    out = [seed]
    for n in (4, 3, 2):
        if len(words) > n:
            out.append(" ".join(words[:n]))
            out.append(" ".join(words[-n:]))
    seen, uniq = set(), []
    for w in out:
        w = w.strip()
        if w and w.lower() not in seen:
            seen.add(w.lower())
            uniq.append(w)
    return uniq[:8]


def rows_of(payload):
    return payload.get("keywords") or []


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("seed", help="тема статьи, как её сформулировал Вадим")
    ap.add_argument("--slug", default="")
    ap.add_argument("--country", default="us")
    ap.add_argument("--limit", type=int, default=40, help="сколько идей тянуть (default 40)")
    ap.add_argument("--out", default="")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--json", action="store_true", help="печатать JSON вместо таблицы")
    a = ap.parse_args(argv)

    seed = a.seed.strip()
    if not seed:
        print("нужна тема: ahrefs-keywords.py \"<seed topic>\"")
        return 2
    if "," in seed:
        # The API takes a comma-separated list, so a comma inside one keyword is
        # unrepresentable. Refusing beats silently splitting the topic in two.
        print("⚠️ в теме есть запятая — API разделяет ключи запятой, так что тему с "
              "запятой передать нельзя. Перефразируй без неё.")
        return 2

    slug = a.slug or re.sub(r"[^a-z0-9]+", "-", seed.lower()).strip("-")[:80]
    today = _dt.date.today().isoformat()
    out = a.out or f"workspace/seo/_keywords/{today}-{slug}.yaml"

    if a.dry_run:
        print(f"[dry-run] seed={seed!r} country={a.country} limit={a.limit}")
        print(f"[dry-run] 2 запроса к Ahrefs (overview + matching-terms), ~100+ юнитов")
        print(f"[dry-run] записал бы {out}")
        return 0

    key = load_key()
    before, limit, plan = units_used(key)

    ov = call(key, "/v3/keywords-explorer/overview",
              {"country": a.country, "keywords": ",".join(variants(seed)), "select": OVERVIEW_COLS})
    # Ideas are pulled against the best HEAD term, not the full topic. A marketing
    # topic is a sentence ("Remote Body Measurement for Online Fitness Coaching
    # Programs") and matching-terms against it returns zero rows every time — the
    # tool's whole idea half would look broken while actually being mis-asked.
    # So: take the highest-volume variant that Ahrefs has data for; if none has
    # data, fall back to the last three words, which is where the head noun of an
    # English topic usually sits.
    # Pick the LONGEST variant that has data, not the highest-volume one. Volume
    # rewards generality and throws the topic away: for this repo's first real
    # run, "coaching programs" (500/mo) beat "online fitness coaching programs"
    # (100/mo) and returned real-estate and life-coaching ideas. Specificity is
    # what a cluster needs; the planner can always widen, but it cannot recover a
    # vertical the seed already lost.
    scored = [r for r in rows_of(ov) if isinstance(r.get("volume"), int)]
    if scored:
        idea_seed = max(scored, key=lambda r: (len(r["keyword"].split()), r["volume"]))["keyword"]
    else:
        idea_seed = " ".join(seed.split()[-3:])
    ideas = call(key, "/v3/keywords-explorer/matching-terms",
                 {"country": a.country, "keywords": idea_seed, "select": IDEA_COLS,
                  "limit": str(a.limit), "order_by": "volume:desc", "match_mode": "terms"})

    after, _l, _p = units_used(key)
    spent = (after - before) if (isinstance(after, int) and isinstance(before, int)) else None

    got = {r.get("keyword", "").lower(): r for r in rows_of(ov)}
    seed_row = got.get(seed.lower())

    doc = {
        "seed": seed, "slug": slug, "country": a.country, "pulled": today,
        "source": "ahrefs api v3 (keywords-explorer)", "plan": plan,
        "seed_has_data": bool(seed_row),
        "seed_metrics": seed_row or None,
        "variants": [got.get(v.lower()) or {"keyword": v, "no_data": True} for v in variants(seed)],
        "idea_seed": idea_seed,
        "ideas": rows_of(ideas),
        "units_spent": spent,
    }

    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write("# Generated by scripts/ahrefs-keywords.py — real Ahrefs figures, do not hand-edit.\n")
        f.write("# null volume/difficulty means Ahrefs has NO figure for that phrase; it is not zero.\n")
        json.dump(doc, f, ensure_ascii=False, indent=2)
        f.write("\n")

    if a.json:
        print(json.dumps(doc, ensure_ascii=False, indent=2))
        return 0

    def cell(r, k):
        v = r.get(k)
        return "—" if v is None else str(v)

    print(f"📊 Ahrefs · {plan} · страна {a.country}")
    if seed_row:
        print(f"✅ seed «{seed}»: vol={cell(seed_row,'volume')} "
              f"kd={cell(seed_row,'difficulty')} tp={cell(seed_row,'traffic_potential')} "
              f"parent={cell(seed_row,'parent_topic')}")
    else:
        print(f"⚠️  seed «{seed}» — данных НЕТ. Точная фраза не имеет измеренного спроса. "
              "Это не ошибка: выбери head-термин из вариантов/идей ниже и скажи об этом в plan.md.")
    print("\nВарианты головы:")
    for r in doc["variants"]:
        mark = " (нет данных)" if r.get("no_data") else ""
        print(f"  {r.get('keyword',''):45} vol={cell(r,'volume'):>7} kd={cell(r,'difficulty'):>4}{mark}")
    print(f"\nИдеи по head-термину «{idea_seed}» ({len(doc['ideas'])}), по убыванию объёма:")
    for r in doc["ideas"][:20]:
        print(f"  {cell(r,'keyword'):45} vol={cell(r,'volume'):>7} kd={cell(r,'difficulty'):>4}")
    if len(doc["ideas"]) > 20:
        print(f"  … ещё {len(doc['ideas'])-20} в файле")
    print(f"\n💾 {out}")
    if spent is not None:
        pct = (after / limit * 100) if limit else 0
        print(f"⚙️  юнитов потрачено: {spent} · использовано за месяц {after}/{limit} ({pct:.1f}%)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
