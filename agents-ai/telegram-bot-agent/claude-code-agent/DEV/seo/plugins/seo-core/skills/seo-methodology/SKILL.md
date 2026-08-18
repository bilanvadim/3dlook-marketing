---
name: seo-methodology
description: How to turn an SEO goal into a data-grounded audit and a prioritized, executable plan — an adaptive diagnostic across all layers (crawl, index, architecture, on-page, keywords/intent, authority, analytics, competition), anti-pattern prediction, ICE prioritization, and a richly structured step list (each step with acceptance, metric, tags, dependencies). Use at the start of any non-trivial SEO project, in /seo-audit, or whenever someone says "improve our rankings / audit our SEO".
---

# SEO methodology — audit → prioritize → plan

The discipline that turns "improve our SEO" into a defensible plan. Mirrors the
dev system's `project-planning`, adapted to search. Diagnose with data, predict
anti-patterns, prioritize by ICE, emit a delegatable step list.

## Principles
- **Data or it didn't happen.** Every finding cites GSC/GA4, a live crawl, a
  fetched SERP, or a tool export. Unmeasured claims are labeled ESTIMATE.
- **Business outcome > vanity metric.** Optimize qualified traffic that converts,
  not raw rankings.
- **Fix the few things that matter.** Ruthless ICE ordering beats a 200-item
  checklist nobody ships.
- **First, do no harm.** Don't deindex, don't break what ranks, don't earn a
  penalty. Every structural change ships with guardrails.

## Diagnostic layers (L0–L8) — adapt depth to scope
- **L0 Business & goals** — what the site sells, target markets/languages, ICP,
  conversion definition, current organic baseline, competitors, constraints (CMS,
  dev capacity, timeline).
- **L1 Accessibility & crawl** — robots.txt, crawlability, crawl budget, server
  responses (status codes, redirects chains/loops), render (JS-dependency, SSR vs
  CSR), orphan pages, `curl`/headless spot checks.
- **L2 Indexation** — GSC Coverage/Pages report, index bloat vs gaps, canonical
  correctness, noindex misuse, duplicate/parameter URLs, `sitemap.xml` health.
- **L3 Architecture & URLs** — site structure, depth, internal linking, URL
  patterns, hreflang for i18n, pagination, faceted navigation.
- **L4 On-page & content quality** — titles/meta, headings, content depth &
  helpfulness, E-E-A-T signals, thin/duplicate content, structured data (JSON-LD),
  media/alt.
- **L5 Keywords & intent** — keyword/intent coverage vs demand, SERP feature
  landscape, cannibalization, topical authority / cluster gaps.
- **L6 Authority (off-page)** — backlink profile quality/toxicity, referring
  domains, anchor distribution, competitive link gap, digital-PR opportunities.
- **L7 Analytics & tracking** — GSC + GA4 setup, rank tracking, event/conversion
  tracking, attribution, reporting cadence.
- **L8 Competitive gap** — where competitors out-rank and why (content, links,
  technical), realistic opportunity sizing.

## Anti-patterns to predict and pre-empt
Keyword cannibalization · index bloat from parameters/facets · redirect chains &
loops · orphaned high-value pages · JS-rendered content Google can't see ·
canonical/hreflang conflicts · thin programmatic pages · migrating URLs without a
301 map · chasing volume over intent · buying links / PBNs (penalty risk) ·
over-optimized exact-match anchors · ignoring indexation lag when judging impact.

## ICE prioritization
Score each finding: **Impact** (1–5, traffic/revenue potential) ×
**Confidence** (0–1, how sure the fix works) ÷ **Effort** (1–5, dev/content
cost). Order desc. Surface **quick wins** (high impact, low effort, high
confidence) first — they fund trust for the bigger bets.

## Plan schema (what seo-strategist emits to plan.md)
Each step is a delegatable unit:
- `step_no` · `phase` (Technical | Content | Authority | Analytics) ·
  `agent` (which specialist) · `title`
- `description` — what to do, concretely
- `tags` — e.g. `[crawl, indexation]`, `[on-page, schema]`, `[links]`
- `acceptance` — verifiable done-conditions (status 200, valid JSON-LD, canonical
  self-referential, sitemap lists it, position tracked…)
- `quality_bar` — the standard (white-hat, no regressions, mobile-first)
- `depends_on` — step numbers that must finish first
- `metric` — the KPI this moves (impressions, position, CTR, indexed count, CWV,
  organic sessions/conversions) + how it's measured
- `ice` — {impact, confidence, effort, score}

## Verification (per step — never trust "done")
Prove it: fetch the page (status + rendered HTML), validate structured data,
confirm canonical/hreflang/robots/sitemap, check no Core Web Vitals regression,
and for on-site code run `verification-protocol`. Record baseline BEFORE and
measure AFTER via `seo-analyst` — and state the indexation lag (weeks) so nobody
judges impact too early.
