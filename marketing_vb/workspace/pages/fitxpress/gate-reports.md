---
product: fitxpress
type: gate-reports
vertical: all
date: 2026-09-27
---

# Gate reports: /fitxpress/

Builder-side record. **Not for the blind judge** (per `gates-and-scorecard.md`, the judge gets only
`page.md`, the page type, the slot list, the scorecard and `fact-sheet.md`).

## Phase 0 · Intake

| Field | Answer | Source |
|---|---|---|
| Page type | Product page (FitXpress product parent) | Vadim, 2026-09-27 |
| Product | fitxpress | |
| Vertical | all (links down to 8) | |
| Target buyer | Product, engineering, clinical-operations, compliance and underwriting decision-makers across the 8 FitXpress segments | `audience.md` shared spine, `CLAUDE.md` §4 |
| Intent | Commercial / navigational: brand "fitxpress", "ai body scanner", "body scanning software", "body scanning API", "body measurement API/SDK" | Task brief; `gsc-findings.md` §0 |
| Place in site | `/fitxpress/`, child of `/`, parent of `/fitxpress/for-{vertical}/` | `site-inventory.md` gap 1 (2026-09-27) |
| One conversion action | Book a demo | Vadim 2026-09-27; SEO plan §0, §9.5 |
| Proof | Logos only: UK Meds, Yazen, Healthyr | Vadim 2026-09-27 |
| Language | English | |

## Phase 1 · Kit routing

**No product-page Kit exists** (`page-types.md`: "Product page … gap — nearest: vertical Kit"). The page
was built from `kit-vertical-page.md` and adapted. Slot map:

| Kit slot | On this page | Status |
|---|---|---|
| 1 Breadcrumbs | Home → FitXpress | Kept |
| 2 H1 | "FitXpress AI body scanner and body measurement API for health programs" | **Adapted**: Kit formula is "[outcome] for [vertical]"; a product parent names the product and its head queries |
| 3 Hero + vertical proof point | Spec row (2 / under 45 s / 80+) + logo strip | **Adapted**: no vertical number exists; product spec numerals and logos stand in |
| 4 Vertical context | Dropped | Not applicable to a cross-vertical parent; each vertical page carries its own |
| 5 Pains | "Why programs stop trusting self-reported body data" | **Adapted** to the shared-spine pain in `audience.md` |
| 6 What the product is + boundary | Outputs table + estimates note; boundary sentence sits in trust block | **Adapted**, and expanded into the outputs table (§2.13 categories) |
| 7 Where the workflow differs | "How a scan works" | **Adapted**: a parent states the base flow; verticals state differences |
| 8 Compliance | Trust table + medical-device and decision boundary + FAQ link | Kept |
| 9 Accuracy, scoped | "Accurate enough for which decision?" | Kept |
| 10 Vertical cases | **Dropped** | Clients refuse public case studies (Vadim 2026-09-27); logos only |
| 11 Customer quote | **Dropped** | No approved quote exists |
| 12 Integration | "How FitXpress fits into your product" | Kept, expanded (two patterns, Admin Panel, access rule, docs) |
| 13 FAQ | 12 questions + FAQPage | **Adapted**: product-level questions (the Kit narrows FAQ to vertical-only questions; on the parent the general ones belong here) |
| 14 Price signal | "What FitXpress costs" | Kept, trial omitted by instruction |
| 15 Primary action | Book a demo (hero + close) | Kept |
| 16 Soft alternative + siblings | Soft alternative in close. Sibling block replaced by the **industries grid linking down to 8 verticals** | **Adapted / invented**: the industries grid is the parent's link-down block that `site-inventory.md` says every parent lacks |
| 17 Technical layer | `wordpress-notes.md` | Kept; `SoftwareApplication` replaces `Service` |

**Invented slots** (no Kit equivalent): the outputs table with output categories; the industries grid;
the pricing section as its own H2 (Kit folds price into the CTA area).

## G-I · Should this page exist

**Not applicable.** G-I is a vertical-page gate (`gates-and-scorecard.md`: "G-I · … vertical pages
only"). A product parent is not a vertical page. The standing FX waiver of 2026-09-27 is therefore
irrelevant here. The page's existence was decided by Vadim on 2026-09-27 (hierarchy decision,
`site-inventory.md` gap 1; SEO plan §9.0).

## G-A · Architecture gate

- [x] **Placed.** Parent `/`; URL `/fitxpress/`; children = all `/fitxpress/for-{vertical}/` pages. Today
  only `/fitxpress/for-connected-and-digital-fitness/` is on the pattern; two root-level FX pages move
  only when rebuilt (`site-inventory.md` migration rules).
- [x] **Cannibalisation checked** against both inventories (below).
- [x] **Inbound internal links named** (below). None exist yet; all are TODO items.
- [x] **Baseline captured** from `workspace/research/seo-fitxpress-2026-09/data/gsc-findings.md` (pulled
  2026-09-25). The URL exists as a 301, so this is a restore, not a new page.

### Search Console baseline

| Signal | Value | Source |
|---|---|---|
| Old `/fitxpress/`, "ai body scanner", Jun 2025 to Feb 2026 (pre-301) | Position **3.1**, 3,060 impressions, **745 clicks** in 9 months | `gsc-findings.md` §0 item 3 |
| Homepage `/`, "ai body scanner", L3M (2026-06-24 to 09-22) | Position **5.6**, 881 impressions, 43 clicks | Same |
| "fitxpress" (brand), L3M | Position **6.0**, 373 impressions, 21 clicks, split across **8 URLs** (lead URL `/for-bmi-verification/`) | `gsc-findings.md` §1, Brand: FitXpress |
| Old `/fitxpress/` on "fitxpress" pre-301 | Position 4.4, 291 clicks | `gsc-findings.md` §0 item 4 |
| "body measurement software" | Position 31.3 (article `/content-hub/body-measurement-software/`) | `gsc-findings.md` §1 |
| "body scanning technology" | 9,188 impressions, position 10.1, held by the apparel article | `gsc-findings.md` §0 item 3 |
| "body measurement API/SDK" | 0-20 searches per month (plan §1 item 6) | SEO plan §1 |

Post-launch review at 30 and 90 days against these rows (Phase 7). Expect a 2-8 week dip on "ai body
scanner" while intent moves from `/` to `/fitxpress/` (SEO plan §9.0 risks).

### Cannibalisation and intent split

| Competing URL | Queries at stake | How intent is separated |
|---|---|---|
| `/` (homepage) | "ai body scanner", "ai body scan", "body scanner ai", "weight tracker 3d" | Homepage becomes the general 3DLOOK products page (brand "3DLOOK", "body scanning technology"). `/fitxpress/` takes the FitXpress product intent: brand "fitxpress", "ai body scanner" as a B2B product, "body measurement API". Homepage keeps a FitXpress block with anchor text "FitXpress" / "AI body scanner" pointing here (TODO). Yoast titles differ: homepage should not carry "AI body scanner" once this ships (homepage title is out of this skill's scope; flagged in TODO) |
| `/content-hub/3d-body-scanning/` | "3d body scan", "3d body analysis", "body measurements visualizer", "bmi 3d model" | That article keeps the informational "what is 3D body scanning" intent. This page never uses "3D body scanning" in H1/H2/title and does not explain the technology; it sells the product. No link from here to that article, to avoid anchor overlap |
| `/for-bmi-verification/` | "fitxpress" (currently the lead URL) | Once `/fitxpress/` exists, the brand query should consolidate here. The BMI page keeps "bmi verification". This page links to it with the anchor "Online pharmacies and BMI verification", not with "FitXpress" |
| `/content-hub/body-measurement-software/` (Dec 2021) | "body measurement software" | Old article, position 31. This page targets "body scanning software" and "body measurement API". Recommend the article link up here with anchor "FitXpress body measurement API" (TODO, nice-to-have) |
| `/content-hub/fitxpress-admin-panel-launch/` | Receives `/fitxpress` (no slash) via 301 | Redirect must change to `/fitxpress/` (TODO blocker). The Admin Panel is described here as optional |
| Vertical pages and hub articles | Vertical queries | This page carries one line per vertical and links down. No vertical workflow, regulator or KPI detail is repeated here |

Note on "ai body scanner" demand: most of the query family in GSC is consumer ("girl body scanner ai",
"ai body scanner app", India-heavy clicks, `gsc-findings.md` §0 item 8). This page is written for
organizations and will convert few of those clicks. That is intended; the SEO plan's goal is
FitXpress pipeline in HubSpot, not position for its own sake.

### Inbound internal links required

1. Homepage FitXpress block → `/fitxpress/` (anchor "FitXpress" or "FitXpress AI body scanner").
2. Header nav "FitXpress" and footer "What We Do → FitXpress" → `/fitxpress/` (footer currently has a
   FitXpress item; target to confirm).
3. Every FX vertical page breadcrumb and body → `/fitxpress/` (link up).
4. `/pricing/` FitXpress tab → `/fitxpress/`.
5. Health hub `/content-hub/ai-body-data-health-hub/` and the accuracy and trust FAQ articles → `/fitxpress/`.
6. `llms.txt` entry (SEO plan §9.0).

## G-T · Technical gate: state on 2026-09-27

| Check | State |
|---|---|
| Indexable, in sitemap, canonical to self | **Open.** Specified; blocked by the live 301 `/fitxpress/` → `/` |
| Schema validates (SoftwareApplication + audience + areaServed, FAQPage, BreadcrumbList) | **Partly.** JSON parses; not run through Rich Results Test |
| Yoast title ≤ 60, description ≤ 155, different from parent and hubs | **Pass** on length (60 / 146). Differs from homepage title ("3DLOOK - AI-powered 3D body scanning solution") and all hub titles |
| Performance and accessibility at 375 / 768 / 1280 / 1440 | **Open.** Not built |
| One primary action; analytics verified manually | **Half.** One action (Book a demo). Events specified, not verified |
| Every `[marker]` replaced; alt text | **Pass on copy** after round 1 (docs link now direct). Visual markers are design briefs. Alt text written in `wordpress-notes.md` |
| `fact-sheet.md` written | **Pass** |

G-T is **not passed**; it cannot be before the page is built.

## Detector and sentence length

| Run | Detector (`--channel page --summary`) | Sentences |
|---|---|---|
| Draft 1 (before any pass) | HARD FAILS (3): `claims_discipline` ×2 ("Diagnosis", "make the decision"), `em_dash` ×1; density 1.34/1000; soft "serve as" | not measured |
| After detector fixes | CLEAN, 0.0/1000 | mean 10.9 words, 4 over 25, 0 over 35 |
| Final (after humanisation, both rounds) | **CLEAN, 0.0/1000** | **mean 11.3 words, 4 over 25 (2.9%), 0 over 35** (via `article_lint.prose_sentences`) |

## G-J status

**Gate not taken: 74/85 after 3 rounds (70, 68, 74), weakest axis = Proof of belonging. Post-round-3 fixes
applied, unscored.** Round 3 had no hard fails. No further judging; handed to Vadim.

Post-round-3 fixes (unscored): H1 rewritten as an outcome ("FitXpress AI body scanner: body measurements
your health program can act on"); hero keeps the exact timing scope; "validation" → "internal study" /
"study dataset"; compliance table cut to HIPAA, GDPR, hosting, photos, identifiers, with the rest pointed
to the trust FAQ; build markers ([LOGO STRIP], spec row, button labels) moved into HTML comments; one
in-body link to the sibling `/mobile-tailor/`. Detector after these: CLEAN, 0.0/1000.

## G-J round 1 and fixes (2026-09-27)

Judge: 70/100, not taken. Proof 12/20, Claims 11/15, Uniqueness 11/15, Conversion 10/15, Buyer language 7/10,
Human copy 7/10, Search/AI 8/10, Place 3/5, Design/technical 1/5. Hard fails: `[PLACEHOLDER]` marker;
"independent regulatory assessment" without a named party (guardrail #3), twice.

Fixes: docs link made direct; "independent" removed in both places (short medical-device form + FDA
sentence + trust FAQ link); new invented slot "What you get back and where it goes" (payload in words, no
invented field names; Admin Panel optional; destinations per program from use-case files); industries grid
rewritten with each segment's own pain; opinion added on what a scan should and should not decide; closing
section reduced to one soft alternative; demo form and events specified; fact-sheet gained a planned-build
section. Detector after fixes: **CLEAN, 0.0/1000**; sentence mean 11.3, 2 over 25, 0 over 35. Second-round
"machine-written" check: a "listed earlier on this page" reading-experience phrase, a contraction and a
noun triad in the opinion line, all fixed.

## G-J round 2 and fixes (2026-09-27)

Judge: 68/100, not taken. Proof 11/20, Claims 10/15, Uniqueness 10/15, Conversion 11/15, Buyer language 7/10,
Human copy 6/10, Search/AI 8/10, Place 3/5, Design 2/5. Hard fail: "90 days" in the fitness card, sourced
only from a use-case file.

Fixes: full digit sweep (every number now traces to `proof-points.md` or live `/pricing/`; "90 days" and
"five scans" removed); model-training row carries the FAQ qualifier; "under 45 seconds from the photos to
structured results" once in the body and once in the FAQ (spec row and step 6 no longer repeat it); Admin
Panel described once; decision boundary once (trust section); body medical line = short form + trust FAQ
link, FDA sentence only in the FDA FAQ answer; training-data line added as non-client proof; paragraph
openings varied (7 paragraphs started with "FitXpress", now 3, two of them canon boundary sentences).
Detector: **CLEAN, 0.0/1000**; sentence mean 11.4, 4 over 25, 0 over 35; no 6-gram repeated 3+ times.
"Machine-written" pass: a "studies that follow" reading-experience phrase, a triple-repeated FAQ anchor
and a duplicated pricing sentence, all fixed. Proof lever for Vadim: open-items A18.

## Humanisation pass (separate, after drafting)

Layer 1 (guardrails): hedged "closes that gap" to "adds", "reduces retakes" to "helps reduce", "flags"
to "can flag"; repeatability wording made conditional per `accuracy-formulations.md` §3.4; "internal"
kept on the validation study (§5 note); M1 scan: expanded API, SDK, BMR, GLP-1, HIPAA, BAA, GDPR, SOC 2,
TLS, SSE-S3, DXA, BIA, UK MDR, EU MDR, FDA, RTPV at first use.
Layer 2 (terminology): removed "below" and a reading-experience line in the trust intro; "customer"
kept only in legal/contract rows; one corrective negation kept as a regulatory boundary.
Layer 3/4: removed two adjective/noun triads (problem section, closing), rewrote the industries intro,
varied rhythm in hero and problem paragraphs, added a stated opinion (single accuracy percentage;
SDK capture recommendation).
Second round, "what still reads as machine-written?": (1) "Each… Each…" repeated opener in the
industries intro; (2) truncated timing phrase that drifted from the canon wording; (3) a flat
verbless card line (bariatric); (4) "below" slipped back in. All four fixed.
