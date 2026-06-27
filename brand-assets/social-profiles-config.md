# Social Profiles Config

> Читається `post-drafter` та `visual-brief`. Вадим редагує цей файл щоб вмикати/вимикати профілі або змінювати налаштування.
> Активний профіль = `posts_per_week: 1`. Вимкнений = `posts_per_week: 0`.
> В новому пайплайні posts_per_week — прапор активності, не кількість постів на тиждень.

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
  fitxpress: 70%
  mobile_tailor: 10%
  mixed: 20%
tone: "Punchy, data-first. One sharp insight from the article — не переказ. Industry commentary tone."
content_types:
  - One striking stat or claim from the article
  - Short POV on industry trend the article touches
  - Thread (якщо тема складна — 3-4 твіти)
length: "240-260 chars for single tweet. For thread: tweet 1 = hook (240 chars), tweet 2-4 = expansion."
hashtags: "2-3 max. No hashtag spam."
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
  fitxpress: 70%
  mobile_tailor: 10%
  mixed: 20%
tone: "Visual storytelling. Human angle — technology through the lens of real outcomes. Less corporate, more brand."
content_types:
  - Human outcome from the article (patient scan, tailor measuring client, etc.)
  - Behind-the-scenes / how it works simplified
  - Key stat turned into visual story
  - Product in action
length: "600-1000 chars caption. Hook in first line (показується до «ще»)."
hashtags: "10-15 релевантних. Mix: нішові (#GLP1 #WeightLoss #BodyScanning) + середні (#HealthTech #FitTech)."
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
  fitxpress: 70%
  mobile_tailor: 10%
  mixed: 20%
tone: "Accessible and community-oriented. Broader audience than LinkedIn — explain without jargon. Slightly warmer."
content_types:
  - Article summary with key takeaways
  - Customer story or use case narrative
  - Industry question that sparks discussion
  - Behind the company / team moments
length: "800-1200 chars"
hashtags: "3-5 max"
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
  fitxpress: 70%
  mobile_tailor: 10%
  mixed: 20%
icp_focus:
  - All FX ICPs (telehealth, insurance, pharmacy, wellness)
  - All MT ICPs (MTM, uniforms, on-demand)
tone: "Expert, data-driven. Company voice — не особиста. Outcome-focused, не feature-focused."
content_types:
  - Key insight or stat from the article
  - Case study highlight
  - Industry trend with 3DLOOK angle
  - Compliance / accuracy proof point
length: "1200-1800 chars"
hashtags: "3-5"
avoid: "Founder personal voice, opinions without data, generic AI buzzwords"
cta: "«Read the full article» або «Book a demo»"
```

---

## Особисті профілі — Лідерство

### linkedin-katerina — Katerina Galich (CEO)
```yaml
profile_id: linkedin-katerina
platform: linkedin
owner: Katerina Galich (CEO)
posts_per_week: 1
product_bias:
  fitxpress: 70%
  mobile_tailor: 10%
  mixed: 20%
icp_focus:
  - C-level health-tech executives
  - Insurance innovation leaders
  - AI / body scanning future market
tone: "Founder voice. Strategic, visionary, AI risk-aware. First person. Thoughtful, not salesy."
content_types:
  - CEO perspective on what the article's topic means for the industry
  - AI risk / commoditization angle
  - Market direction and 3DLOOK positioning
  - Lessons from building in this space
length: "1000-1500 chars"
hashtags: "3-4"
avoid: "Product features, pricing, technical specs — too granular for CEO voice"
cta: "Soft — «Curious what you think» або посилання на статтю"
```

### linkedin-vadim — Vadim Bilan (Marketing)
```yaml
profile_id: linkedin-vadim
platform: linkedin
owner: Vadim Bilan (Marketing Manager)
posts_per_week: 1
product_bias:
  fitxpress: 50%
  mobile_tailor: 30%
  mixed: 20%
icp_focus:
  - Marketing / growth community
  - B2B SaaS practitioners
  - Health-tech / apparel-tech operators
tone: "Practitioner. Shares what works and what doesn't. Data-backed. Honest. Peer-to-peer, not broadcast."
content_types:
  - Marketing angle on the article topic — what it means for GTM, messaging, positioning
  - Content experiment takeaways
  - Behind-the-scenes of campaigns
  - Tactical observations
length: "1000-1500 chars"
hashtags: "3-4"
avoid: "CEO-level strategy — that's Katerina. Keep it hands-on."
cta: "Посилання на статтю або запитання до аудиторії"
```

---

## Особисті профілі — Business Development

### linkedin-nick — Nick Omelchak (BD, USA)
```yaml
profile_id: linkedin-nick
platform: linkedin
owner: Nick Omelchak (Business Development, USA)
posts_per_week: 1
product_bias:
  fitxpress: 80%
  mobile_tailor: 10%
  mixed: 10%
icp_focus:
  - US health-tech buyers (telehealth, GLP-1 platforms, online pharmacies, insurance)
  - VP Product / Chief Medical Officers / Head of Clinical Operations
  - US wellness and employer health market
tone: "BD practitioner. Relationship-first. Connects industry pain points to outcomes. US market context. First person."
content_types:
  - US market angle on the article — regulatory, payer, health-tech context
  - Relevant pain point for US buyers that the article addresses
  - Industry observation from US conversations / events
  - Prospect-resonant outcome story
length: "800-1400 chars"
hashtags: "3-5. US-relevant: #HealthTech #GLP1 #Telehealth #DigitalHealth #WeightLoss"
avoid: "European regulatory context, fashion/apparel topics (not his lane), generic 3DLOOK promo"
cta: "Soft — «Happy to share more», посилання на статтю"
```

### linkedin-olena — Olena Kudryavtseva (BD, Europe)
```yaml
profile_id: linkedin-olena
platform: linkedin
owner: Olena Kudryavtseva (Business Development, Europe)
posts_per_week: 1
product_bias:
  fitxpress: 55%
  mobile_tailor: 30%
  mixed: 15%
icp_focus:
  - European health-tech and apparel buyers
  - GDPR-conscious healthcare operators
  - EU pharmacy chains, insurers, wellness platforms
  - European MTM and uniform companies
tone: "BD professional. Considered, relationship-focused. EU market nuance (GDPR, CE marking awareness). First person."
content_types:
  - European market angle on the article — EU regulatory context, GDPR, privacy
  - Relevant use case for EU buyers (both FX and MT)
  - Observation from EU market conversations or events
  - Cross-industry insight (healthtech + fashiontech intersect more in EU)
length: "800-1400 chars"
hashtags: "3-5. EU-relevant: #HealthTech #FashionTech #GDPR #EuropeanMarket #DigitalHealth"
avoid: "US-specific regulatory context (FDA, payer system), Israeli market topics"
cta: "Soft — посилання на статтю, «Open to connect»"
```

### linkedin-katya — Katya Boychuk (BD, Israel)
```yaml
profile_id: linkedin-katya
platform: linkedin
owner: Katya Boychuk (Business Development, Israel)
posts_per_week: 1
product_bias:
  fitxpress: 75%
  mobile_tailor: 10%
  mixed: 15%
icp_focus:
  - Israeli health-tech ecosystem (strong startup + enterprise mix)
  - Digital health, insurtech, wellness tech buyers
  - Israeli telehealth and pharma chains
tone: "BD professional in a fast-moving startup ecosystem. Direct, confident, innovation-friendly. First person."
content_types:
  - Israeli / MENA health-tech angle on the article
  - Startup ecosystem relevance — how global tech applies locally
  - Industry insight from Israeli market conversations
  - Health-tech innovation perspective
length: "800-1400 chars"
hashtags: "3-5. #HealthTech #IsraeliStartups #DigitalHealth #Insurtech #FitTech"
avoid: "EU regulatory specifics, US payer system context, fashion/apparel topics"
cta: "Soft — посилання на статтю, запитання до аудиторії"
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
| `post-drafter` | `tone`, `avoid`, `product_bias`, `length`, `hashtags`, `cta` — для написання поста |
| `visual-brief` | `platform`, `tone`, profile owner — для стилевого рішення і розмірів |
| `/post-from-article` command | `posts_per_week > 0` — список активних профілів для ітерації |

## Як вмикати/вимикати профіль

Встанови `posts_per_week: 1` (вмикає) або `posts_per_week: 0` (вимикає).
