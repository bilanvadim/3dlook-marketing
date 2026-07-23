#!/usr/bin/env python3
"""
ICP validation for Israel telehealth outbound campaign.
Product: FitXpress. Market: Israel. Profile: katya.
"""
import csv, json, re, os

BASE = '/home/vadim_prod/3dlook-marketing/marketing_vb/workspace/outbound/campaigns/2026-07-23-israel-telehealth'

# --- Load exclusion registry ---
with open('/home/vadim_prod/3dlook-marketing/marketing_vb/workspace/outbound/exclusions/katya-registry.json') as f:
    excl = json.load(f)
excluded_urls = set(excl.get('excluded_people_urls', []))
excluded_companies = set(c.lower() for c in excl.get('excluded_companies', []))

# --- Parse tier files ---
tier_data = {}  # company_lower -> {tier, rank, company, focus, rationale}
for fn, tier_num in [('il_tier1.csv', 1), ('il_tier2.csv', 2), ('il_tier3.csv', 3)]:
    path = os.path.join(BASE, fn)
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            company_raw = row.get('Company', row.get('Company ', '')).strip()
            tier_data[company_raw.lower()] = {
                'tier': tier_num,
                'rank': int(row.get('Rank', '0')),
                'company': company_raw,
            }

# --- Company name normalization and tier matching ---
def normalize_company(name):
    """Normalize company name for matching."""
    n = name.strip().lower()
    # Remove common suffixes
    n = re.sub(r'\s*-\s*מאוחדת.*', '', n)
    n = re.sub(r'\s*ltd\.?\s*$', '', n)
    n = re.sub(r'\s*inc\.?\s*$', '', n)
    n = re.sub(r'\s+', ' ', n).strip()
    return n

def find_tier(company_name):
    """Match a company name to a tier entry, returning (tier, rank, matched_name)."""
    if not company_name:
        return (None, None, None)
    
    cn = normalize_company(company_name)
    
    # Direct match
    if cn in tier_data:
        t = tier_data[cn]
        return (t['tier'], t['rank'], t['company'])
    
    # Try partial matches / known aliases
    aliases = {
        'clalit': 'clalit health services',
        'maccabi': 'maccabi healthcare services',
        'meuhedet': 'meuhedet health services',
        'leumit': 'leumit health services',
        'tytocare': 'tytocare',
        'tyto care': 'tytocare',
        'k health': 'k health',
        'sweetch': 'sweetch',
        'dariohealth': 'dariohealth',
        'bettertogether': 'bettertogether',
        'vim': 'vim',
        'laguna health': 'laguna health',
        'datos health': 'datos health',
        'biobeat': 'biobeat',
        'cardiacsense': 'cardiacsense',
        'shl telemedicine': 'shl telemedicine',
        'sheba': 'sheba medical center / arc innovation',
        'ichilov': 'ichilov (tel aviv sourasky medical center)',
        'tel aviv sourasky': 'ichilov (tel aviv sourasky medical center)',
        'harel': 'harel insurance',
        'migdal': 'migdal insurance',
        'phoenix': 'phoenix holdings',
        'holmes place': 'holmes place israel',
        'holmes place israel': 'holmes place israel',
        'holmes place group': 'holmes place israel',
        'mon4t': 'mon4t',
        'air doctor': 'air doctor',
        'taliaz': 'taliaz',
        'wesure': 'wesure / shomera (israeli health insurance brokers/insurers)',
        'shomera': 'wesure / shomera (israeli health insurance brokers/insurers)',
        'maccabi health tech': 'maccabi health tech accelerator / mdclick',
        'mdclick': 'maccabi health tech accelerator / mdclick',
        'clalit innovation': 'clalit innovation (former tech.mate)',
        'assuta': 'wellness/spa medical aesthetic clinics (e.g. assuta private clinics)',
        'idf': 'israel defense forces (idf) medical corps / fitness programs',
        'maccabi optic': 'maccabi healthcare services',
        'maccabi health services': 'maccabi healthcare services',
        'maccabi health care services': 'maccabi healthcare services',
        'clalit health services': 'clalit health services',
        'leumit health services': 'leumit health services',
        'meuhedet health services': 'meuhedet health services',
        'sheba medical center': 'sheba medical center / arc innovation',
        'sheba - tel hashomer hospital': 'sheba medical center / arc innovation',
        'sheba tel hashomer city of health': 'sheba medical center / arc innovation',
        'sheba medical center, tel hashomer': 'sheba medical center / arc innovation',
        'harel insurance & finance': 'harel insurance',
        'shl telemedicine': 'shl telemedicine',
    }
    
    # Check aliases
    for key, target in aliases.items():
        if key in cn:
            if target in tier_data:
                t = tier_data[target]
                return (t['tier'], t['rank'], t['company'])
    
    # Try checking if any tier company name contains the search term
    for tc_lower, td in tier_data.items():
        # Check if the search company is a substring of a tier company
        if len(cn) > 5 and cn in tc_lower:
            return (td['tier'], td['rank'], td['company'])
        # Check if tier company is a substring
        if len(tc_lower) > 5 and tc_lower in cn:
            return (td['tier'], td['rank'], td['company'])
    
    return (None, None, None)


# --- ICP segment determination ---
COMPANY_SEGMENTS = {
    'clalit health services': 'HMO digital health',
    'maccabi healthcare services': 'HMO digital health',
    'leumit health services': 'HMO digital health',
    'meuhedet health services': 'HMO digital health',
    'dariohealth': 'digital therapeutics / GLP-1',
    'sweetch': 'digital therapeutics / GLP-1',
    'k health': 'digital therapeutics / telehealth',
    'bettertogether': 'digital therapeutics / wellness',
    'vim': 'care coordination',
    'tytocare': 'telehealth',
    'laguna health': 'RPM / care management',
    'datos health': 'RPM / remote monitoring',
    'biobeat': 'RPM / wearables',
    'cardiacsense': 'RPM / wearables',
    'shl telemedicine': 'telemedicine / RPM',
    'sheba medical center / arc innovation': 'hospital / innovation hub',
    'ichilov (tel aviv sourasky medical center)': 'hospital',
    'harel insurance': 'insurance / wellness',
    'migdal insurance': 'insurance / wellness',
    'phoenix holdings': 'insurance / wellness',
    'holmes place israel': 'fitness / wellness',
    'fitness chains (go active / wefitness)': 'fitness / wellness',
    'mon4t': 'RPM / remote monitoring',
    'air doctor': 'telehealth (travel)',
    'taliaz': 'mental health telemedicine',
    'wesure / shomera (israeli health insurance brokers/insurers)': 'insurance / underwriting',
    'maccabi health tech accelerator / mdclick': 'health tech accelerator',
    'clalit innovation (former tech.mate)': 'health tech accelerator',
    'wellness/spa medical aesthetic clinics (e.g. assuta private clinics)': 'medical aesthetics / bariatric',
    'israel defense forces (idf) medical corps / fitness programs': 'institutional / military health',
}

def get_segment(company_tier_match):
    """Get ICP segment from tier match name."""
    if company_tier_match:
        mn = company_tier_match.lower()
        if mn in COMPANY_SEGMENTS:
            return COMPANY_SEGMENTS[mn]
        # Try fuzzy
        for key, seg in COMPANY_SEGMENTS.items():
            if key in mn or mn in key:
                return seg
    return 'unknown'

# --- Keywords for ICP relevance ---
ICP_RELEVANT_KEYWORDS = [
    'digital health', 'digital transformation', 'innovation', 'telemedicine', 'telehealth',
    'medical director', 'chief medical', 'clinical director', 'head of clinical',
    'health promotion', 'health education', 'wellness', 'weight', 'obesity', 'metabolic',
    'chronic', 'diabetes', 'endocrin', 'bariatric', 'nutrition',
    'product', 'technology', 'data', 'ai ', 'artificial intelligence',
    'research and innovation', 'research & innovation',
    'information system', 'digital product', 'digital r&d',
    'member engagement', 'patient', 'care management', 'care coordination',
    'remote', 'rpm', 'monitoring', 'virtual care',
    'business development', 'strategy', 'partnership',
    'marketing', 'growth', 'customer', 'experience',
]

ICP_STRONG_KEYWORDS = [
    'ceo', 'chief executive', 'founder', 'co-founder', 'managing director',
    'chief medical', 'medical director',
    'head of digital health', 'head of innovation', 'chief innovation',
    'deputy director general', 'deputy ceo',
    'chief product', 'head of product',
    'chief operating', 'coo',
    'vp innovation', 'director of innovation',
    'chief transformation',
    'head of clinical operations',
    'chief digital', 'chief data',
    'vp product', 'vp digital',
]

ICP_MODERATE_KEYWORDS = [
    'vp ', 'vice president', 'head of', 'director of',
    'chief information', 'cio', 'chief technology', 'cto',
    'chief marketing', 'cmo',
    'chief business', 'chief strategy',
    'board member', 'board of directors',
    'svp', 'senior vice president',
]

ICP_IRRELEVANT_KEYWORDS = [
    'supply chain', 'logistics', 'facilities', 'maintenance',
    'security', 'ciso', 'cyber', 'soc ',
    'genetics', 'virology', 'pathology', 'radiology',
    'gynecology', 'fertility', 'pediatric', 'women health',
    'mental health', 'psychological', 'psychiatr',
    'addiction', 'substance',
    'dental', 'ophthalmology', 'otolaryngology', 'ent ',
    'pharmacy', 'pharmacist', 'pharmac',
    'nursing', 'nurse',
    'finance', 'financial', 'accounting', 'budget',
    'legal', 'compliance', 'regulation', 'regulatory',
    'hr', 'human resource', 'payroll',
    'property', 'building', 'construction',
    'receptionist', 'sales representative', 'salesperson', 'trainer',
    'instructor', 'hairdresser', 'bookkeeper',
    'teacher', 'student', 'practicum',
    'software developer', 'software engineer',
    'interior design',
    'shift manager', 'branch manager', 'clinic manager',
    'quality assurance', 'qa director',
    'demand gen', 'demand generation',
    'loyalty program',
    'safety', 'security', 'soc',
    'electrical', 'control system',
    'cardiac rehabilitation',  # too narrow, not digital health decision maker
]

def is_title_relevant(title):
    """Check if job title is relevant to FitXpress ICP."""
    t = (title or '').lower()
    
    # First check irrelevance
    for kw in ICP_IRRELEVANT_KEYWORDS:
        if kw in t:
            return False
    
    # Check relevance
    for kw in ICP_RELEVANT_KEYWORDS:
        if kw in t:
            return True
    
    return False

def classify_buyer_role(title, company):
    """Classify buyer role based on job title."""
    t = (title or '').lower()
    c = (company or '').lower()
    
    # Quick exclusion for clearly irrelevant
    if any(kw in t for kw in ['receptionist', 'salesperson', 'sales representative', 'trainer', 
                                'instructor', 'hairdresser', 'bookkeeper', 'payroll', 'accounting clerk',
                                'teacher', 'practicum student', 'software developer', 'software engineer',
                                'interior design', 'shift manager']):
        return 'Not relevant'
    
    # C-level
    c_level = any(kw in t for kw in ['ceo', 'chief executive', 'founder', 'co-founder', 'managing director', 'general manager'])
    vp_level = any(kw in t for kw in ['vp ', 'vice president', 'deputy ceo', 'deputy director general', 'executive vice president', 'evp'])
    
    # More precise c_suite matching to avoid false positives (e.g. 'cio' matching 'ocio')
    c_suite_tokens = set(t.replace(',', ' ').replace('/', ' ').split())
    c_suite_match = any(kw in c_suite_tokens for kw in [
        'cfo', 'coo', 'cto', 'cio', 'cmo', 'cro', 'cpo', 'ciso', 'cdo', 'caio'
    ])
    
    # Chief Officer patterns only (not chief pharmacist, chief nurse, etc.)
    chief_officer_patterns = [
        'chief executive', 'chief financial', 'chief operating', 'chief technology',
        'chief information', 'chief marketing', 'chief product', 'chief revenue',
        'chief data', 'chief ai', 'chief innovation', 'chief digital',
        'chief medical', 'chief business', 'chief strategy', 'chief customer',
        'chief legal', 'chief transformation', 'chief commercial',
    ]
    # Also accept standalone 'chief officer' or 'chief ... officer'
    has_chief_officer = any(p in t for p in chief_officer_patterns)
    c_suite_match = c_suite_match or has_chief_officer
    
    if c_level:
        return 'Decision maker'
    if c_suite_match:
        return 'Decision maker'
    
    # Director-level with ICP relevance
    if any(kw in t for kw in ['director', 'head of']) and is_title_relevant(title):
        if vp_level:
            return 'Decision maker'
        return 'Champion'
    
    # VP-level without strong relevance
    if vp_level:
        return 'Champion'
    
    # Board members
    if 'board member' in t.lower() or 'board of directors' in t.lower():
        return 'Champion'
    
    # Manager/lead with relevance
    if is_title_relevant(title):
        if any(kw in t for kw in ['manager', 'lead', 'senior']):
            return 'Influencer'
    
    # Director/head without ICP relevance
    if any(kw in t for kw in ['director', 'head of']):
        return 'Influencer'
    
    if any(kw in t for kw in ['manager', 'lead', 'senior']):
        return 'Influencer'
    
    return 'Not relevant'


# --- ICP fit assessment ---
def assess_icp_fit(title, company, tier, segment, buyer_role):
    """Assess ICP fit: strong / moderate / weak / none."""
    t = (title or '').lower()
    c = (company or '').lower()
    
    # EXCLUSIONS - clearly not relevant roles
    if buyer_role == 'Not relevant':
        return 'none'
    
    strong_company_segments = ['HMO digital health', 'digital therapeutics / GLP-1', 
                                'digital therapeutics / telehealth', 'telehealth',
                                'RPM / care management', 'RPM / remote monitoring',
                                'hospital / innovation hub']
    
    moderate_company_segments = ['RPM / wearables', 'telemedicine / RPM', 
                                  'hospital', 'insurance / wellness',
                                  'care coordination', 'digital therapeutics / wellness',
                                  'health tech accelerator', 'medical aesthetics / bariatric']
    
    weak_company_segments = ['fitness / wellness', 'insurance / underwriting',
                              'mental health telemedicine', 'telehealth (travel)',
                              'institutional / military health']
    
    is_strong_company = segment in strong_company_segments
    is_moderate_company = segment in moderate_company_segments
    is_weak_company = segment in weak_company_segments
    
    # Check if title specifically targets a FitXpress-relevant function
    title_is_strong = is_title_relevant(title) and any(kw in t for kw in [
        'digital health', 'innovation', 'telemedicine', 'telehealth',
        'medical director', 'chief medical', 'clinical director',
        'product', 'technology', 'strategy',
        'health promotion', 'wellness', 'chronic', 'obesity', 'weight',
        'transformation', 'business development',
    ])
    
    # === STRONG FIT ===
    # Decision maker at strong company + title relevant to ICP
    if buyer_role == 'Decision maker' and is_strong_company:
        return 'strong'
    
    # Champion at strong company with strong title keywords
    if buyer_role == 'Champion' and is_strong_company and title_is_strong:
        return 'strong'
    
    # Decision maker at moderate company with strong title alignment
    if buyer_role == 'Decision maker' and is_moderate_company:
        if any(kw in t for kw in ['innovation', 'digital', 'transformation', 'medical', 
                                    'health', 'wellness', 'product', 'strategy', 'ceo', 'founder']):
            return 'strong'
        return 'moderate'
    
    # === MODERATE FIT ===
    # Champion at strong company without strong title keywords
    if buyer_role == 'Champion' and is_strong_company:
        return 'moderate'
    
    # Influencer with relevant title at strong company
    if buyer_role == 'Influencer' and is_strong_company and title_is_strong:
        return 'moderate'
    
    # Champion at moderate company
    if buyer_role == 'Champion' and is_moderate_company:
        return 'moderate'
    
    # Decision maker at weak company with relevant title
    if buyer_role == 'Decision maker' and is_weak_company:
        if any(kw in t for kw in ['ceo', 'founder', 'chief', 'vp', 'director', 'innovation', 
                                    'digital', 'strategy', 'product', 'head of']):
            return 'moderate'
        return 'weak'
    
    # Influencer at strong company
    if buyer_role == 'Influencer' and is_strong_company:
        return 'moderate'
    
    # === WEAK FIT ===
    # Influencer at moderate company
    if buyer_role == 'Influencer' and is_moderate_company:
        return 'weak'
    
    # Champion at weak company with relevant title
    if buyer_role == 'Champion' and is_weak_company:
        if title_is_strong:
            return 'weak'
    
    # Decision maker at weak segments
    if buyer_role == 'Decision maker' and is_weak_company:
        return 'weak'
    
    # Anyone at fitness chains below VP
    if segment == 'fitness / wellness':
        return 'none'
    
    # === NONE ===
    return 'none'


# --- Parse sheet1 (tier 1 contacts) ---
all_contacts = []

sheet1_path = os.path.join(BASE, 'il_sheet1.csv')
with open(sheet1_path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        first = (row.get('prenom', '') or '').strip().replace('🎗️', '')
        last = (row.get('nom', '') or '').strip().replace('🎗️', '')
        # Handle "Dr." prefix in first name
        if first.lower() in ['dr', 'dr.', 'prof', 'prof.']:
            first = ''
        # Clean last name (some have commas, extra chars)
        last = last.replace('"', '').strip(',').strip()
        title = (row.get('Job Title', '') or '').strip()
        company = (row.get('Company', '') or '').strip()
        company_url = (row.get('Company URL', '') or '').strip()
        location = (row.get('Location', '') or '').strip()
        linkedin = (row.get('url_linkedin', '') or '').strip()
        
        tier, rank, matched = find_tier(company)
        segment = get_segment(matched)
        buyer_role = classify_buyer_role(title, company)
        icp_fit = assess_icp_fit(title, company, tier, segment, buyer_role)
        
        # Build reason
        reason_parts = []
        if matched:
            reason_parts.append(f'Tier {tier} company: {matched}')
        else:
            reason_parts.append(f'Company: {company}')
        reason_parts.append(f'Segment: {segment}')
        reason_parts.append(f'Role: {buyer_role}')
        
        all_contacts.append({
            'first_name': first,
            'last_name': last,
            'job_title': title,
            'company': company,
            'company_url': company_url,
            'location': location,
            'linkedin_url': linkedin,
            'tier': tier,
            'icp_fit': icp_fit,
            'icp_segment': segment,
            'buyer_role': buyer_role,
            'reason': ' | '.join(reason_parts),
            'sheet': 'sheet1',
        })

# --- Parse sheet2 (tier 2 contacts) ---
sheet2_path = os.path.join(BASE, 'il_sheet2.csv')
with open(sheet2_path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        name_raw = (row.get('Name', '') or '').strip()
        title = (row.get('Current Title', '') or '').strip()
        company = (row.get('Company', '') or '').strip()
        company_url = (row.get('Company URL', '') or '').strip()
        
        # Parse name: "First Last, Suffix" or "First Last"
        first = ''
        last = ''
        name_clean = re.sub(r',\s*(MD|PhD|phd|md)\s*$', '', name_raw, flags=re.IGNORECASE)
        name_clean = name_clean.replace('"', '').strip()
        parts = name_clean.split(None, 1)  # Split on whitespace, max 1 split
        if parts:
            first = parts[0]
        if len(parts) > 1:
            last = parts[1]
        
        location = ''  # Sheet2 doesn't have location
        linkedin = ''  # Sheet2 doesn't have linkedin URLs directly
        
        tier, rank, matched = find_tier(company)
        segment = get_segment(matched)
        buyer_role = classify_buyer_role(title, company)
        icp_fit = assess_icp_fit(title, company, tier, segment, buyer_role)
        
        reason_parts = []
        if matched:
            reason_parts.append(f'Tier {tier} company: {matched}')
        else:
            reason_parts.append(f'Company: {company}')
        reason_parts.append(f'Segment: {segment}')
        reason_parts.append(f'Role: {buyer_role}')
        
        all_contacts.append({
            'first_name': first,
            'last_name': last,
            'job_title': title,
            'company': company,
            'company_url': company_url,
            'location': location,
            'linkedin_url': linkedin,
            'tier': tier,
            'icp_fit': icp_fit,
            'icp_segment': segment,
            'buyer_role': buyer_role,
            'reason': ' | '.join(reason_parts),
            'sheet': 'sheet2',
        })

# --- Parse sheet3 (tier 3 contacts) ---
sheet3_path = os.path.join(BASE, 'il_sheet3.csv')
with open(sheet3_path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        name_raw = (row.get('Name', '') or '').strip()
        title = (row.get('Role', '') or '').strip()
        company = (row.get('Company', '') or '').strip()
        location = (row.get('Location', '') or '').strip()
        
        first = ''
        last = ''
        parts = name_raw.split(None, 1)
        if parts:
            first = parts[0]
        if len(parts) > 1:
            last = parts[1]
        
        company_url = ''
        linkedin = ''
        
        tier, rank, matched = find_tier(company)
        if not matched:
            # Try to detect Holmes Place variations
            if 'holmes' in company.lower() or 'icon fitness' in company.lower():
                tier, rank, matched = find_tier('Holmes Place Israel')
        
        segment = get_segment(matched)
        buyer_role = classify_buyer_role(title, company)
        icp_fit = assess_icp_fit(title, company, tier, segment, buyer_role)
        
        reason_parts = []
        if matched:
            reason_parts.append(f'Tier {tier} company: {matched}')
        else:
            reason_parts.append(f'Company: {company}')
        reason_parts.append(f'Segment: {segment}')
        reason_parts.append(f'Role: {buyer_role}')
        
        all_contacts.append({
            'first_name': first,
            'last_name': last,
            'job_title': title,
            'company': company,
            'company_url': company_url,
            'location': location,
            'linkedin_url': linkedin,
            'tier': tier,
            'icp_fit': icp_fit,
            'icp_segment': segment,
            'buyer_role': buyer_role,
            'reason': ' | '.join(reason_parts),
            'sheet': 'sheet3',
        })

# --- Write people-validated.csv ---
output_csv = os.path.join(BASE, 'people-validated.csv')
csv_fields = [
    'first_name', 'last_name', 'job_title', 'company', 'company_url',
    'location', 'linkedin_url', 'tier', 'icp_fit', 'icp_segment',
    'buyer_role', 'reason'
]
with open(output_csv, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=csv_fields)
    writer.writeheader()
    for c in all_contacts:
        writer.writerow({k: c.get(k, '') for k in csv_fields})

print(f'Wrote {len(all_contacts)} contacts to {output_csv}')

# --- Statistics ---
from collections import Counter, defaultdict

total = len(all_contacts)
fit_counts = Counter(c['icp_fit'] for c in all_contacts)
tier_counts = Counter((c.get('tier') or 'unknown') for c in all_contacts)
sheet_counts = Counter(c['sheet'] for c in all_contacts)

print(f'\n=== SUMMARY ===')
print(f'Total contacts: {total}')
print(f'By sheet: {dict(sheet_counts)}')
print(f'By tier: {dict(tier_counts)}')
print(f'By ICP fit: {dict(fit_counts)}')

# Tier x fit breakdown
tier_fit = defaultdict(Counter)
for c in all_contacts:
    t = c.get('tier') or 'unknown'
    tier_fit[t][c['icp_fit']] += 1

print(f'\n=== TIER x FIT BREAKDOWN ===')
for t in sorted(tier_fit.keys(), key=lambda x: (0 if isinstance(x, int) else 99, x)):
    counts = tier_fit[t]
    print(f'Tier {t}: {dict(counts)}')

# Segment breakdown
seg_counts = Counter(c['icp_segment'] for c in all_contacts)
seg_fit = defaultdict(Counter)
for c in all_contacts:
    seg_fit[c['icp_segment']][c['icp_fit']] += 1

print(f'\n=== SEGMENT BREAKDOWN ===')
for seg in sorted(seg_counts.keys()):
    print(f'{seg}: {seg_counts[seg]} total, fit: {dict(seg_fit[seg])}')

# Top strong fit contacts
strong_contacts = [c for c in all_contacts if c['icp_fit'] == 'strong']
print(f'\n=== TOP STRONG FIT ({len(strong_contacts)}) ===')
for i, c in enumerate(strong_contacts[:30]):
    print(f'{i+1}. {c["first_name"]} {c["last_name"]} — {c["job_title"]} at {c["company"]} [{c["icp_segment"]}] [{c["buyer_role"]}]')

moderate_contacts = [c for c in all_contacts if c['icp_fit'] == 'moderate']
print(f'\n=== MODERATE FIT ({len(moderate_contacts)}) ===')
for i, c in enumerate(moderate_contacts[:30]):
    print(f'{i+1}. {c["first_name"]} {c["last_name"]} — {c["job_title"]} at {c["company"]} [{c["icp_segment"]}] [{c["buyer_role"]}]')

# Companies with no tier match
no_tier = [c for c in all_contacts if c.get('tier') is None]
print(f'\n=== UNMATCHED COMPANIES ({len(no_tier)}) ===')
unmatched_companies = Counter(c['company'] for c in no_tier)
for comp, cnt in unmatched_companies.most_common(20):
    print(f'  {comp}: {cnt} contacts')
