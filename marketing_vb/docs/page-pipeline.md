# Website page pipeline (`page-builder` / `/page`) — вынесено из CLAUDE.md §16 (2026-09-21)

> Канонический дом секции. Ссылки вида «CLAUDE.md §16» в старых артефактах ведут на стаб в CLAUDE.md, стаб ведёт сюда.

## 16. Website page pipeline (`page-builder` / `/page`)

> Added 2026-08-23. Owns **marketing pages on 3dlook.ai**, not articles.

**Skill:** `.claude/skills/page-builder/SKILL.md` — one canonical copy, no plugin mirror. Adapted from
Victor Shulga's public `page-builder` skill.

**Command:** `/page [vertical|URL] [gate|build|judge|handoff|full]`. Artifacts in
`workspace/pages/{slug}/`.

**Scope split — read this before routing a request:**

| Request | Owner |
|---|---|
| Use-case / vertical page, campaign landing, product page, case-study page | `/page` |
| Blog article, hub, comparison, buyer guide | `/new-article` (mvb-seo) |
| Social posts from a published article | `/post-from-article` |
| 20-point QC of a pipeline artifact | `/qc` |

**Four gates.** G-I decides whether a vertical page should exist at all (use-case file + **2 or more
publishable cases from that vertical** + demand + 5 facts absent from the parent + the 60% uniqueness
rule). G-A blocks writing until placement, URL, cannibalisation and the Search Console baseline are
settled. G-T blocks publishing on technical grounds. G-J is a **blind judge in a fresh subagent**,
100-point page scorecard, threshold 85, maximum 3 rounds, and publishing below 85 without flagging it
is forbidden. `quality-controller` does not substitute for G-J — it is neither blind nor page-shaped.

**Short and commercial (Vadim, 2026-09-30).** Use-case landings convert and the articles teach:
1,100-1,600 words of visible copy (1,300 until the fitness final of 2026-10-07), 4-6 FAQ, one paragraph then a link for anything deeper, a call to
action on every second screen, "no integration fee" in the price line. Page order and word budget: the
Kit's "Length and order" section. Length and register benchmark (since 2026-10-02):
`workspace/pages/for-insurance-underwriting/page-final-2026-10-02.md`, the copy passed to design after
Asselya's deduplication and guardrails pass. Her rules (direct address at most 12.5 per 1,000 words, every
acronym expanded, no "vs" in headings, a named subject in every sentence, no FAQ repeating the body) are
in the Kit's "Register for an enterprise reader" section, and `detect-ai-tells.py --channel page`
checks the first three.

**Sell, not educate (Vadim, 2026-10-06).** Use-case landings need a stronger sales angle to close
leads, so the team's ten writing rules are now part of the Kit ("Sell, not educate", quoted verbatim):
H1 = product + audience + primary outcome; value before explanation, so "What you get" now comes before
"How it works"; conclusions stated, never left for the reader; every feature turned into a benefit; one
job per section; explanation cut unless it helps the buying decision; proof backing the claim rather
than standing in for it; and the blog test (a paragraph that could move to an article without
weakening the sales argument is cut). They run as their own sales pass after the draft and before
humanisation, the blind judge scores them as a 15-point "Sales argument" axis (the scorecard was
rebalanced and now sums to 100; it summed to 105 before), and `detect-ai-tells.py --channel page`
reports an H1 without the product name. Guardrail hedges, the method sentence and the boundary sentence
are claims discipline, not filler, and always win over "cut qualifiers". The insurance final page stays
the register benchmark only: its H1, block order and record table predate these rules.

**Fitness final = structure benchmark (Vadim, 2026-10-07: "the latest and the most correct").**
`workspace/pages/for-connected-and-digital-fitness/page-final-2026-10-07.{md,html}`, v3 merged with the
team's fixes and the fitness client logos. What it settled is in the Kit's "Fitness final" section: the
value cards for the end user come right after the hero, before the problem; a second approved H1 form,
the mobile alternative to the method the buyer knows, with the product named in the lede (the detector's
H1 check accepts the lede's first two sentences since then); capture claims at the confirmed level until
product confirms more (Real-Time Pose Validation "gives pose and framing guidance"; the record lists
"Processing status and timestamps"); the platform, not FitXpress, links each scan ID to its user; the
white-label boundary (the capture layer stays fixed); five data lines including encryption, then the
privacy contact; one line per price tier and "Custom plans cover higher volumes."; a pilot against a
comparison cohort, randomised where practical, with an evaluate step before rollout; "See a sample record
in the demo"; the comparison as cards on mobile; the vertical's own client logos first in the logo row.

**The schema benchmark:** `/structured-body-data-for-telehealth-digital-health-programs/` (July 2026)
still sets the standard for FAQPage and Service schema (`audienceType` + `areaServed`), claims
discipline and clean headings. Its ~1,600 words and 13 questions are no longer the target.
`/for-bmi-verification/` (~659 words, no FAQ, no schema) is the first rewrite candidate, for the missing
FAQ and schema rather than its length.

**One hierarchy for both products (Vadim, 2026-09-27; replaces the 2026-08-23 "homepage is the
FitXpress parent" rule):** `/fitxpress/` is the FitXpress parent with verticals at
`/fitxpress/for-{vertical}/`, `/mobile-tailor/` the Mobile Tailor parent with
`/mobile-tailor/for-{vertical}/`, and the homepage becomes the general 3DLOOK products page (FitXpress
first, Mobile Tailor, wrist measurement). Reasons and risks:
`workspace/research/seo-fitxpress-2026-09/2026-09-25-fitxpress-seo-plan.md` §9.0.

**Migration, done once, with the use-case release:**
1. `/fitxpress/` ships and its 301 to `/` comes off.
2. Root-level FX pages (`/for-bmi-verification/`, `/structured-body-data-for-telehealth-digital-health-programs/`) move with a 301 only when rebuilt.
3. `/fitxpress/for-connected-and-digital-fitness/` keeps its URL; only its breadcrumb needs fixing.
4. `/fitxpress` without the slash 301s to `/fitxpress/`.

Open debt: **neither parent links down to its verticals in the body**, only through the header nav
dropdown. Every new parent page carries that block.

**The G-I reality check:**

1. **Only Mobile Tailor verticals clear the 2-case bar.** Uniforms has Safariland + Burlington Medical;
   made-to-measure has Generation Tux + Jim's Formal Wear if formal-wear rental counts as the same
   vertical.
2. **Standing G-I waiver for every FitXpress vertical (Vadim, 2026-09-27).** Clients do not agree to public case studies (logos only), so FX vertical pages are built without the 2-case bar. What stands in for cases: customer logos; anonymised figures only from `proof-points.md` (a figure that could identify a client is cleared with Vadim first); the accuracy framework; the trust FAQ; the workflow itself. Never an invented or implied case. The waiver for a vertical ends when its first approved case lands. The other G-I checks (use-case file, demand, 5 facts, 60% rule) still apply. Record `G-I: standing FX waiver 2026-09-27` in `gate-reports.md`.

**Non-negotiables inside the skill:** every number from `proof-points.md`; client names and metrics
only from `case-studies/`; Mobile Tailor customer ARRs never published; the 11 editorial guardrails
along with M1/M2/M3 run as their own pass, not as a habit while drafting; `terminology-guardrails.md`
Part 1 and Part 2 as Layer 2 of the humanisation pass; accuracy figures always carried with their reference and limit, and a link to the accuracy framework,
which holds the "accurate enough for which decision?" reframe and its four conditions; medical framing stated directly
(**"FitXpress is not a medical device."** — since 2026-09-11; "positioned as" is banned for every product, scope and regulatory statement);
IEEE only in the two approved sentences from `proof-points.md`, with no standalone IEEE logo in an award
or certification strip, and "80+ body measurements", never "80+ body metrics" (terminology guardrails
§2.11 and §2.13, synced 2026-09-14);
`DESIGN.md` decides every token; a price signal and a link to `/pricing/` on every commercial page
(FitXpress: from $1,000/mo, no integration fee, no public trial).

**Forms and tracking on FitXpress pages (Vadim, 2026-09-29).** Articles bring the traffic and link to their vertical's landing; the landing converts. Every FX page embeds one shared HubSpot form `FX | LP | Demo` (anchor `#demo`), and GTM fills the hidden `fx_vertical` from the page path. No per-page forms. Hub articles link to the landing above 30% depth and from "Book a demo" to `…/#demo`; GA4 tracks that hop as `article_cta_click`. Spec: `workspace/research/seo-fitxpress-2026-09/2026-09-27-tz-tracking-hubspot-ga4.md`.
