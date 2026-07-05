---
qc_date: 2026-07-05
agent: post-drafter
artifact: workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/instagram-company/post.md
track: social
artifact_type: post
total_score: 19/20
status: excellent
coordinator_review: pending
---

# QC Report — post-drafter — 2026-07-05

**Artifact:** `workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/instagram-company/post.md`
**Total: 19/20** — Excellent

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 5 | 5 |
| B | Factual accuracy | 5 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 5/5
No issues. `product: fitxpress` correctly carried from `publish-package.md` frontmatter. `article_slug` field uses the publish-package's `article_slug` (`clinical-trial-anthropometric-measurement-software-obesity-trials`) verbatim, matching the template spec. `brand-assets/past-posts/instagram-company/` is empty (0 files); per the prompt's explicit fallback ("If the folder is empty, continue without them, do not STOP") this is correctly not treated as a blocker. Section 4 OG image direction was read and quoted accurately in the design tip (multi-site dot motif, guided-scan phone, structured-record/timestamp icon, dark teal-blue palette, ban on patient face/DEXA imagery all carried over). The angle ("fewer measurement-only visits" as a human-burden story) is a real, correctly-attributed thesis from the source article, not a reinvented one.

### B. Factual accuracy — 5/5
No issues. "Two smartphone photos... 80+ measurements and body composition estimates in about 45 seconds" matches both `proof-points.md` (2 photos, 80+ measurements, under 45 seconds) and the article body verbatim ("80+ body measurements, BMI outputs, and body composition estimates, with results processed in roughly 45 seconds," draft-final.md line 94). "Check-ins that can stretch on for a year or more" reflects the article's "study window can run twelve months or longer" (line 83). No invented clients, no comparison claims. The line "FitXpress supports the measurement step. It doesn't replace the methods or decisions a trial's protocol calls for" correctly honors the article's `compliance_guardrails` (no_dexa_alternative, no_endpoint_validation_claim) despite `compliance_sensitive: true` on the source article — this is a compliance-aware paraphrase, not a hallucinated hedge.

### C. Brand & tone — 3/3
No issues. No banned words (leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/unlock/unleash/game-changing/cutting-edge). No em-dash or "not just X, it's Y" construction in the post copy itself (the only em-dash in the file is in the internal `**Angle:**` metadata line, which is not published caption text). No triple parallelism. No clickbait, no unsubstantiated buzzwords — consistent with CLAUDE.md §6.

### D. Format & structure — 3/3
No issues. Frontmatter complete (`profile`, `platform`, `article_slug`, `product`, `status`, `created`). File saved at the exact expected path. Caption is 975 characters — within the profile's 600-1000 char spec. First line/hook is 74 characters, under the 125-char pre-"more" cutoff. Design tip has all 4 required fields (Article visual / Format / Adaptation / Keep) and the carousel format choice fits the "3+ point sequence" use case from the format table.

### E. Output quality — 3/4
- The `instagram-company` profile spec calls for "Visual storytelling... Less corporate, more brand" and content types like "Human outcome from the article" / "Product in action." The actual copy reads closer to a condensed B2B/clinical-ops excerpt than a human-centered IG moment — there's no single vivid scene or specific person in it (e.g., "the participant"), and the compliance-hedge sentence ("FitXpress supports the measurement step. It doesn't replace the methods or decisions a trial's protocol calls for") lands as boilerplate rather than brand voice. This is defensible given the compliance-sensitive topic, but a 5-10 minute pass to make the opening/closing feel less like a policy statement and more like a scene would strengthen it for this specific platform.
- Otherwise strong: single clear angle (participant burden, not a summary of the whole article), a working hook, and a design tip that turns the OG composition into a genuinely IG-native 3-slide carousel rather than reusing the OG crop as-is.

## Top 3 issues (приоритет для improver)

1. Minor: tone leans more institutional/compliance-boilerplate than the profile's "less corporate, more brand" instruction calls for — a light copyedit, not a rewrite.
2. None (Adherence, Factual accuracy, Brand/tone, Format all clean).
3. None.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
