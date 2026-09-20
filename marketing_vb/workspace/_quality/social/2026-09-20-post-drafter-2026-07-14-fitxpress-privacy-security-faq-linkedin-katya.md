---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/2026-07-14-fitxpress-privacy-security-faq/linkedin-katya/post.md
track: social
artifact_type: post
total_score: 18/20
status: excellent
lint: pass
coordinator_review: |
  agreement: ✅ agree
  top_issue: Hook "decides more deals than the demo does" echoes linkedin-company's "not the demo" contrast; open personal instances on their own specific detail, not the company post's framing.
---

# QC Report — post-drafter — linkedin-katya — 2026-09-20

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
- Focus list hit correctly: "The blocker is a procurement question" / "your legal team will ask for anyway" lands squarely on enterprise buying behaviour and trust, both on the profile's focus list.
- Rule 3 (no location announcement) honored: `geo_mentions: 0`, and the AWS regions (US-West-2, US-East-1) are the claim's substance, not a market flag — this isn't the "For US teams…" pattern the rule bans.
- Persona stance rule honored by omission: the post never says "I speak with operators across the region," it just writes from that stance ("I've watched a scanning tool pass the product review and still stall").
- Avoid-list respected: no EU regulatory specifics, no US payer-system context, no apparel.
- CTA matches brief: discussion question in the body, article link deferred to the first comment.

### C. Brand & tone — 2/3
- No banned words, no em-dash rhetoric, no "not just X, it's Y." Clean on the rubric's explicit checklist.
- The lint's `ai-tells:house_rule` warning ("uniform paragraph length: every block the same size") is real and worth a point here, not a shrug: paragraphs 2, 3 and 5 (29, 35, 32 words) are all built the same way — one flat statement, then one longer sentence unpacking it. Three paragraphs in a five-paragraph post sharing identical internal shape is the kind of rhythm-sameness the AI-tells catalog flags even when raw word counts differ (13/29/35/23/32/20). Varying that shape (a one-line paragraph, a three-clause one) would remove the tell.

### E. Output quality — 3/4
- **Position:** "If they won't name the region, I take that as my answer." This is a real judgment call, not a fact restated — a vendor's silence on data location is treated as disqualifying, and the reader can disagree with that bar.
- **Angle distinctness:** The teaching (make the vendor name the AWS region in writing) is genuinely different from every sibling angle — it's the only one built around a specific vendor question. But the framing device in the hook, "decides more deals than the demo does," is the same rhetorical move as `linkedin-company`'s angle, "deals stall at the security and legal review, not the demo." Both posts open by setting the demo up as the wrong signal and the back-office review as the real one. The specific artifact each post hands the reader is different enough that this isn't duplication, but it's close enough in framing that a reader who sees both posts in the same week will notice the same opening move twice.

## Top issue for `post-drafter`

When a personal profile's angle is a specific instance of `linkedin-company`'s broader market-process observation, open with the specific vendor-facing detail (the region question) rather than reusing the company post's "not the demo" contrast as the hook.
