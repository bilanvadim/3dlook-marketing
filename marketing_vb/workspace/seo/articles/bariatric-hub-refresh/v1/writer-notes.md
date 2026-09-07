---
slug: bariatric-pre-qualification-mobile-3d-body-scanning
workspace: bariatric-hub-refresh
artifact: writer-notes for draft-v1-writer.md
stage: write (checkpoint 1 closed, approved 2026-09-03)
author_agent: seo-section-writer
created: 2026-09-03
gate: PASS (scripts/article_lint.py, 9/9 gates, run against the 2026-09-03 pack)
---

# Writer notes, Bariatrics hub refresh

All 12 sections written in one pass. FAQ Branch B (16 questions in 4 blocks). Draft at
`draft-v1-writer.md`. The linter is green; everything below is judgment the editor and the
publisher have to see, not mechanics.

---

## 1. Gate status

```
python3 scripts/article_lint.py workspace/seo/articles/bariatric-hub-refresh/draft-v1-writer.md \
  --pack workspace/seo/_context-packs/2026-09-03-bariatric-hub-refresh.yaml --report
```

`VERDICT: PASS`, all nine gates ok on the final file.

| Gate | Result |
|---|---|
| hard bans (detect-ai-tells, channel `article`) | ok. `CLEAN`, ai_density 0.85/1000 (budget 6.0), rhythm variation 0.53 (want >0.35), 0 em/en dashes |
| prose length | ok. 4,939 prose words vs target 4,400 (band 3,740 to 5,060) |
| claim traceability | ok. `FX-001, FX-002, FX-005, FX-006, FX-007, FX-008, FX-009` |
| banned claims | ok |
| superseded figures | ok (150 to 220 cm, DXA, no `body composition values`, no `predicted weight`) |
| internal links | ok. 18 links, 10 distinct, directions `{up: 1, sideways: 6, down: 1, trust: 1}` |
| keyword placement | ok. `bariatric pre-qualification` in H1, first paragraph, H2 #6; 7 occurrences |
| abbreviations (M1) | ok |
| accuracy discipline | ok. figures present, framework linked from both figure paragraphs |

Three earlier failures, fixed rather than argued: `utilization` is a CLAUDE.md banned word and it
was in the JAMA Surgery table row three times (now "use" / "rate of use"); `, plus the P2 lead
magnet` inside an HTML comment tripped the terminology gate, because the detector reads comments
too; and three lines carried a bare year or `CMS-0057-F` with no claim marker.

## 2. Per-section word counts

`prose_words` counts table cell text. The plan's per-section targets read as prose targets, so both
columns are here. Against the no-table column the draft is 4,493 vs a 4,400 target, +2%.

| Section | Plan target (Branch B) | All | Excluding table cells |
|---|---|---|---|
| Front matter (H1, opening, Use Case Summary, disclaimer) | 300 | 380 | 280 |
| 1. The bariatric intake gap | 360 | 367 | 367 |
| 2. Short answer | 180 | 179 | 179 |
| 3. Why now (1): the 7-calendar-day clock | 420 | 400 | 400 |
| 4. Why now (2): GLP-1 and the funnel | 400 | 421 | 257 |
| 5. Why now (3): current BMI vs qualifying history | 350 | 362 | 362 |
| 6. The pre-qualification workflow | 360 | 345 | 345 |
| 7. Where FitXpress fits | 280 | 324 | 270 |
| 8. Patient progress tracking | 400 | 406 | 406 |
| 9. What improves, and what it does not do | 250 | 281 | 281 |
| 10. Comparison, buyer fit, pilot diligence | 300 | 446 | 320 |
| 11. FAQ | 700 | 945 | 945 |
| 12. Next steps and related reading | 100 | 83 | 83 |
| **Total** | **4,400** | **4,939** | **4,493** |

**The FAQ is the one real overrun: 945 against 700.** Branch B's 16 questions cost about 170 words
in question text alone before a single answer, so 700 was only reachable at roughly 33 words per
answer, which is under the 2-to-5-sentence floor in guidelines §14. Answers average 45 words. If the
editor wants the 700, the cheapest 150 words are the second sentences of Q7, Q9, Q11 and Q12; taking
them out costs GEO liftability, which is what the block is for.

## 3. Decisions and deviations, each reversible in one edit

1. **The disclaimer is verbatim except for two words.** The live sentence opens *"Mobile body
   scanning solutions described in this article do not determine..."*. `this article` is a hard ban
   the detector enforces mechanically with no scope-note exemption, and the brief lists it as a
   linted hard rule. Written as **"described here"**. Every boundary word after that is untouched.
   If legal wants the live string back, it costs exactly one `terminology_guardrails` hard fail and
   the file otherwise still passes.
2. **Section 4's H2 is not the plan's title.** The plan's *"GLP-1 reshaped the funnel, not just the
   volume"* is an `X, not just Y` corrective construction (terminology guardrails Part 1, judgment
   row). Written as **"Why now (2): GLP-1 changed the shape of the intake funnel"**. The section's
   argument is unchanged.
3. **`utilization` never appears**, because CLAUDE.md §6 bans it. The JAMA Surgery finding is
   published by its source as a *utilization* change and appears here as "change in surgery use",
   "surgery use down 34.1%" and "a rate of use within that cohort". The scope words that matter
   (rate, not count; one insured claims cohort) are all intact. Flagging it because a fact-checker
   reading the source will see a different noun.
4. **The sleeve-gastrectomy share is qualitative, not 58%.** The plan asks for the share cited to
   the ASMBS Fact Sheet. The pack's `external_citations` does not carry 58%, and the gap analysis did
   not verify it, so the draft says "more than half of annual volume", which is what the live page's
   own FAQ says. Publishing 58% needs someone to read the Fact Sheet and confirm it first, and the
   pack bans any number not in `approved_claims` or `external_citations`.
5. **The mid-body eBook block is omitted** (audit Open Item #10). `blog-style-guide.md` §5 allows one
   CTA and forbids banner promos mid-body, and the plan sets one CTA in Section 12. It is a deletion,
   not a decision: restoring it is a paste, and it belongs to Vadim or the publisher.
6. **CTA email kept as `sales@3dlook.ai`**, matching the live page, even though CLAUDE.md's team
   addresses are `@3dlook.me`. Not a writer's call to change a published contact address.
7. **KPI list moved out of the front matter.** The plan names the KPIs in Section 10 as well, and
   running the same four-item list twice inside 4,900 words reads as padding. The front-matter
   paragraph now names the roles and states what those roles answer for.
8. **`bariatric surgery requirements`** appears in the documentation sense only, in Section 5 and
   FAQ Q16, both times as "what has to be in the file, dated when". No qualifying BMI, no payer
   threshold, no eligibility guidance anywhere on the page.

## 4. The `<!-- ext-claim: ID -->` marker convention, and why it exists

`article_lint.py` gate 3(b) requires a claim marker on **every** prose line carrying a product-shaped
figure, and its number regex matches any 4-digit run, so `2026`, `40.3%`, `270,000` and `40,265` all
demand one. Gate 3(a) then rejects any `<!-- claim: X -->` whose id is not in the pack's
`approved_claims`, and the pack has ids for the ten FitXpress claims only. There is no id in the pack
for a CDC or an ASMBS figure.

So external figures carry **`<!-- ext-claim: SOURCE-ID -->`**, which the gate treats as a sourced line
without pretending the figure is one of ours. Nine source ids, 15 markers: `CDC-DB508`,
`CDC-PCD-2023`, `PMC12964095`, `ASMBS-FACTSHEET-2025`, `ASMBS-2026-05-05`,
`ASMBS-2026-05-05-CHHABRA`, `ACS-BULLETIN-2025-04`, `JHU-2025-JAMA-SURG`, `CMS-0057-F`. Every one of
them also has an inline anchored link to the primary source in the same paragraph, so the marker is a
trace aid and the link is the citation. The JAMA Surgery 2026 figures need no marker because they sit
in table rows, which the gate exempts, and they carry their citation on the anchor in the cell.

**This is a real gap in the pack shape, not a trick.** The right fix is an `external_claims:` block
in the context pack with ids the linter can resolve, the same way `approved_claims` works. Worth
raising with whoever owns `context-pack-builder`, because every article with third-party statistics
hits this.

## 5. The three volume series, and how they are kept apart

- ASMBS national estimate (more than 270,000 in 2023, down about 3.5%) and the JAMA Surgery 2026
  cohort never share a sentence. They sit in **separate rows** of the market-indicator table, and the
  paragraph under the table states the incomparability in ASMBS's own terms without putting a figure
  from either series in the same clause as the other.
- Every cohort figure carries "one insured claims cohort" or "the same claims cohort", in the table
  and in the third column.
- The `-34.1%` figure is labelled a rate, with "absolute counts in the same cohort move about 7.3%
  lower" beside it, so nobody reads it as a count collapse.
- The `230,207 / 177,297` series does not appear.
- The semaglutide ex-US exclusivity angle does not appear.
- "Surgery appears to be rebounding" does not appear (audit Open Item #7).

Guardrail #2 check, byte-identical across body, table and FAQ: `7 calendar days` / `7-calendar-day`
(adjectival form only), `72 hours`, `1 January 2026`, `90-95%`, `about 8%`, `less than 1 cm`,
`96-97%`, `1.5-2.0 cm`, `±3.5%`, `150 to 220 cm`, `38 to 210 kg`, `16 to 78`.

## 6. Accuracy handling

- FX-001 and FX-002 are copied **verbatim** from `accuracy-formulations.md` §1.1 and §1.2, hyphens
  and all. Nothing was reassembled from `proof-points.md`.
- Accuracy sits in Section 7 only; repeatability sits in Section 8 and FAQ Q10 only. The accuracy
  framework article is linked **inside each of those three paragraphs**, which closes the live page's
  hard FAIL on the trust direction.
- The ISO 8559 benchmark (`0.40 cm`, FX-003) is absent from the page, per audit §C. `95%+
  repeatability consistency` (FX-004) and the bariatric TAM/SAM (FX-010) are absent too. The linter
  reports all three as "approved but uncited", which is the expected reading, not a gap.
- Every figure carries its condition in the same sentence or the next: which reference, which
  protocol, which population, and which decision the tolerance has to serve.
- No reserved words about our own evidence. FX-006 states the negative directly.

## 7. Internal links, four directions

| Direction | Target | Where | Anchor |
|---|---|---|---|
| up | `ai-body-data-health-hub` | S2 | "AI body data for health hub" |
| sideways | `online-pharmacy-bmi-verification-a-2026-compliance-guide` | S3, S12 | "compliance guide to online pharmacy BMI verification" |
| sideways | `glp-1-market` | S4, S12 | "GLP-1 market hub" |
| sideways | `the-potential-of-ai-in-telehealth` | S8, S12 | "AI in telehealth hub" |
| sideways | `occupational-health-screening-software` | S10, S12 | "occupational health screening software hub" |
| sideways | insurance underwriting, wellness rewards | S12 | full titles |
| down | `/for-bmi-verification/` | S6, S12 | "BMI verification capability", "Request a FitXpress demo" |
| trust | `mobile-body-scanning-accuracy` | S7, S8, FAQ Q10 | inside the figure paragraphs |
| trust | Data/Privacy/Security/Regulatory FAQ | S10 | **plain text, no link**, marked "not yet published" |
| product | `/technology/` | S7 | "3DLOOK technology page" |

Two link notes. The year was dropped from two anchor phrases pointing at the online-pharmacy guide
("2026 compliance guide" became "compliance guide"), because gate 3(b) reads anchor text and demanded
a claim marker on the year; the published title is unchanged and the publisher can restore the year
if it also adds a marker. And the six down-link landing anchors for the P1 and P2 children are
**plain text with an HTML comment naming the child**, so the publisher can find them with
`grep "DOWN-LINK LANDING"`: S3 (pre-auth documentation), S4 (GLP-1 bridge), S5 (patient records),
S6 stage 1 (remote intake) and stage 2 (hybrid care), S8 (post-op progress + patient records),
S9 (pre-auth documentation + patient records + the P2 checklist lead magnet).

## 8. Could not source, and did not write

- **No bariatric customer story.** None exists in `case-studies/` or `proof-points.md`. Nothing
  invented, implied or anonymised. Every piece of evidence on the page is either a third-party
  citation with a link or an approved FX claim with a marker. It is the one place the page reads
  thinner than the insurance and wellness hubs, and audit Open Item #4 is the fix.
- **The 22.25% attrition cohort** is cited to the same 2026 narrative review as the "as high as 60%"
  figure, because that is where the gap analysis found it. If a fact-checker wants the primary cohort
  paper, it needs a separate lookup. "up to 50-60% as typical" is gone, and the range is presented as
  measurement-dependent, which is guardrail #4 satisfied rather than dodged.
- **`about 1%` and `90-95%`** are both from ASMBS and appear in the same paragraph in Section 1. They
  are different measures (surgical share of the eligible population; share receiving no treatment of
  any kind during the study period) and the sentence says so. No 33 million figure anywhere.
- **No sources were re-fetched during writing.** Every external figure comes from the pack's
  `external_citations` or the gap analysis, both dated 2026-09-03. The plan asked for the CDC
  *Preventing Chronic Disease* wording to be re-verified at fact-check; that is still open and the
  draft carries the live page's phrasing ("underestimated the prevalence of severe obesity by 40%").
- **Section 10's "what it depends on" row** attributes the scan-side dependencies (smartphone access,
  capture instructions, retake logic, deployment thresholds) to guardrail #5 rather than to a cited
  figure. It is a qualitative dependency statement by design.

## 9. For the editor

1. Judge the three "why now" sections as a set. They are three because the documented-BMI-history
   argument dies as a paragraph inside a GLP-1 section, which was the audit's own reasoning; if the
   editor disagrees, S5 folds into S4 and about 100 words come out of the seams.
2. The FAQ needs a length decision (item 2 above).
3. `sales@3dlook.ai` vs `@3dlook.me` needs someone with authority over the address.
4. The disclaimer's two changed words need a yes or no, not a silent restore.
5. Nothing in `plan-audit.md` §C was reintroduced. Nothing in §N was covered: no clinical outcomes,
   no benefits, no side effects, no procedure comparison, no post-op diet or vitamins, no qualifying
   BMI, no payer threshold, no SOC 2, no pricing, no competitor.
