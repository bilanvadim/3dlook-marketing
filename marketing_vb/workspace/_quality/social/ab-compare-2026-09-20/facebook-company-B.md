---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/bariatric-hub-refresh/facebook-company/post.md
track: social
artifact_type: post
total_score: 16/20
status: good
lint: pass
coordinator_review: |
  agreement:
  top_issue:
---

# QC Report — post-drafter — facebook-company — 2026-09-20

**Total: 16/20** — good

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 3 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 3 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 2 | 4 | judged |

## Findings

### A. Adherence — 3/5

The brief for `facebook-company` is explicit: *"Broader audience than LinkedIn — explain without jargon. Slightly warmer."* and *avoid: "Dry B2B corporate tone."* The post does not execute this; it reads as a compressed clinical/B2B summary of the source article, indistinguishable in register from a LinkedIn-company post:

- "as long as the later ones use the same guided sequence and return the same fields" — "guided sequence" and "same fields" are lifted straight from the article's clinical-workflow vocabulary and never translated for a lay reader. A broader Facebook audience is not expected to know what a "guided sequence" or a record's "fields" are.
- "how much more of their trajectory would your team see?" — the closing line addresses "your team," i.e. a clinical/operations audience. This is the same addressee as the LinkedIn-company post would use, not a broadened, warmer readership.
- No sentence in the post attempts plain-language framing, an analogy, or a warmer register (e.g. speaking to a patient's or family's experience) that would differentiate it from a B2B channel. "Circumference measurements," "body composition estimates," and "medication history" are used exactly as clinical shorthand, unexplained.

What is followed correctly: length (1128 chars, within 800-1200), no hashtags, CTA format, product bias (100% FitXpress), and the closing question does satisfy the "Industry question that sparks discussion" content type structurally — the failure is tone/audience, not structure.

### C. Brand & tone — 3/3

No banned words (leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/tapestry/realm/unlock/unleash/game-changing/cutting-edge), no em dash, no "not just X, it's Y" construction, no triads, no inflated-significance phrasing ("a new era of," "plays a crucial role"), no slogan-style close, no trailing filler clause. "Here is the question we keep coming back to" uses first-person plural appropriately for a company page voice — this is not a personal-profile post, so the company "we" is correct rather than a violation.

### E. Output quality — 2/4

- **Position:** Not found. Every substantive claim in the post is explicitly hedged into neutrality rather than resolved into a stance: "When the care team deems them appropriate, these values can be reviewed alongside medication history"; "The program sets the cadence and decides which fields to keep." The post states mechanics (what a scan record can contain, what a study found) and stops there — it never says what 3DLOOK thinks a program should do differently, or why earlier capture is worth the operational cost. The close, "If a patient's body-data record started at the first intake instead of the surgical consultation, how much more of their trajectory would your team see?", is phrased as an open question rather than an assertion; it satisfies the brief's "industry question" content type but is not a substitute for a judgment, per the rubric's standard that a post which only constates reads as compiled regardless of factual density.
- **Angle distinctness:** Cannot be judged — `sibling_angles` was not included in this task's input, unlike the standard qc-prompt contract described in the agent's brief.

## Top issue for `post-drafter`

For `facebook-company`, stop reusing the SEO article's clinical-operations register verbatim (guided sequence, field structure, "your team") — the profile brief calls for a broader, warmer, jargon-free audience than LinkedIn, and the draft currently reads identically to a B2B/LinkedIn summary.
