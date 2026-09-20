---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/2026-07-14-fitxpress-privacy-security-faq/linkedin-nick/post.md
track: social
artifact_type: post
total_score: 19/20
status: excellent
lint: pass
coordinator_review: |
  agreement: ✅ agree
  top_issue: Personal-profile voice should be first person throughout; here only the closing line is, the body leans on "the vendor / the customer / you" — worth an agent-improver note, not a rewrite at 19/20.
---

# QC Report — post-drafter — linkedin-nick — 2026-09-20

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
- **CTA order reversed.** Brief structure is "discussion question → invite to the article." The post runs it the other way: "We published the rest of these answers in writing, with the qualifications attached." lands *before* "Before you sign, do you ask for the BAA first, or the security review?" Minor, but it is a literal brief step done out of order rather than skipped, which is what keeps this at 4 rather than 5.
- **Voice is mostly third person, not first person.** The global personal-profile rule is explicit: "first person, contractions fine." Almost the entire body is written about "a vendor," "you," "the vendor," "the customer," and "We published" (corporate collective) — genuine first person shows up only in the closing sentence, "I'd like to know where your team draws that line." For a post signed by Nick, that's one first-person clause propping up 150 words of impersonal/corporate framing. This is a brief-compliance gap, not a tone defect — the sentences themselves are fine, they're just not written as Nick talking.
- What the brief did get right: no geo announcement in sentence one, hook is a claim not a question ("HIPAA is not a certificate a vendor can hand you."), FitXpress mentioned once and naturally, no European regulatory content, no buzzwords.

### C. Brand & tone — 3/3
- "It's a regulatory framework, not a certification" is the CLAUDE.md-approved exception to the corrective-negation ban (§6, the exact trust-FAQ sentence), not a lapse — flagging so it isn't miscounted by a future pass.
- No em dash, no banned words, no AI-tell constructions found in the body.

### E. Output quality — 4/4
- **Position:** "a certification logo answers the wrong question. Ask whether they'll sign a Business Associate Agreement (BAA) and stand behind it as a business associate. That is the line that actually protects you." This is a judgment call, not a restatement of the FAQ — it tells the reader what to do differently, which is the bar E is checking for.
- **Angle distinctness:** distinct from `sibling_angles` — this post's claim is "the vetting question buyers ask is wrong" (BAA vs. certificate), not `linkedin-company`'s "publishing answers speeds up security review." The two posts share the same underlying artifact (the published FAQ) but assert different things about it; not a restated angle.

## Top issue for `post-drafter`

On the five personal LinkedIn profiles, default to writing the body in first person throughout rather than switching to third-person/corporate framing ("the vendor," "the customer," "we published") and adding a single first-person clause only in the closing line — the brief's "first person" rule should read as a whole-post requirement, not a CTA requirement.
