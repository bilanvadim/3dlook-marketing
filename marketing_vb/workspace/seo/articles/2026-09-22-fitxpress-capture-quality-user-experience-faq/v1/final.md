---
slug: fitxpress-capture-quality-user-experience-faq
product: fitxpress
status: edited
author: Assel Sekerova
primary_keyword: capture quality
hub: off-plan (net-new, approved by Vadim 2026-09-22)
intent: MOFU
word_count: 2039
editing_passes: 5
ai_density_before: 0.44
ai_density_after: 0.44
claims_verified: [FXS-SPEED, FXS-OUTPUTS, FXS-DELIVERY, FXS-ACCURACY, FXS-REPEAT, FXS-POPULATION, FXS-LIFECYCLE, FXS-IDS, FXS-SCOPE, FXS-MEDICAL, FX-CQ-001, FX-CQ-002, FX-CQ-003, FX-CQ-004, FX-CQ-005, FX-CQ-006, FX-CQ-007, FX-CQ-008]
changes_summary: |
  - Citations: none repeated (internal links only, each once). Accuracy and repeatability kept in one paragraph with the framework link, in accuracy-formulations.md short forms; "depend on" became "vary by".
  - Dedupe: intro scope line rewritten ("provides structured body data for review ... Clinical interpretation stays with that team") so it no longer mirrors the Q8 boundary (lint pair L25~L155 0.71 gone). Q8 direct answer no longer repeats step 1 (L140~L144 gone).
  - "front and side" 6 -> 4 in prose (kept Q1, image caption, Q8 step 2, Q10). "reduces avoidable variation" 3 -> 1 (intro only). "app or web experience" 3 -> 2.
  - Q1: merged the two consistency sentences into one; cut the aphorism "The capture step shapes the output"; the own-camera-flow claim now states the mechanism (it removes the checks). "Guidance narrows the ways a scan can go wrong" replaced with a hedged statement.
  - Q4: direct answer now carries the sport/regular/oversized classification once (was stated twice); "The flag also travels with the results" (attributed behaviour) rewritten as a payload statement; limitation sentence merged and tied to onboarding with "therefore".
  - Q7: cut "The setup is simple" (promotional); removed "described above" (page reference); privacy at home expanded into a concrete practical condition; closing points to the program's failed-scan path.
  - Intro: reframe question turned into a plain statement; "It does not remove the need for ..." rewritten as a positive requirement.
  - Next steps: slogan line ("Instructions, retakes, and alternative routes complete the program around it") replaced with a pilot recommendation; CTA verbatim.
  - FX-CQ-004 wording aligned to the pack ("protects measurement accuracy", was "consistency").
  - "the customer" varied to "the organization" where no deployment or legal role is meant (Q8 prose, Q9).
  - No reviewer-verbatim text split (none over 25 words).
self_check: |
  - Still machine-like after pass 1: staccato rhythm (mean 11.3 words, many 6-8 word declaratives in a row), two refrains ("reduces avoidable variation", "front and side"), a slogan close, and Q4 saying the same classification twice. Fixed by merging paired short sentences, deduping the refrains, replacing the close with a pilot recommendation.
  - Position was missing: the draft only stated facts. Added two practitioner caveats with no new claims (custom camera flow removes the checks; privacy at home as a practical condition for form-fitting clothing photos).
  - Remaining: FAQ register stays declarative and even by design (direct answer first); Quick answers table repeats the brief's cells nearly verbatim.
  - Gate numbers: mean_words 12.2, p90 18, over_25 0 (0.0%), over_35 0; detector CLEAN 0.44/1000 (one soft marker, the licensed RTPV clinical boundary in the table).
---

# FitXpress User Experience and Capture Quality FAQ

By Assel Sekerova

Before committing to a build, remote-care and digital-health teams usually ask whether users can complete a two-photo scan reliably without a technician present.

FitXpress is guided two-photo body measurement technology. Programs embed it in an existing app or web experience through a web or mobile software development kit (SDK) and an application programming interface (API). <!-- claim: FXS-DELIVERY --> The FAQ covers the user experience, capture-quality controls, retakes, self-scanning, workflow integration, and timing.

Capture quality depends on the technology and on the conditions of the scan. Guided capture reduces avoidable variation. The program still needs clear instructions, advice on clothing and phone placement, a retake route, and an alternative path for users who cannot scan.

*Scope: FitXpress provides structured body data for review by the organization's care team. Clinical interpretation stays with that team.* <!-- claim: FXS-SCOPE -->

## Quick answers

| **Topic** | **Direct answer** | **Important qualification** |
|---|---|---|
| Photo capture | FitXpress guides the user through front and side photo capture. <!-- claim: FXS-SPEED --> | Usable results still depend on suitable capture conditions. |
| Positioning | Real-Time Pose Validation (RTPV) provides real-time positioning and framing feedback. <!-- claim: FX-CQ-002 --> | RTPV is a capture-quality control, not a clinical posture assessment. |
| Clothing | Clothing conditions are checked during the capture process. <!-- claim: FX-CQ-003 --> | Loose, layered, or oversized clothing can still affect the visible body outline. |
| Self-scanning | Users can complete supported capture flows independently. | Accessibility, available space, and device placement still matter. |
| Retakes | The capture flow can direct the user to correct capture problems and try again. | Not every possible quality problem is detected automatically. |
| Workflow | Capture can be embedded through web or mobile SDKs and connected to the API. <!-- claim: FX-CQ-005 --> | Clinical interpretation and decisions remain outside FitXpress. <!-- claim: FXS-SCOPE --> |
| Timing | The full processing pipeline returns results in under 45 seconds. <!-- claim: FXS-SPEED --> | Onboarding and capture time depend on the implementation. |

## How FitXpress controls capture quality

### How does FitXpress help users capture usable photos?

FitXpress guides the user through a standardized front and side photo capture inside the SDK flow. <!-- claim: FXS-SPEED --> Real-time feedback on positioning and framing runs before each photo. <!-- claim: FX-CQ-002 -->

Capture runs only through the supported SDK flow. Every scan follows the same instructions and the same checks, which supports consistency across repeated scans of the same person.

Replacing the SDK capture with a custom camera flow removes those checks. Implementations that do so see meaningfully worse accuracy. <!-- claim: FX-CQ-001 -->

The guidance reduces avoidable errors, although lighting, clothing, and phone placement still affect each result. The processing that follows capture is explained in [how two photos become structured body data](https://3dlook.ai/content-hub/3dlook-turns-two-photos-structured-body-data/).

(Image 1) - Guided capture and quality-control flow: guided instructions, positioning and framing checks (RTPV), clothing check, front and side capture, processing in under 45 seconds, structured results. <!-- claim: FXS-SPEED --> A retake loop runs back from the checks. Clinical review sits outside the product, in the customer's workflow.

### What is Real-Time Pose Validation (RTPV)?

Real-Time Pose Validation (RTPV) is the real-time pose and tilt validation built into the FitXpress capture SDK. It checks position and framing during capture and guides the user to adjust before each photo. <!-- claim: FX-CQ-002 -->

RTPV compares the user's position, the framing, and the phone's tilt with the capture requirements. Guidance appears on screen while the check runs, allowing the user to correct the setup before the photo is taken. Within the capture flow, RTPV is the validation layer. <!-- claim: FX-CQ-001 -->

Skeletal tracking runs on-device or live in the browser, and face obfuscation is applied automatically. <!-- claim: FX-CQ-002 -->

RTPV is a capture-quality and positioning control. It does not assess posture as a medical, musculoskeletal, or health condition.

The customer brands the surrounding experience, such as onboarding and the results display. <!-- claim: FX-CQ-008 --> The photo capture layer where RTPV runs is not customizable. That restriction is a design decision that protects measurement accuracy. <!-- claim: FX-CQ-004 -->

### What happens when a user's position does not meet the capture requirements?

The capture flow tells the user what to correct and guides them to another attempt. The prompts address position, framing, and phone placement. <!-- claim: FX-CQ-002 -->

The corrections fall into four groups:

- **Repositioning.** The user may be asked to step back or turn to the side.
- **Framing.** The prompt asks the user to bring the full body into the frame.
- **Phone angle and placement.** The user adjusts the tilt of the phone or where it stands.
- **Another attempt.** The user takes the photo again where needed.

Pose validation is designed to reduce retakes. <!-- claim: FX-CQ-002 --> Some users will still need more than one attempt, and the program's support plan should allow for that.

### What happens when clothing may affect scan quality?

The Clothing Detector is a capture-quality feature. It classifies clothing fit for each scan as sport, regular, or oversized. When attire may affect the scan, it flags the condition and prompts the user. <!-- claim: FX-CQ-003 -->

Clothing matters because the scan relies on a visible body outline. Form-fitting or regular-fit clothing keeps that outline visible. <!-- claim: FX-CQ-007 --> Oversized, loose, layered, or body-obscuring garments can hide it. After a prompt, the flow may direct the user to change clothing or repeat the capture.

The response payload also carries the clothing classification as technical data for the customer's team. <!-- claim: FXS-LIFECYCLE -->

The classification covers fit categories and will not catch every garment issue that could affect a scan. Clothing instructions during onboarding therefore remain part of the program design.

## Capture conditions, failed scans, and self-scanning

### How much do user behavior and capture conditions affect the results?

Input conditions matter, and the size of the effect depends on the condition. No single percentage describes it.

The main conditions are positioning, framing, camera placement and angle, lighting, distance from the camera, and clothing. Pose and tilt validation in the SDK is the single biggest factor in measurement accuracy. <!-- claim: FX-CQ-001 --> For repeated scans, using the same setup at baseline and at follow-up supports comparable results.

Three terms describe different things:

- **Accuracy** is how close a result is to the selected reference method.
- **Repeatability** is how consistent repeated scans are under comparable conditions.
- **Capture quality** is whether the submitted photos meet the requirements for processing.

In 3DLOOK's internal repeatability testing, typical scan-to-scan differences remained below 1 cm for most of the evaluated measurements. <!-- claim: FX-CQ-009 --> A separate internal validation compared FitXpress measurements with expert pattern-maker tape measurements. Across the evaluated body measurements, reported accuracy was approximately 96-97%, with a typical absolute error of 1.5-2.0 cm depending on the body part. <!-- claim: FX-CQ-010 --> These figures vary by reference method, protocol, evaluated population, measurement, and capture conditions. The [body-scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) sets out the reference behind each figure and the limits of the evidence.

The figures describe performance under the tested conditions. They do not guarantee the result of any single scan.

(Image 2) - Evidence panel with three columns: accuracy against a reference method, repeatability across comparable scans, and capture-quality controls before processing. Definitions only, no figures.

### What happens if a user cannot complete a valid scan?

The program needs defined exception handling for this case. FitXpress provides corrective prompts and retakes; the route beyond that is a program design decision.

An exception route can include:

- Corrective instructions and retakes inside the capture flow.
- A defined support route, such as help from program staff.
- Accessibility considerations, planned before launch.
- An assisted or alternative capture path, where appropriate.
- An alternative workflow for users who cannot or prefer not to scan.

Remote scanning is one way to take part in a program. Users who do not scan still need a route that keeps them in it.

FitXpress was not specifically trained on data representing people with physical disabilities, and its measurement performance has not been established for this population. This matters when a disability affects the standard standing pose or capture sequence. In those cases, the program needs a documented alternative measurement path. <!-- claim: FXS-POPULATION -->

### Can users complete a scan alone at home?

Yes, in a supported self-scan flow. The flow guides the user through both photos without a technician or a dedicated scanner.

A standard smartphone is enough, and no specialized scanning hardware is needed. The phone stands vertically on a flat surface, such as a table or counter. <!-- claim: FX-CQ-007 --> The user then stands in front and side positions while on-screen feedback guides positioning in real time. <!-- claim: FX-CQ-002 --> Standard indoor lighting is fine, and any background works. <!-- claim: FX-CQ-007 -->

In a body scan app built on FitXpress, completion still depends on the person and the setting. Mobility, available space, smartphone access, and the ability to follow the positioning instructions all affect it. Privacy at home is a practical condition too: the user needs a space where standing for photos in form-fitting clothing is acceptable.

Some users and some homes are not suited to self-scanning. Those users need the assisted or alternative path that the program defines for failed scans.

## Workflow integration, timing, and outputs

### Can FitXpress be integrated into a telehealth or clinical workflow?

Yes. The organization embeds the guided capture step in its own product, and the outputs return to its workflow for review. <!-- claim: FXS-DELIVERY -->

A typical sequence has six steps:

1. The customer places the guided capture step in its app or web experience.
2. The user completes front and side capture.
3. The customer's backend submits the required data to the FitXpress API.
4. FitXpress processes the scan and returns structured outputs.
5. The customer stores, displays, or routes the outputs according to its workflow.
6. The care team or another authorized professional reviews the information.

Integration options include the Camera SDK (React) for web and hybrid apps and native SDKs for iOS and Android. A server-to-server API connects the organization's backend. <!-- claim: FX-CQ-005 --> The optional FitXpress Admin Panel serves teams that do not build their own dashboard. <!-- claim: FXS-DELIVERY -->

Capture and results can sit inside the organization's own interface, such as a telehealth or body measurement app. Results can also stay server-side only, in which case the user sees a submission confirmation. <!-- claim: FX-CQ-008 --> [FitXpress for telehealth and digital health](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/) describes these deployments in more detail.

FitXpress supports clinician or care-team review. Clinical assessment, treatment, and eligibility decisions stay with the customer's clinicians or other designated decision-makers. <!-- claim: FXS-SCOPE --> FitXpress does not replace a reference method that a protocol requires. FitXpress is not a medical device. <!-- claim: FXS-MEDICAL -->

Storage, retention, and regulatory questions are answered in the [FitXpress data, privacy, security, and regulatory FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/).

### How long do capture and processing take?

The full FitXpress processing pipeline returns results in under 45 seconds. <!-- claim: FXS-SPEED --> Onboarding and capture time depend on the implementation.

The flow has three stages:

- **Onboarding and preparation.** The organization's own onboarding screens set the length of this stage.
- **Photo capture.** Capture time varies with how quickly the user follows the positioning prompts and whether a retake is needed.
- **Processing and delivery.** This is the stage the under-45-second figure describes.

Total time from first screen to results is therefore determined by the onboarding design and by each user's capture.

### Can users upload existing photos instead of completing the guided capture?

No. Existing-photo uploads are not supported in the standard FitXpress workflow. Capture runs through the SDK, and access to the device's camera roll is disabled. <!-- claim: FX-CQ-006 -->

The system needs front and side photos taken under defined conditions. RTPV and the Clothing Detector run during the supported flow, and a stored photo never passed through those checks. <!-- claim: FX-CQ-002 -->

Camera position and capture context also contribute to consistency between scans. A photo from the camera roll does not carry the same controlled capture record.

### What progress outputs are available after a successful scan?

Depending on the selected configuration, a successful scan can return the following outputs. <!-- claim: FXS-OUTPUTS -->

- 80+ body measurements.
- Calculated metrics such as BMI and basal metabolic rate (BMR), where the required inputs are provided. Height is submitted with the scan; weight is optional. <!-- claim: FXS-LIFECYCLE -->
- Body-composition estimates: body fat percentage, fat mass, and lean mass.
- A 3D body model.
- Body Progress comparisons between two scans that the customer selects, matched by scan ID.

The customer decides whether and how progress tracking is enabled. Scan records carry randomly generated IDs, and 3DLOOK cannot identify a specific individual from them. <!-- claim: FXS-IDS --> How programs present results over time is covered in [mobile body scanning and patient engagement](https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/).

## Next steps

A short pilot with the program's own users can show how completion, retakes, and support requests behave with its onboarding and its exception route.

Ready to evaluate guided remote body-data capture for your product? [Book a demo](https://3dlook.ai/book-a-demo/) to review the FitXpress capture flow, integration options, and data-quality controls with the 3DLOOK team.
