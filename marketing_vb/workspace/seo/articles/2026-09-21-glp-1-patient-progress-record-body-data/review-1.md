---
source: Google Doc 1XHsliNuHRPpzHW-64oawgiQQ-Y1lQ6dG3jaIAJ0AFR8 ("Article - What Body Data Should Be Included in a GLP-1 Patient Progress Record?"), tab "Review 1" t.82jxayv19e2i
reviewer: Asselya Sekerova (Slack DM D0A1Q2E02P3, thread 1790010074.288389, ts 1795516746.354789, 2026-11-24: "Review 1 для агентов")
fetched: 2026-11-24 via oo googledocs get_document_by_id include_tabs_content=true
base_text: tab "Version 1" t.7fxnr9awl16u = v1/final.md (word-level diff 2026-11-24: only our claim comments and list numbering differ; the reviewer made no edits to the text)
note: verbatim extraction; headings as in the Doc; links shown as in the Doc text
---

# Review 1: GLP-1 patient progress record
The draft of 21.09 was checked against the rules that changed after it was written: landing-map.md (incl. the two-CTA rule of 2026-11-23), roadmap.md (2026-11-11), tech-spec.md (capture-feature wording, 2026-10-07 level), compliance.md, accuracy-formulations.md §5, the terminology sync of 2026-09-28 and the v3.0 plan row.
Detector baseline before edits: 0 markers, 0 hard fails, mean sentence 14.7 words. Keep it that way.
Priority: BLOCKING items must be applied before publishing. SHOULD items are applied unless they conflict with a canon file; if so, record the conflict in Open items. OPTIONAL is the editor's call.

## R1-1 · BLOCKING · Capture log claims exceed approved feature status
Rule: tech-spec.md (Clothing Detector status line, "Superseded on new pages since 2026-10-07") and roadmap.md (Clothing Detector row). On new pages the returned record is described only as "processing status and timestamps". No pose or framing validation results, no clothing information, no payload classes. Face obfuscation belongs to the privacy FAQ, not to the record.
Remove from the article everywhere: capture-quality flags, pose-validation flags, clothing classification, face-obfuscation confirmation, request metadata, "failed pose validation", "usable pose".
Reframe (keep the three-group structure): FitXpress returns processing status, a timestamp and the scan identifier. The program logs what it controls itself: the version of the capture instructions and whether a manual fallback replaced the scan.
Replacements:
- Short answer, third bullet.
- Old: * **Logged about the capture.** Capture-quality and pose-validation flags, clothing classification, face-obfuscation confirmation, and processing logs with timestamps and request metadata.
- New: * **Logged about the capture.** Processing status, a timestamp and the scan identifier for each entry. The program adds what it controls: the version of the capture instructions and whether a manual fallback stood in for the scan.
- Short answer, closing line.
- Old: The first two groups describe the patient. The third describes the conditions of the capture, which is what tells a coordinator whether the entry can be used.
- New: The first two groups describe the patient. The third records what happened to the capture, which tells a coordinator whether the entry can be used.
- Section "The capture log": rewrite both paragraphs. Required content, in this order:
- Processing status tells the team whether a scan produced results before anyone compares it. A failed scan then reads as a known gap in the timeline; without the status, the same time point can read as a result.
- Timestamps place each entry on the timeline. The scan identifier makes one entry retrievable months later, when a partner asks about a single time point.
- The program's own note on capture instructions and manual fallback is what shows whether two entries were taken under the same protocol.
- Optional capture-side sentence, approved wording only: During capture, Real-Time Pose Validation (RTPV) gives pose and framing guidance. Do not describe RTPV output as part of the record. Do not mention voice prompts (native apps still in testing).
- Keep the last sentence about the first entry setting the starting point.
- Audit list.
- Old: * How many entries were captured with a usable pose?
- New: * How many entries returned a completed processing status?
- "Where FitXpress fits", last paragraph.
- Old: Either route delivers the entry in the same shape, structured and timestamped, with the capture-quality flags and processing logs attached.
- New: Either route delivers the entry in the same shape, structured and timestamped, with its processing status and scan identifier.
- Next steps.
- Old: The third group, the fields that describe the capture, is the one a record assembled from several sources rarely holds.
- New: The third group, the fields that record what happened to each capture, is the one a record assembled from several sources rarely holds.
Check after edit: grep the article for flag, clothing, obfuscation, pose, metadata. Only the optional RTPV sentence may remain.

## R1-2 · BLOCKING · Landing link position and the two CTAs
Rule: landing-map.md rules 1, 2, 4, 6 and blog-style-guide.md §5 (two CTAs per article, 2026-11-23). Hub 3 row: landing /fitxpress/for-glp-1-programs/ is planned; "Link now" and "Demo button now" are both https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/.
Current state: the only down link sits at ~53% of body words, with anchor "structured body data for telehealth and digital health programs" (not from the anchor list). The closing CTA goes to /pricing/#bd-modal-personalized, which the rule does not allow.
Fixes:
- Early CTA. Insert a short CTA block directly after the "Short answer" section (before "Why each group of fields earns its place"). It links to the Link-now URL with anchor body composition tracking for GLP-1 programs. BOFU wording, one or two sentences, actor = the program. Example: Programs that want these fields delivered into their own patient record can review [body composition tracking for GLP-1 programs](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/) and book a FitXpress demo. Optional, only if it fits the sentence: 3DLOOK has worked with 100+ clients. No other client-count form.
- Later mention in "Where FitXpress fits".
- Old: Programs evaluating that route can start from [structured body data for telehealth and digital health programs](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/).
- New: Programs evaluating that route can start from [remote progress tracking for GLP-1 clinics](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/).
- Closing CTA.
- Old: Then [talk to 3DLOOK about the GLP-1 progress record workflow](https://3dlook.ai/pricing/#bd-modal-personalized).
- New: Then [book a FitXpress demo](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/) to see how the record arrives in the program's own platform. Never /pricing/, /contact-us/ or a form made for this article.
- Open items (publish-package): Relink when /fitxpress/for-glp-1-programs/ goes live: body composition tracking for GLP-1 programs → /structured-body-data-for-telehealth-digital-health-programs/ (and the same for the closing CTA and the "Where FitXpress fits" anchor).
Check: article_package.py checklist item cta_placement passes (landing link within the first 30% of body words and in the last H2 section).

## R1-3 · BLOCKING · Photos contradict the retention canon
Rule: compliance.md lifecycle table. Photos are deleted immediately after processing or within 30 days, per the customer's instructions. Outputs are stored. The draft says each photo "stays in the entry as its own field".
- Old: * **Submitted with the capture.** Front and side photos, gender, height, and an optional self-reported weight. Each one stays in the entry as its own field.
- New: * **Submitted with the capture.** Front and side photos, gender, height, and an optional self-reported weight. Gender, height and weight stay in the entry as their own fields. The photos are the input to the capture.
Keep the existing sentence in "The submitted fields": Photos are the input to the capture. The stored entry holds the outputs, and photo handling follows the deployment terms the program agreed. Do not add retention periods here; the privacy section links the FAQ.

## R1-4 · BLOCKING · Add the "what programs measure" angle for GLP-1 muscle loss
Rule: v3.0 plan, this row and the Hub 1 GLP-1 bridge row (Vadim, 18.11). The live article https://3dlook.ai/content-hub/glp-1-muscle-loss-fitness-apps/ owns the muscle-loss intent; no second page. This article takes only the program and clinic side: which record fields answer the muscle-loss question.
Add one H2 section of ~150-200 words, placed after "Why each group of fields earns its place" and before "Cadence, and what keeps entries comparable". Starting text (edit for flow, keep the claims and limits):
## What programs measure when the question is muscle loss

Muscle loss during GLP-1 treatment is a question about what the weight change is made of. A program answers it from fields the record already carries. Lean mass and fat mass estimates sit in every entry, next to the weight figure. Circumferences at the waist, hips, thighs and upper arms show where the change happened. A scan-to-scan comparison places two entries the program selects side by side.

These figures support clinician review. FitXpress does not assess muscle strength, muscle function or sarcopenia. Where a protocol names dual-energy X-ray absorptiometry (DXA) or bioelectrical impedance analysis (BIA), that method stays in place. The consumer-app side of the same question is covered in [GLP-1 muscle loss: what fitness apps can track beyond scale weight](https://3dlook.ai/content-hub/glp-1-muscle-loss-fitness-apps/).
Constraints:
- No lean-mass-loss percentages or other figures from trials, and no fat % or lean-mass accuracy numbers (roadmap.md: no body-composition figures until the lab report).
- Do not repeat the fitness-app article's explanation of why muscle loss happens. One link, sideways.
- Verify the four named body sites against the measurement list in product-info. If any is not in the list, replace it with one that is.
- M1: DXA and BIA are now expanded here at first use. In the FAQ "Does a body-data record replace a calibrated scale or a dual-energy X-ray absorptiometry (DXA) scan?", change the H3 and answer to the short forms DXA and BIA.
- Third-party source: the article currently has zero external links. If an approved neutral source on lean mass in GLP-1 treatment exists in the pack or brand-assets, it may be cited in this section. Do not search for and add one on your own; if none is approved, record it in Open items for Asselya.

## R1-5 · SHOULD · Speed wording
Rule: tech-spec.md, the only public timing definition.
- Old: Capture takes two photos, front and side, and returns the structured outputs in under 45 seconds.
- New: Capture takes two photos, front and side, and runs under 45 seconds from the photos to structured results.

## R1-6 · SHOULD · Repeatability paragraph needs the NDA line
Rule: accuracy-formulations.md §5 and §3 (every condition stays: reference, "most of the evaluated measurements", NDA line, framework link in the same paragraph).
In the paragraph that starts Repeatability is the reason two entries can be read against each other at all., add after ...remained below 1 cm.: Detailed methodology is available under a non-disclosure agreement.
Keep "Internal" and the framework link in the same paragraph. Do not add the accuracy percentage here.

## R1-7 · SHOULD · BMI mention needs the BMI verification link
Rule: landing-map.md rule 1, second half: anything the article says about BMI or weight verification also links to /for-bmi-verification/.
FAQ "Can this record confirm eligibility for a GLP-1 program?":
- Old: Programs working through remote BMI verification can read the [online pharmacy BMI verification guide](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/).
- New: For the verification step itself, see [remote BMI verification](https://3dlook.ai/for-bmi-verification/). Online pharmacies can read the [online pharmacy BMI verification guide](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/).
Keep the pharmacy guide link (required by the plan row).

## R1-8 · OPTIONAL · Shorten the privacy section
Rule: compliance.md header: in content, a short context-specific note plus the FAQ link; do not restate the FAQ.
Section "What happens to the record that is kept" may be cut to three or four sentences: outputs retained on an ongoing basis so a later entry can be compared with an earlier one; scan records tied to anonymized, randomly generated IDs; the HIPAA sentence and the GDPR sentence verbatim; the FAQ link. If cut, keep both compliance sentences exactly as they are now.

## Do not change
- Title, H1, slug, primary keyword. The title must not take the landing keyword "body composition tracking for GLP-1 programs".
- Scope note and FitXpress is not a medical device.
- HIPAA and GDPR sentences (verbatim canon).
- Disability limitation in the FAQ (verbatim, accuracy-formulations.md §5).
- Body Progress framing: "comparison outputs for the two entries the program picks".
- Required links: Admin Panel launch post, online pharmacy BMI verification guide, GLP-1 market, accuracy framework, privacy FAQ.
- Terminology already correct: "80+ body measurements", BMI and BMR as calculated metrics, composition as estimates, "customer" only in legal or contract roles, no "organization".
## Acceptance checks
- detect-ai-tells.py --channel article: CLEAN, 0 hard fails.
- article_lint.py: all gates pass, incl. sentence length (mean ≤ 16) and accuracy discipline.
- article_package.py checklist: cta_placement and links_live pass; no ❌ in the compliance block.
- Grep check from R1-1 is clean.
- Exactly two CTA blocks (early, closing), both to the Hub 3 Link-now URL.
- Open items list the relink lines (R1-2), the body-site verification (R1-4) and the third-party-source decision (R1-4).
- Write review-1-decisions.md with each item marked applied / applied with change / rejected, and the reason for any deviation.
