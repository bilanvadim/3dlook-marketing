---
phase: 5_metrics_and_compliance_audit
article: 2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct
date: 2026-06-16
status: ready_for_vadim_full_read
parent: draft-final.md
canonical_url: https://3dlook.ai/content-hub/clinical-trial-anthropometric-measurement-software-obesity-trials/
---

# Phase 5 — Metrics + compliance audit + citation verification

## 1. Word count

| Stage | Body words | Status |
|-------|------------|--------|
| Target | 3,500–4,200 | FX use-case sweet spot |
| v1 draft | **3,910** | ✅ inside target range |

Read time at 225 wpm: ~17.4 minutes → display label **"17-minute read"** for WordPress.

## 2. Stylistic compliance scans

| Check | Result |
|-------|--------|
| Banned 2024-words (leverage / harness / robust / seamless / comprehensive / delve / tapestry / realm / navigate / game-changer / revolutionary / groundbreaking / cutting-edge / disrupt / transform / pioneer / unlock) | **0** ✅ |
| Banned sentence starters (Furthermore / Moreover / Additionally / In today) | **0** ✅ |
| Rhetorical "not just X, it's Y" patterns | **0** ✅ |
| Reserved words ("validated" / "third-party" / "independent" for FitXpress) | **0** ✅ ("validated" used only in "protocol-defined reference methods" / "validated measurement protocols" — describes others, not FitXpress) |
| Banned clinical claims (DEXA alternative / validates the endpoint / FDA-approved / GCP-compliant / guarantees compliance / eliminates screen failures / proves efficacy / determines eligibility) | **0** ✅ |
| Avg sentence length | 24.1w (inflated by 2 table-row artifacts; body-prose-only avg ~22.7w — slightly over 22 ceiling but within range for clinical-trial methodological prose) |
| Short sentences (≤15 words) | 23% (over 10-15% target — partly inflated by FAQ Q&A + bullet leads + GEO crisp answers) |

## 3. Compliance audit — 9 sensitive fragments (C1–C9)

All 9 fragments from Phase 1 §3 resolved per safe-wording recommendations. Full table in `phase-4-self-critique.md` Section "Compliance audit." Summary:

| # | Risk | Resolved |
|---|------|----------|
| C1 | DEXA alternative | ✅ comparison vs MANUAL only |
| C2 | Validated endpoint | ✅ explicit "does not validate" in H2.3 / H2.6 / H2.7 |
| C3 | Determines eligibility | ✅ explicit boundary in H2.4 pre-checks |
| C4 | FDA-approved | ✅ never used; neutral DHT framing only |
| C5 | GCP-compliant standalone | ✅ ICH E6(R3) framework positioned first; FitXpress as contributing tool |
| C6 | Eliminates screen failures | ✅ "may help reduce avoidable" — conditional |
| C7 | Proves efficacy | ✅ never claimed |
| C8 | Specific integration claims | ✅ "confirmed during procurement" |
| C9 | Audit-trail standalone label | ✅ "supports audit readiness" framing throughout |

## 4. External citation verify status (3 of 3 verified live)

| # | Source | URL | Status | Where in article |
|---|--------|-----|--------|---------------------|
| C1 | FDA DHT Guidance (final, Dec 2023) | `https://www.fda.gov/regulatory-information/search-fda-guidance-documents/digital-health-technologies-remote-data-acquisition-clinical-investigations` | ✅ verified live in Phase 1 | H2.7 (auditability section) |
| C2 | ICH E6(R3) GCP (Step 4 final, 2025) | `https://database.ich.org/sites/default/files/ICH_E6(R3)_Step4_FinalGuideline_2025_0106.pdf` | ✅ verified live in Phase 1 | H2.7 (auditability section) |
| C3 | ClinicalTrials.gov | `https://clinicaltrials.gov/` | ✅ verified live in Phase 1 | H2.1 (problem context) |

**Zero fabricated URLs. Zero invented document numbers.** Both regulatory references describe their respective frameworks accurately; no overclaim of FitXpress compliance against either.

## 5. Internal links — 5 confirmed

| # | Target URL | Anchor | Section |
|---|------------|--------|---------|
| 1 | `https://3dlook.ai/fitxpress/` | "FitXpress" | H2.3 (product intro) |
| 2 | `https://3dlook.ai/content-hub/3dlook-turns-two-photos-structured-body-data/` | "how 3DLOOK turns two photos into structured body data" | H2.3 (technology context) |
| 3 | `https://3dlook.ai/content-hub/ai-body-scanners-vs-dexa-scans/` | "AI body scanners vs DEXA scans" | H2.8 (comparison closing — cross-link to DEXA article) |
| 4 | `https://3dlook.ai/fitxpress/for-telehealth-and-weight-loss/` | "obesity, GLP-1, cardiometabolic, and weight-loss trials" | H2.10 (pharma sponsor segment) |
| 5 | `https://3dlook.ai/pricing/#bd-modal-personalized` | "Talk to us about clinical trial workflows" | Conclusion / Next steps CTA |

**Total links: 8 (5 internal + 3 external).** Within style-guide §6's 4–8 range at the upper bound.

## 6. Keyword group coverage (8 of 8)

All 8 brief keyword clusters represented:

| Cluster | Primary section(s) | Status |
|---------|---------------------|--------|
| 1. High-intent commercial | H2.3, H2.11 | ✅ |
| 2. Obesity / metabolic | H2.1, H2.9 | ✅ |
| 3. Hybrid / DCT | H2.2, H2.4, H2.12 | ✅ |
| 4. Site variability / operational pain | H2.1, H2.5, H2.6, H2.8 | ✅ |
| 5. Retention / recruitment / screen failure | H2.4 H3 pre-checks, H2.5 | ✅ |
| 6. Body measurement / endpoint terminology | H2.3, H2.6 | ✅ |
| 7. Auditability / data integrity / compliance | H2.7, Disclaimer | ✅ |
| 8. ICP / buyer | H2.10, CTA | ✅ |

## 7. GEO answer blocks — 9 quotable answer blocks

| Type | Count | Locations |
|------|-------|-----------|
| In-body GEO answer blocks | 3 | End of H2.1 (variability), H2.2 (remote capture), H2.6 (data quality) |
| FAQ Q&A | 6 | H2.14 — standardization / remote capture / CRO site burden / audit trails / DEXA replacement / why anthropometric matters |

The 15 GEO seed questions from brief Section "GEO / LLM-answer seed questions" are covered by:
- 3 explicit in-body GEO blocks (with crisp 2-sentence answers)
- 6 FAQ Q&A (with 2-3 sentence answers)
- 6 additional questions answered by H2 section content itself (without explicit Q&A formatting — the H2 headlines essentially answer them)

All 15 GEO seed questions covered in some form.

## 8. FX fingerprint phrases (3-6 naturally, per style-guide §3)

| Phrase | Count |
|--------|-------|
| "two smartphone photos" / "two-photo" | 3 |
| "80+ body measurements" | 3 |
| "~45 seconds" / "roughly 45 seconds" | 2 |
| "structured body data" / "structured outputs" | 8 |
| "guided scan" / "guided capture" / "guided two-photo flow" | 6 |
| "time-stamped records" / "time-stamped capture" | 7 |

**Coverage above the 3-6 floor.** "Structured" / "guided" / "time-stamped" appear naturally as core operational vocabulary for the clinical-trial use case.

## 9. Pre-publish checklist for Vadim

- [ ] Read `draft-final.md` end-to-end
- [ ] Confirm 5 weakest passages (W1–W5 in Phase 4) — accept or flag for revision
- [ ] Confirm 4 verbatim legal-sensitive blocks (Use Case Summary, Disclaimer, FDA DHT anchor, ICH E6(R3) anchor) render correctly in final article
- [ ] Confirm sentence-length metric is acceptable (avg 24.1w — inflated by tables; body-prose ~22.7w) or flag for compression
- [ ] Verify 5 internal link URLs match production article slugs:
  - `https://3dlook.ai/fitxpress/`
  - `https://3dlook.ai/content-hub/3dlook-turns-two-photos-structured-body-data/`
  - `https://3dlook.ai/content-hub/ai-body-scanners-vs-dexa-scans/`
  - `https://3dlook.ai/fitxpress/for-telehealth-and-weight-loss/`
  - `https://3dlook.ai/pricing/#bd-modal-personalized`
- [ ] Verify 3 external citations still live: FDA DHT guidance, ICH E6(R3) PDF, ClinicalTrials.gov
- [ ] Route to Asselya for editorial review (per `asselya_review_required: true`)
- [ ] Meta title + description: per brief Section "Suggested metadata" — confirm or generate publish-package (matching bariatric / occupational-health / DEXA-rewrite format)
- [ ] Featured image / blog banner: separate Figma asset workflow

## 10. Files manifest

`workspace/seo/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/`

| Path | Status |
|------|--------|
| `v1/phase-1-fact-check.md` | Reference — 12 questions resolved by Vadim |
| `v1/phase-2-outline.md` | Reference — 1 open item resolved (Option A consolidation) |
| **`v1/draft-final.md`** | **Current — 3,910 body words, ready for Vadim full read** |
| `v1/phase-4-self-critique.md` | Reference — 5 weakest passages defensibly kept, 11/11 editorial guardrails passing |
| `v1/phase-5-metrics.md` | This file |

## 11. Verdict

**Compliance:** clean. All 9 Phase 1 sensitive fragments resolved. All 4 verbatim legal-sensitive blocks applied as approved. FDA DHT + ICH E6(R3) framings neutral and defer programmatic compliance to sponsor/CRO. DEXA framing routes to existing DEXA article via "different methods, different roles" cross-link rather than positioning FitXpress as DEXA alternative.

**Citation integrity:** 3/3 external sources verified live. Zero fabricated URLs. Zero invented document numbers. Both regulatory references describe their actual frameworks (FDA DHT guidance scope items, ICH E6(R3) essential records / audit trails / data integrity expectations) accurately.

**Style:** word count, banned-word scans, reserved-word scan all pass. Sentence-length metric marginally over target (body prose ~22.7w vs 22 ceiling) — defensible for clinical-trial methodological vocabulary. Short-sentence ratio 23% over 10-15% target — partly inflated by FAQ + GEO + bullet leads as previously observed.

**Editorial guardrails:** 11/11 passing. No silent edits.

**Recommended next steps:** Vadim full read → optional Asselya editorial pass → publish-package generation (matching the format used for bariatric / occupational-health / DEXA-rewrite articles) → CMS publish to `/content-hub/clinical-trial-anthropometric-measurement-software-obesity-trials/`.
