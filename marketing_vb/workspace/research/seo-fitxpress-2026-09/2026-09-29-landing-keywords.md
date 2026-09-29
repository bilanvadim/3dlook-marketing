---
product: fitxpress
type: keyword-map
date: 2026-09-29
author: Claude (по запросу Вадима)
source: Ahrefs API v3 (2026-09-29), GSC sc-domain:3dlook.ai (2026-06-27…09-26), HubSpot AEO (снапшот 2026-09-29), контент-план v2.0 (синк 09-17 + дрифт 09-29)
builds_on: 2026-09-25-fitxpress-seo-plan.md, data/ahrefs-findings.md, data/gsc-findings.md
language: ru (переведено с украинского 2026-09-29 по просьбе Вадима)
---

# Ключи для лендингов FitXpress: по одному на хаб + страница BMI verification

## Что в этом файле

Для каждого хаба из контент-плана (Hub 0–8) описан свой лендинг `/fitxpress/for-{vertical}/`, отдельно идут родительская `/fitxpress/` и страница функции Weight & BMI verification. На каждую страницу четыре списка:

1. **Главный ключ.** Идёт в title, H1, первый абзац и meta. Один на страницу.
2. **Вторичные.** Для H2, meta description и анкоров, которыми статьи хаба ссылаются на лендинг.
3. **GEO-фразы и FAQ.** В Google спроса нет, но именно так спрашивают ChatGPT, Perplexity и Gemini (промпты из HubSpot AEO с текущей видимостью 3DLOOK) и так звучат запросы покупателей в GSC. Их ставим вопросами в FAQ, а ответ пишем первым предложением.
4. **Не для этой страницы.** Эти ключи принадлежат статье хаба или другому лендингу. Лендинг их не таргетирует, а только ссылается на владельца.

Полная таблица для Sheets лежит в `data/2026-09-29-landing-keywords.csv` (175 строк).

**Как читать цифры.** Указан объём в месяц по Ahrefs, US и UK. «—» значит, что у Ahrefs по фразе нет ни одной строки, то есть измеренного спроса нет. «0» — спрос измерили, и он нулевой. KD — сложность от 0 до 100; если KD не указан, у Ahrefs нет цифры, и это не то же самое, что ноль. Позиции и показы взяты из GSC за 3 месяца.

## Главное

1. **У продуктовых B2B-запросов почти нет спроса.** Это было видно уже в ресёрче 09-25, и вертикальные выгрузки это подтвердили. Поэтому лендинги держат позиции двумя способами:
   - там, где спрос есть, берём нишевый коммерческий ключ с низким KD: `accelerated underwriting`, `occupational health software`, `remote patient monitoring for weight loss`, «body scanner» в контексте зала;
   - там, где спроса нет (GLP-1, bariatric, clinical trials), берём GEO-фразы. Удержать позиции по ним легко, потому что конкурентов почти нет, а успех меряем видимостью в HubSpot AEO, а не трафиком.
2. **Трафик дают статьи, лендинги конвертируют.** Большие информационные запросы стоят в колонке «Не для этой страницы» и принадлежат хабам. Чтобы лендинг не съел статью и наоборот, статья ссылается на лендинг анкором из его главного ключа, а лендинг на статью — её темой.
3. **Две находки, которых нет в контент-плане:**
   - `biometric screening`: 8 600 в месяц при KD 3. **Принято 2026-09-29:** это угол wellness-лендинга, а главный информационный запрос забирает новая статья в Hub 5 (строка 5.x1 в `2026-09-27-content-plan-rows-for-assel.md`);
   - `occupational health software`: US 350 / KD 3 / $15 и UK 200 / KD 0. Самый сильный коммерческий ключ среди всех вертикалей.
4. **Страница BMI verification** — не use case, а функция, поэтому её ключи без вертикального модификатора. Эта же страница несёт и сценарий UK-аптек, потому что отдельного хаба для аптек в плане нет. UK-кластер «BMI for Mounjaro» (самый ценный, KD 0) принадлежит гайду для аптек и ждёт медицинского рецензента. Страница функции его не таргетирует.

## Сводка

| # | Страница (URL — предложение) | Главный ключ | Спрос US / UK | KD | Ориентир |
|---|---|---|---|---|---|
| 0 | `/fitxpress/` | ai body scanner | 200 / 50 | 2 | топ-3 (до 301 была 3,1, сейчас главная на 5,6) |
| 1 | `/fitxpress/bmi-verification/` (с `/for-bmi-verification/`) | bmi verification | 100 / 10 | — | топ-3 (сейчас 5,2) |
| 2 | `/fitxpress/for-connected-and-digital-fitness/` | gym body scanner (+ кластер «body scan gym») | ~220 суммарно | 1–11 | топ-5 за 3–6 мес. |
| 3 | `/fitxpress/for-telehealth/` | remote patient monitoring for weight loss | 100 / — | 1 | топ-5 |
| 4 | `/fitxpress/for-glp-1-programs/` | body composition tracking for GLP-1 programs | — | — | GEO: AEO-промпт 49% → 70%+ |
| 5 | `/fitxpress/for-insurance-underwriting/` | accelerated underwriting (+3 варианта) | ~340 суммарно | 0–1 | топ-5 |
| 6 | `/fitxpress/for-wellness-programs/` | at home / remote biometric screening | 80 / — | — | топ-5 (угол принят 2026-09-29) |
| 7 | `/fitxpress/for-bariatric-clinics/` | bariatric pre-authorization documentation | — | — | GEO: промпты 0% и 6% → вверх |
| 8 | `/fitxpress/for-clinical-trials/` | remote anthropometric measurement for clinical trials (+ кластер «DCT platform» ~410) | — | 2–12 | топ-10 по кластеру DCT |
| 9 | `/fitxpress/for-occupational-health/` | occupational health software | 350 / 200 | 3 / 0 | топ-5 |

Ориентиры — моя оценка по KD, нашему DR 63 и тому, кто стоит в выдаче. Это не прогноз.

## Правила, чтобы лендинги держали позиции и не ели друг друга

- **Один интент — один URL.** Кому что принадлежит:
  - «ai body scanner», API/SDK и бренд «fitxpress» — только `/fitxpress/`;
  - любое «verify BMI / weight» без вертикали — только страница BMI verification. Вертикальные лендинги пишут с модификатором («build and BMI evidence for underwriting») и ссылаются на неё;
  - «remote patient monitoring…» — только telehealth;
  - «GLP-1…» — только GLP-1-лендинг (telehealth упоминает GLP-1 и ссылается);
  - «body composition» без вертикали — Hub 9 (хаб методов);
  - «3d body scanner», «body scanner», «body scanning technology» — comparison-статья, не лендинги.
- **Главный ключ лендинга не появляется в title или H1 ни одной статьи.** Статьи берут информационную версию («what is…», «how to…», «process»).
- **Анкоры.** Каждая статья хаба ссылается на свой лендинг выше 30% глубины анкором из главного или вторичного ключа лендинга (правило 1 из SEO-плана). Такие ссылки — главный рычаг удержания позиций, потому что внешних ссылок на лендинги пока нет. С 2026-09-29 правило работает в пайплайне статей через `brand-assets/content-strategy/landing-map.md`.
- **GEO-фразы — дословно как H3 в FAQ,** ответ первым предложением. Так нас цитируют ИИ-ассистенты.
- **Бренд «fitxpress»** сейчас размазан по 4 URL (поз. 6,0). После запуска `/fitxpress/` остальные страницы пишут в title «FitXpress for …», а в тексте ссылаются на `/fitxpress/` анкором «FitXpress».

# Страницы

## 0. `/fitxpress/`: родительская страница FitXpress (Hub 0)

Владелец продуктовых и API-запросов. Черновик уже есть (`workspace/pages/fitxpress/`), focus keyphrase там `AI body scanner`, то есть совпадает с этим списком. После запуска сюда должен перейти бренд «fitxpress», который сейчас размазан по 4 URL.


**Главный ключ** (title, H1, первый абзац, meta)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| ai body scanner | 200 · KD 2 | 50 | Главная держит поз. 5,6 (881 показ за 3 мес., цитата в AI Overview). До 301 `/fitxpress/` стояла на 3,1 |

**Вторичные** (H2, meta description, alt, анкоры из хаба)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| fitxpress | 20 · KD 0 | 10 | Бренд. Сейчас поз. 6,0 и 4 URL: `/for-bmi-verification/`, telehealth-страница, `/for-connected-…/`. Должен остаться один |
| ai body scan | 80 · KD 0 | 30 | GSC: 458 показов, поз. 5,8 |
| body scanner ai | 10 | 0 | GSC: 269 показов, поз. 2,8 |
| ai body scanner app | 40 | 10 | GSC: 537 показов, поз. 8,4. Много consumer-трафика из Индии, под него не подстраиваться |
| mobile body scanner | 20 · KD 17 | 0 | Формулировку «mobile» используют промпты ИИ-ассистентов |

**GEO-фразы и FAQ** (спроса в Google нет, но именно так спрашивают ИИ-ассистенты и покупатели)

- body scanning software
- body scanning API / body measurement API / SDK — AEO-промпт «top mobile body scanning APIs for health apps»: видимость 65%
- mobile body scanning software for health apps
- Which body scanning tools support high-volume scan workflows for enterprise customers? — AEO, видимость 26%
- Which body scanning tools offer trials or demos? — AEO, 11%. Ответ страницы: «Book a demo», триал публично не обещаем

**Не для этой страницы** (кому принадлежит)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| 3d body scanner | 700 · KD 26 | 150 · KD 18 | Comparison-статья `body-scanning-technology-comparison` (строка 0.x1) |
| 3d body scan | 800 · KD 39 | 150 · KD 26 | Та же comparison-статья |
| body scanner | 1 000 · KD 0 | 500 · KD 32 | Та же comparison-статья |
| body scanning technology | 100 · KD 33 | 10 | Comparison-статья. Сейчас этот ключ держит apparel-статья (9,2K показов, поз. 10) |
| ai body measurement | 150 · KD 0 | 0 | Не забирать у `/mobile-tailor/`: она держит «ai body measurements», поз. 6,9 |
| body composition scanner | 200 · KD 30 | 50 · KD 1 | Родительская тема «inbody scan» (аппаратные сканеры), это Hub 9 |

**Ссылки с лендинга на хаб:** `ai-body-data-health-hub`, `mobile-body-scanning-accuracy`, `fitxpress-data-privacy-security-regulatory-faq`, все вертикальные лендинги.


---

## 1. Weight & BMI verification: страница функции (сейчас `/for-bmi-verification/`)

Это не use case, а описание функции, которой пользуются несколько вертикалей: онлайн-аптеки (UK), telehealth, страхование, bariatric pre-qualification, pre-check в исследованиях. Поэтому ключи здесь без вертикального модификатора, а вертикальные формулировки живут на лендингах и ссылаются сюда. **Отдельного хаба для онлайн-аптек в плане нет, поэтому сценарий UK-аптек несёт эта страница.**

URL: предлагаю `/fitxpress/bmi-verification/` с 301 со старого. Шаблон `for-{vertical}` сюда не подходит, а слово `bmi-verification` в slug стоит сохранить: это единственный ключ страницы со спросом, и по нему она уже на 5-й позиции.

Сейчас страница держит бренд «fitxpress» (249 показов, поз. 6,2), и все 13 её кликов за 3 месяца пришли с этого запроса. После запуска `/fitxpress/` бренд уйдёт туда, как и задумано, так что падение кликов здесь не регресс. Гайд для аптек за те же 3 месяца получил 3 показа, хотя он в индексе: тему BMI verification в Google сейчас не держит ни одна наша страница, кроме этой.

Что исправить в текущем тексте: H1 «…for Regulatory Compliance» и meta «helping telehealth prevent GLP-1 misuse and meet compliance standards» обещают комплаенс, а «AI-powered» стоит отдельно как ценность. Обе формулировки нарушают наши правила. В новом тексте: «supports eligibility review», а не «determines eligibility».


**Главный ключ** (title, H1, первый абзац, meta)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| bmi verification | 100 | 10 | US 100, но часть этого спроса — LADBS (строительный департамент Лос-Анджелеса). GSC: 81 показ, поз. 5,2 именно на этой странице |

**Вторичные** (H2, meta description, alt, анкоры из хаба)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| weight verification | 10 · KD 0 | 0 |  |
| remote bmi verification | — · KD 13 | — | Ahrefs даёт KD 13, но объёма нет |
| verified BMI | — | — | Формулировка из промптов и рекомендаций HubSpot AEO |
| weight discrepancy alerts | — | — | Название функции на странице (H3). Сам запрос «weight discrepancy» про логистику, под него не целимся |

**GEO-фразы и FAQ** (спроса в Google нет, но именно так спрашивают ИИ-ассистенты и покупатели)

- telehealth bmi verification — Интент «как» принадлежит гайду для аптек (секция про telehealth), интент «решение/софт» — этой странице. Title развести
- How do telehealth platforms accurately verify BMI without in-person visits? — AEO (UK), видимость **0%**. Самая большая дыра: страница должна ответить на это первым абзацем
- What mobile body scanning software works for remote BMI verification? — AEO, 82%
- BMI verification for GLP-1 prescribing — Сценарий UK-аптек в тексте страницы
- self-reported weight vs verified BMI — Угол misreporting. Без «fraud detection» как автоматического решения

**Не для этой страницы** (кому принадлежит)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| online pharmacy bmi verification | — | — | Title гайда `online-pharmacy-bmi-verification-…` (информационный, compliance). Страница функции — «software/solution», в title без «guide/compliance» |
| bmi for mounjaro | 60 · KD 38 | 1 100 · KD 0 | UK 1 100 / KD 0: самый ценный кластер. Владелец — секция в гайде `online-pharmacy-bmi-verification-…` (строка 3.x1), и только после медицинского рецензента |
| what bmi for mounjaro | 10 | 1 000 · KD 45 | Тот же кластер |
| bmi for wegovy | 300 · KD 39 | 400 · KD 21 | Тот же кластер |
| bmi for weight loss injections | 30 | 350 | Тот же кластер |
| bmi check | 1 800 · KD 83 | 5 600 · KD 0 | UK 5,6K, но родительская тема — «bmi calculator». Потребительский интент, никому |
| mounjaro online | 3 500 · KD 34 | 2 400 · KD 38 | Потребитель покупает препарат, никому |
| patient identity verification | 150 · KD 2 | 0 | Это не наша функция, не заявлять |

**Ссылки с лендинга на хаб:** `online-pharmacy-bmi-verification-a-2026-compliance-guide` (секция про telehealth), `mobile-body-scanning-accuracy`, trust-FAQ, а также лендинги telehealth, страхования, bariatric и clinical trials.


---

## 2. Hub 1 Fitness → `/fitxpress/for-connected-and-digital-fitness/`

URL уже правильный, чинится только breadcrumb. Сейчас страница ранжируется только по бренду (154 показа за 3 мес.), так что терять ей нечего. Спрос есть на «body scanner» в контексте зала или студии: это ровно наш аргумент «вместо аппаратного сканера».


**Главный ключ** (title, H1, первый абзац, meta)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| gym body scanner | 30 · KD 2 | — | TP 4 200: вся тема «сканер в зале» даёт топ-странице ~4K в месяц. Сейчас в выдаче Fit3D, Styku и InBody с DR ниже нашего |

**Вторичные** (H2, meta description, alt, анкоры из хаба)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| body scan gym | 60 · KD 1 | — |  |
| gym body scan | 50 · KD 4 | — |  |
| body scan machine gym | 40 · KD 11 | — | Интент — «машина». Наш ответ: мобильная альтернатива |
| body composition app | 50 · KD 2 | — |  |
| digital fitness platform | 60 · KD 3 | — |  |
| online coaching app | 150 · KD 28 | — | Только как «for online coaching apps». Сам запрос про коучинг принадлежит статье |

**GEO-фразы и FAQ** (спроса в Google нет, но именно так спрашивают ИИ-ассистенты и покупатели)

- what is a body scan at the gym — US 90 / KD 0. Ответить в FAQ
- What's the best alternative to hardware 3D body scanners for fitness studios? — AEO, 51%
- What's the best body composition tracking software for a fitness app that wants smartphone-based scans? — AEO, 61%
- Which body scanning APIs are easiest to integrate into a fitness or wellness app? — AEO, 63%
- What body scanning SDKs work for fitness apps with remote users? — AEO, 81%

**Не для этой страницы** (кому принадлежит)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| ai fitness | 600 · KD 0 | 100 · KD 38 | Хаб `ai-in-fitness-industry` (поз. 4,6–22,8) |
| connected fitness | 300 · KD 0 | — | Статья `connected-fitness-industry`, поз. 6,9 |
| body composition test | 2 700 · KD 6 | — | Hub 9, хаб методов `how-to-measure-body-composition` |
| body composition analysis | 1 600 · KD 30 | — | Hub 9 |
| online fitness coaching software | 100 · KD 71 | — | KD 71: не пробиться. Коучингу посвящена статья `remote-body-measurement-online-fitness-coaching` |
| gym member retention | 100 · KD 3 | — | Будущая статья «progress visibility as a retention lever» |
| body measurement tracker | 400 · KD 1 | — | Потребительское приложение, никому |
| fitness app development | 700 · KD 0 | — | Агентства, никому |

**Ссылки с лендинга на хаб:** `ai-in-fitness-industry`, `remote-body-measurement-online-fitness-coaching`, `ai-body-scanning-for-fitness`, `mobile-body-scanning-patient-engagement`, `body-scanning-technology-comparison`.


---

## 3. Hub 2 Telehealth → `/fitxpress/for-telehealth/` (сейчас `/structured-body-data-for-telehealth-digital-health-programs/`)

Граница с GLP-1: этот лендинг про **рабочие процессы платформы** (удалённый мониторинг, intake, API, white-label), GLP-1 — про **долгосрочное отслеживание программы**. У текущей страницы поз. 5,6, но почти весь её трафик — брендовые запросы. Переезд с 301 делать только вместе с пересборкой.


**Главный ключ** (title, H1, первый абзац, meta)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| remote patient monitoring for weight loss | 100 · KD 1 | 0 | Точное совпадение с продуктом, KD 1 |

**Вторичные** (H2, meta description, alt, анкоры из хаба)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| remote weight monitoring | 100 · KD 1 | 0 |  |
| remote patient monitoring weight | 40 | 0 |  |
| telehealth api | 100 · KD 1 | 0 | Выдачу частично держат видео-API. Формулировка: «body scanning API for telehealth platforms» |
| digital patient intake | 100 · KD 4 | 10 | Возможный H2 «remote intake with body measurements» |
| white label telehealth | 350 · KD 30 | 0 | Только как упоминание «white-label body scanning inside your telehealth app»: интент запроса — платформа целиком |

**GEO-фразы и FAQ** (спроса в Google нет, но именно так спрашивают ИИ-ассистенты и покупатели)

- best mobile body scanning solution for telehealth — GSC: 46 показов, поз. 2,9, но держит статья `body-scanner-machines-vs-mobile`, которую склеивают. Должен перейти сюда
- What is the best mobile body scanning solution for telehealth? — AEO, 63%
- Which mobile body scanning solution best improves patient engagement metrics? — AEO, 90%
- What body measurement tools minimize exposure of personal data during remote scans? — AEO, 11%. Короткий ответ и ссылка на trust-FAQ
- remote body measurement for telehealth

**Не для этой страницы** (кому принадлежит)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| ai in telehealth | 100 · KD 53 | 20 | Хаб `the-potential-of-ai-in-telehealth` (поз. 21–33) |
| ai telehealth | 100 · KD 51 | 0 | Тот же хаб |
| patient engagement software | 1 300 · KD 2 | 150 · KD 27 | Статья `mobile-body-scanning-patient-engagement` (каноническая тема engagement) |
| remote patient monitoring | 6 800 · KD 51 | 250 · KD 0 | 6,8K / KD 51, интент — RPM-устройства и платформы. Упоминать можно, целиться не стоит |
| remote patient monitoring software | 1 100 · KD 12 | 100 · KD 8 | Тот же интент (RPM-платформы) |
| telehealth weight loss | 450 · KD 39 | 0 | Пациент ищет программу, никому |
| virtual weight loss clinic | 350 · KD 39 | 20 | Пациент, никому |
| telehealth bmi verification | — · KD 1 | — | Страница BMI verification и гайд для аптек |

**Ссылки с лендинга на хаб:** `the-potential-of-ai-in-telehealth`, `mobile-body-scanning-patient-engagement`, `online-pharmacy-bmi-verification-…` (секция telehealth), `fitxpress-admin-panel-launch`, а также будущая статья «Telehealth Documentation» (октябрь).


---

## 4. Hub 3 GLP-1 → `/fitxpress/for-glp-1-programs/`

В Google нет ни одного B2B-запроса с заметным спросом. Всё, что ищут про GLP-1, касается либо пациента (клиника рядом, приложение-трекер), либо медицинского вопроса (потеря мышц). Поэтому лендинг держит позиции на GEO-фразах, где конкурентов почти нет. Трафик даст статья про потерю мышц, и она должна вести сюда. Слово «tools» в title лендинга не ставить: его держит листикл «7 Body Composition & Progress-Tracking Tools for Remote GLP-1 Clinics».


**Главный ключ** (title, H1, первый абзац, meta)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| body composition tracking for GLP-1 programs | — | — | Спроса нет. Это главный вопрос ИИ-ассистентам (см. ниже) |

**Вторичные** (H2, meta description, alt, анкоры из хаба)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| weight loss clinic software | 10 | 10 | Мизерный объём, зато точный интент покупателя |
| medical weight loss software | 10 | 0 | То же |
| GLP-1 progress tracking | — | — | У Ahrefs данных нет |
| lean mass tracking on GLP-1 | — | — | Мостик к статье про потерю мышц |

**GEO-фразы и FAQ** (спроса в Google нет, но именно так спрашивают ИИ-ассистенты и покупатели)

- How can a GLP-1 weight-loss clinic track patient body composition remotely? Include tools. — AEO, 49%
- glp-1 weight-loss clinic remote body composition tracking tools — GSC: листикл top-7 на поз. 1
- what software supports glp workflows? — GSC, листикл, поз. 11

**Не для этой страницы** (кому принадлежит)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| ozempic muscle loss | 1 100 · KD 53 | 200 · KD 54 | Новая статья 3.x2 «GLP-1 and Muscle Loss» (в плане пока нет). Лендинг — в FAQ со ссылкой |
| does ozempic cause muscle loss | 1 800 · KD 52 | 200 | Та же статья |
| glp 1 muscle loss | 400 · KD 11 | 30 | Та же статья, KD 11 |
| tirzepatide muscle loss | 500 · KD 37 | 150 | Та же статья |
| mounjaro muscle loss | 300 · KD 26 | 450 · KD 19 | Та же статья. UK KD 19: заходить через UK |
| glp-1 market | 150 · KD 43 | 10 | Хаб `glp-1-market` |
| glp-1 tracker app free | 300 | — | Кластер «glp 1 tracker app» ~1,7K суммарно по вариантам, но это потребительские приложения (Shotsy). Никому |
| glp-1 clinic | 250 · KD 2 | 0 | Локальный пациентский интент |
| medical weight loss clinic | 1 700 · KD 5 | 150 · KD 45 | Локальный пациентский интент |

**Ссылки с лендинга на хаб:** `glp-1-market`, `top-7-remote-body-composition-tools-glp-1-clinics`, `visual-progress-tracking-glp1-…`, `beyond-bmi-business`, `ai-body-scanners-vs-dexa-scans`, а также будущая статья «GLP-1 Patient Progress Record» (октябрь).


---

## 5. Hub 4 Insurance → `/fitxpress/for-insurance-underwriting/`

Черновик уже есть (`workspace/pages/for-insurance-underwriting/`, 08-31), но URL там старый: `/for-insurance-underwriting/`, `parent: /`. Под новую иерархию его надо исправить. H1 черновика «…for accelerated life insurance underwriting» уже попадает в главный ключ. Guardrail хаба: только поддержка андеррайтинга и BMI/build verification, без автоматического андеррайтинга и выявления мошенничества.


**Главный ключ** (title, H1, первый абзац, meta)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| accelerated underwriting | 100 · KD 0 | 10 | KD 0. Вместе с вариантами ниже ~340 в месяц |

**Вторичные** (H2, meta description, alt, анкоры из хаба)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| accelerated underwriting life insurance | 90 · KD 1 | — |  |
| life insurance accelerated underwriting | 90 · KD 0 | — |  |
| life insurance underwriting software | 150 · KD 11 | — |  |
| insurance underwriting software | 450 · KD 11 | 200 · KD 9 | Интент — core-системы (Guidewire). Только упоминание «works inside your underwriting workflow» |
| digital underwriting | 30 · KD 1 | 70 | В UK выше, чем в US |
| paramedical exam | 350 · KD 3 | 0 | Только в контексте «меньше paramed-визитов ради роста и веса». Не писать, что мы заменяем paramed |

**GEO-фразы и FAQ** (спроса в Google нет, но именно так спрашивают ИИ-ассистенты и покупатели)

- what is accelerated underwriting — US 60, в FAQ
- remote height and weight verification for life insurance
- build and BMI evidence for underwriting — Формулировка из черновика

**Не для этой страницы** (кому принадлежит)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| life insurance underwriting | 800 · KD 0 | 200 · KD 1 | Хаб `mobile-body-scanning-insurance-underwriting` |
| life insurance underwriting process | 350 · KD 4 | 40 | Тот же хаб |
| life insurance build chart | 100 · KD 0 | 0 | Строка «BMI Verification for Life Insurance» (refresh секции хаба) |
| life insurance height and weight chart | 70 · KD 0 | 0 | Та же строка |
| bmi life insurance | 200 · KD 0 | 100 | Та же строка |
| life insurance fraud | 600 · KD 7 | 80 · KD 2 | Строка «Self-Reported BMI vs Verified Body Data» (review/decide) |
| underwriting automation | 350 · KD 12 | 60 | Никому: guardrail «no automated underwriting» |
| automated underwriting life insurance | 100 | 0 | Никому, та же причина |
| no medical exam life insurance | 3 000 · KD 13 | 300 · KD 6 | Потребительский продукт, никому |

**Ссылки с лендинга на хаб:** `mobile-body-scanning-insurance-underwriting`, страница BMI verification, `wellness-rewards-verification-…`, `mobile-body-scanning-accuracy`, trust-FAQ.


---

## 6. Hub 5 Wellness → `/fitxpress/for-wellness-programs/`

**Угол — remote biometric screening (Вадим, 2026-09-29).** «Biometric screening» даёт 8 600 в месяц при KD 3, а в контент-плане этой темы не было. Biometric screening в wellness-программах работодателей — это BMI, талия, давление и анализы крови. FitXpress закрывает часть с измерениями тела: талию измеряет по двум фото, BMI считает из роста и веса (вес сверяет Smart Scales, бета), состав тела даёт как оценки. Давление и анализы крови он не закрывает, и страница говорит это прямо.

Лендинг берёт коммерческие модификаторы: «at home», «remote», «companies», а «onsite» — как альтернативу. Главный информационный запрос забирает новая статья в Hub 5 (строка 5.x1 в списке для Ассель). Границы и запреты — правило 7 в `landing-map.md`: никаких заявлений о соответствии ADA, GINA, EEOC или HIPAA для wellness-программ и никакой интерпретации результатов.


**Главный ключ** (title, H1, первый абзац, meta)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| at home biometric screening | 80 | 0 | Принято 2026-09-29. Формула в title/H1: «remote biometric screening» + «body measurements» |

**Вторичные** (H2, meta description, alt, анкоры из хаба)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| biometric screening companies | 90 · KD 3 | 0 |  |
| onsite biometric screening | 150 · KD 4 | 0 | Угол: удалённая альтернатива для части с измерениями |
| company biometric screening | 100 · KD 3 | — |  |
| wellness rewards program | 200 · KD 1 | 0 | Угол rewards verification. Подробно — статья `wellness-rewards-verification-…` |
| corporate wellness platform | 500 · KD 15 | 60 | Интент — платформа целиком. Формулировка: «for corporate wellness platforms» |
| employee wellness app | 200 · KD 1 | 60 |  |

**GEO-фразы и FAQ** (спроса в Google нет, но именно так спрашивают ИИ-ассистенты и покупатели)

- remote biometric screening — У Ahrefs данных нет
- Best mobile body scanning software for fitness and wellness platforms? — AEO, 53%
- Which body scanning tools are suitable for health and wellness apps that need HIPAA or GDPR controls? — AEO, 78%. Ответ без «HIPAA compliant»: только формулировки из trust-FAQ
- full body scan for employees wellness program — GSC, статья про rewards, поз. 12,8

**Не для этой страницы** (кому принадлежит)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| biometric screening | 8 600 · KD 3 | 150 · KD 7 | 8,6K / KD 3. Новая статья в Hub 5 (строка 5.x1 для Ассель) |
| what is a biometric screening | 2 500 · KD 3 | — | Та же статья |
| corporate wellness programs | 2 600 · KD 0 | 500 · KD 4 | Хаб `ai-body-data-wellness-platforms` |
| wellness incentives | 700 · KD 0 | 150 · KD 0 | Статья `wellness-rewards-verification-…` |
| nutrition coaching software | 100 · KD 0 | 150 | Строка P1 «Body Data for Nutrition and Lifestyle Coaching Platforms» |
| wellness app | 1 000 · KD 2 | 100 · KD 18 | Потребитель, никому |

**Ссылки с лендинга на хаб:** `ai-body-data-wellness-platforms`, `wellness-rewards-verification-employers-insurers-…`, `mobile-body-scanning-patient-engagement`, `beyond-bmi-business`, а также P0-листикл «Top Mobile Body Scanning Software for Wellness Apps» (октябрь; «best/top» оставить ему) и будущая статья про biometric screening (5.x1).


---

## 7. Hub 6 Bariatrics → `/fitxpress/for-bariatric-clinics/`

Весь спрос в Google — пациентский («каким должен быть BMI для операции»). Это YMYL, и это не наши покупатели. Для клиник спроса нет, зато ИИ-ассистенты задают как раз наши вопросы, и в двух из трёх у нас видимость 0–6%. HubSpot AEO отдельно рекомендует с высоким приоритетом страницу «FitXpress for Bariatric Pre-Auth Measurements». Значит, лендинг строим под pre-auth.


**Главный ключ** (title, H1, первый абзац, meta)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| bariatric pre-authorization documentation | — | — | Спроса нет. Главный сценарий (HubSpot AEO, HIGH) |

**Вторичные** (H2, meta description, alt, анкоры из хаба)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| bariatric software | 30 | 0 | GSC: хаб на поз. 19,7 |
| bariatric clinic software body measurement records | — | — | GSC: хаб на поз. 3,6 |
| bariatric program | 150 · KD 30 | — | Только как упоминание «for bariatric programs»: интент запроса локальный |
| bariatric surgery insurance requirements | 10 | — | Угол «документация для payer» |

**GEO-фразы и FAQ** (спроса в Google нет, но именно так спрашивают ИИ-ассистенты и покупатели)

- How can a weight-loss surgery program reduce manual measurement work during pre-auth? — AEO, **0%**
- Which tools can support remote body data collection before bariatric surgery consultations? — AEO, **6%**
- What software helps bariatric clinics collect auditable body measurement records for payer documentation? — AEO, 62%

**Не для этой страницы** (кому принадлежит)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| bariatric surgery requirements | 1 100 · KD 59 | — | Пациент, YMYL. Максимум секция в хабе |
| bmi for bariatric surgery | 450 · KD 53 | — | Пациент, YMYL |
| weight loss surgery requirements | 600 · KD 0 | — | Пациент |
| gastric sleeve requirements | 400 · KD 0 | — | Пациент |
| bariatric pre-qualification | — | — | Title хаба (`bariatric-pre-qualification-…`), лендинг только ссылается |
| bariatric app | 200 · KD 11 | — | Приложение для пациентов (Baritastic), никому |

**Ссылки с лендинга на хаб:** `bariatric-pre-qualification-mobile-3d-body-scanning`, `glp-1-market`, страница BMI verification, `fitxpress-admin-panel-launch`, а также будущие статьи «Pre-Authorization Documentation» и «Patient Progress Record» (P1).


---

## 8. Hub 7 Clinical trials → `/fitxpress/for-clinical-trials/`

FitXpress здесь не DCT-платформа, а модуль измерений внутри неё, поэтому ключи вроде «DCT platform» идут с формулировкой «for DCT platforms». Информационные запросы («decentralized clinical trials», «anthropometric measurements») остаются хабу. Хаб в индексе, но за 3 месяца получил 1 показ.

**Конфликт title:** SEO-title хаба — «Clinical Trial Anthropometric Measurement Software | 3DLOOK», то есть продуктовый, и он совпадает с главным ключом лендинга. Как и с occ-health, вместе с запуском лендинга title хаба сменить на процессный, например «Standardizing Anthropometric Measurements in Obesity Trials».


**Главный ключ** (title, H1, первый абзац, meta)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| remote anthropometric measurement for clinical trials | — | — | Спроса нет. Главная фраза для title/H1 вместе с «decentralized and hybrid trials» |

**Вторичные** (H2, meta description, alt, анкоры из хаба)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| decentralized clinical trial platform | 100 · KD 10 | — | CPC $12: дорогой коммерческий запрос |
| decentralized clinical trials platform | 100 · KD 8 | — |  |
| dct platform | 70 · KD 2 | — |  |
| decentralized clinical trials technology | 70 | — |  |
| decentralized clinical trials software | 70 · KD 12 | — |  |
| remote patient monitoring clinical trials | 90 · KD 14 | — |  |
| clinical trial technology | 200 · KD 1 | — |  |

**GEO-фразы и FAQ** (спроса в Google нет, но именно так спрашивают ИИ-ассистенты и покупатели)

- body measurements in obesity trials between site visits
- anthropometric measurement software — После смены title хаба — лендингу

**Не для этой страницы** (кому принадлежит)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| anthropometric measurements | 2 100 · KD 6 | — | 2,1K / KD 6, академический интент. Хаб (`clinical-trial-anthropometric-…`) |
| decentralized clinical trials | 500 · KD 12 | — | Хаб |
| hybrid clinical trials | 200 · KD 1 | — | Хаб, секция про hybrid |
| benefits of decentralized clinical trials | 200 · KD 6 | — | Хаб |
| obesity clinical trials | 150 · KD 11 | — | Пациенты ищут исследования, никому |
| ecoa | 5 700 · KD 52 | — | Другая категория продуктов, никому |
| waist circumference measurement | 450 · KD 47 | — | Hub 9 |

**Ссылки с лендинга на хаб:** `clinical-trial-anthropometric-measurement-software-obesity-trials`, `mobile-body-scanning-accuracy`, trust-FAQ, а также будущие статьи «What CROs Should Ask» и «DCT Platform Integration» (P1).


---

## 9. Hub 8 Occupational health → `/fitxpress/for-occupational-health/`

Самый сильный коммерческий ключ среди всех вертикалей: «occupational health software» (US 350 / KD 3 / $15, UK 200 / KD 0). Ищут его OH-провайдеры, то есть наши покупатели, хотя продуктовая категория совпадает частично: FitXpress — модуль intake, а не полная OH-система. Формулировка: «adds remote body measurement intake to your occupational health software».

**Риск каннибализации:** slug хаба — `occupational-health-screening-software`. Хаб остаётся на процессе («screening», «pre-employment»), лендинг забирает «software»-запросы. Сейчас SEO-title хаба — «Occupational Health Screening Software | 3DLOOK» (H1 без «software»). **Вместе с запуском лендинга title хаба сменить на процессный**, например «Occupational Health Screening: Faster Intake and Documentation», а из хаба на лендинг поставить анкор «occupational health screening software».


**Главный ключ** (title, H1, первый абзац, meta)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| occupational health software | 350 · KD 3 | 200 · KD 0 |  |

**Вторичные** (H2, meta description, alt, анкоры из хаба)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| occupational health management software | 150 · KD 1 | 200 |  |
| occupational medicine software | 150 · KD 0 | 30 |  |
| employee health screening software | 40 | 10 | GSC: хаб на поз. 25 |
| employee health screening | 250 · KD 1 | 400 · KD 0 | UK 400 / KD 0 |
| pre placement health assessment | 30 | 50 | UK-термин |

**GEO-фразы и FAQ** (спроса в Google нет, но именно так спрашивают ИИ-ассистенты и покупатели)

- pre employment medical software — GSC: хаб на поз. 18
- what are the best tools for occupational health screening without wearables — GSC: хаб на поз. 1,2 (запросы в стиле ИИ)
- what technology is used for pre-employment health screening in 2026 — GSC: поз. 1,0
- can occupational health screening be done remotely? — GSC: поз. 6,2. В FAQ

**Не для этой страницы** (кому принадлежит)

| Ключ | US | UK | Примечание |
|---|---|---|---|
| occupational health screening | 250 · KD 6 | 200 · KD 2 | Хаб (сейчас поз. 51) |
| pre employment health screening | 150 · KD 5 | 200 · KD 0 | Хаб и секция pre-employment |
| return to work assessment | 80 · KD 0 | 150 | Строки про return-to-work (P1) |
| workers compensation return to work | 150 · KD 0 | 0 | Строка про workers' comp (P1) |
| fitness for duty evaluation | 350 · KD 0 | 0 | Только строка «Fit-for-Duty Intake» (ASK). Guardrail: никаких решений о допуске |
| occupational health assessment | 300 · KD 1 | 3 700 · KD 9 | UK 3,7K, но ищут работники. Никому |
| dot physical | 34 000 · KD 0 | 50 · KD 14 | 34K, осмотр водителей, никому |

**Ссылки с лендинга на хаб:** `occupational-health-screening-software`, `manual-vs-digital-intake-occupational-health-screening`, trust-FAQ, а также будущие статьи «Return-to-Work Documentation» и «Workforce Screening Vendors» (P1).


---
## Что требует решения

1. ~~**Wellness и biometric screening.**~~ **Решено 2026-09-29: берём.** Лендинг берёт «remote / at home biometric screening», а Ассель заводит в Hub 5 статью (строка 5.x1 в `2026-09-27-content-plan-rows-for-assel.md`).
2. **Occupational health software.** Берём этот ключ, хотя FitXpress — модуль intake, а не полная OH-система? Ищут его наши покупатели (OH-провайдеры), но в выдаче будут OH-EHR. Я бы брал, с формулировкой «adds remote intake to your occupational health software».
3. **Slug-и.** Все URL в таблице — предложения под иерархию `/fitxpress/for-{vertical}/`. Для страницы функции предлагаю `/fitxpress/bmi-verification/` (не `for-`). В черновике страхования URL ещё старый: `/for-insurance-underwriting/`.
4. **Новые строки контент-плана.** Кроме biometric screening, это статья про потерю мышц на GLP-1 (строка 3.x2 уже есть в списке для Ассель от 09-27). Она забирает кластер ~5K в US (ozempic, tirzepatide, mounjaro muscle loss) и ведёт на GLP-1-лендинг.
5. **Два хаба с «software» в title.** Это `occupational-health-screening-software` («Occupational Health Screening Software») и `clinical-trial-anthropometric-…` («Clinical Trial Anthropometric Measurement Software»). Их title совпадают с главными ключами лендингов. В день запуска лендинга title хаба нужно сменить на процессный, slug оставить (301 не нужен). У остальных хабов конфликтов нет, сверено с живыми title 09-29.

## Данные

- Ahrefs: 44 запроса overview и matching-terms, ~34K юнитов (всего 117K из 800K, счётчик сбрасывается 09-30). Сырые JSON лежат в scratchpad сессии, в репо их нет.
- GSC: page × query по 25 хабам и лендингам, 2026-06-27…09-26, 981 строка. Гайд для аптек и хаб clinical trials за этот период получили 3 и 1 показ, хотя оба в индексе (URL Inspection 09-29, PASS). Значит, проблема не техническая: под их формулировки в Google просто нет спроса.
- HubSpot AEO: 24 промпта, только два ICP (Telehealth & Weight-Loss, Connected Fitness). Для страхования, occ-health и trials промптов нет, поэтому GEO-фразы там взяты из GSC и гайдов хабов. Вариант промпта под biometric screening отправлен Вадиму в Telegram 09-29.
