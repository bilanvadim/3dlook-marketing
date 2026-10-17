---
qc_date: 2026-10-17
agent: post-drafter
artifact: workspace/social/articles/aeo-glp-1-tracking-between-visits/linkedin-katya/post.md
track: social
artifact_type: post
total_score: 17/20
status: good
lint: pass (0 hard fails)
coordinator_review: |
  agreement: ✅ agree
  top_issue: implied scanning has no per-member cost; brand-checker flagged the same independently; polish round sent
---

# QC Report — post-drafter — linkedin-katya — 2026-10-17

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
- Regional discipline is clean: no geo term, no UK/EU/US payer context. Length 151 words, discussion question comes before the comments link, as the brief requires.
- The brief asks for customer problems, enterprise buying behaviour, trust and implementation. The post covers one thing, procurement cost modelling, which fits "enterprise buying behaviour". But it reads as a walk through the article's "At a Glance" column (scales/wearables, analyzers, smartphone), not as a practical observation from someone who talks to customers daily. Nothing about adoption or implementation.
- 3DLOOK appears once ("the category 3DLOOK works in") and is not forced. Good.

### C. Brand & tone — 2/3
- Paragraphs 3-5 are a three-item parallel list with the same build ("X are/carry/runs on Y"). That is the triple-parallelism pattern the brief bans, and it explains the lint warnings (sentence-length variation 0.32, uniform paragraph length).
- "Between visits, every method has a different primary cost driver. That decides how spend grows..." is generic framing. "Primary cost driver" is repeated close to the article's table wording, so it sounds like a table read aloud.
- "My rule of thumb:" and the closing vendor question are plain first person. Good. No banned words, no slogan ending.

### E. Output quality — 3/4
- **Position:** The opening, "the cost of body composition checks follows the hardware", is a claim someone could dispute. The rule "map each method's cost driver before comparing features" is a clear stance. The weakness is that the stance is one-sided. The post treats hardware as the thing that scales with members and calls smartphone scanning "software usage and integration". Per-use software cost also grows with every scan and every member, and the post does not say so. A sceptical operator will see the gap in the first reply. It also quietly favours 3DLOOK's own category without admitting that.
- **Closing question:** "How many devices would your current check-in method need at next year's member count, and who pays for them?" needs the reader's own numbers, so it passes. But it presumes the reader runs a hardware-based method.
- **Angle distinctness:** Distinct from all seven siblings. The cost-driver and scaling lens appears nowhere else. Nearest is linkedin-company (procurement), but that one scores against a fixed question set, not cost growth.

## Top issue for `post-drafter`

When a personal-profile post sorts options by one cost driver, require it to say how the recommended option's own cost also grows (per-usage pricing), and break the three-item parallel list into one stated rule plus one concrete example.
