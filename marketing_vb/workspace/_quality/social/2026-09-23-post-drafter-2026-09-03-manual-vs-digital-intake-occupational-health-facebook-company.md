---
qc_date: 2026-09-23
agent: post-drafter
artifact: workspace/social/articles/2026-09-03-manual-vs-digital-intake-occupational-health/facebook-company/post.md
track: social
artifact_type: post
total_score: 17/20
status: good
lint: pass
coordinator_review: |
  agreement: ✅ agree
  top_issue: Triple "when X, when Y, or when Z" structure repeats three times in one post — the A/B batch's known weak spot on soft-register company accounts reading too technical shows up here as templated rhythm rather than jargon per se.
---

# QC Report — post-drafter — facebook-company — 2026-09-23

**Total: 17/20** — good

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 4 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 2 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 3 | 4 | judged |

## Findings

### A. Adherence — 4/5
- Content type match, length (1050/800-1200 chars), no hashtags, CTA "Read the full article" all correct per `profile_brief`.
- Brief explicitly says facebook is "broader audience than LinkedIn — explain without jargon. Slightly warmer." The post keeps fairly operational vocabulary that reads more like the source article's own register than a simplified consumer explanation: "fixed appointment slots," "rescreens keep tracing back to missing intake data," "equipment-based testing kept on-site." None of these is wrong, but none is de-jargoned for a general Facebook reader either — a LinkedIn version could use nearly the same sentences. This is the one brief instruction not clearly executed, hence 4 not 5.
- Checked the manual-fits / digital-fits / hybrid conditions against the article's decision framework (lines 91-111): all three condition sets are faithful paraphrases, no case swap, no quantifier dropped. One embellishment worth flagging for the writer, not for the score: "manual fallback defined for anyone who cannot complete a scan" narrows the article's "fallback and transfer path... for each remote step" (line 111) to a specific failure scenario the article doesn't state. Minor, not a hard-fail-grade distortion.

### C. Brand & tone — 2/3
- No banned words, no em dash, no clickbait. The lapse is structural-mechanical rather than lexical: the post runs the same "when X, when Y, or when Z" triple-clause list twice back to back ("Manual intake still makes sense when appointment capacity is comfortable, when reliable... or when body measurement is a small part...", then "Digital intake earns its place when high volume is straining..., when several sites..., or when rescreens keep tracing back..."), and closes with a third three-item list in the hybrid paragraph ("eligible steps done ahead of time, equipment-based testing kept on-site, and a manual fallback defined for..."). CLAUDE.md §6 names triple parallelism as an AI signature; the pattern repeating three times across a 165-word post plus the uniform paragraph length lint already flagged (`ai-tells:house_rule`) is exactly the mechanical rhythm the guardrail targets, even though no individual banned word or em dash triggers a hard fail.

### E. Output quality — 3/4
- **Position:** the post does take a stance, not just recite facts — opening line: "Going digital is not automatically the right call for occupational health screening. Sometimes the manual, in-person process is still the better fit," and it closes the framework with a specific recommendation: "Most strong programs land on a hybrid." That is a judged claim (contrarian to a default "digital wins" framing), not a compiled summary.
- **Angle distinctness:** clearly separate from `sibling_angles`. `twitter-company` is narrowly about the appointment-slot squeeze, `instagram-company` simplifies to a single "before you arrive" moment, `linkedin-company` is about cross-site measurement consistency as an enterprise problem. This post is the only one in the pack that lays out the full three-way decision framework (manual / digital / hybrid) and ends on an open discussion question — genuinely a different job than any sibling.
- Held to 3 rather than 4 because the triple-parallelism repetition noted under C makes the execution read slightly templated on a re-read, which is what keeps it from "ready as-is."

## Top issue for `post-drafter`

For `facebook-company` specifically, translate the source article's operational vocabulary (fixed appointment slots, rescreens, intake data) into plainer language per the brief's "broader audience, no jargon" instruction, and avoid running the same three-clause "when X, when Y, or when Z" list structure more than once in a single post.
