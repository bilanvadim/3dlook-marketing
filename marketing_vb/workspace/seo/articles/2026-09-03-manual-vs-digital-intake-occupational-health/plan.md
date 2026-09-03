---
slug: 2026-09-03-manual-vs-digital-intake-occupational-health
product: fitxpress
primary_keyword: manual vs digital intake
primary_use_case: brand-assets/product-info/icp-detail.md §6 (Occupational Health / Pre-Employment Screening)
hub: Occupational Health Screening (Hub 8)
cluster: Comparison
intent: GEO/comparison
action_type: create-net-new
priority: P0
status: approved
target_words: 2500
author: Assel Sekerova
created: 2026-09-03
audit: plan-audit.md
review_package: checkpoint-1-review-package.md
context_pack: workspace/seo/_context-packs/2026-09-03-manual-vs-digital-intake-occupational-health.yaml
keywords_file: workspace/seo/_keywords/2026-09-03-manual-vs-digital-intake-occupational-health.yaml
---

# SEO Plan — Manual vs Digital Intake in Occupational Health Screening

## Content Strategy Fit (Phase 0)

Phase 0 was resolved by the Orchestrator against `brand-assets/content-strategy/content-plan.md:212`
and verified against the context pack. It is recorded here, not re-opened.

- **Hub / cluster:** Occupational Health Screening (Hub 8) → Comparison
- **Action type:** `create-net-new` ("Net-new supporting"). Proceeds because the angle is distinct
  from the live hub: the hub owns the *category* and the FitXpress workflow, this page owns the
  *method-level comparison and the choice between the two methods*.
- **Hub status:** live since 2026-07-10. The guidelines §5 line "do not create broad occupational
  health articles until the Occupational Health hub is live and indexed" does not apply. The Hub-8
  preamble in `content-plan.md:207` lifts the block on supporting articles.
- **Existing pages:** `https://3dlook.ai/content-hub/occupational-health-screening-software/` is
  both the cannibalization warning and the up-link target. Used as the up-link in Sections 1 and 10.
  Nothing to refresh: `already_live: false` for this comparison article.
- **Cannibalization guardrail (row verbatim):** "Throughput, missing data, rescreens, multi-site
  consistency. No medical/clearance claims." The hub already owns pre-employment, pre-placement and
  return-to-work intake, fit-for-duty documentation support, rescreens, multi-site consistency,
  workforce screening vendors and workers' compensation. **How this page stays narrower:** it is a
  method comparison and a decision framework. It does not restate the category definition, the
  buyer-profile roster, the five-step implementation walk-through, or the workflow-vs-workflow table.
  Full working: `plan-audit.md`.
- **Vertical boundary (guidelines §9, verbatim):** Occupational Health "owns pre-employment intake,
  pre-placement intake, return-to-work intake, fit-for-duty documentation support, rescreens,
  multi-site consistency, workforce screening vendors, workers' compensation, and absence workflows.
  Do not imply hiring decisions, employment eligibility decisions, clearance decisions, diagnosis, or
  fitness-for-duty decisioning." **Scope of this page: intake and documentation only.** No sentence
  of the shape "clears employees for duty" appears anywhere. The messaging line "speed clearance
  decisions" means shortening time-to-decision and must not appear as a capability claim.
- **Internal links planned:** up → the live Hub-8 hub (Sections 1, 10) · side → accuracy framework
  and the Privacy/Regulatory FAQ, which is what guidelines §11 line 288 permits for this vertical
  ("may link to privacy FAQ and accuracy framework, not to unrelated wellness pages"); **no sibling
  cluster article is published yet**, so there is nothing else to link sideways to today · down →
  `https://3dlook.ai/` (Section 6) and the demo modal (Section 12), because no occupational-health
  vertical page exists · trust → the accuracy framework, linked from the paragraph carrying the
  figure (Section 7, FAQ 1)

## Keyword Analysis

**Read this before treating checkpoint 1 as "keywords verified".** There is no measured,
in-vertical, un-owned head term available to this article. Every option is one of: owned by the live
hub, reserved for a sibling row, off-vertical, or unmeasured. **This is a GEO / answer-engine and
long-tail procurement-question play with no measured head demand.** The classical-search upside is
close to zero by design; the upside is answer-engine coverage of the "which intake method fits which
workflow" question and the cluster authority it feeds back to the hub. Priced alternatives are in
`plan-audit.md`.

### Primary cluster

- **Primary keyword:** `manual vs digital intake`
- **Monthly volume:** no data (Ahrefs has no measurement for the phrase)
- **Difficulty:** no data
- **Seed had data:** `false`. Vadim's topic phrase, "Manual Intake vs Digital Intake in Occupational
  Health Screening", has no measured demand, and neither do its fragments. `manual intake` on its own
  is volume **0**, which means measured with no demand, a different fact from "no data". The primary
  keyword is a shortened form of the same phrase, chosen so it can sit naturally in the H1, the first
  paragraph and one H2 without stuffing. The full topic phrase stays as the H1 scope clause.
- **Why not the obvious one:** `occupational health screening` (250/mo, KD 6) is the only real
  in-vertical volume and it is **the hub's own target keyword**. Taking it is the exact
  cannibalization failure this article exists to avoid.

### Secondary clusters

Woven for relevance and for answer-engine coverage. None of these is the page's ranking target.

| Cluster | Keywords | Intent | Volume / KD | Where it goes |
|---|---|---|---|---|
| Vertical context (hub's head, used as context only) | `occupational health screening` | informational + commercial | 250 / 6 | Sections 1, 3, 5. Natural vertical naming. Ranking intent stays with the hub, which this page links up to. |
| Tool evaluation | `occupational health employee screening tool` | commercial | 30 / no data | Section 10 |
| Vendor shopping | `occupational health screening services` | commercial | 100 / no data | Section 10 |
| Adjacent intake-software space (relevance cost, use sparingly) | `digital patient intake`, `patient intake forms`, `intake forms` | informational + commercial | 150 / 4 · 150 / 6 · 700 / 4 | Section 2 only, in the definition of what digital intake means generally. **Do not build the article around this space:** it is clinic/patient intake, a different buyer and a different compliance frame. |
| Category naming | `digital occupational health intake` | informational | no data | Sections 4, 6. This is the hub's secondary keyword #1, so it is used as prose, never as a heading target. |
| Unmeasured long tails, GEO targets | `manual intake vs digital intake in occupational health screening`, `occupational health intake process`, `occupational health intake` | informational | no data | H1 scope clause, Section 4, FAQ |

**Explicitly not available to this page:** `occupational health` (5,400 / 22, hub territory and far
too broad), `pre employment occupational health screening` (100 / 1) and
`occupational health pre employment screening` (80 / 0), both hub-owned per `content-plan.md:211`
and reserved for the P2 `section first` row 219.

## Recommended Title

**H1:** Manual vs Digital Intake in Occupational Health Screening: Which Method Fits Which Workflow

Chosen because it carries the primary keyword in the first five words, names the vertical inside the
title so the page reads as occupational-health-scoped instead of a generic intake comparison, and its
closing clause is the promise the article actually keeps. "Which method fits which workflow" is the
`about-me.md` compare-by-role move, and stating it in the title is what stops the piece drifting into
a clean sweep, which guidelines §7 forbids for comparison content.

### Other options

1. **Manual vs Digital Intake in Occupational Health Screening: A Comparison for Providers and
   Employers** — plain and correct, and it names the buyer. Not chosen: "a comparison" describes the
   format instead of the answer, which is weaker for answer-engine extraction than "which method fits
   which workflow".
2. **Manual vs Digital Intake in Occupational Health Screening: Throughput, Rescreens, and Multi-Site
   Consistency** — mirrors the strategy row's angle exactly. Not chosen: the three-item list is a
   triple parallelism, banned as an AI signature by CLAUDE.md §6 and the style guide §7.
3. **Manual vs Digital Intake: A Decision Framework for Occupational Health Screening Programs** —
   leads on the deliverable and reads MOFU-to-BOFU. Not chosen: it pushes the vertical past word six
   and drops the comparison framing that the row and the intent both call for.
4. **Comparing Manual and Digital Intake in Occupational Health Screening** — the cleanest prose of
   the five. Not chosen: it loses the exact `manual vs digital intake` string, which fails the
   keyword-placement gate, and it loses the "vs" that answer engines match comparison queries on.

## Article Outline

Structure follows the 12-part FitXpress structure (`content-strategy-guidelines.md` §12), with the
comparison table pulled forward to Section 5 and the decision framework at Section 9. Those two are
the core of the piece, not optional blocks. Rationale for the reorder: `plan-audit.md`.

Model articles: `body-scanning-technology-comparison.md` for the Type C comparison shape (Quick
Answer Block up top, method-vs-method table, no clean sweep) and
`clinical-trials-anthropometric-measurement.md` for the sensitive-vertical scope note and boundary
discipline. Do not copy the accuracy figures from either: the comparison article's `1.0-1.5 cm` and
`0.4-0.8 cm` are category ranges, not ours, and it uses reserved words we do not use about our own
evidence.

### Section 1. The intake step, not the examination, is where screening programs lose time

- **Goal:** Reader recognises the problem as their own within two sentences, and knows the scope of
  the page before reading further.
- **Word count target:** 200
- **Must-cover:**
  - Open on the operational fact, no runway: the measurement and questionnaire step sits inside a
    capacity-constrained appointment slot.
  - Name the four costs the strategy row owns: throughput, missing or incomplete data, rescreens,
    multi-site inconsistency.
  - State what the page decides: which intake method fits which program, and on what dimensions the
    two actually differ.
  - **Scope note early, plus an italic disclaimer.** Non-negotiable, sensitive vertical. Model the
    format on `clinical-trials-anthropometric-measurement.md` line 40.
  - Up-link to the hub on a meaningful anchor phrase, for readers who want the category rather than
    the comparison.
- **Keywords to weave:** `manual vs digital intake` (H1 and first paragraph), `occupational health
  screening`
- **Sources:** the live hub, `https://3dlook.ai/content-hub/occupational-health-screening-software/`
- **Approved claims:** none. No figure in this section.
- **Boundary:** The scope note states intake and documentation only. Required content: FitXpress does
  not perform examinations, does not make fitness-for-duty or clearance determinations, and is not a
  basis for hiring or employment decisions. Use the licensed sentence "It is not positioned as a
  medical device." and nothing else with "positioned as".

### Section 2. Short answer: what each intake method actually covers

- **Goal:** An answer-engine-extractable summary of the comparison, and clean definitions of the two
  methods, before any argument.
- **Word count target:** 240
- **Must-cover:**
  - A Quick Answer Block, four to five bullets, mirroring the pattern at
    `body-scanning-technology-comparison.md` line 29. Each bullet is one method or one verdict.
  - Manual intake defined: written or paper health questionnaire, staff-administered tape
    measurement, transcription into the screening record, all at or around the appointment.
  - Digital intake defined: the same information collected through a structured remote channel before
    the appointment, with body measurement captured by guided smartphone scan.
  - One honest verdict bullet: the two are not substitutes across the whole of intake. Digital intake
    covers a subset of what manual intake covers, and that subset is where the operational cost sits.
- **Keywords to weave:** `digital patient intake`, `intake forms`, `patient intake forms` (this is
  the only section where the adjacent clinic-intake vocabulary belongs), `manual vs digital intake`
- **Sources:** none required.
- **Approved claims:** FX-006 (under 45 seconds), FX-007 (2 photos, front and side) if the digital
  definition needs the mechanics. Both are product-spec facts.
- **Boundary:** Do not define occupational health screening intake as a category. The hub owns that
  definition and its FAQ answer. Define the two *methods*, not the category.

### Section 3. Why the intake bottleneck is getting more expensive

- **Goal:** Establish the "why now" with a fresh figure, not a repeat of the hub's injury statistic.
- **Word count target:** 170
- **Must-cover:**
  - Hiring volume is the demand driver for pre-employment screening intake, and it draws on a fixed
    supply of appointment slots. Cite the BLS JOLTS hires level.
  - Multi-site and multi-vendor programs raise the cost of inconsistency, because records have to be
    comparable across locations before they are reviewable.
  - Documentation expectations have moved upstream: review teams expect structured records.
  - Adding clinic capacity does not address an intake problem.
- **Keywords to weave:** `occupational health screening`
- **Sources:** BLS Job Openings and Labor Turnover Summary, July 2026,
  `https://www.bls.gov/news.release/jolts.nr0.htm` (verified 2026-09-03: hires 5.1 million, hires
  rate 3.2 percent, "little changed" over the month). Cite the release by name inline with the anchor
  on the meaningful phrase.
- **Approved claims:** none.
- **Boundary:** Hiring volume is context for screening demand. Do not connect body data to hiring
  volume in a way that implies body data informs hiring. Do not re-cite the hub's BLS injury figure.

### Section 4. Occupational health intake, component by component

- **Goal:** The article's central mechanism. Split intake into its parts and mark which parts a
  digital channel can carry and which stay manual or clinician-led. This is what makes the comparison
  honest instead of a sweep.
- **Word count target:** 260
- **Must-cover:**
  - Four components: health history and symptom questionnaire; body measurement and BMI inputs;
    modality-specific testing (drug, vision, hearing, functional); the examination and clinician
    review itself.
  - Only two of the four are candidates for a remote digital channel: the questionnaire and the body
    measurement. Say so plainly.
  - Why manual body measurement varies: it is technique-, landmark- and team-dependent, which is why
    national measurement protocols specify posture, tape position, tension and a recorder role in
    detail. Ground this in the NHANES procedures manual.
  - The regulator already treats the questionnaire as a routed document, not a clinic activity:
    OSHA's mandatory respirator medical evaluation questionnaire must be answerable during working
    hours or at a time and place convenient to the employee, the employer must not review the
    answers, and the employer must be told how to route it to the reviewing health care professional.
    This is the strongest fresh point in the article. A digital intake channel is one way to meet that
    routing and confidentiality posture.
- **Keywords to weave:** `occupational health intake`, `occupational health intake process`,
  `digital occupational health intake`
- **Sources:**
  - Appendix C to § 1910.134, *OSHA Respirator Medical Evaluation Questionnaire (Mandatory)*,
    `https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.134AppC` (verified
    2026-09-03; the confidentiality, timing and routing language quoted above is on that page).
  - CDC / NCHS, *NHANES Anthropometry Procedures Manual*, 2021,
    `https://wwwn.cdc.gov/nchs/data/nhanes/public/2021/manuals/2021-Anthropometry-Procedures-Manual-508.pdf`
    — **open the PDF and quote the protocol text directly.** The URL is confirmed live; the specific
    passages were not machine-readable at plan stage, so do not write from a paraphrase.
- **Approved claims:** FX-008 (80+ body measurements), FX-009 (body composition outputs: BMI, BMR,
  body fat percentage, lean mass, fat mass) where the body-measurement component needs defining.
- **Boundary:** Naming the OSHA respirator questionnaire is a fact about intake mechanics. It is not
  a claim that FitXpress administers that questionnaire, satisfies 1910.134, or supports respirator
  clearance. State the routing principle, then state that the clearance determination and the
  medical evaluation stay with the reviewing health care professional.

### Section 5. Manual and digital intake compared, dimension by dimension

- **Goal:** The comparison table, and a reading of it that names where each method wins. Core of the
  article.
- **Word count target:** 280
- **Must-cover:**
  - A clean Markdown table, two method columns, one dimension per row. Dimensions: where the step
    happens; who performs the body measurement; consistency across staff, sites and vendors; record
    format and time stamping; confidentiality routing of the questionnaire; time consumed inside the
    appointment slot; what the method can capture; access requirement for the candidate or employee;
    setup and change-management cost.
  - **Digital does not win every row, and the table must show that.** Manual intake wins on scope
    (it carries the whole of intake, including the parts no remote channel can), on access (no
    smartphone or network dependency), and on setup cost (no integration, no configuration, no
    change management).
  - A short reading of the table in prose: the dimensions digital improves are the ones that produce
    rescreens and multi-site inconsistency; the dimensions manual holds are scope, access and cost of
    change.
  - One sentence stating that the row-by-row differences are what the decision in Section 9 turns on.
- **Keywords to weave:** `manual vs digital intake` (this section carries the H2 occurrence of the
  primary keyword), `occupational health screening`
- **Sources:** the same OSHA Appendix C page for the confidentiality-routing row. No new source
  needed for the other rows.
- **Approved claims:** FX-006, FX-007, FX-008 for the digital column's mechanics.
  **No accuracy or repeatability figure in this section.** It belongs in Section 7 with its
  conditions and its link.
- **Boundary:** No row and no sentence may claim digital intake is more accurate than manual
  measurement. Our own accuracy figure is measured *against* expert manual measurement as the
  reference, so "more accurate than manual" is not a claim we hold. The consistency row is about
  repeatability and standardisation, and it stays qualitative here. Do not mention ISO 8559 anywhere
  in this article.

### Section 6. Where FitXpress fits in a digital intake workflow

- **Goal:** Position the product against the two components identified in Section 4, briefly, without
  rebuilding the hub's workflow walk-through.
- **Word count target:** 190
- **Must-cover:**
  - FitXpress covers one component: remote, pre-appointment body measurement capture. Say which
    component, and say that the questionnaire, the testing and the examination sit elsewhere in the
    program's stack.
  - The three properties that matter here: capture happens before the appointment on the candidate's
    or employee's own device; outputs are structured and time-stamped; the compliance posture holds
    at procurement.
  - Down-link to `https://3dlook.ai/` on a descriptive anchor.
- **Keywords to weave:** `digital occupational health intake`
- **Sources:** none required.
- **Approved claims:** FX-006, FX-007, FX-008, FX-009, FX-014 (HIPAA maintained; GDPR principles for
  EU processing; AWS S3 SSE-S3 at rest, TLS in transit; no personal identifiers processed; photos
  deleted immediately or within 30 days per client policy).
- **Boundary:** Position FitXpress as a remote intake and documentation layer that supports clinician
  review. Never as a clearance, eligibility or fitness-for-duty input. Do not write "speeds clearance
  decisions": if time-to-decision is mentioned, the sentence says the path to the determination is
  shorter and the determination itself stays with the licensed provider and employer policy. Do not
  restate the hub's five-step implementation sequence.

### Section 7. What improves operationally, and what the evidence behind it actually says

- **Goal:** The genuinely open ground. The hub never states an accuracy or repeatability figure; this
  section introduces repeatability as the property that matters for the manual-vs-digital comparison,
  with its conditions attached.
- **Word count target:** 220
- **Must-cover:**
  - Frame it as the reframe move: the buyer's question is not "how accurate is it" but "accurate
    enough for which decision", and for intake documentation the decision is whether records are
    comparable across staff, sites and time points.
  - Repeatability, FX-003, with its conditions: internal repeatability testing on a real-world
    customer dataset, five repeated scans per participant, and the finding stated in the approved
    words. Copy the sentence from `accuracy-formulations.md` §1.2 verbatim.
  - Accuracy, FX-001, with its reference stated in the same breath: the figure is measured against
    expert pattern-maker manual measurement, over a defined population scope, and it varies by body
    part. Copy from `accuracy-formulations.md` §1.1 verbatim.
  - What that combination means for this comparison, stated carefully: expert manual measurement is
    the reference the figure is measured against, so the case for digital intake rests on consistency
    across repeats and across sites, not on beating a tape measure.
  - The operational outcomes, hedged: measurement time moves out of the appointment slot; records
    arrive before review; missing and inconsistent fields fall, which is the common cause of
    rescreens.
  - **The trust link goes in the paragraph that carries the figure**, not in a further-reading list.
- **Keywords to weave:** `occupational health screening`
- **Sources:** `https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/`
- **Approved claims:** FX-003 (primary here), FX-001 (secondary, with its reference).
- **Boundary:** Hard constraints, all three checked by the linter or the editor:
  1. **Never combine the two benchmarks.** The ISO 8559 figure does not appear in this article at
     all.
  2. **FX-004, "95%+ overall repeatability consistency", is internal and is not published.** The live
     framework article describes the same study and gives no such percentage. Use FX-003.
  3. No per-measurement figures. "Varying by body part" is the published level of detail; detailed
     methodology is available under NDA.
  Outcomes are stated as "can reduce" and "supports", never as guarantees. No claim that fewer
  rescreens are guaranteed.

### Section 8. What FitXpress does not do

- **Goal:** The boundary, stated once and cleanly, in the section §12 reserves for it.
- **Word count target:** 130
- **Must-cover:**
  - A two-column table: what the intake layer supports, and what it does not do.
  - Does not: diagnose; perform or replace the occupational health examination; make
    fitness-for-duty or clearance determinations; inform hiring or employment decisions; replace
    clinician review or employer policy; guarantee compliance.
  - One closing sentence on compliance framing: evaluation runs on data-privacy and recordkeeping
    frameworks, and the regulatory classification of any deployment depends on intended use,
    deployment context and jurisdiction.
- **Keywords to weave:** none forced.
- **Sources:** none.
- **Approved claims:** none. FX-014 only if the compliance sentence needs a specific.
- **Boundary:** This is the section where the licensed sentence "It is not positioned as a medical
  device." belongs, if it was not already used in Section 1. Use it once in the article, not twice.
  Guardrail M2: state each boundary once, do not chain negatives inside a sentence. The hub's
  does-and-does-not table exists; write this one shorter and pointed at the comparison, not as a
  copy.

### Section 9. A decision framework: which intake method fits which program

- **Goal:** The second core block. Tell a buyer when manual intake is still the right answer. This is
  the section that earns the article's credibility.
- **Word count target:** 260
- **Must-cover:**
  - **When manual intake remains the right choice:** single-site or low-volume programs where the
    slot is not the constraint; populations without reliable smartphone or network access; intake
    dominated by history, symptom and functional content; workflows where the measurement is part of
    the examination itself; programs with no downstream system able to receive structured records.
  - **When a digital intake channel earns its cost:** high candidate or employee volume against fixed
    appointment capacity; multiple sites, clinics or vendor partners needing comparable records;
    documented rescreen and rework volume traceable to missing or inconsistent intake data;
    documentation that has to hold up across reporting periods.
  - **The realistic answer is hybrid, and say so as a positive:** the questionnaire and the body
    measurement move to a remote channel, the testing and the examination stay in the clinic, and the
    program decides the split by component rather than wholesale.
  - Frame the choice as a set of conditions on the program, using "depends on" and "varies by".
- **Keywords to weave:** `manual vs digital intake`
- **Sources:** EEOC enforcement guidance,
  `https://www.eeoc.gov/laws/guidance/enforcement-guidance-preemployment-disability-related-questions-and-medical`,
  for the one sentence placing pre-employment medical examination content after a conditional offer.
- **Boundary:** The framework decides an *intake method*. It never decides a candidate, an employee,
  a clearance or an eligibility. The EEOC citation marks the post-offer boundary the workflow sits
  inside; do not restate the hub's fuller EEOC passage, and do not frame anything as a pre-offer
  medical examination.
- **Approved claims:** none.

### Section 10. Buyer fit and the questions to ask before switching

- **Goal:** Who gets the most value from the switch, and what an evaluation should establish. Merges
  §12 items 9 and 10.
- **Word count target:** 190
- **Must-cover:**
  - Which buyer profile the switch pays back fastest for, in one or two sentences each, and route
    readers to the hub for the full roster: occupational health providers and clinic networks;
    workforce screening vendors running multi-employer contracts; multi-site employers. Name
    workers' compensation and absence administrators in a single clause only.
  - Evaluation questions worth answering before a pilot: which intake components move; what the
    current rescreen rate is and what causes it; whether the downstream system can receive structured
    records; what happens for a candidate who cannot complete a remote capture; how repeatability was
    measured and over how many repeated scans.
  - Up-link to the hub on the buyer-profile phrase.
- **Keywords to weave:** `occupational health employee screening tool`, `occupational health
  screening services`
- **Sources:** the live hub.
- **Approved claims:** none.
- **Boundary:** **Keep workers' compensation and return-to-work thin.** Two unwritten sibling rows
  own that ground: row 213 (Return-to-Work Screening Documentation, P0, distinct workers'-comp and
  absence buyer) and row 214 (Remote Intake for Workers' Compensation, P1). No return-to-work delay
  framing, no workers'-comp program-ops detail, no baseline-before-injury argument. One clause and a
  link up.

### Section 11. Frequently asked questions

- **Goal:** GEO/AEO coverage of questions the live hub does not answer. Answers 2 to 5 sentences.
- **Word count target:** 300
- **Must-cover:** These six. **None restates the hub's seven FAQ questions or its five inline bolded
  Q&As**, which are listed in the context pack under `hub_inventory`. Checked one by one in
  `plan-audit.md`.
  1. **Is digital intake more accurate than manual tape measurement in occupational health
     screening?** The honest answer, and the reframe. Our accuracy figure is measured against expert
     manual measurement as the reference, so the useful question is whether the expected error is
     acceptable for the decision the record supports, and whether repeated measurements are
     comparable. Carries FX-003 with its condition and the link to the framework article.
  2. **Which parts of occupational health intake cannot be moved to a digital channel?** History and
     symptom review that needs clinical follow-up, modality-specific testing, functional assessment,
     and the examination itself.
  3. **What happens if a candidate cannot complete a remote scan?** The program keeps the manual path
     as the fallback, and the answer says plainly that a digital intake channel does not remove the
     need for one. Access varies by workforce and by role.
  4. **Does moving intake to a digital channel change the post-offer boundary for pre-employment
     screening?** No. The boundary is set by the timing and content of the medical examination, not by
     the channel the intake data arrives through. Cite EEOC guidance.
  5. **Can digital intake records be compared against measurements taken manually at an earlier
     appointment?** Carefully, and only where the program documents both. The two references differ,
     so a mixed-method series is weaker than a consistent one, which is the argument for
     standardising the method rather than the record.
  6. **What should a program measure to know whether digital intake worked?** Rescreen rate and its
     causes, intake completeness at the point of review, measurement time inside the appointment
     slot, and record comparability across sites.
- **Keywords to weave:** `manual intake vs digital intake in occupational health screening` and the
  other unmeasured long tails belong in these question phrasings.
- **Sources:** EEOC guidance (Q4); `https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/`
  (Q1).
- **Approved claims:** FX-003 in Q1 only.
- **Boundary:** Q1 must not turn into an accuracy sales pitch, and must not combine benchmarks. Q4
  must not read as legal advice: state what the boundary is set by, and leave the determination with
  the employer's counsel and the licensed provider. No question and no answer may touch clearance
  decisioning.

### Section 12. Next steps

- **Goal:** A CTA matched to comparison intent, which leans MOFU to BOFU.
- **Word count target:** 60
- **Must-cover:**
  - An evaluation-framed direct CTA, per guidelines §15 for BOFU: compare the two intake models
    against the program's own throughput and rescreen numbers, then talk to 3DLOOK about the
    workflow, with the demo link.
  - Link the demo on a descriptive anchor: `https://3dlook.ai/pricing/#bd-modal-personalized`.
  - One CTA only. No newsletter block, no mid-body banner.
- **Keywords to weave:** none forced.
- **Sources:** none.
- **Approved claims:** none.
- **Boundary:** Demo only. This is a compliance-buyer audience, so no self-serve trial link. Never
  imply the demo evaluates or clears anyone.

## Article meta

- **Estimated words:** 2,500 prose words

| Section | Words |
|---|---|
| 1. Intake step, not the examination | 200 |
| 2. Short answer: what each method covers | 240 |
| 3. Why the bottleneck is getting more expensive | 170 |
| 4. Intake, component by component | 260 |
| 5. Compared, dimension by dimension | 280 |
| 6. Where FitXpress fits | 190 |
| 7. What improves, and what the evidence says | 220 |
| 8. What FitXpress does not do | 130 |
| 9. Decision framework | 260 |
| 10. Buyer fit and questions to ask | 190 |
| 11. FAQ | 300 |
| 12. Next steps | 60 |
| **Total** | **2,500** |

- **Estimated read time:** 10 minutes
- **Tables:** two required. The method comparison in Section 5, the does-and-does-not table in
  Section 8. Clean Markdown, never a tab-exported blob.
- **CTA placement:** Section 12 only. One CTA.
- **Internal links** (5 distinct targets, 7 placements, inside the style guide's 4 to 8 range; every
  anchor descriptive):

| Direction | Target | Placement |
|---|---|---|
| up | `https://3dlook.ai/content-hub/occupational-health-screening-software/` | Sections 1, 10 |
| trust | `https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/` | Section 7 (in the paragraph carrying the figure), FAQ Q1 |
| side | Data, Privacy, Security & Regulatory FAQ | **Unpublished placeholder.** Draft at `workspace/seo/articles/2026-07-14-fitxpress-privacy-security-faq/`. Plan the anchor in Section 6 next to FX-014 and leave the URL as a placeholder for the publisher to resolve or drop. |
| down | `https://3dlook.ai/` | Section 6 |
| down / CTA | `https://3dlook.ai/pricing/#bd-modal-personalized` | Section 12 |

- **Sideways note:** guidelines §11 permits this vertical to link sideways to the privacy FAQ and the
  accuracy framework only. Both sibling cluster articles (rows 213, 214) are unwritten, so there is
  no third sideways target to add today. This is the permitted set, not a shortcut.

## Writing constraints carried into the draft

- **Hard bans the writer holds in mind** (the full pass is the editor's): no em dash anywhere; no
  `leverage`, `utilize`, `harness`, `robust`, `seamless`, `comprehensive`, `delve`, metaphorical
  `navigate`, `unlock`, `revolutionary`, `game-changing`, `cutting-edge`; no `by hand`, `let`, `plus`
  as a connector, `so` introducing a benefit, `objective` about our own outputs; no `this article`
  outside the scope note; no "positioned as" except the one licensed medical-device sentence.
- **Abbreviations:** BMI, CEO, UK, US and EU are used bare. Everything else expands at first use,
  including regulators (OSHA, EEOC, ADA, HIPAA, GDPR).
- **No named competitors.** Compare method to method. `competitors.md` has no vendor playing in
  occupational health intake, so there is nothing to name even if we wanted to.
- **Author:** Assel Sekerova.
- **No pricing figures.**
