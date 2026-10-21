# Multi-product homepages: how others route visitors (live fetches, 2026-10-21)

Research for the new 3DLOOK homepage. 18 homepages fetched live on 2026-10-21: 8 multi-product
AI/API companies, 6 body-scanning competitors, 4 best-practice sites. Copy is quoted verbatim.

**Not fetched:** Clarifai (connection refused on every method); Entrust IDV / Onfido (Cloudflare 403).
Persona, Withings and Atlassian came only through r.jina.ai; Stripe served the German page, English copy
taken via r.jina.ai. Section counts are approximate; some logo names were inferred from file names.

## 1. Examples

### Multi-product AI / computer vision / API

| Company | H1 (verbatim) | How products are shown | Routing | Primary CTA | FAQ |
|---|---|---|---|---|---|
| Veriff | "The Enterprise Identity Verification Platform" | 12 uniform cards (name, one verb-led sentence, "Explore product") under 3 filter tabs | product families + industry tabs; menu adds use case | "Talk to us" (header, hero, close) + "Try live demo" | no |
| Persona | "Keeping the internet human" | 5 "building blocks" cards on a "modular platform" | nav Platform / Products / Solutions; footer Use cases / Industries / Business goals | "Get a demo" | no |
| Twilio | "The platform for conversations in the AI era" | 6 cards, action links ("Send messages", "Verify users"), "View all products"; new product = "Conversations (New)" | body by product; menu by use case, team, industry, size | "Start for free" + "Contact sales" | no |
| Stripe | "Financial infrastructure to grow your revenue." | job-to-be-done tiles, "designed to work individually or together" | body by company type; menu by model and industry; customer cards list "Products used" | (DE page) start / contact sales | no |
| Banuba | "#1 AR SDK Tailored For Your Industry" | hero carousel + 3 long blocks, mixed link labels | product only, despite the "industry" H1 | "Get free trial" | **yes, 6 Qs** |
| Perfect Corp | "No.1 AR Beauty Tech, AI Skin Tech for Beauty Ecommerce" | ~45 products only in the mega menu, grouped by body part / vertical (incl. "Jewelry and Watches") | the body routes by buying model only | "Discover AI Skin Analysis" | no |
| NuraLogix | "Revolutionizing Digital Health—One Face at a Time™" | 3 product cards; industry cards with **no links** | weak | "Request a Demo" | no |
| Withings Health Solutions | "Empowering healthcare teams to transform patients' lives" | solutions + therapeutic areas | segment line beside logos | two hero CTAs | no |

Notes worth copying:
- **Veriff:** industry tabs never re-describe products. Each tab = headline, 4 bullets naming which products apply, a quote, "Explore [industry] solutions", "Read case study". Logos ("Trusted by 3,000+ businesses worldwide") right under the hero; certifications as the last block.
- **Twilio / HubSpot:** a new product arrives as one more card with a "(New)" or "(Beta)" badge.
- **NuraLogix** sells to the same buyers as FitXpress (insurance, corporate wellness, telehealth); its title is "Home - NuraLogix".

### Body-scanning competitors

| Company | Title | H1 | Structure | CTA |
|---|---|---|---|---|
| Styku | "3D Body Scanning for Fitness, Health, & Wellness - Styku" | "Transform your business with a 3D body scanning ecosystem" | 4 product cards (one sentence + "Learn more →"), then 6 industry cards; nav Products / Industries; 8 academic studies | "Book a demo" ×6 |
| Fit3D | "Fit3D Overview - 3D Body Scanning Technology" | "The Future of" + rotating phrase; "Everything you expect from 3D body scanning. Without the machine." | effectively one product (SNAP) | "Request Demo" |
| Size Stream | "3D Body Scanning & Measurement Technology \| Size Stream" | "Unlock The Power of Body Data" | 3 stacked product blocks **without links**; nav Solutions / Industries (Apparel, Uniforms, Health and Wellness, Research) / Technology | only at the bottom |
| Prism Labs | "Prism Labs \| Mobile Body Composition & Health Tracking" | "A revolution in personal health" | segment-only routing, 8 segment cards in the menu ("Insurance & Population Health — Reduce Risk and Operational Costs"); logos right after hero; "7 publications in peer-reviewed journals" | "Let's connect" |
| Bodygram | "Bodygram \| Unlock customer measurement data…" | rendered H1 differs from the raw-HTML H1 (the closing CTA) | each product is a full section, page grows per product | "Create a free account" |
| Mirrorsize | "AI-Powered 3D Body Scan and Measurement Solutions \| Mirrorsize" | "A smarter ecosystem, powered by AI" | carousel of title-only cards, some duplicated | "Request Demo" |

The "3d body scanner" SERP is made of vendor homepages (Styku, Fit3D) whose titles carry "3D Body Scanning".
That supports the agreed title «3DLOOK: 3D Body Scanning From Two Smartphone Photos».

### Best-practice routing

| Company | H1 | Pattern |
|---|---|---|
| HubSpot | "Build demand, win deals, and delight customers — all on one platform" | 10 uniform cards: name, outcome, 2 bullets, descriptive link ("Learn more about Marketing Hub software"); new products slot in as one card ("AEO (Beta)"); "TRUSTED BY 306,000+ CUSTOMERS WORLDWIDE" under the hero |
| Atlassian | "Unleash your teams and their agents." | products bundled by team in 5 tabs; fits only when products are bought together |
| Datadog | "AI-Powered Observability and Security" | 9 cards on the page, 20+ in a category mega menu; Solutions menu = Industry / Technology / Use Case |
| Siemens Healthineers | no H1 in markup | corporate portal with ~27 blocks; not a model for a 3–5 product company |

## 2. Patterns that scale from 3 to 5+ products

1. **Category H1, no product in the H1** (Veriff, HubSpot, Stripe, Datadog, Twilio). Product #4 never breaks the hero.
2. **One card template, laid out as a grid** (Veriff 12, HubSpot 10, Datadog 9, Twilio 6, Persona 5, Styku 4). New products = one card + a badge.
3. **Group into families after ~6 products** (Veriff filter tabs, Atlassian collections, Datadog and Perfect Corp category menus).
4. **Proof right under the hero:** logos + one company-wide number.
5. **Industry is a second, lighter axis that points to products** (Veriff tabs list products; Twilio outcome blocks carry product tags; Stripe cards say "Products used").
6. **One primary CTA with the same label in the hero, mid-page and the close.**
7. **Integration and trust stated once for the whole company** (Stripe, Twilio, Veriff, Persona).

## 3. Anti-patterns

- The homepage is really one product's page (Fit3D, Perfect Corp's hero, NuraLogix, Banuba). This is what 3dlook.ai is today.
- Cards that can't be told apart (Mirrorsize "MS QuickSize" vs "MS QuickMeasure").
- Products as long stacked sections without links (Size Stream, Bodygram): the page grows with every product. This was the weakness of the old 3DLOOK Figma homepage.
- Routing that leads nowhere (NuraLogix industry cards without links; Size Stream without a hero CTA).
- Inconsistent link labels ("ABOUT" / "See Details" / "Learn more").
- Carousels for product routing (Mirrorsize, Banuba).
- Title/H1 hygiene failures ("Home - NuraLogix"; Bodygram's raw H1; Siemens without an H1).

**FAQ on the homepage:** 1 of 18 (Banuba). Not a norm among leaders; if added for answer engines, keep it company-level and short.

## 4. Recommended order (researcher's synthesis)

Hero (category H1, primary "Book a demo") → proof strip → product grid (routing within the first 2–3 screens)
→ how it works, stated once → industries, each naming its product and linking to its page → results
tagged with product → integration (API / SDK / white-label) → accuracy, trust, privacy → optional
FAQ → closing CTA with the hero's label.

## 5. Product card template (researcher's synthesis)

Family tag · name + status badge · one outcome line (≤ ~12 words) · 2–3 outputs · "best for" chips
linking to industry pages · delivery (API / SDK / white-label) · optional one logo or micro-stat ·
visual with the same aspect ratio on every card · descriptive link ("Explore FitXpress", never "Learn
more"). Equal text length per card, static grid, no carousel.

## 6. Industry axis vs product axis

- Product is the primary axis in the body; industry is secondary. Both get a top-nav menu.
- The industry page owns the pain and the narrative; the product page owns features and specs; the
  homepage only routes.
- Keep one product ↔ industry table; it drives the card chips and the industry tiles, so a new product
  is one row.
- If an industry maps to exactly one product, the tile can link straight to that product's page.
