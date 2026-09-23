---
slug: fitxpress-capture-quality-user-experience-faq
product: fitxpress
status: edited
review_round: 1
author: Assel Sekerova
primary_keyword: capture quality
hub: off-plan (net-new, approved by Vadim 2026-09-22)
intent: MOFU
word_count: 2135
editing_passes: 5
ai_density_before: 0.44
ai_density_after: 0.43
claims_verified: [FXS-SPEED, FXS-OUTPUTS, FXS-DELIVERY, FXS-LIFECYCLE, FXS-IDS, FXS-SCOPE, FXS-MEDICAL, FX-CQ-002, FX-CQ-003, FX-CQ-004, FX-CQ-005, FX-CQ-006, FX-CQ-007, FX-CQ-009]
changes_summary: |
  Review 1 (review-1.md + review-1-decisions.md; the decisions file won where they differ). Item table in edit-notes.md.
  - A1: every answer rewritten as linked prose (because / which means / depends on / while), direct answer kept in the first 1-2 sentences. Sentence mean 12.2 -> 14.3, p90 18 -> 22, none over 25.
  - A2: the diminishing adverb removed everywhere (4 table cells, ~5 in prose); 0 left. A3/A4: no result connector of that kind, no reading-direction verb (grep in edit-notes.md).
  - A5: both illustration placements are blockquotes with a bold bracketed label and a designer brief.
  - C1 SDK-only + worse-accuracy sentence gone (FX-CQ-001 dropped). C2 RTPV = position and framing; phone tilt = separate SDK guidance. C3 skeletal tracking / face obfuscation sentence deleted. C4 "not customizable" -> core capture flow standardized, organization brands onboarding, instructions, results.
  - C5 Q3 separates capture-time correction from a completed-but-unusable capture. C6 Clothing Detector reduced to the reviewer's broader wording; sport/regular/oversized and payload dropped. C7 "single biggest factor" gone; "no single public percentage or ranking" added.
  - C8 Q5 keeps three definitions + the repeatability figure only (FX-CQ-010 dropped); framework link in the same paragraph. C9 disability sentence removed (FXS-POPULATION dropped), practical accessibility guidance kept. C10 lighting/background line replaced with the on-screen-guidance sentence.
  - C11 "web and mobile SDKs, including supported iOS and Android integrations" + API; Admin Panel = optional complementary monitoring/export interface. C12 server-side/submission-confirmation sentence replaced (FX-CQ-008 dropped). C13 one timing definition, canon: under 45 seconds from the photos to structured results (table, Illustration 1, Q9). C14 camera-roll sentence replaced with the reviewer's upload sentence.
  - Invariants: H1, 11 H3 strings and table topics byte-identical to v1; medical-device sentence and CTA verbatim; 5 internal links + demo once each.
self_check: |
  - After the first rewrite the detector flagged monotone rhythm (0.34): the linked sentences had all settled at 15-20 words. Split three of them into a short statement plus its explanation (Q1 guidance, Q2 phone angle, Q5 opening). Rhythm 0.37.
  - Refrains: "front and side" x8 and "photo is taken" x3 after the rewrite. Cut to 5 and 1 (Q4 "both photos", Q6 "standing capture positions", Q9 "two photos").
  - Machine-like on reread: "works best" in the intro (an unsupported judgment), "anyway" in Q3 (the same diminishing emphasis the reviewer flagged in A2), "a better spot" (vague). All three rewritten.
  - Remaining by design: the Q6 exception-route list and Q9 stage bullets stay as bullets (the brief lists them and they read as a checklist). The Quick answers RTPV cell keeps "not a clinical posture assessment" (licensed clinical boundary, the detector's only soft marker).
  - Gate numbers: mean_words 14.3, p90 22, over_25 0 (0.0%), over_35 0; detector CLEAN 0.43/1000, rhythm 0.37.
---

# FitXpress User Experience and Capture Quality FAQ

By Assel Sekerova

Before committing to a build, remote-care and digital-health teams usually ask whether users can complete a two-photo scan reliably without a technician present. The answer depends on how the capture step guides the user and on the conditions in which the user completes the scan.

FitXpress is guided two-photo body measurement technology, which programs embed in their existing app or web experience. The integration runs through a web or mobile software development kit (SDK) and an application programming interface (API). <!-- claim: FXS-DELIVERY --> The FAQ covers the user experience, capture-quality controls, retakes, self-scanning, workflow integration, and timing.

Guided capture reduces avoidable variation in the photos, while the program prepares its users for the conditions that guidance cannot control. That preparation includes clear instructions, advice on clothing and phone placement, a retake route, and an alternative path for users who cannot scan.

*Scope: FitXpress provides structured body data for review by the organization's care team, and clinical interpretation stays with that team.* <!-- claim: FXS-SCOPE -->

## Quick answers

| **Topic** | **Direct answer** | **Important qualification** |
|---|---|---|
| Photo capture | FitXpress guides the user through front and side photo capture. <!-- claim: FXS-SPEED --> | Usable results depend on suitable capture conditions. |
| Positioning | Real-Time Pose Validation (RTPV) provides real-time positioning and framing feedback. <!-- claim: FX-CQ-002 --> | RTPV is a capture-quality control, not a clinical posture assessment. |
| Clothing | Clothing conditions are checked during the capture process. <!-- claim: FX-CQ-003 --> | Loose, layered, or oversized clothing can affect the visible body outline. |
| Self-scanning | Users can complete supported capture flows independently. | Accessibility, available space, and device placement affect completion. |
| Retakes | The capture flow can direct the user to correct capture problems and try again. | Not every possible quality problem is detected automatically. |
| Workflow | Capture can be embedded through web or mobile SDKs and connected to the API. <!-- claim: FX-CQ-005 --> | Clinical interpretation and decisions remain outside FitXpress. <!-- claim: FXS-SCOPE --> |
| Timing | Structured results return in under 45 seconds from the front and side photos. <!-- claim: FXS-SPEED --> | Onboarding time depends on the organization's own screens, and capture time varies by user. |

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

The organization controls and brands the surrounding experience, including onboarding, user instructions, and the results display. The core capture flow where RTPV runs is standardized, a design decision intended to protect measurement accuracy. <!-- claim: FX-R1-CORE -->

### What happens when a user's position does not meet the capture requirements?

During capture, the flow shows the user what to correct, and the user adjusts the setup and tries again. <!-- claim: FX-CQ-002 --> The prompts address position, framing, and phone placement, and each one describes the correction itself:

- **Repositioning.** The user may be asked to step back or turn to the side, depending on which requirement the position misses.
- **Framing.** When part of the body falls outside the frame, the prompt asks the user to bring the full body into view.
- **Phone angle and placement.** The user corrects the tilt of the phone or changes where it stands.

A capture that is completed and later turns out to be unusable is a different case. The user then needs another attempt, and the program decides how that attempt is offered and supported.

Pose validation is designed to reduce retakes. <!-- claim: FX-CQ-002 --> Some users need more than one attempt, and the program's support plan should allow for that.

### What happens when clothing may affect scan quality?

The Clothing Detector is a capture-quality feature. It identifies clothing conditions that may interfere with capture and can prompt corrective action. <!-- claim: FX-R1-CLOTH -->

Clothing matters because the scan relies on the visible body outline in both photos. Form-fitting or regular-fit clothing keeps that outline visible, <!-- claim: FX-CQ-007 --> while oversized, loose, layered, or body-obscuring garments can hide parts of it. When the detector flags a clothing condition, the flow may direct the user to change clothing or repeat the capture.

Some garment issues fall outside what the detector identifies. For that reason, clothing instructions belong in the onboarding screens, before the user starts capture.

## Capture conditions, failed scans, and self-scanning

### How much do user behavior and capture conditions affect the results?

Capture conditions affect the results. The size of the effect depends on the condition and on the measurement. No single public percentage or ranking describes the effect of individual capture conditions.

The conditions that matter are positioning, framing, camera placement and angle, lighting, distance from the camera, and clothing. For repeated scans, using the same room, phone position, and clothing at baseline and at follow-up supports comparable results.

Three terms describe different properties of a scan:

- **Accuracy** is how close a result is to the selected reference method.
- **Repeatability** is how consistent repeated scans are under comparable conditions.
- **Capture quality** is whether the submitted photos meet the requirements for processing.

Capture-quality controls act before processing, while accuracy and repeatability describe the results that processing returns. In 3DLOOK's internal repeatability testing, typical scan-to-scan differences remained below 1 cm for most of the evaluated measurements. <!-- claim: FX-CQ-009 --> The figure varies by protocol, evaluated population, measurement, and capture conditions, and it does not guarantee the result of any single scan. The [body-scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) sets out the validation figures, the tested population, and the methodology.

> **[Illustration 2: Accuracy, repeatability, and capture quality]**
> Designer brief: an evidence panel with three columns, covering accuracy against a reference method, repeatability across comparable scans, and capture-quality controls before processing. The panel carries definitions and no figures.

### What happens if a user cannot complete a valid scan?

The next step depends on the exception route that the program defines. FitXpress provides corrective prompts and retakes inside the capture flow, and the route beyond that is a program design decision.

An exception route can include:

- Corrective instructions and retakes inside the capture flow.
- A defined support route, such as help from program staff.
- Accessibility considerations, planned before launch.
- An assisted or alternative capture path, where appropriate.
- An alternative workflow for users who cannot or prefer not to scan.

Accessibility planning matters most for users whose mobility or health makes the standing capture positions difficult. For those users, a documented alternative measurement path gives them a way to continue. Remote scanning is one way to take part in a program, and users who do not scan need a route that keeps them in it.

### Can users complete a scan alone at home?

Yes, in a supported self-scan flow. The flow guides the user through both photos without a technician or a dedicated scanner, and a standard smartphone is the only hardware involved.

The phone stands vertically on a flat surface, such as a table or counter. <!-- claim: FX-CQ-007 --> With the phone in place, the user stands in the front and side positions while on-screen feedback guides positioning in real time. <!-- claim: FX-CQ-002 --> Users should follow the on-screen guidance for lighting, distance, framing, and phone placement. <!-- claim: FX-CQ-007 -->

In a body scan app built on FitXpress, completion depends on the person and the setting. Mobility, available space, smartphone access, and the ability to follow the positioning instructions all affect whether a user finishes the scan. Privacy at home matters too, because the user needs a space where standing for photos in form-fitting clothing is acceptable.

Some users and some homes are not suited to self-scanning. Those users need the assisted or alternative path that the program defines for failed scans.

## Workflow integration, timing, and outputs

### Can FitXpress be integrated into a telehealth or clinical workflow?

Yes. The organization embeds the guided capture step in its own product, and the structured outputs return to its workflow for review. <!-- claim: FXS-DELIVERY -->

A typical sequence has six steps:

1. The customer places the guided capture step in its app or web experience.
2. The user completes front and side capture.
3. The customer's backend submits the required data to the FitXpress API.
4. FitXpress processes the scan and returns structured outputs.
5. The customer stores, displays, or routes the outputs according to its workflow.
6. The care team or another authorized professional reviews the information.

Integration runs through web and mobile SDKs, including supported iOS and Android integrations, and through a server-to-server API that connects the organization's backend. <!-- claim: FX-R1-SDK --> The optional FitXpress Admin Panel complements that integration as an interface for monitoring and exporting results. <!-- claim: FX-R1-ADMIN -->

Capture and results can sit inside the organization's own interface, such as a telehealth or body measurement app. The organization controls which outputs appear in its interface and how they are routed for review. Deployment options for telehealth programs are described on [FitXpress for telehealth and digital health](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/).

FitXpress supports clinician or care-team review, which means clinical assessment, treatment, and eligibility decisions stay with the customer's clinicians or other designated decision-makers. <!-- claim: FXS-SCOPE --> Where a protocol requires a reference method, that method stays in place. FitXpress is not a medical device. <!-- claim: FXS-MEDICAL -->

Storage, retention, and regulatory questions are answered in the [FitXpress data, privacy, security, and regulatory FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/).

### How long do capture and processing take?

FitXpress returns structured results in under 45 seconds from the two photos. <!-- claim: FXS-SPEED --> Everything before that point depends on the implementation and on the user.

The flow has three stages:

- **Onboarding and preparation.** The organization's own onboarding screens determine the length of this stage.
- **Photo capture.** Capture time depends on how quickly the user follows the positioning prompts and whether a retake is needed.
- **From photos to results.** This is the stage that the under-45-second figure describes.

Total time from the first screen to results is therefore determined by the onboarding design and by each user's capture.

### Can users upload existing photos instead of completing the guided capture?

No. Users cannot upload existing photos in the standard guided FitXpress capture flow. <!-- claim: FX-R1-UPLOAD -->

The system needs front and side photos taken under defined conditions, and RTPV and the Clothing Detector operate during that supported flow. <!-- claim: FX-CQ-002 --> A photo from the camera roll never passed through those checks, which means it does not carry the same controlled capture record. Camera position and capture context also contribute to consistency between scans, which matters when a program compares a follow-up scan with a baseline.

### What progress outputs are available after a successful scan?

Depending on the selected configuration, a successful scan can return the following outputs. <!-- claim: FXS-OUTPUTS -->

- 80+ body measurements.
- Calculated metrics such as BMI and basal metabolic rate (BMR), where the required inputs are provided. Height is submitted with the scan; weight is optional. <!-- claim: FXS-LIFECYCLE -->
- Body-composition estimates: body fat percentage, fat mass, and lean mass.
- A 3D body model.
- Body Progress comparisons between two scans that the customer selects, matched by scan ID.

The customer decides whether and how progress tracking is enabled. Scan records carry randomly generated IDs, and 3DLOOK cannot identify a specific individual from them. <!-- claim: FXS-IDS --> How programs present results over time is covered in [mobile body scanning and patient engagement](https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/).

## Next steps

A short pilot with the program's own users can measure completion, retakes, and support requests under its onboarding and its exception route.

Ready to evaluate guided remote body-data capture for your product? [Book a demo](https://3dlook.ai/book-a-demo/) to review the FitXpress capture flow, integration options, and data-quality controls with the 3DLOOK team.
