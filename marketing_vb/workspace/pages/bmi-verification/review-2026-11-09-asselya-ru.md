---
product: fitxpress
type: feature-page
vertical: bmi-verification
status: review
for: Asselya
draft: 3dlook-bmi-verification-mockup-v3.html (Slack F0CBA73R1K3, 2026-10-22)
---

# BMI verification: разбор драфта v3 (09.11)

**Роль страницы (Вадим, 09.11).** Это страница функции. Она объясняет, как работает BMI verification, ведёт на
use-case лендинги, которые продают, и держит ключи. Поэтому её проверяем не правилами продающего лендинга, а тремя
вопросами: понятно ли она объясняет функцию и точны ли claims, ведёт ли на лендинги, держит ли ключи.

Проверено: claims по `proof-points` / `compliance` / `tech-spec`, Search Console за 16 месяцев, Ahrefs (US, UK),
сравнение с живой `/for-bmi-verification/`, детектор, слепой судья.

## Коротко

1. **Основа правильная для такой страницы.** Она объясняет, а не обещает: честные границы («FitXpress is not a
   medical device», рост вводится, а не меряется, расхождение не равно фроду), live capture без camera roll, пример с
   порогом (арифметика верна в kg и lb), таблица методов, ~1 450 слов. Из живой страницы ушли «eliminates manual
   reviews», «exceeds GPhC requirements», «clinical-grade», и это правильно.
2. **Главного не хватает: переходов на лендинги.** В блоке «One feature · Multiple workflows» четыре карточки и ни
   одной ссылки, а это основная работа страницы (раздел 1).
3. **Ключи (раздел 2).** Страница держит «bmi verification» (позиция ~6), а с августа и бренд «fitxpress»: другой
   страницы под него на сайте нет. Нужны FitXpress в H1, прямой ответ на «What is BMI verification?» и ключ в
   заголовке таблицы методов.
4. **Claims (раздел 3).** Burlington Medical (клиент Mobile Tailor) в ряду «using FitXpress», а UK Meds нет. RTPV,
   Clothing Detector и liveness описаны сильнее, чем подтвердил продукт. На странице про вес нет цифры точности веса.
5. **Слепой судья: 39/100**, но по шкале продающего лендинга. Оси sales и conversion к этой странице не относятся.
   Hard fail по логотипам и слабые claims остаются в силе (раздел 6).

## 1. Переходы на use-case лендинги

Каждая карточка: одна фраза о том, что BMI verification даёт в этой вертикали, и ссылка. Анкор — ключ лендинга из
карты лендингов (для страхования «accelerated underwriting»). Во втором экране героя кнопка «See it in your use
case ↓» ведёт к карточкам. Форма демо внизу остаётся.

| Карточка | Куда ведёт сейчас | Когда выйдет лендинг |
|---|---|---|
| Online pharmacies | статья [Online pharmacy BMI verification: a 2026 compliance guide](https://3dlook.ai/content-hub/online-pharmacy-bmi-verification-a-2026-compliance-guide/) | отдельный лендинг для аптек (UK, GPhC), решение Вадима 09.11. Адрес `/for-online-pharmacies/`, потом `/fitxpress/for-online-pharmacies/`. Эта страница аптекам не продаёт, она ведёт на лендинг |
| Digital health programs (сюда же weight-loss и GLP-1) | [/structured-body-data-for-telehealth-digital-health-programs/](https://3dlook.ai/structured-body-data-for-telehealth-digital-health-programs/) | `/fitxpress/for-telehealth/`; для GLP-1 добавить ссылку на `/fitxpress/for-glp-1-programs/`, когда выйдет |
| Life insurance underwriting | [/for-insurance-underwriting/](https://3dlook.ai/for-insurance-underwriting/), лендинг живой | `/fitxpress/for-insurance-underwriting/` (301) |
| Employer and insurer wellness | хаб [AI Body Data for Wellness Platforms](https://3dlook.ai/content-hub/ai-body-data-wellness-platforms/) | `/fitxpress/for-wellness-programs/` |
| Bariatric programs (новая карточка, по желанию) | статья [bariatric pre-qualification](https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/): она уже на 1-й позиции по «mobile body scanning software remote bmi verification» | `/fitxpress/for-bariatric-programs/` |

Обратные ссылки уже есть: статья для аптек, статья по бариатрии и insurance-лендинг ведут на
`/for-bmi-verification/` (по 2 ссылки).

## 2. Какие ключи держит страница

Search Console, 16 месяцев: 101 клик, 4 398 показов, средняя позиция 7.4. Подробности в приложенном `keywords-2026-11-09.md` (EN).

| Запрос | Клики | Показы | Позиция (16 мес) | Последние 90 дней |
|---|---|---|---|---|
| fitxpress | 31 | 839 | 7.4 | 10 кликов, 243 показа, позиция 6.1 |
| bmi verification | 1 | 555 | 9.6 | 115 показов, позиция 6.4 |
| what is bmi verification | 0 | 103 | 7.8 | 2 показа, позиция 1.0 |
| fit xpress / 3dlook fitxpress | 3 | 110 | 3-12 | — |

**Бренд переехал на эту страницу.** До марта 2026 запрос «fitxpress» держала `/fitxpress/` (20-56 кликов в месяц),
потом она ушла 301 на главную. До июля его держала `/fitxpress/for-telehealth-and-weight-loss/`, теперь это 301 на
telehealth-страницу. С августа Google показывает по «fitxpress» только BMI-страницу: 3-6 кликов в месяц вместо
20-56. Пока `/fitxpress/` нет, на этой странице FitXpress должен стоять в title и в H1.

**Ahrefs.** Спрос маленький, и это нормально для B2B. «bmi verification» в US — 100 в месяц, но половина из них —
лос-анджелесские разрешения на строительство (LADBS), не наше. «what is bmi verification» — 20,
«telehealth bmi verification methods» — 20. В UK люди ищут «voy bmi verification call» (20): британские онлайн-клиники
сейчас проверяют BMI видеозвонком. «bmi check» (5 600 в UK) — калькуляторы NHS, «weight verification» — логистика:
за ними не идём.

Что сделать:

1. **H1 с FitXpress и ключом.** Варианты: «FitXpress BMI verification: cross-check self-reported weight from two
   guided photos» или «Remote BMI verification with FitXpress: predicted weight from two guided photos». Title твой
   («Remote BMI Verification & Smart Scales | FitXpress by 3DLOOK», 60 знаков) подходит.
2. **Прямой ответ на «What is BMI verification?»** — H2 сразу после героя или первая FAQ дословно этим вопросом
   (сейчас «What does “BMI verification” mean here?»). Определение в первом предложении, например: «BMI verification
   checks a self-reported weight against a second source before BMI is used in a decision.» Второе предложение — что
   этим вторым источником даёт FitXpress.
3. **Таблица методов: H2 «BMI verification methods compared»** (сейчас «How the methods compare») и строка «Video
   consultation»: клиницист видит человека на видео, вес всё равно сообщает сам человек или показывает домашние весы.
   Формулировку сверить с руководством GPhC.
4. Ключ «BMI verification» держать в первых 100 словах и в URL (так и есть).

## 3. Что обязательно исправить (claims)

| # | Сейчас | Проблема | Как надо |
|---|---|---|---|
| 1 | Логотипы Burlington Medical, Verv, MagicFit, Healthyr, Coredirection под «Selected companies using FitXpress» | Burlington Medical — клиент Mobile Tailor (фартуки), не FitXpress. Нет UK Meds — единственного клиента, у которого именно BMI verification. Подпись «Logos do not imply adoption…» оправдывается | Общий ряд всех клиентов, как на use-case страницах (Вадим 06.11: «однакова стрічка у всіх юз кейсах»), **UK Meds и Yazen первыми**. Подпись: «100+ clients have used 3DLOOK body scanning since 2016, including online pharmacies.» Заголовок «companies using FitXpress» убрать |
| 2 | «RTPV checks positioning before capture can continue», «RTPV requires alignment checks», чип «✓ Pose requirements met» в мок-апе | Уровень «не даёт продолжить съёмку» продукт не подтвердил. С 07.10 на новых страницах безопасная формулировка | «Real-Time Pose Validation (RTPV) gives pose and framing guidance during capture.» Чип из мок-апа убрать |
| 3 | «Clothing-related flags support review; the Clothing Detector does not automatically request a clothing change or rescan» | Открытый вопрос к продукту. Утверждённая публичная формулировка говорит обратное («can prompt corrective action») | До ответа продукта: «The Clothing Detector identifies clothing conditions that may interfere with capture.» Без утверждения про пересъёмку в любую сторону |
| 4 | Карточка «Prompted-action liveness, Coming soon» | В `tech-spec` нет, даты релиза нет. Это обещание функции на публичной странице | Убрать до подтверждения продукта. Если продукт назовёт срок, вернуть одной строкой |
| 5 | Ни одной цифры точности веса: «Assess Smart Scales against your required reference method…» | Первый вопрос к странице про вес — насколько он точен. Утверждённая цифра есть | «Smart Scales estimates weight with approximately 3.5% mean absolute error under evaluated conditions», ссылка на accuracy framework. Рядом с примером объяснить связь: порог ставится выше ошибки модели (пример 5% как раз выше 3.5%) |
| 6 | «Results within 45 seconds¹» | Публичная формулировка одна | «Under 45 seconds from the photos to structured results» (в полосе фактов «Under 45 sec») |
| 7 | Data handling: «Confirm retention, hosting, access… during procurement», «Responsibilities under HIPAA and GDPR depend on the parties’ roles» | Расплывчато там, где есть утверждённые строки | Пять строк данных, как на фитнес-странице: Photos (удаляются сразу после обработки или до 30 дней, лицо скрывается при съёмке) · Identifiers · GDPR (каноническая фраза) или HIPAA/BAA · Encryption · Model training. Затем ссылка на trust FAQ и privacy@3dlook.me |

## 4. Как страница объясняет функцию

1. **Зачем проверять самоотчёт.** Сейчас «Remote intake often relies on a person’s reported weight…» без цифры. Одна
   цифра из уже проверенной статьи для аптек: CDC, *Preventing Chronic Disease* — по самоотчёту доля тяжёлого
   ожирения занижена на 40% (5.3% против 8.8%, данные 2020).
2. **Повторы оговорок.** «Eligibility, prescribing and underwriting remain with…» стоит в герое, в блоке проблемы, в
   FAQ и над формой. Оставить в FAQ «Does FitXpress approve eligibility?» и «FitXpress is not a medical device» у
   формы. «A mismatch does not establish fraud» и «No single check establishes identity» — по одному разу. Слово
   «review» на странице 35 раз.
3. **Регистр.** «you / your» ~26 на 1 000 слов при бюджете 12.5. «Your team» в объясняющих фразах заменить на
   актора: the pharmacy, the care team, the carrier, the program. «Your» оставить для порога, систем и CTA.
4. **FAQ.** Семь вопросов для страницы функции нормально. «Can users upload saved photos?» повторяет блок live
   capture: убрать или сократить. «Can we use the scan for progress tracking too?» дать со ссылкой на
   фитнес-лендинг.
5. **Пилот и цена.** Пилот и тарифы продают лендинги. Здесь блок пилота можно сжать до строки и кнопки демо, по
   цене — одна строка со ссылкой на `/pricing/`.
6. Детектор `--channel page`: жёстких банов нет, AI-плотность 0.

## 5. Техническое (для дизайна и WordPress)

- Адрес: страница пересобирается на месте, `/for-bmi-verification/`. Когда выйдет `/fitxpress/`, переезд на
  `/fitxpress/bmi-verification/` с 301, как у insurance.
- Форма: общая HubSpot `FX | LP | Demo` с якорем `#demo`, вертикаль через `fx_vertical`. Поле «Use case» в макете не
  нужно.
- Yoast title 60 / description 154: в лимите.
- Schema: Service + FAQPage + BreadcrumbList (на живой сейчас только WebPage и BreadcrumbList).
- `noindex` в макете — только для макета.

## 6. Слепой судья

**39 / 100** по шкале use-case лендинга (порог 85). `judge-round-1-asselya-v3.json`.

| Ось | Балл | Из |
|---|---|---|
| Proof of belonging | 5 | 15 |
| Claims discipline | 4 | 15 |
| Sales argument | 5 | 15 |
| Uniqueness against the parent | 6 | 10 |
| Conversion | 4 | 10 |
| Copy in the buyer's language | 4 | 10 |
| Human copy | 5 | 10 |
| Search and AI visibility | 4 | 10 |
| Place in the site and technical layer | 2 | 5 |

- Sales argument и Conversion судья мерил как у продающего лендинга. У этой страницы другая работа, так что общий
  балл занижен.
- В силе: **hard fail** по ряду логотипов (раздел 3, п. 1) и **claims discipline 4/15** (раздел 3, пп. 2-5).
- После правок — новый судья по критериям страницы функции: объясняет ли функцию, точны ли claims, ведёт ли на
  лендинги, держит ли ключи.
