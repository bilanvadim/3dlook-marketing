---
phase: 4_self_critique
article: 2026-05-29-3dlook-accuracy-enterprise-evaluation
date: 2026-05-29
status: applied_to_draft_v2
parent: draft-v1.md
output: draft-v2.md
---

# Phase 4 — Self-critique of draft-v1.md

Eight findings. The first six are real issues that produce edits in draft-v2.md. The last two are observations I noted but decided not to act on, with the reasoning recorded so the call can be re-examined later if needed.

## Findings that produce edits

### 1. Missing internal cross-links (4) — self-flagged in Phase 3 report

The Phase 2 outline specified four cross-links to past 3DLOOK articles. Zero made it into draft-v1.md. This is a real execution miss, not a judgment call.

**Fix in v2.** Insert all four, in the locations specified by the outline:
- `mobile-body-scanning-insurance-underwriting` → in D4 row 3 (Life & disability underwriting)
- `wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning` → in D4 row 1 (Telehealth / GLP-1)
- `body-scanning-technology-comparison` → in H2.7 opening
- `3dlook-turns-two-photos-structured-body-data` → in H2.3 opening

### 2. Word count over ceiling (+151)

Target was 3,500–4,500 words. Draft-v1 came in at 4,651, which is 4.3% over. Not a structural problem, but worth fixing because the ceiling exists for a reason — enterprise readers skim long-form, and trimming forces tighter sentences.

**Fix in v2.** Targeted trims, total ~180 words, spread across:
- H2.4 ground-truth section: NCSU framing is partially redundant with D5 — compress (-50 words)
- H2.7 opening paragraph: meta-sentence about "honest framing" removed (-30 words)
- H2.1 closing sentence: slight tightening (-20 words)
- FAQ answers 1, 3, 5, 7: pull from 4 sentences to 2–3 each (-50 words total)
- H2.4 closing sentence about "2026 version of dataset has continued to grow": remove (it's a hedge against future drift, not load-bearing) (-30 words)

Target post-trim: ~4,470 words, comfortably inside the ceiling.

### 3. "Table is what makes that decision possible" — editorial close

End of Dimension 1: "The table above is what makes that decision possible." Reads as self-congratulatory framing of 3DLOOK's own disclosure as the standard. The point is fine; the phrasing is the problem.

**Fix in v2.** Replace with neutral close: "Without the per-measurement breakdown, that decision cannot be made on the headline number alone."

### 4. H2.7 industry context claim — weak attribution

The sentence "Published evaluations of mobile body measurement systems typically report waist-circumference error in the 1.5 to 2.2 cm range" is lifted from a 3DLOOK internal deck (Feb 2025 PDF p.7), which itself does not cite third-party studies. Presenting it as "published evaluations" implies an external citation that the article does not provide. Honest framing requires either citing the source or softening the framing.

**Fix in v2.** Reframe as internal observation: "Mobile body measurement systems in this category typically operate in a 1.5 to 2.2 cm waist-circumference error range, with 3DLOOK's internal validation placing it at the lower end of that range." Drops the "published evaluations" wording entirely, which removes the implied external citation.

### 5. NCSU redundancy in H2.4

NCSU is fully described in D5 (purpose, year, public link, framing as dataset enrichment not validation). H2.4 then re-describes the same partnership with the same framing across four sentences. The second description should reference back to D5 instead of repeating it.

**Fix in v2.** Replace the H2.4 NCSU paragraph with a tighter version: state the dataset expansion fact, cite the partnership year and lab, link out to NCSU, and reference D5 for the full validation-vs-enrichment framing.

### 6. Declarative meta-sentence in H2.7

"The honest framing for 3DLOOK is to describe each method in its own terms and note what 3DLOOK is and is not designed to do alongside it." This is a meta-statement about the framing, not actual framing. Same effect achieved by just doing the framing.

**Fix in v2.** Delete this sentence; lead directly into the methods.

## Observations not acted on

### 7. Possible over-disclosure in disclaimer + FAQ

Both the disclaimer block and FAQ Q1, Q6 spell out "not peer-reviewed, not third-party validated, not clinically certified, not a medical device". This appears in at least four places across the article (disclaimer + FAQ Q1 + FAQ Q6 + checklist Q8). Could feel repetitive to a reader who reads the article in full.

**Decision: keep all four.** Each occurrence serves a different reader path. The disclaimer covers the procurement / legal reader. FAQ Q1 covers the SEO snippet reader. FAQ Q6 is the explicit "validation" question. Checklist Q8 closes the framework. A reader who hits the article via search and lands on the FAQ should not have to scroll up to find the disclosure. Reading the article in full is not the primary reader path; the article is built for skim-readers landing on specific sections. Repetition is intentional and correct for this audience.

### 8. Em-dash density (34 instances in 4,651 words)

CLAUDE.md §6 bans em-dashes in the rhetorical "X — это не просто Y" pattern. The blog-style-guide is presumably consistent. Style scans confirmed no rhetorical "not just X — Y" or "It's not just X, it's Y" instances in draft-v1. The 34 em-dashes are all parenthetical or range separators, which are not the banned pattern.

**Decision: keep as is.** Replacing parenthetical em-dashes with parentheses or commas would change voice without removing any banned pattern. The rule is about rhetorical em-dashes specifically, not em-dash density.

## Edits summary applied to draft-v2.md

| # | Section | Change | Word delta |
|---|---------|--------|------------|
| 1 | D4 row 1 | Add link to wellness-rewards article | +0 (link only) |
| 1 | D4 row 3 | Add link to insurance-underwriting article | +0 |
| 1 | H2.3 opener | Add link to 3dlook-turns-two-photos article | +0 |
| 1 | H2.7 opener | Add link to body-scanning-technology-comparison | +0 |
| 2+5 | H2.4 | Compress NCSU paragraph; remove dataset-growth hedge | −80 |
| 2 | H2.1 close | Tighten last sentence | −20 |
| 2+6 | H2.7 opener | Remove meta-sentence; tighten opening | −30 |
| 2 | FAQ Q1, Q3, Q5, Q7 | Trim from 3–4 sentences to 2–3 | −50 |
| 3 | D1 close | Replace "table is what makes..." with neutral close | net 0 |
| 4 | H2.7 industry context | Reframe attribution | net 0 |

Net change: ~−180 words. Target post-trim: ~4,470 words.

Frontmatter status updated to `phase_4_self_critique_applied`, output filename to `draft-v2.md`.
