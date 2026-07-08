# SEO system (`ai-agents-seo`)

Claude Code marketplace for the **SEO** profile. Sibling of `full_stack_sm` (dev)
and `marketing_sm` (digital marketing). Only one profile is active at a time —
switch with `../switch-profile.sh seo` (see `../profiles/`).

The `seo` profile also loads the shared base (`hermes-core`, `hermes-verify` from
`ai-agents-config`), so orchestration, scratchpad handoff, session-handoff and
quality gates work exactly like the dev system.

## The team (5 plugins)

| Plugin | Agent | Owns |
|---|---|---|
| `seo-core` | **seo-strategist** | audit direction, ICE prioritization, the plan (+ `/seo-audit`, `seo-methodology` skill) |
| `seo-technical` | **technical-seo-engineer** | crawl, index, sitemaps, robots, canonical, hreflang, redirects, JSON-LD, Core Web Vitals (+ `technical-seo-audit` skill) |
| `seo-content` | **content-strategist** | keyword/intent research, SERP analysis, clusters, briefs, on-page, internal linking, E-E-A-T (+ `keyword-research` skill) |
| `seo-authority` | **link-authority-strategist** | backlink profile, link-building, digital PR, anchors, disavow (white-hat) |
| `seo-analytics` | **seo-analyst** | GSC/GA4, rank tracking, impact measurement, forecasting, reporting (+ `seo-reporting` skill) |

## Orchestration

`seo_sm/CLAUDE.md` is the SEO orchestrator doc (analogous to
`full_stack_sm/CLAUDE.md`): work cycle, who-to-call table, hard rules
(white-hat, data-grounded, don't break what ranks, prod changes gated), model
tiering. Start a project with **`/seo-audit "<domain / task>"`**.

## Method (skills)

- `seo-methodology` — audit layers L0–L8 → anti-pattern prediction → ICE
  prioritization → plan schema (each step: agent/tags/acceptance/metric/deps).
- `technical-seo-audit` — the technical checklist + evidence method.
- `keyword-research` — intent classification → SERP reading → clusters → brief.
- `seo-reporting` — metric definitions + baseline→change→effect + forecasting.

## Extending

Add domain plugins the same way (e.g. `seo-local`, `seo-ecommerce`,
`seo-international`), or adopt vetted external skills via `/sm-evaluate` +
`skill-guard`, then add the plugin name to `../profiles/seo.json` `enabledPlugins`.
