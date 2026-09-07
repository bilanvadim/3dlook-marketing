---
qc_date: 2026-09-07
agent: seo-editor + seo-publisher (Review 2 application pass)
artifact: workspace/seo/articles/2026-09-03-manual-vs-digital-intake-occupational-health/final.md
secondary_artifact: workspace/seo/articles/2026-09-03-manual-vs-digital-intake-occupational-health/publish-package.md
track: seo
artifact_type: seo-final
revision: final.md rev 4 / publish-package.md rev 3
total_score: 17/20
status: good
scope: judgment only
prior_report: 2026-09-03-seo-full-manual-vs-digital-intake-occupational-health.md (19/20)
coordinator_review: >
  Accepted, and QC earned its place on this run. Finding A-1 is the one that mattered: the
  Section 7 "duplication" we were about to hand Vadim as an unresolvable reviewer-vs-reviewer
  conflict was neither unresolvable nor a conflict - E5 was retained rather than applied, and my
  own decisions file graded that row "Verbatim" and so licensed the mistake downstream. Both the
  row (:184) and my stale gate transcript (section 9) are corrected in place with dated notes,
  not silently. Findings A-2, A-3 and A-4 fixed in revision 5: prose 2,160, both gates re-run at
  exit 0 by editor, coordinator and publisher independently. QC's ruling on the three item-6
  declines (R2-2 / R2-3 / R2-4) is stronger than my own reasoning was - it caught that
  "processes no personal identifiers" is the literal text of approved claim FX-014 in the
  context pack, so deleting it would desync the article from a claim ID it still cites while
  traceability passed. That argument is now the one carried to Vadim. R2-1 stays open: QC agrees
  it is the one genuine reviewer-vs-reviewer call and not ours to settle. Two of QC's additions
  to the escalation are adopted verbatim - the R2-2 fix list must also cover the FX-014 claim
  text or the next context pack regenerates the phrase, and R2-4 is a content gap as much as an
  asset gap, since an article about durable documentation states photo retention and nothing
  about output retention. Standing lesson for the pipeline, and it is mine, not the editor's:
  an agent applying a review reads the decisions file, not the review, so a decisions row that
  summarises an instruction loosely becomes the instruction. Grade rows against the reviewer's
  words, and where a row says "verbatim", quote the words.
---

# QC Report — Review 2 application pass — 2026-09-07

**Artifact:** `final.md` revision 4 + `publish-package.md` revision 3
**Total: 17/20** — good
**Prior: 19/20** (`2026-09-03-seo-full-...md`) — delta −2

**Read the delta with care: the two reports are not scoring the same text.** The 2026-09-03
report describes a 2,745-word, 12-H2 article with an unresolved sideways-link placeholder and the
disputed "FitXpress is not a medical device." That is the pre-Review-1 article (revision 2), not
revision 3. Both defects it deducted for are gone. The −2 is not a regression against that
report's findings; it is three new deductions, two of which this pass created.

**Scope: judgment only.** Both gates were run three times today (`article_lint.py` PASS/exit 0,
9 gates; `detect-ai-tells.py` CLEAN/exit 0, 0 hard fails, ai_density 0.85 vs budget 8.0). Not
re-litigated. Sourcing rule checked and clear: three external sources, all neutral non-vendor
(osha.gov, cdc.gov, eeoc.gov).

## Scores

| # | Category | Score | Max | vs prior |
|---|----------|-------|-----|----------|
| A | Adherence | 4 | 5 | −1 |
| B | Factual accuracy | 5 | 5 | = |
| C | Brand & tone | 2 | 3 | −1 |
| D | Format & structure | 3 | 3 | = |
| E | Output quality | 3 | 4 | = |

## Verdict on the pass itself

**Applying Review 2 improved the article's accuracy and cost it prose.** Five real defects are
gone: BMI stated as a subset of the 80+ measurements (a genuine sourcing error, `proof-points.md:57`
vs `:58`), "time-stamped at capture" over-specified against `use-cases/fx-occupational-health.md:10`,
five absolute table cells, an unsourced "for most programs" prevalence claim, and a boundary
sentence that contradicted the article's own intake-layer framing. Against that: two duplications
knowingly shipped, one repetition regression, one weakened correction, and a compliance sentence
that got longer while being trimmed. Net positive, and the second half was avoidable.

## What was wrong (specific)

### A. Adherence — 4/5

1. **E5 is recorded as "Verbatim" and is not.** `review-2.md:97` instructs: reduce the five
   questions "to the two broader diligence questions: which components move, and **how measurement
   performance was evaluated**." What shipped as question 2 (`final.md:338`) is the old, narrower
   Q5 text: *"How was repeatability measured: over how many repeated scans, on which measurements,
   and against which reference?"* `review-2-decisions.md:179` grades this **Verbatim**. It is a
   retention, not an application — and it is the direct cause of the Section 7 duplication that was
   then escalated to Vadim (`publish-package.md:432-441`) as an unresolvable reviewer-vs-reviewer
   conflict. It is not unresolvable; the reviewer supplied the wording that dissolves it.
2. **The binding decisions file was never reconciled with the artifact it binds.**
   `review-2-decisions.md:189-200` states the gates were run "in this session" against the edited
   file and reports **"Prose 2,173 words"**, **"a net −26"**, and rhythm variation **0.66**.
   `final.md`'s own lint transcript and the publisher's independent re-run both report
   **2,185**, net **−14**, variation **0.65**. §0 says "20 scripted replacements";
   `final.md:112` says "22 replacements". The article's numbers are the correct ones, but a file
   whose header reads *"Where this file and review-2.md disagree, THIS FILE WINS"* now carries a
   gate transcript that never described the shipped file, and nothing in the pass caught it. The
   publisher re-verified the word count against the **rev-2 package** and not against the decisions
   file it cites as binding.

Everything else in A is clean and unusually well evidenced: 21/21 instructions actioned, protected
tables diff-verified byte-identical against `plan.md:251-257` and `:302-311`, every replacement
asserted `count == 1`, gates pasted rather than asserted, and the publisher self-corrects rev 2's
false "zero `rather than`" claim (`publish-package.md:22-29`) instead of carrying it forward.

### B. Factual accuracy — 5/5

No unsourced figure, no invented client, no anti-positioning lead. Claim set unchanged at seven
IDs; both accuracy formulations verbatim from canon with their references; FX-004 absent.

**The three declines are correct, and R2-2 is more clearly correct than the decisions file argues.**
The pass treats "processes no personal identifiers" as standing approved compliance language. It is
more than that: it is the text of **approved claim FX-014** itself
(`_context-packs/...yaml:29` — *"no personal identifiers processed"*), and the sentence carries the
`<!-- claim: FX-014 -->` marker at `final.md:350`. An editor deleting it would put the article out
of sync with the claim ID it cites, and `article_lint.py`'s traceability gate would still pass —
silently. The reviewer's objection is a hypothetical ("session identifiers **can** make such a
statement difficult to maintain"), and the counter-evidence is three assets stating it flatly
(`compliance.md:23`, `proof-points.md:137`, `how-it-works.md:56`). **Decline: right.** R2-3
(controller/processor) and R2-4 (output retention) are also right to decline — both add allocations
no asset carries, which is the same class of error Review 2 spends items 4 and 5 correcting.

Two additions to the escalation, both missing from `publish-package.md:442-462`:
- The R2-2 fix list names `compliance.md`, `proof-points.md`, `how-it-works.md`. It should also
  name the **context-pack claim text for FX-014**, or the next pack regenerates the phrase; two
  packs on disk already carry it.
- R2-4's residual is a **content** gap, not only an asset gap: an article about durable
  documentation states a retention policy for the photos and nothing about the measurement outputs,
  which are the records that persist. Declining the reviewer's unsourced sentence is right;
  the silence is still worth a line in `compliance.md`.

Noted, not deducted: `compliance.md:23` scopes its own claim (*"None — photos cannot be linked to
individuals via 3DLOOK"*) while the article ships the unscoped form. Since the unscoped form is the
approved claim text, this is Vadim's call at the asset, exactly where the pass routed it.

### C. Brand & tone — 2/3

Zero banned words, zero em dashes, no `you`/`we`, both soft markers ruled. The `so` → `therefore`
catch (`final.md:361`, deviating from `review-2-decisions.md:176`, which wrote "so the workflow
needs") is a correct application of a Part 2 hard ban over a file that outranks it on everything
else. That is good work.

**The deduction is a repetition regression this pass introduced, with a licensed fix left on the
table.** The clause *"testing, examination and clinical review remain..."* appears three times in
thirteen lines:

- `final.md:245` — scope note, Review 1 protected: "...testing, examination and clinical review
  remain within the customer's other systems."
- `final.md:253` — Section 2 last bullet: "...while testing, examination and clinical review remain
  unchanged."
- `final.md:257` — Section 3 opener, two sentences later: "...while testing, examination and
  clinical review remain within the wider screening process."

Revision 3 carried the clause **once**. The editor names this in `self_check` as "the most
machine-sounding thing left in the article" and rules it untouchable as reviewer-verbatim. It is
not. `review-2.md:33` introduces the bullet with **"The short-answer bullet could become:"** —
the only conditional instruction in item 1, against "Change the heading to", "Change the opening
to", "Update the figure label accordingly" and "Replace the table row with". The reviewer offered
that sentence; they mandated the other four. The cheapest fix, touching nothing protected and
overriding no instruction, is to end the `:253` bullet at "before the appointment" (−9 words) —
the same fact is stated four lines below in the Section 3 opener, where it does structural work,
and again in the scope note above.

Second, smaller: "at or around the appointment/visit" now appears five times (`:249`, `:252`,
`:277`, `:283`, `:302`). The editor checked the one instance it owns and left it. Defensible
individually, but combined with the triple it is the tone cost of this pass.

### D. Format & structure — 3/3

Frontmatter complete on both files (`product: fitxpress` present on each), correct paths, plan
structure held, 10 H2s, both protected tables intact, FAQ 4 questions, one evaluation-framed CTA.
Meta within the SEO-meta override: title 57 chars (50-60), description 150 chars (140-160), primary
keyword in the first 24 characters. `plan.md` declares no keyword volume/difficulty as TBD — the
article is an explicit GEO/long-tail play (`plan.md:108-112`) — so nothing is owed to Open items on
that count.

### E. Output quality — 3/4

Not a 4: it needs Vadim on five open items and roughly ten minutes of copy editing.

1. **The Section 3 opener partially re-muddies the correction it was applying.** Item 1's whole
   point is that the three phases belong to screening, not to intake. Shipped
   (`final.md:257`): *"Treating the occupational health intake process as one step makes the
   comparison confusing. The occupational health screening workflow runs in three phases."*
   Sentence one names intake as the thing being wrongly treated as one step; sentence two splits
   **screening**, of which intake is phase 1; then a three-item list follows. A reader can still
   attach the list to "intake" by juxtaposition, which is the exact confusion the reviewer
   described. The keyword carve-out (`plan.md:199` assigns `occupational health intake process` to
   this section only) is a legitimate reason to keep a framing sentence; keeping *this* one costs
   part of the correction. Of the four modifications, this is the one that weakened the reviewer's
   point.
2. **E4's fold relocated the interruption instead of removing it.** The reviewer's objection was
   that the clinic-software line "does not add meaningful information and slightly interrupts the
   progression" (`review-2.md:94-96`). Shipped (`final.md:250`): a 46-word definition bullet with
   the same information now embedded inside the definition —
   *"**Digital intake**, called digital patient intake in clinic software, collects the same
   questionnaire content through a structured remote channel before the appointment, replacing
   paper patient intake forms, with body measurement captured by..."* The keywords survive, which
   was the stated goal; the reviewer's actual complaint does not get addressed.
3. **E2's modification did not achieve its own stated purpose.** The reason given for modifying
   (`review-2-decisions.md:176`) is that the reviewer's sentence dropped in whole "would say the
   fallback exists twice in three sentences." Shipped (`final.md:361`): *"The manual path stays open
   as the documented fallback. Access varies by workforce, role and geography, and the workflow
   therefore needs a manual alternative for anyone who lacks..."* — the fallback exists, twice, in
   two sentences. The reviewer's claim-softening (removing "strands part of the population") did
   land, which is what mattered most.
4. **The compliance sentence got longer while being trimmed.** Removing the AWS/TLS detail (−5) and
   adding the BAA clause (+8) leaves a single 68-word inventory sentence at `final.md:350` where
   revision 3 had 57. The reviewer's replacement was five short sentences; the partial application
   kept the run-on shape it was meant to break.
5. **Section 7's duplication is the one I would cut, and cutting it overrides nobody.** `:338`
   and `:340` say the same thing 22 words apart, adding only "sample". Per the A-1 finding, the
   reviewer's own E5 phrasing ("how measurement performance was evaluated") resolves it. **R2-1 in
   Section 4 I would leave** — the two paragraphs overlap on "reduce transcription" and a
   "depends on" cadence, but they are doing different jobs (mechanism vs balanced reading), and
   deleting Review 1's protected A5-5 on editorial judgment is the wrong precedent. If Vadim wants
   it at zero, the editor's proposed one-line cut is the right one.

**Ruling requested on the `rather than` (`final.md:348`): agree, LICENSED.** *"The measurement case
therefore rests on repeatability and standardized capture rather than a claim of superiority over
expert tape measurement."* It draws the single most load-bearing claim boundary in the article —
FX-001 is measured *against* expert manual measurement, so superiority over that reference is not
available — and it satisfies even the strict reading of the guardrail: recommended form first
("rests on repeatability and standardized capture"), limitation second. It is reviewer text, and
rewriting a reviewer's sentence to dodge a soft marker would be the wrong trade. The ruling is also
correctly logged in three places rather than passed silently.

## Top 3 issues (priority for improver)

1. **E5 was retained, not applied, and the escalation it produced is manufactured.** Question 2 at
   `final.md:338` is the old Q5 wording; the reviewer's E5 wording ("how measurement performance was
   evaluated") removes the Section 7 duplication for free. Open item 6 in the publish package should
   be closed by an edit, not by Vadim's ruling.
2. **A conditional reviewer suggestion ("could become") was treated as mandated verbatim text, and
   the article shipped a three-times-in-thirteen-lines clause because of it.** `seo-editor` needs a
   rule for grading reviewer instructions by modality: "Change X to" and "Replace with" bind;
   "could become" and "suggested replacement" are proposals that lose to a house rule such as
   repetition control.
3. **The binding decisions file's gate transcript describes a file that was never shipped**
   (2,173 words / net −26 / 0.66 vs the artifact's 2,185 / −14 / 0.65). Whichever agent writes the
   decisions file must re-run or re-copy the gates after the last edit, or the file should not carry
   gate output at all. A stale number inside the document declared to win every conflict is the
   worst place for one.
