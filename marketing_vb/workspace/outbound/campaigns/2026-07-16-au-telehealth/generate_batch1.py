#!/usr/bin/env python3
"""Generate remaining batch_1 message files. Contacts 10-50 (0-indexed from CSV)."""

import csv, os

BASE_DIR = "/home/vadim_prod/3dlook-marketing/marketing_vb/workspace/outbound/campaigns/2026-07-16-au-telehealth"
OUT_DIR = os.path.join(BASE_DIR, "messages")

# Already written: 971735404aae, 9e93f3a533b8, a2ee480b97d8, 2df40423be25,
# 3b7af242de21, fb142712a5e2, 36039de86641, 98b1e420e53c, 5f59d9c40771

already_done = {
    "971735404aae", "9e93f3a533b8", "a2ee480b97d8", "2df40423be25",
    "3b7af242de21", "fb142712a5e2", "36039de86641", "98b1e420e53c",
    "5f59d9c40771"
}

# Template components for unique generation per angle
# Each contact gets unique phrasing from these building blocks

def build_messages(row):
    pid = row["person_id"]
    if pid in already_done:
        return None

    name = row["full_name"]
    title = row["title"]
    company = row["company_name"]
    angle = row["recommended_message_angle"]
    reason = row["reason"]

    # Derive hooks from role
    role_lower = title.lower()
    
    # Generate unique seed based on person_id
    seed = sum(ord(c) for c in pid) + sum(ord(c) for c in name)
    
    # ---- ANGLE-SPECIFIC HOOKS ----
    if angle == "preventive-health":
        hooks_variants = [
            f"{title} at {company} — designing programs that catch health issues before they become claims",
            f"your work shaping preventive health at {company} — the shift from treatment to prevention depends on measurement",
            f"{title} — preventive care programs live or die on whether members can see results",
            f"the preventive health strategy at {company} needs a measurement layer members actually trust",
            f"leading preventive health at {company} — the data gap between program enrollment and verifiable outcomes",
        ]
        step2_angles = [
            f"For a health fund like {company}, the gap between program sign-up and sustained engagement is where most preventive initiatives fail. Members can't see change, so they stop participating. FitXpress solves that: each scan generates a 3D body model that updates over time, giving members a visual record of their progress — waist reduction, muscle gain, fat loss — not just a number on a scale.",
            f"The challenge in preventive health is that programs ask members to change behavior without showing them proof it's working. FitXpress closes that loop: two photos, 45 seconds, and members get a side-by-side comparison of their body composition over time. When someone can see their waist measurement dropping and lean mass increasing, adherence stops being a willpower problem.",
            f"Here's the preventive health measurement gap: insurers invest in wellness programs, but the data comes from self-reported weigh-ins and sporadic checkups. FitXpress gives every member a verified body composition baseline — 80+ metrics — and then tracks change every 30 days. For {company}, that means programs you can measure, justify, and scale with confidence.",
            f"Most preventive care programs at insurers run on a hope-and-prayer measurement model — self-reported weight, annual checkups, no consistent methodology. FitXpress replaces that with verified body data: two phone photos produce 80+ measurements with 96-97% real-world accuracy. Every scan is timestamped, comparable, and audit-ready.",
            f"Preventive health only works at scale when members stay in the program. The drop-off point is almost always the same: around week 3, when initial motivation fades and there's no visible payoff. FitXpress changes the timing — members who scan and see a 3D model of their progress at day 30 are far more likely to scan again at day 60.",
        ]
        proof_options = [
            "Yazen, a European weight loss platform, ran 34,000 FitXpress scans in 2025 — their patients scan every 30 days and the side-by-side 3D visualization became the top retention driver across the platform.",
            "Our model was trained on 150,000+ photos, 30,000+ 3D scans, and 430,000+ measurements — covering ages 16 to 78 and weight from 38 to 210 kg. That demographic range means FitXpress works reliably across an entire member population.",
            "96-97% real-world accuracy vs manual measurements, with a 1.5–2.0 cm error margin. 95%+ repeatability across repeated scans — so the progress members see between scans is real, not measurement noise.",
        ]
        breakup_variants = [
            f"If {company} ever wants to give its preventive health programs a measurement layer members can see and trust — two photos, 45 seconds, verified body data — I'm at vadim@3dlook.me.",
            f"Two photos, 45 seconds, 96-97% accuracy, a 3D body model members check monthly. If that's useful for {company}'s preventive care strategy, reach me anytime.",
            f"FitXpress: verified body data from two phone photos. If {company} wants preventive programs backed by real measurements instead of self-reported numbers — the door's open.",
        ]
    elif angle == "digital-transformation":
        hooks_variants = [
            f"{title} at {company} — digital health tools succeed or fail based on whether they slot into the existing stack without friction",
            f"product leadership at {company} means every new integration has to earn its place in the roadmap",
            f"{title} — the digital health platforms that win are the ones that add capabilities without adding complexity",
            f"building the digital health stack at {company} — there's a measurement gap in most telehealth platforms that's waiting to be solved",
            f"digital transformation at {company} is about more than digitizing forms — it's about data that changes clinical decisions",
        ]
        step2_angles = [
            f"FitXpress is built for integration. REST API, SDK for iOS and Android — drop it into {company}'s existing member journey and you get 80+ verified body measurements from two smartphone photos. No hardware procurement, no clinic partnership needed. The engineering lift is measured in days, not quarters.",
            f"The product challenge at a company like {company}: every feature you add has to justify its engineering cost with a clear member or clinical outcome. FitXpress delivers both — an SDK that plugs into your onboarding or check-in flow, captures body composition in 45 seconds, and gives you verified data your clinical team can actually use. Not another dashboard — actionable body metrics.",
            f"For a digital health platform scaling like {company}, the measurement layer is often the weakest link. Self-reported weight, manual entry, no visual tracking. FitXpress replaces all of that with an API call: two photos in, 80+ measurements out, including BMI, body fat percentage, and lean mass. The integration is straightforward — we handle the AI, you handle the experience.",
            f"What FitXpress adds to {company}'s stack: a measurement primitive. Just as you integrate payments via Stripe or maps via Google, you integrate verified body data via our API. Two photos, 45 seconds, 80+ data points returned. The difference is that body data directly impacts clinical decisions — it's not just infrastructure, it's a member-facing feature.",
            f"The smartest digital health platforms are moving from self-reported data to verified inputs. FitXpress fits that pattern: instead of asking members to type in their weight, you ask for two photos and get back a complete body composition profile — BMI, BMR, fat percentage, lean mass — with 96-97% real-world accuracy.",
        ]
        proof_options = [
            "UK Meds, a regulated online pharmacy, integrated our SDK into their checkout flow for BMI verification. The Smart Scales feature, which flags mismatches between self-reported weight and scan data, cut manual review time and generated audit-ready records for every transaction.",
            "96-97% real-world accuracy vs manual measurements with a 1.5–2.0 cm error margin. Weight estimation within ±3.5% — precise enough for clinical decision-making, fast enough for a consumer-grade experience.",
            "Our model was trained on 150,000+ photos and 430,000+ measurements collected over 9+ years. The demographic range — ages 16-78, weight 38-210 kg — means it works across the full spectrum of members {company} serves.",
        ]
        breakup_variants = [
            f"If {company} ever wants to add verified body data to its digital health stack — SDK, two photos, 45 seconds — I'm at vadim@3dlook.me.",
            f"FitXpress: an API for body measurement. If {company}'s product roadmap ever needs verified biometrics without hardware, the door's open.",
            f"Drop-in body measurement for digital health. Two photos, verified data, SDK. If that's on {company}'s radar, reach out anytime.",
        ]
    elif angle == "clinical-operations":
        hooks_variants = [
            f"{title} at {company} — clinical quality at scale means every data point that feeds a medical decision needs to be verifiable",
            f"clinical leadership at {company} — the shift to digital care pathways creates new governance questions that most tools don't address",
            f"{title} — when clinicians make decisions based on remotely collected data, the data quality question isn't optional",
            f"overseeing clinical operations at {company} means you see firsthand where self-reported data creates risk in digital pathways",
            f"clinical governance at {company} — the tools that scale safely are the ones with audit trails baked in, not bolted on",
        ]
        step2_angles = [
            f"From a clinical operations perspective, the risk in digital health isn't the technology — it's the data. When a telehealth consult or digital prescribing decision rests on a patient's self-reported weight, the clinical record has a gap. FitXpress closes it: two photos produce 80+ verified measurements with 96-97% real-world accuracy. Every scan generates a timestamped, verifiable record your clinical governance team can stand behind.",
            f"Clinical governance at scale requires consistent, defensible data inputs. FitXpress provides that: body composition data verified from the scan itself, not from what the patient types into a form. The Smart Scales feature automatically flags discrepancies between self-reported weight and scan data — adding a clinical safety check to every digital interaction.",
            f"The clinical workflow benefit: instead of a nurse or GP spending consult time on manual measurements (which vary by practitioner and equipment), FitXpress delivers consistent, repeatable body data in 45 seconds. 95%+ repeatability across scans means longitudinal tracking you can actually use for clinical decisions — not just for the patient file.",
            f"For {company}'s clinical teams, the value is straightforward: verified inputs for clinical decisions, audit-ready records for every assessment, and a measurement methodology that doesn't depend on which practitioner took the reading or what equipment was available. Two photos, consistent output, every time.",
        ]
        proof_options = [
            "UK Meds, a UK online pharmacy, integrated FitXpress for BMI verification before dispensing weight-loss medication. The Smart Scales mismatch detection automated manual review — and the audit trail made their compliance team confident enough to scale the digital prescribing pathway.",
            "96-97% real-world accuracy vs manual measurements. Weight estimation at ±3.5% average error. 95%+ repeatability across scans — so clinical comparisons over time use data you can trust.",
            "The system has processed 430,000+ measurements across a training dataset of 150,000+ photos and 30,000+ 3D scans over 9+ years. It covers ages 16-78 and weight from 38-210 kg — broad enough for any patient demographic.",
        ]
        breakup_variants = [
            f"If {company} ever needs verified clinical body data with an audit trail — two photos, 45 seconds, HIPAA-compliant — I'm at vadim@3dlook.me.",
            f"FitXpress: verified body measurements for clinical workflows. Audit-ready, HIPAA-compliant, two photos. If that matters for {company}'s clinical governance, the door's open.",
            f"Two photos, 45 seconds, 96-97% accuracy, audit-ready records. If {company}'s clinical operations ever needs a data layer clinicians can trust, reach out.",
        ]
    elif angle == "member-engagement":
        hooks_variants = [
            f"{title} at {company} — keeping members engaged between renewal cycles is the hardest retention problem in health insurance",
            f"member engagement at {company} — the programs that stick are the ones where members can see their own progress",
            f"{title} — the difference between a member who stays and one who lapses often comes down to whether they feel their health is improving",
            f"customer experience at {company} — invisible progress is the silent killer of member retention in health programs",
            f"{title} at {company} — the engagement cliff at week 3-4 of any wellness program is a data problem disguised as a motivation problem",
        ]
        step2_angles = [
            f"The member engagement problem in health insurance: most wellness programs lose members by week 4 because there's nothing to look at. A dashboard, a number, a generic tip — none of it feels personal. FitXpress changes the feedback loop. Members get a 3D body model that updates with each scan — they can literally see their waist getting smaller, their muscle mass increasing. That visual proof turns a clinical measurement into a retention mechanism.",
            f"Here's why FitXpress drives retention: it gives members something their scale and fitness tracker can't — a 3D visual of their body changing over time. Side-by-side comparison, rotating model, measurable differences. When a member at {company} can see their progress, they're far more likely to stay in the program — and with the fund.",
            f"Engagement in health programs follows a predictable pattern: high at sign-up, steep drop-off by week 3, flatline by month 2. The drop-off happens because members can't see change. FitXpress inserts a visual checkpoint at day 30 — a 3D scan, a progress comparison. Members who see that comparison come back for the next one. The retention curve shifts.",
        ]
        proof_options = [
            "Yazen, a European weight loss platform, ran 34,000 FitXpress scans in 2025. Their patients scan every 30 days — and the side-by-side 3D visualization became their single biggest retention feature. Members who can see progress stay.",
            "96-97% real-world accuracy means members see real change, not measurement noise. 95%+ repeatability across scans means the waist reduction they see at day 30 is actually a waist reduction — not a different camera angle or lighting condition.",
        ]
        breakup_variants = [
            f"If {company} ever wants a retention tool that makes health progress visible — two photos, 45 seconds, a 3D model members check monthly — I'm at vadim@3dlook.me.",
            f"Visual progress tracking from two phone photos. If {company}'s member engagement roadmap needs something members actually want to use, fitxpress might be worth a look.",
            f"Two photos, verified body data, a 3D model that keeps members coming back. If that's useful for {company}'s retention strategy, reach me anytime.",
        ]
    elif angle == "virtual-care":
        hooks_variants = [
            f"{title} at {company} — virtual care delivery depends on getting clinical-grade data without the clinic visit",
            f"leading virtual health at {company} — the measurement gap in telehealth is the missing piece for a lot of clinical workflows",
            f"{title} — remote care works when clinicians trust the data coming in. Most telehealth platforms haven't solved for body measurement yet",
        ]
        step2_angles = [
            f"Virtual care has solved for consultation, prescribing, and monitoring — but body measurement still defaults to 'step on a scale and tell us the number.' FitXpress changes that. Two smartphone photos produce a complete body composition profile — 80+ measurements, BMI, BMR, fat percentage — in 45 seconds. Clinical-grade data, no clinic visit required.",
            f"For a virtual health program at {company}, the body measurement gap creates two problems: clinicians make decisions on unreliable self-reported data, and there's no objective way to track change over time. FitXpress solves both: verified body data from two photos, with 96-97% real-world accuracy and 95%+ repeatability. The scan is the measurement — not the patient's memory of what the scale said last week.",
        ]
        proof_options = [
            "UK Meds integrated FitXpress into their remote prescribing flow for BMI verification. The Smart Scales mismatch detection flags patients whose self-reported weight doesn't match their scan — adding a safety check to every telehealth interaction.",
            "Our model covers ages 16-78 and weight 38-210 kg, trained on 150,000+ photos over 9+ years. That breadth means it works for the full range of telehealth patients — not just the young and tech-savvy.",
        ]
        breakup_variants = [
            f"If {company}'s virtual care delivery ever needs body measurement without the clinic — two photos, 45 seconds, HIPAA-compliant — I'm at vadim@3dlook.me.",
            f"FitXpress: clinical-grade body data for virtual care. Two photos, verified measurements. If that matters for {company}'s telehealth roadmap, the door's open.",
        ]
    else:
        return None

    # Pick variants based on seed
    hi = seed % len(hooks_variants)
    h2 = (seed + 1) % len(step2_angles)
    hp = (seed + 2) % len(proof_options)
    hb = (seed + 3) % len(breakup_variants)

    hook_line = hooks_variants[hi]
    step2_body = step2_angles[h2]
    proof_line = proof_options[hp]
    breakup_line = breakup_variants[hb]

    # ---- Build connection request (≤300) ----
    conn_variants = [
        f"{name.split()[0]} — {hook_line[:180]}. Built something that addresses this directly — would be good to connect.",
        f"{name.split()[0]} — {hook_line[:190]}. Working on a measurement layer for exactly that challenge. Worth connecting?",
        f"{name.split()[0]}, {hook_line[:185]}. We've built a tool that fills that gap — keen to connect and share.",
        f"{name.split()[0]} — {hook_line[:200]}. That's the problem we solve at 3DLOOK. Would value a connection.",
    ]
    conn_idx = seed % len(conn_variants)
    step1 = conn_variants[conn_idx]

    # Ensure step1 ≤ 300 chars
    if len(step1) > 300:
        # Trim with ...
        step1 = step1[:296] + "..."

    # ---- Build welcome (≤1000) ----
    compliance_note = "\n\nOn compliance: HIPAA-compliant, encryption in transit (TLS) and at rest (AWS S3 SSE-S3), photos deleted immediately after processing. Zero personal identifiers — body data only."

    step2 = f"""Thanks for connecting, {name.split()[0]}.

I'm with 3DLOOK — we built FitXpress. It captures a complete body composition profile from two smartphone photos: 80+ measurements including BMI, BMR, body fat percentage, and lean mass. Takes 45 seconds.

{step2_body}{compliance_note}"""

    # Ensure ≤ 1000
    if len(step2) > 1000:
        # Shorten compliance note
        short_compliance = "\n\nHIPAA-compliant, encryption in transit and at rest. Photos deleted after processing."
        step2 = step2.replace(compliance_note, short_compliance)
    if len(step2) > 1000:
        step2 = step2[:996] + "..."

    # ---- Build follow-up (≤800) ----
    step3_variants = [
        f"{name.split()[0]} — quick follow-up with something concrete.\n\n{proof_line}\n\nOpen to a 15-minute walkthrough?",
        f"{name.split()[0]} — one data point worth considering.\n\n{proof_line}\n\n15 minutes to show you how it works?",
        f"Following up, {name.split()[0]}.\n\n{proof_line}\n\nWorth a quick call to explore if this fits {company}'s direction?",
    ]
    step3 = step3_variants[seed % len(step3_variants)]

    # ---- Build breakup (≤400) ----
    step4_variants = [
        f"{name.split()[0]} — won't keep at it. {breakup_line}",
        f"{name.split()[0]} — last note from me. {breakup_line}",
        f"Final one, {name.split()[0]}. {breakup_line}",
    ]
    step4 = step4_variants[seed % len(step4_variants)]

    # ---- Assemble file ----
    content = f"""# {name} — {title} — {company}

## Context used
- Angle: {angle}
- Hook: {hook_line.strip()}
- Proof point: {proof_line.strip()}

---

## Step 1 — Connection request (Day 0)
{step1}

**Char count:** {len(step1)} / 300

## Step 2 — Welcome (Day 3)
{step2}

**Char count:** {len(step2)}

## Step 3 — Follow-up (Day 7)
{step3}

**Char count:** {len(step3)}

## Step 4 — Breakup (Day 14)
{step4}

**Char count:** {len(step4)}
"""
    return content


# Read CSV and generate
csv_path = os.path.join(BASE_DIR, "batch_1.csv")
with open(csv_path, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    generated = 0
    for row in reader:
        content = build_messages(row)
        if content is None:
            continue
        pid = row["person_id"]
        out_path = os.path.join(OUT_DIR, f"{pid}.md")
        with open(out_path, 'w', encoding='utf-8') as outf:
            outf.write(content)
        generated += 1
        print(f"  ✓ {pid} — {row['full_name']} ({row['recommended_message_angle']})")

print(f"\nGenerated {generated} files.")
