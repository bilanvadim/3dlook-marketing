---
name: technical-seo-audit
description: The technical-SEO checklist and evidence method — how to verify crawl, indexation, sitemaps, robots, canonical, hreflang, redirects, structured data, render and Core Web Vitals with real signals (curl, fetched HTML, validators, GSC/logs). Use when running or reviewing a technical SEO audit, or fixing any crawl/index/render issue.
---

# Technical SEO audit — checklist & evidence

Verify with signals, not assumptions. Every item below is checked by fetching
something real and attaching the result.

## 1. Crawl & access
- `robots.txt`: reachable, not blocking important paths, references sitemap.
- Status codes: key pages return 200; no soft-404s; 4xx/5xx inventory.
- Redirects: `curl -IL` — no chains (>1 hop) or loops; 301 (permanent) not 302
  for moves.
- Crawl budget: parameter/faceted URL explosion, infinite spaces, orphan pages.

## 2. Render & indexability
- JS dependency: compare raw HTML (`curl`) vs rendered DOM — is primary content
  and are links present without JS? Prefer SSR/SSG for indexable content.
- `noindex` / `Disallow` audit: nothing important is excluded by accident.
- Canonical: self-referential on canonical pages; consistent (absolute URL,
  matches sitemap, one per page).

## 3. Sitemaps
- `sitemap.xml` valid, lists canonical 200 URLs only (no redirects/404/noindex),
  under size limits, referenced in robots + submitted in GSC, `lastmod` accurate.

## 4. Internationalization
- `hreflang`: reciprocal, valid language-region codes, `x-default` set, matches
  canonical, no conflicts.

## 5. Structured data
- JSON-LD present for the page type (Article, Product, FAQ, Breadcrumb, Org…),
  valid (Rich Results test / schema validator), truthful (matches visible
  content), no spammy markup.

## 6. Core Web Vitals & performance
- LCP, INP, CLS from field data (CrUX/GSC) + lab (Lighthouse/PSI). Attribute the
  bottleneck (render-blocking, image weight, layout shift, main-thread) and give
  the specific fix. Mobile-first.

## 7. Architecture signals
- Crawl depth of key pages (≤3 clicks), internal links to money pages, breadcrumb
  trail, pagination handling.

## Evidence to capture (per finding)
The command/tool run, its output (status/snippet/validation verdict), severity,
the fix, and the metric it moves. Prefer reproducible checks:
`curl -IL <url>`, `curl -s <url> | grep -i canonical`, PSI/Lighthouse run, GSC
export, log-file sample.

## Guardrails
Never let a fix deindex value; migrations carry a 301 map + internal-link update;
validate structured data before shipping; measure CWV before/after; prod changes
(robots, live canonical/redirects, sitemap) are proposed and gated for human ok.
