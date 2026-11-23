---
slug: ai-body-scanning-for-fitness
workspace: ai-body-scanning-for-fitness-refresh
product: fitxpress
stage: seo-editor
round: Review 1 (EDIT round)
input: v1/final.md + review-1.md + review-1-decisions.md
output: final.md
date: 2026-11-23
verdict: PASS (article_lint 10/10, detector CLEAN)
previous_report: v1/editor-report.md
---

# Editor report: ai-body-scanning-for-fitness, Review 1 round

`review-1-decisions.md` is applied item by item to `final.md`. Nothing outside items A1, A2, A3, B1, B2, B3, and D3 changed. A body diff against `v1/final.md` touches only those items. The sections listed in decision E (short answer apart from B2 and the CTA, member journey apart from the example, S5, S7, the three FAQs, the scope note, Next steps) were not edited. Nothing in them was polished. The decisions file changed on disk during the round: A1's last bullet now cites the new `blog-style-guide.md` §5 two-CTA rule. I re-read it in full, and it needed no further change: the S6 landing link is a plain contextual sentence, not a CTA.

## Result per decision

| ID | Status in decisions | Result |
|---|---|---|
| A1 | ACCEPT, VERBATIM | Done verbatim. The short-answer landing paragraph is unchanged. The two-sentence CTA paragraph follows it, then `[Explore FitXpress for fitness apps](https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/)` on its own line. It goes to the landing, not `#form`, at 15.7% of the body. Text only, no box. |
| A2 | ACCEPT, CHANGED | New H2 verbatim. The section is 220 words with headings (v1: 307), the top of the 180-220 range. Two-sentence answer-first opening carrying FIT-CAPTURE and FIT-SDK. One sentence on in-club hardware, with BIA expanded at first use. Three H3 lists of three bullets each; the own-brand bullet was dropped. The pitch and outputs sentences were removed, with FXS-SPEED and FXS-OUTPUTS. The closing keeps both required sentences and the comparison link, and ends on the map anchor "mobile alternative to a gym body scanner" (69.0%). No heading reuses the landing H1. |
| A3 | ACCEPT, VERBATIM | Inserted verbatim between "Scheduled check-ins." and "Coach review.". No gate failed on it, and no word was changed. |
| B1 | ACCEPT | S4 went from 254 to 225 words with the H2. Adjust and Kidman are kept with their qualifiers, links, and claim comments. ACSM is cut to two sentences. Both internal links are kept, one sentence each. The verbatim question comes after the statistics, then "None of these sources tested body scans." and the measured-with-own-members sentence. The hypothesis is not repeated: the S4 sentence "A record of that change can give the member a reason to return…" was cut, and S8 keeps its own wording. |
| B2 | ACCEPT concern, REJECT wording | The bullet is replaced verbatim with the canon line. The reviewer's "typically … after capture" is not used. |
| B3 | ACCEPT | Primary-outcome wording added. The secondary metrics list is verbatim, in order, in one sentence. The reason is in the article's own words: "Return rates measure engagement; the secondary metrics also capture the friction a new step adds." No landing FAQ wording is used. The rest of S8 is unchanged. |
| D3 | ACCEPT, VERBATIM | `meta_description` in the final.md frontmatter is replaced verbatim. meta.md and publish-package.md are not touched (out of scope for this round); see Open items. |

### What changed beyond the literal instruction, and why

- **A2, length cuts.** Three cuts brought the section from 241 to 220 words:
  - "A club can keep its device for visits and use phone scans between them." It is not on the decision's keep list, and it echoed the landing's comparison close in meaning ("An in-gym scanner still suits members who visit the club; FitXpress covers the check-ins between visits.").
  - The lead-in "The choice turns on where members train and what each check-in has to record." The opening now states where a phone scan fits.
  - "are not measured and" in the third progress-photo bullet. Bullet 2 already says the app needs no measurements.
- **B1, Adjust.** "They count all app users, and paying members may behave differently." became part of the preceding sentence: "The figures are global and use 2022 data from all app users." The three qualifiers the decision names are kept. The paying-members caveat was cut for length.
- **B1, ACSM.** The ACSM paragraph now leads with the finding ("Wearable technology ranked first and mobile exercise apps second in the American College of Sports Medicine (ACSM) 2027 Worldwide Fitness Trends, released October 20, 2026."). This keeps the sentence at 25 words. With the release date first it ran to 26. This also resolves the v1 QC open item: the ACSM paragraph's last two sentences stated a difference without a consequence, and they are now cut.

## Deviations from VERBATIM lines and from the decision text

No gate failed on any VERBATIM line, and no word inside a VERBATIM quote was changed. Three placement or wording choices, recorded so they can be checked:

1. **B1 question, placement.** The question keeps every word, including the capital "Does". It sits after a colon in a lead sentence: "The question an app team can test is narrower: Does showing structured body progress increase the likelihood that a member returns for another check-in?" The lead gives it the "question a team tests" framing the decision asks for, without "this article", which is a hard ban. The full sentence is 25 words, within the gate. To make the question a standalone sentence, end the lead with a full stop instead ("…is narrower."); this has no gate impact.
2. **A2, "an alternative" instead of "the alternative".** The bullet is an instruction, not a quote block. The sentence reads "…is an alternative to a hardware 3D body scanner". This keeps v1 coordinator decision 7, which replaced "the main alternative" to remove a ranking or market-share reading. The sentence still answers the AEO prompt plainly.
3. **A2, "when it fits" is sentence 2, not sentence 1.** One sentence carrying the phone, the app or website, the hardware alternative, and the home/between-visits condition runs to 35 words. Following editorial-rewrites §1, sentence 1 is the answer (25 words) and sentence 2 is the condition: "It fits members who train at home or between club visits." Both claim comments sit at the end of that two-sentence paragraph.

## Passes on the changed text

- **Hard bans / detector:** CLEAN, with no hard_fails and no house_rule_violations.
- **Terminology guardrails (judgment rows):**
  - No `buyer`, `customer`, `organization`, `we/our`, or cluster labels in the new text.
  - No corrective "X, not Y" or "rather than". The S6 trend-line sentence is a kept v1 sentence, and "does not report usage" is a qualifier.
  - `you` appears only implied, in the CTA imperative, which is a practical block.
  - The new link sentences use meaning-bearing anchors.
- **Abbreviations:** ACSM and BIA are expanded at first use. No new abbreviation.
- **Sentence length:** no new sentence is over 25 words.
- **Landing echoes:** I ran a 7-word n-gram check of every changed paragraph against `workspace/pages/for-connected-and-digital-fitness/published-live-2026-11-13.md` and `published-live-2026-11-19.md`. It found no overlap. Landing copy appears only in the verbatim CTA, the verbatim B2 line, and the map anchors.
- **Self-check** (also in the final.md frontmatter). These still read machine-like after the first apply, and are fixed:
  - The trimmed Adjust paragraph ended on three clipped sentences.
  - "For a single app" was vague.
  - The B3 reason called premium conversion friction.
- **Residual, accepted:**
  - The S6 answer sentence and the phone-scan bullet repeat "train at home or between club visits". A2 requires both.
  - The A3 example's last sentence echoes the frozen S3 line "The product team also decides what members and coaches see."
  - "for fitness apps" appears 4 times: map anchors plus the verbatim CTA label.

## Gate outputs (final.md, after all edits)

`python3 scripts/article_lint.py workspace/seo/articles/ai-body-scanning-for-fitness-refresh/final.md --report` (exit 0):

```
workspace/seo/articles/ai-body-scanning-for-fitness-refresh/final.md
mode: article

[ok  ] hard bans (detect-ai-tells)
         . detector_words: 2411
         . ai_density: 0.0
         . verdict: CLEAN
         . rhythm_variation: 0.45
[ok  ] prose length
         prose words 2086 vs target 1950 (band 1657-2242)
         . prose_words: 2086
         . target: 1950
[ok  ] claim traceability
         . claims_used: ['FIT-ACSM', 'FIT-ADJUST', 'FIT-BODY-PROGRESS', 'FIT-CAPTURE', 'FIT-EVIDENCE-LIMIT', 'FIT-KIDMAN', 'FIT-OUTPUTS-NOTE', 'FIT-PLAN', 'FIT-RTPV', 'FIT-SDK', 'FIT-WHITELABEL', 'FXS-ACCURACY', 'FXS-DELIVERY', 'FXS-IDS', 'FXS-MEDICAL', 'FXS-OUTPUTS', 'FXS-POPULATION', 'FXS-REPEAT', 'FXS-SCOPE', 'FXS-SPEED']
         . claims_known: 24
[ok  ] banned claims
[ok  ] superseded figures
[ok  ] internal links
         . links_total: 14
         . links_distinct: 9
         . asset_urls: 0
         . directions: {'up': 1, 'sideways': 5, 'down': 1, 'trust': 2}
[ok  ] keyword placement
         . keyword: ai body scanning for fitness
         . occurrences: 2
         . h2_count: 9
         . in_first_paragraph: False
[ok  ] abbreviations (M1)
[ok  ] accuracy discipline
         . accuracy_figures_present: True
         . links_to_framework: True
[ok  ] sentence length
         . limits: article (mean <= 16, <= 6% over 25, <= 1 over 35)
         . sentences: 138
         . mean_words: 13.4
         . p90_words: 21
         . over_25: 0 (0.0%)
         . over_35: 0
         . near_duplicate_pairs: none
         . repeated_phrases: ['for fitness apps x4', 'body composition estimates x4', 'the product team x3', 'inside the app x3', 'change between two x3', 'a fitness app x3']

--- shape (descriptive, not gated) ---
prose words 2086 across 9 H2 sections
      173  AI body scanning for fitness: the short answer
      394  Where does a body scan sit in a fitness app's member
      225  How visible progress may affect fitness app retentio
      247  What a phone body scan produces, and what it does no
      220  When should fitness programs use phone scanning inst
      234  What should a fitness app look for in smartphone bod
      176  How to test a body scan with a member cohort
      181  Frequently asked questions
       38  Next steps
  links 14 total, 9 distinct, by direction: {'up': 1, 'sideways': 5, 'down': 1, 'trust': 2}
  primary keyword 'ai body scanning for fitness': 2 occurrences
  claim markers 34: {'FIT-ACSM': 1, 'FIT-ADJUST': 1, 'FIT-BODY-PROGRESS': 2, 'FIT-CAPTURE': 3, 'FIT-EVIDENCE-LIMIT': 2, 'FIT-KIDMAN': 1, 'FIT-OUTPUTS-NOTE': 2, 'FIT-PLAN': 1, 'FIT-RTPV': 1, 'FIT-SDK': 2, 'FIT-WHITELABEL': 2, 'FXS-ACCURACY': 2, 'FXS-DELIVERY': 3, 'FXS-IDS': 1, 'FXS-MEDICAL': 1, 'FXS-OUTPUTS': 3, 'FXS-POPULATION': 1, 'FXS-REPEAT': 2, 'FXS-SCOPE': 1, 'FXS-SPEED': 2}
  approved but uncited: FXS-GDPR, FXS-HIPAA, FXS-LIFECYCLE, FXS-RETENTION

VERDICT: PASS
Mechanics are clean. Judgment is still open: run quality-controller on whether
the argument holds and whether each section earns its place.
```

`python3 brand-assets/style-guides/scripts/detect-ai-tells.py workspace/seo/articles/ai-body-scanning-for-fitness-refresh/final.md --channel article --summary` (exit 0; `--channel article` is the article profile; the default channel also returns CLEAN 0.0):

```
SEO / blog article · en · 2411 words
AI density: 0.0/1000 (budget 6.0) -> low
VERDICT: CLEAN — check the positive side (voice, varied rhythm, a stated boundary) and ship.
```

Landing-link placement, from `article_package._cta_placement` run on the body: links at 13.1% (S2 down link), 15.7% (A1 CTA), 69.0% (S6 contextual link), 99.0% and 99.5% (Next steps, demo `#form`). Early link at 30% or less: yes. Closing link in the last H2: yes.

| Measure | v1 (2026-11-18) | Review 1 round |
|---|---|---|
| Prose words (decision target about 2,000-2,150; band 1,657-2,242) | 2,068 | 2,086 |
| Sentences / mean / p90 | 139 / 13.1 / 20 | 138 / 13.4 / 21 |
| Over 25 / over 35 | 0 / 0 | 0 / 0 |
| Detector | CLEAN 0.0, rhythm 0.44 | CLEAN 0.0, rhythm 0.45 |
| S4 retention (words incl. H2) | 254 | 225 |
| S6 hardware (words incl. H2/H3) | 307 | 220 |
| S8 pilot | 142 | 176 |
| Claim IDs cited | 20 | 20 (FXS-SPEED and FXS-OUTPUTS left S6 but are still cited in S2/S5/S7) |

## Open items for the package

1. **D3 meta description in meta.md and publish-package.md.** Both still carry the v1 description. The publisher replaces it with the verbatim D3 text, which is already in the final.md frontmatter. Per the instruction, I did not touch either file.
2. **Package CTA, position, and length lines are stale.** The `cta_type` and `landing_link` checklist lines describe a "hardware-alternative section" link at 60.0% as a CTA. Current state:
   - 2,086 prose words.
   - CTA 1 is the A1 block at 15.7%. The S2 down link "body scanning for fitness apps" is at 13.1%.
   - The S6 link at 69.0% is a contextual internal link under the new `blog-style-guide.md` §5, not a CTA.
   - CTA 2 is Next steps, landing plus `#form`.
   - The S6 H2 is now "When should fitness programs use phone scanning instead of in-club hardware?".
   The context pack's `internal_link_targets.down` note ("CTA 1 … CTA 2 mid, CTA 3 end") predates the two-CTA rule.
3. **A1 rendering note for the web team.** "Explore FitXpress for fitness apps" may be rendered as a button. The markdown is a plain link on its own line.
4. **B2 rationale vs the live landing (for Vadim / landing owner).** The decisions file says the live landing says "results in under 45 seconds", not "after capture". The 2026-11-19 snapshot hero says "with results in under 45 seconds after capture" (`workspace/pages/for-connected-and-digital-fitness/published-live-2026-11-19.md`, line 11). The article follows canon (`tech-spec.md` line 71, `proof-points.md` line 50), so the article is correct. But the landing hero carries a capture-split variant the canon rules out, and the reviewer cited the landing as her reason. Decide whether the landing hero aligns to "under 45 seconds from the photos to structured results". The article does not change either way.
5. **C1, answer to the reviewer.** "3DLOOK's accuracy claims have not been peer-reviewed or externally validated through a third-party clinical study." is canon VERBATIM (`accuracy-formulations.md` §1.9) and is unchanged. If newer validation documentation exists, the canon changes first (Vadim), then the article.
6. **D2 meta title.** v1 is kept: "AI Body Scanning for Fitness: Where a Phone Scan Fits". The reviewer's title contains the landing's primary keyword (landing-map rule 3). If a brand suffix is wanted, the publisher offers one variant of 60 characters or less without the keyword, for example "AI Body Scanning for Fitness: Member Journey | 3DLOOK".
7. **S4 length against the decision's baseline.** The decisions file gives v1 S4 as "about 330" words. By `article_lint` it was 254 (raw `wc` 267). The mandated content alone is about 200 words: Adjust with qualifiers, Kidman with qualifier, two-sentence ACSM, two link sentences, the question, and the two kept sentences. The section now runs 225 with the H2. If it should be tighter, the next cut is "Early in a program, weight can change slowly while body measurements shift." because the intro already shows that scene. The weight-loss link sentence would then need its own antecedent.
8. **Resolved in the QC fix pass below (fix 3, coordinator override).** Original note: **Repeat across a frozen section (for QC awareness).** The A3 example ends "The app determines which results to show and how to use them." The S3 closing paragraph (section E, frozen) says "The product team also decides what members and coaches see." If QC flags it, the fix in a later round is to cut the S3 sentence, not the verbatim example.
9. **Demo anchor in the landing map.** The Hub 1 row says "Demo button now: same page", which by rule 4 implies `#demo`. The live landing anchor is `#form` (snapshot 2026-11-13), and Next steps uses `#form` (unchanged). Re-check `#form` at publish, as v1 already noted. The map owner may want the Hub 1 row to state `#form`, as the insurance row does.
10. **Carried from v1 (decision F):**
    - Byline (Assel Sekerova vs the live Dana Vioreanu).
    - Adjust vendor-blog source (terminology §1.3).
    - ACSM link swap from Newswise to acsm.org if it resolves at publish.
    - Illustrations for Kristina (the cover and Image 1 concepts are unchanged; no concept refers to the hardware section).
    - 3 post-publish inbound-link edits: hub `ai-in-fitness-industry`, `glp-1-muscle-loss-fitness-apps`, and the anchor on `remote-body-measurement-online-fitness-coaching`.
    - The hub's "seven in ten users… stop using a fitness app" framing vs this page's Kidman wording.
    - Two framework links in S5 (deliberate).
    - DXA first expanded in S7.
    - The pilot-design wording vs the landing's pilot step 2. Still compatible, but B3 now adds secondary metrics the landing also lists. The wording is the article's own.
11. **FAQPage JSON-LD** is unchanged: the FAQ questions did not change.

## QC fix pass 2026-11-23 (QC 18/20)

QC report: `workspace/_quality/seo/2026-11-23-ai-body-scanning-for-fitness-refresh-review-1.md`. The coordinator agreed with it, and I applied its five fixes exactly as given. Fixes 2 and 3 edit section-E text under the coordinator's override, because the A3 example had re-created the repeats. The A3 example is unchanged.

1. S6 opening: "It fits members who train at home or between club visits." became "It fits members who train away from the club, at home or between visits." The bullet "Members train at home or between club visits." is unchanged.
2. S3 Coach review: the lead "Before planning the next training block," is cut. The sentence is now "The coach can check the change between two of the member's scans." The rest of the paragraph is unchanged.
3. S3 closing paragraph: "The product team also decides what members and coaches see." is deleted. FIT-WHITELABEL stays.
4. S4: "A product team can test a narrower question." The question follows verbatim, as a standalone sentence.
5. S6 last sentence: "Integration details and plans are on the FitXpress page for a [mobile alternative to a gym body scanner](landing)." The anchor is unchanged.

Gates after the fixes:
- `article_lint.py --report`: PASS, all 10 gates. 2,074 prose words. 138 sentences, mean 13.3, p90 21, 0 over 25, 0 over 35. near_duplicate_pairs none.
- `detect-ai-tells.py --channel article --summary`: CLEAN, density 0.0, rhythm 0.45.
- Landing links at 13.2% / 15.8% (CTA) / 68.9% / 99.0% / 99.5%.
- An internal 7-gram check leaves only the two accepted repeats: the intro and the A2-prescribed S6 phrase "a guided scan on the member's own phone", and the canonical output phrase in S2 and S7.
- S6 is now 225 words with headings against A2's 180-220. Fix 1 adds 3 words. This is the coordinator's wording, and the flag is in meta.md open item 10.

Package: meta.md open item 9 (S3 repeat) is marked resolved. The cta_type and landing_link positions are refreshed to 15.8 / 13.2 / 68.9. Open item 10 now also carries the S6 length. `python3 scripts/article_package.py assemble ai-body-scanning-for-fitness-refresh` rebuilt publish-package.md: mechanics 19/19, judgment 8/8, STOP-rule OK, 2,074 words.

## Inputs

I read `review-1-decisions.md` in full, twice (it changed mid-round), along with `review-1.md`, `final.md` / `v1/final.md`, `v1/editor-report.md`, and the context pack (claim texts for FXS-SPEED, FIT-CAPTURE, FIT-SDK, FIT-ADJUST, FIT-KIDMAN, and FIT-ACSM). I also read:
- `hard-bans-card.md`
- `terminology-guardrails.md` Part 1
- `editorial-rewrites.md` §1-8
- `landing-map.md`
- `blog-style-guide.md` §5
- `tech-spec.md` line 71 and `proof-points.md` line 50
- the landing snapshots of 2026-11-13 and 2026-11-19
- `refresh-gap-analysis.md` around line 103
`plan.md` was background only and was not changed. Untouched: meta.md, publish-package.md, plan.md, and v1/. Nothing was committed.
