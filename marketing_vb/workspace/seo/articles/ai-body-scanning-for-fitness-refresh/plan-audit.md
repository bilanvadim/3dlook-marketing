---
plan: plan.md
slug: ai-body-scanning-for-fitness
workspace: ai-body-scanning-for-fitness-refresh
product: fitxpress
created: 2026-11-18
status: draft
mode: no-checkpoint (decisions recorded, not awaiting approval)
---

# Plan audit: ai-body-scanning-for-fitness (refresh in place)

Why `plan.md` looks the way it does. Read by `seo-publisher` and people; the writer does not need it.
Inputs: context pack `_context-packs/ai-body-scanning-for-fitness-refresh.yaml`, `refresh-gap-analysis.md`,
`published-live-2026-11-18.md`, the live landing snapshot `workspace/pages/for-connected-and-digital-fitness/published-live-2026-11-13.md`,
the live GLP-1 fitness-apps article (published 2026-10-29), `landing-map.md`, `about-me.md`,
`hard-bans-card.md`, `editorial-rewrites.md` §7, `accuracy-formulations.md` §5, `scripts/article_lint.py`.

## 1. Decisions

### D1. Primary keyword: `ai body scanning for fitness` (no data)

- **Chosen:** the URL phrase. Ahrefs US 2026-11-18: no data (null, not zero), KD no data. Search
  Console earned the family `ai body scan fitness` (121 impr. at 2.8) and `… app` (74 at 4.4) in Aug-Nov 2025.
- **Why not a measured head term:** the only measured variants are either owned elsewhere or tiny.
  `ai body scan` (70 / KD 2) and `ai body scanner` (150 / KD 1) share the parent topic `ai body scanner`,
  which landing-map gives to `/fitxpress/` and the homepage holds (1,792 impr. at 7.2, Aug-Nov 2026).
  `ai body scan fitness app` (10 / no data) is measured but cannot sit naturally in an H1 that keeps the
  URL words. `body scanning` (400 / 37) and `body scanner` (1,000 / 47) are consumer and hardware mixes.
- **Gate 7 consequence:** the exact string must appear in the H1 and one H2. Section 2's H2 is
  `AI body scanning for fitness: the short answer`.
- **Rejected:** `ai body scanner` (cannibalizes the homepage / `/fitxpress/`; brief forbids it);
  `body scanning for fitness apps` (landing primary, rule 3); `ai-powered fitness apps` (800 / 12, but
  "AI-powered" as a value is a no-go phrase and the hub owns AI in fitness).

### D2. H1, meta title, and the landing-map rule 3 conflict

- **H1:** AI Body Scanning for Fitness: Where a Phone Scan Fits in the Member Journey (13 words, 75 characters).
- **Meta title:** AI Body Scanning for Fitness: Where a Phone Scan Fits (53 characters).
- **Meta description draft:** How AI body scanning fits a fitness app: onboarding baselines, check-ins,
  premium tiers, phone scans vs gym scanners, and how to test it. (137 characters.)
- **Conflict:** gap analysis §4 suggested the Sheet's "fitness apps" framing for the H1. Rule 3 forbids the
  landing's primary keyword `body scanning for fitness apps` in the title, H1 and meta title, and "AI Body
  Scanning for Fitness Apps" contains it verbatim. **Resolution:** keep "AI body scanning" and "fitness"
  (the URL words), drop "apps" from the H1 and meta title, and carry the app angle in the subtitle ("Where a
  Phone Scan Fits in the Member Journey") and the meta description ("a fitness app", allowed there).
  H1 case follows the published Hub 1 articles (Title Case H1, sentence-case H2/H3).

### D3. Demand, and what the page is for

- Measured demand for the fitness-app phrasing is near zero: seed and both fitness-app phrasings have no
  data; the closest measured phrase is 10 a month. The 2025 traffic (255 clicks in July 2025) was consumer
  `ai body scanner` / `… app` / `… free` demand, now held by the homepage; this page sits at positions 25-80
  for it (171 impr. at 35.8, Aug-Nov 2026). The refresh will not chase it and may lose what remains. Accepted.
- **The page's job:** (1) a commercial step for fitness businesses that reach it from the hub, search or
  AI assistants, sending them to the landing (the row credits the old page with 57 contacts and 4 deals);
  (2) direct answers to two tracked AI-assistant questions where 3DLOOK is named in 22% and 43% of answers.
- **How to judge it (no traffic promise):** clicks from this URL to the landing (GA4 referral), HubSpot
  contacts with this URL as first page, and visibility on prompts 565780358696 and 565540613659 in the
  weekly AEO pull. Suggested look: 8 weeks after re-indexing.

### D4. Reader and owned intent

Reader per pack: product, growth and founder roles at connected and digital fitness companies (icp-detail
§8). Hub 1 header forbids another broad AI-body-scanning overview. The plan answers with a short-answer
block and six body H2s, each a product-team decision (placement, retention case, outputs and limits,
hardware vs photos vs in-app, selection criteria, cohort test), then FAQ and next steps; no capability
survey. Brief elements → sections: member journey → S3; produces / does not → S5; retention (FIT-ADJUST,
FIT-KIDMAN only) → S4; hardware vs photos vs in-app → S6; cohort test → S8; AEO 22 → S6; AEO 43 → S7.

### D5. Cannibalization handling

| Neighbour | Owns | This page | Section |
|---|---|---|---|
| `ai-in-fitness-industry` (hub) | capability landscape, personalization, coaching, bias, implementation | one up link; no survey, no bias, no "who can use it" | S4 |
| Landing `/fitxpress/for-connected-and-digital-fitness/` | product, record table, 4-column comparison table, pricing, pilot steps and metric list, 6-question FAQ | three CTAs; none of its tables, prices, pilot steps or FAQ answers restated. S6 uses a three-H3 decision framework, not a table; S8 covers decisions before a pilot, not the pilot steps or metrics | S2, S6, S10 |
| `glp-1-muscle-loss-fitness-apps` (live 10-29) | GLP-1 members, comparable check-ins (baseline, cadence, capture, review, alternative path), pilot metric list | one link on lean mass vs muscle; S8 does not repeat its check-in parts or metric list | S5 |
| `remote-body-measurement-online-fitness-coaching` | coaching programs | one link | S3 |
| `body-scanning-technology-for-weight-loss` (1.x2 pending) | weight-loss progress tracking | one sentence and link | S4 |
| `body-scanning-technology-comparison` | 2-photo vs video vs hardware | one link; no method table | S6 |
| `ai-body-scanners-vs-dexa-scans` | scan vs DXA (also written DEXA) | one link from FAQ 1 | S9 |
| `mobile-body-scanning-accuracy` | accuracy framework | §5 short forms, link in each figure paragraph | S5 |
| `fitxpress-data-privacy-security-regulatory-faq` | privacy, retention, regulatory | one short answer plus link | S9 |

The S6 H2 is question-shaped ("alternative to a hardware 3D body scanner") and close to the landing's H1
("A mobile gym body scanner alternative for fitness apps"). Accepted: the article holds the informational
question, and CTA 2 hands the commercial phrase to the landing as its anchor.

### D6. AEO

- `no_prompt_covers_topic: false`. `ai_cites` empty in this pull, so rule 2 (named in the answer because
  our page is cited) is not triggered; FitXpress (3DLOOK) is named in the S6 and S7 answer paragraphs
  anyway, within approved claims and without ranking language, because one prompt sits well below the
  portal average (22 vs 32.3) and the other is only modestly above it (43).
- 565780358696 (22) → S6 answer-first. 565540613659 (43) → S7 answer-first. 565767450188 (54) → S7 integration
  bullet (no separate FAQ, it would repeat S7). 554650727324 (55) → S7, fitness side only (wellness is outside
  the vertical boundary). 565540613660 (75) → the landing FAQ already answers it; not repeated.
  565780359239, 554650727322, 565494878373 → telehealth segment, out of scope.
- **open_recommendations:**
  - 184342662 (HIGH, CONTENT, "Best Mobile Body Scanning Software Compared"): **not taken.** A vendor
    listicle names competitors (blog rule) and is a separate asset with no content-plan row; S7 answers the
    criteria part of the question without vendors.
  - 184940079, 185383829, 184940080 (URL, get featured on robosize.com / fit3d.com lists): **not taken**,
    off-page outreach, not article content.
  - 185383818 (LinkedIn post on scan validation): **not taken**, social channel, not this refresh.

### D7. CTAs

| CTA | Section | Position | Anchor (landing-map Hub 1 row) | URL |
|---|---|---|---|---|
| 1 | S2, sentence after the bullets | ~13% | body scanning for fitness apps | landing |
| 2 | S6 answer-first paragraph | ~53% | mobile alternative to a gym body scanner | landing |
| 3 | S10, second sentence ("Then …") | end | body composition tracking for fitness apps · "book a demo" | landing · landing `#form` |

One-CTA rule overridden by the pack (same as the ROI and try-on refreshes). Each anchor from the row is used
once. CTA 3 carries two links in one sentence (text link plus the demo link); if the editor wants exactly
three landing links, drop the text link and keep `#form`. The landing has no `#demo`; `#form` verified live
2026-11-18. No `/contact-us/`, no homepage links (the live page had three).

### D8. Length

Target 1,950 words (brief range 1,600-2,200; §7 puts a comparison/workflow piece near 1,900). Budgets:
110 / 160 / 260 / 240 / 250 / 320 / 190 / 210 / 170 / 40. Live baseline ~2,400.

### D9. Fresh examples

- **Proposed, one:** ACSM's 2027 Worldwide Fitness Trends (S4). Category-level, dated, no vendor. Checked on
  ACSM's own release as distributed by Newswise, 2026-10-20: wearable technology No. 1; mobile exercise
  apps from No. 4 to No. 2; data-driven training technology No. 8; more than 1,400 fitness professionals;
  ACSM's Health & Fitness Journal, Nov/Dec 2026, DOI 10.1249/fit.0000000000001208. acsm.org returned 403
  to WebFetch from the VPS, so the plan marks it **"writer must verify at source"** (acsm.org page or the
  journal). It is a survey of professionals' forecasts, not usage data, and says nothing about body scans.
- **Not proposed:** named fitness apps or gym chains offering scans. Several consumer apps and chains get
  their scan from competitors or hardware makers, and the rule is to describe the category rather than name
  them; no fitness client has a cleared case study. Newer retention benchmarks were not sought: the pack
  allows FIT-ADJUST and FIT-KIDMAN only for retention figures.
- If the ACSM item cannot be verified or gets no claim ID, the plan works without it.

### D10. Byline

Recommend **Assel Sekerova** (CLAUDE.md §15 default; she requested the refresh). Live byline Dana
Vioreanu (2024). Her call: Open item 3.

### D11. FAQ

Chosen (three, none in the landing FAQ, none answered by a body section): DXA equivalence (with the
DXA comparison link), physical-disability limitation (FXS-POPULATION), and whether 3DLOOK knows which
member a scan belongs to (FXS-IDS plus the privacy FAQ link).
Rejected: onboarding completion, gym body scan definition, SDKs for remote users, results delivery,
scan frequency, Apple Health / Health Connect (all on the landing); "Does a scan improve retention?"
(S4); "How long does a scan take?" (S2); integration ease (S7); GLP-1 members (no GLP-1 content;
link only); a GDPR roles answer (the canonical sentence needs the M1 expansion and the trust FAQ owns it).

### D12. Structure

Type A use-case piece with §7 elements borrowed: a short-answer bullet block, a three-H3 "fits when"
decision framework, a three-question FAQ, two-sentence next steps. No comparison table (the landing has
one), no metrics table, no diligence-question list. One inline visual (journey line); a second would
repeat the S6 framework. No italic scope note (fitness register); the boundary sits in S2 bullet 5 and S5.

### D13. Links dropped from the live page

Three homepage links (→ landing CTAs), `virtual-body-measurements` and `body-scanning-technology-for-apparel`
(apparel context, Mobile Tailor-adjacent), Bodygee, Neko Health / The Verge, Stanford 2021, PMC6238835,
gitnux, exercise.com, dr-muscle.com, the BCRPA screening-tools link, and the "Further reading" block
(`top-trends-and-features-in-fitness-apps`, `top-fitness-tech-companies`, `top-fitness-industry-trends`:
2025 listicles, off the commercial angle). None is a required link target.

## 2. Deletions ledger (live → refreshed)

| Live section | Action | Where it went |
|---|---|---|
| Opening paragraph (">10% market growth", "Moreover") | CUT figure; rewrite | S1 |
| Introduction: AI Body Tracking ("unprecedented accuracy", "leverages") | CUT | S1 scene replaces it |
| Evolution of Body Measurement Insights, Jazzercise, Woman's World | CUT | none |
| From Tape Measures to AI Body Scan Fitness Apps | REWRITE, shortened; BMI corrected | S1 (tape), S5 (outputs, BMI) |
| Precision and Speed (MRI, rotating platform, exercise form) | CUT; hardware re-described as a separate category | S6 sentence |
| Visualizing Fitness Progress (Stanford 2021, "seamless", "accurately") | REWRITE as placements | S3 |
| Fitness Progress Photo Apps ("objective") | REWRITE without "objective" | S6 "Progress photos fit when" |
| Weight Gain Progression and Loss Tracking (PMC6238835, real-time weight, predictive analytics) | CUT; one link | S4 weight-loss link |
| Real-World Applications (health monitoring, Bodygee, Mobile Tailor, medical diagnostics, Neko) | CUT | S5 boundary |
| Enhancing Gym Experiences ("objective and comprehensive", fat loss calculator) | CUT | S3 premium tier, rebuilt on FIT-PLAN |
| Next Level of Personal Training (gitnux 28%) | CUT | S3 coach review |
| Driving User Engagement and Retention with FitXpress (metabolic rate claim) | CUT claim; argument kept | S4 |
| Leveraging AI Body Scans / AI's Impact on Retention (53%, 71%) | REWRITE on FIT-ADJUST, FIT-KIDMAN | S4 |
| Conclusion ("game-changer", "revolutionary advancement") | CUT | S10 |
| Further reading | CUT | none |
| "Get a demo of FitXpress" at ~45% to the homepage | MOVED and re-targeted | CTA 1 at ~13%, CTA 2, CTA 3 |

## 3. Open items

1. **BLOCKER for article lint gate 3 (coordinator, before the writer runs).** `gate_claims` resolves
   `<!-- claim: ID -->` markers only against the pack's `approved_claims`. All FIT-* IDs sit under
   `additional_approved_claims_topic_specific`, so a FIT-ADJUST or FIT-KIDMAN marker fails 3(a), and the
   same paragraphs without a marker fail 3(b) (24%, 7%, 70%, and every four-digit year). Same gap cost the
   ROI refresh its Yazen figure (writer-notes there). Fix: copy the FIT-* entries into `approved_claims`
   unchanged, and add the ACSM item once the writer has verified it:
   ```yaml
   - id: FIT-ACSM
     text: "ACSM's 2027 Worldwide Fitness Trends (ACSM's Health & Fitness Journal, Nov/Dec 2026; released 2026-10-20): wearable technology ranked No. 1, mobile exercise apps rose from No. 4 to No. 2, data-driven training technology held at No. 8; more than 1,400 fitness professionals responded."
     source: "ACSM release via Newswise 2026-10-20 https://www.newswise.com/articles/acsm-announces-top-fitness-trends-for-2027 ; primary https://www.acsm.org/2027-fitness-trends/ ; DOI 10.1249/fit.0000000000001208"
     note: "Forecast survey of fitness professionals, not usage data. Says nothing about body scanning."
   ```
   The alternative is extending gate 3 to read `additional_approved_claims_topic_specific`.
2. **ACSM verification.** Writer confirms the ranks, the respondent count and the date on acsm.org or the
   journal. If not confirmable, cut the sentence and drop FIT-ACSM.
3. **Byline:** Assel Sekerova vs Dana Vioreanu. Asselya's call; flag in the publish package and digest.
4. **Landing and demo anchor:** `/fitxpress/for-connected-and-digital-fitness/` answered 200 and the form is
   `#form` on 2026-11-18. Re-check both at publish. No relink debt (the landing is live).
5. **H1/title vs landing-map rule 3:** resolved per D2; record in the publish package.
6. **Pack wording that the lint retires:** FXS-OUTPUTS lists `essential fat` and `beneficial fat`, and
   FIT-OUTPUTS-NOTE uses `body composition values`; the superseded table in `article_lint.py` fails all
   three in any article. The plan tells the writer to omit them. Suggest aligning the pack text (or the
   `_stable-fitxpress.yaml` source) so later packs do not carry the trap.
7. **Inbound links to this URL** from other pages after publication: coordinator, gap analysis §6.
8. **Dates:** keep "Published: June 12, 2024"; set "Updated" at republish.
9. **AEO follow-up:** check prompts 565780358696 and 565540613659 in the AEO pull about 8 weeks after
   re-indexing (D3). `ai_cites` was empty on 2026-11-18, so there is no baseline of our citations.
