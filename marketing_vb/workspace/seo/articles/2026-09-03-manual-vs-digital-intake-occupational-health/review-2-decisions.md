---
slug: 2026-09-03-manual-vs-digital-intake-occupational-health
review: 2
decided: 2026-09-07
decided_by: coordinator (interactive session, Bash + Drive available)
applies_to: final.md revision 3 -> revision 4
purpose: >
  How each Review 2 item is applied, and how it was checked against brand-assets/product-info.
  seo-editor / seo-publisher and any social run MUST read this alongside review-2.md.
  Where this file and review-2.md disagree, THIS FILE WINS, and every disagreement is named below.
verdict: >
  21 of 21 reviewer instructions actioned. 17 applied verbatim, 4 applied with a documented
  modification. 3 sub-points inside item 6 are DECLINED on source-of-truth grounds and carried
  to Vadim as open items - the reviewer's replacement paragraph drops language that
  product-info/compliance.md states as fact and adds language no brand-asset supports.
---

# Review 2 — application decisions

## 0. Provenance

`review-2.md` is verbatim from the Google Doc tab "Review 2" (`t.9ltdnz6zu0ug`), pulled
2026-09-07 through the `oo` googledocs connector with `include_tabs_content=true`. Nothing was
reconstructed. Before applying anything, `final.md` revision 3 was diffed line-by-line against
the doc's "Version 2" tab (`t.tu0rpu3uja72`) after normalising links, emphasis and claim
markers: **identical**, 85 of 85 content lines. So the reviewer read exactly the text that was
edited here, and every quoted "current wording" in the review resolves to a real, unique string
in `final.md`.

**Who applied it.** This file is the coordinator's ruling on each instruction; the edits themselves
were made by the pipeline — `seo-editor` (22 scripted replacements, each asserting `count == 1`)
for revisions 4 and 5, `seo-publisher` for the package, `quality-controller` for the 17/20 review
that triggered revision 5. See §9.

## 1. Essential correction 1 — intake vs screening terminology · APPLIED, one modification

| Reviewer instruction | Applied as |
|---|---|
| H2 -> "The three phases of the occupational health screening workflow" | Verbatim |
| Figure label updated accordingly | "The three phases of the screening workflow, with the remote-capable part marked." |
| Short-answer bullet replacement | Verbatim |
| Comparison-table row -> "Relationship to the wider workflow" | Verbatim, both cells |
| Opening paragraph replacement | **Modified — see below** |

**The modification.** The reviewer's opening is *"The occupational health screening workflow has
three phases. A remote intake channel reaches the first, while testing, examination and clinical
review remain within the wider screening process."* That is correct and it is kept almost whole,
but taken literally it deletes both secondary keywords `plan.md:199` assigns exclusively to this
section (`occupational health intake`, `occupational health intake process`). Shipped:

> Treating the occupational health intake process as one step makes the comparison confusing.
> The occupational health screening workflow runs in three phases. A remote intake channel
> reaches the first, while testing, examination and clinical review remain within the wider
> screening process.

The reviewer's second and third sentences are verbatim. The first keeps the existing framing
sentence and moves the keyword into it, which also carries `occupational health intake` as a
substring. The factual correction the reviewer asked for — the three phases belong to screening,
not to intake — is fully made: nothing in the article now attributes phases to intake.

## 2. Essential correction 2 — the ambiguous "Both" · APPLIED, one modification

The reviewer is right that *"Both are captured and transcribed under appointment-time pressure"*
can be read as "both intake methods". Their replacement is taken almost whole, with one clause
restored:

> **The operational cost sits inside that overlap.** In manual workflows, questionnaires and
> measurements are often collected or transcribed at or around the appointment. Missing or
> inconsistent information can then delay review, require follow-up or trigger a rescreen.

The reviewer's replacement ends at "delay review or require follow-up" and drops the rescreen.
`plan.md:160-170` records this exact bullet as the Review **A5-3/A5-4** rewrite, whose binding
requirement is the mechanism *"an incomplete record can trigger a rescreen"* with no frequency
claim; `content-plan.md` Hub 8 states the article guardrail as *"Throughput, missing data,
rescreens, multi-site consistency."* Rescreens are the guardrail topic, so the outcome is kept
as a third item in the reviewer's own list. The ambiguity the reviewer flagged is gone — the
sentence now names manual workflows explicitly — and no frequency claim is introduced ("often"
is a hedge, not a rate).

## 3. Essential correction 3 — absolute table rows · APPLIED VERBATIM (5 of 5) + paragraph

All five recommended cell revisions are in, word for word:

| Row | New cell |
|---|---|
| Where the step happens (manual) | Usually at or around the clinic appointment |
| Time inside the appointment slot (digital) | Testing, examination and any intake exceptions that require support |
| Ongoing labor (digital) | Less routine collection and transcription; ongoing monitoring and exception support |
| Integration dependency (manual) | Can operate without systems integration, but may still require manual entry into the receiving system |
| Data-entry correction (digital) | Can reduce transcription when integrated; corrections follow the receiving system's process |

The reading paragraph is the reviewer's suggested replacement verbatim ("Manual intake has lower
integration requirements ... the existing technology environment"). It replaces the *"Manual
intake holds three dimensions ... the two rows the decision framework turns on"* paragraph, which
was **ours**, not reviewer-supplied — confirmed against `review-1.md`, so nothing protected by
Review 1 was overwritten here.

**Open item R2-1 (residual, not resolved unilaterally).** The paragraph *above* it — "Moving
eligible intake steps before the appointment can reduce in-appointment collection and
transcription. The effect depends on completion rates, fallback volume, integration quality and
existing rescreen causes." — is the **Review 1 verbatim A5-5 replacement** (`plan.md:230`,
`review-1.md:148`). Now that the paragraph after it is also reviewer-verbatim, the two adjacent
paragraphs both say "reduce transcription" and both end in a "depends on ..." list. The reviewer
read Version 2, which already contained A5-5, and did not ask for it to go. Deleting another
reviewer's protected paragraph on our own judgment is exactly the move this file exists to
prevent, so **both are left verbatim and the overlap goes to Vadim**. The one-line fix, if he
wants it: drop the second sentence of A5-5 ("The effect depends on ...", 17 words), since the
new paragraph's own dependency list supersedes it.

## 4. Essential correction 4 — hybrid prevalence · APPLIED VERBATIM

*"For most programs the answer is hybrid"* asserted a prevalence the article never sourced.
Replaced with the reviewer's paragraph, unchanged. The decisiveness survives: the split is still
stated component by component with a fallback and transfer path per moved step.

## 5. Essential correction 5 — the FitXpress output sentence · APPLIED VERBATIM, and the reviewer is right on the facts

Checked against source before applying, and the review is correct on both counts:

- **BMI is not one of the 80+ measurements.** `product-info/proof-points.md:57` is
  `Body measurements | 80+ | Product spec`; line 58 is a separate row,
  `Body composition outputs | BMI, BMR, fat %, ... | Product spec`. The context pack carries them
  as two distinct claims, **FX-008** and **FX-009**. The old sentence ("80+ body measurements,
  including the circumferences and BMI") merged the two and mis-stated FX-009 as a subset of
  FX-008. The reviewer's "80+ body measurements and calculated metrics such as BMI" restores the
  split. Both claim markers stay on the sentence.
- **"Time-stamped at capture" is over-specified.** Review 1 graded this claim "grounded" against
  `use-cases/fx-occupational-health.md:10` and `faq.md:90`. Re-read today, neither source says
  *at capture*: the use case says "standardized body measurements + BMI/body composition
  (structured, time-stamped)" and the FAQ says "structured, time-stamped audit logs". The
  timestamp is documented; the moment it is taken is not. The reviewer's safer form —
  "structured results associated with a scan timestamp" — is what shipped.
- The other "time-stamped" mention, *"A structured, time-stamped record is easier to compare
  than a written one"* in the accuracy paragraph, was checked and **left**: it is a general
  statement about records, it makes no at-capture claim, and its wording matches the sources'
  own "structured, time-stamped" exactly.

## 6. Essential correction 6 — the privacy paragraph · PARTIALLY APPLIED, 3 sub-points DECLINED

This is the one item where the reviewer's suggested replacement cannot be taken whole. It
removes three statements that `product-info/compliance.md` states as fact, and adds two that no
brand-asset supports. Line by line:

| Reviewer's point | Source of truth | Decision |
|---|---|---|
| Final sentence "It is not a clearance, eligibility or fitness-for-duty input" contradicts the article's own positioning; the boundary is that it does not make the **determination** | The approved scope note already says "make fitness-for-duty or clearance determinations" — the two sentences were inconsistent with each other | **APPLIED.** Now: "FitXpress supports intake and documentation for clinician review; it does not make clearance, eligibility or fitness-for-duty determinations." The reviewer caught a real self-contradiction |
| AWS S3 SSE-S3 / TLS detail adds little comparison value | `compliance.md:17-18` supports both the specific and the general form | **APPLIED.** Trimmed to "encrypts data at rest and in transit". The detail belongs in the Data, Privacy, Security & Regulatory FAQ, as the reviewer says |
| Add "A HIPAA Business Associate Agreement is available on request" | `compliance.md:65` — *"We sign BAAs for HIPAA-covered customers."* | **APPLIED, in the source's own wording**: "signs Business Associate Agreements with HIPAA-covered customers". "On request" is the reviewer's phrasing, not ours; "for HIPAA-covered customers" is what the asset says |
| Remove "processes no personal identifiers" | `compliance.md:23` — *"Personal identifier processing \| None — photos cannot be linked to individuals via 3DLOOK"*; also `proof-points.md:137`, `how-it-works.md:56`. Review 1 §B graded it grounded and kept it | **DECLINED — open item R2-2.** Standing approved compliance language, stated as a product property in three assets. The reviewer's reason is a hypothetical ("session identifiers and customer-side record matching **can** make such a statement difficult to maintain"), not a counter-source. Whether it holds for every deployment is a legal/product call for Vadim, not an editorial one |
| Replace with "the customer acts as controller and 3DLOOK acts as processor under GDPR" | **No source.** `compliance.md` says only "Follows GDPR principles". Review 1 §B is explicit: keep the exact hedge "follows GDPR principles," never a stronger form | **DECLINED — open item R2-3.** Controller/processor is a contractual allocation that varies by deployment and appears in no brand-asset. Adding it would be the same class of error the reviewer is otherwise correcting |
| Replace photo deletion with "Photos are deleted after processing, while generated outputs are retained according to the agreed deployment terms" | `compliance.md:22` — *"Permanently removed immediately after processing OR within 30 days, per client policy."* Output retention: **no source** | **DECLINED — open item R2-4.** The deletion half is already stated more precisely than the replacement, with the client-policy conditionality explicit. The output-retention half is unsourced |

Shipped paragraph:

> FitXpress maintains Health Insurance Portability and Accountability Act (HIPAA) safeguards in
> US healthcare contexts and signs Business Associate Agreements with HIPAA-covered customers,
> follows General Data Protection Regulation (GDPR) principles for processing in the EU,
> encrypts data at rest and in transit, processes no personal identifiers, and deletes photos
> immediately after processing or within 30 days, with the window set by client policy.
> FitXpress supports intake and documentation for clinician review; it does not make clearance,
> eligibility or fitness-for-duty determinations.

The HIPAA and GDPR expansions stay in place because this is their first use in the article and
`article_lint.py` gate 8 (M1 abbreviations) tests exactly that.

## 7. Essential correction 7 — the accuracy conclusion · APPLIED VERBATIM

Both reviewer sentences shipped unchanged. The approved 96-97%, 1.5-2.0 cm and repeated-scan
statements are untouched, as the reviewer directed, and FX-001 / FX-003 markers stay on them.

Note for the detector log: the replacement introduces one soft `rather than` marker
(corrective_contrast, L232). It is reviewer-verbatim and it draws a real accuracy boundary —
a superiority claim against expert tape measurement — which is precisely the licensed use in the
terminology guardrails. Left as written. Detector still CLEAN, 0 hard fails.

## 8. Recommended editorial refinements · 5 of 5 APPLIED, 2 with a modification

| # | Instruction | Decision |
|---|---|---|
| E1 | "switching without checking them spends money to make things worse" -> "Manual intake remains practical in several situations: ..." | **Verbatim.** The reviewer's ellipsis is the existing five-item list, kept intact |
| E2 | "a remote-only channel strands part of the population" -> "The workflow therefore needs a manual alternative for people who lack the required access or cannot complete the remote capture." | **Modified.** Dropped verbatim, the FAQ answer would say the fallback exists twice in three sentences. Shipped: "The manual path stays open as the documented fallback. Access varies by workforce, role and geography, so the workflow needs a manual alternative for anyone who lacks the required access or cannot complete the remote capture." Reviewer's substance intact, one word shorter than before |
| E3 | "The last is the diligence question worth handing any vendor, including this one." -> "Any vendor should be able to explain how repeatability was evaluated, including the measurements, sample, number of repeated scans and reference method." | **Verbatim** |
| E4 | Remove "Clinic software calls this digital patient intake ..." | **Modified — keyword carve-out.** The standalone sentence is gone, which is what the reviewer objected to ("interrupts the progression"). But `plan.md:171` assigns `digital patient intake`, `intake forms` and `patient intake forms` to this section **and only this section**. All three are folded into the definition bullet instead: "**Digital intake**, called digital patient intake in clinic software, collects the same questionnaire content ... replacing paper patient intake forms." Net 4 words shorter than the two-element original |
| E5 | Reduce the five implementation questions to two: which components move, and how measurement performance was evaluated | **Applied, and it reverses a Review 1 protection.** Review 1's "What should be preserved" item 6 explicitly protected all five questions; Review 2, from the same reviewer, cuts three of them as duplicates of the metrics table. Later review wins, and the reviewer is right — rescreen rate, integration success and manual fallback rate are already rows 4, 8 and 5 of that table. Q1 survives. **This row said "Verbatim" and "Q1 and Q5 survive" until 2026-09-07; both were wrong, corrected here after QC finding A-1 (17/20).** Revision 4 shipped the old, narrow Q5 as question 2, which is a retention, not the reduction the instruction asks for, and it manufactured the Section 7 duplication that was then escalated as an unresolvable reviewer-vs-reviewer conflict. Revision 5 ships question 2 in the reviewer's own E5 wording, "How was measurement performance evaluated?". The overlap with the E3 sentence below it is gone and the open item is struck |

One knock-on edit, ours: the lead-in reads "**Two diligence** questions sit alongside the
numbers" rather than "Two questions", because Section 1 already opens with "Two questions decide
the method" and the reduction had put the same construction on the page twice.

## 9. Gates — executed, not asserted

**Correction, 2026-09-07.** This section originally carried gate output from a coordinator
hand-pass that was **reverted and never shipped** (2,173 words, 20 replacements, net -26). Vadim's
instruction was that the pipeline applies reviewer rounds, not the coordinator, so `final.md`
rev 3 and `publish-package.md` rev 2 were restored from `v2/` and the run was handed to
`seo-editor` -> `seo-publisher` -> `quality-controller`. The numbers below are the shipped ones.
The hand-pass survives only as a reference outside the article dir and is not an input to anything.

**Revision 4** — `seo-editor`, Review 2 applied, 22 scripted replacements each asserting
`count == 1`. Both gates run by the editor, then re-run independently by the coordinator and
again by `seo-publisher`; all three runs agreed.

- `article_lint.py` -> **VERDICT PASS, exit 0, all 9 gates.** Prose 2,185 words. Keyword x4 across
  10 H2s. Claims FX-001/003/006/007/008/009/014 traced. Links 6 total / 4 distinct. M1 ok.
- `detect-ai-tells.py` -> **CLEAN, exit 0**, channel `any`. `hard_fails: []`,
  `house_rule_violations: []`. ai_density 0.85, 2 soft markers, em-dashes 0, rhythm 0.65.

**Revision 5** — `seo-editor` again, QC remediation, four fixes from the 17/20 report. Not new
reviewer input: three of the four are this pipeline's own defects, and the first is a fidelity
error against Review 2 that this file caused (see §8 E5).

- `article_lint.py` -> **VERDICT PASS, exit 0, all 9 gates.** Prose **2,160 words**.
- `detect-ai-tells.py` -> **CLEAN, exit 0.** ai_density 0.86, 2 soft markers, rhythm 0.66.

**Word band.** Binding band 1,900-2,200. Revision 3 sat at the 2,199 ceiling; revision 4 landed at
2,185, revision 5 at **2,160** — 40 words of headroom against revision 3's one. The reviewer's own
cuts paid for the additions: the five-questions reduction, the decision-framework opener, the
reading paragraph and the hybrid paragraph against the phases opening, the five revised table
cells and the accuracy conclusion.

**ai_density moved 0.42 -> 0.86** on a single added soft marker (`rather than`, item 7, reviewer
verbatim) against a shorter text. Budget is 8.0. Rhythm variation improved 0.65 -> 0.66.

## 10. Open items for Vadim

1. **R2-1 — a repetition the two reviews created between them.** Section 4 now carries two
   adjacent reviewer-verbatim paragraphs that both say "reduce transcription" and both close on
   a "depends on ..." list. Fix on request: cut the second sentence of the Review 1 A5-5
   paragraph. Not done unilaterally — it is protected text.
2. **R2-2 — "processes no personal identifiers."** Keep or cut? `compliance.md:23` states it
   flatly and Review 1 kept it; Review 2 wants it out unless it has been confirmed for every
   deployment. That confirmation is not something the article pipeline can produce. If the answer
   is "cut", it should be cut from `compliance.md`, `proof-points.md` and `how-it-works.md` in
   the same move, not from this one article.
3. **R2-3 — GDPR controller/processor.** The reviewer wants it stated. No brand-asset carries it.
   If it is true and standard for enterprise deployments, it belongs in `compliance.md` first.
4. **R2-4 — retention of generated outputs.** Same shape: the reviewer assumes a documented
   policy ("retained according to the agreed deployment terms"). `compliance.md` documents photo
   retention only. Worth adding to the asset if a policy exists.
5. **Carried forward from Review 1, still open.** Once the Data, Privacy, Security & Regulatory
   FAQ ships (`content-plan.md:24`, last open P0 hub gap), trim the compliance paragraph to a
   link — the reviewer makes the same point about the encryption detail in item 6.
6. **Carried forward from the rev-2 package, still open.** The Section 1 opening scene still
   echoes the hub's opening paragraph at roughly 20% of its original length. Unchanged by this
   pass.
