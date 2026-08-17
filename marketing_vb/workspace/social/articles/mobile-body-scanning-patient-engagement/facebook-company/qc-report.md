---
qc_date: 2026-08-17
agent: post-drafter
artifact: workspace/social/articles/mobile-body-scanning-patient-engagement/facebook-company/post.md
track: social
artifact_type: post
total_score: 18/20
status: excellent
coordinator_review: pending
---

# QC Report — post-drafter — 2026-08-17

**Artifact:** `workspace/social/articles/mobile-body-scanning-patient-engagement/facebook-company/post.md`
**Total: 18/20** — excellent

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
- Facebook platform rules followed correctly: first paragraph carries full meaning (lines 27-29), accessible walkthrough + audience question (line 37), length inside 800-1200 band.
- Claims C7/C8/C11 used exactly as assigned in `posting-plan.md` line 50; angle matches the plan verbatim.
- **Manifest not updated.** `manifest.json` lists only `twitter-company`; the facebook draft did not add itself. post-drafter hard rule ("After saving — update the manifest") not completed for this run.
- Could not compare to `past-posts/facebook-company/` (per-track override C) — folder does not exist. Context gap, not an agent failure; noted only.

### B. Factual accuracy — 5/5
- Every fact traces to the source article: loop steps (line 31 = draft §How the scan-to-scan experience works), "in about a minute" matches draft line 161, boundaries (line 35 = C11 / draft lines 214-215).
- No invented numbers, no named customers, correct product (`fitxpress`). No retired claims: no "under 45 seconds," no reinstated GLP-1 discontinuation stat.
- No anti-positioning violation; no "most accurate" lead.

### C. Brand & tone — 3/3
- No banned words. No em-dash rhetoric. No "not just X, it's Y." No clichéd opener (the question "How often should a patient scan?" is topic-specific, not a banned "Have you ever wondered").
- Company voice (3rd person) held throughout; boundaries stated cleanly (line 35). Zero emoji, zero hashtags — compliant.

### D. Format & structure — 2/3
- Frontmatter complete, includes `product: fitxpress`; path correct; length 1,196 within band; design tip uses correct DESIGN tokens (navy `#050F40`, electric blue `#143DFF`, Satoshi — not the stale `#2962FF`/Inter).
- **Goal enum mismatch:** line 24 `**Goal:** discussion` — not one of the template's allowed values (conversion | awareness | engagement | thought leadership). Structure not fully per template.

### E. Output quality — 4/4
- Publishable as-is. Cadence-question opener is a genuinely strong Facebook hook and a real discussion driver, distinct from the other 8 profiles.
- Minor: a few sentences (e.g., "Because capture is guided and repeatable, each pass produces data that lines up with the last") are near-verbatim from the draft. Acceptable for an "accessible walkthrough" angle but the ceiling on originality.

## Top 3 issues (приоритет для improver)

1. `manifest.json` not updated with the facebook draft — breaks the Telegram review hand-off signal.
2. Goal field uses out-of-enum value "discussion" (should be "engagement").
3. Light verbatim reuse of article sentences — tolerable here, watch across the pack.

## Coordinator review

(заполняется Claude в чате после автозапуска QC)
