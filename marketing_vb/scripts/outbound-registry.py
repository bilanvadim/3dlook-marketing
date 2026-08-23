#!/usr/bin/env python3
"""
outbound-registry.py — the exclusion registry's only writer, plus a campaign status board.

Why this exists as a script and not as agent instructions:

`workspace/outbound/exclusions/README.md` specifies the whole subsystem — per-profile
registries, a global company registry, which agent updates what. None of it was implemented.
As of 2026-08-23 not one of the eight mvb-outbound agents referenced `exclusions/` at all;
`company-researcher` and `campaign-analyzer` pointed at `workspace/outbound/exclusions.md`,
a flat file that has never existed, so every read silently returned nothing and every write
went nowhere. Ten campaigns ran and the registries still said `excluded_people: 0`.

Four agent prompts hand-editing the same JSON is exactly how that happened, so the agents now
call this instead. One writer, one schema.

Commands
--------
  status                  every campaign: stage reached and what it is blocked on
  record   --campaign S   fold one campaign's contacted people into the registries
  backfill                record every campaign that has a closelyhq import CSV
  check    --profile P    annotate a people CSV with already-contacted flags
  reply    --campaign S   write reply outcomes back onto registry people
  seed-customers          mark existing customers permanently excluded

Every write command supports --dry-run and prints what it would change.
Schema follows exclusions/README.md; unknown keys in existing files are preserved.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

# --------------------------------------------------------------------------- paths

def repo_root() -> Path:
    """marketing_vb/, resolved from this file — never from cwd."""
    return Path(__file__).resolve().parent.parent


def outbound_dir() -> Path:
    return repo_root() / "workspace" / "outbound"


def excl_dir() -> Path:
    return outbound_dir() / "exclusions"


def campaigns_dir() -> Path:
    return outbound_dir() / "campaigns"


PROFILES = ["katerina", "nick", "olena", "katya", "vadim"]

# Market wording that appears in campaign slugs -> sending profile.
# From CLAUDE.md section 5 and runners/outbound-runner.md.
MARKET_TO_PROFILE = [
    ("australia", "vadim"), ("-au-", "vadim"), ("au-", "vadim"),
    ("israel", "katya"),
    ("-us-", "nick"), ("us-", "nick"), ("usa", "nick"),
    ("-uk-", "katerina"), ("uk-", "katerina"),
    ("europe", "olena"), ("-eu-", "olena"), ("eu-", "olena"),
]

# README: always excluded from outbound, whatever a hypothesis says.
EXISTING_CUSTOMERS = [
    "Safariland", "Burlington Medical", "UK Meds", "Yazen", "Jim's Formal Wear",
    "Generation Tux", "Tailoor", "Redthread", "Healthyr",
]

LEGAL_SUFFIXES = {
    "inc", "inc.", "llc", "ltd", "ltd.", "limited", "corp", "corp.", "corporation",
    "co", "co.", "plc", "gmbh", "ag", "bv", "b.v.", "nv", "sa", "srl", "spa", "ab",
    "oy", "as", "a-s", "pty", "pte", "kk", "sas", "sarl", "aps", "holdings", "group",
    "the",
}


# --------------------------------------------------------------------------- helpers

def norm_company(name: str) -> str:
    """Company name -> stable slug. 'Prudential Financial, Inc.' -> 'prudential-financial'."""
    if not name:
        return ""
    s = name.strip().lower()
    s = re.sub(r"[‘’“”']", "", s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    parts = [p for p in s.split() if p and p not in LEGAL_SUFFIXES]
    return "-".join(parts) or re.sub(r"[^a-z0-9]+", "-", name.strip().lower()).strip("-")


def norm_linkedin(url: str) -> str:
    """
    Canonical person URL, so the same human recorded from two different CSVs collapses
    to one entry: lowercase, no scheme/www, no query, no trailing slash.
    """
    if not url:
        return ""
    u = url.strip().split("?")[0].split("#")[0]
    u = re.sub(r"^https?://", "", u, flags=re.I)
    u = re.sub(r"^([a-z]{2,3}\.)?linkedin\.com", "linkedin.com", u, flags=re.I)
    u = re.sub(r"^www\.", "", u, flags=re.I)
    return "https://" + u.rstrip("/").lower() if u else ""


def pick(row: dict, *candidates: str) -> str:
    """First non-empty value among candidate column names, case-insensitively."""
    lower = {k.lower().strip(): v for k, v in row.items() if k}
    for c in candidates:
        v = lower.get(c.lower())
        if v and str(v).strip():
            return str(v).strip()
    return ""


def person_url(row: dict) -> str:
    """
    A person's LinkedIn URL. Column naming drifted across campaigns
    (`linkedin_url`, `person_linkedin_url`), and `company_linkedin_url` must never be
    mistaken for a person — that would exclude a whole company as if it were one human.
    """
    # `url_linkedin` is the Sales-Navigator export spelling seen in 2026-07-27; the naming has
    # drifted every few campaigns, so accept every variant that has actually appeared.
    for col in ("person_linkedin_url", "linkedin_url", "url_linkedin", "profile_url",
                "person_url", "prospect_linkedin_url"):
        v = pick(row, col)
        if v and "/company/" not in v.lower():
            return norm_linkedin(v)
    return ""


def read_csv(path: Path) -> list[dict]:
    for enc in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            with path.open(newline="", encoding=enc) as fh:
                return list(csv.DictReader(fh))
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"    ! cannot read {path.name}: {e}", file=sys.stderr)
            return []
    return []


def load_json(path: Path, default: dict) -> dict:
    if not path.exists():
        return json.loads(json.dumps(default))
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        sys.exit(f"✗ {path} is not valid JSON ({e}). Fix or move it before running this.")


def save_json(path: Path, data: dict, dry: bool) -> None:
    body = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if dry:
        print(f"    [dry-run] would write {rel(path)} ({len(body)} bytes)")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")


def rel(path: Path) -> str:
    """Repo-relative for readability, absolute when the path lies outside the repo."""
    try:
        return str(path.relative_to(repo_root()))
    except ValueError:
        return str(path)


def today() -> str:
    return date.today().isoformat()


def infer_profile(slug: str) -> str | None:
    s = f"-{slug.lower()}-"
    for needle, prof in MARKET_TO_PROFILE:
        if needle in s:
            return prof
    return None


def campaign_product(cdir: Path) -> str:
    """`product:` from the hypothesis frontmatter; FitXpress has been the default since 2026-07-01."""
    h = cdir / "hypothesis.md"
    if h.exists():
        m = re.search(r"^product:\s*([a-z_]+)", h.read_text(encoding="utf-8", errors="replace"),
                      re.M)
        if m:
            return m.group(1)
    return "unknown"


def campaign_id_of(entry: dict) -> str:
    """Campaign key. Legacy stub entries use `slug`; this script writes `campaign_id`."""
    return entry.get("campaign_id") or entry.get("slug") or ""


def profile_registry_path(profile: str) -> Path:
    return excl_dir() / f"{profile}-registry.json"


def blank_profile_registry(profile: str) -> dict:
    return {
        "profile": profile,
        "market": {"katerina": "UK", "nick": "USA", "olena": "Europe / EU",
                   "katya": "Israel", "vadim": "Australia"}.get(profile, ""),
        "last_updated": today(),
        "campaigns": [],
        "excluded_companies": [],
        "excluded_people_urls": [],
    }


def blank_global_registry() -> dict:
    return {"last_updated": today(), "companies": {}}


# --------------------------------------------------------------------------- extraction

IMPORT_GLOBS = ("closelyhq-import*.csv",)
VALIDATED_GLOBS = ("people-validated.csv", "people-validated-full.csv",
                   "people-validated-batch*.csv")


def contacted_people(cdir: Path) -> tuple[list[dict], str]:
    """
    The people a campaign actually put in front of the sender.

    Source of truth is the closelyhq import CSV: that is the file handed to closely.io, so a
    campaign without one never reached anybody and must not be recorded as contacted.
    Batch files overlap (`batch1` + `batch2` + `full` on the same campaign), so rows are
    deduped by canonical URL rather than summed.
    """
    seen: dict[str, dict] = {}
    files: list[Path] = []
    for g in IMPORT_GLOBS:
        files += sorted(cdir.glob(g))
    if not files:
        return [], "none"

    rows_total = 0
    rows_no_url = 0
    for f in files:
        for row in read_csv(f):
            rows_total += 1
            url = person_url(row)
            if not url:
                rows_no_url += 1
                continue
            company = pick(row, "company", "company_name", "organization")
            rec = {
                "linkedin_url": url,
                "name": pick(row, "full_name", "name") or
                        " ".join(x for x in (pick(row, "first_name"), pick(row, "last_name")) if x),
                "company": norm_company(company),
                "company_display": company,
                "title": pick(row, "title", "job_title", "position"),
                "status": "csv_generated",
                "reply": None,
            }
            prev = seen.get(url)
            if prev is None or (not prev.get("title") and rec.get("title")):
                seen[url] = rec

    # An import CSV with rows but no usable person URL is a broken artifact, not an empty
    # campaign — 2026-07-16-au-telehealth has 253 blank rows on the pre-2026-07-21 four-step
    # schema. Reporting it as "0 people" hides a file that needs regenerating.
    if rows_total and not seen:
        return [], "import_csv_unusable"
    # Judge completeness on rows MISSING a URL, never on the dedupe ratio: a campaign with
    # batch1 + batch2 + full on disk has every row filled and still collapses 496 -> 248,
    # which is dedupe working, not data loss.
    if rows_no_url:
        return list(seen.values()), f"import_csv_partial:{rows_no_url} of {rows_total} rows have no URL"
    return list(seen.values()), "import_csv"


def validated_count(cdir: Path) -> int:
    urls = set()
    for g in VALIDATED_GLOBS:
        for f in sorted(cdir.glob(g)):
            for row in read_csv(f):
                u = person_url(row)
                if u:
                    urls.add(u)
    return len(urls)


# --------------------------------------------------------------------------- status

# (milestone label, glob(s) that prove it, what produces the NEXT one)
MILESTONES = [
    ("hypothesis",   ("hypothesis.md",),                        "run `/outbound hypothesis`"),
    ("companies",    ("companies.csv", "companies.md"),         "approve the hypothesis, then `research`"),
    ("sales-nav",    ("sales-nav-raw/*", "people-raw*.csv"),    "VADIM: export Sales Navigator into sales-nav-raw/"),
    ("validated",    ("people-validated*.csv",),                "run `extract`, then `validate`"),
    ("messages",     ("messages*",),                            "approve the list, then `messages`"),
    ("imported",     ("closelyhq-import*.csv",),                "approve the sample, then `import`"),
    ("replies-raw",  ("responses-raw.csv",),                    "VADIM: export replies from closely.io into responses-raw.csv"),
    ("classified",   ("responses-classified.csv",),             "run `responses`"),
    ("metrics",      ("metrics-final.json", "metrics-final.csv"), "VADIM: export final metrics into metrics-final.json"),
    ("closed",       ("post-mortem.md",),                       "run `analyze`"),
]


def stage_of(cdir: Path) -> tuple[str, str]:
    """
    (furthest milestone reached, what unblocks the next one).

    Deliberately NOT "first missing artifact": these campaigns did not run in a straight line.
    Only 3 of 10 ever produced companies.csv, yet several went all the way to a sender-ready
    import CSV. A first-gap reading called a campaign that had already contacted 307 people
    "stage 1 · hypothesis", which is worse than no status at all.
    """
    reached = [i for i, (_, globs, _) in enumerate(MILESTONES)
               if any(next(cdir.glob(g), None) for g in globs)]
    if not reached:
        return "0 · empty", MILESTONES[0][2]
    top = max(reached)
    label = f"{top + 1} · {MILESTONES[top][0]}"
    if top + 1 >= len(MILESTONES):
        return "10 · closed", "—"
    gaps = [i for i in range(top) if i not in reached]
    blocked = MILESTONES[top + 1][2]
    if gaps:
        skipped = ",".join(MILESTONES[i][0] for i in gaps)
        blocked += f"  [skipped: {skipped}]"
    return label, blocked


def cmd_status(args) -> int:
    rows = []
    for cdir in sorted(campaigns_dir().iterdir()):
        if not cdir.is_dir():
            continue
        stage, blocked = stage_of(cdir)
        people, src = contacted_people(cdir)
        prof = infer_profile(cdir.name) or "?"
        note = ""
        if src == "import_csv_unusable":
            note = "  ⚠ import CSV has rows but no LinkedIn URLs — regenerate it"
        elif src.startswith("import_csv_partial"):
            note = f"  ⚠ {src.split(chr(58), 1)[1]}"
        rows.append((cdir.name, prof, stage, len(people), validated_count(cdir), blocked + note))

    w = max((len(r[0]) for r in rows), default=10)
    print(f"{'CAMPAIGN':<{w}}  {'PROF':<9} {'STAGE':<22} {'SENT':>5} {'VALID':>6}  BLOCKED ON")
    print("-" * (w + 74))
    for name, prof, stage, sent, valid, blocked in rows:
        print(f"{name:<{w}}  {prof:<9} {stage:<22} {sent:>5} {valid:>6}  {blocked}")

    waiting = [r for r in rows if r[5].startswith("VADIM")]
    unclosed = [r for r in rows if not r[2].startswith("9")]
    print(f"\n{len(rows)} campaigns · {len(unclosed)} not closed · {len(waiting)} waiting on Vadim")
    if waiting:
        print("\nWaiting on a manual export — nothing downstream can run until these land:")
        for name, _, _, _, _, blocked in waiting:
            print(f"  {name}: {blocked.replace('VADIM: ', '')}")
    return 0


# --------------------------------------------------------------------------- record

def record_campaign(cdir: Path, profile: str, dry: bool, quiet: bool = False) -> dict:
    slug = cdir.name
    people, src = contacted_people(cdir)
    product = campaign_product(cdir)
    stat = {"campaign": slug, "profile": profile, "people": len(people),
            "companies": 0, "new_people": 0, "new_companies": 0, "source": src}

    if src == "none":
        if not quiet:
            print(f"  {slug}: no closelyhq import CSV — never reached anyone, skipping")
        return stat
    if src == "import_csv_unusable":
        if not quiet:
            print(f"  {slug}: import CSV has rows but no LinkedIn URLs — nothing to record. "
                  f"Regenerate it before this campaign can be excluded from future runs.")
        return stat

    companies = sorted({p["company"] for p in people if p["company"]})
    display = {p["company"]: p.get("company_display", p["company"]) for p in people}
    stat["companies"] = len(companies)

    # ---- per-profile registry
    reg_path = profile_registry_path(profile)
    reg = load_json(reg_path, blank_profile_registry(profile))
    reg.setdefault("campaigns", [])
    reg.setdefault("excluded_companies", [])
    reg.setdefault("excluded_people_urls", [])
    reg.setdefault("profile", profile)

    known = set(reg["excluded_people_urls"])
    new_people = [p for p in people if p["linkedin_url"] not in known]
    stat["new_people"] = len(new_people)
    new_companies = [c for c in companies if c not in set(reg["excluded_companies"])]
    stat["new_companies"] = len(new_companies)

    entry = next((c for c in reg["campaigns"] if campaign_id_of(c) == slug), None)
    payload = {
        "campaign_id": slug,
        "product": product,
        "date_started": slug[:10] if re.match(r"^\d{4}-\d{2}-\d{2}", slug) else today(),
        "recorded_on": today(),
        "recorded_from": src,
        # send confirmation lives in closely.io, not here: the import CSV proves the list was
        # handed over, not that every invite went out. Exclusion treats it as contacted anyway,
        # because re-contacting a prospect costs more than skipping one company.
        "send_confirmed": False,
        "companies": companies,
        "people": people,
    }
    if entry is None:
        reg["campaigns"].append(payload)
    else:
        merged = {p["linkedin_url"]: p for p in entry.get("people", [])}
        for p in people:
            if p["linkedin_url"] in merged:
                # keep an outcome that `reply` already wrote
                merged[p["linkedin_url"]].update({k: v for k, v in p.items()
                                                  if k != "reply" or v is not None})
            else:
                merged[p["linkedin_url"]] = p
        payload["people"] = list(merged.values())
        payload["companies"] = sorted(set(entry.get("companies", [])) | set(companies))
        # keep any fields a legacy stub carried that this script does not produce
        for k, v in entry.items():
            payload.setdefault(k, v)
        payload.pop("slug", None)
        reg["campaigns"][reg["campaigns"].index(entry)] = payload

    reg["excluded_people_urls"] = sorted(set(reg["excluded_people_urls"]) |
                                         {p["linkedin_url"] for p in people})
    reg["excluded_companies"] = sorted(set(reg["excluded_companies"]) | set(companies))
    reg["last_updated"] = today()
    save_json(reg_path, reg, dry)

    # ---- global company registry
    g_path = excl_dir() / "global-company-registry.json"
    g = load_json(g_path, blank_global_registry())
    g.setdefault("companies", {})
    for c in companies:
        cur = g["companies"].get(c)
        if cur and cur.get("status") == "existing_customer_excluded":
            continue  # a customer is never reassigned to a campaign
        if cur and cur.get("covered_by_profile") not in (None, profile):
            cur.setdefault("also_covered_by", [])
            if profile not in cur["also_covered_by"]:
                cur["also_covered_by"].append(profile)
            continue  # first profile keeps the company; README rule 1
        g["companies"][c] = {
            "display_name": display.get(c, c),
            "covered_by_profile": profile,
            "campaign_id": slug,
            "product": product,
            "date": payload["date_started"],
            "status": "active",
        }
    g["last_updated"] = today()
    save_json(g_path, g, dry)

    if not quiet:
        print(f"  {slug}: {len(people)} people ({stat['new_people']} new), "
              f"{len(companies)} companies ({stat['new_companies']} new) -> {profile}")
    return stat


def cmd_record(args) -> int:
    cdir = campaigns_dir() / args.campaign
    if not cdir.is_dir():
        sys.exit(f"✗ no such campaign: {args.campaign}")
    profile = args.profile or infer_profile(args.campaign)
    if not profile:
        sys.exit(f"✗ cannot infer the profile from '{args.campaign}'. Pass --profile.")
    if profile not in PROFILES:
        sys.exit(f"✗ unknown profile '{profile}'. One of: {', '.join(PROFILES)}")
    print(f"record{' (dry-run)' if args.dry_run else ''}: {args.campaign} -> {profile}")
    record_campaign(cdir, profile, args.dry_run)
    return 0


def cmd_backfill(args) -> int:
    plan = []
    for cdir in sorted(campaigns_dir().iterdir()):
        if not cdir.is_dir():
            continue
        people, src = contacted_people(cdir)
        if src == "none":
            continue
        prof = infer_profile(cdir.name)
        plan.append((cdir, prof, len(people)))

    print(f"backfill{' (dry-run)' if args.dry_run else ''}: "
          f"{len(plan)} campaigns with an import CSV\n")
    unknown = [c.name for c, p, _ in plan if not p]
    if unknown:
        print("✗ profile could not be inferred for:")
        for n in unknown:
            print(f"    {n}")
        print("  Re-run per campaign with --profile.")
        return 1

    for cdir, prof, n in plan:
        print(f"  {cdir.name:<40} {prof:<9} {n:>4} people")
    print()
    if not args.yes and not args.dry_run:
        print("Refusing to write without --yes. Re-run with --dry-run to preview, "
              "or --yes to apply.")
        return 1

    total = {"people": 0, "new_people": 0, "companies": 0, "new_companies": 0}
    for cdir, prof, _ in plan:
        s = record_campaign(cdir, prof, args.dry_run)
        for k in total:
            total[k] += s.get(k, 0)
    print(f"\n{total['new_people']} people and {total['new_companies']} companies newly excluded "
          f"(of {total['people']} / {total['companies']} seen)")
    return 0


# --------------------------------------------------------------------------- check

def cmd_check(args) -> int:
    """Annotate a people CSV against the registries. This is what icp-validator calls."""
    profile = args.profile
    if profile not in PROFILES:
        sys.exit(f"✗ unknown profile '{profile}'. One of: {', '.join(PROFILES)}")
    src = Path(args.input)
    if not src.is_absolute():
        src = repo_root() / src
    if not src.exists():
        sys.exit(f"✗ no such file: {src}")

    reg = load_json(profile_registry_path(profile), blank_profile_registry(profile))
    mine = set(reg.get("excluded_people_urls", []))
    g = load_json(excl_dir() / "global-company-registry.json", blank_global_registry())
    gc = g.get("companies", {})

    rows = read_csv(src)
    if not rows:
        sys.exit(f"✗ {src.name} has no rows")

    out = []
    hits = {"person_already_contacted": 0, "company_other_profile": 0,
            "existing_customer": 0, "clear": 0, "no_url": 0}
    for row in rows:
        url = person_url(row)
        comp = norm_company(pick(row, "company_name", "company", "organization"))
        flag, why = "", ""
        if url and url in mine:
            flag, why = "EXCLUDE", f"already contacted from {profile}"
            hits["person_already_contacted"] += 1
        elif comp and gc.get(comp, {}).get("status") == "existing_customer_excluded":
            flag, why = "EXCLUDE", "existing customer"
            hits["existing_customer"] += 1
        elif comp and gc.get(comp, {}).get("covered_by_profile") not in (None, profile) \
                and gc.get(comp, {}).get("status") == "active":
            flag, why = "EXCLUDE", f"company covered by {gc[comp]['covered_by_profile']}"
            hits["company_other_profile"] += 1
        else:
            if not url:
                hits["no_url"] += 1
            else:
                hits["clear"] += 1
        r = dict(row)
        r["exclusion_flag"] = flag
        r["exclusion_reason"] = why
        out.append(r)

    print(f"check: {src.name} vs profile '{profile}' — {len(rows)} rows")
    for k, v in hits.items():
        if v:
            print(f"  {k:28} {v}")
    excluded = hits["person_already_contacted"] + hits["company_other_profile"] + hits["existing_customer"]
    print(f"  {'-> must be excluded':28} {excluded}")
    if hits["no_url"]:
        print(f"  note: {hits['no_url']} rows carry no person LinkedIn URL — "
              "cannot be checked against the person registry")

    if args.output:
        dst = Path(args.output)
        if not dst.is_absolute():
            dst = repo_root() / dst
        if args.dry_run:
            print(f"  [dry-run] would write {dst}")
        else:
            with dst.open("w", newline="", encoding="utf-8") as fh:
                wr = csv.DictWriter(fh, fieldnames=list(out[0].keys()))
                wr.writeheader()
                wr.writerows(out)
            print(f"  wrote {rel(dst)}")
    return 0


# --------------------------------------------------------------------------- reply

REPLY_COLS = ("category", "classification", "reply_category", "response_category")


def cmd_reply(args) -> int:
    """Fold responses-classified.csv outcomes onto registry people. campaign-analyzer calls this."""
    cdir = campaigns_dir() / args.campaign
    if not cdir.is_dir():
        sys.exit(f"✗ no such campaign: {args.campaign}")
    profile = args.profile or infer_profile(args.campaign)
    if not profile:
        sys.exit(f"✗ cannot infer the profile from '{args.campaign}'. Pass --profile.")

    rc = cdir / "responses-classified.csv"
    if not rc.exists():
        sys.exit(f"✗ {rel(rc)} does not exist — run `responses` first.")

    by_url: dict[str, str] = {}
    for row in read_csv(rc):
        url = person_url(row)
        cat = pick(row, *REPLY_COLS)
        if url and cat:
            by_url[url] = cat

    reg_path = profile_registry_path(profile)
    reg = load_json(reg_path, blank_profile_registry(profile))
    entry = next((c for c in reg.get("campaigns", []) if campaign_id_of(c) == args.campaign), None)
    if entry is None:
        sys.exit(f"✗ {args.campaign} is not in {reg_path.name} — run `record` first.")

    updated = 0
    for p in entry.get("people", []):
        cat = by_url.get(p.get("linkedin_url", ""))
        if cat and p.get("reply") != cat:
            p["reply"] = cat
            p["status"] = "replied"
            updated += 1
    entry["replies_recorded_on"] = today()
    reg["last_updated"] = today()

    print(f"reply{' (dry-run)' if args.dry_run else ''}: {args.campaign} -> {profile}")
    print(f"  {len(by_url)} classified replies, {updated} registry people updated, "
          f"{len(by_url) - updated} not matched by URL")
    save_json(reg_path, reg, args.dry_run)
    return 0


# --------------------------------------------------------------------------- seed

def cmd_seed_customers(args) -> int:
    g_path = excl_dir() / "global-company-registry.json"
    g = load_json(g_path, blank_global_registry())
    g.setdefault("companies", {})
    added = []
    for name in EXISTING_CUSTOMERS:
        slug = norm_company(name)
        if g["companies"].get(slug, {}).get("status") == "existing_customer_excluded":
            continue
        g["companies"][slug] = {
            "display_name": name,
            "covered_by_profile": None,
            "status": "existing_customer_excluded",
            "note": "customer — never enters outbound (exclusions/README.md)",
        }
        added.append(f"{name} -> {slug}")
    g["last_updated"] = today()
    print(f"seed-customers{' (dry-run)' if args.dry_run else ''}: {len(added)} added")
    for a in added:
        print(f"  {a}")
    save_json(g_path, g, args.dry_run)
    return 0


# --------------------------------------------------------------------------- cli

def main() -> int:
    p = argparse.ArgumentParser(
        description="Outbound exclusion registry writer + campaign status board.")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("status", help="every campaign: stage and what blocks it").set_defaults(
        func=cmd_status)

    r = sub.add_parser("record", help="fold one campaign into the registries")
    r.add_argument("--campaign", required=True)
    r.add_argument("--profile", choices=PROFILES)
    r.add_argument("--dry-run", action="store_true")
    r.set_defaults(func=cmd_record)

    b = sub.add_parser("backfill", help="record every campaign that has an import CSV")
    b.add_argument("--dry-run", action="store_true")
    b.add_argument("--yes", action="store_true", help="required to actually write")
    b.set_defaults(func=cmd_backfill)

    c = sub.add_parser("check", help="annotate a people CSV with exclusion flags")
    c.add_argument("--profile", required=True, choices=PROFILES)
    c.add_argument("--input", required=True)
    c.add_argument("--output")
    c.add_argument("--dry-run", action="store_true")
    c.set_defaults(func=cmd_check)

    y = sub.add_parser("reply", help="write reply outcomes onto registry people")
    y.add_argument("--campaign", required=True)
    y.add_argument("--profile", choices=PROFILES)
    y.add_argument("--dry-run", action="store_true")
    y.set_defaults(func=cmd_reply)

    s = sub.add_parser("seed-customers", help="mark existing customers permanently excluded")
    s.add_argument("--dry-run", action="store_true")
    s.set_defaults(func=cmd_seed_customers)

    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
