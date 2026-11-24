---
review: review-1.md (Doc 1XHsliNuHRPpzHW-64oawgiQQ-Y1lQ6dG3jaIAJ0AFR8, tab "Review 1", fetched 2026-11-24)
reviewer: Asselya Sekerova
base_text: v1/final.md (= the Doc tab "Version 1", identical in wording; the page is NOT published: /content-hub/glp-1-patient-progress-record-body-data/ returns 404 on 2026-11-24)
decided_by: coordinator (new-article.md review procedure), each item checked against brand-assets/ and the live pages in §V
rule: THIS FILE WINS over review-1.md wherever they differ, and over plan.md for headings, CTA count and section content.
type: EDIT round. Section order stays, plus one new H2 (R1-4). Title, H1, slug, primary keyword, byline, scope note unchanged. plan.md is not regenerated.
word_target: about 2,100-2,250 prose words (v1 1,988). The new H2 and the early CTA are required; pay for them by tightening, never by cutting required content.
next: seo-editor -> seo-publisher (meta.md + article_package.py assemble) -> quality-controller -> editor fix pass on QC findings
---

# Review 1: decisions

Status words: **ACCEPT** = do what the review says. **ACCEPT, CHANGED** = do it with the change
written here. **REJECT** = do not do it. **VERBATIM** = use these exact words. Where this file gives
text in a quote block, that text is the instruction: do not paraphrase it.

All eight review items were checked against canon and hold. Nothing is rejected. The reviewer's
"Old / New" pairs are exact strings from v1 and are applied as written.

New claims for this round are in the context pack, added 2026-11-24: FXS-RECORD-STATUS, FXS-RTPV,
FXS-PHOTOS, FXS-MUSCLE-FIELDS, FXS-MUSCLE-LIMITS, FXS-CLIENTS, and the external source EXT-NEELAND.
New product sentences carry a `<!-- claim: ... -->` marker after the sentence, as in v1. The
FXS-LIFECYCLE note in the pack now says the "Technical data" list is NOT described as part of the
record in this article.

Actor naming stays as in v1: "the program" is the default actor; "customer" only in contract or
legal roles; never "organization".

## R1-1. Capture log claims: ACCEPT, VERBATIM where the review gives text.

Checked: `tech-spec.md` Clothing Detector status line ("Superseded on new pages since 2026-10-07":
the returned record is described as "processing status and timestamps", without pose and framing
validation results or clothing-related information) and `roadmap.md` (Clothing Detector: "no
payload flags, classes"). The scan identifier is canon (`compliance.md` §3-§4: deletion and Body
Progress work by scan identifier). v1 described the compliance §3 technical-data list as part of
the delivered entry; that is the payload claim the roadmap forbids.

Apply the five replacements exactly as review-1.md R1-1 gives them:

1. Short answer, third bullet ->
   > * **Logged about the capture.** Processing status, a timestamp and the scan identifier for each entry. The program adds what it controls: the version of the capture instructions and whether a manual fallback stood in for the scan.
   Marker: `<!-- claim: FXS-RECORD-STATUS -->`.
2. Short answer, closing line ->
   > The first two groups describe the patient. The third records what happened to the capture, which tells a coordinator whether the entry can be used.
3. Audit list, item 3 ->
   > How many entries returned a completed processing status?
4. "Where FitXpress fits", last paragraph, first sentence ->
   > Either route delivers the entry in the same shape, structured and timestamped, with its processing status and scan identifier.
   Keep the marker the sentence had (FXS-DELIVERY); add FXS-RECORD-STATUS.
5. Next steps, first paragraph, second sentence ->
   > The third group, the fields that record what happened to each capture, is the one a record assembled from several sources rarely holds.

**Section "The capture log" (H3): rewrite both paragraphs** with exactly this content, in this order
(the editor writes the prose; the claims and their order are fixed):

- Processing status tells the team whether a scan produced results before anyone compares it. A
  failed scan then reads as a known gap in the timeline; without the status, the same time point
  can read as a result. (FXS-RECORD-STATUS)
- Timestamps place each entry on the timeline. The scan identifier makes one entry retrievable
  months later, when a partner asks about a single time point. (FXS-RECORD-STATUS)
- The program's own note on capture instructions and manual fallback is what shows whether two
  entries were taken under the same protocol.
- The RTPV sentence: **ACCEPT, use it once, VERBATIM**, next to the capture-instructions point,
  because it is the capture-side half of "the same protocol":
  > During capture, Real-Time Pose Validation (RTPV) gives pose and framing guidance.
  Marker: `<!-- claim: FXS-RTPV -->`. Nothing about RTPV output, results or flags. No voice prompts.
- KEEP the last sentence unchanged: "The first entry sets the starting point for everything
  compared afterwards, and standardizing that first capture is its own piece of work."

**Coordinator addition (same rule, a sentence the review did not list).** Section "What FitXpress
does not do", second paragraph:
- Old: "Its fields describe measured body change and the conditions of each capture."
- New: > Its fields describe measured body change and what happened to each capture.

**Check after the edit (the review's own check):** grep final.md for `flag`, `clothing`,
`obfuscation`, `pose`, `metadata`. The only hit allowed is the RTPV sentence ("Pose" twice inside
it). Also no "conditions of the capture" anywhere.

## R1-2. Landing link and the two CTAs: ACCEPT.

Checked: `landing-map.md` Hub 3 row ("Link now" and "Demo button now" are both
`https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/`; anchors "body
composition tracking for GLP-1 programs" · "remote progress tracking for GLP-1 clinics"), rules 1,
2, 4, 6, and `blog-style-guide.md` §5 (two CTAs per article, Vadim 2026-11-23). v1's only down link
sits at about 53% of the body with an anchor outside the list, and the closing CTA goes to
`/pricing/#bd-modal-personalized`. The telehealth article's pricing CTA was a one-article exception
(Vadim, 2026-11-23); it does not carry over here.

**Early CTA: VERBATIM.** Its own paragraph, no heading, no bold label, directly after the Short
answer's closing line and before the H2 "Why each group of fields earns its place":

> Programs that want these fields delivered into their own patient record can review [body composition tracking for GLP-1 programs](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/) and book a FitXpress demo.

- This is the article's early CTA and its landing-map rule 1 down link. It must sit inside the
  first 30% of body words (the package check `cta_placement` measures it).
- The link sits inside the sentence, as the reviewer wrote it. Do not add a separate action-label
  line under it: it would repeat the same link two lines apart.
- The "100+ clients" clause (FXS-CLIENTS) is **not used**: the block stays one sentence, and a
  client count with no context reads as a proof point dropped into a CTA. The pack keeps the claim
  in case Asselya wants it.
- The landing keyword is an anchor only. It must not enter the title, H1 or meta title (rule 3).

**"Where FitXpress fits", second paragraph: VERBATIM.**
- Old: "Programs evaluating that route can start from [structured body data for telehealth and digital health programs](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/)."
- New: > Programs evaluating that route can start from [remote progress tracking for GLP-1 clinics](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/).
- This is a contextual internal link, not a CTA.

**Closing CTA, Next steps: VERBATIM.**
- Old: "Then [talk to 3DLOOK about the GLP-1 progress record workflow](https://3dlook.ai/pricing/#bd-modal-personalized)."
- New: > Then [book a FitXpress demo](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/) to see how the record arrives in the program's own platform.
- No `/pricing/`, no `/contact-us/`, no form made for this article, anywhere in the article.
- Exactly two CTA blocks in the article: the early one and this one.

**Open items (publisher, landing-map rule 6), one line each:**
- `Relink when /fitxpress/for-glp-1-programs/ goes live: body composition tracking for GLP-1 programs → /structured-body-data-for-telehealth-digital-health-programs/`
- `Relink when /fitxpress/for-glp-1-programs/ goes live: remote progress tracking for GLP-1 clinics → /structured-body-data-for-telehealth-digital-health-programs/`
- `Relink when /fitxpress/for-glp-1-programs/ goes live: closing CTA "book a FitXpress demo" → /structured-body-data-for-telehealth-digital-health-programs/ (then {landing}#demo, rule 4)`

## R1-3. Photos and retention: ACCEPT, VERBATIM.

Checked: `compliance.md` §3 lifecycle table (photos deleted immediately after processing or within
30 days, per the customer's instructions; outputs stored).

- Short answer, first bullet ->
  > * **Submitted with the capture.** Front and side photos, gender, height, and an optional self-reported weight. Gender, height and weight stay in the entry as their own fields. The photos are the input to the capture.
  Marker: add `<!-- claim: FXS-PHOTOS -->`; keep the v1 marker on that line.
- KEEP in "The submitted fields": "Photos are the input to the capture. The stored entry holds the
  outputs, and photo handling follows the deployment terms the program agreed." No retention
  periods in the body.
- The editor may vary the wording of ONE of the two "Photos are the input to the capture"
  sentences if the near-duplicate check flags the pair; the bullet's wording wins, it is the
  reviewer's.

## R1-4. The muscle-loss angle: ACCEPT, CHANGED (one sentence added from an approved source).

Checked: `content-plan.md` row "What Body Data Should Be Included in a GLP-1 Patient Progress
Record?" and the Hub 1 GLP-1 bridge row (Vadim, 18.11): the live
https://3dlook.ai/content-hub/glp-1-muscle-loss-fitness-apps/ owns the muscle-loss intent, and "the
'what programs and clinics measure' angle belongs to the GLP-1 patient progress record article".

**Body sites, verified** against `tech-spec.md` "Circumferences": waist, low hips, thigh, bicep
(the upper arm). All four are in the list; the live sibling article uses the same four ("waist,
hip, thigh, and upper-arm circumferences"). No replacement needed.

**Third-party source.** The review allows one "if an approved neutral source on lean mass in GLP-1
treatment exists in the pack or brand-assets". One does: EXT-NEELAND (Neeland, Linge, Birkenfeld
2024, PMID 38937282), approved for and cited live on the sibling muscle-loss article. It is now in
this article's pack. Use only its lean-mass-versus-muscle point, which is exactly the limit this
section needs. No percentages or ranges from it (R1-4: no trial figures). Asselya can strike the
sentence; that is an Open item.

**New H2, placed after the "Why each group of fields earns its place" section (after the H3 "The
capture log") and before "Cadence, and what keeps entries comparable".** Heading VERBATIM. Body:
start from this text. The editor may adjust flow and sentence joins only; the claims, the limits,
the link and the order stay.

> ## What programs measure when the question is muscle loss
>
> Muscle loss during GLP-1 treatment is a question about what the weight change is made of. A program answers it from fields the record already carries. Lean mass and fat mass estimates sit in every entry, next to the weight figure. Circumferences at the waist, hips, thighs and upper arms show where the change happened. A scan-to-scan comparison places two entries the program selects side by side. <!-- claim: FXS-MUSCLE-FIELDS -->
>
> These figures support clinician review. A 2024 review by [Neeland, Linge and Birkenfeld](https://pubmed.ncbi.nlm.nih.gov/38937282/) notes that changes in lean mass may not always reflect changes in muscle. Its definition of lean mass also covers organs, bone and fluids. FitXpress does not assess muscle strength, muscle function or sarcopenia. Where a protocol names dual-energy X-ray absorptiometry (DXA) or bioelectrical impedance analysis (BIA), that method stays in place. <!-- claim: FXS-MUSCLE-LIMITS --> The consumer-app side of the same question is covered in [GLP-1 muscle loss: what fitness apps can track beyond scale weight](https://3dlook.ai/content-hub/glp-1-muscle-loss-fitness-apps/).

Constraints (the reviewer's, all binding):
- No lean-mass-loss percentages or other trial figures. No fat % or lean-mass accuracy numbers.
- Do not explain why muscle loss happens. One sideways link to the sibling, as written.
- The Neeland lines are attributed to the review, never in our own voice.
- "These figures support clinician review" stays. Composition figures are "estimates".

**M1 follow-on: VERBATIM.** DXA and BIA are now expanded in the new section, which comes before the FAQ.
- FAQ H3, Old: "Does a body-data record replace a calibrated scale or a dual-energy X-ray absorptiometry (DXA) scan?"
- New: > ### Does a body-data record replace a calibrated scale or a DXA scan?
- FAQ answer: "A DXA scan, bioelectrical impedance analysis (BIA), and a calibrated scale" ->
  > A DXA scan, BIA, and a calibrated scale
- The FAQ answer keeps its last sentence ("Where a workflow, protocol, or regulatory standard names
  one of those methods, it stays in place, and the scan entry sits beside it."). If the
  near-duplicate check pairs it with the new section's DXA/BIA sentence, shorten the NEW section's
  sentence, not the FAQ's.
- Check that the frontmatter `changes_summary` and any "expanded at first use" note no longer
  says DXA/BIA are expanded in the FAQ.

## R1-5. Speed wording: ACCEPT, VERBATIM.

Checked: `tech-spec.md`, the only public timing definition (Vadim, 2026-09-23): "under 45 seconds
from the photos to structured results".
- Old: "Capture takes two photos, front and side, and returns the structured outputs in under 45 seconds."
- New: > Capture takes two photos, front and side, and runs under 45 seconds from the photos to structured results.
- Keep the FXS-SPEED marker.

## R1-6. NDA line in the repeatability paragraph: ACCEPT, VERBATIM.

Checked: `accuracy-formulations.md` §1.8 (methodology, including the definition of repeatability,
is available under NDA) and §5/§3 (every condition stays in the paragraph: reference, "most of the
evaluated measurements", the NDA line, the framework link).
- In the paragraph "Repeatability is the reason two entries can be read against each other at
  all.", directly after "...typical scan-to-scan differences remained below 1 cm. <!-- claim: FXS-REPEAT -->", insert:
  > Detailed methodology is available under a non-disclosure agreement.
- KEEP "Internal" and the framework link in the same paragraph. No accuracy percentage here.

## R1-7. BMI mention needs the BMI verification link: ACCEPT, VERBATIM.

Checked: `landing-map.md` rule 1, second half, and the BMI row (link now `/for-bmi-verification/`,
anchor list includes "remote BMI verification"). The page answers 200 on 2026-11-24.
- FAQ "Can this record confirm eligibility for a GLP-1 program?", Old: "Programs working through remote BMI verification can read the [online pharmacy BMI verification guide](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/)."
- New: > For the verification step itself, see [remote BMI verification](https://3dlook.ai/for-bmi-verification/). Online pharmacies can read the [online pharmacy BMI verification guide](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/).
- Keep the pharmacy guide link (required by the plan row).

## R1-8. Shorter privacy section: ACCEPT, CHANGED.

Checked: `compliance.md` header (in content, a short context-specific note plus the FAQ link; do
not restate the FAQ).
- Cut the sentence "Deletion is by scan identifier on the customer's request." Everything else in
  "What happens to the record that is kept" stays.
- Why not shorter, as the review allows: the sentence "Two frameworks come up in most procurement
  reviews: the Health Insurance Portability and Accountability Act (HIPAA) and the General Data
  Protection Regulation (GDPR)." is the only place HIPAA and GDPR are expanded (gate M1), and the
  HIPAA and GDPR sentences must stay verbatim, so the expansion cannot move into them.
- KEEP verbatim: "FitXpress can support HIPAA-governed deployments where 3DLOOK acts as a business
  associate under an executed Business Associate Agreement (BAA), where applicable." and "In most
  enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data
  processor under GDPR." and the FAQ link.

## Do not change (the review's list, confirmed)

- Title, H1, slug, primary keyword. The title never takes "body composition tracking for GLP-1
  programs" (landing-map rule 3). The known M1 title case (`gate_m1_note`) stays as it is.
- Byline "By Assel Sekerova". Scope note, and "FitXpress is not a medical device."
- HIPAA and GDPR sentences (verbatim canon). Disability limitation in the FAQ (verbatim).
- Body Progress framing: "comparison outputs for the two entries the program picks".
- Required links: Admin Panel launch post, online pharmacy BMI verification guide, GLP-1 market,
  accuracy framework, privacy FAQ. Related reading list stays.
- Terminology: "80+ body measurements", BMI and BMR as calculated metrics, composition as
  estimates, "customer" only in legal or contract roles, no "organization".

## Acceptance checks

- `detect-ai-tells.py --channel article`: CLEAN, 0 hard fails.
- `article_lint.py`: all gates pass, including sentence length (mean ≤ 16) and accuracy discipline.
- `article_package.py checklist`: `cta_placement` and `links_live` pass; no ❌ in the compliance block.
- The R1-1 grep is clean (only the RTPV sentence).
- Exactly two CTA blocks (early, closing), both to the Hub 3 "Link now" URL. No `/pricing/` link.
- Open items list: the three relink lines (R1-2); body sites verified against tech-spec.md, no
  replacement needed (R1-4); the third-party source decision: EXT-NEELAND used, Asselya may strike
  it (R1-4); the consistency question below.

## Open item for Asselya (publisher copies it into publish-package.md)

- **Consistency with the Telehealth Documentation article.** Its Version 2 (handed over
  2026-11-23) still lists the `compliance.md` §3 technical data ("capture-quality and
  pose-validation flags, clothing classification, face-obfuscation confirmation...") under "What
  the system records technically", with a line that not every field appears in every response.
  This article now follows the stricter 2026-10-07 level from `tech-spec.md`. If the same rule
  should apply there, that article's bullet changes to the FXS-RECORD-STATUS wording before it
  goes live.

## §V. Sources checked on 2026-11-24

- Doc tab "Version 1" = v1/final.md (word-level diff: only claim comments and list numbering).
- curl (sequential): /structured-body-data-for-telehealth-digital-health-programs/ 200 ·
  /for-bmi-verification/ 200 · /content-hub/glp-1-muscle-loss-fitness-apps/ 200 ·
  /content-hub/glp-1-patient-progress-record-body-data/ 404 (not published).
- Canon lines: tech-spec.md L59-L71 · roadmap.md rows Clothing Detector, RTPV, voice guidance ·
  compliance.md §3 table, §4 · landing-map.md Hub 3 row, rules 1-6 · blog-style-guide.md §5 ·
  accuracy-formulations.md §1.8, §5 · content-plan.md progress-record row and Hub 1 bridge row ·
  pack 2026-09-19-glp-1-fitness-apps-body-composition-tracking.yaml EXT-NEELAND.

## QC fix pass (2026-11-24): coordinator decisions on QC findings

QC report: `workspace/_quality/seo/2026-11-24-glp-1-patient-progress-record-body-data-review-1.md`
(16/20, ship after a short fix pass). All six findings were checked in final.md and hold. This
section overrides the R1-4 quote block above where they differ.

- **Q1 (medium), muscle-loss H2, first paragraph: VERBATIM.** "A program answers it from fields the
  record already carries." overclaims: the next paragraph says lean mass may not reflect muscle and
  FitXpress does not assess muscle. Replace with:
  > The record already carries the fields a program reviews for that question.
- **Q2 (low-medium), the Neeland sentences: VERBATIM.** The two sentences in the R1-4 block
  repeated the live sibling's wording almost word for word (coordinator's error in the quote
  block). Replace both with:
  > A 2024 review by [Neeland, Linge, and Birkenfeld](https://pubmed.ncbi.nlm.nih.gov/38937282/) describes lean mass as a measure that includes organs, bone, and fluids as well as muscle. By that account, a change in lean mass may not reflect a change in muscle.
  Faithful to the abstract ("the former measure includes not only muscle but also organs, bone,
  fluids, and water in fat tissue"). The EXT-NEELAND Open item adds: the same source and point are
  cited on the live sibling; Asselya keeps or strikes.
- **Q3 (low), the R1-1 grep.** The check is amended: allowed hits are the RTPV sentence AND the
  canon disability line ("standard standing pose", FXS-POPULATION, on the review's do-not-change
  list). Because the reviewer's own check says "only the RTPV sentence", the publisher puts a
  one-line note in Open items so she does not read it as a miss.
- **Q4 (low), RTPV bridge.** Keep the RTPV sentence verbatim. Tie it to "the same protocol" in the
  sentence before or by a short lead-in, so it reads as guidance during capture, not a logged field.
  No "rather than", no corrective negation.
- **Q5 (low), repetitions.** The "only if the gate flags it" condition in R1-3 is waived: vary the
  "Photos are the input to the capture." sentence in "The submitted fields" (the bullet keeps the
  reviewer's words). Reword v1's "Composition estimates describe what the change is made of." in
  "The generated fields" so it no longer echoes the new H2's first sentence.
- **Q6 (low), meta description: VERBATIM** (158 characters, no landing keyword, program-side angle
  per the plan row):
  > A GLP-1 patient progress record stays readable when every entry carries the same fields. See which body data belongs and what programs measure for muscle loss.
