---
qc_date: 2026-08-21
agent: post-drafter
artifact: workspace/social/articles/top-7-remote-body-composition-tools-glp-1-clinics/linkedin-vadim/post.md
track: social
artifact_type: post
total_score: 17/20
status: good
coordinator_review: "agreement: ✅ agree | top_issue: 'under a minute' loosened the sourced '45 seconds' figure — fixed post-QC"
---

# QC Report — post-drafter — 2026-08-21

**Artifact:** `workspace/social/articles/top-7-remote-body-composition-tools-glp-1-clinics/linkedin-vadim/post.md`
**Total: 17/20** — good

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 4 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- `linkedin-vadim` brief followed well: AU operational lens present (line 22 "a spread-out country", line 28 "For AU teams… the plumbing… procurement"), avoids US/EU/UK regulatory framing, closes with a discussion question (line 30), word count 244 (inside 180–250), zero hashtags, zero emoji.
- One sourcing slip: the capture-time figure was loosened rather than restated from source. `publish-package.md` §9 and `proof-points.md` (Speed) both fix this as "under 45 seconds"; the post wrote "under a minute" (line 26). proof-points was reflected everywhere else but not applied precisely here — the "read but not used exactly" pattern.

### B. Factual accuracy — 3/5
- **Line 26: "under a minute"** does not match the sourced figure. `proof-points.md` line 40 = "Under 45 seconds"; `publish-package.md` §9 confirms the article ships "under 45 seconds". This is not a hallucination (45s is under a minute, so it is technically true) but it is a loosened/vaguer restatement of a specific sourced number — a direct editorial-guardrail #2 violation (one number, everywhere the same). It also undersells: "under 45 seconds" is the stronger, more specific claim used on the live page. Strict reading of the QC hard rule ("number absent from proof-points → B ≤ 2") would cap this at 2; scored 3 because the basis figure exists and was rounded, not invented.
- All other numbers correct and sourced: "Two photos" (2 front+side ✓), "80+ measurements" ✓, "scan-to-scan repeatability under 1 cm" (< 1 cm ✓), positioning correct ("isn't a medical device", "doesn't replace DXA or a calibrated scale", "supporting body-data estimates for clinician review" — matches article FAQ and about-me hard rules). Correct product (fitxpress), correct GLP-1 vertical, no invented customers.

### C. Brand & tone — 3/3
- No banned words. No em-dash in the post body (the only em-dash is line 10, the artifact template heading, not copy). No "not just X, it's Y". Voice reads as Vadim (operational, peer-to-peer).
- Watch-item (not scored down): line 22 "they capture in seconds, at home, with no visit" is a three-phrase parallelism. It reads as a natural enumeration rather than the banned rhetorical adjective-triple ("fast, reliable, scalable"), so treated as borderline, not a lapse.
- Note: `brand-assets/past-posts/` has no `linkedin-vadim` folder, so the Social-override 3-post style comparison could not be run.

### D. Format & structure — 3/3
- Frontmatter complete: `profile`, `platform`, `article_slug`, `product: fitxpress`, `status: draft`, `created`. Correct path. Template followed (Angle / Goal / CTA / Design tip with article-visual/format/adaptation/keep). Design tip correctly adapts the article's OG direction (publish-package §4) rather than inventing a new asset.

### E. Output quality — 4/4
- Hook lands in the first two lines before "see more": line 18 question + line 20 "It's the wrong question." Genuine angle (no single best tool; burden-vs-remote trade-off). Reads human, not AI. Publication-ready pending the one-word number fix (counted under B, not double-penalized here).

## Top 3 issues (приоритет для improver)

1. Line 26 "under a minute" must become "under 45 seconds" — editorial-guardrail #2 (one sourced number, consistent across content); current wording loosens and undersells the live-page figure.
2. Verify triple-phrase enumerations (line 22) stay natural and do not drift toward banned rhetorical triples in future drafts.
3. No `past-posts/linkedin-vadim/` corpus exists to style-check against — flag for Vadim to seed the folder so the Social-override C check can run.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
