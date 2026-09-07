---
slug: 2026-09-03-manual-vs-digital-intake-occupational-health
product: fitxpress
status: ready_for_review
created: 2026-09-03
revision: 2
revised: 2026-09-04
hub: Occupational Health Screening (Hub 8)
cluster: Comparison
action_type: create-net-new
author: Assel Sekerova
word_count: 2199
source_final: final.md (revision 3, status: edited, 2026-09-04)
review_applied: review-1.md (verbatim, retrieved 2026-09-04 via Google Drive) + review-1-decisions.md
supersedes: publish-package.md rev 0 (2026-09-03, written before Review 1; certified the
  cannibalization guardrail clean on a claim the reviewer then checked against the live hub and
  graded "Not met" — the worst finding in the review. This rev rewrites that judgment from scratch
  against final.md rev 3 and the live hub page, not by amending the old text.)
---

# Publish Package — 2026-09-03-manual-vs-digital-intake-occupational-health

## Meta

**Title:** Manual vs Digital Intake in Occupational Health Screening (57 chars) — **recommended**
**Description:** Manual vs digital intake in occupational health screening, compared step by
step: workflow, cost, exceptions and the metrics to test before switching. (150 chars)
**Slug:** `manual-vs-digital-intake-occupational-health-screening`
**Category:** Content hub, FitXpress / Occupational Health (supporting comparison article under
the Occupational Health Screening hub)

Brand suffix rule: recommended title is 57 chars, so `| 3DLOOK` is not appended (rule allows it
only at ≤49 chars without it). Primary keyword `manual vs digital intake` occupies the first 24
characters, well inside the first half of a 57-char title. The H1 is unchanged from checkpoint 1
(`plan.md` rev 2 confirms this), so the recommended title tracks it exactly minus the colon
subtitle — no drift between what ranks and what the page says at the top.

## Cannibalization check against the live hub (read this section before the checklist)

The rev-0 package asserted the page "does not restate the buyer roster, workflow, category
definition, or other hub-owned material." Review 1 checked that claim against the
[live hub](https://3dlook.ai/content-hub/occupational-health-screening-software/) and graded the
cannibalization guardrail **Not met** — the single worst finding in the review (see
`review-1.md`, "Overall assessment" and item 1). This section re-verifies the claim against
`final.md` rev 3 by fetching the live hub page again today (2026-09-04) and reading both texts
side by side, rather than re-asserting the old sentence.

**Removed this revision (confirmed absent from `final.md` rev 3):**

- The full "What FitXpress does and does not do" table (12 rows on the hub). Not present.
  Boundary is now two sentences in the Section 1 scope note and a two-sentence pair in Section 8.
- The buyer-profile roster ("Who uses FitXpress for occupational health screening?" — four named
  profiles on the hub). Not present. Section 7 points up instead: "Which buyer profiles gain
  most, and in what order, is set out in the [occupational health screening software hub]."
- The standalone "why now" section that leaned on a hiring-volume BLS figure. Not present in any
  form — review item 6 removed the BLS paragraph outright and no substitute was added.
- The hub's numbered five-step "how digital intake works with FitXpress" implementation walk.
  Not restated. Section 8 compresses the mechanism to two sentences (own device, two photos,
  under 45 seconds, structured/time-stamped output) without the hub's step numbering.
- The hub's pre-employment-vs-return-to-work workflow table. Not present in any form; this
  article's own new table (Section 5) compares manual vs digital, a different axis entirely.

**What the article now owns, verified against the hub text (not just against the outline):**

- The 14-row method-comparison table (Section 4). No equivalent table exists on the hub.
- The workflow-differences table (Section 5) — reviewer-supplied, shipped verbatim. This table
  did not exist in any draft before this revision and has no counterpart on the hub.
- The decision framework (Section 6): when manual intake remains right, when a digital channel
  earns its setup cost. The hub argues for digital intake as an operational upgrade; it does not
  lay out conditions under which manual is still the right call. That inversion is this article's
  own territory.
- The evaluation-metrics table (Section 7, reviewer-supplied, eight rows) plus the five
  implementation questions. Net new; nothing like it is on the hub.
- The accuracy-vs-repeatability distinction with the actual figures (Section 8 ¶2). The context
  pack's own hub inventory records that the hub deliberately does not spend FX-001 or FX-003
  ("the hub never states 96-97% or < 1 cm anywhere"), and a text search of the live page today
  confirms it — no "96-97", no "1.5-2.0 cm", no "1 cm" figure appears on the hub. This is
  genuinely article-exclusive ground.

**What still echoes the hub — flagged, not certified clean:**

- **The opening scene.** `final.md` L123: "A candidate fills in a health questionnaire, a medical
  assistant takes tape measurements, and someone transcribes both into the screening record
  before the clinician sees anything." The hub's opening (`hub_text`): "Candidates and employees
  fill out paper questionnaires in the waiting room; medical assistants record body measurements
  with tape at the appointment...". Different sentences, one paragraph shrunk to one sentence, and
  it now sets up an appointment-slot-economics argument rather than the hub's business narrative —
  but it is the same underlying scene, and review item 1 named "the introductory description of
  the manual bottleneck" as one of its five worst duplication spots. I am not calling this
  resolved to zero; I am calling it an unavoidable shared premise that has been cut by roughly
  four-fifths and re-purposed, which is a materially different thing from the three blocks that
  were removed outright.
- **Shared topical territory, by design.** Throughput, missing/incomplete data, rescreens, and
  multi-site documentation consistency are named in the content-plan's own guardrail row
  (`content-plan.md:213`) as exactly what this supporting article should cover, and the hub also
  covers all four at the category level (its "What improves with digital occupational health
  intake?" section). The hub states them as delivered benefits; this article states them as
  hedged decision conditions ("a digital channel earns its setup cost under different
  conditions..."). Different rhetorical job, same four nouns — licensed overlap under the
  hub-and-cluster model, not the restatement the reviewer flagged, but worth naming so it doesn't
  read as a coincidence.
- **Compliance boilerplate.** "It is not positioned as a medical device," and "not a clearance,
  eligibility or fitness-for-duty input" also appear on the hub. This is the required compliance
  floor under `CLAUDE.md` §6/§15 and belongs on every FitXpress page touching this vertical; it is
  not hub-owned material being duplicated, it is the boundary every page must carry regardless of
  which page it is.

**Verdict:** cannibalization guardrail — substantially resolved. Four of the five duplication
sites the reviewer named outright are gone, and the article now owns four blocks with no hub
counterpart. The fifth (the opening scene) is a real, if much smaller, echo. If Vadim wants it at
zero, the fix is a one-sentence rewrite of the Section 1 opener to drop the tape-measurement/
transcription imagery entirely and open on the appointment-slot economics directly — flagged as
an open item below rather than made silently.

## SEO checklist

- [x] **Primary keyword in H1, first paragraph, 1-2 H2.** Verified independently (not just from
      the frontmatter): H1 line 119, first prose paragraph line 123, one H2 line 157 ("Manual vs
      digital intake, compared dimension by dimension"). `article_lint.py` keyword-placement gate:
      4 occurrences, `manual vs digital intake`.
- [x] **Meta title 57 chars, under 60, primary keyword in the first half.**
- [x] **Meta description 150 chars, inside 140-160, keyword once, does not repeat the title.**
- [x] **Every figure traces to `approved_claims`.** 7 claim markers, all 7 IDs used
      (FX-001, FX-003, FX-006, FX-007, FX-008, FX-009, FX-014). `FX-004` (`publishable: false`,
      the internal 95%+ repeatability figure) is absent — grepped, zero hits. `article_lint.py`
      claim-traceability gate: pass.
- [x] **No banned words.** Grepped the body directly against the full `banned_words` list in the
      context pack (leverage, utilize, harness, robust, seamless, comprehensive, delve, navigate,
      tapestry, realm, unlock, unleash, revolutionary, game-changing, cutting-edge) — zero hits.
      No BMR token (spelled out as "basal metabolic rate" is itself gone; the whole
      body-composition inventory line was cut per review item 7). No stacked negation, no
      corrective negation ("X, not Y"), no "rather than" — grepped, zero hits both.
- [x] **Word count within ±10% of target.** 2,199 words against a 2,050 target = +7.3%, inside
      ±10%. Also inside the reviewer's own binding 1,900-2,200 band (landed 1 word under the
      ceiling), and down from 2,745 at rev 0 — a 20% cut.
- [x] **Intro hook in the first two sentences.** Concrete scene (questionnaire, tape, transcription,
      clinician) in sentence one, reframe to "manual vs digital intake... an operations question
      about a fixed appointment slot" in sentence two.
- [x] **CTA placement per plan; type matches intent.** One CTA, in the closing "Next steps" section
      only, as `plan.md` specifies. Evaluation-framed direct CTA ("run the two intake models
      against the program's own throughput and rescreen numbers... then talk to 3DLOOK"), which
      matches the comparison/MOFU intent — not a hard demo-now ask, not a passive "learn more."
- [x] **No generic AI patterns.** `detect-ai-tells.py` verdict CLEAN, 0 hard fails, 0 house-rule
      violations, ai_density 0.42/1000 (budget 6.0-8.0 depending on channel setting). No em dash
      anywhere (grepped). No triple parallelism spotted on a manual read of all bullet lists and
      table reading paragraphs.
- [x] **Terminology guardrails.** Grepped the body directly against Part 1/Part 2 of
      `terminology-guardrails.md`: no em dash, no `objective` about our own output, no "the
      reader/audience," no "the following sections," no "see below," no "this article/guide"
      outside the scope note, no `by hand`, no `let`, no `plus` as a connector, no `so` introducing
      a benefit, zero corrective negation, zero "rather than." "positioned as" appears exactly
      once, in the licensed medical-device sentence, nowhere else. Presumed-reaction phrasing
      ("what trips people up," etc.) and concept-as-agent phrasing: none found.
- [x] **Abbreviations (M1 + exception).** OSHA, NHANES, EEOC, HIPAA, GDPR each expand at first use
      and each appears exactly once expanded (grepped, confirmed no bare second use except EEOC's
      deliberate short form in FAQ Q4, which is licensed by `changes_summary` since the full form
      already ran in Section 6). BMI, US, EU bare throughout, per the exception. NDA spelled out
      as "non-disclosure agreement," never abbreviated. `article_lint.py` abbreviations (M1) gate:
      pass.
- [x] **Medical framing.** The licensed sentence, verbatim, exactly once: "It is not positioned as
      a medical device." (Section 1 scope note.) "positioned as" appears nowhere else in the
      article — confirmed by direct grep, not by trusting the frontmatter.
- [x] **Links on meaningful anchors; external sources neutral and non-vendor.** All nine links
      checked by hand: hub (x2), accuracy framework (x2), homepage, pricing CTA — all on
      descriptive anchor phrases, no bare URLs (`article_lint.py` bare-URL check: pass, 0 problems).
      Three external sources, all US government: OSHA Appendix C (osha.gov), CDC/NHANES
      Anthropometry Procedures Manual (cdc.gov), EEOC enforcement guidance (eeoc.gov). **The BLS
      JOLTS source from the pre-review draft is gone** — grepped for "bls," "bureau of labor,"
      "jolts": zero hits. No vendor blogs anywhere.
- [x] **AI-tells detector actually run — output pasted below, not estimated.** Ran both gates
      myself in this session, independently of the editor's frontmatter claim, and the numbers
      match exactly.
- [x] **Image / alt-text suggestions provided below.**

**SEO checklist: 15/15.**

### Detector output, verbatim (run by seo-publisher, 2026-09-04, this session)

```
$ python3 brand-assets/style-guides/scripts/detect-ai-tells.py \
    workspace/seo/articles/2026-09-03-manual-vs-digital-intake-occupational-health/final.md \
    --channel article --summary

SEO / blog article · en · 2377 words
AI density: 0.42/1000 (budget 6.0) -> low
VERDICT: CLEAN — check the positive side (voice, varied rhythm, a stated boundary) and ship.

TOP SOFT MARKERS:
  1x 'serve as' (L129)
```

`hard_fails`: `[]`. `house_rule_violations`: `[]`. Exit 0. The one soft marker is "serve as a
basis for hiring or employment decisions" inside the Section 1 scope note — approved boundary
phrasing, left verbatim on purpose (also recorded in `final.md`'s own `self_check`).

### `article_lint.py` output, verbatim (run by seo-publisher, 2026-09-04, this session)

```
$ python3 scripts/article_lint.py \
    workspace/seo/articles/2026-09-03-manual-vs-digital-intake-occupational-health/final.md

[ok  ] hard bans (detect-ai-tells)      verdict CLEAN, ai_density 0.42, rhythm_variation 0.66
[ok  ] prose length                     prose words 2199 vs target 2050 (band 1742-2357)
[ok  ] claim traceability               claims_used FX-001 FX-003 FX-006 FX-007 FX-008 FX-009 FX-014
[ok  ] banned claims
[ok  ] superseded figures
[ok  ] internal links                   6 links, 4 distinct, directions {up 1, sideways 0, down 0, trust 1}
[ok  ] keyword placement                'manual vs digital intake', 4 occurrences, 10 H2s
[ok  ] abbreviations (M1)
[ok  ] accuracy discipline              figures present, links to framework True

VERDICT: PASS
```

Note on `sideways 0` / `down 0`: reporting artifacts, not missing links. The context pack
(`workspace/seo/_context-packs/2026-09-03-manual-vs-digital-intake-occupational-health.yaml`)
holds `sideways` and `down` as prose explanations, not bare URLs, by design — `sideways` records
that the only permitted target (the Privacy & Regulatory FAQ) is unpublished, and `down` routes
CTAs to the homepage/pricing without naming a single canonical URL. The article does carry both
as prose links: `https://3dlook.ai/` (Section 8) and
`https://3dlook.ai/pricing/#bd-modal-personalized` (Next steps).

### Accuracy discipline, verified against the canon directly (not just the linter's boolean)

Both figures were checked word-for-word against
`brand-assets/product-info/accuracy-formulations.md` §1.1 and §1.2:

- Repeatability (Section 8 ¶2, FAQ Q1): "Internal repeatability testing on a real-world customer
  dataset, using five repeated scans per participant, showed strong scan-to-scan consistency
  across the majority of evaluated measurements. For most evaluated measurements, repeated scans
  showed typical scan-to-scan differences of less than 1 cm." — verbatim match.
- Accuracy (Section 8 ¶3): "Internal validation across multiple real-world scan events with five
  repeated scans per person against expert pattern-maker manual measurements shows 3DLOOK's
  measurement accuracy of approximately 96-97% across body metrics, with a typical absolute error
  of 1.5-2.0 cm per measurement, varying by body part." — verbatim match, hyphens not en dashes.
- The two benchmarks never share a paragraph. No ISO 8559 figure anywhere. No per-measurement
  figures. No `95%+ repeatability` (that is `FX-004`, marked `publishable: false`, and it is
  absent). Both figures carry their condition and the framework link
  (`https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/`) sits in the same paragraph as
  the figure, not in a separate "further reading" list.

## Content strategy checklist (`content-strategy-guidelines.md` §16)

- [x] **Bound to the right hub.** Occupational Health Screening (Hub 8), Comparison cluster,
      `content-plan.md:213`.
- [x] **`action_type: create-net-new` respected.** Hub live since 2026-07-10; the row confirms
      "Net-new supporting" is correct, not refresh/section/review.
- [~] **Cannibalization guardrail.** See the dedicated section above — substantially resolved, one
      residual echo flagged and not hidden. Marked passing on balance, not on a blanket claim.
- [x] **Vertical boundary held; scope note present.** Intake and documentation only. No sentence of
      the shape "clears employees for duty." "Speed clearance decisions" is not used as a
      capability claim; Section 6 keeps the determination with the licensed provider. Scope note
      is the italic blockquote in Section 1, non-negotiable per plan and present.
- [x] **Internal links in 4 directions.** up → hub (Sections 1, 7), trust → accuracy framework
      (Section 8 ¶2, FAQ Q1), down → FitXpress homepage (Section 8) and the pricing CTA modal
      (Next steps). Sideways is deliberately absent from the text — its only licensed target, the
      Privacy & Regulatory FAQ, is unpublished, and per `review-1-decisions.md` §B the compliance
      paragraph is kept short and precise rather than linked to a page that is not live. This is a
      declared design choice, not a missed direction; the link-direction gate does not fail it
      because the context pack holds that direction as prose, not a URL.
- [x] **FAQ section present, GEO/AEO-shaped.** 4 questions (down from 6, per review), each answered
      in 2-3 sentences. None restates the hub's 7 FAQ questions or its 5 inline bolded Q&As
      (checked line by line against `hub_inventory.hub_faq_questions` and `hub_inline_qa` in the
      context pack — no overlap in question phrasing or angle).
- [x] **Negative-scope boundary present; no forbidden positioning claim** — with a structural note.
      The hub's full "What FitXpress does and does not do" table is *not* reproduced here by
      design (Review 1 item 1: the hub owns that table). The article instead states the boundary
      twice, briefly: the Section 1 scope note ("does not perform medical examinations, make
      fitness-for-duty or clearance determinations, or serve as a basis for hiring or employment
      decisions... not positioned as a medical device") and the Section 8 boundary pair ("not a
      clearance, eligibility or fitness-for-duty input"). No forbidden positioning claim found
      anywhere in the body. Marking this ✅ on substance (the boundary is stated and correct) while
      noting explicitly that it is not a standalone labeled section, because the reviewer
      specifically directed its removal as hub-owned material.
- [x] **No unsupported medical / legal / underwriting / employment / clinical-trial claim.** OSHA
      and EEOC passages state what the regulator requires and leave the determination with the
      reviewing clinician and the program's own counsel ("What a program may ask stays with its
      own counsel" — FAQ Q4). The one ungrounded inference the reviewer found ("the document
      reaches the reviewer without passing through the employer") is confirmed absent — grepped,
      not present in `final.md`.
- [x] **Owns one distinct search intent.** Method comparison and method choice for occupational
      health screening intake — comparison/MOFU, distinct from the hub's BOFU/use-case intent.

**Content strategy checklist: 9/9, one item (`~`) passed on a documented judgment call rather
than a clean mechanical check** — see the cannibalization section above for the reasoning. No item
in the positioning/compliance/cannibalization block is a ❌, so this package does not STOP.

## Alt options

### Meta title variants

1. **Manual vs Digital Intake in Occupational Health Screening** (57 chars) — **recommended.**
   Unchanged from checkpoint 1 (the H1 didn't move), keyword first, vertical named in full, no
   truncation risk in the mid-50s.
2. Manual vs Digital Intake for Occupational Health Screening (58 chars) — "for" instead of "in";
   reads slightly more like a buyer's-guide title, marginal difference.
3. Manual vs Digital Intake: Which Method Fits Your Program (56 chars) — leads with the
   decision-framework angle that's now more central after Review 1, but drops "occupational
   health screening" from the title itself, which weakens vertical-specific search relevance for
   a GEO/comparison play that depends on exact-match keyword strength.

### Meta description variants

1. **Manual vs digital intake in occupational health screening, compared step by step: workflow,
   cost, exceptions and the metrics to test before switching.** (150 chars) — **recommended.**
   Names four concrete sections of the revised structure (workflow, cost, exceptions, metrics),
   keyword once, closes on an implied action.
2. Manual vs digital intake in occupational health screening: compare workflow, cost and
   consistency, and see which model your program should pilot first. (151 chars) — leads with an
   imperative ("compare... see"), slightly more CTA-forward.
3. A method comparison for manual vs digital intake in occupational health screening: workflow,
   cost, exceptions, and the metrics for testing a pilot. (147 chars) — frames the page as a
   named artifact ("a method comparison") rather than a question, useful if search snippets are
   getting truncated on the other two.

## Image and alt-text suggestions

The article currently carries one text callout that reads as a placeholder for an illustration,
and no embedded images. This is a reduction from rev 0 (which specified two illustrations); the
Section 4/5 tables now carry the comparison visually as tables, so a duplicate diagram for either
is not needed.

1. **Figure 1 (Section 3, "The three phases of occupational health intake").** The callout
   ("> **Figure 1.** The three phases of intake, with the remote-capable part marked.") wants a
   three-block flow diagram: pre-appointment intake → on-site screening → clinical review, with
   the first block visually marked as the one a remote channel reaches.
   Alt text suggestion: "The three phases of occupational health intake — pre-appointment,
   on-site screening, clinical review — with pre-appointment marked as the remote-capable phase."
   No figure or percentage belongs in the alt text; it is published copy and a number there is a
   published claim.
2. No second illustration is specified this revision. If design wants one for the Section 4
   comparison table, keep it decorative (icons for "manual" vs "digital" columns) rather than a
   second data visualization, since the table itself is the primary artifact and Review 1
   specifically warned against restating the hub's visual/positioning material.

Design tokens from `DESIGN.md`: electric blue `#143DFF` for the digital path, navy `#050F40` for
the manual path, Satoshi throughout.

## Open items for Vadim

1. **The opening-scene echo (see cannibalization section above).** Not blocking — four of the
   five duplication sites the reviewer flagged are resolved outright, and this fifth one is cut by
   roughly 80% and repurposed. But it is a real, if small, echo of the hub's opening paragraph. If
   you want it at zero rather than "substantially resolved," the fix is a one-sentence rewrite of
   the Section 1 opener that drops the tape/transcription imagery and opens directly on the
   appointment-slot economics. I did not make this edit myself because it would mean touching
   prose after two lint-and-detector passes already certified it, and the call on how much shared
   premise a comparison article is allowed to state is a judgment call, not a mechanical one.
2. **Compliance-paragraph trim, pending the Privacy & Regulatory FAQ.** The Section 8 compliance
   paragraph is stated at `compliance.md` precision (HIPAA/GDPR/encryption/retention) rather than
   linked, because the Data, Privacy, Security & Regulatory FAQ is still unpublished
   (`content-plan.md:24`, the last open P0 hub gap; drafts under
   `workspace/seo/articles/2026-07-14-fitxpress-privacy-security-faq/`, nothing live). Confirmed:
   `final.md` carries no placeholder pointing at it — the only HTML comments in the file are the
   seven `<!-- claim: FX-xxx -->` markers the traceability gate reads, grepped and verified. When
   that FAQ ships, trim the paragraph to a link, per review item 7's explicit instruction that no
   draft-only placeholder may reach the CMS version.
3. **Two parallel runs collided on this article's files on 2026-09-04** (documented in `log.md`).
   One run had no Drive access or Bash and produced an unverified `final.md` from a stale draft;
   it is preserved only as `final.md.conductor-0944-unverified` and nothing in this package is
   built from it. Flagging so it isn't mistaken for a second, independent version of the article.
4. **Medical-framing wording has now flipped three times across five files** (2026-06-09 →
   2026-08-13 → 2026-09-02). It is correctly applied here (verified above, exactly one instance,
   the licensed sentence), but if 2026-09-02's restoration is meant to be final, it would be worth
   stating once as a licensed exception in `terminology-guardrails.md` itself rather than as a
   footnote repeated in four other documents, so the next article doesn't need this checked by
   hand again.

## Article

# Manual vs Digital Intake in Occupational Health Screening: Which Method Fits Which Workflow

## The intake step is where screening programs lose time

A candidate fills in a health questionnaire, a medical assistant takes tape measurements, and someone transcribes both into the screening record before the clinician sees anything. Framed as manual vs digital intake, that sequence sounds like a software preference; inside a screening program it is an operations question about a fixed appointment slot.

Four operational costs come out of that step: throughput against fixed appointment capacity, missing or incomplete intake data, rescreens caused by unusable records, and documentation that fails to line up across sites or vendor partners. Adding clinic capacity adds appointment slots. It does not change the intake work inside each slot, and whether extra capacity relieves the bottleneck depends on where the time is lost.

Two questions decide the method: which intake steps a remote channel can carry, and which programs gain enough to justify the change. The category, its buyer profiles and the full workflow sit in the [occupational health screening software hub](https://3dlook.ai/content-hub/occupational-health-screening-software/).

> ***Scope note.*** *In this comparison, digital intake means the whole pre-appointment workflow. FitXpress provides the remote body-measurement component; questionnaire collection, testing, examination and clinical review remain within the customer's other systems. FitXpress does not perform medical examinations, make fitness-for-duty or clearance determinations, or serve as a basis for hiring or employment decisions. It is not positioned as a medical device.*

## Short answer: what each intake method covers

- **Manual intake** means a paper health questionnaire, a staff-administered tape measurement, and transcription into the screening record, all at or around the appointment.
- **Digital intake** collects the same questionnaire content through a structured remote channel before the appointment, with body measurement captured by a guided smartphone scan from two photos in under 45 seconds. <!-- claim: FX-006 --> <!-- claim: FX-007 -->
- **The overlap is partial.** A remote channel can carry the questionnaire and the body measurement; modality-specific testing and the examination stay in the clinic.
- **The operational cost sits inside that overlap.** Both are captured and transcribed under appointment-time pressure, which exposes them to missing or inconsistent fields, and an incomplete record can trigger a rescreen.
- **Neither method wins outright.** Manual intake reaches every phase and asks nothing of the candidate beyond attendance and the on-site steps. Digital intake standardizes the part that repeats across a program.

Clinic software calls this digital patient intake: paper patient intake forms replaced by structured pre-visit capture.

## The three phases of occupational health intake

Treating occupational health intake as one step makes the comparison confusing. The occupational health intake process runs in three phases, and a remote channel reaches only the first.

1. **Pre-appointment intake.** The health-history questionnaire, required documents, and eligible body measurements. This is the phase a remote channel can carry.
2. **On-site screening.** Equipment-based testing (drug screening, vision, hearing, functional capacity) and the examination, which need the person present.
3. **Clinical review.** The reviewing provider reads the record and, where the program calls for it, makes the determination.

> **Figure 1.** The three phases of intake, with the remote-capable part marked.

Manual practice varies most at the measurement step. The [anthropometry procedures manual](https://wwwn.cdc.gov/nchs/data/nhanes/public/2021/manuals/2021-Anthropometry-Procedures-Manual-508.pdf) for the National Health and Nutrition Examination Survey (NHANES) specifies the waist measurement down to the anatomy: palpate for the uppermost lateral border of the right ilium, mark it at the midaxillary line, have a second examiner confirm the tape is level, and read at normal expiration. The protocol shows the training, landmarking and quality control behind a standardized manual measurement.

One regulated context already routes the questionnaire for confidentiality: [Appendix C to the Occupational Safety and Health Administration (OSHA) respiratory protection standard](https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.134AppC) forbids the employer and the supervisor from reading a worker's answers, and obliges the employer to explain how to deliver the form to the reviewing health care professional. The requirement is specific to respirator medical evaluations, and any channel carrying the form has to meet it.

FitXpress does not administer that questionnaire; the medical evaluation and the clearance determination stay with the reviewing health care professional.

## Manual vs digital intake, compared dimension by dimension

Each row is a dimension a program can check for itself.

| Dimension | Manual intake | Digital intake |
|---|---|---|
| Where the step happens | In the clinic, in the appointment slot | Remotely, before the appointment |
| Who measures | Clinic staff, with a tape | The person, guided on their own phone |
| Consistency across staff and sites | Varies with technique, landmarking and local training | A standardized guided procedure, subject to capture quality and validation requirements |
| Record format | May require manual entry or scanning; structure depends on the receiving system | Can arrive in a structured format when the integration supports it |
| Questionnaire confidentiality routing | Depends on local paper handling | Depends on permissions, system configuration and the program's data-handling design |
| Time inside the appointment slot | Questionnaire, measurement and transcription | Testing and examination only |
| Phases the method reaches | All three, since the person is on site | Pre-appointment intake only: questionnaire and eligible measurements |
| Access requirement for the person screened | Attendance and completion of the required on-site intake steps | A smartphone, a connection, and a completed guided capture |
| Setup and change-management cost | Lower incremental implementation cost; continuing staff and administration requirements | Integration, configuration and staff retraining before the first scan |
| Ongoing labor | Staff time at every appointment | Configuration and support effort instead of in-appointment staff time |
| Exception handling | Handled in person during the visit | Needs a defined path for incomplete or failed captures |
| Integration dependency | None | Requires a receiving system and a defined transfer path |
| Fallback availability | Is itself the fallback | Requires the manual path to stay open |
| Data-entry correction | Transcription errors corrected by re-entry | Fewer transcription steps; corrections are made in the receiving system |

Moving eligible intake steps before the appointment can reduce in-appointment collection and transcription. The effect depends on completion rates, fallback volume, integration quality and existing rescreen causes.

Manual intake holds three dimensions: it reaches all three phases, it asks nothing of the candidate beyond attendance and the on-site steps, and it is itself the fallback that every digital channel still needs. Digital intake concentrates its gains on consistency and record format. For a program running several sites, those are the two rows the decision framework turns on.

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

Manual intake remains the right answer in several situations, and switching without checking them spends money to make things worse: single-site or low-volume programs where the appointment slot is not the constraint; populations without reliable smartphone or network access; intake dominated by history, symptom and functional content, where body measurement is a minor line item; workflows where the measurement is part of the examination; and programs with no downstream system able to receive a structured record.

A digital channel earns its setup cost under different conditions: high volume against fixed appointment capacity, several sites or vendor partners needing comparable records, rescreens traceable to missing or inconsistent intake data, and documentation that has to hold across reporting periods.

For most programs the answer is hybrid: the questionnaire and the body measurement move to a remote channel, testing and the examination stay in the clinic. The split is decided component by component, and each component that moves needs its own fallback and its own transfer path.

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

Five questions sit alongside the numbers:

1. Which intake steps move to the remote channel, and which stay on site?
2. What is the current rescreen rate, and what causes it?
3. Can the downstream system receive a structured record, or will someone retype it?
4. What is the documented path for a person who cannot complete a remote capture?
5. How was repeatability measured: over how many repeated scans, on which measurements, and against which reference?

The last is the diligence question worth handing any vendor, including this one. Which buyer profiles gain most, and in what order, is set out in the [occupational health screening software hub](https://3dlook.ai/content-hub/occupational-health-screening-software/).

## Where FitXpress fits

FitXpress covers one part of the first phase: body measurement, taken remotely before the appointment. The person scans on their own phone, from two photos, in under 45 seconds. The output is structured and time-stamped at capture, covering 80+ body measurements, including the circumferences and BMI an intake record carries. <!-- claim: FX-006 --> <!-- claim: FX-007 --> <!-- claim: FX-008 --> <!-- claim: FX-009 -->

The useful question about any measurement method is: accurate enough for which decision? For intake documentation, that is whether records stay comparable across staff, sites and time. Internal repeatability testing on a real-world customer dataset, using five repeated scans per participant, showed strong scan-to-scan consistency across the majority of evaluated measurements. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm. <!-- claim: FX-003 --> The [mobile body scanning accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/) sets out those conditions, starting from the point that every accuracy figure is relative to one specific reference.

Accuracy is a separate measurement against a separate reference. Internal validation across multiple real-world scan events with five repeated scans per person against expert pattern-maker manual measurements shows 3DLOOK's measurement accuracy of approximately 96-97% across body metrics, with a typical absolute error of 1.5-2.0 cm per measurement, varying by body part. <!-- claim: FX-001 --> Detailed methodology is available under a non-disclosure agreement. That reference puts a superiority claim over a tape measure out of reach; the case for a digital channel rests on repeatability instead. A structured, time-stamped record is easier to compare than a written one, though structure alone does not ensure comparability or compliance; that depends on the capture method and the receiving system.

FitXpress maintains Health Insurance Portability and Accountability Act (HIPAA) safeguards in US healthcare contexts, follows General Data Protection Regulation (GDPR) principles for processing in the EU, encrypts data with AWS S3 SSE-S3 at rest and TLS in transit, processes no personal identifiers, and deletes photos immediately after processing or within 30 days, with the window set by client policy. <!-- claim: FX-014 --> FitXpress works as a remote intake and documentation layer that supports clinician review. It is not a clearance, eligibility or fitness-for-duty input. Compliance evaluation runs on data-privacy and recordkeeping frameworks, and the regulatory classification of a deployment depends on intended use, context and jurisdiction. [3DLOOK's mobile body scanning platform](https://3dlook.ai/) covers how the data is captured and delivered.

## Frequently asked questions

**Is digital intake more accurate than manual tape measurement in occupational health screening?**
The comparison does not resolve that way, because 3DLOOK's accuracy figure is measured against expert manual measurement as the reference. The answerable questions are whether the expected error suits the decision and whether repeated measurements stay comparable. Repeated scans showed typical scan-to-scan differences of less than 1 cm for most evaluated measurements, with the conditions set out in the [accuracy framework](https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/). <!-- claim: FX-003 -->

**Which parts of occupational health intake cannot be moved to a digital channel?**
History and symptom review that needs clinical follow-up, modality-specific testing such as drug screening or vision and hearing checks, functional assessment, and the examination. Anything needing equipment or a clinician stays in the clinic.

**What happens if a candidate cannot complete a remote scan?**
The manual path stays open as the documented fallback, and a digital channel does not remove the need for one. Access varies by workforce, role and geography, and a remote-only channel strands part of the population.

**Does moving intake to a digital channel change the post-offer boundary for pre-employment screening?**
No. In the US, under EEOC guidance, the boundary is set by the timing and content of disability-related questions and medical examinations, and the channel the data arrives through does not move it. What a program may ask stays with its own counsel.

## Next steps

Run the two intake models against the program's own throughput and rescreen numbers, component by component, and see which are worth moving. Then [talk to 3DLOOK about the intake workflow](https://3dlook.ai/pricing/#bd-modal-personalized).
