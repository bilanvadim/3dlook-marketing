# 3dlook.ai — site inventory and architecture rules

The Site Blueprint this skill treats as an input. It is a **snapshot taken 2026-08-23** from
`https://3dlook.ai/page-sitemap.xml` plus a live read of two use-case pages. Re-pull the sitemap
before trusting it for a placement decision:

```bash
curl -s -A "Mozilla/5.0" https://3dlook.ai/page-sitemap.xml | grep -oE '<loc>[^<]+' | sed 's|<loc>https://3dlook.ai/||' | sort
```

Blog articles are **not** in this file. They live in
`brand-assets/content-strategy/published-articles-inventory.md` (156 articles, mapped to hubs) and
are governed by `content-plan.md`. Marketing pages and articles are two different inventories; do
not mix them when checking cannibalisation — check both.

---

## Current pages — 30, grouped by job

### Product and use-case pages

| URL | Product | Job | State |
|---|---|---|---|
| `/` | FX | Homepage **and the FitXpress parent page** | `/fitxpress/` 301s here |
| `/technology/` | both | How the tech works, cross-product | — |
| `/mobile-tailor/` | MT | Product parent | has 3 children |
| `/mobile-tailor/for-made-to-measure/` | MT | Use-case page | child of MT |
| `/mobile-tailor/for-on-demand-manufacturing/` | MT | Use-case page | child of MT |
| `/mobile-tailor/for-uniforms/` | MT | Use-case page | child of MT |
| `/fitxpress/for-connected-and-digital-fitness/` | FX | Use-case page | **non-existent `/fitxpress/` path level** — normalise to root |
| `/for-bmi-verification/` | FX | Use-case page | at root, child of `/` — correct pattern |
| `/structured-body-data-for-telehealth-digital-health-programs/` | FX | Use-case page | at root, child of `/`; slug off-pattern, but the best-built page on the site — finding 6 |
| `/pricing/` | both | Public pricing, FX and MT tabs | live figures |

### Proof, resources, conversion

`/case-studies/` (index only — **no individual case-study pages exist**) · `/content-hub/` (blog hub)
· `/content-hub/harnessing-ai-and-3d-tech-to-accelerate-mtm/` · `/content-hub/webinar-2023-ecommerce-trends/`
· `/ebook-the-next-big-leap-in-health/` (gated asset) · `/contact-us/` · `/partners/`

### Company and legal

`/about-us/` · `/careers/` · `/sitemap/` · plus 11 policy and terms pages
(`/privacy-policy/`, `/cookie-policy/`, `/refund-policy/`, `/terms-and-conditions/`,
`/terms-and-policies/`, `/fitxpress-privacy-policy/`, `/fitxpress-customer-terms-conditions/`,
`/mt-customer-terms-conditions/`, `/privacy-notice-for-european-residents/`,
`/privacy-notice-for-california-residents/`).

---

## The architecture gaps — read before placing any page

**1. The homepage is the FitXpress parent.** Confirmed by Vadim, and the site agrees:
`/fitxpress/` **301s to `/`**, the homepage H1 is "Real-Time Health & Fitness Insights, Powered by AI"
(~1,005 words, health-and-fitness positioning rather than neutral corporate), and both root-level FX
vertical pages declare a two-level breadcrumb — `Home → BMI Verification`,
`Home → FitXpress for Telehealth & Digital Health`.

So there are **two hierarchies of different depth, both valid**:

| Product | Parent | Children |
|---|---|---|
| FitXpress | `/` (the homepage) | `/for-{vertical}/` at root |
| Mobile Tailor | `/mobile-tailor/` | `/mobile-tailor/for-{vertical}/` |

A new FitXpress vertical page therefore passes G-A on "the page has a parent", and `/for-{vertical}/`
at root is the correct pattern for it — those two pages are not orphans.

**The one anomaly is `/fitxpress/for-connected-and-digital-fitness/`.** It sits under a `/fitxpress/`
path segment that does not exist and declares a breadcrumb `Home → FitXpress → …` whose middle level
301s to the homepage. That is the page to normalise — move it to `/for-connected-and-digital-fitness/`
with a 301 and a Search Console baseline saved first — not the two root-level pages. Related loose end:
`/fitxpress` without the trailing slash 301s somewhere else entirely,
`/content-hub/fitxpress-admin-panel-launch/`.

**What FitXpress verticals genuinely lack** is an in-body link down from their parent — see the
linking finding below. And the homepage itself carries the same problems the vertical pages do: H2
"Leveraging accurate 3D body data" uses a banned word, and its meta description still sells "a diverse
set of industries" while the H1 sells health and fitness only. Homepage positioning is out of this
skill's scope; the mismatch is recorded here so nobody treats the homepage as a style model.

**2. No individual case-study pages.** `/case-studies/` is an index with nothing under it, while
`brand-assets/product-info/case-studies/` holds six real cases with metrics (Safariland 15.5K
scans/year, Burlington Medical 11.5K, Yazen 34K, UK Meds 7.5K, Jim's Formal Wear 3.2K, Generation
Tux). Every vertical page's proof slot therefore has nowhere to link. Until case-study pages exist,
case cards link to the index and the case detail lives on the vertical page itself — and that
limitation is stated in the handover.

**3. One page carries real schema; the other five do not.** Checked 2026-08-23 across all six
vertical pages plus home, `/technology/`, `/pricing/`, `/mobile-tailor/` and `/case-studies/`:

| Page | Words | FAQPage | Service |
|---|---|---|---|
| `/structured-body-data-for-telehealth-digital-health-programs/` | ~1,613 | **yes, 13 questions** | **yes**, with `audienceType` and `areaServed` |
| `/fitxpress/for-connected-and-digital-fitness/` | ~1,352 | no | no |
| `/for-bmi-verification/` | ~659 | no | no |
| `/mobile-tailor/for-uniforms/` | ~1,224 | no — despite 11 visible FAQ questions | no |
| `/mobile-tailor/for-made-to-measure/` | ~1,201 | no | no |
| `/mobile-tailor/for-on-demand-manufacturing/` | ~1,163 | no | no |
| home, technology, pricing, mobile-tailor, case-studies | — | no | no |

Everything except the telehealth page runs Yoast's default `WebPage` / `Organization` /
`BreadcrumbList` graph only. Two consequences: `/mobile-tailor/for-uniforms/` has eleven answers that
are invisible to AI search, and there is already a **working in-house template** to copy from — the
telehealth page. Every page this skill builds ships FAQPage plus Service schema, modelled on it.

**4. The live pages break the current guardrails.** Observed 2026-08-23:
`/for-bmi-verification/` runs H2 "Leveraging accurate 3D body data" and "Get the best-in-class tech"
— `leverage` is banned by CLAUDE.md §6 and "best-in-class" is an anti-positioning violation.
`/mobile-tailor/for-uniforms/` runs H2 "Revolutionize Your Uniform Fitting Process" — `revolutionize`
is banned. Both pages predate the guardrails. Treat them as rewrite candidates, not as style models,
and never copy their phrasing into a new page.

**5. `/for-bmi-verification/` is the outlier.** ~659 words, no FAQ, no case cards, no customer
quote — roughly half of every other vertical page on the site. It is the first rewrite candidate.

**6. The benchmark to build against is already on the site.**
`/structured-body-data-for-telehealth-digital-health-programs/` (published 2026-07-16, modified
2026-07-24) is the one vertical page written to the current standard: a scoped-accuracy H2
("repeatability over a single number"), a three-way comparison block ("FitXpress vs. in-clinic scans
vs. consumer photo apps"), a 13-question FAQ with FAQPage schema, Service schema carrying
`audienceType` and `areaServed`, and no banned words in its headings. Read it before drafting. Its one
flaw is the slug: it sits at root with a non-pattern address instead of under a FitXpress parent.

---

## URL rules

- FitXpress use-case page: `/for-{vertical}/` at root, because the homepage is the parent.
- Mobile Tailor use-case page: `/mobile-tailor/for-{vertical}/`.
- Do not invent a `/fitxpress/` path level. It 301s to the homepage, and the one page that uses it
  carries a breadcrumb pointing at nothing.
- One vertical, one address. A campaign duplicate is a landing page at its own URL, never a copy of
  the use-case page.
- Latin slug, no dates, no numbers, no parameters. Canonical to self — never to the parent.
- A URL change means 301s plus a Search Console baseline saved first. Never rename silently.

## Internal linking — four directions, all mandatory

Per `brand-assets/content-strategy/content-strategy-guidelines.md`:

1. **Up** — to the parent: `/` for FitXpress, `/mobile-tailor/` for Mobile Tailor.
2. **Sideways** — to two sibling verticals of the same product.
3. **To the hub article** for this vertical in the content hub (from
   `published-articles-inventory.md`), plus one supporting article.
4. **Down / across to conversion** — `/pricing/`, `/case-studies/`, and the relevant gated asset.

And the reverse: the parent must link **down** to every vertical page it owns.

**Known gap:** neither parent does this in the body today. The homepage links its three FitXpress
verticals only through the header's "Use Cases" dropdown — zero in-body links — and `/mobile-tailor/`
links its three children the same way. Site-wide navigation is a real link, so this is not a G-A
failure, but a vertical block on the parent is the missing piece, and it is worth requesting in the
handover for every new page: one card, in the body, on the parent.

## Pricing — what may appear on a page

`/pricing/` is public and carried real figures on 2026-08-23:

| Product | Tiers as published |
|---|---|
| FitXpress | Starter $1,000/mo (up to 500 scans) · Pro $1,500/mo (up to 1,000 scans) · Personalized custom |
| Mobile Tailor | Basic $499/mo (up to 100 scans) · Premium $999/mo (up to 500 scans) · Enterprise custom |

Rules:

- A vertical page names the entry tier and links to `/pricing/`. Silence about money reads as
  "expensive and evasive" and loses the buyer before the form.
- **Never** publish the internal per-request rates from `brand-assets/product-info/pricing.md`.
- **Never** publish Mobile Tailor customer ARRs. They are sales-anchoring figures, full stop.
- **Known conflict:** `pricing.md` states Mobile Tailor pricing is "custom (enterprise contract)"
  while `/pricing/` publishes $499 and $999 MT tiers, and its FitXpress volume table does not match
  the published tiers either. Per guardrail #2 this conflict is never averaged and never silently
  resolved — take the figure from the live page, and put the discrepancy in Open items so `pricing.md`
  gets re-synced.

## Platform facts

WordPress with Yoast SEO (`post-sitemap.xml`, `page-sitemap.xml`, `job-sitemap.xml`). Yoast owns the
meta title, description, canonical and the base schema graph. Titles ≤ 60 characters, descriptions
≤ 155. Publishing happens outside this pipeline — see `handoff-kit.md`.
