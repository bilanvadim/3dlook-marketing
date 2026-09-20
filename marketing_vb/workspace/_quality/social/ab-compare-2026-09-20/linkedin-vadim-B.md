---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/bariatric-hub-refresh/linkedin-vadim/post.md
track: social
artifact_type: post
total_score: 19/20
status: excellent
lint: pass
coordinator_review: |
  agreement:
  top_issue:
---

# QC Report — post-drafter — linkedin-vadim — 2026-09-20

**Total: 19/20** — excellent

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 4 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 3 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 4 | 4 | judged |

## Findings

### A. Adherence — 4/5
- Region discipline is clean: `geo_mentions: 0`, no "Here in Australia…" opener, no market named anywhere in the body — exactly what personal-profile rule 3 asks for.
- Hook meets rule 5's spec directly: "The scans that decide your rollout are the ones that never complete." — ~13 words, a stance, not a question or teaser.
- Closing question ("What share of your remote captures need a second attempt right now, and can you break that number down by site?") needs the reader's own data to answer — satisfies "a question only you could have asked," not a "thoughts?" placeholder. "Article in the comments." matches the CTA note and rule 8.
- Focus fit: the post lands on operational excellence / implementation / real-world deployment from Vadim's brief focus list; a reasonable read of "Australian telehealth providers, digital health companies... enterprise health operators" extends to a bariatric-program audience.
- The one deduction: personal-profile rule 4 says "teach one thing… not a listicle," and the post explicitly frames "Two things I would settle before a pilot starts" with "First,… Second,…" — a two-item enumerated structure. The two items are tightly coupled (fallback trigger, split completion metric) so this doesn't read as a scattershot takeaway list, but it is the literal shape the rule warns against, and it's a judgment call the lint cannot catch.

### C. Brand & tone — 3/3
- No banned words, no em dash, no triple parallelism, no "not just X, it's Y."
- No puffery ("a new era of," "plays a crucial role") and no slogan tail — "Article in the comments." is a plain mechanical close, not a commitment-underscoring line.
- Voice is first person throughout ("I would settle," "The rest of the pilot is easier than those two") — correct register for a personal profile, and it reads like someone who has actually run this kind of pilot, not a company account.

### E. Output quality — 4/4
- **Position:** the post judges, it doesn't just describe. "A single blended completion rate hides the cost of the second group." is a specific claim someone could push back on (they might already segment their completion metric). "The scans that decide your rollout are the ones that never complete." reframes what "success" means for a pilot, ahead of any support from the article. "The rest of the pilot is easier than those two." ranks the two recommendations against everything else in the checklist — an opinion, not a summary of the source table.
- **Angle distinctness:** `sibling_angles` was not included in this A/B input, so cross-profile distinctness can't be judged from this file alone. Within the post itself, the angle (pre-pilot fallback design + split completion metric) is a specific translation of the article's "Accessibility and fallback" / "Capture completion" pilot-checklist rows (lines 130–131 of the article), not a restatement of the article's own framing.
- Grounding check beyond lint: "cannot stand unassisted," "second language," "staff or caregiver help," "in-clinic measurement," "retake sequence" all trace to the article's accessibility/fallback and capture-completion checklist rows. "A coordinator improvises one" is an inference from the article's Stage 2 coordinator role and its cross-site comparability note, not a invented customer detail or number — reasonable translation per the brief's "don't simply repeat the article" instruction, not a hallucination.

## Top issue for `post-drafter`

The "two things" structure ("First,… Second,…") is the literal listicle shape personal-profile rule 4 tells the drafter to avoid, even though the two items are one coherent teaching — worth a one-line reminder in the prompt that a tightly coupled pair is fine but should read as connected prose, not as an enumerated First/Second pair, if this pattern recurs across other posts in the pack.
