---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/bariatric-hub-refresh/linkedin-vadim/post.md
track: social
artifact_type: post
total_score: 18/20
status: excellent
lint: pass
coordinator_review: |
  agreement:
  top_issue:
---

# QC Report — post-drafter — linkedin-vadim — 2026-09-20

**Total: 18/20** — excellent

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 5 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 2 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 3 | 4 | judged |

## Findings

### A. Adherence — 5/5
- **Location discipline (personal-profile rule 3):** the post names no country at all — cleanest possible compliance, no "Here in Australia…" opener, no market-naming anywhere in the body.
- **Hook (personal-profile rule 5):** "Remote body capture looks simple until you run it on a bariatric population." — a ~12-word concrete claim someone could disagree with, exactly the prescribed pattern, not a question or teaser.
- **Teach one thing (rule 4):** the post commits to a single instruction — completion rate, split by assisted vs. unassisted, is the pilot metric that matters, not accuracy — and does not drift into a listicle or a walk through the article's section structure.
- **Close (rule 5):** "What completion rate would make a remote-first intake worth running for your program?" needs the reader's own numbers to answer — matches the rule's bar exactly, better than a generic "thoughts?"
- **Brief focus list:** hits operational excellence, scalability ("before you scale it"), implementation, and product quality (retake logic, quality flags) directly; privacy and enterprise procurement are untouched but the brief lists these as a focus menu, not a checklist every post must clear.
- Checked against the article: every claim used (accessibility factors, assisted-vs-unassisted completion split, in-clinic fallback, FitXpress retake logic/quality flags) traces to the "What to confirm in a bariatric pilot" table and Stage-2 workflow text — no quantifier was dropped and no case/subject was swapped.

### C. Brand & tone — 2/3
- The post uses the same negate-then-assert contrast twice, which is the "X, not Y" / "it's not just X, it's Y" AI-signature family split across a sentence boundary instead of a comma — the construction the lint's single-sentence regex won't catch:
  1. "The number I'd watch in a pilot isn't accuracy. It's completion rate, split two ways…"
  2. "Build the fallback path before you send the first scan link. Not after the first patient can't stand long enough for the capture."
  Two instances of the identical rhetorical shape in a 149-word post is a tic, not a coincidence, and it's part of why the lint's own `ai-tells:house_rule` warnings fired ("monotone rhythm… 0.29", "uniform paragraph length: every block the same size") — the negate/assert pairing produces paragraphs of near-identical two-sentence shape throughout.
- No banned words (leverage/utilize/harness/robust/seamless/comprehensive/etc.), no em dash, no puffed-up-significance language ("a new era of…"), no slogan close, no commitment-tail sentence. First person is used correctly and consistently for the personal-profile voice ("I'd watch").

### E. Output quality — 3/4
- **Position:** "The number I'd watch in a pilot isn't accuracy. It's completion rate, split two ways: patients who finish alone, and patients who need staff or caregiver help." — this is a real, arguable judgment about what to measure, not a restatement of the article's checklist. A second position follows it: "Build the fallback path before you send the first scan link. Not after…" is a sequencing prescription, not a neutral description.
- **Angle distinctness:** no `sibling_angles` field was supplied in this input packet, so distinctness against the other eight profiles in the pack could not be checked directly. `post_meta`'s own angle line claims distinctness from the GLP-1, human-moment, bottleneck, CMS-deadline and provenance angles; the angle actually delivered in the body (completion rate, not accuracy, as the pilot metric; accessibility as the mechanism) is specific enough to plausibly be non-overlapping, but this claim is unverified against sibling posts.
- Held at 3 rather than 4 because the repeated negate/assert construction (see C) and the flat paragraph rhythm the lint already flagged mean the post reads slightly patterned on a close read, even though the position and hook are strong and it is close to publishable as-is.

## Top issue for `post-drafter`

The negate-then-assert contrast ("X isn't the thing. It's Y.") is the banned "not X, it's Y" AI-signature rewritten across a sentence boundary to dodge single-sentence detection — worth naming explicitly in the prompt's no-go list as a construction, not just a punctuation pattern, since it recurred twice in one short post.

TOTAL: 18/20
