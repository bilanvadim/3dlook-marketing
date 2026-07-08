---
phase: 5_metrics_and_compliance
article: 2026-05-29-3dlook-accuracy-enterprise-evaluation
date: 2026-05-29
status: ready_for_vadim_pre_publish_review
parent: draft-v2.md
---

# Phase 5 — Metrics, compliance check, pre-publish readiness

Final pre-publish state. Numbers and checks below derived from `draft-v2.md` after Phase 4 self-critique was applied.

---

## 1. Compliance scan (automated)

| Check | Result |
|-------|--------|
| Total word count (incl. frontmatter) | 4,510 |
| Body word count (estimate, excluding frontmatter) | ~4,460 |
| Target range | 3,500–4,500 (body) |
| Compliance | **At ceiling** — body lands within the target range; total file ~10 words over if frontmatter is counted |
| Banned words (leverage, harness, robust, seamless, comprehensive, delve, tapestry, realm, navigate, game-changer, revolutionary, cutting-edge, disrupt) | **0 hits** ✅ |
| Banned sentence starters (Furthermore / Moreover / Additionally) | **0 hits** ✅ |
| Banned rhetorical em-dash pattern ("not just X — Y", "it's not just X, it's Y") | **0 hits** ✅ |
| Banned triple parallelisms (e.g., "fast, reliable, scalable") | **0 hits** ✅ |
| AI-powered as standalone value (without qualifier) | **0 hits** ✅ |
| Em-dash density | 34 instances in 4,510 words — all parenthetical/range; none rhetorical (per CLAUDE.md §6 wording, only rhetorical em-dashes are banned) |
| Reading time at 250 wpm | ~17 minutes |

---

## 2. Hedge discipline audit (spot check)

Every performance number sampled below sits inside an explicit hedge pattern from `phase-1-data-audit.md` Section 4. Sample of 7 randomized claims:

| Claim | Hedge pattern used | Location |
|-------|---------------------|----------|
| 96–97% measurement accuracy | "On 3DLOOK's internal validation benchmark — a real-world dataset of multiple customer scan events with five repeated scans per person, compared against expert pattern-maker manual measurements — measurement accuracy is approximately 96 to 97%..." | Dimension 1 |
| >95% repeatability | "Internal repeatability testing across five repeated scans per person, on a real-world customer dataset, shows scan-to-scan consistency above 95%..." | Dimension 2 |
| Per-body-part errors 0.54–2.37 cm | "Source: 3DLOOK internal validation against expert pattern-maker manual measurements (February 2025). Five repeated scans per person across multiple real-world customer scan events." (table footer) | Dimension 1 |
| Smart Scales MAE 2.1 kg / 3.11% / 3.5% | "Internal testing shows a mean absolute error of 2.1 kg, a mean relative error of 3.11%, and an average prediction error of approximately 3.5%. Smart Scales is designed for contexts where a calibrated scale is unavailable or impractical... not designed as a replacement for a calibrated scale in clinical, compliance, or underwriting workflows where calibrated weight is the requirement." | H2.6 |
| BMI 89% / 76% within 5% | "Internal testing of BMI calculated from estimated weight shows 89% accuracy against reference, with 76% of users falling within 5% deviation." | H2.6 |
| Dataset 5,000+ / 150,000+ / 30,000+ / 430,000+ | "The model is trained on 3DLOOK's proprietary dataset of 5,000+ participants, comprising 150,000+ photographs, 30,000+ ground-truth 3D scans, and 430,000+ individual measurements." | H2.4 |
| ISO benchmark 0.40 cm | "The ISO benchmark study involved 14 companies across 8 countries, 27 participants, 72 subjects measured, and 1,152 data points gathered, using the average of multiple 3D scanner measurements as the reference." (full methodology disclosed before the number) | Dimension 5 |

**Result: hedge discipline holds throughout.** No naked performance number appears without methodology context.

---

## 3. Critical framing checks

| Check | Result |
|-------|--------|
| NCSU **never** described as "validating" 3DLOOK | ✅ — both NCSU mentions use "partnership" + "dataset enrichment" framing; the explicit "not independent validation" disclaimer appears in Dimension 5 |
| NCSU partnership has public verification | ✅ — hyperlinked to `https://3dbodyscan.textiles.ncsu.edu/projects/` |
| Smart Scales framed as estimation aid (not replacement) | ✅ — explicit "not designed as a replacement for a calibrated scale in clinical, compliance, or underwriting workflows" |
| No competitor product named negatively (DEXA, InBody, smart scales) | ✅ — each described in its own methodology terms; no "better than / less than" wording |
| Disclaimer block: full 5-sentence accuracy-adapted, verbatim | ✅ — single paragraph, 5 sentences, before FAQ |
| "Different methodologies serve different purposes" framing in H2.7 | ✅ — explicit closing sentence in H2.7 |
| "Medical device certifications do not apply" line included verbatim | ✅ — in H2.8 with positioning context |
| No claims of "clinically validated", "peer-reviewed", or "third-party validated" | ✅ — explicit negatives in disclaimer, FAQ Q1, FAQ Q6, and checklist Q8 |

---

## 4. Structural verification

| Element | Outline target | Draft-v2 actual | Status |
|---------|----------------|-------------------|--------|
| H2 sections | 10 | 10 | ✅ |
| H3 dimensions in H2.2 | 5 (D1–D5) | 5 | ✅ |
| Per-body-part error table | 14 rows | 14 rows + methodology footer | ✅ |
| Use-case comparison table | 6 rows, Limitation column required | 6 rows with Limitation column | ✅ |
| ISO benchmark supporting line (D5) | Separate from Feb 2025 numbers, methodology disclosed | Present in D5 with full methodology | ✅ |
| Decision checklist | 8 questions | 8 | ✅ |
| FAQ | 8–10 hedged Q&A, Q1 "clinically validated" = No | 9 Q&A; Q1 = "No" | ✅ |
| Disclaimer | Verbatim, before FAQ, full length | Present, before FAQ, 5 sentences | ✅ |
| Internal cross-links to past articles | 4 | 4 | ✅ |
| External links | 1 (NCSU) | 1 (NCSU projects page) | ✅ |
| Author byline | Assel Sekerova | Assel Sekerova | ✅ |

---

## 5. Updated Yurii confirm list (final, for Vadim's pre-publish routing)

These items should be confirmed by Yurii before publish. Vadim routes; deltas come back for any quick fix in `draft-v3-final.md` (or accepted as is if Yurii confirms current).

| Priority | Item | Where in article | What Yurii confirms |
|----------|------|--------------------|----------------------|
| **MEDIUM** | 96–97% measurement accuracy figure | Dimension 1 | Still the current internally-documented figure as of late 2025/2026; methodology (5 repeats per person, expert pattern-maker reference, real-world customer scan events) remains accurate |
| **MEDIUM** | >95% repeatability with variance <1 cm | Dimension 2, Dimension 1 close | Same wording is current |
| **MEDIUM** | Smart Scales MAE 2.1 kg / SD 1.49 / relative error 3.11% / avg prediction error 3.5% | H2.6 | Numbers current; framing as "estimation aid" (not "beta") is approved by product |
| **MEDIUM** | BMI 89% accuracy / 76% within 5% deviation | H2.6 | Both figures current; same test cohort |
| **MEDIUM** | **80+ anatomical parameters** (changed from 86 per Tech May 2025) | H2.4 | Confirm 80+ is the correct current framing |
| LOW | Per-body-part error table (14 measurements) | Dimension 1 | All values match the Feb 2025 internal validation chart |
| LOW | Per-body-part repeatability variance values (wrist 0.11, ankle 0.07, etc.) | H2.5 | All values match the Feb 2025 repeatability charts |
| LOW | Dataset scope (5,000+ / 150,000+ / 30,000+ / 430,000+) | H2.4 | Current as of 2026 (may have grown but stating documented figures) |
| LOW | Demographic ranges (16–78 / 150–205 cm / 38–210 kg) | Dimension 1 + Disclaimer | Ranges have not changed |
| LOW | ISO benchmark figures (14 companies / 8 countries / 1,152 data points / 0.40 cm) | Dimension 5 | Numbers from the April 2023 study match |

---

## 6. Pre-publish checklist for Vadim

Before publish, the following decisions need Vadim's explicit OK:

- [ ] Final draft (`draft-v2.md`) read in full
- [ ] Yurii confirm list (Section 5 above) routed to Yurii; deltas (if any) returned
- [ ] Internal cross-link URLs verified — confirm the four target articles exist at the exact slugs used in draft-v2:
   - `https://3dlook.ai/content-hub/3dlook-turns-two-photos-structured-body-data/`
   - `https://3dlook.ai/content-hub/mobile-body-scanning-insurance-underwriting/`
   - `https://3dlook.ai/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/`
   - `https://3dlook.ai/content-hub/body-scanning-technology-comparison/`
- [ ] External link verified: `https://3dbodyscan.textiles.ncsu.edu/projects/` still shows 3DLook Inc. as funding partner for the 2022 project
- [ ] Author byline (Assel Sekerova) confirmed per CLAUDE.md §15 default
- [ ] Meta title + description: pending — to be generated as Phase 6 if needed (or by `seo-publisher` agent per CLAUDE.md §9)
- [ ] Featured image / blog banner: pending (separate Figma asset workflow)

---

## 7. Files manifest (`workspace/seo/articles/2026-05-29-3dlook-accuracy-enterprise-evaluation/`)

| File | Phase | Status |
|------|-------|--------|
| `source-materials/` (6 PDFs) | input | unchanged |
| `v1/phase-1-data-audit.md` | 1 | superseded by phase-1b |
| `v1/phase-1b-pdf-reverify.md` | 1b | reference (no further changes) |
| `v1/phase-2-outline.md` | 2 | approved |
| `v1/draft-v1.md` | 3 | superseded by draft-v2 |
| `v1/phase-4-self-critique.md` | 4 | reference |
| `v1/draft-v2.md` | 4 → 5 | **current; ready for Vadim review** |
| `v1/phase-5-metrics.md` | 5 | this file |

---

## 8. Recommended next steps after Vadim's review

1. Vadim reads `draft-v2.md` end-to-end.
2. If approved as is → Vadim routes Yurii confirm list (Section 5) and waits for deltas.
3. If Yurii returns no changes → `draft-v2.md` is published as is (rename to `draft-final.md` for archive).
4. If Yurii returns changes → apply as `draft-v3-final.md`, re-run banned-words + hedge scans, then publish.
5. If Vadim wants additional changes from his own review → apply as `draft-v3-final.md` directly.
6. Meta title + description + CMS-ready packaging → handled by `seo-publisher` agent per CLAUDE.md §9.

This pipeline does NOT publish autonomously — final publish is a manual Vadim action per CLAUDE.md §10 rule 2.
