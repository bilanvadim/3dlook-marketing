---
product: fitxpress
type: log
vertical: all
date: 2026-09-27
---

# Log: /fitxpress/ (page-builder, builder role)

**2026-09-27**

- Read SKILL.md (2026-09-27 hierarchy), references (page-types, kit-vertical-page, copy-humanisation,
  ux-pass, gates-and-scorecard, handoff-kit, site-inventory), docs/page-pipeline.md, CLAUDE.md §2/§6/§10/
  §12, about-me.md, audience.md, product-info canon (proof-points, accuracy-formulations, compliance,
  messaging, faq, tech-spec, how-it-works, pricing, overview, 8 FX use cases, UK Meds and Yazen cases),
  editorial-guardrails, terminology-guardrails, hard-bans-card, DESIGN.md, SEO plan §0/§1/§4 1.1/§9.0,
  gsc-findings.md, content-plan.md "Published assets", published-articles-inventory.md.
- Fetched sequentially with a browser UA, 1 s apart: benchmark telehealth page (200), homepage (200),
  `/pricing/` (200), `/fitxpress/` (301 → `/`), `/fitxpress` (301 → `/content-hub/fitxpress-admin-panel-launch/`).
  Live FitXpress entry tier: Starter $1,000/month, up to 500 scans; FX tiers use "Book a demo".
- Routed: product page, no Kit → vertical Kit adapted (slot map in gate-reports.md). G-I n/a. G-A done
  from existing GSC baseline.
- Drafted page.md. Detector run 1: HARD FAILS (3): claims_discipline ×2, em_dash ×1; density 1.34/1000.
- Fixed hard fails → CLEAN. Sentence mean 10.9.
- Humanisation pass (layers 1-4) as a separate step: hedges, M1 expansions, removed two triads and a
  reading-experience line, varied rhythm. Second round ("what still reads machine-written?"): four fixes.
  Final detector: CLEAN 0.0/1000; sentence mean 11.3, 4 over 25 words, 0 over 35.
- Built JSON-LD (WebPage, SoftwareApplication, Organization, BreadcrumbList, FAQPage ×12) from the page
  text; json.load passes. Yoast title 60, description 146.
- Wrote fact-sheet, gate-reports, open-items, TODO, README, wordpress-notes.
- Not done by design: publish, commit, blind judge (coordinator owns G-J).

**2026-09-27, after G-J round 1 (70/100, not taken)**

- Removed the docs `[PLACEHOLDER]`; linked `https://docs.fitxpress.3dlook.me` directly (dofollow note in wordpress-notes).
- Removed "independent regulatory assessment" (trust section, medical-device FAQ); short form + FDA sentence + trust FAQ link. Recorded in open-items A14.
- Added "What you get back and where it goes" (no JSON: canon has no public field names). Industries grid rewritten with verbatim segment pains; opinion line added. Closing reduced to one soft alternative.
- wordpress-notes: JSON-LD FAQ regenerated from page text (valid JSON, `softwareHelp` → docs), demo form spec, events `demo_click`, `generate_lead` (form_name), `docs_click`. fact-sheet: conversion set-up and planned-build sections, all marked not measured.
- Detector: CLEAN 0.0/1000; sentence mean 11.3, 2 over 25, 0 over 35.

**2026-09-27, after G-J round 2 (68/100, not taken)**

- Hard fail fixed: "90 days" removed from the fitness card. Full digit sweep; "five scans per participant" also removed (not in proof-points). All remaining numbers traced in fact-sheet.
- Model-training row carries "unless the customer gives explicit, documented authorization". Timing phrase once in body + once in FAQ; Admin Panel once; decision boundary once; body medical line short form + trust FAQ link; FDA sentence only in the FDA FAQ answer.
- Added training-data line (proof-points L65-68). Varied paragraph openings. FAQ JSON-LD regenerated.
- Detector CLEAN 0.0/1000; sentence mean 11.4, 4 over 25, 0 over 35. Proof lever logged for Vadim (open-items A18).

**2026-09-27, after G-J round 3 (74/100, no hard fails; gate not taken after 3 rounds)**

- Unscored post-round-3 fixes: outcome H1; "validation" → "internal study" / "study dataset"; compliance table cut to 5 rows + trust FAQ pointer; build markers moved into HTML comments; in-body link to /mobile-tailor/. JSON-LD WebPage name updated.
- README/TODO lead with the gate status, the proof lever (open-items A18) and the build-dependent axes. Detector CLEAN 0.0/1000.
