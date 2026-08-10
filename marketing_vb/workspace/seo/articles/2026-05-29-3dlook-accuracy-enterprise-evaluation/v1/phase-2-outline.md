---
phase: 2_outline
article: 2026-05-29-3dlook-accuracy-enterprise-evaluation
date: 2026-05-29
status: awaiting_approval_before_phase_3
parent_phases: [phase-1-data-audit.md, phase-1b-pdf-reverify.md]
---

# Phase 2 — Outline (10 H2 + 5 H3 dimensions)

This outline is execution-ready for Phase 3 writing. Every H2 lists: purpose, vetted numbers used (item # from `phase-1-data-audit.md`), required hedge patterns, and internal links.

---

## 0. Applied decisions + guardrail outcomes (consolidated)

### 5 decisions from Vadim (applied)

1. **PDFs accessible** — all 6 read; vetted numbers re-confirmed (see `phase-1b-pdf-reverify.md`).
2. **Smart Scales positioning** — framed as a **weight-estimation aid, not a replacement for a calibrated scale**. Cite MAE 2.1 kg and 3.11% relative error. **No explicit "beta"** language; described as a distinct output from measurement accuracy. Avoid "scale replacement" claims.
3. **H2.7 comparison framing** — "different methodologies, different purposes." DEXA = "dual-energy X-ray attenuation imaging"; InBody = "bioelectrical impedance analysis (BIA)"; smart scales = "impedance-based estimation"; manual = "anthropometric tape measurement". **No "better/best/more accurate than"** claims. Never name a competitor product negatively.
4. **NCSU framing** — **public verification successful**. Use: *"Through a 2022 partnership with North Carolina State University's Wilson College of Textiles (publicly listed funding-partner project on NCSU's 3D Body Scanning research page), 3DLOOK's training dataset was expanded with ground-truth scans from the university's body scanning lab."* The word **"partnership"** is justified. **NEVER** use "validated by NCSU" or "peer-reviewed" (no published research yet on this collaboration).
5. **Disclaimer** — full 5-sentence accuracy-adapted disclaimer block from brief, verbatim, no compression.

### 2 guardrails (applied)

- **96-97% denominator** — found in Feb 2025 PDF. Use stronger attribution: *"On 3DLOOK's internal validation benchmark — a real-world dataset of multiple customer scan events with five repeated scans per person, compared against expert pattern-maker manual measurements — measurement accuracy is approximately 96–97% across body metrics, with a typical absolute error margin of 1.5–2.0 cm."* Yurii priority for #9 downgraded from HIGH to MEDIUM.
- **NCSU public verification** — done. See decision #4.

### 3 re-verify discrepancies (resolved)

- Item #17: **"80+ anatomical parameters"** (Tech May 2025 framing, newer). Yurii confirm list.
- Item #15: **"3D model generated in under 30 seconds; full capture-to-results pipeline in under 45 seconds."**
- Item #11: **3.5% headline; ±3% as alternate framing in Smart Scales context.**

### April 2023 ISO benchmark — selected for H2.2 Dimension 5 ONLY

One paragraph in D5 referencing the ISO 8559-1:2017 multi-company benchmark (14 companies, 8 countries, 1,152 data points, 3D scanner reference): 3DLOOK session-to-session repeatability **0.40 cm**, the lowest of three methods tested (manual experts 0.94 cm; hardware 3D scanners 0.57 cm). **Do NOT mix with Feb 2025 accuracy numbers** (different references). Frame as a near-independent validation signal.

---

## 1. Article-level metadata

| Field | Value |
|-------|-------|
| Title (working) | How Accurate Is 3DLOOK? An Enterprise Evaluation Framework |
| Slug | 3dlook-accuracy-enterprise-evaluation |
| Product tag | `fitxpress` primary (Mobile Tailor secondary in H2.2 D4 use-case row) |
| Author | Assel Sekerova (per CLAUDE.md §15 default) |
| Target audience | VP Product / Chief Medical Officer / Head of Underwriting / VP Operations evaluating 3DLOOK |
| Reading level | Technical-but-accessible; assume buyer has heard of DEXA and BIA |
| Target length | 3,500–4,500 words |
| Required disclaimer | Full 5-sentence accuracy-adapted block, verbatim, before FAQ |

---

## 2. H2 outline

### H2.1 — What enterprise buyers should actually evaluate

**Purpose.** Frame the article. Open with the observation that "is it accurate?" is the wrong first question for an enterprise buyer. Five dimensions matter together: measurement accuracy, repeatability, real-world robustness, output breadth, validation strength. Set up the rest of the article as the answer to that framing.

**Vetted numbers used.** None directly — pure framing.

**Hedge patterns.** Soft setup ("different buyers, different priorities"). No specific performance claims yet.

**New material used.** None.

**Internal links.** Forward link to H2.2 (the five dimensions). Forward link to H2.10 (decision checklist).

**Length.** ~300 words.

---

### H2.2 — The five dimensions of measurement quality (5 H3 subsections)

**Purpose.** The article's spine. Each dimension gets one H3, with the relevant numbers and hedge.

**Length.** ~1,200 words total across 5 H3s.

---

#### H3 — D1: Measurement Accuracy

**Purpose.** Define accuracy. Give the 96-97% number with full methodology. Show the per-body-part error table (the strongest single piece of evidence in the article).

**Vetted numbers.** #9 (96-97% accuracy), #1–4 (dataset scope as methodology context), #5 (US/Europe), #6 (age/height/weight ranges as scope disclosure).

**Required hedge pattern.** Use the strong attribution sentence from Section 0 guardrails. Add scope-disclosure sentence: *"Demographic scope of the internal validation dataset: ages 16–78, heights 150–205 cm, weights 38–210 kg, US and Europe; this is the population the accuracy figure was measured against — not a universal 'works for everyone' claim."*

**Tables/figures.** **Per-body-part error table** (from Feb 2025 PDF p.5):

| Body part | Absolute error (cm) | Tier |
|-----------|----------------------|------|
| Wrist girth | 0.54 | <1 cm |
| Calf | 1.27 | <2 cm |
| Neck | 1.48 | <2 cm |
| Thigh | 1.64 | <2 cm |
| Back shoulder width | 1.72 | <2 cm |
| Knee | 1.73 | <2 cm |
| Chest | 1.74 | <2 cm |
| Waist height | 1.74 | <2 cm |
| Bicep | 1.85 | <2 cm |
| Back neck point to waist | 2.09 | 2–2.5 cm |
| Waist | 2.14 | 2–2.5 cm |
| Inside leg height | 2.21 | 2–2.5 cm |
| Hip | 2.25 | 2–2.5 cm |
| Back neck height | 2.37 | 2–2.5 cm |

Note above table: *"Source: 3DLOOK internal validation against expert pattern-maker manual measurements (Feb 2025). Five repeated scans per person across multiple real-world customer scan events."*

**Internal links.** → H2.4 (full dataset methodology); → H2.5 (repeatability deep dive).

**Length.** ~400 words including table.

---

#### H3 — D2: Repeatability

**Purpose.** Define repeatability (scan-to-scan consistency for the same person). Show why it matters more than headline accuracy for longitudinal use cases (weight tracking, before-after comparisons, multi-month underwriting).

**Vetted numbers.** #10 (>95% repeatability, variance <1 cm across repeated scans).

**Required hedge pattern.** *"Internal repeatability testing across five repeated scans per person, on a real-world customer dataset, shows scan-to-scan consistency above 95%, with a variance of less than 1 cm across repeated scans."*

**New material used.** Brief reference forward to H2.5 (per-body-part variance chart).

**Internal links.** → H2.5 (deep dive).

**Length.** ~200 words.

---

#### H3 — D3: Real-World Robustness

**Purpose.** What happens when the user is wearing a sweater, in poor lighting, standing slightly off-axis. The reliability features that catch problems before they produce bad measurements.

**Vetted numbers.** #21 (varied capture conditions in Photo Flow Simulation), #28 (real-time skeletal tracking), #31 (AI clothing detection: sport/regular/oversized), #32 (garment-aware shape estimation corrections).

**Required hedge pattern.** Factual product description, present tense (these are in production as of May 2026 per Tech May 2025 roadmap dates and Vadim's confirmation).

**Internal links.** → H2.9 (full production reliability features).

**Length.** ~250 words.

---

#### H3 — D4: Output Breadth (Use-Case Fit)

**Purpose.** Different verticals need different outputs. Show the use-case comparison table mapping 3DLOOK outputs to six target verticals.

**Vetted numbers.** #16 (80+ measurements), #22–24 (BMI/BMR/Body Fat).

**Tables/figures.** **Use-case comparison table** (6 rows):

| Vertical | Primary 3DLOOK output | Why it matters | Limitation to disclose |
|----------|-------------------------|----------------|--------------------------|
| Telehealth / weight-loss (GLP-1, coaching apps) | BMI from height + estimated weight; longitudinal scan-to-scan progress; body composition trends | Verified BMI without requiring user to own a scale; progress visualization drives adherence | Not a clinical diagnosis; not a replacement for calibrated bioimpedance or DEXA |
| Online pharmacy / digital prescriber | BMI verification at intake or refill | Anti-fraud check vs self-reported weight; eligibility screening | Designed for screening, not standalone clinical determination |
| Life & disability underwriting | BMI + waist circumference + body fat estimate | Faster underwriting decisions; remote intake without lab visit | Internal validation only — not a replacement for medical exam where required |
| Made-to-measure apparel | 80+ body measurements with girth + linear dimensions | Reduces remakes and returns; remote measuring at scale | Typical absolute error 1.5–2.5 cm per measurement (see D1) — pattern-makers should account for this in tolerance |
| Uniform / PPE / workwear | Subset of girth + length measurements relevant to garment block | Measurement consistency across a distributed workforce | Same per-measurement tolerance |
| Clinical trials / DCT screening | Body composition trends as a secondary endpoint | Decentralized measurement at low burden | Not third-party validated; not peer-reviewed; not a primary clinical endpoint |

**Required hedge pattern.** Each row's "Limitation to disclose" column is non-optional — keep all six.

**Internal links.** → H2.6 (body composition outputs in depth); → H2.7 (where 3DLOOK fits among other methods).

**Length.** ~350 words including table.

---

#### H3 — D5: Validation Strength

**Purpose.** Be honest about what validation exists and what doesn't. Three pillars: (1) 3DLOOK's internal validation benchmark (Feb 2025 study); (2) the ISO 8559-1:2017 multi-company benchmark from 2022/2023; (3) the 2022 NCSU partnership for dataset enrichment.

**Vetted numbers.** #25 (NCSU 2022 partnership), #10 (>95% repeatability).

**New material used.** **ISO benchmark supporting paragraph:** *"In a separate ISO 8559-1:2017 multi-company benchmark involving 14 companies, 8 countries, 27 participants, 72 subjects, and 1,152 data points (3D scanner average as the reference), 3DLOOK's session-to-session repeatability was 0.40 cm — the lowest of the three measurement methods compared in that study (manual experts: 0.94 cm; hardware 3D scanners: 0.57 cm)."* Note: this is a near-independent validation signal but uses a different reference than the Feb 2025 study — call this out plainly.

**Required hedge pattern.** The "legal-defense-grade" line from the audit: *"Where direct comparative validation against a specific reference method has not been completed, 3DLOOK should not be positioned as equivalent to that method."* Then the NCSU framing: *"Through a 2022 partnership with North Carolina State University's Wilson College of Textiles (publicly listed funding-partner project on NCSU's 3D Body Scanning research page), 3DLOOK's training dataset was expanded with ground-truth 3D scans from the university's body scanning lab. This was dataset enrichment work — not third-party validation."*

**What NOT to claim.** "Validated by NCSU." "Peer-reviewed." "Clinically validated." "DEXA-equivalent" / "InBody-equivalent." "Third-party validated" (the ISO benchmark is 3DLOOK-led, not third-party-led, so this term is also off-limits).

**Internal links.** → H2.4 (dataset and ground-truth methodology); link out to NCSU public projects page.

**Length.** ~400 words.

---

### H2.3 — How the 3DLOOK pipeline actually works

**Purpose.** Explain the four-step mechanism: photo capture → body detection under clothing → 3D model generation → measurement extraction. Make it concrete enough that an engineering-aware buyer can map it to their workflow.

**Vetted numbers.** #14 (two-photo guided capture, any background, fully clothed), #15 (3D model in under 30 seconds; full pipeline under 45 seconds), #16 (80+ measurements).

**New material used.** *"3DLOOK's mobile body scanning is powered by a proprietary statistical generative human body model — a different approach from traditional 3D reconstruction methods that depend on depth sensors or structured-light hardware."* Also: **patented body shape segmentation** (Tech May 2025 p.3 explicitly labels this as patented).

**Required hedge pattern.** Factual product description; cite "patented" only with reference to the patented body shape segmentation, not the broader product.

**Internal links.** → H2.4 (how the model was trained); → H2.9 (real-time pipeline reliability features).

**Length.** ~400 words.

---

### H2.4 — Ground-truth dataset and validation methodology

**Purpose.** The dataset behind the model. Scope, demographics, ground-truth capture setup, NCSU enrichment, photo flow simulation.

**Vetted numbers.** #1–7 (dataset scope), #17 (80+ anatomical parameters per participant — **UPDATED from 86**), #18 (4 dynamic cameras), #19 (34 photo configurations per user), #20 (over 1 million polygons with 1mm accuracy per ground-truth 3D model), #21 (variations: distance, angle, slope, lighting), #25–27 (NCSU).

**Required hedge pattern.** Every internal-scope number prefaced with "in 3DLOOK's proprietary dataset" or "in 3DLOOK's internal validation dataset". NCSU framed exactly as in decision #4.

**New material used.** NCSU public verification — include hyperlink: [NCSU Wilson College of Textiles 3D Body Scanning Projects](https://3dbodyscan.textiles.ncsu.edu/projects/). This is the single external-credibility link in the whole article.

**Internal links.** ← H2.2 D1, D5; → H2.5.

**Length.** ~500 words.

---

### H2.5 — Repeatability and per-body-part stability

**Purpose.** Go deeper on repeatability than D2 did. Show that "repeatability" is not a single number — it varies per body part, with girth measurements like wrist, knee, ankle being the most stable, and waist + soft-tissue areas being the most variable.

**Vetted numbers.** #10 (>95% repeatability).

**New material used.** Per-body-part repeatability variance summary (from Feb 2025 PDF pp.10–13). Recommend a short bullet-list of categories rather than reproducing every chart:

- **Most stable (variance ≤0.15 cm):** ankle, wrist, calf, knee, neck-side-to-chest, chest-to-waist (side linear), shoulder-width, neck linear.
- **Stable (variance 0.15–0.5 cm):** chest girth, neck girth, bicep, hip, mid-thigh, abdomen.
- **Moderate (variance 0.5–1.0 cm):** waist, low hips, waist-middle, waist-lower, bust height, upper hip height, back-neck-point-to-wrist length, total crotch length.
- **Higher variance (>1.0 cm):** overarm girth, certain long-vertical measurements influenced by posture.

Plus the ISO benchmark line from D5 (0.40 cm session-to-session average across 11 ISO measurements — keep it brief here since the full context is in D5).

**Required hedge pattern.** "Internal testing indicates..." Avoid presenting the bullet-list as a precise per-measurement table; this is summary categorization, not the underlying chart.

**Internal links.** ← H2.2 D2; → H2.6 (Smart Scales repeatability is tighter than measurements).

**Length.** ~350 words.

---

### H2.6 — Body composition outputs (BMI, BMR, Body Fat, Smart Scales)

**Purpose.** Each body composition output, with its formula, scope, hedge, and the limitation to disclose. Smart Scales gets its own subsection clearly framed as estimation aid.

**Vetted numbers.** #11 (avg weight prediction error 3.5%, ±3% margin), #12 (Smart Scales MAE 2.1 kg, SD 1.49, relative error 3.11%), #13 (BMI 89% accuracy, 76% within 5% deviation), #22 (BMI formula), #23 (Mifflin-St Jeor for BMR), #24 (U.S. Navy formula for Body Fat).

**Required hedge patterns.**
- BMI: standard formula citation. Reference 89% / 76%-within-5% with: *"Internal testing of BMI calculated from estimated weight."*
- BMR: standard Mifflin-St Jeor citation.
- Body Fat: the audit's exact hedge — *"3DLOOK uses the U.S. Navy formula for body fat percentage estimation, selected through internal comparative evaluation of established anthropometric methods."* **No specific MAE numbers** for Brozek/Navy comparison (PDF data error, see audit exclusion N1).
- Smart Scales: *"Smart Scales is a weight-estimation aid that calculates body weight from two photos using volume-density modeling. Internal testing shows mean absolute error of 2.1 kg, mean relative error of 3.11%. It is designed as an aid where a calibrated scale is unavailable or impractical — not as a replacement for one in clinical or compliance contexts where calibrated weight is required."*

**New material used.** Brief mention of Smart Scales formula: *"Weight is estimated by summing per-segment volume × calibrated density coefficients, derived from 3DLOOK's internal ScanLab dataset."* Smart Scales algorithm formula (Σ V_i × ρ_i) can be referenced without writing out the equation.

**Internal links.** → H2.7 (how this compares to DEXA / InBody / smart scales).

**Length.** ~500 words.

---

### H2.7 — Where 3DLOOK fits among body-measurement methods

**Purpose.** Honest positioning. 3DLOOK is not DEXA. Not InBody. Not a calibrated scale. Each method exists for different reasons. Frame as: "different methodologies serve different purposes."

**Vetted numbers.** None directly.

**New material used.** *"Published evaluations of mobile body measurement systems typically report waist-circumference error in the 1.5–2.2 cm range; 3DLOOK's internal validation places it at the lower end of that range."* (Lifted from Feb 2025 PDF's "aligning with top industry standards for mobile body scanning (1.5–2.2 cm error range)" framing — but phrased as a general industry observation, not a competitive claim.)

**Method positioning (no "better/best"):**
- **DEXA** = dual-energy X-ray attenuation imaging; clinical gold standard for body composition, requires specialized equipment, ionizing radiation, in-clinic visit.
- **InBody / similar** = bioelectrical impedance analysis (BIA); fast, in-clinic or in-pharmacy, sensitive to hydration state.
- **Smart scales (consumer)** = impedance-based estimation through the feet; convenient daily measurement, not designed for clinical decisions.
- **Manual measurement** = trained anthropometrist with tape; gold standard for circumferences when done by certified personnel, has its own session-to-session variability.
- **3DLOOK mobile scanning** = vision-based body measurement from two smartphone photos; designed for remote, repeated, longitudinal use at scale, with measurement output suited to workflow integration.

**Required hedge pattern.** Each method described in its own terms, no comparative superlatives. Close with: *"Where a study or protocol requires direct comparative validation against a specific reference method (e.g., DEXA), 3DLOOK should not be positioned as equivalent to that method."*

**Internal links.** → H2.6 (body composition outputs).

**Length.** ~500 words.

---

### H2.8 — Compliance, privacy, and governance

**Purpose.** What the buyer's compliance team will want to know — answered upfront.

**Vetted numbers.** #34 (HIPAA), #35 (GDPR), #36 (TLS), #37 (AWS S3 SSE-S3 always on), #38 (photo deletion immediate or 30 days), #39 (auto-blur on retained photos), #40 (no personal identifiers processed), #41 (images never shared with third parties), #42 (privacy@3dlook.me).

**New material used.** **Verbatim line from Aug 2025 Security PDF:** *"Since FitXpress does not provide medical advice, diagnosis, or treatment recommendations, medical device certifications do not apply."* Frame as a deliberate positioning choice: the workflow layer is intentionally not a medical device, so medical-device certifications are not the relevant compliance framework.

**Required hedge pattern.** Standard product framing. Direct disclosure.

**Structure suggestion.** Short Q&A format mirroring the Aug 2025 slide layout — five questions: storage, encryption, deletion, photo retention, HIPAA/GDPR. Plus a sixth Q&A on the medical-device-framework positioning.

**Internal links.** → H2.10 (compliance questions in the checklist).

**Length.** ~450 words.

---

### H2.9 — Production reliability features

**Purpose.** The "in production today" reliability layer that catches problems before they produce bad measurements. Frames 3DLOOK as a workflow-aware product, not just a model.

**Vetted numbers.** #28 (AI-driven skeletal tracking with real-time pose validation), #29 (red/green marker visual feedback), #30 (voice prompts for posture correction), #31 (AI clothing detection: sport/regular/oversized), #32 (garment-aware shape estimation corrections), #33 (face obfuscation).

**New material used.** **Cross-platform compatibility:** Android + iOS, older devices to current models (Tech May 2025 p.14). **"Mobile-first and hardware-free"** positioning line. Note that pose detection went into production in 2025 per the Tech Presentation roadmap — and that's why these are present-tense features today, not future roadmap items.

**Required hedge pattern.** Factual product description.

**Internal links.** ← H2.2 D3; → H2.10 checklist Q7.

**Length.** ~400 words.

---

### H2.10 — Enterprise evaluation checklist

**Purpose.** Eight questions a serious enterprise buyer should ask any body scanning vendor — with how 3DLOOK answers each, briefly. The checklist gives the article practical re-use value beyond the read itself.

**Vetted numbers.** All applicable (references back to earlier sections).

**The 8 questions:**

1. **What reference method was used to measure accuracy, and what is the typical error margin?** → 3DLOOK: expert pattern-maker manual measurements; 1.5–2.0 cm typical absolute error; per-body-part table in D1.
2. **How is repeatability measured, and over how many sessions?** → Five repeated scans per person; >95% repeatability; variance <1 cm; per-body-part breakdown in H2.5.
3. **What real-world conditions has the system been tested under?** → 34 photo configurations per user in dataset training (distance, angle, slope, lighting); production-time AI clothing detection, pose validation, and lighting adaptability — see H2.9.
4. **What outputs does the vendor produce, and how do they map to my use case?** → 80+ measurements + BMI/BMR/Fat %/Lean & Fat Body Mass; use-case mapping table in D4.
5. **What external validation exists, and what is its scope?** → 2022 NCSU partnership for dataset enrichment (publicly listed funding-partner project); ISO 8559-1:2017 multi-company benchmark with 0.40 cm session-to-session repeatability; **not** peer-reviewed, **not** third-party validated, **not** clinically certified.
6. **What is the data privacy and compliance posture?** → HIPAA-maintained, GDPR principles, TLS + SSE-S3, immediate or 30-day photo deletion, no personal identifiers processed, auto-blur on retained photos — see H2.8.
7. **What catches a bad scan before it becomes a bad measurement?** → Real-time AI-driven skeletal tracking with red/green marker feedback and voice prompts; AI clothing detection (sport/regular/oversized) with garment-aware shape correction; face obfuscation — see H2.9.
8. **What is explicitly outside the scope of this product?** → Medical advice, diagnosis, or treatment recommendations; medical device certifications (intentionally not pursued — framework does not apply); DEXA/InBody equivalence; peer-reviewed clinical validation.

**Required hedge pattern.** Direct Q&A. Each answer ends with a section link.

**Length.** ~500 words including the eight Q&A items.

---

## 3. Disclaimer (verbatim from brief)

Place after H2.10 and before FAQ. Use the brief's 5-sentence accuracy-adapted disclaimer block in full, no compression. Phase 3 writer: do not edit this block; copy it verbatim from the brief.

---

## 4. FAQ — 9 hedged Q&A

Schema-ready, each answer 2–4 sentences, every performance number hedged per Section 4 hedge inventory in `phase-1-data-audit.md`.

1. **Is 3DLOOK clinically validated?** No. 3DLOOK is not clinically validated, not peer-reviewed, not third-party validated, and not classified as a medical device. Internal validation against expert pattern-maker manual measurements shows approximately 96–97% measurement accuracy and >95% repeatability — see H2.2 D1 and D2.
2. **Is 3DLOOK comparable to DEXA?** No. DEXA is dual-energy X-ray attenuation imaging and serves as a clinical reference standard for body composition. 3DLOOK is a mobile vision-based measurement system designed for remote, repeated, longitudinal use. Different methodologies, different purposes — see H2.7.
3. **Is 3DLOOK comparable to InBody or bioimpedance scales?** No. BIA (including InBody) measures body composition via electrical impedance and is sensitive to hydration state. 3DLOOK estimates body composition from body shape using the U.S. Navy formula and is designed for a different operational context — see H2.6 and H2.7.
4. **Can 3DLOOK replace a calibrated scale?** No. Smart Scales is a weight-estimation aid (internal MAE 2.1 kg, relative error 3.11%) intended for contexts where a calibrated scale is unavailable or impractical, not as a replacement for one where calibrated weight is required — see H2.6.
5. **What is the typical measurement error margin?** 1.5–2.0 cm typical absolute error per body part, with per-body-part variation from 0.54 cm (wrist) to 2.37 cm (back neck height) on 3DLOOK's internal validation benchmark — see H2.2 D1 for the full table.
6. **Has the technology been peer-reviewed or third-party validated?** No peer-reviewed publication is on record specific to 3DLOOK's accuracy claims. The 2022 NCSU partnership is dataset enrichment work, not independent validation. The ISO 8559-1:2017 multi-company benchmark (3DLOOK 0.40 cm session-to-session repeatability) is 3DLOOK-led, not third-party-led — see H2.2 D5.
7. **Does 3DLOOK work for every body type / age / ethnicity?** 3DLOOK's internal validation dataset covers ages 16–78, heights 150–205 cm, weights 38–210 kg, US and Europe, with multi-ethnic and multi-occupation metadata. This is the disclosed population the measurement quality figures were measured against — not a "works for everyone" claim. For populations outside this scope (children, certain mobility constraints, etc.), use cases should be evaluated separately.
8. **Is patient data HIPAA-compliant?** Yes. FitXpress maintains HIPAA compliance and follows GDPR principles. All data is encrypted in transit (TLS) and at rest (AWS S3 SSE-S3, always on). Photos are deleted immediately or within 30 days per client policy; any retained photos are auto-blurred. Personal identifiers are not processed — see H2.8.
9. **Why no medical device certification?** "Since FitXpress does not provide medical advice, diagnosis, or treatment recommendations, medical device certifications do not apply." 3DLOOK is intentionally positioned as a workflow and data layer, not a medical device — see H2.8.

---

## 5. Internal link map (within the article)

| From | To | Anchor purpose |
|------|----|-----------------|
| H2.1 | H2.2 | "the five dimensions are explained below" |
| H2.1 | H2.10 | "evaluation checklist for buyers" |
| H2.2 D1 | H2.4 | "full dataset methodology" |
| H2.2 D1 | H2.5 | "repeatability deep dive" |
| H2.2 D2 | H2.5 | "per-body-part variance" |
| H2.2 D3 | H2.9 | "production reliability features in full" |
| H2.2 D4 | H2.6 | "body composition outputs in detail" |
| H2.2 D4 | H2.7 | "how 3DLOOK fits among methods" |
| H2.2 D5 | H2.4 | "NCSU dataset enrichment" |
| H2.2 D5 | external | NCSU 3D Body Scanning Projects page |
| H2.3 | H2.4 | "how the model was trained" |
| H2.3 | H2.9 | "real-time pipeline features" |
| H2.4 | H2.5 | "repeatability deep dive" |
| H2.6 | H2.7 | "method comparison" |
| H2.8 | H2.10 | "compliance questions in the checklist" |
| H2.9 | H2.10 | "checklist Q7" |

---

## 6. External link map

| Link | Anchor text suggestion | Where |
|------|--------------------------|-------|
| https://3dbodyscan.textiles.ncsu.edu/projects/ | "publicly listed funding-partner project on NCSU's 3D Body Scanning research page" | H2.2 D5 and H2.4 |
| `privacy@3dlook.me` (mailto) | Contact for data deletion requests | H2.8 + footer |

No other external links. No links to competitor products. No links to academic studies that aren't 3DLOOK's own.

---

## 7. Internal cross-links to existing 3DLOOK content

Per CLAUDE.md §15 Blog Authoring Standards, link to past articles where natural:

| When mentioning | Suggested cross-link |
|-----------------|------------------------|
| Insurance / underwriting use case in H2.2 D4 | [mobile-body-scanning-insurance-underwriting](existing article) |
| Wellness rewards / employer angle | [wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning](existing article) |
| Comparison framing in H2.7 | [body-scanning-technology-comparison](existing article) — but do NOT import competitor benchmark numbers (per audit exclusion N10) |
| General "what is 3DLOOK" framing in H2.1 or H2.3 | [3dlook-turns-two-photos-structured-body-data](existing article) |

Phase 3 writer: insert these 4 internal cross-links naturally; do not force.

---

## 8. Yurii-confirm list at time of publish (updated)

| Priority | Item | Why |
|----------|------|------|
| **MEDIUM** (downgraded from HIGH) | #9 96-97% accuracy | Confirmed in Feb 2025 PDF; Yurii should confirm this remains the current internally-documented figure as of late 2025/2026 |
| MEDIUM | #10 >95% repeatability | Same |
| MEDIUM | #12 Smart Scales MAE 2.1 / 3.11% | Confirm if Smart Scales framing is still "estimation aid" vs explicit "beta" |
| MEDIUM | #13 BMI 89% / 76% within 5% | Confirm same test cohort |
| MEDIUM | **#17 — 80+ anatomical parameters** (changed from 86) | New per Tech May 2025; confirm this is correct framing |
| LOW | #11 weight prediction 3.5% vs ±3% | Both numbers in latest PDF; confirm we should lead with 3.5% |
| LOW | Dataset scope numbers (#1–4) | Confirm current as of 2026 (may have grown) |
| LOW | Demographics (#6) | Confirm ranges have not changed |

Surface this updated list back to Vadim in Phase 5 (final compliance / metrics check).

---

## 9. Article-level checklist before Phase 3

- [ ] All numbers in the article appear in `phase-1-data-audit.md` Section 1 OR are derived purely from re-verify Section 1 (96-97% methodology).
- [ ] Every internal performance number sits inside a hedge pattern from `phase-1-data-audit.md` Section 4.
- [ ] No banned phrasings (leverage / harness / robust / seamless / etc. per CLAUDE.md §6).
- [ ] NCSU never appears with the word "validated"; "partnership" wording matches Section 0 decision #4 verbatim.
- [ ] Per-body-part table includes the methodology footer.
- [ ] Smart Scales described as estimation aid, not replacement.
- [ ] Disclaimer block verbatim and full-length.
- [ ] FAQ Q&A all 2–4 sentences with section links.

---

## 10. Open for Vadim's approval

- 10 H2 + 5 H3 structure
- Per-body-part error table (H2.2 D1) — 14 rows
- Use-case comparison table (H2.2 D4) — 6 rows
- ISO benchmark line in H2.2 D5
- Decision checklist (H2.10) — 8 questions
- FAQ — 9 Q&A (one more than minimum 8)
- 4 internal cross-links to past articles
- 1 external link (NCSU projects page)
- Updated Yurii-confirm list

Awaiting your OK to proceed to Phase 3 (full draft).
