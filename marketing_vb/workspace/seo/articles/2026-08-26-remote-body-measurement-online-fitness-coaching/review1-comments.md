---
artifact: review1-comments
slug: remote-body-measurement-online-fitness-coaching
source_doc: https://docs.google.com/document/d/18OTBvrxBuDgvU7MLBVL7Yd5Odh6v7RHgA3rqqhzwYpE/edit?tab=t.juwxysonmspb
source_tab: "Review 1"
reviewed_version: review1-version1.md (== draft-v2-final.md body, the text inside publish-package.md)
synced: 2026-08-31
status: verbatim copy of the reviewer's text, no edits
---

# Review 1 — verbatim

Overall assessment: the article meets the basic brief and MOFU/BOFU intent, but it needs targeted revision before publication. Its main weakness is that it still reads partly like another general fitness/body-scanning article instead of a focused guide for remote coaching operations.

## Priority recommendations

### 1. Sharpen the differentiation

Keep the article strictly focused on:

- coach and platform workflows;
- onboarding and recurring check-ins;
- how coaches review the data;
- integration and implementation;
- pilot evaluation;
- limitations for coaching decisions.

The "Why this matters now" and general fitness-industry discussion overlap with the existing [AI-in-fitness hub](https://3dlook.ai/content-hub/ai-in-fitness-industry/). Shorten or remove that section.

There is also overlap with the older [AI-powered fitness tracking article](https://3dlook.ai/content-hub/ai-body-scanning-for-fitness/). Consider redirecting or rescoping that older page separately.

### 2. Improve the article order

Recommended structure:

1. Introduction and scope
2. The measurement problem in remote coaching
3. What remote body measurement provides
4. How it fits the coaching workflow
5. How coaches can use the results
6. Comparison with scales, tape measurements, photos, BIA, and DXA
7. Where FitXpress fits
8. Accuracy, repeatability, privacy, and implementation
9. How to evaluate a pilot
10. Best-fit programs and limitations
11. FAQs
12. Conclusion and CTA

Move "Where FitXpress fits" later. The current placement makes the article product-led before the reader has completed the evaluation journey.

### 3. Correct or qualify product statements

- Describe body fat percentage, lean mass, and fat mass as **body-composition estimates**, rather than simply "body composition."
- Separate:
    - model-generated body measurements;
    - software-derived body-composition estimates;
    - calculated outputs such as BMI and BMR;
    - predicted weight;
    - the 3D model.
- Weight is optional in supported workflows. Avoid presenting weight and age as universally required inputs.
- Replace "average error margin of ±3.5%." The approved claim is approximately 3.5% average prediction error under evaluated conditions. The ± symbol implies a different statistical meaning.
- Replace the broad "repeatability is typically < 1 cm" claim with:
  "For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm."
- Identify the 96–97% accuracy figures as results from **internal validation against expert manual measurements**.
- Use **dual-energy X-ray absorptiometry (DXA)**, not DEXA.
- Use the approved wording: "FitXpress is not positioned as a medical device."
- Verify privacy wording against the current [FitXpress Privacy Policy](https://3dlook.ai/fitxpress-privacy-policy/).

### 4. Remove unsupported commercial claims

The following statements are too absolute without direct evidence:

- "Progress a client cannot see is progress they stop paying for."
- "Retention is the number that decides whether an online coaching business survives its second year."
- "Acquiring a new client costs more every year."
- "A subscriber who renews for a year is worth several who churn."
- "A client…has a concrete reason to renew."
- "Visible progress supports retention."

Present engagement and retention as outcomes that platforms can test, rather than guaranteed effects.

### 5. Add more decision-making value

Add a compact table showing:

| Coaching stage | Data reviewed | Possible coach action | Limitation |
| :- | :- | :- | :- |
| Onboarding | Baseline measurements and 3D model | Establish the starting record | Does not prescribe a program |
| Recurring check-in | Measurement and composition trends | Review progress with other client data | Small changes require context |
| Apparent plateau | Weight plus regional measurements | Investigate different progress signals | Cannot determine the cause |
| Program completion | Full longitudinal comparison | Summarize progress | Avoid causal conclusions |

Also add practical pilot metrics:

- scan completion and retake rates;
- usable baseline-to-follow-up comparisons;
- coach review time;
- scheduled check-in completion;
- support requests;
- client use of the progress view;
- engagement or retention measured against a baseline.

This would make the article considerably more valuable to product and operational buyers.

### 6. Refine the method-comparison table

- Connected scales should not be described as providing only "one number"; many also provide body-composition estimates.
- Clearly distinguish consumer smart scales from professional BIA.
- Present mobile scanning as complementary to scales, BIA, and DXA.
- Avoid calling DXA the universal reference for every coaching workflow.
- Add the existing [2-Photo vs Video vs Hardware comparison](https://3dlook.ai/content-hub/body-scanning-technology-comparison/) as the relevant sideways link.

### 7. Reduce repetition

The following points appear several times:

- 80+ measurements;
- results in under 45 seconds;
- repeatability under 1 cm;
- visible progress and retention;
- privacy and photo deletion;
- the coach makes the final decision.

State each major product claim once in the main body and, where useful, once in the FAQ.

### 8. Adjust the tone

Remove or soften:

- "easy to misrepresent, whether on purpose or not";
- "an invisible result is a cancelled renewal";
- "The split is clean";
- "Small real changes survive measurement noise";
- "a coach can point to it and defend it."

These formulations sound accusatory, promotional, or more certain than the evidence allows.

With these changes, the article would become a strong cluster piece: more specific than the fitness hub, more useful to platform buyers, and better aligned with the intended MOFU/BOFU role.
