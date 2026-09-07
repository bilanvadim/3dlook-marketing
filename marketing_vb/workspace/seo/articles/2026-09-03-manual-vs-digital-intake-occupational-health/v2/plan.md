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
revision: 2
revised: 2026-09-04
revision_reason: Review 1 (external stakeholder), second pass against the VERBATIM review. Rev 1 was planned against a lossy WebFetch reconstruction; the Drive text surfaced a missing workflow-comparison section, the reviewer's own metrics table, four more flagged product statements, and the whole "What should be preserved" list. See review-1.md (now verbatim) and review-1-decisions.md §0. Checkpoint 1 stays approved; a revision cycle flows straight to checkpoint 2 per .claude/commands/new-article.md.
target_words: 2050
author: Assel Sekerova
created: 2026-09-03
audit: plan-audit.md
review_package: checkpoint-1-review-package.md
review: review-1.md
review_decisions: review-1-decisions.md
context_pack: workspace/seo/_context-packs/2026-09-03-manual-vs-digital-intake-occupational-health.yaml
keywords_file: workspace/seo/_keywords/2026-09-03-manual-vs-digital-intake-occupational-health.yaml
---

# SEO Plan (rev 2) — Manual vs Digital Intake in Occupational Health Screening

> **This is the Review-1 revised plan.** The untouched checkpoint-1 plan is preserved at
> `v1/plan.md`. Read `review-1.md` and `review-1-decisions.md` alongside this file;
> `review-1-decisions.md` wins on any conflict with the review text. What
> changed in this revision, at a glance:
>
> - **Word budget 2,500 → 2,050** (band 1,742–2,357). Review target range 1,900–2,200.
> - **Section count 12 → 9 plus a short CTA.** Three hub-owned blocks removed (Review A1):
>   the full does/does-not-do table, the buyer-profile roster section, and the standalone
>   "why now" section that leaned on a US-economy hiring figure the hub already owns the
>   framing for. The FitXpress positioning is cut to one short section.
> - **"Intake" is split into three phases** (Review A2): pre-appointment intake · on-site
>   screening · clinical review. A remote channel reaches only the first.
> - **An explicit FitXpress-scope line moves into the Section 1 scope note** (Review A3).
> - **The comparison table is rebuilt** with the reviewer's hedged row wording and five new
>   rows (Review A4).
> - **Seven operational sentences are re-sourced, hedged, or cut** (Review A5), including one
>   verbatim replacement supplied by the reviewer.
> - **BLS/NHANES/OSHA/EEOC sourcing is narrowed to what each source actually supports**
>   (Review A6). The BLS hiring figure is removed outright.
> - **The compliance paragraph is stated with `compliance.md` precision** and the unpublished
>   Privacy-FAQ side-link placeholder is dropped, not carried into the text (Review A7 +
>   decisions §B).
> - **FAQ 6 → 4** focused questions; an evaluation-metrics table replaces the old buyer-fit
>   question list.

> **Rev 2 — what the verbatim review changed on top of rev 1.** Rev 1 was planned against a
> WebFetch reconstruction of the review, because that session had no Drive access. The verbatim
> text is now in `review-1.md`, and it carried five things the reconstruction did not:
>
> - **A whole missing section.** The reviewer's brief-compliance table grades *Workflow
>   differences* as **Partial** and asks for a concise step-by-step side-by-side, supplying the
>   table verbatim. It is now **Section 5, "How the workflows differ"** — new in this revision.
> - **The evaluation-metrics table is the reviewer's own, eight rows**, not the five-row table
>   rev 1 invented. Their header is "What to establish before implementation". The rev-1 header,
>   "What it tells you", also carried a hard-banned `you`.
> - **Item 7 flags six product statements, not two.** Five are standing approved compliance
>   language and stay (with `compliance.md` precision); the sixth, *"the document reaches the
>   reviewer without passing through the employer"*, is our own inference from OSHA Appendix C,
>   is grounded in nothing, and is **cut**. Item 7 also says to stop listing the full
>   body-composition inventory, and that no draft-only placeholder may reach the CMS version.
> - **"What should be preserved" exists and names eight elements.** Rev 1 could not read it and
>   flagged it as an open risk. It is now `review-1-decisions.md` §F, and it is binding: the
>   **five implementation questions** it protects were cut to two in rev 1 and are restored in
>   Section 7.
> - **FitXpress moves late and merges.** The reviewer puts it at item 7 of nine as "two or three
>   concise paragraphs" retaining the repeatability statement and the accuracy-framework link.
>   Rev 1's Sections 5 and 6 are merged into **Section 8** and placed after the metrics, which is
>   what moves the article's centre of gravity from explaining the use case to comparing methods.
>
> Per-section budgets were rebalanced to absorb the new section and the merge: total ~2,160,
> inside the reviewer's 1,900–2,200 band.

## Content Strategy Fit (Phase 0)

Unchanged by Review 1 and not re-opened. Phase 0 was resolved against
`brand-assets/content-strategy/content-plan.md:212` and verified against the context pack.

- **Hub / cluster:** Occupational Health Screening (Hub 8) → Comparison
- **Action type:** `create-net-new` ("Net-new supporting"). Proceeds because the angle is a
  method-level comparison and a decision framework, distinct from the live hub, which owns the
  category, the buyer profiles and the FitXpress workflow.
- **Hub status:** live since 2026-07-10. Supporting articles are unblocked.
- **Cannibalization guardrail (row verbatim):** "Throughput, missing data, rescreens, multi-site
  consistency. No medical/clearance claims." **Review 1 A1 is an enforcement of this same rule**
  (see `review-1-decisions.md` §A and `content-strategy-guidelines.md` §5): the buyer-profile
  roster, the full does/does-not-do table, the category definition and the product workflow
  belong to the hub, and this revision removes the places where the draft had restated them.
- **Vertical boundary (guidelines §9):** intake and documentation only. No sentence of the shape
  "clears employees for duty". The messaging line "speed clearance decisions" means shortening
  time-to-decision and must not appear as a capability claim.
- **Internal links planned:** up → the live Hub-8 hub (Sections 1 and 8) · trust → the accuracy
  framework, in the paragraph carrying the figure (Section 6) and FAQ Q1 · down → the FitXpress
  parent homepage (Section 5) and the demo modal (CTA). **Sideways is dropped from the text:**
  the only permitted sideways target (the Privacy & Regulatory FAQ) is still unpublished, and per
  `review-1-decisions.md` §B the compliance paragraph is kept short and precise rather than
  linked to a draft that is not live. The link-direction gate does not require it (the pack holds
  the sideways and down targets as prose, not URLs).

## Keyword Analysis

Unchanged. No measured, in-vertical, un-owned head term exists for this article. It is a GEO /
answer-engine and long-tail procurement-question play. The primary keyword `manual vs digital
intake` sits in the H1, the first paragraph, and one H2 (Section 4). `occupational health
screening` (250/mo, KD 6) stays with the hub and is used only as vertical context. Full working:
`plan-audit.md` and the keywords file.

## Recommended Title

**H1 (unchanged):** Manual vs Digital Intake in Occupational Health Screening: Which Method Fits
Which Workflow

Carries the primary keyword in the first five words, names the vertical so the page reads as
occupational-health-scoped, and the closing clause is the promise the article keeps. Checkpoint 1
approved this title; the revision does not touch it.

## Article Outline (rev 2 — 9 sections + CTA)

Comparison shape (Type C): quick-answer block near the top, a method-vs-method table, no clean
sweep. Model articles unchanged: `body-scanning-technology-comparison.md` (comparison shape) and
`clinical-trials-anthropometric-measurement.md` (sensitive-vertical scope note and boundary
discipline). Do not copy accuracy figures from either.

### Section 1. The intake step is where screening programs lose time

- **Goal:** Reader recognises the problem within two sentences and knows the page's scope before
  reading on.
- **Words:** ~230
- **Must-cover:**
  - Open on the operational fact, no runway: the questionnaire-and-measurement step sits inside a
    capacity-constrained appointment slot.
  - Name the four costs the strategy row owns: throughput, missing/incomplete data, rescreens,
    multi-site inconsistency. **Review A5-1:** do NOT assert "programs report all four" — state
    them as the costs that come out of the step, without a claim about what programs report.
  - **Review A5-2:** the "adding clinic capacity" line is reframed from "moves none of them" to a
    reasoned statement — extra slots do not change the intake work that runs inside each slot, and
    whether capacity relieves the bottleneck depends on where the time is lost.
  - State what the page decides: which intake steps a remote channel can carry, and which programs
    gain enough to justify the change.
  - **Scope note early, italic blockquote. Non-negotiable.** **Review A3:** the note now leads
    with the explicit scope line — FitXpress provides the remote body-measurement component;
    questionnaire collection, testing, examination and clinical review remain in the customer's
    other systems. Then the boundary: no examinations, no fitness-for-duty or clearance
    determinations, not a basis for hiring/employment decisions, and the one licensed sentence
    "It is not positioned as a medical device." Use that sentence and nothing else with
    "positioned as".
  - Up-link to the hub on a meaningful anchor.
- **Keywords:** `manual vs digital intake` (H1 + first paragraph), `occupational health screening`
- **Approved claims:** none.

### Section 2. Short answer: what each intake method covers

- **Goal:** An answer-engine-extractable summary and clean definitions of the two methods.
- **Words:** ~230
- **Must-cover:**
  - Quick Answer Block, four to five bullets, one method or one verdict each.
  - Manual intake defined; digital intake defined (guided smartphone scan, two photos, under
    45 seconds).
  - **Review A5-3 and A5-4:** the "cost sits in the overlap" bullet is reframed from "the two that
    generate rescreens" to a mechanism statement — these two components are captured and
    transcribed under appointment-time pressure, which is what exposes them to missing or
    inconsistent fields, and an incomplete record can trigger a rescreen. No frequency claim, no
    "the common cause".
  - One honest verdict bullet: the two are not substitutes across the whole of intake.
- **Keywords:** `digital patient intake`, `intake forms`, `patient intake forms` (only here),
  `manual vs digital intake`
- **Approved claims:** FX-006 (under 45 s), FX-007 (2 photos, front + side).
- **Boundary:** define the two *methods*, not the category. The hub owns the category definition.

### Section 3. The three phases of occupational health intake

- **Goal:** The article's central mechanism, now **phase-split (Review A2)** instead of a flat
  four-item list. Mark which phase a remote channel can carry.
- **Words:** ~250
- **Must-cover:**
  - **Three phases:** (1) pre-appointment intake — history/symptom questionnaire, required
    documents, eligible body measurements; (2) on-site screening — equipment-based testing (drug,
    vision, hearing, functional) and the examination; (3) clinical review — the reviewing provider
    reads the record and, where the program calls for it, makes the determination. A remote
    channel reaches only phase 1, and inside it only the questionnaire and the body measurement.
  - **Workflow-diagram callout (Review: add one).** A `> **Figure 1.**` line describing the
    three-phase workflow with the pre-appointment phase marked as the remote-capable part.
  - **Review A6-NHANES:** the NHANES waist protocol is reframed. It illustrates the training,
    landmark identification and second-person quality check that standardized manual measurement
    requires — NOT clinic staffing capacity. Remove "a screening clinic is not staffed for that".
  - **Review A6-OSHA:** the OSHA respirator questionnaire is narrowed. It is a specific example of
    a confidentiality-routed intake document, NOT a general rule about how regulators treat all
    questionnaires. Say explicitly it is specific to respirator medical evaluations, then note the
    routing pattern a digital channel can meet.
  - FitXpress does not administer that questionnaire; the medical evaluation and the clearance
    determination stay with the reviewing health care professional.
  - The body-measurement output as structured figures.
- **Keywords:** `occupational health intake`, `occupational health intake process`,
  `digital occupational health intake`
- **Sources:** OSHA Appendix C (§1910.134); NHANES Anthropometry Procedures Manual (both already
  fetched/quoted in the v1 run — see `log.md`).
- **Approved claims:** FX-008 (80+ measurements), FX-009 (body composition outputs).

### Section 4. Manual vs digital intake, compared dimension by dimension

- **Goal:** The comparison table and a reading that names where each method wins. Core of the
  article. Carries the H2 occurrence of the primary keyword.
- **Words:** ~340
- **Must-cover:**
  - **Rebuilt table (Review A4).** Reviewer's hedged wording on six existing cells:
    - Manual setup cost: "Lower incremental implementation cost; continuing staff and
      administration requirements."
    - Digital consistency: "A standardized guided procedure, subject to capture quality and
      validation requirements."
    - Digital confidentiality routing: "Depends on permissions, system configuration and the
      program's data-handling design."
    - Manual record: "May require manual entry or scanning; structure depends on the receiving
      system."
    - Digital record: "Can arrive in a structured format when the integration supports it."
    - Manual access: "Attendance and completion of the required on-site intake steps."
  - **Five new rows (Review A4):** ongoing labor, exception handling, integration dependency,
    fallback availability, data-entry correction. Keep cells terse and free of any number.
  - **Manual must win at least three dimensions (no clean sweep):** scope, access (no
    device/network dependency), and it is itself the fallback. **Review item 2:** the scope row
    may no longer read "every component of intake" — that phrasing is one of the confusing
    statements the reviewer quoted, and it contradicts the three-phase split in Section 3. Write
    it against the phases: manual/on-site intake is the only path that needs no remote channel at
    all, because the person is already present for phases 2 and 3.
  - **Review A5-5:** the reading paragraph uses the reviewer's verbatim replacement — "Moving
    eligible intake steps before the appointment can reduce in-appointment collection and
    transcription. The effect depends on completion rates, fallback volume, integration quality
    and existing rescreen causes." Do not paraphrase it.
  - One sentence stating the rows are what the decision framework turns on.
- **Keywords:** `manual vs digital intake`, `occupational health screening`
- **Approved claims:** none in the table cells (no figure). Mechanics of the digital column are
  described qualitatively; the 45-seconds/two-photos facts live in Sections 2 and 5.
- **Boundary:** no row may claim digital intake is more accurate than manual measurement (our
  accuracy figure is measured *against* expert manual measurement). Consistency row stays
  qualitative. No ISO 8559 anywhere.

### Section 5. How the workflows differ

- **Goal:** The concise step-by-step manual-versus-digital walk the reviewer graded *Partial*
  under "Workflow differences" and could not find anywhere in rev 0. Table only, no re-explaining.
- **Words:** ~120
- **Must-cover:**
  - **The reviewer supplied this table verbatim in `review-1.md` (Recommended structure, item 4).
    Ship it as written. Do not re-word the cells, do not add rows, do not add a third column.**

    | Manual/on-site intake | Structured pre-appointment intake |
    | :- | :- |
    | Forms completed at or around the appointment | Forms completed through the program's intake system |
    | Staff perform required measurements | Eligible measurements captured remotely |
    | Information is entered or transcribed | Structured data is validated and transferred |
    | Missing items are handled during or after the visit | Exceptions are identified before the visit |
    | Tests and examination follow | Tests and examination remain on site |

  - One lead-in sentence and one closing sentence, no more. The closing sentence names the row
    that carries the operational difference: exceptions surface before the visit instead of
    during it. State it as what the structured path makes possible, not as a measured outcome
    (Review item 5 governs).
- **Keywords:** `digital occupational health intake`
- **Approved claims:** none. No figure belongs in this section.
- **Boundary:** the last row is the boundary — tests and examination stay on site under both
  models. Nothing here may imply a remote channel reaches phase 2 or phase 3.

### Section 6. A decision framework: which intake method fits which program

- **Goal:** Tell a buyer when manual intake is still right. The section that earns credibility.
- **Words:** ~235
- **Must-cover:**
  - When manual intake remains right: single-site/low-volume; populations without reliable
    device/network access; intake dominated by history/symptom/functional content; measurement
    that is part of the examination; no downstream system for a structured record.
  - When a digital channel earns its cost: high volume against fixed capacity; several sites or
    vendor partners needing comparable records; documented rescreen volume traceable to
    missing/inconsistent data; documentation that holds across reporting periods.
  - The realistic answer is hybrid, stated as a positive; the split is decided component by
    component.
  - **Review A6-EEOC:** the EEOC boundary is labelled US-specific. "In the US" up front, and an
    explicit line that other jurisdictions set their own timing. Then "choosing between manual vs
    digital intake decides a method; it never decides a candidate."
- **Keywords:** `manual vs digital intake`
- **Sources:** EEOC enforcement guidance.
- **Approved claims:** none.
- **Boundary:** the framework decides a method, never a candidate, a clearance or an eligibility.
  No pre-offer medical examination framing.

### Section 7. How to evaluate the change

- **Goal:** Replaces the old buyer-fit section (Review item 1 removed the buyer-profile roster).
  The evaluation-metrics table the reviewer asked to promote out of the FAQ, plus the five
  implementation questions the reviewer's "What should be preserved" list protects.
- **Words:** ~220
- **Must-cover:**
  - One lead-in sentence: each metric needs a baseline taken before the pilot.
  - **The reviewer supplied this table verbatim in `review-1.md` (Recommended structure, item 6).
    Ship it as written.** It replaces the five-row "what it tells you" table drafted against the
    reconstruction — which also carried a hard-banned `you` in its header.

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

  - **The five implementation questions, all five (protected by Review "What should be
    preserved", item 6).** Rev 1 kept two of them and dropped three; restore the set as a short
    list: which intake steps actually move to the remote channel and which stay on site; what the
    current rescreen rate is and what causes it; whether the downstream system can receive a
    structured record or whether someone will retype it; what the documented path is for a person
    who cannot complete a remote capture; how repeatability was measured, over how many repeated
    scans, and against which reference.
  - The last question is the diligence question worth handing any vendor, including this one. Say
    so in one clause.
  - **Hub owns the buyer roster.** One clause pointing up to the hub for which buyer profiles gain
    most and in what order. Do not restate the roster here.
- **Keywords:** `occupational health employee screening tool`, `occupational health screening
  services`
- **Sources:** the live hub (up-link).
- **Approved claims:** none.

### Section 8. Where FitXpress fits

- **Goal:** Position the product once, late, and briefly — after the buyer has the comparison, the
  workflow split and the metrics. **This section merges rev 1's Sections 5 and 6.** The reviewer's
  recommended structure puts FitXpress at item 7 and asks for "two or three concise paragraphs"
  that "retain the repeatability statement and accuracy-framework link" and "state clearly what
  remains outside FitXpress" — that is one section, not two, and the late placement is what moves
  the article's centre of gravity from explaining the use case to helping a buyer compare.
- **Words:** ~270
- **Must-cover:**
  - *Paragraph 1 — scope.* FitXpress covers one part of phase 1: remote, pre-appointment
    body-measurement capture. Questionnaire collection, modality-specific testing, examination and
    clinical review sit elsewhere in the program's stack. Pre-appointment capture on the person's
    own device, two photos, under 45 seconds. Structured, time-stamped output.
    **Review item 7: cut the body-composition inventory.** Rev 1 still lists "80+ body measurements
    along with BMI, basal metabolic rate, body fat percentage, lean mass and fat mass" — name only
    the outputs the intake workflow consumes and drop the rest. Removing "basal metabolic rate"
    also removes the abbreviation-expansion problem logged against rev 0.
  - *Paragraph 2 — the evidence, reframed.* Not "how accurate" but "accurate enough for which
    decision"; for intake documentation the decision is whether records stay comparable across
    staff, sites and time. Repeatability, FX-003, verbatim from `accuracy-formulations.md` §1.2,
    with its conditions; the trust link to the framework goes in this paragraph. Accuracy, FX-001,
    verbatim from §1.1, with its reference stated in the same breath. What that means for the
    comparison: expert manual measurement is the reference, so the case for a digital channel rests
    on consistency across repeats and sites, not on beating a tape.
    **Review item 5, claim 7:** a structured, time-stamped record is easier to compare, but
    structure alone does not ensure comparability or compliance; that depends on the capture method
    and the receiving system.
  - *Paragraph 3 — compliance and boundary, short.* **Review item 7 + decisions §B:** state
    compliance with `compliance.md` precision — HIPAA safeguards in US healthcare contexts, follows
    GDPR principles for EU processing, AWS S3 SSE-S3 at rest and TLS in transit, no personal
    identifiers processed, photos deleted immediately after processing or within 30 days with the
    window set by client policy. **Drop the unpublished Privacy-FAQ side-link sentence and its
    HTML-comment placeholder entirely** — a draft-only placeholder must not reach the CMS version.
    Then the boundary line: a remote intake and documentation layer that supports clinician review;
    it is not a clearance, eligibility or fitness-for-duty input (two sentences, recommended-form
    first, so it is not a corrective negation). Fold in the closing line: compliance evaluation runs
    on data-privacy and recordkeeping frameworks, and the regulatory classification of any
    deployment depends on intended use, deployment context and jurisdiction.
  - Down-link to `https://3dlook.ai/`.
- **Keywords:** `digital occupational health intake`, `occupational health screening`
- **Sources:** `https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/`
- **Approved claims:** FX-006, FX-007, FX-014, FX-003 (primary), FX-001 (secondary, with reference).
- **Boundary:** never combine the two benchmarks; FX-004 is internal, not published; no
  per-measurement figures; outcomes stated as "can", never guaranteed. No does/does-not-do table —
  the hub owns it (Review item 1).

### Section 9. Frequently asked questions

- **Goal:** GEO/AEO coverage of questions the hub does not answer. **Four** questions
  (Review: down from six). Answers 2–5 sentences. None restates the hub's FAQ or inline Q&As.
- **Words:** ~210
- **The four:**
  1. Is digital intake more accurate than manual tape measurement in occupational health
     screening? The reframe. FX-003 with its condition and the framework link.
  2. Which parts of occupational health intake cannot be moved to a digital channel?
  3. What happens if a candidate cannot complete a remote scan? (fallback)
  4. Does moving intake to a digital channel change the post-offer boundary for pre-employment
     screening? EEOC, labelled US-specific.
  - Dropped from v1: the mixed-method-comparison Q and the "what to measure" Q (the latter is now
    the Section 8 metrics table).
- **Keywords:** the unmeasured long tails belong in these question phrasings.
- **Sources:** EEOC (Q4); accuracy framework (Q1).
- **Approved claims:** FX-003 in Q1 only.
- **Boundary:** Q1 no accuracy sales pitch, no combined benchmarks. Q4 not legal advice.

### Next steps (CTA)

- **Goal:** One CTA, comparison intent, MOFU-to-BOFU.
- **Words:** ~55
- **Must-cover:** evaluation-framed direct CTA — run the two models against the program's own
  throughput and rescreen numbers, then talk to 3DLOOK, demo link
  `https://3dlook.ai/pricing/#bd-modal-personalized`. One CTA only.

## Article meta (rev 2)

- **Estimated words:** 2,050 prose words (band 1,742–2,357; review target 1,900–2,200)

| Section | Words |
|---|---|
| 1. Intake step | 230 |
| 2. Short answer | 230 |
| 3. Three phases of intake | 290 |
| 4. Compared, dimension by dimension | 360 |
| 5. Where FitXpress fits | 190 |
| 6. What the evidence supports | 230 |
| 7. Decision framework | 250 |
| 8. How to evaluate the change | 180 |
| 9. FAQ | 230 |
| Next steps | 55 |
| **Total** | **2,045** |

- **Tables:** two. The method comparison in Section 4 (rebuilt per A4), the evaluation-metrics
  table in Section 8. The old does/does-not-do table is removed (A1).
- **Callout:** one workflow-diagram callout in Section 3.
- **CTA placement:** the closing Next steps only. One CTA.
- **Internal links** (four directions covered; the pack requires up and trust as URLs, holds
  sideways and down as prose):

| Direction | Target | Placement |
|---|---|---|
| up | `https://3dlook.ai/content-hub/occupational-health-screening-software/` | Sections 1, 8 |
| trust | `https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/` | Section 6 (paragraph with the figure), FAQ Q1 |
| down | `https://3dlook.ai/` | Section 5 |
| down / CTA | `https://3dlook.ai/pricing/#bd-modal-personalized` | Next steps |

- **Sideways link removed from the text this revision** (A7 + decisions §B): the Privacy &
  Regulatory FAQ is unpublished. A `log.md` note records the trim-to-link for when it ships.

## Writing constraints carried into the draft

- Hard bans the writer holds in mind (full pass is the editor's): no em dash anywhere; no
  `leverage`, `utilize`, `harness`, `robust`, `seamless`, `comprehensive`, `delve`, metaphorical
  `navigate`, `unlock`, `revolutionary`, `game-changing`, `cutting-edge`; no `by hand`, `let`,
  `plus` as a connector, `so` introducing a benefit, `objective` about our own outputs; no
  corrective negation "X, not Y"; no `this article` outside a scope note; no "positioned as"
  except the one licensed medical-device sentence.
- **Abbreviations:** BMI, US and EU bare; everything else expands at first use (OSHA, EEOC,
  NHANES, HIPAA, GDPR). "basal metabolic rate" written out, no "BMR" token.
- No named competitors. No pricing figures. Author: Assel Sekerova.
