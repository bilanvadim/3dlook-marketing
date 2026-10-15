# Competitive Landscape — Quick Reference

For full positioning, see `brand-assets/product-info/competitors.md` (last verified 2026-10-15). This file is
the asset / screenshot reference for visual / content agents.

## Direct competitors

### Prism Labs
- **Website:** https://www.prismlabs.tech/ (confirmed 2026-10-15)
- **Their messaging:** body composition beyond BMI for digital health at scale; "DEXA precision using a mobile device" (their wording for DXA)
- **Their look:** realistic textured 3D avatars, "Future Me" before/after shape predictions
- **What we DON'T copy:** the avatar-first, clinical body-composition narrative; we lead with verified, decision-ready outputs
- **Screenshots needed in `competitors/screenshots/prism/`:** homepage, pricing page, sample LinkedIn post

### Size Stream
- **Website:** https://www.sizestream.com/ (confirmed 2026-10-15); consumer app MeThreeSixty
- **Their messaging:** body data platform with "DXA-level accuracy"; Size Stream Health for pharma, telehealth and research (since July 2026); "no photos uploaded"
- **What we DON'T copy:** booth / hardware-centric framing; we are pure smartphone
- **Screenshots needed in `competitors/screenshots/sizestream/`:** homepage, Size Stream Health page, MeThreeSixty store listing

### Fit:match
- **Website:** https://www.fitmatch.ai/ (confirmed 2026-10-15); app QuadraScan
- **Their messaging:** "digital twin" body intelligence across sports, health and retail; 2026 emphasis on youth sports
- **What we DON'T copy:** sports-scouting framing and "DEXA-validated" claims without published data
- **Screenshots needed in `competitors/screenshots/fitmatch/`:** homepage, SDK page

### Bodygram
- **Website:** https://bodygram.com (March 2026 review, not re-verified)
- **Their messaging:** body measurement API across retail, uniforms, health and insurance
- **What we DON'T copy:** SMB-trainer aesthetic — we go enterprise
- **Screenshots needed in `competitors/screenshots/bodygram/`:** homepage, developer page

### Mirrorsize
- **Website:** https://www.mirrorsize.com/ (confirmed 2026-10-15)
- **Their messaging:** "World's Best Precision" for apparel, uniforms and e-commerce sizing
- **What we DON'T copy:** superlative accuracy badges without data
- **Screenshots needed in `competitors/screenshots/mirrorsize/`:** homepage, pricing page

### Bodd
- **Website:** https://www.bodd.io/ (confirmed 2026-10-15)
- **Their messaging:** "Real 3D scans. Real data. No AI guesses." Booth scanner for uniforms, pharmacies and wellness
- **What we DON'T copy:** hardware / kiosk framing — we are pure smartphone
- **Screenshots needed in `competitors/screenshots/bodd/`:** homepage, wellness / pharmacy page

## Adjacent (not direct, useful for context)

- **Withings** — smart scales (different category — they need device)
- **InBody** — BIA / hardware (clinical-grade, in-clinic)
- **DXA scan providers** — gold standard (slow, expensive)
- **MyFitnessPal** — self-tracking (no verification)

## Long-term risk (no specific company yet)

- **Apple/Google native body scanning primitives** — future commoditization risk. Watch for:
  - Apple Vision API extensions
  - Google MediaPipe body extensions
  - Health platform body scanning features (HealthKit, Google Fit)

## How agents use this

- `hypothesis-generator` reads `competitors.md` (full doc) to avoid hypothesis where competitor is dominant
- `seo-outline-builder` reads to identify competitive gaps for content
- `message-sequencer` NEVER names competitors in cold outbound
- `response-classifier` uses to pattern-match if prospect mentions competitor
- `visual-brief` looks at `screenshots/{competitor}/` for what NOT to copy stylistically
