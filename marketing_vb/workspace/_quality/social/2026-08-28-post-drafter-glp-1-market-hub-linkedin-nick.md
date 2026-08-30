---
qc_date: 2026-08-28
agent: post-drafter
artifact: workspace/social/articles/glp-1-market-hub/linkedin-nick/post.md
track: social
artifact_type: post
total_score: 17/20
status: good
coordinator_review:
---

# QC Report — post-drafter — 2026-08-28

**Artifact:** `workspace/social/articles/glp-1-market-hub/linkedin-nick/post.md`
**Total: 17/20** — good

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5

- Correct source. Line 16 cites `published-live-2026-08-28.md`, not a superseded `draft-v*`. Every claim in the body traces to that file.
- `linkedin-nick` brief honoured item by item: US lens (line 27 "largest US employers", line 41 "For US teams in employer-sponsored channels"), focus areas from the brief's list (enterprise partnerships, evidence generation, healthcare workflows), the prescribed structure hook → short paragraphs → discussion question → article, 249 words inside 180-250, 1 emoji, 0 hashtags, no European regulatory context. GLP-1 expanded at first use per the run brief's mandatory rule; BMI not used.
- Sibling posts were actually read, and it shows in two checkable places. Line 18 lists the five angles already taken; all five are correct against the files on disk (twitter = market scale, instagram = the individual check-in record, facebook = the four delivery models, linkedin-company = the market-structure shift, linkedin-katerina = procurement governance). The KFF employer block is genuinely untouched by all five. Line 53 coordinates with the Twitter crop by name rather than colliding with it.
- **The one shallow step: the self-check was never reported.** Run brief lines 62-67 state that `post-brand-checker` is not callable from this agent's toolset and that the drafter must instead "run the 10-point checklist, the Part 2 terminology guardrails and the ai-tells hard fails yourself, and **report your self-check**." The artifact reports a scoping guard (line 20), a US-lens note (line 21) and a claims list (line 19), which covers the highest-risk dimension well, but there is no terminology-guardrail or ai-tells line anywhere in the file. The substituted check is the one the coordinator explicitly asked for, and it is missing.
- Not scored: `brand-assets/past-posts/linkedin-nick/` does not exist, so step 4 of the spec is unrunnable. Per the spec and the run brief's past-posts map, continuing without it is correct behaviour.

### B. Factual accuracy — 4/5

- **Statistical scoping is largely done right, and tighter than the source in one place.** Line 29 carries the qualifier at the numbers: "among surveyed firms with 5,000 or more workers, 43% provided coverage in 2025, up from 28% in 2024." The 59% and 66% are attributed to "those that provided coverage" — the live article buries that attribution in the table's indicator column (line 61) while the figure column does not carry it; the post moves it into the sentence with the numbers. Line 31 restates the limit in the first person before any consequence is drawn.
- **The hedge is preserved, not hardened.** Line 33 reads "may contribute to greater interest in consistent program-level reporting", matching live line 85 word for word on the modal. No "does", no "is driving".
- **Line 27 is the scoping slip: "Coverage ... moved quickly inside the largest US employers."** The subject is the population of largest US employers, with no survey qualifier. The article's own indicator column says "the very large employers included in the survey" (line 60). The post self-limits two sentences later, but line 27 is the hook, i.e. the part visible above "see more", and it is the only sentence in the post where the guard does not apply.
- **Line 33 "for those firms" drifts from its antecedent.** The nearest plural in line 31 is "firms that size", which is broader than the article's attribution for the utilization and spending effects ("the surveyed firms that provided coverage", live line 61). Small, but it is in the exact dimension being audited.
- Line 37 "Program-level reporting is assembled from individual check-in records" is an inference. The live page says reporting requirements vary by structure and contract (line 85) and that employer-supported programs "may require aggregate reporting" (line 141); it does not state that composition. Low severity — this is a logical bridge, not a number or a product capability.
- Product claims all clean. "Two photos, front and side, roughly 30 to 45 seconds, no special hardware" matches live line 145 and is consistent with `proof-points.md` (2 photos, under 45 seconds). "Typical scan-to-scan differences of less than 1 cm" for "most evaluated measurements" matches live line 147 and `proof-points.md` Repeatability (`< 1 cm`); no universal accuracy number is asserted anywhere, per `about-me.md`. "It is not a medical device and does not determine treatment eligibility" is the direct 2026-08-25 framing.
- No invented customers, no invented numbers, no anti-positioning claim, correct product (`fitxpress`). The $200B incretin figure is not used at all, so the incretin-vs-GLP-1 trap in the run brief is avoided by construction.

### C. Brand & tone — 3/3

- Grep across the whole file: zero em dashes in the post body, zero banned words (leverage / utilize / harness / robust / seamless / comprehensive / delve / tapestry / realm / unlock / unleash / game-changing / cutting-edge), no `positioned as`, no `objective` about our output, no `by hand`, no `plus` stacking, no `so` introducing a benefit. The only em dashes in the file are in the `## Post — linkedin-nick — glp-1-market` heading, which is the drafter template's own format (post-drafter.md line 115), not published prose.
- Line 35 "with reporting rights determined by contract and applicable privacy requirements" applies the terminology-guardrails "write relationships explicitly" rule rather than compressing it.
- No presumed-reaction opener, no "not just X, it's Y", no adjectival punch triad. `you` is absent; `I` appears twice, correct for a personal profile.
- `audience.md` respected on both segments this post touches. Segment 1 (Telehealth/GLP-1): repeatability framing present, no DEXA or scale-replacement claim, no eligibility decisioning. Segment 4 (employers/insurers): claims kept soft, no implication that a reward or eligibility decision is automated.
- Voice matches `about-me.md` "honest about limits" — line 31 states the limit and then argues from it rather than bolting a disclaimer on the end. Rule 6c satisfied: the post takes a position ("The operational work starts at capture").
- Blocked checks, not scored: the social-track 3-post style comparison cannot run because `brand-assets/past-posts/linkedin-nick/` does not exist; `detect-ai-tells.py` not run (this QC pass has no Bash).

### D. Format & structure — 3/3

- Frontmatter complete: `profile`, `platform`, `article_slug: glp-1-market` (the published slug, not the folder name — the error caught on the first two posts is not repeated), `product: fitxpress`, `status`, `created`, plus useful extras (`handle`, `article_url`, `vertical`, `format`). Correct path.
- Word count independently recounted at ~249, matching the self-report and inside the 180-250 brief. No headroom left at the ceiling.
- All four design-tip fields present. Design tokens correct per `DESIGN.md`: `#050F40`, `#143DFF`, Satoshi — no `#2962FF`, no Inter. Line 54 explicitly states that `cover-3.webp` is photographic and not the reference, which is the correction the run brief carried forward from the Twitter QC.
- Manifest handled correctly: one `linkedin-nick` entry appended, exactly one length field (`word_count_body: 249`, the right unit for a `linkedin-*` profile), all eight other entries untouched, `ready_for_review: false`.
- Deviation noted, not penalised: `Claims used` / `Scoping guard` / `US lens` / `Length` are not in the post-drafter template. They make the artifact auditable against the run brief, which is why the scoping check above could be verified line by line.
- Very minor: the `Article visual` field substitutes a live in-body asset without noting that `publish-package.md` §4 carries no OG direction. The substitution is the coordinator's instruction, so it is not a miss, but a designer reading only this file has no way to know why §4 was not quoted.

### E. Output quality — 3/4

- Copy is close to publishable for a BD profile, and the angle is genuinely differentiated inside a nine-post pack — verified against all five siblings that preceded it, none of which used the employer-coverage block.
- Best thing in the artifact: the scoping caution is the argument, not a disclaimer. "One survey, very large employers only, and I would not read it wider than that ... it still says something about the buyer across the table" turns a limitation into the credibility move, in a sales-facing channel where that is the hardest place to do it.
- The design tip does work above the brief: it instructs the designer to set "surveyed firms with 5,000 or more workers, 2025 KFF Employer Health Benefits Survey" as a readable footnote rather than fine print, because the live asset's own label reads "43% large employer coverage" with no qualifier. That fixes an under-scoped label in the published asset.
- Deductions are the two scoping wobbles in B. Both sit in the highest-visibility lines (the hook and the consequence paragraph), and both are ~5-minute edits — which is the definition of a 3, not a 4. With 249 of 250 words used, the fix has to trade words out, not add them.
- Watch item, not scored: format is `text + photo` with the URL inside the body (line 43). An attached image suppresses the LinkedIn link preview, so the URL will render as bare text under the stat card. A publishing-time decision, not a defect.

## Top 3 issues (приоритет для improver)

1. Line 27: "Coverage ... moved quickly inside the largest US employers" makes the population of largest US employers the subject of a survey finding, with no qualifier, in the one line that shows above "see more". The post's own guard on line 31 arrives two sentences too late to protect it.
2. Line 33: "for those firms" points at "firms that size" (line 31), not at the article's actual attribution for the utilization and spending effects ("the surveyed firms that provided coverage"). The antecedent needs to be restated, not inferred.
3. The self-check required by run brief lines 62-67 (terminology guardrails Part 2 + ai-tells hard fails, reported in the artifact because `post-brand-checker` is not callable) is absent. The scoping guard and claims list cover one dimension well and are the reason this artifact is auditable; the substitute compliance check the coordinator actually asked for is still missing, and nothing in the file shows it was run.

## Coordinator review

