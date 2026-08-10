#!/usr/bin/env python3
"""Generate outbound messages for Australia Telehealth campaign."""

import csv
import re
import os
import json

CSV_PATH = "/home/vadim_prod/.hermes/cache/documents/doc_fcd2e8a3280d_Telehealth_Australia - Sheet1 (1).csv"
CAMPAIGN_DIR = "/home/vadim_prod/3dlook-marketing/marketing_vb/workspace/outbound/campaigns/2026-07-27-australia-telehealth"
MESSAGES_DIR = os.path.join(CAMPAIGN_DIR, "messages")

# --- Segment assignments ---
ENTERPRISE_COMPANIES = {
    "Medibank", "Medibank Private", "Medibank Health Solutions",
    "Bupa Australia", "Bupa",
    "HCF Australia", "HCF", "HCF Eyecare",
}

DIGITAL_HEALTH_COMPANIES = {
    "Mosh", "InstantScripts", "Medmate", "qoctor", "Qoctor",
    "Amplar Health", "Hopstep",
}

# Job titles that are clearly irrelevant (no decision-making authority in digital health/product/ops)
SKIP_TITLE_PATTERNS = [
    r"(?i)^Creative\s*\|?\s*Senior Art Director$",
    r"(?i)Executive Assistant to",
    r"(?i)Personal Assistant",
    r"(?i)Roving Maintenance",
    r"(?i)Maintenance Supervisor",
    r"(?i)^Pharmacist$",
    r"(?i)^Dentist$",
    r"(?i)^Care Manager$",
    r"(?i)^Practice Manager",
    r"(?i)^practice manager",
    r"(?i)^Assistant Manager$",
    r"(?i)^Assistant Store Manager$",
    r"(?i)^Store Manager$",
    r"(?i)^Retail Store Manager$",
    r"(?i)^Retail Centre Manager",
    r"(?i)^Branch Manager$",
    r"(?i)^branch manager$",
    r"(?i)^Team Leader$",
    r"(?i)^Team Manager$",
    r"(?i)^Team manager$",
    r"(?i)^Call Centre Manager$",
    r"(?i)^Territory Manager$",
    r"(?i)^Zone Manager",
    r"(?i)^Regional Manager$",
    r"(?i)^Local Community Leader",
    r"(?i)^Outbound Services Manager$",
    r"(?i)^Clinic Coordinator$",
    r"(?i)^Center Manager$",
    r"(?i)^Cluster Manager$",
    r"(?i)^Quality Partner$",
    r"(?i)^Acting Quality Partner$",
    r"(?i)^Quality Education Manager$",
    r"(?i)^Business Support Manager$",
    r"(?i)^Business Adminstration Manager$",
    r"(?i)^Business Practice Manager$",
    r"(?i)^Test Manager$",
    r"(?i)^End User Services Manager$",
    r"(?i)^Customer Support Manager$",
    r"(?i)^Engagement and Support Coordinator$",
    r"(?i)^Roving Maintenance ",
    r"(?i)^Pharmacist in Charge$",
    r"(?i)^Nursing Manager$",
    r"(?i)^Management Team$",
    r"(?i)^Manager$",  # Just "Manager" with no qualifier = too generic
    r"(?i)^manager$",
    r"(?i)^Business Owner$",
    r"(?i)^Owner$",
    r"(?i)^Head Of School$",
    r"(?i)^Continuous Improvement/Transformation$",
    r"(?i)^UXC Managed Services$",
    r"(?i)^Case Manager$",
    r"(?i)^Initiative Owner$",
    r"(?i)^Group Capital Works Manager$",
    r"(?i)^Capital Works Manager$",
    r"(?i)^Business Projects - Change Management$",
    r"(?i)^(Acting) Practice Manager",
    r"(?i)^CX Division Manager$",
    r"(?i)^Manager Ezipay$",
    r"(?i)^Senior Manager - Customer Engagement Delivery$",  # Too operational
]

# Titles that are always INCLUDED even if they could match a generic pattern
INCLUDE_TITLE_PATTERNS = [
    r"(?i)Chief.*Officer",
    r"(?i)^CEO$",
    r"(?i)^CEO & MD$",
    r"(?i)^Managing Director",
    r"(?i)^Co-Founder",
    r"(?i)^Founder",
    r"(?i)^Director.*(?!Assistant|Personal|Creative\|.*Art)",  # Director, but not assistant/personal
    r"(?i)^Chair$",
    r"(?i)^Non Executive Director",
    r"(?i)^Group.*Lead",
    r"(?i)^Group Medical",
    r"(?i)^Group Executive",
    r"(?i)^General Manager",
    r"(?i)^Head of",
    r"(?i)^VP",
    r"(?i)^Vice President",
    r"(?i)^Medical Director",
    r"(?i)^National Medical Director",
    r"(?i)^Regional Clinical Director",
    r"(?i)^Chief of Staff",
    r"(?i)^Squad Lead",
    r"(?i)^Product.*(Manager|Owner|Director)",
    r"(?i)^Program Director",
    r"(?i)^Transformation Director",
    r"(?i)^Digital Director",
    r"(?i)^Integration Director",
    r"(?i)^Legal Director",
    r"(?i)^National Dental Director",
    r"(?i)^Product Owner",
    r"(?i)^Principal.*(Engineer|Architect)",
    r"(?i)^Enterprise Architect",
    r"(?i)^Data Scientist",
    r"(?i)^Chief Data Scientist",
    r"(?i)^Partner - Digital",
    r"(?i)^New Ventures",
    r"(?i)^AI Product Strategy",
    r"(?i)^Analytics Manager",
    r"(?i)^Data & Analytics Manager",
    r"(?i)^Content & Campaigns",
    r"(?i)^Overseas Partner",
    r"(?i)^Partnership Manager",
    r"(?i)^National Partnership Manager",
    r"(?i)^Head of Provider",
    r"(?i)^Provider Network Manager",
]


def normalize_company(company):
    """Normalize company name to canonical form."""
    c = company.strip()
    # Normalize Medibank variants
    if c in ("Medibank", "Medibank Private", "Medibank Health Solutions"):
        return "Medibank"
    # Normalize Bupa variants
    if c in ("Bupa Australia", "Bupa"):
        return "Bupa Australia"
    # Normalize HCF variants
    if c in ("HCF Australia", "HCF", "HCF Eyecare"):
        return "HCF Australia"
    # Normalize Qoctor
    if c.lower() in ("qoctor",):
        return "Qoctor"
    return c


def get_segment(company):
    """Determine segment from company name."""
    norm = normalize_company(company)
    if norm in ENTERPRISE_COMPANIES:
        return "enterprise"
    if norm in DIGITAL_HEALTH_COMPANIES:
        return "digital-health"
    # Check broader match
    if "Medibank" in norm or "medibank" in norm.lower():
        return "enterprise"
    if "Bupa" in norm or "bupa" in norm.lower():
        return "enterprise"
    if "HCF" in norm or "hcf" in norm.lower():
        return "enterprise"
    return "digital-health"


def should_skip(title):
    """Check if a job title should be excluded."""
    # First check if it's clearly included
    for pat in INCLUDE_TITLE_PATTERNS:
        if re.search(pat, title):
            return False
    # Then check exclusion patterns
    for pat in SKIP_TITLE_PATTERNS:
        if re.search(pat, title):
            return True
    return False


def seniority_score(title):
    """Assign a seniority score for sorting (lower = more senior)."""
    t = title.lower()
    if "ceo" in t or "chief executive" in t or "ceo & md" in t:
        return 1
    if "chief" in t or "chair" in t:
        return 2
    if "non executive director" in t:
        return 3
    if "group lead" in t or "group executive" in t or "group medical director" in t:
        return 4
    if "managing director" in t or "general manager" in t:
        return 5
    if "director" in t and "assistant" not in t and "personal" not in t:
        return 6
    if "head of" in t:
        return 7
    if "vp" in t or "vice president" in t:
        return 8
    if "co-founder" in t or "founder" in t:
        return 9
    if "chief of staff" in t:
        return 10
    if "squad lead" in t:
        return 11
    if "medical director" in t or "national medical director" in t:
        return 12
    if "senior manager" in t:
        return 13
    if "manager" in t:
        return 14
    if "principal" in t:
        return 15
    if "lead" in t:
        return 16
    return 20


def generate_enterprise_message(name, title, company, linkedin):
    """Generate enterprise-segment message."""
    first_name = name.split()[0]

    # Pick personalization angle based on title
    t = title.lower()
    if any(w in t for w in ("medical", "clinical", "health", "wellbeing", "wellness")):
        angle = "your clinical and preventive health programs"
    elif any(w in t for w in ("product", "innovation", "strategy", "digital", "transformation")):
        angle = "your digital health roadmap"
    elif any(w in t for w in ("member", "customer", "experience", "engagement", "retention")):
        angle = "your member engagement and wellness programs"
    elif any(w in t for w in ("data", "analytics", "ai", "technology", "cio", "cto")):
        angle = "your digital health and data initiatives"
    elif any(w in t for w in ("chief", "ceo", "managing director", "growth")):
        angle = "Medibank's digital health strategy" if "medibank" in company.lower() else f"{company}'s digital health strategy"
    else:
        angle = "your telehealth and wellness programs"

    message = (
        f"Hi {first_name}, structured body data from two smartphone photos — "
        f"80+ measurements and body composition in 45 seconds, remote-friendly. "
        f"FitXpress supports telehealth intake, preventive health tracking, and "
        f"member wellness verification with audit-ready records. "
        f"Would this be relevant to {angle}?"
    )

    # Trim to ~300 chars if needed
    if len(message) > 300:
        message = (
            f"Hi {first_name}, two smartphone photos → 80+ body measurements & composition in 45 sec. "
            f"FitXpress enables remote body data for telehealth, wellness verification, and preventive programs. "
            f"Worth exploring for {angle}?"
        )

    return message


def generate_digital_health_message(name, title, company, linkedin):
    """Generate digital-health segment message."""
    first_name = name.split()[0]

    # Pick angle based on title/company
    t = title.lower()
    c = company.lower()
    if "mosh" in c:
        prog = "Mosh's weight-loss programs"
    else:
        prog = f"{company}'s programs"

    if any(w in t for w in ("medical", "clinical")):
        angle = f"remote patient progress tracking for {prog}"
    elif any(w in t for w in ("product", "cto", "technology", "engineering")):
        angle = f"integrating objective body data into {prog}"
    elif any(w in t for w in ("chief", "ceo", "founder", "managing", "growth", "marketing")):
        angle = f"member retention and program outcomes for {prog}"
    elif any(w in t for w in ("customer", "experience", "operations")):
        angle = f"scaling member progress tracking for {prog}"
    else:
        angle = f"remote body measurement for {prog}"

    message = (
        f"Hi {first_name}, 80+ body measurements and body composition from two smartphone photos "
        f"in 45 seconds — no clinic visit needed. FitXpress gives members visual progress tracking "
        f"with 95%+ repeatability across repeat scans, ideal for telehealth weight management. "
        f"Open to seeing how this works for {angle}?"
    )

    if len(message) > 300:
        message = (
            f"Hi {first_name}, 80+ body measurements + composition from two photos, no clinic visit. "
            f"FitXpress delivers visual progress tracking with 95%+ repeatability — built for telehealth "
            f"weight management programs. Open to exploring this for {angle}?"
        )

    return message


def parse_csv(path):
    """Parse the messy CSV file. Handles embedded newlines in quoted fields."""
    contacts = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = (row.get("Name") or "").strip()
            title = (row.get("Job Title") or "").strip()
            company = (row.get("Company") or "").strip()
            linkedin = (row.get("url_linkedin") or "").strip()

            if not name or not company:
                continue

            contacts.append({
                "name": name,
                "title": title,
                "company": company,
                "linkedin": linkedin,
            })

    return contacts


def main():
    contacts = parse_csv(CSV_PATH)
    print(f"Parsed {len(contacts)} total contacts from CSV")

    # Filter: skip clearly irrelevant titles
    valid = []
    skipped = []
    for c in contacts:
        if should_skip(c["title"]):
            skipped.append(c)
        else:
            valid.append(c)

    print(f"Valid contacts: {len(valid)}")
    print(f"Skipped contacts: {len(skipped)}")

    # Classify and group
    enterprise = []
    digital_health = []

    for c in valid:
        segment = get_segment(c["company"])
        c["segment"] = segment
        c["company_norm"] = normalize_company(c["company"])
        if segment == "enterprise":
            enterprise.append(c)
        else:
            digital_health.append(c)

    print(f"Enterprise contacts: {len(enterprise)}")
    print(f"Digital Health contacts: {len(digital_health)}")

    # Combine all, sort by company then seniority
    all_contacts = enterprise + digital_health

    # Sort: by company, then by seniority score
    all_contacts.sort(key=lambda c: (
        c["company_norm"],
        seniority_score(c["title"]),
        c["name"]
    ))

    # Generate message files
    os.makedirs(MESSAGES_DIR, exist_ok=True)

    # Group into batches of ~25 for file naming (matching Israel campaign convention)
    batch_size = 25
    batch_num = 1
    contact_in_batch = 0

    stats = {
        "total": len(valid),
        "skipped": len(skipped),
        "enterprise": len(enterprise),
        "digital_health": len(digital_health),
        "by_company": {},
        "by_segment": {"enterprise": 0, "digital-health": 0},
        "skipped_contacts": [],
    }

    for i, c in enumerate(all_contacts):
        if contact_in_batch >= batch_size:
            batch_num += 1
            contact_in_batch = 0

        contact_in_batch += 1
        filename = f"b{batch_num:02d}-{contact_in_batch}.md"
        filepath = os.path.join(MESSAGES_DIR, filename)

        segment = c["segment"]
        company_norm = c["company_norm"]

        # Generate message
        if segment == "enterprise":
            message = generate_enterprise_message(
                c["name"], c["title"], company_norm, c["linkedin"]
            )
        else:
            message = generate_digital_health_message(
                c["name"], c["title"], company_norm, c["linkedin"]
            )

        # Escape quotes in name/title for YAML
        escaped_name = c["name"].replace('"', "'")
        escaped_title = c["title"].replace('"', "'")

        content = f"""---
to: "{escaped_name}"
title: "{escaped_title}"
company: "{company_norm}"
linkedin: "{c['linkedin']}"
segment: "{segment}"
status: draft
---

{message}
"""

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        # Track stats
        stats["by_company"][company_norm] = stats["by_company"].get(company_norm, 0) + 1
        stats["by_segment"][segment] += 1

    # Generate summary
    summary_lines = [
        "# Australian Telehealth Outbound — Message Generation Summary",
        "",
        f"**Date:** 2026-07-27",
        f"**Campaign:** 2026-07-27-australia-telehealth",
        f"**Profile:** vadim (Vadim Bilan, Australia market)",
        f"**Product:** FitXpress",
        "",
        "## Overall Stats",
        "",
        f"- **Total contacts parsed:** {len(contacts)}",
        f"- **Valid contacts (messages generated):** {len(valid)}",
        f"- **Skipped contacts:** {len(skipped)}",
        f"- **Message files created:** {len(valid)}",
        "",
        "## By Segment",
        "",
        f"- **Enterprise (health insurers):** {stats['by_segment']['enterprise']} contacts",
        f"- **Digital Health (telehealth platforms):** {stats['by_segment']['digital-health']} contacts",
        "",
        "## By Company",
        "",
    ]

    # Sort companies by count
    for comp, count in sorted(stats["by_company"].items(), key=lambda x: -x[1]):
        segment = "enterprise" if comp in ENTERPRISE_COMPANIES else "digital-health"
        summary_lines.append(f"- **{comp}:** {count} contacts ({segment})")

    summary_lines.extend([
        "",
        "## Skipped Contacts",
        "",
    ])

    for c in skipped:
        summary_lines.append(f"- **{c['name']}** — {c['title']} @ {c['company']}")

    summary_lines.extend([
        "",
        "## Message Templates Used",
        "",
        "### Enterprise Template (Medibank, Bupa, HCF)",
        "Personalized by role: clinical → \"clinical and preventive health programs\", "
        "product/innovation → \"digital health roadmap\", "
        "member experience → \"member engagement and wellness programs\", "
        "data/tech → \"digital health and data initiatives\", "
        "executive → \"[Company]'s digital health strategy\".",
        "",
        "### Digital Health Template (Mosh, InstantScripts, Medmate, Qoctor, Amplar Health, Hopstep)",
        "Personalized by role: clinical → \"remote patient progress tracking\", "
        "product/tech → \"integrating objective body data\", "
        "executive/growth → \"member retention and program outcomes\", "
        "operations/customer → \"scaling member progress tracking\".",
        "",
        "## File Naming",
        "",
        "Files named `b{NN}-{M}.md` where NN = batch number (30 contacts per batch), "
        "M = position within batch. Contacts are grouped by company, then sorted by seniority "
        "(Chief → Director → Head → Manager → other).",
    ])

    summary_path = os.path.join(MESSAGES_DIR, "_summary.md")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("\n".join(summary_lines))

    print(f"\nDone! Generated {len(valid)} message files in {MESSAGES_DIR}")
    print(f"Summary written to {summary_path}")
    print(f"\nCompany breakdown:")
    for comp, count in sorted(stats["by_company"].items(), key=lambda x: -x[1]):
        print(f"  {comp}: {count}")


if __name__ == "__main__":
    main()
