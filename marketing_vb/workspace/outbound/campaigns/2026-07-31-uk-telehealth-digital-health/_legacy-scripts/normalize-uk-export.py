#!/usr/bin/env python3
"""Normalize the UK telehealth CloselyHQ export into people-raw.csv for the outbound pipeline.

Differs from the generic normalize-closelyhq-csv.py:
- Uses company website_url as the source of truth for canonical company names
  (the export contains heavy noise: fake "ZOE"/"Peppy" companies from unrelated
  countries/people named Zoe — these must NOT collapse into the real target companies).
- Keeps noise rows with their cleaned raw company name so the ICP validator can FAIL them.
"""

import csv
import hashlib
import re
from collections import Counter

SRC = "/home/vadim_prod/3dlook-marketing/marketing_vb/workspace/outbound/campaigns/2026-07-31-uk-telehealth-digital-health/sales-nav-raw/export-uk-new-hypothesis.csv"
DST = "/home/vadim_prod/3dlook-marketing/marketing_vb/workspace/outbound/campaigns/2026-07-31-uk-telehealth-digital-health/people-raw.csv"

# Canonical company by website domain (target companies from companies.md)
DOMAIN_TO_COMPANY = {
    "joinzoe.com": "Zoe",
    "peppy.health": "Peppy",
    "vira.health": "Vira Health",
    "hertilityhealth.com": "Hertility",
    "physitrack.com": "Physitrack",
    "thebodycoach.com": "The Body Coach",
    "thriva.co": "Thriva",
    "sweatco.in": "Sweatcoin",
    "healthierweight.co.uk": "Healthier Weight",
    "newsonhealth.co.uk": "Newson Health",
    "onefiit.com": "ONE FIIT",
    "huma.com": "Huma",
    "flo.health": "Flo Health",
    "slimmingworld.co.uk": "Slimming World",
    "onstella.com": "Vira Health",
}

# Raw-company-name → canonical (used ONLY when website is empty — for names that
# are unambiguous). Zoe/Peppy/Fiit are deliberately NOT here: the export has many
# fake rows ("Zoe" shop owners in Zambia/Burundi, "Peppy" cafes in Indonesia, etc.)
# that must stay as noise so the ICP validator can FAIL them.
NAME_TO_COMPANY = {
    "Vira Health": "Vira Health",
    "Hertility": "Hertility",
    "Hertility Health": "Hertility",
    "Thriva": "Thriva",
    "Thriva Health": "Thriva",
    "Sweatcoin": "Sweatcoin",
    "Physitrack PLC": "Physitrack",
    "The Body Coach": "The Body Coach",
    "Healthier Weight": "Healthier Weight",
    "Newson Health Limited": "Newson Health",
    "Newson Clinic": "Newson Health",
    "TONIC WEIGHT LOSS SURGERY LIMITED": "Tonic Weight Loss Surgery",
    "Tonic Surgery UK": "Tonic Weight Loss Surgery",
    "Flo Health": "Flo Health",
}

EMPLOYMENT_SUFFIX_RE = re.compile(
    r"\s*\.\s*(Full-time|Part-time|Contract|Freelance|Self-employed|"
    r"Permanent|Temporary|Internship|Undefined|Contract Full-time)\s*$",
    re.IGNORECASE,
)

OUT_COLS = [
    "person_id", "full_name", "first_name", "last_name", "title", "seniority",
    "company_name", "company_linkedin_url", "person_linkedin_url",
    "email_guess", "location_country", "location_city",
    "years_in_role", "profile_summary", "company_website_url",
]


def clean_company(name: str) -> str:
    if not name:
        return ""
    name = name.strip()
    name = EMPLOYMENT_SUFFIX_RE.sub("", name)
    return name.strip()


# Canonical target company names — rows whose raw name matches one of these EXACTLY
# (case-insensitive) but whose website does NOT confirm the target domain are noise
# (e.g. "Zoe" shop owners in Zambia, "Peppy" cafes in Indonesia) → marked NOISE:.
TARGET_NAMES = {
    "zoe", "peppy", "vira health", "hertility", "thriva", "sweatcoin",
    "physitrack", "the body coach", "healthier weight", "newson health",
    "newson clinic", "tonic weight loss surgery", "fiit", "flo health",
    "huma", "slimming world", "one fiit",
}


def canonical_company(raw_name: str, website: str) -> str:
    """Map to canonical target company when confident; else keep cleaned raw name."""
    cleaned = clean_company(raw_name)
    if not cleaned:
        return cleaned
    if website:
        w = website.strip().lower()
        for domain, comp in DOMAIN_TO_COMPANY.items():
            if domain in w:
                return comp
    # Website empty/unhelpful — try name map (exact or case-insensitive match)
    exact = NAME_TO_COMPANY.get(cleaned)
    if exact:
        return exact
    lower = cleaned.lower()
    for raw, comp in NAME_TO_COMPANY.items():
        if raw.lower() == lower:
            return comp
    # Name matches a target company but website doesn't confirm → noise, NOT the target
    if lower in TARGET_NAMES:
        return f"NOISE: {cleaned}"
    return cleaned


def detect_seniority(title: str) -> str:
    if not title:
        return "Unknown"
    t = title.lower()
    if any(k in t for k in ("chief", "ceo", "cto", "cfo", "cmo", "coo", "cso",
                             "cro", "cpo", "cio", "cco", "president")):
        return "C-Level"
    if any(k in t for k in ("vp ", "vice president", "svp ", "evp ")):
        return "VP"
    if any(k in t for k in ("director", "head of")):
        return "Director"
    if any(k in t for k in ("manager", "lead")):
        return "Manager"
    if any(k in t for k in ("founder", "owner")):
        return "Founder/Owner"
    if any(k in t for k in ("board", "advisor", "advisory")):
        return "Board/Advisor"
    if any(k in t for k in ("md", "medical director", "physician", "doctor",
                             "surgeon", "clinician")):
        return "Medical"
    return "Individual"


def main():
    with open(SRC, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    out = []
    for r in rows:
        linkedin_url = (r.get("linkedin_url", "") or "").strip()
        person_id = hashlib.md5(linkedin_url.encode()).hexdigest()[:12]
        first = (r.get("first_name", "") or "").strip()
        last = (r.get("last_name", "") or "").strip()
        full = f"{first} {last}".strip()
        title = (r.get("job_title", "") or "").strip()
        raw_company = (r.get("company_name", "") or "").strip()
        website = (r.get("company website_url", "") or "").strip()
        company = canonical_company(raw_company, website)
        company_linkedin = (r.get("company linkedin_url", "") or "").strip()
        location = (r.get("location", "") or "").strip()
        headline = (r.get("headline", "") or "").strip()
        bio = (r.get("bio", "") or "").strip()
        summary = f"{headline} | {bio}"[:500] if bio else headline[:500]

        out.append({
            "person_id": person_id,
            "full_name": full,
            "first_name": first,
            "last_name": last,
            "title": title,
            "seniority": detect_seniority(title),
            "company_name": company,
            "company_linkedin_url": company_linkedin,
            "person_linkedin_url": linkedin_url,
            "email_guess": "",
            "location_country": location,
            "location_city": "",
            "years_in_role": "",
            "profile_summary": summary,
            "company_website_url": website,
        })

    with open(DST, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=OUT_COLS)
        writer.writeheader()
        writer.writerows(out)

    companies = Counter(o["company_name"] for o in out)
    countries = Counter(o["location_country"] for o in out)
    seniorities = Counter(o["seniority"] for o in out)

    print(f"Done. {len(out)} contacts → {DST}")
    print(f"Unique companies (canonical): {len(companies)}")
    print(f"\nTop companies:")
    for c, cnt in companies.most_common(20):
        print(f"  {cnt:3d}  {c}")
    print(f"\nCountry distribution:")
    for c, cnt in countries.most_common(15):
        print(f"  {cnt:3d}  {c}")
    print(f"\nSeniority:")
    for s, cnt in seniorities.most_common():
        print(f"  {s}: {cnt}")

    # Noise estimate: rows whose canonical company is NOT in the target set
    targets = set(DOMAIN_TO_COMPANY.values()) | set(NAME_TO_COMPANY.values())
    noise = [o for o in out if o["company_name"] not in targets]
    print(f"\nRows NOT mapping to target companies (noise/other): {len(noise)}")
    nc = Counter(o["company_name"] for o in noise)
    for c, cnt in nc.most_common(15):
        print(f"  {cnt:3d}  {c}")


if __name__ == "__main__":
    main()
