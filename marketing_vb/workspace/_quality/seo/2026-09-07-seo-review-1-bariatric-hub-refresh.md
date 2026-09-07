---
qc_date: 2026-09-07
agent: seo-editor + seo-publisher (Review 1 application pass)
artifact: workspace/seo/articles/bariatric-hub-refresh/publish-package.md
secondary_artifact: workspace/seo/articles/bariatric-hub-refresh/draft-v3-editor.md
track: seo
artifact_type: seo-final
revision: publish-package.md rev 2 (Review-1 rebuild) / draft-v3-editor.md
total_score: 17/20
status: good
scope: judgment only — mechanics (article_lint 9/9, detect-ai-tells 1.0/1000) taken as given per task brief
prior_state: v1/publish-package.md (from draft-v2-editor.md), external review scored it 6.5/10
coordinator_review: |
  agreement: ✅ agree, all three findings, and finding 1 is my defect not the editor's
  top_issue: B4 handed the editor two blocks for one figure without saying they were
    alternatives, and it placed both — a decisions file that offers a choice without naming it
    as one reads as an instruction to apply everything.
  actions: G1 deduplicated by the coordinator (figure now once, in §6, lint re-run PASS);
    G2 heading deviation approved and disclosed; G3 kept and moved to package open items;
    publisher fix pass sent for the three §3 arithmetic slips and for the escalation rule.
  note: The process finding is the one worth carrying to agent-improver. Both G1 and G2 were
    caught by the editor and written into its own report, then died there. An editor flag has
    to become a package open item by default, because publish-package.md is the file Vadim
    reads and the editor report is not.
---

# QC Report — Review 1 application pass — bariatric hub refresh — 2026-09-07

**Artifact:** `workspace/seo/articles/bariatric-hub-refresh/publish-package.md` (§6 body included)
**Total: 17/20** — good

**Headline: every "Text to place" block shipped literally.** I diffed B1b, B2, B4 (all seven
blocks, not five), B7's compliance bullet, D1 and both D5 items word for word against
`review-1-decisions.md`. Zero paraphrase. The occupational-health failure mode did not recur.
The three carve-outs (CDC self-report sentence, §5 Epic Cosmos study, B1c's two payer-mix
sentences) are intact and untouched. The defects below are second-order: escalation hygiene and
three self-verification slips inside the package's own prose.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## Verbatim verification — what I actually checked, block by block

| Block | Decisions ref | Body line | Verdict |
|---|---|---|---|
| CMS timeframe statement | B1b :87-92 | pkg :561 | Verbatim. Only addition is a markdown anchor on `CMS-0057-F` |
| Payer-acceptance distinction | B2 :112-116 | pkg :540 | Verbatim |
| Comparison-table rename + new row | B2 :118-122 | pkg :634, :637 | Applied. `Documentation generated` keeps both original cells; `Payer acceptance` is the final row, both cells identical, neither implies pre-acceptance |
| One surviving indicator | B3 :138-140 | pkg :575 | Verbatim, cited to `doi.org/10.1001/jamasurg.2026.1343`. EurekAlert gone |
| Product output paragraph | B4 :195-197 | pkg :603 | Verbatim |
| BMI cross-check | B4 :204-208 | pkg :609 | Verbatim, closing clause not rewritten |
| 3.5% qualification | B4 :217-220 | pkg :611 | Verbatim + one added two-benchmark sentence carrying the framework link |
| Use Case Outputs / Role rows | B4 :241-242 | pkg :526-527 | Verbatim |
| Stage 1 | B4 :246-251 | pkg :550 | Verbatim |
| Post-operative paragraph | B4 :255-259 | pkg :591 | Verbatim |
| Compliance bullet | B7 :335-344 | pkg :667 | Verbatim, whole bullet |
| Introduction | D1 :377-381 | pkg :515 | Verbatim + one added keyword sentence (disclosed) |
| Capture-asset line | D5 :407-409 | pkg :622 | Verbatim (sentence-initial capital only) |
| Pilot-evaluation table | D5 :410-412 | pkg :655-663 | Seven rows, reviewer's order, each phrased as what the program confirms |

Carve-outs held: CDC sentence at pkg :542 is word-for-word intact and only the generalising
inference after it is gone; Epic Cosmos study at pkg :579 untouched; disclaimer at pkg :532
untouched; validation-population and validation-strength bullets untouched; no accuracy or
repeatability figure added beyond the two already on the page (no 0.40 cm, no 95%+).

## What was wrong (specific)

### A. Adherence — 4/5

- **The two judgment items the editor explicitly escalated never reached the checkpoint artifact.**
  `editor-report-review-1.md` "Left undone / flagged" #2 (the ±3.5% passage now appears twice) and
  #4 ("consult-to-procedure conversion" survives in §7) were both raised for a coordinator ruling.
  Item #4 made it into `publisher-report.md` §4.9; item #2 made it nowhere. Neither appears in
  `publish-package.md`, which is the file Vadim reads at this checkpoint and which states at :39
  that it is "reproduced here rather than referenced so this file stays self-contained." D7's
  deliberate-removal record got its own §3g exactly as instructed; the editor's own two flags got
  no equivalent.
- **A third deviation from the adopted section headings is undisclosed.** Decisions §C row 7 adopts
  *"Where FitXpress fits: outputs, accuracy, repeatability and limitations"*; the shipped H2 is
  `## 6. Where FitXpress fits: outputs, accuracy and limitations` (pkg :601). Dropping
  "repeatability" is defensible — FX-002 lives in §5, not §6 — but `editor-report-review-1.md` :41
  states "**Two** deviations from the reviewer's literal wording" and `publisher-report.md` §3.4
  re-verifies only those two. A completeness claim that is not complete.
- Everything else the publisher was asked to do landed: §3a recomputed fresh (13/9 and 8/7, both
  correct against the file), §3b rebuilt as an explanation rather than a stale table, §3g created,
  §4 re-anchored to the new section numbers, §5 rebuilt from the current draft, D8 rationale
  rewritten instead of left standing.
- Zero-volume dependency is surfaced, not dropped: pkg :307-309 plus `publisher-report.md` §4.4.

### B. Factual accuracy — 4/5

The **body** is clean. Every figure traces:

- `96-97% / 1.5-2.0 cm` at pkg :607 is `accuracy-formulations.md` §1.1 verbatim; `less than 1 cm`
  at pkg :591 is §1.2's preferred variant (FX-002). The two benchmarks are never combined and
  0.40 cm never appears. `±3.5% average error margin` ships with the symbol intact in both
  instances, sourced to real-world conditions, never to "internal validation" (B4.3 held).
  Smart Scales is plural and carries `(beta)` at first mention (Outputs row) and twice more.
- Validation population `16 to 78 / 150 to 220 cm / 38 to 210 kg` matches §1.4; no 150-205 cm.
- No invented customer. No named client at all, which is honest here — `publisher-report.md` §4.3
  keeps "no named bariatric customer story" open.
- **Sourcing: 9 external citations, all neutral-quality, no vendor blog** — CDC ×2, ASMBS ×2
  (2025 fact sheet PDF, 2026 news release), CMS, PMC, ACS Bulletin, JAMA Surgery doi, Johns
  Hopkins. This clears the external-sourcing floor comfortably.

Three slips, all in the package's **own verification prose**, in a package whose §3a opens by
warning about two prior miscounts:

- **pkg :231** — *"9 external citation links (CDC x2, ASMBS x3, CMS, PMC, ACS Bulletin, JAMA
  Surgery doi, Johns Hopkins)"*. The parenthetical enumerates 10 and the file contains ASMBS ×2,
  not ×3. The total, 9, is right; the breakdown is not.
- **pkg :120** — *"the product name enters the body from §6 onward"*, used as the argument for
  keeping FitXpress out of the title and description. FitXpress first appears in **§2, Stage 1**
  (pkg :550, "FitXpress returns structured body data"). The conclusion survives; the supporting
  statement is false.
- **pkg :342** — *"21 comment markers across 18 comment lines (two lines carry two markers each)"*.
  18 lines with two doubled lines is 20, not 21. The real distribution is one line with three
  markers (the CDC/ASMBS/PMC sentence in the intro, pkg :517) and one with two (pkg :591). Totals
  21 and 18 are both correct; the explanation of them is not.

Unverified carry-forward, not scored: the Chhabra study is described as drawing on Epic Cosmos
records "from 2019 to 2025" (pkg :579) while `review-1.md` :77 dates the Epic Cosmos analysis
2018-2025. B3 ruled this attribution correct as-is and it is a different release, so I did not
re-open it — flagging only so nobody assumes it was re-checked this round.

### C. Brand & tone — 3/3

- Zero em/en dashes. Zero banned words. No triple parallelism (the comma lists at pkg :593, :641
  are literal enumerations of four or more items).
- `positioned as` appears exactly once, in the licensed sentence: *"It is not positioned as a
  medical device."* (pkg :624). Equivalence uses guardrail #7's wording (*"not equivalent to
  dual-energy X-ray absorptiometry (DXA), bioelectrical impedance analysis or a calibrated
  scale..."*, pkg :593), never `accuracy-formulations.md` §1.9's "positioned as equivalent".
- Corrective `rather than` ×3, all inside B4 boundary sentences the decisions file forbids
  rewriting. `so` at pkg :515 is the inversion "and so does", not the banned result connector.
- No anti-positioning violation, no "most accurate", no diagnosis/decisioning/clearance claim.
  The eight-statement "does not do" block at pkg :624 gained B2's payer sentence and closes on the
  licensed medical-device line.
- Register is the measured, operator-facing one `about-me.md` asks for; the reframe move survives
  at pkg :607 ("accurate enough for which decision").

### D. Format & structure — 3/3

- Frontmatter carries `product: fitxpress`, `status: ready_for_review`, slug, dates, `revised`,
  `source_draft`, `lint_verdict`, `review_applied`. Path and filename follow convention.
- Meta title 54 chars, primary keyword at position 1; description 145 chars. Both inside the hard
  bands.
- Package structure (§0 CMS warnings → §6 body → STOP) matches the prior package; §6 carries zero
  HTML comments (verified against `draft-v3-editor.md` line by line — the body is byte-identical
  minus the 21 markers, no stray double spaces).
- The reviewer's ten sections ship as unnumbered front matter + 10 H2s, with their §10 split into
  §9 FAQ and §10 next steps. Disclosed in `editor-report-review-1.md` :23-26 and consistent
  everywhere the package cites a section number. I checked every §-reference in the package
  against the new numbering; all resolve correctly.

### E. Output quality — 3/4

The restructure works. The four-stage workflow now opens at roughly 20% instead of 45%, and the
chain holds end to end: §2 closes on "Each of the four stages names the person who reviews" and §3
opens on "Stage 4 hands the record to a pre-authorization coordinator"; §3 closes on who now
arrives at intake and §4 answers it; §4 closes on the record that begins earlier and §5 tracks it.
The intro compression is real, not a truncation — CDC prevalence, the ASMBS 1% reach figure and
the attrition spread all survive in two sentences. Payer discipline holds in all five required
places (Use Case Role row, §1, §4 :583, §7 table, FAQ Q3 and Q8), and the "supporting evidence"
frame is now stated rather than implied.

Four things stop it short of 4:

- **Near-duplicate copy, §5 and §6.** pkg :591 — *"Smart Scales carries a ±3.5% average error
  margin against scale weight under real-world conditions, averaged across captures rather than
  guaranteed on any one of them. Programs should treat it as a software estimate and continue
  using a calibrated scale wherever their clinical protocol requires a directly measured weight."*
  pkg :611 — *"Against scale weight it carries a ±3.5% average error margin under real-world
  conditions, an average across the evaluated captures rather than a bound on any single reading.
  A calibrated scale remains the reading wherever a clinical protocol or a payer requires a
  directly measured weight."* Roughly 55 words of the same content twice in adjacent sections.
  This is the one genuine over-application of the round: B4 supplies both a "wherever the figure
  lands" block and a separate post-operative block, and both were placed. The accuracy-discipline
  gate requires the framework link in a paragraph carrying a figure; it does not require the
  figure twice.
- **`predicted weight through Smart Scales (beta)`** appears three times (pkg :526, :550, :603) and
  the DXA/BIA/calibrated-scale boundary three times (pkg :593, :624, :706). The editor names both
  in `self_check` and declines to touch mandated text, which is the right call — but the residue
  is visible to a reader.
- **Use Case Summary "Problem" row is the one payer-verification frame left standing**: *"pre-auth
  packets built from notes a payer reviewer cannot date"* (pkg :524). B2 lists the Use Case Summary
  first among the places the drift appears, and B2's own §5 instruction cut the mirror-image clause
  ("a reviewer at the payer cannot confirm when it was taken or how") from the body. The Role row
  two lines below counteracts it, so this is a wobble rather than a violation — but it is the
  strongest payer-acceptance residual on the page and it was not flagged anywhere.
- **Thin structure in two spots**: the "Patient progress tracking" FAQ H3 now holds a single
  question, and the `Payer acceptance` row in a *comparison* table has two identical cells. Both
  follow instructions exactly; both read as artifacts of the edit rather than as authored copy.

Inherited, not created this round, and low priority: British/American spelling is mixed —
`labour` (:544), `counselling` and `behavioural` (:593, :597) against `standardized`,
`organizations`, `characterizes` — on an article whose regulatory spine is CMS and Medicare.
Present since `draft-v1-writer.md` and in `plan.md`; worth one pass before publish.

## Top 3 issues (priority for improver / coordinator)

1. **The ±3.5% passage ships twice, in §5 and §6, and the package does not say so.** The editor
   flagged it and asked for a ruling; it appears in neither `publish-package.md` nor
   `publisher-report.md` §4. Either rule that both blocks stay (and record why) or cut one — but
   it should not reach Vadim as an unmarked repetition.
2. **Editor-escalated judgment items are not making it into the checkpoint artifact.** Two flags
   raised, one carried to the publisher report, zero carried to the package. The pipeline already
   proved it can do this well — §3g exists because D7 said "record it in the package". The same
   discipline should apply to flags the editor raises on its own.
3. **Three arithmetic/self-verification slips in the package's own prose** (:231 ASMBS ×3, :120
   "product name enters the body from §6 onward", :342 "two lines carry two markers each"). None
   reaches the CMS, but §3a's whole premise is that recomputed numbers beat carried-forward ones.
   A recomputed number stated wrong is worse than one carried forward, because it is trusted.

## Coordinator review

