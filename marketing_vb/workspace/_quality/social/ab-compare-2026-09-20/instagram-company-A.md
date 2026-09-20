---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/bariatric-hub-refresh/instagram-company/post.md
track: social
artifact_type: post
total_score: 18/20
status: excellent
lint: pass
coordinator_review: |
  agreement:
  top_issue:
---

# QC Report — post-drafter — instagram-company — 2026-09-20

**Total: 18/20** — excellent

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 4 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 3 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 3 | 4 | judged |

## Findings

### A. Adherence — 4/5
- Hook rule met: "Two photos on a phone, before the appointment even starts." is visual, human, and lands before the "see more" cutoff, matching `length: "... Hook in first line (показується до «ще»)."`.
- `product_bias: fitxpress 100%` honored, length lands at 918/600-1000 chars (per `post_meta`), hashtags = 0 (per lint), CTA channel matches (`«Link in bio»`).
- One real lapse: three consecutive sentences — "FitXpress supplies the inputs, not the decisions. Clinical eligibility stays with the care team, and each payer decides what documentation it accepts. FitXpress is not a medical device." — read as enterprise compliance copy stacked together. The content itself is correct and necessary (matches CLAUDE.md §12 verbatim on the medical-device line), but the brief's tone line is explicit: `tone: "... Less corporate, more brand."` and `avoid: "Занадто технічні деталі, ... jargon."` Three hedge sentences in a row, in the middle of an otherwise warm five-paragraph post, is the one place the post reads like it forgot which feed it's for.
- Secondary, minor: the CTA phrasing "Link in bio for the full intake workflow" is workflow-toned rather than tied to the visual hook the post opens with ("two photos"); not wrong, just generic against a brief that wants "brand" over "workflow."

### C. Brand & tone — 3/3
- No banned-words-list hits (leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/unlock/unleash/game-changing/cutting-edge) — none present.
- No em dash, no "not just X, it's Y", no triple-parallelism construction.
- Medical-device line uses the exact canonical form, "FitXpress is not a medical device." — matches CLAUDE.md §6/§12 fourth-state wording precisely, not a paraphrase.
- The two-beat fragments ("No specialized hardware. No measurement-only visit." / "Fewer minutes on the tape measure. More on the patient.") are intentional punchy copy appropriate to an Instagram caption, not a generic AI tic from the catalog (no triple list, no "it's not just... it's").

### E. Output quality — 3/4
- **Position:** the post explicitly argues a stance rather than just reporting facts — "So what does that free? The consultation itself." and the close, "Fewer minutes on the tape measure. More on the patient. That is the shift worth piloting." This is a judgment (reallocate clinical time toward the patient), not a recap of the article's use-case table.
- **Angle distinctness:** per the post's own `**Angle:**` line, it's framed as "The human moment before the appointment... distinct from Twitter's GLP-1 documentation angle." This scoped input didn't carry a `sibling_angles` list for the rest of the pack, so distinctness beyond that single stated comparison couldn't be cross-checked here.
- Held to 3 rather than 4 for the same reason as the A finding: the compliance paragraph needs roughly five minutes of smoothing to sit inside the human narrative instead of reading as an inserted disclaimer, and the CTA is a touch generic. Everything else — hook, structure, closing stance, zero AI-tell density (lint: `ai_density_per_1000_words: 0.0`) — is publish-ready.

## Top issue for `post-drafter`

When a bariatric/clinical post needs the medical-device and payer-decision disclaimers, thread them one at a time into the surrounding human sentences instead of stacking three hedge sentences back to back — `instagram-company`'s brief explicitly calls for "less corporate, more brand," and that's the one paragraph in this post that reads like it was written for LinkedIn.
