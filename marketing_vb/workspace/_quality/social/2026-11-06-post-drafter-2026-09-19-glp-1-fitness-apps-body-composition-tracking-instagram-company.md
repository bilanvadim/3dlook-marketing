---
qc_date: 2026-11-06
agent: post-drafter
artifact: workspace/social/articles/2026-09-19-glp-1-fitness-apps-body-composition-tracking/instagram-company/post.md
track: social
artifact_type: post
total_score: 18/20
status: excellent
lint: pass
coordinator_review: |
  agreement: ✅ agree
  top_issue: Minor overlap with facebook-company's honesty-about-limits beat; craft is solid enough to ship as-is, no rewrite round spent.
---

# QC Report — post-drafter — instagram-company — 2026-11-06

**Total: 18/20** — excellent

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 4 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 3 | 3 | lint |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 3 | 4 | judged |

## Findings

### A. Adherence — 4/5
- Brief's first listed `content_type` for this profile is "Human outcome from the article (patient scan, tailor measuring client, etc.)". The post delivers a direct second-person address ("Your progress," "that conversation stays with your clinician") but never grounds it in a concrete human moment, it stays at the explainer level. The middle paragraph reads as a repackaged feature list rather than a scene: "Weight. Waist and hip measurements. Body composition estimates. Completed strength sessions." Four noun fragments in a row is closer to the article's comparison table than to "visual storytelling, less corporate, more brand."
- What it does get right: hook is a genuine two-line visual metaphor visible before "more" ("The scale is one line on the chart. Your progress is the whole picture. 📊"), matches brief's "hook in first line" requirement exactly. CTA ("Link in bio.") matches the brief's prescribed options. No pricing, no API-talk, no jargon beyond the one necessary GLP-1 spell-out (which the source article itself spells out on first use).
- Design tip pairing is tight: the post's central "fuller picture" framing maps directly onto the four-row timeline infographic (`banner_2-2.webp`) the design tip calls for, so caption and visual will read as one idea on the feed.

### C. Brand & tone — 3/3
- No banned words (leverage/utilize/robust/etc.), no em dash, no "not just X, it's Y." The one negation, "lean mass, and lean mass is not the same as muscle," is a single clinical-boundary statement (the §1.8 exception pattern: state the limit once, plainly), not a rhetorical corrective-negation tic. Nothing flags against CLAUDE.md §6.

### E. Output quality — 3/4
- **Position:** the post does judge, not just list. "The scale is one line on the chart. Your progress is the whole picture." asserts that scale weight alone is an inadequate progress signal. The closer, "Progress is easier to read when every value shows its source," is a stance about design (provenance labeling), not a recap of article facts. This clears the E≤2 "no position" floor.
- **Angle distinctness:** per `post_meta`, the assigned angle is the visual timeline ("fuller picture" + source labels). In execution, though, the honesty beat ("A scan can estimate lean mass... It cannot tell you which tissue changed") lands very close to `facebook-company`'s sibling angle ("what a scan can and cannot tell you... it cannot prove a member lost muscle"). The two posts share the same core admission almost one-for-one; what differs is the opening visual metaphor and the close (Instagram: declarative + "Link in bio"; Facebook: closes with a question for a broad audience). The platform-appropriate packaging is distinct enough to not be a duplicate, but the substance underneath is the same honesty beat used twice in the pack.
- Craft is solid and ready with light editing (the noun-fragment paragraph is the one spot an editor would tighten), not quite the as-is, no-touch bar for a 4.

## Top issue for `post-drafter`

When the assigned angle is "visual timeline, human screen-level moment," write an actual beat (a person checking their app, not a list of data types) instead of restating the article's comparison-table rows as sentence fragments, and check the draft against sibling angles before finalizing so the same honesty-about-limits beat isn't the load-bearing line in two profiles at once.
