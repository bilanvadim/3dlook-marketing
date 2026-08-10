#!/usr/bin/env python3
"""Normalize a CloselyHQ export CSV into people-raw.csv for the outbound pipeline.

Cleans company name artifacts (employment-type suffixes), normalizes known
aliases, computes person_id, seniority, and profile_summary.

Usage:
  python3 normalize-closelyhq-csv.py <input.csv> <output.csv>
"""

import csv
import hashlib
import re
import sys

# Known company name aliases → canonical
COMPANY_ALIASES = {
    "Suomen Terveystalo Oy": "Terveystalo",
    "Doktor.Se": "Doktor.se",
    # Add more as discovered
}

OUT_COLS = [
    "person_id", "full_name", "first_name", "last_name", "title", "seniority",
    "company_name", "company_linkedin_url", "person_linkedin_url",
    "email_guess", "location_country", "location_city",
    "years_in_role", "profile_summary",
]

# Employment-type suffixes CloselyHQ leaks into company_name
EMPLOYMENT_SUFFIX_RE = re.compile(
    r"\s*\.\s*(Full-time|Part-time|Contract|Freelance|Self-employed|"
    r"Permanent|Temporary|Internship|Undefined)\s*$",
    re.IGNORECASE,
)


def clean_company(name: str) -> str:
    """Remove employment-type artifacts and normalize known aliases."""
    if not name:
        return ""
    name = name.strip()
    name = EMPLOYMENT_SUFFIX_RE.sub("", name)
    name = name.strip()
    return COMPANY_ALIASES.get(name, name)


def detect_seniority(title: str) -> str:
    """Detect seniority level from job title."""
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
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input.csv> <output.csv>")
        sys.exit(1)

    src, dst = sys.argv[1], sys.argv[2]

    with open(src, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with open(dst, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=OUT_COLS)
        writer.writeheader()

        for r in rows:
            linkedin_url = (r.get("linkedin_url", "") or "").strip()
            person_id = hashlib.md5(linkedin_url.encode()).hexdigest()[:12]
            first = (r.get("first_name", "") or "").strip()
            last = (r.get("last_name", "") or "").strip()
            full = f"{first} {last}".strip()
            title = (r.get("job_title", "") or "").strip()
            company_raw = (r.get("company_name", "") or "").strip()
            company_clean = clean_company(company_raw)
            company_linkedin = (r.get("company linkedin_url", "") or "").strip()
            location = (r.get("location", "") or "").strip()
            headline = (r.get("headline", "") or "").strip()
            bio = (r.get("bio", "") or "").strip()
            summary = f"{headline} | {bio}"[:500] if bio else headline[:500]
            seniority = detect_seniority(title)

            writer.writerow({
                "person_id": person_id,
                "full_name": full,
                "first_name": first,
                "last_name": last,
                "title": title,
                "seniority": seniority,
                "company_name": company_clean,
                "company_linkedin_url": company_linkedin,
                "person_linkedin_url": linkedin_url,
                "email_guess": "",
                "location_country": location,
                "location_city": "",
                "years_in_role": "",
                "profile_summary": summary,
            })

    # Stats
    from collections import Counter
    companies = Counter(r["company_name"] for r in rows)
    countries = Counter(r.get("location", "").strip() for r in rows)
    seniorities = Counter(detect_seniority(r.get("job_title", "")) for r in rows)

    print(f"Done. {len(rows)} contacts → {dst}")
    print(f"Unique companies: {len(companies)}")
    print(f"Unique countries: {len(countries)}")
    print(f"\nTop companies:")
    for c, cnt in companies.most_common(10):
        print(f"  {c}: {cnt}")
    print(f"\nSeniority:")
    for s, cnt in seniorities.most_common():
        print(f"  {s}: {cnt}")


if __name__ == "__main__":
    main()
