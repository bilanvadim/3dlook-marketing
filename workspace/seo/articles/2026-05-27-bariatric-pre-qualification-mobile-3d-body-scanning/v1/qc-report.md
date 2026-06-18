---
phase: 4_qc_pass
article: 2026-05-27-bariatric-pre-qualification-mobile-3d-body-scanning
date: 2026-05-28
status: awaiting_vadim_final_approval
artifact: workspace/seo/articles/2026-05-27-bariatric-pre-qualification-mobile-3d-body-scanning/v1/draft-final.md
---

# QC Report — Bariatric Pre-Qualification Article (v1)

## 1. Style metrics

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Word count | 2,500–3,000 (brief) | **3,034** | ⚠️ 1.1% over brief upper bound; in v3 BMI density range |
| Avg sentence length | 17–22 | **21.0** | ✅ in range |
| Short sentences (<10w), narrative | 10–15% | **12.5%** | ✅ in range |
| Short sentences (<10w), raw | — | 18.6% (incl. 4× `Stage N — …` subheads and 9× FAQ question lines) | informational |
| Banned 2024-words | 0 | **0** | ✅ |
| External citations (inline links) | every cited number | **10 (8 unique URLs)** — every cited number has an inline source link | ✅ |
| Internal links | ≥4 | **7 (5 unique URLs)** | ✅ |

**Note on word count overshoot:** The brief target ceiling is 3,000 and the article is 3,034 — 1.1% over. Trimming further would either remove citation context (Funk/Kurian affiliations, JAMA Surgery cohort size) or reduce the use-case workflow detail in H2.5/H2.6, both of which carry real reader value. Leaving as-is; happy to cut the last 34 words on request.

**Note on short-sentence count:** The raw short-sentence rate (18.6%) includes 4 `Stage 1 — / Stage 2 — / Stage 3 — / Stage 4 —` bold subheads in H2.5 (each formatted as a period-terminated label followed by body text) and 9 FAQ question lines. Excluding those formatting elements — which are structural, not narrative prose — the narrative short-sentence share is 12.5%, in the 10–15% target band.

## 2. Banned-word scan

Scanned for full list from CLAUDE.md section 6 + blog style guide section 7:
- leverage / leveraging — **0**
- utilize / utilization — **0**
- harness — **0**
- robust — **0**
- seamless — **0**
- comprehensive — **0**
- delve — **0**
- tapestry / realm — **0**
- game-changer / revolutionary / cutting-edge / disrupt — **0**
- unlock the power — **0**
- pioneer / pioneering — **0**
- navigate (figurative) — **0**
- "in today's …" — **0**
- "Furthermore / Moreover / Additionally" as sentence starters — **0**
- "It's not just X, it's Y" rhetorical — **0**

Em-dashes used only as parenthetical separators (per style guide: "em-dash is fine as a parenthetical separator"), not as rhetorical "X — Y" constructions.

## 3. Citation completeness

Every external numeric or claim-based citation has a working inline link to first-source. List below maps each cited claim to its inline link target.

| Claim | Inline link |
|-------|-------------|
| 40.3% adult obesity, 9.4% severe (NHANES Aug 2021–Aug 2023) | `cdc.gov/nchs/products/databriefs/db508.htm` |
| 33M eligible, <1% complete annually | `pmc.ncbi.nlm.nih.gov/articles/PMC10136401/` |
| ASMBS 270,089 procedures 2023 | `asmbs.org/resources/estimate-of-bariatric-surgery-numbers/` |
| Self-reported BMI underestimated severe obesity by 40% | `cdc.gov/pcd/issues/2023/23_0005.htm` |
| Pre-op attrition 50–60% | `pmc.ncbi.nlm.nih.gov/articles/PMC10136401/` (same URL — second use, allowed) |
| Bariatric surgery 8.7% YoY decline, 17M cohort | `statnews.com/2024/10/25/bariatric-surgery-falls-as-glp-1-demand-rises-wegovy-zepbound/` |
| Funk + Kurian quotes ("initial gateway", "increase in new consults") | `facs.org/.../bulletin/2025/april-2025-volume-110-issue-4/are-anti-obesity-medications-changing-bariatric-surgery/` |
| KFF 43%/28% GLP-1 employer coverage 2025 | `kff.org/health-costs/2025-employer-health-benefits-survey/` |
| 1-in-7 (14%) bariatric patients initiate GLP-1 post-surgery, n=112,858 | `publichealth.jhu.edu/2025/one-in-seven-bariatric-surgery-patients-turn-to-new-weight-loss-drugs` (also cited again in H2.7) |
| Pre-auth windows | Soft phrasing only, no numeric anchor — per Vadim's hedge decision in fact-check approval |

## 4. Verification checklist (Type A — FX use-case deep-dive)

- [x] Disclaimer block placed before H2.1 (bariatric-specific phrasing — "do not determine medical eligibility for bariatric surgery, provide diagnoses, replace clinical evaluations, or make pre-authorization decisions")
- [x] Use Case Summary block placed in H2.5 (Industry / Problem / Solution / Outputs / Role / Business value)
- [x] Author byline: "By **Assel Sekerova**, Marketing Lead at 3DLOOK."
- [x] H1 contains target keyword: "Bariatric Pre-Qualification with Mobile 3D Body Scanning…"
- [x] All 10 approved H2s present, in approved order
- [x] H2.3 framing reflects Vadim-approved correction (volume contracted while intake complexity rose)
- [x] H2.8 patient-journey table present (6 rows, AEO-friendly)
- [x] FAQ section: 9 Q&A pairs (6 broad-keyword educational + 3 product-specific)
- [x] CTA block under "See FitXpress inside a bariatric intake" — demo-only, compliance-buyer-appropriate
- [x] Related reading block — 2 internal content-hub links
- [x] Internal links ≥4 — actual 7 (5 unique URLs)
- [x] Inline external citations on every cited number — yes
- [x] Frontmatter includes `brief_corrections` field per Vadim's request
- [x] Frontmatter author = Assel Sekerova
- [x] Frontmatter product = fitxpress
- [x] Frontmatter article_type = use_case_deep_dive
- [x] No competitors named directly (no Prism Labs, Bodygram, Size Stream)
- [x] No clinical-decisioning claims ("determines", "ensures", "guarantees") — hedged throughout
- [x] No first-person "we"/"our" in narrative (FitXpress referenced in third person)
- [x] No banned phrases (full scan in section 2)

## 5. Fingerprint phrases used (target 3–6 from style guide section 3)

Counted naturally occurring fingerprint phrases:
1. **two-photo guided flow** / **two-photo guided capture** / **front and side smartphone image** (variants of "two photos" + "guided")
2. **80+ body measurements** (used 3× — always exact form, always with "+")
3. **roughly 45 seconds** (used 1×)
4. **structured body data** (signature 2026 phrase — used 4× across H2.4, H2.5, H2.6, H2.8)
5. **HIPAA-maintained / BAA / encrypted in transit and at rest** (compliance vocabulary cluster)
6. **audit-ready evidence / audit posture** (workflow-vocabulary cluster — used 3×)
7. **supporting evidence — not standalone decisioning / clinical decisioning** (hedge cluster — used 4×)

✅ Within target band.

## 6. Decisions made during writing (deviations from outline or worth flagging)

1. **Pre-H2 disclaimer placement.** Outline placed disclaimer "before H2.1". In the actual draft, I placed it AFTER the 2-paragraph intro and BEFORE H2.1 — same logical position, but it reads more naturally as a postscript to the orientation paragraph than as an interruption to the first sentence. Matches the v3 BMI pattern.
2. **Stage 1–4 formatting in H2.5.** Outline had no specific format guidance for the four-stage workflow walkthrough. I used `**Stage N — Name.** Body text…` (bold-label-then-prose) — the same pattern v3 BMI uses for its "minimum standard" bullet list. This inflated raw short-sentence count (the bold labels read as 4-word sentences to the metric script) — addressed in section 1 above.
3. **H2.6 dropped one paragraph from outline.** Outline mapped "Manual measurements taken at consult vs structured remote data" as two adjacent paragraphs. I merged them into one tighter explanation to stay inside the word-count target. No factual content lost.
4. **JAMA Surgery citation appears twice.** Once in H2.3 (post-surgery GLP-1 framing as part of the gateway argument) and again in H2.7 (longitudinal tracking framing — adjunct medication makes baseline scanning more valuable). Both uses are substantively different and the duplication is intentional, not a citation-stuffing problem.
5. **FAQ Q9 doubled as workflow recap.** "How does FitXpress support bariatric pre-auth documentation?" answer recaps the H2.6 thesis. Standard SEO-FAQ pattern — answer should hold up as a standalone snippet for AI Overview / featured-snippet capture.
6. **Word count overshoot 34 words.** Article runs 3,034 vs 3,000 brief ceiling. Trimming further would have removed Funk/Kurian institutional affiliations, JAMA Surgery cohort size, or H2.5 use-case workflow detail — each of which carries real reader value. Flagged for Vadim's call; happy to cut on request.

## 7. Comparable to reference articles

Quick comparison to the two style-anchor reference articles:

| Dim | v3 BMI (verified) | Insurance underwriting | This article (v1) |
|-----|------------------|------------------------|-------------------|
| Word count | ~2,400 | 4,200 | 3,034 |
| H2 count | 7 | 15 | 10 |
| Disclaimer block | yes | yes | yes |
| Use Case Summary block | yes (mid-article) | yes (top) | yes (in H2.5) |
| Author | Assel | Assel | Assel |
| Inline external links | yes (6) | no (named-source style) | yes (8 unique) |
| Internal links | 3 | 3 | 5 unique |

The article hews to the v3 BMI pattern more than to the older insurance-underwriting pattern — inline first-source URLs throughout, modern compliance-aware framing. Aligns with Vadim's note that v3 is the freshest example of our style.

## 8. Ready for Vadim final approval

Awaiting decision on:
1. **Word count overshoot** (3,034 vs 3,000 ceiling). Keep, or trim 34 more words?
2. **Citation duplication** of JAMA Surgery URL in H2.3 + H2.7. Intentional dual-use — confirm OK.
3. **Pre-auth window phrasing** ("from a few weeks to several months") — Vadim approved soft phrasing in fact-check; final draft uses it without numeric anchor. Confirm reads correctly.
4. **Anything else flagged on read-through.**

No automatic publication. Awaiting Vadim's final go-ahead before any further action (e.g., promotion to a versioned `v1-final` folder or handoff to publish-package generation).
