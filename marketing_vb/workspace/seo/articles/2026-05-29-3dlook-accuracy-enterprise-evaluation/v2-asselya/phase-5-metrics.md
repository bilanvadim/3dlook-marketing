---
phase: 5_metrics_and_verification
article: 2026-05-29-3dlook-accuracy-enterprise-evaluation
version: v2-asselya-rewrite
date: 2026-05-29
status: ready_for_vadim_pre_publish_review
parent: draft-final.md
---

# Phase 5 — Metrics, compliance, verification lists

## 1. Compliance scan (automated)

| Check | Result |
|-------|--------|
| Total word count | 3,134 |
| Target range | 2,800–3,500 |
| Compliance | ✅ — comfortably inside the range |
| Read time at 250 wpm | ~12 minutes |
| Banned 2024-words | **0** ✅ |
| Banned sentence starters | **0** ✅ |
| Rhetorical em-dash patterns | **0** ✅ |
| Triple parallelisms | **0** ✅ |
| AI-powered as standalone value | **0** ✅ |
| Em-dash density | 18 instances — all parenthetical/range, none rhetorical |
| Word "vendor" | **0** ✅ |
| Insider-tone phrases ("framework 3DLOOK uses internally", "every sales call", "two vendors quoting") | **0** ✅ |
| Academic definitions of DEXA / InBody / manual | **0** ✅ |
| Per-body-part error table | **0** ✅ (removed entirely per Asselya [o] / Vadim confirm) |
| Smart Scales formula / volume-density methodology | **0** ✅ (removed per [p]) |
| Dataset methodology deep-dive (4 cameras / 34 configs / 86 params / 1M polygons) | **0** ✅ (removed per [o]) |
| ISO benchmark internal scope detail (14 companies, 8 countries, 1,152 data points) | **0** ✅ (removed pending Asselya verification on [l]) |

---

## 2. Hedge discipline audit — 9 sampled numeric claims

All 9 sampled performance claims sit inside explicit "Internal X" hedge patterns. Full table in `phase-4-self-critique.md` Section "Hedge discipline audit".

**Net result: zero naked performance numbers in the article body.**

---

## 3. Critical framing checks

| Check | Result |
|-------|--------|
| New title is generic (not branded with "3DLOOK") | ✅ "Body Scanning Accuracy: A Framework for Enterprise Decisions" |
| Intro reframes from "how accurate is" to "accurate enough for which decision" | ✅ (intro paragraph 1 verbatim per approved sample) |
| 3DLOOK appears as illustrative example, not subject | ✅ — intro paragraph 2: "3DLOOK is referenced throughout as a working example" |
| No insider/sales-call framing anywhere | ✅ (confirmed via grep scan) |
| Dataset detail reduced to scope disclosure only | ✅ ("trained on a proprietary dataset of thousands of participants across US and Europe" — verbatim Asselya wording) |
| Per-body-part data removed entirely | ✅ |
| Smart Scales formula / methodology removed | ✅ — only the performance numbers (MAE / relative error / prediction error) and the "estimation aid, not replacement" framing remain |
| DEXA / InBody mentioned only as "different methodologies, different purposes" | ✅ — operational context only, no technical definitions |
| List-with-bold-leads format used for features (pipeline, production reliability, body composition, compliance) | ✅ — all four section types use bullet lists with bold leading phrases |
| NCSU framing | ✅ "partnership" + public link + explicit "not independent validation" |
| Smart Scales as estimation aid | ✅ |
| No competitor product named negatively | ✅ |
| Disclaimer block: full 5 sentences with [y] verbatim closing line | ✅ — "3DLOOK should not be positioned as equivalent to DEXA, BIA, calibrated scale, or certified manual anthropometry methods." |
| "Medical device certifications do not apply" verbatim in compliance section | ✅ |
| No claims of "clinically validated", "peer-reviewed", "third-party validated" | ✅ — explicit negatives in disclaimer, FAQ Q1, FAQ Q6, checklist Q8 |
| Five-dimensions backbone preserved | ✅ (Dimensions 1–5 with H3 headings) |
| Use-case comparison table with Limitation column | ✅ (6 rows in Dimension 4) |
| Eight-question decision checklist | ✅ |
| FAQ with 9 Q&A, Q1 = clinical validation "No" | ✅ |
| Disclaimer before FAQ | ✅ |
| 4 internal cross-links to past articles | ✅ |
| 1 external link (NCSU public project page) | ✅ |
| Author byline (Assel Sekerova) | ✅ |

---

## 4. Asselya verification needed (consolidated list — present this to Asselya before publish)

This list groups everything that needs Asselya's explicit OK or input before publish.

### Priority 1 — [l] fact identification

| # | Item | Status | What Asselya confirms |
|---|------|--------|------------------------|
| L1 | ISO benchmark internal scope detail (14 companies, 8 countries, 27 participants, 72 subjects, 1,152 data points) — **removed** from v2-asselya as best-guess match to her [l] flag | Removed pending confirm | Was [l] actually about the ISO benchmark detail? If not, surface the actual flagged fact so it can be removed cleanly |
| L2 | Smart Scales MAE 2.1 kg / SD 1.49 / relative error 3.11% — **kept** in draft (matches the v1 audit's allow-list) | Kept | If [l] was about Smart Scales numbers, confirm and they can be cut |
| L3 | "U.S. Navy formula selected through internal comparative evaluation of established anthropometric methods" — **kept** in draft | Kept | If [l] was about this selection-rationale framing, confirm |

**Recommendation:** route the list above with the inline comments file Asselya marked up, so the [l] mapping can be confirmed in one pass.

### Priority 2 — Tone confirmation

| # | Item | Status | What Asselya confirms |
|---|------|--------|------------------------|
| T1 | New title ("Body Scanning Accuracy: A Framework for Enterprise Decisions") | Applied per Vadim approval | Asselya signs off that the title matches her [a][b][c] reframe direction |
| T2 | Intro 2-paragraph reframe | Applied verbatim per approval | Asselya signs off |
| T3 | "3DLOOK as working example" framing throughout | Applied | Asselya re-reads the article in full and confirms no insider tone leaks survived |
| T4 | Removal of per-body-part table and per-body-part repeatability bullets | Applied | Asselya confirms the simplified "1.5 to 2.0 cm typical absolute error per measurement, varying by body part" framing reads correctly |
| T5 | List-with-bold-leads format adopted for features (pipeline, reliability, composition, compliance) | Applied | Asselya confirms the bold-lead style matches her [r][v] note |
| T6 | DEXA / BIA mentioned only as "different methodologies, different purposes" without technical definitions | Applied | Asselya confirms this read is right per [q] |
| T7 | "[Section name] section" cross-references kept (e.g., "see the compliance section", "See Dimension 1") | Light cross-references kept, deeper meta-talk removed | Asselya confirms these are not too meta |

### Priority 3 — Fact verification (Yurii route)

The Yurii confirm list from v1 Phase 5 carries forward unchanged. The numbers stayed the same (96–97%, >95% repeatability, Smart Scales MAE / SD / relative error, BMI 89% / 76% within 5%, 80+ anatomical parameters, 0.40 cm ISO benchmark). Full table in `v1/phase-5-metrics.md` Section 5; not duplicated here.

---

## 5. Pre-publish checklist for Vadim

- [ ] Read `draft-final.md` end-to-end
- [ ] Route the **Asselya verification list** (Section 4 above) to Asselya for sign-off — especially [l] mapping (Priority 1)
- [ ] Route the **Yurii confirm list** (carried forward from v1 Phase 5 metrics) to Yurii
- [ ] Verify 4 internal cross-link URLs at content-hub paths:
    - `https://3dlook.ai/content-hub/3dlook-turns-two-photos-structured-body-data/`
    - `https://3dlook.ai/content-hub/mobile-body-scanning-insurance-underwriting/`
    - `https://3dlook.ai/content-hub/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning/`
    - `https://3dlook.ai/content-hub/body-scanning-technology-comparison/`
- [ ] Verify external NCSU link: `https://3dbodyscan.textiles.ncsu.edu/projects/` still shows 3DLook Inc. as funding partner for the 2022 project
- [ ] Author byline (Assel Sekerova) confirmed
- [ ] Meta title + description: pending — to be generated by `seo-publisher` agent
- [ ] Featured image / blog banner: pending (separate Figma asset workflow)

---

## 6. Files manifest

`workspace/seo/articles/2026-05-29-3dlook-accuracy-enterprise-evaluation/`

| Path | Phase | Status |
|------|-------|--------|
| `source-materials/` | input | unchanged (6 PDFs) |
| `v1/phase-1-data-audit.md` | 1 | superseded by 1b |
| `v1/phase-1b-pdf-reverify.md` | 1b | reference |
| `v1/phase-2-outline.md` | 2 | superseded by Asselya rewrite philosophy |
| `v1/draft-v1.md` | 3 | archived |
| `v1/phase-4-self-critique.md` | 4 | archived (v1 critique) |
| `v1/draft-v2.md` | 4-applied | archived (Asselya found this version misframed; rewrite supersedes) |
| `v1/phase-5-metrics.md` | 5 | archived |
| **`v2-asselya/draft-final.md`** | rewrite | **current; ready for Vadim full read** |
| `v2-asselya/phase-4-self-critique.md` | 4 | rewrite critique |
| `v2-asselya/phase-5-metrics.md` | 5 | this file |

---

## 7. Recommended next steps after Vadim reads draft-final.md

1. Vadim reads `v2-asselya/draft-final.md` end-to-end.
2. If approved as is → Vadim routes Asselya verification list (Priority 1 [l] mapping first) + Yurii confirm list.
3. If Asselya returns no further changes and Yurii returns no number changes → `draft-final.md` is published as is.
4. If Asselya or Yurii return changes → apply as targeted edits; re-run banned-words + insider-tone + hedge scans; then publish.
5. If Vadim wants further changes from his own read → apply targeted edits inline.
6. Meta title + description + CMS-ready packaging → handled by `seo-publisher` agent per CLAUDE.md §9.

Final publish is a manual Vadim action per CLAUDE.md §10 rule 2 (no autonomous publishing).
