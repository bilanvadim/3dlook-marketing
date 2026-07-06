---
phase: 5_metrics_v2_asselya
article: 2026-06-08-occupational-health-screening
date: 2026-06-09
status: ready_for_vadim_full_read
parent: v2-asselya/draft-final.md
---

# Phase 5 — Metrics + link verification (v2-asselya)

## 1. Word count

| Stage | Body words | Status |
|-------|------------|--------|
| v1 baseline | 3,939 | — |
| v2-asselya post-revisions | **3,719** | At ceiling +19 of Asselya's 3500–3700 target |
| Net delta vs v1 | −220 words | Dedup [a]+[l] target was 200–300 — achieved 220 |

## 2. Stylistic compliance

| Check | Result |
|-------|--------|
| Banned 2024-words | **0** ✅ |
| Banned sentence starters | **0** ✅ |
| Rhetorical "not just X" patterns | **0** ✅ |
| Forbidden clearance language | **0** ✅ |
| Avg sentence length | 23.4 words (target 17-22 — slightly over) |
| Short sentences (≤15w) | 26.4% (down from v1's 44%; over 10-15% target but acceptable for dense compliance prose) |

## 3. Citation verify status — all 3 live URLs

| # | Source | URL | Status | Where in article |
|---|--------|-----|--------|---------------------|
| C1 | EEOC enforcement guidance under the ADA | `https://www.eeoc.gov/laws/guidance/enforcement-guidance-preemployment-disability-related-questions-and-medical` | ✅ verified live | Section 5 anchor (link) + FAQ Q4 (mention without link) |
| C2 | BLS Survey of Occupational Injuries and Illnesses 2024 (2.5M cases, 2.3 per 100 FTE, down 3.1% from 2023) | `https://www.bls.gov/news.release/osh.nr0.htm` | ✅ verified live — exact numbers match BLS news release (released January 22, 2026) | Section 2 |
| C3 | ACOEM Guidance and Position Statements | `https://acoem.org/Guidance-and-Position-Statements/Guidance-and-Position-Statements` | ✅ verified live — broad index page (Option A per Vadim's decision) | Section 3 |

**Zero fabricated URLs. Zero invented statistics. Every cited number matches its source verbatim.**

## 4. All external links in v2

| URL | Anchor text | Type |
|-----|-------------|------|
| `https://3dlook.ai/fitxpress/` | "FitXpress by 3DLOOK" | Internal (product page) |
| `https://3dlook.ai/for-bmi-verification/` | "BMI/build verification" | Internal (product capability) |
| `https://3dlook.ai/content-hub/mobile-body-scanning-insurance-underwriting/` | "employer-side underwriting use case" | Internal (cross-link to article) |
| `https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/` | "bariatric pre-qualification workflow" | Internal (cross-link to article) |
| `https://3dlook.ai/pricing/#bd-modal-personalized` | "book a FitXpress demo" | Internal (CTA) |
| **`https://www.bls.gov/news.release/osh.nr0.htm`** | "U.S. Bureau of Labor Statistics' Survey of Occupational Injuries and Illnesses for 2024" | **External — gov citation (NEW in v2)** |
| **`https://www.eeoc.gov/laws/guidance/enforcement-guidance-preemployment-disability-related-questions-and-medical`** | "EEOC enforcement guidance under the Americans with Disabilities Act (ADA)" | **External — gov citation (NEW in v2)** |
| **`https://acoem.org/Guidance-and-Position-Statements/Guidance-and-Position-Statements`** | "ACOEM guidance for occupational medicine physicians" | **External — professional body citation (NEW in v2)** |

**Total: 8 links (5 internal + 3 external).** Style-guide §6 says 4–8 for FX articles. ✅ at upper bound.

## 5. 13 Asselya edits — application status

| # | Edit | Status |
|---|------|--------|
| [a] | Deduplication across sections (~200-300 word target) | ✅ Applied — 220 words removed |
| [b] | Use Case Summary → table format | ✅ Applied — 6-row Markdown table |
| [c] | Disclaimer medical device replaced with Asselya verbatim | ✅ Applied verbatim |
| [d] | Remove "happens after intake, not before" | ✅ Removed |
| [e] | BLS stat → direct link | ✅ Applied (inline markdown link) |
| [f] | "Each recordable case represents..." → Asselya verbatim | ✅ Applied verbatim |
| [g] | Section 3 definition → Asselya verbatim | ✅ Applied verbatim |
| [h] | ACOEM guidance → link | ✅ Applied (Option A — broad index page per Vadim) |
| [i] | Section 3 GEO block dedup/rephrase | ✅ Rephrased to crisp standalone different from body |
| [j] | "45 seconds" capture vs processing fix | ✅ Applied in Section 4 + Section 13 Step 3 |
| [k] | EEOC ADA guidance → link | ✅ Applied (inline markdown link) |
| [l] | Section 5 paragraph compression | ✅ Applied via P3 compression |
| [m] | "Neither is auditable" → Asselya verbatim | ✅ Applied verbatim |
| **+ #3 Vadim** | BLS "down 3.1% from 2023" addition | ✅ Applied |

**13/13 Asselya edits applied. 3/3 Vadim decisions applied.**

## 6. Open items for Asselya (flagged per editorial guardrail #11)

1. **Section 12 medical-device closing line** still uses "medical device certifications do not apply" — same framing Asselya replaced in the Disclaimer per [c]. Per editorial guardrail #6, "not positioned as" replaces "do not apply." Asselya's [c] addressed only the Disclaimer; Section 12 was not in the 13 comments. **Suggested fix in `phase-4-self-critique.md`. Awaiting Asselya sign-off on whether to apply.**

2. **OSHA link** — Section 8 references OSHA 29 CFR Part 1904 but is not linked. Vadim's "(BLS, ACOEM, EEOC)" list excluded OSHA. URL verified live (`https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XVII/part-1904`). Consistent gov-source principle would support adding it. **Awaiting Asselya sign-off.**

3. **FAQ Q4 EEOC mention** is not linked (the link is on the Section 5 anchor, standard "first-mention-only" practice). If Asselya wants both linked, can add — but adds redundancy. **Default kept Section 5 only.**

4. **Avg sentence 23.4 words** is slightly over the 17–22 target. Inflated by dense compliance/disclaimer language and by markdown tables/bullets parsed as long sentences. If Asselya wants under 22, ~10 sentences in the disclaimer/compliance/scope sections would need rewriting. **Default left as is — content density justifies length.**

## 7. Files manifest

`workspace/seo/articles/2026-06-08-occupational-health-screening/`

| Path | Status |
|------|--------|
| `v1/phase-1-fact-check.md` | reference (v1 phase 1) |
| `v1/phase-2-outline.md` | reference (v1 phase 2) |
| `v1/draft-final.md` | reference (v1 final, preserved) |
| `v1/phase-4-self-critique.md` | reference (v1 critique) |
| `v1/phase-5-metrics.md` | reference (v1 metrics) |
| **`v2-asselya/draft-final.md`** | **current — 13 Asselya revisions + 3 Vadim decisions applied** |
| `v2-asselya/phase-4-self-critique.md` | v2 critique |
| `v2-asselya/phase-5-metrics.md` | this file |
