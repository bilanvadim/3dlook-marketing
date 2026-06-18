# Competitive Landscape — Quick Reference

For full positioning, see `brand-assets/product-info/competitors.md`. This file is the asset / screenshot reference for visual / content agents.

## Direct competitors

### Prism Labs
- **Website:** https://prismlabs.tech (approximate — confirm)
- **Their messaging:** body composition for digital health at scale
- **What we DON'T copy:** their over-emphasis on visceral fat / clinical body comp narrative — we have broader positioning
- **Screenshots needed in `competitors/screenshots/prism/`:** homepage, key product page, sample LinkedIn post

### Bodygram
- **Website:** https://bodygram.com
- **Their messaging:** body measurement for fitness pros
- **What we DON'T copy:** SMB-trainer aesthetic — we go enterprise
- **Screenshots needed in `competitors/screenshots/bodygram/`:** same

### Size Stream
- **Website:** https://sizestream.com (approximate — confirm)
- **Their messaging:** clinical-grade hybrid scanning
- **What we DON'T copy:** hardware-centric framing — we are pure smartphone
- **Screenshots needed:** same

## Adjacent (not direct, useful for context)

- **Withings** — smart scales (different category — they need device)
- **InBody** — BIA / hardware (clinical-grade, in-clinic)
- **DEXA scan providers** — gold standard (slow, expensive)
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
