# Visual Brief — linkedin-company — Clinical Trials (Obesity/Metabolic Hybrid-DCT)

## Source
- Post text: `workspace/social/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/linkedin-company/post.md`
- Article: `workspace/seo/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/v3/publish-package.md` (Section 4, OG Image Brief)
- Article comparison table (grounding for the 3 rows): `workspace/seo/articles/2026-06-16-clinical-trials-obesity-metabolic-hybrid-dct/v3/draft-final.md`, "Scan-based capture vs manual anthropometric measurement" section
- Product: fitxpress
- Status: text QC-passed (19/20), visual brief drafted 2026-07-05

## Note: Figma exports unavailable

This brief is built on secondary/approximate data, not confirmed brand assets. Missing at time of writing:
- `brand-assets/past-posts/_figma-exports/` does not exist — no blog-banner or website-page exports to use as a literal style reference.
- No logo files anywhere in `brand-assets/` (`brand-assets/logos/` does not exist).
- No confirmed brand book — `colors.md` and `fonts.md` are both explicitly marked "approximate — confirm with Vadim/Figma."
- `brand-assets/past-posts/linkedin-company/` has 15 past posts, but all are text-only `.md` files — no PNG/JPG visuals in the folder to check past infographic composition or comparison-table styling against.

Per Vadim's decision (2026-07-05), proceeding on best-available data rather than blocking. **Designer/Vadim should cross-check the final Canva execution against the two live Figma files before publish:**
- Blog banners: https://www.figma.com/design/zWV1W9fs7cbp7Jc0pVDTDX/Blog-banners
- Website pages: https://www.figma.com/design/yQlvzqLeCJAAQjaHSKIduC/3DLOOK-website

Specifically verify: exact 3DLOOK Blue HEX (brief below uses `#2962FF`, marked approximate), the dark teal-blue tone referenced for the bariatric/insurance-underwriting sibling banners (not in `colors.md` — sample from Figma), and the logo/wordmark lockup to badge into the corner. This graphic is a comparison schema, not a data table, so also confirm with the designer that no literal gridlines/table-cell borders creep in during Canva execution — see Composition below.

## Format decision
**Recommended:** infographic (single static image, 3-row comparison schema) — per the post's own Design tip, not overridden.
**Why:** LinkedIn-company's audience (compliance-literate CRO/sponsor operations readers) responds to a structured, scannable argument, and the post's Design tip is explicit: rebuild the article OG banner's three visual elements (multi-site motif, guided-scan phone, timestamp/structured-record icon) as a compact 3-row comparison mirroring the article's "manual vs FitXpress" table, using icons rather than a literal data table. A single infographic (not a carousel) suits LinkedIn's native single-image post rendering and keeps the "manual → FitXpress" contrast visible in one glance without requiring a swipe.
**Dimensions:** 1200×1200 px (LinkedIn feed square). Export a 1600×1600 master for reuse/repurposing (e.g. as a content-hub supporting image) without re-doing the design.

## Visual concept
**Big idea (1 sentence):** Three operational dimensions — site consistency, coordinator workload, remote use — flip from "depends on the site" (manual) to "standardized" (FitXpress), read left-to-right in one glance.
**Mood:** data-driven, serious, operational — "trial infrastructure," not consumer fitness app. Same register as the article: precise, hedged, non-clinical.

## Composition
- Full-bleed dark teal-blue background (see Colors below) — flat or very subtle gradient within the brand palette, no purple-pink AI-style gradient.
- Two-column schema, NOT a literal ruled data table (no gridlines, no table-cell borders, no spreadsheet look) — this should read as a designed comparison graphic:
  - Column header left: "Manual measurement" (muted/secondary treatment — Mid Gray or lower-opacity white)
  - Column header right: "FitXpress" (primary treatment — 3DLOOK Blue accent, visually "wins" the comparison)
  - Three horizontal rows below the headers, each row = one dimension with a small abstract icon + short label pair on each side:
    - **Row 1 — Site consistency:** left icon = the article's multi-site motif compressed to 2-3 small abstract pin/dot marks scattered unevenly (suggesting drift/inconsistency); right icon = the same marks aligned in a single neat row (suggesting standardization)
    - **Row 2 — Coordinator workload:** left icon = a simple abstract "manual effort" mark (e.g., a hand/pencil-adjacent abstract glyph or a small stack of marks suggesting manual notes — NOT a literal clipboard-with-checkmark per the article's avoid list); right icon = the article's guided-scan phone element (pose-validation silhouette or bounding-box guide) at small scale
    - **Row 3 — Remote use:** left icon = a small "limited/blocked" abstract glyph (e.g., a dimmed or partial version of a location/connectivity mark); right icon = the article's timestamp/structured-record icon (small rows of abstract marks, not a literal form)
  - Thin horizontal divider rules between rows (hairline, low-opacity white or Mid Gray) are acceptable for readability — these read as row separators within a designed graphic, not as a spreadsheet grid; do not add vertical column-dividing lines.
- Bottom-right: 3DLOOK or FitXpress wordmark badge, small, consistent with other content-hub visuals per the source article's brief. No logo file currently in `brand-assets/` — designer to source current lockup from the Figma website file or confirm with Vadim before placing.
- Generous margins around the 3-row block; do not let icons or labels crowd the edges of the 1200×1200 canvas.

## Text on visual
- Title (top, above the two columns): **"Manual measurement vs. FitXpress"**
- Column headers: **"Manual"** / **"FitXpress"**
- Row labels (left-aligned, small, sits between the two icon columns or directly above each row): **"Site consistency"** / **"Coordinator workload"** / **"Remote use"**
- Footer/badge: 3DLOOK or FitXpress wordmark only (no additional footer line needed at this size).

Note: keep row labels to the 2-3 word form above — do not pull the fuller table-cell phrasing from `draft-final.md` (e.g. "Depends on staff technique and local execution") onto the graphic. The post caption already carries the full argument; the image should carry only the schema and the row labels, sized to be legible at LinkedIn feed thumbnail size.

## Colors
- Background: 3DLOOK Black/near-black `#0A0A0A`–`#000000`, or the dark teal-blue tone referenced in the article's OG brief for the bariatric/insurance-underwriting sibling banners (exact teal HEX not in `colors.md` — designer to sample from Figma blog-banners file per the Note above; do not invent a new teal).
- Primary accent (FitXpress column header, right-column icons, headline text): 3DLOOK Blue `#2962FF` (marked approximate in `colors.md` — confirm before final export).
- Manual column / left-column icons: Mid Gray `#6B7280` (approximate) or White at reduced opacity — deliberately more muted than the FitXpress column so the eye reads FitXpress as the "resolved" state.
- Body/label text: White `#FFFFFF` at high opacity, or Light Gray `#F5F5F7` for secondary labels.
- Do not introduce Red Alert `#FF3B30` or Green Success `#34C759` — the manual-vs-FitXpress contrast should be carried by the gray-vs-blue treatment described above, not by red/green pass-fail coloring (which would overstate a status/verification claim the article doesn't make).

## Typography
- Title: Inter Bold or Black (per `fonts.md`) — large, tight tracking.
- Column headers ("Manual" / "FitXpress"): Inter Bold, mid-size, consistent size across both columns (only the color should differ, not the weight/size — avoid implying one column is "less real" than the other).
- Row labels: Inter Medium, smaller than column headers.
- Max 2 font weights on the graphic; no third typeface.

## Reference / inspiration
- No past visuals exist for `linkedin-company` in image form (`brand-assets/past-posts/linkedin-company/` has 15 past text posts, no PNG/JPG) and `_figma-exports/` is missing — there is no direct prior-post visual precedent to point to. Closest available reference is the source article's own OG Image Brief (Section 4 of `publish-package.md`) and its full comparison table (`draft-final.md`, "Scan-based capture vs manual anthropometric measurement" — 6 rows total; this graphic surfaces 3 of the 6: Site consistency, Coordinator workload, Remote use, per the post's Design tip).
- Undesirable reference (explicit avoid, per the article brief): any DEXA/imaging-equipment iconography, any patient face/body close-up, any real map or country outline, any specific EDC/CTMS/eConsent product logo, any stethoscope-with-checkmark icon, any literal spreadsheet/data-table look (this is a schema, not a dense chart, per the post's own Adaptation note).

## What NOT to do
- No stock-photo "people in office / clinicians shaking hands."
- No generic AI-illustration purple-pink gradients.
- No Font Awesome-style icons stacked on top of text.
- No patient imagery or body close-ups (this is a clinical-operations claim, not a consumer body-scan visual).
- No literal map/geography for the site-consistency row icon — keep it abstract dot/pin marks, not a real map.
- No DEXA/imaging-equipment iconography anywhere on the graphic.
- No vertical gridlines or spreadsheet/table-cell borders — this must read as a designed comparison schema, not a dense data table (per the post's Adaptation note).
- No red/green pass-fail coloring on the two columns — use the gray (manual) vs. blue (FitXpress) contrast specified above instead.
- Don't pull full table-cell sentences from the article onto the graphic — row labels only, 2-3 words each.

## Designer checklist
- [ ] Logo/wordmark present (bottom-right) — confirm current lockup file with Vadim first (none found in `brand-assets/`)
- [ ] Font is Inter (Bold/Black title and column headers, Medium row labels) — no substitutions
- [ ] Colors drawn only from `brand-assets/color-palette/colors.md` (blue/black/white/gray) — flag if a teal outside this palette is used, pending Figma confirmation
- [ ] Text contrast ≥ 4.5:1 for all labels
- [ ] No purple-pink gradient, no stock photography, no DEXA/clinical-equipment iconography, no patient imagery, no spreadsheet/table-grid look
- [ ] All 3 rows present and correctly mapped: Site consistency, Coordinator workload, Remote use (in this order, matching the article table's row order)
- [ ] Cross-checked against the two Figma reference files (Blog banners, Website pages) before final export — see Note above
- [ ] Exported at 1200×1200 (feed) with a 1600×1600 master saved
