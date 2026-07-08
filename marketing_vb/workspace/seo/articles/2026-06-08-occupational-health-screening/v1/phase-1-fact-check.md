---
phase: 1_pre_writing_fact_check
article: 2026-06-08-occupational-health-screening
date: 2026-06-08
status: awaiting_vadim_approve_before_phase_2
brief_source: Google Doc occupational health (Vadim, 2026-06-08)
compliance_sensitive: true
---

# Phase 1 — Pre-writing fact-check

Five fact-check passes against the brief. Findings grouped by criticality.

---

## 1. EEOC framing verification (Guardrail 2)

**Brief's claim:** "In the U.S., the EEOC says employers generally may not ask medical questions or require medical exams before making a job offer; after a conditional offer, exams may be allowed if applied consistently to all entering employees in the same job category."

**Verification:** ✅ **Accurate.** This aligns with EEOC Enforcement Guidance on Preemployment Disability-Related Questions and Medical Examinations (1995) and subsequent guidance under the ADA:

- **Pre-offer stage** — employers MAY NOT require medical examinations or ask disability-related questions.
- **Post-offer stage (after conditional offer, before start date)** — medical examinations are permitted IF (a) all entering employees in the same job category are subject to the same examination, and (b) results are kept confidential and stored separately from personnel records.
- **Post-employment** — medical inquiries must be job-related and consistent with business necessity.

**Recommendation for Phase 3 writing:** Section 5 (pre-employment use case) should include one explicit sentence anchoring the EEOC framework, not just a writer-side compliance note. Suggested wording:

> "In U.S. employment contexts, pre-employment medical examinations apply only after a conditional offer of employment and where the same examination is required of all entering employees in the same job category, consistent with EEOC guidance under the ADA. FitXpress intake operates inside that framework — it does not enable a pre-offer medical examination and should not be deployed in a way that would."

This is the strongest defensive line in the article and removes any reader inference that the product is a way to "screen candidates before an offer." Worth including verbatim.

---

## 2. Compliance-sensitive fragments + recommended safe wording

| # | Brief location | Risk | Recommended safe wording |
|---|----------------|------|--------------------------|
| C1 | Section 9 heading: "Faster time-to-clearance" | Guardrail 4 — reads as if FitXpress speeds up clearance itself (clinician decision) | Reframe heading: **"Faster pre-appointment data turnaround"** or **"Reduced intake-related delays in clearance workflows"**. Body text "Better pre-appointment data can reduce back-and-forth" is already hedged — keep that. |
| C2 | Section 11 positioning line: "FitXpress is not just a remote body measurement app. It is a digital intake and documentation layer..." | Banned rhetorical pattern "is not just X, it's Y" per CLAUDE.md §6 + style-guide §7 | Reframe: **"FitXpress operates as a digital intake and documentation layer for high-volume occupational health screening — beyond the raw body measurement capability, it standardizes intake workflow, QA, reporting, and multi-site deployment."** |
| C3 | Section 5 brief mention: "post-offer medical exam" | Guardrail 2 — used carelessly invites EEOC misreading | Always pair with: "after a conditional offer of employment and where consistently applied to all entering employees in the same job category." Never appears without that frame. |
| C4 | Section 4 scope line | Guardrail 1 — needs to be in every use-case section, not only Section 12 | Add micro-scope line at the close of Section 5 AND Section 6 (parallel to Section 4 wording). E.g., end of Section 5: "FitXpress supports intake before the post-offer medical examination. It does not perform the examination, make clearance determinations, or replace clinician review." End of Section 6: parallel wording for RTW. |
| C5 | Sections 9 + 4 + general — BMI/body composition framing in employment context | Guardrail 3 — BMI/body composition data that influences employment = discrimination risk | Throughout the article, anywhere BMI or body composition appears, use the phrase **"structured measurement data supporting the screening workflow"** or **"body-related intake data"** — never "health assessment" or "fitness indicator" in this article. Add a single explicit line in Section 4 (use case overview) or Section 12 (compliance/scope): "BMI and body composition outputs captured by FitXpress are intake data points within the documentation workflow; they are not designed for, and should not be used as, the basis of hiring, clearance, or employment decisions." |
| C6 | Section 5 + Section 6 + Section 12 — "supports clearance workflow" framing | Guardrail 1 — verb choice matters | Use **"supports the intake step that feeds the clearance workflow"**, **"captures structured documentation for clinical review"**, **"helps standardize the data clinicians review"**. AVOID: "FitXpress clears", "determines fitness", "makes clearance decisions", "speeds up clearance" (Guardrail 4). |
| C7 | Brief Section 8 mentions "audit-friendly screening records" + Section 12 compliance documentation | Should align with FX standard compliance vocabulary | Use style-guide §3 fingerprint phrases: "auditable digital trail per case", "structured body data", "time-stamped". Brief's terminology already aligns but worth confirming in writing. |

---

## 3. Logical consistency across 15 sections

The 15-section structure is internally consistent and follows a defensible flow. Three minor structural observations:

| # | Observation | Recommendation |
|---|-------------|------------------|
| L1 | Sections 1 (problem) + 2 (urgency) both touch throughput/bottlenecks | Keep distinct: Section 1 frames operational pain (bottlenecks); Section 2 frames market pressure (employer hiring volume + clinic capacity). Writer should ensure no sentence-level repetition. |
| L2 | Section 11 (resilience against generic AI) placed between Section 10 (buyer fit) and Section 12 (compliance) | Standard placement; works. No restructure required. |
| L3 | Section 9 (business outcomes) + Section 8 (documentation) have adjacent value-proposition framing | Acceptable. Section 8 = documentation/QA quality; Section 9 = throughput/conversion outcomes. Writer should keep them on distinct axes. |

**No logical contradictions identified.** No section claims something another section refutes.

---

## 4. External stats — what's needed (brief does not include any)

The brief contains zero external citations. Style guide §1 + §4 are explicit: "Stats-first, opinion-second. Numbers from named external sources (NAIC, CDC, Swiss Re, McKinsey, LIMRA, Munich Re, Gen Re) carry the argument."

The bariatric and insurance reference articles each cite 3–5 external sources (CDC, NHANES, ASMBS, Munich Re, Swiss Re, NAIC, KFF, JAMA Network Open). To match production-grade FX article quality, the occupational health article needs at least **3 external citations**.

**Suggested external anchors for this article** (writer to verify each in Phase 3 before citing):

| Suggested source | What it would anchor | Article section |
|--------------------|-----------------------|-----------------|
| **U.S. Bureau of Labor Statistics (BLS)** — Survey of Occupational Injuries and Illnesses | Annual count of recordable workplace injury cases requiring return-to-work clearance (~2.6 million private-industry cases in recent years) | Section 2 (urgency) or Section 6 (RTW) |
| **National Council on Compensation Insurance (NCCI)** — annual workers' comp report | Average duration of indemnity claim / days away from work | Section 6 (RTW) |
| **ACOEM** (American College of Occupational and Environmental Medicine) — fitness-for-duty guidance | Industry framing for what fit-for-duty assessment covers | Section 3 (definition) or Section 6 (RTW definition) |
| **EEOC enforcement guidance** | Pre-offer vs post-offer ADA framing | Section 5 (pre-employment) — already recommended in EEOC framing above |
| **OSHA recordkeeping standards (29 CFR 1904)** | Why standardized documentation matters | Section 8 (documentation) |
| **DOL / Workforce Investment** — pre-employment screening volume estimates | Scale of the screening market | Section 2 (urgency) |

**Phase 3 task:** writer picks 3–4 of the above (or equivalents), verifies the actual current numbers via direct lookup, and cites inline per style-guide pattern ("According to BLS...", "OSHA recordkeeping requires...", "EEOC guidance under the ADA states..."). No invented numbers.

If Vadim prefers to ship the article without external stats (faster, but weakens the article relative to the production-grade FX standard), flag and proceed.

---

## 5. Brief gaps against FX style-guide Type A pattern

The brief mostly follows Type A but is missing three standard FX article elements:

| # | Missing element | Where it goes | Source |
|---|------------------|----------------|--------|
| G1 | **Use Case Summary block** at article top (before intro) — six-line structured block: Industry / Problem / Solution / Outputs / Role / Business value | Top of article, before Section 1 | Style-guide §2, §9 Type A item 1 |
| G2 | **`**Disclaimer.**` block** in or right after the intro | After Section 2 (before Section 3 Definition) or after Section 4 (use case overview) | Style-guide §1 (FX hedging intensity), §8 FitXpress disclaimers note |
| G3 | **Author byline line under H1** ("By **Assel Sekerova**, Marketing Lead at 3DLOOK.") | Directly under H1 | Bariatric reference article line 40 + insurance article masthead |

**Recommendation:** Add all three in Phase 3 draft. They are non-negotiable for FX production parity.

**Draft scope line for the Disclaimer block** (occupational-health-adapted):

> **Disclaimer.** FitXpress and the mobile body scanning workflow described in this article support intake and documentation steps in occupational health screening programs. They do not perform medical examinations, make fitness-for-duty or clearance determinations, replace clinician review or employer policies, or function as a medical device under any regulatory framework. Body measurement and composition outputs are intake data points within the documentation workflow; they are not designed for, and should not be used as, the basis of hiring or employment decisions.

---

## 6. Open questions for Vadim before Phase 2

1. **External stats:** ship with 3+ external citations (CDC/BLS/NCCI/ACOEM/EEOC/OSHA), or ship without (faster but below FX production standard)? **My recommendation: with 3+ citations.**
2. **Section 11 positioning rewrite** (banned "not just X, it's Y" pattern): confirm rewrite per C2 above.
3. **Section 9 "Faster time-to-clearance" heading reframe** (per C1 above): confirm.
4. **Disclaimer block addition** (G2 above): confirm placement (suggested: right after Use Case Summary block + intro paragraph, before Section 3).
5. **EEOC framing sentence in Section 5** (item 1 above): confirm verbatim wording acceptable, or revise.
6. **Customer reference status:** Are there any occupational health customers (workforce screening vendors, multi-site employers) that should be referenced anonymously, or is this thought-leadership entry into a new vertical similar to the bariatric article's stance? **My default assumption: thought-leadership entry, no customer reference.**
7. **CTA route:** Style-guide says compliance buyers get demo-only. Brief proposes "Book a FitXpress Demo" or "Talk to Our Team". CTA target URL: `https://3dlook.ai/pricing/` (demo modal) per style-guide §5 default, or `https://3dlook.ai/contact-us/`?

---

## 7. Phase 1 verdict

The brief is **structurally sound and ready to move to Phase 2 outline confirmation** after Vadim resolves the 7 open questions above.

The article carries higher compliance risk than the previous four FX articles because it touches employment decisions, ADA/EEOC pre-offer rules, and BMI/body composition data in a context where misuse creates discrimination exposure. The five guardrails from Vadim's instruction are the right frame; Phase 3 writing will apply them in the body text per items C1–C7 above.

**No fact-check fails. Seven safe-wording recommendations, one EEOC anchor sentence, three brief-pattern gaps to fill, one external-stats decision to make.**

Awaiting Vadim's resolution on the 7 open questions before proceeding to Phase 2.
