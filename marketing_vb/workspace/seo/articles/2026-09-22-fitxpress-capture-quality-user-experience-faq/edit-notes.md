# Edit notes: fitxpress-capture-quality-user-experience-faq, review round 1 (seo-editor, 2026-09-23)

Input: `final.md` = `v1/final.md` (the Doc's "Version 1" tab), plus `review-1.md` and `review-1-decisions.md`. Where the two disagree, the decisions file won (C8, C9, C13).
Output: `final.md`, 2,135 prose words (v1 had 2,039; the target band is 1,785-2,415).

Gates: `article_lint.py` PASS, all 10 gates. Sentence stats: mean 14.3 (v1: 12.2), p90 22, 0 sentences over 25 words, 0 over 35, 127 sentences, no near-duplicate pairs. `detect-ai-tells.py --channel article` CLEAN, 0.43/1000, rhythm 0.37. The one soft marker is the licensed RTPV clinical boundary in the Quick answers table. The first pass FAILed on monotone rhythm (0.34), and the second pass fixed it.

Self-check grep: `grep -niwE "still|so|see" final.md` returns nothing, frontmatter included.

Invariants were checked by diff against v1:
- The H1, the 3 H2 group headings, Next steps and the 11 H3 strings are byte-identical, and the 11 H3s are the FAQPage `Question.name`.
- The Quick answers table has the same 3 columns and 7 topic rows. Cells were edited per A2 and C13.
- "FitXpress is not a medical device." appears once, verbatim.
- The CTA line is byte-identical.
- The 5 internal links and the demo link each appear once.

Claim IDs:
- Dropped: FX-CQ-001, FX-CQ-008, FX-CQ-010 and FXS-POPULATION, as expected. FXS-ACCURACY and FXS-REPEAT were not used in v1 either.
- Still used (14): FXS-SPEED, FXS-OUTPUTS, FXS-DELIVERY, FXS-LIFECYCLE, FXS-IDS, FXS-SCOPE, FXS-MEDICAL, FX-CQ-002 to FX-CQ-007, and FX-CQ-009.

## Item by item

| Review item | Decision | What changed | Where (final.md) |
|---|---|---|---|
| A1: reads like a presentation, facts with no connection | ACCEPT | Every answer was rewritten as linked prose, and each answer still opens with its direct answer in sentences 1-2. The links are stated relationships: "because every scan … follows the same instructions", "which allows problems to be corrected during capture", "the phone's angle is a separate requirement … which concerns the device, while RTPV concerns the person", "Capture-quality controls act before processing, while accuracy and repeatability describe the results", "Privacy at home matters too, because…". Paired v1 declaratives were merged, for example "Capture runs only through… / Every scan follows…" → Q1 ¶2. Mean sentence length went from 12.2 to 14.3 words (target 14-16), with none over 25 | whole body, intro to Next steps |
| A2: "still" overemphasizes | ACCEPT | Removed from the table's Photo capture, Clothing and Self-scanning cells, from the intro, and from Q1, Q3, Q6 and Q7 (v1 had it 9 times). The count is now 0. The Self-scanning cell reads "…affect completion." "Anyway", a similar diminishing adverb, was cut from Q3 too | table L49-54; prose |
| A3: "so" as a result connector | ACCEPT | The v1 sentence "Implementations that do so see…" is gone (C1). The word "so" appears 0 times | Q1 |
| A4: "see" | ACCEPT | Same sentence deleted. "See" appears 0 times. Every link anchor sits inside a sentence | Q1 |
| A5: illustration formatting | ACCEPT | Each illustration is its own blockquote with a bold bracketed label and a "Designer brief:" line, with a blank line before and after. Illustration 1 uses the C13 timing definition and puts clinical review in "the organization's workflow". Illustration 2 carries definitions and no figures | L67-68, L116-117 |
| C1: "SDK only" + custom flows "meaningfully worse accuracy" | ACCEPT | Now reads "In the standard end-user flow, capture runs through the supported SDK, which provides these guided capture controls." The accuracy comparison was deleted, and FX-CQ-001 is gone | Q1 ¶2, L63 |
| C2: RTPV presented as pose + framing + tilt | ACCEPT | RTPV = position and framing (Q2 ¶1). Phone tilt is covered by the SDK's guidance as a separate requirement: "Phone angle is a separate requirement. The SDK's guidance also covers phone tilt…" (FX-CQ-006, pose and tilt validation). No gyroscope is mentioned | Q2 ¶1-2, L72-74 |
| C3: skeletal tracking + face obfuscation | ACCEPT | Sentence deleted. Face obfuscation now appears 0 times, and the privacy FAQ stays linked in Q8 | Q2 |
| C4: "not customizable" | ACCEPT | Now reads "The organization controls and brands the surrounding experience, including onboarding, user instructions, and the results display. The core capture flow where RTPV runs is standardized, a design decision intended to protect measurement accuracy." (FX-CQ-004). There is no "not customizable" and no disabled tutorial | Q2 ¶4, L78 |
| C5: real-time correction blended with retakes | ACCEPT | Q3 opens with correction during capture (prompts plus three bullets). A separate paragraph covers the second case: "A capture that is completed and later turns out to be unusable is a different case…", and the program decides how the next attempt is offered. Q6 owns the failed-scan route. Nothing says which conditions block capture | Q3, L82-90 |
| C6: sport/regular/oversized, prompts, payload | ACCEPT | Q4 now opens with the reviewer's wording, split in two: "The Clothing Detector is a capture-quality feature. It identifies clothing conditions that may interfere with capture and can prompt corrective action." The three classes and the payload sentence were dropped. The body-outline explanation and the onboarding instruction stay | Q4, L94-98 |
| C7: "single biggest factor" | ACCEPT | Deleted. Replaced by: "No single public percentage or ranking describes the effect of individual capture conditions." | Q5 ¶1, L104 |
| C8: accuracy block duplicates the framework | ACCEPT as decided | Q5 keeps the three definitions and one proof point, the repeatability figure (FX-CQ-009). The 96-97% / 1.5-2.0 cm sentence and FX-CQ-010 are gone. The standalone "do not guarantee" paragraph was folded into the figure paragraph, and the framework link sits in that same paragraph ("sets out the validation figures, the tested population, and the methodology"). Q5 is about one paragraph shorter, and the accuracy gate passes | Q5, L106-114 |
| C9: disability sentence | ACCEPT for this article (the decisions file records a partial disagreement on the reason) | The FXS-POPULATION paragraph was deleted. The practical guidance stays with no claim attached: "Accessibility planning matters most for users whose mobility or health makes the standing capture positions difficult. For those users, a documented alternative measurement path gives them a way to continue." | Q6 last ¶, L131 |
| C10: "indoor lighting is fine, any background works" | ACCEPT | Replaced with "Users should follow the on-screen guidance for lighting, distance, framing, and phone placement." The phone-on-a-flat-surface detail (FX-CQ-007) stays | Q7 ¶2, L137 |
| C11: "Camera SDK (React)…"; Admin Panel | ACCEPT | Now reads "Integration runs through web and mobile SDKs, including supported iOS and Android integrations, and through a server-to-server API…" and "The optional FitXpress Admin Panel complements that integration as an interface for monitoring and exporting results." React appears 0 times | Q8, L158 |
| C12: "server-side only… submission confirmation" | ACCEPT | Replaced with "The organization controls which outputs appear in its interface and how they are routed for review." FX-CQ-008 is gone | Q8, L160 |
| C13: timing definitions | PARTLY REJECT (canon wins) | One definition across the page: structured results in under 45 seconds from the front and side photos (FXS-SPEED). It appears in 3 places: the table Timing row, Illustration 1 and Q9. The Q9 stage bullet was renamed "From photos to results" (v1 said processing only). Onboarding "depends on the organization's own screens", and capture time varies by user. The page has no "under a minute" and no other figure | table L55, L68, Q9 L168-174 |
| C14: "camera roll is disabled" | ACCEPT | Replaced with the reviewer's sentence verbatim: "Users cannot upload existing photos in the standard guided FitXpress capture flow." The explanation of why guided capture matters stays, with no fraud framing | Q10, L180 |
| Cannibalization note: shorten the accuracy subsection | ACCEPT (with C8) | Q5 is shorter by one proof-point sentence pair and one paragraph | Q5 |

## New wording that makes a product statement (the coordinator adds these to the pack)

The claim markers point to the nearest existing ID, but the wording itself comes from the review:

| Wording in final.md | Source | Marker used |
|---|---|---|
| "In the standard end-user flow, capture runs through the supported SDK, which provides these guided capture controls." | review-1 C1 / decisions C1 | FXS-DELIVERY |
| "The SDK's guidance also covers phone tilt…" (tilt as a check separate from RTPV) | decisions C2 (tech-spec.md "pose / tilt validation") | FX-CQ-006 |
| "The organization controls and brands the surrounding experience, including onboarding, user instructions, and the results display. The core capture flow where RTPV runs is standardized…" | review-1 C4 / decisions C4 | FX-CQ-004 |
| "It identifies clothing conditions that may interfere with capture and can prompt corrective action." | review-1 C6 (verbatim, split after "feature") | FX-CQ-003 |
| "No single public percentage or ranking describes the effect of individual capture conditions." | review-1 C7 | none (a statement about the evidence, not about the product) |
| "Users should follow the on-screen guidance for lighting, distance, framing, and phone placement." | review-1 C10 (verbatim) | FX-CQ-007 |
| "web and mobile SDKs, including supported iOS and Android integrations" | review-1 C11 (verbatim) | FX-CQ-005 |
| "The optional FitXpress Admin Panel complements that integration as an interface for monitoring and exporting results." ("exporting" is new) | review-1 C11 / decisions C11 | FXS-DELIVERY |
| "The organization controls which outputs appear in its interface and how they are routed for review." | decisions C12 (the reviewer wrote "customer") | none |
| "Users cannot upload existing photos in the standard guided FitXpress capture flow." | review-1 C14 (verbatim) | FX-CQ-006 |
| "structured results in under 45 seconds from the front and side photos" | decisions C13 (canon FXS-SPEED, "time from photo to results") | FXS-SPEED |

No reviewer sentence over 25 words was split, except C6. C6 was split in two at "feature" (21 words → 7 + 14) to keep the Clothing Detector's feature label in its own sentence.

## §16 final editorial QA

1. **The article covers capture reliability, not general telehealth: PASS.** Telehealth appears only in Q8 and in its link. Q8 gained no deployment marketing: the server-side pattern (FX-CQ-008) was removed.
2. **The progress questions have not grown into a competing progress article: PASS.** Q11 is unchanged in scope: 5 bullets, 2 sentences and the patient-engagement link.
3. **RTPV is not described as clinical posture analysis: PASS.** The brief's boundary is verbatim in Q2 and in the table cell. RTPV is now scoped only to position and framing.
4. **Clothing Detector claims are not overstated: PASS, and narrower than v1.** It only identifies conditions and can prompt corrective action. There are no fit classes and no payload. The text says "Some garment issues fall outside what the detector identifies."
5. **Accuracy, repeatability and capture quality stay distinct: PASS.** Q5 gives three definitions plus a sentence on where each one sits (capture quality before processing, the other two on results). It carries one figure, in the §5 short form with "internal", and the framework link is in the same paragraph.
6. **"Lean mass" is not replaced with "muscle mass": PASS.** "Muscle" appears only inside "musculoskeletal" in the RTPV boundary.
7. **Predicted weight appears only with Smart Scales: PASS.** It appears 0 times.
8. **Timing claims are consistent: PASS.** "Under 45 seconds from the photos" is the only timing figure, and it appears 3 times with the same definition. The page contains no "minute", no "40 seconds" and no processing-only definition.
9. **FitXpress supports professional review and does not make decisions: PASS.** This holds in the intro scope line, the table Workflow row, Q8 step 6 and Q8 ¶5 (decision ownership named: "stay with the customer's clinicians or other designated decision-makers").
10. **The article links to the accuracy, telehealth, patient-engagement and privacy pages: PASS.** Each is linked once, plus the two-photo mechanics page and the demo. The telehealth URL is the current one, not the 301.
11. **The FAQ schema matches the visible FAQ exactly: PENDING (publisher).** The H3 strings are unchanged, so `Question.name` stays as it was. Every answer text changed in this round, so the schema `acceptedAnswer` values must be regenerated from this final.md.

Terminology pass:
- Corrective negation: only the licensed RTPV clinical boundary (table, Q2).
- "rather than", "you", "we/our", "buyer" and "positioned as": 0 each.
- "customer" appears only in a deployment or contract role (Q8 steps 1, 3 and 5; decision ownership) and in Body Progress, where the brief requires it.

## Open items

- **Product: one central timing definition (C13).** The reviewer notes that live pages mix 40 s, 45 s and "under a minute". This page follows canon (FXS-SPEED, "from photo to results").
- **Product: Clothing Detector classes and payload field (C6).** If sport/regular/oversized and the payload field are confirmed, they can come back to Q4 (FX-CQ-003 / FXS-LIFECYCLE already hold them).
- **Vadim: the disability sentence (C9).** The reviewer wants Product and Legal sign-off. The sentence is canon (accuracy-formulations.md §5) and is live on the occupational-health intake article. It was removed here only.
- **Pack: legalize the reviewer wording** listed above. "Exporting results" for the Admin Panel is the one product capability that canon does not state anywhere (FXS-DELIVERY says "centralized view").
- **Feature names** (carried over from v1): canon does not attest "Real-Time Pose Validation (RTPV)" or "Clothing Detector" as names. Both come from the brief and are kept, and the reviewer accepted both.
- **Lint note (tooling, not article):** `article_lint.py` `_SENT_SKIP` recognises `(Image N)` and `(Cover)` placeholders, but not the new `> **[Illustration N: …]**` blockquote format. The two illustration blocks are therefore counted as prose: 4 sentences and roughly 70 words in the gate numbers above. They pass either way, but the skip pattern should learn the new label if A5 becomes the house format.
