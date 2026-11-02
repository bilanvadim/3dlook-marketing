# QC: accuracy-drives-roi-digital-health (review round 1, 2026-11-02)

Total: 18/20. Verdict: ship with notes.
A and E below are judged by the rubric's own categories. B and D are taken from the code verdicts (lint PASS, 18/18, detector 0.0).

| Cat | Score | Basis |
|---|---|---|
| A. Adherence to plan, intent and decisions | 5/5 | see below |
| B. Facts | 5/5 | code verdict, not rechecked |
| C. Voice, readability, argument | 2/3 | see below |
| D. Format | 3/3 | code verdict, not rechecked |
| E. Value and position | 3/4 | see below |

## A (5/5)
- The A1 ROI model is built as decided. It uses P, m_before, m_after, c, s, F and I, with the formulas as given: "P × (m_before − m_after) × c ÷ 60 − P × s". Onboarding is a separate metric on a started-onboarding denominator, and there are no example numbers.
- The decisions are carried out as written:
  - A2: the comparison H2 matches the decision, and "A scan-estimated weight that differs from the self-reported value flags a discrepancy for review; it does not prove the actual weight."
  - A3: RTPV and the timing use the agreed wording, with no Clothing Detector mention. "The full enrollment step, including the program's own onboarding inputs, can take longer."
  - A4: the repeatability sentence is verbatim, and so is "These figures describe body measurements, not weight, BMI, or body-composition estimates."
  - A5: there are three CTAs with different anchors, all demo-only.
  - E3: the FAQ has four questions, with the pilot question first.
  - E6: the final H2 is as decided.
- BOFU intent holds. The article moves from where the cost comes from, to comparing methods, to the model, to a "fits when" decision frame, to a pilot design. Nothing foreign has been added.

## C (2/3)
- The through-line is clear: manual work grows with volume, so measure staff minutes, and the savings count only after costs. The closing paragraph of the ROI section states it well: "that saving counts only after costs".
- Hedging is dense, especially in the intro and the ROI section: "can demand", "may require", "Whether this lowers costs depends on...", "may fall". In places it softens a point the text has already conditioned. Example: "Better body data can reduce staff verification time when the measurements meet the program's quality requirements. Reliable measurements can reduce the need for repeated checks." The second sentence repeats the first and adds nothing.
- Some sentences read like glue, not like an expert talking:
  - "Seen this way, telehealth patient monitoring is an operations question for program leaders at..."
  - "The difference shows estimated savings, before accounting for any excluded costs." It is unclear what "excluded costs" are.
- The scope note, the product section and the FAQ each repeat the "not a medical device / no eligibility decisions" boundary. This was decision B3, so it is not a defect. The repetition does weigh on the prose, and the boundary paragraph in the product section is the heaviest.

## E (3/4)
- The statements a template would not make:
  - "It is not an error rate for an individual submission, where the gap can be larger or smaller." (The CDC figure is handled honestly.)
  - The `m_before` and `m_after` model, with cohorts timed on real submissions.
  - Onboarding is kept out of the savings formula because of the denominator.
  - "Where a protocol requires dual-energy X-ray absorptiometry, BIA, a calibrated scale, or direct observation, that method stays in place."
- The "fits when" blocks name the conditions under which self-report is enough. That is a position, and it is not sales-driven.
- What is missing is a sentence from someone who has seen the product in a real pilot, for example a typical exception pattern. The claims base does not allow this, so it is a limit of the base and not a fault of the editor.
- The GLP-1 section (about 150 words) is thin. It is a three-step pattern plus a repeatability reference, with little that is specific to a GLP-1 clinic.

## Notes
For the editor:
1. Cut the repeated hedge: delete "Reliable measurements can reduce the need for repeated checks." or merge it with the previous sentence.
2. Rewrite "The difference shows estimated savings, before accounting for any excluded costs." in plain terms: operating savings are before F and I.
3. Replace "Seen this way, telehealth patient monitoring is an operations question for program leaders at telehealth, digital-health, and GLP-1 or weight-management providers." The audience list adds nothing.
4. The final text still has placeholder lines "(Cover) - Concept...", "(Image 1)..." and "(Image 2)...". Confirm they are stripped at publish (D says OK, so this is only a reminder).

For the reviewer (no score penalty):
1. The H2 "Short answer: self-reported data and the cost of checking it" was already flagged by the editor as awaiting approval. It reads fine and matches the GSC query.
2. The verbatim "Better body data can reduce staff verification time..." paragraph (B1) is circular, and it is the least informative paragraph in the text. Consider compressing it to two sentences.
3. The mid-article CTA is placed after the paragraph about the scan fee. It works, but it sits close to the "technology alone does not guarantee" caveat, which weakens the call to action.

for_agent_improver:
- seo-editor: add a rule against stacked hedges ("can ... may ... tends to") in one paragraph. When a sentence is already conditioned by "when", the main verb should be plain.
- seo-editor: after a verbatim insert from the reviewer, check the neighbouring sentences for repetition of the inserted idea.
- seo-planner or claims base: for GLP-1 sections, supply at least one product-specific operational detail (for example, what a clinic reviews between visits) so the section is not generic.

## coordinator_review

```
agreement: ✅ agree
top_issue: B1 paragraph was circular (verbatim L3 after L2, then the chain restated both) and ended on the no-guarantee line right before the mid CTA; sent back to seo-editor as a fix pass (keep L2/L3 verbatim, collapse the rest, end on costs), together with the L7b follow-up sentence and the "Seen this way" line.
```

Notes:
- QC's editor item 1 asked to remove or merge L3. L3 is the reviewer's own required line edit (decisions D3), so it stays and the sentences around it are cut instead.
- Editor item 4 (placeholder lines) is not a defect. `(Cover)` / `(Image N)` lines are the house convention, and the web team strips them on publish.
