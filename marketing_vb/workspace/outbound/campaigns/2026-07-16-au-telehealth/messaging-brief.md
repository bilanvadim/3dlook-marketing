# Messaging Brief — 2026-07-16-au-telehealth

> Read this FIRST before writing any messages. All proof points, tone rules, and banned words are consolidated here.

## Product
**FitXpress** — AI-powered body measurement from 2 smartphone photos. 80+ measurements + body composition in <45 seconds.

## Hero message for this campaign
**Verify body progress remotely to boost retention, reduce drop-off, and prove program ROI.**

## Target audience
Australian health insurers (Medibank, Bupa, HCF) and digital health/telehealth platforms (Mosh, InstantScripts, Medmate, Qoctor).

## Proof points — USE ONLY THESE NUMBERS

### Accuracy
- 96-97% accuracy vs manual measurements in real-world benchmarks
- 1.5–2.0 cm typical error margin
- Weight estimation ±3.5% average error
- 95%+ repeatability across repeated scans

### Scale & training
- 9+ years of training data: 150,000+ photos, 30,000+ 3D scans, 430,000+ measurements
- Demographic coverage: ages 16-78, weight 38-210 kg, height 150-220 cm (corrected 2026-09-02)

### Customer evidence
- **Yazen** — 34,000 scans in 2025, weight loss patient progress tracking
- **UK Meds** — 7,500 scans, BMI verification for online pharmacy dispensing
- 100+ customers all-time, 67 active, $1.084M ARR

### Compliance (MUST mention in step 2 or 3 for health audiences)
- HIPAA-compliant, follows GDPR principles
- Encryption: TLS in transit, AWS S3 SSE-S3 at rest (always on)
- Photos: deleted immediately after processing or within 30 days per client policy
- Zero personal identifiers processed — body data only

### What FitXpress delivers
- 2 photos (front + side) → 80+ body measurements
- Body composition: BMI, BMR, fat %, lean mass, fat mass
- 3D model + side-by-side progress visualization
- Smart Scales: detects self-reported weight mismatch (anti-fraud)
- Audit-ready records for regulated workflows

## Tone — Vadim's voice
- Direct, peer-to-peer, no corporate fluff
- Data-driven but not academic
- Focus on business outcomes, not technology
- Formal enough for C-Level at insurers, direct enough for founders at digital health platforms

## BANNED WORDS — NEVER USE
leverage, utilize, harness, robust, seamless, comprehensive, delve, navigate (metaphorical), tapestry, realm, "game-changer", "revolutionary", "disrupt"

## Anti-positioning — DO NOT
- Lead with "most accurate body scanning"
- Say "AI-powered" without a concrete outcome
- Use "I help companies like yours..."
- Use generic openers: "I hope this finds you well", "I came across your profile", "I noticed you work at..."
- Invent numbers not in proof points above
- Repeat the same text across different people (aim for 60%+ uniqueness)

## Message structure (4 steps, LinkedIn)

### Step 1 — Connection request (Day 0, ≤300 chars)
Hook ONLY. Get the connection. NO selling. Reference something specific about their role/company.

### Step 2 — Welcome (Day 3, after acceptance, ≤1000 chars)
Introduce + problem we solve + 1 specific resonance point. Include compliance mention for health audiences.

### Step 3 — Follow-up (Day 7, ≤800 chars)
One specific proof point + soft CTA (15 min call).

### Step 4 — Breakup (Day 14, ≤400 chars)
"Won't keep bothering you, leaving this here" + last value share.

## Message angles
- **digital-transformation** → focus on how FitXpress integrates into existing telehealth/digital health stack
- **preventive-health** → focus on member engagement, preventive care programs, health outcomes
- **member-engagement** → focus on retention, NPS, member experience
- **clinical-operations** → focus on workflow efficiency, clinical governance, audit trail
- **compliance** → focus on HIPAA/GDPR, audit-ready records, regulatory alignment
- **virtual-care** → focus on remote care delivery, telehealth integration
- **weight-management** → focus on GLP-1/weight loss programs, body composition tracking

## Yazen case study (use for telehealth/weight loss angles)
"Yazen, a European weight loss platform, uses FitXpress for member progress tracking — 34,000 scans in 2025. Their patients scan every 30 days, and the side-by-side 3D visualization is their #1 retention feature."

## UK Meds case study (use for compliance/pharmacy angles)
"UK Meds, a UK online pharmacy, integrated FitXpress into their checkout flow for BMI verification before dispensing weight-loss medication. The Smart Scales feature flags self-reported weight mismatches automatically — cutting manual review time and keeping the audit trail regulator-ready."

## Key phrases to use
- "verified body data" (not "accurate measurements")
- "audit-ready records"
- "real-world accuracy"
- "longitudinal progress tracking"
- "member engagement and retention"
- "two photos, 45 seconds"

## Output format per person
File: messages/{person_id}.md
```markdown
# {full_name} — {title} — {company_name}

## Context used
- Angle: {recommended_message_angle}
- Hook: {specific connection point}
- Proof point: {what we'll cite}

---

## Step 1 — Connection request (Day 0)
{message}

**Char count:** XXX / 300

## Step 2 — Welcome (Day 3)
{message}

**Char count:** XXX

## Step 3 — Follow-up (Day 7)
{message}

**Char count:** XXX

## Step 4 — Breakup (Day 14)
{message}

**Char count:** XXX
```

## Also produce
messages/_summary.md with stats: total people, total messages, avg char counts, angle distribution, 5 random samples for Vadim review.
