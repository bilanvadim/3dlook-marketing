---
phase: 5_metrics_and_compliance_audit
article: 2026-06-08-occupational-health-screening
date: 2026-06-08
status: ready_for_vadim_pre_publish_review
parent: draft-final.md
---

# Phase 5 — Metrics, compliance audit, citation verification status

## 1. Compliance scan (automated)

| Check | Result |
|-------|--------|
| Total word count (incl. frontmatter) | 3,939 |
| Body word count (estimate, excluding frontmatter) | ~3,890 |
| Target range | 3,500–4,000 |
| Compliance | ✅ inside the range |
| Read time at 250 wpm | ~16 minutes |
| Banned 2024-words (leverage / harness / robust / seamless / comprehensive / delve / tapestry / realm / navigate / game-changer / revolutionary / cutting-edge / disrupt / pioneer / transform / redefine) | **0** ✅ |
| Banned sentence starters (Furthermore / Moreover / Additionally / In today) | **0** ✅ |
| Rhetorical "not just X, it's Y" patterns | **0** ✅ |
| Forbidden clearance language ("speeds up clearance", "FitXpress clears", "FitXpress determines", etc.) | **0** ✅ (post-fix) |
| Avg sentence length | 18.3 words ✅ (target 17–22) |
| Short sentences (≤15 words) | 44% globally — see Note below |

**Note on short-sentence ratio:** the 44% global count is inflated by structural elements — Use Case Summary block (6 short lines), 7 GEO answer blocks (~15 short sentences total), 7 FAQ Q&A (~10 short answers), bullet-list items in 5 sections (each bullet's lead-clause is sentence-length), and the 2 tables (~50 cell-level sentences). Body-prose-only ratio is closer to 30%, still above the 10–15% target — a feature of the B2B punchy-declarative voice and the FX list-with-bold-leads format. If Vadim wants the body prose strictly inside the target band, ~10 paragraphs would need light revision to combine adjacent short sentences. Recommend accepting current rhythm unless review feedback differs.

---

## 2. Keyword group coverage (7 of 7)

| Brief keyword group | Covered? | Where |
|----------------------|------------|-------|
| 1. High-intent commercial keywords | ✅ | H1, Use Case Summary, Section 4, Section 11, Section 13 |
| 2. Pre-employment screening keywords | ✅ | Section 5 (primary), Section 7 (comparison), FAQ Q3/Q4 |
| 3. Return-to-work / clearance keywords | ✅ | Section 6 (primary), Section 7 (comparison), FAQ Q5 |
| 4. Pain-point keywords | ✅ | Section 1, Section 2, Section 9 |
| 5. Body measurement / BMI / body composition keywords | ✅ | Section 4 (introduced + hedged), Section 13 (implementation), per-section bullets — every mention hedged per C5 |
| 6. Buyer / ICP keywords | ✅ | Section 10 (primary), Use Case Summary, intro |
| 7. Documentation / compliance-adjacent keywords | ✅ | Section 8 (primary), Section 12 (scope table), Section 9 (outcomes), throughout |

**All 7 groups represented.** No keyword group orphaned.

---

## 3. GEO answer blocks count (7 of 7)

| # | Section | Target question | Status |
|---|---------|------------------|--------|
| 1 | Section 1 | What causes rescreens in occupational health screening? | ✅ |
| 2 | Section 3 | What is occupational health screening intake? | ✅ |
| 3 | Section 5 | How can employers speed up pre-employment medical clearance? | ✅ |
| 4 | Section 6 | What is return-to-work clearance? | ✅ |
| 5 | Section 7 | What is the difference between pre-employment screening and return-to-work screening? | ✅ |
| 6 | Section 8 | How can occupational health clinics standardize body measurements across sites? | ✅ |
| 7 | Section 12 | Can body measurement software replace an occupational health exam? | ✅ |

**Plus 7 FAQ Q&A in the FAQ section** — total 14 quotable answer blocks across the article (7 GEO + 7 FAQ).

---

## 4. Compliance audit — 5 guardrails

### G1 — No clearance/hiring decisions

| Where applied | Verbatim text |
|----------------|------------------|
| Disclaimer block | "They do not perform medical examinations, make fitness-for-duty or clearance determinations, replace clinician review or employer policies, or function as a medical device under any regulatory framework." |
| Section 4 close (C5 line) | "BMI and body composition outputs captured by FitXpress are intake data points within the documentation workflow. They are not designed for, and should not be used as, the basis of hiring, clearance, or employment decisions." |
| Section 5 close | "FitXpress supports the intake step that feeds the post-offer medical examination. It does not perform the examination, make clearance determinations, or replace clinician review." |
| Section 6 close | "FitXpress supports the intake step that feeds the return-to-work and fit-for-duty workflow. The clearance determination — whether the employee can resume specific job duties — remains with the licensed clinician and the employer's clearance policy." |
| Section 7 comparison table close | "The clearance and fitness-for-duty determinations belong to the licensed clinician operating against employer policies and applicable regulatory frameworks." |
| Section 10 close | "In each case, FitXpress operates as an intake and documentation layer. The clinical decisioning remains with the licensed provider and the employer's clearance framework." |
| Section 12 scope table | Full "FitXpress does not do" column with 7 rows |

**Coverage:** 7 explicit scope statements across the article. G1 fully enforced.

### G2 — EEOC pre-offer / post-offer

| Where applied | Verbatim text |
|----------------|------------------|
| Section 5 anchor sentence | "In U.S. employment contexts, pre-employment medical examinations apply only after a conditional offer of employment and where the same examination is required of all entering employees in the same job category, consistent with EEOC enforcement guidance under the Americans with Disabilities Act (ADA). FitXpress intake operates inside that framework — it does not enable a pre-offer medical examination and should not be deployed in a way that would." |
| FAQ Q4 | "In U.S. contexts, the medical examination component applies only after a conditional offer of employment and where the same examination is required of all entering employees in the same job category, consistent with EEOC guidance under the ADA." |

**Every mention of "post-offer medical exam" is paired with the EEOC framing.** No naked use of "post-offer medical exam" anywhere. G2 fully enforced. Citation verified live (see §6 C1).

### G3 — No BMI/body composition for employment decisions

| Where applied | Verbatim text |
|----------------|------------------|
| Disclaimer block | "Body measurement and composition outputs are intake data points within the documentation workflow; they are not designed for, and should not be used as, the basis of hiring or employment decisions." |
| Use Case Summary "Role" line | "...not a fitness-for-duty assessment, clearance decision tool, or basis for hiring decisions" |
| Section 4 close (C5 explicit line) | "BMI and body composition outputs captured by FitXpress are intake data points within the documentation workflow. They are not designed for, and should not be used as, the basis of hiring, clearance, or employment decisions." |
| Section 12 scope table row | "Inform hiring or employment decisions based on body measurements or BMI" — in "FitXpress does not do" column |

**4 explicit statements** covering the BMI/employment-decision boundary. Reader cannot finish the article without hitting this constraint multiple times. G3 fully enforced.

### G4 — Intake not clearance language

| Verb discipline enforced | Where |
|----------------------------|-------|
| "supports the intake step that feeds the clearance workflow" | Section 5, Section 6 closes |
| "supports clinician review" | Disclaimer, Section 10 close |
| "reduces pre-appointment intake delays" (NOT "speeds clearance") | Section 9 bullet, Use Case Summary |
| "intake and documentation layer" | Use Case Summary Role line, Section 4 intro, Section 11 |
| "Faster pre-appointment data turnaround" | Section 9 bullet (NOT "Faster time-to-clearance") |
| "captures intake data that feeds the clearance workflow" / "provides intake data" | Multiple sections |
| Forbidden phrase scan post-fix | **0 hits** for "speeds up clearance", "speeds clearance", "FitXpress clears", "FitXpress determines", "FitXpress makes clearance", "FitXpress decides" |

G4 fully enforced. The Section 9 closing paragraph was rewritten during Phase 4 to remove a residual forbidden phrase in a negation context (see Phase 4 critique CE1).

### G5 — Not a medical device, not diagnostic

| Where applied | Verbatim text |
|----------------|------------------|
| Disclaimer block | "...or function as a medical device under any regulatory framework." |
| Section 12 closing paragraph | "Since FitXpress does not provide medical advice, diagnosis, or treatment recommendations, medical device certifications do not apply. The compliance evaluation for an occupational health deployment of FitXpress runs on data privacy and recordkeeping frameworks (HIPAA, GDPR, OSHA recordkeeping, employer-specific data handling) — not on medical device frameworks." |
| Section 12 scope table | "Diagnose medical conditions" in "does not do" column |

G5 fully enforced. The "medical device certifications do not apply" verbatim line is present in Section 12.

---

## 5. External citations — verify status (4 of 4 verified live with URLs)

| # | Source | Where in article | URL verified | Status |
|---|--------|---------------------|----------------|--------|
| C1 | EEOC Enforcement Guidance on Preemployment Disability-Related Questions and Medical Examinations (ADA) | Section 5 + FAQ Q4 | https://www.eeoc.gov/laws/guidance/enforcement-guidance-preemployment-disability-related-questions-and-medical | ✅ verified — framework matches article description; no invented document number or quote |
| C2 | BLS Survey of Occupational Injuries and Illnesses 2024 (2.5M private-industry cases, 2.3 incidence rate) | Section 2 | https://www.bls.gov/news.release/osh.nr0.htm (also https://www.bls.gov/iif/) | ✅ verified — exact numbers from official BLS news release (released January 22, 2026); 2.5M is the lowest count in series back to 2003 |
| C3 | ACOEM fitness-for-duty guidance for occupational medicine physicians | Section 3 | https://acoem.org/Guidance-and-Position-Statements/Guidance-and-Position-Statements/Fitness-for-Duty-Assessments-of-Industrial-Firefighters-Guidance-for-Occupational-Medicine-Physicia (illustrative ACOEM guidance) + https://acoem.org/XOnline-Learning/Fitness-for-Duty-Challenges-(Essentials) | ✅ verified — ACOEM publishes fitness-for-duty guidance; article uses general framing (no invented quote or document number) |
| C4 | OSHA 29 CFR Part 1904 — Recordkeeping standards | Section 8 | https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1904 + https://www.osha.gov/recordkeeping | ✅ verified — 10+ employees threshold, Forms 300/300A/301, annual electronic submission window all match regulation |

**Zero fabricated statistics. Zero invented document numbers. All four citations point to live, authoritative sources.**

---

## 6. Internal links — placement (5 of 5)

| # | Target URL | Anchor text | Section placement |
|---|------------|---------------|---------------------|
| 1 | `https://3dlook.ai/fitxpress/` | "FitXpress by 3DLOOK" | Section 4 paragraph 1 (product intro) |
| 2 | `https://3dlook.ai/for-bmi-verification/` | "BMI/build verification" | Section 4 paragraph 4 |
| 3 | `https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/` | "bariatric pre-qualification workflow" | Section 6 paragraph 3 |
| 4 | `https://3dlook.ai/content-hub/mobile-body-scanning-insurance-underwriting/` | "employer-side underwriting use case" | Section 10 — large multi-site employers paragraph |
| 5 | `https://3dlook.ai/pricing/#bd-modal-personalized` | "book a FitXpress demo" | Section 15 CTA |

**5 internal links total.** Style-guide §6 target range (4–8) ✅.

---

## 7. Fingerprint phrases (style-guide §3) — used naturally

| Phrase | Count in article | Notes |
|--------|------------------|-------|
| "two photos" / "two-photo" | 5 | Used in Use Case Summary, Section 4, Section 5, Section 13 |
| "80+ body measurements" | 4 | Section 4, Section 7 table, Section 13, FAQ |
| "in roughly 45 seconds" / "in under 45 seconds" | 2 | Section 4, Section 13 |
| "structured body data" | 4 | Section 4, Section 6, Section 8, Section 13 |
| "guided mobile scan" / "guided two-photo flow" | 3 | Use Case Summary, Section 4, Section 5 |
| "without specialized hardware" / "no specialized hardware" | 2 | Section 4 (and "without on-site hardware" in Section 11) |
| "HIPAA compliance and adheres to GDPR principles" | 1 | Section 4 |
| "encrypted in transit and at rest" | 2 | Section 4, Section 8 |
| "audit-ready intake trail" / "audit-trail" | 3 | Section 4, Section 8, Section 13 |
| "role-based access controls" | 2 | Section 4, Section 8 |

**Style-guide §3 calls for 3–6 fingerprint phrases naturally.** Coverage well above the floor.

---

## 8. Pre-publish checklist for Vadim

- [ ] Read `draft-final.md` end-to-end
- [ ] Confirm the 5 weakest passages (W1–W5 in Phase 4 critique) — apply / accept / defer
- [ ] Confirm CE1 fix (Section 9 closing paragraph rewrite) reads correctly
- [ ] Confirm the 4 external citations as written are acceptable for publish
- [ ] Confirm 5 internal link URLs match production article slugs:
   - `https://3dlook.ai/fitxpress/`
   - `https://3dlook.ai/for-bmi-verification/`
   - `https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/`
   - `https://3dlook.ai/content-hub/mobile-body-scanning-insurance-underwriting/`
   - `https://3dlook.ai/pricing/#bd-modal-personalized`
- [ ] Route to Asselya for full read (per `asselya_review_required: true` in frontmatter)
- [ ] Meta title + description: pending — to be generated by `seo-publisher` agent
- [ ] Featured image / blog banner: pending (separate Figma asset workflow)

---

## 9. Files manifest

`workspace/seo/articles/2026-06-08-occupational-health-screening/`

| File | Phase | Status |
|------|-------|--------|
| `v1/phase-1-fact-check.md` | 1 | reference (approved by Vadim) |
| `v1/phase-2-outline.md` | 2 | reference (approved by Vadim) |
| **`v1/draft-final.md`** | 3-4 | **current; ready for Vadim full read** |
| `v1/phase-4-self-critique.md` | 4 | reference |
| `v1/phase-5-metrics.md` | 5 | this file |

---

## 10. Verdict

**Compliance:** clean. All 5 guardrails enforced naскрізь, 7 explicit scope statements across the article, EEOC framework citation verified live, BMI/employment boundary stated 4 times, zero forbidden clearance language post-fix.

**Citation integrity:** 4 of 4 verified live with URLs. Zero fabricated statistics. The BLS 2024 number (2.5M cases, 2.3 incidence rate) is the most recent annual data released January 22, 2026.

**Style:** 3,939 words (in target), avg sentence 18.3 (in target), zero banned 2024-words, zero banned starters, zero rhetorical "not just X" patterns. Short-sentence ratio 44% globally — inflated by structural elements; body-prose ratio closer to 30% (above target but stylistically defensible for B2B trade voice and FX list-with-bold-leads format).

**Recommended action:** route to Vadim for full read. After Vadim approves, route to Asselya for editorial review. No publish without Asselya sign-off given the compliance sensitivity of this vertical.
