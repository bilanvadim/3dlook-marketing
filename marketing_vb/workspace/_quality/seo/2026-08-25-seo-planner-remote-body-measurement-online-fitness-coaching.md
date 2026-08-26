---
qc_date: 2026-08-25
agent: seo-planner
artifact: workspace/seo/articles/remote-body-measurement-online-fitness-coaching/plan.md
track: seo
artifact_type: seo-outline
total_score: 19/20
status: excellent
coordinator_review: done
---

# QC Report — seo-planner — 2026-08-25

**Artifact:** `workspace/seo/articles/remote-body-measurement-online-fitness-coaching/plan.md`
**Total: 19/20** — excellent

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 5 | 5 |
| B | Factual accuracy | 5 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 4 | 4 |

## What was wrong (specific)

### A. Adherence — 5/5
- Phase 0 gate executed and documented (Hub 1 → Digital coaching, create-net-new, P1); action_type carried into frontmatter and header.
- All seo-planner requirements present: keyword clustering (primary + 5 secondary), 5 title variants with a reasoned pick, 12-part outline with per-H2 goal / word target / must-cover / keywords / sources / approved-claim IDs / boundary, mandatory FAQ (7 Qs), 4-direction internal links, CTA-by-intent.
- Correctly did NOT invent SEO volumes when no Ahrefs export was supplied — marked TBD and flagged as an open item. Right call over fabrication.

### B. Factual accuracy — 5/5
- Every product figure maps to a proof-point ID (FX-001…FX-008); no number appears that is not in `proof-points.md`.
- Accuracy is scoped, never reduced to one universal figure; repeatability written as `< 1 cm`; the two benchmarks are kept separate.
- No fabricated customer — the plan explicitly refuses to borrow Yazen/UK Meds (weight-loss/pharmacy, would breach the GLP-1/vertical boundary) and flags the absence of a fitness-coaching reference to Vadim.

### C. Brand & tone — 2/3
- The plan prose itself contains em dashes (e.g., header line "create-net-new — cleared by…", and several H2 "Goal:" lines). `terminology-guardrails.md` bans the em dash "always, without exceptions" across all corporate content. This is an internal brief, not shipped copy, so impact is low — but it must not migrate into the article, and the writer/editor own the full pass. No banned words; no other AI signatures.

### D. Format & structure — 3/3
- Frontmatter complete (`slug`, `product`, `primary_keyword`, `hub`, `cluster`, `intent`, `action_type`, `priority`, `author`, `status`, `created`); file in the correct `workspace/seo/articles/{slug}/` path; matches the seo-planner `plan.md` template.

### E. Output quality — 4/4
- Writer-ready: narrow owned intent is unambiguous, each section carries its boundary, approved claims are pre-assigned, and the four open items are surfaced rather than silently resolved. A section-writer could start without clarifying questions on scope.

## Top 3 issues (priority for improver)

1. Em dashes present in the planning prose — trivial here, but the em-dash ban is absolute; ensure it does not carry into H2.x drafting (already load-bearing at editor Pass 4 / detect-ai-tells).
2. Keyword volumes are TBD — the plan depends on an Ahrefs pull that was never provided; the primary keyword should be reconciled before writing.
3. No fitness-coaching named customer — a real limitation of the proof-point corpus, not a planner error; needs a Vadim decision (accept capability framing vs supply a reference).

## Coordinator review

agreement: ✅ agree — 19/20 is fair; the plan is tight, on-strategy, and honest about its two real gaps (keyword data, missing customer).
top_issue: The two dependencies are external, not planner defects — get the Ahrefs pull and a customer-framing decision from Vadim at this checkpoint so the writer stage is not blocked later.
