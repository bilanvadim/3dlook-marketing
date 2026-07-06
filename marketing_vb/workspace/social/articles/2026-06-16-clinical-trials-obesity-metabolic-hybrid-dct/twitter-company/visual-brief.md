# Visual Brief — twitter-company — Clinical Trials (Obesity/Metabolic Hybrid-DCT)

## Source
- Post text: `workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/twitter-company/post.md`
- Article: `workspace/seo/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/v3/publish-package.md` (Section 4, OG Image Brief)
- Product: fitxpress
- Status: text QC-passed (19/20), visual brief drafted 2026-07-05

## Note: Figma exports unavailable

This brief is built on secondary/approximate data, not confirmed brand assets. Missing at time of writing:
- `brand-assets/past-posts/_figma-exports/` does not exist — no blog-banner or website-page exports to use as a literal style reference.
- No logo files anywhere in `brand-assets/` (`brand-assets/logos/` does not exist).
- No confirmed brand book — `colors.md` and `fonts.md` are both explicitly marked "approximate — confirm with Vadim/Figma."
- `brand-assets/past-posts/twitter-company/` exists but is empty — no past visuals for this profile to check format/composition precedent against.

Per Vadim's decision (2026-07-05), proceeding on best-available data rather than blocking. **Designer/Vadim should cross-check the final Canva execution against the two live Figma files before publish:**
- Blog banners: https://www.figma.com/design/zWV1W9fs7cbp7Jc0pVDTDX/Blog-banners
- Website pages: https://www.figma.com/design/yQlvzqLeCJAAQjaHSKIduC/3DLOOK-website

Specifically verify: exact 3DLOOK Blue HEX (brief below uses `#2962FF`, marked approximate), logo file/lockup to use in the badge corner, and whether the dark teal-blue tone used on the bariatric/insurance-underwriting blog banners (referenced in the source article's OG brief) matches what's specified here.

## Format decision
**Recommended:** screenshot (stat/text card) — per the post's own Design tip, not overridden.
**Why:** Twitter/X rewards a single sharp, legible claim over dense composition — the post-drafter's design tip already correctly identifies this: strip the multi-site dot-map and phone-capture illustration from the article's OG banner (those need room to breathe at 1200×630 hero size and would compress badly in-feed) and isolate the one line that carries the tweet's argument. This matches `twitter-company`'s content_types in `social-profiles-config.md` ("One striking stat or claim from the article") and its punchy, data-first tone.
**Dimensions:** 1200×675 px (16:9, standard X/Twitter in-feed image crop). Export a 1600×900 master so it can be reused/cropped for other placements without re-doing the design.

## Visual concept
**Big idea (1 sentence):** Trials don't fail on the measurement — they fail on the workflow around it — landing as one bold stat card, no clinical imagery.
**Mood:** data-driven, serious, operational — "trial infrastructure," not consumer fitness app.

## Composition
- Full-bleed dark teal-blue background (see Colors below) — flat or very subtle gradient within the brand palette, no purple-pink AI-style gradient.
- Center: the headline claim set as the dominant visual element (see Text on visual) — this replaces the article banner's phone-illustration + dot-map with typography as the hero.
- Upper-left or lower-left, small and secondary: the structured-record icon from the article's OG brief — rows of small abstract marks/ticks (NOT a literal form, NOT a clipboard-with-checkmark, NOT a stethoscope) — signaling "time-stamped documentation" without competing with the headline.
- Bottom-right: 3DLOOK or FitXpress wordmark badge, small, consistent with other content-hub banners per the source article's brief. (No logo file currently in `brand-assets/` — designer to source current lockup from the Figma website file or ask Vadim before placing.)
- Generous negative space — do not crowd the card; this is a single-claim card, not an infographic.

## Text on visual
- Headline (dominant): **"The measurement rarely fails. The workflow does."**
- Sub (smaller, below headline): **"FitXpress standardizes capture in under 45 seconds — time-stamped, every site."**
- Footer/badge: 3DLOOK or FitXpress wordmark only (no separate footer line needed at this size).

Note: keep the headline as the two-sentence contrast pair above rather than restating the full tweet body — the tweet text itself carries the "12-month drift" detail; the card should carry only the sharpest fragment so it reads in under a second.

## Colors
- Background: 3DLOOK Black/near-black `#0A0A0A`–`#000000`, or the dark teal-blue tone referenced in the article's OG brief for the bariatric/insurance-underwriting sibling banners (exact teal HEX not in `colors.md` — designer to sample from Figma blog-banners file per the Note above; do not invent a new teal).
- Primary accent (headline text, icon strokes): 3DLOOK Blue `#2962FF` (marked approximate in `colors.md` — confirm before final export).
- Body/sub text: White `#FFFFFF` at high opacity, or Light Gray `#F5F5F7` for the secondary line.
- Do not introduce Red Alert `#FF3B30` or Green Success `#34C759` — no status/verification connotation belongs in this card.

## Typography
- Headline: Inter Bold or Black (per `fonts.md`) — large, tight tracking, sized to dominate the card.
- Sub: Inter Regular or Medium, ~40-50% the headline size.
- Numeric ("45 seconds"): Inter with tabular nums if set apart as a standalone stat; otherwise inline within the sub line is fine at this length.
- Max 2 font weights on the card; no third typeface.

## Reference / inspiration
- No past visuals exist for `twitter-company` (folder empty) or in `_figma-exports/` (missing) — there is no direct prior-post precedent to point to. Closest available reference is the source article's own OG Image Brief (Section 4 of `publish-package.md`), which this card deliberately simplifies down from.
- Undesirable reference (explicit avoid, per the article brief): any DEXA/imaging-equipment iconography, any patient face/body close-up, any real map or country outline, any specific EDC/CTMS/eConsent product logo, any stethoscope-with-checkmark icon.

## What NOT to do
- No stock-photo "people in office / clinicians shaking hands."
- No generic AI-illustration purple-pink gradients.
- No Font Awesome-style icons stacked on top of text.
- No patient imagery or body close-ups (this is a clinical-operations claim, not a consumer body-scan visual).
- No literal map/geography — the "multi-site" idea should stay abstract if used at all (and per the Design tip, it's dropped entirely from this card).
- Don't restate the full tweet copy on the card — one sharp headline + one sub line only.

## Designer checklist
- [ ] Logo/wordmark present (bottom-right) — confirm current lockup file with Vadim first (none found in `brand-assets/`)
- [ ] Font is Inter (Bold/Black headline, Regular/Medium sub) — no substitutions
- [ ] Colors drawn only from `brand-assets/color-palette/colors.md` (blue/black/white + gray) — flag if a teal outside this palette is used, pending Figma confirmation
- [ ] Text contrast ≥ 4.5:1
- [ ] No purple-pink gradient, no stock photography, no DEXA/clinical-equipment iconography, no patient imagery
- [ ] Cross-checked against the two Figma reference files (Blog banners, Website pages) before final export — see Note above
- [ ] Exported at 1200×675 (in-feed) with a 1600×900 master saved
