---
qc_date: 2026-09-20
agent: post-drafter
artifact: workspace/social/articles/2026-07-14-fitxpress-privacy-security-faq/instagram-company/post.md
track: social
artifact_type: post
total_score: 18/20
status: excellent
lint: pass
coordinator_review: |
  agreement: ✅ agree
  top_issue: Uniform paragraph rhythm is the one recurring AI-tell here; claims discipline and distinct angle are solid.
---

# QC Report — post-drafter — instagram-company — 2026-09-20

**Total: 18/20** — excellent

## Scores

| # | Category | Score | Max | Basis |
|---|----------|-------|-----|-------|
| A | Adherence | 5 | 5 | judged |
| B | Factual accuracy | 5 | 5 | lint + judged |
| C | Brand & tone | 2 | 3 | judged |
| D | Format & structure | 3 | 3 | lint |
| E | Output quality | 3 | 4 | judged |

## Findings

### A. Adherence — 5/5
- Hook в перших двох рядках, як вимагає override "Social post / E" і сам бриф профілю:
  «You take two photos. Your face is hidden before the result even loads.» — видно до «ще»,
  людський, без технічного заходу.
- Довжина 793 символи всередині 600-1000, CTA «Full privacy and data FAQ, link in bio.»
  точно відповідає дозволеному `cta: «Link in bio»`, хештегів 0 (`hashtags: none`).
- `avoid: «Занадто технічні деталі, API-talk, pricing, jargon»` дотримано: пост не згадує
  API/SDK, ціни чи регуляторні номери статей, хоча стаття рясніє ними (HIPAA, GDPR, SOC 2,
  DPA) — драфтер свідомо відфільтрував це для IG-аудиторії.
- Angle і design tip узгоджені: caption будує «подорож фото» (капчур → обробка → видалення/
  блюр), design tip розбиває той самий Photos-рядок таблиці на 3-slide carousel — це саме
  той content type, який бриф називає «Behind-the-scenes / how it works simplified».
- Перевірив дослівно проти `published-live-2026-09-18.md`: «face obfuscation is applied at
  capture, regardless of the retention policy» → «Face obfuscation happens at capture,
  whatever the retention setting» — квантифікатор і межа збережені, не загублені (це той
  клас дефекту, який лінтер не ловить). «returns structured outputs in under 45 seconds» —
  цифра й межа перенесені точно, не «under a minute».

### C. Brand & tone — 2/3
- `lint.warnings` містить `ai-tells:house_rule uniform paragraph length` — це не
  design-tip-попередження (тому D лишається 3), але це прямий сигнал AI-сигнатури, який
  рубрика відносить до категорії C. Перевірив вручну: усі шість абзаців мають практично
  однакову форму — 2-3 короткі речення кожен, однаковий ритм від «You take two photos» до
  «Everyone asks…». Це і є те, чого лінтер сам не інтерпретує як зміст, а лише фіксує як
  патерн; людське прочитання підтверджує — текст читається трохи метрономно.
- Заборонених слів зі списку CLAUDE.md §6 (leverage, seamless, «game-changing» тощо) і
  em dash немає — сама лексика чиста, лапс саме в ритмі, тобто «1-2 minor lapse» за шкалою
  рубрики.

### E. Output quality — 3/4
- **Position:** «Everyone asks what a body scan produces. Fewer ask what it keeps and what
  it forgets on purpose. That second question is worth answering before you trust any tool
  with a photo.» — це не переказ FAQ, а явне судження: пост стверджує, що питання
  retention важливіше за питання output, і адресує це читачеві напряму («before you trust
  any tool with a photo»). Це справжня позиція, не компіляція фактів.
- **Angle distinctness:** відрізняється від `twitter-company` («honesty vs compliance
  badge», кут для procurement) — тут кут особистий і тактильний: що станеться з конкретним
  фото конкретної людини. Немає перетину формулювань чи фокусу.
- Знято один бал не за брак позиції чи фактів, а за виконання: ритмічна одноманітність
  абзаців (див. C) заважає тексту звучати як написаний людиною, а не згенерований по
  шаблону «твердження. твердження. твердження.» — це саме те, що рубрика описує як
  «мінімальні правки на 5-10 хвилин» (варіювати довжину речень/абзаців), а не концептуальна
  переробка.

## Top issue for `post-drafter`

Варіювати довжину і кількість речень між абзацами навмисно (один абзац-панч на одне
речення, інший розлогіший), щоб уникнути метричного ритму, який лінтер уже фіксує як
`ai-tells:house_rule uniform paragraph length` — це повторюваний дефект саме цього кроку
пайплайну, не разовий.
