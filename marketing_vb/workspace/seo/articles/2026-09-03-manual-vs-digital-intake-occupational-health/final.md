---
slug: 2026-09-03-manual-vs-digital-intake-occupational-health
product: fitxpress
status: edited
revision: 5
author: Assel Sekerova
hub: Occupational Health Screening (Hub 8)
cluster: Comparison
intent: GEO/comparison
action_type: create-net-new
primary_keyword: manual vs digital intake
target_words: 2050
word_count: 2160
editing_passes: 5
ai_density_before: 0.42
ai_density_after: 0.86
claims_verified: [FX-001, FX-003, FX-006, FX-007, FX-008, FX-009, FX-014]
claims_withheld: [FX-004]
source_draft: draft.md (revision 2, 2026-09-04 09:48)
review: [review-1.md, review-2.md]
review_decisions: [review-1-decisions.md, review-2-decisions.md]
qc: workspace/_quality/seo/2026-09-07-seo-review-2-manual-vs-digital-intake-occupational-health.md (17/20, rev 4)
gates_run: 2026-09-07, by seo-editor, in marketing_vb (both executed against this file, exit 0)
gate_article_lint: |
  $ python3 scripts/article_lint.py workspace/seo/articles/2026-09-03-manual-vs-digital-intake-occupational-health/final.md
  mode: article

  [ok  ] hard bans (detect-ai-tells)
           . detector_words: 2338
           . ai_density: 0.86
           . verdict: CLEAN
           . rhythm_variation: 0.66
  [ok  ] prose length
           prose words 2160 vs target 2050 (band 1742-2357)
           . prose_words: 2160
           . target: 2050
  [ok  ] claim traceability
           . claims_used: ['FX-001', 'FX-003', 'FX-006', 'FX-007', 'FX-008', 'FX-009', 'FX-014']
           . claims_known: 8
  [ok  ] banned claims
  [ok  ] superseded figures
  [ok  ] internal links
           . links_total: 6
           . links_distinct: 4
           . asset_urls: 0
           . directions: {'up': 1, 'sideways': 0, 'down': 0, 'trust': 1}
  [ok  ] keyword placement
           . keyword: manual vs digital intake
           . occurrences: 4
           . h2_count: 10
  [ok  ] abbreviations (M1)
  [ok  ] accuracy discipline
           . accuracy_figures_present: True
           . links_to_framework: True

  VERDICT: PASS
  Mechanics are clean. Judgment is still open: run quality-controller on whether
  the argument holds and whether each section earns its place.
  (exit 0)
gate_detect_ai_tells: |
  $ python3 brand-assets/style-guides/scripts/detect-ai-tells.py workspace/seo/articles/2026-09-03-manual-vs-digital-intake-occupational-health/final.md
  {"language": "en", "channel": "any", "channel_label": "unspecified", "profile": null,
   "total_words": 2338, "total_markers": 2, "em_dashes_excluded_from_density": 0,
   "ai_density_per_1000_words": 0.86, "density_budget": 8.0, "severity": "low",
   "short_form": false,
   "verdict": "CLEAN - check the positive side (voice, varied rhythm, a stated boundary) and ship.",
   "hard_fails": [], "house_rule_violations": [],
   "markers_by_category": {"avoiding_is": 1, "corrective_contrast": 1},
   "style_metrics": {"em_dashes": 0, "bold_count": 14, "bold_per_1000_words": 6.0,
    "title_case_headings": 0, "emoji_count": 0, "hashtag_count": 1, "bullet_lines": 5,
    "bold_lead_in_bullets": 0, "list_to_prose_ratio": 0.15, "wall_of_text": false,
    "rhythm": {"sentences": 73, "mean_words": 21.1, "variation": 0.66, "monotone": false,
     "uniform_paragraphs": false}, "punch_triads": [], "punch_triad_count": 0},
   "top_offenders": [{"marker": "serve as", "count": 1, "first_line": 285},
                     {"marker": "rather than", "count": 1, "first_line": 388}]}
  (exit 0, channel "any" - the default, nothing muted)
soft_marker_rulings: >
  Two soft markers, unchanged from revision 4, both left in on purpose.
  (1) "serve as" sits inside the Review 1 scope note ("or serve as a basis for hiring or
  employment decisions"). Reviewer boundary wording, protected.
  (2) "rather than" arrives with Review 2 item 7 verbatim: "rests on repeatability and
  standardized capture rather than a claim of superiority over expert tape measurement."
  Corrective "rather than" is a terminology-guardrails Part 1 JUDGMENT line, so the editor
  rules it, not the script. Ruled LICENSED: the contrast draws a real accuracy boundary,
  since FX-001 is measured against expert manual measurement as its reference and superiority
  over that reference is not available to us. Recommended form comes first, limitation second.
  QC concurred on 2026-09-07 ("agree, LICENSED").
word_band: >
  Reviewer's binding band from Review 1 is 1,900-2,200 and it still governs. Revision 5 lands at
  2,160, a net -25 on revision 4's 2,185 and -39 on revision 3's 2,199. Every QC fix paid for
  itself: question 2 rewritten to the reviewer's E5 wording (-11), the Section 2 verdict bullet
  trimmed of its third "testing, examination and clinical review" clause (-9), the fallback FAQ
  merged so the fallback is stated once (-8), against the Section 3 opener restructure (+3).
  The definition-bullet split is word-neutral.
protected_untouched: >
  Re-verified by diff after this pass, not by eye: the five-row workflow table in Section 5
  (plan.md:251-257) and the eight-row metrics table in Section 7 (plan.md:302-311) are still
  byte-identical to plan.md. Also unchanged across revisions 4 and 5: the Section 1 scope note,
  all four sentences including the licensed "It is not positioned as a medical device."; FX-003
  with its conditions and FX-001 with its reference and its "varying by body part"; the
  non-disclosure-agreement sentence; the EEOC paragraph and its closing pair; the
  evaluation-framed CTA; all ten <!-- claim: FX-xxx --> markers across the same seven IDs,
  including the FX-014 marker on the "processes no personal identifiers" sentence. Section 4's
  two adjacent reviewer-verbatim paragraphs (Review 1 A5-5 and Review 2 item 3) are untouched
  per open item R2-1, which stays Vadim's call. R2-2, R2-3 and R2-4 stay declined and unedited.
  No new claim, source or figure; the claim set stays at seven.
changes_summary: |
  ## Revision 5 - QC remediation (2026-09-07, seo-editor)
  This pass carries NO new reviewer input. It closes three deductions from the 17/20 QC report on
  revision 4 (`workspace/_quality/seo/2026-09-07-seo-review-2-...md`), all of them defects this
  pipeline introduced while applying Review 2, plus one optional tighten. Five scripted edits,
  each asserted count == 1.
  - QC A-1, the important one: **E5 was retained, not applied.** The instruction is to reduce the
    five questions to two broader ones, "which components move, and how measurement performance
    was evaluated". Revision 4 kept Q1 and the old narrow Q5 verbatim, which is a retention. That
    is also what manufactured the Section 7 duplication escalated to Vadim as an unresolvable
    reviewer-vs-reviewer conflict. Question 2 now reads "How was measurement performance
    evaluated?", the reviewer's own E5 wording. The E3 sentence underneath now answers it instead
    of repeating it, and no coverage is lost: repeated scans, measurements and reference method
    are all still named, in that sentence. **The Section 7 open item is closed by edit.**
    `review-2-decisions.md:179` graded this row "Verbatim" and "Q1 and Q5 survive"; both were
    wrong and are corrected in place, with the correction dated and attributed to the QC finding.
  - QC C, repetition regression: "testing, examination and clinical review remain ..." ran three
    times in thirteen lines, where revision 3 had it once. QC is right that the Section 2 instance
    was not mandated: review-2.md:33 introduces it with "The short-answer bullet **could
    become**", the only conditional in item 1 against four "Change X to" / "Replace with"
    instructions. Graded as a proposal, and a proposal loses to repetition control. The bullet
    now ends at "before the appointment". The scope note and the Section 3 opener keep the clause,
    where it is protected and where it does structural work.
  - QC E-1, weakened correction: the Section 3 opener let a reader attach the three-phase list to
    intake, which is the exact confusion item 1 exists to remove. Restructured so the sentence the
    list hangs off is unambiguously the screening workflow: "The comparison gets confusing when
    the occupational health intake process is treated as the whole of screening. The occupational
    health screening workflow has three phases." The keyword carve-out holds
    (`occupational health intake process`, plan.md:199, this section only), and the reviewer's
    mandated sentence is now closer to verbatim than in revision 4 ("has three phases", their
    wording, not "runs in three phases").
  - QC E-3, E2 missed its own purpose: it was modified to avoid stating the fallback twice in
    three sentences and stated it twice in two. Merged. The answer now states it once, in the
    reviewer's own E2 sentence, with "therefore" rather than the banned `so`.
  - Optional, QC E-2: the definition bullet ran 46 words after the E4 fold, which relocated the
    interruption instead of removing it. Split into a definition sentence and a mechanism
    sentence at zero word cost. All three carve-out keywords survive in Section 2:
    `digital patient intake`, `patient intake forms` and `intake forms` (plan.md:171).
  - Not touched, per instruction and per QC's own recommendation: R2-1 (Section 4's two adjacent
    paragraphs) and the three declines R2-2 / R2-3 / R2-4.
  - Left for the coordinator, flagged not fixed: `review-2-decisions.md` section 9 carries a gate
    transcript describing a file that was never shipped (2,173 words / net -26 / 0.66 against the
    artifact's 2,185 / -14 / 0.65, now 2,160 / 0.66). A dated staleness marker was added above it
    pointing at this file's gate blocks as authoritative; the coordinator's numbers were left
    intact rather than rewritten, since that section is theirs.

  ## Revision 4 - Review 2 applied (2026-09-07, seo-editor)
  Input: final.md revision 3. Every edit below is scripted with a count == 1 assertion on the
  string being replaced, so nothing was matched loosely. 22 replacements, all asserted unique.
  - Item 1, intake vs screening terminology (5 edits). H2 -> "The three phases of the
    occupational health screening workflow"; figure label to match; the short-answer verdict
    bullet and the "Phases the method reaches" table row replaced with the reviewer's own
    wording ("Relationship to the wider workflow"). Nothing in the article now attributes
    on-site testing or clinical review to intake. MODIFIED, per decisions §1: the opening
    paragraph keeps its framing sentence so that `occupational health intake process`
    (plan.md:199, this section only) survives; the reviewer's second and third sentences are
    verbatim.
  - Item 2, the ambiguous "Both". MODIFIED, per decisions §2: the reviewer's replacement is
    taken whole with the rescreen outcome restored as the third item in their own list. The
    A5-3/A5-4 mechanism (plan.md:160-170) and the Hub 8 guardrail both require it. "Often"
    is a hedge, not a rate, so no frequency claim enters.
  - Item 3, absolute table rows. All five recommended cells verbatim, plus the reviewer's
    replacement reading paragraph. The paragraph it replaced ("Manual intake holds three
    dimensions ...") was ours, not Review 1's - checked against review-1.md first.
  - Item 4, hybrid prevalence. "For most programs the answer is hybrid" is gone; the reviewer's
    paragraph is verbatim. The split is still stated component by component with a fallback and
    a transfer path per moved step, so the section stays decisive without a prevalence claim.
  - Item 5, the FitXpress output sentence. Verbatim. This was a real sourcing error: BMI is not
    one of the 80+ measurements (proof-points.md:57 vs :58, carried as FX-008 and FX-009).
    "Time-stamped at capture" over-specified what use-cases/fx-occupational-health.md:10 and
    faq.md:90 actually say. Both claim markers stay on the sentence. The other "time-stamped"
    mention, in the accuracy paragraph, is a general statement about records and is left.
  - Item 6, privacy paragraph. PARTIALLY APPLIED, per decisions §6. Applied: the self-contradiction
    the reviewer caught (the boundary is the determination, not the input); the AWS S3 SSE-S3 /
    TLS detail trimmed to "at rest and in transit"; Business Associate Agreements added in
    compliance.md's own wording ("with HIPAA-covered customers", not "on request"). Declined and
    carried to Vadim as R2-2 and R2-4: dropping "processes no personal identifiers"
    (compliance.md:23 states it flatly and three assets repeat it) and the output-retention
    rewrite (the deletion half is already more precise than the replacement). R2-3, adding GDPR
    controller/processor, was declined on 2026-09-07 because no brand-asset carried it, then
    APPLIED the same day once Vadim made the sentence canonical in compliance.md ("GDPR roles").
    It now stands as its own sentence in the privacy paragraph, hedge intact.
  - Item 7, accuracy conclusion. Both reviewer sentences verbatim. The approved 96-97%,
    1.5-2.0 cm and repeated-scan statements are untouched and keep their FX-001 / FX-003 markers;
    the two benchmarks stay in separate paragraphs against separate references.
  - E1, E3 verbatim. E2 MODIFIED (decisions §8): the reviewer's sentence dropped in whole would
    say the fallback exists twice in three sentences, so their substance is carried in two
    sentences instead. One further deviation from the decisions file, one word: it ships
    "and the workflow therefore needs" where the decisions file wrote "so the workflow needs".
    `so` introducing a result is a Part 2 hard ban and the reviewer's own connector was
    "therefore", so the guardrail and the reviewer agree against the decisions file's phrasing.
    Substance identical, +1 word.
  - E4 MODIFIED (keyword carve-out, decisions §8): the standalone clinic-software sentence is
    gone as instructed, and `digital patient intake`, `patient intake forms` and `intake forms`
    (plan.md:171, this section only) are folded into the definition bullet. Net -4 words.
  - E5 verbatim, and it deliberately reverses Review 1's "What should be preserved" item 6.
    Five implementation questions down to two. Rescreen rate, integration success and manual
    fallback rate are already rows 4, 8 and 5 of the metrics table directly above them.
    plan.md:314-319 still carries the Review 1 protection and is now stale on this one point.
  - One knock-on edit, ours: "Two diligence questions sit alongside the numbers", because
    Section 1 already opens "Two questions decide the method" and the reduction had put the
    same construction on the page twice.

  ## Revision 3 - Review 1 applied (2026-09-04, seo-editor) - retained
    - Pass 1, citations: no source is cited twice. NHANES, OSHA and EEOC each appear once with a
      link; FAQ Q4 refers back to EEOC by short form without re-linking. The accuracy framework is
      linked twice by plan design (figure paragraph + FAQ Q1) and the hub twice (Sections 1 and 7),
      both internal navigation rather than citations.
    - Pass 1, sourcing gap fixed: the OSHA Appendix C passage asserted what a federal standard
      requires and carried no link. It now sits on a meaningful anchor (terminology guardrails Part
      1 rule 2). Zero prose-word cost.
    - Pass 2, intro: reordered to open on the concrete scene (questionnaire, tape, transcription,
      clinician) and reframe in sentence two. The old opener led with the framing and the paragraph
      closed on "The intake around the examination runs long", which was cut.
    - Pass 2, flow: Section 4 went H2 straight into a fourteen-row table with no orientation. Added
      one lead-in line. Section 6's hybrid conclusion was one 34-word sentence; split in two, and
      the second half now pays off the fallback and integration rows that otherwise only lived in
      the table.
    - Pass 3, expert voice: "which decision it must be accurate enough for" replaced with the
      canonical "accurate enough for which decision?"; "The role is a remote intake and
      documentation layer" given its subject back; "the fallback, which no digital channel removes
      the need for" rewritten as "the fallback that every digital channel still needs".
    - Pass 3, repetition: "capture" three times in three sentences in Section 8 p1; "across staff,
      sites and time" and "across repeats, staff and sites" two paragraphs apart; "depends on" used
      nine times, one of which was in a cell we own. Each fixed once.
    - Pass 3, table cells we own (not the reviewer's): "Integration dependency | Depends on
      integration with the receiving system" was circular and now reads "Requires a receiving system
      and a defined transfer path"; the data-entry cell lost its "depends on".
    - Pass 3b, strategy: positioning §8 clean (no diagnosis / decisioning / clinician-replacement /
      guaranteed compliance / fraud-detection claim). Boundary carried by the Section 1 scope note
      and the Section 8 pair, which is where review item 1 put it after removing the does/does-not
      table the hub owns. Vertical boundary held: intake and documentation only. Internal links up /
      trust / down / CTA present; sideways is deliberately absent because its only permitted target
      is unpublished (plan.md, decisions §B). FAQ 4 questions, 2-4 sentences each. CTA evaluation-
      framed, no forced demo.
    - Pass 4, EEOC: "One legal boundary sets the timing, and in the US it is explicit" still carried
      the universal framing review item 6 rejected. Now "In the US the timing is set explicitly."
    - Pass 4, abbreviations: OSHA, NHANES, EEOC, HIPAA, GDPR expanded at first use; BMI, US, EU
      bare; NDA written out. EEOC uses the short form on its second appearance in FAQ Q4.
    - Pass 4, accuracy discipline: FX-003 and FX-001 remain verbatim from accuracy-formulations.md
      with their conditions and their reference; the two benchmarks stay apart; no ISO 8559 figure,
      no per-measurement figures, no 95%+ repeatability; repeatability written "less than 1 cm";
      the figure paragraph carries the framework link.
    - Pass 4, stacked negation (M2): no sentence carries two negations. Boundary statements are
      recommended-form-first, one negation each.
self_check: |
  Asked after the QC remediation: what here still reads machine-written?
  - The honest one first: the Section 7 duplication I escalated last pass as an unresolvable
    reviewer-vs-reviewer conflict was not one. I graded a reviewer instruction by the decisions
    file's summary of it instead of by the instruction, and then treated the resulting overlap as
    protected. The reviewer had supplied the wording that dissolved it. The general lesson is
    modality: "Change X to" and "Replace with" bind, "could become" and "suggested replacement"
    are proposals, and a proposal loses to a house rule. Two of this pass's five fixes come from
    getting that wrong once.
  - "at or around the appointment/visit" still appears five times. Four are cells or sentences
    Review 2 supplied or Review 1 protected, and the fifth is the manual-intake definition bullet.
    Checked it again for a rewrite and left it again: every alternative either hardens the hedge
    Review 2 spent item 3 softening, or is clunkier for no gain. It is the residual tone cost of a
    pass whose whole job was adding hedges.
  - Section 8 still reads assembled rather than written, unchanged from revision 3, because about
    200 of its words are fixed approved text (FX-003 with its conditions, FX-001 with its
    reference, the non-disclosure-agreement line, the compliance sentence, the boundary pair). QC
    flags the compliance sentence as a 68-word inventory that got longer while being trimmed, and
    that is fair. Not fixed here: breaking it into the reviewer's five short sentences means
    re-opening item 6, whose three declines are settled and waiting on Vadim.
  - Still no first person anywhere. Deliberate, unchanged: there is no occupational-health
    deployment proof point in the pack, and an invented "in our experience" would be worse than
    its absence.
---

# Manual vs Digital Intake in Occupational Health Screening: Which Method Fits Which Workflow

## The intake step is where screening programs lose time

A candidate fills in a health questionnaire, a medical assistant takes tape measurements, and someone transcribes both into the screening record before the clinician sees anything. Framed as manual vs digital intake, that sequence sounds like a software preference; inside a screening program it is an operations question about a fixed appointment slot.

Four operational costs come out of that step: throughput against fixed appointment capacity, missing or incomplete intake data, rescreens caused by unusable records, and documentation that fails to line up across sites or vendor partners. Adding clinic capacity adds appointment slots. It does not change the intake work inside each slot, and whether extra capacity relieves the bottleneck depends on where the time is lost.

Two questions decide the method: which intake steps a remote channel can carry, and which programs gain enough to justify the change. The category, its buyer profiles and the full workflow sit in the [occupational health screening software hub](https://3dlook.ai/content-hub/occupational-health-screening-software/).

> ***Scope note.*** *In this comparison, digital intake means the whole pre-appointment workflow. FitXpress provides the remote body-measurement component; questionnaire collection, testing, examination and clinical review remain within the customer's other systems. FitXpress does not perform medical examinations, make fitness-for-duty or clearance determinations, or serve as a basis for hiring or employment decisions. It is not positioned as a medical device.*

## Short answer: what each intake method covers

- **Manual intake** means a paper health questionnaire, a staff-administered tape measurement, and transcription into the screening record, all at or around the appointment.
- **Digital intake**, or digital patient intake in clinic software, collects the same questionnaire content through a structured remote channel before the appointment, replacing paper patient intake forms. The body measurement comes from a guided smartphone scan of two photos in under 45 seconds. <!-- claim: FX-006 --> <!-- claim: FX-007 -->
- **The overlap is partial.** A remote channel can carry the questionnaire and the body measurement; modality-specific testing and the examination stay in the clinic.
- **The operational cost sits inside that overlap.** In manual workflows, questionnaires and measurements are often collected or transcribed at or around the appointment. Missing or inconsistent information can then delay review, require follow-up or trigger a rescreen.
- **Neither method wins outright.** Manual intake combines data collection with the on-site visit. Digital intake moves eligible steps before the appointment.

## The three phases of the occupational health screening workflow

The comparison gets confusing when the occupational health intake process is treated as the whole of screening. The occupational health screening workflow has three phases. A remote intake channel reaches the first, while testing, examination and clinical review remain within the wider screening process.

1. **Pre-appointment intake.** The health-history questionnaire, required documents, and eligible body measurements. This is the phase a remote channel can carry.
2. **On-site screening.** Equipment-based testing (drug screening, vision, hearing, functional capacity) and the examination, which need the person present.
3. **Clinical review.** The reviewing provider reads the record and, where the program calls for it, makes the determination.

> **Figure 1.** The three phases of the screening workflow, with the remote-capable part marked.

Manual practice varies most at the measurement step. The [anthropometry procedures manual](https://wwwn.cdc.gov/nchs/data/nhanes/public/2021/manuals/2021-Anthropometry-Procedures-Manual-508.pdf) for the National Health and Nutrition Examination Survey (NHANES) specifies the waist measurement down to the anatomy: palpate for the uppermost lateral border of the right ilium, mark it at the midaxillary line, have a second examiner confirm the tape is level, and read at normal expiration. The protocol shows the training, landmarking and quality control behind a standardized manual measurement.

One regulated context already routes the questionnaire for confidentiality: [Appendix C to the Occupational Safety and Health Administration (OSHA) respiratory protection standard](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.134AppC) forbids the employer and the supervisor from reading a worker's answers, and obliges the employer to explain how to deliver the form to the reviewing health care professional. The requirement is specific to respirator medical evaluations, and any channel carrying the form has to meet it.

FitXpress does not administer that questionnaire; the medical evaluation and the clearance determination stay with the reviewing health care professional.

## Manual vs digital intake, compared dimension by dimension

Each row is a dimension a program can check for itself.

| Dimension | Manual intake | Digital intake |
|---|---|---|
| Where the step happens | Usually at or around the clinic appointment | Remotely, before the appointment |
| Who measures | Clinic staff, with a tape | The person, guided on their own phone |
| Consistency across staff and sites | Varies with technique, landmarking and local training | A standardized guided procedure, subject to capture quality and validation requirements |
| Record format | May require manual entry or scanning; structure depends on the receiving system | Can arrive in a structured format when the integration supports it |
| Questionnaire confidentiality routing | Depends on local paper handling | Depends on permissions, system configuration and the program's data-handling design |
| Time inside the appointment slot | Questionnaire, measurement and transcription | Testing, examination and any intake exceptions that require support |
| Relationship to the wider workflow | Intake is completed at or around the visit; testing and review follow | Eligible intake is completed before the visit; testing and review follow |
| Access requirement for the person screened | Attendance and completion of the required on-site intake steps | A smartphone, a connection, and a completed guided capture |
| Setup and change-management cost | Lower incremental implementation cost; continuing staff and administration requirements | Integration, configuration and staff retraining before the first scan |
| Ongoing labor | Staff time at every appointment | Less routine collection and transcription; ongoing monitoring and exception support |
| Exception handling | Handled in person during the visit | Needs a defined path for incomplete or failed captures |
| Integration dependency | Can operate without systems integration, but may still require manual entry into the receiving system | Requires a receiving system and a defined transfer path |
| Fallback availability | Is itself the fallback | Requires the manual path to stay open |
| Data-entry correction | Transcription errors corrected by re-entry | Can reduce transcription when integrated; corrections follow the receiving system's process |

Moving eligible intake steps before the appointment can reduce in-appointment collection and transcription. The effect depends on completion rates, fallback volume, integration quality and existing rescreen causes.

Manual intake has lower integration requirements and provides immediate in-person support. Digital intake can improve pre-appointment availability, standardize the capture procedure and reduce transcription when connected to the receiving system. The appropriate model depends on volume, access requirements, exception rates and the existing technology environment.

## How the workflows differ

Side by side, the two models run the same steps in a different place and order.

| Manual/on-site intake | Structured pre-appointment intake |
| :- | :- |
| Forms completed at or around the appointment | Forms completed through the program's intake system |
| Staff perform required measurements | Eligible measurements captured remotely |
| Information is entered or transcribed | Structured data is validated and transferred |
| Missing items are handled during or after the visit | Exceptions are identified before the visit |
| Tests and examination follow | Tests and examination remain on site |

The operational difference sits in the fourth row: a structured pre-appointment path can surface exceptions before the visit instead of during it, while tests and the examination stay on site under both models.

## A decision framework: which intake method fits which program

Manual intake remains practical in several situations: single-site or low-volume programs where the appointment slot is not the constraint; populations without reliable smartphone or network access; intake dominated by history, symptom and functional content, where body measurement is a minor line item; workflows where the measurement is part of the examination; and programs with no downstream system able to receive a structured record.

A digital channel earns its setup cost under different conditions: high volume against fixed appointment capacity, several sites or vendor partners needing comparable records, rescreens traceable to missing or inconsistent intake data, and documentation that has to hold across reporting periods.

A hybrid model combines remote questionnaire and body-measurement capture with on-site testing and examination. The split is determined component by component, with a fallback and transfer path for each step moved before the visit.

In the US the timing is set explicitly. Under [Equal Employment Opportunity Commission (EEOC) enforcement guidance](https://www.eeoc.gov/laws/guidance/enforcement-guidance-preemployment-disability-related-questions-and-medical), an employer may not ask disability-related questions or conduct medical examinations until after a conditional job offer. Other jurisdictions set their own timing. Choosing between manual vs digital intake decides a method. It never decides a candidate.

## How to evaluate the change

Each metric needs a baseline before the pilot.

| Metric | What to establish before implementation |
| :- | :- |
| Intake time during the appointment | Current median time per appointment |
| Pre-appointment completion | Share of records complete before arrival |
| Missing-data rate | Fields most frequently absent |
| Rescreen rate | Volume and reasons for repeat appointments |
| Manual fallback rate | Share unable to complete remote intake |
| Correction or re-entry rate | Records requiring staff intervention |
| Multi-site consistency | Defined completeness and repeatability criteria |
| Integration success | Share transferred without manual transcription |

Two diligence questions sit alongside the numbers:

1. Which intake steps move to the remote channel, and which stay on site?
2. How was measurement performance evaluated?

Any vendor should be able to explain how repeatability was evaluated, including the measurements, sample, number of repeated scans and reference method. Which buyer profiles gain most, and in what order, is set out in the [occupational health screening software hub](https://3dlook.ai/content-hub/occupational-health-screening-software/).

## Where FitXpress fits

FitXpress covers one part of the first phase: body measurement, taken remotely before the appointment. The person scans on their own phone, from two photos, in under 45 seconds. The scan produces structured results associated with a scan timestamp. Outputs include 80+ body measurements and calculated metrics such as BMI. <!-- claim: FX-006 --> <!-- claim: FX-007 --> <!-- claim: FX-008 --> <!-- claim: FX-009 -->

The useful question about any measurement method is: accurate enough for which decision? For intake documentation, that is whether records stay comparable across staff, sites and time. Internal repeatability testing on a real-world customer dataset, using five repeated scans per participant, showed strong scan-to-scan consistency across the majority of evaluated measurements. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm. <!-- claim: FX-003 --> The [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) sets out those conditions, starting from the point that every accuracy figure is relative to one specific reference.

Accuracy is a separate measurement against a separate reference. Internal validation across multiple real-world scan events with five repeated scans per person against expert pattern-maker manual measurements shows 3DLOOK's measurement accuracy of approximately 96-97% across body metrics, with a typical absolute error of 1.5-2.0 cm per measurement, varying by body part. <!-- claim: FX-001 --> Detailed methodology is available under a non-disclosure agreement. The measurement case therefore rests on repeatability and standardized capture rather than a claim of superiority over expert tape measurement. The wider operational case includes pre-appointment availability, structured transfer and reduced reliance on transcription. A structured, time-stamped record is easier to compare than a written one, though structure alone does not ensure comparability or compliance; that depends on the capture method and the receiving system.

FitXpress maintains Health Insurance Portability and Accountability Act (HIPAA) safeguards in US healthcare contexts and signs Business Associate Agreements with HIPAA-covered customers, encrypts data at rest and in transit, processes no personal identifiers, and deletes photos immediately after processing or within 30 days, with the window set by client policy. In most enterprise deployments, the customer acts as controller and 3DLOOK acts as processor under the General Data Protection Regulation (GDPR). <!-- claim: FX-014 --> FitXpress supports intake and documentation for clinician review; it does not make clearance, eligibility or fitness-for-duty determinations. Compliance evaluation runs on data-privacy and recordkeeping frameworks, and the regulatory classification of a deployment depends on intended use, context and jurisdiction. [3DLOOK's mobile body scanning platform](https://3dlook.ai/) covers how the data is captured and delivered.

## Frequently asked questions

**Is digital intake more accurate than manual tape measurement in occupational health screening?**
The comparison does not resolve that way, because 3DLOOK's accuracy figure is measured against expert manual measurement as the reference. The answerable questions are whether the expected error suits the decision and whether repeated measurements stay comparable. Repeated scans showed typical scan-to-scan differences of less than 1 cm for most evaluated measurements, with the conditions set out in the [accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/). <!-- claim: FX-003 -->

**Which parts of occupational health intake cannot be moved to a digital channel?**
History and symptom review that needs clinical follow-up, modality-specific testing such as drug screening or vision and hearing checks, functional assessment, and the examination. Anything needing equipment or a clinician stays in the clinic.

**What happens if a candidate cannot complete a remote scan?**
Access varies by workforce, role and geography. The workflow therefore needs a documented manual alternative for people who lack the required access or cannot complete the remote capture.

**Does moving intake to a digital channel change the post-offer boundary for pre-employment screening?**
No. In the US, under EEOC guidance, the boundary is set by the timing and content of disability-related questions and medical examinations, and the channel the data arrives through does not move it. What a program may ask stays with its own counsel.

## Next steps

Run the two intake models against the program's own throughput and rescreen numbers, component by component, and see which are worth moving. Then [talk to 3DLOOK about the intake workflow](https://3dlook.ai/pricing/#bd-modal-personalized).
