#!/usr/bin/env python3
"""Generate Message 1 + Message 2 for batches b06, b07, b08."""

import csv
import os

# Template constants
KATYA_CALENDAR = "https://meetings.hubspot.com/kateryna-boichuk"

# Hook starters - vary across contacts
HOOKS = [
    "Circling back after connecting",
    "Quick thought after our connection",
    "Noticed your background in",
    "Saw your work at",
    "Got me thinking about",
    "Curious about your take on",
    "Spotted something relevant to",
    "Quick note on something I think",
    "Thought I'd share given your role at",
    "Had a thought relevant to",
    "Quick idea for",
    "Caught my eye that",
    "Wanted to reach out about",
    "This stood out given your focus on",
    "Made me think about what",
    "Quick reaction to what",
]

# Product intro (stable, adapted)
PRODUCT_INTRO_FX = (
    "At 3DLOOK we built FitXpress: a mobile body scanning layer that lets members "
    "capture consistent measurements via smartphone (key circumferences, body comp) "
    "in under 45 seconds, with 96-97% accuracy, HIPAA/GDPR compliant."
)

PRODUCT_INTRO_FX_SHORT = (
    "We built FitXpress: mobile body scanning from two phone photos. 80+ measurements, "
    "body composition, 3D progress tracking, HIPAA/GDPR compliant."
)

PRODUCT_INTRO_TELEHEALTH = (
    "At 3DLOOK we built FitXpress: a mobile scanning layer that captures body metrics "
    "and 3D progress visuals from a smartphone. Members see real change, teams get "
    "structured data for clinical workflows."
)

SOFT_CTAS = [
    "Might be worth a quick chat?",
    "Worth a quick chat to explore?",
    "Open to a quick chat?",
    "Worth a quick chat?",
]

# Use cases by segment
SEGMENT_HOOKS = {
    "HMO digital health": {
        "observation": [
            "how digital health teams at Israeli HMOs are layering remote monitoring into patient journeys",
            "how HMOs in Israel are scaling telehealth while maintaining clinical data quality",
            "the shift toward remote patient verification at leading health organizations",
            "how digital health leaders are thinking about body measurement consistency across virtual visits",
            "the growing need for structured anthropometric data in HMO member apps",
        ],
        "m2_value": [
            "HMOs we work with use FitXpress to give members objective progress data between clinic visits, which drives engagement and reduces no-shows. Members scan at home, metrics flow into the patient record.",
            "Where FitXpress helps HMOs: members track body change between appointments, clinicians get reliable metrics without in-person measurements, and the data integrates into existing digital health workflows.",
            "For digital health teams at HMOs, FitXpress adds a verified body data layer to telehealth: members scan from home, clinicians see structured metrics and 3D progress, all HIPAA/GDPR compliant.",
        ],
    },
    "telehealth": {
        "observation": [
            "how telehealth platforms are solving the body measurement gap in virtual care",
            "how remote patient monitoring companies are thinking about objective progress tracking",
            "the challenge of getting reliable body metrics without in-person visits",
            "what telehealth leaders see as the next layer: verified body data for better clinical decisions",
        ],
        "m2_value": [
            "For telehealth platforms, FitXpress closes the measurement gap: patients scan from home, clinicians get 80+ metrics and 3D progress in under 45 seconds. UK Meds uses it for BMI verification, Yazen for 34K+ weight loss scans.",
            "Telehealth teams tell us the missing piece is objective body data between visits. FitXpress provides that: smartphone scans, structured metrics, audit-ready records that integrate into existing platforms.",
        ],
    },
    "hospital / innovation hub": {
        "observation": [
            "how innovation hubs like yours are thinking about remote patient data collection for clinical programs",
            "the role of AI-driven body metrics in hospital innovation pipelines",
            "how digital health innovation centers are evaluating mobile scanning for remote care pathways",
        ],
        "m2_value": [
            "Innovation teams we work with see FitXpress as a data layer for remote care: patients scan at home, metrics populate research and clinical workflows. 96-97% accuracy in real-world benchmarks, HIPAA/GDPR compliant.",
            "Where FitXpress fits innovation programs: adding standardized body metrics to remote monitoring protocols. Two photos, 45 seconds, structured data that drops into clinical records.",
        ],
    },
    "RPM / wearables": {
        "observation": [
            "how RPM companies are combining wearable data with objective body composition tracking",
            "the opportunity to add verified body metrics to remote monitoring platforms",
        ],
        "m2_value": [
            "RPM platforms we partner with layer FitXpress body scanning alongside their existing monitoring to give patients and clinicians a complete picture: vitals plus verified body change data.",
            "FitXpress complements RPM workflows with structured body metrics. Two photos from a smartphone, 80+ measurements, integrated via API into existing dashboards.",
        ],
    },
    "RPM / remote monitoring": {
        "observation": [
            "how remote monitoring platforms are thinking about adding body measurement data to their dashboards",
            "the gap between wearable data and objective body composition in RPM",
        ],
        "m2_value": [
            "Remote monitoring platforms that add FitXpress give clinicians objective body metrics alongside vitals. Patients scan from home in 45 seconds, data flows into the existing dashboard.",
            "For RPM platforms, FitXpress adds the body composition layer: verified metrics from a smartphone that complement existing monitoring data.",
        ],
    },
    "insurance / wellness": {
        "observation": [
            "how insurers are approaching remote body verification for wellness programs and underwriting",
            "the growing need for fraud-resistant body metrics in insurance workflows",
        ],
        "m2_value": [
            "Insurers use FitXpress for remote body verification: members scan from home, structured metrics flow into underwriting or wellness tracking workflows. 96-97% accuracy, HIPAA/GDPR compliant, AI fraud detection built in.",
            "For insurance wellness programs, FitXpress provides verified body data that reduces disputes and improves program reporting. Members scan from a smartphone, metrics are audit-ready.",
        ],
    },
    "fitness / wellness": {
        "observation": [
            "how fitness brands are giving members objective progress data beyond the scale",
            "the shift toward verified body metrics in premium wellness experiences",
        ],
        "m2_value": [
            "Fitness brands use FitXpress to give members 3D progress tracking from a smartphone. Members see real body change, which drives retention and premium upgrades.",
            "For fitness and wellness, FitXpress adds the progress layer members want: body metrics and 3D visuals from two phone photos. Works as a white-label integration.",
        ],
    },
    "telemedicine / RPM": {
        "observation": [
            "how telemedicine companies are solving the body measurement gap in virtual consults",
            "the challenge of getting objective body metrics into telemedicine workflows",
        ],
        "m2_value": [
            "Telemedicine platforms use FitXpress to add verified body metrics to virtual consults: patients scan at home, clinicians get 80+ measurements in 45 seconds, all HIPAA/GDPR compliant.",
            "For telemedicine, FitXpress bridges the measurement gap: structured body data from a smartphone that integrates into clinical workflows.",
        ],
    },
}

# Role-specific personalization
def get_role_context(row):
    """Get role-specific context for personalization."""
    title = row.get("job_title", "").lower()
    company = row.get("company", "")
    segment = row.get("icp_segment", "")
    role = row.get("buyer_role", "")
    
    # Decision makers
    if "ceo" in title or "chief executive" in title:
        return "leading digital health strategy", "Members stay engaged when they can see real body change"
    if "cfo" in title or "chief financial" in title:
        return "driving operational efficiency and ROI in healthcare delivery", "Remote body verification cuts the cost of in-person measurements"
    if "cio" in title or "chief information" in title:
        return "shaping the tech stack for digital health at scale", "A lightweight scanning layer that integrates into existing patient platforms"
    if "chief transformation" in title or "chief innovation" in title:
        return "driving digital transformation in healthcare", "Mobile body scanning as a data layer for remote care innovation"
    if "chief medical" in title or "medical director" in title or "assistant medical director" in title:
        return "overseeing clinical quality across telehealth programs", "Clinicians get objective body metrics without scheduling in-person measurements"
    if "chief operating" in title or "coo" in title:
        return "scaling clinical operations with technology", "Faster member onboarding with remote body verification"
    
    # Head of / Director / VP
    if "head of digital" in title or "head of digital health" in title:
        return "shaping digital health product strategy", "Mobile body scanning as a new data layer for digital health platforms"
    if "head of" in title and ("medical" in title or "technology" in title or "technologies" in title):
        return "evaluating medical technologies for clinical adoption", "Verified body metrics from a smartphone that integrate into clinical workflows"
    if "head of" in title and ("product" in title or "digital product" in title):
        return "building digital health products that members actually use", "Members get objective progress data between visits, which drives engagement"
    if "director of" in title and "product" in title:
        return "building products that bridge hardware and telehealth", "Adding verified body metrics to the telehealth product experience"
    if "vp" in title and "marketing" in title:
        return "driving growth through differentiated member experiences", "3D progress tracking as a retention and engagement tool"
    if "vp" in title and ("product" in title or "r&d" in title):
        return "building product roadmaps for digital health", "Mobile body scanning as a feature layer for health platforms"
    if "vp" in title and "business development" in title:
        return "exploring partnerships that expand telehealth capabilities", "Body scanning as a partner integration that adds measurable value"
    if "vp" in title and "corporate development" in title:
        return "evaluating strategic additions to the digital health portfolio", "Verified body data as a workflow layer for insurance innovation"
    
    # Regional Directors
    if "regional director" in title or "regional medical director" in title:
        return "managing clinical operations across district facilities", "Standardized body metrics from a smartphone, consistent across every location"
    
    # Board members
    if "board" in title:
        return "shaping strategic direction for healthcare innovation", "Mobile body scanning as a scalable layer for member engagement"
    
    # Engineering / R&D
    if "engineering" in title or "r&d" in title:
        return "building the technical foundation for telehealth products", "An API-first body scanning SDK that integrates into existing platforms"
    if "cto" in title:
        return "driving the technical vision for AI in healthcare", "Mobile body scanning as an AI-driven data layer for remote care"
    
    # Managers
    if "manager" in title or "director" in title:
        if "clinic" in title or "branch" in title:
            return "running day-to-day clinical operations", "Members scan at home, metrics are ready before they walk in"
        if "telemedicine" in title or "telehealth" in title:
            return "running telehealth operations at scale", "Verified body metrics from a smartphone that complement virtual visits"
        if "pharmacy" in title:
            return "managing pharmacy operations and patient care", "Remote BMI verification that speeds approvals and reduces manual checks"
        if "nursing" in title or "nurse" in title:
            return "overseeing nursing and patient care quality", "Patients track body metrics at home, nurses review structured data"
        if "digital" in title or "crm" in title or "marketing" in title:
            return "driving member engagement through digital channels", "3D body progress tracking as a member engagement and retention tool"
        if "product" in title:
            return "building products that solve real clinical problems", "Body scanning that adds objective progress data to health platforms"
        if "logistics" in title or "property" in title:
            return "managing operational infrastructure", "Remote body verification that reduces the need for in-person measurement logistics"
        if "quality" in title:
            return "ensuring clinical quality and data consistency", "Standardized body metrics with 96-97% accuracy in real-world benchmarks"
        if "finance" in title or "budget" in title:
            return "evaluating ROI of digital health investments", "Body verification that reduces operational costs and drives measurable outcomes"
        if "planning" in title:
            return "shaping strategic planning for healthcare services", "Mobile body scanning as a scalable layer for digital health strategy"
        if "insurance" in title:
            return "managing insurance and risk programs", "Remote body verification that strengthens audit trails and reduces disputes"
        if "it" in title or "information" in title:
            return "managing IT infrastructure for healthcare delivery", "A lightweight API integration that adds body scanning to existing systems"
        if "soc" in title or "security" in title:
            return "protecting healthcare data and infrastructure", "HIPAA/GDPR compliant body scanning with built-in security controls"
        if "pediatric" in title or "child" in title:
            return "overseeing pediatric care programs", "Remote body metrics for pediatric growth tracking and care continuity"
        if "health" in title and ("promotion" in title or "education" in title):
            return "driving health education and member wellness", "Body metrics that members can track at home, supporting health literacy and engagement"
        if "addiction" in title or "mental health" in title:
            return "leading mental health and addiction treatment programs", "Objective body metrics that support whole-person care and treatment monitoring"
        if "pharmacy" in title or "clinical pharmacy" in title:
            return "leading clinical pharmacy services", "BMI verification from a smartphone that speeds prescription workflows"
        if "women" in title:
            return "overseeing women's health services", "Mobile body metrics for women's health programs and longitudinal tracking"
        if "otolaryngology" in title or "ent" in title:
            return "leading head and neck specialty care", "Remote body metrics that support comprehensive patient assessment"
        if "cardiac" in title or "heart" in title:
            return "directing cardiac rehabilitation programs", "Body metrics and 3D progress tracking for cardiac rehab patients at home"
        if "innovation" in title:
            return "driving innovation partnerships in healthcare", "Body scanning as a building block for digital health innovation programs"
        if "cmc" in title:
            return "leading pharmaceutical development programs", "Standardized body metrics for clinical research and development programs"
        if "global" in title:
            return "leading global medical initiatives", "Mobile body scanning as a standardized layer for international health programs"
        if "commercial" in title:
            return "leading commercial strategy for health technology", "Body scanning as a differentiator in competitive health tech markets"
        if "trauma" in title:
            return "directing trauma care operations", "Remote body metrics that support trauma follow-up and recovery tracking"
        if "spa" in title or "wellness" in title:
            return "leading premium wellness experiences", "3D body progress tracking as a premium member experience differentiator"
        if "ophthalmology" in title:
            return "directing ophthalmology clinic operations", "Remote body metrics that support comprehensive patient care workflows"
    
    # Fallback
    return "working at the intersection of healthcare and technology", "Mobile body scanning that adds verified body data to clinical workflows"


def count_chars(text):
    """Count characters in message text."""
    return len(text)


def generate_m1(first_name, row, hook_idx, segment):
    """Generate Message 1."""
    title = row.get("job_title", "")
    company = row.get("company", "")
    role_context, _ = get_role_context(row)
    
    hook = HOOKS[hook_idx % len(HOOKS)]
    
    seg = SEGMENT_HOOKS.get(segment, SEGMENT_HOOKS["HMO digital health"])
    obs_idx = hook_idx % len(seg["observation"])
    observation = seg["observation"][obs_idx]
    
    cta = SOFT_CTAS[hook_idx % len(SOFT_CTAS)]
    
    # Build message
    msg = f"Hi {first_name},\n\n{hook} {role_context}, I've been thinking about {observation}.\n\n{PRODUCT_INTRO_FX}\n\n{cta}\nKatya"
    
    # If too long, use shorter intro
    if count_chars(msg) > 600:
        msg = f"Hi {first_name},\n\n{hook} {role_context}. {observation}.\n\n{PRODUCT_INTRO_FX_SHORT}\n\n{cta}\nKatya"
    
    # Still too long, trim more
    if count_chars(msg) > 600:
        msg = f"Hi {first_name},\n\n{hook} {role_context}. Curious about {observation}.\n\nWe built FitXpress: mobile body scanning from two phone photos. 80+ measurements, body comp, 3D tracking. HIPAA/GDPR.\n\n{cta}\nKatya"
    
    # Final trim if needed
    while count_chars(msg) > 600:
        # Shorten observation
        msg = f"Hi {first_name},\n\n{hook} {role_context}. We built FitXpress: mobile body scanning from two phone photos, giving members objective body metrics and 3D progress tracking in 45 seconds.\n\n{cta}\nKatya"
        break
    
    return msg


def generate_m2(first_name, row, hook_idx, segment):
    """Generate Message 2."""
    title = row.get("job_title", "")
    company = row.get("company", "")
    _, role_value = get_role_context(row)
    
    seg = SEGMENT_HOOKS.get(segment, SEGMENT_HOOKS["HMO digital health"])
    m2_idx = hook_idx % len(seg["m2_value"])
    value_text = seg["m2_value"][m2_idx]
    
    msg = f"Hi {first_name},\n\nQuick follow-up. {value_text}\n\nWorth 15 min to walk through it? Grab a slot: {KATYA_CALENDAR}\nKatya"
    
    if count_chars(msg) > 550:
        # Try shorter
        msg = f"Hi {first_name},\n\nFollowing up. {value_text}\n\nWorth 15 min? {KATYA_CALENDAR}\nKatya"
    
    if count_chars(msg) > 550:
        # Even shorter
        msg = f"Hi {first_name},\n\n{value_text}\n\nWorth 15 min? {KATYA_CALENDAR}\nKatya"
    
    # Final fallback
    if count_chars(msg) > 550:
        msg = f"Hi {first_name},\n\nQuick one: {value_text[:200]}...\n\nWorth 15 min? {KATYA_CALENDAR}\nKatya"
    
    return msg


def process_batch(batch_name, csv_path, out_dir):
    """Process a single batch CSV."""
    results = []
    
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    for i, row in enumerate(rows):
        first_name = row.get("first_name", "").strip()
        last_name = row.get("last_name", "").strip()
        
        # Skip empty rows
        if not first_name and not last_name:
            continue
        
        full_name = f"{first_name} {last_name}".strip()
        title = row.get("job_title", "").strip()
        company = row.get("company", "").strip()
        segment = row.get("icp_segment", "").strip()
        
        person_id = f"{batch_name}-{i+1}"
        
        m1 = generate_m1(first_name, row, i, segment)
        m2 = generate_m2(first_name, row, i, segment)
        
        # File content
        content = f"# {full_name} — {title} — {company}\n\n## Message 1 (after connection accepted)\n{m1}\n\n## Message 2 (+5 days, no reply to Message 1)\n{m2}\n"
        
        filepath = os.path.join(out_dir, f"{person_id}.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
        results.append({
            "person_id": person_id,
            "name": full_name,
            "company": company,
            "m1_chars": count_chars(m1),
            "m2_chars": count_chars(m2),
        })
    
    return results


def main():
    base = "/home/vadim_prod/3dlook-marketing/marketing_vb/workspace/outbound/campaigns/2026-07-23-israel-telehealth"
    out_dir = os.path.join(base, "messages")
    
    batches = [
        ("b06", os.path.join(base, "batches", "b06.csv")),
        ("b07", os.path.join(base, "batches", "b07.csv")),
        ("b08", os.path.join(base, "batches", "b08.csv")),
    ]
    
    all_results = []
    for batch_name, csv_path in batches:
        results = process_batch(batch_name, csv_path, out_dir)
        all_results.extend(results)
        print(f"\n=== {batch_name}: {len(results)} contacts ===")
    
    # Check for any violations
    violations = []
    for r in all_results:
        if r["m1_chars"] > 600:
            violations.append(f"{r['person_id']} M1: {r['m1_chars']} chars (limit 600)")
        if r["m2_chars"] > 550:
            violations.append(f"{r['person_id']} M2: {r['m2_chars']} chars (limit 550)")
    
    print(f"\n=== TOTAL: {len(all_results)} contacts ===")
    if violations:
        print(f"\n=== VIOLATIONS ({len(violations)}) ===")
        for v in violations:
            print(f"  {v}")
    else:
        print("\n=== ALL MESSAGES WITHIN CHARACTER LIMITS ===")
    
    # Print summary
    print("\n--- Per-contact summary ---")
    for r in all_results:
        print(f"  {r['person_id']}: {r['name']} @ {r['company']} | M1={r['m1_chars']}c M2={r['m2_chars']}c")


if __name__ == "__main__":
    main()
