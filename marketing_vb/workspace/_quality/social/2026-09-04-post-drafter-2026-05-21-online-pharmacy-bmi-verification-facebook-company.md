---
qc_date: 2026-09-04
agent: post-drafter
artifact: workspace/social/articles/2026-05-21-online-pharmacy-bmi-verification/facebook-company/post.md
track: social
artifact_type: post
total_score: 16/20
status: good
lint: pass
coordinator_review: |
  agreement: ✅ agree — the two corrective-negation constructions QC caught are a hard ban under CLAUDE.md §6, and lint's regex missed both. Applied a targeted fix post-QC (removed both "not X, it is Y" constructions, plain-languaged the CDC follow-up sentence and the FitXpress spec line) before finalizing the pack artifact; this report keeps the pre-fix scoring intact for agent-improver.
  top_issue: post-drafter carries the article's own clinical sentence structure into non-LinkedIn profiles instead of re-registering it for the audience; watch for corrective-negation constructions specifically since lint does not catch them.
---

# QC Report — post-drafter — facebook-company — 2026-09-04

**Total: 16/20** — good

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 3 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 2 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 3 | 4 | judged |

## Findings

### A. Adherence — 3/5
- Structural fit is good: the hook ("How much would you trust a health number that someone typed in themselves?") and the close ("how much verification is enough, and at which step?") both match the brief's `Industry question that sparks discussion` content type, and the CTA follows the required "Read the full article (link in comments)" pattern.
- The brief calls for "Accessible and community-oriented... Broader audience than LinkedIn — explain without jargon. Slightly warmer." The post instead imports the article's clinical register close to verbatim: "self-reported BMI underestimated the prevalence of severe obesity by 40% compared with bias-corrected estimates, 5.3% versus 8.8% in 2020 data" is the article's own sentence (`published-live-2026-08-24.md` line 166), lightly trimmed, not translated for a lay FB reader. "Bias-corrected estimates," "eligibility," and "prescribing decision" are exactly the kind of jargon the profile brief asks to strip out for this audience.
- "FitXpress handles the scan: two guided live photos, processing typically under 45 seconds, camera roll disabled, image captured live." is a telegraphic spec list, not warmer community copy — the brief's own `avoid` line names "technical API details" and, more broadly, "dry B2B corporate tone." This paragraph reads as B2B-compliance shorthand carried over unchanged from a LinkedIn-register source, not adapted down for Facebook.

### C. Brand & tone — 2/3
- "It is a population-level finding, not a verdict on any one person" and "The hard part is not the technology, it is the judgment call" are both corrective-negation constructions ("X, not Y" / "not X, it is Y") — the exact family CLAUDE.md §6 and `terminology-guardrails.md` Part 1 ban ("It's not just X, it's Y", corrective negation). Neither is the literal banned phrase, so lint's regex-based `ai_density` check (5.43%) didn't flag them, but two instances of the same rhetorical tic in a 177-word post is a pattern, not a one-off.
- `lint.warnings` also flags "uniform paragraph length: every block the same size" — a mechanically-detected AI signature (monotone rhythm) that reinforces the same read: the post is well-formed but has the cadence of a template rather than a person writing to a Facebook audience.
- No banned vocabulary (leverage/utilize/harness/etc.) and no em dash — so this stays at 2, not 1.

### E. Output quality — 3/4
- **Position:** "it shows why a typed-in number and a loose photo are thin evidence when a prescribing decision rides on them" — this is a real judgment, not just a restatement of the CDC finding. The post earns credit here that a purely-descriptive summary wouldn't.
- The close deliberately reopens as a question ("how much verification is enough, and at which step?") rather than answering it — on-brief for the "sparks discussion" content type, so this isn't a defect, but it means the piece's only stated position sits mid-post and the ending doesn't reinforce it with a stance.
- **Angle distinctness:** clearly separate from `instagram-company` (Katerina's personal AI-photo experiment narrative) and `linkedin-katya` (single procurement question on capture method). This post's route — population-level CDC data → general discussion question — is its own lane and doesn't restate either sibling.

## Top issue for `post-drafter`

When adapting a stat-heavy sentence from the source article for `facebook-company`, rewrite it in lay language instead of trimming the article's own clinical phrasing, and avoid stacking more than one "not X, it is/it's Y" construction in a single short post.
