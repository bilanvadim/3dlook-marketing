# Social Profiles Config

> Читається `post-drafter` та `visual-brief`. Вадим редагує цей файл щоб вмикати/вимикати профілі або змінювати налаштування.
> Активний профіль = `posts_per_week: 1`. Вимкнений = `posts_per_week: 0`.
> В новому пайплайні posts_per_week — прапор активності, не кількість постів на тиждень.
>
> ⚠️ **Для всіх 6 `linkedin-*` профілів джерело правди по промпту — `brand-assets/linkedin-post-prompts.md`**
> (офлайн-копія [Google Doc](https://docs.google.com/document/d/19KKWLtJv4Jx_hKbgxy0TCWnLXgnHe0-gxGuDj9vA2WQ/edit), синк 2026-08-07).
> `post-drafter` **обов'язково** читає той файл перед написанням будь-якого LinkedIn-поста. Блоки нижче — операційне резюме;
> при конфлікті виграє `linkedin-post-prompts.md`, окрім двох house rules, які виграють завжди:
> **хештегів немає ніде** і **1–2 емодзі максимум**.
> Twitter / Instagram / Facebook документ не зачіпає — їхні блоки лишаються без змін.

---

## Компанійські акаунти

### twitter-company — 3DLOOK (Twitter / X)
```yaml
profile_id: twitter-company
platform: twitter
handle: "@3DLOOK"
owner: Vadim (manages)
posts_per_week: 1
product_bias:
  fitxpress: 100%
  mobile_tailor: 0%
  mixed: 0%
tone: "Punchy, data-first. One sharp insight from the article — не переказ. Industry commentary tone."
content_types:
  - One striking stat or claim from the article
  - Short POV on industry trend the article touches
  - Thread (якщо тема складна — 3-4 твіти)
length: "240-260 chars for single tweet. For thread: tweet 1 = hook (240 chars), tweet 2-4 = expansion."
hashtags: none
avoid: "Long paragraphs, bullet lists, emoji flood, generic corporate speak"
cta: "Link in bio / article link у відповіді до треду"
```

### instagram-company — 3DLOOK (Instagram)
```yaml
profile_id: instagram-company
platform: instagram
handle: "@3dlook.ai"
owner: Vadim (manages)
posts_per_week: 1
product_bias:
  fitxpress: 100%
  mobile_tailor: 0%
  mixed: 0%
tone: "Visual storytelling. Human angle — technology through the lens of real outcomes. Less corporate, more brand."
content_types:
  - Human outcome from the article (patient scan, tailor measuring client, etc.)
  - Behind-the-scenes / how it works simplified
  - Key stat turned into visual story
  - Product in action
length: "600-1000 chars caption. Hook in first line (показується до «ще»)."
hashtags: none
avoid: "Занадто технічні деталі, API-talk, pricing, jargon"
cta: "«Link in bio» або «Save this post»"
```

### facebook-company — 3DLOOK (Facebook)
```yaml
profile_id: facebook-company
platform: facebook
page: "3DLOOK"
owner: Vadim (manages)
posts_per_week: 1
product_bias:
  fitxpress: 100%
  mobile_tailor: 0%
  mixed: 0%
tone: "Accessible and community-oriented. Broader audience than LinkedIn — explain without jargon. Slightly warmer."
content_types:
  - Article summary with key takeaways
  - Customer story or use case narrative
  - Industry question that sparks discussion
  - Behind the company / team moments
length: "800-1200 chars"
hashtags: none
avoid: "Dry B2B corporate tone, technical API details, pricing"
cta: "«Read the full article» з посиланням"
```

### linkedin-company — 3DLOOK (LinkedIn Company Page)
```yaml
profile_id: linkedin-company
platform: linkedin
owner: Vadim (manages)
posts_per_week: 1
product_bias:
  fitxpress: 100%
  mobile_tailor: 0%
  mixed: 0%
writing_brief: "brand-assets/linkedin-post-prompts.md → ## linkedin-company (MANDATORY READ)"
icp_focus:
  - All FX ICPs (telehealth, insurance, pharmacy, wellness)
tone: "Educational, credible, enterprise-focused. Professional B2B SaaS — як enterprise technology company. Company voice (third person / «we»), не особиста. Business value, не product promotion."
content_types:
  - The biggest market trend or problem the article discusses, with 3DLOOK positioned as part of the solution
  - Key insight or stat from the article
  - Case study highlight
  - Compliance / accuracy proof point
length: "180-280 words (~1200-1850 chars)"
emoji: "1-2 max"
hashtags: none
avoid: "Founder personal voice, opinions without data, generic AI buzzwords, promotional language, summarising the article instead of building on it"
cta: "«Read the full article» — завжди запрошення до статті"
```

---

## Особисті профілі — Лідерство

### linkedin-katerina — Katerina Galich (CEO)
```yaml
profile_id: linkedin-katerina
platform: linkedin
owner: Katerina Galich (CEO)
posts_per_week: 1
market: UK
product_bias:
  fitxpress: 100%
  mobile_tailor: 0%
  mixed: 0%
writing_brief: "brand-assets/linkedin-post-prompts.md → ## linkedin-katerina (MANDATORY READ)"
icp_focus:
  - UK telehealth and GLP-1 / weight loss platforms (NHS-adjacent and private)
  - UK online pharmacies and digital prescribers (e.g. UK Meds, Zava, Phlo)
  - UK life and disability insurers (underwriting innovation)
  - UK employer health and wellness buyers
  - UK health-tech C-level and innovation leaders
tone: "Founder sharing market observations, not marketing. Calm, executive, visionary, experienced, credible — Satya Nadella, не інфлюенсер. Thoughtful rather than emotional. First person. No sales pitch. UK market lens — MHRA, CQC, NHS context, UK health-tech ecosystem."
content_types:
  - One strategic observation about the broader industry shift behind the article
  - Why the market is changing and what enterprise buyers are beginning to expect
  - Leadership, digital health, AI adoption, enterprise healthcare, product strategy, market evolution
  - AI risk / commoditization through a UK market lens
  - UK regulatory and compliance angle (MHRA, GDPR, NHS digital transformation)
length: "180-250 words (~1200-1650 chars)"
emoji: "1-2 max"
hashtags: none
avoid: "Marketing voice, sales pitch, claiming experiences the article doesn't support, Mobile Tailor / apparel topics, US regulatory context (FDA, US payer system), EU-specific regulatory framing, product features and pricing — too granular for CEO voice"
cta: "Invitation to explore the article — soft, «Curious what you think»"
```

### linkedin-vadim — Vadim Bilan (BD/Marketing, Australia)
```yaml
profile_id: linkedin-vadim
platform: linkedin
owner: Vadim Bilan (Marketing Manager)
posts_per_week: 1
market: Australia
product_bias:
  fitxpress: 100%
  mobile_tailor: 0%
  mixed: 0%
writing_brief: "brand-assets/linkedin-post-prompts.md → ## linkedin-vadim (MANDATORY READ)"
icp_focus:
  - Australian telehealth providers
  - Australian digital health companies
  - Fitness platforms
  - Enterprise health operators
tone: "Someone helping operators build better products. Practitioner, hands-on, honest, peer-to-peer — not broadcast, not marketing language. First person."
content_types:
  - What the article means specifically for Australian health operators
  - Operational excellence, implementation, real-world deployment, reliability
  - Privacy and scalability in an AU context
  - Product quality and enterprise procurement
length: "180-250 words (~1200-1650 chars)"
emoji: "1-2 max"
hashtags: none
avoid: "Marketing language, repeating the article instead of translating it for AU, CEO-level strategy (that's Katerina), US/EU/UK regulatory framing unless the article raises it, generic 3DLOOK promo. The old marketing/growth-community + GTM angle is superseded (2026-08-07)."
cta: "Question or invitation to discuss + посилання на статтю"
```

---

## Особисті профілі — Business Development

### linkedin-nick — Nick Omelchak (BD, USA)
```yaml
profile_id: linkedin-nick
platform: linkedin
owner: Nick Omelchak (Business Development, USA)
posts_per_week: 1
market: USA
product_bias:
  fitxpress: 100%
  mobile_tailor: 0%
  mixed: 0%
writing_brief: "brand-assets/linkedin-post-prompts.md → ## linkedin-nick (MANDATORY READ)"
icp_focus:
  - US telehealth providers, online pharmacies, GLP-1 programs, digital health companies
  - Healthcare providers, insurers, employers, enterprise healthcare organizations
  - VP Product / Chief Medical Officers / Head of Clinical Operations
tone: "Confident, practical, professional, consultative, solution-oriented. Writes as someone who speaks with US healthcare leaders every day. Relationship-first. First person."
content_types:
  - Why the article's topic matters specifically to US healthcare organizations
  - Enterprise healthcare, telehealth, GLP-1 programs, remote patient monitoring
  - Operational efficiency, patient engagement, healthcare workflows
  - Evidence generation, enterprise partnerships, scalability
length: "180-250 words (~1200-1650 chars)"
emoji: "1-2 max"
hashtags: none
avoid: "Marketing buzzwords, exaggerated claims, forced product promotion, European regulatory context, fashion/apparel topics (not his lane), generic 3DLOOK promo"
cta: "Discussion question + invitation to explore the article"
```

### linkedin-olena — Olena Kudryavtseva (BD, Europe)
```yaml
profile_id: linkedin-olena
platform: linkedin
owner: Olena Kudryavtseva (Business Development, Europe)
posts_per_week: 1
product_bias:
  fitxpress: 100%
  mobile_tailor: 0%
  mixed: 0%
market: Continental Europe (UK excluded)
writing_brief: "brand-assets/linkedin-post-prompts.md → ## linkedin-olena (MANDATORY READ)"
icp_focus:
  - Digital health providers, telehealth companies, wellness platforms across Continental Europe
  - Connected fitness businesses
  - Insurers, employers, enterprise healthcare organizations
  - GDPR-conscious healthcare operators
tone: "Practical, consultative, customer-focused, business-oriented, educational, conversational. Sounds like someone speaking with healthcare operators and product teams every day. First person."
content_types:
  - Why the topic matters to European healthcare and wellness companies
  - Operational, regulatory and adoption challenges
  - Implementation, scalability, user trust, measurable outcomes
  - Examples relevant to European enterprise buyers
length: "180-250 words (~1200-1650 chars)"
emoji: "1-2 max"
hashtags: none
avoid: "US-specific regulatory context (FDA, payer system), UK-specific references, country-specific regulations unless the article raises them (EU-wide GDPR framing is fine), Israeli market topics, fashion/apparel topics, positioning 3DLOOK as the centre of the conversation instead of an enabling technology"
cta: "Engaging question + invitation to read the article"
```

### linkedin-katya — Kateryna Boichuk (BD, Israel & Gulf)
```yaml
profile_id: linkedin-katya
platform: linkedin
owner: Kateryna Boichuk (Business Development, Israel & Gulf)
posts_per_week: 1
market: Israel and the Gulf
product_bias:
  fitxpress: 100%
  mobile_tailor: 0%
  mixed: 0%
writing_brief: "brand-assets/linkedin-post-prompts.md → ## linkedin-katya (MANDATORY READ)"
icp_focus:
  - Digital health operators, founders and product teams across Israel and the Gulf
  - Healthcare companies in the region
  - Israeli health-tech ecosystem (strong startup + enterprise mix)
  - Digital health, insurtech, wellness tech buyers; telehealth and pharma chains
tone: "Someone who spends every day talking to customers. Conversational, professional, insightful. Direct, confident, innovation-friendly. First person."
content_types:
  - Why the topic matters commercially — customer problems, product adoption
  - Operational challenges and implementation
  - Enterprise buying behaviour and trust
  - Scaling digital health in the region
length: "180-250 words (~1200-1650 chars)"
emoji: "1-2 max"
hashtags: none
avoid: "Technical deep dives, product promotion, EU regulatory specifics, US payer system context, fashion/apparel topics"
cta: "Discussion question BEFORE the article link"
```

---

## Вимкнені профілі

### linkedin-whitney — Whitney Cathcart (CCO) — DISABLED
```yaml
profile_id: linkedin-whitney
platform: linkedin
owner: Whitney Cathcart (Co-founder & CCO)
posts_per_week: 0  # disabled
product_bias:
  fitxpress: 20%
  mobile_tailor: 60%
  mixed: 20%
tone: "Industry insider. Fashion-tech veteran. Conference circuit. Relationships-focused."
avoid: "Heavy health/insurance topics"
note: "Disabled 2026-06-27. Activate by setting posts_per_week: 1."
```

---

## Як агенти використовують цей файл

| Агент | Що бере з конфігу |
|-------|-------------------|
| `post-drafter` | `tone`, `avoid`, `product_bias`, `length`, `emoji`, `hashtags`, `cta` — для написання поста. Для `linkedin-*` **додатково обов'язково** читає `writing_brief` → відповідну секцію `brand-assets/linkedin-post-prompts.md` |
| `social-planner` | `icp_focus`, `market`, `content_types` — для розподілу кутів між профілями |
| `visual-brief` | `platform`, `tone`, profile owner — для стилевого рішення і розмірів |
| `/post-from-article` command | `posts_per_week > 0` — список активних профілів для ітерації |

## Як вмикати/вимикати профіль

Встанови `posts_per_week: 1` (вмикає) або `posts_per_week: 0` (вимикає).
