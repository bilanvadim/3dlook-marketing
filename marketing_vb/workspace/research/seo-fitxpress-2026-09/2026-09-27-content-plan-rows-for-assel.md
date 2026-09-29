---
product: fitxpress
type: content-plan-proposal
date: 2026-09-27
for: Ассель (добавить строки в Sheet «Content Plan v 2.0»)
source: 2026-09-25-fitxpress-seo-plan.md (фаза 3) + data/ahrefs-findings.md, data/gsc-findings.md
---

# Новые строки контент-плана: список для Ассель

## Зачем эти строки

Ассель, привет! Это предложения из SEO-плана FitXpress. Зачем они нужны:

- Сейчас в контент-плане только темы вертикалей ICP (telehealth, GLP-1, pharmacy и т.д.). Почти у всех этих тем **нулевой или очень маленький поисковый спрос**: «telehealth weight verification», «GLP-1 progress tracking», «body measurement API» ищут 0–20 раз в месяц. Такие статьи полезны для продаж и для ИИ-ассистентов, но трафика они не дают.
- Трафик сайта держат старые образовательные статьи про состав тела: lean mass, abs, BIA, талия. В плане их нет, и они теряют позиции: `body-fat-percentage-men-women…` потеряла 90% кликов.
- У конкурентов с похожими темами (InBody, BodySpec) огромный трафик как раз на калькуляторах и страницах «X% body fat», и эти ключи несложные (KD 0–30).

**Предлагаю:**
1. Новый хаб **«Hub 9 — Body Composition & Measurement»**. Туда входят существующие образовательные статьи, калькуляторы и серия «X% body fat».
2. Несколько строк в **Hub 3 (GLP-1)** и **Hub 1 (Fitness)**.
3. Несколько решений по каннибализации между уже опубликованными страницами.

**Как читать таблицы.** Колонки те же, что в Sheet. «Спрос» — объём в месяц по Ahrefs (US, если не сказано иначе). KD — сложность от 0 до 100; для нашего DR 63 реально до ~35. Приоритет — моё предложение, окончательно решает Вадим.

**Правило для всех строк Hub 9.** Это образовательный трафик, а не ICP-покупатели. Поэтому на каждой странице **в первых 30% текста** стоит блок, который ведёт к FitXpress: «If your app or program needs this measurement at scale: FitXpress API» → ссылка на страницу вертикали (обычно fitness или wellness) и CTA «Book a demo». Clarity показывает, что до конца статьи почти никто не доходит, а CTA в конце никто не видит.

**Язык и compliance как обычно:**
- дисклеймер «FitXpress is not a medical device.» на калькуляторах;
- без eligibility-решений;
- формулировки точности только из `accuracy-formulations.md`;
- BMI и body composition называем calculated metrics или estimates, а не measurements.

---

## A. Новый Hub 9 — Body Composition & Measurement

| # | Cluster | Article / asset | Intent | Action | Pri | Спрос / KD | Existing URL | Notes / guardrail |
|---|---|---|---|---|---|---|---|---|
| 9.1 | Main hub | Body Composition Testing: DEXA, BIA, 3D Scanning, Tape and Calipers Compared | Hub / TOFU | Refresh / expand into hub | P1 | body composition test 2 700 / KD 22; body composition analysis 1 600 / KD 30 | `/content-hub/how-to-measure-body-composition/` | Хаб, на который ссылаются все старые body-comp статьи (BIA, InBody, Fit3D, DEXA, body fat). В выдаче .edu-лаборатории и InBody, пробиться реально сравнением методов. **Граница:** accuracy-вопросы уводить ссылкой на `mobile-body-scanning-accuracy`, не повторять. **Не путать** с `body-scanning-technology-comparison` (там сравнение технологий сканирования для бизнеса) |
| 9.2 | Tools | Body Fat Percentage Calculator (US Navy method) | Tool / TOFU | Create net-new tool (страница-инструмент, делает девелопер) | **P1** | 22 000 / KD 16; UK 3 900. AI Overview нет, сайт с DR 13 стоит на #3 | — | Самая большая возможность плана. Только классическая формула по обхватам, без «по фото». Под калькулятором короткое объяснение метода и его ограничений, ссылка на 9.1 и на 9.6 |
| 9.3 | Tools | Waist-to-Height Ratio Calculator | Tool / TOFU | Create net-new tool | **P1** | 4 500 / KD 36 (UK 2 200 / **KD 12**); calculator 3 100 / KD 26 | — | Особенно UK. Ссылка на нашу статью про колебания талии (58K показов, позиция 5). Пороги WHtR — со ссылкой на NHS/NICE |
| 9.4 | Tools | Lean Body Mass Calculator | Tool / TOFU | Create net-new tool | P2 | 3 200 / KD 31 | — | Расширяет кластер lean mass, где мы уже на 1-м месте. Ссылки на 9.7 и 9.5 |
| 9.5 | Tools | Muscle Mass Calculator | Tool / TOFU | Create net-new tool | P2 | 1 400 / KD 25 | — | Можно объединить с 9.4 на одной странице, если формулы пересекаются: решить при брифе |
| 9.6 | Body fat reference | What Different Body Fat Percentages Look Like (Men and Women) | Hub / TOFU | Refresh / expand + merge | **P1** | 15% body fat 5 500 / KD 0; 20% 4 400 / KD 11; 10% 4 000 / KD 0; 25% 2 500 / KD 29; 12% 2 400 / KD 0 и др. (30+ ключей) | `/content-hub/body-fat-percentage-men-women-ai-3d-scanning-goals/` (−90% кликов) **и** `/content-hub/body-fat-percentage/` | **Каннибализация:** две страницы про body fat %. Предлагаю сильнее сделать хабом серии, слабее склеить в неё 301 (кто сильнее — проверю по GSC перед брифом). Визуализация — наши 3D-аватары, это отличие от фото у BodySpec и InBody |
| 9.7 | Body fat reference | Серия «X% body fat»: 10%, 12%, 15%, 20%, 25%, 30% (men / women) | TOFU | Create net-new **if** 9.6 выходит в топ-20 через 6–8 недель | P2 | по 800–5 500 каждый, KD 0–30 | — | Условная строка: сначала хаб 9.6, серия — только если он поднялся. Каждая страница короткая, с одним 3D-аватаром, ссылки на 9.2 и 9.6 |
| 9.8 | Lean mass | Lean Body Mass vs Muscle Mass | TOFU | Refresh / CTR | P1 | 80K показов за 3 мес., 56 кликов, позиции 6–9 | `/content-hub/lean-body-mass-vs-muscle-mass/` | Проблема не в позиции, а в клике: ответ забирает AI Overview. Новый title и meta, короткий ответ или таблица в первом экране (чтобы AIO нас цитировал), FitXpress-блок выше 30%, ссылка на 9.4 |
| 9.9 | Abs / body fat | Visible Abs Myths | TOFU | Refresh / CTR | P2 | 81K показов, 188 кликов; «what body fat percentage to see abs» 1 700 / KD 3 | `/content-hub/visible-abs-myths-measurable-outcomes-ai-driven-3d-body-scanning/` | То же, что 9.8. Ссылки на 9.6 и 9.2 |
| 9.10 | Methods | BIA scan, body composition scale, AI body scanners vs DEXA, Fit3D vs 3DLOOK, InBody vs 3DLOOK | TOFU / comparison | Refresh / link to 9.1 | P2 | — | `/content-hub/bia-scan/`, `/content-hub/body-composition-scale/`, `/content-hub/ai-body-scanners-vs-dexa-scans/`, `/content-hub/fit3d-vs-3dlook/`, `/content-hub/inbody-vs-3dlook-the-future-of-body-composition-measurement/` | Не переписывать целиком. Добавить ссылку наверх на хаб 9.1 и FitXpress-блок. Сейчас они не ведут ни на хаб, ни на продукт |

---

## B. Hub 0 и сканеры как категория

| # | Cluster | Article | Intent | Action | Pri | Спрос / KD | Existing URL | Notes / guardrail |
|---|---|---|---|---|---|---|---|---|
| 0.x1 | Category / comparison | 3D Body Scanners Compared: Booth, Hardware and Mobile | MOFU / GEO-comparison | Refresh / expand | P1 | 3d body scanner 700 / KD 26; 3d body scan 800 / KD 39; body scanner 1 000 / KD 0; body scanning technology 9,2K показов, позиция 10 | `/content-hub/body-scanning-technology-comparison/` (+383% показов, растёт) | Эта статья должна забрать и «3d body scanner», и «body scanning technology». Сейчас последний держит apparel-статья. В выдаче Styku и Fit3D (DR 49–53, ниже нашего) |
| 0.x2 | Category / comparison | Body Scanner Machines vs Mobile 3D Body Scan | — | **Merge** в 0.x1 (301) | P1 | — | `/content-hub/body-scanner-machines-vs-mobile-3d-body-scan/` | Каннибализирует 0.x1. Лучшие куски перенести, страницу склеить 301 |
| 0.x3 | Category | 3D Body Scanning (overview) vs Virtual Body Measurements | — | **Review / decide** | P2 | 2,9K показов в споре с главной; 1,2K между двумя статьями | `/content-hub/3d-body-scanning/`, `/content-hub/virtual-body-measurements/` | Две статьи и главная делят одни запросы. Предложение: `3d-body-scanning` держит «3d body scan / analysis», `virtual-body-measurements` держит «measure body online / virtual measurements», и они не пересекаются. `virtual-body-measurements` исторически дала 39 контактов и 4 сделки, её не удалять |
| 0.x4 | Listicle | Best Body Scan Apps in 2026 | MOFU / listicle | **Review / decide** | P2 | body scan app 150 / KD 46 (выдача — App Store и Google Play) | — | **Граница:** не пересекаться с открытым P0 «Top Mobile Body Scanning Software for Wellness Apps» (Hub 5, B2B, октябрь). Этот листикл потребительский. Предлагаю отложить до выхода P0 и решить по его результатам |

---

## C. Hub 3 — GLP-1 (строки с высокой чувствительностью)

| # | Cluster | Article | Intent | Action | Pri | Спрос / KD | Existing URL | Notes / guardrail |
|---|---|---|---|---|---|---|---|---|
| 3.x1 | BMI thresholds (UK) | BMI Requirements for Mounjaro and Wegovy in the UK: What Online Pharmacies Verify | MOFU / BOFU | **Section-first** в pharmacy-гайде; standalone — только по решению Вадима | P1 | **bmi for mounjaro (UK) 1 100 / KD 0**; what bmi for mounjaro 1 000 / KD 45; bmi for wegovy 400 / KD 21. Кластер ~6–8K UK + ~5K US, CPC $3–9 | `/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/` (владелец intent «BMI verification / eligibility») | Самая ценная возможность для ICP pharmacy: в UK-выдаче сайты GP с DR 0–6. **Ограничения:** (1) критерии NICE/MHRA только с первоисточником; (2) никаких «you are eligible» и eligibility-решений от FitXpress; (3) **публикация только после появления медицинского рецензента** (фармацевт с регистрацией GPhC или врач). Сейчас рецензента нет, Вадим ищет. Строку завести сейчас, статус — «ждёт рецензента» |
| 3.x2 | Muscle loss | GLP-1 and Muscle Loss: Why Programs Track Lean Mass, Not Just Weight | TOFU / MOFU | Create net-new supporting article | P2 | ozempic muscle loss 1 100 / KD 53; does ozempic cause muscle loss 1 800 / KD 52; glp-1 muscle loss 600 / KD 45; **mounjaro muscle loss (UK) 450 / KD 19** | — | В US выдаче медицинские издатели (Mayo, PMC), поэтому заходить через UK-ключи и через угол программы («что программа измеряет и зачем»), без клинических утверждений. **Граница:** не повторять `glp-1-market` (рынок) и `beyond-bmi-business` (метрики). Ссылки на 9.4 и 9.8. Рецензент желателен |

---

## D. Hub 1 — Fitness и старые статьи, которые продавали

HubSpot показал, какие статьи раньше приводили контакты со сделками. Сейчас они просели, их надо обновить в первую очередь.

| # | Cluster | Article | Intent | Action | Pri | Данные | Existing URL | Notes / guardrail |
|---|---|---|---|---|---|---|---|---|
| 1.x1 | Fitness use case | AI Body Scanning for Fitness | MOFU | Refresh / expand | **P1** | 57 контактов, 4 сделки; сессии GA4 410 → 29 год к году | `/content-hub/ai-body-scanning-for-fitness/` | По таблице overlap хаб `ai-in-fitness-industry` образовательный, а эта статья коммерческая. Сделать её мостом на `/fitxpress/for-connected-and-digital-fitness/`: CTA выше 30%, свежие примеры, без повторов хаба |
| 1.x2 | Progress tracking | Body Scanning Technology for Weight Loss | MOFU | Refresh / expand | P1 | 21 контакт, 3 сделки | `/content-hub/body-scanning-technology-for-weight-loss/` | В плане уже есть P2-строка «AI Fitness Progress Tracking: Why Weight Alone Is Not Enough», где эта статья указана как existing. **Предлагаю вместо новой статьи обновить эту**, и строку P2 закрыть этим рефрешем |
| 1.x3 | Industry | Top Fitness Tech Companies | TOFU | Refresh (уже в Backlog: обновить список и год) | P2 | «fitness software companies» 633 показа, позиция 18; «fitness technology» 735, позиция 12 | `/content-hub/top-fitness-tech-companies/` | Строка уже есть в Backlog. Прошу поднять: запросы в зоне быстрого роста |

---

## F. Hub 5 — Wellness: biometric screening (добавлено 2026-09-29, решение Вадима)

«Biometric screening» — 8 600 поисков в месяц в US при KD 3, и в плане этой темы нет совсем. Это чек-ап сотрудника в wellness-программе работодателя или страховщика: BMI, талия, давление, анализы крови. FitXpress закрывает часть с измерениями тела, поэтому Вадим решил: **лендинг wellness строится вокруг remote biometric screening**, а информационный запрос забирает статья ниже.

| # | Cluster | Article | Intent | Action | Pri | Спрос / KD | Existing URL | Notes / guardrail |
|---|---|---|---|---|---|---|---|---|
| 5.x1 | Biometric screening | Biometric Screening: What It Measures, and Which Measurements Can Be Captured Remotely | TOFU / MOFU | Create net-new supporting article | **P1** | biometric screening 8 600 / KD 3; what is a biometric screening 2 500 / KD 3; what is biometric screening 1 800 / KD 3; biometric screening meaning 500; biometric health screening 350; what is included in a biometric screening 90. UK почти нет (150): это US-тема | — | **Статья владеет информационным запросом**, лендинг `/fitxpress/for-wellness-programs/` — коммерческими («remote / at home biometric screening», «biometric screening companies», «onsite biometric screening» как альтернатива). Ссылка на лендинг — в первых 30% текста (правило `landing-map.md`). **Граница, дословно для писателя:** FitXpress закрывает измерения тела. Талия измеряется по двум фото, BMI считается из роста и веса (вес сверяет Smart Scales, бета), состав тела — оценки. Давление, холестерин, глюкоза и другие анализы крови — **нет**, и это сказано прямо. Никаких заявлений о соответствии ADA, GINA, EEOC или HIPAA для wellness-программ: дизайн стимулов определяет работодатель со своими юристами. Результаты не интерпретируем и риск здоровья не присваиваем. «FitXpress is not a medical device.» Цифры точности по отдельным измерениям не публикуем — только `accuracy-formulations.md`. Ссылки: хаб `ai-body-data-wellness-platforms`, `wellness-rewards-verification-…`, trust-FAQ. **Не пересекается** с P0-листиклом «Top Mobile Body Scanning Software for Wellness Apps» (там выбор вендора для приложений, здесь что такое скрининг и что из него можно снять удалённо) |

---

## E. Что не добавлять (решение и почему)

- **«Weight loss clinic marketing»** (`top-10-weight-loss-clinic-marketing-tips`, 12K показов) — оставить как есть. Ищут агентства, а не клиники-покупатели. Контакты и сделки ноль.
- **«bmi calculator» (2,4M), «how to measure body fat» (45K), «body fat percentage» (61K / KD 63)** — выдачу держат сайты с DR 84–95, и нам туда не пробиться. Работаем через 9.2 и 9.6.
- **Отдельные статьи под «body measurement API / SDK», «telehealth weight verification»** — спроса нет. Эти запросы закрывают страницы продукта (`/fitxpress/`, `/developers/`), а не блог.

## Порядок, если брать по одной

1. 9.2 Body fat calculator
2. 1.x1 AI body scanning for fitness
3. 0.x1 + 0.x2 comparison-статья со склейкой
4. 9.6 Body fat % хаб
5. 9.3 WHtR calculator
6. 9.8 CTR-рефреш lean mass
7. 9.1 хаб методов
8. 1.x2 рефреш weight-loss
9. 3.x1 — только когда появится рецензент

Остальное — по мере ресурсов.

Вопросы — ко мне или к Вадиму. После того как строки появятся в Sheet, скрипт `content-plan-sync.py` подтянет их в офлайн-копию в понедельник, и пайплайн статей сможет брать их в работу.
