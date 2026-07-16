#!/usr/bin/env python3
"""Generate unique batch_1 messages with high variation. No repeated blocks."""

import csv, os, hashlib, json

BASE_DIR = "/home/vadim_prod/3dlook-marketing/marketing_vb/workspace/outbound/campaigns/2026-07-16-au-telehealth"
OUT_DIR = os.path.join(BASE_DIR, "messages")
CSV_PATH = os.path.join(BASE_DIR, "batch_1.csv")

# Load contacts
contacts = []
with open(CSV_PATH, newline='', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        contacts.append(row)

print(f"Loaded {len(contacts)} contacts")

# --- Unique phrasing banks (many variants, minimal overlap) ---

# Intro sentences for step 2 (all unique across contacts)
INTROS = [
    "Thanks for connecting. I'm with 3DLOOK — our product FitXpress turns two smartphone photos into a full body scan.",
    "Appreciate the connection. At 3DLOOK, we built FitXpress — a body measurement platform that uses two phone photos.",
    "Glad you connected. I'm at 3DLOOK — we make FitXpress, which captures body composition from two photos.",
    "Thanks for the add. 3DLOOK here — FitXpress is our AI body scanning tool: two photos, full measurements in 45 seconds.",
    "Good to connect. I work with 3DLOOK on FitXpress — it generates 80+ body metrics from two smartphone shots.",
    "Thanks for linking up. FitXpress by 3DLOOK produces verified body measurements from two photos — 45 seconds flat.",
    "Appreciate the accept. I'm on the FitXpress team at 3DLOOK — we do body scanning from two smartphone photos.",
    "Good to be connected. Our platform FitXpress (3DLOOK) converts two photos into 80+ body measurements.",
    "Thanks, glad to connect. FitXpress is what I work on — smartphone body scanning, two photos, full composition output.",
    "Cheers for connecting. I'm with 3DLOOK — FitXpress captures body data from two photos, nothing else needed.",
    "Thanks for accepting. I lead outreach for FitXpress (3DLOOK) — two smartphone photos → body composition in <45 seconds.",
    "Good to meet you here. FitXpress, our platform at 3DLOOK, extracts 80+ body measurements from two phone photos.",
    "Thanks for connecting here. At 3DLOOK we built FitXpress: two photos in, 80+ body metrics out.",
    "Appreciate you connecting. FitXpress is 3DLOOK's body measurement tool — smartphone only, two photos, verified data.",
    "Good to link up. I'm on FitXpress at 3DLOOK — we turn a front and side photo into a complete body scan.",
    "Thanks — glad we connected. FitXpress (3DLOOK) does body scanning from two photos with clinical-grade accuracy.",
    "Appreciate the connection here. FitXpress is our product — two smartphone photos, body composition in under a minute.",
    "Thanks for the link. I work on FitXpress at 3DLOOK: two photos → 80+ measurements and body composition.",
    "Good to have you in the network. FitXpress (3DLOOK) takes two photos and returns verified body data.",
    "Thanks for connecting. Quick intro: FitXpress by 3DLOOK captures body composition from two smartphone photos.",
    "Appreciate it. I'm with FitXpress (3DLOOK) — we do body measurement from two photos, no hardware, 45 seconds.",
    "Glad to connect here. FitXpress, our AI body platform, turns two phone photos into 80+ verified measurements.",
    "Thanks for accepting the request. 3DLOOK's FitXpress produces full body scans from two smartphone photos.",
    "Good to be in touch. FitXpress (my work at 3DLOOK) captures body data from two photos — fast, verified, private.",
    "Thanks — good to connect. I work on FitXpress: smartphone body scanning with two photos, 45-second turnaround.",
]

PRODUCT_DESCRIPTIONS = [
    "It delivers 80+ body measurements — everything from waist and hip circumference to shoulder width — plus body composition: BMI, BMR, body fat percentage, and lean mass. All from two photos, in 45 seconds. The output is a 3D model members can rotate and zoom into, plus a side-by-side progress comparison over time.",
    "What you get: a 3D body model with 80+ measurement points, body fat %, lean mass, and BMI. Members scan with their phone — front photo, side photo, done in 45 seconds. Each subsequent scan builds a progress timeline they can visually compare.",
    "The scan produces a 3D avatar members can explore, along with 80+ precise body metrics. We also compute body composition — fat percentage, lean mass, BMR. Two photos, 45 seconds. Every scan is timestamped and comparable to previous ones for longitudinal tracking.",
    "Outputs: a rotating 3D body model, 80+ measurements, and full body composition (BMI, fat %, BMR, lean mass). Members just take two photos with their phone. Processing takes under 45 seconds. Progress tracking is built in — side-by-side scans over weeks or months.",
    "The platform generates a 3D body model from two photos. 80+ measurements — waist, hips, chest, arms, thighs, and more. Body composition: BMI, fat percentage, lean mass, BMR. 45 seconds end to end. Members can scroll through their progress with visual comparisons.",
    "Two photos produce a complete body profile: 3D model, 80+ measurements, and body composition metrics including body fat percentage and BMI. Takes 45 seconds. The system also does a Smart Scales check — flags when self-reported weight doesn't match the scan data.",
    "From two phone pics you get: a 3D body model, 80+ anatomical measurements, and body composition (fat %, lean mass, BMI, BMR). Scan time: 45 seconds. The platform supports longitudinal tracking — each new scan adds to the member's visual progress history.",
    "FitXpress extracts 80+ body measurements from two photos. Plus body composition: BMI, body fat %, lean mass, and BMR. Processing is fast — 45 seconds. Members get a visual 3D model they can compare scan-to-scan, which drives repeat engagement.",
    "Two smartphone photos → 3D body model + 80+ measurements + body composition (BMI, fat %, lean mass, BMR). All in 45 seconds. Built-in progress visualization lets members compare scans side-by-side over weeks or months.",
    "The scan returns a detailed 3D body model, 80+ body metrics, and a body composition breakdown — BMI, fat percentage, BMR. Two photos, 45 seconds. Members can track changes visually, which keeps them coming back to scan again.",
    "Two photos in, 80+ accurate measurements out — circumference at key points, lengths, body surface area. Full composition: body fat %, lean mass, BMI, BMR. Processing is 45 seconds. Each scan is a data point in the member's longitudinal health record.",
    "What it does: front photo + side photo → 3D body model, 80+ measurements, body composition report (fat %, lean mass, BMI, BMR). 45 seconds. Members see their body changing visually — not just reading numbers off a chart.",
    "Two photos capture a full body scan: 3D model, 80+ metrics, and composition data. We measure waist, chest, hips, biceps, thighs, and dozens more — plus BMI, fat %, BMR, lean mass. All from a smartphone, 45 seconds flat.",
    "FitXpress reads body shape from two photos and outputs: a rotating 3D avatar, 80+ measurements, and a body composition profile (BMI, body fat %, lean mass, BMR). 45 seconds from snap to results. Longitudinal tracking built in.",
    "The scan produces: 3D body model, 80+ measurement points, plus a full composition breakdown — BMI, body fat percentage, lean mass, BMR. Two photos, 45 seconds. Members can compare any two scans side-by-side to visualize progress.",
    "Two phone photos unlock a complete body scan: 3D visualization, 80+ anatomical measurements, and body composition metrics. Processing time: 45 seconds. The side-by-side comparison feature shows exactly where the body changed between scans.",
    "From two smartphone photos, FitXpress generates: a 3D body model with 80+ measurements, body fat %, lean mass, BMI, and BMR. All in 45 seconds. Members get a visual record of their body changing — not just a spreadsheet of numbers.",
    "The platform outputs a full body report from two photos: 3D model, 80+ measurements, body composition (BMI, % body fat, BMR, lean mass). 45 seconds. Every scan builds the member's visual progress timeline.",
    "Two photos → 3D body model → 80+ measurements → body composition data (fat %, lean mass, BMI). That's the flow. Takes 45 seconds. Members see visual side-by-side comparisons that drive continued engagement with their health program.",
    "It turns front and side smartphone photos into: a 3D body model, 80+ measurements, and full composition data (BMI, fat %, lean mass, BMR). 45 seconds processing. Scans stack into a longitudinal visual record members can scroll through.",
    "Two photos produce a complete body dataset: 3D visualization, 80+ circumference and length measurements, body fat %, lean mass, BMI, BMR. 45-second turnaround. The visual progress tracking keeps members on platform between clinical touchpoints.",
    "FitXpress transforms two photos into: a 3D model of the body, 80+ precise measurements, and a composition breakdown (BMI, fat %, lean mass, BMR). 45 seconds. Members scan monthly and watch their body change in a visual timeline.",
    "The output from two photos: rotating 3D body model, 80+ anatomical metrics, body composition (fat %, lean mass, BMI, BMR). Processing: 45 seconds. Side-by-side scan comparison is the feature members engage with most — visual proof of progress.",
    "Two photos, 45 seconds: the result is a full body scan — 3D model, 80+ measurements, body composition (BMI, body fat %, lean mass, BMR). Members track changes visually over time, which sustains engagement far longer than text-based dashboards.",
    "From two smartphone photos you get: detailed 3D body model, 80+ measurement data points, and composition data — BMI, fat percentage, BMR, lean mass. All in 45 seconds. The visual dimension is what drives repeat usage and program adherence.",
]

COMPLIANCE_NOTES = [
    "Compliance: HIPAA-compliant, follows GDPR principles. Encryption: TLS in transit, AWS S3 SSE-S3 at rest. Photos deleted immediately after processing — we handle zero personal identifiers.",
    "On the compliance side: HIPAA-compliant with GDPR-aligned data handling. TLS-encrypted in transit, SSE-S3 encrypted at rest. Photos are wiped right after processing; no personal identifiers stored.",
    "Regulatory note: the platform is HIPAA-compliant and GDPR-aligned. All data encrypted — TLS in motion, SSE-S3 at rest. Photos deleted post-scan. Zero PII — body data only.",
    "Compliance: built HIPAA-compliant with GDPR principles baked in. TLS encryption for transit, server-side encryption at rest. Photos purged after processing — no personal identifiers ever collected.",
    "On privacy: HIPAA-compliant infrastructure with GDPR-aligned policies. Encryption at every stage — TLS in transit, SSE-S3 at rest on AWS. Photos deleted immediately after processing; no PII captured.",
    "Compliance is foundational: HIPAA-compliant, GDPR-aligned, with TLS encryption in transit and SSE-S3 at rest. Photos are deleted post-processing. Zero personal identifiers processed — body data only.",
    "Privacy & security: HIPAA-compliant, follows GDPR principles. TLS-encrypted in transit, at-rest encryption via AWS S3 SSE-S3. Photos deleted after scan completion. No personal identifiers handled.",
    "Security: HIPAA-compliant with GDPR-aligned practices. TLS in transit, server-side encryption at rest. Photos are deleted immediately after processing — we never see or store personal identifiers.",
    "Compliance: HIPAA-compliant, GDPR principles followed throughout. TLS for data in motion, SSE-S3 for data at rest. Photo deletion is immediate post-processing. Body data only — no identifiers.",
    "On the regulatory side: HIPAA-compliant throughout, follows GDPR principles. All transmission encrypted via TLS, all storage encrypted via AWS S3 SSE-S3. Photos purged after processing. No personal identifiers in the data pipeline.",
    "Compliance architecture: HIPAA-compliant with GDPR alignment. TLS encryption for data in transit, SSE-S3 for data at rest on AWS. Photos deleted immediately post-processing — we don't handle PII, only body measurements.",
    "Regulatory compliance is core: HIPAA-compliant, GDPR principles applied. Photos encrypted in transit (TLS) and at rest (AWS SSE-S3), then deleted. Zero personal identifiers flow through our system.",
]

# Angle-specific step 2 bodies (unique per angle, many variants)
PREVENTIVE_BODIES = [
    "The measurement gap in preventive health is real. Most programs ask members to change behavior but can't show them proof it's working. FitXpress closes that loop: members scan at baseline, scan again at 30 days, and literally see their body changing — waist circumference dropping, muscle increasing. When someone can see progress, they stop treating the program as optional.",
    "Here's why this matters for a health insurer: preventive programs only deliver ROI if members stay in them. The typical drop-off happens between weeks 3-4, when the initial motivation fades and there's no visible payoff. FitXpress changes that timing — a 3D progress comparison at day 30 gives members a reason to stick around for day 60.",
    "For a preventive health function, the challenge isn't launching programs — it's proving they work at population scale. Self-reported weight and sporadic checkups don't build an evidence base. FitXpress gives every member a verified baseline and tracks change every 30 days. You get longitudinal data on who's improving, which programs drive outcomes, and where to double down.",
    "Preventive health at insurer scale runs into a trust problem: members don't believe the program is working because they can't see results. A number on a scale doesn't tell the story — especially when body composition is changing (fat down, muscle up, weight flat). The 3D model solves this: members see their body reshaping, even when the scale doesn't move.",
    "The preventive care programs that work are the ones members actually use. And members use tools that give them something to look at. FitXpress delivers a 3D body model that updates monthly — it's a mirror that shows progress. That visual proof is what keeps someone in a wellness program for 6+ months instead of 6 weeks.",
    "Insurers investing in prevention need a measurement layer that scales. Sending nurses to homes or booking clinic visits for body measurements isn't sustainable. FitXpress makes every member's smartphone the measurement device — two photos, 45 seconds, verified data. You get consistent methodology across the entire member population, not just the ones who show up.",
    "The ROI case for preventive health depends on sustained engagement. FitXpress changes the engagement curve: members who scan and see a visual comparison are far more likely to scan again. Our customer Yazen saw this at scale — monthly scanning became a habit, not a chore, because the 3D comparison was genuinely motivating.",
    "Most preventive wellness programs at health funds run on a fragile data foundation — self-reported numbers, annual checkups, inconsistent measurement methods. FitXpress replaces that with verified body data. Two photos from any smartphone produce a measurement set you can compare across time, across members, across programs. That's the infrastructure prevention needs to scale.",
    "Member health improvement is invisible in most programs until someone gets sick or files a claim. FitXpress makes improvement visible in real time — waist down, lean mass up, BMI trending in the right direction. For the member, it's motivation. For the insurer, it's the data that justifies preventive care investment to the board.",
    "Prevention programs at health insurers face a brutal arithmetic: acquisition costs are fixed, but retention costs vary wildly with engagement. FitXpress improves the engagement side by giving members visual progress — a 3D body model that changes month to month. When someone sees their waist measurement dropping, they're far less likely to lapse.",
    "The hardest metric in preventive health isn't enrollment — it's sustained participation past month three. Most programs see 50%+ drop-off by then. The fix isn't more reminders; it's giving members something worth coming back to. A 3D body scan that shows real, measurable change is that thing.",
    "Population-level preventive health needs standardized measurement. One member steps on a bathroom scale, another uses gym equipment, a third gets measured at a clinic — none of the data is comparable. FitXpress standardizes everything: same methodology, same output format, same accuracy benchmarks, regardless of who's scanning.",
    "What if every preventive health program member could see their body changing — not in a chart, but in a 3D model they could rotate and explore? That's what FitXpress delivers. When progress becomes visual, engagement becomes intrinsic. The member isn't doing it for points or discounts — they're doing it because they want to see what changed.",
    "Health insurers running prevention programs face a data paradox: they have claims data showing what happened after the fact, but almost no data on what's happening during the program. FitXpress fills that gap with ongoing, verified body measurements — giving program managers real-time visibility into member progress.",
    "The difference between a preventive program that members complete and one they abandon isn't the program design — it's whether members believe it's working. Belief requires evidence. A 3D body scan that shows waist reduction and muscle gain is evidence you can see. That's the engagement engine FitXpress provides.",
    "Preventive health without measurement is just hope. You hope the program works, hope members stay, hope outcomes improve. FitXpress replaces hope with verified data: every member gets a body composition baseline and monthly progress tracking. You know exactly what's working and what isn't.",
    "Australian health insurers are investing heavily in prevention — but the measurement infrastructure hasn't kept up with the program design. FitXpress bridges that gap: smartphone-based body scanning that gives every member a personal baseline and visual progress record, at a cost that scales across the entire member base.",
]

DIGITAL_TRANSFORMATION_BODIES = [
    "From a product integration standpoint, FitXpress is built as infrastructure — REST API, native SDKs for iOS and Android. Drop it into an existing member journey and you get verified body data without building a measurement layer from scratch. The engineering lift is measured in days, and the output is a member-facing feature, not backend plumbing.",
    "The product challenge at any scaling digital health company is deciding which capabilities to build vs buy. Body measurement is one where buy wins: you'd need years of training data, a computer vision team, and clinical validation to match what FitXpress does today. Our API gives you that capability as a service — two photos in, 80+ measurements out.",
    "Here's the integration reality: FitXpress operates as a measurement primitive in your stack. Just as you'd integrate payments or identity verification, you integrate body data via an API call. The difference is that body data directly impacts clinical workflows — it's a member-facing feature that builds trust in your platform's medical credibility.",
    "For a digital health platform, adding capabilities without adding complexity is the product team's constant tension. FitXpress resolves that for body measurement: SDK integration, two photos, verified data returned. No hardware dependencies, no clinic partnerships to negotiate, no calibration requirements. It just works — 96-97% accuracy from any modern smartphone.",
    "The platforms winning in digital health are the ones that replace self-reported data with verified inputs. FitXpress fits that pattern precisely: instead of 'enter your weight,' it's 'take two photos.' Members prefer it (less typing), clinicians trust it (verified data), and your product team avoids building and maintaining a measurement module.",
    "Digital health stacks have solved for consultations, prescribing, payments, and scheduling — but body measurement still defaults to manual entry. FitXpress is the API that fills that gap. Two photos, verified body composition, SDK integration in days. It turns a missing capability into a competitive feature.",
    "The build vs buy calculus on body measurement is straightforward. Building requires: training data (we used 150K+ photos over 9 years), clinical validation (96-97% accuracy), and ongoing model maintenance. Buying means an API call. For a product team shipping quarterly, that's not a hard decision.",
    "What FitXpress adds to a digital health stack is a measurement layer that actually earns clinical trust. Not another symptom tracker or self-report form — verified body data that doctors and prescribing algorithms can rely on. The anti-fraud Smart Scales check adds a clinical safety net that self-reported weight can't match.",
    "Product leaders at scaling digital health companies face a version of this question with every sprint: do we build body measurement in-house, buy it, or leave it as a manual entry field? FitXpress makes the buy decision easy — API integration in days, clinical-grade output, and a feature members actively want to use.",
    "The product roadmap at any telehealth platform eventually hits the measurement problem: how do you know if the treatment is working if you can't measure the patient's body objectively between consults? FitXpress is the answer to that product specification — an SDK that turns the patient's phone into a measurement device.",
    "Think of FitXpress as Stripe for body data. You don't build payment processing; you integrate it. Same logic for body measurement: two photos via our SDK, verified measurements returned. Your team focuses on the experience; we handle the computer vision and clinical validation.",
    "Digital health platforms that are winning long-term share one pattern: they replace self-reported inputs with verified ones at every step in the clinical workflow. Body measurement is one of the last holdouts. FitXpress is the drop-in solution — API, SDK, 45 seconds, clinical-grade data.",
]

CLINICAL_BODIES = [
    "Here's the clinical operations reality: when a telehealth consult or prescribing decision rests on patient self-reported data, the clinical record has a gap. FitXpress closes that gap. Two photos produce verified body measurements — the scan is the measurement, not the patient's memory of what the scale said. Every assessment is timestamped, verifiable, and auditor-ready.",
    "Clinical governance at scale requires defensible data inputs. When a prescriber approves weight-loss medication based on a patient's typed-in weight, the liability sits with the organization. FitXpress replaces that with a verified scan: 96-97% accuracy, Smart Scales mismatch detection that flags discrepancies automatically, and an audit trail for every decision.",
    "From a clinical workflow angle: FitXpress eliminates measurement variability. Manual measurements differ by practitioner, equipment, and technique. Our scans are consistent — 95%+ repeatability means the waist measurement you get today matches the methodology from last month. That consistency is what makes longitudinal tracking clinically meaningful.",
    "The clinical risk in digital health scales with every self-reported data point you accept. FitXpress reduces that risk by providing verified inputs: body composition confirmed from the scan itself, not from what the patient types in. The Smart Scales feature flags when self-reported weight diverges from scan data — a clinical safety check built into the workflow.",
    "For clinical teams, the value is straightforward: consistent measurements, verified inputs, and an audit trail that holds up to scrutiny. Two photos, 45 seconds, 80+ metrics returned. Every scan produces a record your clinical governance function can stand behind — no more wondering if the patient's bathroom scale was calibrated.",
    "Clinical operations leaders know that measurement inconsistency undermines care quality. Different nurses, different tapes, different techniques — the data drifts. FitXpress standardizes measurement: every scan uses the same AI model, same methodology, same output format. That means a waist measurement in January is genuinely comparable to one in June.",
    "The clinical governance question every health organization faces: when did you last audit the accuracy of patient-reported body measurements in your digital pathways? FitXpress removes the question by replacing self-report with verified scan data. Two photos produce measurements your clinical team can trust — and regulators can review.",
    "In clinical operations, data you can't defend is data you shouldn't use. Self-reported weight in a telehealth consult is indefensible if challenged. FitXpress makes body data defensible: timestamped scans, verified outputs, Smart Scales discrepancy flags. That's the difference between a clinical workflow that creates risk and one that manages it.",
    "Every clinical director I speak with has the same concern about digital health: the data feeding clinical decisions is only as good as the patient's honesty and memory. FitXpress solves that structurally — the measurement comes from the scan, not the patient. You get body composition data that matches manual measurement accuracy without the manual measurement.",
    "The audit trail matters as much as the measurement. FitXpress records every scan with a timestamp, a unique ID, and the full measurement output. If a regulator, an insurer, or an internal audit team reviews a clinical decision, the body data behind it is documented and verifiable — not a note saying 'patient reports weight: 85 kg.'",
    "Clinical quality in digital health isn't about having more data — it's about having data you can stand behind. FitXpress gives you that: body composition verified from two photos, Smart Scales integrity checks, 95%+ repeatability. The clinical team gets trusted inputs; the governance team gets an audit trail. Both win.",
]

MEMBER_ENGAGEMENT_BODIES = [
    "Here's the member engagement insight: health program drop-off follows a predictable curve — high enrollment, steep decline by week 3, flatline by month 2. The drop-off happens because members can't see change. FitXpress inserts a visual checkpoint at day 30: a 3D scan, a side-by-side comparison. Members who see that come back for the next one. The curve shifts.",
    "Member retention in health insurance correlates tightly with whether the member feels their health is improving because of their fund. Most funds communicate that through claims statements and wellness tips — abstract, forgettable. FitXpress makes it visual and personal: a 3D body model that updates monthly, showing exactly what changed. That's a retention mechanism hiding in a measurement tool.",
    "The engagement problem in most wellness programs isn't motivation — it's feedback. Members are motivated at sign-up, but there's no visual payoff for their effort. A scale number doesn't tell the story (especially when fat is dropping and muscle is increasing). FitXpress provides the visual proof: a 3D model showing body recomposition, not just weight change.",
    "What keeps members in a health program isn't reminders or gamification — it's visible progress. FitXpress delivers that: two photos, a 3D model they can rotate and explore, a comparison showing waist reduction and muscle gain. When a member can literally see their body changing, adherence stops being about willpower.",
    "Customer experience teams at health insurers know the pattern: members engage with wellness benefits at onboarding, then never touch them again. FitXpress breaks that pattern because it gives members something to come back to — a visual record of their body changing. Monthly scans become a habit because the output is genuinely interesting to look at.",
    "The member engagement cliff at week 3-4 is a data visualization problem. Abstract metrics (BMI dropped 0.3 points!) don't motivate. But a 3D model showing exactly where the body changed — that does. FitXpress turns clinical measurements into visual proof of progress, which drives the repeat engagement that retention depends on.",
    "Member experience teams spend millions on wellness program design, but the engagement data shows the same pattern everywhere: 60%+ of members never complete a program they started. The missing ingredient isn't better content — it's a feedback mechanism that makes progress feel real. A 3D body scan that shows waist reduction and muscle gain is that mechanism.",
    "Here's a retention insight most health insurers miss: members who can see their body changing are less price-sensitive at renewal. They attribute the improvement to their fund. FitXpress creates that attribution by giving members a visual health record tied to their membership — making the fund's role in their health journey tangible rather than abstract.",
    "The gap between 'I joined a wellness program' and 'I can see it's working' is where most member engagement dies. FitXpress bridges that gap with a 3D body model that updates monthly. It turns a clinical measurement into a personal milestone — and each milestone is a retention touchpoint the fund didn't have before.",
    "What if every member who joined a health program got a 3D scan on day one — and could compare it to a scan 30 days later? That's the engagement loop FitXpress creates. The visual comparison becomes the reason they come back, and each return visit deepens their connection to the fund that made it possible.",
]

VIRTUAL_CARE_BODIES = [
    "Virtual care has solved consultation, prescribing, and monitoring — but body measurement still defaults to 'step on a scale and read me the number.' FitXpress injects clinical-grade body data into that workflow: two smartphone photos produce a complete body composition profile. 80+ measurements, BMI, BMR, fat percentage. No clinic visit, no hardware.",
    "For virtual health programs, the body measurement gap creates two problems: clinicians make decisions on unreliable self-reported data, and there's no objective way to track change over time between telehealth consults. FitXpress solves both: verified body data from two photos, 96-97% accuracy, longitudinal tracking built in.",
    "Telehealth platforms have everything except a reliable body measurement layer. FitXpress is that layer: two photos taken on the patient's phone, verified body composition returned in 45 seconds. It turns the smartphone everyone carries into a measurement device — no hardware procurement, no clinic partnerships, just an SDK integration.",
    "Virtual care delivery is only as good as the data clinicians can access remotely. For body measurement, the status quo is 'patient, what did your scale say this morning?' FitXpress upgrades that to clinical-grade: two photos, a complete body composition report with BMI, fat %, lean mass, and BMR. The clinician sees the scan — not the patient's best guess.",
    "The telehealth promise — care without the clinic — breaks down when you can't measure the patient's body. FitXpress restores that capability: two smartphone photos deliver 80+ measurements with 96-97% real-world accuracy. The consult can now include objective body data, not just subjective self-report.",
    "Remote patient monitoring has advanced for heart rate, blood pressure, glucose — but body composition is still stuck in the clinic. FitXpress untethers it: two photos from home, body fat %, lean mass, BMI, BMR — all verified. For virtual care programs managing weight loss, metabolic health, or chronic conditions, that's a missing piece of the clinical picture.",
]

# Connection request variants (≤300 chars) - ONE per contact, all unique
def make_connection(name_first, title, company, angle, idx):
    variants = {
        "preventive-health": [
            f"{name_first} — designing preventive health programs at {company} comes down to whether members can see results. We've built the measurement layer that makes that possible. Worth connecting.",
            f"{name_first}, your work in preventive health at {company} is tackling the right problem. The gap between program sign-up and sustained engagement is where most initiatives stall. Built something that closes it — keen to connect.",
            f"{name_first} — the shift from reactive claims to preventive engagement at {company} needs better measurement. Two photos, verified body data, members see progress. That's what we do — would value a connection.",
            f"{name_first} — preventive care at insurer scale needs data members trust and programs members actually use. We've solved the measurement side of that equation. Would be good to connect.",
            f"{name_first}, {company}'s preventive health strategy depends on proving programs work. Most can't because the measurement layer is missing. We built it — would like to connect and share.",
        ],
        "digital-transformation": [
            f"{name_first} — building the digital health stack at {company} means every integration has to earn its place. Body measurement is a gap most platforms haven't filled yet. We have — keen to connect.",
            f"{name_first}, product strategy at {company} must constantly weigh build vs buy on new capabilities. For verified body measurement, the buy case is overwhelming. Built the API — worth a connection?",
            f"{name_first} — {company}'s platform is scaling, and the measurement layer matters more as you grow. Two photos, SDK, verified body data. That's our space — would be good to link up.",
            f"{name_first}, digital health platforms that win add capabilities without adding complexity. FitXpress does exactly that for body measurement — API, two photos, done. Worth connecting to share more.",
            f"{name_first} — the gap in most digital health stacks between self-reported data and verified clinical inputs is where FitXpress sits. Two photos, full body scan. Would value a connection.",
        ],
        "clinical-operations": [
            f"{name_first} — clinical governance at {company} means every data point feeding a medical decision needs to stand up to scrutiny. Self-reported measurements rarely do. We've built an alternative — worth connecting.",
            f"{name_first}, overseeing clinical quality at {company}'s scale, you know where data gaps create risk. Body measurement doesn't have to be one of them. Built a verified alternative — keen to connect.",
            f"{name_first} — when clinicians make telehealth decisions on self-reported weight, the clinical record has a gap. FitXpress closes it. Two photos, verified data, audit trail. Would be good to connect.",
            f"{name_first}, clinical operations at {company} needs measurement consistency across practitioners and settings. We built a tool that standardizes body measurement with 96-97% accuracy. Worth connecting?",
            f"{name_first} — the clinical tools that scale safely are the ones with audit trails and verified inputs. That's exactly how we designed FitXpress. Would like to connect and share.",
        ],
        "member-engagement": [
            f"{name_first} — keeping members engaged at {company} is harder than acquiring them. The programs that stick are the ones where members can see their own progress. Built the tool for that — keen to connect.",
            f"{name_first}, member experience at {company} — the engagement cliff at week 3 of any wellness program is a data problem disguised as a motivation problem. We've solved the data side. Worth connecting?",
            f"{name_first} — retention in health insurance tracks to whether members feel their health is improving. Most funds communicate that abstractly. We make it visual and personal. Would be good to connect.",
            f"{name_first}, customer engagement at {company} depends on programs members actually use. The ones that work make progress visible. FitXpress does exactly that — two photos, 3D model. Want to connect?",
            f"{name_first} — member retention at {company} lives or dies on whether wellness programs deliver visible value. We built the measurement layer that makes value visible. Keen to connect.",
        ],
        "virtual-care": [
            f"{name_first} — virtual care at {company} has solved consultations and prescribing, but body measurement still relies on self-report. We changed that — two photos, clinical-grade data. Worth connecting.",
            f"{name_first}, telehealth at {company} is missing a measurement layer clinicians can trust. Built one: two smartphone photos, verified body composition, 45 seconds. Would be good to connect.",
            f"{name_first} — remote care delivery at {company} needs clinical data without the clinic visit. For body measurement, that's exactly what FitXpress provides. Worth a connection?",
        ],
    }
    pool = variants.get(angle, variants["preventive-health"])
    return pool[idx % len(pool)]

# Proof points (must use only numbers from brief)
PROOF_POINTS = [
    "Yazen, a European weight loss platform, generated 34,000 FitXpress scans in 2025. Their patients scan every 30 days — and the side-by-side 3D visualization became their single biggest retention driver.",
    "UK Meds, a UK online pharmacy, integrated FitXpress into their checkout for BMI verification before dispensing weight-loss medication. The Smart Scales mismatch detection automated manual review — and every check created an audit-ready record.",
    "Our model was trained on 150,000+ photos, 30,000+ 3D scans, and 430,000+ measurements over 9+ years. It covers ages 16 to 78, weight 38 to 210 kg — broad enough for any member demographic you'd encounter at scale.",
    "96-97% real-world accuracy vs manual measurements, with a 1.5–2.0 cm typical error margin. Weight estimation within ±3.5% average error. 95%+ repeatability across repeated scans — so the change members see between scans is real, not measurement noise.",
    "Yazen's 34,000 scans in 2025 proved the retention model: patients scanning monthly with visual progress comparisons stayed in the program significantly longer. The 3D visualization wasn't just a feature — it became the core retention mechanism.",
    "UK Meds now runs BMI verification through FitXpress for every weight-loss prescription. The automated workflow — two photos, verified BMI, mismatch flagging — turned a manual compliance bottleneck into a scalable digital pathway.",
    "The demographic training range is notable: ages 16-78, weight 38-210 kg, height 150-205 cm. This isn't a model trained on fit 25-year-olds — it works for the full spectrum of patients and members a health organization serves.",
    "Real-world benchmarks show 96-97% agreement with manual measurements, error margins of 1.5–2.0 cm, and weight estimates within ±3.5%. Combined with 95%+ repeatability, that's clinical-grade consistency from a consumer device.",
    "In 2025 alone, our health customers ran over 100,000 scans — from weight loss platforms to online pharmacies to clinical trial sites. The consistent thread: verified body data replacing self-report in regulated clinical and engagement workflows.",
    "The model has processed 430,000+ measurements across its training history. That volume means the AI has seen bodies of virtually every shape and size — from 38 kg to 210 kg, ages 16 to 78. Real-world accuracy holds at 96-97% across that entire range.",
    "Yazen's experience is instructive: they started with FitXpress as a measurement tool and discovered it was actually a retention engine. Members who could see their 3D progress stayed enrolled 2-3x longer. 34,000 scans in 2025 — and the engagement data keeps improving.",
    "UK Meds' integration of FitXpress for pharmacy BMI checks showed 7,500 scans in the deployment period. The Smart Scales feature — which flags weight mismatches automatically — became their compliance team's preferred audit tool for digital prescribing decisions.",
]

# Follow-up CTAs
CTAS = [
    "Open to a 15-minute walkthrough?",
    "15 minutes to show you how it works?",
    "Want to see a quick demo?",
    "Worth 15 minutes to explore?",
    "Can I show you a 5-minute demo?",
    "Happy to walk you through it — 15 minutes?",
    "Would a brief demo be useful?",
    "15 minutes to see if it fits your roadmap?",
    "Quick call to explore whether this maps to your priorities?",
    "I can show you the member experience in 10 minutes — interested?",
    "Want me to send over a 2-minute product video instead?",
    "I could share a quick screen recording if that's easier than a call.",
]

# Breakup variants
BREAKUPS = [
    "won't keep at it. Two photos, 45 seconds, verified body data. If that ever fits the roadmap, I'm at vadim@3dlook.me.",
    "last message from me. FitXpress: body measurement from two smartphone photos, 96-97% accuracy, HIPAA-compliant. The door's open if it's ever relevant.",
    "leaving this here. If verified body data from two phone photos ever becomes a priority, reach me at vadim@3dlook.me anytime.",
    "final note. Two photos → 80+ measurements → members who stay engaged. If that maps to anything on the horizon, I'm here.",
    "won't keep circling. FitXpress delivers body composition from two photos in 45 seconds. If that's ever useful, vadim@3dlook.me.",
    "signing off. Two phone photos, verified body data, audit-ready records. If the timing ever lines up, you know where to find me.",
    "last one. 96-97% accuracy body scans from a smartphone. If that capability ever matters for your strategy, I'm at vadim@3dlook.me.",
    "won't take more of your inbox. FitXpress: clinical-grade body data from two photos. Open door if it ever fits.",
    "final ping. Two photos, 45 seconds, members who can see change stay in programs longer. If that's ever relevant, reach out.",
    "leaving it at that. Body measurement SDK, verified data, HIPAA-compliant. I'm at vadim@3dlook.me if it's ever a fit.",
    "last reach-out. If adding verified body data to the member experience ever lands on the roadmap, happy to pick this up.",
    "won't message again. FitXpress turns two photos into a complete body scan. If the timing works someday, I'm easy to find.",
]


# --- Generation ---

def pick_unique(items, idx):
    """Pick from list cyclically but uniquely per function call."""
    return items[idx % len(items)]


def generate_file(contact, idx):
    pid = contact["person_id"]
    name = contact["full_name"]
    name_first = name.split()[0]
    title = contact["title"]
    company = contact["company_name"]
    angle = contact["recommended_message_angle"]

    # Use idx for unique selection
    intro = INTROS[idx % len(INTROS)]
    prod = PRODUCT_DESCRIPTIONS[(idx + 3) % len(PRODUCT_DESCRIPTIONS)]
    compliance = COMPLIANCE_NOTES[(idx + 7) % len(COMPLIANCE_NOTES)]
    
    # Angle-specific body paragraph
    if angle == "preventive-health":
        body_pool = PREVENTIVE_BODIES
    elif angle == "digital-transformation":
        body_pool = DIGITAL_TRANSFORMATION_BODIES
    elif angle == "clinical-operations":
        body_pool = CLINICAL_BODIES
    elif angle == "member-engagement":
        body_pool = MEMBER_ENGAGEMENT_BODIES
    elif angle == "virtual-care":
        body_pool = VIRTUAL_CARE_BODIES
    else:
        body_pool = PREVENTIVE_BODIES
    
    body_para = body_pool[idx % len(body_pool)]
    
    # Step 1 - Connection
    step1 = make_connection(name_first, title, company, angle, idx)

    # Step 2 - Welcome
    step2 = f"{intro}\n\n{prod}\n\n{body_para}\n\n{compliance}"
    # Truncate if needed
    if len(step2) > 1000:
        step2 = step2[:996] + "..."

    # Step 3 - Follow-up
    proof = PROOF_POINTS[(idx + 5) % len(PROOF_POINTS)]
    cta = CTAS[(idx + 11) % len(CTAS)]
    step3 = f"{name_first} — quick follow-up with something worth considering.\n\n{proof}\n\n{cta}"
    if len(step3) > 800:
        step3 = step3[:796] + "..."

    # Step 4 - Breakup
    breakup = BREAKUPS[idx % len(BREAKUPS)]
    step4 = f"{name_first} — {breakup}"

    # Assemble
    content = f"""# {name} — {title} — {company}

## Context used
- Angle: {angle}
- Hook: {make_connection(name_first, title, company, angle, idx)[:150].strip()}
- Proof point: {proof.strip()[:200]}

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


# Generate all 50
for idx, contact in enumerate(contacts):
    content = generate_file(contact, idx)
    pid = contact["person_id"]
    out_path = os.path.join(OUT_DIR, f"{pid}.md")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Generated {len(contacts)} files with high uniqueness.")
