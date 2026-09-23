---
slug: fitxpress-capture-quality-user-experience-faq
product: fitxpress
status: edited
review_round: 2
author: Assel Sekerova
primary_keyword: capture quality
hub: off-plan (net-new, approved by Vadim 2026-09-22)
intent: MOFU
word_count: 2431
editing_passes: 5
ai_density_before: 0.43
ai_density_after: 0.37
claims_verified: [FXS-SPEED, FXS-OUTPUTS, FXS-DELIVERY, FXS-LIFECYCLE, FXS-IDS, FXS-SCOPE, FXS-MEDICAL, FX-CQ-002, FX-CQ-003, FX-CQ-005, FX-CQ-006, FX-CQ-007, FX-CQ-009, FX-R1-FLOW, FX-R1-CORE, FX-R1-SDK, FX-R1-ADMIN, FX-R1-UPLOAD, FX-R2-PLACEMENT, FX-R2-STANDARD, FX-R2-CLOTH, FX-R2-SUBMIT, FX-R2-UPLOAD, FX-R2-LEAN, FX-R2-3D]
changes_summary: |
  Review 2 (review-2.md + review-2-decisions.md; decisions won, incl. over brief §7 and the pack's excluded_topics, P0). Structural round: plan.md (16 sections) followed section by section. Item table in edit-notes.md.
  - P1: Q11 "What progress outputs are available after a successful scan?" replaced by the three H3s verbatim from P1, under a new H2 "Tracking and displaying progress". The old H2 is now "Workflow integration and timing". FAQPage = 13 questions.
  - P2: Q11 opens with fat %, fat mass, lean mass estimates compared baseline vs later scan; FX-R2-LEAN terminology correction verbatim (two sentences) + "interfaces and supporting copy should use the term lean mass"; v2 output list folded in (80+ body measurements, BMI/BMR with weight optional, 3D model); Body Progress = two customer-selected scans by scan ID, customer decides tracking and presentation; FXS-IDS line kept.
  - P3: Q12 = organization controls display (FX-R2-3D), five-item combination list condensed to four bullets, 3D shape vs numbers, tissue-boundary sentence, patient-engagement link (moved here, once).
  - P4: Q13 answers from each person's actual baseline and follow-up scans. The reviewer's "does not apply a generic 5-, 10-, or 20-pound body transformation" is NOT used; goal/target-weight visualization mentioned in neither direction. Weight source named; milestone thresholds and logic belong to the program (FXS-SCOPE).
  - P5: Quick answers row "Progress" added with the decisions-file wording.
  - W1 intro: review paragraphs used; "web and mobile SDKs" became "a web or mobile software development kit (SDK)" (article_lint M1 needs the singular expansion before the first bare "SDK"). "The FAQ covers..." deleted. W2-W7 applied verbatim (FX-R2-STANDARD, FX-R2-CLOTH, W4 conditions list, FX-R2-PLACEMENT, FX-R2-SUBMIT, FX-R2-UPLOAD); W6 steps 1 and 5 now "The organization", the Q8 API sentence reduced to FX-R1-SDK wording (dropped "server-to-server ... backend").
  - V1 Illustration 1 unchanged. V2 Illustration 2 (evidence panel) deleted from Q5 and replaced after Q12 by a baseline vs follow-up progress display brief.
  - Tightening for the 2,450 ceiling: Q5 lost its bridging sentence, Q9 lost "The flow has three stages:" and the closing total-time sentence, Q6 lost its closing aphorism, Q7 merged its last two paragraphs.
  - Claim markers: FX-R1-CLOTH dropped (superseded by FX-R2-CLOTH). FX-CQ-004 removed from claims_verified (no marker since review 1). Added FX-R2-PLACEMENT/STANDARD/CLOTH/SUBMIT/UPLOAD/LEAN/3D.
  - Invariants: H1, first 10 H3 byte-identical to v2 (diff), 3 new H3 verbatim; "FitXpress is not a medical device." x1; CTA byte-identical; 5 internal links + demo once each; timing only "under 45 seconds" from the photos.
self_check: |
  - First pass PASS on every gate except M1 (plural "SDKs" in the intro did not count as expanding "SDK"); fixed with the singular form.
  - Reread of the progress section: the Q12 opener ran 26 words and ended in an abstraction ("part of the program's own design"); split into two plain statements. "The composition figures belong in the numbers" read as a slogan; replaced with a literal sentence. The Illustration 2 brief ran 33 words; split.
  - Refrain check: "fat mass and lean mass" hit x4 after the rewrite; the Q12 sentence now says "body composition". The remaining repeats (body fat percentage x4, front and side x5) are the subject terms of the answers and FAQ answers must stand alone.
  - Still reads a little templated: the three progress answers all use "direct answer + bullet list + boundary sentence". Kept, because the review gives each one as a checklist and the bullets are short noun lists; the prose around them is linked (because / which means / then).
  - Gate numbers: prose 2,431 words; sentences 144, mean_words 14.2, p90 22, over_25 0 (0.0%), over_35 0; detector CLEAN 0.37/1000, rhythm 0.37, one soft marker = licensed RTPV clinical boundary in the table.
---

# FitXpress User Experience and Capture Quality FAQ

By Assel Sekerova

Before integrating remote body capture, telehealth and digital-health teams need to know whether users can complete a two-photo scan reliably without a technician present. The answer depends on the guidance provided during capture and the conditions in which the scan is completed.

FitXpress is a guided, two-photo body-measurement technology that programs embed in their existing app or web experience. Integration is available through a web or mobile software development kit (SDK) and an application programming interface (API). <!-- claim: FXS-DELIVERY -->

Guided capture reduces avoidable variation in the photos, while the program prepares its users for the conditions that guidance cannot control. That preparation includes clear instructions, advice on clothing and phone placement, a retake route, and an alternative path for users who cannot scan.

*Scope: FitXpress provides structured body data for review by the organization's care team, and clinical interpretation stays with that team.* <!-- claim: FXS-SCOPE -->

## Quick answers

| **Topic** | **Direct answer** | **Important qualification** |
|---|---|---|
| Photo capture | FitXpress guides the user through front and side photo capture. <!-- claim: FXS-SPEED --> | Usable results depend on suitable capture conditions. |
| Positioning | Real-Time Pose Validation (RTPV) provides real-time positioning and framing feedback. <!-- claim: FX-CQ-002 --> | RTPV is a capture-quality control, not a clinical posture assessment. |
| Clothing | Clothing conditions are checked during the capture process. <!-- claim: FX-CQ-003 --> | Clothing that does not follow the body outline can hide parts of it. |
| Self-scanning | Users can complete supported capture flows independently. | Accessibility, available space, and device placement affect completion. |
| Retakes | The capture flow can direct the user to correct capture problems and try again. | Not every possible quality problem is detected automatically. |
| Workflow | Capture can be embedded through web or mobile SDKs and connected to the API. <!-- claim: FX-CQ-005 --> | Clinical interpretation and decisions remain outside FitXpress. <!-- claim: FXS-SCOPE --> |
| Timing | Structured results return in under 45 seconds from the front and side photos. <!-- claim: FXS-SPEED --> | Onboarding time depends on the organization's own screens, and capture time varies by user. |
| Progress | Programs can compare fat mass, lean mass, body fat percentage, measurements, and selected scans over time. <!-- claim: FXS-OUTPUTS --> | Lean mass is not the same as muscle mass, and milestone views are built from each person's actual scans. <!-- claim: FX-R2-LEAN --> |

## How FitXpress controls capture quality

### How does FitXpress help users capture usable photos?

FitXpress guides each user through a standardized front and side photo capture. <!-- claim: FXS-SPEED --> Before each photo, real-time feedback on positioning and framing tells the user what to adjust, which allows problems to be corrected during capture. <!-- claim: FX-CQ-002 -->

In the standard end-user flow, capture runs through the supported SDK, which provides these guided capture controls. <!-- claim: FX-R1-FLOW --> Because every scan in that flow follows the same instructions and checks, repeated scans of the same person start from comparable conditions. That comparability supports consistency between a baseline scan and the scans that follow it.

The guidance reduces avoidable errors. Lighting, clothing, and phone placement affect each result as well, and the program's own instructions shape those conditions before the checks run. What happens to the photos after capture is covered in [how two photos become structured body data](https://3dlook.ai/content-hub/3dlook-turns-two-photos-structured-body-data/).

> **[Illustration 1: Guided capture and quality-control flow]**
> Designer brief: guided instructions → positioning and framing checks (RTPV) → clothing check → front and side capture → structured results in under 45 seconds from the photos. <!-- claim: FXS-SPEED --> A retake loop runs back from the checks, and clinical review sits outside the product, in the organization's workflow.

### What is Real-Time Pose Validation (RTPV)?

Real-Time Pose Validation (RTPV) is the positioning check built into the FitXpress capture SDK. It runs during capture and compares the user's position and framing with the capture requirements before each photo is taken. <!-- claim: FX-CQ-002 -->

When the position or framing falls outside those requirements, on-screen guidance shows the user how to adjust. The problem is corrected at the moment it occurs, which makes RTPV the validation layer of the capture flow. Phone angle is a separate requirement. The SDK's guidance also covers phone tilt, which concerns the device, while RTPV concerns the person in front of it. <!-- claim: FX-CQ-006 -->

RTPV is a capture-quality and positioning control. It does not assess posture as a medical, musculoskeletal, or health condition.

The organization controls and brands the surrounding experience, including onboarding, user instructions, and the results display. <!-- claim: FX-R1-CORE --> The core capture flow in which RTPV operates is standardized to support consistent capture across users and scan sessions. <!-- claim: FX-R2-STANDARD -->

### What happens when a user's position does not meet the capture requirements?

During capture, the flow shows the user what to correct, and the user adjusts the setup and tries again. <!-- claim: FX-CQ-002 --> The prompts address position, framing, and phone placement, and each one describes the correction itself:

- **Repositioning.** The user may be asked to step back or turn to the side, depending on which requirement the position misses.
- **Framing.** When part of the body falls outside the frame, the prompt asks the user to bring the full body into view.
- **Phone angle and placement.** The user corrects the tilt of the phone or changes where it stands.

A capture that is completed and later turns out to be unusable is a different case. The user then needs another attempt, and the program decides how that attempt is offered and supported.

Pose validation is designed to reduce retakes. <!-- claim: FX-CQ-002 --> Some users need more than one attempt, and the program's support plan should allow for that.

### What happens when clothing may affect scan quality?

The Clothing Detector identifies clothing conditions that may interfere with capture. When the supported flow identifies a clothing problem, the user can be asked to adjust the clothing or repeat the capture. <!-- claim: FX-R2-CLOTH -->

Clothing matters because the scan relies on the visible body outline in both photos. Clothing that follows the body outline helps keep that outline visible, <!-- claim: FX-CQ-007 --> while loose, layered, or body-obscuring garments can hide parts of it.

Some garment issues fall outside what the detector identifies. For that reason, clothing instructions belong in the onboarding screens, before the user starts capture.

## Capture conditions, failed scans, and self-scanning

### How much do user behavior and capture conditions affect the results?

Capture conditions affect the results. The size of the effect depends on the condition and on the measurement. No single public percentage or ranking describes the effect of individual capture conditions.

The conditions that matter are positioning, framing, camera placement and angle, lighting, distance from the camera, and clothing. For repeated scans, using similar lighting, camera placement, pose, distance, and clothing conditions at baseline and at follow-up supports comparable results.

Three terms describe different properties of a scan:

- **Accuracy** is how close a result is to the selected reference method.
- **Repeatability** is how consistent repeated scans are under comparable conditions.
- **Capture quality** is whether the submitted photos meet the requirements for processing.

In 3DLOOK's internal repeatability testing, typical scan-to-scan differences remained below 1 cm for most of the evaluated measurements. <!-- claim: FX-CQ-009 --> The figure varies by protocol, evaluated population, measurement, and capture conditions, and it does not guarantee the result of any single scan. The [body-scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) sets out the validation figures, the tested population, and the methodology.

### What happens if a user cannot complete a valid scan?

The next step depends on the exception route that the program defines. FitXpress provides corrective prompts and retakes inside the capture flow, and the route beyond that is a program design decision.

An exception route can include:

- Corrective instructions and retakes inside the capture flow.
- A defined support route, such as help from program staff.
- Accessibility considerations, planned before launch.
- An assisted or alternative capture path, where appropriate.
- An alternative workflow for users who cannot or prefer not to scan.

Accessibility planning matters most for users whose mobility or health makes the standing capture positions difficult. For those users, a documented alternative measurement path gives them a way to continue in the program.

### Can users complete a scan alone at home?

Yes, in a supported self-scan flow. The flow guides the user through both photos without a technician or a dedicated scanner, and a standard smartphone is the only hardware involved.

The phone stands vertically on a stable surface around desk height. <!-- claim: FX-R2-PLACEMENT --> With the phone in place, the user stands in the front and side positions while on-screen feedback guides positioning in real time. <!-- claim: FX-CQ-002 --> Users should follow the on-screen guidance for lighting, distance, framing, and phone placement. <!-- claim: FX-CQ-007 -->

In a body scan app built on FitXpress, completion depends on mobility, available space, smartphone access, and the ability to follow the positioning instructions. Privacy at home matters too, because the user needs a space where standing for photos in fitted clothing is acceptable. Users and homes that are not suited to self-scanning need the assisted or alternative path that the program defines for failed scans.

## Workflow integration and timing

### Can FitXpress be integrated into a telehealth or clinical workflow?

Yes. The organization embeds the guided capture step in its own product, and the structured outputs return to its workflow for review. <!-- claim: FXS-DELIVERY -->

A typical sequence has six steps:

1. The organization places the guided capture step in its app or web experience.
2. The user completes front and side capture.
3. The captured data is submitted through the integration for FitXpress processing. <!-- claim: FX-R2-SUBMIT -->
4. FitXpress processes the scan and returns structured outputs.
5. The organization stores, displays, or routes the outputs according to its workflow.
6. The care team or another authorized professional reviews the information.

Integration runs through web and mobile SDKs, including supported iOS and Android integrations, and through the API. <!-- claim: FX-R1-SDK --> The optional FitXpress Admin Panel complements that integration as an interface for monitoring and exporting results. <!-- claim: FX-R1-ADMIN -->

Capture and results can sit inside the organization's own interface, such as a telehealth or body measurement app. The organization controls which outputs appear in its interface and how they are routed for review. Deployment options for telehealth programs are described on [FitXpress for telehealth and digital health](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/).

FitXpress supports clinician or care-team review, which means clinical assessment, treatment, and eligibility decisions stay with the customer's clinicians or other designated decision-makers. <!-- claim: FXS-SCOPE --> Where a protocol requires a reference method, that method stays in place. FitXpress is not a medical device. <!-- claim: FXS-MEDICAL -->

Storage, retention, and regulatory questions are answered in the [FitXpress data, privacy, security, and regulatory FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/).

### How long do capture and processing take?

FitXpress returns structured results in under 45 seconds from the two photos. <!-- claim: FXS-SPEED --> Everything before that point depends on the implementation and on the user.

- **Onboarding and preparation.** The organization's own onboarding screens determine the length of this stage.
- **Photo capture.** Capture time depends on how quickly the user follows the positioning prompts and whether a retake is needed.
- **From photos to results.** This is the stage that the under-45-second figure describes.

### Can users upload existing photos instead of completing the guided capture?

No. Users cannot upload existing photos in the standard guided FitXpress capture flow. <!-- claim: FX-R1-UPLOAD -->

The system needs front and side photos taken under defined conditions, and RTPV and the Clothing Detector operate during that supported flow. <!-- claim: FX-CQ-002 --> Camera-roll photos are outside the standard guided FitXpress flow and do not provide the same controlled capture process within the current scan session. <!-- claim: FX-R2-UPLOAD --> Camera position and capture context also contribute to consistency between scans, which matters when a program compares a follow-up scan with a baseline.

## Tracking and displaying progress

### How do you track fat loss and lean-mass change?

FitXpress can return body fat percentage, fat mass, and lean mass estimates for each successful scan. <!-- claim: FXS-OUTPUTS --> Programs track change by comparing these estimates between a baseline scan and a later scan, together with selected body measurements.

FitXpress estimates lean mass and does not provide a direct measurement of muscle mass. Lean mass includes muscle along with water, bone, organs, and other non-fat tissue. <!-- claim: FX-R2-LEAN --> For that reason, interfaces and supporting copy should use the term lean mass.

Depending on the configuration, a successful scan can also return:

- 80+ body measurements.
- Calculated BMI and basal metabolic rate (BMR), where the required inputs are provided. Height is submitted with the scan, and weight is optional. <!-- claim: FXS-LIFECYCLE -->
- A 3D body model.

Body Progress compares two customer-selected scans by their scan IDs. The customer decides whether progress tracking is enabled and how the comparison is presented to users or care teams. Scan records carry randomly generated IDs, and 3DLOOK cannot identify a specific individual from them. <!-- claim: FXS-IDS -->

### How can programs visually display fat-mass and lean-mass changes?

The organization controls how scan outputs and the 3D body model appear in its interface. <!-- claim: FX-R2-3D --> FitXpress returns the structured outputs and the 3D model, and the program designs its progress view around them.

A progress view can combine:

- Baseline and follow-up values, with the change from baseline.
- Body fat percentage, fat mass, and lean mass.
- Selected circumference changes.
- A comparison of the 3D body models generated from the two scans.

The 3D comparison shows how body shape changed between the two scans, while the numerical outputs carry the quantitative record. Visual differences between 3D models are not a direct map of fat or muscle tissue. <!-- claim: FX-R2-3D --> Changes in body composition come from the estimates shown beside the models. How programs present results over time is covered in [mobile body scanning and patient engagement](https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/).

> **[Illustration 2: Baseline versus follow-up progress display]**
> Designer brief: matching baseline and follow-up 3D body models side by side. Body fat percentage, fat mass, lean mass, and one or two circumference changes sit under clear "Baseline", "Follow-up", and "Change" labels. No body region is coloured to suggest a tissue change, and every figure is an illustrative placeholder.

### How should programs show meaningful progress at 5, 10, or 20 pounds of weight loss?

Programs show milestone progress from each person's actual baseline and follow-up scans. The same weight change can correspond to different changes in fat mass, lean mass, body shape, and circumferences from one person to the next.

Where the program collects body weight separately, the interface should name the source of that figure, such as a clinic weigh-in or a self-reported entry. Weight change then sits alongside the scan outputs:

- Fat mass and lean mass changes.
- Body fat percentage.
- Selected body measurements.
- The actual baseline-to-follow-up 3D comparison.

Milestone thresholds and the logic behind them belong to the program, because FitXpress returns scan outputs and does not detect milestones by itself. <!-- claim: FXS-SCOPE --> Placed together, these values show what changed for that person without implying that every pound lost came from fat.

## Next steps

A short pilot with the program's own users can measure completion, retakes, and support requests under its onboarding and its exception route.

Ready to evaluate guided remote body-data capture for your product? [Book a demo](https://3dlook.ai/book-a-demo/) to review the FitXpress capture flow, integration options, and data-quality controls with the 3DLOOK team.
