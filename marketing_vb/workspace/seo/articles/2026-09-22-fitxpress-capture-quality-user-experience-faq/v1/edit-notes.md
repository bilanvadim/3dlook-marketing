# Edit notes: fitxpress-capture-quality-user-experience-faq (seo-editor, 2026-09-22)

Input: draft.md (2,046 prose words, lint PASS, detector CLEAN 0.44). Output: final.md (2,039 prose words, lint PASS, detector CLEAN 0.44, one soft marker: the licensed RTPV clinical boundary in the Quick answers table). Sentence gate: mean 12.2, p90 18, over 25 words: 0, over 35: 0. No near-duplicate pairs left.

Invariants kept: 11 H3 strings byte-identical to the draft (diffed); "FitXpress is not a medical device." once, verbatim; CTA verbatim; 6 links once each (5 internal + demo); all 18 claim markers intact; no new claim IDs.

## What changed and why

| Where | Change | Why |
|---|---|---|
| Intro | "…ask one question… Can users…?" became one statement | Reframe as a plain statement (about-me, editorial-rewrites §4) |
| Intro | "It does not remove the need for…" became "The program still needs…" | Positive frame; one fewer negation |
| Intro scope line | Now "provides structured body data for review by the organization's care team. Clinical interpretation stays with that team." | Lint near-duplicate with Q8 (0.71). Q8 keeps the decision-ownership sentence |
| Q1 | The two consistency sentences became one. Cut "The capture step shapes the output". Custom camera flow now "removes those checks" | Repetition, aphorism (§2, §4). The mechanism comes from FX-CQ-001 with no new claim |
| Q1 | "Guidance narrows the ways a scan can go wrong" became a statement with the hedge at the end | Slogan, §5 hedge placement |
| Q2 | Pack wording: "protects measurement accuracy" (was "consistency") | FX-CQ-004 text |
| Q3 | "The user is asked to step back" became "may be asked" | Examples stay generic. No invented error messages |
| Q4 | Classification stated once in the direct answer (was twice). "The flag also travels with the results" became a payload sentence | Repetition; attributed behaviour (§1.6) |
| Q5 | "depend on" became "vary by" in the conditions sentence. Framework anchor sentence now says it sets out the reference behind each figure | Varied relationship verbs. The framework page does not publish the full methodology |
| Q7 | Cut "The setup is simple". Replaced "described above". Privacy at home now a concrete condition | Promotional filler; page reference (§3); added a practitioner caveat |
| Q8 | Direct answer says "its own product" (no repeat of step 1). Prose uses "organization" where no deployment or legal role is meant | Lint pair L140~L144; terminology §2.12 |
| Q8 boundary | Kept as "Clinical assessment, treatment, and eligibility decisions stay with the customer's clinicians or other designated decision-makers." | Carries the "does not diagnose / does not determine treatment or eligibility" requirement without the banned `diagnos*` stem. The actor owns the decision (editorial-rewrites §5). No stacked negation |
| Q9 | Bullet label "Front and side photo capture" became "Photo capture" | "front and side" 6 → 4 |
| Next steps | Slogan line replaced with a pilot recommendation | Actionable close; no restated central message |

## §16 final editorial QA, item by item

1. **The article covers capture reliability, not general telehealth: PASS.** Telehealth appears only as the context in Q8 and in one link. Every H3 is about capture, retakes, conditions, timing or integration mechanics.
2. **The progress questions have not grown into a competing progress article: PASS.** Q11 is five bullets and two sentences, then the patient-engagement link. There are no milestones, no fat-versus-lean tracking and no visual display section.
3. **RTPV is not described as clinical posture analysis: PASS.** The brief's boundary sentence is verbatim in Q2, and the table row says "not a clinical posture assessment". Nothing calls it motion analysis, health assessment or validation.
4. **Clothing Detector claims are not overstated: PASS.** The text covers fit classification (sport, regular, oversized), a flag with a prompt, the classification in the payload, and a flow that "may" direct a change or retake. It states that the classification "will not catch every garment issue". There is no measuring through clothing, no "prevents manipulation" and no automatic rejection.
5. **Accuracy, repeatability and capture quality stay distinct: PASS.** Q5 gives three definitions. The figures use the §5 short forms with "internal" and the reference. The framework link is in the same paragraph. There is no ISO benchmark.
6. **"Lean mass" is not replaced with "muscle mass": PASS.** "Muscle" appears 0 times.
7. **Predicted weight appears only with Smart Scales: PASS.** Predicted weight and Smart Scales both appear 0 times.
8. **Timing claims are consistent: PASS.** The only figure is "under 45 seconds" (table, image caption, Q9). No other duration appears.
9. **FitXpress supports professional review and does not make decisions: PASS.** This holds in the intro scope line, the table Workflow row, Q8 step 6 and the Q8 boundary paragraph.
10. **The article links to the accuracy, telehealth, patient-engagement and privacy pages: PASS.** Each is linked once, plus the two-photo mechanics page and the CTA. The telehealth URL is the current one, not the 301.
11. **The FAQ schema matches the visible FAQ exactly: PENDING (publisher).** final.md has no schema block. The 11 H3 strings are unchanged from the plan and draft, so Question.name can be copied verbatim. The schema answers must be the final.md answer text, which changed in Q1, Q2, Q4, Q7 and Q8. The Quick answers table stays out of the FAQPage.

## Canon wording not in the pack (for the coordinator to legalize)

- "expert pattern-maker tape measurements" and "reported accuracy was approximately 96-97%, with a typical absolute error of 1.5-2.0 cm depending on the body part". Source: `brand-assets/product-info/accuracy-formulations.md` §5 (approved short form). The pack's FXS-ACCURACY holds the §1.1 wording. The writer used this in the draft and I kept it. Same claim, different approved form.
- "typical scan-to-scan differences remained below 1 cm for most of the evaluated measurements". Source: `accuracy-formulations.md` §5 short form of FXS-REPEAT. The writer used it and I kept it.
- I added no new canon sentences.

## Open items

- **Feature names.** The pack's `unconfirmed_product_behavior` says canon does not attest "Real-Time Pose Validation (RTPV)" or "Clothing Detector" as named features. Canon uses lowercase descriptive phrasing. The external brief (§6, §8) requires both names, so both are kept. Vadim should confirm them before publication.
- **BMI with optional weight.** Q11 says "where the required inputs are provided. Height is submitted with the scan; weight is optional." Brief §8 wants the weight input and calculation basis to be clear. If BMI can come from a weight that is not user-submitted (Smart Scales predicted weight), Q11 needs a product confirmation. The current wording stays within canon.
- **plan-audit.md was not read.** The seo-editor role file tells the editor not to read it. The coordinator's task message listed it, and the two instructions conflict. I followed the role file, and plan.md covered what the edit needed.
