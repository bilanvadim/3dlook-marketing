---
qc_date: 2026-07-05
agent: post-drafter
artifact: workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/linkedin-olena/post.md
track: social
artifact_type: post
total_score: 19/20
status: excellent
coordinator_review: pending
---

# QC Report — post-drafter — 2026-07-05

**Artifact:** `workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/linkedin-olena/post.md`
**Total: 19/20** — ⭐ Excellent

## Special focus: unsourced-claim check (per sibling failure precedent)

`linkedin-katerina` v1 for this same article failed QC (10/20) for asserting a specific, dated, unsourced regulatory claim (MHRA ICH-membership date) absent from the source article and `product-info/`. This draft was checked line-by-line against that exact failure mode:

- **Line 18:** "A trial running across several European countries carries more variability than a single-site study." This is a generalization drawn from the article's own multi-site variability thesis ("the manual measurement workflow varies by site, staff member, tool used..."), extended to a cross-border framing and voiced as Olena's personal observation ("I keep noticing the same pattern in conversations with European sponsors and CROs"), not asserted as an external statistic, named study, or regulator finding. No date, institution, or market figure attached — consistent with the corrected pattern in `linkedin-katya` and `linkedin-nick` (both scored 5/5 on this category with similar hedged framing).
- **Line 20 (GDPR paragraph):** "FitXpress follows GDPR principles, deletes photos immediately or within 30 days per client policy, and does not process personal identifiers." This is a near-verbatim match to `brand-assets/product-info/proof-points.md` → Compliance & security table ("Follows GDPR principles" / "Immediate delete OR within 30 days per client policy" / "Personal identifier processing: None"). No invented regulation name, no invented date, no fabricated certification — the exact category of claim that sank `linkedin-katerina` v1 is absent here.
- **No CE marking claim** is made despite the profile's tone line mentioning "CE marking awareness" — correctly omitted rather than invented, since no CE-marking fact exists in `product-info/` for FitXpress in a clinical-trial context.
- **No named EU CRO** (e.g., ICON, PSI CRO, SGS, Eurofins from `icp-detail.md`) is used, avoiding an implied, unsourced customer/prospect relationship.
- **Conclusion:** the sibling failure mode does not recur. Every checkable claim traces to the source article or `proof-points.md`, or is explicitly framed as personal opinion.

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
No issues. `CLAUDE.md` tone/no-go read and applied. Profile block (`linkedin-olena`, `social-profiles-config.md` lines 194-217) correctly honored: `product_bias: 100% fitxpress`, tone ("BD professional... EU market nuance (GDPR)... First person" — post opens "I keep noticing..."), `content_types` ("European market angle... GDPR" and "Observation from EU market conversations" both directly used), length 800-1400 chars, CTA pattern ("Open to connect" + article-in-comments, line 26, matches the config's `cta` field verbatim). `avoid` list respected: no US-specific regulatory context (no FDA mention, unlike the source article which cites it), no Israeli-market content. `brand-assets/past-posts/linkedin-olena/` is empty — correctly handled per the prompt's edge case ("if empty, continue without them, do not STOP") and documented in `manifest.json`. Article (`publish-package.md` v3) read for claims and Section 4 OG image brief, correctly adapted rather than reinvented.

### B. Factual accuracy — 5/5
No issues. See special-focus section above. No invented numbers, no invented case studies or client names, no unsourced regulatory dates/institutions. Compliance guardrails from the source article respected ("None of this replaces the reference methods a protocol already defines" correctly restates `no_dexa_alternative` / `no_endpoint_validation_claim` from Section 11 of `publish-package.md`).

### C. Brand & tone — 3/3
No issues. No banned words from `messaging.md` (leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/unlock/unleash/game-changing/cutting-edge — none present). No em-dash used in a rhetorical "X — it's not just Y" construction anywhere in the post body (the three em-dashes in the file are all in metadata fields — Angle, CTA, Article visual — not in the published copy). No triple-parallelism pattern, no "It's not just X, it's Y" construction, no listed no-go clichés. Style-consistency check against `past-posts/linkedin-olena/` (per rubric's Social-post override) could not be performed — folder is empty; no penalty applied, documented as N/A.

### D. Format & structure — 3/3
No issues. Frontmatter complete (`profile`, `platform`, `article_slug`, `product`, `status`, `created`). File saved at the exact expected path (`workspace/social/articles/{slug}/linkedin-olena/post.md`). Template fully followed (Angle / Goal / body / CTA / Design tip with all 4 required fields: Article visual, Format, Adaptation, Keep). Body copy measures 1,334 characters — within the profile's 800-1400 char range. `hashtags: none` respected (zero hashtags used). Design tip accurately quotes the Section 4 OG image brief (multi-site dot-map motif, guided two-photo capture icon, timestamp/structured-record icon, dark teal-blue palette) and the `carousel` format choice fits the table's stated use case ("problem → solution → result" sequence), with a coherent 3-slide adaptation plan.

### E. Output quality — 3/4
- Opening line is a specific, credible hook ("the protocol reads identical on paper at every site, and the execution doesn't") that lands before LinkedIn's "see more" cutoff and sets a distinct angle (cross-border amplification + GDPR) rather than restating the article's US/FDA framing.
- Closing sentence is slightly convoluted: "It's the operational layer underneath: the part deciding whether data from a multi-country trial is actually comparable a year in." The idea is sound (echoes the article's audit-readiness thesis) but the phrasing is dense enough to require a light edit for a natural BD voice.
- Net: publish-ready with a light polish pass on the closing line rather than a substantive rewrite.

## Top 3 issues (приоритет для improver)

1. Closing sentence reads dense/abstract ("the part deciding whether data... is actually comparable a year in") — needs a light rewrite for natural spoken BD voice. Minor, does not block approval.
2. Style-consistency check against past posts could not be performed (`past-posts/linkedin-olena/` empty) — flag for Vadim to backfill 10 exports so future QC runs can score C fully.
3. No CE-marking angle used despite it being named in the profile's tone description — correctly avoided (no sourced CE-marking fact exists for this context), but worth flagging to Vadim in case he wants that fact added to `product-info/` for future EU-angle posts.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
