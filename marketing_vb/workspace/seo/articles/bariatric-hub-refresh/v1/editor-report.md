---
slug: bariatric-pre-qualification-mobile-3d-body-scanning
workspace: bariatric-hub-refresh
artifact: editor report for draft-v2-editor.md
stage: edit (checkpoint 1 closed, approved 2026-09-03)
author_agent: seo-editor
created: 2026-09-03
input: draft-v1-writer.md
output: draft-v2-editor.md
gate: PASS (scripts/article_lint.py, 9/9 gates, 2026-09-03 pack)
next: seo-publisher
---

# Editor report, Bariatrics hub refresh

Four passes plus the AI-tells sweep, run in order, on `draft-v1-writer.md`. Output at
`draft-v2-editor.md`. The linter is green on all nine gates. Everything below is either a
substantive change the publisher or a fact-checker needs to see, or an open item that leaves
this stage unresolved.

---

## 1. Final gate status

```
python3 scripts/article_lint.py workspace/seo/articles/bariatric-hub-refresh/draft-v2-editor.md \
  --pack workspace/seo/_context-packs/2026-09-03-bariatric-hub-refresh.yaml --report
```

`VERDICT: PASS`, 9/9.

| Gate | Result | Movement against draft v1 |
|---|---|---|
| hard bans (detect-ai-tells, channel `article`) | ok. `CLEAN` | ai_density 0.69 -> **0.36** (budget 6.0); rhythm variation 0.53 -> **0.57**; em/en dashes 0 -> 0 |
| prose length | ok. 4,712 vs target 4,400 (band 3,740-5,060) | 4,939 -> 4,712 all-in; 4,500 -> 4,316 excluding table cells |
| claim traceability | ok. `FX-001, FX-002, FX-005, FX-006, FX-007, FX-008, FX-009` | unchanged set; one new `ext-claim` id added (`ASMBS-ESTIMATE-2023`) |
| banned claims | ok | unchanged |
| superseded figures | ok | unchanged |
| internal links | ok. 18 links, 10 distinct, `{up: 1, sideways: 6, down: 1, trust: 1}` | unchanged. All four directions intact |
| keyword placement | ok. H1, first paragraph, H2 #6 | 7 -> 6 occurrences (a trimmed FAQ sentence), still above the gate |
| abbreviations (M1) | ok | CDC now expanded at first use; the AWS abbreviation removed rather than expanded |
| accuracy discipline | ok. figures present, framework linked from every figure paragraph | unchanged |

Detector soft markers remaining: `2x 'facilitated'`. Both are inside the proper noun
*Federally Facilitated Exchange* and are not touchable.

---

## 2. Per-section word counts

`prose_words` (the linter's number) counts table cell text. The plan's per-section targets read
as prose targets, so both columns are here, as in the writer's notes.

| Section | Branch B target | v1 all | v1 ex-tables | **v2 all** | **v2 ex-tables** |
|---|---|---|---|---|---|
| Front matter (H1, opening, Use Case Summary, disclaimer) | 300 | 380 | 280 | **363** | **269** |
| 1. The bariatric intake gap | 360 | 367 | 367 | **369** | **369** |
| 2. Short answer | 180 | 179 | 179 | **179** | **179** |
| 3. Why now (1): the 7-calendar-day clock | 420 | 400 | 400 | **394** | **394** |
| 4. Why now (2): GLP-1 and the funnel | 400 | 421 | 257 | **401** | **268** |
| 5. Why now (3): current BMI vs qualifying history | 350 | 362 | 362 | **354** | **354** |
| 6. The pre-qualification workflow | 360 | 345 | 345 | **344** | **344** |
| 7. Where FitXpress fits | 280 | 324 | 270 | **322** | **268** |
| 8. Patient progress tracking | 400 | 406 | 406 | **390** | **390** |
| 9. What improves, and what it does not do | 250 | 281 | 281 | **270** | **270** |
| 10. Comparison, buyer fit, pilot diligence | 300 | 446 | 325 | **430** | **315** |
| 11. FAQ | 700 | 945 | 945 | **791** | **791** |
| 12. Next steps and related reading | 100 | 83 | 83 | **105** | **105** |
| **Total** | **4,400** | **4,939** | **4,500** | **4,712** | **4,316** |

**The two totals cannot both land on 4,400, and the brief asks for both.** Cutting 539 words
from the all-in number puts the ex-table number at roughly 3,960; landing the ex-table number
on 4,400 leaves the all-in number near 4,800. The split above is the compromise: **4,316
ex-tables, 1.9% under target**, and 4,712 all-in, inside the linter's band. Every mandated
table (Use Case Summary, market indicators, pathway stages, comparison) is intact and accounts
for 396 words of the gap between the two columns.

### The FAQ could not reach 700, and here is the arithmetic

| Component | Words | Compressible? |
|---|---|---|
| 16 question headings | 144 | No. They are the search-query surface |
| 4 block sub-headings | 13 | No |
| H2 | 4 | No |
| 16 answers | 630 (avg 39) | Partly. Floor reached |
| **Total** | **791** | |

Every answer is now **2 to 4 sentences**, inside the guidelines §14 range, and the average
dropped from 45 words to 39. Reaching 700 needs the 16 answers at 539 words, an average of 33.
Five answers cannot go there without losing mandated content:

- **Q4, 59 words.** Carries the whole CMS-0057-F scope statement, which the brief requires in
  the answer itself: the four impacted payer classes, the ERISA exclusion, and Medicare
  fee-for-service.
- **Q10, 42 words.** Carries FX-002 verbatim (25 words on its own) and the framework link.
- **Q15, 48 words.** Carries 58.2% / 23.4% / 11.9% against the 270,089 total plus the
  methodology footnote, per the ruling on the sleeve share.
- **Q13, 49 words.** Four separate boundary statements, unstacked per guardrail M2.
- **Q5, 49 words.** The 8% figure, the operational consequence, and the "program and payer
  decide" boundary.

Those five cost 247 words. The remaining eleven average 35. Dropping questions was ruled out,
so 791 is where prose-tightening ends. The FAQ is now **16.8% of the article**, against 32% on
the live page, which was the structural defect being fixed.

**Section 10** is 430 all-in / **315 prose against a 300 prose target** (+5%). The 115 words of
table cells belong to the mandated five-row comparison, and the three evaluation bullets carry
FX-009, FX-005 and FX-006 in full. Front matter is 363 all-in / **269 prose, under its 300
target**; the 94-word gap is the Use Case Summary table the plan requires at the top.

---

## 3. Pass 1, citation dedup

Three sources were cited more than once in v1. Each is now linked exactly once.

| Source | v1 | v2 | How the second mention reads |
|---|---|---|---|
| ASMBS 2025 Fact Sheet (PDF) | S1, S4 table, FAQ Q15 | **S1 only**, on "about 1% of those who meet eligibility requirements" | S4 now cites the ASMBS estimate page instead (see §4); FAQ Q15 no longer touches the PDF at all |
| ASMBS release, 5 May 2026 (untreated share) | S1, S4 table | **S1 only** | The S4 "Untreated share" row is deleted. It republished S1's 90-95% figure and its link, and it was not a volume series, which is what the table is for |
| ASMBS estimate of bariatric surgery numbers | not used in v1 | **S4 table only** | FAQ Q15 attributes the procedure split to "ASMBS's national estimate" in prose and ties it to the same 270,089 total, without a second hyperlink |

**One deliberate exception.** The accuracy framework
(`/content-hub/mobile-body-scanning-accuracy/`) stays linked **three** times, in Section 7,
Section 8 and FAQ Q10. The accuracy-discipline rule requires the framework link inside every
paragraph that carries an accuracy figure, and gate 9 checks it. Dedup loses to that rule.

Also unchanged: the five sideways and down targets each appear twice, once in the body and once
in the Section 12 related-reading list. That is site navigation, not citation stacking.

---

## 4. Substantive figure changes, and the one that needs a fact-checker's eye

### a) Section 4, the national volume anchor

v1: *"More than 270,000 procedures, down about 3.5% from the prior year (ASMBS 2025 Fact Sheet)"*.
v2: *"270,089 procedures, down about 3.5% from 279,967 in 2022 ([ASMBS estimate of bariatric
surgery numbers])"*.

Reason: gap analysis §3b, which the brief made binding, states that the Fact Sheet PDF carries
its year-by-year numbers **as a graphic**, so they cannot be quoted from it, and names the
estimate page as the extractable source. The exact figures are stronger than the rounded ones
and they make FAQ Q15's split commensurate with the total.

### b) FAQ Q15, the sleeve-gastrectomy share

Per the ruling, the qualitative "more than half of annual volume" is gone. The answer now
carries **58.2%**, gastric bypass **23.4%** and revisions **11.9%** against the 270,089 total,
with the methodology footnote referenced.

**Open item for the publisher, one-line fix either way.** The ruling says "cited to that page",
and Pass 1 says one link per source. I chose the contextual attribution: Q15 says "ASMBS's
national estimate" and the hyperlink for that estimate sits in the Section 4 table, 2,000 words
above. If the preference is a live link inside the FAQ answer for GEO liftability, the edit is
to wrap *ASMBS's national estimate* in
`[...](https://asmbs.org/resources/estimate-of-bariatric-surgery-numbers/)`. Nothing else moves.

### c) Four figures now on the page that are not in the pack

`270,089`, `279,967`, `58.2%`, `23.4%` and `11.9%` come from **gap analysis §3b**, which was
added after the pack was built. The pack's `banned_claims` includes "any number not in
approved_claims or external_citations", so on a literal read of the pack these are
unauthorised, and on the brief's read (§3b is binding) they are required. **Recommendation:**
add a `verified_current_keep` entry to the pack for the ASMBS estimate page before the article
is published, so a later fact-check does not re-litigate this.

### d) The `utilization` noun differs from the source, flagged for the fact-checker

The JAMA Surgery finding is published by its source as a change in **utilization**.
`utilize`/`utilization` is a CLAUDE.md §6 banned word, so the page says "change in surgery
use", "surgery use down 34.1%" and "a rate of use within that cohort". The scope words that
carry the meaning are intact in every instance: a rate, not a count; one insured claims cohort;
absolute counts move about 7.3% lower. **A fact-checker reading the source will see a different
noun for the same measure.** Ruling 3 approved this; the note is here so nobody treats it as
drift.

### e) Scope restored to one figure

v1 had trimmed "before the pandemic" off the 8.9% single-centre attrition figure during
drafting. Restored, because a percentage without its scope is guardrail #4.

---

## 5. The three volume series, re-verified after editing

- ASMBS national estimate (270,089 in 2023, down about 3.5% from 279,967 in 2022, series ends
  2023) and the JAMA Surgery 2026 cohort never share a sentence. They sit in separate rows, and
  the paragraph under the table states the incomparability in ASMBS's own terms.
- Every cohort figure carries "one insured claims cohort" or "the same claims cohort".
- `-34.1%` is labelled a rate, with "absolute counts in the same cohort move about 7.3% lower"
  beside it.
- The `230,207 / 177,297` series does not appear. §3b's own note applies: the ASMBS series puts
  2022 at 279,967, so that report is not this series under any reading.
- "Surgery appears to be rebounding" does not appear. Neither does the semaglutide ex-US
  exclusivity angle, nor the KFF employer-coverage figure.

**Guardrail #2, byte-identical across body, table and FAQ** (verified by count, frontmatter
excluded): `7 calendar days` x2 and `7-calendar-day` x4 (adjectival form only), `72 hours` x2,
`1 January 2026` x2, `90-95%` x1, `about 8%` x3, `less than 1 cm` x2, `96-97%` x1,
`1.5-2.0 cm` x1, `±3.5%` x1, `150 to 220 cm` x1, `38 to 210 kg` x1, `16 to 78` x1, `270,089`
x2, `58.2%` x1, `40.3%` / `9.4%` x1 each. No variant spellings.

**CMS-0057-F scope** appears twice with its full reach, in Section 3 paragraph 2 and in FAQ Q4:
Medicare Advantage, Medicaid, CHIP, Federally Facilitated Exchange Qualified Health Plans; not
all commercial ERISA plans; Medicare fee-for-service uses no prior authorization for bariatric
procedures.

**Attrition** stays a measurement-dependent range (60% / 22.25% / 36-76% / 39-70% / 8.9%) with
"depends on program design and on how it is counted". No "50-60% as typical".

---

## 6. Pass 2, structure and flow

- **Section 3 into Section 4** had no bridge; Section 4 opened cold on "Three data series
  describe...". Now: *"The clock tightened while the funnel feeding it changed shape."*
- **Section 4's own frame was wrong.** It announced three data series and printed four rows, two
  of which were the same series. Now three indicators from two measurement systems, which is
  what the sources support, and the fourth row's argument went back to Section 1 where it lives.
- **Section 10 opened on a bare table.** In the buyer's decision section that is a gap. Added
  the workflow-comparison framing, and the section now closes on a stated boundary ("neither
  method replaces the other") instead of "the output of the comparison is a division of labour".
- **Intro** kept its two-sentence reframe. The third sentence was a comma-spliced appositive
  three clauses deep; the verification stack is now a colon list.
- **Conclusion** gained a concrete first step (map one payer's packet requirements against what
  the file already holds on the day of the consult) ahead of the single CTA.
- No `Furthermore` / `Moreover` / `Additionally` anywhere, at either draft stage.

---

## 7. Pass 3, expert voice

Eleven sentences rewritten. The ones worth naming:

| Was | Now | Why |
|---|---|---|
| "Seven calendar days inverts the documentation argument." | "Window length changes what the documentation has to do." | Behaviour attributed to a duration (guardrail Part 1 #6) |
| "A program's payer mix therefore decides how much of its volume sits on this clock." | "How much of a program's volume sits on this clock depends on its payer mix." | Same, plus it is now an explicit `depends on` relationship (Part 1 #4) |
| "The compliance posture holds at procurement, and its detail belongs with the pilot diligence." | "The third is the compliance posture. Its diligence questions belong with the pilot evaluation." | Compressed relationship, and it read as filler |
| "Accuracy on this page means one specific comparison." | "One accuracy figure applies here, and it comes from one specific comparison." | Self-referential page language, the same shape as the banned `this article` |
| "it carries a ±3.5% average error margin and is a software estimate, not a reading from a calibrated scale" | "it carries a ±3.5% average error margin as a software estimate, and a calibrated scale remains the reading where a protocol requires one" | Corrective "X, not Y" reframed into the positive with the boundary intact |
| "Audit-ready records are a property of how the data was captured" | "Whether those records are audit-ready follows from how the data was captured" | Category error: records are not a property |
| "medications can serve as a bridge" | "for some patients a medication becomes a bridge to surgery later" | Detector soft marker, and vague |
| "The technology behind the capture..." + "takes the place of" | "replaces" | Two words doing the work of five |

**Repetition, fixed.** Four phrases repeated three or more times in v1: *"in the file, dated
when"* (x3), *"the capture sequence is the same"* (x4), *"the capture-quality outcomes from the
guided flow"* (x3), *"the companion guide to"* (x5, one per down-link landing sentence). Each
down-link sentence now has its own phrasing, and the only 5-gram still repeating three times is
the primary keyword phrase *"a bariatric patient progress record"*, which is deliberate.

**Rhythm.** Six paragraphs held adjacent sentences of the same length, which is the signature of
prose written to a template. All six split. The monotone-pair count is now zero; the detector's
rhythm variation moved 0.53 -> 0.57.

**Caveats kept and added.** The FX-005 population limit against a severe-obesity intake
population, the payer-mix dependency on CMS-0057-F exposure, "none of this shortens the payer's
own clock", the anti-manipulation controls stated with their limit in the next sentence, and
manual measurement holding its ground where a clinician needs a hand on the landmark. No
presumed-reaction constructions, at either stage.

**What was not added.** No first-person voice and no `you`. The pack's register is buyer framing
without `you`-spam, and `we/our` is licensed only for a claim of ownership; ownership is stated
in the third person ("3DLOOK's measurement accuracy"), which matches the corpus. No customer
proof point either, because none exists for this vertical (see §11).

---

## 8. Pass 3b, content strategy compliance

| Check | Result |
|---|---|
| Positioning §8, no forbidden claim | ok. No diagnosis, no treatment / underwriting / hiring / clearance decisioning, no replacement of clinician / DXA / reference method, no compliance guarantee, no fraud detection, no standalone medical authority. "Fraud-prevention support inside a human review process" only |
| "What FitXpress does not do" section present | ok. Section 9, seven separate statements, one negation each (guardrail M2). Closes on the licensed *"It is not positioned as a medical device."* |
| Vertical boundary §9 | ok. No clinical outcome of surgery anywhere. Branch B's three basics questions carry none: benefits, side effects and pros-and-cons did not return. No qualifying BMI, no payer threshold, no procedure recommendation |
| Sensitive vertical, scope note early | ok. Italic disclaimer before Section 1, verbatim except `described here` (ruling 1) |
| Cannibalization §5 | ok. GLP-1 market economics, telehealth workflow, BMI-verification mechanics, body-composition methodology and multi-site consistency are all linked, not re-explained. No KFF figure |
| Internal links §11, four directions | ok. `{up: 1, sideways: 6, down: 1, trust: 1}`, 18 links across 10 distinct targets. Privacy / regulatory FAQ stays plain text, marked not yet published |
| Down-link landing anchors | ok. **7** `DOWN-LINK LANDING` comments, greppable, covering all five P1 children, the P2 remote-intake child and the P2 checklist lead magnet |
| FAQ §14 | ok. 16 questions, every answer 2 to 4 sentences, includes "what FitXpress does not do" (Q13) and "used for decisioning?" (Q11) plus "who reviews?" (Q12) |
| CTA §15 | ok. One CTA, Section 12, BOFU-direct demo to `/for-bmi-verification/`, no self-serve trial, no mid-body second CTA, no pricing |

---

## 9. Pass 3c, AI-tells sweep

Detector run against the hard-bans card and then the soft categories the detector cannot see.

- **Hard categories, 11 of 11 clean.** `hard_fails: 0`, `house_rule_violations: 0`, verdict
  `CLEAN`, density 0.36/1000 against a budget of 6.0. Zero em or en dashes, in either draft.
- **Judgment rows, run by hand against `terminology-guardrails.md` Part 3.** Corrective negation
  survives in four places and each is a real boundary, which is the licensed exception: the Use
  Case Summary `Role` row (plan-mandated wording), "Not a national count" in the market table (a
  methodological boundary that the two-series rule requires), "The mechanism here is not clinical
  decision-making" (the protected mechanism paragraph), and the Section 9 boundary list.
  Corrective `rather than`: **zero occurrences** in the article body, at either stage. `we/our`: zero. `you`: zero.
  No bare URLs, every link on a meaning-carrying anchor. Vendor blogs as sources: none. The external
  sources are CDC (two documents), ASMBS (four documents), CMS, PubMed Central, Johns Hopkins,
  the American College of Surgeons, and EurekAlert (the AAAS press service, which is the pack's
  own locator for the JAMA Surgery figures). Compressed relationships: two rewritten into `depends on`.
- **Soft categories.** Elegant variation found and fixed: one thing was being called "the
  quality outcomes the guided flow returns", "capture-quality outcomes" and "quality outcomes"
  in three sections; settled on the one term. No empty participial tails (`, ensuring...`,
  `, allowing...`): zero matches. No inflated significance (`crucial`, `critical`, `pivotal`,
  `significant`): zero matches in prose. No false ranges.
- **Positive checks.** Concrete over abstract: every section carries a dated figure, a named
  source or a disclosed limit. Acknowledged difficulty: the attrition spread is presented as the
  argument, and the accuracy figure is presented as a question about tolerance. Named boundary:
  Section 9 in full, plus the payer-scope limit and the validation-population limit. Stated
  position: the attrition paragraph, "first-pass completeness is the one variable a program
  controls", and "neither method replaces the other".
- **Self-check answers** are in the draft's `self_check` frontmatter field, and the fixes they
  produced are in §7 above. The second pass is where five of the eleven sentence rewrites came
  from.

---

## 10. Pass 4, final polish

- **Banned words.** Zero hits on the pack's list and on `utilize` / `utilizing` /
  `utilization`. Also checked by hand and clean: `plus` as a connector, `so` introducing a
  benefit, `let`, `by hand`, `this article` / `this guide`, `objective` about our own output,
  `positioned as` outside the one licensed medical-device sentence.
- **Abbreviations (M1).** CDC now expanded as *Centers for Disease Control and Prevention (CDC)*
  at first use, which v1 had left bare. The AWS abbreviation was removed rather than expanded
  ("Amazon Web Services S3"), because it was never used again in short form. Already correct in
  v1 and left alone: GLP-1, CHIP, ASMBS, CMS-0057-F, DXA, BIA, HIPAA, GDPR, BMR, Transport Layer
  Security, ERISA and Federally Facilitated Exchange spelled out. BMI, US, EU stay bare per the
  2026-08-25 override.
- **Stacked negation (M2).** Two fixed. Section 3 paragraph 2 had "It does not cover every
  commercial plan... and Medicare fee-for-service does not use prior authorization..." in one
  sentence; now two sentences, one negation each. FAQ Q13 had a four-item negation plus a second
  "does not guarantee" clause in the same sentence; now four sentences. The Section 9 boundary
  list was already one negation per sentence and was not touched. The disclaimer's single
  negation with a four-item list is the approved wording and stands.
- **`guarantee` phrasing.** A shorter draft of Q13 read "It offers no guarantee of compliance",
  which the linter's `guaranteed compliance` core would have fired on, since its lookbehind only
  licenses `not ` and `does not `. Kept as "It does not guarantee compliance or an approval".
- **Accuracy discipline.** FX-001 and FX-002 are verbatim from `accuracy-formulations.md`,
  hyphens and all; repeatability reads `less than 1 cm`; the two benchmarks never meet, because
  the ISO 8559 figure is absent from the page per audit §C, along with FX-004 and FX-010; every
  figure paragraph links the framework article; no reserved word (`independent`, `third-party`,
  `validated`, `clinically validated`, `peer-reviewed`) is used about our own evidence except
  inside FX-006, which is the licensed negative statement. `DXA`, never `DEXA`.
- **Numbers.** Every figure traces to `approved_claims`, `external_citations`, or gap analysis
  §3b. The §3b ones are listed in §4c above with the pack-update recommendation.
- **Keyword placement.** `bariatric pre-qualification` in the H1, the first paragraph, and H2 #6.
  Six occurrences overall, down from seven where a trimmed FAQ sentence dropped one.

---

## 11. Open items handed to the publisher

1. **`external_claims:` is missing from the context-pack schema** (writer's item 5, left as
   ruled). The article carries 16 `<!-- ext-claim: SOURCE-ID -->` markers across ten source ids,
   because gate 3(b) demands a marker on every prose line with a figure and gate 3(a) only
   resolves ids in `approved_claims`, which holds FitXpress claims only. **Recommendation:** add
   an `external_claims:` block to the pack shape with ids the linter can resolve, the same way
   `approved_claims` works, and teach `context-pack-builder` to emit it. Every article with
   third-party statistics hits this, and the marker convention is currently a workaround that
   looks like a claim id without being one.
2. **Pack entry for the ASMBS estimate page** (§4c). Five figures on the page come from gap
   analysis §3b rather than the pack, and the pack bans numbers it does not carry.
3. **FAQ Q15's link** (§4b). One-line edit if a live link inside the answer is preferred over
   the contextual attribution.
4. **No named bariatric customer story.** Unchanged from the writer's finding and not fixable at
   the editing stage: no bariatric case study exists in `case-studies/` or `proof-points.md`.
   Every operational claim on the page rests on a third-party citation or a disclosed internal
   limit, which is the one respect in which this hub still reads thinner than the insurance and
   wellness hubs. Audit Open Item #4.
5. **`sales@3dlook.ai` vs `@3dlook.me`** (writer's item, unresolved). Left at the live-page
   address. Needs someone with authority over the published contact.
6. **CDC *Preventing Chronic Disease* wording** is still carried in the live page's phrasing
   ("underestimated the prevalence of severe obesity by 40%") and the plan asked for it to be
   re-verified at fact-check. Still open.
7. **The mid-body eBook block stays omitted** (audit Open Item #10). One CTA, in Section 12.
   Restoring it is a paste and it belongs to Vadim or the publisher.
8. **Six of seven `DOWN-LINK LANDING` anchors have no link yet**, by design. `grep "DOWN-LINK
   LANDING"` finds all seven; each comment names the child that takes the anchor over when it
   ships.

## 12. Nothing reintroduced

Verified by grep against the ledgers: no `ISO 8559` / `0.40 cm`, no `95%+`, no per-measurement
girth figure, no `SOC 2`, no pricing, no market sizing, no `DEXA`, no `230,207` / `177,297`, no
semaglutide angle, no KFF figure, no `33 million`, no `50-60%`, no "rebounding", no competitor
name, no clinical outcome of bariatric surgery. Audit §C, §D and §N all hold.
