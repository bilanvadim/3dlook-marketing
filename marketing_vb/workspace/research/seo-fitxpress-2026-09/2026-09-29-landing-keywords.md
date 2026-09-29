---
product: fitxpress
type: keyword-map
date: 2026-09-29
author: Claude (на запит Вадима)
source: Ahrefs API v3 (2026-09-29), GSC sc-domain:3dlook.ai (2026-06-27…09-26), HubSpot AEO (снапшот 2026-09-29), контент-план v2.0 (синк 09-17 + дрифт 09-29)
builds_on: 2026-09-25-fitxpress-seo-plan.md, data/ahrefs-findings.md, data/gsc-findings.md
---

# Ключі для лендінгів FitXpress: по одному на хаб + сторінка BMI verification

## Що в цьому файлі

Для кожного хабу з контент-плану (Hub 0–8) описаний свій лендінг `/fitxpress/for-{vertical}/`, окремо йдуть батьківська `/fitxpress/` і сторінка фічі Weight & BMI verification. На кожну сторінку чотири списки:

1. **Головний ключ.** Іде в title, H1, перший абзац і meta. Один на сторінку.
2. **Вторинні.** Для H2, meta description і анкорів, якими статті хабу посилаються на лендінг.
3. **GEO-фрази і FAQ.** У Google попиту немає, але саме так питають ChatGPT, Perplexity і Gemini (промпти з HubSpot AEO з поточною видимістю 3DLOOK) і так звучать запити покупців у GSC. Їх ставимо питаннями у FAQ, а відповідь пишемо першим реченням.
4. **Не для цієї сторінки.** Ці ключі належать хаб-статті або іншому лендінгу. Лендінг їх не таргетить, а тільки посилається на власника.

Повна таблиця для Sheets лежить у `data/2026-09-29-landing-keywords.csv` (175 рядків).

**Як читати цифри.** Вказано обсяг на місяць за Ahrefs, US і UK. «—» означає, що Ahrefs не має по фразі жодного рядка, тобто виміряного попиту немає. «0» — попит виміряли, і він нульовий. KD — складність від 0 до 100; якщо KD не вказано, Ahrefs цифри не має, і це не те саме, що нуль. Позиції й покази взяті з GSC за 3 місяці.

## Головне

1. **Продуктові B2B-запити майже не мають попиту.** Це вже було видно в ресерчі 09-25, і вертикальні вивантаження це підтвердили. Тому лендінги тримають позиції двома способами:
   - там, де попит є, беремо нішевий комерційний ключ з низьким KD: `accelerated underwriting`, `occupational health software`, `remote patient monitoring for weight loss`, «body scanner» у контексті зали;
   - там, де попиту немає (GLP-1, bariatric, clinical trials), беремо GEO-фрази. Позиції на них утримати легко, бо конкурентів майже немає, а вимірюємо успіх видимістю в HubSpot AEO, а не трафіком.
2. **Трафік дають статті, лендінги конвертують.** Великі інформаційні запити стоять у колонці «Не для цієї сторінки» і належать хабам. Щоб лендінг не з'їв статтю і навпаки, стаття посилається на лендінг анкором з його головного ключа, а лендінг на статтю — її темою.
3. **Дві знахідки, яких немає в контент-плані:**
   - `biometric screening`: 8 600 на місяць при KD 3. **Прийнято 2026-09-29:** це кут wellness-лендінгу, а головний інформаційний запит забирає нова стаття в Hub 5 (рядок F в `2026-09-27-content-plan-rows-for-assel.md`);
   - `occupational health software`: US 350 / KD 3 / $15 і UK 200 / KD 0. Найсильніший комерційний ключ серед усіх вертикалей.
4. **Сторінка BMI verification** — не use case, а фіча, тому її ключі не мають вертикального модифікатора. Ця сторінка несе і сценарій UK-аптек, бо окремого хабу для аптек у плані немає. UK-кластер «BMI for Mounjaro» (найцінніший, KD 0) належить гайду для аптек і чекає на медичного рецензента. Сторінка фічі його не таргетить.

## Зведення

| # | Сторінка (URL — пропозиція) | Головний ключ | Попит US / UK | KD | Орієнтир |
|---|---|---|---|---|---|
| 0 | `/fitxpress/` | ai body scanner | 200 / 50 | 2 | топ-3 (до 301 була 3,1, зараз головна на 5,6) |
| 1 | `/fitxpress/bmi-verification/` (з `/for-bmi-verification/`) | bmi verification | 100 / 10 | — | топ-3 (зараз 5,2) |
| 2 | `/fitxpress/for-connected-and-digital-fitness/` | gym body scanner (+ кластер «body scan gym») | ~220 сумарно | 1–11 | топ-5 за 3–6 міс. |
| 3 | `/fitxpress/for-telehealth/` | remote patient monitoring for weight loss | 100 / — | 1 | топ-5 |
| 4 | `/fitxpress/for-glp-1-programs/` | body composition tracking for GLP-1 programs | — | — | GEO: AEO-промпт 49% → 70%+ |
| 5 | `/fitxpress/for-insurance-underwriting/` | accelerated underwriting (+3 варіанти) | ~340 сумарно | 0–1 | топ-5 |
| 6 | `/fitxpress/for-wellness-programs/` | at home / remote biometric screening | 80 / — | — | топ-5 (кут прийнято 2026-09-29) |
| 7 | `/fitxpress/for-bariatric-clinics/` | bariatric pre-authorization documentation | — | — | GEO: промпти 0% і 6% → вгору |
| 8 | `/fitxpress/for-clinical-trials/` | remote anthropometric measurement for clinical trials (+ кластер «DCT platform» ~410) | — | 2–12 | топ-10 на кластері DCT |
| 9 | `/fitxpress/for-occupational-health/` | occupational health software | 350 / 200 | 3 / 0 | топ-5 |

Орієнтири — моя оцінка за KD, нашим DR 63 і тим, хто стоїть у видачі. Це не прогноз.

## Правила, щоб лендінги тримали позиції і не їли одне одного

- **Один інтент — один URL.** Кому що належить:
  - «ai body scanner», API/SDK і бренд «fitxpress» — тільки `/fitxpress/`;
  - будь-яке «verify BMI / weight» без вертикалі — тільки сторінка BMI verification. Вертикальні лендінги пишуть із модифікатором («build and BMI evidence for underwriting») і посилаються на неї;
  - «remote patient monitoring…» — тільки telehealth;
  - «GLP-1…» — тільки GLP-1-лендінг (telehealth згадує GLP-1 і посилається);
  - «body composition» без вертикалі — Hub 9 (хаб методів);
  - «3d body scanner», «body scanner», «body scanning technology» — comparison-стаття, не лендінги.
- **Головний ключ лендінгу не з'являється в title чи H1 жодної статті.** Статті беруть інформаційну версію («what is…», «how to…», «process»).
- **Анкори.** Кожна стаття хабу посилається на свій лендінг вище 30% глибини анкором з головного або вторинного ключа лендінгу (це правило 1 з SEO-плану). Такі посилання — головний важіль утримання позицій, бо зовнішніх посилань на лендінги поки немає.
- **GEO-фрази — дослівно як H3 у FAQ,** відповідь першим реченням. Так нас цитують ШІ-асистенти.
- **Бренд «fitxpress»** зараз розмазаний по 4 URL (поз. 6,0). Після запуску `/fitxpress/` решта сторінок у title пишуть «FitXpress for …», а в тексті посилаються на `/fitxpress/` анкором «FitXpress».

# Сторінки

## 0. `/fitxpress/`: батьківська сторінка FitXpress (Hub 0)

Сторінка-власник продуктових і API-запитів. Драфт уже є (`workspace/pages/fitxpress/`), focus keyphrase там `AI body scanner`, тобто збігається з цим списком. Після запуску сюди має перейти бренд «fitxpress», який зараз розмазаний по 4 URL.


**Головний ключ** (title, H1, перший абзац, meta)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| ai body scanner | 200 · KD 2 | 50 | Головна тримає поз. 5,6 (881 показ за 3 міс., цитата в AI Overview). До 301 `/fitxpress/` стояла на 3,1 |

**Вторинні** (H2, meta description, alt, анкори з хабу)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| fitxpress | 20 · KD 0 | 10 | Бренд. Зараз поз. 6,0, 4 URL: `/for-bmi-verification/`, telehealth-сторінка, `/for-connected-…/`. Має лишитися один |
| ai body scan | 80 · KD 0 | 30 | GSC: 458 показів, поз. 5,8 |
| body scanner ai | 10 | 0 | GSC: 269 показів, поз. 2,8 |
| ai body scanner app | 40 | 10 | GSC: 537 показів, поз. 8,4. Багато consumer-трафіку з Індії, під нього не підлаштовуватися |
| mobile body scanner | 20 · KD 17 | 0 | Формулювання «mobile» використовують промпти ШІ-асистентів |

**GEO-фрази і FAQ** (попит у Google нульовий, але саме так питають ШІ-асистенти і покупці)

- body scanning software
- body scanning API / body measurement API / SDK — AEO-промпт «top mobile body scanning APIs for health apps»: видимість 65%
- mobile body scanning software for health apps
- Which body scanning tools support high-volume scan workflows for enterprise customers? — AEO, видимість 26%
- Which body scanning tools offer trials or demos? — AEO, 11%. Відповідь сторінки: «Book a demo», тріал публічно не обіцяємо

**Не для цієї сторінки** (кому належить)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| 3d body scanner | 700 · KD 26 | 150 · KD 18 | Comparison-стаття `body-scanning-technology-comparison` (рядок 0.x1) |
| 3d body scan | 800 · KD 39 | 150 · KD 26 | Та сама comparison-стаття |
| body scanner | 1 000 · KD 0 | 500 · KD 32 | Та сама comparison-стаття |
| body scanning technology | 100 · KD 33 | 10 | Comparison-стаття. Зараз цей ключ тримає apparel-стаття (9,2K показів, поз. 10) |
| ai body measurement | 150 · KD 0 | 0 | Не забирати в `/mobile-tailor/`: вона тримає «ai body measurements», поз. 6,9 |
| body composition scanner | 200 · KD 30 | 50 · KD 1 | Батьківська тема «inbody scan» (апаратні сканери), це Hub 9 |

**Посилання з лендінгу на хаб:** `ai-body-data-health-hub`, `mobile-body-scanning-accuracy`, `fitxpress-data-privacy-security-regulatory-faq`, усі вертикальні лендінги.


---

## 1. Weight & BMI verification: сторінка фічі (зараз `/for-bmi-verification/`)

Це не use case, а опис функції, яку використовують кілька вертикалей: онлайн-аптеки (UK), telehealth, страхування, bariatric pre-qualification, pre-check у дослідженнях. Тому ключі тут без вертикального модифікатора, а вертикальні формулювання живуть на лендінгах і посилаються сюди. **Окремого хабу для онлайн-аптек у плані немає, тож сценарій UK-аптек несе ця сторінка.**

URL: пропоную `/fitxpress/bmi-verification/` з 301 зі старого. Шаблон `for-{vertical}` сюди не пасує, а слово `bmi-verification` у slug варто зберегти: це єдиний ключ сторінки з попитом, і вона на ньому вже стоїть на 5-й позиції.

Зараз сторінка тримає бренд «fitxpress» (249 показів, поз. 6,2), і всі 13 її кліків за 3 місяці прийшли з цього запиту. Після запуску `/fitxpress/` бренд піде туди, як і задумано, тож падіння кліків тут не буде регресом. Гайд для аптек за ті ж 3 місяці мав 3 покази при тому, що він в індексі: тему BMI verification у Google зараз не тримає жодна наша сторінка, крім цієї.

Що виправити в поточному тексті: H1 «…for Regulatory Compliance» і meta «helping telehealth prevent GLP-1 misuse and meet compliance standards» обіцяють комплаєнс, а «AI-powered» стоїть окремо як цінність. Обидва формулювання порушують наші правила. У новому тексті: «supports eligibility review», а не «determines eligibility».


**Головний ключ** (title, H1, перший абзац, meta)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| bmi verification | 100 | 10 | US 100, але частина цього попиту — LADBS (будівельний департамент Лос-Анджелеса). GSC: 81 показ, поз. 5,2 саме на цій сторінці |

**Вторинні** (H2, meta description, alt, анкори з хабу)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| weight verification | 10 · KD 0 | 0 |  |
| remote bmi verification | — · KD 13 | — | Ahrefs дає KD 13, але обсягу немає |
| verified BMI | — | — | Формулювання з промптів і рекомендацій HubSpot AEO |
| weight discrepancy alerts | — | — | Назва фічі на сторінці (H3). Сам запит «weight discrepancy» — про логістику, під нього не цілимося |

**GEO-фрази і FAQ** (попит у Google нульовий, але саме так питають ШІ-асистенти і покупці)

- telehealth bmi verification — Інтент «як» належить гайду аптек (секція про telehealth), інтент «рішення/софт» — цій сторінці. Title розвести
- How do telehealth platforms accurately verify BMI without in-person visits? — AEO (UK), видимість **0%**. Найбільша діра: сторінка має відповісти на це першим абзацом
- What mobile body scanning software works for remote BMI verification? — AEO, 82%
- BMI verification for GLP-1 prescribing — Сценарій UK-аптек у тексті сторінки
- self-reported weight vs verified BMI — Кут misreporting. Без «fraud detection» як автоматичного рішення

**Не для цієї сторінки** (кому належить)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| online pharmacy bmi verification | — | — | Title гайду `online-pharmacy-bmi-verification-…` (інформаційний, compliance). Сторінка фічі — «software/solution», у title без «guide/compliance» |
| bmi for mounjaro | 60 · KD 38 | 1 100 · KD 0 | UK 1 100 / KD 0: найцінніший кластер. Власник — секція в гайді `online-pharmacy-bmi-verification-…` (рядок 3.x1), і тільки після медичного рецензента |
| what bmi for mounjaro | 10 | 1 000 · KD 45 | Той самий кластер |
| bmi for wegovy | 300 · KD 39 | 400 · KD 21 | Той самий кластер |
| bmi for weight loss injections | 30 | 350 | Той самий кластер |
| bmi check | 1 800 · KD 83 | 5 600 · KD 0 | UK 5,6K, але батьківська тема — «bmi calculator». Споживчий інтент, нікому |
| mounjaro online | 3 500 · KD 34 | 2 400 · KD 38 | Споживач купує препарат, нікому |
| patient identity verification | 150 · KD 2 | 0 | Це не наша функція, не заявляти |

**Посилання з лендінгу на хаб:** `online-pharmacy-bmi-verification-a-2026-compliance-guide` (секція про telehealth), `mobile-body-scanning-accuracy`, trust-FAQ, а також лендінги telehealth, страхування, bariatric і clinical trials.


---

## 2. Hub 1 Fitness → `/fitxpress/for-connected-and-digital-fitness/`

URL уже правильний, лагодиться лише breadcrumb. Зараз сторінка ранжується тільки за брендом (154 покази за 3 міс.), тож втрачати їй нічого. Попит є на «body scanner» у контексті зали чи студії: це точно наш аргумент «замість апаратного сканера».


**Головний ключ** (title, H1, перший абзац, meta)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| gym body scanner | 30 · KD 2 | — | TP 4 200: уся тема «сканер у залі» віддає топ-сторінці ~4K на місяць. Зараз у видачі Fit3D, Styku та InBody з DR нижчим за наш |

**Вторинні** (H2, meta description, alt, анкори з хабу)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| body scan gym | 60 · KD 1 | — |  |
| gym body scan | 50 · KD 4 | — |  |
| body scan machine gym | 40 · KD 11 | — | Інтент — «машина». Наша відповідь: мобільна альтернатива |
| body composition app | 50 · KD 2 | — |  |
| digital fitness platform | 60 · KD 3 | — |  |
| online coaching app | 150 · KD 28 | — | Лише як «for online coaching apps». Сам запит про коучинг належить статті |

**GEO-фрази і FAQ** (попит у Google нульовий, але саме так питають ШІ-асистенти і покупці)

- what is a body scan at the gym — US 90 / KD 0. Відповісти в FAQ
- What's the best alternative to hardware 3D body scanners for fitness studios? — AEO, 51%
- What's the best body composition tracking software for a fitness app that wants smartphone-based scans? — AEO, 61%
- Which body scanning APIs are easiest to integrate into a fitness or wellness app? — AEO, 63%
- What body scanning SDKs work for fitness apps with remote users? — AEO, 81%

**Не для цієї сторінки** (кому належить)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| ai fitness | 600 · KD 0 | 100 · KD 38 | Хаб `ai-in-fitness-industry` (поз. 4,6–22,8) |
| connected fitness | 300 · KD 0 | — | Стаття `connected-fitness-industry`, поз. 6,9 |
| body composition test | 2 700 · KD 6 | — | Hub 9, хаб методів `how-to-measure-body-composition` |
| body composition analysis | 1 600 · KD 30 | — | Hub 9 |
| online fitness coaching software | 100 · KD 71 | — | KD 71: не пробитися. Коучингу присвячена стаття `remote-body-measurement-online-fitness-coaching` |
| gym member retention | 100 · KD 3 | — | Майбутня стаття «progress visibility as a retention lever» |
| body measurement tracker | 400 · KD 1 | — | Споживчий застосунок, нікому |
| fitness app development | 700 · KD 0 | — | Агенції, нікому |

**Посилання з лендінгу на хаб:** `ai-in-fitness-industry`, `remote-body-measurement-online-fitness-coaching`, `ai-body-scanning-for-fitness`, `mobile-body-scanning-patient-engagement`, `body-scanning-technology-comparison`.


---

## 3. Hub 2 Telehealth → `/fitxpress/for-telehealth/` (зараз `/structured-body-data-for-telehealth-digital-health-programs/`)

Межа з GLP-1: цей лендінг про **робочі процеси платформи** (віддалений моніторинг, intake, API, white-label), GLP-1 — про **поздовжнє відстеження програми**. Поточна сторінка має поз. 5,6, але майже весь її трафік — брендові запити. Переїзд із 301 робити тільки разом із перезбиранням.


**Головний ключ** (title, H1, перший абзац, meta)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| remote patient monitoring for weight loss | 100 · KD 1 | 0 | Точний збіг із продуктом, KD 1 |

**Вторинні** (H2, meta description, alt, анкори з хабу)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| remote weight monitoring | 100 · KD 1 | 0 |  |
| remote patient monitoring weight | 40 | 0 |  |
| telehealth api | 100 · KD 1 | 0 | Видачу частково тримають відео-API. Формулювання: «body scanning API for telehealth platforms» |
| digital patient intake | 100 · KD 4 | 10 | Можливий H2 «remote intake with body measurements» |
| white label telehealth | 350 · KD 30 | 0 | Тільки як згадка «white-label body scanning inside your telehealth app»: інтент запиту — платформа цілком |

**GEO-фрази і FAQ** (попит у Google нульовий, але саме так питають ШІ-асистенти і покупці)

- best mobile body scanning solution for telehealth — GSC: 46 показів, поз. 2,9, але тримає стаття `body-scanner-machines-vs-mobile`, яку склеюють. Має перейти сюди
- What is the best mobile body scanning solution for telehealth? — AEO, 63%
- Which mobile body scanning solution best improves patient engagement metrics? — AEO, 90%
- What body measurement tools minimize exposure of personal data during remote scans? — AEO, 11%. Коротка відповідь і посилання на trust-FAQ
- remote body measurement for telehealth

**Не для цієї сторінки** (кому належить)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| ai in telehealth | 100 · KD 53 | 20 | Хаб `the-potential-of-ai-in-telehealth` (поз. 21–33) |
| ai telehealth | 100 · KD 51 | 0 | Той самий хаб |
| patient engagement software | 1 300 · KD 2 | 150 · KD 27 | Стаття `mobile-body-scanning-patient-engagement` (канонічна тема engagement) |
| remote patient monitoring | 6 800 · KD 51 | 250 · KD 0 | 6,8K / KD 51, інтент — RPM-пристрої та платформи. Згадувати можна, цілитися не варто |
| remote patient monitoring software | 1 100 · KD 12 | 100 · KD 8 | Той самий інтент (RPM-платформи) |
| telehealth weight loss | 450 · KD 39 | 0 | Пацієнт шукає програму, нікому |
| virtual weight loss clinic | 350 · KD 39 | 20 | Пацієнт, нікому |
| telehealth bmi verification | — · KD 1 | — | Сторінка BMI verification і гайд аптек |

**Посилання з лендінгу на хаб:** `the-potential-of-ai-in-telehealth`, `mobile-body-scanning-patient-engagement`, `online-pharmacy-bmi-verification-…` (секція telehealth), `fitxpress-admin-panel-launch`, а також майбутня стаття «Telehealth Documentation» (жовтень).


---

## 4. Hub 3 GLP-1 → `/fitxpress/for-glp-1-programs/`

У Google немає жодного B2B-запиту з помітним попитом. Усе, що шукають про GLP-1, стосується або пацієнта (клініка поруч, трекер-застосунок), або медичного питання (втрата м'язів). Тому лендінг тримає позиції на GEO-фразах, де конкурентів майже немає. Трафік дасть стаття про втрату м'язів, і вона має вести сюди. Слово «tools» у title лендінгу не ставити: його тримає листикл «7 Body Composition & Progress-Tracking Tools for Remote GLP-1 Clinics».


**Головний ключ** (title, H1, перший абзац, meta)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| body composition tracking for GLP-1 programs | — | — | Попиту немає. Це головне питання ШІ-асистентам (див. нижче) |

**Вторинні** (H2, meta description, alt, анкори з хабу)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| weight loss clinic software | 10 | 10 | Мізерний обсяг, зате точний інтент покупця |
| medical weight loss software | 10 | 0 | Те саме |
| GLP-1 progress tracking | — | — | Ahrefs даних не має |
| lean mass tracking on GLP-1 | — | — | Мостик до статті про втрату м'язів |

**GEO-фрази і FAQ** (попит у Google нульовий, але саме так питають ШІ-асистенти і покупці)

- How can a GLP-1 weight-loss clinic track patient body composition remotely? Include tools. — AEO, 49%
- glp-1 weight-loss clinic remote body composition tracking tools — GSC: листикл top-7 стоїть на поз. 1
- what software supports glp workflows? — GSC, листикл, поз. 11

**Не для цієї сторінки** (кому належить)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| ozempic muscle loss | 1 100 · KD 53 | 200 · KD 54 | Нова стаття 3.x2 «GLP-1 and Muscle Loss» (у плані поки немає). Лендінг — у FAQ з посиланням |
| does ozempic cause muscle loss | 1 800 · KD 52 | 200 | Та сама стаття |
| glp 1 muscle loss | 400 · KD 11 | 30 | Та сама стаття, KD 11 |
| tirzepatide muscle loss | 500 · KD 37 | 150 | Та сама стаття |
| mounjaro muscle loss | 300 · KD 26 | 450 · KD 19 | Та сама стаття. UK KD 19: заходити через UK |
| glp-1 market | 150 · KD 43 | 10 | Хаб `glp-1-market` |
| glp-1 tracker app free | 300 | — | Кластер «glp 1 tracker app» ~1,7K сумарно по варіантах, але це споживчі застосунки (Shotsy). Нікому |
| glp-1 clinic | 250 · KD 2 | 0 | Локальний пацієнтський інтент |
| medical weight loss clinic | 1 700 · KD 5 | 150 · KD 45 | Локальний пацієнтський інтент |

**Посилання з лендінгу на хаб:** `glp-1-market`, `top-7-remote-body-composition-tools-glp-1-clinics`, `visual-progress-tracking-glp1-…`, `beyond-bmi-business`, `ai-body-scanners-vs-dexa-scans`, а також майбутня стаття «GLP-1 Patient Progress Record» (жовтень).


---

## 5. Hub 4 Insurance → `/fitxpress/for-insurance-underwriting/`

Драфт уже є (`workspace/pages/for-insurance-underwriting/`, 08-31), але URL там старий: `/for-insurance-underwriting/`, `parent: /`. Під нову ієрархію треба виправити. H1 драфту «…for accelerated life insurance underwriting» вже влучає в головний ключ. Guardrail хабу: лише підтримка андеррайтингу й BMI/build verification, без автоматичного андеррайтингу чи виявлення шахрайства.


**Головний ключ** (title, H1, перший абзац, meta)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| accelerated underwriting | 100 · KD 0 | 10 | KD 0. Разом із варіантами нижче ~340 на місяць |

**Вторинні** (H2, meta description, alt, анкори з хабу)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| accelerated underwriting life insurance | 90 · KD 1 | — |  |
| life insurance accelerated underwriting | 90 · KD 0 | — |  |
| life insurance underwriting software | 150 · KD 11 | — |  |
| insurance underwriting software | 450 · KD 11 | 200 · KD 9 | Інтент — core-системи (Guidewire). Лише згадка «works inside your underwriting workflow» |
| digital underwriting | 30 · KD 1 | 70 | UK вище, ніж US |
| paramedical exam | 350 · KD 3 | 0 | Тільки в контексті «менше paramed-візитів заради зросту й ваги». Не писати, що ми замінюємо paramed |

**GEO-фрази і FAQ** (попит у Google нульовий, але саме так питають ШІ-асистенти і покупці)

- what is accelerated underwriting — US 60, у FAQ
- remote height and weight verification for life insurance
- build and BMI evidence for underwriting — Формулювання з драфту

**Не для цієї сторінки** (кому належить)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| life insurance underwriting | 800 · KD 0 | 200 · KD 1 | Хаб `mobile-body-scanning-insurance-underwriting` |
| life insurance underwriting process | 350 · KD 4 | 40 | Той самий хаб |
| life insurance build chart | 100 · KD 0 | 0 | Рядок «BMI Verification for Life Insurance» (refresh секції хабу) |
| life insurance height and weight chart | 70 · KD 0 | 0 | Той самий рядок |
| bmi life insurance | 200 · KD 0 | 100 | Той самий рядок |
| life insurance fraud | 600 · KD 7 | 80 · KD 2 | Рядок «Self-Reported BMI vs Verified Body Data» (review/decide) |
| underwriting automation | 350 · KD 12 | 60 | Нікому: guardrail «no automated underwriting» |
| automated underwriting life insurance | 100 | 0 | Нікому, та сама причина |
| no medical exam life insurance | 3 000 · KD 13 | 300 · KD 6 | Споживчий продукт, нікому |

**Посилання з лендінгу на хаб:** `mobile-body-scanning-insurance-underwriting`, сторінка BMI verification, `wellness-rewards-verification-…`, `mobile-body-scanning-accuracy`, trust-FAQ.


---

## 6. Hub 5 Wellness → `/fitxpress/for-wellness-programs/`

**Кут — remote biometric screening (Вадим, 2026-09-29).** «Biometric screening» має 8 600 на місяць при KD 3, і в контент-плані цієї теми не було. Biometric screening у wellness-програмах роботодавців — це BMI, талія, тиск, кров. FitXpress закриває частину з вимірами тіла: талію міряє з двох фото, BMI рахує зі зросту й ваги (вагу звіряє Smart Scales, бета), склад тіла дає як оцінки. Тиск і аналізи крові не закриває, і сторінка каже це прямо. Лендінг бере комерційні модифікатори («at home», «remote», «companies», «onsite» як альтернатива). Головний інформаційний запит забирає нова стаття в Hub 5 (рядок F у списку для Ассель). Межі та заборони — правило 7 у `landing-map.md`: жодних заяв про комплаєнс з ADA, GINA, EEOC чи HIPAA щодо wellness-програм, жодної інтерпретації результатів.


**Головний ключ** (title, H1, перший абзац, meta)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| at home biometric screening | 80 | 0 | Прийнято 2026-09-29. Формула в title/H1: «remote biometric screening» + «body measurements» |

**Вторинні** (H2, meta description, alt, анкори з хабу)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| biometric screening companies | 90 · KD 3 | 0 |  |
| onsite biometric screening | 150 · KD 4 | 0 | Кут: віддалена альтернатива для частини з вимірами |
| company biometric screening | 100 · KD 3 | — |  |
| wellness rewards program | 200 · KD 1 | 0 | Кут rewards verification. Детально — стаття `wellness-rewards-verification-…` |
| corporate wellness platform | 500 · KD 15 | 60 | Інтент — платформа цілком. Формулювання: «for corporate wellness platforms» |
| employee wellness app | 200 · KD 1 | 60 |  |

**GEO-фрази і FAQ** (попит у Google нульовий, але саме так питають ШІ-асистенти і покупці)

- remote biometric screening — Ahrefs даних не має
- Best mobile body scanning software for fitness and wellness platforms? — AEO, 53%
- Which body scanning tools are suitable for health and wellness apps that need HIPAA or GDPR controls? — AEO, 78%. Відповідь без «HIPAA compliant»: лише формулювання з trust-FAQ
- full body scan for employees wellness program — GSC, стаття rewards, поз. 12,8

**Не для цієї сторінки** (кому належить)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| biometric screening | 8 600 · KD 3 | 150 · KD 7 | 8,6K / KD 3. Нова стаття в Hub 5 (рядок F для Ассель) |
| what is a biometric screening | 2 500 · KD 3 | — | Та сама стаття |
| corporate wellness programs | 2 600 · KD 0 | 500 · KD 4 | Хаб `ai-body-data-wellness-platforms` |
| wellness incentives | 700 · KD 0 | 150 · KD 0 | Стаття `wellness-rewards-verification-…` |
| nutrition coaching software | 100 · KD 0 | 150 | Рядок P1 «Body Data for Nutrition and Lifestyle Coaching Platforms» |
| wellness app | 1 000 · KD 2 | 100 · KD 18 | Споживач, нікому |

**Посилання з лендінгу на хаб:** `ai-body-data-wellness-platforms`, `wellness-rewards-verification-employers-insurers-…`, `mobile-body-scanning-patient-engagement`, `beyond-bmi-business`, а також P0-листикл «Top Mobile Body Scanning Software for Wellness Apps» (жовтень; «best/top» лишити йому).


---

## 7. Hub 6 Bariatrics → `/fitxpress/for-bariatric-clinics/`

Весь попит у Google — пацієнтський («яким має бути BMI для операції»), це YMYL і не наші покупці. Для клінік попиту немає, зате ШІ-асистенти ставлять саме наші питання, і в двох із трьох у нас видимість 0–6%. HubSpot AEO окремо рекомендує з високим пріоритетом сторінку «FitXpress for Bariatric Pre-Auth Measurements». Отже, лендінг будуємо під pre-auth.


**Головний ключ** (title, H1, перший абзац, meta)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| bariatric pre-authorization documentation | — | — | Попиту немає. Головний сценарій (HubSpot AEO, HIGH) |

**Вторинні** (H2, meta description, alt, анкори з хабу)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| bariatric software | 30 | 0 | GSC: хаб на поз. 19,7 |
| bariatric clinic software body measurement records | — | — | GSC: хаб на поз. 3,6 |
| bariatric program | 150 · KD 30 | — | Тільки як згадка «for bariatric programs»: інтент запиту локальний |
| bariatric surgery insurance requirements | 10 | — | Кут «документація для payer» |

**GEO-фрази і FAQ** (попит у Google нульовий, але саме так питають ШІ-асистенти і покупці)

- How can a weight-loss surgery program reduce manual measurement work during pre-auth? — AEO, **0%**
- Which tools can support remote body data collection before bariatric surgery consultations? — AEO, **6%**
- What software helps bariatric clinics collect auditable body measurement records for payer documentation? — AEO, 62%

**Не для цієї сторінки** (кому належить)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| bariatric surgery requirements | 1 100 · KD 59 | — | Пацієнт, YMYL. Щонайбільше секція в хабі |
| bmi for bariatric surgery | 450 · KD 53 | — | Пацієнт, YMYL |
| weight loss surgery requirements | 600 · KD 0 | — | Пацієнт |
| gastric sleeve requirements | 400 · KD 0 | — | Пацієнт |
| bariatric pre-qualification | — | — | Title хабу (`bariatric-pre-qualification-…`), лендінг лише посилається |
| bariatric app | 200 · KD 11 | — | Застосунок для пацієнтів (Baritastic), нікому |

**Посилання з лендінгу на хаб:** `bariatric-pre-qualification-mobile-3d-body-scanning`, `glp-1-market`, сторінка BMI verification, `fitxpress-admin-panel-launch`, а також майбутні статті «Pre-Authorization Documentation» і «Patient Progress Record» (P1).


---

## 8. Hub 7 Clinical trials → `/fitxpress/for-clinical-trials/`

FitXpress тут не DCT-платформа, а модуль вимірювань усередині неї, тому ключі типу «DCT platform» ідуть із формулюванням «for DCT platforms». Інформаційні запити («decentralized clinical trials», «anthropometric measurements») лишаються хабу. Хаб в індексі, але за 3 місяці мав 1 показ.

**Конфлікт title:** SEO-title хабу — «Clinical Trial Anthropometric Measurement Software | 3DLOOK», тобто продуктовий, і він збігається з головним ключем лендінгу. Як і з occ-health, разом із запуском лендінгу title хабу змінити на процесний, наприклад «Standardizing Anthropometric Measurements in Obesity Trials».


**Головний ключ** (title, H1, перший абзац, meta)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| remote anthropometric measurement for clinical trials | — | — | Попиту немає. Головна фраза для title/H1 разом із «decentralized and hybrid trials» |

**Вторинні** (H2, meta description, alt, анкори з хабу)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| decentralized clinical trial platform | 100 · KD 10 | — | CPC $12: дорогий комерційний запит |
| decentralized clinical trials platform | 100 · KD 8 | — |  |
| dct platform | 70 · KD 2 | — |  |
| decentralized clinical trials technology | 70 | — |  |
| decentralized clinical trials software | 70 · KD 12 | — |  |
| remote patient monitoring clinical trials | 90 · KD 14 | — |  |
| clinical trial technology | 200 · KD 1 | — |  |

**GEO-фрази і FAQ** (попит у Google нульовий, але саме так питають ШІ-асистенти і покупці)

- body measurements in obesity trials between site visits
- anthropometric measurement software — Після зміни title хабу — лендінгу

**Не для цієї сторінки** (кому належить)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| anthropometric measurements | 2 100 · KD 6 | — | 2,1K / KD 6, академічний інтент. Хаб (`clinical-trial-anthropometric-…`) |
| decentralized clinical trials | 500 · KD 12 | — | Хаб |
| hybrid clinical trials | 200 · KD 1 | — | Хаб, секція про hybrid |
| benefits of decentralized clinical trials | 200 · KD 6 | — | Хаб |
| obesity clinical trials | 150 · KD 11 | — | Пацієнти шукають дослідження, нікому |
| ecoa | 5 700 · KD 52 | — | Інша категорія продуктів, нікому |
| waist circumference measurement | 450 · KD 47 | — | Hub 9 |

**Посилання з лендінгу на хаб:** `clinical-trial-anthropometric-measurement-software-obesity-trials`, `mobile-body-scanning-accuracy`, trust-FAQ, а також майбутні статті «What CROs Should Ask» і «DCT Platform Integration» (P1).


---

## 9. Hub 8 Occupational health → `/fitxpress/for-occupational-health/`

Найсильніший комерційний ключ серед усіх вертикалей: «occupational health software» (US 350 / KD 3 / $15, UK 200 / KD 0). Шукають його OH-провайдери, тобто наші покупці, хоча продуктова категорія збігається частково: FitXpress — модуль intake, а не повна OH-система. Формулювання: «adds remote body measurement intake to your occupational health software».

**Ризик канібалізації:** slug хабу — `occupational-health-screening-software`. Хаб лишається на процесі («screening», «pre-employment»), лендінг забирає «software»-запити. Зараз SEO-title хабу — «Occupational Health Screening Software | 3DLOOK» (H1 без «software»). **Разом із запуском лендінгу title хабу змінити на процесний**, наприклад «Occupational Health Screening: Faster Intake and Documentation», а з хабу на лендінг поставити анкор «occupational health screening software».


**Головний ключ** (title, H1, перший абзац, meta)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| occupational health software | 350 · KD 3 | 200 · KD 0 |  |

**Вторинні** (H2, meta description, alt, анкори з хабу)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| occupational health management software | 150 · KD 1 | 200 |  |
| occupational medicine software | 150 · KD 0 | 30 |  |
| employee health screening software | 40 | 10 | GSC: хаб на поз. 25 |
| employee health screening | 250 · KD 1 | 400 · KD 0 | UK 400 / KD 0 |
| pre placement health assessment | 30 | 50 | UK-термін |

**GEO-фрази і FAQ** (попит у Google нульовий, але саме так питають ШІ-асистенти і покупці)

- pre employment medical software — GSC: хаб на поз. 18
- what are the best tools for occupational health screening without wearables — GSC: хаб на поз. 1,2 (запити в стилі ШІ)
- what technology is used for pre-employment health screening in 2026 — GSC: поз. 1,0
- can occupational health screening be done remotely? — GSC: поз. 6,2. У FAQ

**Не для цієї сторінки** (кому належить)

| Ключ | US | UK | Примітка |
|---|---|---|---|
| occupational health screening | 250 · KD 6 | 200 · KD 2 | Хаб (зараз поз. 51) |
| pre employment health screening | 150 · KD 5 | 200 · KD 0 | Хаб і секція pre-employment |
| return to work assessment | 80 · KD 0 | 150 | Рядки про return-to-work (P1) |
| workers compensation return to work | 150 · KD 0 | 0 | Рядок про workers' comp (P1) |
| fitness for duty evaluation | 350 · KD 0 | 0 | Лише рядок «Fit-for-Duty Intake» (ASK). Guardrail: жодних рішень про допуск |
| occupational health assessment | 300 · KD 1 | 3 700 · KD 9 | UK 3,7K, але шукають працівники. Нікому |
| dot physical | 34 000 · KD 0 | 50 · KD 14 | 34K, огляд водіїв, нікому |

**Посилання з лендінгу на хаб:** `occupational-health-screening-software`, `manual-vs-digital-intake-occupational-health-screening`, trust-FAQ, а також майбутні статті «Return-to-Work Documentation» і «Workforce Screening Vendors» (P1).


---
## Що потребує рішення

1. ~~**Wellness і biometric screening.**~~ **Вирішено 2026-09-29: беремо.** Лендінг бере «remote / at home biometric screening», а Ассель заводить у Hub 5 статтю (рядок F у `2026-09-27-content-plan-rows-for-assel.md`).
2. **Occupational health software.** Беремо цей ключ, хоча FitXpress — модуль intake, а не повна OH-система? Шукають його наші покупці (OH-провайдери), але у видачі будуть OH-EHR. Я б брав, формулюючи «adds remote intake to your occupational health software».
3. **Slug-и.** Усі URL у таблиці — пропозиції під ієрархію `/fitxpress/for-{vertical}/`. Для сторінки фічі пропоную `/fitxpress/bmi-verification/` (не `for-`). У драфті страхування URL ще старий: `/for-insurance-underwriting/`.
4. **Нові рядки контент-плану.** Крім biometric screening, це стаття про втрату м'язів на GLP-1 (рядок 3.x2 уже є у списку для Ассель від 09-27). Вона забирає кластер ~5K у US (ozempic, tirzepatide, mounjaro muscle loss) і веде на GLP-1-лендінг.
5. **Два хаби зі «software»-title.** Це `occupational-health-screening-software` («Occupational Health Screening Software») і `clinical-trial-anthropometric-…` («Clinical Trial Anthropometric Measurement Software»). Їхні title збігаються з головними ключами лендінгів. У день запуску лендінгу title хабу треба змінити на процесний, slug лишити (301 не потрібен). Решта хабів конфліктів не мають, звірено з живими title 09-29.

## Дані

- Ahrefs: 44 запити overview і matching-terms, ~34K юнітів (сумарно 117K з 800K, лічильник скидається 09-30). Сирі JSON лежать у scratchpad сесії, у репо їх немає.
- GSC: page × query по 25 хабах і лендінгах, 2026-06-27…09-26, 981 рядок. Гайд для аптек і хаб clinical trials за цей період мали 3 і 1 показ, хоча обидва в індексі (URL Inspection 09-29, PASS). Отже, проблема не технічна: під їхні формулювання в Google просто немає попиту.
- HubSpot AEO: 24 промпти, лише два ICP (Telehealth & Weight-Loss, Connected Fitness). Для страхування, occ-health і trials промптів немає, тому GEO-фрази там узяті з GSC і гайдів хабів.
