---
plan: plan.md
slug: accuracy-drives-roi-digital-health
workspace: accuracy-roi-telehealth-refresh
created: 2026-09-23
---

# Plan audit: accuracy-drives-roi-digital-health refresh

Why `plan.md` looks the way it does. Read by `seo-publisher` and Vadim; the writer does not need it.

## 1. Decisions made

| # | Decision | Why |
|---|---|---|
| D1 | Phase 0 gate overridden; refresh in place, slug unchanged | Vadim's explicit «го» of 2026-09-23. Both rows are non-create (`Refresh / expand existing`, `Create if validated`). Precedent: bariatric-hub-refresh, glp-1-market, online-pharmacy-bmi-verification |
| D2 | GLP-1 clinic-operations row delivered as one ~200-word section, not a standalone page | Row 2 offers "section in this URL" as an option. A standalone page would compete with `glp-1-market` on progress tracking, and demand for the clinic-ops phrasing was not measured |
| D3 | Primary keyword `digital health roi` (40 / KD 0) | The only measured term matching the page's promise and the H1; 115 SC impressions at pos 18. The GEO family ("self-reported vs verified", no Ahrefs data, pos 4-9 in SC) is carried by the short answer and Section 4 instead of being named primary, because Ahrefs cannot measure it and it would not describe the ROI half of the page |
| D4 | H1 keeps "Accuracy and ROI"; content-plan title after the colon; shorter SEO title carries the self-reported vs verified question | Keeps both ranked word sets. 86-character H1 would truncate as a SERP title |
| D5 | ROI model with named variables and no worked numeric example | Brief forbids 3DLOOK outcome numbers. A worked example with "illustrative" figures would still be read as a claim, and the number-drift gates would treat it as a figure to substantiate |
| D6 | Every live unsupported number defaults to CUT; only the CDC *Preventing Chronic Disease* figure is kept as the preferred evidence line (still subject to writer verification) | It is the figure the BMI guide already publishes, so the two pages agree (guardrail #2); the NHANES, PLOS and "40% lack scales" lines duplicate its point with weaker sourcing |
| D7 | Comparison table uses the four methods of the BMI guide's "Remote verification methods", with self-report replacing the guide's "hybrid" column | Brief requires self-report as a column; hybrid is covered in the reading after the table and in Section 8 |
| D8 | Accuracy paragraph (S7) and repeatability paragraph (S6) in different sections, both in `accuracy-formulations.md` §5 short form, framework link in each; no ISO figure | Two-benchmarks rule and sentence-length gate; §5 forms were approved in the 2026-09-11 editorial final |
| D9 | No full "What FitXpress does not do" H2; boundary carried by the scope note, S7 item 6 and FAQ 1-2 | `editorial-rewrites.md` §7 for workflow articles whose hub owns that section |
| D10 | Yazen (FX-YAZEN) allowed as an optional one-sentence volume signal in S7; UK Meds not used | Pack approves both; UK Meds would pull the page toward the BMI guide's territory. Neither is attached to the ROI model |
| D11 | Byline Vadim Bilan kept | His own article; flag in the digest (CLAUDE.md §15 default is Assel) |
| D12 | Target 2,150 words | Baseline 1,280 plus three required assets and a FAQ, minus about 350 words of cut claims and the repeated use-case list. §7 format finals land near 1,900; this page adds the model |

## 2. Alternatives rejected

- **Standalone GLP-1 clinic-operations article.** Cannibalization with `glp-1-market`; row is conditional.
- **`remote patient monitoring` (6,800 / KD 51) or `remote patient monitoring software` (1,100 / KD 12) as primary.** The SERP is RPM platforms and reimbursement codes; the page does not own that intent and would lose on it. Used once each as a secondary term.
- **Keeping the retention arithmetic as a "hypothetical".** Cut. It reads as an outcome claim; retention belongs to the engagement article.
- **Title "…: A Workflow Comparison".** The page's main asset is the ROI model.
- **A metrics table or vendor diligence list.** The BMI guide owns the procurement checklist; §7 format excludes both.

## 3. Deletions ledger (live → refreshed)

| Live element | Fate |
|---|---|
| Precision-medicine opening, "eligibility without ambiguity" | Cut; replaced by operational scene + scope note |
| NHANES / PLOS / 40%-no-scales lines | Cut unless verified (default cut); CDC PCD figure preferred |
| "Regulatory bodies now demand…" | Cut |
| Time-savings block (10 min, 16 h vs 1.25 h, 93%, +20% capacity) | Cut; replaced by the ROI model |
| "Risk Reduction Through Documentation" | Reduced to one sentence in S3; documentation belongs to the pending telehealth-documentation article |
| Retention arithmetic ($5-6M) | Cut |
| "Personalization Built on Reality" incl. "Dose medications accurately." | Cut |
| "Deploying FitXpress" bullet list | Rewritten as S7 with canon wording |
| "Proven Use Cases" (3 H3s) | Cut; the BMI verification case is linked, progress tracking moves to S6 |
| "The Path Forward" + CTA | Two-sentence Next steps, one CTA |
| Further reading (3 links) | Publisher to verify liveness and relevance; default drop |

## 4. Open items for Vadim

1. **Thin demand, accepted knowingly.** Primary term 40/month; the GEO family has SC impressions but no Ahrefs data. The refresh is justified by the deindexing, the compliance defects and GEO/sales use, not by volume.
2. **Re-indexing is not guaranteed.** After republish, request indexing in GSC and add the three inbound links from gap analysis §6 (telehealth hub, BMI guide, glp-1-market). Without inbound links the quality signal may stay weak.
3. **Weight-estimate wording.** The BMI guide says "predicted weight"; the bariatric plan banned that term. The plan uses "weight estimate" / "estimated weight". Confirm, or align with the live BMI guide.
4. **Yazen named in content.** Optional sentence in S7. Confirm naming is fine on this page (no-client-names rule applies to outbound only).
5. **Byline** Vadim Bilan kept; confirm.
6. **Telehealth-documentation article** (pending Oct 2026): when it ships, add a link from S3's documentation sentence.
7. **Title** — recommended H1 is 86 characters; if Vadim prefers a single title for H1 and SERP, use option 2 (`Digital Health ROI: Self-Reported vs Verified Body Data at Scale`).
