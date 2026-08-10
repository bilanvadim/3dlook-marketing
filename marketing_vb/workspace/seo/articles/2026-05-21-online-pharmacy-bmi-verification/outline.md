---
track: seo
product: fitxpress
stage: plan
target_keyword: online pharmacy BMI verification
secondary_keywords:
  - GLP-1 photo verification
  - prevent BMI photo manipulation
  - live photo capture pharmacy
  - AI photo fraud detection
audience: Online pharmacy operators and telehealth platform leaders (UK first, US second); clinical and compliance teams
reader_action: Understand the problem, see the verification standard, request a FitXpress demo
length_target_words: 1500-2000
status: approved
created: 2026-05-21
approved: 2026-05-21
approval_notes:
  - UK Meds — reference as live customer only, no metrics (per case-study confidentiality)
  - Regulators — general formulations only (GPhC UK / FDA US scrutiny); no invented clauses
  - CTA — demo only; drop the 200-request free trial mention
---

# SEO Plan — online-pharmacy-bmi-verification

## 1. Keyword analysis

- **Intent:** Mixed informational + commercial. The primary keyword "online pharmacy BMI verification" reads like a buyer researching how to solve a compliance/fraud problem they already know they have. Commercial intent grows once "AI photo fraud detection" and "live photo capture pharmacy" enter the query.
- **SERP shape (expected):** Compliance/legal explainers (GPhC, MHRA, FDA-adjacent), telehealth thought-leadership posts, and a few vendor pages from competitors (Prism Labs, Bodygram). Few pages combine the regulatory pressure narrative with a concrete verification standard — that gap is where we win.
- **Where 3DLOOK wins:** We can credibly speak to (a) the photo-manipulation experiment narrative Katerina has already established publicly, (b) a working customer in this exact use case (UK Meds), and (c) the workflow/audit posture (HIPAA, GDPR, retention, audit-ready logs). Competitors usually stop at "we measure body" — we frame the answer as a verification standard plus a trusted workflow layer.
- **Geo angle:** UK-first language (GPhC, online weight-loss prescribing scrutiny) with US secondary (FDA monitoring, telehealth weight-loss platforms). UK Meds case anchors the UK story.
- **Position in funnel:** Mid-funnel education that ends in a demo CTA — not a feature page, not a generic explainer.

## 2. Title options

1. **(Recommended) How Online Pharmacies Verify BMI Without Manipulated Photos: A 2026 Compliance Guide**
   - Rationale: Hits target keyword in first six words, signals the year (freshness), and pairs the buyer's pain (manipulated photos) with what they actually buy (compliance). Direct, no buzzwords.
2. **Online Pharmacy BMI Verification in the Age of AI-Generated Photos**
   - Rationale: Strong topical match, but slightly soft on the buyer outcome — reads as commentary, not a guide. Good fallback if a shorter title is preferred.
3. **BMI Verification for Online Pharmacies: Why Photo Uploads No Longer Pass Audit**
   - Rationale: Sharpest pain framing, strong for CTR among compliance leads. Less explicit on the "what to do about it" promise, which we want present for demo conversion.

## 3. Outline

Target total: ~1,750 words.

### H2.1 — The problem: BMI verification by photo upload has stopped working
- ~250 words
- Key arguments:
  - Self-reported weight + uploaded photo is still the default eligibility gate for online weight-loss prescribing.
  - Patients are now manipulating photos with free AI tools before submitting them — pharmacy clinical teams are flagging this as a recurring issue, not an edge case.
  - The verification method, not patient behaviour, is what's broken.
- Secondary keywords: "online pharmacy BMI verification", "prevent BMI photo manipulation"
- Sources: `brand-assets/past-posts/linkedin-personal/katerina-galich/2026-03-27-patients-gaming-the-system-fitxpress.md` (UK pharmacy teams flagging manipulation); `brand-assets/product-info/use-cases/fx-online-pharmacy-bmi.md` (self-reported weight is the status quo)

### H2.2 — Why it's getting worse: AI made fake evidence cheap
- ~280 words
- Key arguments:
  - Generative tools can produce a convincing "before" body image in seconds — Katerina's own experiment with ChatGPT and Gemini produced two different but plausible fake bodies from one real photo.
  - The deeper issue isn't editing — it's that file uploads have no provenance: no capture time, no liveness, no proof the photo belongs to the patient submitting it.
  - Regulators (UK GPhC scrutiny of online weight-loss prescribing; US FDA monitoring) are circling the same gap.
- Secondary keywords: "GLP-1 photo verification", "AI photo fraud detection"
- Sources: `brand-assets/past-posts/linkedin-personal/katerina-galich/2026-03-31-i-ran-an-experiment-fake-bmi-photos.md` (the experiment narrative); `brand-assets/past-posts/linkedin-personal/katerina-galich/2026-04-09-bmi-checks-not-just-glp1-thing.md` (no-provenance argument); `brand-assets/product-info/use-cases/fx-online-pharmacy-bmi.md` (regulator pressure)

### H2.3 — Why "upload two photos" was never built for this
- ~220 words
- Key arguments:
  - A camera-roll upload assumes good-faith behaviour and reviewer time — neither is realistic at scale.
  - Manual photo review can't catch a well-edited image; clinicians cannot reliably distinguish a generated body from a real one at a glance.
  - When eligibility for a regulated medication depends on what's in that file, the audit defence "we looked at the photo" no longer holds up.
- Secondary keywords: "prevent BMI photo manipulation", "online pharmacy BMI verification"
- Sources: `brand-assets/past-posts/linkedin-personal/katerina-galich/2026-04-09-bmi-checks-not-just-glp1-thing.md` (upload has no provenance); `brand-assets/past-posts/linkedin-personal/katerina-galich/2026-03-27-patients-gaming-the-system-fitxpress.md` (clinical risk framing)

### H2.4 — What real BMI verification needs to look like in 2026
- ~360 words
- Format: Short intro + checklist (mirrors Katerina's bullet style).
- Key arguments (the checklist):
  - **Live, in-session photo capture** — images taken inside the verification flow, not pulled from the camera roll.
  - **Liveness and pose checks** — confirm a real person is on camera, in the right posture, in real time.
  - **Clothing detection** — flag oversized or baggy attire used to inflate visual BMI.
  - **AI-derived weight and body data** — replace subjective photo review with a measured estimate that can be compared to self-reported weight.
  - **Audit-ready evidence** — timestamped capture, pass/fail outcomes, exportable logs that a regulator or internal compliance team can review.
- Secondary keywords: "live photo capture pharmacy", "AI photo fraud detection", "prevent BMI photo manipulation"
- Sources: `brand-assets/past-posts/linkedin-personal/katerina-galich/2026-04-09-bmi-checks-not-just-glp1-thing.md` (full checklist origin); `brand-assets/product-info/how-it-works.md` (pose validation, clothing detection, face obfuscation); `brand-assets/product-info/tech-spec.md` (clothing classification sport/regular/oversized, Smart Scales mismatch flag)

### H2.5 — How FitXpress applies this standard inside the pharmacy order flow
- ~400 words
- Key arguments:
  - **Where it sits:** a 2-photo scan triggered as a verification step inside the order/checkout flow, with results consumed server-side (Pattern B) so body metrics never need to be exposed to the patient.
  - **What it returns:** BMI plus 80+ measurements derived from the scan, with results in under 45 seconds.
  - **Anti-manipulation layer:** capture happens through the SDK (pose/tilt validation, in-session, not camera-roll); clothing detection classifies fit type; Smart Scales cross-checks self-reported weight against the AI estimate and flags mismatch.
  - **Compliance posture for UK/US pharmacy buyers:** HIPAA-maintained for US healthcare contexts, GDPR-aligned for UK/EU; AWS S3 with SSE-S3 encryption; photos deleted immediately or within 30 days per client policy; auto-blurred when stored; no personal identifiers processed.
  - **Live customer:** UK Meds runs FitXpress as the BMI verification step in their order flow.
- Secondary keywords: "online pharmacy BMI verification", "live photo capture pharmacy"
- Sources: `brand-assets/product-info/use-cases/fx-online-pharmacy-bmi.md`; `brand-assets/product-info/case-studies/uk-meds.md` (Pattern B, server-side validation, audit trail); `brand-assets/product-info/how-it-works.md` (capture flow, Smart Scales, 45 sec); `brand-assets/product-info/tech-spec.md` (Pattern B detail, clothing classification); `brand-assets/product-info/compliance.md` (HIPAA/GDPR, SSE-S3, retention, blurring, no PII); `brand-assets/product-info/proof-points.md` (UK Meds reference, 80+ measurements, <45 sec)

### H2.6 — What a pharmacy compliance team should ask any verification vendor
- ~220 words
- Format: Short evaluation checklist for buyers (8 questions max).
- Key arguments (sample questions):
  - Is capture in-session, or can the patient upload from their camera roll?
  - Do you produce timestamped, exportable evidence for audit?
  - How do you flag oversized clothing or posture inflation?
  - Do you cross-check self-reported weight against an independent estimate?
  - Where is data stored, how long, and under what encryption?
  - Will you sign a BAA (US) and confirm GDPR alignment (UK/EU)?
- Secondary keywords: "online pharmacy BMI verification", "AI photo fraud detection"
- Sources: `brand-assets/product-info/compliance.md` (buyer questions section, BAA, retention, SSE-S3); `brand-assets/product-info/how-it-works.md` (capture flow details); `brand-assets/product-info/tech-spec.md` (clothing classification, Smart Scales)

### H2.7 — Closing + CTA: See FitXpress inside an order flow
- ~120 words
- Key arguments:
  - One-paragraph recap: the problem is the method, not the patient; the answer is in-session capture plus auditable evidence.
  - Direct CTA to request a FitXpress demo for online pharmacy BMI verification, with UK Meds as the live reference.
  - Single demo CTA only. Do NOT mention the 200-request free trial (compliance-buyer tone — they need a conversation, not self-serve testing).
- Secondary keywords: "online pharmacy BMI verification"
- Sources: `brand-assets/product-info/use-cases/fx-online-pharmacy-bmi.md` (hero message)

## 4. Style notes (Katerina voice calibration)

- **Open with a flat declarative line, not a setup.** Mirror the "I ran an experiment that kept me up at night" or "In the past few weeks, I've had the same conversation…" pattern. No "in today's fast-paced world" lead-in.
- **Short paragraphs, sometimes single sentences.** Katerina lets a one-line claim stand alone for emphasis ("This isn't a workflow problem. It's a clinical verification problem."). We'll use that rhythm at section transitions.
- **Checklists with concrete verbs, not abstract benefits.** The "Live photo upload stops X. Clothing detection flags Y" pattern from the 2026-03-27 and 2026-04-09 posts becomes the template for H2.4 and H2.6.
- **Name the uncomfortable truth, then offer the method.** Don't soften ("Photos can sometimes be misleading"); state plainly ("If your eligibility gate is a camera-roll upload, you're not verifying BMI") and then walk to the standard.
- **Banned-signature discipline:** no rhetorical em-dash construction ("X — это не просто Y"), no "leverage/utilize/harness/robust/seamless/comprehensive", no "Furthermore/Moreover" sentence starters, no "It's not just X, it's Y", no triple parallelism like "fast, reliable, scalable". The brand-checker pass will enforce this before publish.

## 5. Missing facts

None — proceeding with available facts.

Two soft notes for the section-writer stage (not blockers):
- Specific regulator citations (e.g., exact GPhC guidance section, FDA monitoring memo) are not in the source files. The writer should reference regulatory pressure in general terms ("UK GPhC scrutiny of online weight-loss prescribing", "US FDA monitoring") as the use-case file does, without inventing specific clauses.
- UK Meds-specific outcome metrics (e.g., fraud caught, drop-off change) are intentionally not to be disclosed per the case-study file. Reference UK Meds only as the live customer using FitXpress for BMI verification.
