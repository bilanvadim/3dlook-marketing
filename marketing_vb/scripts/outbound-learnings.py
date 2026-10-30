#!/usr/bin/env python3
"""outbound-learnings.py — pooled step-9 numbers across every outbound campaign, and the
monthly loop that turns them into rules the agents read.

WHY
---
Vadim, 2026-10-30: «а ти робиш якісь висновки і покращуєш систему на основі даних по
кампаніям?» The honest answer was no. Replies were pulled, classified and reported every
night, but step 9 had run once (2026-09-02, five July/Aug campaigns, still `awaiting_review`),
18 of 29 campaign folders had replies nobody analysed, the pooled analysis booked for
2026-10-26 never ran, and there was no file a hypothesis or a message could learn from.
«роби всі кроки»: analyse now, keep one learnings file the agents must read, and repeat it
monthly with Vadim approving the changes.

Per campaign almost nothing is significant (≤ 15 replies each), so the analysis is POOLED:
every number here is a sum over campaigns, cut by one dimension at a time, with its
denominator and a 95% Wilson interval. The script only counts. Judgment (what the numbers
mean, what to change) belongs to campaign-analyzer in pooled mode and to Vadim.

DATA
----
- Funnel per campaign: the last nightly Closely snapshot (`~/.hermes/outbound-stats/`,
  written by `closely-pull.py pull-all --stats`); folder grouping, sender and positives come
  from outbound-responses-daily.py, imported so the rules cannot drift.
- Message step: the Closely flow is a tree, a message's rank is the number of message steps
  on its path (same walk as outbound-responses-daily.step_replies, here with sends too).
- Per person: `closelyhq-import.csv` (who was sent) joined to `people-approved.csv` /
  `people-validated.csv` (lane, priority, title) and `responses-raw.csv` +
  `responses-classified.csv` (who replied, to which message, with what). Closely gives no
  per-person acceptance, so person-level rates are per person CONTACTED, not per accepted.

USAGE
    outbound-learnings.py build [--snapshot PATH] [--min-age 21]
        → workspace/outbound/learnings/data-YYYY-MM-DD.md + .json
    outbound-learnings.py monthly [--notify] [--dry-run]
        cron, the 1st of the month: build, then enqueue `/outbound learnings <data date>`
    outbound-learnings.py check [--proposals FILE]
        gate: learnings.md has its sections and every % carries its denominator
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import math
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import date, datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
MVB = HERE.parent
CAMPAIGNS = MVB / "workspace" / "outbound" / "campaigns"
OUT_DIR = MVB / "workspace" / "outbound" / "learnings"
LEARNINGS = MVB / "workspace" / "outbound" / "learnings.md"
MVB_RUN = Path(os.environ.get("OUTBOUND_DAILY_MVB_RUN")
               or Path.home() / "3dlook-marketing" / "hermes_agent" / "ops" / "mvb-run.py")
LOG = Path.home() / ".hermes" / "logs" / "outbound-learnings.log"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


D = _load("outbound_daily", HERE / "outbound-responses-daily.py")
PACK = _load("outbound_pack", HERE / "outbound_pack.py")
OP, REG = D.OP, D.REG

POSITIVE = set(D.POSITIVE)                      # interested, question, referral
MIN_AGE = 21                                    # days since the Closely campaign started
MIN_SENT_SHARE = 0.8                            # invites sent / contacts loaded

# Read in this order; the first match names the segment. Slugs carry the segment, the three
# July campaigns without a folder only have their Closely name.
SEGMENTS = [
    ("insurance underwriting", r"insurance"),
    ("employer obesity care", r"employer"),
    ("longevity clinics (Everlab-like)", r"everlab"),
    ("clinical obesity care", r"bariatric|obesity-medicine|cardiometabolic|virta"),
    ("digital fitness / wellness apps", r"fitness|erakulis|sport"),
    ("online pharmacy", r"pharma"),
    ("men's health", r"mens-health"),
    ("GLP-1 / weight-loss telehealth", r"telehealth|weight|options-medical|latam-health"),
]
SENIORITY = [
    ("C-level / founder", r"\bchief\b|\bc[efmotp]o\b|\bcmio\b|\bcco\b|founder|\bowner\b|president|"
                          r"managing director|\bmd\b(?! ?phd)|general manager|managing partner"),
    ("VP", r"\bvp\b|vice president|\bsvp\b|\bevp\b"),
    ("director / head", r"director|\bhead\b"),
    ("manager / lead", r"manager|\blead\b|principal"),
]


# ----------------------------------------------------------------------------- utils

def read_csv(p: Path) -> list[dict]:
    return D.read_csv(p)


def wilson(k: int, n: int) -> tuple[float, float]:
    if not n:
        return 0.0, 0.0
    z, p = 1.96, k / n
    den = 1 + z * z / n
    mid = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return max(0.0, mid - half), min(1.0, mid + half)


def rate(k, n, ci: bool = True) -> str:
    """`k/n (x%)`, plus `[lo–hi]` — a percent never travels without its denominator."""
    if not isinstance(k, (int, float)) or not n:
        return "—"
    s = f"{k}/{n} ({100 * k / n:.1f}%)"
    if ci:
        lo, hi = wilson(int(k), int(n))
        s += f" [{100 * lo:.0f}–{100 * hi:.0f}]"
    return s


def segment_of(text: str) -> str:
    t = text.lower()
    return next((name for name, rx in SEGMENTS if re.search(rx, t)), "other")


def seniority_of(title: str) -> str:
    t = (title or "").lower()
    for name, rx in SENIORITY:
        if re.search(rx, t):
            return name
    return "individual / other"


def norm_priority(p: str) -> str:
    m = re.search(r"\d", p or "")
    return f"P{m.group(0)}" if m else "—"


def frontmatter(cdir: Path) -> dict:
    h = cdir / "hypothesis.md"
    if not h.exists():
        return {}
    text = h.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    out = {}
    for line in (m.group(1).splitlines() if m else []):
        k, _, v = line.partition(":")
        if v and not line.startswith(" "):
            out[k.strip()] = v.strip()
    return out


def step_funnel(rows: list[dict]) -> dict:
    """Sends and replies per rank: invite, M1, M2 (M3+ folded into m3)."""
    out = {k: {"sent": 0, "replied": 0} for k in ("invite", "m1", "m2", "m3")}
    for r in rows:
        steps = r.get("steps") or []
        ids = {s.get("id") for s in steps}
        kids: dict = defaultdict(list)
        for s in steps:
            kids[s.get("prev")].append(s)
        stack = [(s, 0) for s in steps if s.get("prev") not in ids]
        seen: set = set()
        while stack:
            s, n = stack.pop()
            if s.get("id") in seen:
                continue
            seen.add(s.get("id"))
            typ = s.get("type") or ""
            if typ == "message":
                n += 1
                key = {1: "m1", 2: "m2"}.get(n, "m3")
                out[key]["sent"] += s.get("message_sent") or 0
                out[key]["replied"] += s.get("message_replied") or 0
            elif typ.startswith("connection"):
                out["invite"]["sent"] += s.get("connection_sent") or 0
                out["invite"]["replied"] += s.get("message_replied") or 0
            stack += [(k, n) for k in kids.get(s.get("id"), [])]
    return out


# -------------------------------------------------------------------------- campaigns

def latest_snapshot() -> Path:
    snaps = sorted(D.STATS_DIR.glob("20??-??-??.json"))
    if not snaps:
        sys.exit(f"✗ no snapshot in {D.STATS_DIR} (closely-pull.py pull-all --stats)")
    return snaps[-1]


def campaign_units(snap: dict, as_of: date, min_age: int) -> list[dict]:
    rows = [r for r in snap["campaigns"] if "error" not in r and r.get("status") != "template"]
    units = []
    for u in D.stat_units(rows):
        folder = u["folder"]
        fm = frontmatter(CAMPAIGNS / folder) if folder else {}
        names = " + ".join(r["name"] for r in u["rows"])
        created = min(r["created_at"] for r in u["rows"])
        f = D.funnel(u["rows"])
        known = u["profile"] in D.PROFILE_NAMES
        age = (as_of - date.fromisoformat(created)).days
        sent_share = (f["sent"] or 0) / f["contacts"] if f["contacts"] else 0
        if not known:
            state = "excluded"
            why = "sender account is not one of the five pipeline profiles (wrist outreach, warm-up)"
        elif age < min_age or sent_share < MIN_SENT_SHARE:
            state = "immature"
            why = f"{age} days old, {100 * sent_share:.0f}% of contacts invited"
        else:
            state, why = "mature", ""
        cl_rows = read_csv(CAMPAIGNS / folder / D.CLASSIFIED) if folder else []
        cats = Counter()
        for p, rs in _by_person(cl_rows).items():
            cs = {(r.get("category") or "").strip() for r in rs}
            cats[next((c for c in ("interested", "question", "referral") if c in cs),
                      sorted(cs)[0] if cs else "other/unclear")] += 1
        rc = str(fm.get("referral_call", "")).lower()
        q_rule = (rc in ("yes", "true", "required")) if rc else (fm.get("created", "")[:10] >= "2026-10-07")
        units.append({
            "key": folder or "closely:" + u["rows"][0]["closely_id"],
            "folder": folder, "closely": names, "created": created, "age_days": age,
            "profile": u["profile"], "market": fm.get("market") or "",
            "segment": segment_of(folder or names),
            "cohort": cohort_of(created, folder, q_rule),
            "m1_question_rule": q_rule, "state": state, "why": why,
            "funnel": f, "steps": step_funnel(u["rows"]),
            "positives": u["positives"], "categories": dict(cats),
        })
    return sorted(units, key=lambda x: x["created"])


def cohort_of(created: str, folder: str, q_rule: bool) -> str:
    if created < "2026-07-21":
        return "A · Jul 7–16, before the agent pipeline"
    if created < "2026-09-01":
        return "B · Jul 21–Aug 11, agent pilot"
    if not q_rule:
        return "C · Sep 12–Oct 6, pipeline v2 (gates, lanes, cards)"
    return "D · from Oct 7, question in M1 + call in M2"


def _by_person(rows: list[dict]) -> dict:
    out: dict = defaultdict(list)
    for r in rows:
        out[D.person_of(r)].append(r)
    return out


# ----------------------------------------------------------------------------- people

def people_rows(units: list[dict]) -> tuple[list[dict], list[str]]:
    """One row per person contacted in a mature campaign that kept its import CSV."""
    out, missing = [], []
    for u in units:
        if u["state"] != "mature" or not u["folder"]:
            continue
        cdir = CAMPAIGNS / u["folder"]
        imp = read_csv(cdir / "closelyhq-import.csv")
        loaded = u["funnel"]["contacts"] or 0
        # The import file must be the list Closely got. 2026-07-31 UK kept 92 rows of its two
        # Closely campaigns' 297 contacts; Israel kept 215 rows of which 130 were loaded.
        # Either way the denominator would be wrong, so such a campaign stays funnel-only.
        if not imp or not loaded or not 0.9 <= len(imp) / loaded <= 1.1:
            missing.append(f"{u['folder']} (import {len(imp)} rows, Closely {loaded} contacts)")
            continue
        attrs: dict = {}
        for name in ("people-validated.csv", "people-approved.csv"):    # approved wins
            for r in read_csv(cdir / name):
                for k in _keys(r):
                    attrs[k] = r
        raw = read_csv(cdir / D.RAW)
        cl = D.Classified(read_csv(cdir / D.CLASSIFIED))
        replies: dict = defaultdict(list)
        for r in raw:
            for k in _keys(r):
                replies[k].append(r)
        seen = set()
        for r in imp:
            ks = _keys(r)
            if not ks or ks[0] in seen:
                continue
            seen.add(ks[0])
            a = next((attrs[k] for k in ks if k in attrs), {})
            rr = next((replies[k] for k in ks if replies.get(k)), [])
            cats = [((cl.find(x) or {}).get("category") or "unclassified").strip() for x in rr]
            first_step = min((int(x.get("which_message_replied_to") or 1) for x in rr), default=0)
            title = r.get("title") or a.get("title") or ""
            m1 = r.get("message_1") or ""
            out.append({
                "campaign": u["folder"], "cohort": u["cohort"], "segment": u["segment"],
                "profile": u["profile"],
                "lane": (a.get("recommended_message_angle") or a.get("message_angle")
                         or "—").strip().lower() or "—",
                "priority": norm_priority(a.get("priority", "")),
                "seniority": seniority_of(title), "function": PACK.bucket_of(title),
                "m1_chars": len(m1), "m1_question": "?" in m1,
                "replied": bool(rr), "first_step": first_step,
                "positive": any(c in POSITIVE for c in cats),
                "category": next((c for c in ("interested", "question", "referral") if c in cats),
                                 cats[0] if cats else ""),
                "title": title, "company": r.get("company") or a.get("company_name") or "",
                "summary": next(((cl.find(x) or {}).get("summary") or "" for x in rr), ""),
            })
    return out, missing


def _keys(r: dict) -> list[str]:
    ks = []
    for col in ("linkedin_url", "person_linkedin_url"):
        v = (r.get(col) or "").strip()
        if v and "linkedin.com" in v:
            ks.append("li:" + REG.norm_linkedin(v))
    first, last = (r.get("first_name") or "").strip().lower(), (r.get("last_name") or "").strip().lower()
    full = (r.get("full_name") or f"{first} {last}").strip().lower()
    if full:
        ks.append("name:" + re.sub(r"\s+", " ", full))
    return ks


# ----------------------------------------------------------------------------- tables

def sum_funnel(us: list[dict]) -> dict:
    t = defaultdict(int)
    for u in us:
        f, s = u["funnel"], u["steps"]
        for k in ("contacts", "sent", "acc", "replied"):
            t[k] += f[k] or 0
        t["positives"] += u["positives"] or 0
        t["pos_known_acc"] += (f["acc"] or 0) if u["positives"] is not None else 0
        for step in ("invite", "m1", "m2", "m3"):
            t[f"{step}_sent"] += s[step]["sent"]
            t[f"{step}_rep"] += s[step]["replied"]
    return dict(t)


def funnel_table(groups: dict[str, list[dict]], label: str) -> list[str]:
    out = [f"| {label} | campaigns | accepted / invites | replied / accepted | positive / accepted* |",
           "|---|---|---|---|---|"]
    for name, us in groups.items():
        t = sum_funnel(us)
        out.append(f"| {name} | {len(us)} | {rate(t['acc'], t['sent'])} | "
                   f"{rate(t['replied'], t['acc'])} | {rate(t['positives'], t['pos_known_acc'])} |")
    return out


def step_table(groups: dict[str, list[dict]], label: str) -> list[str]:
    out = [f"| {label} | replies to invite | M1: replied / sent | M2: replied / sent | "
           "share of replies after M2 |", "|---|---|---|---|---|"]
    for name, us in groups.items():
        t = sum_funnel(us)
        tot = t["invite_rep"] + t["m1_rep"] + t["m2_rep"] + t["m3_rep"]
        out.append(f"| {name} | {t['invite_rep']} | {rate(t['m1_rep'], t['m1_sent'])} | "
                   f"{rate(t['m2_rep'], t['m2_sent'])} | {rate(t['m2_rep'] + t['m3_rep'], tot, False)} |")
    return out


def people_table(rows: list[dict], dim: str, label: str, min_n: int = 1) -> list[str]:
    g: dict = defaultdict(list)
    for r in rows:
        g[r[dim]].append(r)
    out = [f"| {label} | contacted | replied / contacted | positive / contacted |",
           "|---|---|---|---|"]
    for name, rs in sorted(g.items(), key=lambda kv: -len(kv[1])):
        if len(rs) < min_n:
            continue
        rep = sum(r["replied"] for r in rs)
        pos = sum(r["positive"] for r in rs)
        out.append(f"| {name} | {len(rs)} | {rate(rep, len(rs))} | {rate(pos, len(rs))} |")
    return out


def group(us: list[dict], key) -> dict[str, list[dict]]:
    g: dict = defaultdict(list)
    for u in us:
        g[key(u)].append(u)
    return dict(sorted(g.items()))


EMAIL = re.compile(r"[\w.+-]+@[\w-]+(\.[\w-]+)+")


def repliers(units: list[dict]) -> list[dict]:
    """One row per person who replied, from the classifier's file, title from the raw pull."""
    out = []
    for u in units:
        cdir = CAMPAIGNS / u["folder"]
        raw = _by_person(read_csv(cdir / D.RAW))
        titles: dict = {}
        for name in ("closelyhq-import.csv", "people-validated.csv", "people-approved.csv"):
            for r in read_csv(cdir / name):
                for k in _keys(r):
                    if r.get("title"):
                        titles[k] = r["title"]
        for p, rs in _by_person(read_csv(cdir / D.CLASSIFIED)).items():
            cats = [(r.get("category") or "").strip() for r in rs]
            cat = next((c for c in ("interested", "question", "referral") if c in cats), cats[0])
            rr = raw.get(p, [])
            title = next((x.get("title") for x in rr if x.get("title")), "") or next(
                (titles[k] for x in rs + rr for k in _keys(x) if k in titles), "")
            out.append({"campaign": u["folder"], "category": cat, "title": title,
                        "company": rs[0].get("company") or next((x.get("company_name") for x in rr), ""),
                        "step": min((int(x.get("which_message_replied_to") or 1) for x in rr), default=1),
                        "summary": EMAIL.sub("[email]", next(
                            (r.get("summary") or "" for r in rs if r.get("category") == cat), ""))})
    return sorted(out, key=lambda r: (r["campaign"], r["category"]))


def m1_len_bucket(n: int) -> str:
    return ("< 350" if n < 350 else "350–449" if n < 450 else "450–549" if n < 550 else "550+")


def render(snap: dict, units: list[dict], people: list[dict], missing: list[str],
           min_age: int) -> str:
    mature = [u for u in units if u["state"] == "mature"]
    immature = [u for u in units if u["state"] == "immature"]
    excluded = [u for u in units if u["state"] == "excluded"]
    L = [f"# Outbound pooled numbers — snapshot {snap['pulled_at'][:10]}", "",
         f"<!-- generated by scripts/outbound-learnings.py build on {date.today()}; "
         "numbers only, no judgment. Do not edit by hand: re-run the script. -->", "",
         "## Scope", "",
         f"- Closely snapshot `{snap['pulled_at']}`, campaigns created since {snap['since']}.",
         f"- **Mature** (≥ {min_age} days old and ≥ {int(MIN_SENT_SHARE * 100)}% of contacts invited): "
         f"{len(mature)} campaigns. **Immature**: {len(immature)}. **Excluded**: {len(excluded)} "
         "(not the five pipeline senders).",
         "- `[lo–hi]` is the 95% Wilson interval in percent. Two rates whose intervals overlap are "
         "not shown to differ.",
         "- *Positive* = interested + question + referral people in `responses-classified.csv`. "
         "Campaigns without a folder (cohort A) have no classified replies, so positive/accepted "
         "is computed only over campaigns that have them.",
         "- Person-level tables count people **contacted** (rows of `closelyhq-import.csv`); "
         "Closely gives no per-person acceptance.", ""]
    if missing:
        L += [f"- Mature, funnel only (no import CSV that matches what Closely loaded): "
              + ", ".join(f"`{m}`" for m in missing), ""]

    L += ["## 1. Funnel by cohort", ""] + funnel_table(group(mature, lambda u: u["cohort"]), "cohort")
    L += ["", "## 2. Funnel by sender", ""] + funnel_table(
        group(mature, lambda u: u["profile"]), "sender")
    L += ["", "## 3. Funnel by segment", ""] + funnel_table(group(mature, lambda u: u["segment"]), "segment")
    L += ["", "## 4. Which message gets the reply", ""] + step_table(
        group(mature, lambda u: u["cohort"]), "cohort")
    L += ["", "### Same, every campaign with the Oct-7 rule (immature included, read as early signal)", ""]
    L += step_table(group([u for u in units if u["state"] != "excluded"],
                          lambda u: "question-in-M1 rule" if u["m1_question_rule"] else "before the rule"),
                    "rule")

    L += ["", "## 5. Per campaign (mature)", "",
          "| campaign | sender | segment | accepted / invites | replied / accepted | positive | invite·M1·M2 replies |",
          "|---|---|---|---|---|---|---|"]
    for u in mature:
        f, s = u["funnel"], u["steps"]
        L.append(f"| {u['folder'] or u['closely']} | {u['profile']} | {u['segment']} | "
                 f"{rate(f['acc'], f['sent'], False)} | {rate(f['replied'], f['acc'], False)} | "
                 f"{'—' if u['positives'] is None else u['positives']} | "
                 f"{s['invite']['replied']}·{s['m1']['replied']}·{s['m2']['replied'] + s['m3']['replied']} |")

    rep = [r for r in people if r["replied"]]
    L += ["", f"## 6. People contacted in mature campaigns: {len(people)}, replied {len(rep)}", ""]
    lanes = Counter(r["lane"] for r in people)
    for r in people:
        r["lane_g"] = r["lane"] if lanes[r["lane"]] >= 30 else "other lanes (< 30 people each)"
    L += ["### By lane (message angle)", "",
          "`referral` = people the validator judged not to be the buyer; their Message 1 asks who "
          "owns the topic, and a «talk to X» answer is classified `referral`, which counts as positive.",
          ""] + people_table(people, "lane_g", "lane")
    L += ["", "### By seniority (title)", ""] + people_table(people, "seniority", "seniority")
    L += ["", "### By function (title, outbound_pack.bucket_of)", ""] + people_table(people, "function", "function", 10)
    L += ["", "### By priority tier (icp-validator)", ""] + people_table(people, "priority", "priority")
    for r in people:
        r["m1_len"] = m1_len_bucket(r["m1_chars"])
    L += ["", "### By Message 1 length (characters)", ""] + people_table(people, "m1_len", "M1 length")
    L += ["", "### By cohort (person level)", ""] + people_table(people, "cohort", "cohort")

    cats = Counter()
    for u in mature:
        if u["folder"]:
            cats.update(u["categories"])
    tot = sum(cats.values())
    L += ["", f"## 7. Reply categories (people, mature campaigns with a folder): {tot}", "",
          "| category | people |", "|---|---|"]
    L += [f"| {c} | {rate(n, tot, False)} |" for c, n in cats.most_common()]

    repl = repliers([u for u in mature if u["folder"]])
    L += ["", "## 8. Positive replies (title · company · campaign · step · classifier summary)", ""]
    for r in (r for r in repl if r["category"] in POSITIVE):
        L.append(f"- **{r['category']}** · {r['title'] or '?'} · {r['company'] or '?'} · "
                 f"`{r['campaign']}` · M{r['step']} — {D.short(r['summary'], 220)}")
    L += ["", "## 9. Everything else people said (decline, maybe-later, negative, unclear)", ""]
    for r in (r for r in repl if r["category"] not in POSITIVE):
        L.append(f"- {r['category']} · {r['title'] or '?'} · `{r['campaign']}` · M{r['step']} — "
                 f"{D.short(r['summary'], 200)}")

    L += ["", "## 10. Immature campaigns (next round)", "",
          "| campaign | sender | started | state | accepted / invites | replied / accepted |",
          "|---|---|---|---|---|---|"]
    for u in immature:
        f = u["funnel"]
        L.append(f"| {u['folder'] or u['closely']} | {u['profile']} | {u['created']} | {u['why']} | "
                 f"{rate(f['acc'], f['sent'], False)} | {rate(f['replied'], f['acc'], False)} |")
    if excluded:
        L += ["", "Excluded: " + "; ".join(f"{u['closely']} ({u['profile']})" for u in excluded)]
    return "\n".join(L) + "\n"


def cmd_build(args) -> int:
    path = Path(args.snapshot) if args.snapshot else latest_snapshot()
    snap = json.loads(path.read_text(encoding="utf-8"))
    as_of = date.fromisoformat(snap["pulled_at"][:10])
    units = campaign_units(snap, as_of, args.min_age)
    people, missing = people_rows(units)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stem = OUT_DIR / f"data-{as_of}"
    md = render(snap, units, people, missing, args.min_age)
    stem.with_suffix(".md").write_text(md, encoding="utf-8")
    keep = ("campaign", "cohort", "segment", "profile", "lane", "priority", "seniority",
            "function", "m1_chars", "m1_question", "replied", "first_step", "positive", "category")
    stem.with_suffix(".json").write_text(json.dumps({
        "snapshot": str(path), "pulled_at": snap["pulled_at"], "min_age": args.min_age,
        "built_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "campaigns": units, "people": [{k: r[k] for k in keep} for r in people],
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    m = [u for u in units if u["state"] == "mature"]
    t = sum_funnel(m)
    print(f"✓ {stem.with_suffix('.md').relative_to(MVB)} ({len(md.encode()):,} bytes)")
    print(f"  mature {len(m)} · immature {sum(u['state'] == 'immature' for u in units)} · "
          f"excluded {sum(u['state'] == 'excluded' for u in units)} · people {len(people)}")
    print(f"  pooled: accepted {rate(t['acc'], t['sent'])} · replied {rate(t['replied'], t['acc'])}")
    return 0


# ---------------------------------------------------------------------------- check

REQUIRED = ("## How to use", "## Hypotheses", "## People", "## Messages", "## Open questions",
            "## Change log")
# A percent inside "(12.8%)", "[3–7]" or "12.6–12.8%" already sits next to its k/n; the
# lookbehind skips it, "." included so "12.8%" is not read as a bare "8%". "95% Wilson
# interval" is a confidence level, not a rate.
BARE_PCT = re.compile(r"(?<![\d/(\[–.-])\b\d{1,3}(?:\.\d)?%(?!\s*(?:Wilson|interval|CI\b|confidence))")


def check_text(text: str, name: str) -> list[str]:
    bad = []
    for i, line in enumerate(text.splitlines(), 1):
        if line.lstrip().startswith(("|", "<!--")):
            continue
        for m in BARE_PCT.finditer(line):
            ctx = line[max(0, m.start() - 40):m.start()]
            if not re.search(r"\d+\s*/\s*\d+|N\s*=\s*\d+|\bn\s*=\s*\d+", ctx + line[m.end():m.end() + 25]):
                bad.append(f"{name}:{i}: «{m.group(0)}» without a denominator (k/n or N=)")
    return bad


def cmd_check(args) -> int:
    bad = []
    if not LEARNINGS.exists():
        print(f"✗ {LEARNINGS.relative_to(MVB)} missing", file=sys.stderr)
        return 1
    text = LEARNINGS.read_text(encoding="utf-8")
    bad += [f"learnings.md: no section «{s}»" for s in REQUIRED if s not in text]
    if not re.search(r"(?m)^version:\s*\d{4}-\d{2}-\d{2}", text):
        bad.append("learnings.md: frontmatter has no `version: YYYY-MM-DD`")
    bad += check_text(text, "learnings.md")
    if args.proposals:
        p = Path(args.proposals)
        if not p.exists():
            p = OUT_DIR / args.proposals
        if not p.exists():
            bad.append(f"proposals file {args.proposals} not found")
        else:
            pt = p.read_text(encoding="utf-8")
            bad += check_text(pt, p.name)
            if not re.search(r"data-\d{4}-\d{2}-\d{2}\.md", pt):
                bad.append(f"{p.name}: does not name the data file it was built from")
    for b in bad[:30]:
        print("  ✗ " + b)
    if bad:
        print(f"\n✗ {len(bad)} problem(s)", file=sys.stderr)
        return 1
    print("✓ learnings.md" + (f" + {Path(args.proposals).name}" if args.proposals else "") + " pass")
    return 0


# -------------------------------------------------------------------------- monthly

def log(msg: str) -> None:
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"{datetime.now(timezone.utc):%Y-%m-%d %H:%M:%SZ} {msg}\n")


def cmd_monthly(args) -> int:
    """Cron. Build the numbers, then hand the judgment to a conductor job: the coordinator
    runs campaign-analyzer in pooled mode, writes proposals and sends Vadim the TL;DR.
    Nothing reaches learnings.md before Vadim approves (`/outbound learnings-apply`)."""
    try:
        path = latest_snapshot()
        age = (date.today() - date.fromisoformat(path.stem)).days
        if age > 3:
            raise RuntimeError(f"last snapshot {path.name} is {age} days old — "
                               "check `stats snapshot` in closely-pull.log")
        rc = cmd_build(argparse.Namespace(snapshot=str(path), min_age=MIN_AGE))
        if rc:
            raise RuntimeError(f"build exit {rc}")
        data = f"data-{json.loads(path.read_text(encoding='utf-8'))['pulled_at'][:10]}"
        if args.dry_run:
            print(f"(dry run) would enqueue: mvb-run.py outbound \"learnings {data}\"")
            return 0
        env = dict(os.environ, HO_DB=D.HO_DB)
        r = subprocess.run([sys.executable, str(MVB_RUN), "outbound", f"learnings {data}"],
                           capture_output=True, text=True, timeout=120, env=env)
        out = (r.stdout + r.stderr).strip()
        m = re.search(r"job #(\d+)", out)
        if r.returncode not in (0, 2) or not m:
            raise RuntimeError(f"mvb-run exit {r.returncode}: {out.splitlines()[-1] if out else '—'}")
        log(f"enqueued job #{m.group(1)} for {data}")
        print(f"✓ job #{m.group(1)} — /outbound learnings {data}")
        return 0
    except Exception as e:                                          # noqa: BLE001
        log(f"FAILED {e}")
        print(f"✗ {e}", file=sys.stderr)
        if args.notify:
            OP.telegram_send(f"⚠️ Щомісячний аналіз outbound не стартував: {D.short(str(e), 300)}")
        return 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build", help="pooled numbers → workspace/outbound/learnings/data-*.md")
    b.add_argument("--snapshot", help="snapshot JSON (default: the latest)")
    b.add_argument("--min-age", type=int, default=MIN_AGE)
    m = sub.add_parser("monthly", help="cron: build + enqueue /outbound learnings")
    m.add_argument("--notify", action="store_true", help="Telegram on failure")
    m.add_argument("--dry-run", action="store_true")
    c = sub.add_parser("check", help="gate for learnings.md (+ a proposals file)")
    c.add_argument("--proposals")
    args = ap.parse_args(argv)
    return {"build": cmd_build, "monthly": cmd_monthly, "check": cmd_check}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
