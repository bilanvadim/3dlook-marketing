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

**The benchmark:** `/structured-body-data-for-telehealth-digital-health-programs/` (July 2026) is the
one vertical page already built to the current standard — scoped accuracy, a real comparison block, a
13-question FAQ with FAQPage schema, Service schema with `audienceType` + `areaServed`, ~1,600 words,
no banned words in the headings. The Kit tells writers to match it. `/for-bmi-verification/` (~659
words, no FAQ, no cases) is the first rewrite candidate.

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
Part 1 and Part 2 as Layer 2 of the humanisation pass; accuracy always scoped through
"accurate enough for which decision?" and its four conditions; medical framing stated directly
(**"FitXpress is not a medical device."** — since 2026-09-11; "positioned as" is banned for every product, scope and regulatory statement);
IEEE only in the two approved sentences from `proof-points.md`, with no standalone IEEE logo in an award
or certification strip, and "80+ body measurements", never "80+ body metrics" (terminology guardrails
§2.11 and §2.13, synced 2026-09-14);
`DESIGN.md` decides every token; a price signal and a link to `/pricing/` on every commercial page.
