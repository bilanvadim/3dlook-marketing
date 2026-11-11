# Product roadmap and feature status (claims gate)

Source: the company's Q3 2026 quarterly update (internal, read 2026-11-11). The full digest with
numbers and accounts is in the private repo (`3dlook-marketing-private/board/2026-q3/`). This file
lists only feature status and how to write about each feature.

**Rule:** copy describes as available only what is in the "Live" column. Anything "ready for
release", "in testing" or "planned" is either left out or phrased as coming ("is being added",
"in development"), never in the present tense as a capability. When a status changes, update
this file in the same commit as the copy that uses it.

## Feature status as of 2026-10-21

| Area | Feature | Status | How to write about it |
|---|---|---|---|
| FitXpress | Admin panel: photo-deletion date, failed-scan messages | Live | OK as a capability |
| FitXpress | Anti-fraud live human validation (iOS/Android SDK) | Ready for release, not live | Not as a live capability. "Coming soon" is backed (this reverses item 4 of the BMI-page review of 2026-11-09, which asked to remove the "Prompted-action liveness, Coming soon" card). Event visuals = "coming" |
| FitXpress | Anti-fraud ratio validation | Planned Q4 2026 | Don't claim |
| FitXpress | Clothing Detector / clothes detection in the API | Retrain + API planned Q4 2026. Vadim 11-11: live by the conference | Keep the 2026-10-07 safer wording from `tech-spec.md` until release is confirmed; no payload flags, classes or "prompts the user" |
| FitXpress | Android SDK on devices without a gyroscope | Planned Q4 2026 | Don't promise "any Android device" beyond the current wording |
| FitXpress | Weight-prediction accuracy baseline | Q4 2026 (R&D) | No weight-accuracy numbers until R&D publishes the baseline (see `accuracy-formulations.md`) |
| FitXpress | Body-composition validation vs a reference device (EU research lab, 100+ people) | Lab opening; first report Dec 2026 | Lab story needs the CEO's OK; no fat % until the report |
| FitXpress | Clinical validation study | Not started | Don't mention as running |
| FitXpress | Height verification, DEXA reference data | Moved to 2027 | Don't claim or imply |
| MT + FX | Real-Time Pose Validation (RTPV) | Live | Approved wording in `tech-spec.md` |
| MT + FX | RTPV 2.0 (new flow) | Internal testing | Don't name "2.0" publicly |
| MT + FX | Real-time voice guidance during capture | Web ready; iOS/Android in testing | OK for web flows; for native apps write "coming" |
| MT + FX | Localization versioning, updated measurement guides | Planned Q4 2026 | Don't claim |
| Mobile Tailor | Widget redesign, pre-populated widget fields, "Scan now" in admin | Live | OK |
| Mobile Tailor | Welcome-screen customization, logo in emails | Ready for release, not live | Don't claim yet |
| Mobile Tailor | Widget localization (languages) | Planned Q4 2026 | Don't claim multi-language widget |
| Mobile Tailor | Data-deletion settings | Planned Q4 2026 | Don't claim |
| Wrist | Wrist measurement as a separate product | Final stage of development; anchor client live since Sep 2026 | Approved homepage wording (SDK, under 10 s; 2026-10-22) stands. No accuracy figures publicly |
| Wrist | Public wrist API + SDK with docs; web demo for Sales | Planned Q4 2026 | No "public docs" or "self-serve" until release |
| Fingers (ring sizing) | Data collection (100 people) → POC | Research, Q4 2026 – Q1 2027 | Not a product. No public claims; outbound to ring buyers only per approved hypothesis |
| Head | Data audit, demand check, accuracy test → product or feature decision | Research | Not a product. No public claims |
| Company | SOC 2 | Readiness for an audit is a goal | Unchanged: "working toward a SOC 2 Attestation Report; not certified" (`compliance.md`) |

## Company priorities Q4 2026 – Q1 2027 (for content planning)

- **Wrist:** product demo and SDK for customers; first customer beyond the anchor client (pilots).
- **Fingers:** prove ring sizing works (POC); talk to smart-ring and jewelry buyers.
- **Head:** decide product vs feature after an accuracy test; first demand checks in protective headwear.
- **FitXpress:** EU research lab, body-composition baseline vs a reference device, then an external validation partner; weight accuracy.
- **Core body tech:** body accuracy update to production.
- **Company:** data rights documentation; SOC 2 audit readiness.

Quarterly strategist: "особые точки" for the social plan = release dates of the items above once
product confirms them, plus the December lab report. No dates on this list are public commitments.
