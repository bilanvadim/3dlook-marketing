---
phase: 2_outline_confirmation
article: 2026-06-08-occupational-health-screening
date: 2026-06-08
status: awaiting_vadim_approve_before_phase_3
parent: phase-1-fact-check.md
brief_status: structure_intact_compliance_overlay_applied
---

# Phase 2 — Outline confirmation

The brief's 15-section outline is structurally intact. This document confirms the structure, surfaces the four legal-sensitive verbatim blocks for your sign-off, and maps keyword groups, GEO blocks, external citations, internal links, and guardrails to specific sections.

---

## 1. Final structural map (H1 → CTA)

```
H1 — Standardizing Occupational Health Screening: Faster Intake, Better Documentation, Fewer Rescreens
  Byline — By Assel Sekerova, Marketing Lead at 3DLOOK.
  USE CASE SUMMARY BLOCK (6 lines, FX standard) — see §2 below
  INTRO PARAGRAPHS (2-3 paragraphs)
  DISCLAIMER BLOCK (occupational-health-adapted) — see §3 below

H2.1  — The problem: occupational health screening still slowed by manual intake
H2.2  — Why this matters now: employers need faster screening without adding clinic capacity
H2.3  — What is occupational health screening intake? [GEO answer block]
H2.4  — How FitXpress supports digital occupational health intake [Use case overview + scope line + C5 line]
H2.5  — Standardizing pre-employment screening before the appointment [Pre-employment + EEOC anchor + scope line]
H2.6  — Reducing delays in return-to-work and fit-for-duty workflows [RTW + scope line]
H2.7  — Pre-employment screening vs return-to-work screening [Comparison table + GEO answer block]
H2.8  — Better occupational health documentation across sites and vendors [GEO answer block]
H2.9  — What improves with digital occupational health intake? [Outcomes — reframed verb discipline per C1/C6]
H2.10 — Who uses FitXpress for occupational health screening? [Buyer fit]
H2.11 — More than body scanning: workflow rules, QA, reporting, and scale [Resilience — rewritten per C2]
H2.12 — What FitXpress does and does not do [Compliance/scope table + GEO answer block]
H2.13 — How digital occupational health intake works with FitXpress [Implementation 5-step]
H2.14 — Frequently asked questions [FAQ 7 Q&A]
H2.15 — Next steps [CTA]
```

**Total H2 count: 15**, plus author byline, Use Case Summary block, intro, and Disclaimer block at the article opening. This matches FX Type A pattern from style-guide §9.

---

## 2. Use Case Summary block — verbatim draft (FX standard, top of article)

> **Industry** — Occupational health providers, workforce screening vendors, workers' compensation administrators, multi-site employers
> **Problem** — Manual intake and inconsistent body measurements slow occupational health screening throughput and cause rescreens, rework, and delayed candidate clearance
> **Solution** — Guided mobile body scan from two smartphone photos completed remotely before the appointment
> **Outputs** — Structured, time-stamped body measurements and BMI/body composition estimates as intake documentation
> **Role** — Intake and documentation layer that supports clinician review — not a fitness-for-duty assessment, clearance decision tool, or basis for hiring decisions
> **Business value** — Faster pre-appointment intake, fewer rescreens, more consistent multi-site documentation, audit-ready records

---

## 3. Disclaimer block — verbatim draft (placement: after intro, before Section 1)

> **Disclaimer.** FitXpress and the mobile body scanning workflow described in this article support intake and documentation steps in occupational health screening programs. They do not perform medical examinations, make fitness-for-duty or clearance determinations, replace clinician review or employer policies, or function as a medical device under any regulatory framework. Body measurement and composition outputs are intake data points within the documentation workflow; they are not designed for, and should not be used as, the basis of hiring or employment decisions.

---

## 4. EEOC anchor sentence for Section 5 — verbatim draft (legal-sensitive)

Placement: in Section 5 body, immediately after the section's opening paragraph that introduces pre-employment screening intake.

> In U.S. employment contexts, pre-employment medical examinations apply only after a conditional offer of employment and where the same examination is required of all entering employees in the same job category, consistent with EEOC guidance under the Americans with Disabilities Act (ADA). FitXpress intake operates inside that framework — it does not enable a pre-offer medical examination and should not be deployed in a way that would.

**Notes:**
- "EEOC guidance under the Americans with Disabilities Act (ADA)" — neutral attribution that does not invent a specific publication number or memo title. References the agency and the underlying statute, both verifiable.
- Sentence two pre-empts the misread "FitXpress lets us screen candidates before an offer" — explicitly closes that door.
- This wording is **legal-sensitive** — flagging it for your final review here so it is not edited downstream without re-review.

---

## 5. Section 11 rewrite — verbatim draft (C2 fix, removes banned pattern)

Replaces brief's "FitXpress is not just a remote body measurement app. It is a digital intake and documentation layer..." (banned "not just X, it's Y" rhetorical pattern per CLAUDE.md §6).

> FitXpress operates as a digital intake and documentation layer for high-volume occupational health screening workflows. Beyond the raw body measurement capability, it standardizes intake, supports QA, generates structured reporting, and deploys across multi-site programs without on-site hardware. The operational layer is what makes the difference at enterprise scale, where reliable measurement on its own does not solve the screening throughput problem.

---

## 6. C5 explicit BMI/hiring line — verbatim draft (placement: Section 4 close)

Closes Section 4 (Use case overview) — the gate where FitXpress is first introduced. Reinforces Guardrail 3.

> BMI and body composition outputs captured by FitXpress are intake data points within the documentation workflow. They are not designed for, and should not be used as, the basis of hiring, clearance, or employment decisions. Clinical review, fitness-for-duty determination, and employer clearance policies remain with the licensed occupational health provider and the employer's compliance framework.

Also reinforced in Section 12 compliance/scope table by adding a "does not do" row: **"Inform hiring or employment decisions based on body measurements or BMI"**.

---

## 7. Keyword group → section mapping

| Brief keyword group | Primary section(s) | Secondary section(s) |
|---------------------|-----------------------|--------------------------|
| 1. High-intent commercial keywords (occupational health screening software, employee health screening software, etc.) | Section 4 (use case overview), Section 11 (resilience) | H1, throughout intro, Section 9 (outcomes), Section 13 (implementation) |
| 2. Pre-employment screening keywords | Section 5 (primary) | Section 7 (comparison), Section 14 FAQ (Q1-Q4), Section 3 (definition) |
| 3. Return-to-work / clearance keywords | Section 6 (primary) | Section 7 (comparison), Section 14 FAQ (Q5), Section 10 (buyer fit) |
| 4. Pain-point keywords | Section 1 (problem), Section 2 (urgency) | Section 9 (outcomes) |
| 5. Body measurement / BMI / body composition keywords | Section 4 (use case overview), Section 13 (implementation) | Section 5 (pre-employment use case), Section 11 (resilience) — always hedged per C5 |
| 6. Buyer / ICP keywords | Section 10 (buyer fit, primary) | Section 4, Section 11, CTA Section 15 |
| 7. Documentation / compliance-adjacent keywords | Section 8 (documentation), Section 12 (compliance/scope) | Section 9 (outcomes), Section 6 (RTW) |

---

## 8. Guardrail → section mapping (scope lines naскрізь, not only Section 12)

| Guardrail | Where applied | How |
|-----------|---------------|-----|
| **G1 — No clearance/hiring decisions** | Section 4 close (C5 explicit line), Section 5 close (scope line), Section 6 close (scope line), Section 11 (positioning), Section 12 (full scope table) | Verb discipline naскрізь ("supports intake", "captures structured data", not "clears", "determines") |
| **G2 — EEOC pre-offer / post-offer** | Section 5 (EEOC anchor sentence — see §4 above), Section 14 FAQ (Q3 or Q4) | Always pair "post-offer medical exam" with EEOC framing (C3) |
| **G3 — No BMI/body composition for employment decisions** | Section 4 close (C5 explicit line), Section 12 (table row added), Disclaimer block | Verbatim "not designed for, and should not be used as, the basis of hiring or employment decisions" |
| **G4 — Intake not clearance language** | Section 9 (heading reframe per C1), Section 5/6 throughout, Section 13 (implementation) | "Faster pre-appointment data turnaround" not "faster time-to-clearance"; "supports the intake step that feeds the clearance workflow" not "speeds up clearance" |
| **G5 — Not a medical device, not diagnostic** | Disclaimer block (explicit), Section 12 table, Section 14 FAQ Q6 | Use verbatim "medical device certifications do not apply" framing where contextually appropriate |

**Article-level scope-line count:** 5 explicit scope lines (Disclaimer + Section 4 close + Section 5 close + Section 6 close + Section 12 table), plus verb discipline throughout.

---

## 9. GEO answer blocks — locations + target questions

For LLM citation visibility, each GEO block is a crisp 2-3 sentence answer to a target question, placed at the end of its section.

| # | Section | Target question | Answer pattern |
|---|---------|------------------|------------------|
| 1 | Section 1 | What causes rescreens in occupational health screening? | Missing data + inconsistent measurements + cross-site variance |
| 2 | Section 3 | What is occupational health screening intake? | Definition: data collection before pre-employment/pre-placement/RTW/fit-for-duty assessment |
| 3 | Section 5 | How can employers speed up pre-employment medical clearance? | Pre-appointment data collection + standardized measurements + structured records for clinic teams |
| 4 | Section 6 | What is return-to-work clearance? | Determination of fitness to resume duties after injury/illness/absence — clinician-led |
| 5 | Section 7 | What is the difference between pre-employment screening and return-to-work screening? | Goal + intake need + FitXpress role per workflow (comparison table feeds this) |
| 6 | Section 8 | How can occupational health clinics standardize body measurements across sites? | Same digital intake + same workflow + structured time-stamped data + same documentation rules |
| 7 | Section 12 | Can body measurement software replace an occupational health exam? | No. Supports intake/documentation — does not replace exams, clinician review, or employer policies |

**Total GEO blocks: 7.** Plus 7 FAQ Q&A in Section 14 (reinforces GEO at FAQ level).

---

## 10. External citations placement (3-4 confirmed)

All must be **verified live by writer in Phase 3** — no fabricated stats. If a specific number cannot be verified, ship without it rather than guess.

| # | Source | Where | What to cite | Verify in Phase 3 |
|---|--------|-------|-----------------|----------------------|
| 1 | **EEOC** — enforcement guidance under the ADA on pre-employment medical examinations | Section 5 (EEOC anchor sentence) | Pre-offer vs post-offer framework, "same examination required of all entering employees in the same job category" | Find on eeoc.gov — Enforcement Guidance on Preemployment Disability-Related Questions and Medical Examinations |
| 2 | **U.S. Bureau of Labor Statistics (BLS)** — Survey of Occupational Injuries and Illnesses (annual) | Section 2 (urgency) or Section 6 (RTW intro) | Total recordable workplace injury/illness cases in most recent year (private industry) — supports RTW screening volume framing | Find on bls.gov/iif/ — most recent SOII press release |
| 3 | **ACOEM** (American College of Occupational and Environmental Medicine) — guidance documents on fitness-for-duty / pre-placement evaluations | Section 3 (definition) or Section 6 (RTW) | Industry definition of fitness-for-duty examination scope OR statement about variation in screening practices | Find on acoem.org — Practice Guidelines OR Position Statements |
| 4 (optional) | **OSHA** — 29 CFR 1904 recordkeeping requirements | Section 8 (documentation) | Why standardized employer health records matter — recordkeeping requirement framing | Find on osha.gov — 1904 recordkeeping standards page |

**Citation style:** inline per FX standard ("According to BLS…", "EEOC enforcement guidance under the ADA states…", "ACOEM practice guidelines describe…"). **No footnotes, no external hyperlinks** (per style guide §4).

**If any citation cannot be verified live:** skip and rely on the remaining 2-3.

---

## 11. Internal links placement (5 confirmed, 4-6 target met)

| # | Target URL | Anchor text suggestion | Where placed |
|---|------------|---------------------------|----------------|
| 1 | `https://3dlook.ai/fitxpress/` (or product subpage) | "FitXpress by 3DLOOK" / "FitXpress" | Section 4 (use case overview — product intro) |
| 2 | `https://3dlook.ai/for-bmi-verification/` | "BMI/build verification" or "live photo capture" | Section 5 (BMI verification capability in pre-employment context) |
| 3 | `https://3dlook.ai/content-hub/mobile-body-scanning-insurance-underwriting/` | "Mobile 3D Body Scanning for Remote Evidence Collection" | Section 10 (buyer fit — employer-side adjacent vertical) |
| 4 | `https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/` | "Bariatric Pre-Qualification with Mobile 3D Body Scanning" | Section 6 (RTW — related FX use-case with similar pre-appointment intake pattern) |
| 5 | `https://3dlook.ai/pricing/#bd-modal-personalized` | "Book a FitXpress Demo" / "Talk to Our Team" | Section 15 (CTA — single per article per style-guide §5) |

**5 internal links total.** Within style-guide §6 target range (4–8 for FX articles).

Brief also listed `online-pharmacy-bmi-verification-2026-guide` as a potential link — **deferred** because it overlaps with the bariatric and insurance links and would push past optimal density.

---

## 12. Verb discipline checklist for Phase 3 (Guardrail 4 + C6 enforcement)

| ❌ Do NOT use | ✅ Use instead |
|---------------|------------------|
| FitXpress clears candidates | FitXpress captures intake data that feeds the clearance workflow |
| FitXpress determines fitness | FitXpress provides structured intake data for clinician review |
| FitXpress speeds up clearance | FitXpress reduces pre-appointment intake delays |
| FitXpress makes clearance decisions | FitXpress supports the intake step before the clearance decision |
| Faster time-to-clearance | Faster pre-appointment data turnaround / reduced intake-related delays |
| Health assessment | Structured measurement data supporting the screening workflow |
| FitXpress decides X | FitXpress documents X for clinician review |
| post-offer medical exam *(unqualified)* | post-offer medical examination — after a conditional offer of employment and where consistently applied to all entering employees in the same job category |

---

## 13. Phase 3 length and stylistic targets

- **Word count:** 3,500–4,000 (per brief and FX use-case sweet spot 3,500–4,200)
- **H2 count:** 15 (confirmed above)
- **Avg sentence length:** 17–22 words
- **Short sentences (≤15 words):** 10–15% of all sentences
- **Banned 2024-words:** 0 hits (leverage, harness, robust, seamless, comprehensive, navigate, delve, realm, tapestry, "in today's…")
- **Author byline:** "By **Assel Sekerova**, Marketing Lead at 3DLOOK."
- **Disclaimer block:** placed after intro, before Section 1
- **Use Case Summary block:** placed before intro, after H1+byline
- **CTA:** single, demo target, per style-guide §5
- **Tone target:** 2026 Assel Sekerova voice — measured, B2B trade publication, fingerprint phrases used 3–6 times naturally (per style-guide §3)

---

## 14. Open questions for Vadim before Phase 3 begins

1. **Use Case Summary block (§2)** — confirm 6-line draft acceptable, or any line needs revision?
2. **Disclaimer block (§3)** — confirm verbatim acceptable?
3. **EEOC anchor sentence (§4)** — confirm verbatim acceptable? **This is the legal-sensitive one you flagged.**
4. **Section 11 rewrite (§5)** — confirm acceptable?
5. **C5 explicit BMI/hiring line (§6)** — confirm acceptable?
6. **External citations list (§10)** — confirm 4 candidates (EEOC mandatory + BLS + ACOEM + optional OSHA)? Any specific stat you already have in hand that I should use?
7. **Internal links (§11)** — confirm 5 listed. Drop or swap any?
8. **Customer reference note for frontmatter** — `customer_reference_status: none_yet_research_mode` per your instruction. Confirmed.

---

## 15. Phase 2 verdict

The 15-section structure carries through unchanged from the brief. The five verbatim blocks above (Use Case Summary, Disclaimer, EEOC anchor, Section 11 rewrite, C5 BMI/hiring line) are the legal-sensitive surface area — once you sign off on those, Phase 3 draft can proceed with no remaining compliance ambiguity.

**Awaiting your sign-off on the 8 open questions above (especially #3 — EEOC anchor sentence) before Phase 3 draft begins.**
