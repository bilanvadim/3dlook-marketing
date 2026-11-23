---
slug: ai-body-scanning-for-fitness
workspace: ai-body-scanning-for-fitness-refresh
product: fitxpress
status: edited
title: "AI Body Scanning for Fitness: Where a Phone Scan Fits in the Member Journey"
meta_title: "AI Body Scanning for Fitness: Where a Phone Scan Fits"
meta_description: "Explore how AI body scanning fits fitness apps, from member onboarding and progress tracking to coach reviews, SDK integration, and pilot testing."
primary_keyword: ai body scanning for fitness
intent: MOFU
author: Assel Sekerova
author_status: "open item, her call (live byline Dana Vioreanu)"
live_url: https://3dlook.ai/content-hub/ai-body-scanning-for-fitness/
published: 2024-06-12
plan: plan.md
source_draft: draft-v1-writer.md
word_count: 2074
word_count_note: "prose words per article_lint.py; Review 1 target about 2,000-2,150, band 1657-2242 (plan target 1950)"
editing_passes: 9
ai_density_before: 0.0
ai_density_after: 0.0
claims_verified: [FXS-SPEED, FXS-OUTPUTS, FXS-SCOPE, FXS-DELIVERY, FXS-REPEAT, FXS-ACCURACY, FXS-MEDICAL, FXS-POPULATION, FXS-IDS, FIT-WHITELABEL, FIT-BODY-PROGRESS, FIT-CAPTURE, FIT-PLAN, FIT-ADJUST, FIT-KIDMAN, FIT-ACSM, FIT-OUTPUTS-NOTE, FIT-EVIDENCE-LIMIT, FIT-SDK, FIT-RTPV]
claims_dropped: [FXS-LIFECYCLE]
changes_summary: |
  - 3D model (coordinator decision 1): removed "and a 3D model" from the S2 "What it returns" bullet and "the record includes a 3D model" from S5. The base output list is now 80+ body measurements, body composition estimates, and BMI/BMR as calculated metrics. 3D appears only as 3D Body Progress tracking and 3D Goal Visualization on the FitXpress Pro plan (S3) and in the Image 1 concept, which is now labeled as a Pro plan feature. The cover concept says "flat body silhouettes" so the cover does not suggest a 3D model. FXS-LIFECYCLE is no longer cited.
  - FAQ 1 heading (decision 5): 17 words cut to 10: "Is a phone body scan the same as a DXA scan?". DXA is now expanded where it first appears in the body, the S7 "Evidence with its reference" bullet ("such as expert tape measurement or dual-energy X-ray absorptiometry (DXA)"). That is a natural reference-method example, and gate 8 passes.
  - Unsourced judgment lines (decision 7): "The step matters most in online coaching" became the descriptive "In online coaching, the coach may never meet the member in person, and the record gives the coach a view of body change." "the main alternative to a hardware 3D body scanner" became "a hardware-free alternative to a 3D body scanner", with no ranking or market-share reading. The lean mass line is now a limitation of estimates: "Lean mass is one of those estimates, and it is not a direct measure of muscle." It moved into the evidence-limits paragraph.
  - S8 (decision 6): the four bold-label paragraphs became three short prose paragraphs, about 120 words against the plan's 210. The cohort-test lead duplicated the intro and was cut. The hypothesis is framed as "One testable example:" so it cannot read as a finding. The test now fixes one baseline placement (onboarding or the first check-in), which removes a conflict in the draft: its "one placement" rule sat next to a hypothesis that needed scans at both points. Capture conditions are listed once (S3), and S8 refers to them.
  - Headings: S4 H2 "Why visible progress matters for fitness app retention" became "How visible progress may affect fitness app retention", a hedged descriptive heading (editorial-rewrites §4). The section's own limit is that no source tested body scans.
  - Citation dedup (Pass 1): every external source appears once (Adjust, JMIR, ACSM/Newswise). The accuracy framework is linked twice on purpose, once from each figure paragraph (repeatability, accuracy), following accuracy-formulations §3.2 and the coordinator's instruction. Link sentences of the form "X covers Y" were varied.
  - Repetition: "inside the app" x3, "come back" x2, "calculated ... calculated" in consecutive sentences, and "a cohort test" in the intro and in the S8 lead were reduced. "a fitness app" dropped from 4 to 3 (FAQ 1 now says "for progress tracking"). "The app needs" dropped from 3 to 2 (S6 now says "what each check-in has to record").
  - FAQ 3 anchor "data, privacy, and security FAQ" became "FitXpress data, privacy, and security answers". This removes the unexpanded abbreviation FAQ from the prose (M1).
  - Voice: added one expert trade-off in S3 (baseline at onboarding vs at the first check-in). Added two positions: "Each method should keep its own trend line, because numbers from different methods are not interchangeable" (S6) and "their results are reported separately" for fallback-path members (S8).
  - Fix pass 2026-11-18 (coordinator, after article_package.py STOP on boundary_section and scope_note_early): added a bold-label "**Scope note.**" paragraph after the intro, before the short answer (body line 12; editorial-rewrites §7 shape, same as glp-1-muscle-loss-fitness-apps). It has four short sentences: scope (fitness and coaching apps: check-ins, progress views, coach review), "FitXpress is not a medical device.", interpretation and training decisions stay with the app and its coaches, and no diagnosis or health-risk assessment. It carries FXS-MEDICAL and FXS-SCOPE. To keep the boundary in one place: removed the S2 bullet "What it does not do" (S2 now has four bullets) and the S5 boundary paragraph ("FitXpress is not a medical device. It provides structured body data…"). The medical-device sentence now appears once, in the scope note. This overrides the plan's "no scope note, medical-device line once in Section 5".
  - QC fix pass 2026-11-18 (QC 17/20, workspace/_quality/seo/2026-11-18-ai-body-scanning-for-fitness-refresh.md):
    - (1) S7 evidence bullet now says the published figures are for body measurements (accuracy against expert pattern-maker tape measurements, and scan-to-scan repeatability) and that composition estimates are derived from those measurements (FIT-OUTPUTS-NOTE added).
    - (2) S7 answer: "one option built for this" became two quotable sentences (two smartphone photos through the FitXpress SDK; the API delivers 80+ body measurements and body composition estimates to the app).
    - (3) S6 opening now answers for any studio: the scan runs in the studio's app or on its website (FIT-SDK web SDK). It says what the scan returns and drops the "hardware-free … no extra hardware" repeat. The H3 "An in-app phone scan fits when" became "A phone scan fits when".
    - (4) Landing echoes reworded with claim IDs unchanged: the coach-review "the same record" lines (S3, S6 bullet), the S3 white-label close, the S7 SDK and recommended-setup sentences, and the S8 pilot-design lines. S8's onboarding-completion sentence was cut; the trade-off stays once, in S3. S8's "one … one … one" run is gone. The remaining 7+ word overlaps with the landing are canonical claim text (capture conditions, Pro plan feature names, NDA line, output names).
    - (5) Premium tier gains a hedged outcome line: "A cohort test can also show whether those views change how many members upgrade."
    - Actor in S3 is now consistently "the product team" for decisions.
  - Mechanical: "The platform decides" (anthropomorphism hard fail, introduced in pass 1) became "The product team decides". Tape measurements are hedged ("usually need a second person"). The boundary paragraph now uses positive scoping: "Interpreting a change for the member stays with the app and its coaches."
  - Review 1 round 2026-11-23 (review-1-decisions.md; review-1.md by Asselya Sekerova). Sections listed in decisions E were not touched.
    - A1: Added the early CTA verbatim right after the unchanged short-answer landing paragraph. It is two sentences, then "[Explore FitXpress for fitness apps](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/)" on its own line as the button label. It goes to the landing (not #form) at 15.7% of the body; the S2 down link stays at 13.1%.
    - A2: The hardware section is reshaped: new H2 verbatim, "When should fitness programs use phone scanning instead of in-club hardware?". It is 220 words with headings (v1: 307). The answer-first opening has two sentences, carrying FIT-CAPTURE and FIT-SDK: a guided scan on the member's own phone, in the studio's app or on its website, is an alternative to a hardware 3D body scanner, and it fits members who train at home or between club visits. One sentence follows on in-club hardware, with BIA expanded. The lead-in "The choice turns on where members train and what each check-in has to record." was cut: the opening now says where a phone scan fits. Three H3 lists of three bullets each; the own-brand bullet was dropped. The FitXpress pitch and outputs sentences were removed, and with them FXS-SPEED and FXS-OUTPUTS. The closing keeps "The options can work together." and the trend-line sentence, then the comparison link in one sentence. The section ends on a contextual landing link with the map anchor "mobile alternative to a gym body scanner", at 69.0% of the body. To reach the length target, two cuts: "A club can keep its device for visits and use phone scans between them." (which also echoed the landing's comparison close in meaning), and "are not measured and" from the third progress-photo bullet (bullet 2 already says no measurements).
    - A3: The six-week example is inserted verbatim between "Scheduled check-ins." and "Coach review.". No word changed; no gate failed on it.
    - B1: S4 went from 254 to 225 words with the H2. ACSM is now two sentences: the ranking and the release date, then the survey basis and "does not report usage". Dropped: the eighth-place line, the two "different kind of data" sentences, and "A record of that change can give the member a reason to return for the next check-in." (that is the hypothesis, which S8 now owns). The Adjust qualifiers were folded into one sentence: "The figures are global and use 2022 data from all app users." The question comes verbatim after "None of these sources tested body scans.", introduced by "The question an app team can test is narrower:". Both claim comments and all four links are kept.
    - B2: The short-answer bullet is replaced verbatim with the canon timing line ("guided"; "It takes under 45 seconds from the photos to structured results."). The reviewer's "typically ... after capture" is not used.
    - B3: "The outcome is then a single measure, the share of members who come back." became "The primary outcome is the share of members who come back." The secondary metrics follow, verbatim and in order, in one sentence. The reason is in the article's own words: "Return rates measure engagement; the secondary metrics also capture the friction a new step adds." This is now its own paragraph after the hypothesis. The rest of S8 is unchanged, and no landing FAQ wording is used.
    - D3: meta_description replaced verbatim. meta.md and publish-package.md are the publisher's to update.
  - QC fix pass 2026-11-23 (QC 18/20, workspace/_quality/seo/2026-11-23-ai-body-scanning-for-fitness-refresh-review-1.md). Five fixes, applied exactly as the coordinator gave them. Fixes 2 and 3 edit section-E text under a coordinator override, because the A3 example had re-created the repeats.
    - (1) S6 opening: "It fits members who train at home or between club visits." became "It fits members who train away from the club, at home or between visits." The H3 bullet "Members train at home or between club visits." is unchanged. This removes the 7-word verbatim repeat between the answer and the bullet.
    - (2) S3 Coach review: "Before planning the next training block, the coach can check…" became "The coach can check the change between two of the member's scans." The A3 example now carries "the next training block" alone, and the landing step-3 echo is gone. The rest of the paragraph is unchanged.
    - (3) S3 closing paragraph: deleted "The product team also decides what members and coaches see." It repeated the A3 example's "The app determines which results to show and how to use them.", which stays verbatim. FIT-WHITELABEL stays on the paragraph.
    - (4) S4: "The question an app team can test is narrower: Does showing…?" became "A product team can test a narrower question. Does showing…?" The question is verbatim and now a standalone sentence. "Product team" is the article's actor everywhere else, and the colon frame (editorial-rewrites §4) is gone.
    - (5) S6 last sentence: "Integration options and plans are on the FitXpress [anchor] page." became "Integration details and plans are on the FitXpress page for a [mobile alternative to a gym body scanner](landing)." The map anchor is unchanged. The noun stack is gone, and "integration options" is no longer reused from the A1 CTA.
self_check: |
  - Still machine-like after pass 1: four sections in a row ran "lead sentence + four bold-label items" (S2, S3, S7, S8), so the page had a template rhythm. Fixed: S8 is now prose. S2, S3, and S7 keep their lists because the items are parallel and assistants lift them whole (AEO).
  - Still machine-like: the S8 hypothesis read as a result ("For example, members who see ... return more often"), and two judgment lines were stated as facts ("matters most", "the main alternative"). Fixed: the hypothesis is labeled as an example, and the judgment lines are descriptive or hedged.
  - Still machine-like: echo words in consecutive sentences ("calculated" x2, "come back" x2, "that ... that"), a repeated "X covers Y" link-sentence shape, and "onboarding, onboarding". Fixed in the second pass.
  - Residual, accepted: the bold-label lists in S2/S3/S7 and the three H3 "fits when" blocks in S6 still give the page a scannable, structured feel. This follows the comparison-cluster format of the editorial final (editorial-rewrites §7), so they stay.
  - After the QC fix pass, the residual is repetition of canonical output wording ("80+ body measurements" x4, "body composition estimates" x5). The S2, S6, and S7 answer blocks each need it to stand alone for assistants, and it was varied where possible (produce / delivers).
  - Review 1 round, still machine-like after the first apply: (1) after the trim, the S4 Adjust paragraph ended on three clipped sentences in a row. Fixed by folding "all app users" into the data sentence. (2) The lead to the question ("For a single app") was vague. It is now "The question an app team can test is narrower:", which gives the question the test framing B1 asks for. (3) The S8 reason sentence called all four secondary metrics friction, but premium conversion is not friction. It now says "also capture the friction".
  - Residual, accepted in this round: the S6 answer sentence and the phone-scan bullet both say "train at home or between club visits". A2 requires both, and the answer block and the list each have to stand alone. In the A3 example (verbatim), "The app determines which results to show" sits two paragraphs above "The product team also decides what members and coaches see", which section E freezes. "for fitness apps" appears 4 times: three map anchors plus the verbatim CTA label.
  - Superseded by the QC fix pass below. Final gate numbers (Review 1 round, 2026-11-23): article_lint PASS, all 10 gates. Sentence length: mean_words 13.4, p90 21, over_25 0 (0.0%), over_35 0, 138 sentences. Detector CLEAN (article channel and default), density 0.0, rhythm_variation 0.45. Prose words 2086. Landing links at 13.1% / 15.7% (CTA) / 69.0% / 99.0% / 99.5% of the body; the demo link (#form) is at the end. No 7-word overlap between the changed text and the landing snapshots of 2026-11-13 and 2026-11-19.
  - QC fix pass (18/20): QC's two lapses were the S6 answer/bullet verbatim repeat and the S4 "The question … is: …?" frame. Both are fixed (fixes 1 and 4). QC's position point, that S3 made the coach / next-block point three times and said who decides what is shown twice, is fixed by fixes 2 and 3 under the coordinator override. The A3 example is still verbatim. Remaining internal 7-word repeats are accepted: "a guided scan on the member's own phone" (intro and the A2-prescribed S6 opening) and the canonical "80+ body measurements and body composition estimates" (S2 and S7). "a product team" now appears 3 times (intro, S3 lead, S4). That is the article's one actor name, so it is not variation.
  - Final gate numbers (QC fix pass, 2026-11-23): article_lint PASS, all 10 gates. Sentence length: mean_words 13.3, p90 21, over_25 0 (0.0%), over_35 0, 138 sentences. Detector CLEAN (article channel), density 0.0, rhythm_variation 0.45. Prose words 2074. Landing links at 13.2% / 15.8% (CTA) / 68.9% / 99.0% / 99.5% of the body; the demo link (#form) is at the end. The S6 section is 225 words with headings: fix 1 adds 3 words, against A2's 180-220.
---

# AI Body Scanning for Fitness: Where a Phone Scan Fits in the Member Journey

(Cover) - Concept: A phone showing a fitness app's own branded progress screen, with two flat body silhouettes side by side (baseline and check-in) and a waist callout. No numbers, no 3DLOOK interface, no device-maker hardware.

A member reaches the first check-in in a fitness app. The weight chart has barely moved, though waist and hip measurements may have changed. Nothing in the app shows it.

Tape measurements could show the change. They usually need a second person, and the technique has to stay the same each time. With AI body scanning, a guided scan on the member's own phone captures body measurements at home. <!-- claim: FIT-CAPTURE -->

For a product team, the decision is where a scan sits in the member journey and what the member sees. A cohort test before full release answers whether it changes member behavior.

**Scope note.** The scope is body scanning in fitness and coaching apps: member check-ins, progress views, and coach review. FitXpress is not a medical device. Interpretation of results and training decisions stay with the app and its coaches. The scan does not diagnose or assess health risk. <!-- claim: FXS-MEDICAL --> <!-- claim: FXS-SCOPE -->

## AI body scanning for fitness: the short answer

An AI body scan in a fitness app is a short, guided step within its onboarding or check-in flow.

- **What it is.** The member takes two guided smartphone photos, front and side. It takes under 45 seconds from the photos to structured results. <!-- claim: FXS-SPEED -->
- **What it returns.** 80+ body measurements and body composition estimates. BMI and basal metabolic rate (BMR) are calculated metrics. <!-- claim: FXS-OUTPUTS -->
- **Where it sits.** A baseline at onboarding, scheduled check-ins, coach review, or a premium-tier progress feature.
- **What it adds.** It can show body change between check-ins when the scale moves slowly. Its effect on retention is measured per app, in a cohort test.

3DLOOK's FitXpress provides [body scanning for fitness apps](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/) under the app's own brand. Integration runs through a software development kit (SDK) and an application programming interface (API). <!-- claim: FIT-WHITELABEL --> <!-- claim: FXS-DELIVERY -->

See how FitXpress works for fitness apps. Explore the guided scan experience, member progress features, and integration options for connected and digital fitness platforms.

[Explore FitXpress for fitness apps](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/)

## Where does a body scan sit in a fitness app's member journey?

A product team chooses among four placements, and each one changes what the scan is for.

**Baseline at onboarding.** The first scan is the reference for every later comparison. Taken at onboarding, it records the starting point but adds a step for a new member. Taken at the first check-in, it leaves onboarding unchanged, although the record then starts later in the program. A member cohort test can settle which trade-off suits the app.

**Scheduled check-ins.** A second scan fits the end of a training block or a program phase. The product team chooses which two scans to compare, and the app shows the member the change between them. Repeat scans need consistent conditions: form-fitting clothing, the same place, and the phone on a stable surface. <!-- claim: FIT-BODY-PROGRESS --> <!-- claim: FIT-CAPTURE -->

**An example: a six-week program.** A member completes a baseline scan at enrollment and another scan at the end of the program. The app displays the change in waist and hip measurements alongside the member's weight log. If a coach reviews the program, the two scan records provide additional context for the next training block. The app determines which results to show and how to use them.

**Coach review.** The coach can check the change between two of the member's scans. In online coaching, the coach may never meet the member in person, and the comparison shows body change without a visit. The remote workflow is set out in [remote body measurement in online coaching](https://3dlook.ai/content-hub/remote-body-measurement-online-fitness-coaching/).

**Premium tier.** The product team decides which features sit in the paid tier. For apps that want a 3D progress view there, 3D Body Progress tracking and 3D Goal Visualization are features of the FitXpress Pro plan. A cohort test can also show whether those views change how many members upgrade. <!-- claim: FIT-PLAN -->

In every placement, the onboarding, consent, and results screens follow the app's design. The photo-capture step is the one fixed part: pose validation runs there, and keeping it unchanged protects measurement quality. <!-- claim: FIT-WHITELABEL -->

(Image 1) - Concept: A member-journey line: onboarding (baseline scan), a scheduled check-in (second scan and comparison), coach review, and a premium-tier 3D progress view marked as a FitXpress Pro plan feature. Markers show where each scan record is created. No figures.

## How visible progress may affect fitness app retention

Adjust's [mobile app retention benchmarks for 2023](https://www.adjust.com/blog/get-the-mobile-app-retention-benchmarks-for-2023/) put day-1 activity for health and fitness apps at 24% of users. By day 30, it was 7%. The figures are global and use 2022 data from all app users. <!-- claim: FIT-ADJUST -->

A 2024 scoping review by Kidman and colleagues in the [Journal of Medical Internet Research](https://www.jmir.org/2024/1/e56897) covered lifestyle behavior and mental health apps. Across the studies it reviewed, a median of 70% of users stopped using these apps within the first 100 days. The reasons included a lack of personalization. Body data can feed the personalization and coaching features described in [AI in the fitness industry](https://3dlook.ai/content-hub/ai-in-fitness-industry/). <!-- claim: FIT-KIDMAN -->

Wearable technology ranked first and mobile exercise apps second in the American College of Sports Medicine (ACSM) [2027 Worldwide Fitness Trends](https://www.newswise.com/articles/acsm-announces-top-fitness-trends-for-2027), released October 20, 2026. The ranking reflects how widely more than 1,400 fitness professionals observe each trend, and it does not report usage. <!-- claim: FIT-ACSM -->

Early in a program, weight can change slowly while body measurements shift. Weight-loss programs face the same slow-scale problem, covered in [body scanning for weight-loss progress](https://3dlook.ai/content-hub/body-scanning-technology-for-weight-loss/).

None of these sources tested body scans. A product team can test a narrower question. Does showing structured body progress increase the likelihood that a member returns for another check-in? The effect in a given app has to be measured with its own members.

## What a phone body scan produces, and what it does not

Each scan returns 80+ body measurements: circumferences such as waist, hip, chest, and thigh, along with lengths and widths. It also returns body composition estimates for body fat percentage, lean mass, and fat mass. BMI and BMR are calculated metrics. BMI comes from height and weight and does not measure body fat. <!-- claim: FXS-OUTPUTS -->

For check-ins, repeatability is especially important, because the change between two scans may be small. Repeatability testing used a real-world customer dataset with five scans per participant. For most of the evaluated measurements, typical scan-to-scan differences remained below 1 cm. The [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) describes the test conditions and treats repeatability and accuracy as separate questions. <!-- claim: FXS-REPEAT -->

A separate validation compared FitXpress measurements with expert pattern-maker tape measurements. Across the evaluated body measurements, reported accuracy was approximately 96-97%, with a typical absolute error of 1.5-2.0 cm depending on the body part. Detailed methodology is available under a non-disclosure agreement. What counts as adequate performance depends on how the measurements will be used, and the [accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) sets out how to judge it. <!-- claim: FXS-ACCURACY -->

The accuracy figures describe body measurements. Body composition estimates are derived from the measurements with height and, where provided, weight. Lean mass is one of those estimates, and it is not a direct measure of muscle. The difference matters for [muscle loss questions in fitness apps](https://3dlook.ai/content-hub/glp-1-muscle-loss-fitness-apps/). 3DLOOK's accuracy claims have not been peer-reviewed or externally validated through a third-party clinical study. <!-- claim: FIT-OUTPUTS-NOTE --> <!-- claim: FIT-EVIDENCE-LIMIT -->

## When should fitness programs use phone scanning instead of in-club hardware?

A guided scan on the member's own phone, in the studio's app or on its website, is an alternative to a hardware 3D body scanner. It fits members who train away from the club, at home or between visits. <!-- claim: FIT-CAPTURE --> <!-- claim: FIT-SDK -->

In-club hardware, such as 3D camera booths, rotating-platform scanners, and bioelectrical impedance analysis (BIA) platforms, means a club visit for every repeat scan.

### In-club hardware fits when

- Members visit the club regularly and can scan on site.
- Staff run the scan and explain the results in person.
- The club sells the scan as an in-person service.

### Progress photos fit when

- The goal is a visual reminder for the member.
- The app needs no measurements or structured data.
- The team accepts that photos vary with lighting, pose, and clothing.

### A phone scan fits when

- Members train at home or between club visits.
- Each check-in calls for a structured record.
- A coach reviews scan results remotely.

The options can work together. Each method should keep its own trend line, because numbers from different methods are not interchangeable. The [comparison of two-photo, video, and hardware body scanning](https://3dlook.ai/content-hub/body-scanning-technology-comparison/) sets out those differences. Integration details and plans are on the FitXpress page for a [mobile alternative to a gym body scanner](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/).

## What should a fitness app look for in smartphone body composition tracking?

A fitness app needs software that runs the capture inside the app, returns a structured record, and states the reference behind its figures. FitXpress by 3DLOOK captures two smartphone photos inside the app through the FitXpress SDK. The API then delivers 80+ body measurements and body composition estimates to the app. <!-- claim: FXS-SPEED --> <!-- claim: FXS-OUTPUTS --> <!-- claim: FXS-DELIVERY -->

- **Capture inside the app.** Web and mobile SDKs are available, with supported iOS and Android integrations. In the SDK, Real-Time Pose Validation pauses capture until pose and framing requirements are met, which helps avoid retakes. Voice prompts support members who scan without help. Because that validation happens in the SDK's capture layer, the recommended setup pairs the SDK with the API. <!-- claim: FIT-SDK --> <!-- claim: FIT-RTPV -->
- **A record inside the platform.** Results arrive as structured data that the app's own screens and coaching tools can use. The FitXpress Admin Panel is optional, for teams that want to monitor and export results without building a dashboard. <!-- claim: FXS-DELIVERY -->
- **Evidence with its reference.** Published figures should name the reference method, such as expert tape measurement or dual-energy X-ray absorptiometry (DXA), along with the protocol behind them. FitXpress publishes its figures for body measurements: accuracy against expert pattern-maker tape measurements, and scan-to-scan repeatability. Its composition estimates are derived from those measurements. <!-- claim: FXS-ACCURACY --> <!-- claim: FXS-REPEAT --> <!-- claim: FIT-OUTPUTS-NOTE -->
- **Labeled estimates.** Results screens should show composition as estimates, and BMI and BMR as calculated metrics.

## How to test a body scan with a member cohort

The team writes its hypothesis before launch. A testable example: members who see the change between two scans return for the next check-in more often than members who log weight only. The baseline scan keeps the same placement for the whole test.

The primary outcome is the share of members who come back. Secondary metrics are scan completion rate, retake rate, onboarding completion, and premium conversion if the feature is offered in a paid tier. Return rates measure engagement; the secondary metrics also capture the friction a new step adds.

Without a comparison group, a rise in check-in returns could come from the season, a campaign, or another release. Random assignment, where practical, separates the scan's effect from those factors. Fixing the success threshold before launch helps keep a borderline result from being read as a win.

Scans in the test follow the same capture conditions as any check-in. Members who cannot complete the standard capture need a documented fallback, and their results are reported separately.

## Frequently asked questions

### Is a phone body scan the same as a DXA scan?

They are different methods. FitXpress is not equivalent to DXA, BIA, or a calibrated scale when the workflow, protocol, or regulatory standard requires those methods. For progress tracking, the comparison that matters is between scans taken with the same method. [AI body scanners and DXA (also written DEXA)](https://3dlook.ai/content-hub/ai-body-scanners-vs-dexa-scans/) compares the two in detail. <!-- claim: FIT-EVIDENCE-LIMIT -->

### Can members with a physical disability use the scan?

FitXpress was not specifically trained on data representing people with physical disabilities, and its measurement performance has not been established for this population. This matters when a disability affects the standard standing pose or capture sequence. In those cases, the app needs a documented alternative measurement path. <!-- claim: FXS-POPULATION -->

### Does 3DLOOK know which member a scan belongs to?

Scan records are associated with anonymized, randomly generated IDs; 3DLOOK cannot identify a specific individual from stored scan records. The platform connects each scan ID to its own member profile and chooses which scans to compare. The [FitXpress data, privacy, and security answers](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) cover retention, hosting, and regulatory questions. <!-- claim: FXS-IDS --> <!-- claim: FIT-BODY-PROGRESS -->

## Next steps

Map the check-ins the app already runs and pick the one where a scan record would change what the member sees. Then see how FitXpress handles [body composition tracking for fitness apps](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/), or [book a demo](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/#form).
