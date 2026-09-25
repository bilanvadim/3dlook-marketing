# 3dlook.ai on-site SEO / IA audit: how well the site can rank FitXpress for health & fitness terms

Crawled 2026-09-25, read-only. All 194 sitemap URLs were fetched one at a time with curl, a Chrome User-Agent and a 0.8 s pause between requests. Every response was a real 200: no 503s and no 592-byte bodies, so no retries were needed. Raw data is in `scratchpad/crawl/`, parsed per-page data in `parsed.json`, the link graph in `graph.json` / `graph.txt`, and the per-page detail for 23 key pages in `keypages.md`.

"Editorial inlinks" means `<a href>` links in page content. Links in the header nav, the footer and the sitewide "latest posts" widget (`div.d-posts`) are excluded. The HTML `/sitemap/` page is counted, so an inlink count of **1** usually means the page is reachable *only* from `/sitemap/`.

---

## 0. Headline verdict

The health **content** layer is now strong: about 15 recent hubs and cluster posts of 2,000–4,700 words each, with FAQPage schema, self-canonicals, and links to the trust FAQ and the accuracy framework. The **commercial / product layer** that this content should feed is thin and structurally disconnected:

- There is no FitXpress product page. `/fitxpress/` 301s to `/`, and `/fitxpress` (no slash) 301s to a 2026 *blog post* (`/content-hub/fitxpress-admin-panel-launch/`).
- There are only 3 FitXpress use-case pages, and none of them has a single crawlable body link out. Their CTAs are JS buttons or modals.
- The homepage body has exactly **one** crawlable link, to `/contact-us/`.
- There is no indexable developer or API page on 3dlook.ai. The docs live on a separate domain (`docs.fitxpress.3dlook.me`) and are linked once, with nofollow.
- None of these verticals has a landing page: GLP-1, online pharmacy, insurance, wellness, occupational health, clinical trials, bariatric. Each is served only by a `/content-hub/` blog post.
- The site as a whole is still about two-thirds fashion/apparel by URL count. The sitewide mega-menu promos, the case-study library and the internal-link equity all lean toward Mobile Tailor and fashion.

---

## 1. Inventory and classification (194 sitemap URLs)

Yoast sitemaps: `post-sitemap.xml` 160, `page-sitemap.xml` 31, `job-sitemap.xml` 3. The index is at `/sitemap_index.xml`.

| Class | Count | Notes |
|---|---|---|
| Homepage | 1 | Leads with **FitXpress / health & fitness** (details below) |
| FitXpress use-case pages | 3 | `/structured-body-data-for-telehealth-digital-health-programs/`, `/fitxpress/for-connected-and-digital-fitness/`, `/for-bmi-verification/` |
| Mobile Tailor pages | 4 | `/mobile-tailor/` plus `/for-made-to-measure/`, `/for-on-demand-manufacturing/`, `/for-uniforms/` |
| Wrist | 1 | `/wrist-measurement/`: 162 words, **no meta description**, yet sits in the main-nav "Use Cases" group next to the FitXpress pages |
| Corporate | 8 | pricing, technology, about-us, partners, contact-us, case-studies, content-hub, ebook landing |
| Legal / utility | 11 | privacy ×4, terms ×3, cookie, refund, terms-and-policies, HTML sitemap. The trust FAQ lives under `/content-hub/` |
| Careers | 4 | |
| Blog posts: health / fitness / body-comp | ~53 | about 15 are the 2026 strategy hubs and clusters. The rest are 2023–25 TOFU and comparison posts plus a few old news items |
| Blog posts: fashion / apparel / uniforms / corporate news | ~107 | about 2 : 1 against health |

**Missing page types (checked by URL guess and link scan):**
- **FitXpress product/overview page:** none. `/fitxpress/` → 301 → `/`. The Yoast breadcrumb on `/fitxpress/for-connected-and-digital-fitness/` still points its "FitXpress" crumb at `https://3dlook.ai/?page_id=36425`, which **returns 404**.
- **Pricing:** `/pricing/` exists and covers both products. In the DOM the Mobile Tailor plans (Basic $499 / Premium $999 / Enterprise) come first, then FitXpress (Starter $1,000 / Pro $1,500 / Personalized). The Mobile Tailor FAQ also comes before the FitXpress FAQ. The content is duplicated twice (desktop and mobile), and an H2 "Our Pricing" appears before the H1. The nav "Pricing" link under Mobile Tailor is `/pricing/?mt`. The page has no Product/Offer schema.
- **API / developer docs:** `/api/` and `/developers/` return 404. The real docs are `https://docs.fitxpress.3dlook.me/` ("FitXpress API Reference", a Slate page), on a **different registrable domain**. On 3dlook.ai they are linked once, from the trust FAQ, with `rel="nofollow"`. The product pages and pricing page mention "API access + Web & Mobile SDKs" but never link to the docs.
- **Per-industry landing pages:** telehealth (1 page), connected fitness (1), BMI verification (1). There are **no** pages for GLP-1 / weight-loss programs, online pharmacy, insurance, employer wellness, occupational health, clinical trials or bariatric. Those intents are carried only by blog posts. Guessed URLs such as `/fitxpress/for-insurance/`, `/health/` and `/category/health/` all return 404.
- `/fitxpress/for-telehealth-and-weight-loss/` 301s to the telehealth page, but **llms.txt still lists the old URL**.

**What the homepage leads with:** FitXpress and health.
- H1: "Real-Time Health & Fitness Insights, Powered by AI". Hero eyebrow "FitXpress". Mobile Tailor is not mentioned once in the body.
- The **title and meta description are generic and fashion-era**:
  - title: "3DLOOK - AI-powered 3D body scanning solution"
  - description: "…specializing in mobile body scanning and visualization for a diverse set of industries."
  - Neither mentions FitXpress, BMI, body composition, telehealth or API.
- Structured data is only Yoast's default WebPage/Organization. There is no SoftwareApplication or Product schema, and the `Organization` node has no description.
- Homepage JSON-LD dateModified is 2025-08-29.

---

## 2. Key-page metrics (full per-page detail in `keypages.md`)

| Page | Words | Title / H1 | Schema beyond Yoast default | Editorial inlinks | Body outlinks | CTA |
|---|---|---|---|---|---|---|
| `/` | 1,005 | generic title; H1 health | none | 64 | **1** (contact) | "Let's talk" |
| `/structured-body-data-for-telehealth-digital-health-programs/` | 1,610 | "Remote Body Measurement & Progress Tracking for Telehealth" / H1 "Structured Body Data for Telehealth & Digital Health Programs" | **Service + FAQPage** (the only product page with them) | 17 | **0** | "Book a demo" (JS) |
| `/fitxpress/for-connected-and-digital-fitness/` | 1,352 | "FitXpress for Connected & Digital Fitness - 3DLOOK" | none. Breadcrumb crumb → 404 | 8 | **0** | "Request a demo" (JS) |
| `/for-bmi-verification/` | **659** | "FitXpress for Weight & BMI verification" / H1 "AI-Powered Weight Validation for Regulatory Compliance" | none | 12 | **0** | "Get Started" / "Request a Demo" (JS) |
| `/pricing/` | 2,260 | "3DLOOK Pricing \| FitXpress & Mobile Tailor Plans" | none (no Offer/FAQ) | 34 | 0 | trial / demo |
| `/technology/` | 1,134 | "Our Technology - 3DLOOK" | none | 6 | 1 | "Contact us" |
| `/about-us/` | 1,510 | "About Us - 3DLOOK" | AboutPage, FAQPage, Service | **1** | 15 | "Book a Consultation" |
| `/case-studies/` | 459 | 1 health case (Tera Science) vs 6 fashion/uniform | none | 6 | 7 | none |
| `/content-hub/` | 461 | shows the 10 latest posts only | none | 2 | 7 | none |
| `/content-hub/ai-body-data-health-hub/` (main hub) | 2,040 | "Verified Body Data Across Health Programs — FitXpress Guide" | Article, FAQPage | 9 | 14 | eBook + demo |
| `/content-hub/glp-1-market/` | 2,572 | | Article, FAQPage | 10 | 8 | |
| `/content-hub/the-potential-of-ai-in-telehealth/` | 3,471 | | Article, FAQPage | 8 | 8 | |
| `/content-hub/ai-in-fitness-industry/` | 4,116 | | Article, FAQPage | 8 | 7 | |
| `/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/` | 2,838 | | Article, FAQPage | 6 | 10 | demo |
| `/content-hub/mobile-body-scanning-insurance-underwriting/` | 2,834 | | Article, FAQPage | 5 | 6 | |
| `/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/` | 3,321 | | Article, FAQPage | 4 | 12 | |
| `/content-hub/occupational-health-screening-software/` | 4,076 | | Article, FAQPage | 4 | 6 | demo |
| `/content-hub/clinical-trial-anthropometric-measurement-software-obesity-trials/` | 4,696 | | Article, FAQPage | **2** (main hub + sitemap) | 7 | |
| `/content-hub/ai-body-data-wellness-platforms/` | 2,354 | | Article, FAQPage | 3 | 10 | |
| `/content-hub/mobile-body-scanning-accuracy/` | 4,062 | | Article, FAQPage | 13 | 4 | |
| `/content-hub/fitxpress-data-privacy-security-regulatory-faq/` | 4,590 | | Article + **broken FAQPage JSON-LD** | 16 | 10 | |
| `/content-hub/top-7-remote-body-composition-tools-glp-1-clinics/` | 3,890 | | Article, FAQPage | **1 (sitemap only)** plus the rotating widget | 20 | |
| `/content-hub/case-study-tera-science/` | 996 | | Article | 2 | 1 | |

**Checks that hold across all 194 URLs:**
- Every page is self-canonical. The two canonical bugs noted on 09-17 are fixed.
- No page is noindex. Every page has exactly one H1.
- Every page has og:image and a Twitter card.
- No page has hreflang (the site is English only, so that is fine).
- Only `/wrist-measurement/` lacks a meta description.
- Eleven titles run past about 65 characters, and all of them are fashion or old posts.
- Image alt coverage looks fine by count (53 missing out of about 11.8k `<img>`), **but** the homepage "Trusted by" logo strip carries AI-generated junk alt text that misidentifies the customers:
  - the Healthyr logo is described as "Reddit… alien mascot"
  - the Verv logo as "vevo"
  - the Warrior logo as "A Dannebrog flag, perfect for home decor… Consider adding this timeless piece to your home in 2025"
  - "Fitexpress" is misspelled
  - About 17 such alts sit across 6 pages.
- Health customer proof (UK Meds, Yazen, Healthyr) exists **only as logo images**, on the telehealth page, the fitness page and pricing. None has a case study.

**Author signals:**
- Post schema `Person` names include **"admin"** (32 posts), a raw email **"[staff email @3dlook.me]"** (13 posts, 12 of them health or body-comp, e.g. `/content-hub/glp-1-compliance-challenge/`, `/content-hub/beyond-bmi-business/`, `/content-hub/bia-scan/`, `/content-hub/case-study-tera-science/`), "[personal gmail]" (1) and "Nadya" (13).
- No `Person` has a `url`, because author archives are 404.
- The visible author box on the 2026 hubs reads "By Assel Sekerova — Marketing professional with over 10 years of experience…", with no link. There is no health or clinical credential and no medical or scientific reviewer anywhere on the site.

---

## 3. Technical

- **Stack:** WordPress with a custom theme (`/wp-content/themes/3dlook/`), Elementor, Yoast SEO and WP Rocket 3.22. nginx serves directly, with no CDN header seen.
- **HTTPS and redirects:** HSTS with preload is on.
  - `http://3dlook.ai` → 301 → https (1 hop)
  - `https://www.3dlook.ai` → 301 → apex
  - **`http://www.3dlook.ai/` → 404** (no redirect)
  - `/blog/` → 301 → `https://3dlook.me/content-hub/` → 301 → `https://3dlook.ai/content-hub/` (a **2-hop chain via the legacy domain**)
  - `3dlook.me` → 301 → 3dlook.ai
  - The legacy domain `3dlook.me` is still referenced in CSS on every page (e.g. the hero background `3dlook.me/wp-content/uploads/2021/03/file_main.png`)
- **Performance (194 sequential fetches):**
  - TTFB averages 0.70 s (max 1.41 s), and total HTML fetch averages 1.21 s.
  - HTML averages **~320 KB uncompressed** (about 66 KB gzipped on the homepage) because of inlined WP Rocket CSS and SVG.
  - Pages carry 50–100 `<img>` each.
  - HTML responses have no Cache-Control header.
- **Mobile:** `viewport` is `width=device-width,minimal-ui` on every page, with no `initial-scale=1`. This is fine.
- **robots.txt** is served by the "Virtual Robots.txt" plugin.
  - `User-agent: *` gets `Allow: /` only. OAI-SearchBot, GPTBot, Google-Extended and ClaudeBot each get `Allow: /`.
  - All the `Disallow` lines (`/?`, `/?s=*`, `/wp-admin/`, `/author/`, `*utm*=`…) sit **after `User-agent: anthropic-ai` and bind only that bot**. This **confirms** the known issue: Googlebot and every other bot can crawl `?s=` search, `?page_id=`, utm URLs and `/wp-admin/`.
  - The `Sitemap:` directive is present, but the file ends without a trailing newline. That is minor.
- **AI-crawler reality differs from robots.txt:**
  - **nginx returns 403 to any User-Agent containing "GPTBot"**, even for `/robots.txt`, although robots.txt says `Allow`.
  - ClaudeBot, PerplexityBot (not named in robots, so it falls under `*`), OAI-SearchBot, ChatGPT-User, Google-Extended, Googlebot and Bingbot all get 200.
  - Net effect: ChatGPT search and browse can read the site, but OpenAI's training crawler cannot. That is fine if intended, but it contradicts robots.txt.
- **llms.txt** is present (20.9 KB, "Last updated: 2026-06-15") but **stale**:
  - It lists 110 URLs but **none of the 2026 P0 hubs**: `ai-body-data-health-hub`, `mobile-body-scanning-accuracy`, `fitxpress-data-privacy-security-regulatory-faq`, `occupational-health-screening-software`, `clinical-trial-…`, `ai-body-data-wellness-platforms`, `top-7-…glp-1`, `remote-body-measurement-online-fitness-coaching`, `mobile-body-scanning-patient-engagement`.
  - It lists 2 URLs that 301: `/fitxpress/for-telehealth-and-weight-loss/` and the old IEEE post.
  - `llms-full.txt` returns 404.
- **Content-hub crawlability:**
  - `/content-hub/` renders only the 10 latest posts.
  - The topic filters (Health, Fitness…) are `<span>` form controls, not links.
  - There are no pagination links. `/content-hub/page/2/` returns 200 but canonicals to `/content-hub/`.
  - As a result the only HTML crawl path to about 60 posts is the `/sitemap/` HTML page (168 content-hub links) plus the XML sitemap.
- **Structured-data defect:** on `/content-hub/fitxpress-data-privacy-security-regulatory-faq/`, the hand-inserted FAQPage JSON-LD (14 KB) is **invalid JSON**, because WordPress wpautop injected `<br />` into the script (`<br />\n{<br />\n "@context"…`). The FAQ rich result and schema are lost on the most important trust asset.
- **Sitewide chrome:**
  - The mega-menu on all 192 non-home pages promotes two **fashion items**: the Safariland body-armour case study and the Digiday "Best In-Store Technology" award.
  - The footer's "FitXpress" link points to `/`.
  - The footer shows a "HIPAA Compliant" badge (alt text "…'HIPAA Compliant'…") on every page.
  - The homepage body says "GDPR & HIPAA Compliant… never link photos to personal identifiers". That contradicts the trust-FAQ wording rules (compliance.md treats "HIPAA compliant" and "no personal identifiers" as hard fails).
  - Every post also shows a "Download the eBook" CTA and a featured promo card for the online-pharmacy guide.

---

## 4. Hub-and-cluster reality

Link matrix: an X means the page has a body link to the target. HUB = `/content-hub/ai-body-data-health-hub/`, TH/FIT/BMI = the three FitXpress pages, FAQ = trust FAQ, ACC = accuracy framework.

- **The main health hub exists** and links down to 8 vertical posts (bariatric, clinical trials, insurance, occupational health, wellness-rewards, accuracy, trust FAQ, two-photos) and to all three FitXpress pages.
- **It does not link to the GLP-1 hub, the AI in Telehealth hub, the AI in Fitness hub, the Wellness Platforms hub, the online-pharmacy guide, fitness coaching, patient engagement or the GLP-1 tools listicle.** Hubs 1, 2, 3 and 5 of the strategy are therefore not reachable from Hub 0.
- **Link-up to Hub 0 is patchy.** Only 8 posts link to it: glp-1-market, bariatric, manual-vs-digital-intake, patient-engagement, online-pharmacy, top-7-glp1, wellness-platforms and the trust FAQ. **These do not:**
  - AI in Telehealth
  - AI in Fitness
  - the accuracy framework
  - insurance underwriting
  - occupational health
  - clinical trials
  - wellness rewards
  - remote coaching
- **Links down to product (BOFU) pages:**
  - The telehealth page has 17 editorial referrers.
  - `/for-bmi-verification/` has 12, but not from the GLP-1 hub or the GLP-1 tools post.
  - The fitness page has 8.
  - For comparison, `/mobile-tailor/` has **36** editorial referrers, more than any FitXpress page.
  - The homepage passes nothing to any FitXpress page in body content; only the nav dropdown carries those links.
- **The product pages are dead ends.** All three FitXpress pages have 0 body links: none to hubs, case studies, accuracy, the trust FAQ, the docs or pricing.
- **Older health and body-comp TOFU posts are islands.** The body-fat, BIA, InBody-vs, Fit3D-vs, DEXA, body-comp-scale, lean-mass, skinny-fat, how-to-measure and 3d-body-scanning posts:
  - link to no hub and no product page (most link only to `/` or `/contact-us/`)
  - receive no links from the 2026 hubs
  - 9 of them are reachable only via `/sitemap/`:
    - `/content-hub/fit3d-vs-3dlook/`
    - `/content-hub/3d-body-scanning/`
    - `/content-hub/body-fat-percentage/`
    - `/content-hub/body-fat-percentage-men-women-ai-3d-scanning-goals/`
    - `/content-hub/body-composition-activities-…/`
    - `/content-hub/visible-abs-…/`
    - `/content-hub/breast-cancer-related-lymphedema-…/`
    - `/content-hub/top-health-tech-companies/`
    - `/content-hub/3d-body-scanning-apps-market-analysis-…/`
- **The P0/P1 listicle `/content-hub/top-7-remote-body-composition-tools-glp-1-clinics/` has no editorial inlink.** It survives only on the rotating latest-posts widget, and it drops out of that after about 8 newer posts.
- **Orphans in total:** 60 of 160 posts get editorial inlinks only from `/sitemap/`. Eleven of these are health or body-comp posts; most of the rest are old fashion or news items.
- **The sitewide widget is the de-facto hub.** Every post shows the same 8 latest posts, which today are all health. That inflates inlinks to whatever was published last and spreads nothing to the evergreen hubs (Hub 0, telehealth, fitness, accuracy).
- **Cannibalization risks visible on-site:**
  - Body composition: `/content-hub/how-to-measure-body-composition/`, `/body-composition-scale/`, `/bia-scan/`, `/inbody-vs-3dlook-…/`, `/body-scanner-machines-vs-mobile-3d-body-scan/`, `/body-scanning-technology-comparison/`, `/ai-body-scanners-vs-dexa-scans/`, `/fit3d-vs-3dlook/`. No comparison hub ties them together.
  - Body fat: `/body-fat-percentage/` vs `/body-fat-percentage-men-women-ai-3d-scanning-goals/` vs `/visible-abs-…/`.
  - Fitness: `/ai-body-scanning-for-fitness/` vs `/ai-in-fitness-industry/`. The fitness page links to neither, and the AI-in-fitness hub links to the page but not to the older post.

---

## 5. E-E-A-T

- **Author pages:** none. `/author/*` returns 404, and author names are unlinked.
  - The only bios are a marketing bio for Assel Sekerova, and some authors have none.
  - Schema author names include "admin" and raw email addresses.
- **Medical, clinical or scientific reviewer:** none anywhere, for either people or process. That is weak for YMYL-adjacent topics (GLP-1, bariatric, BMI, clinical trials, lymphedema).
- **About page:** good content (founded 2016, patented tech, both products, company snapshot, AboutPage/FAQPage/Service schema), but it has **1 editorial inlink**. Its leadership and team section appears to lack health credentials.
- **Case studies:** 1 health case, Tera Science (996 words, `/content-hub/case-study-tera-science/`). None exist for **UK Meds, Yazen or Healthyr**, which appear as logos only (Healthyr's logo alt reads "Reddit"). `/case-studies/` is 6/7 fashion and uniforms, and its topic filter isn't crawlable.
- **Trust and compliance:**
  - The central trust FAQ (`/content-hub/fitxpress-data-privacy-security-regulatory-faq/`) is good and has 16 editorial referrers, but it is a blog post with broken FAQ schema.
  - There is no `/security/`, `/trust/` or `/compliance/` page. The legal pages (FitXpress privacy policy, customer terms) are fine.
  - Sitewide "HIPAA Compliant" badges and homepage claims contradict the FAQ's careful wording, a trust and consistency risk for procurement readers and for LLM summarizers.
- **Accuracy evidence:**
  - Strong: the accuracy framework (`/content-hub/mobile-body-scanning-accuracy/`, 13 referrers) and `/ai-body-scanners-vs-dexa-scans/`.
  - The homepage's own "89% accuracy… 76% of users within 5%" BMI claim and its unsourced stats ("58 %… © HealthTech Industry Report", "40 %… © Health & Fitness Data Insights") are not linked to the framework.

---

## 6. Prioritised opportunities

1. **Create an indexable FitXpress product hub** at `/fitxpress/`, replacing today's 301 to home:
   - what it is, outputs, the API/SDK, the integration path, security, pricing link, docs link and case studies
   - SoftwareApplication or Product schema
   - fix the breadcrumb that points at `?page_id=36425`
   - set `/fitxpress` (no slash) to redirect there, not to the Admin Panel post
2. **Build BOFU vertical landing pages** under `/fitxpress/for-…/`: GLP-1 & weight-loss programs, online pharmacy BMI verification, insurance underwriting & wellness rewards, occupational health, clinical trials, bariatric. Consolidate `/for-bmi-verification/` (659 words) under the same path. Each page should link to its blog hub, and each hub back to it.
3. **Make the product pages link out.** Replace the JS-only CTAs with real `<a>` links (demo, pricing, docs), and add related hub, case study, accuracy and trust-FAQ links.
4. **Homepage:**
   - rewrite the title and meta description around FitXpress, verified BMI, body composition and the API
   - add crawlable links to each vertical page, the health hub, the accuracy framework, the trust FAQ, pricing and docs
   - fix the logo alt text
   - replace the fashion mega-menu promos with health ones
5. **Fix the hub graph:**
   - Hub 0 must link to the GLP-1, Telehealth, Fitness and Wellness hubs and the pharmacy guide
   - every vertical hub must link up to Hub 0 and down to its product page
   - link the orphaned body-comp and comparison posts into a comparison hub (e.g. make `/content-hub/body-scanning-technology-comparison/` the parent) and to `/fitxpress/for-connected-and-digital-fitness/`
   - give `/content-hub/top-7-remote-body-composition-tools-glp-1-clinics/` permanent inlinks
   - add crawlable `/content-hub/` pagination or category archives (e.g. `/content-hub/health/`)
6. **Bring the docs onto the main domain.** Put them on a `3dlook.ai` subpath or subdomain (or at least link them followed from the product and pricing pages), and add a short "Developers / API" overview page on 3dlook.ai.
7. **Technical fixes:**
   - repair the FAQ JSON-LD on the trust FAQ (move it out of post content or disable wpautop)
   - fix robots.txt grouping (the Disallows should apply to `*`)
   - decide on GPTBot (drop the nginx 403, or make robots.txt say Disallow)
   - regenerate llms.txt with the 2026 hubs and without the 301 URLs
   - redirect `http://www.` and `/blog/` in one hop
8. **E-E-A-T:**
   - add author pages with real bios
   - add a named clinical or scientific reviewer (or a "methodology & review" note) on the health hubs
   - clean the schema authors (no "admin", no emails)
   - publish case studies for UK Meds, Yazen and Healthyr, even anonymised if needed
   - add a `/trust/` or `/security/` page, or promote the FAQ to a page
   - align the "HIPAA Compliant" badge and homepage claims with the FAQ wording
