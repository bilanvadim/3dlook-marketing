# Nick · FitXpress retention post (one-off, 2026-11-19)

Hlib Hlazovyi wrote a LinkedIn post for Nick (`linkedin-nick`) plus a banner and sent them to Vadim in a Slack DM on 2026-11-19
(«Сделал для Ника такой пост, что думаешь?»). The post supports the US connected-fitness outbound campaign that runs from
Nick's profile (`workspace/outbound/campaigns/2026-11-19-us-connected-fitness`). People who accept an invite will see it.

Status: review, rewrite and fixed visuals were sent to Hlib in the same DM on 2026-11-19. Hlib publishes from Nick's account.

## Files

| Path | What |
|---|---|
| `post/hlib-draft-v1.md` | Hlib's original text (204 words) |
| `post/post.md` | Rewrite: 153 words with the link, post-lint clean (only the one-off `design_tip` / `cta` warnings) |
| `visual/original-hlib-1800x942.png` | Hlib's banner as sent |
| `visual/fitxpress-post-4x5-1080x1350.png` | **Feed version** (use this one) |
| `visual/fitxpress-post-1800x942.png` | Same fixes, original 1.91:1 layout (backup) |
| `visual/tools/` | `build.sh` rebuilds both PNGs from the original byte for byte: `clean.py` erases the old text and logo, `compose.py` draws the new text, `compose45.py` lays out the 4:5 version |

## Text review (what changed and why)

- 204 words → 153. The house ceiling for the five personal profiles is 170 (`brand-assets/linkedin-post-prompts.md`).
- One 38-word sentence held both retention stats. Only the Adjust day-1/day-30 pair is kept (24% → 7%, global 2022 data,
  verified in `workspace/pages/for-connected-and-digital-fitness/fact-sheet.md`).
- The hook is now a short claim, and the post closes on a question the reader answers with their own numbers. The old
  ending was a sales offer ("Happy to share how teams test this in a cohort pilot").
- Product facts follow canon: 80+ measurements, body composition *estimates*, "under 45 seconds", "isn't a medical device".
- **Link:** the landing page goes as the last line of the body, not the first comment (Vadim, 2026-11-19). The evidence
  that LinkedIn penalises links is mixed, and so is the evidence that the first-comment trick helps.

## Visual fixes

- Logo: the light-blue symbol is replaced by the white horizontal lockup (`brand-assets/logos/3dlook-logo-white.svg`).
  The guideline allows a black or white logo only.
- Phone headline: "Instant, accurate, mobile" → "Scan, measure, compare". An unconditioned "accurate" is out, and timing
  has one public form, "under 45 seconds".
- "Your transformation · 10 months" (biceps +1.5 in, chest +2 in, waist −1 in) → "Your progress · 3 months":
  Weight −0.6 lb, Waist −1.0 in, Body fat −2%. The card now tells the post's story: the scale barely moves while the
  waist and body fat do.
- Font: the banner is set in Jost, so the new text is Jost too. DESIGN.md asks for Satoshi on social, but mixing two
  typefaces in one image would read worse. A redesign from scratch would use Satoshi.

## Numbers: one consistent US profile

Persona: woman, 5'6" (66 in), 140 lb, three months of training (recomposition).

| Field | Was | Now | Check |
|---|---|---|---|
| BMI | 26.3 | 22.6 | 703 × 140 / 66² = 22.6. The old value is overweight, which the photo doesn't show |
| BMR | 1800 Cal | 1,420 Cal | Katch-McArdle at 23% fat: lean mass 48.9 kg → 370 + 21.6 × 48.9 ≈ 1,426. Mifflin-St Jeor at age 30 gives ≈ 1,371 |
| Current Body Fat | 25% | 23% | The chart keeps falling after the May tooltip (25%), so "current" must be lower. The tooltip stays |
| Progress, 3 months | — | −0.6 lb · −1.0 in waist · −2% fat | Fat mass 35.2 → 32.2 lb, lean mass +2.4 lb: plausible for a beginner over 12 weeks |

Units are US throughout: lb, in, Cal, and a comma as the thousands separator. BMI has no unit.

Left unchanged: the banner subtitle ("next-level fitness progress tracking") and the phone buttons. "Find out my weight"
is Smart Scales, which is public wording (`brand-assets/product-info/tech-spec.md`).
