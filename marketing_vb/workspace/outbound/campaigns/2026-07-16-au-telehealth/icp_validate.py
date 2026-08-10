#!/usr/bin/env python3
"""ICP Validation Script v3 for 2026-07-16-au-telehealth campaign.
Evaluates 439 contacts against FitXpress ICP (telehealth/health insurance segments).
Fixed: positive indicators checked before negative fail patterns."""

import csv, os, re
from collections import Counter

INPUT_CSV = "/home/vadim_prod/3dlook-marketing/marketing_vb/workspace/outbound/campaigns/2026-07-16-au-telehealth/people-raw.csv"
OUTPUT_CSV = "/home/vadim_prod/3dlook-marketing/marketing_vb/workspace/outbound/campaigns/2026-07-16-au-telehealth/people-validated.csv"
OUTPUT_MD = "/home/vadim_prod/3dlook-marketing/marketing_vb/workspace/outbound/campaigns/2026-07-16-au-telehealth/icp-validation-summary.md"

def normalize_company(name):
    n = name.strip()
    # Case-insensitive matching
    n_lower = n.lower()
    if n_lower in ("medibank private", "medibank health solutions", "amplar health"):
        return "Medibank"
    if n_lower in ("hcf", "hcf eyecare"):
        return "HCF Australia"
    if n_lower == "qoctor":
        return "Qoctor"
    return n

HIGH_FIT_SET = {"Medibank", "Bupa Australia", "HCF Australia", "Mosh", "InstantScripts", "Medmate", "Qoctor"}
INSURER_SET = {"Medibank", "Bupa Australia", "HCF Australia"}
DIGITAL_HEALTH_SET = {"Mosh", "InstantScripts", "Medmate", "Qoctor"}

def is_insurer(raw):
    return normalize_company(raw) in INSURER_SET

def is_digital_health(raw):
    return normalize_company(raw) in DIGITAL_HEALTH_SET

def is_high_fit(raw):
    return normalize_company(raw) in HIGH_FIT_SET

def _angle(t, insurer):
    tl = t.lower()
    if any(x in tl for x in ["virtual health", "telehealth", "virtual care"]):
        return "virtual-care"
    if any(x in tl for x in ["member experience", "customer experience", "voice of customer", "member growth", "customer engagement", "customer insights", "customer channels", "customer value", "customer health", "member"]):
        return "member-engagement"
    if any(x in tl for x in ["medical director", "clinical director", "chief medical", "clinical operations", "clinical governance", "vp clinical", "group medical"]):
        return "clinical-operations"
    if any(x in tl for x in ["wellbeing", "wellness", "preventive", "health and wellbeing", "health insights", "health policy"]):
        return "preventive-health"
    if any(x in tl for x in ["digital", "technology", "transformation", "innovation", "product", "ai"]):
        return "digital-transformation"
    if any(x in tl for x in ["compliance", "risk", "governance", "assurance", "regulatory"]):
        return "compliance"
    if any(x in tl for x in ["weight", "glp", "obesity"]):
        return "weight-management"
    if any(x in tl for x in ["ceo", "chief executive", "founder", "managing director", "group executive", "chairman"]):
        return "digital-transformation" if not insurer else "preventive-health"
    if any(x in tl for x in ["cfo", "chief financial", "finance"]):
        return "compliance"
    if any(x in tl for x in ["cmo", "chief marketing", "marketing", "growth", "strategy"]):
        return "member-engagement"
    if any(x in tl for x in ["coo", "chief operating", "operations"]):
        return "clinical-operations"
    if any(x in tl for x in ["chief data", "data scientist", "chief information", "cio", "chief technology", "cto"]):
        return "digital-transformation"
    if any(x in tl for x in ["health", "care", "patient", "hospital", "primary care"]):
        return "preventive-health" if insurer else "clinical-operations"
    return "preventive-health" if insurer else "weight-management"


def classify(title_raw, company_raw, seniority):
    t = title_raw.lower().strip()
    c = company_raw
    cn = normalize_company(c)
    insurer = is_insurer(c)
    dh = is_digital_health(c)
    
    # 0. Hopstep
    if "hopstep" in cn.lower():
        return ("FAIL", "", f"{title_raw} at {c} — healthcare recruitment platform, not a telehealth provider or health insurer.", "")
    
    # 0. Not high-fit
    if not is_high_fit(c):
        return ("FAIL", "", f"{title_raw} at {c} — company not in target segment (not an Australian health insurer or digital health platform).", "")
    
    # ============================================================
    # POSITIVE INDICATORS FIRST (check before fail patterns)
    # ============================================================
    
    # A. Non-Exec Directors / Chair → WEAK
    if "non executive" in t or "non ex director" in t or t.strip() == "chair":
        return ("WEAK", "", f"{title_raw} at {c} — board role; strategic influence but not operational decision-maker for health program tools.", _angle(t, insurer))
    
    # A2. Creative/Art/Design Directors → FAIL (these are creative leadership, not health execs)
    if any(kw in t for kw in ["creative director", "art director", "creative |", "senior art director"]):
        if dh:
            return ("WEAK", "", f"{title_raw} at {c} — creative role at digital health company; adjacent but not in health product decision chain.", "member-engagement")
        return ("FAIL", "", f"{title_raw} at {c} — creative/art direction role; not in FitXpress buying chain.", "")
    
    # A3. Dental-specific directors → FAIL (explicitly excluded per hypothesis)
    if "dental" in t and ("director" in t or "manager" in t or "head" in t):
        return ("FAIL", "", f"{title_raw} at {c} — dental division role; explicitly excluded per hypothesis anti-cases.", "")
    
    # A5. Security/Cybersecurity roles → FAIL (regardless of seniority)
    if any(kw in t for kw in ["security awareness", "security engineering", "security and networks",
                               "cyber security", "cybersecurity", "cyber defence", "cyber threat",
                               "ciso", "it security", "cloud security",
                               "head of risk - technology, security"]):
        return ("FAIL", "", f"{title_raw} at {c} — security/cybersecurity role; not in FitXpress buying chain.", "")
    
    # A6. Optical/Hearing-specific → WEAK (non-core for FitXpress)
    if any(kw in t for kw in ["optical", "hearing"]) and ("director" in t or "head" in t or "general manager" in t or "chief operating" in t):
        return ("WEAK", "", f"{title_raw} at {c} — optical/hearing division leader; non-core for FitXpress but may have broader health portfolio.", "other")
    
    # B. Clinical/Medical Directors (PASS P1)
    clinical_titles = [
        "medical director", "clinical director", "group medical",
        "chief medical", "medical officer",
        "national medical director", "regional clinical director",
        "western aust medical director",
        "group clinical governance",
    ]
    for kw in clinical_titles:
        if kw in t:
            if seniority in ("C-Level", "Director", "VP", "Individual Contributor"):  # IC can be "Senior Executive, Group Clinical Governance"
                return ("PASS", "1", f"{title_raw} at {c} — clinical/medical leadership role directly relevant to FitXpress telehealth and preventive health programs.", "clinical-operations")
            return ("WEAK", "", f"{title_raw} at {c} — clinical role but {seniority} level; potential internal champion.", "clinical-operations")
    
    # C. Virtual Health / Telehealth leaders (PASS P1)
    if any(kw in t for kw in ["virtual health", "virtual care", "telehealth", "digital health"]):
        return ("PASS", "1", f"{title_raw} at {c} — directly owns telehealth/virtual care strategy; perfect FitXpress target.", "virtual-care")
    
    # D. Health & Wellbeing / Preventive Health leaders (PASS P1)
    wellbeing_kw = [
        "head of health and wellbeing", "head of wellbeing",
        "head of health & safety", "head of health, safety",
        "head of health insights", "health insights",
        "head of healthcare programs", "healthcare programs",
        "head of health policy", "health policy",
        "head of health advisory",
        "head of integrated healthcare",
        "head of homecare", "health prevention",
        "head of connected health",
    ]
    for kw in wellbeing_kw:
        if kw in t:
            return ("PASS", "1", f"{title_raw} at {c} — directly owns health/preventive program design; strong FitXpress fit.", _angle(t, insurer))
    
    # E. Member/Customer Experience leaders (PASS P1 if senior, WEAK otherwise)
    member_kw = [
        "chief of - member experience", "member experience",
        "chief customer officer",
        "chief officer, member growth",
    ]
    for kw in member_kw:
        if kw in t:
            return ("PASS", "1", f"{title_raw} at {c} — member/customer experience leader; FitXpress plugs into member engagement and retention KPIs.", "member-engagement")
    
    cust_kw = [
        "head of customer insights", "customer insights",
        "head of customer engagement", "customer engagement",
        "head of customer channels", "head of customer",
        "vp of customer",
    ]
    for kw in cust_kw:
        if kw in t:
            if seniority in ("C-Level", "Director", "VP"):
                return ("PASS", "1", f"{title_raw} at {c} — customer experience leader; FitXpress value prop maps to member engagement KPIs.", "member-engagement")
            return ("WEAK", "", f"{title_raw} at {c} — customer-facing role at {seniority} level; potential internal champion for digital health tools.", "member-engagement")
    
    # F. Product leaders
    if "chief product officer" in t or "head of product" in t:
        return ("PASS", "1", f"{title_raw} at {c} — product leadership owns digital health tool strategy.", "digital-transformation")
    
    # G. CEO / MD / Founder
    ceo_kw = ["chief executive officer", "ceo & md", "managing director and founder",
              "co-founder", "group executive chairman"]
    for kw in ceo_kw:
        if kw in t:
            return ("PASS", "1", f"{title_raw} at {c} — CEO/Founder at target company; ultimate decision-maker for new digital health partnerships.", _angle(t, insurer))
    
    # H. C-Suite / GM at target companies (PASS P3 for insurers, P2 for digital health)
    c_suite = [
        "chief strategy officer", "chief operating officer", " coo ",
        "chief financial officer", "chief marketing officer",
        "chief technology officer", "chief information officer",
        "chief data scientist", "chief customer officer",
        "group executive",
        "general manager",
        "managing director",
    ]
    for kw in c_suite:
        if kw in t or t.startswith(kw.strip()):
            if insurer:
                return ("PASS", "3", f"{title_raw} at {c} — C-Level executive at target insurer; may sponsor digital health initiatives.", _angle(t, True))
            else:
                return ("PASS", "2", f"{title_raw} at {c} — senior executive at digital health company; broad decision-making scope.", _angle(t, False))
    
    # I. "Head of" with strong health/digital signal → at minimum WEAK
    head_health_kw = [
        "head of health", "health manager", "health policy manager",
        "head of mental health", "health ventures",
        "head of provider", "head of clinical",
        "head of hospital",
        "head of operations", "head of workplace health",
        "head of performance", "head of delivery",
        "head of business insights", "head of strategy",
        "head of digital", "head of technology",
        "head of data", "head of ai",
        "head of innovation", "head of growth",
        "head of design", "head of customer",
        "head of marketing", "head of content",
        "head of communications",
        "head of partnerships", "head of business development",
        "head of retention", "head of portfolio",
        "head of expansion",
        "head of corporate strategy",
        "head of commercial",
    ]
    for kw in head_health_kw:
        if kw in t:
            if seniority in ("C-Level", "Director", "VP"):
                if any(x in t for x in ["health", "medical", "clinical", "wellbeing", "wellness", "care", "patient", "member", "customer", "digital", "virtual", "telehealth"]):
                    return ("PASS", "2", f"{title_raw} at {c} — health-relevant senior role at target company; potential FitXpress champion.", _angle(t, insurer))
                return ("WEAK", "", f"{title_raw} at {c} — senior role at target company; unclear if they own health program decisions.", _angle(t, insurer))
            return ("WEAK", "", f"{title_raw} at {c} — relevant role but {seniority} level; may inform rather than make decisions.", _angle(t, insurer))
    
    # J. Any C-Level that fell through (catch-all for execs at target companies)
    if seniority == "C-Level":
        if insurer:
            return ("PASS", "3", f"{title_raw} at {c} — executive role at target insurer; may influence digital health strategy.", "digital-transformation")
        if dh:
            return ("PASS", "2", f"{title_raw} at {c} — executive at digital health company; relevant to FitXpress.", _angle(t, False))
    
    # K. Director/VP health-adjacent
    if seniority in ("Director", "VP"):
        # First check: is this clearly a non-health role?
        non_health_dir = ["security", "cyber", "ciso", "legal", "finance", "accounting",
                          "people and culture", "hr", "human resources", "recruitment",
                          "procurement", "property", "facilities", "maintenance",
                          "communications", "public relations", "marketing technology", "martech"]
        if any(x in t for x in non_health_dir):
            return ("FAIL", "", f"{title_raw} at {c} — {seniority}-level non-health role at insurer; not in FitXpress buying chain.", "")
        
        if any(x in t for x in ["health", "clinical", "medical", "wellbeing", "wellness", "care", "patient", "member", "customer"]):
            return ("PASS", "2", f"{title_raw} at {c} — health-relevant director at target company; potential program decision-maker.", _angle(t, insurer))
        if any(x in t for x in ["digital", "technology", "data", "analytics", "transformation", "innovation", "strategy", "product", "growth", "insights"]):
            return ("WEAK", "", f"{title_raw} at {c} — director at target company; may influence digital health tool decisions.", _angle(t, insurer))
        if any(x in t for x in ["partnership", "commercial", "sales", "business development", "marketing", "design", "experience", "communications"]):
            return ("WEAK", "", f"{title_raw} at {c} — director at target company; commercial/design role not directly in health program decisions.", _angle(t, insurer))
        return ("WEAK", "", f"{title_raw} at {c} — director-level at target company; unclear health program ownership.", _angle(t, insurer))
    
    # L. Manager/IC at digital health companies → more generous
    if dh:
        if any(x in t for x in ["health", "clinical", "medical", "patient", "product", "technology", "data", "analytics", "customer", "support", "engagement", "growth", "marketing", "operations", "design", "practice"]):
            return ("WEAK", "", f"{title_raw} at {c} — relevant role at digital health company; smaller orgs mean broader decision influence even at {seniority} level.", _angle(t, False))
        return ("FAIL", "", f"{title_raw} at {c} — role at digital health company without clear health/product relevance.", "")
    
    # M. Manager/IC at insurers — health keyword = WEAK
    if insurer:
        health_signal = any(x in t for x in ["health", "clinical", "medical", "wellbeing", "wellness", "care", "patient", "member experience", "customer experience", "customer health", "customer engagement", "primary care", "hospital", "nursing", "pharmacist"])
        tech_signal = any(x in t for x in ["product manager", "product owner", "technology application", "enterprise architect", "data scientist", "ai", "digital product"])
        biz_signal = any(x in t for x in ["cx ", " cx", "customer experience", "new ventures", "venture", "innovation", "strategy", "business development"])
        
        if health_signal:
            if "nursing" in t or "pharmacist" in t:
                return ("WEAK", "", f"{title_raw} at {c} — frontline clinical role; limited program/strategy authority but health-adjacent; potential internal champion.", _angle(t, insurer))
            return ("WEAK", "", f"{title_raw} at {c} — health-relevant but {seniority} level at large insurer lacks purchasing authority; internal champion potential.", _angle(t, insurer))
        
        if tech_signal:
            if any(x in t for x in ["clinical", "health", "healthcare", "primary care"]):
                return ("WEAK", "", f"{title_raw} at {c} — health-adjacent tech role at insurer; potential internal champion for digital health tools.", _angle(t, insurer))
            # AI/innovation/product roles at insurer → WEAK (may touch member-facing health tools)
            if any(x in t for x in ["ai", "artificial intelligence", "machine learning", "innovation", "new venture", "ventures"]):
                return ("WEAK", "", f"{title_raw} at {c} — innovation/tech role at insurer; may touch member-facing digital health tools.", "digital-transformation")
            # Product manager/owner without health context
            if "product manager" in t or "product owner" in t:
                return ("WEAK", "", f"{title_raw} at {c} — product role at insurer; may touch member-facing tools if relevant to health products.", "digital-transformation")
            return ("FAIL", "", f"{title_raw} at {c} — technology role without clear health program connection.", "")
        
        if biz_signal:
            return ("WEAK", "", f"{title_raw} at {c} — business/strategy role at insurer; may touch digital health innovation but unclear decision authority.", _angle(t, insurer))
    
    # ============================================================
    # FAIL PATTERNS (only for non-exec, non-senior, non-health roles)
    # ============================================================
    
    fail_kw = [
        "security", "cyber", "ciso",
        "property", "facilities", "maintenance",
        "procurement", "supplier",
        "people and culture", "human resources", "people partner", "strategic people",
        "people & culture", "leadership development",
        "executive assistant", "personal assistant",
        "legal operations", "head of legal", "privacy legal",
        "team manager", "call centre", "outbound services",
        "business support manager", "zone manager", "territory manager",
        "regional manager", "cluster manager", "retail centre", "retail store",
        "branch manager", "branch support", "store manager",
        "practice manager", "assistant manager", "assistant store", "assistant to",
        "local community leader", "community leader",
        "manager ezypay", "business adminstration",
        "group reporting manager", "group capital works",
        "test manager", "principal engineer",
        "integration platform", "api/integration",
        "cloud security", "end user services",
        "it business partner", "it finance",
        "team leader", "management team",
        "dentist", "optical",
        "business practice", "business projects",
        "business improvement", "operational excellence",
        "continuous improvement", "continuous delivery",
        "capability & process", "quality education", "quality partner",
        "initiative owner", "decisioning manager",
        "commercial & pricing", "conversion optimisation",
        "customer retention principal",
        "senior manager - group strategy", "group senior manager",
        "group strategy manager",
        "partner - digital, data, & ai risk",
        "hsw partner", "hsw business partner",
        "employee change", "employee communications",
        "internal communications", "external communications",
        "corporate communications", "communications manager",
        "head of martech", "martech data", "technology domain manager - martech",
        "creative director", "art director",
        "loyalty partnerships", "cost optimisation",
        "actuarial", "treasury", "tax",
        "audit", "internal audit",
        "remediation", "controls mastery",
        "planning and reporting",
        "capital and reserving",
        "payment integrity",
        "roving maintenance",
        "hs partner",
        "business owner", "owner",
        "group reporting",
    ]
    
    for kw in fail_kw:
        if kw in t:
            return ("FAIL", "", f"{title_raw} at {c} — role not in FitXpress buying chain.", "")
    
    # ============================================================
    # FINAL CATCH-ALL
    # ============================================================
    
    # If we got here and it's an insurer or digital health company, classify as FAIL
    return ("FAIL", "", f"{title_raw} at {c} — role does not align with FitXpress buyer personas.", "")


def main():
    contacts = []
    with open(INPUT_CSV, 'r', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            contacts.append(row)
    print(f"Read {len(contacts)} contacts")
    
    results = []
    for c in contacts:
        d, p, r, a = classify(c['title'], c['company_name'], c['seniority'])
        results.append({
            'person_id': c['person_id'], 'full_name': c['full_name'],
            'title': c['title'], 'company_name': c['company_name'],
            'decision': d, 'priority': p, 'reason': r, 'recommended_message_angle': a,
        })
    
    pass_r = [r for r in results if r['decision'] == 'PASS']
    weak_r = [r for r in results if r['decision'] == 'WEAK']
    fail_r = [r for r in results if r['decision'] == 'FAIL']
    
    p1 = sum(1 for r in pass_r if r['priority'] == '1')
    p2 = sum(1 for r in pass_r if r['priority'] == '2')
    p3 = sum(1 for r in pass_r if r['priority'] == '3')
    
    print(f"\nPASS: {len(pass_r)} (P1:{p1} P2:{p2} P3:{p3})")
    print(f"WEAK: {len(weak_r)}")
    print(f"FAIL: {len(fail_r)}")
    
    # Write CSV
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=[
            'person_id', 'full_name', 'title', 'company_name',
            'decision', 'priority', 'reason', 'recommended_message_angle'
        ])
        w.writeheader()
        w.writerows(results)
    
    # Company stats
    cc = Counter(r['company_name'] for r in results)
    cp = Counter(r['company_name'] for r in pass_r)
    ac = Counter(r['recommended_message_angle'] for r in results if r['recommended_message_angle'])
    
    # Build MD
    pass_ex = [r for r in pass_r if r['priority'] == '1'][:5]
    fail_ex = fail_r[:5]
    
    md = f"""# ICP Validation Summary — 2026-07-16-au-telehealth

**Product:** FitXpress
**Campaign:** Australian telehealth & health insurance
**Validation date:** 2026-07-16
**Validator:** icp-validator (automated classification v3)

---

## Stats

| Metric | Count | % |
|--------|-------|---|
| **Total contacts** | {len(results)} | 100% |
| **PASS** | {len(pass_r)} | {len(pass_r)/len(results)*100:.1f}% |
| **WEAK** | {len(weak_r)} | {len(weak_r)/len(results)*100:.1f}% |
| **FAIL** | {len(fail_r)} | {len(fail_r)/len(results)*100:.1f}% |

### PASS priority distribution

| Priority | Count | % of PASS |
|----------|-------|-----------|
| P1 (direct match) | {p1} | {p1/max(len(pass_r),1)*100:.1f}% |
| P2 (strong fit) | {p2} | {p2/max(len(pass_r),1)*100:.1f}% |
| P3 (exec sponsor) | {p3} | {p3/max(len(pass_r),1)*100:.1f}% |

### By company

{chr(10).join(f'- **{c}**: {t} total ({cp.get(c, 0)} PASS, {sum(1 for r in weak_r if r["company_name"]==c)} WEAK, {sum(1 for r in fail_r if r["company_name"]==c)} FAIL)' for c, t in cc.most_common())}

### Message angle distribution

{chr(10).join(f'- {angle}: {count}' for angle, count in ac.most_common())}

---

## Top concerns

1. **Security/Risk/IT infrastructure roles dominate FAILs** — Large security and IT teams at insurers are entirely outside the FitXpress buying chain.

2. **Retail/branch operations** — Medibank and HCF maintain physical retail networks; branch/territory managers are customer-facing but not health-program decision-makers.

3. **Manager/IC level at enterprise insurers** — Even health-relevant managers at Medibank/Bupa/HCF (10K+ employees) lack purchasing authority for digital health tools.

4. **Dental/Optical divisions** — Specifically excluded per hypothesis; directors in these areas are WEAK at best.

5. **Board members** — Non-Executive Directors and Chairs have strategic influence but aren't operational buyers.

---

## 5 PASS P1 examples

1. **Andrew Wilson, Group Chief Medical Officer, Medibank** — 15-year tenure; ultimate clinical authority at Australia's largest health insurer.
2. **Pauline Smyth, Head of Virtual Health (Amplar Health), Medibank** — Exact match to "Head of Virtual Care" target persona.
3. **Shona Sundaraj, Group Medical Director, Medibank** — Direct match to "Group Medical Director" buyer persona.
4. **Dr Jonathan Brown, Medical Director - BUPA Medical, Bupa Australia** — Medical Director with clinical governance authority.
5. **James McDonald, Head of Telehealth Operations, Bupa Australia** — Perfect FitXpress target for virtual-care angle.

---

## 5 FAIL examples

1. **Daisy Wong, Head of Security Awareness, Medibank** — Security awareness; zero health program relevance.
2. **Aaron Green, National Property Manager, Medibank** — Facilities management; no connection to telehealth.
3. **Chloe Dwyer, People and Culture Business Partner, HCF Australia** — HR role; not in health program decision chain.
4. **Philip Mackney, Co-Founder, Hopstep** — Wrong vertical entirely (healthcare recruitment).
5. **Faiza Kazmi, Dentist, HCF Australia** — Dental; explicitly excluded per hypothesis.

---

## Recommendations

1. **Start with P1 contacts ({p1} contacts)** — Direct-bullseye titles owning telehealth, virtual care, clinical ops, and member experience.
2. **Digital health platforms as parallel track** — Mosh, InstantScripts, Medmate, Qoctor are smaller and faster-moving. Lead with weight-management/GLP-1 angle using UK Meds/Yazen proof points.
3. **P2 contacts as wave 2 ({p2} contacts)** — Health-relevant directors and operational leaders.
4. **P3 contacts for executive sponsorship ({p3} contacts)** — Broad C-Level roles; useful for warm intros or referrals.
5. **Review WEAK group ({len(weak_r)} contacts)** — Board members, design/strategy directors, manager-level health roles. Some may be valuable internal champions.
6. **Exclude FAIL ({len(fail_r)} contacts)** — No FitXpress relevance.

---

## Vadim — please confirm

### WEAK group ({len(weak_r)} contacts)
Categories needing your decision:
- **Board members** (Non-Executive Directors, Chairs): Strategic but not operational. Include or skip?
- **Digital/Tech Directors at insurers**: May influence tool procurement but unclear health program ownership.
- **Design/Experience Directors**: Member-facing but not typically health-program buyers.
- **Manager-level health roles**: Close to topic but no budget authority. Use for referrals?
- **Small digital health company roles**: Broader roles at Mosh/InstantScripts that don't directly touch clinical/health.

### P3 group ({p3} contacts)
{p3} C-Level executives at insurers (CFO, CSO, CMO, GMs). Senior enough to sponsor but unlikely direct buyers. Treat as exec sponsor targets or skip?

### Open questions from hypothesis
- Existing relationships with Medibank/Bupa/HCF to exclude?
- Medibank Health Solutions / Medibank Private as separate entities or same group? (Currently normalized)
- Priority order: insurers first or digital platforms first?
"""
    
    with open(OUTPUT_MD, 'w', encoding='utf-8') as f:
        f.write(md)
    
    print(f"\nWrote {OUTPUT_CSV} ({len(results)} rows)")
    print(f"Wrote {OUTPUT_MD}")


if __name__ == '__main__':
    main()
