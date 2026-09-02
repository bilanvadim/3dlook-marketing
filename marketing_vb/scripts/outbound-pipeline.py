#!/usr/bin/env python3
"""outbound-pipeline.py — the mechanical steps of the outbound flow, as tested code.

WHY THIS EXISTS
---------------
`people-extractor.md` and `closelyhq-importer.md` hand the agent pandas snippets:

    companies = pd.read_csv('companies.csv')
    df = df.merge(companies[['company_name']], on='company_name', how='inner')

**pandas is not installed anywhere on this box** — not in the system python3, not in the
Hermes venv. So those snippets have never run. Every campaign's agent hand-rolled its own
replacement instead, and the results diverged: `2026-07-16-au-telehealth` still holds six
different `gen_batch*.py`, a `generate_batch1.py`, a `_v2.py` and an `icp_validate.py`.

That is how 253 people ended up in `closelyhq-import.csv` with `first_name`, `last_name`,
`linkedin_url` and `location` empty in **all 253 rows**: the ad-hoc validator emitted
`person_id,full_name,title,company_name,decision,priority,...`, which has no first/last
name and no LinkedIn URL for the importer to map. The importer's own assertion only
checked that the COLUMN existed, so an entirely blank column passed. Seven weeks of a
campaign nobody could send.

Every command is stdlib and every command's contract is its exit code.

    hypothesis-gate      refuse step 2/3 when the hypothesis scope moved under the list
    validate-companies   gate the step-2 list: schema, geo, fit, verification, scope
    extract-people       step 3, joining on a company SLUG with aliases, not a raw name
    check-import         refuse a closely.io CSV with blank identity or off-standard copy
    check-responses      gate a responses export before step 8 reads it
    fix-validated        put identity columns back into a validated list from people-raw
    remind               weekly digest of what outbound is waiting on (Telegram)

Shared logic (`norm_company`, `infer_profile`, `pick`, `stage_of`, `PROFILES`) is imported
from `outbound-registry.py` rather than copied, so the slug and stage rules cannot drift
between the two.

USAGE
    scripts/outbound-pipeline.py hypothesis-gate    --campaign <slug> [--stamp]
    scripts/outbound-pipeline.py validate-companies --campaign <slug> [--in F] [--write-routed]
    scripts/outbound-pipeline.py extract-people     --campaign <slug> [--dry-run] [--overwrite]
    scripts/outbound-pipeline.py check-import       --campaign <slug> | --file <path>
    scripts/outbound-pipeline.py check-responses    --campaign <slug> | --file <path>
    scripts/outbound-pipeline.py fix-validated      --campaign <slug>
    scripts/outbound-pipeline.py remind             [--notify]
"""
from __future__ import annotations

import argparse
import csv
import importlib.util
import re
import sys
from pathlib import Path

# --------------------------------------------------------------------- shared logic

def _load_registry():
    """Import outbound-registry.py by path — the hyphen makes it un-importable normally."""
    here = Path(__file__).resolve().parent
    spec = importlib.util.spec_from_file_location(
        "outbound_registry", here / "outbound-registry.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


REG = _load_registry()
norm_company = REG.norm_company
norm_linkedin = REG.norm_linkedin
pick = REG.pick
infer_profile = REG.infer_profile
PROFILES = REG.PROFILES


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def campaign_dir(slug: str) -> Path:
    return repo_root() / "workspace" / "outbound" / "campaigns" / slug


# --------------------------------------------------------------------- geo routing

# CLAUDE.md section 5: one profile owns one market, and a company belongs to exactly one
# profile. Matching is substring-based on purpose — the real data holds "England",
# "England (US parent)", "England (status unclear)", "Unknown", not clean ISO codes.
PROFILE_GEO: dict[str, tuple[str, ...]] = {
    "katerina": ("uk", "united kingdom", "england", "scotland", "wales",
                 "northern ireland", "britain", "gb"),
    "nick": ("usa", "united states", "u.s.", "us-hq", "america"),
    "olena": ("sweden", "germany", "france", "spain", "italy", "netherlands", "poland",
              "denmark", "norway", "finland", "ireland", "portugal", "austria",
              "belgium", "switzerland", "czech", "estonia", "latvia", "lithuania",
              "romania", "bulgaria", "greece", "hungary", "slovakia", "slovenia",
              "croatia", "ukraine", "europe", "eu"),
    "katya": ("israel", "uae", "united arab emirates", "saudi", "qatar", "kuwait",
              "bahrain", "oman", "gulf"),
    "vadim": ("australia", "new zealand"),
}

# "US" is a two-letter token that appears inside dozens of unrelated words, so it is
# matched as a standalone token only, never as a substring.
_TOKEN_ONLY = {"uk", "us", "eu", "gb", "u.s."}


def geo_profile(country: str) -> str | None:
    """Which sending profile owns this HQ country. None when it cannot be decided."""
    c = (country or "").strip().lower()
    if not c or "unknown" in c:
        return None
    tokens = set(re.split(r"[^a-z.]+", c))
    # A US parent does not move the HQ: "England (US parent)" is still katerina's.
    for prof, needles in PROFILE_GEO.items():
        for n in needles:
            if n in _TOKEN_ONLY:
                if n in tokens:
                    return prof
            elif n in c:
                return prof
    return None


# --------------------------------------------------------------------- csv helpers

# --------------------------------------------------------------- company matching

# Sales Navigator writes the employment type INTO the company cell: the 2026-08-07 export
# holds "Personify Health . Full-time", "iFIT . undefined", "Echelon . undefined". And the
# shortlist writes disambiguating asides: "Personify Health (formerly Virgin Pulse)",
# "iFIT (incl. NordicTrack)", "Peloton (digital)".
#
# Neither side is wrong; a raw name-to-name join just cannot see through either. On the
# real 643-row export it matched 94 people and threw away 549 — 193 of them Personify
# Health alone — and the old pandas `merge(on='company_name', how='inner')` would have
# thrown away the same 549 without printing a word.
EMPLOYMENT_SUFFIX = re.compile(
    r"\s*[.·]\s*(?:permanent|fixed[- ]term|full|part)?\s*"
    r"(full-?time|part-?time|self-?employed|contract|freelance|internship|"
    r"temporary|seasonal|apprenticeship|permanent|undefined)\s*$",
    re.I,
)

# A parenthetical alias that is one generic word is not an identity — "(digital)" must
# never let a row match every company whose aside happens to say digital.
GENERIC_PAREN = {
    "digital", "formerly", "incl", "including", "group", "holdings", "usa", "uk", "us",
    "eu", "app", "apps", "online", "global", "international", "the", "inc", "ltd",
    "limited", "corp", "company", "brand", "division", "subsidiary", "and", "clinic",
}


def clean_company(name: str) -> str:
    """Company cell → the company, without employment type or trailing punctuation."""
    s = (name or "").strip()
    prev = None
    while prev != s:                     # "X . Full-time . undefined" happens
        prev = s
        s = EMPLOYMENT_SUFFIX.sub("", s).strip()
    return s.strip(" .,·-")


def company_keys(name: str) -> set[str]:
    """Every slug this company could legitimately be written as.

    "iFIT (incl. NordicTrack)" -> {ifit-incl-nordictrack, ifit, nordictrack}
    "Peloton (digital)"        -> {peloton-digital, peloton}      ('digital' dropped)
    """
    base = clean_company(name)
    if not base:
        return set()
    keys = {norm_company(base)}

    outside = re.sub(r"\([^)]*\)", " ", base).strip(" -,")
    if outside:
        keys.add(norm_company(outside))

    for inner in re.findall(r"\(([^)]*)\)", base):
        inner = re.sub(r"^\s*(incl\.?|including|formerly|fka|aka|now)\s+", "", inner, flags=re.I)
        for part in re.split(r"\s*/\s*|\s+or\s+", inner):
            slug = norm_company(part)
            if not slug:
                continue
            if slug in GENERIC_PAREN or (len(slug) < 4 and slug.isalpha()):
                continue
            keys.add(slug)
    return {k for k in keys if k}


# Trailing industry words the two sides disagree about: shortlist "Echelon Fitness" vs
# export "Echelon" (19 people), "iFit - fitness technology" vs "iFIT". Stripped only when
# what remains is still a real name — 4+ chars and not itself an industry word.
INDUSTRY_TAIL = (
    "fitness", "health", "healthcare", "wellness", "technology", "technologies",
    "labs", "digital", "media", "multimedia", "nutrition", "clinic", "clinics",
    "pharmacy", "telehealth", "solutions", "systems", "brands",
)


def shortlist_keys(name: str) -> set[str]:
    """company_keys plus industry-tail variants. For the SHORTLIST side only."""
    keys = set(company_keys(name))
    for k in list(keys):
        parts = k.split("-")
        while len(parts) > 1 and parts[-1] in INDUSTRY_TAIL:
            parts = parts[:-1]
            cand = "-".join(parts)
            if len(cand) >= 4 and cand not in INDUSTRY_TAIL and cand not in GENERIC_PAREN:
                keys.add(cand)
    return keys


def read_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8-sig") as fh:
        return list(csv.DictReader(fh))


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(repo_root()))
    except ValueError:
        return str(p)


def resolve_input(args, default_names: tuple[str, ...]) -> Path | None:
    """--file wins; else --in inside the campaign; else the first default that exists."""
    if getattr(args, "file", None):
        return Path(args.file).expanduser().resolve()
    cdir = campaign_dir(args.campaign)
    if getattr(args, "infile", None):
        return cdir / args.infile
    for name in default_names:
        p = cdir / name
        if p.exists():
            return p
    return None


# --------------------------------------------------------------------- P1.6 validate

FIT_OK = {"high", "medium"}          # what proceeds to Sales Navigator
FIT_DROP = {"exclude", "low", "route elsewhere", "medium-low", "low-medium"}


def fit_of(row: dict) -> str:
    """Normalised fit. Handles both the icp_fit words and the fit_score_1_to_5 number."""
    raw = pick(row, "icp_fit", "fit", "fit_score", "fit_score_1_to_5").lower()
    if not raw:
        return ""
    if re.fullmatch(r"[1-5](\.\d+)?", raw):
        n = float(raw)
        return "high" if n >= 4 else ("medium" if n >= 3 else "low")
    return raw


def cmd_validate_companies(args) -> int:
    src = resolve_input(args, ("companies-verified.csv", "companies.csv"))
    if src is None or not src.exists():
        print(f"✗ no companies CSV in {rel(campaign_dir(args.campaign))} "
              f"(looked for companies-verified.csv, companies.csv)", file=sys.stderr)
        return 2
    rows = read_csv(src)
    if not rows:
        print(f"✗ {rel(src)} is empty", file=sys.stderr)
        return 2

    profile = args.profile or infer_profile(args.campaign)
    print(f"→ {rel(src)}: {len(rows)} rows | profile: {profile or '(undetermined)'}\n")

    errors: list[str] = []
    warnings: list[str] = []
    routed: list[dict] = []
    proceed: list[dict] = []
    seen: dict[str, int] = {}

    # The hypothesis gate runs INSIDE this check, not beside it. A separate optional
    # command is a command that gets skipped on the run where it mattered.
    hyp = campaign_dir(args.campaign) / "hypothesis.md"
    if hyp.exists():
        text = hyp.read_text(encoding="utf-8", errors="replace")
        st = hypothesis_status(text)
        if st != "approved":
            errors.append(f"hypothesis status is {st or 'missing'}, not `approved`")
        lock = campaign_dir(args.campaign) / LOCK_NAME
        if lock.exists():
            import json
            digest, _ = scope_hash(text)
            try:
                prev = json.loads(lock.read_text(encoding="utf-8")).get("scope_hash")
            except (OSError, ValueError):
                prev = None
            if prev and prev != digest:
                errors.append(
                    "hypothesis scope changed after this list was built "
                    f"(stamped {prev}, now {digest}) — re-approve and rebuild "
                    "(`hypothesis-gate --campaign … --stamp`)"
                )
        else:
            warnings.append(
                f"no {LOCK_NAME} — the list is not tied to a hypothesis version; "
                "run `hypothesis-gate --stamp` when you build it"
            )
    else:
        errors.append("no hypothesis.md — step 2 cannot be validated without it")

    cols_present = {c.lower() for c in rows[0] if c}

    has_verification = "verification" in cols_present
    if not has_verification:
        errors.append(
            "no `verification` column — run `web-verify.py verify` first. A shortlist that "
            "has not touched the web is not research (see the 2026-09-02 blind-search run)."
        )

    # Schema drift, reported instead of inferred. company-researcher.md documents
    #   company_name,website,linkedin_url,hq_country,hq_city,employees,
    #   revenue_estimate,fit_score_1_to_5,fit_reason,source_url,notes
    # and neither list produced on 2026-09-02 matched it: the broadened one invented 13
    # different columns, the GLP-1 one has no fit column at all. A missing fit column does
    # not error — it silently disables the fit filter below, which is worse, so it is named.
    if not (cols_present & {"icp_fit", "fit", "fit_score", "fit_score_1_to_5"}):
        warnings.append(
            "NO FIT COLUMN (icp_fit / fit_score_1_to_5). The High/Medium filter is therefore "
            "inert and every row proceeds. Nothing downstream can prioritise — add fit in step 2."
        )
    for opt in ("linkedin_url", "hq_city", "employees"):
        if opt not in cols_present:
            warnings.append(f"missing `{opt}` from the documented step-2 schema")

    for i, r in enumerate(rows, start=2):          # 2 = first data line in the file
        name = pick(r, "company_name", "company")
        if not name:
            errors.append(f"line {i}: empty company_name")
            continue
        slug = norm_company(name)

        if slug in seen:
            warnings.append(f"line {i}: duplicate of line {seen[slug]} ({name})")
        else:
            seen[slug] = i

        site = pick(r, "website", "url", "domain")
        if not site:
            errors.append(f"line {i}: {name} has no website")
        elif not site.lower().startswith(("http://", "https://")):
            errors.append(f"line {i}: {name} website is not http(s): {site!r}")

        verdict = pick(r, "verification")
        if has_verification:
            if not verdict:
                errors.append(f"line {i}: {name} has an empty verification")
            elif verdict.startswith("unverified"):
                errors.append(f"line {i}: {name} is {verdict} — never checked against a source")
            elif not verdict.startswith("verified"):
                warnings.append(f"line {i}: {name} is {verdict} (not usable as proof)")

        if verdict.startswith("verified") and not pick(r, "source_url"):
            errors.append(f"line {i}: {name} is verified but has no source_url")

        # geo: the row must belong to this campaign's profile
        country = pick(r, "hq_country", "country", "hq")
        owner = geo_profile(country)
        r["_slug"] = slug
        r["_fit"] = fit_of(r)
        if profile and owner and owner != profile:
            r["routed_to_profile"] = owner
            r["routed_reason"] = f"HQ {country!r} belongs to `{owner}`, campaign runs `{profile}`"
            routed.append(r)
            continue
        if profile and not owner:
            warnings.append(f"line {i}: {name} HQ {country!r} maps to no profile — decide manually")

        if r["_fit"] and r["_fit"] not in FIT_OK:
            r["routed_to_profile"] = ""
            r["routed_reason"] = f"fit={r['_fit']} — below the High/Medium bar"
            routed.append(r)
            continue
        proceed.append(r)

    for w in warnings:
        print(f"  ⚠ {w}")
    if warnings:
        print()
    for e in errors:
        print(f"  ✗ {e}")
    if errors:
        print()

    print(f"{'-' * 66}")
    print(f"  proceed to step 3      {len(proceed)}")
    print(f"  routed out / dropped   {len(routed)}")
    print(f"  errors                 {len(errors)}")
    print(f"  warnings               {len(warnings)}")

    if routed:
        by_prof: dict[str, int] = {}
        for r in routed:
            key = r.get("routed_to_profile") or "(low fit)"
            by_prof[key] = by_prof.get(key, 0) + 1
        print("\n  routed out by owner:")
        for k, v in sorted(by_prof.items()):
            print(f"    {k:<14} {v}")

    if args.write_routed and routed:
        dst = src.with_name("companies-routed-out.csv")
        cols = [c for c in rows[0] if c and not c.startswith("_")]
        write_csv(dst, routed, cols + ["routed_to_profile", "routed_reason"])
        print(f"\n→ wrote {rel(dst)} ({len(routed)} rows)")
        print("  Each needs its OWN campaign folder under the owning profile — "
              "a company belongs to exactly one profile (exclusions/README.md rule 1).")

    if errors:
        print(f"\n✗ NOT READY for step 3: {len(errors)} error(s) above.", file=sys.stderr)
        return 1
    print("\n✓ companies list is ready for step 3")
    return 0


# --------------------------------------------------------------- hypothesis gate

# Only the sections that decide WHO is on the list. Rewriting "Why plausible" is editing;
# rewriting the sub-segment is a different campaign. Hashing the whole file would fire on
# a typo fix and get switched off within a week.
SCOPE_HEADINGS = (
    "vertical", "sub-segment", "subsegment", "use case", "target buyer persona",
    "anti-cases", "anticases", "validation criteria",
)

LOCK_NAME = ".hypothesis-lock.json"


def hypothesis_status(text: str) -> str:
    """`status:` from YAML frontmatter or a `**Status:** approved` bullet — both exist."""
    m = re.search(r"^status:\s*([a-z_-]+)", text, re.M | re.I)
    if m:
        return m.group(1).lower()
    m = re.search(r"^[-*]\s*\*\*status:?\*\*:?\s*([A-Za-z_-]+)", text, re.M | re.I)
    return m.group(1).lower() if m else ""


def scope_sections(text: str) -> dict[str, str]:
    """{heading: normalised body} for the scope-defining sections."""
    out: dict[str, str] = {}
    parts = re.split(r"^##+\s+(.+?)\s*$", text, flags=re.M)
    # parts = [pre, heading1, body1, heading2, body2, ...]
    for i in range(1, len(parts) - 1, 2):
        head = parts[i].strip().lower().rstrip(":")
        if any(h in head for h in SCOPE_HEADINGS):
            out[head] = re.sub(r"\s+", " ", parts[i + 1]).strip()
    return out


def scope_hash(text: str) -> tuple[str, dict[str, str]]:
    import hashlib
    secs = scope_sections(text)
    basis = "\n".join(f"{k}::{v}" for k, v in sorted(secs.items())) if secs \
        else re.sub(r"\s+", " ", text).strip()
    return hashlib.sha256(basis.encode("utf-8")).hexdigest()[:16], secs


def cmd_hypothesis_gate(args) -> int:
    import json
    cdir = campaign_dir(args.campaign)
    hyp = cdir / "hypothesis.md"
    if not hyp.exists():
        print(f"✗ no hypothesis.md in {rel(cdir)} — run `/outbound hypothesis` first",
              file=sys.stderr)
        return 2
    text = hyp.read_text(encoding="utf-8", errors="replace")
    status = hypothesis_status(text)
    digest, secs = scope_hash(text)
    lock = cdir / LOCK_NAME

    print(f"→ {rel(hyp)}")
    print(f"  status        {status or '(none found)'}")
    print(f"  scope hash    {digest}")
    print(f"  scope sections {len(secs)}: {', '.join(sorted(secs)) or '(none — hashing whole file)'}")

    if status != "approved":
        print(f"\n✗ hypothesis status is {status or 'missing'}, not `approved`. "
              "Step 2 needs an approved hypothesis.", file=sys.stderr)
        return 1

    if args.stamp:
        lock.write_text(json.dumps({
            "scope_hash": digest,
            "sections": sorted(secs),
            "stamped_at": __import__("datetime").datetime.now(
                __import__("datetime").timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "note": "Written when the company list was built. If the hypothesis scope "
                    "changes after this, the list no longer answers it.",
        }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"\n✓ stamped {rel(lock)} — the company list is now tied to this scope")
        return 0

    if not lock.exists():
        print(f"\n⚠ no {LOCK_NAME}: this list is not tied to any hypothesis version. "
              "Run with --stamp when you build the list.")
        return 0

    try:
        prev = json.loads(lock.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        print(f"\n✗ {LOCK_NAME} is unreadable ({e}) — re-stamp it", file=sys.stderr)
        return 1

    if prev.get("scope_hash") == digest:
        print(f"\n✓ hypothesis scope unchanged since {prev.get('stamped_at', '?')}")
        return 0

    print(f"\n✗ HYPOTHESIS SCOPE CHANGED since {prev.get('stamped_at', '?')}\n"
          f"    stamped: {prev.get('scope_hash')}\n"
          f"    now:     {digest}\n"
          "  The company list was built against the old scope, so it no longer answers\n"
          "  this hypothesis. This is the 2026-09-02 failure: at 03:23 the ask widened to\n"
          "  fitness and nutrition apps, hypothesis.md kept describing GLP-1 telehealth,\n"
          "  and 26 rows were produced against neither — 10 of them Exclude.\n"
          "  Re-approve the hypothesis with Vadim, rebuild the list, then --stamp.",
          file=sys.stderr)
    return 1


# --------------------------------------------------- P1.7 + P1.8 extract-people

PEOPLE_COLUMNS = [
    "person_id", "full_name", "first_name", "last_name", "title", "seniority",
    "company_name", "company_slug", "company_linkedin_url", "person_linkedin_url",
    "email_guess", "location_country", "location_city", "years_in_role",
    "profile_summary",
]

SENIORITY_PATTERNS = [
    (r"\b(founder|co-?founder|ceo|chief executive)\b", "founder/ceo"),
    (r"\bc[a-z]?o\b|chief\s+\w+\s+officer", "c-level"),
    (r"\b(vp|vice president|svp|evp)\b", "vp"),
    (r"\b(head of|director)\b", "director/head"),
    (r"\b(lead|manager|principal)\b", "manager"),
]


def seniority_of(title: str) -> str:
    t = (title or "").lower()
    for pat, label in SENIORITY_PATTERNS:
        if re.search(pat, t):
            return label
    return "other"


def split_name(full: str, first: str, last: str) -> tuple[str, str]:
    """Sales Navigator sometimes gives only a full name. Never leave both blank.

    This is the exact hole that produced 253 unusable rows: `full_name` present,
    `first_name`/`last_name` empty, and nothing downstream noticed.
    """
    if first or last:
        return first, last
    parts = [p for p in re.split(r"\s+", (full or "").strip()) if p]
    if not parts:
        return "", ""
    if len(parts) == 1:
        return parts[0], ""
    return parts[0], " ".join(parts[1:])


def cmd_extract_people(args) -> int:
    cdir = campaign_dir(args.campaign)
    companies_src = resolve_input(args, ("companies-verified.csv", "companies.csv"))
    if companies_src is None or not companies_src.exists():
        print(f"✗ no companies CSV in {rel(cdir)} — run step 2 first", file=sys.stderr)
        return 2

    raw_dir = cdir / "sales-nav-raw"
    raw_files = sorted(raw_dir.glob("*.csv")) if raw_dir.exists() else []
    if not raw_files:
        print(f"✗ no CSV in {rel(raw_dir)} — VADIM must export Sales Navigator first",
              file=sys.stderr)
        return 2

    profile = args.profile or infer_profile(args.campaign)
    companies = read_csv(companies_src)

    # Shortlist = only rows that pass fit + geo. This is the filter whose absence let
    # `Exclude` rows walk into people-raw.csv untouched: the old pandas snippet merged on
    # company_name with no fit column in sight.
    shortlist: dict[str, dict] = {}          # canonical slug -> row
    key_index: dict[str, str] = {}           # every alias slug -> canonical slug
    dropped_fit = dropped_geo = 0
    for r in companies:
        name = pick(r, "company_name", "company")
        if not name:
            continue
        owner = geo_profile(pick(r, "hq_country", "country", "hq"))
        if profile and owner and owner != profile:
            dropped_geo += 1
            continue
        f = fit_of(r)
        if f and f not in FIT_OK:
            dropped_fit += 1
            continue
        canon = norm_company(clean_company(name))
        shortlist[canon] = r
        for k in shortlist_keys(name):
            # First writer wins: a two-company alias collision must not silently
            # reassign people from the company that claimed it first.
            key_index.setdefault(k, canon)

    print(f"→ shortlist: {len(shortlist)} companies "
          f"(dropped {dropped_fit} on fit, {dropped_geo} on geo) from {rel(companies_src)}")
    print(f"→ raw: {len(raw_files)} file(s) in {rel(raw_dir)}\n")

    people: list[dict] = []
    unmatched: dict[str, int] = {}
    seen_urls: set[str] = set()
    dupes = 0

    for f in raw_files:
        rows = read_csv(f)
        kept = 0
        for r in rows:
            company_raw = pick(r, "company_name", "company", "Company", "Company Name",
                               "Account Name", "Current Company")
            company = clean_company(company_raw)
            slug = next((key_index[k] for k in company_keys(company_raw) if k in key_index),
                        None)
            if slug is None:
                unmatched[company or "(blank)"] = unmatched.get(company or "(blank)", 0) + 1
                continue

            full = pick(r, "full_name", "Full Name", "Name")
            first = pick(r, "first_name", "First Name", "Firstname")
            last = pick(r, "last_name", "Last Name", "Lastname", "Surname")
            first, last = split_name(full, first, last)
            if not full:
                full = " ".join(x for x in (first, last) if x)

            purl = norm_linkedin(pick(r, "person_linkedin_url", "linkedin_url",
                                      "person linkedin url", "linkedin url",
                                      "profile_url", "profile url", "profileurl", "profile"))
            if purl and purl in seen_urls:
                dupes += 1
                continue
            if purl:
                seen_urls.add(purl)

            title = pick(r, "title", "job_title", "jobtitle", "position", "job title")
            people.append({
                "person_id": (purl.rsplit("/", 1)[-1] or full).lower()[:64],
                "full_name": full,
                "first_name": first,
                "last_name": last,
                "title": title,
                "seniority": seniority_of(title),
                "company_name": company,
                "company_slug": slug,
                "company_linkedin_url": pick(r, "company_linkedin_url", "company linkedin_url",
                                             "company linkedin url"),
                "person_linkedin_url": purl,
                "email_guess": pick(r, "email_guess", "email", "Email"),
                "location_country": pick(r, "location_country", "country",
                                          "company headquarter_country"),
                "location_city": pick(r, "location_city", "city", "location",
                                       "company headquarter_city"),
                "years_in_role": pick(r, "years_in_role", "Years In Role", "Tenure"),
                "profile_summary": pick(r, "profile_summary", "summary", "headline", "bio")[:400],
            })
            kept += 1
        print(f"  {f.name}: {len(rows)} rows → {kept} kept")

    if not people:
        print("\n✗ zero people matched the shortlist. Either the export is for the wrong "
              "companies, or the company names differ so much that even slug matching "
              "fails — check the unmatched list below.", file=sys.stderr)

    dst = cdir / "people-raw.csv"
    if args.dry_run:
        print("\n  (--dry-run: nothing written)")
    else:
        if dst.exists() and not args.overwrite:
            print(f"\n✗ {rel(dst)} already exists. This campaign may have already shipped "
                  "from it —\n  pass --overwrite to replace it, or --dry-run to only see the "
                  "numbers.", file=sys.stderr)
            return 1
        write_csv(dst, people, PEOPLE_COLUMNS)

    covered = {p["company_slug"] for p in people}
    gaps = sorted(set(shortlist) - covered)

    print(f"\n{'-' * 66}")
    print(f"  people kept            {len(people)}")
    print(f"  duplicate profiles     {dupes}")
    print(f"  companies covered      {len(covered)} of {len(shortlist)}")
    missing_id = sum(1 for p in people if not p["person_linkedin_url"])
    print(f"  missing LinkedIn URL   {missing_id}")
    if not args.dry_run:
        print(f"\n→ wrote {rel(dst)}")

    # The two silent-failure modes of the old name-based join, now printed instead.
    if gaps:
        print(f"\n⚠ {len(gaps)} shortlisted companies got ZERO people — a Sales Navigator "
              "gap, not a fit decision:")
        for g in gaps[:15]:
            print(f"    · {shortlist[g].get('company_name') or g}")
        if len(gaps) > 15:
            print(f"    … and {len(gaps) - 15} more")
    if unmatched:
        top = sorted(unmatched.items(), key=lambda kv: -kv[1])[:10]
        total = sum(unmatched.values())
        print(f"\n⚠ {total} people dropped: their company is not in the shortlist. "
              "Check for a name mismatch before accepting this:")
        for name, n in top:
            print(f"    · {name} ({n})")
    if missing_id:
        print(f"\n✗ {missing_id} people have no LinkedIn URL. closely.io cannot act on "
              "them — fix the export before `validate`.", file=sys.stderr)
        return 1
    return 0 if people else 1


# --------------------------------------------------------------- P1.10 check-import

# SIX different header layouts exist across the 11 import CSVs on disk (audited
# 2026-09-02). What is stable in every one of them is the identity triplet; what drifts is
# everything else:
#
#   company : company | company_name          title : title | job_title
#   msg 1   : message_1 | message_m1 | message_step1
#   msg 2   : message_2 | message_m2 | message_step2
#   extras  : location, connection_note, campaign_tag, tag, segment, angle, priority,
#             contact_id, person_id, email_guess
#
# So this check is strict where it matters and alias-tolerant where it does not. Being
# strict on `company` vs `company_name` would have rejected
# `2026-08-07-us-digital-fitness/closelyhq-import-batch1.csv` — the file closely.io
# actually accepted and sent 124 invites from. The column mapping happens in closely.io's
# own import UI; what closely.io cannot invent is a missing name or profile URL.
IDENTITY_COLUMNS = ["first_name", "last_name", "linkedin_url"]

COLUMN_ALIASES: dict[str, tuple[str, ...]] = {
    "company": ("company", "company_name", "account_name"),
    "title": ("title", "job_title", "position"),
    "message_1": ("message_1", "message_m1", "message_step1"),
    "message_2": ("message_2", "message_m2", "message_step2"),
}

# The canonical shape closelyhq-importer.md documents, for the drift report.
CANONICAL = ("first_name", "last_name", "linkedin_url", "company", "title",
             "message_1", "message_2")


def resolve_alias(cols: list[str], logical: str) -> str | None:
    """Which actual column carries this logical field, if any."""
    lower = {c.lower(): c for c in cols}
    for cand in COLUMN_ALIASES[logical]:
        if cand in lower:
            return lower[cand]
    return None


def cmd_check_import(args) -> int:
    src = resolve_input(args, ("closelyhq-import.csv", "closelyhq-import-full.csv"))
    if src is None or not src.exists():
        print(f"✗ no import CSV found ({src if src else 'none'})", file=sys.stderr)
        return 2
    rows = read_csv(src)
    print(f"→ {rel(src)}: {len(rows)} rows\n")
    if not rows:
        print("✗ file has no rows", file=sys.stderr)
        return 1

    cols = [c for c in rows[0] if c]
    problems: list[str] = []

    # A third or fourth touch means the pre-2026-08 four-message sequence. That is a
    # regenerate, not a mapping issue: message-sequencer now writes exactly two.
    legacy = [c for c in cols if re.fullmatch(r"message_step[34]", c.lower())]
    if legacy:
        problems.append(
            f"legacy 4-step sequence: {', '.join(legacy)}. Since 2026-08 the sequence is "
            "2 messages (note-less invite → M1 on accept → M2 +5 days). Regenerate."
        )

    for c in IDENTITY_COLUMNS:
        if c not in [x.lower() for x in cols]:
            problems.append(f"missing identity column `{c}` — closely.io cannot invent it")

    mapping: dict[str, str | None] = {k: resolve_alias(cols, k) for k in COLUMN_ALIASES}
    for logical, actual in mapping.items():
        if actual is None:
            problems.append(
                f"no column carries `{logical}` (tried: {', '.join(COLUMN_ALIASES[logical])})"
            )

    drift = [f"{k} → {v}" for k, v in mapping.items() if v and v != k]
    if drift:
        warn_drift = ", ".join(drift)
        print(f"  ⚠ header drift vs the documented schema: {warn_drift}")
        print("    Accepted (closely.io maps columns at import), but six different layouts "
              "now exist across 11 import files — worth converging.\n")

    # The actual 2026-07-16 bug: the column existed and every cell in it was blank.
    # Presence is not the test. Non-emptiness is.
    blank_counts: dict[str, int] = {}
    for c in IDENTITY_COLUMNS:
        if c not in cols:
            continue
        n = sum(1 for r in rows if not (r.get(c) or "").strip())
        if n:
            blank_counts[c] = n

    bad_urls = [
        (i, (r.get("linkedin_url") or "").strip())
        for i, r in enumerate(rows, start=2)
        if (r.get("linkedin_url") or "").strip()
        and "linkedin.com" not in (r.get("linkedin_url") or "").lower()
    ]

    m1, m2 = mapping["message_1"], mapping["message_2"]
    empty_msg = sum(
        1 for r in rows
        if not (r.get(m1) or "").strip() or not (r.get(m2) or "").strip()
    ) if m1 and m2 else 0

    # The copy gate. A row can carry a name, a URL and two messages and still be
    # unsendable, because the messages break rules the pipeline already has:
    #   message_1 <= 600 chars, message_2 <= 550   (message-sequencer.md, lines 42-43)
    #   em dash is a hard ban, no exceptions        (CLAUDE.md section 6)
    # Without this, a mechanically-correct file looks ready. `2026-07-16-au-telehealth`
    # is the case: its 253 messages are the old 4-touch shape, and remapping Step2 into
    # message_1 gives 253/253 rows over the 600 cap (median 902) with an em dash in
    # 253/253. Identity-only checks would have waved that through.
    CAPS = {"message_1": 600, "message_2": 550}
    over_cap: dict[str, tuple[int, int]] = {}
    emdash: dict[str, int] = {}
    for logical, cap in CAPS.items():
        col = mapping[logical]
        if not col:
            continue
        lens = [len((r.get(col) or "").strip()) for r in rows]
        n_over = sum(1 for L in lens if L > cap)
        if n_over:
            over_cap[logical] = (n_over, max(lens))
        n_dash = sum(1 for r in rows if re.search(r"[—–]", r.get(col) or ""))
        if n_dash:
            emdash[logical] = n_dash

    for p in problems:
        print(f"  ✗ {p}")
    for c, n in blank_counts.items():
        pct = 100 * n / len(rows)
        print(f"  ✗ `{c}` is blank in {n}/{len(rows)} rows ({pct:.0f}%)")
    if bad_urls:
        print(f"  ✗ {len(bad_urls)} rows have a linkedin_url that is not a LinkedIn URL "
              f"(first: line {bad_urls[0][0]} {bad_urls[0][1][:50]!r})")
    if empty_msg:
        print(f"  ✗ {empty_msg} rows are missing message_1 or message_2")
    for logical, (n, longest) in over_cap.items():
        print(f"  ✗ {logical} over the {CAPS[logical]}-char cap in {n}/{len(rows)} rows "
              f"(longest {longest}) — message-sequencer.md lines 42-43")
    for logical, n in emdash.items():
        print(f"  ✗ em dash in {logical} in {n}/{len(rows)} rows — hard ban, CLAUDE.md §6")

    failed = bool(problems or blank_counts or bad_urls or empty_msg or over_cap or emdash)
    print(f"\n{'-' * 66}")
    if failed:
        print("✗ IMPORT NOT SENDABLE. closely.io needs a name and a profile URL per row;\n"
              "  blank identity columns produce a campaign that silently sends to nobody.\n"
              "  This is exactly how 2026-07-16-au-telehealth lost 253 contacts for 7 weeks.",
              file=sys.stderr)
        return 1
    print(f"✓ import CSV is sendable — {len(rows)} rows, identity and both messages present")
    return 0


# --------------------------------------------------------------------------- main

# ------------------------------------------------- check-classified (step 8 output)

CATEGORIES = {"interested", "maybe-later", "referral", "decline", "negative", "question",
              "out-of-office", "other/unclear"}
CONFIDENCES = {"high", "medium", "low"}


def cmd_check_classified(args) -> int:
    """Gate the step-8 output before step 9 reads it.

    An agent writing a CSV by hand can emit an unquoted comma, and then every column after
    it shifts one to the left in silence. That happened on the first real run:
    `2026-07-23-israel-telehealth` had `Clalit Health Services (Innovation Center, South
    District)` written unquoted, so `response_date` held " South District)", `category`
    held a timestamp and `confidence` held "question". Nothing complained —
    `campaign-analyzer` would simply have counted a timestamp as a category.

    A row with exactly one extra field is repairable and this says so; anything else is
    reported for a human.
    """
    src = resolve_input(args, ("responses-classified.csv",))
    if src is None or not src.exists():
        print(f"✗ no responses-classified.csv — run step 8 first", file=sys.stderr)
        return 2

    with src.open(newline="", encoding="utf-8-sig") as fh:
        raw = list(csv.reader(fh))
    if len(raw) < 2:
        print("✗ file has no data rows", file=sys.stderr)
        return 1
    hdr, data = raw[0], raw[1:]
    print(f"→ {rel(src)}: {len(data)} rows, {len(hdr)} columns\n")

    problems: list[str] = []
    for i, r in enumerate(data, start=2):
        if len(r) != len(hdr):
            extra = len(r) - len(hdr)
            hint = (" — one extra field: almost certainly an unquoted comma inside a "
                    "value; re-quote it and the columns line up again") if extra == 1 else ""
            problems.append(f"line {i}: {len(r)} fields against {len(hdr)} columns{hint}")

    rows = [dict(zip(hdr, r)) for r in data if len(r) == len(hdr)]
    for i, r in enumerate(rows, start=2):
        cat = (r.get("category") or "").strip().lower()
        if cat not in CATEGORIES:
            problems.append(f"line {i}: category {cat!r} is not one of the eight "
                            "documented values")
        conf = (r.get("confidence") or "").strip().lower()
        if conf and conf not in CONFIDENCES:
            problems.append(f"line {i}: confidence {conf!r} is not high/medium/low")
        if not (r.get("person_id") or r.get("linkedin_url") or "").strip():
            problems.append(f"line {i}: no person_id and no linkedin_url — unattributable")

    for p_ in problems:
        print(f"  ✗ {p_}")

    counts: dict[str, int] = {}
    for r in rows:
        c = (r.get("category") or "?").strip().lower()
        counts[c] = counts.get(c, 0) + 1
    print(f"\n{'-' * 66}")
    for c in sorted(counts, key=lambda k: -counts[k]):
        print(f"  {c:<16} {counts[c]}")
    hot = sum(counts.get(c, 0) for c in ("interested", "question", "referral"))
    print(f"\n  needs a human: {hot}")

    if problems:
        print(f"\n✗ {len(problems)} problem(s) — step 9 would read these as data.",
              file=sys.stderr)
        return 1
    print("\n✓ responses-classified.csv is well-formed")
    return 0


# ------------------------------------------------------------- P2.13 remind

TELEGRAM_ENV = Path.home() / ".hermes" / ".env"


def telegram_send(text: str) -> bool:
    """Push one message to Vadim's Telegram. Same convention as check-agent-copies.py.

    The token goes through `curl --config -` and never through argv: this runs from cron
    and /proc is world-readable. `-sf` so an HTTP 400/429 is a failure here rather than a
    silent success.
    """
    import subprocess
    bot = chat = ""
    try:
        for line in TELEGRAM_ENV.open(encoding="utf-8"):
            if line.startswith("TELEGRAM_BOT_TOKEN="):
                bot = line.split("=", 1)[1].strip()
            elif line.startswith("TELEGRAM_ALLOWED_USERS="):
                chat = line.split("=", 1)[1].strip().split(",")[0]
    except OSError:
        pass
    if not bot or not chat:
        print("(no TELEGRAM creds in ~/.hermes/.env — not sending)", file=sys.stderr)
        return False
    try:
        subprocess.run(
            ["curl", "-sf", "-m", "15", "--config", "-",
             "--data-urlencode", f"chat_id={chat}",
             "--data-urlencode", f"text={text}"],
            input=f'url = "https://api.telegram.org/bot{bot}/sendMessage"\n',
            text=True, check=True, capture_output=True)
        return True
    except Exception as e:  # noqa: BLE001
        print(f"(Telegram failed: {type(e).__name__})", file=sys.stderr)
        return False


def cmd_remind(args) -> int:
    """Weekly digest of what outbound is waiting on.

    Ten of eleven campaigns were blocked on a manual export by Vadim on 2026-09-02, eight
    of them on the same `responses-raw.csv`, and steps 8-9 had therefore never run once
    across 1276 sent messages. Nothing surfaced that: `status` only tells you when you
    think to run it, and nobody runs a status command about work they have forgotten.

    Deliberately NOT fingerprint-deduplicated (unlike check-agent-copies.py --notify): a
    standing blocker is exactly what this is for, and going quiet about it would reproduce
    the failure. The cadence keeps it bearable — weekly, not daily.
    """
    cdirs = sorted(p for p in REG.campaigns_dir().iterdir() if p.is_dir()
                   and not p.name.startswith("_"))
    waiting: list[tuple[str, str, str]] = []
    other: list[tuple[str, str, str]] = []
    for cdir in cdirs:
        stage, blocker = REG.stage_of(cdir)
        if stage.startswith("10"):
            continue
        prof = REG.infer_profile(cdir.name) or "?"
        (waiting if blocker.startswith("VADIM:") else other).append(
            (cdir.name, prof, blocker.replace("VADIM: ", ""))
        )

    lines = [f"Outbound — {len(waiting)} campaign(s) waiting on you, "
             f"{len(other)} on the pipeline"]
    if waiting:
        # Group on the ASK, not on the annotated string. stage_of() appends
        # "[skipped: companies]" and "⚠ …" notes per campaign, and grouping on those split
        # one ask into three groups — which buries the fact that six campaigns are stuck
        # behind the same single export.
        by_blocker: dict[str, list[str]] = {}
        for name, prof, blocker in waiting:
            ask = re.split(r"\s*(?:\[skipped:|⚠)", blocker)[0].strip()
            note = blocker[len(ask):].strip()
            label = f"{name} ({prof})" + (f"  {note}" if note else "")
            by_blocker.setdefault(ask, []).append(label)
        lines.append("")
        for blocker, names in sorted(by_blocker.items(), key=lambda kv: -len(kv[1])):
            lines.append(f"• {blocker}  [{len(names)}]")
            for n in names:
                lines.append(f"    – {n}")
    if other:
        lines.append("")
        lines.append("Pipeline side:")
        for name, prof, blocker in other:
            lines.append(f"• {name} ({prof}): {blocker}")

    text = "\n".join(lines)
    print(text)

    if not args.notify:
        return 0
    if not waiting and not other:
        print("\n(nothing outstanding — not sending)")
        return 0
    return 0 if telegram_send(text) else 1


# -------------------------------------------------------- P2.12 check-responses

# response-classifier.md: person_id (or linkedin_url to join on), response_date,
# response_text, which_message_replied_to.
RESPONSE_REQUIRED = ("response_date", "response_text")
RESPONSE_JOIN = ("person_id", "linkedin_url", "person_linkedin_url")


def cmd_check_responses(args) -> int:
    """Gate a responses export before step 8 touches it.

    Whatever route the replies arrive by — a manual closely.io export, a HubSpot pull, a
    browser session — step 8 needs the same four fields. This says whether the file it got
    is one the classifier can actually work with, and whether the replies can be joined
    back to the people and messages on disk.
    """
    src = resolve_input(args, ("responses-raw.csv",))
    if src is None or not src.exists():
        print(f"✗ no responses-raw.csv in {rel(campaign_dir(args.campaign))}.\n"
              "  Step 8 (response-classifier) and step 9 (campaign-analyzer) cannot run "
              "without it —\n  this is the blocker on 8 of 11 campaigns.", file=sys.stderr)
        return 2
    rows = read_csv(src)
    print(f"→ {rel(src)}: {len(rows)} rows\n")
    if not rows:
        print("✗ file has no rows", file=sys.stderr)
        return 1

    cols = [c for c in rows[0] if c]
    lower = {c.lower() for c in cols}
    problems: list[str] = []

    # Pick the join column that actually HAS values, not merely the first one present.
    # closely-pull writes a `person_id` column always, but leaves it empty for a campaign
    # whose own files carry no person_id (2026-07-23-israel-telehealth). Choosing the
    # empty column then reported "0 matched, 4 not found" on a perfectly good export.
    def _filled(col: str) -> int:
        actual = next((c for c in cols if c.lower() == col), None)
        if not actual:
            return -1
        return sum(1 for r in rows if (r.get(actual) or "").strip())

    join_col = None
    for cand in RESPONSE_JOIN:
        n = _filled(cand)
        if n > 0:
            join_col = next(c for c in cols if c.lower() == cand)
            if n < len(rows):
                print(f"  ⚠ join column `{join_col}` is filled in only {n}/{len(rows)} rows")
            break
    if join_col is None and any(_filled(c) == 0 for c in RESPONSE_JOIN):
        empty = [c for c in RESPONSE_JOIN if _filled(c) == 0]
        problems.append(
            f"join column(s) present but EMPTY in every row: {', '.join(empty)} — "
            "nothing can be tied back to a person"
        )
    if not join_col:
        problems.append(
            f"no join column: need one of {', '.join(RESPONSE_JOIN)} — without it a reply "
            "cannot be tied back to the person or to messages/{person_id}.md"
        )
    for c in RESPONSE_REQUIRED:
        if c not in lower:
            problems.append(f"missing required column `{c}`")

    blanks = {c: sum(1 for r in rows if not (r.get(c) or "").strip())
              for c in RESPONSE_REQUIRED if c in lower}
    blanks = {k: v for k, v in blanks.items() if v}

    # Can the replies actually be joined to what is on disk?
    cdir = campaign_dir(args.campaign) if args.campaign else src.parent
    matched = unmatched = 0
    if join_col:
        # EVERY people file, and index person_id, full URL and bare lid alike. Two real
        # campaigns break a narrower reading, both against a correct export on 2026-09-02:
        # the UK one keeps its contacts only in `people-raw-batch2.csv`, and the Israel one
        # has no `person_id` column at all (`people-to-sequence.csv`, keyed on
        # linkedin_url). Each reported 0 matches and looked like a wrong-campaign export.
        known: set[str] = set()
        for p in sorted(cdir.glob("people-*.csv")) + sorted(cdir.glob("*/people-*.csv")):
            try:
                for r in read_csv(p):
                    if r.get("person_id"):
                        known.add(r["person_id"].strip())
                    u = REG.norm_linkedin(pick(r, "linkedin_url", "person_linkedin_url"))
                    if u:
                        known.add(u)
                        known.add(u.rsplit("/", 1)[-1].lower())
            except (OSError, csv.Error):
                continue
        if known:
            for r in rows:
                v = (r.get(join_col) or "").strip()
                key = REG.norm_linkedin(v) if "linkedin" in join_col else v
                lid = key.rsplit("/", 1)[-1].lower() if "linkedin" in join_col else ""
                if key and (key in known or (lid and lid in known)):
                    matched += 1
                else:
                    unmatched += 1

    for p in problems:
        print(f"  ✗ {p}")
    for c, n in blanks.items():
        print(f"  ✗ `{c}` blank in {n}/{len(rows)} rows")
    if join_col and (matched or unmatched):
        print(f"  · join on `{join_col}`: {matched} matched, {unmatched} not found "
              "in people-validated/people-raw")
        if unmatched and unmatched >= matched:
            problems.append(
                f"{unmatched} of {len(rows)} replies do not match any known person — "
                "wrong campaign export, or the join column is a different id"
            )
            print(f"  ✗ more unmatched than matched — check the export is for this campaign")

    print(f"\n{'-' * 66}")
    if problems or blanks:
        print("✗ responses-raw.csv is not usable by step 8 yet.", file=sys.stderr)
        return 1
    print(f"✓ responses-raw.csv is ready — run `/outbound responses {args.campaign or ''}`")
    return 0


# ----------------------------------------------------- P2.11 fix-validated

def cmd_fix_validated(args) -> int:
    """Put the identity columns back into a validated list, from people-raw.csv.

    `2026-07-16-au-telehealth/people-validated.csv` carries
    `person_id, full_name, title, company_name, decision, priority, reason,
    recommended_message_angle` — no first_name, no last_name, no linkedin_url. The ad-hoc
    `icp_validate.py` dropped them, so the importer had nothing to map and wrote 253 rows
    with blank identity.

    The data was never lost: all 253 batch ids are present in `people-raw.csv` and all 253
    have a non-empty person_linkedin_url. This re-joins them on person_id. Non-destructive
    — writes a new file and leaves the original as the record of what shipped.
    """
    cdir = campaign_dir(args.campaign)
    raw_p = cdir / "people-raw.csv"
    val_p = cdir / (args.infile or "people-validated.csv")
    if not raw_p.exists():
        print(f"✗ {rel(raw_p)} not found — nothing to re-join identity from", file=sys.stderr)
        return 2
    if not val_p.exists():
        print(f"✗ {rel(val_p)} not found", file=sys.stderr)
        return 2

    raw = {r["person_id"]: r for r in read_csv(raw_p) if r.get("person_id")}
    val = read_csv(val_p)
    print(f"→ {rel(val_p)}: {len(val)} rows | {rel(raw_p)}: {len(raw)} people\n")

    ident = ["first_name", "last_name", "person_linkedin_url", "company_linkedin_url",
             "email_guess", "location_country", "location_city", "seniority"]
    missing_id = restored = no_url = 0
    out: list[dict] = []
    for r in val:
        pid = (r.get("person_id") or "").strip()
        src_row = raw.get(pid)
        if not src_row:
            missing_id += 1
        else:
            for c in ident:
                if not (r.get(c) or "").strip():
                    r[c] = src_row.get(c, "")
            # the column closelyhq-importer maps from
            r.setdefault("linkedin_url", "")
            if not r["linkedin_url"].strip():
                r["linkedin_url"] = src_row.get("person_linkedin_url", "")
            restored += 1
        if not (r.get("linkedin_url") or "").strip():
            no_url += 1
        out.append(r)

    fields = [c for c in val[0] if c]
    for c in ident + ["linkedin_url"]:
        if c not in fields:
            fields.append(c)

    dst = val_p.with_name(f"{val_p.stem}-with-identity.csv")
    if dst.exists() and not args.overwrite:
        print(f"✗ {rel(dst)} exists — pass --overwrite", file=sys.stderr)
        return 1
    write_csv(dst, out, fields)

    decisions: dict[str, int] = {}
    for r in out:
        d = (r.get("decision") or "?").strip()
        decisions[d] = decisions.get(d, 0) + 1

    print(f"  identity restored     {restored}/{len(val)}")
    print(f"  person_id not in raw  {missing_id}")
    print(f"  still without a URL   {no_url}")
    print(f"  decisions             {decisions}")
    print(f"\n→ wrote {rel(dst)}")
    if no_url:
        print(f"\n✗ {no_url} rows still have no LinkedIn URL", file=sys.stderr)
        return 1
    print("\n✓ every row now carries a name and a LinkedIn URL — "
          "message-sequencer and closelyhq-importer can run against this file")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        prog="outbound-pipeline.py",
        description="Mechanical outbound steps as tested code (no pandas — it is not installed).",
    )
    sub = ap.add_subparsers(dest="cmd", required=True)

    v = sub.add_parser("validate-companies", help="gate the step-2 companies list")
    v.add_argument("--campaign", required=True)
    v.add_argument("--in", dest="infile")
    v.add_argument("--profile", choices=PROFILES)
    v.add_argument("--write-routed", action="store_true",
                   help="write companies-routed-out.csv with the owning profile per row")
    v.set_defaults(func=cmd_validate_companies)

    e = sub.add_parser("extract-people", help="step 3: normalise Sales Navigator, join by slug")
    e.add_argument("--campaign", required=True)
    e.add_argument("--in", dest="infile", help="companies CSV to join against")
    e.add_argument("--profile", choices=PROFILES)
    e.add_argument("--dry-run", action="store_true",
                   help="report the numbers, write nothing")
    e.add_argument("--overwrite", action="store_true",
                   help="replace an existing people-raw.csv (it may be a shipped list)")
    e.set_defaults(func=cmd_extract_people)

    r = sub.add_parser("remind", help="weekly digest of what outbound waits on (Telegram)")
    r.add_argument("--notify", action="store_true", help="push to Vadim's Telegram")
    r.set_defaults(func=cmd_remind)

    cl = sub.add_parser("check-classified",
                        help="gate the step-8 output (catches column shifts, bad categories)")
    cl.add_argument("--campaign")
    cl.add_argument("--in", dest="infile")
    cl.add_argument("--file")
    cl.set_defaults(func=cmd_check_classified)

    q = sub.add_parser("check-responses", help="gate a responses-raw.csv before step 8")
    q.add_argument("--campaign")
    q.add_argument("--in", dest="infile")
    q.add_argument("--file")
    q.set_defaults(func=cmd_check_responses)

    fv = sub.add_parser("fix-validated",
                        help="re-join identity columns into people-validated.csv from people-raw.csv")
    fv.add_argument("--campaign", required=True)
    fv.add_argument("--in", dest="infile")
    fv.add_argument("--overwrite", action="store_true")
    fv.set_defaults(func=cmd_fix_validated)

    h = sub.add_parser("hypothesis-gate",
                       help="refuse step 2/3 when the hypothesis scope changed under the list")
    h.add_argument("--campaign", required=True)
    h.add_argument("--stamp", action="store_true",
                   help="tie the current scope to the list being built now")
    h.set_defaults(func=cmd_hypothesis_gate)

    c = sub.add_parser("check-import", help="refuse a closely.io CSV with blank identity columns")
    c.add_argument("--campaign")
    c.add_argument("--in", dest="infile")
    c.add_argument("--file", help="check any CSV by absolute path")
    c.set_defaults(func=cmd_check_import)

    args = ap.parse_args(argv)
    if args.cmd in ("check-import", "check-responses", "check-classified") \
            and not args.campaign and not args.file:
        ap.error(f"{args.cmd} needs --campaign or --file")
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
