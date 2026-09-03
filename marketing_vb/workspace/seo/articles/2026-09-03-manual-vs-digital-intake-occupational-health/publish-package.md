---
slug: 2026-09-03-manual-vs-digital-intake-occupational-health
product: fitxpress
status: ready_for_review
created: 2026-09-03
hub: Occupational Health Screening (Hub 8)
cluster: Comparison
action_type: create-net-new
author: Assel Sekerova
word_count: 2745
---

# Publish Package - 2026-09-03-manual-vs-digital-intake-occupational-health

## Meta

**Title:** Manual vs Digital Intake in Occupational Health Screening (57 chars)
**Description:** Manual vs digital intake, compared across nine dimensions of occupational health screening. See what moves to a remote channel, and when manual intake wins. (156 chars)
**Slug:** `manual-vs-digital-intake-occupational-health-screening`
**Category:** Content hub, FitXpress / Occupational Health (supporting comparison article under the Occupational Health Screening hub)

Brand suffix rule applied: the recommended title is 57 chars, so `| 3DLOOK` is not appended
(the rule allows it only when the title is 49 chars or shorter without it). Primary keyword
`manual vs digital intake` occupies the first 24 characters.

## SEO checklist

- [x] Primary keyword in H1, first paragraph, 1-2 H2. **Verified by script:** H1, first prose
      paragraph, and the Section 5 H2 "Manual vs digital intake, compared dimension by dimension".
      4 occurrences total.
- [x] Meta title 57 chars, under 60, primary keyword in the first half
- [x] Meta description 156 chars, inside 140-160, keyword once, does not repeat the title
- [x] Every figure traces to `approved_claims`. 10 claim markers across 7 ids
      (FX-001, FX-003, FX-006 x2, FX-007 x2, FX-008, FX-009, FX-014). `article_lint.py`
      claim-traceability gate passes in both directions. **FX-004 (`publishable: false`) is absent.**
- [x] No banned words. Pack `banned_words` and `banned_claims` gates both pass.
- [x] Word count 2,745 prose words against a 2,500 target: +9.8%, inside the +/-10% publisher band
      and inside the linter's +/-15% band
- [x] Intro hook in the first two sentences (keyword reframe, then the fixed appointment slot)
- [x] CTA in Section 12 only, one CTA, evaluation-then-direct shape for MOFU-to-BOFU comparison
      intent, demo modal rather than a self-serve trial (compliance-buyer audience)
- [x] No generic AI patterns. Detector `banned_phrasings`, `negative_parallelism`,
      `presumed_reaction`, `anthropomorphism` and triad checks all clean
- [x] Terminology guardrails. No em dash or en dash anywhere. No `objective` about our own output,
      no `the reader`, no `the following sections`, no `see below`, no `this article`, no `by hand`,
      no `let`, no `plus` as a connector, no `so` introducing a benefit. Two corrective negations
      found in the draft were rewritten in the edit pass.
- [x] Abbreviations (M1). HIPAA and GDPR expanded at first use; OSHA, EEOC and NHANES expanded at
      first use; basal metabolic rate written out; BMI, US and EU left bare per the commonly-known
      exception. Script gate `abbreviations (M1)` passes.
- [x] Medical framing. Section 1 scope note carries the licensed sentence verbatim: **"It is not
      positioned as a medical device."** `positioned as` appears nowhere else in the article.
      **Corrected 2026-09-03 after the run.** The run brief had instructed the direct form
      ("FitXpress is not a medical device.") and the writer followed it, correctly flagging the
      conflict. The brief was wrong: `CLAUDE.md` section 6 and section 15, `plan.md`, the context
      pack and the publisher checklist all prescribe the "positioned as" sentence, restored
      2026-09-02 by Review 1 and Vadim's call, and `detect-ai-tells.py` licenses it explicitly with
      the lookahead `(?!a\s+medical\s+device\b)` while telling the author to write that exact
      sentence. The brief's stated reason, a detector hard fail, does not exist.
      "Positioned as" appears nowhere else in the article, which is the stricter reading either way.
- [x] Links on meaningful anchor phrases, no bare URLs, canonical trailing slashes. External
      sources are a regulator, a national statistics office and a national health statistics
      agency. No vendor blogs.
- [x] **Detector actually run** (output pasted verbatim in the next block, not estimated)
- [x] Image / alt-text suggestions provided in this package

### Detector output, verbatim

```
$ python3 brand-assets/style-guides/scripts/detect-ai-tells.py \
    workspace/seo/articles/2026-09-03-manual-vs-digital-intake-occupational-health/final.md \
    --channel article --summary

SEO / blog article - en - 2946 words
AI density: 0.34/1000 (budget 6.0) -> low
VERDICT: CLEAN - check the positive side (voice, varied rhythm, a stated boundary) and ship.

TOP SOFT MARKERS:
  1x 'serve as' (L64)
```

`hard_fails`: none. `house_rule_violations`: none. `ai_density_per_1000_words`: 0.34.
`severity`: low. The single soft marker is "serve as a basis for hiring or employment decisions"
inside the scope note, which is the approved boundary phrasing and stays.

### article_lint.py output, verbatim

```
$ python3 scripts/article_lint.py \
    workspace/seo/articles/2026-09-03-manual-vs-digital-intake-occupational-health/final.md

[ok  ] hard bans (detect-ai-tells)      verdict CLEAN, ai_density 0.34, rhythm_variation 0.73
[ok  ] prose length                     prose words 2745 vs target 2500 (band 2125-2875)
[ok  ] claim traceability               claims_used FX-001 FX-003 FX-006 FX-007 FX-008 FX-009 FX-014
[ok  ] banned claims
[ok  ] superseded figures
[ok  ] internal links                   6 links, 4 distinct, directions {up 1, sideways 0, down 0, trust 1}
[ok  ] keyword placement                'manual vs digital intake', 4 occurrences, 12 H2s
[ok  ] abbreviations (M1)
[ok  ] accuracy discipline              figures present, links to framework True

VERDICT: PASS
```

Note on the link-direction counters: `sideways 0` and `down 0` are reporting artifacts, not
missing links. In the context pack those two keys hold prose explanations rather than URLs
(`sideways` records that no sibling cluster article is published yet, `down` records that no
occupational-health vertical page exists), so the gate has no URL to match and correctly does not
fail. The article does carry both down-links, `https://3dlook.ai/` in Section 6 and
`https://3dlook.ai/pricing/#bd-modal-personalized` in Section 12.

## Content strategy checklist

- [x] Bound to the right hub: Occupational Health Screening (Hub 8), Comparison cluster,
      `content-plan.md:212`
- [x] `action_type: create-net-new` respected. The hub is live since 2026-07-10 and the Hub-8
      preamble lifts the "no broad occupational health articles" block.
- [x] Does not duplicate `existing_urls`. The hub owns the category definition, the buyer-profile
      roster, the five-step implementation walk-through and the workflow-vs-workflow table. None of
      the four is restated. This page owns the method comparison and the choice between methods.
      The one figure family the hub never spends (accuracy and repeatability) is where Section 7
      goes, which is the open ground the audit identified.
- [x] Vertical boundary held. Intake and documentation only. No sentence of the shape "clears
      employees for duty". The messaging line "speed clearance decisions" is not used as a
      capability claim anywhere; Section 6 states instead that the determination stays with the
      licensed provider and employer policy. No hiring, eligibility, clearance, diagnosis or
      fitness-for-duty decisioning. Scope note sits in Section 1 as an italic blockquote.
- [x] Internal links, four directions: up to the Hub-8 hub (Sections 1 and 10), trust to the
      accuracy framework (Section 7 in the paragraph carrying the figure, and FAQ Q1), down to the
      FitXpress parent (Section 6) and the demo modal (Section 12). Sideways is the one permitted
      target that is still unpublished, carried as a placeholder (see Open items).
- [x] FAQ present, 6 questions, answers 3 to 5 sentences, GEO/AEO shaped. None restates the hub's
      7 FAQ questions or its 5 inline bolded Q&As.
- [x] "What FitXpress does not do" section present. No forbidden positioning claim.
- [x] No unsupported medical, legal, underwriting or employment claim. The OSHA and EEOC passages
      state what the regulator requires and leave the determination with the reviewing health care
      professional and the program's counsel. **Routing for legal or compliance review is still
      recommended** for the OSHA paragraph in Section 4 and FAQ Q4.
- [x] Owns one distinct search intent: method comparison and method choice for occupational health
      screening intake

**SEO checklist: 14/15 passed, 1 flagged for Vadim's ruling (medical framing wording).
Strategy checklist: 9/9 passed.** No item is a positioning, compliance or cannibalization failure,
so the publisher does not STOP; the flagged item is a wording decision that has flipped three
times and belongs with Vadim.

## Alt options

### Meta title variants

1. Manual vs Digital Intake in Occupational Health Screening (57 chars) - **recommended.** Keyword
   first, vertical named in full, no truncation risk in the mid-50s.
2. Manual vs Digital Intake in Occupational Health | 3DLOOK (56 chars) - carries the brand, drops
   "Screening", which is the word the vertical is actually searched with.
3. Manual vs Digital Intake: Occupational Health Screening (55 chars) - shortest of the three; the
   colon reads as a category label instead of a comparison and loses the "in" that makes the
   phrase read as a sentence.

### Meta description variants

1. Manual vs digital intake, compared across nine dimensions of occupational health screening. See
   what moves to a remote channel, and when manual intake wins. (156 chars) - **recommended.**
   Names the deliverable (nine dimensions), keeps the keyword once, and the second clause signals
   the article is not a clean sweep, which is what a comparison query wants.
2. Manual vs digital intake, compared on throughput, rescreens and multi-site consistency,
   including the programs where the manual path is still the right answer. (159 chars) - mirrors
   the strategy row's angle exactly; weaker as a click promise because it front-loads three nouns.
3. A method comparison for occupational health screening intake: what a remote channel can carry,
   what stays in the clinic, and how a program decides between them. (160 chars) - the clearest
   prose; drops the exact `manual vs digital intake` string, which is the string answer engines
   match a comparison query on.

## Image and alt-text suggestions

Two illustrations, both placed so they carry an argument rather than decorate it. No figure appears
in alt text, because alt text is published copy and a number there is a published claim.

1. After the Section 5 table. Two-column workflow diagram, manual intake path against digital
   intake path, with the appointment slot drawn as a fixed-width box in both.
   Alt: "Manual and digital occupational health intake workflows side by side, showing which steps
   sit inside the appointment slot."
2. After the Section 4 component list. Four-block diagram of the intake components with the two
   remote-capable blocks marked.
   Alt: "The four components of occupational health intake, with the questionnaire and body
   measurement marked as the two a remote channel can carry."

Design tokens from `DESIGN.md`: electric blue `#143DFF` for the digital path, navy `#050F40` for
the manual path, Satoshi throughout.

## Open items for Vadim

1. **Medical-framing wording — resolved in the text, still worth one ruling from you.** The
   article now carries the licensed "It is not positioned as a medical device.", matching every
   repo document. No action needed to publish. What is still open is the rule itself: this is the
   **third flip of one sentence** (2026-06-09 prescribed "positioned as" -> 2026-08-13 banned it ->
   2026-09-02 restored it), it lives in five files, and each flip has cost a correction pass on a
   live article. If the restored form is final, say so and it gets stated once as a licensed
   exception in `terminology-guardrails.md` rather than as a footnote in four other documents.
2. **Privacy and Regulatory FAQ is still unpublished.** It is one of only two trust assets the
   guidelines permit this vertical to link sideways to. Section 6 carries the anchor phrase
   "FitXpress privacy and regulatory FAQ" with an HTML-comment placeholder instead of a URL.
   Either the FAQ ships or the sentence is dropped at CMS entry. A second article now depends on it.
3. **P0 versus P1 — CLOSED 2026-09-03, no action needed.** The inventory was the wrong document and
   has been fixed: this row now sits in its P0 table, and the reconciliation turned out to cover
   **five of seven** open rows, not one (the whole open list sat under P1 regardless of the plan).
   Return-to-Work Screening Documentation is also P0 and is the next Hub 11 article. One thing found
   on the way that changes how these checks are done: `content-plan.md` was itself two months stale
   (`Last synced 2026-07-07`), and the live sheet had moved two clinical-trials rows P2 -> P1, so
   reconciling against the md alone got those two backwards before they were corrected. A weekly
   sync job (`scripts/content-plan-sync.py`, Mon 06:23 UTC) now reports this drift.
4. **No sibling to link sideways to.** Rows 213 through 220 are unwritten, so the sideways
   direction collapses onto the two permitted trust assets. Compliant, and thin. It resolves when
   row 213 ships.
5. **BLS figure provenance.** `bls.gov` returned HTTP 403 to this run, so the hires figure
   (5.1 million, 3.2 percent, July 2026 release) is carried from `plan-audit.md`, which fetched and
   verified it on 2026-09-03 with the sentence quoted verbatim. Worth one manual eyeball before
   publish, since it is the only external figure in the article.

## Article

# Manual vs Digital Intake in Occupational Health Screening: Which Method Fits Which Workflow

## The intake step is where screening programs lose time

Framed as manual vs digital intake, the question sounds like a software preference. Inside a screening program it is an operations question about a fixed appointment slot. A candidate completes a health questionnaire, a medical assistant takes body measurements with a tape, someone transcribes both into the screening record, and only then does the clinician have something to review. The examination is the part the schedule plans for. The intake around it is the part that runs long.

Four costs come out of that step, and screening programs report all four: throughput against fixed appointment capacity, missing or incomplete intake data, rescreens caused by records that arrive unusable, and documentation that fails to line up between sites or between vendor partners running one program. Adding clinic capacity moves none of them.

Two questions decide the method: which intake components a remote channel can actually carry, and which programs gain enough from moving them to justify the change. The category itself, including the buyer profiles and the workflow end to end, is covered in the [occupational health screening software hub](https://3dlook.ai/content-hub/occupational-health-screening-software/).

> ***Scope note.*** *FitXpress supports intake and documentation steps in occupational health screening programs. It does not perform medical examinations, make fitness-for-duty or clearance determinations, or serve as a basis for hiring or employment decisions. It is not positioned as a medical device. The determination stays with the licensed provider and with employer policy.*

## Short answer: what each intake method covers

- **Manual intake** means a written or paper health questionnaire, a staff-administered tape measurement, and transcription into the screening record, all at or around the appointment.
- **Digital intake** collects the same questionnaire content through a structured remote channel before the appointment, with body measurement captured by a guided smartphone scan from two photos in under 45 seconds. <!-- claim: FX-006 --> <!-- claim: FX-007 -->
- **The overlap is partial.** A remote channel can carry the questionnaire and the body measurement. Modality-specific testing and the examination stay in the clinic.
- **The operational cost sits inside that overlap.** The two components a remote channel can carry are also the two that generate rescreens and inconsistency across sites.
- **Neither method wins outright.** Manual intake carries the whole of intake and asks nothing of the candidate beyond turning up. Digital intake standardizes the part that repeats thousands of times a year.

Clinic software describes the same shift as digital patient intake: paper patient intake forms replaced by structured pre-visit capture. Occupational health carries one requirement on top of that, which is the confidentiality routing of the health questionnaire. Intake forms in this setting are documents with a designated reviewer, and that changes how a digital channel has to be configured.

## Why the intake bottleneck is getting more expensive

Hiring volume drives pre-employment screening demand, and it draws on a fixed supply of appointment slots. The [Job Openings and Labor Turnover Summary](https://www.bls.gov/news.release/jolts.nr0.htm) from the Bureau of Labor Statistics put hires at 5.1 million for the month at a hires rate of 3.2 percent, little changed from the month before. Steady hiring at that level means steady screening volume against clinic capacity that does not flex.

Multi-site and multi-vendor programs pay a second cost. A record has to be comparable across locations before it can be reviewed as one dataset, and comparability is a function of how the measurement was taken. Filing it in one system does not create it.

Documentation expectations have moved upstream as well. Review teams increasingly expect a structured record at the point of review instead of a file to be reconstructed afterwards. That expectation lands on the intake step.

## Occupational health intake, component by component

The occupational health intake process is four things, and treating it as one is what makes the comparison confusing.

1. The health history and symptom questionnaire.
2. Body measurement and BMI inputs.
3. Modality-specific testing: drug screening, vision, hearing, functional capacity.
4. The examination itself and the clinician review that follows.

Two of the four are candidates for a remote digital channel: the questionnaire and the body measurement. The other two need the person present, with equipment and a clinician.

Body measurement is where manual practice varies most, and national protocols show why. The [anthropometry procedures manual](https://wwwn.cdc.gov/nchs/data/nhanes/public/2021/manuals/2021-Anthropometry-Procedures-Manual-508.pdf) for the National Health and Nutrition Examination Survey (NHANES) specifies the waist measurement down to the anatomy: the examiner palpates the hip for the uppermost lateral border of the right ilium, marks it where it crosses the midaxillary line, has a second staff member check from the other side that the tape sits parallel to the floor and lies snug without compressing the skin, and reads the value at the end of normal expiration. A screening clinic running back-to-back appointments is not staffed for that.

Regulators already treat the questionnaire as a routed document. Appendix C to the Occupational Safety and Health Administration (OSHA) respiratory protection standard, the mandatory respirator medical evaluation questionnaire, has to be answerable during normal working hours or at a time and place convenient to the employee, forbids the employer and the supervisor from looking at the answers, and obliges the employer to tell the employee how to deliver it to the reviewing health care professional. Height and weight are items in its mandatory first section.

A digital intake channel is one way to meet that posture, because the document reaches the reviewer without passing through the employer. FitXpress does not administer that questionnaire. The medical evaluation and the clearance determination stay with the reviewing health care professional.

Where that component moves to a digital occupational health intake channel, the output is a structured set of figures: 80+ body measurements along with BMI, basal metabolic rate, body fat percentage, lean mass and fat mass. <!-- claim: FX-008 --> <!-- claim: FX-009 -->

## Manual vs digital intake, compared dimension by dimension

| Dimension | Manual intake | Digital intake |
|---|---|---|
| Where the step happens | In the clinic, inside the appointment slot | Remotely, before the appointment |
| Who performs the body measurement | Clinic staff, with a tape | The candidate or employee, guided on their own phone |
| Consistency across staff, sites and vendors | Varies with technique, landmark marking and local training | One capture procedure applied everywhere |
| Record format | Written or transcribed, timestamped when entered | Structured and time-stamped at capture |
| Questionnaire confidentiality routing | Depends on local paper handling | Set once by configuration |
| Time consumed inside the appointment slot | Questionnaire, measurement and transcription | Testing and examination only |
| What the method can capture | Every component of intake | The questionnaire and the body measurement |
| Access requirement for the person screened | Attendance | A smartphone, a network connection, and the ability to complete a guided capture |
| Setup and change-management cost | None, it is already in place | Integration, configuration and staff retraining before the first scan |

The rows split cleanly. Digital intake improves the dimensions that produce rescreens and cross-site inconsistency: who performs the measurement, how consistent the procedure is, and what format the record arrives in. Manual intake holds scope, access and cost of change, and none of those is small. It carries every component of occupational health screening intake, including the ones no remote channel can, it asks nothing of the person beyond attendance, and it needs no integration work.

One row stays deliberately qualitative. Consistency here means repeatability and a single capture procedure, and that evidence belongs with its conditions attached. The rows are the inputs to a program-level decision, and the decision framework turns them into one.

## Where FitXpress fits in a digital intake workflow

FitXpress covers one component of digital occupational health intake, which is remote body measurement capture before the appointment. The questionnaire, the modality-specific testing and the examination sit elsewhere in the program's stack, with their own systems and their own owners.

Three properties matter at that component. Capture happens on the candidate's or employee's own phone, before the appointment, from two photos in under 45 seconds. <!-- claim: FX-006 --> <!-- claim: FX-007 --> Outputs are structured and time-stamped at the moment of capture, which is what allows a record to be compared later. The compliance posture holds at procurement: FitXpress maintains Health Insurance Portability and Accountability Act (HIPAA) safeguards in US healthcare contexts, follows General Data Protection Regulation (GDPR) principles for processing in the EU, encrypts data at rest and in transit, processes no personal identifiers, and deletes photos immediately or within 30 days according to client policy. <!-- claim: FX-014 --> Data, privacy, security and regulatory detail sits in a dedicated FitXpress privacy and regulatory FAQ. <!-- SIDE-LINK PLACEHOLDER: Data, Privacy, Security & Regulatory FAQ. Draft at workspace/seo/articles/2026-07-14-fitxpress-privacy-security-faq/, not published. Publisher resolves the URL onto the anchor phrase "FitXpress privacy and regulatory FAQ" or drops the sentence. -->

The role is a remote intake and documentation layer that supports clinician review. For the wider picture of how structured body data is captured and delivered, [3DLOOK's mobile body scanning platform](https://3dlook.ai/) is the entry point.

## What improves operationally, and what the evidence behind it says

The question worth asking about any measurement method is which decision it has to be accurate enough for. For intake documentation the decision is whether records stay comparable across staff, across sites and across time points. Repeatability is the property that answers it.

Internal repeatability testing on a real-world customer dataset, using five repeated scans per participant, showed strong scan-to-scan consistency across the majority of evaluated measurements. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm. <!-- claim: FX-003 --> The conditions matter as much as the figure, and the [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) sets them out, starting from the point that every accuracy figure is relative to one specific reference.

Accuracy is a separate measurement against a separate reference. Internal validation across multiple real-world scan events with five repeated scans per person against expert pattern-maker manual measurements shows 3DLOOK's measurement accuracy of approximately 96-97% across body metrics, with a typical absolute error of 1.5-2.0 cm per measurement, varying by body part. <!-- claim: FX-001 --> Detailed methodology is available under a non-disclosure agreement.

The reference in that sentence decides what a method comparison can claim. Expert manual measurement is what the figure is measured against, which puts a superiority claim over a tape measure out of reach and puts the case for a digital intake channel where it belongs: on consistency across repeats, across staff and across sites.

Three operational effects follow, each conditional on the program. Measurement time can move out of the appointment slot. Records can arrive before the review step instead of during it. Missing and inconsistent fields, the common cause of rescreens, can fall. How far any of it goes depends on how the program routes the data and what the downstream system accepts.

## What FitXpress does not do

| The intake layer supports | The intake layer does not do |
|---|---|
| Remote body measurement capture before the appointment | Does not diagnose medical conditions |
| Structured, time-stamped intake records | Does not perform or replace the occupational health examination |
| BMI and body composition estimates as intake data points | Does not make fitness-for-duty or clearance determinations |
| Consistent capture across sites and vendor partners | Does not inform hiring or employment decisions |
| Documentation that supports clinician review | Does not replace clinician judgment or employer policy |
| Records available ahead of the review step | Does not guarantee compliance |

Compliance evaluation here runs on data-privacy and recordkeeping frameworks. The regulatory classification of any given deployment depends on intended use, deployment context and jurisdiction.

## A decision framework: which intake method fits which program

Manual intake remains the right answer in five situations, and switching without checking them spends money to make things worse. Single-site or low-volume programs where the appointment slot is not the constraint. Populations without reliable smartphone or network access, which includes plenty of industrial and seasonal workforces. Intake dominated by history, symptom and functional content, where body measurement is a minor line item. Workflows where the measurement is part of the examination itself and the clinician wants it in hand. Programs with no downstream system able to receive a structured record.

A digital intake channel earns its setup cost under a different set of conditions: high candidate or employee volume against fixed appointment capacity, several sites or vendor partners that need comparable records, a documented volume of rescreens traceable to missing or inconsistent intake data, and documentation that has to hold up across reporting periods.

For most programs the answer is hybrid. The questionnaire and the body measurement move to a remote channel. The testing and the examination stay in the clinic. The split is decided component by component, and which components move depends on the workforce.

One legal boundary sets the timing of all of it. Under [Equal Employment Opportunity Commission (EEOC) enforcement guidance on pre-employment disability-related questions and medical examinations](https://www.eeoc.gov/laws/guidance/enforcement-guidance-preemployment-disability-related-questions-and-medical), an employer may not ask disability-related questions or conduct medical examinations until after it makes a conditional job offer, and once that offer is made those questions and examinations are permitted where they apply to all entering employees in the job category. Choosing between manual vs digital intake decides a method. It never decides a candidate.

## Buyer fit and the questions to ask before switching

Occupational health providers and clinic networks see the payback first, because the appointment slot is their constrained resource and intake is what overruns it. Workforce screening vendors running multi-employer contracts come second: their records have to be comparable across employers, sites and subcontractors, and a single capture procedure is what makes that possible. Multi-site employers with in-house programs come third, where the gain is documentation consistency across locations more than clinic throughput. Workers' compensation and absence administrators have a related but separate problem, and the [full roster of occupational health buyer profiles](https://3dlook.ai/content-hub/occupational-health-screening-software/) covers it.

An evaluation of any occupational health employee screening tool, or of occupational health screening services that bundle one, is worth running against five questions.

- Which intake components actually move to the remote channel, and which stay in the clinic.
- What the current rescreen rate is, and what causes it.
- Whether the downstream system can receive a structured record, or whether someone will retype it.
- What the documented path is for a candidate who cannot complete a remote capture.
- How repeatability was measured, over how many repeated scans, and against which reference.

## Frequently asked questions

**Is digital intake more accurate than manual tape measurement in occupational health screening?**
The comparison does not resolve that way. 3DLOOK's accuracy figure is measured against expert manual measurement as the reference, which makes expert manual measurement the benchmark. Two questions are answerable: whether the expected error suits the decision the record supports, and whether repeated measurements stay comparable. On the second, repeated scans showed typical scan-to-scan differences of less than 1 cm for most evaluated measurements, with the conditions set out in the [accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/). <!-- claim: FX-003 -->

**Which parts of occupational health intake cannot be moved to a digital channel?**
History and symptom review that needs clinical follow-up, modality-specific testing such as drug screening or vision and hearing checks, functional assessment, and the examination itself. Anything needing equipment or a clinician in the room stays in the clinic.

**What happens if a candidate cannot complete a remote scan?**
The manual path stays open as the documented fallback, and a digital intake channel does not remove the need for one. Access varies by workforce, by role and by geography, and treating the remote channel as a full replacement strands part of the population. The fallback rate is worth measuring during a pilot.

**Does moving intake to a digital channel change the post-offer boundary for pre-employment screening?**
No. Under Equal Employment Opportunity Commission guidance, the boundary is set by the timing and the content of disability-related questions and medical examinations, and the channel the intake data arrives through does not move it. Programs still schedule them after a conditional offer, applied to all entering employees in the job category. What a specific program may ask, and when, stays with its own counsel.

**Can digital intake records be compared against measurements taken manually at an earlier appointment?**
Carefully, and only where the program documents both methods. The two references differ, which makes a mixed-method series weaker than a consistent one. Standardizing the capture method is what makes a series across time points usable.

**What should a program measure to know whether digital intake worked?**
Four numbers: the rescreen rate and its causes, intake completeness at the point of review, measurement time inside the appointment slot, and record comparability across sites. A baseline for each one before the pilot is what makes the result readable.

## Next steps

Run the two intake models against the program's own throughput and rescreen numbers, component by component, and see which components are worth moving. Then [talk to 3DLOOK about the intake workflow](https://3dlook.ai/pricing/#bd-modal-personalized).
