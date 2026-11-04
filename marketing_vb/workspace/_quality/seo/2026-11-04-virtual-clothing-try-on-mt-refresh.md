---
artifact: workspace/seo/articles/virtual-clothing-try-on-mt-refresh/final.md
slug: virtual-clothing-try-on
product: mobile_tailor
agent: seo-qc
date: 2026-11-04
stage: final
total: 18/20
verdict: ship with notes
---

# QC: virtual-clothing-try-on (refresh in place, Mobile Tailor)

| Category | Score | Max | Source |
|---|---|---|---|
| A. Adherence (plan and intent) | 5 | 5 | judged |
| B. Factual accuracy | 5 | 5 | code verdict (lint PASS, detector 0.0/1000, checklist 18/18), accepted as given |
| C. Brand, tone, argument | 2 | 3 | judged |
| D. Format and structure | 3 | 3 | code verdict, accepted as given |
| E. Output quality, position | 3 | 4 | judged |
| **Total** | **18** | **20** | |

## A. Adherence: 5/5

All 11 outline sections exist in order, with H2 titles matching the plan (only the Oxford comma differs in S3). The intent holds: informational/MOFU, with virtual try-on as the primary search intent. The Mobile Tailor bridge is limited to fit and size, as briefed. The three requested touchpoints are present and escalate in strength:
- Early, after the S2 bullets: "A try-on image can settle the look, while size for custom and made-to-measure orders comes from body measurements, which [Mobile Tailor] captures from smartphone photos." The sentence keeps try-on primary and says Mobile Tailor captures measurements, not images.
- Mid, in S9: "To [capture body measurements with Mobile Tailor], the person being measured takes front and side photos with a smartphone."
- Final, in the S11 CTA: "Teams that run made-to-measure, formalwear rental, or uniform programs can [see how Mobile Tailor works]."

The boundary sentence "Mobile Tailor does not render garments on a person or offer virtual try-on." is honest and prevents a product mismatch. Customers are anonymized ("A custom-fit PPE manufacturer", "A formalwear rental company"). Nothing foreign was added. The only drift is that S9 (about 350 words) is the heaviest section and is mostly product proof, which is deliberate under the 2026-11-04 instruction.

## B. Factual accuracy: 5/5

Taken from the code verdict. No independent re-check.

## C. Brand, tone and argument: 2/3

What works. The thread is clear: try-on shows the look, measurements decide the fit. The hedges are in the right places ("can help with the first cause", "likely", "may not always be accurate"). There are no banned words, and the detector reports 0 AI tells. Sentence rhythm is varied.

Lapses:
1. The thesis is still repeated, even after the editor's fix. The same look-versus-size line appears in S1 ("Try-on shows how a garment looks. Size and fit come from body measurements."), S2 ("What it leaves open. Size and fit. Both depend on body measurements"), S6 ("Treat the image as a check on the look."), S7 ("the second is a sizing problem, and sizing depends on body measurements"), S8 ("Fit is a separate question.") and S11 ("Orders where size decides the outcome will still start from body measurements"). Six passes of one idea read as a refrain, not as development.
2. The middle is list-heavy and compilation-like. S2, S5, S6 and S7 are mostly bold-label bullets and numbered routes. The editor flags this as intentional for answer-block queries. That is acceptable, but the text between the lists, such as "Each approach needs different input from the shopper and the brand, and each returns a different kind of image.", is neutral connective tissue.
3. S9 shifts register. After about 1,500 words of neutral explainer it becomes product copy: "The production-ready measurements and 3D models feed pattern, design, and order-management automation." The 62-word verbatim accuracy block ("Internal validation across multiple real-world scan events with five repeated scans per person...") is dense for a reader who arrived for virtual try-on. It is mandated, so the lapse lies in how it is introduced, not in the text itself.

## D. Format and structure: 3/3

Taken from the code verdict.

## E. Output quality and position: 3/4

Strengths. The article takes real positions that a template would not:
- "That makes generative try-on the approach most shoppers are likely to meet first."
- "Where size decides the outcome, as with jeans or a tailored jacket, pick the size from the size chart. Treat the image as a check on the look."
- The observation that Google's own selfie try-on "asks shoppers to select their usual clothing size", set beside the Doppl caveat "Fit, appearance and clothing details may not always be accurate." This is a sharp, sourced argument for the fit gap.
- "How close the preview gets depends on both inputs: the body data and the quality of the garment's digital twin."
- "Whether that error matters depends on the garment and how closely it is cut."

Why not 4. Nothing in the text shows someone who has watched Mobile Tailor orders go wrong or right. The three proof bullets are generic once anonymized: "their consistency helps avoid remakes", "Each result feeds the customization of that member's order". The best analytical lines (S5 closer, S6 jeans rule) are two sentences each. About 5-10 minutes of Vadim's editing would lift this: one operator-level detail in S9, and fewer repeats of the thesis.

## Notes on the touchpoints

The early touchpoint at 12.6% reads naturally and does not hijack the intent. The mid touchpoint is correctly placed where the topic turns to made-to-measure, rental and uniform. The final one is a CTA on a topical anchor. This is three CTAs by design, overriding the one-CTA rule, and the article still reads as a try-on explainer, not a product page.

for_agent_improver:
- seo-editor: after Pass 2/3, count how many sections end on or restate the main thesis (here the look-versus-size line appears in six sections). Allow at most three: one early, one at the pivot (S8) and one in the close. In the others, replace the restatement with a new fact or a condition.
- seo-writer: for the MT bridge section in a non-MT-intent article, write one sentence of operator-level observation (what happens to an order when a measurement is wrong) before the claim list. Without it, the anonymized customer bullets read as filler.
- seo-planner (for refresh briefs): when a verbatim mandatory block such as the accuracy paragraph lands in a lay-intent article, include a lead-in sentence in the outline that ties it to the reader's try-on question (why a 1.5-2.0 cm error matters for a jacket), so the block does not appear as a register shift.

## coordinator_review

```
agreement: ✅ agree
top_issue: the look-vs-size refrain in six sections; fix pass by seo-editor on issues 1-2. Issue 3 (operator-level detail) needs facts canon does not have, so it is left for Vadim, no invention.
```
