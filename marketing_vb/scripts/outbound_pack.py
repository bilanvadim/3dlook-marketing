#!/usr/bin/env python3
"""outbound_pack.py — compact inputs and mechanical gates for outbound steps 2-6.

WHY THIS EXISTS
---------------
Measured 2026-09-28 with `scripts/pack-cost.py` on two campaigns run the same day:

    2026-09-14-eu-erakulis-similar    56.2M tokens  ~$73   125 contacts
    2026-09-27-uk-bariatric-prequal   26.8M tokens  ~$35    74 contacts

Almost none of that was writing. A subagent started at ~20K tokens of context, climbed to
150-240K, and then held it for 34-72 requests, each of which re-reads the whole context.
What filled it:

  * `hypothesis.md` (49 KB) read by every agent, when message-sequencer needs ~3 KB of it;
  * `compliance.md`, `proof-points.md`, `accuracy-formulations.md`, another campaign's
    STATUS.md, read whole for a handful of lines each;
  * profile dumps every agent built for itself out of the 749 KB raw export (15-71 KB);
  * one Bash or Write round per person, plus detector loops;
  * four validation rounds, three of which only added people Vadim had named.

And the coordinator, one long session on the largest model, was 57% of the bill.

So the same split as `social_pack.py` and `article_package.py`: agents write and judge,
code does everything that has one right answer. Every command prints a summary of at most
~2 KB and writes the full report to a file, because whatever a script prints lands in the
caller's context and is re-billed on every later request of that session.

    next             where a campaign stands and the exact next command
    sales-nav-query  step 2 -> the Sales Navigator filter Vadim pastes (titles, not companies)
    compact          step 4 input: one row per person, ~70 chars each, with mechanical flags
    card             the campaign's rules for one stage, cut verbatim from hypothesis.md
    apply-decisions  step 4 output: decisions.csv -> people-validated.csv, identity kept
    skipped          who was left out, grouped by function, seniors first (goes in report 1)
    promote          add named people to SEND without an agent round
    profiles         step 5 input: batch plan + one compact profile card per person
    split-messages   step 5 output: one batch file -> per-person files, then the gate
    check-messages   the gate: completeness, limits, signature, bans, detector, repetition
    qc-prompt        what quality-controller is asked to read after a stage, and nothing more
    build-import     step 6: one closely.io CSV for everyone, check-import, import-log.md

Shared logic is imported from `outbound-pipeline.py` and `outbound-registry.py`, not copied.
Stdlib only: pandas is not installed anywhere on this box.

USAGE
    scripts/outbound_pack.py next            [--campaign <slug> | --find "<words>"]
    scripts/outbound_pack.py sales-nav-query --campaign <slug>
    scripts/outbound_pack.py compact         --campaign <slug>
    scripts/outbound_pack.py card            --campaign <slug> --for validate|messages [--check]
    scripts/outbound_pack.py apply-decisions --campaign <slug> [--in decisions.csv]
    scripts/outbound_pack.py skipped         --campaign <slug>
    scripts/outbound_pack.py promote         --campaign <slug> --names "A; B" | --file pool.csv
    scripts/outbound_pack.py profiles        --campaign <slug> [--max 35]
    scripts/outbound_pack.py split-messages  --campaign <slug> --in messages/_batch-<name>.md
    scripts/outbound_pack.py check-messages  --campaign <slug> [--batch <name>]
    scripts/outbound_pack.py qc-prompt       --campaign <slug> --stage hypothesis|validate|messages
    scripts/outbound_pack.py build-import    --campaign <slug> [--overwrite] [--out-dir D]
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import difflib
import importlib.util
import json
import re
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


PIPE = _load("outbound_pipeline", HERE / "outbound-pipeline.py")
REG = PIPE.REG
norm_company = REG.norm_company
norm_linkedin = REG.norm_linkedin
pick = REG.pick
rel = PIPE.rel

OWNER = {"katerina": "Katerina", "nick": "Nick", "olena": "Olena",
         "katya": "Kateryna", "vadim": "Vadim"}
CAPS = {1: 600, 2: 550}

# How Vadim names a profile in a request. "Лена" is olena, not a new person.
PROFILE_ALIASES = {
    "olena": ("olena", "lena", "elena", "олена", "лена", "лены", "лени", "елена"),
    "katerina": ("katerina", "катерина", "катерины", "катерини", "galich"),
    "katya": ("katya", "катя", "кати", "kateryna"),
    "nick": ("nick", "нік", "ник", "ніка", "ника"),
    "vadim": ("vadim", "вадим", "вадима"),
}

_TRANSLIT = str.maketrans({
    "а": "a", "б": "b", "в": "v", "г": "g", "ґ": "g", "д": "d", "е": "e", "є": "e",
    "ё": "e", "ж": "zh", "з": "z", "и": "i", "і": "i", "ї": "i", "й": "i", "к": "k",
    "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t",
    "у": "u", "ф": "f", "х": "h", "ц": "c", "ч": "ch", "ш": "sh", "щ": "sch", "ы": "y",
    "э": "e", "ю": "yu", "я": "ya", "ь": "", "ъ": "", "'": "", "’": "",
})


def translit(s: str) -> str:
    return s.lower().translate(_TRANSLIT)


# ------------------------------------------------------------------ small helpers

def campaigns_root() -> Path:
    return ROOT / "workspace" / "outbound" / "campaigns"


def cdir_of(slug: str) -> Path:
    d = campaigns_root() / slug
    if not d.is_dir():
        have = sorted(p.name for p in campaigns_root().iterdir()
                      if p.is_dir() and not p.name.startswith("_"))
        print(f"✗ no campaign `{slug}`. Existing:\n  " + "\n  ".join(have), file=sys.stderr)
        sys.exit(2)
    return d


def read_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8-sig") as fh:
        return [dict(r) for r in csv.DictReader(fh)]


def write_csv(path: Path, rows: list[dict], cols: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in cols})


def today() -> str:
    return dt.date.today().isoformat()


def frontmatter(text: str) -> dict:
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    out: dict = {}
    if not m:
        return out
    for line in m.group(1).splitlines():
        if ":" not in line or line[:1] in (" ", "#", "-"):
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            out[k.strip()] = [x.strip().strip("'\"") for x in v[1:-1].split(",") if x.strip()]
        else:
            out[k.strip()] = v.strip("'\"")
    return out


def h2_sections(text: str) -> list[tuple[str, str]]:
    """[(heading, whole section incl. its ### children)], frontmatter dropped."""
    body = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    out = []
    for part in re.split(r"(?m)^(?=## )", body):
        if part.startswith("## "):
            out.append((part.splitlines()[0][3:].strip(), part.rstrip() + "\n"))
    return out


def md_section(path: Path, *needles: str, level: str = "##") -> str:
    """Sections of a markdown file whose heading contains any needle (case-insensitive)."""
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8")
    # Cut at the next heading of the same OR a higher level: splitting on "### " alone let
    # "### Aggregate" run on through "## Pricing" and "## Funding" into the messages card.
    parts = re.split(rf"(?m)^(?=#{{1,{len(level)}}} )", text)
    keep = [p.rstrip() for p in parts
            if p.startswith(level + " ")
            and any(n.lower() in p.splitlines()[0].lower() for n in needles)]
    return "\n\n".join(keep)


def demote(md: str, by: int = 1) -> str:
    """Push every heading down, so quoted material nests under the card's own headings."""
    return re.sub(r"(?m)^(#+) ", lambda m: "#" * (len(m.group(1)) + by) + " ", md)


def pid_of(url: str) -> str:
    u = norm_linkedin(url or "")
    return (u.rsplit("/", 1)[-1] if u else "").lower()[:64]


def company_slug_of_url(url: str) -> str:
    m = re.search(r"linkedin\.com/company/([^/?#]+)", (url or "").lower())
    return m.group(1) if m else ""


def hypothesis_of(cdir: Path) -> tuple[str, dict]:
    p = cdir / "hypothesis.md"
    if not p.exists():
        print(f"✗ no hypothesis.md in {rel(cdir)}", file=sys.stderr)
        sys.exit(2)
    text = p.read_text(encoding="utf-8")
    return text, frontmatter(text)


def profile_of(cdir: Path, fm: dict | None = None) -> str:
    fm = fm if fm is not None else hypothesis_of(cdir)[1]
    return (fm.get("profile") or REG.infer_profile(cdir.name) or "").strip()


def calendar_link(profile: str) -> str:
    t = ROOT / "brand-assets" / "product-info" / "outbound-message2-template.md"
    if not t.exists():
        return ""
    m = re.search(rf"(?m)^\|\s*{re.escape(profile)}\s*\|\s*(https?://\S+)\s*\|", t.read_text())
    return m.group(1) if m else ""


def raw_index(cdir: Path) -> dict[str, dict]:
    """person_id -> raw Sales Navigator row, keys lower-cased."""
    out: dict[str, dict] = {}
    raw = cdir / "sales-nav-raw"
    for f in sorted(raw.glob("*.csv")) if raw.exists() else []:
        for r in read_csv(f):
            low = {(k or "").strip().lower(): (v or "") for k, v in r.items()}
            pid = pid_of(low.get("linkedin_url", ""))
            if pid and pid not in out:
                out[pid] = low
    return out


def clip(s: str, n: int) -> str:
    s = re.sub(r"\s+", " ", s or "").strip()
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"


def snapshot(path: Path) -> Path | None:
    """Keep the previous version next to the file as <stem>-vN-<date>.<ext>."""
    if not path.exists():
        return None
    n = 1
    while True:
        dst = path.with_name(f"{path.stem}-v{n}-{today()}{path.suffix}")
        if not dst.exists() and not list(path.parent.glob(f"{path.stem}-v{n}-*{path.suffix}")):
            break
        n += 1
    shutil.copy2(path, dst)
    return dst


# ------------------------------------------------------------------ shortlist / groups

def shortlist(cdir: Path) -> list[dict]:
    for name in ("companies-verified.csv", "companies.csv"):
        p = cdir / name
        if p.exists():
            return read_csv(p)
    return []


def group_map(cdir: Path) -> dict[str, str]:
    """company slug -> group name.

    A multi-brand group is written in the shortlist as "FitCoach (Welltech)",
    "DoFasting (Kilo Health)". The parenthetical is a group only when two or more rows
    share it: "Activerse (Diet & Training by Ann)" is one company with a product name.
    """
    rows = shortlist(cdir)
    paren = Counter()
    for r in rows:
        for inner in re.findall(r"\(([^)]*)\)", pick(r, "company_name", "company")):
            paren[inner.strip()] += 1
    out: dict[str, str] = {}
    for r in rows:
        name = pick(r, "company_name", "company")
        if not name:
            continue
        inner = [x.strip() for x in re.findall(r"\(([^)]*)\)", name)]
        grp = next((x for x in inner if paren[x] >= 2), None)
        base = re.sub(r"\([^)]*\)", " ", name).strip(" -,")
        out[norm_company(PIPE.clean_company(name))] = grp or base or name
        for k in PIPE.shortlist_keys(name):
            out.setdefault(k, grp or base or name)
    return out


def group_of(row: dict, gmap: dict[str, str]) -> str:
    g = (row.get("group") or "").strip()
    if g:
        return g
    slug = (row.get("company_slug") or "").strip()
    if slug in gmap:
        return gmap[slug]
    for k in PIPE.company_keys(row.get("company_name", "")):
        if k in gmap:
            return gmap[k]
    return (row.get("company_name") or "?").strip()


def shortlist_company_urls(cdir: Path) -> dict[str, set[str]]:
    """group name -> LinkedIn company slugs the shortlist knows for it."""
    gmap = group_map(cdir)
    out: dict[str, set[str]] = defaultdict(set)
    for r in shortlist(cdir):
        name = pick(r, "company_name", "company")
        g = gmap.get(norm_company(PIPE.clean_company(name)), name)
        s = company_slug_of_url(pick(r, "linkedin_url", "company_linkedin_url"))
        if s:
            out[g].add(s)
    return out


# ------------------------------------------------------------------ who is being sent

def validated_rows(cdir: Path) -> list[dict]:
    p = cdir / "people-validated.csv"
    return read_csv(p) if p.exists() else []


def expected_people(cdir: Path) -> tuple[list[dict], str]:
    """The people messages are written for, and where that list came from.

    New flow: `send == SEND` in people-validated.csv (apply-decisions and promote fill it).
    Older campaigns: people-approved.csv if Vadim's checkpoint wrote one, else PASS rows.
    """
    rows = validated_rows(cdir)
    if any((r.get("send") or "").strip() for r in rows):
        return ([r for r in rows if (r.get("send") or "").strip().upper() == "SEND"],
                "people-validated.csv (send == SEND)")
    ap = cdir / "people-approved.csv"
    if ap.exists():
        return read_csv(ap), "people-approved.csv"
    keep = [r for r in rows
            if (r.get("decision") or "").strip().upper() == "PASS"
            or str(r.get("vadim_approved_weak", "")).lower() in ("true", "1", "yes")]
    return keep, "people-validated.csv (decision == PASS)"


def wave_of(row: dict) -> int:
    w = re.sub(r"\D", "", str(row.get("wave") or ""))
    return int(w) if w else 1


# ================================================================== next

def resolve_campaign(find: str) -> list[str]:
    words = [w for w in re.split(r"[\s,.;]+", find.lower()) if len(w) > 2]
    prof = None
    rest = []
    for w in words:
        hit = next((p for p, al in PROFILE_ALIASES.items() if w in al), None)
        if hit:
            prof = hit
        else:
            rest.append(translit(w))
    scored = []
    for d in sorted(campaigns_root().iterdir(), reverse=True):
        if not d.is_dir() or d.name.startswith("_"):
            continue
        tokens = d.name.split("-")[3:]
        score = 0.0
        if prof:
            p = REG.infer_profile(d.name)
            hp = d / "hypothesis.md"
            if hp.exists():
                p = frontmatter(hp.read_text(encoding="utf-8")).get("profile") or p
            if p != prof:
                continue
            score += 1
        for w in rest:
            best = max((difflib.SequenceMatcher(None, w, t).ratio() for t in tokens),
                       default=0)
            if best >= 0.72:
                score += best
        if score > 0:
            scored.append((score, d.name))
    scored.sort(key=lambda x: (-x[0], x[1]), reverse=False)
    top = scored[0][0] if scored else 0
    return [n for s, n in sorted(scored, key=lambda x: (-x[0], x[1])) if s >= top - 0.01]


NEXT_STEPS = {
    0: ["/outbound hypothesis"],
    1: ["Vadim approves the hypothesis (status: approved)", "/outbound research {slug}"],
    2: ["scripts/outbound_pack.py sales-nav-query --campaign {slug}",
        "VADIM: run that filter in Sales Navigator, export into sales-nav-raw/"],
    3: ["scripts/outbound-pipeline.py extract-people --campaign {slug} --dry-run   (then without)",
        "scripts/outbound_pack.py compact --campaign {slug}",
        "scripts/outbound_pack.py card --campaign {slug} --for validate",
        "/outbound validate {slug}"],
    4: ["CHECKPOINT: Vadim approves the list (icp-validation-summary.md + skipped pools)",
        "scripts/outbound_pack.py promote --campaign {slug} --names \"...\"   (if he adds people)",
        "scripts/outbound_pack.py card --campaign {slug} --for messages",
        "scripts/outbound_pack.py profiles --campaign {slug}",
        "/outbound messages {slug}"],
    5: ["scripts/outbound_pack.py check-messages --campaign {slug}",
        "CHECKPOINT: Vadim approves the texts",
        "scripts/outbound_pack.py build-import --campaign {slug}"],
    6: ["VADIM: import the CSVs into closely.io and start the campaign",
        "scripts/outbound-registry.py record --campaign {slug} --profile {profile}",
        "replies arrive by the nightly cron (closely-pull.py pull-all)"],
    7: ["/outbound responses {slug}   (the nightly job does this by itself)"],
    8: ["metrics-final.json, then /outbound analyze {slug}"],
    9: ["/outbound analyze {slug}"],
}


def cmd_next(args) -> int:
    if args.campaign:
        slugs = [args.campaign]
    elif args.find:
        slugs = resolve_campaign(args.find)
        if not slugs:
            print(f"✗ nothing matches «{args.find}». `outbound-registry.py status` lists all.",
                  file=sys.stderr)
            return 1
        if len(slugs) > 1:
            print(f"«{args.find}» matches {len(slugs)} campaigns, newest first:")
    else:
        print("✗ give --campaign or --find", file=sys.stderr)
        return 2

    for slug in slugs[:4]:
        cdir = cdir_of(slug)
        stage, blocked = REG.stage_of(cdir)
        idx = int(stage.split("·")[0].strip() or 0)
        fm = frontmatter((cdir / "hypothesis.md").read_text(encoding="utf-8")) \
            if (cdir / "hypothesis.md").exists() else {}
        profile = fm.get("profile") or REG.infer_profile(slug) or "?"
        print(f"\ncampaign   {slug}  ({profile} · {fm.get('product', '?')} · "
              f"hypothesis {fm.get('status', 'missing')})")
        print(f"stage      {stage}   blocked on: {blocked}")

        facts = []
        sl = shortlist(cdir)
        if sl:
            facts.append(f"companies {len(sl)}")
        raw = cdir / "sales-nav-raw"
        if raw.exists():
            n = sum(len(read_csv(f)) for f in raw.glob("*.csv"))
            facts.append(f"sales-nav-raw {n} rows")
        if (cdir / "people-raw.csv").exists():
            facts.append(f"people-raw {len(read_csv(cdir / 'people-raw.csv'))}")
        v = validated_rows(cdir)
        if v:
            exp, _ = expected_people(cdir)
            facts.append(f"validated {len(v)} (to send {len(exp)})")
            have = sum(1 for p in exp if (cdir / "messages" / f"{p.get('person_id')}.md").exists())
            if (cdir / "messages").exists():
                facts.append(f"messages {have}/{len(exp)}")
        imps = sorted(cdir.glob("closelyhq-import*.csv"))
        if imps:
            facts.append("import " + "+".join(str(len(read_csv(f))) for f in imps))
        print("files      " + " · ".join(facts))

        lock = cdir / PIPE.LOCK_NAME
        if lock.exists() and (cdir / "hypothesis.md").exists():
            cur, _ = PIPE.scope_hash((cdir / "hypothesis.md").read_text(encoding="utf-8"))
            was = json.loads(lock.read_text()).get("scope_hash")
            print("scope      " + ("unchanged since the list was built" if cur == was
                                   else "CHANGED since the list was built: hypothesis-gate --stamp"))
        print("next")
        for line in NEXT_STEPS.get(min(idx, 9), ["—"]):
            print("  " + line.format(slug=slug, profile=profile))
    return 0


# ================================================================== sales-nav-query

EXCLUDE_TITLES = ("Engineer", "Developer", "Designer", "Recruiter", "Accountant",
                  "Support", "Intern", "Assistant", "Scrum Master", "QA")


TITLE_WORD = re.compile(r"\b(officer|chief|c[etofpm]o|founder|director|head|vp|vice president|"
                        r"president|manager|lead|owner|gm|partner|staff)\b", re.I)


def expand_titles(text: str) -> list[str]:
    """The persona bullet is prose; Sales Navigator wants one title per term.

    "VP / Head / Director of Growth, Retention or Engagement" is nine titles: the heads
    carry over to the bare tails that follow them. A fenced ```titles block in the
    hypothesis skips all of this, and is what hypothesis-generator now writes.
    """
    out: list[str] = []
    for chunk in re.split(r";|\n", text):
        chunk = re.sub(r"\([^)]*\)", "", chunk)
        chunk = re.sub(r"\bsince \d{4}-\d{2}-\d{2}( also)?\b", "", chunk).strip(" .-*")
        heads: list[str] = []
        for item in chunk.split(","):
            for piece in re.split(r"\bor\b|\band\b", item):
                piece = piece.strip(" .")
                if not piece:
                    continue
                m = re.match(r"(.+?)\s+of\s+(.+)", piece)
                if m and "/" in m.group(1):
                    heads = [h.strip() for h in m.group(1).split("/") if h.strip()]
                    out += [f"{h} of {m.group(2).strip()}" for h in heads]
                elif m and "/" in m.group(2):
                    heads = [m.group(1).strip()]
                    out += [f"{heads[0]} of {t.strip()}" for t in m.group(2).split("/")
                            if t.strip()]
                elif "/" in piece:
                    out += [x.strip() for x in piece.split("/") if x.strip()]
                    heads = []
                elif heads and not TITLE_WORD.search(piece):
                    out += [f"{h} of {piece}" for h in heads]
                else:
                    out.append(piece)
                    heads = []
    seen, uniq = set(), []
    for t in out:
        t = re.sub(r"\s+", " ", t)
        if 2 < len(t) < 60 and t.lower() not in seen:
            seen.add(t.lower())
            uniq.append(t)
    return uniq


def titles_from_hypothesis(text: str) -> tuple[list[str], str]:
    m = re.search(r"```titles\n(.*?)```", text, re.S)
    if m:
        return [t.strip() for t in m.group(1).splitlines() if t.strip()], "```titles block"
    m = re.search(r"\*\*Titles to include:?\*\*:?\s*(.+)", text)
    if m:
        return expand_titles(m.group(1)), "«Titles to include» bullet"
    return [], ""


def cmd_sales_nav_query(args) -> int:
    cdir = cdir_of(args.campaign)
    text, fm = hypothesis_of(cdir)
    profile = profile_of(cdir, fm)
    rows = []
    for r in shortlist(cdir):
        owner = PIPE.geo_profile(pick(r, "hq_country", "country", "hq"))
        if profile and owner and owner != profile:
            continue
        f = PIPE.fit_of(r)
        if f and f not in PIPE.FIT_OK:
            continue
        rows.append(r)
    if not rows:
        print("✗ no shortlisted companies: run step 2 first", file=sys.stderr)
        return 2
    titles, src = titles_from_hypothesis(text)
    if not titles:
        print("✗ the hypothesis names no titles. Add a fenced ```titles block (one title per\n"
              "  line) under «Target buyer persona», or a «**Titles to include:**» bullet.",
              file=sys.stderr)
        return 1

    boolean = " OR ".join(f'"{t}"' for t in titles)
    exclude = " OR ".join(f'"{t}"' for t in EXCLUDE_TITLES)
    out = [f"# Sales Navigator pull — {cdir.name}", "",
           f"Profile: **{profile}** · generated {today()} from the hypothesis ({src}).", "",
           "**Pull by TITLE inside the company list, never by company alone.** A company-only",
           "pull returns whole staff lists: 276 of 321 people (86%) on the 2026-09-28 EU export",
           "and 72 of 98 on the UK one were never candidates, and the real buyers (CPO, Head of",
           "Product, brand GMs) were missing from both.", "",
           f"## 1. Current company ({len(rows)})", ""]
    for r in rows:
        url = pick(r, "linkedin_url", "company_linkedin_url")
        out.append(f"- {pick(r, 'company_name', 'company')}" + (f" — {url}" if url else ""))
    out += ["", f"## 2. Current job title ({len(titles)} titles)", "",
            "Paste into «Current job title» (Boolean):", "", "```", boolean, "```", "",
            "Exclude:", "", "```", f"NOT ({exclude})", "```", "",
            "## 3. Export", "",
            f"Save the CSV into `{rel(cdir / 'sales-nav-raw')}/`, then:", "", "```",
            f"scripts/outbound_pack.py next --campaign {cdir.name}", "```", ""]
    dst = cdir / "sales-nav-query.md"
    dst.write_text("\n".join(out), encoding="utf-8")
    print(f"✓ {rel(dst)}: {len(rows)} companies × {len(titles)} titles")
    print("  titles: " + clip(", ".join(titles), 400))
    return 0


# ================================================================== compact (step 4 input)

COMPACT_COLS = ["person_id", "full_name", "title", "group", "location", "headline",
                "earlier_roles", "flags"]


def strip_employment(s: str) -> str:
    return re.sub(r"\s*[.·]\s*(full-?time|part-?time|self-?employed|contract|freelance|"
                  r"internship|temporary|seasonal|apprenticeship|permanent|undefined)\b",
                  "", s or "", flags=re.I)


def legit_company_pages(people: list[dict], raw: dict[str, dict], gmap: dict[str, str],
                        urls: dict[str, set[str]]) -> dict[str, set[str]]:
    """group -> company pages that really are that group.

    Not "the page in the shortlist": all 104 Welltech people sit on `welltech22` while the
    shortlist lists the brands' own pages. A page is the group's when the shortlist names
    it OR several of the group's people are on it; what is left is an outlier.

    This does NOT catch every name collision. An export pulled by company attaches the
    real company page to everyone in it, "Founder KILO Akustik" included, so that one is
    only visible in the headline, which is why `compact` keeps the headline.
    """
    seen: dict[str, Counter] = defaultdict(Counter)
    for p in people:
        r = raw.get(p.get("person_id", ""), {})
        s = company_slug_of_url(r.get("company linkedin_url", ""))
        if s:
            seen[group_of(p, gmap)][s] += 1
    out: dict[str, set[str]] = {}
    for g, c in seen.items():
        total = sum(c.values())
        out[g] = set(urls.get(g) or ()) | {s for s, n in c.items()
                                           if n >= 3 or n >= 0.2 * total}
    return out


def person_flags(p: dict, raw: dict, profile: str, grp: str,
                 urls: dict[str, set[str]]) -> list[str]:
    flags = []
    if raw:
        cslug = company_slug_of_url(raw.get("company linkedin_url", ""))
        known = urls.get(grp) or set()
        if cslug and known and cslug not in known:
            flags.append(f"other-company-page:{cslug}")
        roles = [r for r in strip_employment(raw.get("experience", "")).split(", ") if r]
        if not raw.get("bio", "").strip() and not raw.get("skills", "").strip() and len(roles) <= 1:
            flags.append("empty-profile")
        owner = PIPE.geo_profile(raw.get("location", ""))
        if profile and owner and owner != profile:
            flags.append(f"geo:{owner}")
    else:
        flags.append("not-in-raw-export")
    return flags


def headline_if_new(headline: str, title: str, company: str) -> str:
    """The headline only when it says something the title does not."""
    h = clip(headline, 100)
    bare = re.sub(r"\b(at|@|bei|chez)\b.*$", "", h, flags=re.I).strip(" |-·,")
    t = title.lower()
    if not bare or bare.lower() in t or t in bare.lower():
        return ""
    if difflib.SequenceMatcher(None, bare.lower(), t).ratio() > 0.8:
        return ""
    return h


def cmd_compact(args) -> int:
    cdir = cdir_of(args.campaign)
    src = cdir / "people-raw.csv"
    if not src.exists():
        print(f"✗ no people-raw.csv in {rel(cdir)}: run extract-people first", file=sys.stderr)
        return 2
    _, fm = hypothesis_of(cdir)
    profile = profile_of(cdir, fm)
    people = read_csv(src)
    raw = raw_index(cdir)
    gmap = group_map(cdir)
    urls = legit_company_pages(people, raw, gmap, shortlist_company_urls(cdir))

    checked = {}
    cp = cdir / "people-checked.csv"
    if cp.exists():
        checked = {r.get("person_id"): r for r in read_csv(cp)}

    rows, flagged = [], Counter()
    for p in people:
        pid = p.get("person_id") or pid_of(pick(p, "person_linkedin_url", "linkedin_url"))
        r = raw.get(pid, {})
        grp = group_of(p, gmap)
        flags = person_flags(p, r, profile, grp, urls)
        ex = checked.get(pid, {})
        if (ex.get("exclusion_flag") or "").strip():
            flags.append("registry:" + clip(ex.get("exclusion_reason", "excluded"), 40))
        for f in flags:
            flagged[f.split(":")[0]] += 1
        title = p.get("title", "")
        exp = [x for x in strip_employment(r.get("experience", "")).split(", ") if x]
        rows.append({
            "person_id": pid,
            "full_name": p.get("full_name") or f"{p.get('first_name','')} {p.get('last_name','')}".strip(),
            "title": clip(title, 90),
            "company_name": p.get("company_name", ""),
            "group": grp,
            "location": clip(r.get("location") or p.get("location_country", ""), 30),
            "seniority": p.get("seniority", ""),
            "headline": headline_if_new(r.get("headline", ""), title, p.get("company_name", "")),
            "earlier_roles": clip(", ".join(exp[1:3]), 90),
            "flags": " ".join(flags),
        })
    dst = cdir / "people-compact.csv"
    write_csv(dst, rows, COMPACT_COLS)
    size = dst.stat().st_size
    print(f"✓ {rel(dst)}: {len(rows)} people, {size:,} bytes "
          f"(raw export: {sum(f.stat().st_size for f in (cdir / 'sales-nav-raw').glob('*.csv')):,})")
    by_grp = Counter(r["group"] for r in rows)
    print("  groups: " + ", ".join(f"{g} {n}" for g, n in by_grp.most_common(12)))
    if flagged:
        print("  flags:  " + ", ".join(f"{k} {n}" for k, n in flagged.most_common()))
    return 0


# ================================================================== card

CARD_SECTIONS = {
    "validate": ("target buyer persona", "anti-case", "exclusion", "decisions",
                 "feature screen", "company types in scope"),
    "messages": ("rules for steps", "use case", "message angle", "outreach language",
                 "decisions"),
}

BATCH_FORMAT = """\
Write ONE file per batch, `messages/_batch-<batch>.md`, in exactly this shape:

    @@@ <person_id>
    hook: <the specific thing about this person or company the opener stands on>
    proof: <the fact cited, and its source file>
    --- M1
    Hi <first name>,

    <message 1>

    <signature>
    --- M2
    Hi <first name>,

    <message 2>

    <signature>

Then run `scripts/outbound_pack.py split-messages --campaign <slug> --in <that file>`.
It writes the per-person files, counts characters, runs the detector and every ban, and
prints ONLY what failed. Fix those entries in the batch file and run it again. Do not write
per-person files yourself, do not count characters yourself, do not run the detector
yourself.
"""


def use_case_file(fm: dict, text: str) -> Path | None:
    d = ROOT / "brand-assets" / "product-info" / "use-cases"
    name = fm.get("use_case")
    if name and (d / f"{name}.md").exists():
        return d / f"{name}.md"
    hits = Counter(re.findall(r"use-cases/([a-z0-9-]+)\.md|\b((?:fx|mt)-[a-z-]+)\.md", text))
    for (a, b), _ in hits.most_common():
        f = d / f"{a or b}.md"
        if f.exists():
            return f
    return None


def bullets_about(section: str, word: str) -> str:
    """Top-level bullets of a section (with their sub-bullets) that mention `word`."""
    # `word` has to be in the bullet's opening, where its subject is named. Anywhere in the
    # bullet also caught the falsification criterion, which only mentions messages.
    keep, cur = [], []

    def flush():
        if not cur:
            return
        lead = re.match(r"[-*] \*\*(.+?)\*\*", cur[0])
        if re.search(word, lead.group(1) if lead else cur[0][:40], re.I):
            keep.append("\n".join(cur).rstrip())

    for line in section.splitlines()[1:]:
        if re.match(r"[-*] ", line):
            flush()
            cur = [line]
        elif cur:
            cur.append(line)
    flush()
    return "\n".join(keep)


def build_card(cdir: Path, stage: str) -> str:
    text, fm = hypothesis_of(cdir)
    profile = profile_of(cdir, fm)
    product = fm.get("product", "fitxpress")
    h, _ = PIPE.scope_hash(text)
    secs = [body for title, body in h2_sections(text)
            if any(k in title.lower() for k in CARD_SECTIONS[stage])]
    banned = fm.get("banned_terms") or []
    if isinstance(banned, str):
        banned = [banned]

    out = [f"# {stage.capitalize()} card — {cdir.name}", "",
           f"<!-- generated by outbound_pack.py card; hypothesis {h}; {today()} -->", "",
           "This card replaces reading `hypothesis.md`, `STATUS.md`, `CLAUDE.md` and the",
           "product files. Everything below is cut verbatim from its source. If something you",
           "need is not here, say so in your report; do not go and read the sources.", "",
           "## Campaign", "",
           f"- campaign: `{cdir.name}`",
           f"- product: **{product}** · market: {fm.get('market', '?')}",
           f"- sending profile: **{profile}** ({OWNER.get(profile, '?')})", ""]

    if stage == "messages":
        link = calendar_link(profile)
        out += ["## Sender", "",
                f"- signature: exactly `{OWNER.get(profile, '?')}` on its own last line",
                "- language: English",
                "- Message 1 ≤ 600 characters, Message 2 ≤ 550 (the script counts)",
                (f"- calendar link for Message 2, plain text: {link}" if link else
                 "- no calendar link for this profile: close Message 2 with a soft ask"),
                "- referral-angle people: a short ask for the owner of the app roadmap,"
                " no pitch, calendar link optional", ""]
        if banned:
            out += ["## Never name (this campaign)", "",
                    ", ".join(f"`{b}`" for b in banned), ""]

    out += ["## Campaign rules (hypothesis.md, verbatim)", ""]
    out += [demote(s) for s in secs] or ["_(the hypothesis has none of the expected sections)_\n"]
    if stage == "messages":
        # The hypothesis keeps its message gate inside "Validation criteria", between the
        # company schema and the reply targets. The first new-flow batch went out without
        # it and 0 of 22 pairs carried a number, against 22 of 22 the day before.
        gate = "\n".join(bullets_about(body, r"\bmessage") for title, body in h2_sections(text)
                         if "validation criteria" in title.lower()).strip()
        if gate:
            out += ["### What every message must carry (hypothesis.md, Validation criteria)", "",
                    gate, ""]

    pi = ROOT / "brand-assets" / "product-info"
    if stage == "validate":
        m = re.search(r"icp-detail\.md[` ]*(?:§|section )\s*(\d+)", text)
        icp = pi / "icp-detail.md"
        if m and icp.exists():
            sec = md_section(icp, f"{m.group(1)}. ")
            if sec:
                out += ["## ICP segment (icp-detail.md, verbatim)", "", demote(sec), ""]
    else:
        uc = use_case_file(fm, text)
        if uc:
            out += [f"## Use case ({uc.name}, verbatim)", "",
                    demote(uc.read_text(encoding="utf-8").strip(), 2), ""]
        prod_heading = "FitXpress" if product == "fitxpress" else "Mobile Tailor"
        proof = pi / "proof-points.md"
        facts = [md_section(proof, "Repeatability", "Speed", "Output coverage",
                            "How agents should cite"),
                 md_section(proof, prod_heading, "Aggregate", level="###")]
        icp = pi / "icp-detail.md"
        tti = re.search(r"(?m)^- (Time-to-integrate[^\n]*)$", icp.read_text(encoding="utf-8")) \
            if icp.exists() else None
        out += ["## Facts you may cite (proof-points.md, verbatim)", "",
                "Numbers come from here and nowhere else. The campaign rules above decide",
                "which of them may be used and how a client is referred to.", "",
                "**The gate checks two things per person** (referral-angle people excepted):",
                "Message 1 carries a product specific (what the scan returns, from how many",
                "photos, how fast), and the pair carries at least one number from this section",
                "or one the campaign rules clear by name.", "",
                demote("\n\n".join(f for f in facts if f)), ""]
        if tti:
            out += [f"Integration, for the technical-integration angle only (icp-detail.md): "
                    f"{tti.group(1)}. A generic figure, never a promise for this company.", ""]
        comp = pi / "compliance.md"
        lines = [md_section(comp, "1. Status at a glance", "2. GDPR roles"),
                 md_section(comp, "Outbound", level="###")]
        out += ["## Compliance lines (compliance.md, verbatim)", "",
                demote("\n\n".join(x for x in lines if x)), ""]
        msg = pi / "messaging.md"
        out += ["## Positioning (messaging.md, verbatim)", "",
                demote(md_section(msg, "Master positioning", "Anti-positioning",
                                  "Tone calibrations")), ""]
        bans = ROOT / "brand-assets" / "style-guides" / "hard-bans-card.md"
        if bans.exists():
            out += ["## Hard bans (hard-bans-card.md, verbatim)", "",
                    demote(bans.read_text(encoding="utf-8").strip(), 2), ""]
        for n in (1, 2):
            t = pi / f"outbound-message{n}-template.md"
            if t.exists():
                body = re.sub(r"\A---\n.*?\n---\n", "", t.read_text(encoding="utf-8"), flags=re.S)
                out += [f"## Message {n} template (verbatim)", "",
                        demote(body.strip(), 2), ""]
        out += ["## Output format", "", BATCH_FORMAT]
    return "\n".join(out).rstrip() + "\n"


def card_path(cdir: Path, stage: str) -> Path:
    return cdir / f"card-{stage}.md"


def card_is_fresh(cdir: Path, stage: str) -> tuple[bool, str]:
    p = card_path(cdir, stage)
    if not p.exists():
        return False, "missing"
    m = re.search(r"hypothesis ([0-9a-f]{8,})", p.read_text(encoding="utf-8")[:400])
    cur, _ = PIPE.scope_hash(hypothesis_of(cdir)[0])
    if not m or m.group(1) != cur:
        return False, "hypothesis scope changed since the card was built"
    if p.stat().st_mtime < (cdir / "hypothesis.md").stat().st_mtime:
        return False, "hypothesis.md is newer than the card"
    return True, "fresh"


def cmd_card(args) -> int:
    cdir = cdir_of(args.campaign)
    stage = getattr(args, "stage")
    if args.check:
        ok, why = card_is_fresh(cdir, stage)
        print(("✓ " if ok else "✗ ") + f"{rel(card_path(cdir, stage))}: {why}")
        return 0 if ok else 1
    text = build_card(cdir, stage)
    dst = card_path(cdir, stage)
    dst.write_text(text, encoding="utf-8")
    hyp = (cdir / "hypothesis.md").stat().st_size
    print(f"✓ {rel(dst)}: {len(text.encode()):,} bytes (hypothesis.md alone is {hyp:,})")
    heads = re.findall(r"(?m)^## (.+)$", text)
    print("  sections: " + clip(" · ".join(heads), 600))
    return 0


# ================================================================== apply-decisions

DECISION_COLS = ["person_id", "decision", "priority", "angle", "wave", "reason"]
VALIDATED_COLS = ["person_id", "full_name", "first_name", "last_name", "linkedin_url",
                  "person_linkedin_url", "title", "company_name", "company_slug", "group",
                  "person_location", "decision", "priority", "send", "reason",
                  "recommended_message_angle", "wave", "pool", "release_note", "flags",
                  "exclusion_flag", "exclusion_reason"]


def read_decisions(path: Path) -> list[dict]:
    """CSV, or the pipe form an agent writes: `person_id | decision | priority | angle |
    wave | reason`, one person per line.

    The pipe form exists because a hand-written CSV with a comma inside an unquoted cell
    shifts every later column and nothing complains: on 2026-09-02 `category` held a
    timestamp that way. A reason is prose and will contain commas. It will not contain `|`.
    """
    text = path.read_text(encoding="utf-8-sig")
    lines = [l for l in text.splitlines() if l.strip() and not l.lstrip().startswith("#")]
    if not lines or "|" not in lines[0]:
        return read_csv(path)
    out = []
    for l in lines:
        cells = [c.strip() for c in l.strip().strip("|").split("|", 5)]
        if cells[0].lower() in ("person_id", "") or set(cells[0]) <= set("-: "):
            continue
        cells += [""] * (6 - len(cells))
        out.append(dict(zip(DECISION_COLS, cells)))
    return out


def cmd_apply_decisions(args) -> int:
    cdir = cdir_of(args.campaign)
    if args.infile:
        src = Path(args.infile)
        if not src.exists():
            src = cdir / args.infile
    else:
        src = next((cdir / n for n in ("decisions.md", "decisions.txt", "decisions.csv")
                    if (cdir / n).exists()), cdir / "decisions.md")
    if not src.exists():
        print(f"✗ no decisions file ({rel(src)})", file=sys.stderr)
        return 2
    people = read_csv(cdir / "people-raw.csv")
    compact = {r["person_id"]: r for r in read_csv(cdir / "people-compact.csv")} \
        if (cdir / "people-compact.csv").exists() else {}
    checked = {r.get("person_id"): r for r in read_csv(cdir / "people-checked.csv")} \
        if (cdir / "people-checked.csv").exists() else {}
    dec = {}
    bad = []
    for i, r in enumerate(read_decisions(src), start=2):
        pid = (r.get("person_id") or "").strip().lower()
        d = (r.get("decision") or "").strip().upper()
        if d not in ("PASS", "WEAK", "FAIL"):
            bad.append(f"line {i}: decision «{r.get('decision')}» for {pid or '?'}")
            continue
        if d != "FAIL" and not (r.get("reason") or "").strip():
            bad.append(f"line {i}: {pid} is {d} with no reason")
        dec[pid] = r | {"decision": d}

    ids = [p.get("person_id") for p in people]
    missing = [i for i in ids if i not in dec]
    unknown = [i for i in dec if i not in set(ids)]
    if bad or missing or unknown:
        for b in bad[:10]:
            print(f"  ✗ {b}")
        if missing:
            print(f"  ✗ {len(missing)} people have no decision: {', '.join(missing[:8])}"
                  + (" …" if len(missing) > 8 else ""))
        if unknown:
            print(f"  ✗ {len(unknown)} decisions are for nobody in people-raw.csv: "
                  f"{', '.join(unknown[:8])}")
        print("\n✗ decisions not applied. Every person needs exactly one decision.",
              file=sys.stderr)
        return 1

    gmap = group_map(cdir)
    rows = []
    for p in people:
        pid = p["person_id"]
        d = dec[pid]
        c = compact.get(pid, {})
        ex = checked.get(pid, {})
        excluded = bool((ex.get("exclusion_flag") or "").strip())
        decision = "FAIL" if excluded else d["decision"]
        url = pick(p, "person_linkedin_url", "linkedin_url")
        rows.append({
            "person_id": pid, "full_name": p.get("full_name", ""),
            "first_name": p.get("first_name", ""), "last_name": p.get("last_name", ""),
            "linkedin_url": url, "person_linkedin_url": url,
            "title": p.get("title", ""), "company_name": p.get("company_name", ""),
            "company_slug": p.get("company_slug", ""),
            "group": c.get("group") or group_of(p, gmap),
            "person_location": c.get("location") or p.get("location_country", ""),
            "decision": decision,
            "priority": (d.get("priority") or "").strip() if decision == "PASS" else "",
            "send": {"PASS": "SEND", "WEAK": "REVIEW"}.get(decision, ""),
            "reason": ex.get("exclusion_reason") if excluded else (d.get("reason") or "").strip(),
            "recommended_message_angle": (d.get("angle") or d.get("recommended_message_angle")
                                          or "").strip(),
            "wave": (d.get("wave") or ("1" if decision == "PASS" else "")).strip(),
            "pool": (d.get("pool") or "").strip(),
            "release_note": (d.get("release_note") or "").strip(),
            "flags": c.get("flags", ""),
            "exclusion_flag": ex.get("exclusion_flag", ""),
            "exclusion_reason": ex.get("exclusion_reason", ""),
        })
    dst = cdir / "people-validated.csv"
    snap = snapshot(dst)
    write_csv(dst, rows, VALIDATED_COLS)
    n = Counter(r["decision"] for r in rows)
    print(f"✓ {rel(dst)}: {len(rows)} people · PASS {n['PASS']} · WEAK {n['WEAK']} · FAIL {n['FAIL']}"
          + (f" · previous kept as {snap.name}" if snap else ""))
    _print_distribution(cdir, [r for r in rows if r["send"] == "SEND"])
    return 0


# Vadim 2026-09-29: 30 for every campaign, raised the same day to 50 ("підніми ліміти до 50"). A hypothesis without
# `cap_per_group` gets this cap instead of none; a campaign can still set its own.
DEFAULT_CAP_PER_GROUP = 50


def cap_of(cdir: Path) -> int:
    fm = hypothesis_of(cdir)[1]
    v = str(fm.get("cap_per_group") or "").strip()
    return int(v) if v.isdigit() else DEFAULT_CAP_PER_GROUP


def _print_distribution(cdir: Path, send: list[dict]) -> bool:
    """Per-group counts against the cap. Returns True when a cap is broken."""
    cap = cap_of(cdir)
    gmap = group_map(cdir)
    by = Counter(group_of(r, gmap) for r in send)
    total = max(len(send), 1)
    over = False
    print(f"  to send {len(send)} · cap {cap} per group")
    for g, n in by.most_common(12):
        mark = ""
        if cap and n > cap:
            mark, over = f"  ✗ over the cap of {cap}", True
        print(f"    {g:28s} {n:4d}  {100 * n // total:3d}%{mark}")
    return over


# ================================================================== skipped

BUCKETS = [
    ("product", r"\bproduct\b|\bpm\b|\bpo\b|\bcpo\b"),
    ("retention / CRM / growth", r"retention|\bcrm\b|engagement|lifecycle|\bgrowth\b|subscription|"
                                 r"monetiz|loyalty|customer success|user success"),
    ("analytics / data / BI", r"analytic|\bbi\b|business intelligence|data scien|\binsights?\b|"
                              r"experimentation|\bresearch"),
    ("engineering / ML", r"engineer|developer|devops|devsecops|architect|\bsre\b|android|\bios\b|"
                         r"backend|frontend|full.?stack|tech(nical)? lead|infrastructure|software|"
                         r"machine learning|\bml\b|\bcto\b|technology|\bqa\b"),
    ("design / UX", r"\bdesign|\bux\b|\bui\b|\bcreative"),
    # Before partnerships: a "Finance Business Partner" is finance.
    ("finance / legal", r"financ|\bcfo\b|account(ant|ing)|controll|\btax\b|treasury|fp&a|\blegal|"
                        r"counsel|compliance|\bpayments?\b|billing|\brisk\b"),
    ("marketing / UA / content", r"marketing|\bcmo\b|user acquisition|\bua\b|\baso\b|\bseo\b|"
                                 r"\bbrand|\bcontent|\bsocial\b|\bpr\b|communications?|\bmedia\b|"
                                 r"\bvideo|community|affiliate|influencer|localization"),
    ("partnerships / BD / sales", r"partnerships?\b|business development|\bbd\b|\bsales\b|commercial|"
                                  r"account (manager|executive)|\bstrategy\b|corporate development"),
    ("clinical / coaching", r"doctor|physician|surgeon|\bnurse|dietit|nutrition|\bcoach|trainer|"
                            r"clinical|medical|pharmac|therap|psycholog"),
    ("operations", r"operations|\bcoo\b|supply chain|procurement|sourcing|logistics|portfolio|"
                   r"program manager|project manager|chief of staff"),
    # \boffice\b, not "office": "Chief Executive Officer" is not office staff.
    ("HR / office / support", r"\bhr\b|\bpeople\b|talent|recruit|\blearning\b|\boffice\b|facilit|"
                              r"assistant|\bsupport\b|help ?desk|customer (service|care)|scrum|"
                              r"\btravel\b"),
    ("executives (no function)", r"\bceo\b|chief executive|founder|president|managing director|"
                                 r"general manager|country manager|\bowner\b|\bboard\b|"
                                 r"founding partner"),
]
SENIOR = re.compile(r"\b(chief|c[efmotp]o|vp|vice president|svp|evp|head|director|founder|"
                    r"co-founder|owner|president|managing|general manager|country manager|"
                    r"lead|principal|partner)\b", re.I)


def bucket_of(title: str, headline: str = "") -> str:
    """Function by title; the headline only when the title names none."""
    for text in (title, headline):
        t = (text or "").lower()
        for name, rx in BUCKETS:
            if re.search(rx, t):
                return name
    return "other"


def cmd_skipped(args) -> int:
    cdir = cdir_of(args.campaign)
    rows = validated_rows(cdir)
    if not rows:
        print(f"✗ no people-validated.csv in {rel(cdir)}", file=sys.stderr)
        return 2
    raw = raw_index(cdir)
    gmap = group_map(cdir)
    sent_ids = {p.get("person_id") for p in expected_people(cdir)[0]}
    out_rows = [r for r in rows if r.get("person_id") not in sent_ids]

    pools: dict[str, list[dict]] = defaultdict(list)
    for r in out_rows:
        rw = raw.get(r.get("person_id", ""), {})
        head = rw.get("headline", "")
        pools[bucket_of(r.get("title", ""), head)].append(r | {
            "_headline": clip(head, 110),
            "_senior": bool(SENIOR.search(r.get("title", "") + " " + head)),
            "_group": group_of(r, gmap),
            "_hold": (r.get("send") or r.get("decision") or "").strip(),
        })

    order = sorted(pools, key=lambda b: (-sum(1 for x in pools[b] if x["_senior"]), -len(pools[b])))
    md = [f"# Skipped people — {cdir.name}", "",
          f"{len(out_rows)} of {len(rows)} people are not being sent. Grouped by function, "
          "seniors first. Generated by `outbound_pack.py skipped`, " + today() + ".", ""]
    summary = []
    for b in order:
        ppl = pools[b]
        seniors = sorted((x for x in ppl if x["_senior"]), key=lambda x: (x["_group"], x["title"]))
        others = [x for x in ppl if not x["_senior"]]
        md += [f"## {b}: {len(ppl)} ({len(seniors)} senior)", ""]
        if seniors:
            md += ["| Person | Title | Company | Status | Why left out |", "|---|---|---|---|---|"]
            for x in seniors:
                md.append(f"| {x.get('full_name','')} | {clip(x.get('title',''), 70)} | "
                          f"{x['_group']} | {x['_hold'] or 'FAIL'} | {clip(x.get('reason',''), 140)} |")
            md.append("")
        if others:
            md += ["Others: " + "; ".join(
                f"{x.get('full_name','')} ({clip(x.get('title',''), 45)}, {x['_group']})"
                for x in sorted(others, key=lambda x: x["_group"])), ""]
        names = "; ".join(f"{x.get('full_name','')} ({clip(x.get('title',''), 34)}, {x['_group']})"
                          for x in seniors[:3])
        summary.append(f"  {b:28s} {len(ppl):4d}  senior {len(seniors):3d}"
                       + (f"  e.g. {names}" if names else ""))
    dst = cdir / "skipped-detail.md"
    dst.write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"✓ {rel(dst)}: {len(out_rows)} not sent, {sum(1 for p in pools.values() for x in p if x['_senior'])} of them senior")
    text = "\n".join(summary)
    while len(text) > 2200 and len(summary) > 4:          # whole lines, never half of one
        summary.pop()
        text = "\n".join(summary) + "\n  … smaller pools in the file"
    print(text)
    print("\nPut the senior pools in the FIRST report to Vadim, with a proposed angle per pool.\n"
          "He adds by name: scripts/outbound_pack.py promote --campaign "
          f"{cdir.name} --names \"A; B\" --angle referral --wave 2 --pool X")
    return 0


# ================================================================== promote

def find_person(rows: list[dict], needle: str) -> list[dict]:
    n = needle.strip().lower()
    exact = [r for r in rows if (r.get("person_id") or "").lower() == n
             or (r.get("full_name") or "").strip().lower() == n]
    if exact:
        return exact
    toks = [t for t in re.split(r"\s+", n) if t]
    return [r for r in rows
            if all(t in (r.get("full_name") or "").lower() for t in toks)]


def cmd_promote(args) -> int:
    cdir = cdir_of(args.campaign)
    dst = cdir / "people-validated.csv"
    rows = validated_rows(cdir)
    if not rows:
        print(f"✗ no people-validated.csv in {rel(cdir)}", file=sys.stderr)
        return 2
    asks: list[dict] = []
    if args.file:
        for r in read_csv(Path(args.file)):
            asks.append({"who": pick(r, "person_id", "name", "full_name"),
                         "angle": r.get("angle") or args.angle, "wave": r.get("wave") or args.wave,
                         "priority": r.get("priority") or args.priority,
                         "pool": r.get("pool") or args.pool,
                         "release_note": r.get("release_note") or args.release_note})
    for n in re.split(r"[;\n]", args.names or ""):
        if n.strip():
            asks.append({"who": n.strip(), "angle": args.angle, "wave": args.wave,
                         "priority": args.priority, "pool": args.pool,
                         "release_note": args.release_note})
    if not asks:
        print("✗ nobody named: --names \"A; B\" or --file pool.csv", file=sys.stderr)
        return 2

    _, fm = hypothesis_of(cdir)
    profile = profile_of(cdir, fm)
    raw = raw_index(cdir)
    gmap = group_map(cdir)
    urls = legit_company_pages(rows, raw, gmap, shortlist_company_urls(cdir))
    problems, changes, notes = [], [], []
    for a in asks:
        hits = find_person(rows, a["who"])
        if not hits:
            problems.append(f"«{a['who']}»: nobody by that name in people-validated.csv")
            continue
        if len(hits) > 1:
            problems.append(f"«{a['who']}» matches {len(hits)} people: "
                            + ", ".join(f"{h['full_name']} [{h['person_id']}]" for h in hits[:4])
                            + ". Use the person_id.")
            continue
        r = hits[0]
        if (r.get("exclusion_flag") or "").strip():
            problems.append(f"{r['full_name']}: excluded by the registry "
                            f"({r.get('exclusion_reason')}). Not promotable.")
            continue
        if not (a["angle"] or r.get("recommended_message_angle")):
            problems.append(f"{r['full_name']}: no angle given and none on the row")
            continue
        flags = person_flags(r, raw.get(r["person_id"], {}), profile, group_of(r, gmap), urls)
        hard = [f for f in flags if f.startswith(("other-company-page", "empty-profile",
                                                  "not-in-raw-export"))]
        if hard and not args.force:
            problems.append(f"{r['full_name']} ({r.get('title')}): {', '.join(hard)}. "
                            "Check the profile, then repeat with --force.")
            continue
        if flags:
            notes.append(f"{r['full_name']}: {', '.join(flags)}")
        changes.append((r, a, flags))

    if problems:
        for p in problems:
            print(f"  ✗ {p}")
        print(f"\n✗ nothing written: {len(problems)} of {len(asks)} need a decision first.",
              file=sys.stderr)
        return 1

    for r, a, flags in changes:
        was = (r.get("send") or r.get("decision") or "FAIL").strip()
        r["decision"] = "PASS"
        r["send"] = "SEND"
        r["priority"] = str(a["priority"] or r.get("priority") or "3")
        r["recommended_message_angle"] = a["angle"] or r.get("recommended_message_angle", "")
        r["wave"] = str(a["wave"] or r.get("wave") or "1")
        if a["pool"]:
            r["pool"] = a["pool"]
        if a["release_note"]:
            r["release_note"] = a["release_note"]
        r["group"] = group_of(r, gmap)
        if flags:
            r["flags"] = " ".join(flags)
        r["reason"] = clip(f"Added by Vadim {today()}"
                           + (f" (pool {a['pool']})" if a["pool"] else "")
                           + f"; was {was}: {r.get('reason', '')}", 300)

    send = [r for r in rows if (r.get("send") or "").upper() == "SEND"]
    if args.dry_run:
        print(f"(dry run) would add {len(changes)} people; to send would be {len(send)}")
        _print_distribution(cdir, send)
        return 0
    over = _cap_broken(cdir, send)
    if over and not args.allow_over_cap:
        _print_distribution(cdir, send)
        print("\n✗ nothing written: a group would go over cap_per_group. Raise the cap in the\n"
              "  hypothesis frontmatter (Vadim's call) or repeat with --allow-over-cap.",
              file=sys.stderr)
        return 1
    snap = snapshot(dst)
    cols = list(rows[0].keys())
    for c in ("send", "wave", "pool", "release_note", "group", "flags"):
        if c not in cols:
            cols.append(c)
    write_csv(dst, rows, cols)
    print(f"✓ {len(changes)} people added to SEND" + (f" · previous kept as {snap.name}" if snap else ""))
    for n in notes[:8]:
        print(f"  ⚠ {n}")
    _print_distribution(cdir, send)
    return 0


def _cap_broken(cdir: Path, send: list[dict]) -> bool:
    cap = cap_of(cdir)
    if not cap:
        return False
    gmap = group_map(cdir)
    return any(n > cap for n in Counter(group_of(r, gmap) for r in send).values())


# ================================================================== profiles (step 5 input)

def batch_plan(people: list[dict], gmap: dict[str, str], max_size: int) -> dict[str, list[dict]]:
    by: dict[str, list[dict]] = defaultdict(list)
    for p in people:
        by[group_of(p, gmap)].append(p)
    plan: dict[str, list[dict]] = {}
    small: list[tuple[str, list[dict]]] = []
    for g, ppl in sorted(by.items(), key=lambda kv: -len(kv[1])):
        if len(ppl) >= max(12, max_size // 2):
            chunks = [ppl[i:i + max_size] for i in range(0, len(ppl), max_size)]
            for i, ch in enumerate(chunks, start=1):
                name = re.sub(r"[^a-z0-9]+", "-", g.lower()).strip("-")
                plan[name if len(chunks) == 1 else f"{name}-{i}"] = ch
        else:
            small.append((g, ppl))
    cur: list[dict] = []
    n = 1
    for g, ppl in small:
        if cur and len(cur) + len(ppl) > max_size:
            plan[f"mixed-{n}"] = cur
            cur, n = [], n + 1
        cur += ppl
    if cur:
        prev = f"mixed-{n - 1}"
        if len(cur) < 8 and prev in plan:
            plan[prev] += cur          # three people are not worth an agent of their own
        else:
            plan[f"mixed-{n}" if (n > 1 or plan) else "all"] = cur
    return plan


def cmd_profiles(args) -> int:
    cdir = cdir_of(args.campaign)
    people, src = expected_people(cdir)
    if not people:
        print(f"✗ nobody to write for ({src})", file=sys.stderr)
        return 2
    raw = raw_index(cdir)
    gmap = group_map(cdir)
    plan = batch_plan(people, gmap, args.max)
    mdir = cdir / "messages"
    mdir.mkdir(exist_ok=True)
    # The list the messages are written for. Kept as a file because the importer of older
    # campaigns and the registry both read it.
    write_csv(cdir / "people-approved.csv", people, list(people[0].keys()))

    index = {}
    print(f"✓ {len(people)} people from {src} → {len(plan)} batch(es)")
    for name, ppl in plan.items():
        out = [f"# Profiles — batch `{name}` — {cdir.name}", "",
               f"{len(ppl)} people. One card each. Write `messages/_batch-{name}.md` for exactly "
               "these person_ids.", ""]
        groups = Counter(group_of(p, gmap) for p in ppl)
        if max(groups.values()) > 3:
            out += ["Several people here work at the same company. Give each a different hook and",
                    "a different central argument, and do not open two Message 2s the same way:",
                    "a forwarded screenshot must not read as a mail merge.", ""]
        for p in sorted(ppl, key=lambda x: (group_of(x, gmap), wave_of(x), x.get("priority", "9"))):
            pid = p["person_id"]
            r = raw.get(pid, {})
            exp = [x for x in strip_employment(r.get("experience", "")).split(", ") if x]
            head = clip(r.get("headline", ""), 140)
            out += [f"### {pid}",
                    f"{p.get('full_name','')} · first name: {p.get('first_name','')} · "
                    f"{clip(p.get('title',''), 90)} · {p.get('company_name','')}"
                    f" ({group_of(p, gmap)}) · {clip(r.get('location') or p.get('person_location',''), 30)}",
                    f"angle: **{p.get('recommended_message_angle','?')}**"
                    f" · P{p.get('priority') or '?'}",
                    f"why on the list: {clip(p.get('reason',''), 220)}"]
            if head and head.lower() != (p.get("title") or "").lower():
                out.append(f"headline: {head}")
            if r.get("bio", "").strip():
                out.append(f"bio: {clip(r['bio'], args.bio)}")
            if len(exp) > 1:
                out.append(f"earlier: {clip(', '.join(exp[1:4]), 200)}")
            if p.get("flags"):
                out.append(f"flags: {p['flags']} (write neutral, title-based copy)")
            out.append("")
        f = mdir / f"_profiles-{name}.md"
        f.write_text("\n".join(out), encoding="utf-8")
        index[name] = [p["person_id"] for p in ppl]
        print(f"  {name:22s} {len(ppl):3d} people  {f.stat().st_size:7,} bytes  "
              + ", ".join(f"{g} {n}" for g, n in groups.most_common(5)))
    (mdir / "_batches.json").write_text(json.dumps(index, indent=1), encoding="utf-8")
    ok, why = card_is_fresh(cdir, "messages")
    if not ok:
        print(f"\n  ⚠ card-messages.md is {why}: run `outbound_pack.py card --campaign "
              f"{cdir.name} --for messages` before the agents start")
    print("\nOne message-sequencer per batch, in parallel. Each reads card-messages.md and its\n"
          "own _profiles-<batch>.md, and nothing else.")
    return 0


# ================================================================== split + check messages

PERSON_FILE = """\
# {full_name} — {title} — {company}

## Context used
- Angle: {angle}
- Hook: {hook}
- Proof point: {proof}

---

## Connection request (Day 0)
_Без note — отправляем запрос в друзья без сопроводительного текста._

## Message 1 — Opener (сразу после принятия запроса)
{m1}

**Char count:** {n1} / 600

## Message 2 — Value + demo call (+5 дней, если нет ответа)
{m2}

**Char count:** {n2} / 550
"""


def parse_batch(text: str) -> tuple[dict[str, dict], list[str]]:
    out: dict[str, dict] = {}
    errs: list[str] = []
    parts = re.split(r"(?m)^@@@[ \t]*(\S+)[ \t]*$", text)
    for i in range(1, len(parts), 2):
        pid, body = parts[i].strip().lower(), parts[i + 1]
        m = re.search(r"(?ms)^(.*?)^---[ \t]*M1[ \t]*$(.*?)^---[ \t]*M2[ \t]*$(.*)\Z", body)
        if not m:
            errs.append(f"{pid}: needs `--- M1` and `--- M2` markers, each on its own line")
            continue
        head = dict(re.findall(r"(?m)^(hook|proof)\s*:\s*(.+)$", m.group(1)))
        if pid in out:
            errs.append(f"{pid}: appears twice in the batch file")
        out[pid] = {"hook": head.get("hook", "").strip(), "proof": head.get("proof", "").strip(),
                    "m1": m.group(2).strip(), "m2": m.group(3).strip()}
    return out, errs


def cmd_split_messages(args) -> int:
    cdir = cdir_of(args.campaign)
    src = Path(args.infile)
    if not src.exists():
        src = cdir / args.infile
    if not src.exists():
        print(f"✗ no batch file {args.infile}", file=sys.stderr)
        return 2
    batch = re.sub(r"^_batch-|\.md$", "", src.name)
    people, _ = expected_people(cdir)
    by_id = {p["person_id"]: p for p in people}
    parsed, errs = parse_batch(src.read_text(encoding="utf-8"))
    unknown = [p for p in parsed if p not in by_id]
    for u in unknown:
        close = difflib.get_close_matches(u, list(by_id), n=1, cutoff=0.8)
        errs.append(f"{u}: not on the send list" + (f" (did you mean {close[0]}?)" if close else ""))
    gmap = group_map(cdir)
    mdir = cdir / "messages"
    mdir.mkdir(exist_ok=True)
    written = 0
    for pid, m in parsed.items():
        p = by_id.get(pid)
        if not p:
            continue
        (mdir / f"{pid}.md").write_text(PERSON_FILE.format(
            full_name=p.get("full_name", ""), title=p.get("title", ""),
            company=p.get("company_name", ""),
            angle=p.get("recommended_message_angle", ""), wave=wave_of(p),
            hook=m["hook"] or "—", proof=m["proof"] or "—",
            m1=m["m1"], n1=len(m["m1"]), m2=m["m2"], n2=len(m["m2"])), encoding="utf-8")
        written += 1
    print(f"→ {rel(src)}: {written} people written to messages/")
    for e in errs[:12]:
        print(f"  ✗ {e}")
    rc = run_check(cdir, batch=batch, quiet_ok=False)
    return 1 if errs else rc


def load_detector():
    p = ROOT / "brand-assets" / "style-guides" / "scripts" / "detect-ai-tells.py"
    return _load("detect_ai_tells", p) if p.exists() else None


def client_names() -> list[str]:
    names = set(REG.EXISTING_CUSTOMERS) | {"Erakulis"}
    cs = ROOT / "brand-assets" / "product-info" / "case-studies"
    for f in cs.glob("*.md") if cs.exists() else []:
        m = re.search(r"(?m)^# (?:Case Study[:—-]\s*)?(.+)$", f.read_text(encoding="utf-8"))
        if m:
            names.add(re.sub(r"\s*[\(—-].*$", "", m.group(1)).strip())
    return sorted(n for n in names if len(n) > 3)


def competitor_names() -> list[str]:
    f = ROOT / "brand-assets" / "competitors" / "list.md"
    if not f.exists():
        return ["Prism Labs", "Bodygram", "Size Stream"]
    direct = md_section(f, "Direct competitors")
    return re.findall(r"(?m)^### (.+)$", direct) or ["Prism Labs", "Bodygram", "Size Stream"]


# Exactly what outbound-message1-template.md bans, no more. The same template LISTS
# "Noticed your background" and "Came across your work" among its hook phrases, so they are
# not failures: on 2026-09-28 this gate (and the coordinator before it) treated them as
# generic and was wrong about the rule.
GENERIC_OPENER = re.compile(
    r"^(i hope this (finds|message)|hope (you('re| are)|this finds) |"
    r"i came across your profile|came across your profile|i noticed you work at|"
    r"i help companies|i admire your|excited about your)", re.I)
# "80+ body measurements per scan" is a product fact, not a price: «per scan» alone is not
# a hit. A currency amount or a trial offer is.
PRICE_HARD = re.compile(r"[$€£]\s?\d|\d\s?(usd|eur|gbp)\b|free trial", re.I)
# Lower case only for "tier": "TIER Mobility" is a former employer, not a price plan.
PRICE_SOFT = re.compile(r"\b[Pp]ric(e|es|ing)\b|\btiers?\b")


# What "a product specific" is, mechanically. The 2026-07-21 campaign sent 307 first
# messages and none carried one; it drew 1 reply from 67 sends.
NUMBER_FACT = re.compile(
    r"\b\d[\d,.]*\+?\s?(%|body measurements|measurements|scans|seconds|sec\b|weeks?|days?|"
    r"photos|minutes?)|\b\d+-\d+\s?(weeks?|%)|\bunder \d+", re.I)
PRODUCT_SPECIFIC = re.compile(
    r"two (phone |smartphone )?photos|2 photos|3D (body |progress |model)|body composition|"
    r"body measurements|lean mass|fat mass|SDK|API", re.I)


def first_sentence(body: str) -> str:
    paras = [p.strip() for p in body.split("\n\n") if p.strip()]
    text = paras[1] if len(paras) > 1 and re.match(r"(hi|hello|hey)\b", paras[0], re.I) \
        else (paras[0] if paras else "")
    return re.split(r"(?<=[.?!:])\s", text, maxsplit=1)[0].strip()


def read_messages(path: Path) -> dict[int, str]:
    text = path.read_text(encoding="utf-8")
    return {int(n): b.strip() for n, b in
            re.findall(r"## Message (\d)[^\n]*\n(.*?)\n\*\*Char count", text, re.S)}


def run_check(cdir: Path, batch: str | None = None, quiet_ok: bool = False) -> int:
    people, src = expected_people(cdir)
    _, fm = hypothesis_of(cdir)
    profile = profile_of(cdir, fm)
    mdir = cdir / "messages"
    if batch:
        idx = mdir / "_batches.json"
        ids = set(json.loads(idx.read_text()).get(batch, [])) if idx.exists() else set()
        if not ids:
            print(f"  ⚠ batch «{batch}» is not in messages/_batches.json: checking every person")
        else:
            people = [p for p in people if p["person_id"] in ids]
    gmap = group_map(cdir)
    owner = OWNER.get(profile, "")
    link = calendar_link(profile)
    banned = fm.get("banned_terms") or []
    banned = [banned] if isinstance(banned, str) else banned
    clients = [c for c in client_names()]
    rivals = competitor_names()
    det = load_detector()
    # The number rule belongs to the campaign, not to the pipeline. A hypothesis that
    # carries a message gate ("every message 1 carries a product specific") makes it a
    # failure; without one it is a note, because `2026-09-27-uk-bariatric-prequal` was
    # approved and sent with 18 article-led pairs that cite no number.
    hyp_text = hypothesis_of(cdir)[0]
    demands_specific = bool(re.search(r"message 1 gate|product specific", hyp_text, re.I)) \
        or str(fm.get("message_gate", "")).lower() in ("specific", "number", "true", "yes")

    hard: list[tuple[str, str, str]] = []      # (code, person, detail)
    soft: list[tuple[str, str, str]] = []
    bodies: dict[tuple[str, int], str] = {}
    lens = {1: [], 2: []}

    for p in people:
        pid = p["person_id"]
        f = mdir / f"{pid}.md"
        if not f.exists():
            hard.append(("missing", pid, f"no message file for {p.get('full_name')}"))
            continue
        msgs = read_messages(f)
        for n in (1, 2):
            b = msgs.get(n, "")
            if not b:
                hard.append(("missing", pid, f"Message {n} is empty"))
                continue
            bodies[(pid, n)] = b
            lens[n].append(len(b))
            tag = f"{pid} M{n}"
            if len(b) > CAPS[n]:
                hard.append(("too long", tag, f"{len(b)} / {CAPS[n]}"))
            lines = [x.strip() for x in b.splitlines() if x.strip()]
            if owner and lines[-1] != owner:
                hard.append(("signature", tag, f"last line is «{clip(lines[-1], 40)}», not «{owner}»"))
            first = re.sub(r"^(dr|prof|mr|mrs|ms)\.?\s+", "",
                           (p.get("first_name") or "").strip(), flags=re.I)
            if first and first.split()[0].lower() not in lines[0].lower():
                soft.append(("greeting", tag, f"«{clip(lines[0], 40)}» has no «{first}»"))
            if not det and re.search(r"[—–]", b):          # the detector reports it itself
                hard.append(("dash", tag, "em or en dash"))
            for name in clients:
                if re.search(rf"\b{re.escape(name)}\b", b, re.I) and \
                        norm_company(name) not in norm_company(p.get("company_name", "")):
                    hard.append(("client named", tag, name))
            for name in rivals:
                if re.search(rf"\b{re.escape(name)}\b", b, re.I):
                    hard.append(("competitor named", tag, name))
            for term in banned:
                if re.search(rf"\b{re.escape(term)}\b", b, re.I):
                    hard.append(("campaign ban", tag, term))
            m = PRICE_HARD.search(b)
            if m:
                hard.append(("pricing", tag, m.group(0)))
            else:
                m = PRICE_SOFT.search(b)
                if m:
                    s = next((x for x in re.split(r"(?<=[.?!])\s", b) if m.group(0) in x), "")
                    soft.append(("pricing word", tag, clip(s, 110)))
            # A note, not a failure: messaging.md itself carries "Two photos. 80+
            # measurements. 45 seconds." The guardrails (§2.13) ban "80+ body metrics" and
            # name "80+ body measurements" as the approved claim, so that is the preference.
            if re.search(r"80\+\s+measurements", b, re.I):
                soft.append(("terminology", tag, "«80+ measurements»: §2.13 prefers «80+ body measurements»"))
            fs = first_sentence(b)
            if GENERIC_OPENER.search(fs):
                hard.append(("generic opener", tag, clip(fs, 70)))
            if det:
                r = det.analyze(b, "en", "dm", profile)
                for hf in r.get("hard_fails", []):
                    marks = ", ".join(sorted({h["marker"] for h in hf["hits"]})[:3])
                    hard.append((f"detector: {hf['category']}", tag, marks))
                for v in r.get("house_rule_violations", []):
                    hard.append(("detector: house rule", tag, clip(str(v), 90)))
        angle = (p.get("recommended_message_angle") or "").lower()
        if angle != "referral" and msgs.get(1) and msgs.get(2):
            m1 = re.sub(r"https?://\S+", "", msgs[1])
            pair = m1 + " " + re.sub(r"https?://\S+", "", msgs[2])
            sink = hard if demands_specific else soft
            if not (NUMBER_FACT.search(m1) or PRODUCT_SPECIFIC.search(m1)):
                sink.append(("no product specific", f"{pid} M1",
                             "say what the scan returns, from the card's facts"))
            if not NUMBER_FACT.search(pair):
                sink.append(("no number", f"{pid}",
                             "neither message cites a number from the card's facts"))
        m2 = msgs.get(2, "")
        if link and m2 and link not in m2:
            (soft if angle == "referral" else hard).append(
                ("no calendar link", f"{pid} M2", f"angle {angle or '?'}"))

    dup: dict[str, list[str]] = defaultdict(list)
    for (pid, n), b in bodies.items():
        dup[re.sub(r"\s+", " ", b.split("\n\n", 1)[-1]).lower()].append(f"{pid} M{n}")
    for who in dup.values():
        if len(who) > 1:
            hard.append(("identical text", who[0], "same body as " + ", ".join(who[1:4])))

    for n in (1, 2):
        per_group: dict[tuple[str, str], list[str]] = defaultdict(list)
        overall: dict[str, list[str]] = defaultdict(list)
        for p in people:
            b = bodies.get((p["person_id"], n))
            if not b:
                continue
            fs = first_sentence(b).lower()
            per_group[(group_of(p, gmap), fs)].append(p["person_id"])
            overall[fs].append(p["person_id"])
        for (g, fs), who in per_group.items():
            if len(who) >= 3:
                soft.append((f"M{n} opener repeated", f"{g} ×{len(who)}",
                             f"«{clip(fs, 50)}»: " + ", ".join(who[:4])))
        for fs, who in overall.items():
            if len(who) >= max(4, len(people) // 8) and all(
                    len(v) < 3 for (g, f2), v in per_group.items() if f2 == fs):
                soft.append((f"M{n} opener repeated", f"campaign ×{len(who)}", f"«{clip(fs, 50)}»"))

    report = {"campaign": cdir.name, "checked": len(people), "source": src, "batch": batch,
              "generated": dt.datetime.now().isoformat(timespec="seconds"),
              "hard": [list(x) for x in hard], "soft": [list(x) for x in soft]}
    mdir.mkdir(exist_ok=True)
    (mdir / ("_check.json" if not batch else f"_check-{batch}.json")).write_text(
        json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")

    def digest(items, mark, limit):
        by = defaultdict(list)
        for code, who, detail in items:
            by[code].append(f"{who}: {detail}")
        out = []
        for code, lst in sorted(by.items(), key=lambda kv: -len(kv[1])):
            out.append(f"  {mark} {code} ×{len(lst)}")
            out += [f"      {x}" for x in lst[:limit]]
            if len(lst) > limit:
                out.append(f"      … {len(lst) - limit} more in the report file")
        return out

    avg = lambda xs: sum(xs) // len(xs) if xs else 0
    print(f"→ checked {len(people)} people" + (f" (batch {batch})" if batch else "")
          + f" · M1 avg {avg(lens[1])}, max {max(lens[1], default=0)}"
          f" · M2 avg {avg(lens[2])}, max {max(lens[2], default=0)}"
          + ("" if det else " · ⚠ detector not found, skipped"))
    lines = digest(hard, "✗", 6) + digest(soft, "⚠", 3)
    text = "\n".join(lines)
    if text:
        print(text if len(text) < 2400 else text[:2400] + "\n  … (rest in the report file)")
    print("-" * 66)
    if hard:
        print(f"✗ {len(hard)} hard failure(s) in "
              f"{len({w.split()[0] for _, w, _ in hard})} people. Fix them and run again.",
              file=sys.stderr)
        return 1
    print(f"✓ messages pass the gate: {len(people)} people, {len(bodies)} messages"
          + (f", {len(soft)} soft note(s) for Vadim" if soft else ""))
    return 0


def cmd_check_messages(args) -> int:
    return run_check(cdir_of(args.campaign), batch=args.batch)


# ================================================================== qc-prompt

QC_AGENT = {"hypothesis": "hypothesis-generator", "validate": "icp-validator",
            "messages": "message-sequencer"}


def cmd_qc_prompt(args) -> int:
    """The prompt for `quality-controller` (opus) after a stage.

    Auto-QC stays on the opus controller for outbound: Vadim's decision, 2026-09-28. What
    this command fixes is what the controller reads. It judges an artifact against what
    the agent was GIVEN, and since the same date that is a card and a compact list, not
    the hypothesis and the raw export. Pointed at the old inputs it would mark the agent
    down for not using material it never saw, and read 800 KB to do it.
    """
    cdir = cdir_of(args.campaign)
    base = rel(cdir)
    stage = args.stage
    if stage == "hypothesis":
        artifact = [f"{base}/hypothesis.md"]
        inputs = ["brand-assets/product-info/icp-detail.md (the segment the hypothesis names)",
                  "brand-assets/product-info/proof-points.md"]
        kind = "hypothesis"
    elif stage == "validate":
        need = [cdir / "icp-validation-summary.md", cdir / "people-validated.csv"]
        if not all(p.exists() for p in need):
            print("✗ step 4 has not finished: no icp-validation-summary.md / "
                  "people-validated.csv", file=sys.stderr)
            return 1
        dec = next((n for n in ("decisions.md", "decisions.txt", "decisions.csv")
                    if (cdir / n).exists()), None)
        artifact = [f"{base}/icp-validation-summary.md"] + ([f"{base}/{dec}"] if dec else [])
        inputs = [f"{base}/card-validate.md", f"{base}/people-compact.csv"]
        kind = "icp-validation"
    else:
        people, _ = expected_people(cdir)
        by: dict[str, list[dict]] = defaultdict(list)
        for p in people:
            if (cdir / "messages" / f"{p['person_id']}.md").exists():
                by[(p.get("recommended_message_angle") or "?").lower()].append(p)
        if not by:
            print("✗ step 5 has not finished: no message files", file=sys.stderr)
            return 1
        # One person per angle, the three largest angles, the best-ranked person in each:
        # deterministic, so a re-run judges the same three.
        angles = sorted(by, key=lambda a: (a == "referral", -len(by[a]), a))[:3]
        pick3 = [sorted(by[a], key=lambda p: (str(p.get("priority") or "9"), p["person_id"]))[0]
                 for a in angles]
        artifact = [f"{base}/messages/{p['person_id']}.md  ({p.get('recommended_message_angle')})"
                    for p in pick3]
        artifact.append(f"{base}/messages/_check.json  (the mechanical gate's findings)")
        artifact += [f"{base}/messages/{f.name}" for f in sorted((cdir / "messages").glob("_summary*.md"))]
        idx = cdir / "messages" / "_batches.json"
        batches = json.loads(idx.read_text()) if idx.exists() else {}
        prof = sorted({f"{base}/messages/_profiles-{b}.md" for b, ids in batches.items()
                       if any(p["person_id"] in ids for p in pick3)})
        inputs = [f"{base}/card-messages.md"] + prof
        kind = "messages"

    print(f"Use the quality-controller subagent to evaluate step «{stage}» of {cdir.name}.")
    print(f"Pass: agent_name={QC_AGENT[stage]}, track=outbound, artifact_type={kind}.\n")
    print("Artifact to score:")
    for a in artifact:
        print(f"  - {a}")
    print("\nWhat the agent was given (score against THIS, not against hypothesis.md or the\n"
          "raw export, which the agent does not read since 2026-09-28):")
    for i in inputs:
        print(f"  - {i}")
    print("\nLimits, signature, bans, detector and completeness are already checked by code:\n"
          "take them as fact and score the judgment, the fit to the persona and the copy.")
    print(f"\nReport: workspace/_quality/outbound/{today()}-{QC_AGENT[stage]}-"
          f"{re.sub(r'^\d{4}-\d{2}-\d{2}-', '', cdir.name)}.md")
    return 0


# ================================================================== build-import

IMPORT_COLS = ["first_name", "last_name", "linkedin_url", "company", "title", "email",
               "connection_note", "message_1", "message_2"]


def cmd_build_import(args) -> int:
    cdir = cdir_of(args.campaign)
    people, src = expected_people(cdir)
    if not people:
        print(f"✗ nobody to import ({src})", file=sys.stderr)
        return 2
    if run_check(cdir) != 0 and not args.force:
        print("✗ import not built: the messages do not pass the gate (above).", file=sys.stderr)
        return 1
    out_dir = Path(args.out_dir) if args.out_dir else cdir
    out_dir.mkdir(parents=True, exist_ok=True)
    files: dict[str, list[dict]] = defaultdict(list)
    seen = set()
    for p in people:
        pid = p["person_id"]
        if pid in seen:
            continue
        seen.add(pid)
        msgs = read_messages(cdir / "messages" / f"{pid}.md")
        row = {"first_name": p.get("first_name", ""), "last_name": p.get("last_name", ""),
               "linkedin_url": pick(p, "linkedin_url", "person_linkedin_url"),
               "company": p.get("company_name", ""), "title": p.get("title", ""),
               "email": p.get("email_guess", ""), "connection_note": "",
               "message_1": msgs.get(1, ""), "message_2": msgs.get(2, "")}
        # One file, everyone at once. Vadim 2026-09-29: «хвиль робити не потрібно, давай
        # всіх в один файл» — per-wave CSVs were awkward to launch in closely.io. The
        # `wave` column may still be filled in older lists; it no longer splits anything.
        files["closelyhq-import.csv"].append(row)

    existing = [n for n in files if (out_dir / n).exists()]
    if existing and not args.overwrite:
        print(f"✗ {', '.join(existing)} already exist in {rel(out_dir)}. They may have been\n"
              "  imported into closely.io already. --overwrite replaces them.", file=sys.stderr)
        return 1

    rc = 0
    log = [f"# Closely.io import — {cdir.name}", "",
           f"Built {today()} by `outbound_pack.py build-import` from {src} "
           f"and `messages/`. {len(seen)} people, 0 skipped.", "",
           "Sequence: connection request with no note → Message 1 right after acceptance → "
           "Message 2 five days later.", "", "| File | People | When |", "|---|---:|---|"]
    for name in sorted(files):
        rows = files[name]
        write_csv(out_dir / name, rows, IMPORT_COLS)
        log.append(f"| `{name}` | {len(rows)} | now, everyone at once |")
        res = PIPE.cmd_check_import(SimpleNamespace(
            file=str((out_dir / name).resolve()), campaign=None, infile=None)) \
            if args.verbose else _quiet(PIPE.cmd_check_import, SimpleNamespace(
                file=str((out_dir / name).resolve()), campaign=None, infile=None))
        print(f"  {'✓' if res == 0 else '✗'} {name}: {len(rows)} rows, check-import exit {res}")
        rc = rc or res
    profile = profile_of(cdir)
    log += ["", "## After the import", "", "```",
            f"scripts/outbound-registry.py record --campaign {cdir.name} --profile {profile}",
            "```", ""]
    if not args.out_dir:
        (cdir / "import-log.md").write_text("\n".join(log), encoding="utf-8")
    over = _print_distribution(cdir, people)
    if over and not args.allow_over_cap:
        print("✗ a group is over cap_per_group: files written, but do not import them until\n"
              "  Vadim raises the cap or the list is cut.", file=sys.stderr)
        return 1
    return rc


def _quiet(fn, ns) -> int:
    import contextlib
    import io
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
        rc = fn(ns)
    if rc != 0:
        print(buf.getvalue()[-1500:])
    return rc


# ================================================================== main

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        prog="outbound_pack.py",
        description="Compact inputs and mechanical gates for outbound steps 2-6.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    def camp(p, required=True):
        p.add_argument("--campaign", required=required)
        return p

    n = camp(sub.add_parser("next", help="where a campaign stands and the next command"), False)
    n.add_argument("--find", help='words from a request, e.g. "лена еракуліс"')
    n.set_defaults(func=cmd_next)

    camp(sub.add_parser("sales-nav-query",
                        help="the title filter for Sales Navigator")).set_defaults(
        func=cmd_sales_nav_query)
    camp(sub.add_parser("compact", help="step 4 input: one short row per person")).set_defaults(
        func=cmd_compact)

    c = camp(sub.add_parser("card", help="the campaign's rules for one stage"))
    c.add_argument("--for", dest="stage", choices=("validate", "messages"), required=True)
    c.add_argument("--check", action="store_true", help="exit 1 if the card is stale")
    c.set_defaults(func=cmd_card)

    a = camp(sub.add_parser("apply-decisions", help="decisions.csv -> people-validated.csv"))
    a.add_argument("--in", dest="infile")
    a.set_defaults(func=cmd_apply_decisions)

    camp(sub.add_parser("skipped", help="who was left out, by function")).set_defaults(
        func=cmd_skipped)

    p = camp(sub.add_parser("promote", help="add named people to SEND, no agent round"))
    p.add_argument("--names", help='"Name A; Name B" or person_ids')
    p.add_argument("--file", help="CSV: name|person_id, angle, wave, priority, pool")
    p.add_argument("--angle")
    p.add_argument("--wave", default="")
    p.add_argument("--priority", default="")
    p.add_argument("--pool", default="")
    p.add_argument("--release-note", dest="release_note", default="")
    p.add_argument("--force", action="store_true", help="accept flagged profiles")
    p.add_argument("--allow-over-cap", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    p.set_defaults(func=cmd_promote)

    pr = camp(sub.add_parser("profiles", help="step 5 input: batch plan + profile cards"))
    pr.add_argument("--max", type=int, default=35, help="people per batch (default 35)")
    pr.add_argument("--bio", type=int, default=320, help="bio characters kept (default 320)")
    pr.set_defaults(func=cmd_profiles)

    s = camp(sub.add_parser("split-messages", help="batch file -> per-person files + gate"))
    s.add_argument("--in", dest="infile", required=True)
    s.set_defaults(func=cmd_split_messages)

    k = camp(sub.add_parser("check-messages", help="the mechanical gate on messages"))
    k.add_argument("--batch")
    k.set_defaults(func=cmd_check_messages)

    q = camp(sub.add_parser("qc-prompt", help="the prompt for quality-controller after a stage"))
    q.add_argument("--stage", choices=("hypothesis", "validate", "messages"), required=True)
    q.set_defaults(func=cmd_qc_prompt)

    b = camp(sub.add_parser("build-import", help="one closely.io CSV + check-import"))
    b.add_argument("--overwrite", action="store_true")
    b.add_argument("--force", action="store_true", help="build even if the gate fails")
    b.add_argument("--allow-over-cap", action="store_true")
    b.add_argument("--out-dir", help="write the CSVs elsewhere (for a comparison)")
    b.add_argument("--verbose", action="store_true")
    b.set_defaults(func=cmd_build_import)

    args = ap.parse_args(argv)
    # One stream, so a verdict never prints above the findings it sums up: the caller is
    # usually an agent reading both.
    sys.stdout.flush()
    sys.stderr = sys.stdout
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
