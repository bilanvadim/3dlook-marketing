# Header navigation and site structure: live teardowns and guidance (fetched 2026-10-22)

Research for the 3dlook.ai site architecture. 15 sites fetched live (curl + HTML parsing, r.jina.ai, or a
headless browser that hovered and clicked menus). Labels are verbatim.

**Not covered / partial:** Onfido/Entrust (Cloudflare 403 on every method); Persona's header dropdowns
(rendered only in a real browser; its footer mirrors them); Perfect Corp (menu read from markup); Twilio
(a cookie overlay blocked the hover-vs-click test).

## A. Teardowns

| Site | Top level (count) | Right side | How products are shown | Industry axis | URLs |
|---|---|---|---|---|---|
| Stripe | Products · Solutions · Developers · Resources · Pricing (5) | "Sign in", "Contact sales" | 4 family columns (Payments, Revenue, Money Management, Embedded Finance), 2–4-word descriptor per item, "More" overflow column, one featured card, "See all products" → /products | Solutions: By stage · By use case · By industry · Ecosystem | flat /payments, /billing; children /payments/checkout; /use-cases/saas, /industries/insurance; docs on docs.stripe.com |
| Twilio | Products · Solutions · Why Twilio · Resources · Pricing (5) | "Contact sales", "Start for free"; utility bar with a **login chooser** ("Log in to Twilio Console…" / "Or log in to access: Twilio Segment / Twilio SendGrid") | "Twilio Platform" overview link first; 4 family tabs; "New" badges; "See all products" | Solutions: Use Cases · Teams · Industry · Company Size | /en-us/messaging, /en-us/products/email-api (mixed); footer links /llms.txt |
| Datadog | Product · Customers · Pricing · Solutions · Docs · About · Blog (7) | "Login", "Get started free" | left tab rail, ~100 links; items repeated 2–3 times | Solutions: Industry · Technology · Use Case | /product/apm/ vs /products/ai/… drift |
| Veriff | Products · Solutions · Pricing · Resources · Company (5) | "Talk to us"; utility bar Login · Help Center · "How to get verified" | 4 families, family titles are links, icons, no descriptions | Solutions: By Industry (6) · By Use Case (6) | /product/liveness, /industry/marketplaces, /use-cases/kyc, /for-developers |
| Persona | Platform · Products · Solutions · Customers · Pricing · Research · Resources (7) | "Verify me", "Login", "Get a demo" | top-level "Platform" overview page | Use cases · Industries · Business goals (footer) | /product/verifications/government-id, /industry/fintech; header menus missing from server HTML |
| Yoti | Technologies · Solutions · Personal · Company · Resources (5) | "Talk to sales", **"Business login" dropdown** (Yoti Hub / Portal / Sign / Verified Calls) | 7 items with icon + one-liner | 12 use cases and industries mixed | inconsistent (/business/age-verification/, /retail/) |
| Mitek | Products · Solutions · Innovators · Resources · Company (5) | "Speak with an expert" | 3 families, descriptor per item | By use case · By fraud type · By industry | /products/x, /use-cases/x, /industry/x |
| Perfect Corp | Enterprise · Online Service · Technologies · Demo Store · Resources · AI API · Blog (7) | "Contact Sales", "TRY OUR DEMO", "Sign In" in utility bar | ~37 products under category labels incl. "Jewelry and Watches"; one product listed twice; **hamburger on desktop** | — | /business/products/ar-virtual-ring |
| Banuba | one item per product + Technology · About us (5) | "Get free trial" | each product menu repeats products / use cases / comparisons / resources | inside each product | flat keyword slugs (/video-editor-sdk) |
| NuraLogix | Home · Technology · Research · Products · News · Company · Get in Touch (7) | — | "Products" → "#", mixes variants and delivery channels | none | — |
| Styku | Products · Industries · More (3) | "Book a demo"; client portal login hidden in "More" | product list | Industries | flat (/styku-studio, /fitness) |
| Size Stream | Solutions · Industries · Technology · Resources · Company · Contact (6) | none | every dropdown starts with "Overview"; no product names | Industries (Apparel, Uniforms, Health and Wellness…) overlaps Solutions | /solutions/made-to-measure/, /industries/body-scanning-uniforms/, /technology/api-sdk/ |
| Prism Labs | Why Prism · Solutions · Developers · Pricing · Blog · About (6) | "Contact us", "Scan Yourself" | one product | Solutions: 8 industries with icon + benefit line | /solutions/insurance-population-health, /developers |
| Bodygram | Technology & Services · Case studies · About us (3) | "Get in touch"; sign-in only in footer | an app login listed as a product | tags on case studies | — |
| Fit3D | Product · Customer Success · End User Experience · Blog · About Us (5) | "Login", "Request Demo" | industries hidden under "Customer Success"; "Contact Sales" listed as a product | — | footer "Compare to" column |

## B. Guidance

- **NN/g, mega menus:** "an excellent design choice for accommodating a large number of options"; "Chunk options into related sets"; "Use concise, yet descriptive labels for each group"; "Show each choice only once"; "use the space to show choices, not fluff." https://www.nngroup.com/articles/mega-menus-work-well/
- **NN/g, opening:** wait 0.3–0.5 s before opening on hover, show within 0.1 s; the 2024 menu checklist recommends click-to-open because hover is unavailable for touch and keyboard; "Failing to indicate the current location is probably the single most common mistake." Baymard: 300–500 ms hover delay.
- **NN/g, count and labels:** no magic number ("It's not 7"); "5 categories are perfectly adequate" for small sites; no made-up words, jargon or vague verbs ("Explore", "Discover", "Learn").
- **NN/g, audience-based navigation:** users don't know which group to pick; make audience categories mutually exclusive and jargon-free. Applies to "Industries" / "For X" menus.
- **NN/g, hamburger:** no hidden navigation on desktop; on mobile show links directly if there are 4 or fewer. Log in / Sign up = utility navigation, top right, secondary prominence.
- **Google Search Central:** "Google generally doesn't look at the structure of URLs to work out the structure of a site. Instead, it analyzes the linkages between pages." Menus "can impact Google's understanding of your site structure"; click depth and inbound links signal importance. Keywords in URL paths have "hardly any effect beyond appearing in breadcrumbs"; directories help with "more than a few thousand URLs". Breadcrumbs should "represent a typical user path… instead of mirroring the URL structure"; desktop-only in results since Jan 2025. Only `<a href>` links are crawlable. Sitelinks are automatic, from link structure.
- **AI answer engines (weak evidence):** Google AI features use the same crawling and indexing as Search; Microsoft (Ads blog 2025): "Don't hide important answers in tabs or expandable menus"; OpenAI and Perplexity only ask to allow their bots. No primary source says /products/x/ vs /x/ affects AI citation.

## C. Synthesis (researcher)

1. Typical count is 5 top-level items (Stripe, Twilio, Veriff, Yoti, Mitek, Banuba, Fit3D); range 3–7. Skeleton "Products · Solutions · Developers · Resources · Pricing", plus "Company" when there is room.
2. Right side: one primary CTA ("Contact sales", "Talk to us", "Get a demo", "Book a demo"), a second only for self-serve; login as utility, a **chooser** when there are several apps (Twilio, Yoti).
3. Adding products: family columns (Stripe, Veriff, Mitek); left-rail tabs past ~7 families (Twilio, Datadog); an overview entry first ("Twilio Platform", Persona "Platform", Size Stream "Overview"); "See all products" catalog; "New" badges.
4. With 3+ products everyone runs a separate industry/solutions menu; single-product companies make industries the main axis. Larger companies' industry pages span products; none nests industry pages under a product URL. Banuba is the only one nesting use cases inside each product menu.
5. URL choice is mostly maintenance and analytics, not rankings; moving existing URLs is the bigger risk.
6. Anti-patterns: one top-level item per product (Banuba); delivery channels mixed with products (NuraLogix); catch-all "More" hiding the login (Styku); login only in the footer (Bodygram); duplicated items (Datadog, Perfect Corp); overlapping "Solutions" and "Industries" (Size Stream); "Products" → "#" without an overview (NuraLogix); hamburger on desktop (Perfect Corp); header menus missing from server HTML (Persona); 100-link mega menus (Datadog).
