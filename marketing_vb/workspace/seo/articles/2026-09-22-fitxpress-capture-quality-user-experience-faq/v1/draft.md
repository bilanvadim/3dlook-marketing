---
slug: fitxpress-capture-quality-user-experience-faq
product: fitxpress
section: full
status: draft
author: Assel Sekerova
primary_keyword: capture quality
hub: off-plan (net-new, approved by Vadim 2026-09-22)
cluster: capture quality and user experience
intent: MOFU
word_count: 2046
claims_used: [FXS-SPEED, FXS-OUTPUTS, FXS-DELIVERY, FXS-ACCURACY, FXS-REPEAT, FXS-POPULATION, FXS-LIFECYCLE, FXS-IDS, FXS-SCOPE, FXS-MEDICAL, FX-CQ-001, FX-CQ-002, FX-CQ-003, FX-CQ-004, FX-CQ-005, FX-CQ-006, FX-CQ-007, FX-CQ-008]
---

# FitXpress User Experience and Capture Quality FAQ

By Assel Sekerova

Remote-care and digital-health teams often ask one question before they commit to a build. Can users complete a two-photo scan reliably without a technician present?

FitXpress is guided two-photo body measurement technology. Programs embed it in an existing app or web experience through a web or mobile software development kit (SDK) and an application programming interface (API). <!-- claim: FXS-DELIVERY --> The FAQ covers the user experience, capture-quality controls, retakes, self-scanning, workflow integration, and timing.

Capture quality depends on the technology and on the conditions of the scan. Guided capture reduces avoidable variation. It does not remove the need for clear instructions, suitable clothing, careful phone placement, retakes, and an alternative route.

*FitXpress supports review by the organization's care team. Clinical interpretation and decisions stay outside the product.* <!-- claim: FXS-SCOPE -->

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

Every scan follows the same instructions and the same checks. That shared procedure supports consistency across repeated scans of the same person. Capture runs only through the supported SDK flow, which keeps the procedure identical from one scan to the next.

The capture step shapes the output. Implementations that replace the SDK capture with their own camera flow see meaningfully worse accuracy. <!-- claim: FX-CQ-001 -->

Guidance narrows the ways a scan can go wrong. Lighting, clothing, and phone placement still affect each result. The processing that follows capture is explained in [how two photos become structured body data](https://3dlook.ai/content-hub/3dlook-turns-two-photos-structured-body-data/).

(Image 1) - Guided capture and quality-control flow: guided instructions, positioning and framing checks (RTPV), clothing check, front and side capture, processing in under 45 seconds, structured results. <!-- claim: FXS-SPEED --> A retake loop runs back from the checks. Clinical review sits outside the product, in the customer's workflow.

### What is Real-Time Pose Validation (RTPV)?

Real-Time Pose Validation (RTPV) is the real-time pose and tilt validation built into the FitXpress capture SDK. It checks position and framing during capture and guides the user to adjust before each photo. <!-- claim: FX-CQ-002 -->

RTPV compares the user's position, the framing, and the phone's tilt with the capture requirements. Guidance appears on screen in real time. The user can correct the setup before the photo is taken. Within the capture flow, RTPV is the validation layer. <!-- claim: FX-CQ-001 -->

Skeletal tracking runs on-device or live in the browser, and face obfuscation is applied automatically. <!-- claim: FX-CQ-002 -->

RTPV is a capture-quality and positioning control. It does not assess posture as a medical, musculoskeletal, or health condition.

The customer brands the surrounding experience, such as onboarding and the results display. <!-- claim: FX-CQ-008 --> The photo capture layer where RTPV runs is not customizable. That is a design decision to protect measurement consistency. <!-- claim: FX-CQ-004 -->

### What happens when a user's position does not meet the capture requirements?

The capture flow tells the user what to correct and guides them to another attempt. The prompts address position, framing, and phone placement. <!-- claim: FX-CQ-002 -->

Each instruction names the correction in plain terms:

- **Repositioning.** The user is asked to step back or turn to the side.
- **Framing.** The prompt asks the user to bring the full body into the frame.
- **Phone angle and placement.** The user adjusts the tilt of the phone or where it stands.
- **Another attempt.** The user takes the photo again where needed.

Pose validation is designed to reduce retakes. <!-- claim: FX-CQ-002 --> Some users will still need more than one attempt, and the program's support route should expect that.

### What happens when clothing may affect scan quality?

The Clothing Detector is a capture-quality feature. It classifies clothing fit during capture and prompts the user when attire may affect the scan. <!-- claim: FX-CQ-003 -->

Clothing matters because the scan relies on a visible body outline. Form-fitting or regular-fit clothing keeps that outline visible. <!-- claim: FX-CQ-007 --> Oversized, loose, layered, or body-obscuring garments can hide it.

For each scan, the Clothing Detector classifies fit as sport, regular, or oversized. When attire is unsuitable for capture, it flags the condition and prompts the user. <!-- claim: FX-CQ-003 --> The flow may then direct the user to change clothing or repeat the capture.

The flag also travels with the results. The response payload carries the clothing classification as technical data for the customer's team. <!-- claim: FXS-LIFECYCLE -->

The classification covers fit categories. It does not identify every garment issue that could affect a scan. Clear clothing instructions during onboarding remain part of the program design.

## Capture conditions, failed scans, and self-scanning

### How much do user behavior and capture conditions affect the results?

Input conditions matter, and the size of the effect depends on the condition. No single percentage describes it.

The main conditions are positioning, framing, camera placement and angle, lighting, distance from the camera, and clothing. Pose and tilt validation in the SDK is the single biggest factor in measurement accuracy. <!-- claim: FX-CQ-001 --> For repeated scans, consistency between baseline and follow-up also matters. The same setup each time supports comparable results.

Three terms describe different things:

- **Accuracy** is how close a result is to the selected reference method.
- **Repeatability** is how consistent repeated scans are under comparable conditions.
- **Capture quality** is whether the submitted photos meet the requirements for processing.

In 3DLOOK's internal repeatability testing, typical scan-to-scan differences remained below 1 cm for most of the evaluated measurements. <!-- claim: FXS-REPEAT --> A separate internal validation compared FitXpress measurements with expert pattern-maker tape measurements. Across the evaluated body measurements, reported accuracy was approximately 96-97%, with a typical absolute error of 1.5-2.0 cm depending on the body part. <!-- claim: FXS-ACCURACY --> These figures depend on the reference method, protocol, evaluated population, measurement, and capture conditions. The [body-scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) describes the methodology and the limits of the evidence.

The figures describe performance under the tested conditions. They are not a guarantee for any single scan.

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

Yes, in a supported self-scan flow. The flow guides the user through front and side capture without a technician or a dedicated scanner.

The setup is simple. A standard smartphone is enough, and no specialized scanning hardware is needed. The phone stands vertically on a flat surface, such as a table or counter. <!-- claim: FX-CQ-007 --> The user then stands in front and side positions while on-screen feedback guides positioning in real time. <!-- claim: FX-CQ-002 --> Standard indoor lighting is fine, and any background works. <!-- claim: FX-CQ-007 -->

In a body scan app built on FitXpress, completion still depends on the person and the setting. Mobility, available space, smartphone access, privacy at home, and the ability to follow the positioning instructions all affect it.

Not every user or physical environment suits self-scanning. For those cases, the alternative path described above applies.

## Workflow integration, timing, and outputs

### Can FitXpress be integrated into a telehealth or clinical workflow?

Yes. The customer embeds the guided capture step in its own app or web experience, and the outputs return to its workflow for review. <!-- claim: FXS-DELIVERY -->

A typical sequence has six steps:

1. The customer places the guided capture step in its app or web experience.
2. The user completes front and side capture.
3. The customer's backend submits the required data to the FitXpress API.
4. FitXpress processes the scan and returns structured outputs.
5. The customer stores, displays, or routes the outputs according to its workflow.
6. The care team or another authorized professional reviews the information.

Integration options include the Camera SDK (React) for web and hybrid apps and native SDKs for iOS and Android. A server-to-server API connects the customer's backend. <!-- claim: FX-CQ-005 --> The optional FitXpress Admin Panel serves teams that do not build their own dashboard. <!-- claim: FXS-DELIVERY -->

Capture and results can sit inside the customer's own interface, such as a telehealth or body measurement app. Results can also stay server-side only, in which case the user sees a submission confirmation. <!-- claim: FX-CQ-008 --> [FitXpress for telehealth and digital health](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/) describes these deployments in more detail.

FitXpress supports clinician or care-team review. Clinical assessment, treatment, and eligibility decisions stay with the customer's clinicians or other designated decision-makers. <!-- claim: FXS-SCOPE --> FitXpress does not replace a reference method that a protocol requires. FitXpress is not a medical device. <!-- claim: FXS-MEDICAL -->

Storage, retention, and regulatory questions are answered in the [FitXpress data, privacy, security, and regulatory FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/).

### How long do capture and processing take?

The full FitXpress processing pipeline returns results in under 45 seconds. <!-- claim: FXS-SPEED --> Onboarding and capture time depend on the implementation.

The flow has three stages:

- **Onboarding and preparation.** The customer's own onboarding screens set the length of this stage.
- **Front and side photo capture.** Capture time varies with how quickly the user follows the positioning prompts and whether a retake is needed.
- **Processing and delivery.** This is the stage the under-45-second figure describes.

Total time from first screen to results is therefore determined by the customer's onboarding design and by each user's capture.

### Can users upload existing photos instead of completing the guided capture?

No. Existing-photo uploads are not supported in the standard FitXpress workflow. Capture runs through the SDK, and access to the device's camera roll is disabled. <!-- claim: FX-CQ-006 -->

The system needs front and side photos taken under defined conditions. RTPV and the Clothing Detector run during the supported flow. <!-- claim: FX-CQ-002 --> A stored photo never passed through those checks.

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

Guided capture reduces avoidable variation in remote scans. Instructions, retakes, and alternative routes complete the program around it.

Ready to evaluate guided remote body-data capture for your product? [Book a demo](https://3dlook.ai/book-a-demo/) to review the FitXpress capture flow, integration options, and data-quality controls with the 3DLOOK team.
