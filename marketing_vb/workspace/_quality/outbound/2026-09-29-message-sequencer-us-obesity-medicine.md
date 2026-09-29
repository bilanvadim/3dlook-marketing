---
qc_date: 2026-09-29
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-09-29-us-obesity-medicine/messages/ (sample: carrollmedia, adrian-krutz-fnp-c-a0779554, angelafitchmd, nathan-linsley, joseph-grasso-2388b44, conradlai, christina-link-ms-rdn-ldn-cdces-64302321a; 5 summaries; _check.json)
track: outbound
artifact_type: message
total_score: 13/20
status: marginal
coordinator_review: done
---

# QC Report: message-sequencer, 2026-09-29

**Artifact:** `workspace/outbound/campaigns/2026-09-29-us-obesity-medicine/messages/` (112 people, 5 batches)
**Total: 13/20, marginal.** The copy alone scores 15 (good). The 2-point gap is the `product:` frontmatter cap in D, and the fix for that belongs in the `split-messages` template, not in the agent prompt.
This needs targeted fixes (22 referral M2s, 2 scan-count lines, a handful of copy lines). It does not need regeneration.

Scored against `card-messages.md` and the three `_profiles-*.md` files named by the coordinator. Every hook in the sample checks out against its profile card: Ryan's bio, Adrian's earlier roles, Nathan's bio, Joseph's Two Chairs FP&A role, Conrad's JumpstartMD co-founder row, and the knownwell Outcomes Report fact.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 1 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence: 4/5
- Three of five batches skipped prompt rule 7 (compliance line mandatory for healthcare ICP) across the referral lane: 22 of 29 referral sequences have it in neither message. All three summaries flagged the omission openly (form-health-1:9, flytehealth:8, mixed-1:8), so this is a flagged departure rather than a silent one. The rule is still broken. Scored under B per the outbound override.
- christina-link…:17-19. Ilant is Lane B (card:38: circumferences lead, and "Lean mass and fat mass estimates come from the same scan as a further line"). M1 leads with lean mass and fat mass and mentions circumferences only as "such as waist circumference".
- Batches read card:68 ("No brands other than the prospect's own") differently. flytehealth and form-health-2 withheld former employers (DrChrono, Cedar, Microsoft). Other batches name them: joseph-grasso:17 "Two Chairs", jenn-roberts:17 "Hello Heart", _batch-knownwell:271/387/403 (Interwell Health, One Medical, Carbon Health). One reading needs to be picked.

### B. Factual accuracy: 3/5
- **The compliance line is missing in 22 healthcare-ICP sequences.** The outbound override requires it, and so do card:65 ("One compliance line per sequence, in message 2") and compliance.md. Affected: joseph-grasso M2, conradlai M2, scott-albrecht, pete-moen, jenn-roberts and 17 others.
- **112,100 is stretched into a FitXpress process claim.** _batch-knownwell:169 (Brian Dragutsky M2) has "FitXpress runs the same guided capture each time: 112,100 scans in 2025 across all 3DLOOK customers". _batch-form-health-1:327 (Karla Saint Andre M2) has "112,100 scans ran in 2025 across all 3DLOOK customers, all using the same guided capture sequence". The figure is company-wide and includes Mobile Tailor apparel scans (proof-points:203: "as 3DLOOK-wide scale only… never attributed to one platform"). Nothing sources "all using the same guided capture sequence". _batch-flytehealth:43 (Ishraf) keeps the figure in its own sentence and is acceptable.
- **Accuracy wording, christina-link…:28** ("estimates of lean mass and fat mass, and circumferences at 96-97% accuracy against expert manual measurement"). Grammatically this is not a misattribution. The figure (accuracy-formulations §1.1) measures scan output against tape-measured body measurements, so it attaches to circumferences and not to the estimates. But the placement invites a misreading. The sentence opens "For the nutrition plan:", goes to a Director of Nutrition whose hook is lean mass, and puts lean mass and fat mass first in the same list. That reader will carry the percentage over to the body-composition estimates, and proof-points has no accuracy figure for those. It also narrows an aggregate stated "across body metrics" onto circumferences, where the study's own per-site errors are the largest (waist 2.14 cm, hip 2.25 cm). Verdict: ambiguous, not wrong. The figure must not share a sentence with lean mass or fat mass.
- carrollmedia:19 ("80+ body measurements come back in under 45 seconds") and the Karla M1 ("in under 45 seconds, in the Form app") paraphrase the single locked definition, "under 45 seconds from the photos to structured results" (proof-points:50). This is minor drift.
- christina-link…:19 says "inside the Ilant app". The card's Ilant facts never mention an app ("continuous insights from connected devices").
- No number outside proof-points, no client names, no pricing, and the compliance line is verbatim in all 90 sequences that carry it.

### C. Brand & tone: 2/3
- Presumed-knowledge openers, the same family as the `presumed_reaction` ban: adrian-krutz:17 "You know how an online visit starts.", conradlai:17 "you'll know this better than most", scott-albrecht:28 "since finance sees the whole picture", jenn-roberts:17 "you hear what employers want to see".
- adrian-krutz:17 "from nurse practitioner to regional director to running clinical operations" is a three-step chain, borderline under the template's triple ban.
- carrollmedia:17 hands the bio back nearly word for word ("Your bio on asynchronous data workflows and healthcare integrations behind the Form Health product is the reason for this note."), which reads scraped.
- Person-first language holds throughout. No banned terms and no stigmatizing framing.

### D. Format & structure: 1/3
- Hard rule: none of the 112 per-person files has frontmatter with `product: fitxpress` (CLAUDE.md §10.4). The cause is the `split-messages` output template. The card's Output format has no frontmatter slot, and the agent is barred from writing per-person files. The fix goes in `scripts/outbound_pack.py`.
- Everything else matches the template: char limits, signature, plain-text calendar link, one article per M2, no article in the referral lane, and summaries in the prompt's format.

### E. Output quality: 3/4
- adrian-krutz:17. "What does the clinician have on the patient's body that day?" is awkward and can be misread. At :28 the M2 core line is a feature ("Workflow detail: under 45 seconds…"), not the outcome the M2 template asks for.
- angelafitchmd:17. "Curious how you'd bring patients seen on video into that same record" sits right after the in-clinic lean-mass Outcomes Report. That implies phone estimates could join an in-clinic lean-mass dataset. This is the one reader most likely to reject that equivalence. M2 (:28) recovers by pivoting to circumferences.
- The knownwell referral M2s splice the compliance line in. nathan-linsley:26 has "For context on data handling: We support…" (colon, then capital W). _batch-knownwell:393 and :447 do the same. _batch-knownwell:409 (Ben) appends it with no bridge after "One name is plenty."
- scott-albrecht:17-19 and :28 never say what Nick does. The CFO has nothing to route on.
- Strong: carrollmedia is correctly technical for Lane D. angelafitchmd uses a real company-specific hook. joseph-grasso and conradlai are clean, short asks with no pitch. M2 openers vary within each company.
- Uniqueness ceiling: in wave-1 M2s at the same company, the verbatim compliance line plus the mandated article framing take up about half the characters. The card causes this, not the agent.

## Referral compliance line: which batch is right

**knownwell is right; the other 22 need the line.**
- card:65 says "One compliance line per sequence, in message 2, the US variant verbatim", with no lane exemption.
- The card lists the referral lane's exemptions precisely: the product specific (card:73), the article (card:58) and the calendar link (card:21, :41). The compliance line is not on that list.
- Prompt rule 7 and the rubric's outbound B override agree.
- "No pitch" does not conflict with the line: it states how data is handled, not what the product delivers.

To make all 29 consistent, add the verbatim line to M2 of the 22. Copy knownwell's placement (M2), but not its splice: the line should stand as its own sentence or paragraph, as it does in the 83 non-referral M2s. Rework the 7 knownwell ones the same way. The gate never checked compliance for `angle referral`, which is why the batches split. That check belongs in `check-messages`.

## Top 3 issues (priority for improver)

1. The compliance line is missing from 22 of 29 referral M2s (form-health-1: 8, flytehealth: 3, mixed-1: 11), against card:65. The 7 knownwell lines are spliced in with a colon and a capital "We". The gate does not check this lane.
2. 112,100 is presented as FitXpress guided-capture volume (_batch-knownwell:169, _batch-form-health-1:327). It is a 3DLOOK-wide count that includes Mobile Tailor, and "all using the same guided capture sequence" has no source.
3. None of the 112 per-person files has `product:` frontmatter. This is a `split-messages` template fix, and it holds D at 1 on every message-sequencer run until it is made.

## Coordinator review

(filled in by Claude in chat after the auto-QC run)

## coordinator_review

```
agreement: ⚠️ disagree on D only: the missing `product:` frontmatter is in per-person files written by `split-messages` for every campaign, not by the agent; the copy findings stand.
top_issue: 22 of 29 referral M2s lacked the card:65 compliance line because `check-messages` never checks it for the referral angle; all four batches sent back for targeted fixes before Vadim's checkpoint.
```
