---
slug: glp-1-muscle-loss-fitness-apps
title: "GLP-1 Muscle Loss: What Fitness Apps Can Track Beyond Scale Weight"
status: published
published_url: https://3dlook.ai/content-hub/glp-1-muscle-loss-fitness-apps/
article_published_time: 2026-10-29T08:52:54+00:00
article_modified_time: 2026-10-29T09:30:49+00:00
captured_from_live: 2026-11-06
capture_method: "scripts/capture-live.py — curl of the live page, body converted to markdown; images, eBook CTA and author bio dropped"
source_of_truth: live page
---

# GLP-1 Muscle Loss: What Fitness Apps Can Track Beyond Scale Weight

What a fitness app progress view can show members on GLP-1 treatment and what research says about GLP-1 muscle loss.

By Assel Sekerova

Published: October 29, 2026

## Why GLP-1 treatment is a question for fitness apps

A member taking a glucagon-like peptide-1 (GLP-1) medication logs a weight loss in a fitness app. The number shows the change in weight. It does not show whether fat mass, lean mass, or fluid made up the change.

A fitness app can show weight, body measurements, body composition estimates, and strength-training history together. A mobile body scan cannot determine whether a member has lost muscle or establish the cause of a change in lean mass.

[Structured body data](https://3dlook.ai/content-hub/ai-in-fitness-industry/) already supports progress tracking, personalization, and digital coaching in fitness apps. Waist, hip, thigh, and upper-arm circumferences record changes in body dimensions at specific sites. A guided smartphone scan can capture them remotely.

**Scope note.** This article addresses progress tracking in fitness and coaching apps, including apps operated by GLP-1 programs. FitXpress is not a medical device and does not evaluate medication, dosing, or side effects. Treatment decisions remain with the prescribing clinician.

Some members on GLP-1 treatment also follow a strength program in the app. The app already stores their training history, including strength progression and completed sessions. A weight chart alone leaves that training record disconnected from body-change data. With [body composition tracking in fitness apps](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/), the app can add circumference measurements and composition estimates to that record at each check-in.

GLP-1 programs also need [progress records that extend beyond scale weight](https://3dlook.ai/content-hub/glp-1-market/) for recurring reviews. The effect of [visual progress tracking on adherence and retention](https://3dlook.ai/content-hub/visual-progress-tracking-glp1-adherence-retention/) requires separate evaluation. In a fitness app, the immediate task is to display body data alongside training history. [Explore FitXpress for fitness apps](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/)

## What the evidence says about GLP-1 muscle loss, and what a scan cannot determine

A 2024 review by [Neeland, Linge, and Birkenfeld](https://pubmed.ncbi.nlm.nih.gov/38937282/) in *Diabetes, Obesity and Metabolism* examined changes in lean mass with GLP-1-based therapies. The review reports that in some studies, reductions in lean mass accounted for 40% to 60% of total weight loss. Other studies in the same review put the share at approximately 15% or less.

The same review notes that changes in lean mass may not always reflect changes in muscle. Its definition of lean mass also covers organs, bone, fluids, and water in fat tissue. In the studies reviewed, changes in skeletal muscle volume appeared broadly consistent with what the authors expected given participants’ age, disease status, and weight loss. That population-level observation does not establish an individual member’s muscle health or function. A scan’s lean mass estimate cannot show what share of a member’s loss was muscle.

[A 2025 joint advisory](https://www.obesity.org/nutritional-priorities-to-support-glp-1-therapy-for-obesity/) names muscle and bone loss among the challenges of GLP-1 therapy. It comes from the American College of Lifestyle Medicine, the American Society for Nutrition, the Obesity Medicine Association, and The Obesity Society. The advisory supports strength training, alongside adequate protein intake, as part of broader nutritional and medical management. An app that offers workouts can support one part of that guidance.

## What a fitness progress view can show for members on GLP-1 treatment

The app team decides what its progress view displays, how each value is labeled, and which conclusions the app avoids. Those choices matter more when a member’s weight changes due to factors outside the training program.

| **App displays** | **Source** | **Interpretation shown to the member** |
|---|---|---|
| Weight trend | Member-entered or synced scale reading | Total weight change |
| Waist and other circumferences | Guided scans | Measurement changes, subject to capture variation |
| Fat and lean mass estimates | FitXpress calculation using scan-derived measurements, height, and the weight supplied by the app | Estimated trends: lean mass is not muscle mass |
| Completed strength sessions and performance | Fitness app | Training context alongside the body-data trends |

Weight in the progress view is the value the member enters or the app syncs from a connected scale. Body composition estimates are derived from body measurements, height, and, optionally, weight. In this workflow, the app sends the member’s current progress-view weight as an optional input with each scan. Body fat percentage is calculated using an anthropometric formula applied to those measurements. These are model-derived estimates to review alongside weight and measurements. They do not determine which tissue changed.

Sometimes the trends disagree, as when weight falls, and the waist measurement stays the same. The member or coach first reviews capture conditions and earlier readings. The app avoids assigning a cause from one scan, including a claim that the training program caused a measured change. If a member has a clinical concern about their results, the app directs them to contact their prescribing clinician. Any transfer of records between services follows the applicable sharing arrangements. The app does not generate any medication or clinical advice.

When the prescribing provider already records body composition using dual-energy X-ray absorptiometry (DXA) or bioelectrical impedance analysis (BIA), the app’s scans provide a second record obtained by a different method. Compare results with earlier results obtained using the same method. [Remote body measurement for online fitness coaching programs](https://3dlook.ai/content-hub/remote-body-measurement-online-fitness-coaching/) compares scales, tape measurements, photos, BIA, DXA, and mobile scans method by method.

## How to run comparable body scan check-ins

On the app’s side, comparable check-ins involve five parts: a baseline, a cadence, capture conditions, a review of differences, and an alternative path.

**Baseline.** The first scan occurs during onboarding or at the start of a strength program, using the same guided capture as subsequent scans. A member may already be partway through treatment when the app’s record begins. A later scan can establish a new baseline, but it cannot recreate the earlier measurement.

**Cadence.** Check-ins sit at defined points, such as the end of a training block. Set the check-in interval according to the program schedule, expected changes, member burden, and variation in the specific measurements being compared.

**Capture conditions.** Members wear similar clothing and scan at about the same time of day, in the same setting. The guided flow checks pose and capture quality.

**Review of differences.** As in [online coaching programs](https://3dlook.ai/content-hub/remote-body-measurement-online-fitness-coaching/), the smallest difference worth showing a member depends on observed scan-to-scan variation and the check-in interval. Smaller differences can stay in the record without a callout in the member’s view.

**An alternative path.** FitXpress was not specifically trained on data representing people with physical disabilities, and its measurement performance has not been established for this population. This matters when a disability affects the standard standing pose or capture sequence. The app can offer manual measurements or a weight-only progress view to members who cannot use standard capture. The progress view labels the method behind each value and keeps results from different methods as separate trends.

## Where FitXpress fits, and what to test in a pilot

3DLOOK’s FitXpress provides [body scanning for fitness apps](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/) and supports body composition progress tracking inside the app’s own interface. The app embeds guided front-and-side photo capture through a web or mobile software development kit (SDK). The app uses an application programming interface (API) to submit scans and retrieve results, then displays selected outputs in its progress view. FitXpress processes the captured photos into structured results in under 45 seconds. The outputs include 80+ body measurements, body composition estimates (body fat percentage, fat mass, and lean mass), and a 3D model. BMI and basal metabolic rate (BMR) are calculated metrics. GLP-1 programs that run their own member app can use the same integration.

The app company links each scan identifier to its own member record and chooses which two scans to compare. 3DLOOK does not track individuals or determine whether two scans belong to the same person.

When a member’s treatment is managed through a separate prescribing service, the fitness app company and the prescribing provider may each maintain different records. Sharing records between the fitness app company and the prescribing provider depends on the [applicable lawful basis](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/), privacy notices, member permissions, and the agreements between them. Consent is required in some workflows.

Repeatability matters for a progress view because each check-in is compared with an earlier scan. The [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) evaluates repeatability separately from accuracy. Internal repeatability testing used a real-world customer dataset with five repeated scans per participant. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm.

A separate internal validation compared FitXpress measurements with expert pattern-maker tape measurements. Across the evaluated body measurements, [reported accuracy](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) was approximately 96-97%, with a typical absolute error of 1.5-2.0 cm depending on the body part. Detailed methodology is available under a non-disclosure agreement.

These figures describe body measurements. They are not validated for accuracy in measuring lean mass, detecting muscle loss, or detecting the smallest meaningful change during GLP-1 treatment.

Some clinical protocols and research studies require DXA or professional BIA. FitXpress is not equivalent to DXA, BIA, or a calibrated scale when the workflow, protocol, or regulatory standard requires those methods.

Before launch, the app team defines the pilot period, eligible members, and success criteria. Track capture completion, retakes, the proportion of members with a valid baseline and follow-up scan, scheduled check-in completion, and use of the progress view. Compare check-in behavior with a comparable pre-launch period or cohort where possible, and review member and coach feedback before a wider rollout.

## Next steps

Compare the app’s current progress view with what members on GLP-1 treatment need to see. Then [see how FitXpress supports body composition tracking in connected and digital fitness apps](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/).

## FAQ

### Can a mobile body scan measure muscle loss during GLP-1 treatment?

A FitXpress scan does not measure muscle or muscle loss. The lean mass output is an estimate, and lean mass includes more than muscle. Where a protocol requires DXA, that method applies.

### Does a fitness app need to know whether a member takes a GLP-1 medication?

Not for body composition tracking itself, because the scan and the progress view need only photos and basic profile details. Asking about medication is a [health data decision](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) that involves purpose, lawful basis, notice, and consent, where required.

Related reading:
- [GLP-1 Market Growth and the Need for Better Patient Progress Tracking](https://3dlook.ai/content-hub/glp-1-market/)
- [Visual Progress Tracking for GLP-1 Adherence: The Secret to Long-Term Retention](https://3dlook.ai/content-hub/visual-progress-tracking-glp1-adherence-retention/)
- [7 Body Composition and Progress-Tracking Tools for Remote GLP-1 Clinics](https://3dlook.ai/content-hub/top-7-remote-body-composition-tools-glp-1-clinics/)
