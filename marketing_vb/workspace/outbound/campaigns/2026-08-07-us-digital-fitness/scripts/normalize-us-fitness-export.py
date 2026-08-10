#!/usr/bin/env python3
"""Normalize CloselyHQ export for 2026-08-07-us-digital-fitness (Nick/USA).

Handles:
- employment-type suffix stripping (. Full-time, . Permanent Full-time, ...)
- canonical company mapping by website_url (source of truth)
- name alias mapping for rows with empty website
- homonym/vendor/fund/self-employed noise marking (NOISE: prefix)
- day-job noise: people whose current employer is unrelated to the campaign
"""

import csv
import hashlib
import re
import sys

# ---------------------------------------------------------------------------
# Canonical target companies: website -> canonical name (highest confidence)
# ---------------------------------------------------------------------------
TARGET_BY_WEBSITE = {
    "https://future.co": "Future",
    "http://www.future.co": "Future",
    "http://future.co": "Future",
    "https://noom.com": "Noom",
    "http://noom.com": "Noom",
    "https://joinladder.com": "Ladder",
    "http://joinladder.com": "Ladder",
    "https://www.ww.com": "WW (WeightWatchers)",
    "http://www.ww.com": "WW (WeightWatchers)",
    "https://www.joincalibrate.com": "Calibrate",
    "http://www.joincalibrate.com": "Calibrate",
    "https://www.calibratehealth.com/": "Calibrate",
    "http://www.calibratehealth.com/": "Calibrate",
    "https://www.joinfound.com": "Found",
    "http://www.joinfound.com": "Found",
    "https://joinfound.com/business": "Found",
    "https://joinfound.com": "Found",
    "https://ro.co": "Ro",
    "http://ro.co": "Ro",
    "https://www.tonal.com": "Tonal",
    "http://www.tonal.com": "Tonal",
    "https://www.personifyhealth.com": "Personify Health",
    "http://www.personifyhealth.com": "Personify Health",
    "http://www.virginpulse.com": "Personify Health",
    "https://www.virginpulse.com": "Personify Health",
    "https://www.onepeloton.com": "Peloton",
    "http://www.onepeloton.com": "Peloton",
    "https://fitbod.me": "Fitbod",
    "http://fitbod.me/": "Fitbod",
    "http://fitbod.me": "Fitbod",
    "https://echelonfit.com": "Echelon",
    "http://echelonfit.com": "Echelon",
    "http://www.echeloncommercial.com": "Echelon",
    "https://hydrow.com": "Hydrow",
    "http://www.hydrow.com": "Hydrow",
    "http://hydrow.com": "Hydrow",
    "https://www.trainwell.net": "Trainwell",
    "http://www.trainwell.net?utm_source=linkedin&utm_content=company_page_button": "Trainwell",
    "https://www.myfitnesspal.com": "MyFitnessPal",
    "http://www.myfitnesspal.com": "MyFitnessPal",
    "https://www.strava.com": "Strava",
    "https://www.bodi.com": "BODi",
    "https://www.ifit.com": "iFIT",
    "http://ifit.com": "iFIT",
    "https://www.whoop.com": "Whoop",
    "https://www.joincaliber.com": "Caliber",
    "https://www.aaptiv.com": "Aaptiv",
    "https://www.fitonapp.com": "FitOn",
    "https://obefitness.com": "obé Fitness",
    "https://www.jefit.com": "Jefit",
    "https://www.vshred.com": "V Shred",
    "https://shotsyapp.com": "Shotsy",
    "https://www.shotsyapp.com": "Shotsy",
    "https://www.loseit.com": "Lose It!",
}

# ---------------------------------------------------------------------------
# Name aliases for rows with empty/unmatched website (lowercased)
# ---------------------------------------------------------------------------
TARGET_BY_NAME_ALIAS = {
    "future": "Future",
    "future corp": "Future",
    "future inc": "Future",
    "noom": "Noom",
    "ladder": "Ladder",
    "weightwatchers": "WW (WeightWatchers)",
    "ww": "WW (WeightWatchers)",
    "calibrate": "Calibrate",
    "found": "Found",
    "found corp": "Found",
    "founded": "Found",
    "ro": "Ro",
    "tonal": "Tonal",
    "personify health": "Personify Health",
    "personify": "Personify Health",
    "virgin pulse": "Personify Health",
    "ifit santé & fitness inc": "iFIT",
    "ifit santé & fitness inc.": "iFIT",
    "peloton": "Peloton",
    "peloton interactive": "Peloton",
    "fitbod": "Fitbod",
    "echelon": "Echelon",
    "echelon fitness": "Echelon",
    "echelon fitness multimedia, llc.": "Echelon",
    "echelon fitness multimedia, llc": "Echelon",
    "echelon, llc": "Echelon",
    "echelon llc": "Echelon",
    "hydrow": "Hydrow",
    "hydrow, inc.": "Hydrow",
    "hydrow, inc": "Hydrow",
    "trainwell": "Trainwell",
    "myfitnesspal": "MyFitnessPal",
    "strava": "Strava",
    "bodi": "BODi",
    "beachbody": "BODi",
    "ifit": "iFIT",
    "ifit health and fitness": "iFIT",
    "ifit santé & fitness inc.": "iFIT",
    "ifit santé & fitness inc.": "iFIT",
    "icon health and fitness": "iFIT",
    "icon health & fitness": "iFIT",
    "icon health and fitness inc": "iFIT",
    "icone health and fitness": "iFIT",
    "nordictrack": "iFIT",
    "nordictrack, inc.": "iFIT",
    "freemotion fitness": "iFIT",
    "freemotion fitness inc.": "iFIT",
    "freemotion fitness - a division of ifit": "iFIT",
    "proform fitness": "iFIT",
    "pro form fitness": "iFIT",
    "whoop": "Whoop",
    "caliber": "Caliber",
    "aaptiv": "Aaptiv",
    "fiton": "FitOn",
    "obé fitness": "obé Fitness",
    "obe fitness": "obé Fitness",
    "jefit": "Jefit",
    "v shred": "V Shred",
    "vshred": "V Shred",
    "shotsy": "Shotsy",
    "lose it!": "Lose It!",
}

# ---------------------------------------------------------------------------
# Homonym / fund / unrelated noise patterns (lowercased substring match)
# A row matching any of these is NOT the target company.
# ---------------------------------------------------------------------------
NOISE_PATTERNS = [
    # Calibrate homonyms (different businesses)
    "calibrate bodyworks", "calibrate adhd", "calibrate aero", "calibrate clinic",
    "calibrate consulting", "calibrate estates", "calibrate iv hydration",
    "calibrate network", "calibrate them", "calibrate visuals", "edge-calibrate",
    "a.d.a.s calibrate", "adaptive adas calibrate",
    # Tonal homonyms
    "tonal music", "tonal salon", "tonal yoga", "tonal domination",
    "nubian tonal science",
    # Future homonyms
    "future corp", "future inc",
    # iFIT homonyms
    "ifit golf", "ifit gourmet", "ifit lifestyle", "isle madame ifit",
    # Echelon homonyms / non-fitness
    "echelon health & fitness", "echelon health and fitness",
    # Personify homonyms
    "personify %",
    # Investment funds / VCs (people at funds, not target companies)
    "francisco partners", "delta-v capital", "recursion partners", "laveer capital",
    "westcap", "westcap group", "ta associates", "plex capital",
    # Self-employment placeholder
    "self-employed",
    # Other unrelated businesses seen in this export
    "silicon labs", "machinify", "aetna", "kaiser permanente", "boyd gaming",
    "general mills", "etsy", "reddit", "lionsgate", "bruker", "new york life",
    "commonspirit", "vivint", "giant tiger", "green imaging", "picklebos",
    "original bear", "mcfadden sales", "space dynamics laboratory",
    "webster university", "encore strategies", "cleanboss", "wondr health",
    "virta health", "chamber", "fox sports", "foxsports", "oddity", "calibrate health",
    "northern california employee benefit council", "the belasco theatre",
    "tzorin cuisine", "vitality specific chiropractic", "younker consulting",
    "handmade motion", "centerville grace church", "lifetime fitness",
    "retailsync", "ript", "trainwell.org", "train well",
    "silicon lab",
]

# Exact-match names that are pure noise (case-insensitive)
NOISE_EXACT = {
    "self-employed", "undefined", "found", "founded", "future", "personify",
    "echelon", "tonal", "ifit",
}

OUT_COLS = [
    "person_id", "full_name", "first_name", "last_name", "title", "seniority",
    "company_name", "company_linkedin_url", "person_linkedin_url",
    "email_guess", "location_country", "location_city",
    "years_in_role", "profile_summary",
]

# Employment-type suffixes to strip — handles ". Full-time", ". Permanent Full-time", etc.
SUFFIX_TOKENS = [
    "full-time", "part-time", "contract", "freelance", "self-employed",
    "permanent", "temporary", "internship", "undefined",
]


def clean_company_name(name: str) -> str:
    """Strip employment suffixes and trailing junk from a CloselyHQ company name."""
    if not name:
        return ""
    n = name.strip()
    changed = True
    while changed:
        changed = False
        # pattern: [. ]+ <token>$  OR [.] <token> $ (with optional extra employment word)
        for tok in SUFFIX_TOKENS:
            # e.g. ". Full-time", ". Permanent Full-time", ". Contract Full-time"
            m = re.search(r"\s*\.\s*([A-Za-z-]+\s+)?%s\s*$" % re.escape(tok), n, re.IGNORECASE)
            if m:
                n = n[: m.start()].strip()
                n = re.sub(r"[\s.]+$", "", n)
                changed = True
    # strip standalone trailing employment word without dot (e.g. "Tonal Full-time")
    for tok in SUFFIX_TOKENS:
        m = re.search(r"\s+%s\s*$" % re.escape(tok), n, re.IGNORECASE)
        if m:
            n = n[: m.start()].strip()
    n = re.sub(r"\s+", " ", n).strip()
    n = n.strip(" .")
    return n


def is_target_noise(name: str) -> bool:
    """Check if a cleaned company name resolves to noise (homonym/fund/unrelated)."""
    low = name.lower().strip()
    if not low:
        return True
    if low in NOISE_EXACT:
        return True
    for pat in NOISE_PATTERNS:
        if pat in low:
            return True
    return False


def resolve_company(name: str, website: str) -> str:
    """Map raw company name + website to canonical target / NOISE / raw."""
    cleaned = clean_company_name(name)
    if not cleaned:
        return "NOISE: (empty)"

    # 1) website is the source of truth for canonical mapping
    site = (website or "").strip().rstrip("/")
    if site in TARGET_BY_WEBSITE:
        return TARGET_BY_WEBSITE[site]

    # 2) exact name alias
    if cleaned.lower() in TARGET_BY_NAME_ALIAS:
        return TARGET_BY_NAME_ALIAS[cleaned.lower()]

    # 3) noise?
    if is_target_noise(cleaned):
        # apply exact alias first in case an alias also matches
        return f"NOISE: {cleaned}"

    # 4) unknown company -> keep raw cleaned name (validator decides)
    return cleaned


def detect_seniority(title: str) -> str:
    if not title:
        return "Unknown"
    t = title.lower()
    # C-suite: match whole words / common prefixes (e.g. "CTO", "Vice President")
    c_level = re.compile(r"\b(chief|ceo|cto|cfo|cmo|coo|cso|cro|cpo|cio|cco|president)\b")
    if c_level.search(t):
        return "C-Level"
    vp_level = re.compile(r"\b(vp|vice president|svp|evp)\b")
    if vp_level.search(t):
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
    src = "sales-nav-raw/export-nick-us-fitness.csv"
    dst = "people-raw.csv"
    if len(sys.argv) >= 3:
        src, dst = sys.argv[1], sys.argv[2]

    with open(src, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

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
            website = (r.get("company website_url", "") or "").strip()
            company = resolve_company(company_raw, website)
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
                "company_name": company,
                "company_linkedin_url": company_linkedin,
                "person_linkedin_url": linkedin_url,
                "email_guess": "",
                "location_country": location,
                "location_city": "",
                "years_in_role": "",
                "profile_summary": summary,
            })

    from collections import Counter
    with open(dst, encoding="utf-8") as f2:
        out_rows = list(csv.DictReader(f2))
    companies = Counter(r["company_name"] for r in out_rows)
    noise = Counter(c for c in companies if c.startswith("NOISE:"))
    targets = Counter(c for c in companies if not c.startswith("NOISE:"))
    print(f"Done. {len(rows)} contacts -> {dst}")
    print(f"Unique target companies: {len(targets)} | Unique noise labels: {len(noise)}")
    print(f"\nTarget rows: {sum(targets.values())} | Noise rows: {sum(noise.values())}")
    print("\nCompanies (rows):")
    for c, n in targets.most_common(40):
        print(f"  {n:4d}  {c}")
    print("\nNoise (rows):")
    for c, n in noise.most_common(20):
        print(f"  {n:4d}  {c}")


if __name__ == "__main__":
    main()