---
phase: 1b_pdf_reverify
article: 2026-05-29-3dlook-accuracy-enterprise-evaluation
date: 2026-05-29
status: awaiting_vadim_ok_before_applying_5_decisions
parent_phase: phase-1-data-audit.md
---

# Phase 1b — PDF Re-verification of the Audit

This re-checks every number in `phase-1-data-audit.md` against the 6 PDFs now sitting in `source-materials/`. It flags confirmations, discrepancies, and new material the original audit could not see.

---

## 0. PDFs read

| # | File | Date | Pages | Role |
|---|------|------|-------|------|
| 1 | Comprehensive Datasets and Precision Metrics May 2024.pdf | May 2024 | 10 | Original dataset + body comp methodology |
| 2 | 3DLOOK Accuracy_and_Repeatability_Analysis (1).pdf | April 2023 (Apr 23 file date, study date older) | 26 | **NEW — multi-company industry benchmark study** |
| 3 | 3DLOOK_Accuracy and Repeatabilty 2_26_2025 (2).pdf | February 2025 | 19 | **NEW — gives the 96-97% denominator** |
| 4 | 3DLOOK Technology Presentation May 2025.pdf | April–May 2025 | 15 | Latest tech overview |
| 5 | Updated Security_Privacy Slide 8_13_2025.pdf | August 2025 | 1 | Compliance/security |
| 6 | _Intro to FitXpress by 3DLOOK Health and Fitness Sept 2025.pdf | September 2025 | 36 | FitXpress product overview |

---

## 1. THE BIG ANSWER: what does "96-97% accuracy" actually mean?

**FOUND** — the Feb 2025 PDF spells out the denominator. From p.19 (Conclusion slide), verbatim:

> "3DLOOK's AI-powered body measurement technology demonstrates approximately **96-97% accuracy when compared to manual measurements across all body metrics, with a typical error margin of 1.5–2.0 cm**.
>
> For repeatability, the technology shows over **95% consistency, with a variance of less than 1 cm across repeated scans**, ensuring high stability and reliability across the full range of body measurements.
>
> This data comes from a **real-world study utilizing multiple customer scan events, benchmarked against expert manual measurements** to assess consistency and precision, ensuring that results are reflective of actual use cases rather than controlled lab conditions."

### Methodology unpacked (Feb 2025 PDF, pp.2–17)

- **Reference (ground truth):** Multiple sets of manual measurements taken by **expert pattern makers** (not 3D scanner ground truth).
- **Dataset structure:** Multiple real-world customer scan events; each person undergoing **five repeated scans** for repeatability analysis.
- **Measurement categories:** Front linear, side linear, volume/circumference.
- **Per-body-part absolute error (Feb 2025 PDF p.5 chart):** Wrist 0.54 cm; Calf 1.27 cm; Neck 1.48 cm; Thigh 1.64 cm; Knee 1.73 cm; Chest 1.74 cm; Waist height 1.74 cm; Back shoulder width 1.72 cm; Bicep 1.85 cm; Back neck point to waist 2.09 cm; Waist 2.14 cm; Inside leg height 2.21 cm; Hip 2.25 cm; Back neck height 2.37 cm.
- **Repeatability per body part (Feb 2025 PDF p.10 chart):** girth variance 0.11–1.29 cm; linear variance 0.04–0.77 cm. Median well under 1 cm.
- **Limitations acknowledged in the PDF itself:** "Different people may measure the same body part differently, introducing variability" — i.e., even the manual reference has noise.

### How to phrase "96-97%" in the article

Recommended attribution sentence (uses the PDF's own language):

> "On 3DLOOK's internal validation benchmark — a real-world dataset of multiple customer scan events with five repeated scans per person, compared against expert pattern-maker measurements — measurement accuracy is approximately 96–97% across body metrics, with a typical absolute error margin of 1.5–2.0 cm."

This is **stronger than the original audit** could have written, because we now have the dataset description and per-body-part error range to back it up. The 96-97% is no longer a bare claim — it sits inside a described methodology.

**Note on the per-body-part chart:** the Feb 2025 chart is itself an **article asset** — a comparison table (or simple list) of absolute error per body part is one of the strongest things we can show without revealing anything not already in 3DLOOK's own deck. Recommended for H2.5.

### Yurii priority adjustment

Original audit had #9 (96-97%) at **HIGH priority for Yurii** because no denominator was available. With the Feb 2025 PDF in hand, this drops to **MEDIUM** — Yurii still needs to confirm this is the current internally-documented figure as of late 2025/2026 (the methodology may have moved on since Feb 2025), but it's no longer a structural risk.

---

## 2. The OTHER bonus PDF — April 2023 multi-company benchmark study

This was **not on the original brief's vetted-numbers list**. It is a different study entirely and needs careful handling.

### What it is

A 2022/2023-era industry benchmark study run by 3DLOOK ("ACCURACY AND REPEATABILITY OF HUMAN BODY MEASURING ANALYSIS"). Key figures (PDF p.2):

- 4 measuring days
- 8 measuring stations
- 14 companies participated
- 27 participants from 8 countries
- 72 subjects measured
- 1,152 data points gathered
- 11 ISO 8559-1:2017 compatible body measurements

**Reference (ground truth) was different:** the average of 3D scanner measurements — NOT manual measurements. So the resulting accuracy/repeatability numbers are NOT directly comparable to the Feb 2025 study.

### Headline results (PDF p.16)

| Method | Accuracy vs 3D scanner reference | Repeatability (avg session-to-session diff) |
|--------|----------------------------------|---------------------------------------------|
| 3DLOOK | 2.54 cm | **0.40 cm** |
| Experts (manual) | 1.56 cm | 0.94 cm |
| 3D scanners | (reference) | 0.57 cm |

The headline story of this study: **3DLOOK is the most repeatable of the three** (manual experts being the least repeatable on waist and crotch length specifically), while being less accurate than experts when measured against the 3D scanner average.

### What to do with this PDF

**Option A (recommended): do NOT use the 2.54 cm number** in the article. Reason: it uses a different reference (3D scanner average) than the Feb 2025 study (manual), and mixing them would confuse readers and weaken the cleaner Feb 2025 story.

**Option B (consider): use the 0.40 cm repeatability number** as an additional supporting data point. It's consistent with the Feb 2025 "variance of less than 1 cm" claim and adds methodological richness. Frame as: "in a separate ISO 8559-1:2017 multi-company benchmark study with a 3D-scanner reference, 3DLOOK's session-to-session repeatability was 0.40 cm — the lowest of the three measurement methods compared (manual experts, hardware 3D scanners, mobile)." Optional — depends on whether we want to bring multiple studies in.

**Option C (skip entirely):** Treat this PDF as out-of-scope; only use the Feb 2025 PDF and the May 2025 Tech Presentation as the article's data spine. Simplest.

I am inclined to **Option A + maybe Option B as a single optional supporting line in H2.5** — the 0.40 cm number is impressive and adds breadth without dragging an entire second methodology into the article. Flagging for your call.

### One more thing worth noting from this PDF

P.5 (Understanding Accuracy and Repeatability) has a nice didactic dartboard visual explaining accuracy vs repeatability. Could be referenced or replicated as an article diagram if Yurii green-lights using this PDF.

---

## 3. Vetted numbers re-verification — line by line

Status: ✅ confirmed by PDFs / ⚠ discrepancy noted / 🟨 confirmed with nuance.

### A. Dataset scope (items #1–8)

| # | Original audit | PDF check | Status |
|---|----------------|-----------|--------|
| 1 | 5,000+ participants | May 2024 PDF p.2 confirms "5000+ participants" | ✅ |
| 2 | 150,000+ photographs | May 2024 p.2; Tech May 2025 p.6 both confirm | ✅ |
| 3 | 30,000+ 3D scans | Same — both confirm | ✅ |
| 4 | 430,000+ measurements | Same — both confirm | ✅ |
| 5 | US/Europe geography | Both PDFs confirm | ✅ |
| 6 | Age 16–78, height 150–205 cm, weight 38–210 kg | Both PDFs confirm exactly | ✅ |
| 7 | Gender 48% / 52% | Both PDFs confirm | ✅ |
| 8 | "Nearly a decade of R&D" | Tech May 2025 p.9 says "nearly a decade of R&D" verbatim. Tech May 2025 p.14 ALSO says "9 years of R&D". FitXpress Sept 2025 p.3 says "9+ years". So both "nearly a decade" and "9 years" exist in 3DLOOK's own materials. Audit's preferred phrasing "nearly a decade" is the safer evergreen choice. | ✅ |

### B. Performance metrics (items #9–13)

| # | Original audit | PDF check | Status |
|---|----------------|-----------|--------|
| 9 | Measurement accuracy 96–97% | Tech May 2025 p.10 + Feb 2025 p.19 + FitXpress Sept 2025 p.12. **Denominator now known** (see Section 1). | ✅ stronger than before |
| 10 | Repeatability >95% across scan sessions | Same three PDFs confirm with consistent phrasing | ✅ |
| 11 | Avg weight prediction error 3.5% (±3% margin) | Tech May 2025 p.10 says "Average Weight Prediction Error: 3.5%". Tech May 2025 p.13 says "±3% average error margin under ideal and real world conditions". **Both numbers present, slightly different framings.** | 🟨 — recommend use 3.5% as the headline and note ±3% as alternate framing |
| 12 | Smart Scales MAE 2.1 kg, SD 1.49, rel error 3.11% | May 2024 p.9 confirms exactly. Also: **SD of Relative Error 2.45%** (NOT in audit — bonus number). PDF explicitly labels Smart Scales as "in beta" in May 2024. | ✅ + new SD of relative error available |
| 13 | BMI 89% accuracy, 76% within 5% deviation | Tech May 2025 p.10 confirms exactly | ✅ |

### C. Methodology specifics (items #14–21)

| # | Original audit | PDF check | Status |
|---|----------------|-----------|--------|
| 14 | Two-photo guided capture, any background, fully clothed | Tech May 2025 p.3 + FitXpress Sept 2025 p.3 confirm | ✅ |
| 15 | ~30 second 3D model generation | Tech May 2025 p.3 says "less than 30 seconds" (for 3D model generation). FitXpress Sept 2025 p.3 says "under 45 seconds" (for full data output: BMI+BMR+Fat%+masses+80+ measurements). **These describe different things** — 3D model gen alone vs full pipeline including computed metrics. | ⚠ — recommend article uses: "3D model generation in under 30 seconds; full body data output in under 45 seconds" |
| 16 | 80+ body measurements | Both PDFs confirm. Tech May 2025 p.4 lists ~80 specific measurement names. | ✅ |
| 17 | 86 anatomical parameters per person | May 2024 p.3 says "86 different parameters per person" (older PDF). Tech May 2025 p.7 (newer) says "80+ anatomical parameters per person" — softened. FitXpress Sept 2025 p.7 uses 86 (reproduces May 2024 slide). | ⚠ Discrepancy — newer doc reduced to "80+". Recommend article matches Tech May 2025: "80+ anatomical parameters per participant". Add to Yurii list. |
| 18 | 4 dynamic cameras | Both confirm | ✅ |
| 19 | 34 photo configurations per user | Both confirm | ✅ |
| 20 | 1 million polygons with 1 mm accuracy per 3D model | Tech May 2025 p.7 confirms "over 1 million polygons with 1mm accuracy for each 3D model". May 2024 p.3 used different framing: "over 5 million points for each 3D model". Points and polygons are different metrics (a polygon = multiple points), so both can be true simultaneously. **Use the newer Tech May 2025 framing** — audit was correct. | ✅ |
| 21 | Varied capture conditions (distance/angle/slope/lighting) | Both confirm | ✅ |

### D. Body composition framework (items #22–24)

| # | Original audit | PDF check | Status |
|---|----------------|-----------|--------|
| 22 | BMI formula | May 2024 p.8 confirms | ✅ |
| 23 | BMR Mifflin-St Jeor | May 2024 p.8 confirms | ✅ |
| 24 | Body Fat %: U.S. Navy formula | May 2024 pp.5–6 confirm. **Critical: May 2024 p.5 labels U.S. Navy formula as "a scientifically validated method"** — this is 3DLOOK's own 2024 wording, but per Vadim and the brief we **deliberately do NOT echo "scientifically validated"** in the article. Use the safer "selected through internal comparative evaluation of established anthropometric methods" instead. | ✅ confirmed — keep audit's hedge |

**Brozek vs Navy comparison error (audit's exclusion N1) — CONFIRMED as a real PDF error:**
May 2024 p.6 shows identical numbers for BOTH formulas — Brozek: MAE 12.91%, SD 9.37%; Navy (Males): MAE 12.91%, SD 9.37%; Navy (Females): MAE 12.91%, SD 9.37%. The numbers are clearly duplicated rather than distinct, so the slide cannot support a "Navy is more accurate" claim with specific numbers. Audit was right to exclude these.

### E. NCSU academic partnership (items #25–27)

| # | Original audit | PDF check | Status |
|---|----------------|-----------|--------|
| 25 | NCSU / Wilson College of Textiles, 2022 | **Tech May 2025 p.8 explicitly says "(North Carolina State University, 2022)"** — the year is in the title of the slide. May 2024 p.4 has the partnership but without a year. Audit's framing is fully backed by internal docs. | ✅ — year is in writing |
| 26 | Both casual and tight-fitting clothing | Both PDFs confirm | ✅ |
| 27 | Multi-ethnic, multi-occupation metadata | Both PDFs confirm metadata collected: Height, Weight, Age, Gender, Ethnicity, Occupation | ✅ |

**One nuance:** the NCSU slides describe the partnership as "to facilitate the enhancement of 3DLOOK's dataset and measurement accuracy" — i.e., dataset enhancement, not validation. The brief's hedge ("never 'validated by NCSU'") remains correct.

**Public verification of the NCSU partnership via web search:** still TBD. Per your instruction, this is a guardrail to run before applying decision #4. Recommend running it as the first step after your OK on this re-verify.

### F. Real-world reliability features (items #28–33)

All six features confirmed in production-ready language by Tech May 2025:

| # | Feature | PDF location | Status |
|---|---------|---------------|--------|
| 28 | AI-driven skeletal tracking with real-time pose validation | Tech May 2025 p.11 ("Automated Posture Validation for Scan Precision") | ✅ — but see nuance below |
| 29 | Red/green marker visual feedback | Tech May 2025 p.11 verbatim | ✅ |
| 30 | Voice prompts for posture correction | Tech May 2025 p.11 verbatim | ✅ |
| 31 | AI clothing detection (sport / regular / oversized) | Tech May 2025 p.12 verbatim | ✅ |
| 32 | Garment-aware shape estimation corrections | Tech May 2025 p.12 | ✅ |
| 33 | Face obfuscation for privacy | Tech May 2025 p.11; Aug 2025 Security PDF | ✅ |

**Nuance on items #28–32 production status:** Tech May 2025 p.11 says pose detection was "currently being implemented into production est May 2025". Tech May 2025 p.12 says updated clothing detection models were "coming Q3 2025". By **today (May 2026)** both have been past their planned production dates for ~6–12 months, so the audit's present-tense framing is justified. The original audit noted "Vadim confirmed" — that remains good guidance and should be re-confirmed once before publish.

### G. Compliance (items #34–42)

The Aug 2025 Security/Privacy slide and the FitXpress Sept 2025 deck (p.34, verbatim same slide) confirm every compliance bullet in the audit:

- HIPAA compliance maintained for US healthcare contexts ✅
- GDPR principles followed ✅
- TLS encryption in transit + AWS S3 SSE-S3 at rest (always on, cannot be disabled) ✅
- Photo deletion: immediate or within 30 days per client policy ✅
- Automatic blur on any retained photos ✅
- No personal identifiers processed; images never shared with third parties ✅
- `privacy@3dlook.me` for data deletion requests ✅

One verbatim line worth lifting into the article (Aug 2025 slide):

> "Since FitXpress does not provide medical advice, diagnosis, or treatment recommendations, medical device certifications do not apply."

This is an excellent disclosure for the H2.8 governance section — it gets ahead of the question "is this medical-grade?" by directly explaining why medical device certifications are not in scope. Recommend using this line near the disclaimer.

---

## 4. New material the original audit did not have access to

Beyond confirming numbers, these are net-new facts/phrases the PDFs give us:

1. **Per-body-part absolute error chart (Feb 2025 PDF p.5)** — 14 measurements with values from 0.54 cm (wrist) to 2.37 cm (back neck height). Strong material for the comparison/breakdown section.
2. **Per-body-part repeatability variance (Feb 2025 PDF pp.10–13)** — girth, front linear, side linear. Can support a "where the measurements are most/least stable" section.
3. **"Aligning with top industry standards for mobile body scanning (1.5–2.2 cm error range)"** (Feb 2025 PDF p.7) — useful for H2.7 (3DLOOK in context of the broader body scanning landscape) WITHOUT bashing competitors.
4. **Smart Scales algorithm explanation** (May 2024 p.9) — Weight = Σ(V_i × ρ_i) for all body parts, where ρ_i is "average density" calibrated from 3DLOOK's ScanLab dataset. Adds methodological credibility to H2.3 if we want to go one layer deeper.
5. **"Statistical generative human body model"** (Tech May 2025 p.2) — the canonical phrase for what powers 3DLOOK. Use this exact phrasing in H2.1 and again in H2.4.
6. **Patented body shape segmentation** (Tech May 2025 p.3) — explicitly labeled as patented; we can say "patented" without overreach.
7. **"Mobile-first and hardware free"** (Tech May 2025 p.14) — positioning line worth borrowing.
8. **Cross-platform compatibility** — Android + iOS, older + newest devices (Tech May 2025 p.14). Useful for the H2.10 deployment/integration checklist.
9. **Body composition outputs grouping (Tech May 2025 p.5)**: BMI, BMR, Fat %, Lean Body Mass, Fat Body Mass, Smart Scale Validation. Note the Tech May 2025 framing is "Smart Scale **Validation**" — softer than "Smart Scales" as a standalone product. This supports your decision #2 (treat as "estimation aid").
10. **Industry benchmark context: 14 companies, 8 countries, 11 ISO 8559-1:2017 measurements** (April 2023 study) — optional supporting material if we want to use that PDF.
11. **Mifflin-St Jeor formula for BMR** (May 2024 p.8) is the explicit citation for the BMR equation, which we can call out by name in H2.3.
12. **The verbatim "medical device certifications do not apply" disclaimer line** (Aug 2025 slide) — for H2.8.

---

## 5. Summary table — what changed vs original audit

| Change category | Items affected | Action |
|-----------------|----------------|--------|
| ✅ Fully confirmed by PDFs | Items 1–7, 9–14, 16, 18, 19, 21–33, 34–42 | No action — use as planned |
| 🟨 Confirmed with nuance | Item 8 ("nearly a decade" vs "9 years" — both exist); Item 11 (3.5% vs ±3% — both exist); Item 15 (30 sec model gen vs 45 sec full output — different things) | Article should clarify scope when the number appears |
| ⚠ Discrepancy needing decision | Item 17 (86 → 80+) | Recommend match newest doc: "80+ anatomical parameters"; ask Yurii |
| 🆕 Denominator now known | Item 9 (96-97% accuracy) | Use stronger attribution; downgrade Yurii priority from HIGH → MEDIUM |
| 🆕 New bonus material | Per-body-part error chart, repeatability variance chart, Smart Scales formula, statistical generative body model phrasing, patented framing, medical-device disclaimer line, industry benchmark study | Incorporate into outline; optional vs core to be decided in Phase 2 |
| 🟰 Vadim's exclusions still hold | N1 (Brozek/Navy MAE numbers) — confirmed PDF error; N2–N10 unchanged | Keep all exclusions |
| 🌐 Public verification still needed | Item 25 (NCSU partnership being externally verifiable) | Web search before Phase 2 outlines NCSU mentions |

---

## 6. Recommendations / open questions for you before applying the 5 decisions

1. **April 2023 benchmark study (the bonus PDF):** A / B / C above. I lean A + one supporting line in H2.5 referencing the 0.40 cm repeatability. Your call.
2. **Item 17 (86 vs 80+ parameters):** I recommend the newer "80+ anatomical parameters" framing; mark for Yurii. OK?
3. **Item 15 (30s vs 45s):** I recommend stating both with their scope ("3D model in under 30 seconds; full body data output in under 45 seconds"). OK?
4. **Per-body-part error chart from Feb 2025:** I recommend reproducing it in H2.5 (either as a table or selected highlights — Wrist 0.54, Calf 1.27, Neck 1.48, Waist 1.74, Hip 2.25 etc.). This is the single strongest piece of evidence in the article. OK to include?
5. **"Medical device certifications do not apply" verbatim line:** I recommend including it in H2.8. OK?
6. **NCSU web search:** I will run this as the very first step after your OK on this re-verify — outcome determines whether decision #4 keeps the word "partnership" or switches to softer phrasing.

---

**Status: ready for your OK to apply the 5 decisions + 2 guardrails, then Phase 2 outline.**
