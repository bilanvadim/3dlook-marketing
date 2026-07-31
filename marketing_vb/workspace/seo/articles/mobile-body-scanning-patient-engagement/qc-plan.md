---
qc_date: 2026-07-31
agent: seo-planner
artifact: workspace/seo/articles/mobile-body-scanning-patient-engagement/plan.md
track: seo
artifact_type: seo-outline
total_score: 16/20
status: good
coordinator_review: done
---

# QC Report — seo-planner — 2026-07-31

**Artifact:** `workspace/seo/articles/mobile-body-scanning-patient-engagement/plan.md`
**Total: 16/20** — good

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 2 | 5 |
| C | Brand & tone | 3 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 4 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- Phase 0 gate executed well: cannibalization check, vertical boundary, 4-direction links, CTA-by-intent, open items all present. Evidence about-me.md was read (repeatability `< 1 cm`, "two benchmarks" framing, reframe move, standard 12-part structure).
- Prompt Phase 2 asks for **5 H1 variants**; only the locked title is given (line 68). Justified by "locked by brief," but the step was skipped rather than shown-and-noted.
- content-plan.md row 76 action is a **dual option** "Net-new / major hub section." Planner silently collapsed it to `create-net-new` without surfacing the "major hub section" alternative to Vadim at a checkpoint gate.

### B. Factual accuracy — 2/5
- **Line 111 (H2.2 Approved claims):** "3D model (< 30 s)" — this timing is NOT in `proof-points.md`. proof-points documents only "Time from photo to results | Under 45 seconds" (line 40); no 30-second decomposition exists. Labeled as an "Approved claim," not merely a hypothesis. Hard rule (number absent from proof-points → B ≤ 2) applies.
- **Priority inconsistency:** frontmatter `priority: P0` (matches content-plan.md row 76) but Phase 0 prose line 30 states "planned **P1** supporting article … confirmed in published-articles-inventory.md, line 330." Sources genuinely disagree (content-plan = P0, inventory line 330 = P1). Not reconciled; the plan asserts both values.
- Correct product (`fitxpress`). All other numbers sourced: 96-97%, `< 1 cm`, 80+ measurements, 45 s total, body composition set (BMI/BMR/fat %/lean+fat mass), immediate/30-day deletion. Internal-figure claims are correctly hedged "Verify against Accuracy Framework before publish."

### C. Brand & tone — 3/3
- Plan's own prose is clean; no banned words used as claims. Strong style contract encoded for the writer (line 78): zero em-dash, banned-word list, M1/M2, no triple parallelism, `< 1 cm` convention, "supports clinician review" workhorse phrase.

### D. Format & structure — 3/3
- Frontmatter exceptionally complete: product, hub, cluster, intent, action_type, priority, existing_urls, cannibalization_guardrail, vertical_boundary, primary_keyword, secondary_keyword, title, meta_description, author (+ slug/status/created). Correct path. Follows template.
- Minor (not penalized): `meta_description` runs ~200 chars vs the 140-160 SEO limit, but meta finalization is a later step (seo-meta-generator), not this artifact type.

### E. Output quality — 4/4
- Checkpoint-1-ready. Angle is genuinely distinct; GLP-1 hand-off explicit (H2.9 sideways to visual-progress page); boundary owned in a dedicated H2.8 + early italic scope note (H2.2) + closing disclaimer (H2.12). FAQ locked (8 Qs). Internal-link map has direction + anchor + placement per link. A writer can execute with minimal ambiguity.

## Brief-specific checks (all requested items)

- **Strategy fit / cannibalization:** PASS. Stays broader than GLP-1; guardrail quoted verbatim (line 35); GLP-1-specific adherence explicitly handed to `visual-progress-tracking-glp1-adherence-retention/` as sideways link only (H2.9). No adherence-mechanics duplication.
- **Vertical boundary:** PASS. No diagnosis / treatment / eligibility / underwriting / replace-clinician / DEXA-BIA-replacement / compliance-guarantee / auto-fraud claims baked in. "Not positioned as a medical device"; compliance framed on data-privacy frameworks, not device frameworks (H2.7, H2.8).
- **Title exactness:** PASS. "How Mobile Body Scanning Improves Patient Engagement" — exact, primary keyword in first six words.
- **Internal links (4 directions, no invented URL):** PASS. Up / sideways / down / trust all covered. Every URL verified real against published-articles-inventory.md. Correctly refuses to invent a Privacy FAQ URL (lines 45, 180) and routes the privacy note to `/legal/` instead.
- **FAQ + AEO:** PASS. 8 Q&A pairs locked (H2.11), AEO direct-answer in H2.2 first screen, plain declarative H2s.
- **Frontmatter completeness:** PASS on field presence; flagged for the internal P0/P1 value conflict (see B).

## Top 3 issues (приоритет для improver)

1. Unsourced number "< 30 s" for the 3D model (line 111), presented as an approved claim — not in proof-points.md (only "under 45 seconds" total exists). Remove or replace with the sourced 45 s figure before Checkpoint 1.
2. Priority conflict: frontmatter P0 vs Phase 0 prose "P1" (content-plan.md and inventory disagree). Reconcile to one value and flag the source discrepancy to Vadim.
3. Surface the two suppressed decision points to Vadim at Checkpoint 1: the content-plan's dual "Net-new / major hub section" action, and the absence of the required 5 title variants.

## Coordinator review

agreement: ✅ agree
top_issue: Unsourced "<30s" 3D-model claim must be cut/replaced with the sourced 45s figure, and the P0/P1 priority conflict needs Vadim's call before Checkpoint 1 — both are cheap fixes but factual, not stylistic.
