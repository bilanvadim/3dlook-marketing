---
slug: 2026-09-21-ai-body-scanning-telehealth-documentation
product: fitxpress
status: edited
round: Review 1 (EDIT round)
base_text: v1/final.md
decisions: review-1-decisions.md
title: "How AI Body Scanning Supports More Consistent Telehealth Documentation"
author: Assel Sekerova
primary_keyword: telehealth documentation
hub: AI in Telehealth (Hub 2)
cluster: Documentation
intent: BOFU
word_count: 2181
word_count_note: "prose words per article_lint.py; Review 1 target about 2,150-2,300 (v1 1,867; plan target 2,100, band 1785-2415)"
editing_passes: 5
ai_density_before: 0.0
ai_density_after: 0.0
claims_verified: [FX-001, FX-002, FX-003, FX-004, FX-005, FX-006, FX-007, FX-008, FX-009, FX-011, FX-012, FX-013, FX-014, FX-015, FX-016]
changes_summary: |
  Review 1 round. review-1-decisions.md applied item by item to v1/final.md; text outside the
  items is unchanged (S3, scope note, intro, "At intake", "Before clinician review", S7 paragraphs
  1 and 3, "Who this fits", FAQ 1-3, Related reading are byte-identical to v1).
  - A: H1 replaced verbatim; title field added with the same text. Byline and slug unchanged.
  - B: reviewer's early-link sentence added as its own paragraph after the scope note (early CTA
    and landing-map rule 1 down link, at 9.3% of the body). Gate M1 failed on "API/SDK" there, so
    per B's fallback the terms are expanded at this first use: "application programming interface
    and software development kit (API/SDK) integration". No other word changed. S5 now uses API
    and SDK bare.
  - C: "What the scan generates" now lists 80+ body measurements, a 3D model, applicable BMI- and
    weight-related metrics, body composition estimates, and Body Progress comparisons between two
    scans the program selects. The technical-data bullet keeps the compliance.md list and adds one
    sentence: not every technical field appears in every API response, in the Admin Panel, or in
    the program's record system. BMR expansion and the body-fat / lean-mass / fat-mass examples
    moved from the bullet into the distinction paragraph. "in under 45 seconds" unchanged.
  - D: S4 lead names what the program controls (scan scheduling, integration, which patient a scan
    belongs to, documentation requirements, clinical review). "Between visits": Body Progress by
    scan IDs; FitXpress keeps no patient timeline; 3DLOOK does not determine whether two scans
    belong to the same person. One negation per sentence.
  - E: S5 rewritten: two-sentence lead (complementary capabilities, API/SDK primary, the
    retrievable timestamped record said once), H3 "API/SDK integration" (capture in the program's
    app, outputs via API/SDK, customer maps results; EHR connection is the customer's integration
    work; landing link with the map anchor "body scanning API for telehealth platforms"), H3
    "FitXpress Admin Panel for scan management" (canon line, not a replacement for API/SDK or an
    EHR, seven FX-013 bullets, FX-014 availability, launch-post link). No client tab names, no
    Clothes Detector.
  - F: H2 renamed verbatim; structured column rewritten verbatim; "quicker to read" removed; the
    two reading paragraphs merged into one (the re-entry and comparability sentences restated
    table rows); hedge and recalculation sentence kept.
  - G: "FitXpress is not a clinical diagnostic tool." added to paragraph 2; new closing paragraph:
    using FitXpress does not by itself make a workflow compliant with HIPAA, GDPR or telehealth
    documentation rules, and compliance stays with the program and its legal advisors. HIPAA and
    GDPR are expanded here, their first use now.
  - H: S8 opens with the photo sentence ("within 30 days"); output retention now reads "unless the
    customer agreement says otherwise or a deletion request applies"; HIPAA sentence loses its
    expansion (moved to S7); GDPR sentence is now the canonical verbatim form ending "under GDPR."
  - I: five measures kept; "Each of those is something the program measures..." and "Baselines
    taken before launch..." cut (now steps 4 and 1); five-step numbered framework added in the
    decision's order; FX-012 limitation kept.
  - J (Vadim 2026-11-23: "як Аселя хоче"): closing CTA links the pricing demo deep link (#bd-modal-personalized), anchor "book a demo of FitXpress for
    telehealth intake". The landing links stay at ~9% (early) and ~42% (E1). No other promotional text.
  - K: FAQ 4 opens with the protocol condition and the Body Progress / scan ID sentence; the
    dataset, below-1-cm and framework-link sentences are unchanged. FAQ 5 added verbatim.
  - L, M: no new AI mentions, no client count, no roadmap features; all seven required URLs present,
    anchors distinct (Admin Panel anchor reworded to "Admin Panel launch announcement").
  - QC fix pass (2026-11-23, QC review 1 fixes 1-6, 8, 9 per coordinator_review; fix 7 is the
    coordinator's, no external source added): S6 reading paragraph rehedged once ("How much less of
    the record needs rebuilding ... depends on how much was missing before"), correction sentence
    kept and moved to the end as "Corrections to an entry are made in the program's record system.";
    S7 "FitXpress is not a clinical diagnostic tool." now opens its paragraph; compliance sentence
    reads "The program and its legal advisors remain responsible for compliance."; E1 names the
    program as integration owner (map + EHR sentences) and the landing link reads "The page on the
    FitXpress [...]"; "Between visits" says the program links each scan ID to its own patient record
    (FX-016 marker on the sentence); pilot bridge states why the baseline comes first; "Before
    clinician review" names the clinical team. "stay(s) with" now 3 (all v1). FAQ 5, "customer's API
    keys" and "selected FitXpress clients" unchanged. Gates after: lint PASS (mean 12.9, p90 20,
    over_25 2 of 146, over_35 0), detector CLEAN 0.0, checklist 19/19.
self_check: |
  - Still machine-like after the first apply: the S6 reading under the table repeated two table
    rows in prose (re-entry "can fall where...", entries "stay comparable when..."), and both
    paragraphs ran on an "although" hedge. Merged into one four-sentence reading; the restatements
    are cut and one hedge remains.
  - Still machine-like: the G compliance sentences sat inside the decision paragraph, which read
    as an inventory of disclaimers. They now close S7 as their own paragraph, which also hands
    over to the data-handling section.
  - Still machine-like: "according to the customer agreement and the customer's instructions"
    (double "customer"), "five measures ... five steps", "the program's own" x6. Reworded; "the
    program's own" is down to 4 (two of them v1 text).
  - Residual, accepted: the B sentence runs 33 words after the M1 expansion, and the G compliance
    sentence runs 29 words because of the two expansions. Both are within the gate (2 of 146 over
    25, none over 35). "API/SDK integration" appears 3 times in prose; B, the S5 lead and the canon
    line each require it.
  - sentence length gate after edits: mean_words 12.8, p90 20, over_25 = 2 (1.4%), over_35 = 0;
    near_duplicate_pairs none. Detector CLEAN, density 0.0, rhythm 0.46.
---

# How AI Body Scanning Supports More Consistent Telehealth Documentation

By Assel Sekerova

## Where telehealth documentation loses consistency

A telehealth record usually collects body data from three places. The person reports a weight at sign-up, a home scale reports a different one later, and a progress photo arrives in a message thread. Each input lands in its own format, on its own day.

Consistency is decided at capture. What a program collects at intake sets what it can retrieve and compare later.

Self-reported weight and height are hard to verify at intake. Staff re-enter values and chase missing fields before a consultation can start. That work sits with the clinical team, and it grows with volume.

The cost shows up later. A care coordinator opens a record before a check-in and finds four entries in three formats. A program lead builds an outcomes summary for a payer partner, and two of the time points have no usable entry at all.

***Scope note.*** *FitXpress provides remote body-measurement capture and structured records. The program's own systems hold the rest of the chart. Clinical review, treatment decisions, and eligibility decisions stay with the program's clinicians. FitXpress is not a medical device.*

For telehealth teams standardizing remote intake, [FitXpress supports structured body-data collection and repeat measurement](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/) through a guided smartphone capture flow, application programming interface and software development kit (API/SDK) integration, and optional scan-management tools. <!-- claim: FX-001 --> <!-- claim: FX-006 -->

## Short answer: what a structured body-data record contains

A guided two-photo scan returns structured outputs in under 45 seconds. <!-- claim: FX-004 --> The entry it produces carries three groups of data.

- **What the person submits.** Front and side photos, gender, height, and optionally weight. <!-- claim: FX-002 -->
- **What the scan generates.** 80+ body measurements, a 3D model, applicable BMI- and weight-related metrics, body composition estimates, and Body Progress comparisons between two scans the program selects. <!-- claim: FX-002 --> <!-- claim: FX-005 --> <!-- claim: FX-016 -->
- **What the system records technically.** Capture-quality and pose-validation flags, clothing classification, face-obfuscation confirmation, and processing logs with timestamps and request metadata. Not every technical field appears in every API response, in the Admin Panel, or in the program's record system. <!-- claim: FX-002 -->

Body measurements are circumferences, lengths, and widths. BMI and basal metabolic rate (BMR) are calculated from the inputs. Body fat percentage, lean mass, and fat mass are body composition estimates. The distinction matters when a program decides which fields it stores and which ones it compares over time.

## Why record consistency is under pressure now

Remote-first programs grew faster than their intake did. Consultation capacity moved online early, and the record-keeping around it often stayed manual.

Programs are also asked to show their work. Payers, employers, and regulators expect outcomes traceable to a dated, consistent entry. A summary built from mixed inputs is harder to defend than one built from entries that share a format.

Documentation expectations for telehealth keep being revised. Each revision lands on the same operational question: which fields the program captures, and whether it can retrieve them later.

AI reached documentation work first through note-taking tools that draft the visit summary. Body data is a separate input to the same record. It arrives before the consultation, and it describes the body while the note describes the conversation.

## Where body data enters a telehealth workflow

Body data reaches a telehealth program at three points. The workflow around each one decides how much of it lands in the record in usable form. The program controls that workflow: scan scheduling, the integration, which patient a scan belongs to, documentation requirements, and clinical review. <!-- claim: FX-016 --> [AI in telehealth](https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/) covers the wider picture of remote-care workflows, privacy, and patient experience.

### At intake

Remote capture runs before the first consultation. The person completes a guided two-photo scan on a smartphone, and the record exists before anyone opens it for review. <!-- claim: FX-006 --> Programs that verify BMI as part of eligibility follow a separate path, covered in the guide to [remote BMI verification for online pharmacies](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/).

### Between visits

Repeat capture happens at intervals the program chooses. Each capture produces an entry in the same format, with its own timestamp. Body Progress compares two scans the program selects, using their scan IDs. <!-- claim: FX-016 --> FitXpress does not keep a patient timeline; the program links each scan ID to its own patient record. <!-- claim: FX-016 --> 3DLOOK does not determine whether two scans belong to the same person. <!-- claim: FX-016 -->

### Before clinician review

The clinical team retrieves the record in one place ahead of the consultation. Missing or low-quality captures become visible earlier, while there is still time to repeat them. Testing, physical examination, and clinical judgment stay with the provider. <!-- claim: FX-006 -->

Documentation of a telehealth physical exam still rests on what the provider observes and writes during the visit. Remote capture changes when the measurement data arrives, and what shape it arrives in. Telehealth visit documentation requirements are set by the program and its advisors, and remote capture supplies input to them.

## Where FitXpress fits: capture, records, and the Admin Panel

[FitXpress](https://3dlook.ai/) delivers results through two capabilities that work together, and either one leaves a timestamped record the program can retrieve months after capture. <!-- claim: FX-001 --> <!-- claim: FX-003 --> API/SDK integration is the primary route, and the Admin Panel serves teams that do not want to build a dashboard of their own. <!-- claim: FX-001 -->

### API/SDK integration

The person completes a guided scan inside the program's own application. <!-- claim: FX-001 --> Structured outputs come back through the FitXpress API or SDK. The program decides how those results map into its own record systems. Connecting them to an electronic health record (EHR), or updating a medical record, is the program's integration work. <!-- claim: FX-016 --> The page on the FitXpress [body scanning API for telehealth platforms](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/) describes what an integration covers.

### FitXpress Admin Panel for scan management

The FitXpress Admin Panel is an optional, complementary interface for monitoring and exporting results. It does not replace API/SDK integration or an EHR. <!-- claim: FX-001 --> The first version, described in the [Admin Panel launch announcement](https://3dlook.ai/content-hub/fitxpress-admin-panel-launch/), includes:

- Centralized access to scans made with the customer's API keys.
- Scans separated by API-key environment, such as primary and sandbox keys.
- Scan statuses: Success, Failed, and Pending.
- Sorting and filtering of scan records.
- Individual scan details, including measurement information.
- Export of selected records as a comma-separated values (CSV) file.
- API key, scan allowance, and subscription details. <!-- claim: FX-013 -->

That first version is available to selected FitXpress clients. The 3DLOOK team provides client credentials directly, and there is no public sign-up. <!-- claim: FX-014 -->

## Fragmented inputs and structured records, side by side

What changes is the shape of the entry. Who reviews it, and who decides, stays the same.

| **What the record carries** | **Fragmented intake inputs** | **Structured body-data record** |
|---|---|---|
| Fields on each entry | Vary with the source and the visit | Consistent fields when scans use the same successful capture configuration |
| Timestamp | Depends on when someone logged the item | A timestamp associated with each scan record |
| Format | Free text, images, and scale readings | Structured outputs in one shape |
| Availability before review | Assembled during or just before the consultation | Available once the scan completes and the program's integration or retrieval brings it into the record |
| Manual re-entry | Often needed to move values into the system | Can be reduced where the integration transfers the required fields |
| Comparison across time points | Limited by differing formats | Possible between records the program selects, under a consistent capture protocol |

Consistent fields make records easier to compare across time points. <!-- claim: FX-002 --> How much less of the record needs rebuilding inside the consultation depends on how much was missing before. Calculated metrics and body composition estimates are recalculated on each scan, and each entry shows the figures from that day. <!-- claim: FX-005 --> Corrections to an entry are made in the program's record system.

## What FitXpress does not do

FitXpress supports remote intake and body-measurement capture, body composition outputs, and comparison of the scans a program selects. It also covers structured data collection for research protocols, and documentation that supports workflows the customer manages. <!-- claim: FX-006 -->

FitXpress is not a clinical diagnostic tool. It does not independently determine a diagnosis, a treatment or medication recommendation, insurance or clinical-trial eligibility, employment eligibility, or any other high-impact individual decision. <!-- claim: FX-006 --> Final decisions stay with the program's clinicians, underwriters, and other designated decision-makers. <!-- claim: FX-006 -->

Remote capture does not replace clinician review, dual-energy X-ray absorptiometry (DXA), bioelectrical impedance analysis (BIA), or calibrated scales. Those methods answer different questions under different conditions. Where a program needs a reference-method measurement, remote capture sits alongside it. FitXpress is not a medical device.

Using FitXpress does not by itself make a workflow compliant with the Health Insurance Portability and Accountability Act (HIPAA), the General Data Protection Regulation (GDPR), or telehealth documentation rules. The program and its legal advisors remain responsible for compliance.

## Data handling, retention, and access

Photos are deleted immediately after processing or within 30 days, depending on the customer agreement and instructions. <!-- claim: FX-015 --> Measurements, body composition data, and 3D models are retained on an ongoing basis unless the customer agreement says otherwise or a deletion request applies. <!-- claim: FX-003 --> Deletion is by scan identifier, on the customer's request. <!-- claim: FX-003 --> Scan records are associated with anonymized, randomly generated identifiers, and 3DLOOK cannot identify a specific individual from stored scan records. <!-- claim: FX-009 -->

FitXpress can support deployments governed by HIPAA. In those deployments 3DLOOK acts as a business associate under an executed Business Associate Agreement (BAA), where applicable. <!-- claim: FX-007 --> In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR. <!-- claim: FX-008 -->

Procurement and security reviews of secure telehealth documentation platforms go further than retention and legal roles. The [FitXpress data, privacy, security, and regulatory FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) answers the rest, including storage regions, photo handling, and model training.

## How to evaluate documentation consistency in a pilot

A capture change earns its place where the existing gap is in intake. If records are already complete and comparable, moving the capture step will not return much.

Five measures describe the record before and during a pilot:

- Completion rate of remote capture, by cohort.
- Share of records complete at the point of review.
- How often a value is re-entered manually.
- How often the manual fallback path is used.
- How many entries are comparable across time points.

None of them is a result to expect in advance, which is why the baseline comes first. The pilot follows this order:

1. Establish baseline performance.
2. Define the pilot cohort and capture protocol.
3. Configure result retrieval and documentation handling.
4. Measure outcomes within the program's own systems.
5. Compare against the baseline and evaluate operational fit.

One limit belongs in the pilot design from the start. FitXpress was not specifically trained on data representing people with physical disabilities, and its measurement performance has not been established for this population. <!-- claim: FX-012 --> This matters when a disability affects the standard standing pose or capture sequence.

### Who this fits

Remote-first programs running repeat check-ins across more than one site or partner. The roles that usually own the decision are Head of Clinical Operations, Care Coordination Manager, and Medical Director. A single-site program with low volume and a complete paper trail has less to gain.

## FAQ

### Can body scan records help a telehealth program meet its documentation requirements?

The program and its advisors decide which documentation requirements for telehealth apply and how records are used. FitXpress provides structured, timestamped records that enter the program's own process. It does not guarantee compliance or certify a program's records.

### How is this different from AI tools that draft telehealth visit notes?

Note-taking tools capture what was said during a consultation and turn it into a summary. FitXpress captures body-measurement data before the consultation and returns it as a structured record. Programs reviewing AI tools for telehealth visit documentation are usually solving a different part of the chart. The two inputs meet in the same record, from different points in the workflow.

### What happens when a patient cannot complete a remote scan?

Some people lack a suitable device or a stable connection. Others cannot hold the capture pose. The program, therefore, needs a documented manual alternative, and a rule for how a measurement taken that way joins the record. <!-- claim: FX-006 -->

### Do repeat scans produce comparable entries over time?

Comparability depends on a consistent capture protocol and on the receiving system. Each Body Progress comparison uses two entries the program picks by scan ID. <!-- claim: FX-016 --> Internal repeatability testing used a real-world customer dataset with five scans per participant. For most of the evaluated measurements, typical scan-to-scan differences remained below 1 cm. <!-- claim: FX-011 --> The [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) describes the test conditions and separates repeatability from accuracy.

### Does FitXpress replace a telehealth platform's existing medical record system?

No. FitXpress provides remote body-data capture and structured scan outputs through supported integration interfaces. The customer determines how these results are stored, displayed, associated with patients, and incorporated into its existing documentation workflows. The optional Admin Panel supports scan-data management but is not a replacement for an electronic health record system. <!-- claim: FX-001 --> <!-- claim: FX-016 -->

## Next steps

Compare the inputs the program collects today against what the record has to carry at review, and name the fields that arrive inconsistently. Then [book a demo of FitXpress for telehealth intake](https://3dlook.ai/pricing/#bd-modal-personalized).

Related reading:

- [AI in telehealth: workflows, privacy, patient experience, and remote body data use cases](https://3dlook.ai/content-hub/the-potential-of-ai-in-telehealth/)
- [How mobile body scanning improves patient engagement](https://3dlook.ai/content-hub/mobile-body-scanning-patient-engagement/)
