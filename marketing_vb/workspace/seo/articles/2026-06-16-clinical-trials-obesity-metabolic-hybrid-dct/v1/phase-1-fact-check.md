---
phase: 1_pre_writing_fact_check
article: 2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct
date: 2026-06-16
status: awaiting_vadim_approve_before_phase_2
brief_source: Vadim brief 2026-06-16 (Use Case — Clinical Trials Metabolic/Obesity incl. Hybrid/DCT)
target_keyword: clinical trial anthropometric measurement software
length_target: 3,500–4,200 (FX use-case sweet spot, per default)
external_sources_verify_status: 3 of 3 verified live
editorial_guardrails_applied: brand-assets/style-guides/editorial-guardrails.md (11-point checklist)
---

# Phase 1 — Pre-writing fact-check

## 1. External sources verified (3 of 3)

All three sources confirmed via direct web search; URLs return live documents.

### 1a. FDA Digital Health Technologies guidance — VERIFIED

- **Document:** *Digital Health Technologies for Remote Data Acquisition in Clinical Investigations; Guidance for Industry, Investigators, and Other Stakeholders*
- **Status:** **Final guidance**, issued December 22, 2023 (finalized the December 23, 2021 draft)
- **Primary URL:** https://www.fda.gov/regulatory-information/search-fda-guidance-documents/digital-health-technologies-remote-data-acquisition-clinical-investigations
- **Federal Register URL:** https://www.federalregister.gov/documents/2023/12/22/2023-28262/digital-health-technologies-for-remote-data-acquisition-in-clinical-investigations-guidance-for
- **Covers (relevant to article):**
  - DHT selection suitability for clinical investigations
  - Verification and validation ("fit-for-purpose")
  - Use of DHTs to collect data for trial endpoints
  - Risk identification and management
  - Data retention and protection
  - Sponsor and investigator roles
- **Safe framing supported by source:**
  - "DHTs for remote data acquisition" — direct phrase from guidance title
  - "Fit-for-purpose verification and validation"
  - "Sponsor responsibilities for DHT selection and risk management"
  - Important nuance: the guidance says when a DHT meets the device definition and is **used only for remote data collection** in a clinical investigation, and the sponsor demonstrates fit-for-purpose, **FDA does not intend to assess design-controls compliance**. This is the safer regulatory framing — we are NOT claiming FitXpress is FDA-approved or device-cleared; we are referencing the FDA's framework for how DHTs fit into trials.

### 1b. ICH E6(R3) Good Clinical Practice — VERIFIED

- **Document:** *ICH Harmonised Guideline: Guideline for Good Clinical Practice E6(R3)*
- **Status:** **Step 4 / Final**, dated 2025-01-06; FDA adopting per Sidley Austin December 2025 update
- **Primary URL (ICH database):** https://database.ich.org/sites/default/files/ICH_E6(R3)_Step4_FinalGuideline_2025_0106.pdf
- **EMA Step 5 URL:** https://www.ema.europa.eu/en/documents/scientific-guideline/ich-e6-r3-guideline-good-clinical-practice-gcp-step-5_en.pdf
- **EMA overview page:** https://www.ema.europa.eu/en/ich-e6-good-clinical-practice-scientific-guideline
- **Covers (relevant to article):**
  - Essential documents and records requirements
  - Source records, audit trails, metadata
  - Data integrity, traceability, security
  - Sponsor and investigator responsibilities
  - Quality-by-design principles
  - Proportionality of process and risk-mitigation strategies
- **Safe framing supported by source:**
  - "ICH E6(R3) GCP framework" — direct attribution
  - "Essential records requirements (source records, audit trails, metadata)"
  - "Data integrity and traceability expectations"
  - **Critical for FitXpress positioning:** E6(R3) explicitly requires policies ensuring data integrity, traceability, and security. FitXpress can be positioned as **supporting** these requirements through structured/time-stamped capture, but **NOT as ensuring compliance** by itself. Compliance is a programmatic outcome the sponsor/CRO achieves through process — not a vendor-deliverable.

### 1c. ClinicalTrials.gov + anthropometric endpoints — VERIFIED

- **Use:** Background context for "obesity trials commonly track BMI / waist circumference / anthropometric measures as endpoints." Confirmed via multiple sources:
  - PMC 7391719 (systematic review): performance of anthropometric tools for obesity
  - NCT05579977: registered obesity trial using waist circumference as measured endpoint
  - Nature Scientific Reports (2024): "Validation of remote anthropometric measurements in a rural randomized pediatric clinical trial" — directly supports the "remote anthropometric measurement is being validated in clinical research" framing
- **Citation strategy:** the article should cite ClinicalTrials.gov generically ("obesity-related trial records commonly reference BMI, waist circumference, and body composition measures") without naming specific NCT numbers — keeps the framing topical without dragging in trial-specific protocol details.
- **URL (generic):** https://clinicaltrials.gov/

---

## 2. Editorial guardrails 11-point alignment with brief

| # | Guardrail | Brief alignment | Action for Phase 3 |
|---|-----------|-----------------|--------------------|
| 1 | Claim substantiation — cut what you can't back | ✅ Strong — Brief Section "Keywords to use cautiously" + Content guardrails explicitly counsel against "FitXpress is a DEXA alternative" / "endpoint validation" claims | Apply throughout — especially Section 6 (data quality), Section 7 (auditability), Section 11 (resilience) |
| 2 | One number, everywhere the same | ✅ Brief uses FX standard product spec (80+ body measurements, BMI, body composition estimates) | Use FX fingerprint numbers consistently |
| 3 | "Independent" / "validated" / "third-party" reserved | ✅ Brief Section 6 explicitly says "Avoid overclaiming that FitXpress independently validates endpoints or replaces protocol-defined reference methods" | Apply — never use "validated" for FitXpress in clinical-trial endpoint context |
| 4 | Drop bare ">X%" without methodology | ✅ Brief makes no performance percentage claims | Apply — no accuracy %s in this article (this article is positioning/operational, not benchmark) |
| 5 | Honest caveats beat clean overclaims | ✅ Brief Section 4 ("Use cautious wording: 'support pre-check workflows,' not 'determine eligibility' unless protocol-specific") explicitly uses this principle | Apply throughout |
| 6 | Medical/regulatory: "not positioned as," never "does not apply" | ✅ Brief content guardrails ban "FDA-approved" / "clinically validated endpoint" / "guarantees compliance" | Apply — use "supports," "helps," "contributes to" framings only |
| 7 | Conditional language for boundaries | ✅ Brief uses "where protocol allows," "where applicable," "depending on protocol" throughout | Apply — every remote-workflow claim conditioned on protocol allowance |
| 8 | Diligence register, not insider register | ✅ Brief specifies CRO/sponsor/clinical-ops audience and protocol-aware register | Apply — clinical-trial-operations vocabulary throughout |
| 9 | Concrete verticals up front | ✅ Brief explicitly names obesity, metabolic, GLP-1, cardiometabolic trials + CRO/sponsor/academic/DCT buyer segments | Apply |
| 10 | Structure defaults | ✅ Brief includes 12 numbered sections + 1 comparison table + 6 FAQ + buyer segments list | Apply (with one structural addition flagged below) |
| 11 | When in doubt, flag — don't decide | ✅ Brief explicitly defers regulatory positioning ("avoid claiming that FitXpress alone makes a study compliant") | Apply — surface any flagged item to Open Items rather than silent edit |

**Brief is internally consistent with editorial guardrails 2026-06-09.** No violations.

---

## 3. Compliance-sensitive fragments + recommended safe wording

| # | Risk area | Brief location | Recommended safe wording |
|---|-----------|----------------|---------------------------|
| C1 | "FitXpress is a DEXA alternative" inference | Brief "Keywords to use cautiously" + Section 8 comparison table | Never use "DEXA alternative" as a positioning claim. Section 8 comparison should compare FitXpress vs **manual measurement workflows** (per brief), not vs DEXA. If DEXA is mentioned at all, use the framing from the existing DEXA article: "different methods, different roles." |
| C2 | "Validated endpoint" / "endpoint validation" | Brief Section 6 (data quality) | Use "supports standardized capture for protocol-defined endpoints" / "contributes to documentation of repeated measurement data." Never "validates the endpoint." |
| C3 | "Determines eligibility" in remote pre-check context | Brief Section 4 subsection on pre-checks | Verbatim from brief: "support pre-check workflows, not determine eligibility unless protocol-specific" |
| C4 | "FDA-approved for clinical trials" | Brief Content guardrails | Never used. Use FDA DHT guidance framing instead: "Per the FDA's Digital Health Technologies for Remote Data Acquisition in Clinical Investigations guidance, DHTs used to acquire data in clinical investigations require sponsor-led fit-for-purpose verification and validation. FitXpress is positioned to support sponsor workflows within that framework, not to claim independent regulatory clearance." |
| C5 | "GCP-compliant" / "guarantees compliance" | Brief Content guardrails | Never. Use: "supports the data integrity, traceability, and audit-trail expectations described in ICH E6(R3) GCP" — places the framework first, FitXpress as a tool that contributes to meeting it. |
| C6 | "Eliminates screen failures" | Brief Content guardrails | Use: "may help reduce avoidable screen failures by surfacing eligibility-relevant data earlier in the workflow" — conditional + qualitative. |
| C7 | "Proves efficacy" / "validates outcomes" | Brief Content guardrails | Never. The article is about operational/documentation support, not endpoint generation. |
| C8 | Implementation Section 12 specific integration claims | Brief Section 12 explicitly says "Keep wording flexible to avoid promising specific integrations unless confirmed" | Apply: "can integrate via API/SDK into protocol-aligned workflows; specific integration paths confirmed during procurement" |
| C9 | Audit-trail claims | Brief Section 7 says "Avoid claiming that FitXpress alone makes a study compliant" | Use "supports audit readiness" / "structured time-stamped records that contribute to monitoring and QA review." Never "audit-ready" as a standalone product claim. |

---

## 4. Brief format question — most important Phase 1 flag

The brief proposes **slug `/clinical-trial-anthropometric-measurement-software-obesity-trials/`** — **without** the `/content-hub/` prefix that other FX content-hub articles use.

This suggests the article may be intended as a **use-case landing page** (sitting under `/fitxpress/` or root) rather than a content-hub blog article.

Format implications:

| Aspect | Use-case landing page (e.g., `/fitxpress/for-telehealth-and-weight-loss/`) | Content-hub article (e.g., `/content-hub/mobile-body-scanning-insurance-underwriting/`) |
|--------|-------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| Length | 1,500–2,500 words | 3,500–4,200 (FX use-case sweet spot) |
| Tone | Product-led, conversion-focused | Educational, B2B-trade, hedged |
| Structure | Hero + product positioning + buyer fit + CTA | Use Case Summary + Disclaimer + 10–15 H2s + FAQ |
| Hero section | Yes (per brief Hero section spec) | No — replaced by Use Case Summary block |
| Disclaimer block | Sometimes (sales-led pages skip it) | Always (FX standard for compliance-touching content) |
| CTAs | Multiple (Hero primary + secondary; mid-page) | Single ("Next steps" at end) per style-guide §5 |
| FAQ | Sometimes | Always (FX standard) |
| External citations | Rare | Standard now (per editorial guardrails 2026-06-09) |

The brief reads as a **hybrid**: it has the Hero section + 2 CTAs + landing-page structure, but also has 12 educational H2 sections + FAQ + 6 GEO questions + 8 keyword clusters that are content-hub depth.

**My recommendation:** treat this as a **content-hub article** (Type A FX use-case deep-dive) and use the slug `/content-hub/clinical-trial-anthropometric-measurement-software-obesity-trials/`. The Hero section from the brief converts into:
- H1 (article title)
- Author byline (Assel Sekerova)
- **Use Case Summary block** (6 lines per FX standard)
- Intro paragraphs (2)
- **Disclaimer block** (FX standard, clinical-trial-adapted)

The Hero's "5 bullets" become a slightly compressed Use Case Summary. The brief's "Primary CTA" + "Secondary CTA" collapse into a single end-of-article CTA per style-guide §5.

**Confirm with Vadim before Phase 2.**

---

## 5. Other brief gaps vs FX standard pattern

| # | Missing element | Recommended Phase 3 action |
|---|------------------|-----------------------------|
| G1 | **No Use Case Summary block** (FX Type A standard 6-line block: Industry / Problem / Solution / Outputs / Role / Business value) | Add at top of article. Draft below in §7. |
| G2 | **No Disclaimer block** (FX standard for compliance-touching content) | Add after intro, before first H2. Draft below in §7. |
| G3 | **No author byline line** under H1 | Add "By **Assel Sekerova**, Marketing Lead at 3DLOOK." per CLAUDE.md §15 default |
| G4 | **Multiple CTAs in Hero + ad-hoc** | Reduce to single demo CTA per style-guide §5 (compliance buyers = demo only, never trial) |
| G5 | **No external citation strategy** explicit in brief | Apply: cite **FDA DHT guidance** (Section 2 OR Section 7), **ICH E6(R3) GCP** (Section 7), and **ClinicalTrials.gov** generically (Section 1 OR Section 6) — all 3 verified live |

---

## 6. Length, customer reference, structure target — defaults proposed

Pending Vadim confirmation:

| Decision | Default proposed |
|----------|---------------------|
| Article format | **Content-hub Type A FX use-case deep-dive** (per format question §4 above) |
| URL | **`/content-hub/clinical-trial-anthropometric-measurement-software-obesity-trials/`** (preserves canonical content-hub pattern) |
| Length target | **3,500–4,200 words** (FX use-case sweet spot per style-guide §2) |
| Customer reference status | **Thought-leadership entry** — no live CRO/sponsor customer reference; this is FitXpress's first published clinical-trials vertical content (frontmatter: `customer_reference_status: none_yet_thought_leadership_entry`) |
| H2 count | **12 (per brief)** — within style-guide §2 range; possible consolidation in Phase 2 if needed |
| FAQ count | **6 (per brief)** — within FX standard range; could expand to 8 if additional GEO questions warrant |
| External citations | **3 verified live**: FDA DHT guidance + ICH E6(R3) GCP + ClinicalTrials.gov generic |
| Internal links | **5–6**: FitXpress product page, FitXpress telehealth/weight-loss, DEXA comparison article, BMI verification, technology page, CTA pricing/demo modal |
| CTA | **Single** demo CTA (style-guide §5): `https://3dlook.ai/pricing/#bd-modal-personalized` |
| Disclaimer block | **Add** per FX standard (compliance-sensitive vertical) |

---

## 7. Draft verbatim blocks for Vadim sign-off in Phase 2

These will be finalized at Phase 2 outline stage. Surfacing here so Vadim can react in Phase 1.

### 7a. Use Case Summary block (FX standard, 6 lines, draft)

> **Industry** — Sponsors, CROs, academic research networks, decentralized clinical trial platforms running obesity and metabolic studies
> **Problem** — Manual anthropometric measurement creates site-to-site variability, coordinator workload, and measurement-only visit burden in multi-site and hybrid obesity trials
> **Solution** — Guided scan-based body measurement capture from two smartphone photos, deployable across sites and remote check-ins
> **Outputs** — Structured, time-stamped body measurements, BMI, and body composition estimates supporting protocol-defined measurement workflows
> **Role** — Standardization and documentation layer that supports trial operations — not a replacement for protocol-defined reference methods, not a validated endpoint
> **Business value** — Reduced site-to-site variability, lower coordinator burden, fewer measurement-only visits, structured records that support monitoring and audit readiness

### 7b. Disclaimer block (FX standard, clinical-trial-adapted, draft)

> **Disclaimer.** FitXpress and the mobile body scanning workflow described in this article support structured anthropometric measurement capture, time-stamped documentation, and remote check-in workflows where the trial protocol allows. They do not replace protocol-defined reference measurement methods (such as DEXA or trained-anthropometrist circumference measurement), validate clinical endpoints independently, determine participant eligibility outside protocol-specific criteria, or guarantee regulatory compliance. FitXpress is positioned as an operational standardization and documentation tool for clinical trial workflows; protocol design, endpoint validation, GCP compliance, and sponsor/CRO regulatory obligations remain with the sponsor, CRO, and investigator teams responsible for the study.

### 7c. FDA DHT guidance anchor (Section 2 or 7, draft)

> Per the [FDA's *Digital Health Technologies for Remote Data Acquisition in Clinical Investigations* guidance](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/digital-health-technologies-remote-data-acquisition-clinical-investigations) (final, December 2023), digital health technologies used to acquire data in clinical investigations require sponsor-led fit-for-purpose verification and validation; the guidance addresses DHT selection, verification, endpoint data collection, risk management, data retention, and sponsor/investigator roles. FitXpress is positioned to support sponsor workflows within that framework — the regulatory classification for any specific deployment depends on intended use, protocol design, and sponsor risk assessment.

### 7d. ICH E6(R3) anchor (Section 7, draft)

> Trial sponsors and CROs operate under the [ICH E6(R3) Good Clinical Practice framework](https://database.ich.org/sites/default/files/ICH_E6%28R3%29_Step4_FinalGuideline_2025_0106.pdf) (Step 4 final guideline, 2025), which explicitly addresses essential records, source data, audit trails, metadata, data integrity, and traceability. Structured, time-stamped measurement capture supports the documentation and traceability expectations the framework describes — but compliance is a programmatic outcome the sponsor and CRO achieve through process design, not a vendor-deliverable.

---

## 8. Open questions for Vadim before Phase 2

1. ⭐ **Article format decision (most important):** content-hub blog article (recommended) or use-case landing page? See §4 above.

2. **URL slug:** if content-hub article → `/content-hub/clinical-trial-anthropometric-measurement-software-obesity-trials/`. Confirm pattern or propose shorter slug (e.g., `/content-hub/clinical-trial-anthropometric-measurement-software/`).

3. **Customer reference status:** confirm thought-leadership entry (no live CRO/sponsor customer to name)?

4. **Length target:** confirm FX use-case sweet spot 3,500–4,200?

5. **Use Case Summary block draft** (§7a) — confirm acceptable or revise?

6. **Disclaimer block draft** (§7b) — confirm acceptable or revise? **This is the highest-compliance-sensitivity block in the article.**

7. **FDA DHT guidance anchor draft** (§7c) — confirm placement (Section 2 OR Section 7) and wording?

8. **ICH E6(R3) anchor draft** (§7d) — confirm placement (Section 7) and wording?

9. **External citations** — confirm 3 (FDA DHT + ICH E6 + ClinicalTrials.gov generic)?

10. **Internal links (5–6) including DEXA cross-link** — confirm we link to the existing DEXA comparison article (`/content-hub/ai-body-scanners-vs-dexa-scans/`) since brief FAQ 5 mentions DEXA?

11. **CTA discipline** — single end-of-article demo CTA per style-guide §5 (collapsing brief's Hero primary + secondary)?

12. **Hero section fate** — convert into H1 + byline + Use Case Summary block + intro paragraphs + Disclaimer (recommended). Confirm.

---

## 9. Phase 1 verdict

Brief is comprehensive and well-aligned with editorial guardrails. Three external sources verified live. The main editorial decision is the **format question** (§4) — whether this is a content-hub article or a use-case landing page. Default recommendation: content-hub article with the slug under `/content-hub/`.

The article carries moderate-high compliance risk (clinical-trial domain, GCP/DHT regulatory context, multiple ban-list claims in brief content guardrails). All 9 compliance-sensitive fragments (C1–C9) have recommended safe wording in §3.

**No fact-check fails. 12 open questions surface above for Vadim resolution before Phase 2 outline begins.**
