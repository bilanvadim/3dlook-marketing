---
slug: accuracy-drives-roi-digital-health
workspace: accuracy-roi-telehealth-refresh
stage: draft-v1
draft: draft-v1-writer.md
author: Vadim Bilan
created: 2026-09-23
---

# Writer notes, draft v1

Lint: `python3 scripts/article_lint.py .../draft-v1-writer.md --pack .../accuracy-roi-telehealth-refresh.yaml`
gave VERDICT PASS on the second pass. Prose words 2,135 (target 2,150). Sentences 131, mean 11.7
words, none over 25.

Pass 1 failed one gate: the detector's `terminology_guardrails` flagged "This guide" in the scope
note. Replaced with "The workflows and the cost model described here are operational."

## Number decisions

| Figure (live page or plan) | Decision | Evidence |
|---|---|---|
| CDC: self-reported BMI underestimated severe obesity prevalence by 40%, 5.3% vs 8.8%, 2020 data | **KEPT**, cited inline, `<!-- ext-claim: CDC-PCD-2023 -->` | WebFetch of the primary source, https://www.cdc.gov/pcd/issues/2023/23_0005.htm (Zhao, Park, Ward, Cradock, Gortmaker, Blanck, *Preventing Chronic Disease* 2023). The page states the 40% underestimation, 5.3% vs 8.8%, 2020 data. Self-report came from BRFSS 2020; the bias correction was calibrated against measured NHANES 2013-2018 data. Stated as population-level in the draft. Matches the BMI verification guide's wording. |
| NHANES self-report bias: height +~1 cm, weight -0.75 kg, BMI -0.6 (live link PMC2784464) | **CUT** | WebFetch of PMC2784464 returned only a reCAPTCHA page. WebSearch did not surface the paper or these exact values. A related NHANES/NHIS source in the results gives different values (height +1.22 cm men / +0.68 cm women, BMI 1.16 lower). The figures could not be confirmed as stated, and the plan's default is cut. The CDC figure carries the point. |
| PLOS "10-20% misclassification rates for treatment eligibility" (pone.0231229) | **CUT** | WebFetch of the paper ("Validation of self-reported height and weight in a large, nationwide cohort of U.S. adults", 2020). It reports about 15% of men and 10% of women with misclassified BMI. It does not state "10-20%" and never mentions treatment eligibility. |
| "approximately 40% of adults lack access to scales at home" | **CUT** | The live page gives no source. Not searched further, per the plan's default. |
| "Regulatory bodies now demand objective, documented verification" | **CUT** | No named rule. `objective` is banned about our output. No specific cited requirement added in its place. |
| "up to ten minutes per patient" | **CUT** | Sourced only to "internal reviews from telehealth providers". No primary source exists. Replaced by variable `m` in the ROI model. |
| "16 hours vs 1.25 hours, a 93% reduction" (100 patients/day) | **CUT** | Hypothetical arithmetic presented as an outcome, with no source. |
| "lift consultation capacity by up to 20% without adding staff" | **CUT** | Same unsourced internal reviews. |
| "80% to 90% retention … 10 months instead of 5 … $5-6 million" | **CUT** in full | Hypothetical arithmetic presented as an outcome. Retention is now an optional fourth stream measured by the program, linking to the engagement article. |
| "Scaling from 1,000 to 100,000 patients requires no new infrastructure", "deployment in weeks, not months" | **CUT** | Unsourced. |
| FitXpress timing | **KEPT as FXS-SPEED only**: "in under 45 seconds" (S7) | Pack approved_claims. No other timing variant appears anywhere. |
| Accuracy 96-97%, 1.5-2.0 cm | **KEPT**, S7 only, own paragraph, framework link in the paragraph, `<!-- claim: FXS-ACCURACY -->` | Wording is the `accuracy-formulations.md` §5 short form, which the plan specifies (S7 must-cover 4). The pack's FXS-ACCURACY text is the §1.1 form. Same claim, figures, and conditions; §5 is approved on a par with §1 and keeps every sentence under 26 words. Flagged in case the coordinator reads "verbatim" as §1.1. |
| Repeatability "below 1 cm" | **KEPT**, S6 only, framework link in the paragraph, `<!-- claim: FXS-REPEAT -->` | §5 short form, verbatim, as the plan asks. |
| Photo deletion "immediately after processing, or within 30 days under the customer's policy" | **KEPT** (S7, FAQ 4) | `compliance.md` §3 and §10. This replaces the live page's wrong "automatic photo deletion after model generation". The 30-day window is not in FXS-RETENTION's text, but it is in `compliance.md`, which the writer instructions treat as pre-approved. |
| Yazen, 34,000 scans in 2025 (FX-YAZEN, optional S7 sentence) | **CUT** | Optional in the plan. FX-YAZEN sits in `additional_approved_claims_topic_specific`, and gate 3 only resolves markers against `approved_claims`, so the figure could not carry a valid marker. The plan also forbids tying customer volume to the ROI argument. The editor can restore it if the gate is extended. |

The ROI model uses named variables only (`P`, `m`, `e`, `x`, `c`, `d`, `a`, `s`). There is no worked
example, no price, and no customer name in S5.

## Deviations from the plan

1. **H1 wording.** The plan's H1, "Accuracy and ROI in Digital Health: …", does not contain the exact
   primary keyword, and gate 7 requires it in the H1. The draft uses **"Accuracy and Digital Health ROI:
   Scaling Patient Monitoring Without More Manual Work"**. "Accuracy" and "ROI" stay in the first five
   words, and the content-plan title follows the colon. The SEO title for the publisher is unchanged.
2. **Opening H2.** The plan names Section 1 but gives no H2 text. The draft uses "Where manual work grows
   as a telehealth program scales", per the editorial-rewrites §7 pattern (hedged and descriptive, cover
   concept directly under it).
3. **Privacy paragraph has five sentences** (the plan says four). The first sentence carries the FAQ link
   and the HIPAA/GDPR expansions (M1). Retention is split into photos and outputs, which keeps both
   sentences under 25 words. FXS-HIPAA and FXS-GDPR are verbatim.
4. **FXS-RETENTION wording is shortened** in S7: "retained unless the customer agreement says otherwise,
   with deletion by scan identifier". "On an ongoing basis" was dropped for length. The claim itself is
   unchanged, and outputs are stated as retained.
5. **The GLP-1 section pattern is three bold-label bullets**, not prose, following the §7 "phases" shape.
6. **The down link appears in S10 only.** The plan allows an optional second one in S7, but the draft
   keeps a single CTA.
7. **"Smart Scales" is not named.** Its output is called "weight estimate" / "the scan's weight estimate"
   (S4 table, S6, S7), matching canon ("AI estimate") and the coordinator's instruction. The BMI guide's
   "predicted weight" is not used.

## Checks against the live defect list

Every row in the plan's defect checklist is gone from the draft. The draft does not contain "compliant",
"medical-grade", "dose medications", "fraud", "altered photos", "eliminates", "80+ body metrics",
"objective", "robust", "Moreover", "Disruption", em dashes, or Title Case headings. The only em dashes in
the file are in the frontmatter `hub` strings, which were copied from `plan.md`. There are 10 H2s, all in
sentence case.

## For the editor

- `near_duplicate_pairs` L43~L138: the intended-use sentence appears in the scope note and again in S7,
  where the plan requires it. Repeating a boundary reminder is acceptable per editorial-rewrites §2. Vary
  one of them if it reads as a refrain.
- "The return from better body data rarely comes from a more accurate number alone. It comes from…" is
  the reframe written as a statement. Check it for corrective-negation feel.
- `plan-audit.md` was not read. The writer agent definition excludes it, and the plan says it holds
  everything the writer needs. The coordinator's brief asked for it, so this is flagged as a deviation.
- Byline Vadim Bilan is kept, per the pack's `live_byline`. Flag it in the digest.
