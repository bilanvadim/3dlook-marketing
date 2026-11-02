---
review: review-1.md (Doc "Article - Accuracy and Digital Health ROI", tab "Review 1", fetched 2026-11-02)
reviewer: Asselya Sekerova
base_text: v1/final.md (= live page since 2026-10-30, = the Doc's tab "Version 1")
decided_by: coordinator (new-article.md review procedure), checked against brand-assets/
rule: THIS FILE WINS over review-1.md wherever they differ, and over plan.md for headings, CTA count and section content.
type: EDIT round. Sections keep their order, with three changes. The ROI model section is rebuilt (A1). The last two sections are reshaped (E6). The FAQ gains one question (E3). plan.md is not regenerated.
next: seo-editor -> seo-publisher (meta.md + article_package.py assemble) -> seo-qc -> editor fix pass on QC findings
---

# Review 1: decisions

Status words: **ACCEPT** = do what the review says. **ACCEPT, CHANGED** = do it with the change written
here. **REJECT** = do not do it, with the reason. **VERBATIM** = use these exact words, no rewording.
Where this file gives text in a quote block, that text is the instruction. Do not paraphrase it.

## A. P1, required

### A1. ROI model and its denominators: ACCEPT. Rebuild section "A digital health ROI model the program fills in".

The reviewer is right. v1 has four defects:
- `P` mixes patients and submissions.
- `m + e × x` can count exception time twice when `m` already includes it.
- `P × d × a` applies an onboarding drop-off rate to repeat check-ins.
- "The difference between the two totals is the return" calls savings "return".

Replace the variable table with this one, in this order. You may phrase the cells, but keep the meaning.

| Variable | What to measure | Where the figure comes from |
|---|---|---|
| `P` | Body-data submissions per month: enrollment captures and repeat check-ins together | Enrollment and check-in logs |
| `m_before` | Average staff minutes per submission on the current process, including checking, follow-up, video sessions, record entry, and the time spent on exceptions and resubmissions | Timed sample of real submissions in the baseline cohort, plus exception logs |
| `m_after` | The same measure in the pilot cohort | Timed sample of real submissions in the pilot cohort, plus exception logs |
| `c` | Loaded staff cost per hour | Finance or HR |
| `s` | Cost per scan under the company's contract | The vendor quote |
| `F` | Other monthly running costs of the new step, where they apply: software, support | The vendor quote and internal estimates |
| `I` | One-time costs: integration and staff training | Internal estimates |

Then the calculations, VERBATIM formulas. Plain-text ASCII inside backticks, the same style as v1:

- Monthly operating savings = `P × (m_before − m_after) × c ÷ 60 − P × s`
- Net monthly savings = monthly operating savings − `F`
- Payback period in months = `I ÷ net monthly savings`
- ROI for a chosen period = net savings for the period, minus `I`, divided by the total cost of the new step for that period (scan fees, running costs and `I`)

Write the three result terms so they cannot be confused: **net savings** is money per month,
**payback** is months, **ROI** is a ratio for a stated period. Define each once, then stop.
Do not add worked numbers, example values or a sample calculation. Any figure would read as
customer performance (review P3, "no fake savings").

- Exceptions: `e` and `x` leave the table and the formula, because they now sit inside `m_before` and `m_after`. One sentence may say that the exception rate and minutes per exception are worth logging, because they explain a change in `m`. Do not add a second formula for them.
- Onboarding: `d` and `a` leave the table and the formula. Onboarding completion is reported **separately**: verification-step completion = patients who complete the verification step ÷ patients who started onboarding in the same period. Retries and abandonment are counted on the same started-onboarding denominator. Do not convert drop-off into money and do not call acquisition spend "lost" (see D6).
- Retention: v1's "fourth stream" paragraph stays as an optional, separately measured metric with its own denominator, outside the savings formula. Keep the link to the patient engagement article.
- Line edit L7 (D7) applies here. Read D7 before writing this section.
- After the calculations, place the accuracy-to-ROI paragraph (B1), then the mid-article CTA (A5).
- Pilot design (time both cohorts; comparable groups, consistent stages, comparable periods) does not go here. It goes once, in the final section (E6).

### A2. Scan estimates are not verified weight: ACCEPT, CHANGED in one cell.

- H2 VERBATIM: "Self-reported vs device-recorded, observed, and scan-estimated body data"
- Remove "verified capture" as an umbrella term everywhere. This covers the short answer, the table intro and the body. "Verified" / "verification" stays only for the **verification step**: checking a submitted value against a second source. That is a method with a described basis, as the review requires.
- Remove "gives the program a record it did not have to take on trust" and anything like it.
- Table, row "What the program receives", column "Guided mobile scan", cell becomes: "Scan-estimated weight from two guided live photos and the supplied height, BMI calculated from them, body measurements, and body-composition estimates".
  **REJECT "modeled body measurements".** Canon calls them body measurements (CLAUDE.md §1, `accuracy-formulations.md` §1.1, terminology guardrails §2.13). "Modeled" would contradict the published accuracy framework.
- Section "Where FitXpress fits", weight-check paragraph: rewrite as a discrepancy check. The meaning to carry: the program can compare BMI calculated from the scan-estimated weight with BMI from self-reported weight, using the same supplied height. A large difference is a discrepancy to review. It does not prove the actual weight. The company sets the threshold and the review rule.
- The device-recorded weight from a connected scale stays "device-recorded weight". Video observation stays a "staff-observed measurement".

### A3. Guided capture and timing: ACCEPT, CHANGED to canon.

- DELETE the v1 paragraph "Guided capture includes real-time pose validation and clothing detection. When a capture is unusable, the guided flow requests a retake. These controls reduce resubmissions; they do not guarantee data quality."
- Replace it with the canon "safer level" for new pages (`tech-spec.md` "Page wording since 2026-10-07"). VERBATIM core: "Real-Time Pose Validation (RTPV) gives pose and framing guidance during capture." Then one sentence that links the [capture-quality FAQ](https://3dlook.ai/content-hub/fitxpress-capture-quality-user-experience-faq/) for what happens when a capture does not meet the requirements. Then one sentence saying that whether guided capture changes resubmissions in a given program is something the pilot measures.
- **Clothing Detector: do not mention it in this article.** The review wants "clothing conditions can be flagged for review and do not automatically force retakes". Canon has an unresolved product open item on exactly that: "does not trigger a retake" vs "can prompt corrective action" (`tech-spec.md` line 61). Neither direction may be stated until product confirms. Leaving it out also satisfies the review, because no retake claim remains.
- Table, column "Guided mobile scan":
  - "Where the manual work sits" → "At capture, where pose and framing guidance runs; manual review remains for cases outside the company's rules"
  - "Typical failure mode" row (renamed, see B5) → "Pose or framing that does not meet the capture requirements; guidance during capture asks for a correction"
  - "What a reviewer can see afterwards" → "A scan record with processing status, timestamps, and structured outputs". Drop "capture-quality flags": since 2026-10-07 the canon safer level describes the record as processing status and timestamps.
- Timing. **REJECT the reviewer's wording** "within 45 seconds after submission of two photos". `tech-spec.md` line 69 allows only one public timing definition and bans processing-only splits. Use VERBATIM "under 45 seconds from the photos to structured results". **ACCEPT the journey note:** add one short sentence saying that the full enrollment step, including the program's own onboarding inputs, can take longer. Give no number for it.

### A4. Accuracy and repeatability: ACCEPT.

- VERBATIM, replacing "For GLP-1 progress tracking, repeatability matters more than accuracy.": "Repeatability is particularly important for longitudinal progress tracking, alongside accuracy."
- Keep the repeatability short form and the accuracy short form from `accuracy-formulations.md` §5 exactly as in v1. Do not mix §1 and §5 sentences in one paragraph, and the framework link stays on each paragraph.
- Add one sentence after the accuracy short form, VERBATIM: "These figures describe body measurements, not weight, BMI, or body-composition estimates."
- Do **not** add the weight-estimation figure (±3.5%). It is a separate study, and its public descriptor is an open item in `proof-points.md` line 29 ("real-world" vs "evaluated" conditions). Article roles (B6) also send methodology to the framework. Weight estimation is named only as an estimate, without a figure.

### A5. Three CTAs: ACCEPT, for this article.

This overrides `blog-style-guide.md` §5 "One CTA per article" for this article only. Basis: the review, together with our own SEO plan and `landing-map.md` rule 1. Clarity shows health articles are read to 5-35% depth, so a product link must sit in the first 30%. All three CTAs are text sentences. No banners, boxes, or "Book now" language. Demo only: no trial, no free pilot, no numbers about the sales path (CLAUDE.md §2).

1. **Early**, within the first ~30% of the body, at the end of the first section after the scope note. One sentence, at most 25 words, product-relevant, linking `https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/` (no modal anchor). It doubles as the landing-map down link.
2. **Mid**, right after the ROI calculations and the B1 paragraph. One sentence linking `https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/#bd-modal`. The natural angle: the scan cost `s` and the setup costs `F` and `I` come from a conversation with 3DLOOK about the company's workflow.
3. **Final**, last sentence of the last section (E6), linking the same `#bd-modal` URL. Keep v1's anchor idea: talk to 3DLOOK about the program's body-data workflow.

The three anchors must differ from each other.

## B. P2, content, scope and evidence

### B1. Accuracy-to-ROI chain: ACCEPT. One short paragraph in the ROI section, after the calculations.

The chain, in plain sentences without arrows: measurement quality, repeatability and capture usability
can mean fewer cases that need manual review under the company's review policy; fewer such cases can
save staff time; savings count only after costs. Close with: the company sets quality thresholds and
exception rules, and the technology alone does not guarantee a lower review workload.
Line edits L2 and L3 (D2, D3) are used here, VERBATIM, once each. The paragraph opens with L2 and uses L3 inside it.

### B2. Onboarding separate from repeat monitoring: ACCEPT. Done by A1 (separate denominator) and D6. Pilot cohorts comparable: E6.

### B3. Clinical and regulatory boundaries: ACCEPT.

- State the boundary **twice** in body copy. The first is the scope note near the start: keep v1's `**Scope note.**` paragraph and its claim comments, unchanged. The second is in the product section, where v1's paragraph "Inside the program, the scan record is one input to clinician review…" stays. Add "or direct observation" to its protocol sentence: "Where a protocol requires dual-energy X-ray absorptiometry (DXA), BIA, a calibrated scale, or direct observation, that method stays in place."
- **Remove** the short-answer bullet "What stays the same. Clinicians still review the record and make every clinical decision." It is a third repetition.
- FAQ "Is scan data used to decide eligibility or medication dosing?" stays, because it is a real buyer question and holds the FAQPage slot. Answer it in at most two sentences, without repeating "not a medical device".
- Keep the disability paragraph (FXS-POPULATION, `accuracy-formulations.md` §5) VERBATIM, as in v1.

### B4. Privacy claims: ACCEPT.

- "Where FitXpress fits": keep only the HIPAA and GDPR canonical sentences (FXS-HIPAA, FXS-GDPR, VERBATIM as in v1) and the link to the privacy FAQ. **Delete** the two retention sentences from this section. They repeat in the FAQ.
- FAQ "What happens to the photos and the scan results?" Rewrite in the order below, with canon wording from `compliance.md` §3:
  1. Photos: 3DLOOK deletes them immediately after processing, or within 30 days, per the customer's instructions.
  2. Measurements, body-composition estimates and 3D models: retained unless the customer agreement says otherwise. Deletion is by scan identifier, on request.
  3. Copies the company keeps in its own systems follow its own policies. This is the distinction between 3DLOOK processing and the company's policy that the review asks for (`compliance.md` §3, SDK copies).
  4. The link to the privacy and security FAQ for the details.
- **Drop the FXS-IDS sentence** ("Stored records carry randomly generated IDs…") from this article. It is canon, but the review asks to avoid de-identification statements that may vary by deployment, and the privacy FAQ carries it. Remove `FXS-IDS` from `claims_used`.

### B5. Generalized claims: ACCEPT.

- CDC paragraph: keep the citation and figures as in v1. It already says the finding describes a population. Make sure the wording says explicitly that this is not an error rate for an individual submission.
- Make these illustrative or conditional:
  - "A common operational pattern has three steps" → "One possible pattern has three steps"
  - "Programs usually combine methods." → "A program can combine methods."
  - "A hybrid of two or three methods is common." → drop it or make it conditional
  - FAQ "A common pattern collects…" → "One approach collects…"
  - Table row label "Typical failure mode" → "Common failure points"
  - "Unless the capture step changes, staff time grows roughly in step with patient volume." → "If the capture and review steps stay the same, staff time tends to grow with patient volume."
  - "A connected scale and guided mobile capture move it to the capture step, where software carries most of it." → move **part** of the work to the capture step, and say manual review still applies to cases outside the company's rules. Never "always", never "removes manual review".
  - "Most of it sits in…" (short answer): replaced by D5.
- No customer names, case studies or quantified savings. v1 had none, so keep it that way.

### B6. Article roles: ACCEPT. Link, do not clone.

- Accuracy framework: only the §5 short forms plus the framework link.
- Capture-quality FAQ: flow mechanics, through the new link in A3.
- Privacy FAQ: detail, through the links in B4.
- Telehealth landing: conversion, through the CTAs in A5.

## C. Language and terminology: ACCEPT, merged with our guardrails.

- **company** = the commercial business: costs, acquisition spend, contract choices, thresholds and review rules it sets. **program** stays for the care program and its workflow (terminology guardrails §2.14 lists "program" as a named actor). **customer** stays in the GDPR canonical sentence (VERBATIM, legal role) and in retention lines where the contract matters. **patient** = the person receiving care.
- "mobile body scanning" when naming the technology. Use these terms precisely: "body measurements", "body-composition estimates", "scan-estimated weight", "device-recorded weight", "manual review".
- "verified": see A2.
- Unnecessary acronyms: if an acronym appears only once, write the term out and drop the acronym. Standard acronyms stay as they are (BMI, US, UK, EU), per CLAUDE.md §6.
- Cut defensive repetition: B3 limits the boundary to two body mentions and one FAQ answer.
- All hard bans still apply: em dash, "this article", "so" as a result connector, "let", "plus", corrective "rather than" / "X, not Y" outside a product or regulatory boundary, and the rest. One exception: A4's VERBATIM sentence "…body measurements, not weight, BMI, or body-composition estimates" is a product-scope boundary and is allowed (Doc §1.8).

## D. Required line edits

| # | Current (v1) | Decision |
|---|---|---|
| L1 | "Every self-reported height and weight that needs a second check or a re-entry becomes staff time." | **SUPERSEDED by F.** The recommended introduction replaces the paragraph that holds it. Do not add L1 anywhere. |
| L2 | "Most of the return from better body data comes from fewer manual touches per patient…" | Its paragraph is replaced by F. The replacement sentence is used ONCE, VERBATIM, as the first sentence of the B1 paragraph: "Better body data can reduce staff verification time when the measurements meet the program's quality requirements." |
| L3 | "Accuracy matters as far as it lets a reviewer accept a record without checking it again." | Its paragraph is replaced by F. The replacement is used ONCE, VERBATIM, inside B1: "Reliable measurements can reduce the need for repeated checks." |
| L4 | "Self-report is the fastest to collect and needs the most checking downstream." | VERBATIM: "Self-reported data is quick to collect but may require additional verification." First sentence of the first short-answer bullet's answer. See E1. |
| L5 | "Where the cost sits" / "three cost streams" | VERBATIM: "Where the costs come from" (short-answer bullet label) and "three sources of cost" everywhere "three cost streams" appeared, including the Image 1 concept. |
| L6 | "The acquisition spend on that signup is then lost." | VERBATIM: "When a patient abandons enrollment, the company may not recover its acquisition costs." |
| L7 | "The arithmetic has two lines." / "The difference between the two totals is the return." | **L7a "The model uses two calculations." is DROPPED.** The rebuilt model (A1) no longer has two lines, and the sentence would be false. **L7b VERBATIM**, directly after the monthly-operating-savings formula: "The difference shows estimated savings, before accounting for any excluded costs." Then the net-savings, payback and ROI lines follow. Nowhere may the text call the savings result "the return". |
| L8 | "The clinician reads them as estimates within the wider record." | VERBATIM: "Clinicians can review these estimates alongside other patient information." |
| L9 | H2 "When standardizing capture pays back, and how to test it" | VERBATIM H2: "When standardized measurement becomes cost-effective". ", and how to test it" goes, because the pilot paragraph moves to E6. |
| L10 | "Fill in the ROI model from a timed sample…" | VERBATIM, first sentence of the final section (E6): "Use actual staff time and verification records to estimate potential savings." |

## E. P3: SEO, GEO, FAQ, visuals

### E1. Short answer section. Keep it, with three bullets.

- **Bullet 1.** The question keeps the search phrasing "Self-reported or verified body data: which is more reliable?". It is the GSC query family with 93 impressions at position 4.1 (plan.md keyword table). This is the only place "verified" names an option, and the answer immediately says what verification means.
- **Bullet 1 answer** = L4 verbatim, then: verification compares a submitted value with a second source, which can be a device-recorded weight, a staff-observed measurement, or a scan estimate. Then: a scan estimate that differs from the self-reported value flags a discrepancy for review; it does not prove the actual weight.
- **Bullet 2.** "Where the costs come from" (L5): staff minutes per submission, exceptions and resubmissions, and patients who stop at the verification step. Phrase it as "can come from", not "most of it".
- **Bullet 3.** "How to model the return" becomes "How to estimate savings". Compare timed staff minutes per submission in comparable baseline and pilot cohorts, using the company's own figures.
- The "What stays the same" bullet is removed (B3).

### E2. Titles and meta: ACCEPT. Asel owns the site meta, so her choice wins over plan.md and over the current live title.

- H1 VERBATIM: "Accuracy and Digital Health ROI: Reducing Manual Patient Monitoring"
- SEO title VERBATIM: "Digital Health ROI: Accuracy and Verification Costs | 3DLOOK" (60 characters)
- Meta description VERBATIM: "How body-data accuracy affects digital health ROI. Compare manual verification, connected scales and mobile scans, and learn what to measure in a pilot." (152 characters)
- OG and Twitter title and description: the same two strings. The live page still carries the January OG values, an open item since 10-30.
- Slug and URL unchanged: `accuracy-drives-roi-digital-health`, self-canonical.

### E3. FAQ: four questions.

1. **NEW, first.** A practical question on evaluating pilot ROI, for example "How can a digital health company measure the ROI of a body-data pilot?". Answer in 2-4 sentences:
   - time staff minutes per submission in comparable baseline and pilot cohorts;
   - subtract scan fees and running costs to get net monthly savings;
   - payback is the one-time costs divided by net monthly savings;
   - report onboarding completion separately, on a started-onboarding denominator.
2. Eligibility and dosing: kept, at most two sentences (B3).
3. Self-reported and scan data together: kept, "One approach…" (B5).
4. Photos and scan results: rewritten (B4).

FAQPage schema: four questions. The live FAQPage is Asel's Custom HTML block (since a47f00e), so the publisher puts the updated JSON-LD in the package as an open item for her. Do not promise rich results (FAQ rich results stopped for non-authority sites in 2026-05). Article schema: author Vadim Bilan, the original datePublished kept, dateModified = the republish date.

### E4. Comparison table: ACCEPT. Keep the four columns and six rows. Apply A2, A3 and B5 to the cells and labels, with the same terms as the body.

### E5. Visual concepts. They stay as `(Cover)` / `(Image N)` placeholder lines, like v1.

- **Cover:** unchanged. It already matches the review: self-reported gaps beside structured records, no numbers.
- **Image 1:** new concept. A baseline cohort → pilot cohort comparison showing three panels: staff minutes per submission, exceptions per submission, and onboarding completion on its own started-onboarding denominator. Labeled "Illustrative". No figures, no savings amounts. "three sources of cost" wording if any text appears.
- **Image 2** (GLP-1 between-visit timeline): keep it. The review calls it optional. Mark it "Illustrative".
- Kristina is already updating the live visuals (Slack 11-02). The publisher lists these three concepts in the package's open items for her, together with the old banner_1 problem: it shows "Eligibility Verified" and "Create Treatment Plan", which contradict the scope note.

### E6. Final section: ACCEPT.

The last H2 replaces "Next steps", VERBATIM: "How to evaluate the ROI of remote body measurement".

Content, in this order:
1. L10 verbatim.
2. Pilot design, moved here from v1's "When standardizing capture pays back" closing paragraph. Measure the inputs on the current workflow first. Time both the baseline and the pilot cohort. Use comparable groups, consistent stages and comparable periods, not only the same duration. Compare minutes per submission, exceptions, and onboarding completion on the started-onboarding denominator.
3. The final CTA (A5.3).

At most about 120 words.

### E7. Introduction (review's "Recommended introduction"): ACCEPT, CHANGED in the last sentence.

It replaces v1's first two paragraphs under "Patient volume and the staff time behind body data" (the H2 stays). VERBATIM, except the last sentence, which is changed because the review's "This article compares…" is a hard ban (terminology guardrails, "this article"):

> As telehealth and glucagon-like peptide-1 (GLP-1) weight-management programs grow, collecting and checking patient body measurements can demand more staff time. Self-reported information may require follow-up calls, additional checks, or resubmissions.
>
> Mobile body scanning offers another approach. It can standardize how measurements are collected remotely and help companies identify cases that need additional review. Whether this lowers costs depends on the program's accuracy requirements, the frequency of exceptions, and the cost of implementing the workflow.
>
> Comparing the main collection methods and the staff time behind each one gives a digital health company a way to evaluate its operational costs and potential return on investment.

Then keep, in this order:
1. v1's paragraph "That makes telehealth patient monitoring an operations question…" with the telehealth AI overview link. Adjust its first words so it follows the new intro.
2. The scope note.
3. The early CTA (A5.1).

The cover placeholder line stays where it is.

## F. Keep unchanged

- Slug, byline "By Vadim Bilan", `**Scope note.**` in bold.
- CDC citation and link.
- The FXS-POPULATION paragraph.
- The §5 accuracy and repeatability short forms with the framework links.
- The HIPAA and GDPR canonical sentences.
- Internal links: telehealth AI overview, BMI verification guide, GLP-1 market, patient engagement, accuracy framework, privacy FAQ. The new link is the capture-quality FAQ.
- `<!-- claim: … -->` comments stay on the sentences that carry claims. Update `claims_used` and `claims_verified` (FXS-IDS out).
- Word count: 1,950-2,350.

## G. Deliverables (from the review's checklist)

- `final.md`, publication-ready. Update the frontmatter: `edited: 2026-11-02`, `review_round: 1`, `changes_summary`, `word_count`, claims lists.
- `editor-report.md`: a short change log **mapped to P1 / P2 / P3** (the review asks for this). It also lists every detail the editor could not support from `brand-assets/` as a flag. Do not guess.
- The publisher copies any editor flag into `publish-package.md` open items (`feedback_pipeline_applies_reviews`, third rule).

## H. Open items for Vadim (non-blocking, go into the package and the digest)

1. `blog-style-guide.md` §5 says "One CTA per article". This article now has three (A5). Should the style guide change for FX health articles, given the 30%-depth finding?
2. The H2 loses "verified" (A2). The GSC query family "self-reported vs verified" (93 impressions, position 4.1) is now answered only in the short-answer question (E1). Watch the GSC position after the republish.
3. Timing: the review's "within 45 seconds after submission" was rejected under the one-definition rule (A3). If product wants a processing-only figure, that changes canon for every channel.
4. Clothing Detector is left out until product settles "does not trigger a retake" vs "can prompt corrective action" (A3).
5. Web (Asel): FAQPage Custom HTML 3 → 4 questions, and the OG/Twitter values (E2, E3). Visuals go to Kristina (E5).
