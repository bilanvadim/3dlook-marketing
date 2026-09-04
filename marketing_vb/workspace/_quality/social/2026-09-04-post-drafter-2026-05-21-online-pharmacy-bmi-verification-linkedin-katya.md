---
qc_date: 2026-09-04
agent: post-drafter
artifact: workspace/social/articles/2026-05-21-online-pharmacy-bmi-verification/linkedin-katya/post.md
track: social
artifact_type: post
total_score: 19/20
status: excellent
lint: pass
coordinator_review: |
  agreement: ✅ agree
  top_issue: paragraph-rhythm uniformity (two near-identical "It ___." sentences back to back) is the one real miss; everything else clears cleanly
---

# QC Report — post-drafter — linkedin-katya — 2026-09-04

**Total: 19/20** — excellent

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 5 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 2 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 4 | 4 | judged |

## Findings

### A. Adherence — 5/5
- Location discipline held exactly: the post never names Israel, the Gulf, or a region. Personal rule 3 ("do not announce your location") is fully respected, and `lint` confirms 0 geo mentions.
- Stays inside the brief's "avoid" list: no EU regulatory specifics (the article's GPhC guidance is dropped entirely), no US payer context, no fashion/apparel drift.
- Focus matches the katya brief's list almost word for word — "enterprise buying behaviour" and "trust" — via the procurement-question frame: *"When a buyer evaluates a verification vendor, I'd start with one question."*
- Hook satisfies personal rule 5 (claim, ~10 words, arguable): *"A verification tool that accepts camera-roll uploads isn't verifying much."* — 11 words, a position, not a teaser.
- Teaches exactly one usable thing per personal rule 4: the single vendor question ("in-session capture, or camera-roll upload?"), not a listicle of the article's five capabilities.
- Closes on a discussion question that needs the reader's own judgment, before the soft article invite, per the katya brief's explicit structure requirement.
- I checked the CEO anecdote against the article (`published-live-2026-08-24.md` lines 65-69) rather than trusting the lint pass alone, since this is the one place a subject/number could have drifted: "27 kg heavier," "both took seconds," and "kept her real face and widened the body" all match the source's ChatGPT/Gemini experiment with no quantifier loss and no subject swap. No B deduction beyond what lint already cleared.

### C. Brand & tone — 2/3
- `lint` flags two `ai-tells:house_rule` warnings the drafter should self-correct against: sentence-length variation at 0.35 (rubric wants >0.35) and "uniform paragraph length: every block the same size." This is the mechanical signature personal rule 2 explicitly names — *"nine sentences of the same length is a machine"* — and it's borderline-tripped here, not comfortably cleared.
- Concrete instance of the pattern: *"It's a cheap question to ask early. It can save a pilot that was never going to hold up."* — two adjacent sentences, same "It ___." opener, similar length, sitting right after a paragraph of two similarly-shaped sentences. The post reads clean and personal on a first pass, but the block-by-block cadence is more uniform than the brief's own rhythm instruction asks for.
- No banned words, no em-dash rhetoric, no triple parallelism, first-person voice throughout ("I'd start," "the kind of image that could sit"). Everything else in the C checklist is clean — the deduction is specifically the rhythm/paragraph-uniformity flag, not a tone or word-choice violation.

### E. Output quality — 4/4
- **Position:** the post judges, it doesn't just report. *"A verification tool that accepts camera-roll uploads isn't verifying much"* and *"If the camera roll is open, the rest of the demo matters less"* are both stance statements a reader could push back on — exactly the bar the brief and rubric set. This isn't a compiled recap of the article's capability list.
- **Angle distinctness:** `sibling_angles` is empty ("none yet") — this is the first profile drafted in the pack, so there is nothing yet to compare against. Flagging for the coordinator: confirm at digest time that later profiles in this pack (especially any other trust/vendor-evaluation angle) don't converge on the same "one procurement question" framing this post has now claimed.

## Top issue for `post-drafter`

When a personal-profile post opens with a short one-line hook, don't default to near-uniform two-sentence paragraphs for the rest of the post — deliberately drop in one genuinely short beat (three to five words) and one longer one mid-post so the block-by-block rhythm doesn't trip the ai-tells monotone/uniform-paragraph check the way this draft did (variation 0.35 against a >0.35 want).
