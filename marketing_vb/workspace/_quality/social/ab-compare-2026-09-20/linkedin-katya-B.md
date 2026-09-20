---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/bariatric-hub-refresh/linkedin-katya/post.md
track: social
artifact_type: post
total_score: 20/20
status: excellent
lint: pass
coordinator_review: |
  agreement:
  top_issue:
---

# QC Report — post-drafter — linkedin-katya — 2026-09-20

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
- **Location discipline (personal rule 3, the pipeline's most common real defect) is clean.** `geo_mentions: 0` in the lint metrics, and I confirm by reading: the post never names Israel, the Gulf, or any region, and never lapses into "I speak with operators across the region every week" or any variant the brief explicitly bans.
- **Structure matches the profile's closing requirement exactly.** "Finish with a discussion question before linking to the article" → the post does "How long does a flagged record sit in your queue before someone opens it?" immediately followed by "The article is in the comments." — question first, link second, in that order.
- **Hits the profile's focus list without drifting into forbidden territory.** The angle (who owns a flagged discrepancy before a contract is signed) sits squarely in "enterprise buying behaviour" and "implementation," and the post never touches the "Avoid" list items (no EU regulatory specifics, no US payer/CMS-0057-F detail even though the source article discusses it at length, no apparel content).
- **Personal-profile rule 5 (hook, first person, closing question) is followed to the letter**: hook is a declarative, disagreeable claim ("Deployments stall on one unanswered question: who acts when the system raises a flag."), the "what I would do about it" beat is first-person ("Before signing anything, I would put one question to the program itself…"), and the closing question needs the reader's own operational number to answer — not a "thoughts?" placeholder.
- **Rule 4 ("teach one thing") is satisfied via the explicitly-sanctioned form** — "a question to put to a vendor" — rather than a listicle or a walk through the article's structure.
- I checked the mechanism claim against the article itself (`workspace/seo/articles/bariatric-hub-refresh/published-live-2026-09-20.md`) for the two things the lint can't verify — case/client substitution and quantifier loss. Neither is present: "BMI from self-reported height and weight... BMI from the same height and the predicted weight from the scan... A difference above the configured threshold is routed for human review" tracks the article's Stage 1 paragraph almost verbatim, with no subject swapped and no bound (threshold, "configured") dropped.

### C. Brand & tone — 3/3
- No banned words, no em-dash rhetoric, no triple parallelism, no inflated-significance phrase ("a new era of," "plays a crucial role") and no slogan-tail ("…, underscoring our commitment").
- The post consistently calls the actor "the program," never "the customer" — this is the judgment-level terminology-guardrails distinction (CLAUDE.md §6: `customer` only for a contractual/deploy role) executed correctly without being told to in the profile brief.
- One very minor, non-scoring stylistic note for the record: "Here is the mechanic." uses "mechanic" where "mechanism" (or "how it works") is the more standard noun. Colloquial enough to read as intentional voice rather than an error, and not a banned-word or AI-signature hit, so it does not cost a point.

### E. Output quality — 4/4
- **Position:** the post has two, not one. First, an interpretive claim about fault: *"If no one owns that step, the flag becomes a ticket nobody closes, and the technology takes the blame."* — an arguable judgment about where the failure actually sits (process, not product). Second, a concrete prescription: *"Before signing anything, I would put one question to the program itself: which role reviews a flagged record, and what is that person allowed to do next?"* This is a real stance a reader could push back on, not a restatement of the article's mechanic.
- **Angle distinctness:** no `sibling_angles` were supplied with this A/B input (single-post scoring task, not the full qc-prompt), so I cannot compare against the rest of the pack. Judged in isolation, the angle is not a restatement of the article's own framing — the article documents the BMI-comparison mechanism and the pilot checklist as features to confirm; this post turns the same checklist row ("who reviews the record… what happens after a discrepancy is flagged?") into a pre-signature commercial test, which is a genuine reframing rather than the mechanic described a second time.
- The closing question is specific enough to generate a real LinkedIn reply (a queue-time number), not a "thoughts?" filler.

## Top issue for `post-drafter`

None — this post is a clean execution of an unusually detailed and constraint-heavy profile brief; nothing here indicates a prompt gap to fix.
