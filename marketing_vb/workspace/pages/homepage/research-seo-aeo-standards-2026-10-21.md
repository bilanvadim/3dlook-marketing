# Homepage standards: SEO, structured data, AEO, accessibility, UX (sources fetched 2026-10-21)

Research for the new 3DLOOK homepage. **MUST** = law, standard, or documented as required by the platform.
**SHOULD** = documented best practice or strong evidence. **OPTIONAL** = cheap, marginal or unproven.

## Changes in 2025–26 that matter

- **FAQ rich results are gone.** Google stopped showing them on 7 May 2026 and removed the docs on 15 Jun 2026. https://developers.google.com/search/updates
- **Google treats "AEO/GEO" as SEO.** Its May 2026 AI optimization guide says Search does not use llms.txt, and AI features need no "chunking" and no special schema. https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- **Search Console "Search generative AI" setting** can remove a site from AI Overviews and AI Mode; rolled out to all sites by 31 Aug 2026, default Include. https://support.google.com/webmasters/answer/16908024
- Sitelinks search box retired 21 Nov 2024; breadcrumbs in results are desktop-only since Jan 2025.

## Live 3dlook.ai check (curl, 2026-10-21)

- Title "3DLOOK - AI-powered 3D body scanning solution"; one H1 "Real-Time Health & Fitness Insights, Powered by AI" (no category term); self canonical; no hreflang.
- Yoast `#organization`: 146 px logo, 5 sameAs; no description, contactPoint or Crunchbase. `#website` carries an unused SearchAction (harmless). One-item BreadcrumbList.
- GPTBot user agent → 403; OAI-SearchBot, PerplexityBot, ClaudeBot → 200. robots.txt blocks none of them (nginx/WAF). The test IP is not OpenAI's, so part of this may be IP verification.
- `/llms.txt` live. **No Wikidata item.**

## 1. Technical SEO

- **MUST** Title = brand + category. Google allows a short site description in a homepage title and rewrites vague or stuffed titles. https://developers.google.com/search/docs/appearance/title-link
- **MUST** One visible H1 with "3D body scanning" (feeds title links; one H1 is for clarity and screen readers). https://developers.google.com/search/docs/fundamentals/seo-starter-guide · https://www.w3.org/WAI/tutorials/page-structure/headings/
- **SHOULD** One H2 per section, no skipped levels; Microsoft says headings mark idea boundaries when AI parses a page. https://about.ads.microsoft.com/en/blog/post/october-2025/optimizing-your-content-for-inclusion-in-ai-search-answers
- **SHOULD** Site-level meta description (definition + products); no length limit, truncated by device width. https://developers.google.com/search/docs/appearance/snippet
- **MUST** Plain `<a href>` links from the body (not only the nav) to each product parent, with descriptive anchors. https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- **SHOULD** Short, consistent product titles and nav labels (the only documented sitelink levers). https://developers.google.com/search/docs/appearance/sitelinks
- **MUST** "3DLOOK" spelled identically in title, og:site_name, WebSite.name and hero (site names). https://developers.google.com/search/docs/appearance/site-names
- **OPTIONAL** Drop the homepage's one-item BreadcrumbList (a trail needs 2+ items). https://developers.google.com/search/docs/appearance/structured-data/breadcrumb
- **MUST** Absolute canonical `https://3dlook.ai/`, 301s from variants, the same URL in the sitemap. https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- hreflang not needed (one English version); **MUST** `<html lang="en">` (WCAG 3.1.1).
- **MUST** Good Core Web Vitals at p75: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1. https://web.dev/articles/vitals
- What usually breaks them on WordPress: hero video (use a light poster + `fetchpriority="high"`, YouTube behind a facade), sliders and page-builder heroes ("Never lazy-load your LCP image"; one static `<img>` hero), logo marquees (static grid, width/height on every logo), cookie banner/popups/chat (overlay, facade, no full-page interstitials), page-builder CSS/JS and fonts. https://web.dev/articles/optimize-lcp · https://web.dev/articles/optimize-cls · https://developers.google.com/search/docs/appearance/avoid-intrusive-interstitials

## 2. Structured data

- **MUST** Extend Yoast's single @graph through `wpseo_schema_graph*` filters and reuse its @ids; never a second Organization block. https://developer.yoast.com/features/schema/functional-specification/
- **MUST** Organization on the homepage. Google requires no property and recommends all that apply: name, alternateName, url, description, sameAs, contactPoint, address, foundingDate, numberOfEmployees, legalName (if different), logo ≥ 112×112, iso6523Code. https://developers.google.com/search/docs/appearance/structured-data/organization
- **MUST** WebSite with name, alternateName, url (site names). SearchAction is ignored and harmless. https://developers.google.com/search/blog/2024/10/sitelinks-search-box
- **MUST** Mark up only what is visible on the page. https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- **SHOULD** SoftwareApplication/Product on the product pages, each with a stable @id the homepage can point to. SoftwareApplication rich results need `offers.price` plus a rating or review; never invent ratings. https://developers.google.com/search/docs/appearance/structured-data/software-app
- **OPTIONAL** ItemList / OfferCatalog pointing at the product @ids: no rich result (carousels cover only Course, Movie, Recipe, Restaurant); it only makes the product list machine-readable.
- **FAQ:** visible Q&A block = SHOULD (Microsoft: assistants lift Q&A pairs "word for word"); FAQPage markup = OPTIONAL (Bing: may support clearer grounding, no guarantee; Google: AI features need no special schema). https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a

## 3. AEO / GEO

| Token / control | Governs | Action |
|---|---|---|
| Googlebot | Search, including AI Overviews and AI Mode | MUST allow |
| GSC "Search generative AI" | AI Overviews, AI Mode | MUST keep Include |
| Google-Extended | Gemini training and grounding in Gemini Apps/Vertex; not Search | SHOULD allow |
| OAI-SearchBot | ChatGPT search answers | MUST allow |
| GPTBot | Training only; settings are independent | business choice (3DLOOK decided 09-27: allow) |
| ChatGPT-User / Perplexity-User / Claude-User | User-triggered fetches | allow |
| PerplexityBot | Perplexity search | MUST allow |
| Claude-SearchBot / ClaudeBot | Claude search / training | allow Claude-SearchBot |
| Applebot / Applebot-Extended | Siri, Spotlight / training | allow Applebot |
| Bingbot | Bing and Copilot | MUST allow; IndexNow |

Sources: https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers · https://developers.openai.com/api/docs/bots · https://docs.perplexity.ai/guides/bots · https://support.claude.com/en/articles/8896518 · https://support.apple.com/en-us/119829
If a Cloudflare CDN is ever added: from 15 Sep 2026 blocking "Training" there also blocks crawlers that do both search and training (Googlebot, Bingbot, Applebot). https://blog.cloudflare.com/content-independence-day-ai-options/

**Documented by the platforms:** Google: eligibility = indexed + snippet allowed; important content as text, structured data matching the page, first-hand "non-commodity" content, no pages per fan-out query. https://developers.google.com/search/docs/appearance/ai-features · ChatGPT rewrites a prompt into several queries; referrals carry `utm_source=chatgpt.com`. https://help.openai.com/en/articles/9237897-chatgpt-search · Microsoft scores sections, wants titles matching the H1, Q&A pairs, lists and tables; may skip facts hidden in tabs, PDFs or images.

**Study evidence (not platform documentation):** Pew 2025: clicks in 8% of searches with an AI summary vs 15% without. Ahrefs 2025: ~12% of URLs cited by AI assistants rank top-10 for the prompt (ChatGPT ~8%, AI Overviews 76%). Ahrefs (75k brands): branded web mentions correlate with AI Overview visibility at ρ=0.664 vs DR 0.326 (correlation). GEO paper (KDD 2024): quotations, statistics and cited sources +22–41% visibility in a lab setting. Vercel: GPTBot, ClaudeBot and PerplexityBot don't run JavaScript. Ahrefs (137k domains): 97% of llms.txt files got zero requests in May 2026.

**Checklist:**
- **MUST** All homepage copy in the server HTML; no key fact only in a slider, tab, image or PDF.
- **MUST** One definition sentence, word for word everywhere (hero/FAQ, About, Organization.description, LinkedIn, Crunchbase, G2, boilerplate, llms.txt).
- **SHOULD** "What is 3D body scanning?" answer block, 3-step "How it works", a comparison table (phone scan vs booth scanner vs tape measure) for the "3d body scanner/scanning" queries. Expect citations more than clicks.
- **SHOULD** Publish only numbers with a public source that are already approved.
- **SHOULD** Wikidata item (needs "serious and publicly available references", disclose the conflict of interest), then add it and Crunchbase to sameAs. https://www.wikidata.org/wiki/Wikidata:Notability
- **SHOULD** Earn genuine mentions (PR, partners, reviews).
- **OPTIONAL** Keep llms.txt, but rewrite instruction-like lines ("Do not infer…") as plain facts; Bing treats content "designed to manipulate… language models" as abuse. https://llmstxt.org/
- **Unproven, skip:** llms.txt as a citation lever, "chunking", AI-only page versions, schema as an AI ranking factor, vendor "AI visibility scores".

## 4. Accessibility and legal

**WCAG 2.2 AA** (W3C Recommendation, 5 Oct 2023), all MUST: 1.1.1 alt text (logo alt = company name) · 1.2.2 captions · 1.4.3 / 1.4.11 contrast 4.5:1 text, 3:1 UI and focus · 1.4.10 reflow at 320 px · 2.1.1 / 4.1.2 keyboard and state for menus · 2.2.2 pause/stop/hide for anything moving > 5 s · 2.4.4 link purpose · 2.4.7 + 2.4.11 visible focus not hidden by sticky header or cookie banner · 2.5.8 targets ≥ 24×24 px · 3.2.6 consistent help · 1.3.5 / 3.3.2 form labels and autocomplete. https://www.w3.org/TR/WCAG22/

**European Accessibility Act:** covers listed services provided to consumers after 28 Jun 2025; a B2B-only homepage with a demo form is most likely outside direct scope (researcher's reading; confirm with counsel). EU clients who embed scans in consumer apps are in scope and will push requirements onto the scan UI; EN 301 549 (WCAG 2.1 AA) is the presumption of conformity. https://eur-lex.europa.eu/eli/dir/2019/882/oj/eng · US: DOJ says ADA Title III covers business websites. https://www.ada.gov/resources/web-guidance/

**Cookies:** MUST consent before non-essential cookies (ePrivacy 5(3)); no cookie wall; scrolling ≠ consent; withdrawal as easy as consent, so a permanent "Cookie settings" link in the footer. MUST (GA4/Ads on EEA traffic) Consent Mode v2 with all four signals and defaults before any tag fires. https://developers.google.com/tag-platform/security/guides/consent · SHOULD banner as an overlay, keyboard-operable, never covering focus.

## 5. Conversion and UX (Nielsen Norman Group)

- MUST What 3DLOOK is, who it's for and the primary CTA above the fold (~57% of viewing time above the fold, 74% within two screens). https://www.nngroup.com/articles/homepage-design-principles/ · https://www.nngroup.com/articles/scrolling-and-attention/
- MUST Logo top left, linking home. MUST One dominant primary CTA, one secondary.
- SHOULD One card per product (outcome, audience, link) in a grid that takes new products.
- SHOULD Mega menu grouped by product and industry: short labels, key word first, ~0.5 s hover delay, keyboard support. https://www.nngroup.com/articles/mega-menus-work-well/
- SHOULD Pricing in the main nav (price was B2B users' most-wanted information). https://www.nngroup.com/articles/b2b-vs-b2c/
- SHOULD Serve "users" (engineers: API docs, SDKs, compliance) and "choosers" (executives: ROI, cases).
- SHOULD Logos only with permission, in a static grid; testimonials with name and title.
- MUST NOT Auto-rotating hero carousel. https://www.nngroup.com/articles/auto-forwarding/
- SHOULD Labelled mobile "Menu" button; minimal autoplay and motion; no popups except legally required ones.

**Not read directly:** OpenAI publisher FAQ (403, search-index text used); EDPB 05/2020 (dead PDF, law-firm summaries); EN 301 549 → WCAG 2.1 (Deque); Microsoft October 2025 guidance is a blog post, not formal documentation.
