#!/usr/bin/env python3
"""Normalize the UK Huma+Slimming World CloselyHQ export into people-raw-batch2.csv.

Key differences vs batch 1:
- Companies: only TWO targets — Huma (huma.com) and Slimming World (slimmingworld.co.uk).
- Slimming World: ~700 rows are FRANCHISE network (Consultant, District Manager, Team
  Developer, Owner, Weight Loss Consultant...) — independent group leaders, NOT corporate
  buyers. They are tagged in profile_summary so the ICP validator can FAIL them correctly,
  while HQ roles (Product Manager, Software Developer, Digital Designer, engineering,
  marketing, HR) stay as genuine prospects.
- Everything else (NHS, schools, taxi firms, Utility Warehouse...) stays with its cleaned
  raw name so the ICP validator FAILs it as non-target noise.
"""

import csv
import hashlib
import re
from collections import Counter

CAMP = "/home/vadim_prod/3dlook-marketing/marketing_vb/workspace/outbound/campaigns/2026-07-31-uk-telehealth-digital-health"
SRC = f"{CAMP}/sales-nav-raw/export-uk-huma-slimming.csv"
DST = f"{CAMP}/people-raw-batch2.csv"

DOMAIN_TO_COMPANY = {
    "huma.com": "Huma",
    "slimmingworld.co.uk": "Slimming World",
}

NAME_TO_COMPANY = {
    "Huma": "Huma",
    "huma": "Huma",
    "Slimming World": "Slimming World",
    "SLIMMING WORLD": "Slimming World",
    "slimming world": "Slimming World",
    "Slimming World UK": "Slimming World",
    "Slimming World magazine": "Slimming World",
}

EMPLOYMENT_SUFFIX_RE = re.compile(
    r"\s*\.\s*(Full-time|Part-time|Contract|Freelance|Self-employed|"
    r"Permanent|Temporary|Internship|Undefined|Apprenticeship)\s*$",
    re.IGNORECASE,
)

# Franchise/field-network titles at Slimming World → NOT corporate buyers
FRANCHISE_TITLE_RE = re.compile(
    r"(consultant|district manager|team developer|team leader|owner|"
    r"weight loss consultant|slimming consultant|field support|"
    r"franchisee|group leader|promoter)", re.IGNORECASE,
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
    name = re.sub(r"\s{2,}", " ", name)
    return name.strip()


def canonical_company(raw_name: str, website: str) -> str:
    cleaned = clean_company(raw_name)
    if not cleaned:
        return cleaned
    if website:
        w = website.strip().lower()
        for domain, comp in DOMAIN_TO_COMPANY.items():
            if domain in w:
                return comp
    lower = cleaned.lower()
    for raw, comp in NAME_TO_COMPANY.items():
        if raw.lower() == lower:
            return comp
    # "Slimming World" variants with city/extra suffix → Slimming World franchise
    if lower.startswith("slimming world") and "consultant" not in lower:
        return "Slimming World"
    if "slimmingworld" in lower.replace(" ", ""):
        return "Slimming World"
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
    if any(k in t for k in ("founder", "co-founder")):
        return "Founder/Owner"
    if any(k in t for k in ("manager", "lead")):
        return "Manager"
    if any(k in t for k in ("board", "advisor", "advisory")):
        return "Board/Advisor"
    if any(k in t for k in ("md", "medical director", "physician", "doctor",
                            "surgeon", "clinician", "pharmacist", "nurse")):
        return "Medical"
    return "Individual"


def main():
    with open(SRC, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    out = []
    franchise_count = 0
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
        country = (r.get("company location_country", "") or r.get("location", "") or "").strip()
        city = (r.get("company location_city", "") or "").strip()
        headline = (r.get("headline", "") or "").strip()
        bio = (r.get("bio", "") or "").strip()
        industry = (r.get("industry", "") or "").strip()
        summary = f"{headline} | {bio}"[:500] if bio else headline[:500]
        if industry:
            summary = f"[industry: {industry}] {summary}"[:520]

        # Franchise detection for Slimming World
        is_franchise = company == "Slimming World" and bool(FRANCHISE_TITLE_RE.search(title))
        if is_franchise:
            franchise_count += 1
            summary = f"[SLIMMING WORLD FRANCHISE/field network — NOT corporate HQ] {summary}"[:540]

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
            "location_country": country,
            "location_city": city,
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
    print(f"Slimming World franchise/field rows tagged: {franchise_count}")
    print(f"\nTop companies:")
    for c, cnt in companies.most_common(20):
        print(f"  {cnt:4d}  {c}")
    print(f"\nCountry distribution:")
    for c, cnt in countries.most_common(8):
        print(f"  {cnt:4d}  {c}")
    print(f"\nSeniority:")
    for s, cnt in seniorities.most_common():
        print(f"  {s}: {cnt}")

    # HQ vs franchise split for Slimming World
    sw = [o for o in out if o["company_name"] == "Slimming World"]
    sw_hq = [o for o in sw if "FRANCHISE" not in o["profile_summary"]]
    print(f"\nSlimming World: {len(sw)} total → HQ/corporate-ish: {len(sw_hq)}, franchise/field: {len(sw) - len(sw_hq)}")
    print(f"Huma: {sum(1 for o in out if o['company_name'] == 'Huma')}")


if __name__ == "__main__":
    main()
