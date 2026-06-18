# Social Profiles Config

> Настройки для каждого из 5 профилей. Читается quarterly-strategist и post-drafter. Вадим может менять кол-во постов, ICP bias, тон для каждого профиля.

## Профили

### company — 3DLOOK (LinkedIn Company Page)
```yaml
profile_id: company
platform: linkedin
owner: Vadim (manages)
posts_per_week: 2
product_bias:
  fitxpress: 70%
  mobile_tailor: 10%
  mixed: 20%
icp_focus:
  - All FX ICPs (telehealth, insurance, pharmacy, wellness)
  - All MT ICPs (MTM, uniforms, on-demand)
tone: "Expert, data-driven, balanced both products. Company voice, not personal."
content_types:
  - Product updates
  - Case study highlights
  - Industry trends with 3DLOOK angle
  - Accuracy / compliance proof points
  - Customer wins
avoid: "Too personal, founder voice — that's for personal profiles"
```

### katerina — Katerina Galich (LinkedIn Personal)
```yaml
profile_id: katerina
platform: linkedin
owner: Katerina Galich (CEO)
posts_per_week: 1
product_bias:
  fitxpress: 70%
  mobile_tailor: 10%
  mixed: 20%
icp_focus:
  - C-level health-tech
  - Insurance innovation leaders
  - AI / body scanning future
tone: "Founder voice. Strategic, visionary, AI risk-aware. First person. Thoughtful, not salesy."
content_types:
  - AI risk / commoditization thoughts
  - FitXpress strategy and direction
  - Health-tech industry perspective
  - Lessons from building 3DLOOK
  - Conference takeaways
avoid: "Product features, pricing, technical specs — too granular for CEO voice"
```

### whitney — Whitney Cathcart (LinkedIn Personal)
```yaml
profile_id: whitney
platform: linkedin
owner: Whitney Cathcart (Co-founder & CCO)
posts_per_week: 1
product_bias:
  fitxpress: 20%
  mobile_tailor: 60%
  mixed: 20%
icp_focus:
  - Apparel / MTM industry
  - Fashion-tech community
  - Retail innovation
tone: "Industry insider. Fashion-tech veteran. Conference circuit. Relationships-focused."
content_types:
  - MT customer wins and stories
  - Fashion-tech events and takeaways
  - Industry trends (sustainability, on-demand, fit tech)
  - Networking / partnerships
avoid: "Heavy health/insurance topics — that's Katerina's lane"
```

### vadim — Vadim Bilan (LinkedIn Personal)
```yaml
profile_id: vadim
platform: linkedin
owner: Vadim Bilan (Marketing Manager)
posts_per_week: 1
product_bias:
  fitxpress: 50%
  mobile_tailor: 30%
  mixed: 20%
icp_focus:
  - Marketing / growth community
  - B2B SaaS tactics
  - Health-tech / apparel-tech
tone: "Practitioner. Shares what works. Data-backed. Honest about failures. Peer-to-peer."
content_types:
  - Marketing experiments and results
  - Growth tactics with 3DLOOK examples
  - Behind-the-scenes of campaigns
  - Lessons learned
avoid: "CEO-level strategy — that's Katerina. Keep it hands-on tactical."
```

### profile4 — [TBD] (LinkedIn Personal)
```yaml
profile_id: profile4
platform: linkedin
owner: TBD
posts_per_week: 0  # disabled until configured
product_bias:
  fitxpress: 50%
  mobile_tailor: 50%
icp_focus: TBD
tone: TBD
content_types: TBD
avoid: TBD
```

## Как менять кол-во постов

Вадим редактирует `posts_per_week` в этом файле. Quarterly-strategist использует это число при планировании. Post-drafter проверяет перед запуском.

**Минимум:** 0 (профиль отключён)
**Максимум:** 5 (для очень активных периодов — launches, events)
**Default:** 1-2

## Как агенты используют

| Агент | Что берёт из config |
|-------|---------------------|
| quarterly-strategist | `posts_per_week`, `product_bias`, `icp_focus`, `content_types` для планирования квартала |
| post-drafter | `tone`, `avoid`, `product_bias` для написания конкретного поста |
| visual-brief | `tone` + profile owner для стилевого решения |
| context-pack-builder | `profile_id` → выбирает нужный блок и включает в context pack |
