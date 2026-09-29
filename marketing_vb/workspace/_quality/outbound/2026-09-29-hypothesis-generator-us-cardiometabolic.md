---
qc_date: 2026-09-29
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-09-29-us-cardiometabolic/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 17/20
status: good
coordinator_review: done
---

# QC Report: hypothesis-generator, 2026-09-29

**Artifact:** `workspace/outbound/campaigns/2026-09-29-us-cardiometabolic/hypothesis.md`
**Total: 17/20** (good)

Scored against: icp-detail.md §1, proof-points.md, accuracy-formulations.md §1.1-1.4, compliance.md, audience.md segment 1, the hypothesis-generator prompt, the 2026-09-29 obesity-medicine QC reports, `sales-nav-raw/export-1.csv` and `scripts/outbound_pack.py` CARD_SECTIONS. The messages card gets `Use case`, `Message angle`, `Rules for steps 3-5` and `Vadim's decisions`. The per-account table and `Target buyer persona` go to the validate card only. Vadim's standing decisions and the coordinator-confirmed Signos scan were taken as given. Limits, bans, detector and completeness were taken as passed. notify.py was not run: this QC session has no shell.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 5 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence: 5/5
- No issues. Every template section is present. There is an IN/OUT verdict for all 21 export company names, matched on URL. The Message 1 gate line is kept and the titles block is clean. Prior lessons are applied (post-mortem, both obesity-medicine QC reports). Both of the last hypothesis QC's top issues are fixed: the device premise is now per account, and FDA is answered only with the FAQ sentence (lines 176, 251).
- Export counts check out against the CSV: 108 rows, 9amHealth 31, Level2 18, Superpower 21, Signos 20+1, and 75/21/12 by tier and pool.

### B. Factual accuracy: 3/5
- **The artifact says something about its own links that is not true.** Open question 4 (line 319) says the GLP-1 hub carries "approximately 30 to 45 seconds", which goes against the one public definition. It then says "None of these is linked here." The GLP-1 hub is `/content-hub/glp-1-market/` (content-plan.md:44, plan-audit.md:83), and lines 19 and 237 link it as the M2 article for 9amHealth and Level2 in three lanes (about 20 people). Those M2s would say "under 45 seconds from the photos to structured results" and link a page with the retired variant.
- **Superpower (focus item 1): one per-account check is missing.** Line 92 cites Superpower's own guide listing waist-to-hip ratio as a body composition biomarker and naming DXA and BIA as methods. The artifact never checks two things. First, whether Superpower already records waist, hip or WHR for members (self-entry or synced apps). Second, whether it sells a DXA or BIA add-on. The "Not verified" column covers only weight and body fat. The Superpower lead (lines 92, 219: "adds" waist and hip circumference) assumes both answers are no. Line 24, "What none of those devices returns is circumferences", infers from device category and was not sourced per account.
- **Level2 presumes what its own table marks as unknown.** Line 91's "adds" column opens with "A body record next to glucose", but the same row lists "Whether Level2 records weight or any body data today" as not verified. The `clinical` lane (line 224, messages card) says "next to glucose, blood pressure and labs". Level2 BP and lab collection is not sourced anywhere.
- **Numbers with no source tied to them** (line 43, outside Rules and Why): Superpower "has raised more than $40M" and Signos "$129-$449 monthly plans".
- **Evidence #1 overstates its source** (line 121). The Lancet Commission accepts direct body-fat measurement *or* an anthropometric criterion alongside BMI. The paraphrase drops the direct-measurement route, and that is the route 9amHealth's new scale already covers.
- Line 16: "22 distinct `Company_name` values". The export has 21. Signos takes two table rows.
- Clean on the focus items: every number in `Rules for steps 3-5` and `Why this is plausible` comes from proof-points.md, accuracy-formulations.md §1.4 (38-210 kg) or icp-detail.md:597 (2-4 weeks), or has a source cited. (Rules labels 2-4 weeks as "from proof-points.md". It is not there, but it has been licensed before.) The compliance line is verbatim from compliance.md §9, and the SOC 2 and FDA sentences are verbatim from the FAQ. "Not a medical device" is scoped to UK/EU MDR. No client names appear in copy-seeding text except the ban list at line 248. The 34,000 line carries no name and no geography.
- Sourcing: about 40 external URLs, from primary, trade or regulator sources. There is no vendor-blog evidence apart from prospect-owned pages used as evidence about that prospect.

### C. Brand & tone: 3/3
- No lapses in the sections carded to the sequencer.
- Note only: line 172 (objection answer, validate card) has "so a pilot compares both", a result-introducing "so". It does not reach the messages card.
- Person-first language, the "comprehensive" and "objective" traps and the no-replacement framing (line 253) match audience.md segment 1 "Don't".

### D. Format & structure: 3/3
- No issues. The frontmatter is complete (`product`, `profile`, `market`, `use_case`, `cap_per_group`, `banned_terms`), the path is correct and the titles block has one title per line. The Use case is one sentence (66 words, carded verbatim: long but acceptable).

### E. Output quality: 3/4
- The article choice works against the artifact's own guardrails. Line 237 sends the sequencer to the section "Why Scale Weight Alone Provides an Incomplete Progress Record" for 9amHealth. Line 217 forbids implying "weight only" or "just a scale" to 9amHealth, which just rolled out body-composition scales. For Level2, line 218 says to say nothing about whether it records weight, and the same section title presumes scale weight.
- Otherwise strong, near reference quality. Name collisions and investors are caught by URL. Six people are re-grouped with a registry-safe record. The Signos hold is sourced, with a trigger list. The Level2/UHG buyer and procurement analysis is useful. The per-account "already has" guardrails, honest limits, and falsified/inconclusive thresholds at `nick`'s acceptance rate are all set out.

## Top 3 issues (priority for improver)

1. The GLP-1 hub is linked as the M2 article for 9amHealth and Level2 (lines 19, 237). The artifact's own Open question 4 (line 319) flags that same page for the retired "approximately 30 to 45 seconds" and says it is not linked. The section named for the sequencer, "Why Scale Weight Alone...", pushes the "weight only" implication that line 217 bans for 9amHealth.
2. Superpower's existing waist, hip and WHR capture (its guide lists WHR as a biomarker) and any DXA or BIA offering were not checked, and are missing from the "Not verified" column (line 92). The Superpower lead still presumes circumferences are new. Level2's "A body record next to glucose" (line 91) and "blood pressure and labs" (line 224) presume data marked unverified.
3. Two uncited context numbers (line 43: "more than $40M", "$129-$449 monthly"). The Lancet Commission paraphrase (line 121) omits the direct body-fat route. Line 16 says 22 distinct company names; there are 21.

## Coordinator review

(filled in by Claude in chat after the automatic QC run)

## coordinator_review

```
agreement: ✅ agree
top_issue: the M2 article for 9amHealth and Level2 was a page the hypothesis itself flags as carrying a retired figure and weight-only framing; sent back with all seven items before the list is stamped. The same hub went out in the 2026-09-29-us-obesity-medicine M2s: flagged to Vadim.
```
