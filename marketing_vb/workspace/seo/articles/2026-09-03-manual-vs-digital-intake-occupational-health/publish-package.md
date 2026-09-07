---
slug: 2026-09-03-manual-vs-digital-intake-occupational-health
product: fitxpress
status: ready_for_review
created: 2026-09-03
revision: 4
revised: 2026-09-07
hub: Occupational Health Screening (Hub 8)
cluster: Comparison
action_type: create-net-new
author: Assel Sekerova
word_count: 2160
source_final: "final.md (revision 5, status: edited, 2026-09-07)"
qc: "workspace/_quality/seo/2026-09-07-seo-review-2-manual-vs-digital-intake-occupational-health.md (17/20, scored against final.md revision 4 / publish-package.md revision 3); remediation applied in final.md revision 5, not yet re-scored"
review_applied: >
  review-1.md + review-1-decisions.md (rev 2 baseline, retained) + review-2.md (verbatim, pulled
  2026-09-07 via Google Docs connector) + review-2-decisions.md, PLUS a QC remediation pass (17/20,
  report above) that closed three pipeline-introduced defects in final.md revision 5 without new
  reviewer input. Review 2 item 6 (the privacy paragraph) remains PARTIALLY applied - the
  self-contradiction the reviewer caught and the AWS/TLS trim and the Business Associate Agreement
  clause are in. Of the three sub-points that were DECLINED on source-of-truth grounds per
  review-2-decisions.md section 6, with QC concurring (report section B), **R2-3 (GDPR
  controller/processor) was reopened and APPLIED on 2026-09-07 after Vadim made the sentence
  canonical in compliance.md**; R2-2 ("processes no personal identifiers" removal) and R2-4
  (output-retention rewrite) stay declined and are carried to Vadim below.
supersedes: >
  publish-package.md rev 3 (2026-09-07, built against final.md revision 4, before QC scored the
  pass and before remediation). Rev 3 is not wrong, it is superseded: QC found three real defects
  in revision 4 (a fidelity error against Review 2's own instruction, a repetition regression this
  pipeline introduced, a weakened correction), seo-editor fixed all three plus one optional tighten
  in revision 5, and this rev re-verifies every number and line reference against revision 5 rather
  than copying rev 3 forward. One open item rev 3 escalated to Vadim (the Section 7 diligence-
  question duplication) turned out to be closable by edit rather than a real reviewer-vs-reviewer
  conflict; it is struck below, not silently dropped, with QC's finding named. R2-1 is not that
  item and stays open, per QC's own recommendation to leave it for Vadim.
---

# Publish Package — 2026-09-03-manual-vs-digital-intake-occupational-health

## Meta

**Title:** Manual vs Digital Intake in Occupational Health Screening (57 chars) — **recommended**
**Description:** Manual vs digital intake in occupational health screening, compared step by
step: workflow, cost, exceptions and the metrics to test before switching. (150 chars)
**Slug:** `manual-vs-digital-intake-occupational-health-screening`
**Category:** Content hub, FitXpress / Occupational Health (supporting comparison article under
the Occupational Health Screening hub)

**Re-checked against `final.md` revision 5, not assumed.** The H1 (`final.md:275`, "Manual vs
Digital Intake in Occupational Health Screening: Which Method Fits Which Workflow") is
byte-identical to revisions 3 and 4 — the QC remediation pass touched Sections 2, 3 and 7 only,
none of which is the H1 or the meta strings. Both strings were re-counted with a script again this
session: title 57 chars, description 150 chars. Unchanged on that evidence, not on the assumption
that "nothing changed."

Brand suffix rule: recommended title is 57 chars, so `| 3DLOOK` is not appended (rule allows it
only at ≤49 chars without it). Primary keyword `manual vs digital intake` occupies the first 24
characters, well inside the first half of a 57-char title.

## QC remediation cycle (2026-09-07) — read this before the checklists below

This article went through an independent QC pass between `publish-package.md` rev 3 and this
revision. **Total score 17/20** (`A` adherence 4/5, `B` factual accuracy 5/5, `C` brand & tone 2/3,
`D` format & structure 3/3, `E` output quality 3/4) — full report at
`workspace/_quality/seo/2026-09-07-seo-review-2-manual-vs-digital-intake-occupational-health.md`.
`seo-editor` then ran a remediation pass, producing `final.md` revision 5. What changed as a direct
result:

1. **QC A-1 (the important one).** Editorial refinement E5 instructed reducing five implementation
   questions to two, one of them worded "how measurement performance was evaluated." Revision 4
   shipped the old, narrower Q5 verbatim instead of the reviewer's E5 wording — a retention, not an
   application — and that retention is what manufactured the Section 7 duplication that rev 3's
   package escalated to Vadim as an unresolvable reviewer-vs-reviewer conflict. It was not one.
   Revision 5 ships question 2 as "How was measurement performance evaluated?" (`final.md:378`),
   the overlap with the E3 sentence below it is gone, and `review-2-decisions.md:184` has been
   corrected in place with a dated note recording that the row said "Verbatim" and was wrong. **The
   Section 7 open item is closed below, not carried forward.**
2. **QC C (repetition regression).** "testing, examination and clinical review remain..." ran three
   times in thirteen lines in revision 4, where revision 3 had it once. QC traced this to a
   conditional reviewer suggestion ("The short-answer bullet **could become**," `review-2.md:33`)
   being graded as mandated verbatim text. The Section 2 bullet now ends at "before the
   appointment" (`final.md:293`); the clause survives twice, in the protected scope note
   (`final.md:285`) and the Section 3 opener (`final.md:297`), where it does structural work.
3. **QC E-1 (weakened correction).** The Section 3 opener let a reader still attach the three-phase
   list to intake — the exact confusion item 1 exists to remove. Restructured
   (`final.md:297`) so the sentence the list hangs off is unambiguously the screening workflow,
   closer to the reviewer's own "has three phases" wording. The keyword carve-out
   (`occupational health intake process`, `plan.md:199`, this section only) still survives.
4. **QC E-3 (E2 missed its own purpose)**, plus optional QC E-2. E2's stated reason for modifying
   the reviewer's sentence was to avoid stating the fallback twice in three sentences; it stated it
   twice in two instead. Merged to state it once (`final.md:401`). Separately, the Section 2
   definition bullet split into two sentences at zero word cost, so the E4 keyword fold no longer
   sits in a 46-word run. All three carve-out keywords (`digital patient intake`,
   `patient intake forms`, `intake forms`) verified still present.

**Left standing, per QC's own recommendation, not touched by this pass:** R2-1 (the Section 4
repetition between Review 1's protected A5-5 paragraph and Review 2 item 3's reading paragraph) —
QC explicitly says it would leave this one, since the two paragraphs do different jobs and cutting
Review 1's protected text on editorial judgment is the wrong precedent. The three item-6 declines
(R2-2, R2-3, R2-4) — QC's factual-accuracy section (`B`, 5/5) reviewed all three independently and
found the declines correct, R2-2 more clearly correct than the decisions file argued (see that open
item below for the addition QC made to it). All four remain Vadim's calls, listed in Open items.

**Result: this 17/20 was acted on, not filed.** Three of the five `E`-category deductions are fixed
in revision 5; the two structural, judgment-level items (R2-1, item 6's three declines) are exactly
the ones QC said should stay with Vadim, and they are still here.

## Cannibalization check against the live hub

**Carried forward from the rev-2/rev-3 packages, not re-fetched against the live hub this pass —
reasoning stated, not assumed.** The rev-2 section fetched the
[live hub](https://3dlook.ai/content-hub/occupational-health-screening-software/) on 2026-09-04
and read it side by side with `final.md` revision 3, confirming four of the five duplication sites
Review 1 flagged were removed outright and one (the opening scene) was cut by roughly four-fifths
and re-purposed rather than fully zeroed. Neither Review 2 (revision 3 → 4) nor the QC remediation
pass (revision 4 → 5) touched any of that ground. Every change since revision 3 is inside an
existing section and none of it restates hub-owned material:

- Review 2 items 1-7 and E1-E5: heading/cell/paragraph-level edits inside Sections 2, 3, 4, 6, 7
  and 8, as detailed in the rev-3 package.
- QC remediation (this pass): a trimmed bullet in Section 2, a restructured opening sentence in
  Section 3, a merged FAQ answer, and a split definition bullet — all word-level edits inside
  sections that already existed at rev 3.

No section was added, removed, or re-scoped across any of these passes, and no hub-owned block
(buyer roster, the twelve-row does/does-not table, the five-step implementation walk, the
pre-employment-vs-return-to-work table, the BLS "why now" section) re-entered the article. On that
basis, the rev-2 verdict is carried forward rather than re-verified against the live page. If the
hub itself changed since 2026-09-04, this section would not catch it — flagged so the inference is
checkable, not hidden behind "unchanged."

**Verdict, carried forward: substantially resolved.** One residual echo remains flagged, not
certified clean: the Section 1 opening scene (unchanged since revision 3) still shares its
underlying premise with the hub's opening paragraph, cut to roughly a fifth of its original length
and re-purposed toward appointment-slot economics rather than the hub's business narrative. See
Open item 1 below for the one-sentence fix if Vadim wants it at zero.

## SEO checklist

- [x] **Primary keyword in H1, first paragraph, 1-2 H2.** Re-verified against `final.md` revision
      5 directly, line numbers moved again (frontmatter grew further with the QC report and
      remediation `changes_summary`): H1 `final.md:275`, first prose paragraph `final.md:279`
      (byte-identical text since revision 3), one H2 `final.md:311` ("Manual vs digital intake,
      compared dimension by dimension"). `article_lint.py` keyword-placement gate, run this
      session: 4 occurrences, 10 H2s total — unchanged counts, new line numbers.
- [x] **Meta title 57 chars, under 60, primary keyword in the first half.** Re-counted this
      session (see Meta section above).
- [x] **Meta description 150 chars, inside 140-160, keyword once, does not repeat the title.**
      Re-counted this session.
- [x] **Every figure traces to `approved_claims`.** 10 claim markers in the body (`final.md:290`
      x2, `:384` x4, `:386`, `:388`, `:390`, `:395`), covering the same 7 distinct IDs as every
      prior revision (FX-001, FX-003, FX-006, FX-007, FX-008, FX-009, FX-014). `FX-004`
      (`publishable: false`) grepped, zero hits. `article_lint.py` claim-traceability gate, run
      this session: pass, same 7-ID list. QC's factual-accuracy section (5/5) separately confirmed
      the claim set is unchanged and both accuracy formulations remain verbatim from canon.
- [x] **No banned words.** Grepped the body directly (`final.md:275-408`) against the full
      `banned_words` list (leverage, utilize, harness, robust, seamless, comprehensive, delve,
      navigate, tapestry, realm, unlock, unleash, revolutionary, game-changing, cutting-edge) —
      zero hits. Corrective negation ("X, not Y") — grepped, zero hits. **Corrective "rather
      than" — one hit, not zero, unchanged from rev 3's correction.** `final.md:388`: "the
      measurement case therefore rests on repeatability and standardized capture rather than a
      claim of superiority over expert tape measurement." Reviewer-verbatim (Review 2 item 7),
      ruled LICENSED by `seo-editor` under terminology-guardrails Part 1 rule 9, and QC
      independently reviewed the ruling this pass and **explicitly concurred**: "agree, LICENSED"
      (QC report, Output quality section) — the sentence draws the article's single most
      load-bearing claim boundary (FX-001 is measured against expert manual measurement, so
      superiority over that same reference is not available to us), recommended form first,
      limitation second. Per CLAUDE.md §7, this class of judgment sits with the editor, now with
      an independent QC concurrence on record, not with the script. One other soft marker,
      "serve as" (`final.md:285`, the Section 1 scope note), is unchanged since revision 3 and
      separately protected as Review 1 boundary wording.
- [x] **Word count within ±10% of target.** 2,160 words against a 2,050 target = +5.4%, inside
      ±10%. Also inside the reviewer's own binding 1,900-2,200 band — **40 words under the
      ceiling**, not the 14 reported for revision 4 or the 1 reported for revision 3, each of
      which is now stale. Net change from revision 4: -25 words. Per `final.md`'s own `word_band`
      note, the QC fixes paid for themselves: question 2 rewritten to the reviewer's E5 wording
      (-11), the Section 2 verdict bullet trimmed of its third repeated clause (-9), the fallback
      FAQ merged so the fallback is stated once (-8), against the Section 3 opener restructure
      (+3); the definition-bullet split is word-neutral. Confirmed independently: `article_lint.py`,
      run this session, reports `prose_words: 2160` — matches `final.md`'s own frontmatter exactly,
      not just trusted from it.
- [x] **Intro hook in the first two sentences.** Byte-identical since revision 3: concrete scene
      (questionnaire, tape, transcription, clinician) in sentence one, reframe to "manual vs
      digital intake... an operations question about a fixed appointment slot" in sentence two
      (`final.md:279`). Neither Review 2 nor the QC remediation pass touched Section 1's opening
      paragraph.
- [x] **CTA placement per plan; type matches intent.** One CTA, in the closing "Next steps"
      section only, unchanged text since revision 3 (`final.md:408`). Evaluation-framed direct CTA,
      matching the comparison/MOFU intent.
- [x] **No generic AI patterns.** `detect-ai-tells.py`, run by me in this session (output below):
      verdict CLEAN, 0 hard fails, 0 house-rule violations, `ai_density_per_1000_words: 0.86`
      (budget 8.0, severity low) — up marginally from revision 4's 0.85 on the same two soft
      markers against a shorter text, still well inside budget. Rhythm variation improved to 0.66
      (from 0.65), consistent with QC's finding that the repetition regression fix reads better,
      not worse. No em dash anywhere (grepped, 0). `punch_triad_count: 0` per the detector; a
      manual scan of every three-item list in the body found factual enumerations of real workflow
      components, not rhetorical triads — unchanged assessment from rev 3, re-checked against the
      current body.
- [x] **Terminology guardrails.** Grepped the body directly against Part 1/Part 2 of
      `terminology-guardrails.md`: no em dash, no `objective` about our own output, no "the
      reader/audience," no "the following sections," no "see below," no "this article/guide"
      outside the scope note, no `by hand`, no `let`, no `plus` as a connector, no `so` introducing
      a result or benefit. `positioned as` appears exactly once, in the licensed medical-device
      sentence, nowhere else. Presumed-reaction phrasing and concept-as-agent phrasing: none found.
      One licensed corrective `rather than` (see the banned-words row above), now with an
      independent QC concurrence on the ruling.
- [x] **Abbreviations (M1 + exception).** OSHA, NHANES, EEOC, HIPAA, GDPR each expand at first use
      and appear exactly once expanded, re-grepped against revision 5: NHANES `final.md:305`, OSHA
      `:307`, EEOC `:358` (with the licensed bare short form reused once more in FAQ Q4, `:404`),
      HIPAA and GDPR both `:390`. BMI, US, EU bare throughout. NDA spelled out as "non-disclosure
      agreement," never abbreviated. `article_lint.py` abbreviations (M1) gate, run this session:
      pass.
- [x] **Medical framing.** The licensed sentence, verbatim, exactly once: "It is not positioned as
      a medical device." (`final.md:285`, Section 1 scope note.) `positioned as` appears nowhere
      else — confirmed by direct grep this session. Section 8's boundary sentence (Review 2 item 6,
      unchanged by the QC pass) reads "it does not make clearance, eligibility or fitness-for-duty
      determinations" (`final.md:390`) and carries no `positioned as` language.
- [x] **Links on meaningful anchors; external sources neutral and non-vendor.** Nine links checked
      by hand against revision 5's body — same URL set as revision 4, none added or removed by the
      QC pass: internal — hub (x2), accuracy framework (x2), homepage, pricing CTA
      (`article_lint.py`'s internal-links gate: 6 total, 4 distinct); external — OSHA Appendix C
      (osha.gov), CDC/NHANES Anthropometry Procedures Manual (cdc.gov), EEOC enforcement guidance
      (eeoc.gov). QC separately confirmed sourcing is clear: "three external sources, all neutral
      non-vendor." All on descriptive anchor phrases, no bare URLs.
- [x] **AI-tells detector actually run — output pasted below, not estimated.** Ran both gates
      myself in this session (`python3 scripts/article_lint.py .../final.md` and
      `python3 brand-assets/style-guides/scripts/detect-ai-tells.py .../final.md`), independently
      of the editor's frontmatter claim and of QC's own re-run. Both verbatim transcripts below.
      Numbers match `final.md`'s own frontmatter exactly (`ai_density: 0.86`, `prose_words: 2160`,
      `hard_fails: []`, `house_rule_violations: []`, exit 0 both times) and match QC's numbers too
      — three independent runs now agree.
- [x] **Image / alt-text suggestions provided below.**

**SEO checklist: 15/15.** No row changed its pass/fail verdict from the rev-3 package; several rows
changed their *evidence* (line numbers, word count, ai_density) because the QC remediation pass
edited the article and moved the frontmatter.

### `article_lint.py` output, verbatim (run by seo-publisher, 2026-09-07, this session)

```
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
```

Note on `sideways 0` / `down 0`: reporting artifact, not missing links, unchanged since revision 3
— the context pack holds `sideways` and `down` as prose explanations rather than bare URLs by
design. The article carries both as prose links: `https://3dlook.ai/` (Section 8) and
`https://3dlook.ai/pricing/#bd-modal-personalized` (Next steps).

### `detect-ai-tells.py` output, verbatim (run by seo-publisher, 2026-09-07, this session)

```
$ python3 brand-assets/style-guides/scripts/detect-ai-tells.py workspace/seo/articles/2026-09-03-manual-vs-digital-intake-occupational-health/final.md

{"language": "en", "channel": "any", "channel_label": "unspecified", "profile": null,
 "total_words": 2338, "total_markers": 2, "em_dashes_excluded_from_density": 0,
 "ai_density_per_1000_words": 0.86, "density_budget": 8.0, "severity": "low",
 "short_form": false,
 "verdict": "CLEAN — check the positive side (voice, varied rhythm, a stated boundary) and ship.",
 "hard_fails": [], "house_rule_violations": [],
 "markers_by_category": {"avoiding_is": 1, "corrective_contrast": 1},
 "style_metrics": {"em_dashes": 0, "bold_count": 14, "bold_per_1000_words": 6.0,
  "title_case_headings": 0, "emoji_count": 0, "hashtag_count": 1, "bullet_lines": 5,
  "bold_lead_in_bullets": 0, "list_to_prose_ratio": 0.15, "wall_of_text": false,
  "rhythm": {"sentences": 73, "mean_words": 21.1, "variation": 0.66, "monotone": false,
   "uniform_paragraphs": false}, "punch_triads": [], "punch_triad_count": 0},
 "top_offenders": [{"marker": "serve as", "count": 1, "first_line": 285},
                   {"marker": "rather than", "count": 1, "first_line": 388}]}
(exit 0)
```

The two soft markers are `avoiding_is` ("serve as," `final.md:285`, unchanged Section 1 scope-note
phrasing, protected since revision 3) and `corrective_contrast` ("rather than," `final.md:388`,
reviewer-verbatim since revision 4, ruled LICENSED and now QC-concurred — see the banned-words
checklist row above). Both are named and ruled, not silently passed.

### Accuracy discipline, verified against the canon directly (not just the linter's boolean)

Both figures re-checked word-for-word against `brand-assets/product-info/accuracy-formulations.md`
§1.1 and §1.2, unchanged since revision 3:

- Repeatability (`final.md:386`, FAQ Q1 `final.md:395`): "Internal repeatability testing on a
  real-world customer dataset, using five repeated scans per participant, showed strong
  scan-to-scan consistency across the majority of evaluated measurements. For most evaluated
  measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm." —
  verbatim match.
- Accuracy (`final.md:388`): "Internal validation across multiple real-world scan events with
  five repeated scans per person against expert pattern-maker manual measurements shows 3DLOOK's
  measurement accuracy of approximately 96-97% across body metrics, with a typical absolute error
  of 1.5-2.0 cm per measurement, varying by body part." — verbatim match, hyphens not en dashes.
- The two benchmarks never share a paragraph (the repeatability paragraph ends and a new one opens
  "Accuracy is a separate measurement against a separate reference" before the 96-97% figure). No
  ISO 8559 figure anywhere. No per-measurement figures. No `95%+ repeatability` (`FX-004`, marked
  `publishable: false`, confirmed absent). Both figures carry their condition, and the framework
  link (`https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/`) sits in the same paragraph
  as the repeatability figure, not in a separate "further reading" list.

## Content strategy checklist (`content-strategy-guidelines.md` §16)

- [x] **Bound to the right hub.** Occupational Health Screening (Hub 8), Comparison cluster.
      Unchanged since revision 3.
- [x] **`action_type: create-net-new` respected.** Unchanged.
- [~] **Cannibalization guardrail.** See the dedicated section above — carried forward from the
      rev-2 verdict (substantially resolved, one residual echo flagged) on the reasoning that
      neither Review 2 nor the QC remediation pass changed section boundaries or added hub-owned
      material. Marked passing on balance, not on a blanket claim, unchanged since rev 2.
- [x] **Vertical boundary held; scope note present.** Intake and documentation only. Scope note
      (`final.md:285`) unchanged since revision 3. Section 8's boundary sentence, corrected by
      Review 2 item 6 and untouched by the QC pass, states the same boundary — no clearance,
      eligibility or fitness-for-duty determination.
- [x] **Internal links in 4 directions.** up → hub (`final.md:283`, `:380`), trust → accuracy
      framework (`final.md:386`, `:395`), down → FitXpress homepage (`final.md:390`) and the
      pricing CTA modal (`final.md:408`). Sideways remains deliberately absent — its only licensed
      target, the Privacy & Regulatory FAQ, is still unpublished (see Open items). Unchanged since
      revision 3.
- [x] **FAQ section present, GEO/AEO-shaped.** 4 questions (`final.md:394-404`), each answered in
      2-3 sentences. The Q3 answer was merged by the QC pass into a single fallback statement
      (`final.md:401`, QC finding E-3) but stays inside the same 2-sentence shape. None restates
      the hub's FAQ questions or inline Q&As.
- [x] **Negative-scope boundary present; no forbidden positioning claim.** Same structural note as
      rev 2/3: the hub's full does/does-not table is not reproduced by design (Review 1 item 1);
      the boundary is stated twice, briefly — the Section 1 scope note and the Section 8 boundary
      sentence. No forbidden positioning claim found anywhere in the body (re-grepped this
      session).
- [x] **No unsupported medical / legal / underwriting / employment / clinical-trial claim.** OSHA
      and EEOC passages unchanged since revision 3; both leave the determination with the
      reviewing clinician or the program's own counsel. The privacy paragraph (Review 2 item 6,
      untouched by the QC pass) was independently re-reviewed by QC's factual-accuracy section
      (5/5) — see Open items R2-2/R2-3/R2-4 for the three points the reviewer wanted added or
      removed that had no source and remain declined.
- [x] **Owns one distinct search intent.** Method comparison and method choice for occupational
      health screening intake — unchanged, comparison/MOFU, distinct from the hub's BOFU/use-case
      intent.

**Content strategy checklist: 9/9, one item (`~`) passed on a documented judgment call rather
than a clean mechanical check** — unchanged since rev 2, reasoning above. No item in the
positioning/compliance/cannibalization block is a ❌, so this package does not STOP. Consistent
with QC's own scoring, which deducted nothing from this dimension (`D` format & structure 3/3, and
`B` factual accuracy 5/5 covers the compliance/positioning content).

## Alt options

### Meta title variants

1. **Manual vs Digital Intake in Occupational Health Screening** (57 chars) — **recommended.**
   Unchanged since revision 3 (H1 didn't move), keyword first, vertical named in full.
2. Manual vs Digital Intake for Occupational Health Screening (58 chars) — "for" instead of "in";
   marginal difference.
3. Manual vs Digital Intake: Which Method Fits Your Program (56 chars) — leads with the
   decision-framework angle but drops "occupational health screening" from the title itself,
   weakening exact-match keyword strength for a GEO/comparison play.

### Meta description variants

1. **Manual vs digital intake in occupational health screening, compared step by step: workflow,
   cost, exceptions and the metrics to test before switching.** (150 chars) — **recommended.**
   Names four concrete sections of the article's structure, all still present and unrenamed by
   Review 2 or the QC pass (workflow — Sections 3-5; cost — Section 4/6; exceptions — Section 4
   row and FAQ Q3; metrics — Section 7's table). Keyword once, closes on an implied action.
2. Manual vs digital intake in occupational health screening: compare workflow, cost and
   consistency, and see which model your program should pilot first. (151 chars) — leads with an
   imperative, slightly more CTA-forward.
3. A method comparison for manual vs digital intake in occupational health screening: workflow,
   cost, exceptions, and the metrics for testing a pilot. (147 chars) — frames the page as a named
   artifact rather than a question.

## Image and alt-text suggestions

The article carries one text callout for an illustration and no embedded images, unchanged since
revision 3. The Section 4/5 tables carry the comparison visually as tables, so a duplicate diagram
for either is not needed.

1. **Figure 1 (Section 3, "The three phases of the occupational health screening workflow").**
   Heading and callout wording are unchanged from revision 4 — the QC remediation pass restructured
   the *opening paragraph* underneath the heading (QC finding E-1, see above) but did not touch the
   H2 or the figure caption itself. Current callout (`final.md:303`): "**Figure 1.** The three
   phases of the screening workflow, with the remote-capable part marked."

   Design brief: a three-block flow diagram — pre-appointment intake → on-site screening →
   clinical review — with the first block visually marked as the one a remote channel reaches.

   Alt text suggestion: "The three phases of the occupational health screening workflow —
   pre-appointment intake, on-site screening, clinical review — with pre-appointment intake marked
   as the remote-capable phase." No figure or percentage belongs in the alt text; it is published
   copy and a number there is a published claim.

   **Flag for design/production, carried forward unchanged:** if an illustration for Figure 1 has
   already been drafted, or if the Illustrations tab of the source Google Doc has a caption for it,
   both are very likely to still carry the *old* label ("The three phases of occupational health
   intake" / "the remote-capable part" without "workflow"). That wording was current from revision
   0 through revision 3 (2026-09-03 to 2026-09-04) and only changed with Review 2 on 2026-09-07.
   Check before using anything produced against that window.

2. No second illustration is specified this revision, unchanged since rev 2. If design wants one
   for the Section 4 comparison table, keep it decorative (icons for "manual" vs "digital" columns)
   rather than a second data visualization.

Design tokens from `DESIGN.md`: electric blue `#143DFF` for the digital path, navy `#050F40` for
the manual path, Satoshi throughout.

## Open items for Vadim

**Carried forward from the rev-2 package (4):**

1. **The opening-scene echo (see cannibalization section above).** Not blocking. Unchanged since
   revision 3. If you want it at zero rather than "substantially resolved," the fix is a
   one-sentence rewrite of the Section 1 opener dropping the tape/transcription imagery and
   opening directly on the appointment-slot economics.
2. **Compliance-paragraph trim, pending the Privacy & Regulatory FAQ.** The Section 8 compliance
   paragraph (`final.md:390`, same underlying gap since revision 4) is stated at `compliance.md`
   precision rather than linked, because the Data, Privacy, Security & Regulatory FAQ is still
   unpublished (`content-plan.md:24`). When that FAQ ships, trim the paragraph to a link, per
   Review 1 item 7's original instruction, restated by Review 2 item 6. QC separately flagged
   (Output quality, item 4) that this sentence got longer while being trimmed (57 words at
   revision 3, 68 now) and that the reviewer's own proposed form was five short sentences — worth
   revisiting together with the FAQ-link trim rather than as two separate edits.
3. **Two parallel runs collided on this article's files on 2026-09-04** (documented in `log.md`).
   `final.md.conductor-0944-unverified` is a stale, unused artifact from that collision; nothing
   in this package is built from it. Flagging again so it is not mistaken for a version of the
   article.
4. **Medical-framing wording has flipped three times across five files** (2026-06-09 → 2026-08-13
   → 2026-09-02). Correctly applied here (verified above, exactly one instance, the licensed
   sentence), unchanged since revision 3. Still worth stating once as a licensed exception in
   `terminology-guardrails.md` itself rather than as a footnote repeated across documents.

**CLOSED since the rev-3 package (1) — struck, not silently dropped:**

- ~~The Section 7 diligence-question duplication.~~ **Closed by edit in revision 5, not escalated
  to Vadim.** Rev 3's package framed this as two Review-2-sourced pieces of text saying the same
  thing and treated it as an unresolvable overlap requiring Vadim's call. QC established this was
  wrong: editorial refinement E5 instructs reducing the questions to two, one worded "how
  measurement performance was evaluated," and revision 4 had shipped the old, narrower Q5 verbatim
  instead of applying that instruction — a retention, not the reduction the reviewer asked for, and
  the retention is what created the duplication. Revision 5 ships question 2 in the reviewer's own
  E5 words ("How was measurement performance evaluated?", `final.md:378`); the E3 sentence
  underneath now answers it instead of repeating it, with no coverage lost (measurements, sample,
  scan count and reference method are all still named there). `review-2-decisions.md:184` is
  corrected in place with a dated note. This does not need Vadim.

**New from Review 2, still open (3) — plus one QC addition:**

5. **R2-1 — a repetition the two reviews created between them, in Section 4.** The paragraph
   before the table's closing reading paragraph is Review 1's verbatim A5-5 replacement (`final.md:332`,
   "Moving eligible intake steps before the appointment can reduce in-appointment collection and
   transcription. The effect depends on completion rates, fallback volume, integration quality and
   existing rescreen causes.," `plan.md:230`); the paragraph after it is Review 2 item 3's verbatim
   replacement (`final.md:334`, "Manual intake has lower integration requirements..."). Both say
   "reduce transcription" and both close on a "depends on..." list. **QC reviewed this one directly
   and recommends leaving it as is** — the two paragraphs do different jobs (mechanism vs. balanced
   reading) and cutting Review 1's protected text on editorial judgment alone would be the wrong
   precedent, unlike the Section 7 item above, which the reviewer's own words already resolved.
   **One-line fix if you want it anyway:** drop the second sentence of the A5-5 paragraph ("The
   effect depends on...," 17 words) — the newer paragraph's own dependency list supersedes it.
6. **R2-2 — "processes no personal identifiers": keep or cut?** Review 2 wants it removed unless
   confirmed for every deployment. `compliance.md:23` states it flatly ("None — photos cannot be
   linked to individuals via 3DLOOK"), and it is repeated in `proof-points.md:137` and
   `how-it-works.md:56`; Review 1 already checked and kept it. `seo-editor` declined the removal on
   source-of-truth grounds, and **QC's factual-accuracy review makes the decline stronger than
   originally argued**: the sentence is not just standing approved language, it is the text of
   **approved claim FX-014 itself** (the context pack's own claim text reads "no personal
   identifiers processed"), and the sentence carries the `<!-- claim: FX-014 -->` marker at
   `final.md:390`. Cutting it would put the article out of sync with the claim ID it cites, and
   `article_lint.py`'s traceability gate would still pass silently. **If the answer is cut, it
   needs to come out of four places in the same move, not just this article: `compliance.md`,
   `proof-points.md`, `how-it-works.md`, and the context-pack claim text for FX-014** — QC notes
   two packs on disk already carry the unscoped phrase and would regenerate it otherwise.
7. **R2-3 — GDPR controller/processor allocation. RESOLVED 2026-09-07, no longer an open item.**
   The decline stood on one condition: *"it belongs in `compliance.md` first, then this article can
   cite it."* Vadim ruled on 2026-09-07 that the sentence is canonical, and `compliance.md` now
   carries it under "GDPR roles". The body was updated in the same move: the GDPR clause left the
   comma chain and the approved sentence stands on its own, hedge intact. Review 1 §B's instruction
   never to strengthen "follows GDPR principles" is superseded by the ruling, not bent by the
   article. Scope: the ruling covers the roles sentence only, not Article 28 DPA, Standard
   Contractual Clauses, the UK Addendum or Article 9.
8. **R2-4 — retention of generated outputs: add or not?** Review 2 wants output retention stated
   ("generated outputs are retained according to the agreed deployment terms"). `compliance.md`
   documents photo retention only ("removed immediately after processing or within 30 days, per
   client policy") — nothing on how long the measurement outputs themselves are kept. Not added;
   the existing photo-deletion sentence is already more precise than the reviewer's proposed
   replacement, and the output-retention half has no source. QC agrees the decline is right and
   adds a content-level note: an article about durable documentation stating a retention policy for
   photos and nothing about the measurement outputs (the records that actually persist) is worth a
   line in `compliance.md` on its own merits, independent of whether Review 2's specific sentence
   ships.

## Article

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
