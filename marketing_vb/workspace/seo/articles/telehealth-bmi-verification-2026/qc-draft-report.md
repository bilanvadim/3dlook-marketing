---
artifact_reviewed: draft-v1.md
track: seo
stage: Phase 3 output (Writer) — pre-edit QC
qc_date: 2026-08-02
reviewer: quality-controller (rubric v. docs/quality-rubric.md)
word_count: 2910 (incl. frontmatter/headers; body ≈ 2830)
---

# QC Report — draft-v1.md (Telehealth BMI Verification 2026)

## Scores

| Category | Score | Notes |
|---|---|---|
| A. Adherence | 4/5 | Structure, claims table, and positioning guardrails from plan.md all followed. One step done thinner than it should be: the plan's internal-link map lists Main Health hub (up) and several sideways options (How to Measure Body Composition, Body Composition Scale, Visual Progress Tracking); the draft only links Online Pharmacy BMI Verification sideways and skips Main Health hub entirely. |
| B. Factual accuracy | 5/5 | All five locked claims (FAIR Health utilization, WeightWatchers Clinic/Ard et al. 2024, CDC self-report BMI, Forseth et al. 2022 remote-measurement validation, HHS OIG RPM audit) appear with correct figures and correct attribution. No invented numbers, no drug-efficacy claim attributed to 3DLOOK — the 19.4% figure is correctly scoped as the cited study's own outcome. Vertical boundary held: no GLP-1 eligibility claims, no pharmacy-compliance re-explanation. |
| C. Brand & tone | 2/3 | Two real lapses, both fixable in edit: (1) **M2 stacked-negation** — "What FitXpress does not do" opens with two sentences chaining 2-3 separate "does not / not" clauses each (lines ~93, first two sentences of that section), which is exactly the pattern editorial-guardrails.md M2 tells writers to avoid. (2) **Self-reference workaround** — "this piece" appears 4× (lines 17, 31, 37, 101) functioning exactly as the banned "this article / this guide" self-reference the brief's zero-list targets, just with different wording. Minor watch items, not scored down further: "How do you verify BMI remotely..." FAQ heading uses "you" in an educational (non-conversion) context; the illustrative quote "we have a number in the chart" risks reading as 3DLOOK's own "we" rather than a generic program's internal voice. |
| D. Format & structure | 3/3 | Frontmatter complete for a draft stage. File in the correct directory. All 12 structure elements present in the brief's order, FAQ count is exactly 8 as specified, H1 matches the locked title exactly. |
| E. Output quality | 3/4 | Strong, close to publishable, but needs a real editor pass rather than a light copyedit: the section-8 rewrite and the internal-link additions both change actual sentences, not just polish. |
| **Total** | **17/20** | ✅ Good — approve with the fixes below, do not regenerate. |

## Required fixes for Phase 4 (Editor)

1. **Rewrite "What FitXpress does not do" opening two sentences** to remove chained negation. Current:
   > "FitXpress is not positioned as a medical device, and it is not a decisioning system. Inside a telehealth BMI verification workflow, it does not diagnose a condition, does not make a treatment or eligibility decision, and does not replace the clinician who reviews the data it produces."

   Split into single-negation sentences with positive framing carrying the rest, per M2's own worked example pattern (e.g., "Diagnosis, treatment decisions, and eligibility decisions stay with the clinician; FitXpress supports the data behind that review.").

2. **Remove or rephrase all 4 instances of "this piece"** (lines 17, 31, 37, 101) — replace with a concrete noun phrase (e.g., "this workflow," "the split described here," or restructure the sentence to drop the self-reference entirely).

3. **FAQ heading:** change "How do you verify BMI remotely in a telehealth program?" to a non-"you" phrasing, e.g., "How is BMI verified remotely in a telehealth program?" — keeps the secondary keyword, drops the second-person address outside a conversion section.

4. **Rephrase the quoted internal line** "we have a number in the chart" to remove first-person ambiguity, e.g., attribute it explicitly to a generic compliance team's phrasing rather than leaving "we" free-floating.

5. **Add the missing internal links** from plan.md's map, placed where they earn their spot rather than stuffed in:
   - Up: Main Health hub (https://3dlook.ai/content-hub/ai-body-data-health-hub/) — natural fit near the opening or the Next Steps close, alongside the existing AI in Telehealth hub link.
   - Sideways: How to Measure Body Composition and/or Body Composition Scale in the "Methods of remote BMI verification" section (body-composition mention already exists there — anchor it).
   - Sideways: Visual Progress Tracking for GLP-1 Adherence & Retention in the FitXpress "scan-to-scan comparison for progress tracking" bullet — legitimate because that page is about progress-tracking mechanics, not GLP-1 eligibility, so linking it does not blur the vertical boundary the guardrail protects.

## What's already strong (do not touch)

- Section 9 (telehealth vs. pharmacy compliance) does the hand-off cleanly: one paragraph of contrast, one link, no re-explanation of the pharmacy workflow. This was the highest cannibalization-risk section in the brief and it holds the line.
- Claims are cited with real figures and no rounding to sound better; the WeightWatchers Clinic scale point is used for what it actually demonstrates (program scale) rather than repackaged as a 3DLOOK outcome.
- FitXpress positioning throughout section 7 uses only approved phrases (reduces manual intake, standardizes capture, supports clinician review, structured records, documentation consistency, scan-to-scan comparison) with no unapproved claims.

## Coordinator review

agreement: ✅ agree
top_issue: the section-8 stacked negation is the one item that would actually get caught in an editorial pass by Asselya — worth fixing precisely, not just noting, before this goes to publisher.
