---
article: bariatric-hub-refresh
published_slug: bariatric-pre-qualification-mobile-3d-body-scanning
stage: edit
review_round: 1
instruction_set: review-1-decisions.md
input: draft-v2-editor.md (untouched on disk)
output: draft-v3-editor.md
written: 2026-09-07
written_by: seo-editor
lint: FAIL on one gate only (gate 5, `predicted weight` x6) — see "Gates" below
detector: CLEAN, ai density 1.0/1000 against a 6.0 budget
word_count: 4413 all-in (3988 excluding table cells), from 4712
---

# Editor report — Review 1 rulings applied

Every ruling in `review-1-decisions.md` has a row. Section numbers in the "Where" column are the
**new** numbering in `draft-v3-editor.md`; the old numbers are given where the two differ.

## Section map, old to new

The reviewer's ten-section order is adopted exactly. Their section 1 (introduction and Use Case
Summary) is unnumbered front matter, as it was in v2, and their section 10 stays split across two
H2s because the live page and the plan both carry "Next steps and related reading" as its own
section. So the page has 10 H2s plus front matter, and the reading order is the reviewer's.

| Reviewer § | New H2 | Came from (v2) |
|---|---|---|
| 1 | front matter | new intro (D1) + compressed v2 §1 + Use Case Summary + disclaimer |
| 2 | ## 1 What structured remote body data contributes, and what it does not decide | v2 §2 + B2 text + the CDC self-report sentence rescued from v2 §1 |
| 3 | ## 2 Remote body measurement for bariatric patient intake: a four-stage pre-qualification workflow | v2 §6 |
| 4 | ## 3 Bariatric pre-qualification and pre-authorization documentation | v2 §3 |
| 5 | ## 4 The GLP-1 bridge: current BMI, historical BMI and documentation continuity | v2 §5 + the one surviving indicator and the two quotes from v2 §4 |
| 6 | ## 5 Patient progress tracking before and after surgery | v2 §8 |
| 7 | ## 6 Where FitXpress fits: outputs, accuracy and limitations | v2 §7 + the "does not do" block from v2 §9 |
| 8 | ## 7 Manual measurement versus guided capture | v2 §10 table and buyer-fit paragraph |
| 9 | ## 8 What to confirm in a bariatric pilot | v2 §10 diligence bullets + v2 §9 operational content + new pilot table + KPI list |
| 10 | ## 9 Frequently asked questions and ## 10 Next steps and related reading | v2 §11 reduced + v2 §12 with three links removed |

Two deviations from the reviewer's literal wording, both mechanical and both on the same principle
the decisions file used for B1b (style conforms to the page, content does not change):

1. **The section-3 H2 is sentence case**, not the reviewer's Title Case. The wording is theirs word
   for word. `detect-ai-tells.py` raises a house-rule violation on any Title Case H2, and a house-rule
   violation is a lint failure through gate 1, so shipping their capitalisation would have failed the
   gate on a formatting rule the reviewer was not ruling on.
2. **The H2 carrying the primary keyword is ## 3**, "Bariatric pre-qualification and pre-authorization
   documentation". The reviewer's title for that section omits "bariatric", and lint gate 7 needs the
   exact primary keyword in at least one H2.

## B. Must-fix issues

| Ruling | What changed | Where |
|---|---|---|
| **B1a** delete two CMS inference sentences | Both deleted outright. Nothing hedged took their place. The surviving operational point reads "A long review window absorbs a request for more information, and 7 calendar days leaves little room for one", using the decisions file's own "little room" rather than v2's "no room". | §3, para 4 |
| **B1b** timeframe statement | Placed verbatim, with the two conformances the ruling authorises (`1 January 2026`, numerals). The only addition is a markdown anchor around `CMS-0057-F` pointing at the CMS rule page, so the paragraph carries its source; no word was changed, added or repunctuated. | §3, para 2 |
| **B1c** keep the two payer-mix sentences and the counsel line | Both kept verbatim. The payer-mix and counsel sentences are merged into one sentence for rhythm; wording unchanged. CHIP is expanded as "Children's Health Insurance Program (CHIP)" in the bridge sentence that opens the section, because B1b's verbatim text uses the bare abbreviation and guardrail M1 wants first use expanded. | §3, paras 1 and 3 |
| **B1d** FAQ timeframe answer | Rewritten. Timeframes now attach to Medicare Advantage plus specified Medicaid and CHIP payers; the QHP exclusion is stated; the extension of up to 14 additional calendar days appears once; the ERISA and Medicare fee-for-service scope notes follow. | §9, FAQ Q4 |
| **B2** payer acceptance, first statement | The two-sentence distinction placed verbatim. | §1, para 3 |
| **B2** Use Case Summary | Role row takes the B4 text ("it does not determine eligibility or payer acceptance"). Problem row unchanged. | front matter |
| **B2** §3 (was §3) | The pre-auth section no longer implies a payer will accept a scan record. What survives is "whether its first submission is complete". | §3 |
| **B2** §5 (was §5) | Comparison kept, implication cut: "A tape measurement typed into a free-text note carries neither, which leaves a reviewer with the note and nothing behind it. Whether a scan record then satisfies a given plan's documentation requirement is a separate question, and it is settled with the plan." The v2 clause "a reviewer at the payer cannot confirm when it was taken or how" is gone. | §4, para 5 |
| **B2** §6 and §7 (was §6, §7) | Workflow closer now reads "a structured, dated body-data input", not "structured, verifiable". Pathway table keeps "Provides structured, timestamped documentation inputs" as an input claim and is not paired with any verification claim. | §2 closer, §6 table |
| **B2** §9 audit-readiness | Reframed: "Audit-readiness is the program's own determination, and a human reviewer still reads every record." | §8, para 2 |
| **B2** §10 comparison table | Row renamed to **Documentation generated**, both cells unchanged. New final row **Payer acceptance**, both cells identical: "Follows the plan's own documentation requirements and is confirmed during implementation." Neither cell implies pre-acceptance. | §7 table |
| **B2** FAQ | Q3 no longer says a timestamp makes a record verifiable; it says the timestamp dates the record and acceptance is confirmed with the plan. Q8 closes on "Whether a payer accepts a scan record for a given documentation requirement is decided by the plan." | §9 |
| **B3** §4 dataset conflation | Three-row indicator table deleted. ASMBS-versus-claims reconciliation paragraph deleted. 2023 national estimate (270,089 / 279,967) deleted, including from the FAQ, which lost the question that carried the procedure-type split. Cohort counts (40,265 / 42,615 / 37,339 / 33,429) deleted. | §4 |
| **B3** the one surviving indicator | Placed verbatim, cited to `https://doi.org/10.1001/jamasurg.2026.1343` on the anchor "JAMA Surgery, 13 May 2026". The EurekAlert link is gone from the page. GLP-1 market hub linked in the same paragraph. | §4, para 1 |
| **B3** Funk and Kurian quotes | Kept. The section survived the restructure as the GLP-1 bridge, which is the condition the ruling set, and the quotes now carry the funnel-shape point on their own without a market-size claim. | §4, para 2 |
| **B3** §5 Epic Cosmos study | Untouched, as instructed. | §4, para 3 |
| **B4.1** Smart Scales, plural | Every instance is "Smart Scales". | §2, §5, §6, front matter |
| **B4.2** beta at first mention | First mention on the page is the Use Case Summary Outputs row, which carries "(beta)". Stage 1 and the product paragraph carry it too. | front matter, §2, §6 |
| **B4.3** no "internal validation" on the weight figure | The 3.5% sentences say "under real-world conditions". "Internal validation" appears only on FX-001 and FX-005, where it belongs. | §6 |
| **B4.4** no clothing clause on the weight figure | Not present. The clothing detector appears once, in Stage 2, as a capture-quality behaviour. | §2 |
| **B4.5** no "mean absolute error" | Not present. The figure ships as `±3.5% average error margin` with the symbol intact, and both sentences say in words that it is an average across captures. | §5, §6 |
| **B4** product paragraph | Placed verbatim as the second and third sentences of the section opener. | §6, para 1 |
| **B4** BMI cross-check | Placed verbatim, including the "review signal rather than an automated eligibility conclusion" clause, which was not rewritten. | §6, para 4 |
| **B4** the 3.5% qualification text | Placed verbatim. The paragraph also links the accuracy framework, per the gate note, on a sentence that says which reference each figure is measured against. | §6, para 5 |
| **B4** Use Case Summary Outputs and Role rows | Both placed verbatim with Smart Scales corrected. | front matter |
| **B4** Stage 1 | Placed verbatim. | §2 |
| **B4** post-operative paragraph | Placed verbatim, as the closing three sentences of the repeatability paragraph so that the paragraph carrying the figure also carries the framework link, which is the gate note's requirement. | §5, para 2 |
| **B4** gate note, framework link follows the figure | Satisfied in all three paragraphs that carry a figure: §5 (repeatability and 3.5%), §6 (96-97% and 1.5-2.0 cm), §6 (3.5%). | §5, §6 |
| **B5** Business value row | Now reads "What a pilot sets out to measure:" followed by five of the six KPIs. | front matter |
| **B5** five named phrases | All five gone: "Higher consult-to-procedure conversion" and "fewer measurement-only visits" (Business value row), "the difference between a first-pass submission and a resubmission" (Stage 4, replaced by "Whether that changes how long a packet takes to assemble is one of the things a pilot measures"), "Every verification step... is also a point where a patient can leave the pathway" (deleted with the v2 §1 compression), "replaces the fragmented manual measurements" (replaced by the D5 line). | front matter, §2, §6 |
| **B5** pilot KPIs | All six listed as a set, verbatim, in one sentence. | §8, para 4 |
| **B5 carve-out** CDC sentence | Sentence untouched, word for word, and re-homed into §1 so the compression of v2 §1 did not take it with it. The inference "a self-reported value is a placeholder that still has to be verified" is gone; what follows now is that the comparison is population-level and characterises no individual file. | §1, para 4 |
| **B5** attrition paragraph | Range and variance kept ("varies with program design and with how it is counted", 60% / 22.25% / 36-76%, and "That spread is a stronger case..."). The causal sentence about verification steps and patient departure is gone. | front matter, para 2 |
| **B6** seven guide promises | All seven removed. Where a promise went, the sentence before it now answers: §3 lists what the body-data half of a pre-auth packet contains; §4 ends on the both-directions record argument; §5 lists what belongs in a progress record; Stage 1 and Stage 2 are rewritten under B4/D2; Stage 3 states the hybrid schedule in one clause instead of promising a guide. | §2, §3, §4, §5 |
| **B6** eighth promise (privacy FAQ) | "A dedicated FitXpress privacy and regulatory FAQ, not yet published, holds the fuller detail" removed with the rest of the old compliance bullet. No link was added. | §8 |
| **B6** DOWN-LINK markers | All eight `DOWN-LINK LANDING` comments removed with their prose. `draft-v3-editor.md` carries zero. The publisher rebuilds `publish-package.md` §3b. | whole file |
| **B7a** "processes no personal identifiers" | Gone, replaced inside the verbatim bullet by the linkage statement. | §8 |
| **B7b** GDPR roles | Shipped as written in the bullet. Open item E1 unchanged and non-blocking. | §8 |
| **B7c** photo retention | Declined by the ruling, so the concrete approved wording ships: "permanently removed immediately after processing, or within 30 days, depending on the client's configured policy". | §8 |
| **B7d** output retention | Not added. The bullet says body data and session-linked outputs can still qualify as personal data. | §8 |
| **B7** whole bullet | Placed verbatim, with the FX-009 claim marker appended. | §8 |
| **B7** SOC 2, Validation population, Validation strength | SOC 2 unmentioned. Both other bullets verbatim from v2. | §8 |

## C. Structure

Applied as mapped, see the section map above. Prose words per section after the move: §1 299,
§2 331, §3 381, §4 479, §5 426, §6 570, §7 262, §8 605, §9 540, §10 85, plus 435 in the front
matter. The four-stage workflow now begins at roughly 20% of the page.

## D. Additional content improvements

| Ruling | What changed | Where |
|---|---|---|
| **D1** new introduction | Placed verbatim as the first paragraph. One sentence added at its end, "Bariatric pre-qualification runs on that record, and so does patient progress tracking after the procedure", because lint gate 7 requires the primary keyword in the first paragraph and the reviewer's three sentences do not contain it. The two abstract phrases they named are gone with the old intro. | front matter |
| **D2** Stage 2 | "Patients who clearly meet criteria move into a clinical-evaluation consult" is gone, along with the routing sentence that followed it. Stage 2 now has a coordinator confirming completeness, routing for authorized clinical review, real-time pose validation and the clothing detector surfacing an unusable capture in session, and a retake or in-clinic fallback. | §2 |
| **D3** estimates versus measurements post-op | Added: "Body-composition estimates complement weight and circumference trends where the program considers them appropriate. They are not equivalent to dual-energy X-ray absorptiometry (DXA), bioelectrical impedance analysis or a calibrated scale where the workflow, protocol or regulatory standard requires those methods." Guardrail #7 wording; no "positioned as". DXA expanded at this, its first use. | §5, para 3 |
| **D4** "weeks apart" | Removed from the repeatability definition. | §5, para 2 |
| **D5** capture-asset line | Replaced verbatim: "The same data structure can be generated at multiple pathway stages alongside measurements required by the program or payer." The comparison table's reuse cell was aligned to the same wording. | §6, §7 table |
| **D5** pilot-evaluation table | Added, seven rows in the reviewer's order, each stating what the program confirms. | §8 |
| **D6** FAQ reduction | The seven named questions are gone. **Nine remain, not eight** — see "Left undone / flagged" below. "What are common program and payer requirements?" is retained and re-homed into the pre-qualification and pre-authorization group. The "Bariatric surgery basics" H3 is gone entirely, since both of its other questions were removed. | §9 |
| **D7** internal links | Occupational health screening software removed from the buyer-fit paragraph; insurance underwriting and wellness rewards verification removed from related reading. Link directions still covered: up 1, sideways 3, down 1, trust 1. The online-pharmacy BMI verification guide stays, as instructed. | §7, §10 |
| **D8** meta description | Replaced verbatim in the frontmatter. Publisher owns the character budget and the "Why this direction" rationale rewrite. | frontmatter |

## Gates

| Gate | Result |
|---|---|
| hard bans (detect-ai-tells, article channel) | ok, CLEAN, density 1.0 per 1,000 against a 6.0 budget, rhythm variation 0.56 |
| prose length | ok, 4,413 against target 4,400, band 3,740-5,060 |
| claim traceability | ok, FX-001, FX-002, FX-005, FX-006, FX-007, FX-008, FX-009 |
| banned claims | ok |
| **superseded figures** | **FAIL, six hits, all on `predicted weight`** |
| internal links | ok, 14 links, 7 distinct, all four directions covered |
| keyword placement | ok, H1, first paragraph, one H2, 6 occurrences |
| abbreviations (M1) | ok |
| accuracy discipline | ok |

### The one failing gate, in full

`scripts/article_lint.py` gate 5 carries this row:

```
(r"\bpredicted weight\b", "omit; no approved claim supports it",
 "Review 1 item 13 closed against the reviewer, 2026-09-02"),
```

It fires six times, at file lines 100, 124, 165, 177, 183 and 185. **All six sit inside B4 "Text to
place" blocks** and not one is editorial:

| Line | Block |
|---|---|
| 100 | Use Case Summary, Outputs row |
| 124 | Stage 1 of the workflow |
| 165 | post-operative paragraph |
| 177 | product paragraph in §6 |
| 183 | BMI cross-check |
| 185 | the 3.5% qualification text |

I did not paraphrase them. The decisions file's opening section exists to stop exactly that move, and
a sixth wording change on top of B4's five authorised ones is not mine to make.

The row itself looks over-scoped rather than wrong. Three things sit against it:

- **`brand-assets/product-info/how-it-works.md`** backend pipeline step 6, "Smart Scales (beta) —
  cross-validates self-reported weight against the AI estimate, flags mismatch", and
  **`tech-spec.md`** line 12, "Returns: ... Smart Scales (beta)", and line 100, "Smart Scales weight
  estimate + mismatch flag".
- **Two live articles already publish the phrase.**
  `brand-assets/past-articles/blog/online-pharmacy-bmi-verification.md` uses "Predicted weight" in its
  Use Case Summary Outputs row and five more times in the body, and
  `3dlook-turns-two-photos-structured-body-data.md` describes Smart Scales predicting weight.
- The row's own provenance is the **wellness hub's** Review 1 item 13 on 2026-09-02, a different page
  with a different reviewer. This decisions file, dated 2026-09-07, rules the opposite way for this
  page and grounds it in the product docs above.

Two ways to clear it, neither of which belongs to the editor:

1. Amend the `SUPERSEDED` row to scope it to the claim rather than the phrase, for example by
   requiring `predicted weight` to sit in a paragraph carrying an FX-008 marker, or by exempting it
   where "Smart Scales" appears in the same sentence.
2. Have the decisions file amend B4's blocks to a phrase the gate allows.

Recommend routing this to Vadim alongside E1, since it is a repo-level rule collision and not a
defect in this page.

## Left undone / flagged

1. **FAQ count is 9, not 8.** D6's headline says sixteen go to eight, and its explicit list names two
   basics questions plus five body-copy repeats, which is seven removals, leaving nine. The retained
   keyword question is the ninth. I followed the named list, because deleting a tenth would mean
   choosing a question the decisions file did not name. Flagging the arithmetic rather than acting on
   it.
2. **The ±3.5% figure now appears twice**, in §5 and §6, because B4 supplies a "wherever the 3.5%
   figure lands" block and a separate post-operative block and both carry the figure. Both paragraphs
   link the accuracy framework, so the framework is linked three times on the page. That is the
   accuracy rule working as written, not a dedup miss, and it matches the exception v2 already
   recorded.
3. **Word count is 4,413, not "well below" 4,712.** Deletions removed roughly 1,100 words. The
   mandated additions, B2's distinction, five B4 blocks, the D5 pilot table, the B5 KPI list, the B7
   bullet and the D1 intro, put back roughly 800. No padding was added, and the length gate's floor
   against the plan's 4,400 target is 3,740, so a much larger cut would have failed gate 2.
4. **"consult-to-procedure conversion" survives once**, in §7's buyer-fit paragraph, as one of the
   measures those roles are accountable for. B5's target was the Business value row's assertion that
   the product raises it, which is gone. Naming the metric a director owns is the same register as
   the pilot KPI list. Flagging it in case the coordinator reads B5 more broadly.
5. **Curated internal links are 7 distinct, against the plan's 8 to 11.** D7 removed three, and the
   plan's target predates that ruling. All four directions are still covered.
6. **`plan.md` writer note 6 says "No `predicted weight`".** B4 overrides it for this page. Recorded
   here so the publisher does not re-apply the plan note over the ruling.
7. **`publish-package.md` was not touched**, as instructed. Its §3b DOWN-LINK table and §6 body are
   now both stale against `draft-v3-editor.md` and belong to the publisher.
