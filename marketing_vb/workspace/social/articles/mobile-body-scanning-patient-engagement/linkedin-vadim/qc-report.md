---
qc_date: 2026-08-17
agent: post-drafter
artifact: workspace/social/articles/mobile-body-scanning-patient-engagement/linkedin-vadim/post.md
track: social
artifact_type: post
total_score: 19/20
status: excellent
coordinator_review: pending
---

# QC Report — post-drafter — 2026-08-17

**Artifact:** `workspace/social/articles/mobile-body-scanning-patient-engagement/linkedin-vadim/post.md`
**Total: 19/20** — excellent

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 5 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 4 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- Line 21 frontmatter `**Claims used:** C8, C12, C13, C10` references a claim-ID scheme that does not exist anywhere in the source. The article's `claims_used` are `FX-*` codes (draft-v5-revision1.md lines 35-45), and no `C`-numbered claims registry exists in `brand-assets/`. The labels are unmappable/unverifiable. No impact on the post body (which carries no numeric claims), so it is a traceability annotation slip, not a factual one.
- brief compliance otherwise complete: AU-operator lens (line 28), operations/privacy/scalability/implementation focus (lines 30-40), no US/EU/UK regulatory framing, closes with a discussion question (line 42), 235 words inside the 180-250 band.
- OG-image handling acceptable: the source draft has no Open Graph / section-4 block, and the design tip openly states this (line 52) and derives a direction rather than fabricating a quote. Honest handling of a missing input.

### B. Factual accuracy — 5/5
- Post contains zero numeric claims — no accuracy %, no `< 1 cm`, no 80+ / 45 sec — so there is nothing to hallucinate. Every operational statement traces to the article: capture protocol > model (line 30 ↔ article line 30 framing), cadence noise-vs-friction (line 36 ↔ article line 196), "engagement signals not clinical outcome measures" (line 38 ↔ article lines 200/172), API/SDK capture-and-structuring layer with the care team keeping the decision (line 40 ↔ article lines 198/210).
- On-strategy: leads with "what decides whether it holds up is not the model. It is the capture protocol" — workflow/governance framing, no anti-positioning ("most accurate") violation. Product correctly FitXpress / telehealth. No invented customers.

### C. Brand & tone — 3/3
- No banned words (checked: leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/unlock — none present).
- No em-dash rhetorical constructions, no "not just X, it's Y". Colons/periods used instead.
- Two three-item enumerations ("stands in poor light, wears a loose sweater, or holds the phone at the wrong angle", line 32; "scan completion rate, repeat check-in rate, or progress-visualization views", line 38) are descriptive/enumerative lists, not rhetorical adjective triples, and are lifted from the source article which cleared brand-check. Not a §6 violation.
- Voice matches Vadim's operator register; 0 emoji (within the 1-2 ceiling), 0 hashtags.

### D. Format & structure — 3/3
- Frontmatter complete: `product: fitxpress`, `status: draft`, `created`, plus profile/platform/market/vertical/format. Path correct.
- Design tip carries all four fields (Article visual / Format / Adaptation / Keep) and uses correct DESIGN.md tokens — navy `#050F40`, electric blue `#143DFF`, Satoshi (line 55) — not the stale `#2962FF`/Inter.

### E. Output quality — 4/4
- Hook lands in the first two lines, visible before "see more" (line 28): "a progress feature is easy to demo and hard to keep honest at scale."
- Genuine practitioner voice, distinct angle (capture protocol / cadence / measurement), not a summary of the article. Publishable essentially as-is.

## Top 3 issues (приоритет для improver)

1. `Claims used: C8, C12, C13, C10` cites a non-existent claim-ID scheme (article uses `FX-*`, no `C`-registry exists) — traceability metadata is wrong/unverifiable.
2. Source draft lacked an OG/section-4 block, so the design tip is derived rather than adapted from an approved article visual — coherence with the eventual blog banner is unverified.
3. No other blocking issues; borderline enumerative triples are inherited from the cleared source and do not require a fix.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
