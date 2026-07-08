---
qc_date: 2026-07-05
agent: post-drafter
artifact: workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/linkedin-vadim/post.md
track: social
artifact_type: post
total_score: 18/20
status: excellent
coordinator_review: pending
---

# QC Report — post-drafter — 2026-07-05

**Artifact:** `workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/linkedin-vadim/post.md`
**Total: 18/20** — ⭐ Excellent

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 5 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 4 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- CLAUDE.md, the `linkedin-vadim` profile block (`social-profiles-config.md`), and the correct source article version (`v3/publish-package.md`, the approved final, not `v1`/`v2`) were all read and correctly applied. `brand-assets/past-posts/linkedin-vadim/` does not exist at all (not just empty) — per the agent's own prompt ("If the folder is empty, continue without them, do not STOP") the agent correctly proceeded without it; not a fault.
- Minor superficiality: the `linkedin-vadim` profile's `tone` field explicitly calls for "**Data-backed**" content, but the post uses zero quantifiable proof points from the article (no coordinator-time, TAM, or operational-metric figures from the "Operational gains for obesity trial teams" section, lines 482-501 of the source). The chosen angle (writing-process/positioning meta-commentary) is a legitimate `post-drafter.md` content type ("Content experiment takeaways" / "Tactical observations"), and the "8 guardrails" count is itself a concrete detail, but the post could have anchored the GTM argument in one article stat without breaking the angle. This keeps it off a 5, not off a 4.

### B. Factual accuracy — 5/5
No issues. This is the standout category, especially set against the sibling `linkedin-katerina` v1 draft that failed QC (10/20) for introducing an unsourced external regulatory claim (MHRA/ICH-membership date) found nowhere in the article or `product-info/`.
- "8 compliance guardrails" (line 11) — verified exact match against `publish-package.md` frontmatter `compliance_guardrails: [not_diagnostic, no_dexa_alternative, no_endpoint_validation_claim, no_FDA_clearance_claim, no_GCP_compliance_claim_standalone, no_eligibility_determination, no_screen_failure_elimination, no_efficacy_proof_claim]` (8 items). The 4 explicitly named ("no DEXA-replacement claim, no endpoint-validation claim, no eligibility-determination claim, no efficacy-proof claim") map 1:1 to guardrails in that list; "four more just like them" correctly covers the remainder.
- "operational standardization and documentation layer for clinical trial workflows" (line 15) — near-verbatim from the article's own repeated framing (`publish-package.md` lines 415, 424, 458, 515, 568), and the FAQ does reinforce the "not a replacement" framing, so "repeated across every section and the FAQ" holds up.
- `"May help reduce avoidable screen failures"` (line 21) — verified as a **direct quote** from the article body (line 478: "...may help reduce avoidable screen failures by identifying participants who fall outside the protocol's measurement criteria before the site visit."). Not invented, not embellished.
- "accuracy alone won't stay a differentiator for long" (line 19) — matches CLAUDE.md §3 AI Risk positioning shift verbatim in spirit ("позиционирование смещается с «лучшая модель» на outcomes + workflow + governance + auditability").
- No client names, no product-performance numbers (accuracy %, pricing, scan counts) are used anywhere in the post, so there is no exposure to `proof-points.md` mismatches — a deliberate scope choice the manifest note confirms ("No product performance numbers... used, so no proof-points.md citation was needed").
- No external, unverifiable regulatory/legal claims of any kind — the exact failure mode flagged for the sibling `linkedin-katerina` draft is absent here.

### C. Brand & tone — 3/3
No issues. Zero banned words from `messaging.md` (leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/unlock/unleash/game-changing/cutting-edge). The only em-dashes in the file (line 13 `**Angle:**`, line 38 `**Article visual:**`) are plain descriptive separators in metadata fields, not rhetorical "X — is not just Y" constructions in body prose — body copy (lines 18-30) has none. No "it's not just X, it's Y" pattern. Tone matches the profile's "Practitioner... shares what works and what doesn't... peer-to-peer, not broadcast" spec (e.g., "My first instinct as a marketer was that this would flatten the copy... It went the other way." — short, honest, first-person). Style comparison against past posts (per Social-post override in the rubric) could not be performed — `linkedin-vadim` has no past-posts history to compare against; not counted against the score.

### D. Format & structure — 2/3
- Frontmatter complete (`profile`, `platform`, `article_slug`, `product`, `status`, `created`). File saved at the exact expected path.
- Char count slightly exceeded: body copy (from "Before we wrote..." through "...link in the comments.") is **1,528 characters**, against the `linkedin-vadim` profile's specified **1000-1500 char** range — about 28 characters (~2%) over. Within the platform-wide LinkedIn range (800-1800) from `post-drafter.md`, but not within the profile-specific spec. Per rubric: "char count чуть превышен" = 2/3.

### E. Output quality — 4/4
No issues. Ready to use as-is (the char overage is a 30-second trim, not a rework). The angle is genuinely distinctive — a meta-narrative about how compliance guardrails sharpened the copy rather than the more generic "here's what our new article says" recap the other 8 profile drafts for this article take. Reads as a practitioner's honest observation, not AI-generic: short declarative sentences ("It went the other way."), a real trade-off question to the audience instead of generic engagement bait, no filler intro.

## Top 3 issues (приоритет для improver)

1. Char count 1,528 vs the profile's 1000-1500 spec — trim ~30 characters before publish.
2. Profile tone spec calls for "data-backed," but the post uses no article statistic to anchor its GTM claim — not wrong, but a missed opportunity given the source article has strong operational-metric material available.
3. No `past-posts/linkedin-vadim/` reference material exists at all — flag to Vadim to seed this folder (per CLAUDE.md §7 STOP condition, this should ideally block personal-profile posts until seeded, but `post-drafter.md`'s own instruction explicitly permits continuing without it).

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
