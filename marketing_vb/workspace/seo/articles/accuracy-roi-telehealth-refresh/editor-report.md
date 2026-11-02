---
slug: accuracy-drives-roi-digital-health
workspace: accuracy-roi-telehealth-refresh
stage: final
review_round: 1
input: v1/final.md (= live page since 2026-10-30) + review-1.md + review-1-decisions.md
output: final.md
editor: seo-editor
date: 2026-11-02
---

# Editor report, Review 1

## Gates

- `article_lint.py final.md`: **PASS**, all 10 gates `ok`.
- Detector (`--channel article`): **CLEAN**. It shows 0 hard fails, 0 house-rule violations, 0 markers and density 0.0/1000.
- Prose words: **2,337**. Decisions F allows 1,950-2,350 and the lint band is 1,827-2,472, so the two agree. Headroom under F is 13 words: recount if anything is added to the body.
- Sentence length: mean 13.0 words, p90 21, 2 sentences over 25 (1.5%), none over 35.
  - Both long sentences are VERBATIM (the ROI formula line and the last sentence of E7), so neither was split.
- Near-duplicate pairs: none.
- Repeated phrases: scan-estimated weight, body-composition estimates and net monthly savings. These are the precise terms C requires.

## Change log

### P1, required

| Review item | Decision | What changed |
|---|---|---|
| 1. ROI model and denominators | A1, D L7 | The variable table is now `P`, `m_before`, `m_after`, `c`, `s`, `F`, `I`; `e`, `x`, `d` and `a` are out. All four formulas are verbatim. L7a is dropped. L7b sits directly after the operating-savings formula. One lead-in states the units (money per month, months, a ratio for a period). One sentence covers logging the exception rate. Onboarding completion is reported separately on a started-onboarding denominator. Retention is an optional metric with its own denominator, and the engagement link stays. No worked numbers. The pilot design moved to the final section. |
| 2. Scan estimates are not verified weight | A2, E1, E4 | The comparison H2 is verbatim. "Verified capture" and "a record it did not have to take on trust" are gone. The scan cell is verbatim. The weight-check paragraph is now a discrepancy check, and the company sets the threshold and the review rule. "Verified" names an option only in short-answer question 1. Everywhere else the word family means the verification step. |
| 3. Guided capture and timing | A3 | The v1 pose/clothing/retake paragraph is deleted. In its place: the RTPV sentence verbatim, the [capture-quality FAQ](https://3dlook.ai/content-hub/fitxpress-capture-quality-user-experience-faq/) link (HTTP 200 on 11-02), and one sentence that the pilot measures resubmissions. The Clothing Detector is not mentioned. Three scan cells are verbatim. The timing is "under 45 seconds from the photos to structured results", followed by the journey note with no number. |
| 4. Accuracy and repeatability | A4 | The repeatability sentence is replaced verbatim. The §5 short forms are unchanged, in separate paragraphs, each with the framework link. The body-measurement scope sentence is added verbatim after the accuracy short form. There is no ±3.5% figure. |
| 5. Three CTAs | A5 | Three text sentences, each with a different anchor:<br>• Early: after the scope note, 18 words, at 10% of prose. It links to the landing without a modal, using the landing-map anchor "remote body measurement for telehealth".<br>• Mid: after B1, to `#bd-modal`.<br>• Final: the last sentence of the article, to `#bd-modal`, with v1's anchor. |

### P2, content and evidence

| Review item | Decision | What changed |
|---|---|---|
| 6. Accuracy-to-ROI chain | B1, D L2, L3 | One paragraph in the ROI section. It opens with L2 and puts L3 second. It closes on the company setting thresholds and exception rules, with no guarantee of a lower workload. |
| 7. Onboarding separate | B2 | Done through A1 (separate denominator), L6 and E6 (comparable cohorts). |
| 8. Clinical and regulatory boundaries | B3 | The scope note is unchanged. The product-section boundary paragraph gains "or direct observation". The "What stays the same" bullet is removed. The eligibility FAQ is cut to two sentences without "not a medical device". The FXS-POPULATION paragraph is verbatim. |
| 9. Privacy claims | B4 | The two retention sentences are out of "Where FitXpress fits". The photos FAQ is rewritten in compliance.md §3 order: photos, then outputs and deletion by scan identifier, then the company's own copies, then the FAQ link. The FXS-IDS sentence and claim are removed. |
| 10. Generalized claims | B5 | The CDC paragraph now says it is not an error rate for an individual submission, and CDC is used twice. Also changed:<br>• "One possible pattern"<br>• "A program can combine methods."<br>• the hybrid sentence dropped<br>• "One approach collects…"<br>• "Common failure points"<br>• the B5 staff-time sentence<br>• "move part of the manual work", with manual review still applying. |
| 11. Article roles | B6 | Accuracy uses the §5 forms plus the framework link. Capture mechanics go through the FAQ link, privacy detail through the FAQ link, and conversion through the CTAs. |
| Language | C | Company / program / customer split applied. Acronyms used only once are written out: basal metabolic rate, application programming interface, software development kit, dual-energy X-ray absorptiometry. No em dashes, "so", "let", "plus" or "this article". |
| Line edits | D L1-L10 | L1 is not added. L2-L8 and L10 are verbatim. L9 is the verbatim H2. L5: "Where the costs come from" is the bullet label, and "three sources of cost" is in the Image 1 concept (see flag 4). |

### P3, SEO, GEO, FAQ, visuals

| Review item | Decision | What changed |
|---|---|---|
| Short answer | E1 | Three bullets as specified. L4 opens bullet 1. Bullet 2 uses "can come from". Bullet 3 is "How to estimate savings". |
| Title, meta | E2 | H1 is verbatim. The SEO title, meta description and OG/Twitter values belong to the publisher (meta.md); they are not in final.md. |
| FAQ | E3 | Four questions; the pilot-ROI question is new and first. FAQPage JSON-LD (Asel's Custom HTML) goes to the publisher. |
| Visuals | E5 | The cover line is unchanged. Image 1 is the new baseline vs pilot concept, labeled "Illustrative", with no figures. Image 2 is kept and labeled "Illustrative". |
| Final section | E6, D L10 | New H2, verbatim. It runs L10, then the pilot design (moved out of "When standardized measurement becomes cost-effective"), then the final CTA. About 70 words. |
| Introduction | E7 | The E7 text is verbatim. Then come v1's operations paragraph (now opening "Seen this way") with the telehealth AI link, the scope note and the early CTA. |

## Flags

Decisions not applied exactly as written:

1. **B3 protocol sentence, "(DXA)".** B3 quotes the sentence with "dual-energy X-ray absorptiometry (DXA)". DXA appears only once in the article, so I applied C (write the term out, drop the acronym): "Where a protocol requires dual-energy X-ray absorptiometry, BIA, a calibrated scale, or direct observation, that method stays in place." If the quoted form should win, put "(DXA)" back. Lint passes either way.
2. **Short-answer H2 has no text in the decisions.** v1's "Short answer: self-reported or verified body data" uses "verified" as an option, which A2 and E1 rule out outside question 1. I wrote "Short answer: self-reported data and the cost of checking it". Asel or Vadim should approve it. It touches the GSC "self-reported vs verified" family (H item 2).
3. **A5.2 mid CTA wording.** A5.2 calls `F` and `I` "setup costs". A1 defines `F` as monthly running costs and sources `I` from internal estimates. To stay consistent with A1, the CTA reads: "The scan fee `s`, running costs `F`, and the integration scope behind `I` come from [a conversation with 3DLOOK about scan volume and integration](…#bd-modal)."
4. **L5 "three sources of cost".** The phrase appears only in the Image 1 concept. v1's other occurrence (short-answer bullet 3) is replaced by E1's text, which does not carry it.
5. **C single-use acronyms kept where VERBATIM wins.**
   - RTPV appears once, inside A3's verbatim sentence.
   - BAA appears once, inside the verbatim FXS-HIPAA sentence, as in v1.
   - ROI is not expanded. It is not on the standard list, but E7 writes out "return on investment" and M1 passes.

Product and operational claims I could not trace to brand-assets, or that have no claim ID in the pack:

6. **Scan-estimated weight has no claim ID.** about-me.md lists Smart Scales weight as a software output. compliance.md §3 lists "weight- and BMI-related outputs". The pack's FXS-OUTPUTS text does not include weight, but "Each scan can also return body-composition estimates and a scan-estimated weight." carries the FXS-OUTPUTS marker. Product should add a claim ID, or confirm FXS-OUTPUTS covers it.
7. **RTPV and the three scan cells carry no claim marker.** The pack has no ID for them. The wording traces to the tech-spec.md "safer level" for new pages (2026-10-07, lines 54-61). Lint does not require a marker without a figure.
8. **Non-3DLOOK columns of the table are unsourced.** Self-report, connected scale and staff-observed are carried from v1 and are not traceable to brand-assets or the pack. Examples: "some models estimate body composition, often with bioelectrical impedance analysis (BIA); height is usually a separate input" and "No device at home, or readings that do not sync". These describe other methods, not FitXpress, and are hedged, but the review checklist asks to flag them.
9. **General operational statements without a source.**
   - "in-person appointment capacity does not automatically grow with enrollment"
   - the journey note "The full enrollment step, including the program's own onboarding inputs, can take longer."

   Both are hedged and give no number. The journey note is accepted by A3 and fits tech-spec Pattern A, where the host app owns onboarding. No brand-asset gives a full-journey duration.
10. **A4 sentence vs the live framework.** The new verbatim sentence says the accuracy figures describe body measurements. The live framework sentence (accuracy-formulations §1.1) says "across body metrics". The article uses §5 ("Across the evaluated body measurements"), so it is consistent with itself. The mismatch is the open item already on file in terminology-guardrails §2.13.
11. **CTA targets.** `#bd-modal` follows A5 and v1. landing-map rule 4 points demo buttons at `{landing}#demo` once `/fitxpress/for-telehealth/` is live with the shared form. When it ships, relink all three CTAs, per the rule 6 relink line.
12. **Retention denominator.** It is not named, because brand-assets has no definition. A1 only requires "its own denominator".

## For the publisher

- meta.md: apply E2 verbatim (SEO title, meta description, OG and Twitter). The live OG still carries January values.
- FAQPage JSON-LD: 4 questions, as an open item for Asel (Custom HTML block, a47f00e). Do not promise rich results.
- Article schema: author Vadim Bilan, keep the original datePublished, dateModified = republish date.
- Visuals to Kristina: the cover (unchanged), Image 1 (new) and Image 2 (Illustrative). Also the old banner_1 still shows "Eligibility Verified" and "Create Treatment Plan".
- Copy flags 1-12 into publish-package.md open items, and add the H section items for Vadim.
- plan.md and v1/ are untouched.

## QC fix pass 2026-11-02

seo-qc scored 18/20, ship with notes. Only the four requested fixes were made; review-1-decisions.md still wins.

1. **B1 paragraph.** L2 stays first and L3 stays verbatim. The rest collapses to two sentences:
   - "Measurement quality, repeatability, and capture usability, along with the company's thresholds and exception rules, decide how many cases reach manual review."
   - "The technology alone does not guarantee a lower review workload, and saved staff time counts only after the new step's costs."

   The paragraph now ends on the costs point. The mid CTA follows and names those costs (`s`, `F`, `I`).
2. **L7b.** Kept verbatim. The next sentence names the excluded costs: "Those are the running costs `F` and the one-time costs `I`." Then "Three results add them in: …" and the three formulas.
3. **Operations paragraph.** It now reads: "In telehealth patient monitoring, that cost falls on program leaders at telehealth, digital-health, and GLP-1 or weight-management providers, as reviewer time per submission." The keyword and the telehealth AI overview link stay in the paragraph, and it does not repeat the intro.
4. **Hedge stacking** (ROI section and short answer only).
   - The one stacked case, "When fewer cases need review, staff time may fall", went with fix 1.
   - Nothing else qualified. L2 and L4 are VERBATIM. Bullet 2's "can come from" is E1's mandated wording. "They can track it" (retention) is optional, not hedged.

The (Cover)/(Image N) lines are unchanged.

**Gates after the pass:**
- `article_lint.py`: PASS. Prose words 2,340, inside 1,950-2,350. Mean sentence 13.1 words, 2 over 25 (both VERBATIM), 0 over 35, no near-duplicate pairs.
- Detector: CLEAN, 0 hard fails, 0 markers.

The flags above are unchanged.
