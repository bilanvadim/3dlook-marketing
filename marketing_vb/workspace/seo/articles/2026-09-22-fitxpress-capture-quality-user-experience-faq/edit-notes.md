# Edit notes: fitxpress-capture-quality-user-experience-faq, review round 2 (seo-editor, 2026-09-23)

Inputs:
- `final.md`, which equals `v2/final.md` (the Doc's "Version 2" tab).
- `plan.md`, revised for review 2: 16 sections and 13 FAQ questions.
- `review-2.md` and `review-2-decisions.md`. The decisions file won everywhere, including over brief.md §7 and the pack's `excluded_topics` (P0).
- `review-1-decisions.md`, which stays in force: connected prose, no "still", no "so" as a result connector, no "see", blockquote illustrations, and section D.

Output: `final.md` with 2,431 prose words. v2 had 2,135. The target is 2,300, the lint band is 1,955-2,645, and the ceiling was ≤ 2,450. Round 1 notes are in `v2/edit-notes.md`.

Gates:
- `article_lint.py`: PASS on all 10 gates. The first pass failed only M1: the intro's plural "SDKs" did not count as expanding the first bare "SDK" in Q1. That was fixed in the second pass.
- Sentence stats: 144 sentences, mean 14.2 words, p90 22, 0 over 25, 0 over 35, no near-duplicate pairs.
- `detect-ai-tells.py --channel article`: CLEAN at 0.37/1000, rhythm 0.37. The one soft marker is the licensed RTPV clinical boundary in the Quick answers table, unchanged since round 1.

## Item by item

| Item | Decision | What changed | Where (final.md) |
|---|---|---|---|
| P0: brief §7 / pack `excluded_topics` conflict | ACCEPT (decisions override) | The three prospect progress questions are answered at about 150-170 words each. Presentation depth stays with the patient-engagement page, which is linked once in Q12 | L178-221 |
| P1: replace Q11 with three H3s | ACCEPT | Replaced by the three H3 strings from P1, byte-for-byte and in order, under the new H2 "Tracking and displaying progress". The previous H2 is renamed "Workflow integration and timing". The v2 output list is folded into the first question. FAQPage now has 13 questions | L141, L178-210 |
| P2: fat loss and lean-mass change | ACCEPT | Direct answer: body fat %, fat mass and lean mass estimates for each successful scan, compared between a baseline and a later scan along with selected body measurements. The FX-R2-LEAN correction is kept verbatim as two sentences, followed by "interfaces and supporting copy should use the term lean mass." Bullets cover 80+ body measurements, calculated BMI and BMR (height submitted, weight optional) and the 3D model. Body Progress compares two customer-selected scans by scan ID, and the customer decides whether tracking is enabled and how it is presented. The FXS-IDS sentence stays | L180-192 |
| P3: visual display | ACCEPT | The organization controls display (FX-R2-3D). The review's five-item list became four bullets: baseline and follow-up values are merged with change from baseline. Next come 3D shape against the numerical record, the tissue-boundary sentence (FX-R2-3D), one sentence on where composition changes come from, and the patient-engagement link | L194-205 |
| P4: 5/10/20 lb | ACCEPT with change | The reviewer's "does not apply a generic 5-, 10-, or 20-pound body transformation" is not used anywhere. Goal and target-weight visualization is mentioned in neither direction (grep `goal\|target\|transformation` in the body returns 0). The answer builds progress from each person's actual baseline and follow-up scans, because the same weight change maps differently. The weight source is named ("such as a clinic weigh-in or a self-reported entry"). Milestone thresholds and logic belong to the program, and FitXpress does not detect milestones by itself (FXS-SCOPE). The close is the reviewer's "without implying every pound lost came from fat" | L210-221 |
| P5: Quick answers Progress row | ACCEPT | Added as the last row. The first cell is verbatim. The second cell uses the decisions wording ("milestone views are built from each person's actual scans") | L58 |
| W1: opening | ACCEPT, one adjustment | The review's two paragraphs are used. The adjustment: "web and mobile software development kits (SDKs)" became "a web or mobile software development kit (SDK)", because gate M1 needs the singular expansion before Q1's "supported SDK". "The FAQ covers…" is deleted. The preparation paragraph and the scope note are kept | L39-45 |
| W2: "protect measurement accuracy" | ACCEPT | Now FX-R2-STANDARD verbatim: "The core capture flow in which RTPV operates is standardized to support consistent capture across users and scan sessions." | Q2, L81 |
| W3: Clothing Detector | ACCEPT | FX-R2-CLOTH is verbatim, and the paragraph opens with it. "Form-fitting or regular-fit clothing keeps…" became "Clothing that follows the body outline helps keep that outline visible". "Oversized" was dropped. The old sentence "When the detector flags… may direct" is deleted. The Quick answers Clothing qualification now reads "Clothing that does not follow the body outline can hide parts of it." and names no garment classes. Q7's "form-fitting clothing" became "fitted clothing" | Q4 L97-101; table L53; Q7 |
| W4: repeatability conditions | ACCEPT | "using similar lighting, camera placement, pose, distance, and clothing conditions at baseline and at follow-up supports comparable results" | Q5 L109 |
| W5: phone placement | ACCEPT | "The phone stands vertically on a stable surface around desk height." (FX-R2-PLACEMENT). "Table or counter" is gone | Q7 L137 |
| W6: integration step 3 | ACCEPT | Step 3 is FX-R2-SUBMIT verbatim. Steps 1 and 5 use "The organization" as the actor (v2 said "The customer…"). The prose API sentence is reduced to FX-R1-SDK wording ("…and through the API"), which drops the "server-to-server API that connects the organization's backend" architecture assumption | Q8 L149-161 |
| W7: existing photos | ACCEPT | FX-R2-UPLOAD verbatim replaces "A photo from the camera roll never passed through those checks…" | Q10 L176 |
| V1: keep Illustration 1 | ACCEPT | Unchanged, byte-identical | L70-71 |
| V2: replace Illustration 2 | ACCEPT | The evidence panel is deleted from Q5. The new blockquote goes after Q12, in the same R1 A5 format. It shows matching baseline and follow-up 3D models; body fat %, fat mass and lean mass; one or two circumference changes; and "Baseline", "Follow-up" and "Change" labels. No body region is coloured to suggest a tissue change, and all figures are illustrative placeholders | L207-208 |
| H: publish-pack housekeeping | FORWARDED to seo-publisher | Remove both designer briefs once the visuals are in. Set the Quick Answers table to about 30/35/35 columns with the smaller font. FAQ schema gets 13 questions, with Question.name equal to the visible H3 text. The internal links are unchanged. The editor did not touch meta.md | meta.md (publisher) |
| Word budget (≤ 2,450) | ACCEPT | Cuts made to stay under 2,450. Q5 lost the bridging sentence before the figure. Q9 lost "The flow has three stages:" and the closing total-time sentence (81 words). Q6 lost its closing aphorism ("Remote scanning is one way…"). Q7 merged its last two paragraphs | Q5, Q6, Q7, Q9 |

## Invariants (checked by diff and grep)
- H1 is unchanged. The first 10 H3 strings are byte-identical to v2 (`diff` of `grep '^### '` is empty), and the 3 new H3 strings are verbatim from P1.
- "FitXpress is not a medical device." appears once, verbatim. The CTA line is byte-identical.
- Links: the 5 internal links and the demo link each appear once (`uniq -c`). The patient-engagement link moved from old Q11 to Q12.
- Timing is defined once: "under 45 seconds" from the photos to structured results (table, Illustration 1, Q9). No other figure appears.
- There are no client names. In the body, "still", "so" and "see" occur 0 times.
- "Muscle mass" occurs twice: in the Quick answers qualification and in the Q11 terminology correction. "Muscle tissue" occurs once, in the Q12 tissue-boundary sentence. "Muscle" appears on its own inside the lean-mass definition.

## Claim markers
- Added: FX-R2-PLACEMENT, FX-R2-STANDARD, FX-R2-CLOTH, FX-R2-SUBMIT, FX-R2-UPLOAD, FX-R2-LEAN (Q11 and the table's Progress row), FX-R2-3D (Q12, twice).
- Dropped: FX-R1-CLOTH, whose text FX-R2-CLOTH supersedes. FX-CQ-004 is removed from `claims_verified` because it has had no marker in the text since round 1.
- Used (25): FXS-SPEED, FXS-OUTPUTS, FXS-DELIVERY, FXS-LIFECYCLE, FXS-IDS, FXS-SCOPE, FXS-MEDICAL, FX-CQ-002, FX-CQ-003, FX-CQ-005, FX-CQ-006, FX-CQ-007, FX-CQ-009, FX-R1-FLOW, FX-R1-CORE, FX-R1-SDK, FX-R1-ADMIN, FX-R1-UPLOAD, and the seven FX-R2 IDs. Lint claim traceability: ok.

## New wording without its own claim ID (coordinator: legalize or confirm)

| Wording | Source | Marker |
|---|---|---|
| "Programs track change by comparing these estimates between a baseline scan and a later scan, together with selected body measurements." | review-2 P2 text | none (program action) |
| "For that reason, interfaces and supporting copy should use the term lean mass." | review-2 P2 text | none (copy guidance) |
| "…and the program designs its progress view around them." / "Changes in body composition come from the estimates shown beside the models." | review-2 P3 | none |
| "such as a clinic weigh-in or a self-reported entry" (examples of a weight source) | editor, from brief §9 "identify the weight source" | none |
| "FitXpress returns scan outputs and does not detect milestones by itself." | review-2-decisions P4 / brief §9 | FXS-SCOPE |

## §16 QA (plan Section 16 and page-level checks)
- Next steps: the pilot sentence is unchanged, and the CTA is verbatim and appears once. There is no second CTA anywhere in the body.
- FAQPage: 13 H3 questions (Sections 3-15), in the P1 order after Q10. The schema answer should be the full visible answer text (publisher).
- Keyword: "capture quality" appears in H1 and in the H2 "How FitXpress controls capture quality". "Body scan app" and "body measurement app" each appear once, both unchanged from v2.
- Abbreviations are expanded at first use: SDK, API, RTPV, BMR. BMI is not expanded.
- Boundaries: RTPV posture, lean mass versus muscle mass, the 3D model is not a tissue map, the medical device sentence, and the scope note. Corrective negation is used only for these product and clinical boundaries.

## Open items
1. For Vadim (P4): should the optional target-weight visualization be mentioned in Q13 as a clearly labelled projection? It is currently absent in both directions.
2. For the coordinator: the five new wordings in the table above have no claim ID.
3. Style: all three progress answers use the same shape: direct answer, short bullet list, then a boundary sentence. The review sets them out as checklists, so the bullets stay. A human editor may still want to vary one of them.
