---
qc_date: 2026-07-31
agent: seo-writer
artifact: workspace/seo/articles/mobile-body-scanning-patient-engagement/draft-v1-writer.md
track: seo
artifact_type: seo-final
total_score: 14/20
status: marginal
coordinator_review: done
---

## Coordinator review

agreement: ✅ agree
top_issue: SOC 2 overclaim is real and correctly load-bearing (compliance.md explicitly bans it pending Vadim's confirmation) — fixed directly in draft-v3-edited.md (3 instances removed, replaced with substantiated HIPAA/GDPR claims) plus the related "faces obfuscated at capture" → "blurred at storage" correction; also flagging plan.md's H2.7 approved-claims list (line 185) for correction so SOC 2 is not re-inherited on any future regeneration of this article.

# QC Report — seo-writer — 2026-07-31

**Artifact:** `workspace/seo/articles/mobile-body-scanning-patient-engagement/draft-v1-writer.md`
**Total: 14/20** — marginal

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 1 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- Plan executed comprehensively: all 12 sections in order, 8 FAQs locked, early italic scope note (line 31), full boundary section (H2.8), closing disclaimer (line 170), 4-direction internal links, external stats fetched + cited with named source and link. Evidence about-me.md/guardrails read: repeatability written `< 1 cm`, accuracy figure deliberately kept out of the headline and routed to the Accuracy Framework, "supports clinician review" / "structured body-data capture layer" workhorse phrases used.
- **Correctly avoided the plan's unsourced "<30 s" 3D-model timing** (the plan QC top issue) — the draft states only "under 45 seconds" and does not decompose it.
- Gap: the plan's own style contract mandates guardrail #1 (substantiation — cut what you can't back) and "internal 3DLOOK figures use the documented set only" (plan line 83). The writer's notes claim a guardrails spot-check was run, but the SOC 2 claim (see B) was neither verified against the claim source nor surfaced in Open Items, despite the writer flagging lesser items (link count, accuracy-figure choice). One mandated check done superficially.

### B. Factual accuracy — 1/5
- **Lines 92, 106, 151: FitXpress "meets System and Organization Controls 2 (SOC 2) where applicable."** This is contradicted by the source of truth: `brand-assets/product-info/compliance.md` line 48 — *"We are NOT SOC 2 certified yet (in progress — confirm with Vadim before claiming)."* SOC 2 is also absent from `proof-points.md` and CLAUDE.md §12. Asserting a certification the company does not hold, three times, in an article explicitly written for a "compliance buyer" (line 92), is a significant trust-affecting error. The "where applicable" hedge does not rescue it — it still asserts the attestation exists.
- Line 92: "faces are obfuscated **at capture**" vs `proof-points.md` line 126 "Photo blur **on storage** — auto-applied when stored." Capture-vs-storage timing mismatch (minor).
- All other internal figures are correct and sourced: 80+ measurements, under 45 s, `< 1 cm` repeatability, body composition set (BMI/BMR/body fat %/lean+fat mass), immediate/30-day deletion, TLS in transit, AWS at rest, no personal identifiers. Correct product (`fitxpress`).
- External stats (7%→12% telehealth utilization; 64.8% GLP-1 discontinuation) are named + linked and consistent with the sibling GLP-1 page (guardrail #2). Not 3DLOOK figures, so proof-points does not govern them. Source substitution (MEPS/*Healthcare* study for CDC after 403s) is documented transparently per guardrail #11.

### C. Brand & tone — 3/3
- Article body (lines 11–170) is clean: zero em dashes, zero banned/hype words, no `Furthermore/Moreover/Additionally` sentence-starters, no `objective`/`reader`/`audience`/`this article`/`this guide`/`by hand`, no `plus` as a connector (only the compound "80-plus", acceptable). Em dashes and the banned-word list that appear on lines 179–202 are inside the "Writer notes" block, outside the article body.
- No triple parallelism: three- and four-item lists are grouped clauses, not adjective-triples (e.g. line 166 is four items). Measured, hedged, stats-first 2026 Assel voice throughout. `you` confined to the H2.12 conversion close; `we/our` only in the FitXpress product statement.

### D. Format & structure — 3/3
- Frontmatter complete: `product: fitxpress`, `author: Assel Sekerova`, `status`, `word_count`, `claims_used`. Correct path. Word count 2,814 within the 2,200–3,000 target. All 12 sections present and ordered; FAQ block; writer notes correctly separated from body per guardrail #11.

### E. Output quality — 3/4
- Genuinely distinct angle; cannibalization guardrail respected (GLP-1 handed off to the visual-progress page as a sideways link, kept as one of four verticals — H2.9). Boundary owned in a dedicated H2.8. Reads human, not AI.
- Not publishable as-is: the false SOC 2 claim must be removed in three places and confirmed with Vadim before ship — a substantive factual correction, not a stylistic pass. Secondary: 10 internal-link targets vs the style-guide 6–9 soft cap (writer already flagged this for the editor with a drop candidate).

## Top 3 issues (приоритет для improver)

1. **False SOC 2 certification claim (lines 92, 106, 151).** `compliance.md` line 48 says 3DLOOK is NOT SOC 2 certified yet — remove the SOC 2 mention in all three places (or confirm status with Vadim before any claim). Also fix the plan's approved-claims list (plan line 185) that introduced it, so it is not re-inherited.
2. **Blur timing mismatch (line 92):** "faces obfuscated at capture" contradicts proof-points "blur on storage / auto-applied when stored" — align to the documented wording.
3. **Trim internal links 10 → 6–9** (writer's flagged drop candidate: the second `mobile-body-scanning-accuracy` or second `/legal/` instance).

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
