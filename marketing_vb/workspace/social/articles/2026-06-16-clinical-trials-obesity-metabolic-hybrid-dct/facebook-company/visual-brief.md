# Visual Brief — facebook-company — Clinical Trials (Obesity/Metabolic Hybrid-DCT)

## Source
- Post text: `workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/facebook-company/post.md`
- Article: `workspace/seo/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/v3/publish-package.md` (Section 4, OG Image Brief)
- Product: fitxpress
- Status: text QC-passed (19/20), visual brief drafted 2026-07-05

## Note: Figma exports unavailable

This brief is built on secondary/approximate data, not confirmed brand assets. Missing at time of writing:
- `brand-assets/past-posts/_figma-exports/` does not exist — no blog-banner or website-page exports to use as a literal style reference.
- No logo files anywhere in `brand-assets/` (`brand-assets/logos/` does not exist).
- No confirmed brand book — `colors.md` and `fonts.md` are both explicitly marked "approximate — confirm with Vadim/Figma."
- `brand-assets/past-posts/facebook-company/` exists but is empty — no past visuals for this profile to check format/composition precedent against.

Per Vadim's decision (2026-07-05), proceeding on best-available data rather than blocking. **Designer/Vadim should cross-check the final Canva execution against the two live Figma files before publish:**
- Blog banners: https://www.figma.com/design/zWV1W9fs7cbp7Jc0pVDTDX/Blog-banners
- Website pages: https://www.figma.com/design/yQlvzqLeCJAAQjaHSKIduC/3DLOOK-website

Specifically verify: exact 3DLOOK Blue HEX (brief below uses `#2962FF`, marked approximate), the dark teal-blue tone referenced for the bariatric/insurance-underwriting sibling banners (not in `colors.md` — sample from Figma), and the logo/wordmark lockup to badge onto the image.

## Format decision
**Recommended:** text + photo (single image) — per the post's own Design tip, not overridden.
**Why:** The post's angle is a plain-language accessibility play on the article's variability problem, closing on an engagement question ("consistency or speed?"). A single, simple image supports that without competing for attention with a carousel sequence or a dense infographic — matches `facebook-company`'s tone in `social-profiles-config.md` ("Accessible and community-oriented... explain without jargon") and its "Article summary with key takeaways" content type. The Design tip's own adaptation logic (crop tight on the guided-scan phone element, drop the multi-site dot-map and timestamp icon) is correct for this platform: it reduces "clinical-trial infrastructure" to one human, legible "two photos, done" moment that a general Facebook audience can parse in a scroll.
**Dimensions:** 1200×630 px (Facebook link/feed image, matches the article's own OG dimensions per publish-package.md Section 4). Export a 1600×900 master for repurposing.

## Visual concept
**Big idea (1 sentence):** Two photos, one guided scan, done — the phone-in-hand moment that stands in for "consistent measurement," with no clinical apparatus around it.
**Mood:** human, calm, approachable — the same dark teal-blue palette as the article banner, but the composition should read as a simple everyday moment, not trial infrastructure.

## Composition
- Full-bleed dark teal-blue background (see Colors below) — matches the source article banner's tone, not the brighter consumer-fitness FX banners.
- Center (dominant): a smartphone in guided-scan capture mode — pose-validation silhouette or bounding-box guide framing a person's outline on the phone screen, representing the two-photo FitXpress capture. Crop tight on this element only; no multi-site dot-map, no timestamp/clipboard icon, no other supporting motifs from the article's OG brief.
- Generous negative space around the phone — let it sit as the single visual anchor, not surrounded by icons or clutter.
- Text block: positioned beside or below the phone (left-aligned if phone is right-of-center, or below if phone is centered) — short headline + optional one-line sub, not overlapping the phone illustration.
- Bottom-right: 3DLOOK or FitXpress wordmark badge, small, consistent with other content-hub banners per the source article's OG brief. No logo file currently exists in `brand-assets/` — designer to source current lockup from the Figma website file or confirm with Vadim before placing.

## Text on visual
- Headline: **"Two photos. One consistent measurement."**
- Sub (optional, smaller): **"Every scan, same way, every time."**
- Footer/badge: 3DLOOK or FitXpress wordmark only.

Note: keep the on-image text short — the post caption already carries the full explanation and the discussion-question CTA. The image's job is to make the "two photos, done" moment legible at a glance, not to restate the post.

## Colors
- Background: 3DLOOK Black/near-black `#0A0A0A`–`#000000`, or the dark teal-blue tone referenced in the article's OG brief for the bariatric/insurance-underwriting sibling banners (exact teal HEX not in `colors.md` — designer to sample from Figma blog-banners file per the Note above; do not invent a new teal).
- Primary accent (phone-screen guide lines, headline text): 3DLOOK Blue `#2962FF` (marked approximate in `colors.md` — confirm before final export).
- Body/sub text: White `#FFFFFF` at high opacity, or Light Gray `#F5F5F7` for the secondary line.
- Do not introduce Red Alert `#FF3B30` or Green Success `#34C759` — no status/verification connotation belongs in this image.

## Typography
- Headline: Inter Bold or Black (per `fonts.md`) — large, tight tracking.
- Sub: Inter Regular or Medium, ~40-50% the headline size.
- Max 2 font weights on the image; no third typeface.

## Reference / inspiration
- No past visuals exist for `facebook-company` (folder empty) or in `_figma-exports/` (missing) — there is no direct prior-post precedent to point to. Closest available reference is the source article's own OG Image Brief (Section 4 of `publish-package.md`), specifically the "smartphone in guided-scan capture mode" element, which this image isolates and simplifies.
- Undesirable reference (explicit avoid, per the article brief and compliance guardrails): any DEXA/imaging-equipment iconography, any patient face or realistic body close-up, any real map or country outline, any specific EDC/CTMS/eConsent product logo, any stethoscope-with-checkmark icon.

## What NOT to do
- No stock-photo "people in office / clinicians shaking hands."
- No generic AI-illustration purple-pink gradients.
- No Font Awesome-style icons stacked on top of text.
- No patient face or realistic body imagery — the guided-scan element should stay an abstract pose-validation silhouette or bounding-box guide, never a depicted person or photo-real body.
- No multi-site dot-map, no timestamp/clipboard icon — both explicitly dropped per the post's Design tip; do not reintroduce "clinical-trial infrastructure" cues into this crop.
- No DEXA/imaging-equipment iconography.
- Don't crowd the phone element with extra supporting icons — this is a single, simple moment, not an infographic.

## Designer checklist
- [ ] Logo/wordmark present (bottom-right) — confirm current lockup file with Vadim first (none found in `brand-assets/`)
- [ ] Font is Inter (Bold/Black headline, Regular/Medium sub) — no substitutions
- [ ] Colors drawn only from `brand-assets/color-palette/colors.md` (blue/black/white + gray) — flag if a teal outside this palette is used, pending Figma confirmation
- [ ] Text contrast ≥ 4.5:1
- [ ] No purple-pink gradient, no stock photography, no DEXA/clinical-equipment iconography, no patient/body imagery
- [ ] No multi-site dot-map or timestamp/clipboard icon present (dropped per Design tip)
- [ ] Cross-checked against the two Figma reference files (Blog banners, Website pages) before final export — see Note above
- [ ] Exported at 1200×630 with a 1600×900 master saved
