---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/bariatric-hub-refresh/linkedin-olena/post.md
track: social
artifact_type: post
total_score: 20/20
status: excellent
lint: pass
coordinator_review: |
  agreement: ✅ agree
  top_issue: none
---

# QC Report — post-drafter — linkedin-olena — 2026-09-20

**Total: 20/20** — excellent

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 5 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 3 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 4 | 4 | judged |

## Findings

### A. Adherence — 5/5
- Geo discipline is exact for this profile: `geo_mentions: 0`, no country named, no "operators across Europe" tell — the market stays the audience, never the subject, per house rule 3. Checked for the two most common failure modes on this profile (UK reference, US regulatory reference) and found neither; the post stays EU-wide via GDPR, which is explicitly permitted.
- All five personal-profile rules land: hook is a ~12-word disputable claim, not a question ("Governance stalls remote-scan pilots in obesity care more often than accuracy does."); one thing taught, stated as a rule of thumb ("write the data-governance answer into the pilot plan before the first scan"); first-person prescription ("My rule of thumb…"); closing question requires the reader's own program specifics, not a generic "thoughts?" ("Where does your program draw the line between what a scan captures and what it stores?").
- Verified the two factual claims against the article's Privacy and security section and Data governance checklist row (`published-live-2026-09-20.md` lines 138, 142): the controller/processor sentence and the photo-deletion window are lifted at the article's own wording, not a rebuilt or drifted version — including the article's own "controller"/"processor" phrasing without "the data" prefix, which matches the CLAUDE.md canonical GDPR line's substance even though it isn't verbatim from CLAUDE.md itself.
- Structure follows the brief (hook → short paragraphs → question → article pointer); bullet points are "where appropriate" and the post correctly has none, given its length.

### C. Brand & tone — 3/3
- No banned words, no em-dash rhetoric, no triple parallelism, no "not just X, it's Y". Reads as a person's rule of thumb, not a company memo — consistent with the personal-profile register.
- The one paraphrase from the article's "the customer's policy" to "your policy" is a deliberate second-person address in an advisory sentence, not a claims or actor error — CLAUDE.md's `you` guardrail explicitly permits this in practical blocks.

### E. Output quality — 4/4
- **Position:** The post opens on a judgment that could be disputed on its face — governance, not accuracy, is the real blocker — and backs it with a concrete instruction rather than just restating the article's checklist: "write the data-governance answer into the pilot plan before the first scan. Retention, access control, and photo deletion are questions you answer once, up front." This is Olena's own prescriptive framing, not a summary of the article's nine-row table.
- **Angle distinctness:** Genuinely separate from all seven sibling angles — none of GLP-1 documentation, the human moment, the intake bottleneck, CMS-0057-F deadlines, provenance, post-op baseline, or completion touches data governance or GDPR roles. No overlap risk in this pack.

## Top issue for `post-drafter`

None — this post is publish-ready as-is; no repeatable defect to flag for the prompt.
