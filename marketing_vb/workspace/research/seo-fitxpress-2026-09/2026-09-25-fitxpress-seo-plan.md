---
product: fitxpress
type: seo-growth-plan
date: 2026-09-25
author: Claude (по запросу Вадима)
status: draft — ждёт решений Вадима (раздел 9)
---

# FitXpress: план выхода в топ по health и fitness

## Источники

| Источник | Объём | Период |
|---|---|---|
| Google Search Console (`sc-domain:3dlook.ai`) | — | L3M = 2026-06-24…09-22, P3M = 03-25…06-23, YoY = 2025-06-24…09-22 |
| GA4 (property 251675969) | — | 90 дней и год к году. Трекинг страниц лежал 02-05…06-25 |
| Ahrefs API v3 | 40K units | — |
| Microsoft Clarity | ~10–20 живых сессий на FitXpress-страницу | последние 72 часа, 09-22…09-25 (больше API не даёт) |
| HubSpot | 8 761 контакт, 1 858 сделок | контакты с 2024-09, сделки с 2022 |
| Последовательный обход сайта | все 194 URL | — |

Сырые таблицы лежат в `data/`: `gsc-`, `ga4-`, `ahrefs-`, `onsite-` и `clarity-findings.md`, а также `keypages.md`. `hubspot-findings.md` с суммами пайплайна и выручки лежит только локально на VPS: репозиторий публичный, файл исключён через `.git/info/exclude`. На сайте и в CRM ничего не менялось.

---

## 1. Коротко

1. **Органика продавала и перестала.**
   - С 2024-09 органика дала 131 сделку и 25 побед. Из них FitXpress: 44 сделки, 4 победы и ещё 9 открытых. Суммы — в локальном `data/hubspot-findings.md`, в git его нет, потому что репозиторий публичный.
   - Органических контактов было 95–155 в месяц в 2025 году. Стало 37 в июле 2026, 24 в августе и 15 в сентябре.
   - **Цель плана — органический FitXpress-пайплайн в HubSpot, а не позиции ради позиций.**
2. **Главная не работает как страница FitXpress.**
   - По решению 2026-08-23 FitXpress-родитель — главная. Но её title не называет ни FitXpress, ни BMI, ни API, а в тексте одна ссылка.
   - Отдельных страниц под вертикали ICP (GLP-1, pharmacy, insurance, occ-health, trials, bariatric) нет.
   - Документация API живёт на поддомене с одной nofollow-ссылкой.
   - Старый `/fitxpress/` до 301 в марте стоял на 3,1 месте по «ai body scanner» и дал 745 кликов за 9 месяцев.
3. **Путь к конверсии сломан технически.**
   - `/pricing/`: мёртвые клики в 10% сессий, JS-ошибки в 21% (на мобильных в 27%).
   - `/contact-us/`: JS-ошибки в 31% сессий (на десктопе в 42%).
   - Кнопки demo сделаны на JS, а не обычными ссылками.
   - Это главная страница выручки: форма Contact us & Partnership принесла 143 контакта со сделками, ссылки бронирования встреч ещё 117.
   - **Чинить нужно до любого нового контента.**
4. **Health-контент даёт показы, а не лиды.**
   - Доля health-страниц: 48% показов, 19% кликов, 0 конверсий в GA4.
   - За 24 месяца health-статьи были первой страницей для 251 контакта. Сделки есть у 12.
   - Статьи дочитывают на 5–35% (Clarity), поэтому CTA в конце не видит никто.
   - Со статей на продукт почти нет ссылок.
5. **Consumer-трафик — это мусор в CRM.**
   - 60% органических контактов первым делом видят главную.
   - Popup на главной собрал 743 контакта, 90% из них с Gmail-адресов, в основном из Индии, Индонезии, Саудовской Аравии и Египта.
   - По органике Индия (18%) почти догнала US (19%). UK, CA, AU и DE вместе дают ~11%.
6. **Запросов по самому продукту почти нет.**
   - «body measurement API/SDK», «telehealth weight verification», «GLP-1 progress tracking» — 0–20 поисков в месяц.
   - Отсюда два слоя:
     - страницы продукта нужны для конверсии и для цитирования ИИ-ассистентами;
     - трафик и тематический авторитет — из health-тем с реальным спросом (калькуляторы body fat, WHtR и lean mass; порог BMI для GLP-1 в UK; 3D body scanner). **Каждая такая страница ведёт на продукт.**
7. **Ссылки не проблема.**
   - DR 63 — лучший среди body-scan вендоров: Styku 53, Fit3D 49, Bodygram 46, Prism 28.
   - Органики у API-конкурентов почти нет, B2B-ниша в поиске свободна.
   - Реальные соперники в health-выдаче — BodySpec и InBody.
8. **Измерения не позволяют увидеть прогресс.**
   - GA4: ключевое событие одно (`/contact-us/`). Ещё 298 отправок форм и 259 кликов demo не учитываются.
   - Внутренний трафик не отфильтрован.
   - По Clarity, 63% сессий — боты. Все 47 сессий google/cpc — тоже боты.
   - HubSpot: `utm_*` не заполняется никогда, `industry` пуст на 100%, поля ICP-сегмента у сделок нет. 42% контактов с источником «Offline», у них нет ни страницы, ни формы.
9. **ИИ-ассистенты — единственный растущий веб-источник.**
   - HubSpot: 260 контактов, 8 сделок (побед пока нет).
   - GA4: ~1,4K сессий, из них ChatGPT 1 233.
   - Но ИИ ведут на главную и страницы Mobile Tailor. LLM всё ещё видят в 3DLOOK фешн-бренд.

---

## 2. Диагноз в цифрах

### Поиск (GSC и Ahrefs)

**Трафик**
- **Органика в целом (Ahrefs):** 5 953 в месяц в марте 2025 → 653 в сентябре 2026, −89%.
- **Health/fitness-клики по видимым запросам:** 2 937 (YoY) → 1 795 (P3M) → 742 (L3M).
- **Небрендовые видимые клики:** 4 623 в июле 2025 → 339 в августе 2026.
- **Брендовые показы:** ~4,8K → 2,2K в месяц. Спрос на бренд упал вдвое.

**Позиции FitXpress**
- **«fitxpress»:** 6-е место. Запрос размазан по 4–8 URL, главный из них `/for-bmi-verification/` (659 слов).
- **«ai body scanner»:** 1-е место в Ahrefs, 5,6 в GSC, есть в AI Overview. Это единственный коммерческий head-термин в топе.
- **Остальные head-термины:** «3d body scanner» 26, «body scanner» 28, «3d body composition scanner» 33.
- **Кластеры ICP:**
  - Telehealth / AI in healthcare: 8,3K показов, 0 кликов, позиция 39,7.
  - GLP-1: 7,2K показов, 12 кликов, позиция 35. `/glp-1-market/` на 43–68 месте.
- **Десктоп** (где идёт B2B-ресёрч): позиция 20,5, CTR 0,1%. Мобайл: позиция 8,5.

**Другие проблемы**
- **Нулевой CTR на больших страницах:** lean-body-mass (80K показов, 56 кликов), visible-abs (81K / 188). В 9 из 10 целевых выдач есть AI Overview.
- **Каннибализация:**
  - главная и `/content-hub/3d-body-scanning/`;
  - `3d-body-scanning` и `virtual-body-measurements`;
  - `body-scanner-machines-vs-mobile` и `body-scanning-technology-comparison`;
  - «body scanning technology» (9,2K показов, позиция 10) держит apparel-статья.

**Что растёт**
- `body-scanning-technology-comparison`: +383% показов.
- `/structured-body-data-for-telehealth-digital-health-programs/`: новая, позиция 5,6.
- `3dlook-turns-two-photos-structured-body-data`: +62%.
- Статья о колебаниях талии: 58K показов, позиция 5.

### Конверсия и CRM (GA4, HubSpot, Clarity)

**Выручка и лиды**
- **Органика в выручке:** 32% сделок, 27% пайплайна, 39% побед, но только 20% выигранной выручки. В FitXpress органика — 22% сделок и 16% выручки. Победы FitXpress пришли в основном из Direct (6), Offline (5), Organic (4) и Referrals (2).
- **Органические лиды в GA4 год к году:** 59 → 31 (−47%). Органических сессий 18,1K → 13,4K.
- **FitXpress-воронка:** 196 сделок с 2024-09, 17 побед, win rate 13%. У Mobile Tailor 215 сделок и 47 побед.

**Статьи, которые когда-то продавали**
| Статья | Контакты | Сделки | Трафик сейчас (GA4) |
|---|---|---|---|
| ai-body-scanning-for-fitness | 57 | 4 | 410 → 29 сессий |
| body-scanning-technology-for-weight-loss | 21 | 3 | — |
| virtual-body-measurements | 39 | 4 | — |

**Их надо обновлять в первую очередь.**

**eBook**
- «The Next Big Leap in Health»: 128 контактов, 6 сделок.
- eBook по GLP-1: 38 контактов, 0 сделок.

**Формы, которые приносят сделки**
- Contact us & Partnership: 1 115 контактов, 1% личных email.
- Ссылки на бронирование встреч.
- Новые FX pricing-формы (FX Starter / Talk to sales): 63 контакта за 12 месяцев.
- FitXpress-лендинги: 76% личных email.

**Поведение (Clarity, 72 часа)**
- Health-статьи дочитывают на 5–35%, активное время меньше 30 секунд.
- Мобайл — треть реального трафика: 31 секунда активности против 88 на десктопе.
- На `/for-bmi-verification/` 20% сессий с мёртвыми кликами и 20% quickbacks.

### Сайт и E-E-A-T

**Внутренние ссылки**
- Главный хаб `/content-hub/ai-body-data-health-hub/` не связан с хабами GLP-1, Telehealth, Fitness и Wellness.
- 60 из 160 постов получают ссылки только со страницы `/sitemap/`.
- `/content-hub/` показывает 10 постов и не имеет пагинации.

**Структура**
- `/fitxpress/for-connected-and-digital-fitness/` сидит на несуществующем уровне URL, и её breadcrumb ведёт на 404.
- `/fitxpress` без слеша редиректит на блог-пост.

**Техника**
- FAQ-schema trust-FAQ невалидна: WordPress вставляет `<br />` в JSON-LD.
- В `robots.txt` все Disallow стоят под `anthropic-ai`.
- GPTBot получает 403.
- `llms.txt` устарел.
- `http://www.3dlook.ai/` отдаёт 404.
- `/contact/` отдаёт 404 (111 заходов).
- TTFB 0,7 с, HTML ~320 KB.

**Авторство**
- Страниц авторов нет.
- В schema в качестве автора стоят «admin» и сырой email.
- Медицинского рецензента нет.

**Compliance**
- Бейдж «HIPAA Compliant» стоит на каждой странице.
- На главной написано «never link photos to personal identifiers».
- Обе фразы противоречат trust-FAQ и являются hard fail.

**Фешн-перекос**
- Фешн-постов ~107, health ~53.
- В меню Safariland и Digiday.
- Health-кейс на сайте один.
- UK Meds, Yazen и Healthyr есть только логотипами, и alt-тексты у логотипов бредовые (Healthyr подписан как «Reddit»).

---

## 3. Стратегия

### Три уровня целей

| Уровень | Что | Зачем | KPI |
|---|---|---|---|
| **A. Деньги** | Главная (FitXpress), `/for-{vertical}/`, `/developers/`, pricing, кейсы; ключи API/SDK/software, BMI verification, ключи вертикалей | Конверсия и цитирование ИИ | Органические FX-сделки и пайплайн в HubSpot; топ-3 по 30–40 B2B-ключам |
| **B. Категория** | ai body scanner, 3d body scanner, body scanner, body composition analysis/test, 3d body scan | Нас должны находить в своей категории | «ai body scanner» — топ-3, «3d body scanner» — топ-10 |
| **C. Авторитет и трафик** | Калькуляторы, «X% body fat», BMI для GLP-1 (UK), GLP-1 и потеря мышц | Тематический авторитет, ссылки, бренд | Клики и ссылки; переходы C → A |

### Три правила

1. **Каждая страница уровня C ведёт на A.** Контекстный FitXpress-блок ставится **выше 30% глубины страницы**, а не в конце: Clarity показывает, что ниже почти никто не доходит.
2. **Consumer-лиды не попадают в воронку продаж.** Форму на главной и формы калькуляторов квалифицируем (рабочий email, роль, компания). Consumer-посетителей не гоним в «Contact sales».
3. **География: US и UK** (UK — для pharmacy и GLP-1), затем CA, AU, DE. Consumer-волны из Азии и MENA не преследуем.

---

## 4. План по фазам

### Фаза 0. Измерения и путь к конверсии (недели 1–2, блокирует всё остальное)

| # | Действие | Кто |
|---|---|---|
| 0.1 | **Починить `/pricing/` и `/contact-us/`.** В Clarity UI найти элементы с мёртвыми кликами (карта кликов, слои dead/rage) и текст JS-ошибок (записи с фильтром JS errors, дашборд top errors). Исправить скрипты форм и кнопок, demo-кнопки сделать обычными `<a href>` | dev + Вадим (Clarity UI) |
| 0.2 | **GA4.** Ключевые события на каждую форму с `form_name`: contact, pricing (FX Starter, Talk to sales), home popup, ebook. Плюс `demo_click`, `docs_click`, `meeting_booked` | dev |
| 0.3 | **Фильтры.** Внутренний трафик (офис/VPN, wp-admin, staging, UA/PL) в GA4 и Clarity. Сегмент ботов для Direct. Сверить paid-сессии с кликами Google Ads (в Clarity все 47 cpc-сессий — боты) | Вадим |
| 0.4 | **HubSpot.** Скрытые поля UTM и landing page в формах. Свойства контакта и сделки: `icp_segment` (10 сегментов FX) и `product` (FX/MT). Заполнение `industry`. Отделить careers-формы и Offline-импорты от маркетинговой атрибуции | Вадим / RevOps |
| 0.5 | **Квалификация.** Popup на главной и формы калькуляторов: рабочий email или поле «компания/роль»; lead scoring, чтобы личные email не попадали в MQL | Вадим |
| 0.6 | **Дашборд «FitXpress organic»** (Looker Studio + HubSpot-отчёт): сессии и позиции по уровням A/B/C → формы → контакты с рабочим email → FX-сделки и пайплайн по landing page | я |
| 0.7 | **Трекинг позиций.** ~60 ключей трёх уровней раз в неделю через Ahrefs API по образцу `gsc-indexing-watch.py`, диф в Telegram | я |
| 0.8 | **Редиректы.** 301 `/contact/` → `/contact-us/`; `http://www` → `https://`; `/fitxpress` без слеша → на главную | dev |
| 0.9 | **Compliance.** Убрать бейдж «HIPAA Compliant» и «never link photos to personal identifiers», заменить формулировками из `compliance.md` | dev + Вадим |

### Фаза 1. Архитектура FitXpress (недели 1–4, самый сильный рычаг)

Все страницы идут через скилл `page-builder`: гейты G-I, G-A, G-T и слепой судья с порогом 85/100. Иерархия по решению 2026-08-23: **главная — родитель FitXpress, вертикали на `/for-{vertical}/`, уровня `/fitxpress/` нет.** Пересмотр этого решения вынесен в вопросы (раздел 9).

**1.1. Главная как полноценная страница FitXpress.**
- Title вроде «AI Body Scanner & Body Measurement API for Health | 3DLOOK FitXpress». Description про BMI verification и API.
- Блоки:
  - что измеряем: 80+ body measurements, BMI, body composition estimates;
  - как работает: 2 фото;
  - **ссылки в тексте** на каждую `/for-*` (сейчас они только в выпадающем меню);
  - интеграция: API/SDK, Admin Panel, docs, pricing;
  - кейсы;
  - trust (из `compliance.md`);
  - FAQ.
- Schema: `SoftwareApplication` или `Product`, `Organization`, валидный `FAQPage`.
- Popup квалифицирует (п. 0.5).

**1.2. Лендинги вертикалей `/for-{vertical}/`**
- Каждый: 800–1 500 слов, кейс или proof point, CTA выше 30% глубины, FAQ, ссылки на хаб и на 3–5 статей кластера.
- **Гейт G-I:** у каждой FX-вертикали максимум один кейс. Нужен второй кейс, согласованный референс или записанный waiver.

| Страница | Статус | Приоритет |
|---|---|---|
| Telehealth и GLP-1 programs | есть `/structured-body-data-for-telehealth-…/` (позиция 5,6): усилить и связать, URL не трогать | P0 |
| Online pharmacies (UK, BMI verification) | тонкий `/for-bmi-verification/`: расширить, разобраться с 20% мёртвых кликов | P0 |
| Connected & digital fitness | перенести с `/fitxpress/for-…` на `/for-connected-and-digital-fitness/` с 301, починить breadcrumb | P0 |
| Life insurance underwriting | нет | P1 |
| Employer wellness и health plans | нет | P1 |
| Occupational health | нет | P1 |
| Clinical trials (DCT) | нет | P2 |
| Bariatric и metabolic clinics | нет | P2 |
| Plastic surgery clinics (Турция) | нет | P2 |

**1.3. `/developers/` на основном домене.** Обзор API, quickstart, SDK (iOS/Android/Web), лимиты, dofollow-ссылка на `docs.fitxpress.3dlook.me`. Это канонический источник для запросов по API/SDK и для ИИ-ассистентов.

**1.4. Кейсы UK Meds, Yazen, Healthyr отдельными страницами.** Нужно согласие клиентов, иначе обезличенно. Заменить сгенерированные alt-тексты логотипов.

**1.5. Перелинковка**
- Главный хаб ↔ хабы GLP-1, Telehealth, Fitness, Wellness и pharmacy-гайд.
- В каждой health-статье одна контекстная ссылка на лендинг вертикали и одна на главную с FitXpress-анкором, выше 30% глубины. Начать со страниц с наибольшими показами: lean-body-mass, visible-abs, waist-fluctuation, comparison.
- Старые body-composition посты (BIA, InBody, Fit3D, DEXA, body fat) собрать в хаб «Body composition measurement methods».
- Пагинация `/content-hub/`, фильтры тем сделать ссылками, найти место для 60 постов-сирот.

**1.6. Каннибализация**
- Главная держит «ai body scanner», `3d-body-scanning` — «3d body scan / analysis». Развести title, H1 и анкоры.
- `3d-body-scanning` и `virtual-body-measurements`: развести или склеить.
- `body-scanner-machines-vs-mobile` склеить 301 в растущую `body-scanning-technology-comparison`.
- Под «body scanning technology» (9,2K показов) сделать health-страницу или переориентировать comparison, чтобы запрос не держала apparel-статья.

### Фаза 2. Техническая гигиена (недели 1–3, параллельно)

- **FAQ JSON-LD:** убрать `wpautop` из блока, прогнать Rich Results Test по всем FAQ-страницам.
- **`robots.txt`:** пересобрать группы. Для `*` закрыть `/?s=`, `/author/`, `*utm*=`.
- **GPTBot:** снять 403 в WAF/Cloudflare. Рекомендация — пускать все поисковые ИИ-боты: ChatGPT уже даёт контакты и сделки.
- **`llms.txt`:** пересобрать (главная как FitXpress, `/for-*`, хабы, `/developers/`, trust-FAQ), убрать URL с редиректами. `/blog/` — один 301 вместо двух.
- **Авторы:** страницы `/author/…` с био и `Person`-schema. Убрать «admin» и email из поля автора. **Медицинский или клинический рецензент** (`reviewedBy`) на YMYL-страницах: GLP-1, BMI, body composition.
- **Скорость и мобайл:** WP Rocket (critical CSS, лишние виджеты Elementor), цель TTFB меньше 0,4 с. Отдельно разобрать мобильные JS-ошибки: на мобайле 12% сессий с ошибками против 8% на десктопе, на `/pricing/` 27%.
- **После каждой волны:** `gsc-indexing-watch.py` и ручной «Request indexing».

### Фаза 3. Контент (месяцы 1–4)

Статьи — через `/new-article`, страницы и инструменты — через `page-builder`. Все новые темы сначала заводятся строками в контент-плане: без строки Phase 0 gate в `seo-planner` остановит статью.

**3.1. Обновить статьи, которые когда-то продавали** (самый быстрый путь к сделкам):
- `ai-body-scanning-for-fitness`: 57 контактов, 4 сделки; сессии упали 410 → 29.
- `body-scanning-technology-for-weight-loss`: 21 контакт, 3 сделки.
- `virtual-body-measurements`: 39 контактов, 4 сделки. Заодно решить каннибализацию из 1.6.
- Обновлять на месте, с FitXpress-блоком выше 30% и ссылками на вертикали.

**3.2. Интерактивные инструменты** (лучшее соотношение спроса и сложности):

| Инструмент | Спрос US | KD | Примечание |
|---|---|---|---|
| Body fat percentage calculator (метод US Navy, опционально «по 2 фото») | 22K | 16 | Нет AI Overview; сайт с DR 13 стоит на #3 |
| Waist-to-height ratio calculator | 4,5K / 3,1K (UK 2,2K, KD 12) | 26–36 | Наша сильная тема |
| Lean body mass calculator | 3,2K | 31 | Наша lean-mass статья стоит на 7-м месте |
| Muscle mass calculator | 1,4K | 25 | |

- На каждом инструменте блок «Embed this in your app: FitXpress API» и B2B-форма с триалом на 200 запросов. Квалификация — п. 0.5.
- Дисклеймер дословно: «FitXpress is not a medical device.»

**3.3. Порог BMI для GLP-1 в UK** — самый ценный кластер: KD 0, CPC $3–9, прямо в ICP pharmacy.
- «BMI for Mounjaro»: 1,1K в UK при KD 0. В выдаче страницы GP с DR 0–6. Весь кластер ~6–8K в UK и ~5K в US.
- Страницы:
  1. Гайд «BMI requirements for Mounjaro / Wegovy in the UK» (критерии NICE/MHRA со ссылками на источники).
  2. Гайд «How online pharmacies verify BMI for GLP-1 prescribing» со ссылкой на pharmacy-лендинг.
  3. Опционально калькулятор с порогами. Формулировки только информационные, без «you are eligible». **Нужна проверка compliance.**
- Рядом: «GLP-1 / Ozempic muscle loss» (~5K в US, KD 11–53), со ссылкой на отслеживание lean mass и body composition.

**3.4. Серия «X% body fat».**
- 30+ ключей по 800–5 500 в месяц, KD 0–30.
- Хаб «What X% body fat looks like» и страницы 10/15/20/25/30% для мужчин и женщин с 3D-визуализациями: наши аватары выигрывают у фото BodySpec.
- Страница `body-fat-percentage-men-women…` потеряла 90% и станет хабом серии.
- Серия ведёт на `/for-connected-and-digital-fitness/`.

**3.5. Уровень B.**
- «3D body scanners compared: booth vs mobile» на базе растущей comparison-статьи.
- «Body composition test / analysis».
- «Best body scan apps» с честным сравнением: в «body scan app» выдачу держат App Store и Google Play, другого способа войти нет.

**3.6. CTR-рефреш страниц с огромными показами и нулевыми кликами.**
- Title и meta под клик. Короткий ответ или таблица в первом экране, чтобы нас цитировал AI Overview, а не заменял.
- FitXpress-блок выше 30%.

**3.7. ICP-статьи (уровень A).** Продолжаем контент-план (GLP-1, telehealth, pharmacy, occ-health, insurance), но **каждая статья привязана к лендингу вертикали**, а head-ключ проверен в Ahrefs (`seed_has_data`). Темы без спроса честно помечаем как GEO и поддержку продаж.

**3.8. eBook.** «The Next Big Leap in Health» работает (6 сделок), GLP-1 eBook — нет (0 сделок). Ставить первый на health-хабы и в калькуляторы. Второй переупаковать под pharmacy/telehealth-оператора.

### Фаза 4. Ссылки и PR (месяцы 1–6)

- **Быстрые каталоги:** PitchBook, Product Hunt (запуск FitXpress API / Admin Panel), Wellfound, HackerNoon, G2 и Capterra (категории body scanning software, telehealth tools).
- **Health-медиа** (Women's Health, Men's Journal, Verywell Fit, Shape, MindBodyGreen, MedPage Today; DR 82–87): digital PR на собственных анонимизированных данных. Через Ассель и compliance.
- **Наука:** страница «Research & validation» и публикация или препринт о точности. Формулировки — только из `accuracy-formulations.md`. У Fit3D и InBody ссылки идут с Frontiers, BMC и ~13 университетов.
- **Экосистема:** Rock Health, EIT Health, интеграционные страницы партнёров, «powered by 3DLOOK» у клиентов.
- **Калькуляторы как линкбейт:** embed-код «Powered by 3DLOOK».
- **Анкоры:** на лендинги вертикалей, брендовые — на главную.

### Фаза 5. GEO: поиск через ИИ (с месяца 1)

**Цель.** На «body measurement API for telehealth» или «how to verify BMI online pharmacy» ChatGPT, Perplexity и Gemini называют FitXpress и ведут на health-страницу, а не на Mobile Tailor.

**Что сделать**
- Главная, `/developers/`, вертикали и trust-FAQ получают короткие фактические блоки: что это, для кого, цены от $1K за 500 запросов, триал на 200 запросов.
- Свежий `llms.txt` и доступ для GPTBot.
- Одинаковое описание FitXpress в G2, Capterra, Crunchbase и Wikidata.
- Упоминания в LinkedIn и Reddit через соцпайплайн.

**Как измеряем**
- Раз в месяц 20 промптов в ChatGPT, Perplexity и Gemini: упоминают ли FitXpress и какую страницу цитируют.
- Плюс HubSpot-отчёт по контактам и сделкам из ИИ-источников (сейчас 260 контактов и 8 сделок).

### Фаза 6. Фешн-наследие (месяцы 2–4)

- **Аудит ~107 фешн-постов** (трафик, ссылки, контакты в HubSpot):
  - мёртвые — noindex или 301 в раздел Mobile Tailor;
  - живые (например, `body-scanning-technology-for-apparel`: 48 контактов, 6 сделок) — оставить и изолировать в разделе Mobile Tailor.
- **Меню:** FitXpress и Mobile Tailor как два равноценных раздела. Safariland и Digiday убрать из глобального меню.

---

## 5. Таймлайн

| Когда | Результат |
|---|---|
| Недели 1–2 | Фаза 0: pricing и contact починены, GA4-события и фильтры, UTM и поля в HubSpot, квалификация popup, compliance-правки, дашборд; технические правки фазы 2 |
| Недели 2–4 | Главная переписана как страница FitXpress; `/developers/`; P0-вертикали; перелинковка хабов; рефреш трёх статей, которые продавали |
| Месяц 2 | P1-вертикали; калькуляторы body fat и WHtR; UK-кластер BMI для GLP-1; 2 кейса |
| Месяцы 3–4 | Серия «X% body fat»; калькуляторы lean mass и muscle mass; CTR-рефреш; фешн-консолидация; P2-вертикали |
| Месяцы 3–6 | PR на данных, каталоги, research-страница, ежемесячный GEO-замер |

## 6. KPI на 6 месяцев

Ориентиры. Core updates и AI Overviews могут съесть часть CTR.

| Метрика | Сейчас | Цель |
|---|---|---|
| Органические FX-сделки (HubSpot, первый контакт — organic) | 11 за 12 мес. (~3 в квартал) | 6–8 в квартал |
| Органические контакты с рабочим email | 42 за 2026-Q2 | ≥ 120 в квартал (уровень 2025) |
| Лиды в GA4 с health-страниц | 0 | > 0 каждый месяц, растёт |
| JS-ошибки на `/pricing/` и `/contact-us/` (Clarity) | 21% / 31% сессий | < 3% |
| «fitxpress» | 6-е место, 4–8 URL | 1-е место на главной |
| «ai body scanner» / «3d body scanner» | 5,6 / 26 | топ-3 / топ-10 |
| B2B-ключи уровня A в топ-3 | ~5 | 15+ |
| Небрендовые health-клики | 742 за 3 мес. | ×2–3 |
| Калькулятор body fat (US), «bmi for mounjaro» (UK) | — | топ-10 / топ-5 |
| Контакты из ИИ-ассистентов | ~11 в месяц | ×2, причём с health-страниц |

## 7. Чего не делать

- Не гнаться за «bmi calculator» (2,4M) и «how to measure body fat» (45K): там сайты с DR 84–95.
- Не писать новые ICP-статьи без лендинга, на который они ведут.
- Не возвращать consumer-запросы из MENA и Азии и не пускать такие лиды в продажи.
- Не ставить CTA только в конце статьи.
- Не писать «HIPAA compliant», «medical-grade», «processed, not stored» и подобное: только `compliance.md`. Точность — только из `accuracy-formulations.md`.

## 8. Что посмотреть руками в Clarity (API этого не даёт)

1. Карта кликов `/pricing/` со слоями dead и rage clicks: какой элемент не отвечает.
2. Записи `/pricing/` и `/contact-us/` с фильтром «JS errors» и дашборд top errors.
3. Heatmap прокрутки главной, `/for-bmi-verification/`, telehealth-страницы и 3–4 health-статей: где стоит CTA относительно того, где люди уходят.
4. Воронка demo_click → `/contact-us/` → submit.
5. Paid-сессии против кликов Google Ads.
6. Фильтр внутреннего трафика.

## 9. Вопросы к Вадиму

0. **Иерархия.** Оставляем решение 2026-08-23 (главная — это FitXpress, уровня `/fitxpress/` нет) или возвращаем отдельный `/fitxpress/`, который до 301 стоял на 3,1 месте по «ai body scanner»? План написан под текущее решение.
1. **Правки сайта.** Кто делает правки в WordPress/Elementor и чинит JS на pricing/contact: dev в команде или мы через `page-builder` и ручную вставку?
2. **Кейсы.** Согласятся ли UK Meds, Yazen и Healthyr на публичные кейсы с именем?
3. **Гейт G-I.** Где брать второй кейс или референс для telehealth/GLP-1, pharmacy и fitness? Или даём waiver?
4. **Рецензент.** Есть ли медицинский или клинический консультант, которого можно указать рецензентом YMYL-страниц?
5. **Калькуляторы.** Только классические (сантиметровая лента) или с живым демо API «по 2 фото» (нужны trial-ключ и бэкенд)?
6. **ИИ-боты.** Пускаем GPTBot (сейчас 403)?
7. **HubSpot.** Кто добавит поля `icp_segment` и `product`, UTM и скрытые поля в формы: ты или RevOps?
8. **Бюджет** на PR и каталоги (у G2 и Capterra платное featured-размещение)?
9. **Контент-план.** Калькуляторы и новые темы нужно завести строками. Кто добавляет их в Sheet: Ассель или я?
