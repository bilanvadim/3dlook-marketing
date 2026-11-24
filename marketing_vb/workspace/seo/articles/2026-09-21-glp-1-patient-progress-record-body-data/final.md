---
slug: 2026-09-21-glp-1-patient-progress-record-body-data
product: fitxpress
section: full
status: edited
author: Assel Sekerova
primary_keyword: glp-1 patient progress record
hub: GLP-1 Market & Progress Tracking (Hub 3)
cluster: Documentation
intent: BOFU
target_words: 2100
word_count: 2230
editing_passes: 5
edit_round: Review 1 (Asselya Sekerova, 2026-11-24), applied per review-1-decisions.md
ai_density_before: 0.0
ai_density_after: 0.0
gate_m1_note: gate 8 fails on GLP-1 in the H1, the known title case; expanded at first prose use, title unchanged per plan
claims_verified: [FXS-LIFECYCLE, FXS-OUTPUTS, FXS-SPEED, FXS-REPEAT, FXS-DELIVERY, FXS-SCOPE, FXS-MEDICAL, FXS-RETENTION, FXS-IDS, FXS-HIPAA, FXS-GDPR, FXS-POPULATION, FXS-RECORD-STATUS, FXS-RTPV, FXS-PHOTOS, FXS-MUSCLE-FIELDS, FXS-MUSCLE-LIMITS]
external_sources_used: [EXT-NEELAND]
changes_summary: |
  Review 1 edit round. Base: v1/final.md (1,988 prose words). Result: 2,207 prose words,
  then 2,230 after the QC fix pass (last entry).
  - R1-1 (applied, verbatim): the five replacements as given (Short answer third bullet and
    closing line, audit item 3, first sentence of the last "Where FitXpress fits" paragraph,
    Next steps second sentence). The capture log H3 rewritten in the fixed order: processing
    status and the known gap; timestamps and the scan identifier; the program's own log of
    capture instructions and manual fallback; the RTPV sentence once, verbatim, with its
    FXS-RTPV marker; the first-entry sentence unchanged. Coordinator addition applied in
    "What FitXpress does not do" ("what happened to each capture").
  - R1-1, one wording choice: the program-log sentence opens "What the program logs about
    capture instructions and manual fallback" where the decision's outline said "The
    program's own note on". The gate counted "program's own" three times (delivery paragraph,
    closing CTA, this sentence); "logs" also ties it to the bullet's "The program adds what it
    controls". Claim and position unchanged.
  - R1-1, marker deviation: the decision says keep FXS-DELIVERY on the delivery sentence, but
    v1 carried FXS-LIFECYCLE there. The sentence now carries FXS-DELIVERY and
    FXS-RECORD-STATUS, which is what the decision intends; FXS-LIFECYCLE no longer supports it
    because the pack note excludes its technical-data list from the record.
  - R1-1, frontmatter: the gate_m1_note value now says "fails on" so the R1-1 grep does not
    hit the frontmatter. Field kept.
  - R1-2 (applied, verbatim): early CTA as its own paragraph after the Short answer closing
    line, link inside the sentence, no action-label line, no client count. Landing links sit
    at 19.8%, 57.1% and 97.5% of body words (cta_placement ok). "Where FitXpress fits" anchor
    and the closing CTA replaced as given. The old demo-modal link is gone; no contact-page link was added.
  - R1-3 (applied, verbatim): first bullet replaced; FXS-PHOTOS added, FXS-LIFECYCLE kept. The
    "Photos are the input to the capture" sentence in the H3 kept in this round (the gate did
    not pair it with the bullet); varied in the QC fix pass, see Q5.
  - R1-4 (applied with change): new H2 between the capture log and Cadence, heading verbatim,
    EXT-NEELAND sentences attributed to the review, no figures. Two edits to the starting
    text: "These figures support clinician review." moved from the start of paragraph 2 to the
    end of paragraph 1 (it is the last sentence of FXS-MUSCLE-FIELDS, claim order unchanged,
    and it no longer sits against "A 2024 review"); serial commas added in the section's lists
    per editorial-rewrites.md section 6. M1 follow-on applied verbatim: FAQ H3 and answer use
    DXA and BIA; both are expanded once, in the new H2.
  - R1-4, one cut outside the touched sentences: "An entry that carries them sits next to a
    weight figure in the file." removed from "The generated fields", because the new H2 now
    states the same point ("next to the weight figure"). No other v1 sentence changed.
  - R1-5, R1-6 (applied, verbatim). The NDA line carries an FXS-REPEAT marker; "Internal" and
    the framework link stay in the same paragraph; no percentage there.
  - R1-7 (applied, verbatim). Transition: v1's "The decision itself stays with the clinical
    team." lost "itself", which the new next sentence also uses.
  - R1-8 (applied with change, as decided): only the deletion-by-identifier sentence cut;
    HIPAA and GDPR expansion sentence, both canon sentences and the FAQ link kept.
  - R1-1 grep: two hits. The RTPV sentence, and the FXS-POPULATION disability limitation in the
    FAQ, whose canon wording names the person's standing position. That sentence is verbatim
    canon on the do-not-change list and says nothing about the record. Kept. The coordinator
    amended the check to allow it (QC Q3); the publisher lists it in Open items.
  - QC fix pass (2026-11-24, QC 16/20, review-1-decisions.md "QC fix pass" section):
    Q1 verbatim: "A program answers it from fields the record already carries." became "The
    record already carries the fields a program reviews for that question." (the old sentence
    said more than the limits paragraph allows).
    Q2 verbatim: both Neeland sentences replaced with the reworded pair ("describes lean mass
    as a measure that includes organs, bone, and fluids as well as muscle" / "By that account,
    a change in lean mass may not reflect a change in muscle."); the old pair near-copied the
    live sibling and called the measure "Its definition".
    Q4: bridge added before the RTPV sentence, "The guidance given while the photos are taken
    is part of that protocol." It ties RTPV to "the same protocol" as capture-time guidance;
    the RTPV sentence is unchanged and no logged-field reading is left.
    Q5: in "The submitted fields", "Photos are the input to the capture." became "The capture
    works from the two photos." (the bullet keeps the reviewer's words), and the paragraph now
    carries an FXS-PHOTOS marker. In "The generated fields", "Composition estimates describe
    what the change is made of." became "Composition estimates split body weight into fat and
    lean components.", which leaves the "made of" framing to the new H2 only.
    Q3 and Q6 belong to the publisher. Gates after the pass: see self_check.
self_check: |
  - Still machine-like after the paste-in: the new H2's first paragraph was a run of
    same-shaped field sentences, and paragraph 2 opened "clinician review. A 2024 review".
    Moving the boundary sentence to close paragraph 1 gave the inventory a short last beat and
    separated the two uses of "review".
  - Still machine-like: "program's own" became a refrain (x3) once the capture log was
    rewritten. The capture-log sentence now leads with what the program logs.
  - Still machine-like: the new H2 and "The generated fields" both put composition next to the
    weight figure; the v1 sentence went. "lean mass and fat mass" still appears three times
    (output list, H3, new H2); it is the field name, kept.
  - Still machine-like: "itself" twice in the BMI FAQ answer; v1's dropped.
  - QC fix pass: the two leftovers above are resolved (the H3 photo sentence varied, the "made
    of" echo removed from "The generated fields"). Still slightly machine-like: "question" sits
    in the new H2 heading and in its first two sentences; the second is Q1 verbatim and points
    back to the first, so it stays.
  - sentence length gate after edits (and again after the QC fix pass, 2,230 words): mean_words
    13.1, p90 20, over_25 = 0 (0.0%), over_35 = 0;
    near_duplicate_pairs none; repeated_phrases "for glp 1" x4 (fixed anchors and related
    reading), "scan to scan" x3, "lean mass and fat mass" x3. Detector CLEAN, ai_density 0.0.
---

# What Body Data Should Be Included in a GLP-1 Patient Progress Record?

By Assel Sekerova

## Where a GLP-1 progress record can lose its shape

A glucagon-like peptide-1 (GLP-1) patient file at month four holds whatever each check-in left behind. One entry has a weight and a coach's note. The next has a weight, a waist measurement taken at the clinic, and two photos. The month after that, there is a message thread and nothing else.

Entries arrive from different places and in different formats. The set of fields changes from one month to the next.

Scale weight records that something changed. It does not record what changed, or where.

The question that settles a record's structure is which fields every entry has to carry. A GLP-1 patient progress record becomes readable as a series once that answer stops changing between check-ins.

The cost of an unstructured file arrives later. When a payer or employer partner asks what the program achieved, the record has to be reassembled after the fact. Someone reads back through message threads, scale exports, and photos taken at three different distances. The clinical team absorbs that work, and it grows with the number of members enrolled. Wider context on medication-supported weight-loss programs sits in the [GLP-1 market overview](https://3dlook.ai/content-hub/glp-1-market/).

***Scope note.*** *FitXpress provides remote body-measurement capture and structured records. Clinical review, treatment and dosing decisions, and eligibility decisions stay with the program's clinicians. FitXpress is not a medical device.* <!-- claim: FXS-MEDICAL -->

## Short answer: what belongs in a GLP-1 patient progress record

Every entry carries three groups of fields.

- **Submitted with the capture.** Front and side photos, gender, height, and an optional self-reported weight. <!-- claim: FXS-LIFECYCLE --> Gender, height and weight stay in the entry as their own fields. The photos are the input to the capture. <!-- claim: FXS-PHOTOS -->
- **Generated by the scan.** 80+ body measurements, which are circumferences, lengths, and widths. Body composition outputs cover BMI, basal metabolic rate (BMR), body fat percentage, lean mass, and fat mass. <!-- claim: FXS-OUTPUTS --> BMI and BMR are calculated metrics, and the composition figures are estimates. The entry also holds a 3D model and scan-to-scan comparison outputs. <!-- claim: FXS-LIFECYCLE -->
- **Logged about the capture.** Processing status, a timestamp and the scan identifier for each entry. <!-- claim: FXS-RECORD-STATUS --> The program adds what it controls: the version of the capture instructions and whether a manual fallback stood in for the scan. <!-- claim: FXS-RECORD-STATUS -->

Capture takes two photos, front and side, and runs under 45 seconds from the photos to structured results. <!-- claim: FXS-SPEED -->

The first two groups describe the patient. The third records what happened to the capture, which tells a coordinator whether the entry can be used.

Programs that want these fields delivered into their own patient record can review [body composition tracking for GLP-1 programs](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/) and book a FitXpress demo.

## Why each group of fields earns its place

### The submitted fields

Height and gender come from the patient, and the capture uses both to generate the rest. <!-- claim: FXS-LIFECYCLE --> The same photo set produces different figures when the stated height changes. Keeping both values in the entry records the basis the outputs were generated from.

An optional self-reported weight keeps its own field. It sits beside the generated figures in the entry, and a coordinator can see which number came from where.

The capture works from the two photos. The stored entry holds the outputs, and photo handling follows the deployment terms the program agreed. <!-- claim: FXS-PHOTOS -->

### The generated fields

Measurements record where the body changed. <!-- claim: FXS-OUTPUTS --> A weight figure on its own cannot answer a question about a specific body area.

Composition estimates split body weight into fat and lean components. Lean mass and fat mass are held as separate fields, and both are estimates. <!-- claim: FXS-OUTPUTS -->

A comparison output allows one entry to be read against an earlier one. <!-- claim: FXS-LIFECYCLE --> Without it, the file holds a series of unrelated snapshots.

Collecting 80+ measurements does not decide which of them a check-in reads. That stays a program decision, and a record that carries the full set leaves it open.

### The capture log

Processing status tells the team whether a scan produced results before anyone compares it. <!-- claim: FXS-RECORD-STATUS --> A failed scan then reads as a known gap in the timeline. Without the status, the same time point can read as a result.

Timestamps place each entry on the timeline. The scan identifier makes one entry retrievable months later, when a partner asks about a single time point. <!-- claim: FXS-RECORD-STATUS -->

What the program logs about capture instructions and manual fallback shows whether two entries were taken under the same protocol. The guidance given while the photos are taken is part of that protocol. During capture, Real-Time Pose Validation (RTPV) gives pose and framing guidance. <!-- claim: FXS-RTPV -->

The first entry sets the starting point for everything compared afterwards, and standardizing that first capture is its own piece of work.

## What programs measure when the question is muscle loss

Muscle loss during GLP-1 treatment is a question about what the weight change is made of. The record already carries the fields a program reviews for that question. Lean mass and fat mass estimates sit in every entry, next to the weight figure. Circumferences at the waist, hips, thighs, and upper arms show where the change happened. A scan-to-scan comparison places two entries the program selects side by side. These figures support clinician review. <!-- claim: FXS-MUSCLE-FIELDS -->

A 2024 review by [Neeland, Linge, and Birkenfeld](https://pubmed.ncbi.nlm.nih.gov/38937282/) describes lean mass as a measure that includes organs, bone, and fluids as well as muscle. By that account, a change in lean mass may not reflect a change in muscle. FitXpress does not assess muscle strength, muscle function, or sarcopenia. Where a protocol names dual-energy X-ray absorptiometry (DXA) or bioelectrical impedance analysis (BIA), that method stays in place. <!-- claim: FXS-MUSCLE-LIMITS --> The consumer-app side of the same question is covered in [GLP-1 muscle loss: what fitness apps can track beyond scale weight](https://3dlook.ai/content-hub/glp-1-muscle-loss-fitness-apps/).

## Cadence, and what keeps entries comparable

The program sets the interval. Many capture at intake and then at the check-ins the care plan already runs. Cadence is an operational choice, and the record inherits whatever that schedule produces.

What makes an interval useful is repetition. Each entry repeats the field set and the capture protocol of the one before it. An interval the program cannot sustain surfaces later as missing time points in a partner report. A monthly entry with three empty fields leaves the same hole, less visibly.

Comparability depends on two things the program controls. The capture protocol has to be the same each time, and the receiving system has to store the entry in the same structure. Where capture instructions change mid-program, entries from before and after the change are not directly comparable, even at a steady interval.

Repeatability is the reason two entries can be read against each other at all. Internal repeatability testing used a real-world customer dataset with five scans per participant. For most of the evaluated measurements, typical scan-to-scan differences remained below 1 cm. <!-- claim: FXS-REPEAT --> Detailed methodology is available under a non-disclosure agreement. <!-- claim: FXS-REPEAT --> The [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) describes the test conditions and separates repeatability from accuracy.

Small real changes between two check-ins survive into the record when the captures follow the same protocol. For GLP-1 progress tracking, the interval matters less than the consistency of what each entry carries.

The program also selects which scans are compared. FitXpress produces comparison outputs for the two entries the program picks, and that choice stays with the team. <!-- claim: FXS-LIFECYCLE -->

## Where FitXpress fits: capture and delivery

Results reach the program primarily through integration. An application programming interface (API) or software development kit (SDK) delivers them into the program's own product or interface. <!-- claim: FXS-DELIVERY --> That is where the progress record already lives, in the file a coordinator opens before a check-in.

The integration decides where each entry lands. The program's platform holds the record, and FitXpress supplies the body-data fields inside it. Programs evaluating that route can start from [remote progress tracking for GLP-1 clinics](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/).

The FitXpress Admin Panel is the second route, and it is optional. It gives teams that do not want to build their own dashboard a centralized view of scan results. <!-- claim: FXS-DELIVERY --> The [FitXpress Admin Panel launch post](https://3dlook.ai/content-hub/fitxpress-admin-panel-launch/) covers the records and the workflow it holds.

Either route delivers the entry in the same shape, structured and timestamped, with its processing status and scan identifier. <!-- claim: FXS-DELIVERY --> <!-- claim: FXS-RECORD-STATUS --> A scan captured at home before a check-in and a scan captured during onboarding produce the same entry structure. A coordinator can open the entry from March and the entry from June and find the same fields in both.

## What FitXpress does not do

FitXpress does not independently determine a diagnosis, a treatment or medication recommendation, insurance eligibility, clinical-trial eligibility, employment eligibility, or any other high-impact individual decision. <!-- claim: FXS-SCOPE --> Final decisions stay with the program's clinicians and other designated decision-makers. <!-- claim: FXS-SCOPE -->

The record carries no information about the medication itself. Its fields describe measured body change and what happened to each capture. Questions about dosing, response, and treatment plans belong with the care team.

FitXpress is not a medical device. <!-- claim: FXS-MEDICAL -->

What FitXpress supports is narrower. It covers remote intake and body-measurement capture, body composition outputs and Body Progress comparisons, and structured records for workflows the program manages. <!-- claim: FXS-SCOPE -->

## What happens to the record that is kept

Measurements, body composition data, and 3D models are retained on an ongoing basis unless the customer agreement says otherwise. <!-- claim: FXS-RETENTION --> Retention is what allows a later entry to be compared with an earlier one.

Scan records are associated with anonymized, randomly generated IDs, and 3DLOOK cannot identify a specific individual from stored scan records. <!-- claim: FXS-IDS -->

Two frameworks come up in most procurement reviews: the Health Insurance Portability and Accountability Act (HIPAA) and the General Data Protection Regulation (GDPR). FitXpress can support HIPAA-governed deployments where 3DLOOK acts as a business associate under an executed Business Associate Agreement (BAA), where applicable. <!-- claim: FXS-HIPAA --> In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR. <!-- claim: FXS-GDPR --> The [FitXpress privacy, security, and regulatory FAQ](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/) answers the photo-handling, storage, and documentation questions in full.

## How a program can check its own progress record

A program can audit the record it already has without new tooling. Five counts, taken over the entries of one quarter:

1. Does every entry carry the same fields?
2. Does every entry carry a timestamp?
3. How many entries returned a completed processing status?
4. How many entries can be compared with the one before them?
5. How often did a manual fallback stand in for a capture?

Each count comes from records the program already holds. The answers show where the record loses its shape. When one entry in five is missing a field, the capture step is where to look. A missing timestamp points at the integration.

The first reading is a baseline. The second one, a quarter later, is the one that shows whether anything moved.

### Who this fits

The check belongs to whoever answers for the record. That is usually a Head of Clinical Operations, a Care Coordination Manager, a Medical Director, or a Head of Outcomes. It pays off in GLP-1 programs that run repeat check-ins at more than one site or through a partner. In those programs, several people write into the same file. A program with one site and one person entering data has a smaller gap to close. The field set still decides what a partner report can show.

## FAQ

### How is a body-data progress record different from GLP-1 lab monitoring?

Lab monitoring answers clinical questions through bloodwork that the care team orders and reads. A body-data record documents measured body change over time: measurements, body composition estimates, and timestamps. The two sit in the same patient file and answer different questions. FitXpress produces the measurement side of that file and says nothing about labs, dosing, or medication response.

### What belongs in the record when a patient cannot complete a scan?

FitXpress was not specifically trained on data representing people with physical disabilities, and its measurement performance has not been established for this population. <!-- claim: FXS-POPULATION --> This matters when a disability affects the standard standing pose or capture sequence. In those cases, the program needs a documented alternative measurement path. <!-- claim: FXS-POPULATION --> The time point is then a known gap in the scan series. The value from that alternative path is held wherever the program keeps its own records.

### Can this record confirm eligibility for a GLP-1 program?

Not on its own. FitXpress provides structured intake and supporting documentation for eligibility workflows the customer manages, and it does not independently determine eligibility. <!-- claim: FXS-SCOPE --> The decision stays with the clinical team. For the verification step itself, see [remote BMI verification](https://3dlook.ai/for-bmi-verification/). Online pharmacies can read the [online pharmacy BMI verification guide](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/).

### Does a body-data record replace a calibrated scale or a DXA scan?

No. It supports remote capture between clinical assessment points. A DXA scan, BIA, and a calibrated scale each measure under controlled conditions that a remote capture does not reproduce. Where a workflow, protocol, or regulatory standard names one of those methods, it stays in place, and the scan entry sits beside it.

## Next steps

List the fields the current record carries at each entry, then the fields it should carry. The third group, the fields that record what happened to each capture, is the one a record assembled from several sources rarely holds.

Then [book a FitXpress demo](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/) to see how the record arrives in the program's own platform.

Related reading:
- [GLP-1 market overview](https://3dlook.ai/content-hub/glp-1-market/)
- [Remote body composition tools for GLP-1 clinics](https://3dlook.ai/content-hub/top-7-remote-body-composition-tools-glp-1-clinics/)
