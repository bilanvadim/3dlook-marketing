#!/usr/bin/env python3
"""Generate Message 1 + Message 2 for batches b06, b07, b08. V2 - fixed grammar and role detection."""

import csv
import os

KATYA_CALENDAR = "https://meetings.hubspot.com/kateryna-boichuk"

# Hook openers - used as: "{hook} - "
HOOK_PHRASES = [
    "Circling back after connecting",
    "Quick thought after connecting",
    "Noticed your background",
    "Saw your work",
    "Got me thinking",
    "Curious about your take",
    "Spotted something",
    "Had a thought",
    "Quick idea for you",
    "Caught my eye",
    "Wanted to reach out",
    "This stood out",
    "Made me think",
    "Quick reaction",
]

# Product intro - short enough to fit
PRODUCT_INTRO = (
    "At 3DLOOK we built FitXpress: mobile body scanning from two phone photos. "
    "Members get 80+ measurements, body composition, and 3D progress tracking in 45 seconds. "
    "96-97% accuracy in real-world benchmarks, HIPAA/GDPR compliant."
)

SOFT_CTAS = [
    "Might be worth a quick chat?",
    "Worth a quick chat to explore?",
    "Open to a quick chat?",
]


def get_observation(title_lower, company, segment, buyer_role, hook_idx):
    """Generate a personalized observation based on role, segment, and company."""
    
    # Determine what kind of role/person this is
    is_decision_maker = buyer_role.lower() in ("decision maker",)
    is_champion = buyer_role.lower() in ("champion",)
    is_influencer = buyer_role.lower() in ("influencer",)
    
    # Segment/keyword matching for company context
    is_hmo = any(kw in company.lower() for kw in ["clalit", "maccabi", "meuhedet", "leumit"])
    is_tytocare = "tytocare" in company.lower()
    is_sheba = "sheba" in company.lower()
    is_datos = "datos" in company.lower()
    is_biobeat = "biobeat" in company.lower()
    is_cardiacsense = "cardiacsense" in company.lower()
    is_shl = "shl telemedicine" in company.lower()
    is_harel = "harel" in company.lower()
    is_holmes = "holmes" in company.lower()
    
    # Build observation based on role keywords
    obs_options = []
    
    # C-suite
    if any(kw in title_lower for kw in ["ceo", "chief executive"]):
        obs_options = [
            f"how digital health leaders at {company} are thinking about remote patient verification",
            f"the role of objective body data in {company}'s member experience strategy",
            f"whether mobile body metrics could strengthen {company}'s digital health offering",
        ]
    elif any(kw in title_lower for kw in ["cfo", "chief financial"]):
        obs_options = [
            f"the ROI case for remote body verification at organizations like {company}",
            f"how digital measurement tools could reduce operational costs at {company}",
            f"whether remote body data could improve efficiency at {company}",
        ]
    elif any(kw in title_lower for kw in ["cio", "chief information"]):
        obs_options = [
            f"how {company} is thinking about layering body scanning into its digital health stack",
            f"the integration potential for mobile body metrics at {company}",
            f"whether verified body data fits into {company}'s tech roadmap",
        ]
    elif any(kw in title_lower for kw in ["chief transformation", "chief innovation"]):
        obs_options = [
            f"where mobile body scanning fits in {company}'s innovation roadmap",
            f"how digital transformation leaders at {company} are approaching remote patient data",
            f"the role of AI-driven body metrics in {company}'s innovation pipeline",
        ]
    elif any(kw in title_lower for kw in ["chief medical", "medical director", "assistant medical director"]):
        obs_options = [
            f"how clinical leaders at {company} are thinking about remote body measurement for patient care",
            f"whether objective body metrics from a smartphone could support {company}'s clinical workflows",
            f"the potential for mobile body scanning in {company}'s telehealth programs",
        ]
    elif any(kw in title_lower for kw in ["chief operating", " coo "]) or title_lower.startswith("coo"):
        obs_options = [
            f"how {company} approaches operational efficiency in remote patient monitoring",
            f"the operational case for adding body scanning to {company}'s care delivery",
            f"whether remote body verification could streamline {company}'s patient workflows",
        ]
    
    # Head of roles
    elif "head of digital health" in title_lower or "head of digital" in title_lower:
        obs_options = [
            f"how digital health product leaders are thinking about body measurement data",
            f"whether mobile body scanning could add a new dimension to digital health platforms",
            f"the potential of verified body metrics for {company}'s digital member experience",
        ]
    elif "head of" in title_lower and any(kw in title_lower for kw in ["medical technology", "medical technologies", "med tech"]):
        obs_options = [
            f"how {company} evaluates new medical technologies for clinical adoption",
            f"the landscape for mobile body measurement tools in {company}'s clinical toolkit",
            f"whether smartphone-based body metrics could fit {company}'s technology portfolio",
        ]
    elif "head of" in title_lower and any(kw in title_lower for kw in ["product", "digital product"]):
        obs_options = [
            f"how product leaders are thinking about adding body data to member-facing apps",
            f"the gap between telehealth consults and objective body measurement",
            f"whether mobile body scanning could strengthen {company}'s product experience",
        ]
    elif "head of" in title_lower and "medical" in title_lower:
        obs_options = [
            f"how clinical technology evaluation works at organizations like {company}",
            f"whether remote body measurement tools could support {company}'s medical teams",
            f"the role of objective body data in clinical decision-making at {company}",
        ]
    elif "head of" in title_lower:
        obs_options = [
            f"how your team at {company} approaches new tools for remote patient engagement",
            f"whether mobile body scanning could add value to {company}'s service delivery",
            f"the potential for verified body data in {company}'s operations",
        ]
    
    # Director roles
    elif "regional director" in title_lower or "regional medical director" in title_lower:
        obs_options = [
            f"how regional teams at {company} handle body measurement consistency across locations",
            f"whether standardized remote body metrics could help your district operations",
            f"the challenge of maintaining measurement quality across {company}'s regional facilities",
        ]
    elif "director of product" in title_lower:
        obs_options = [
            f"how product teams at companies like {company} are thinking about body measurement",
            f"whether a body scanning SDK could fit {company}'s product roadmap",
            f"the product opportunity for adding objective body data to health platforms",
        ]
    elif "director" in title_lower and any(kw in title_lower for kw in ["cardiac", "heart"]):
        obs_options = [
            f"how cardiac rehab programs could benefit from remote body progress tracking",
            f"whether smartphone body metrics could support {company}'s cardiac patients between visits",
            f"the potential for mobile body scanning in rehab and recovery monitoring",
        ]
    elif "director" in title_lower and any(kw in title_lower for kw in ["ophthalmology", "eye"]):
        obs_options = [
            f"how clinic directors are thinking about adding remote body metrics to patient care",
            f"whether smartphone scanning could complement {company}'s outpatient services",
            f"the role of objective body data in comprehensive patient management",
        ]
    elif "director" in title_lower and any(kw in title_lower for kw in ["pediatric", "child"]):
        obs_options = [
            f"how pediatric programs could use remote body metrics for growth tracking",
            f"whether smartphone body scanning could support {company}'s pediatric care",
            f"the potential for mobile body measurement in children's health monitoring",
        ]
    elif "director" in title_lower and any(kw in title_lower for kw in ["innovation", "r&d"]):
        obs_options = [
            f"how innovation teams at {company} are evaluating body measurement technologies",
            f"where mobile body scanning fits in {company}'s R&D pipeline",
            f"the potential of AI-driven body metrics for {company}'s innovation programs",
        ]
    elif "director" in title_lower:
        obs_options = [
            f"how your team at {company} approaches remote patient measurement",
            f"whether objective body data from a phone could support your department's work",
            f"the role of mobile body metrics in {company}'s service delivery",
        ]
    
    # VP roles
    elif "vp" in title_lower and "marketing" in title_lower:
        obs_options = [
            f"how marketing leaders at health companies are thinking about member engagement data",
            f"whether 3D body progress tracking could differentiate {company}'s offering",
            f"the retention potential of giving members visible body change data",
        ]
    elif "vp" in title_lower and any(kw in title_lower for kw in ["product", "r&d"]):
        obs_options = [
            f"how product leaders are solving the body measurement gap in digital health",
            f"whether a body scanning API could fit {company}'s product ecosystem",
            f"the product opportunity for verified body metrics at companies like {company}",
        ]
    elif "vp" in title_lower and "business development" in title_lower:
        obs_options = [
            f"partnership opportunities for body scanning technology in the health space",
            f"whether verified body metrics could add value to {company}'s partner ecosystem",
            f"the business case for adding mobile body data to health platforms",
        ]
    elif "vp" in title_lower and "corporate development" in title_lower:
        obs_options = [
            f"how body verification fits into insurance and wellness innovation strategies",
            f"whether remote body metrics could strengthen {company}'s digital offering",
            f"the strategic case for verified body data in insurance workflows",
        ]
    elif "vp" in title_lower:
        obs_options = [
            f"how {company} is approaching remote body measurement and verification",
            f"whether mobile body scanning could add value to {company}'s platform",
            f"the potential for objective body data in {company}'s growth strategy",
        ]
    
    # Board
    elif "board" in title_lower:
        obs_options = [
            f"how board-level conversations at healthcare organizations are evolving around remote monitoring",
            f"the strategic opportunity for mobile body scanning in {company}'s future",
            f"whether verified body data could strengthen {company}'s market position",
        ]
    
    # Engineering
    elif "engineering" in title_lower:
        obs_options = [
            f"the technical landscape for body scanning integration in health platforms",
            f"how engineering teams are thinking about adding body measurement APIs",
            f"whether an SDK for mobile body scanning could fit your current architecture",
        ]
    
    # CTO specific
    elif any(kw in title_lower for kw in ["cto", "chief technology"]):
        obs_options = [
            f"how CTOs at health companies are approaching body measurement technology",
            f"the technical opportunity for AI-driven body data at organizations like {company}",
            f"whether mobile body scanning fits into {company}'s technology vision",
        ]
    
    # Manager roles with specific keywords
    elif "manager" in title_lower or "director" in title_lower:
        if any(kw in title_lower for kw in ["clinic", "branch"]):
            obs_options = [
                f"how clinic teams at {company} handle body measurement workflows day to day",
                f"whether remote body scanning could reduce in-clinic measurement time at {company}",
                f"the operational case for smartphone body metrics in {company}'s clinics",
            ]
        elif any(kw in title_lower for kw in ["telemedicine", "telehealth"]):
            obs_options = [
                f"how telehealth operations handle the body measurement gap at {company}",
                f"whether remote body metrics could complement {company}'s virtual care workflows",
                f"the challenge of getting objective body data into telehealth consults at {company}",
            ]
        elif "pharmacy" in title_lower or "clinical pharmacy" in title_lower:
            obs_options = [
                f"how pharmacy teams at {company} handle BMI verification workflows",
                f"whether smartphone-based body metrics could speed up prescription processes",
                f"the potential for remote BMI verification in {company}'s pharmacy operations",
            ]
        elif any(kw in title_lower for kw in ["nursing", "nurse"]):
            obs_options = [
                f"how nursing teams at {company} could use remote body metrics for patient monitoring",
                f"whether smartphone body data could support {company}'s nursing workflows",
                f"the role of objective body metrics in {company}'s patient care quality",
            ]
        elif any(kw in title_lower for kw in ["digital", "crm", "marketing"]):
            obs_options = [
                f"how digital engagement tools could include body progress tracking at {company}",
                f"whether 3D body visualization could boost member engagement at {company}",
                f"the potential for body data as a member retention tool at {company}",
            ]
        elif "product" in title_lower:
            obs_options = [
                f"how product teams at {company} approach body measurement features",
                f"whether a body scanning integration could benefit {company}'s users",
                f"the product case for adding objective body data to your platform",
            ]
        elif any(kw in title_lower for kw in ["logistics", "property"]):
            obs_options = [
                f"how {company} manages the logistics of in-person measurements at scale",
                f"whether remote body scanning could reduce operational overhead at {company}",
                f"the efficiency case for smartphone body metrics in {company}'s operations",
            ]
        elif "quality" in title_lower:
            obs_options = [
                f"how quality teams at {company} think about measurement consistency and data integrity",
                f"whether standardized remote body metrics could improve {company}'s quality benchmarks",
                f"the potential of verified body data for {company}'s quality management",
            ]
        elif any(kw in title_lower for kw in ["finance", "budget"]):
            obs_options = [
                f"the financial case for adding remote body measurement to {company}'s toolkit",
                f"whether verified body metrics could deliver measurable ROI at {company}",
                f"cost-benefit of remote body verification vs in-person measurements at {company}",
            ]
        elif "planning" in title_lower:
            obs_options = [
                f"how strategic planning at {company} considers new digital health tools",
                f"whether mobile body scanning fits into {company}'s long-term planning",
                f"the strategic case for verified body data at organizations like {company}",
            ]
        elif "insurance" in title_lower:
            obs_options = [
                f"how remote body verification could support {company}'s insurance workflows",
                f"whether smartphone body metrics could reduce claims disputes at {company}",
                f"the compliance case for verified body data in insurance programs",
            ]
        elif any(kw in title_lower for kw in ["soc", "security"]):
            obs_options = [
                f"how security teams evaluate body scanning tools against HIPAA and GDPR requirements",
                f"whether FitXpress's compliance posture aligns with {company}'s security standards",
                f"the data protection considerations for mobile body measurement at {company}",
            ]
        elif any(kw in title_lower for kw in ["pediatric", "child"]):
            obs_options = [
                f"how pediatric programs could use remote body metrics for growth monitoring",
                f"whether smartphone body scanning could support {company}'s pediatric care",
                f"the potential for mobile body measurement in children's health services",
            ]
        elif "health" in title_lower and any(kw in title_lower for kw in ["promotion", "education"]):
            obs_options = [
                f"how health education programs at {company} could use body data for member engagement",
                f"whether 3D body tracking could support {company}'s health promotion initiatives",
                f"the potential of mobile body metrics for {company}'s wellness education",
            ]
        elif any(kw in title_lower for kw in ["addiction", "mental health"]):
            obs_options = [
                f"how mental health programs could integrate objective body metrics for whole-person care",
                f"whether body scanning could support {company}'s treatment monitoring approaches",
                f"the role of body data in comprehensive behavioral health at {company}",
            ]
        elif any(kw in title_lower for kw in ["women", "womens"]):
            obs_options = [
                f"how women's health programs at {company} could use remote body measurement",
                f"whether body scanning could support {company}'s women's health services",
                f"the potential for mobile body metrics in women's longitudinal care",
            ]
        elif any(kw in title_lower for kw in ["otolaryngology", "ent"]):
            obs_options = [
                f"how specialty care teams at {company} could use remote body measurement",
                f"whether body scanning could complement {company}'s head and neck services",
                f"the role of objective body data in {company}'s specialty care",
            ]
        elif any(kw in title_lower for kw in ["cardiac", "heart"]):
            obs_options = [
                f"how cardiac rehab programs could use remote body progress tracking",
                f"whether smartphone body metrics could support {company}'s cardiac patients",
                f"the potential for mobile body scanning in rehabilitation monitoring",
            ]
        elif "innovation" in title_lower:
            obs_options = [
                f"how innovation teams at {company} are evaluating body measurement technologies",
                f"where mobile body scanning fits in {company}'s innovation initiatives",
                f"the potential of AI-driven body metrics for {company}'s partnerships",
            ]
        elif "cmc" in title_lower:
            obs_options = [
                f"how clinical research teams handle body measurement standardization",
                f"whether remote body metrics could support {company}'s research programs",
                f"the potential for standardized body data in clinical development",
            ]
        elif "global" in title_lower:
            obs_options = [
                f"how global health initiatives could standardize body measurement across borders",
                f"whether mobile body scanning could support {company}'s international programs",
                f"the potential for standardized body metrics in global health",
            ]
        elif "commercial" in title_lower:
            obs_options = [
                f"how commercial leaders are positioning body measurement in competitive markets",
                f"whether verified body data could differentiate {company}'s commercial offering",
                f"the market opportunity for mobile body scanning in health tech",
            ]
        elif "trauma" in title_lower:
            obs_options = [
                f"how trauma centers handle body measurement in patient follow-up",
                f"whether remote body metrics could support {company}'s trauma recovery programs",
                f"the potential for mobile body scanning in post-trauma care",
            ]
        elif any(kw in title_lower for kw in ["spa", "wellness"]):
            obs_options = [
                f"how premium wellness brands are giving members objective progress data",
                f"whether 3D body tracking could differentiate {company}'s member experience",
                f"the potential for mobile body scanning in high-end wellness",
            ]
        elif any(kw in title_lower for kw in ["it ", " it", "information technology", "information resources"]):
            obs_options = [
                f"how IT teams at {company} think about integrating new health data tools",
                f"whether a body scanning API could fit {company}'s existing systems",
                f"the integration potential for mobile body metrics at {company}",
            ]
        else:
            obs_options = [
                f"how your team at {company} approaches remote patient measurement",
                f"whether objective body data from a phone could support your work at {company}",
                f"the potential for mobile body metrics in {company}'s operations",
            ]
    
    # Knowledge / specialist roles
    elif "knowledge manager" in title_lower:
        obs_options = [
            f"how health knowledge teams at {company} approach new digital measurement tools",
            f"whether body scanning data could enrich {company}'s health information resources",
            f"the potential for mobile body metrics in {company}'s knowledge programs",
        ]
    
    # Physician/family doctor
    elif "physician" in title_lower or "family doctor" in title_lower:
        obs_options = [
            f"how physicians at {company} are thinking about remote body measurement for patients",
            f"whether smartphone body metrics could support clinical decision-making at {company}",
            f"the potential for mobile body scanning in primary care at {company}",
        ]
    
    # Investor / board
    elif "investor" in title_lower:
        obs_options = [
            f"investment trends in body measurement and digital health infrastructure",
            f"whether verified body data represents a growth opportunity in health tech",
            f"the market potential for mobile body scanning technology",
        ]
    
    # Default
    else:
        obs_options = [
            f"how organizations like {company} approach remote body measurement",
            f"whether mobile body scanning could add value to {company}'s service offering",
            f"the potential for verified body data in {company}'s workflows",
        ]
    
    return obs_options[hook_idx % len(obs_options)]


def get_m2_value(title_lower, company, segment, buyer_role, hook_idx):
    """Generate Message 2 value statement based on role and segment."""
    
    # Segment-based values
    segment_values = {
        "HMO digital health": [
            f"HMOs we work with use FitXpress to give members objective progress data between clinic visits, which drives engagement and reduces no-shows. Members scan at home, metrics flow into the patient record.",
            f"Where FitXpress helps HMOs: members track body change between appointments, clinicians get reliable metrics without in-person measurements, and the data integrates into existing digital health workflows.",
            f"For digital health teams at HMOs, FitXpress adds a verified body data layer to telehealth. Members scan from home, clinicians see structured metrics and 3D progress, all HIPAA/GDPR compliant.",
        ],
        "telehealth": [
            f"For telehealth platforms, FitXpress closes the measurement gap: patients scan from home, clinicians get 80+ metrics and 3D progress in under 45 seconds. UK Meds uses it for BMI verification, Yazen for 34K+ weight loss scans in 2025.",
            f"Telehealth teams tell us the missing piece is objective body data between visits. FitXpress provides that: smartphone scans, structured metrics, audit-ready records that integrate into existing platforms.",
        ],
        "hospital / innovation hub": [
            f"Innovation teams we work with see FitXpress as a data layer for remote care: patients scan at home, metrics populate research and clinical workflows. 96-97% accuracy in real-world benchmarks, HIPAA/GDPR compliant.",
            f"Where FitXpress fits innovation programs: adding standardized body metrics to remote monitoring protocols. Two photos, 45 seconds, structured data that drops into clinical records.",
        ],
        "RPM / wearables": [
            f"RPM platforms we partner with layer FitXpress body scanning alongside their existing monitoring to give patients and clinicians a complete picture: vitals plus verified body change data.",
            f"FitXpress complements RPM workflows with structured body metrics. Two photos from a smartphone, 80+ measurements, integrated via API into existing dashboards.",
        ],
        "RPM / remote monitoring": [
            f"Remote monitoring platforms that add FitXpress give clinicians objective body metrics alongside vitals. Patients scan from home in 45 seconds, data flows into the existing dashboard.",
            f"For RPM platforms, FitXpress adds the body composition layer: verified metrics from a smartphone that complement existing monitoring data.",
        ],
        "insurance / wellness": [
            f"Insurers use FitXpress for remote body verification: members scan from home, structured metrics flow into underwriting or wellness tracking workflows. 96-97% accuracy, HIPAA/GDPR compliant, AI fraud detection built in.",
            f"For insurance wellness programs, FitXpress provides verified body data that reduces disputes and improves program reporting. Members scan from a smartphone, metrics are audit-ready.",
        ],
        "fitness / wellness": [
            f"Fitness brands use FitXpress to give members 3D progress tracking from a smartphone. Members see real body change, which drives retention and premium upgrades.",
            f"For fitness and wellness, FitXpress adds the progress layer members want: body metrics and 3D visuals from two phone photos. Works as a white-label integration.",
        ],
        "telemedicine / RPM": [
            f"Telemedicine platforms use FitXpress to add verified body metrics to virtual consults: patients scan at home, clinicians get 80+ measurements in 45 seconds, all HIPAA/GDPR compliant.",
            f"For telemedicine, FitXpress bridges the measurement gap: structured body data from a smartphone that integrates into clinical workflows.",
        ],
    }
    
    default_values = [
        f"FitXpress adds verified body metrics to digital health workflows. Members scan from home in 45 seconds, structured data integrates via API. 96-97% accuracy, HIPAA/GDPR compliant.",
        f"Where FitXpress helps: members get objective progress data between visits, teams get structured metrics for clinical decisions. Two photos, 45 seconds, audit-ready records.",
    ]
    
    values = segment_values.get(segment, default_values)
    return values[hook_idx % len(values)]


def count_chars(text):
    return len(text)


def generate_m1(first_name, row, hook_idx):
    """Generate Message 1 following template strictly."""
    title = row.get("job_title", "").strip()
    title_lower = title.lower()
    company = row.get("company", "").strip()
    segment = row.get("icp_segment", "").strip()
    buyer_role = row.get("buyer_role", "").strip()
    
    hook_phrase = HOOK_PHRASES[hook_idx % len(HOOK_PHRASES)]
    observation = get_observation(title_lower, company, segment, buyer_role, hook_idx)
    cta = SOFT_CTAS[hook_idx % len(SOFT_CTAS)]
    
    # Build: Hi X, {hook} - {observation}.
    msg = f"Hi {first_name},\n\n{hook_phrase} - {observation}.\n\n{PRODUCT_INTRO}\n\n{cta}\nKatya"
    
    # Trim if needed
    if count_chars(msg) > 600:
        # Shorter product intro
        short_intro = (
            "We built FitXpress: mobile body scanning from two phone photos. "
            "80+ measurements, body composition, 3D progress tracking in 45 seconds, HIPAA/GDPR compliant."
        )
        msg = f"Hi {first_name},\n\n{hook_phrase} - {observation}.\n\n{short_intro}\n\n{cta}\nKatya"
    
    if count_chars(msg) > 600:
        # Ultra short
        ultra_intro = (
            "We built FitXpress: mobile body scanning from two phone photos, "
            "giving members 80+ measurements and 3D progress tracking in 45 seconds."
        )
        msg = f"Hi {first_name},\n\n{hook_phrase} - {observation}.\n\n{ultra_intro}\n\n{cta}\nKatya"
    
    # Final safety trim
    while count_chars(msg) > 600:
        msg = f"Hi {first_name},\n\n{hook_phrase} - curious about mobile body scanning at {company}.\n\nWe built FitXpress: body metrics from a phone camera, 45 seconds, HIPAA/GDPR.\n\n{cta}\nKatya"
        break
    
    return msg


def generate_m2(first_name, row, hook_idx):
    """Generate Message 2 following template strictly."""
    title = row.get("job_title", "").strip()
    title_lower = title.lower()
    company = row.get("company", "").strip()
    segment = row.get("icp_segment", "").strip()
    buyer_role = row.get("buyer_role", "").strip()
    
    value_text = get_m2_value(title_lower, company, segment, buyer_role, hook_idx)
    
    msg = f"Hi {first_name},\n\nQuick follow-up. {value_text}\n\nWorth 15 min to walk through it? Grab a slot: {KATYA_CALENDAR}\nKatya"
    
    if count_chars(msg) > 550:
        msg = f"Hi {first_name},\n\nFollowing up. {value_text}\n\nWorth 15 min? {KATYA_CALENDAR}\nKatya"
    
    if count_chars(msg) > 550:
        msg = f"Hi {first_name},\n\n{value_text}\n\nWorth 15 min? {KATYA_CALENDAR}\nKatya"
    
    if count_chars(msg) > 550:
        # Truncate value text
        shortened = value_text[:180] + "..."
        msg = f"Hi {first_name},\n\n{shortened}\n\nWorth 15 min? {KATYA_CALENDAR}\nKatya"
    
    return msg


def process_batch(batch_name, csv_path, out_dir):
    """Process a single batch CSV and generate message files."""
    results = []
    
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    
    for i, row in enumerate(rows):
        first_name = row.get("first_name", "").strip()
        last_name = row.get("last_name", "").strip()
        
        # Skip completely empty rows
        if not first_name and not last_name:
            continue
        
        # Use last_name as greeting when first_name is empty
        greeting_name = first_name if first_name else last_name
        
        full_name = f"{first_name} {last_name}".strip()
        title = row.get("job_title", "").strip()
        company = row.get("company", "").strip()
        
        person_id = f"{batch_name}-{i+1}"
        
        m1 = generate_m1(greeting_name, row, i)
        m2 = generate_m2(greeting_name, row, i)
        
        content = (
            f"# {full_name} — {title} — {company}\n\n"
            f"## Message 1 (after connection accepted)\n{m1}\n\n"
            f"## Message 2 (+5 days, no reply to Message 1)\n{m2}\n"
        )
        
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
    
    violations = []
    for r in all_results:
        if r["m1_chars"] > 600:
            violations.append(f"{r['person_id']} M1: {r['m1_chars']}c (limit 600)")
        if r["m2_chars"] > 550:
            violations.append(f"{r['person_id']} M2: {r['m2_chars']}c (limit 550)")
    
    # Also check for banned patterns
    banned_words = ["leverage", "utilize", "harness", "robust", "seamless", "comprehensive",
                    "cutting-edge", "game-changing", "revolutionary", "delve", "tapestry", "realm"]
    
    print(f"\n=== TOTAL: {len(all_results)} contacts ===")
    if violations:
        print(f"\n=== CHARACTER LIMIT VIOLATIONS ({len(violations)}) ===")
        for v in violations:
            print(f"  {v}")
    else:
        print("\n=== ALL MESSAGES WITHIN CHARACTER LIMITS ===")
    
    print("\n--- Per-contact summary ---")
    for r in all_results:
        print(f"  {r['person_id']}: {r['name']} @ {r['company']} | M1={r['m1_chars']}c M2={r['m2_chars']}c")


if __name__ == "__main__":
    main()
