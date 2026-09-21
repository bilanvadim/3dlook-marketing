---
slug: 2026-09-21-glp-1-patient-progress-record-body-data
plan: plan.md
product: fitxpress
stage: plan
created: 2026-09-21
mode: no-checkpoint run, 2026-09-21. Post-factum review by Vadim.
---

# Plan audit, 2026-09-21-glp-1-patient-progress-record-body-data

Why the plan looks the way it does. The writer does not need this file; `seo-publisher`, the
editor and Vadim do.

## 1. Phase 0, how the gate was resolved

The pack arrived with `phase_0_resolved: true` and `action_type: "Create net-new"` quoted
verbatim from content-plan.md:163, so the gate is a GO and Phase 1 ran. `published_inventory`
reports `already_live: false`, and the two live Hub 3 assets (`glp-1-market`,
`top-7-remote-body-composition-tools-glp-1-clinics`) are both inside four weeks, so this is not a
refresh in disguise. Nothing in the row is conditional, so no question went back to Vadim on
placement.

Priority is P1 and the row is pencilled for October 2026. It is being written in September because
the Admin Panel post and the BMI-verification guide both need a documentation anchor inside Hub 3,
and the same-day Hub 2 sibling is taking the general telehealth half of that job.

## 2. The keyword finding, and why the plan says it out loud

Three seeds were pulled. Two returned nothing and the third returned a different topic:

| Seed | Result | Read |
|---|---|---|
| glp-1 patient progress record | `seed_has_data: false`, variants also no data | The phrase is not searched |
| glp-1 progress tracking | no data; "glp-1 progress" measured at 0/mo | Demand is absent, not merely unmeasured |
| glp-1 monitoring | 10/mo, with 60/30/20 satellites | Real, but it is bloodwork and dosage follow-up intent |

No substitution was made. The usual move when a seed has no data is to promote a head term from
the variants, but the only head term with a number here is "glp-1 patient" at 10/mo, and its idea
set is patient-assistance programs, education PDFs, portal logins and satisfaction surveys. Taking
it would have produced a keyword narrative pointing at a different article. Writing "primary
keyword: glp-1 patient, 10/mo" in the frontmatter would also have read on a later checkpoint as
though demand had been verified. It has not been, and the plan says so in the keyword section
rather than in a footnote.

The failure mode being avoided is the one from 2026-08-25, when
`remote-body-measurement-online-fitness-coaching` shipped against a primary keyword with zero
data and nobody found out until afterwards. Here the finding is on the front page of the plan and
in the success criteria: assisted conversions, sales use and AI-answer citations, not sessions.

The monitoring pocket was the one real temptation, 120/mo across four phrases. It was confined to
a single FAQ answer. Writing toward it would have meant lab tests, dosage follow-up and clinical
interpretation, all of which this vertical is explicitly barred from, and it would have put the
page in competition with clinical publishers who own that query properly.

## 3. Cannibalization, five boundaries checked

1. **`glp-1-market` (live hub, 2026-08-28).** Owns market growth and the progress-tracking thesis.
   Used as an up-link in Section 1 and as related reading. No growth figure, no market sizing and
   no "why GLP-1 is growing" passage appears anywhere in the outline.
2. **`top-7-remote-body-composition-tools-glp-1-clinics` (live, 2026-08-21).** Owns buyer
   evaluation and vendor comparison. This plan has no comparison table, no tool list and no
   selection criteria. Section 8 is a check a program runs on its own record, not on vendors.
3. **`online-pharmacy-bmi-verification-a-2026-compliance-guide` (live, 2026-08-24).** Owns BMI
   verification and eligibility workflow. It is linked from exactly one sentence, in FAQ 3, and the
   workflow is never re-explained. Section 6 deliberately states eligibility only at claim level.
4. **Sister row, "How Weight-Loss Clinics Can Standardize Baseline Body Data for GLP-1 Patients"
   (P1, separately pencilled).** Owns baseline standardization. Section 3 is limited to one passing
   sentence about the first entry, and Section 4 is written about cadence and comparability rather
   than about how a baseline is defined. If the writer finds a baseline paragraph growing, it is
   the sister article and it gets cut.
5. **Same-day Hub 2 sibling, `2026-09-21-ai-body-scanning-telehealth-documentation`.** Owns record
   consistency across telehealth generally. This page owns which fields a GLP-1 entry carries and
   why. The split held in practice on four specific choices, listed in section 4 below.

## 4. Separating this plan from the same-day sibling

Same anchor claim, same Admin Panel, same product page, planned the same day. Four deliberate
divergences so the two pages do not read as one article split in half:

- **Spine.** The sibling runs problem, short answer, why now, workflow placement. This one runs
  problem, short answer, then a reasoning section on why each field group is in the record. There
  is no "why now" section here, because the why-now for GLP-1 belongs to the hub.
- **The figure.** The sibling keeps repeatability in its FAQ. Here it sits in Section 4, in the
  cadence argument, which is where the pack's own note places it: repeatability is the reason two
  entries are comparable at all. That is also the only figure in this draft.
- **Tables.** The sibling has one comparison table about record shape. This plan has none. The
  field list is bullets in Section 2 and appears once. A table here would have restated it and
  would have made the two pages look alike at a glance.
- **FAQ sets do not overlap.** The sibling asks about documentation requirements, note-taking AI,
  incomplete scans and comparability. This one asks about lab monitoring, incomplete scans,
  eligibility and reference methods. The incomplete-scan question is the single shared item. It is
  kept because it carries an approved limitation that a GLP-1 program genuinely asks about, and
  because the two answers sit on different pages in different hubs. Flagged for the editor rather
  than quietly duplicated.

## 5. Structure calls that could have gone the other way

- **The question as the H1, unchanged.** With no keyword to place, the ranking surface is the
  direct question itself. Four alternatives were written and rejected; the closest, "GLP-1 Progress
  Documentation: What Belongs in the Patient Record", was dropped because "documentation" as the
  lead noun is the sibling's territory. The declarative variant is kept for social and outreach.
- **Retention was moved out of Section 5.** An early pass had delivery and retention together.
  Splitting them puts the retention rule, the random IDs and the HIPAA and GDPR roles in one place
  (Section 7) with the trust link, and keeps Section 5 about how the entry reaches the team. It
  also stops the same fact appearing twice.
- **The disability limitation moved from the evaluation section to FAQ 2.** It was in both at
  first. Section 8 is now only what the program counts; the limitation is stated once, as an
  approved claim, where a reader would ask it.
- **Section 6 hands two questions to the FAQ.** Eligibility (FAQ 3) and reference methods (FAQ 4)
  are answered once, in the FAQ, so Section 6 stays at claim level. Without this split the editor
  would have had two near-duplicate passages to cut, which is what happened on 2026-09-11 when a
  fourth FAQ question was moved into the body.
- **No word count for an intro block.** The scope note sits at the end of Section 1 inside its 200
  words, not as a separate unnumbered block, because the sensitive-vertical rule asks for it early
  and this is the earliest place it can carry context.

## 6. Risks

1. **Zero-demand topic.** If this page is measured on organic sessions it will look like a failure.
   Success criteria are named in the plan; they need to travel with the page into any reporting.
2. **Clinical drift.** Every field in the record invites a sentence about what a change in that
   field means. Three boundaries in Sections 3, 4 and 6 exist for that reason, and the FAQ 1 answer
   is the pressure point, since it sits next to a genuinely clinical query.
3. **Invented fields.** The record framing tempts a writer into export formats, audit logs, alerts
   and dashboards. The approved claims carry a closed list, and Section 5's boundary says so
   directly.
4. **Admin Panel wording.** The feature's existence is confirmed by the live launch post; exact
   capability wording beyond FXS-DELIVERY is not. One plain sentence, API and SDK first, Admin
   Panel second, matching the sibling.
5. **Gate 8 and the title.** GLP-1 appears in the H1 before any prose can expand it. The live GLP-1
   articles have the same shape. If the gate fires, the editor rules; the title does not change to
   satisfy a regex.

## 7. Open items for Vadim

1. **No measured demand, confirmed and accepted.** This page is a sales-support and answer-engine
   asset, not a traffic play. Confirm it is judged that way when Hub 3 performance is next reviewed.
2. **Written ahead of its October pencil date.** Fine if the intent is to have the Hub 3
   documentation anchor live alongside the Hub 2 sibling. Say if the October slot matters.
3. **Baseline sister row.** This plan leaves baseline standardization untouched by design. The
   sister row is still unwritten, and the two will link to each other once it exists.
4. **One shared FAQ question with the Hub 2 sibling** (what happens when a patient cannot complete
   a scan). Kept deliberately, flagged here in case a single canonical answer is preferred.
5. **Cover visual concept** described in the plan's visuals table, plus one optional in-text
   visual. The designer decides whether the second one earns its place.
