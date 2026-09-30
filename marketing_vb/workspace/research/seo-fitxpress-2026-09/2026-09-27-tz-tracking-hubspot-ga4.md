---
product: fitxpress
type: tech-spec
date: 2026-09-27
owner: Вадим или подрядчик (админ HubSpot, доступ к GTM и GA4)
related: 2026-09-25-fitxpress-seo-plan.md (фаза 0, п. 0.2–0.6); 2026-09-29-landing-keywords.md
updated: 2026-09-29 — одна форма на все FX-лендинги, `fx_vertical`, `article_cta_click` (решение Вадима)
---

# ТЗ: трекинг лидов (GA4, GTM, HubSpot, Clarity)

## Зачем

Сейчас нельзя ответить на главный вопрос плана: «сколько FitXpress-сделок принесла органика и с каких страниц».

| Система | Что не так |
|---|---|
| **GA4** | Ключевое событие одно (форма на `/contact-us/`). Ещё 298 отправок форм и 259 кликов demo не учитываются; `form_name` приходит пустым. Внутренний трафик и боты не отфильтрованы. |
| **HubSpot** | `utm_*` не заполнен ни у одного контакта, `industry` пуст на 100%. Нет поля ICP-сегмента. У сделок нет источника трафика. Среди форм смешаны карьерные формы, логины приложения Mobile Tailor и consumer-заявки из popup (90% личные email). |
| **Clarity** | 63% сессий — боты. Внутренний трафик не исключён. |

**Что уже стоит на сайте (проверено 2026-09-27):** GTM `GTM-PW77M7K` на всех страницах и формы HubSpot, встроенные через `js.hsforms.net`. GA4 и Clarity, судя по всему, грузятся через GTM.

**Оценка:** 2–4 рабочих дня. Порядок блоков ниже — порядок работы.

### Что поменялось 2026-09-30

**В общую форму `FX | LP | Demo` добавляется необязательное поле «Expected monthly scan volume»** (решение Вадима). Идея пришла из драфта insurance-лендинга Ники, где это было отдельное поле одной страницы. Объём квалифицирует лид в любой вертикали, поэтому поле живёт в общей форме, а не на странице (B1). Необязательное, чтобы не резать конверсию.

### Что поменялось 2026-09-29

Статьи дают трафик и ведут на лендинг своей вертикали, лендинг конвертирует. Под это ТЗ поменялось в трёх местах:

1. **Одна форма `FX | LP | Demo` на всех FitXpress-лендингах** (`/fitxpress/`, все `/fitxpress/for-*/`, страница BMI verification) вместо отдельной формы на каждый. Какой лендинг конвертировал, видно по URL отправки и по полю `fx_vertical`. Десять форм — это десять копий consent, блокировки gmail, scoring, workflows и строк в GTM, которые рано или поздно разъедутся (A1, B1, B5).
2. **Поле `fx_vertical`** на контакте и сделке. Его заполняет GTM по пути страницы (B1, B2, B3).
3. **Событие `article_cta_click`**: переход из статьи на лендинг. Без него не видно, работает ли связка «статья → лендинг» (A2).

---

## Блок A. GA4 и GTM (1–1,5 дня)

### A1. Событие отправки каждой HubSpot-формы

1. В GTM создать тег Custom HTML на All Pages. Он слушает события отправки HubSpot-форм и отправляет в `dataLayer` `{event: 'hs_form_submit', form_id: <GUID формы>}`. Какое событие слушать, зависит от версии встраивания:
   - **Legacy-встраивание** (`hbspt.forms.create`, сейчас на сайте используется `js.hsforms.net`): `message`-событие, где `event.data.type === 'hsFormCallback' && event.data.eventName === 'onFormSubmitted'`. `id` формы — в `event.data.id`.
   - **Новые формы (v4):** window-событие `hs-form-event:on-submission:success`.
   
   Слушать оба варианта. Проверить в DebugView на каждой форме.
2. В GTM завести Lookup-таблицу `form_id → form_name` по списку ниже. Реальные ID взять в HubSpot → Marketing → Forms.
3. GA4-тег события `generate_lead` с параметрами `form_id`, `form_name`, `page_location`, `fx_vertical` (переменная из B2.5).
4. В GA4 → Admin → Custom definitions зарегистрировать `form_name`, `form_id` и `fx_vertical` как event-scoped dimensions.
5. В GA4 → Admin → Key events отметить `generate_lead` ключевым событием. Старое событие для `/contact-us/` оставить, чтобы не рвать историю, но отчитываться по `generate_lead`.

**Названия форм** (выровнять с HubSpot, см. блок B5):

| Форма в HubSpot | form_name |
|---|---|
| Contact us & Partnership form | `contact_us` |
| FX Starter | `fx_pricing_starter` |
| FX Pricing - Talk to sales | `fx_pricing_talk_to_sales` |
| Contact Us - Pricing page (Entreprise plan) | `pricing_enterprise` |
| Homepage Popup | `home_popup` |
| **FX \| LP \| Demo** (новая, одна на все FX-лендинги) | `fx_lp_demo` |
| Telehealth & Weight Loss (former Health & Fitness LP) | `fx_lp_telehealth` (оставить до переезда страницы, потом снять) |
| Connected & Digital Fitness (former Health & Fitness LP) | `fx_lp_fitness` (оставить до переезда страницы, потом снять) |
| Downloadable content (The Next Big Leap in Health) | `ebook_health` |
| … (The Digital Health Revolution) 2025 | `ebook_glp1` |
| Career forms | `careers`. **Не** ключевое событие |

### A2. Клики и бронирование встреч

- **`demo_click`:** клик по любой кнопке и ссылке «Book a demo», «Request a demo», «Talk to sales». Параметры `cta_text` и `page_location`. Сейчас эти кнопки работают на JS. После того как девелопер сделает их обычными `<a href>` (фаза 0, п. 0.1), триггер — Click URL или Click Text.
- **`meeting_booked`:** HubSpot Meetings присылает `postMessage` с `meetingBookSucceeded`. Тот же приём, что в A1; это тоже ключевое событие.
- **`docs_click`:** исходящий клик на `docs.fitxpress.3dlook.me`.
- **`pricing_plan_click`:** клик по плану на `/pricing/` с параметром `plan`.
- **`article_cta_click`:** клик на странице `/content-hub/*` по ссылке, ведущей на FitXpress-лендинг (путь начинается с `/fitxpress/`), включая кнопку «Book a demo» со ссылкой на `#demo` лендинга. Параметры:
  - `from_page`: путь статьи;
  - `to_page`: путь ссылки без домена, вместе с `#demo`, если он есть;
  - `cta_depth`: на какой глубине страницы стоит ссылка, в процентах с округлением до 10. Custom JS variable: `Math.round(({{Click Element}}.getBoundingClientRect().top + window.scrollY) / document.documentElement.scrollHeight * 10) * 10`. По ней видно, работает ли блок выше 30% (правило SEO-плана), и статьи для этого править не нужно.
  
  **Не** ключевое событие. Зарегистрировать `from_page`, `to_page`, `cta_depth` как event-scoped dimensions.

### A3. Фильтры

1. **Внутренний трафик.** GA4 → Admin → Data streams → Configure tag settings → Define internal traffic: IP офиса и VPN, IP подрядчиков. Затем Admin → Data filters → Internal traffic → **Active**. Сначала неделю в режиме Testing, потом Active.
2. **wp-admin и staging.** В GTM не стрелять GA4-тегами, если hostname не `3dlook.ai` или путь начинается с `/wp-admin`. Та же исключающая логика для Clarity.
3. **Боты в Direct.** Отфильтровать в GA4 полностью нельзя, поэтому:
   - сохранённый сегмент или comparison «Direct без ботов»: исключить страну Singapore/China при длительности сессии < 10 с;
   - в отчётах смотреть engaged sessions, а не sessions.
4. **Unwanted referrals:** `3dlook.me`, `hsforms.com`, `hubspot.com`, `docs.fitxpress.3dlook.me` (если там отдельный поток).

### A4. Связки

- GA4 ↔ Search Console: Admin → Product links.
- Clarity ↔ GA4: Clarity → Settings → Setup → Google Analytics integration.
- **Clarity:** Settings → IP blocking (те же IP, что в A3.1). Проверить, что Bot detection включён.

### Приёмка блока A

- Тестовая отправка каждой формы из списка A1 видна в GA4 DebugView как `generate_lead` с правильным `form_name`.
- Клик «Book a demo» даёт `demo_click`, тестовое бронирование встречи даёт `meeting_booked`.
- Клик из статьи на FX-лендинг даёт `article_cta_click` с заполненными `from_page`, `to_page` и `cta_depth`.
- Визит с офисного IP не попадает в Realtime после активации фильтра.

---

## Блок B. HubSpot (1–2 дня)

### B1. Новые свойства

| Объект | Свойство | Тип | Значения | Кто заполняет |
|---|---|---|---|---|
| Contact | `icp_segment` | Dropdown | FX: Telehealth & GLP-1 · Online pharmacy · Life & disability insurance · Health plans & employer wellness · Bariatric & metabolic · Occupational health · CROs & clinical trials · Connected & digital fitness · Plastic surgery · BCRL / oncology RPM. MT: MTM brands & tailors · On-demand manufacturers · Uniforms · Wrist / limb. Прочее: Consumer · Agency / vendor · Job seeker · Other | Поле формы (если есть) или sales при квалификации |
| Deal | `icp_segment` | Dropdown | те же значения | Workflow копирует из контакта; sales правит |
| Contact | `fx_vertical` | Dropdown | `fitxpress_parent` · `bmi_verification` · `fitness` · `telehealth` · `glp1` · `insurance` · `wellness` · `bariatric` · `clinical_trials` · `occupational_health` | Скрытое поле формы `FX \| LP \| Demo`, значение ставит GTM (B2.5). **Это страница конверсии, а не сегмент:** на wellness-лендинг может прийти страховщик, поэтому `icp_segment` остаётся за sales, и workflow из `fx_vertical` его **не** заполняет |
| Contact | `expected_scan_volume` | Dropdown | `under_500` · `500_1000` · `1000_5000` · `over_5000` · `not_sure` (подписи в форме: Under 500 · 500–1,000 · 1,000–5,000 · Over 5,000 · Not sure yet; границы совпадают с тарифами на `/pricing/`) | **Необязательное** видимое поле формы `FX \| LP \| Demo`, подпись «Expected monthly scan volume» (Вадим, 2026-09-30) |
| Deal | `fx_vertical` | Dropdown | те же значения | Workflow (B3) |
| Deal | `original_traffic_source` | Dropdown | как `hs_analytics_source` у контакта | Workflow (B3) |
| Deal | `first_page_seen` | Single-line text | URL | Workflow (B3) |
| Deal | `first_conversion_form` | Single-line text | название формы | Workflow (B3) |

**Отдельное поле «product» не создавать.** У сделок продукт уже задаётся pipeline (`Health & Fitness` = FitXpress) и `product_to_sell`. У контактов уже есть поле «The solution I'm interested in» (заполнено 13 раз), его и использовать в формах.

### B2. UTM и страница входа в каждой форме

1. Во все маркетинговые формы добавить скрытые поля: `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`. Свойства в HubSpot уже существуют, но пустые.
2. Заполнение: HubSpot сам подставляет скрытые поля из query string, но только на странице первого входа. Поэтому GTM-скрипт при входе сохраняет UTM в cookie `first_utm` на 90 дней и подставляет значения в скрытые поля формы на любой странице (`onFormReady`).
3. Поле `landing_page` (скрытое) — первая страница визита из того же cookie.
4. **Наша сторона:** все ссылки на сайт в соцпостах, аутбаунде и email получают UTM по схеме `utm_source={linkedin|twitter|facebook|instagram|closely|email}&utm_medium={social|outbound|email}&utm_campaign={slug статьи или кампании}`. Это правка в наших пайплайнах: `post-lint` и `message-sequencer`. Её делаю я.
5. **`fx_vertical`.** GTM-переменная Lookup Table по Page Path:

   | Page Path | fx_vertical |
   |---|---|
   | `/fitxpress/` | `fitxpress_parent` |
   | `/fitxpress/bmi-verification/` и старый `/for-bmi-verification/` | `bmi_verification` |
   | `/fitxpress/for-connected-and-digital-fitness/` | `fitness` |
   | `/fitxpress/for-telehealth/` и старый `/structured-body-data-for-telehealth-digital-health-programs/` | `telehealth` |
   | `/fitxpress/for-glp-1-programs/` | `glp1` |
   | `/fitxpress/for-insurance-underwriting/` | `insurance` |
   | `/fitxpress/for-wellness-programs/` | `wellness` |
   | `/fitxpress/for-bariatric-clinics/` | `bariatric` |
   | `/fitxpress/for-clinical-trials/` | `clinical_trials` |
   | `/fitxpress/for-occupational-health/` | `occupational_health` |

   Тот же GTM-скрипт, что подставляет UTM (п. 2), в `onFormReady` пишет это значение в скрытое поле `fx_vertical`. Новый лендинг = одна новая строка в таблице. Отдельная форма для него не нужна. Slug-и новых страниц пока предварительные: при публикации сверить таблицу с финальным URL (это пункт в handoff `page-builder`).

### B3. Источник на сделке (workflow)

Нужен HubSpot Operations Hub Pro или Marketing Hub Pro и выше (действие «Copy property value»).

- **Триггер:** сделка создана в pipeline `Health & Fitness` (и любом другом).
- **Действия:** у **первой созданной** ассоциированной контакт-записи скопировать:
  - `hs_analytics_source` → `original_traffic_source`;
  - `hs_analytics_first_url` → `first_page_seen`;
  - `first_conversion_event_name` → `first_conversion_form`;
  - `icp_segment` → `icp_segment`;
  - `fx_vertical` → `fx_vertical`.
- **Если тарифа не хватает:** sales заполняет эти поля при создании сделки (выпадающие списки), а раз в месяц их сверяю я.

### B4. Качество лидов

1. **Homepage Popup**, 90% личных email. Варианты по возрастанию жёсткости:
   1. добавить обязательные поля Company и Job title;
   2. включить в настройках формы «Block free email providers»;
   3. вести consumer-посетителя на другой сценарий (например, статьи), а не в Contact sales.
   
   **Решено 2026-09-27: варианты 1 + 2** (обязательные Company и Job title, блок бесплатных email-доменов). Количество заявок упадёт, мусора станет меньше. Через месяц сверить число заявок popup и долю сделок.
2. **Lead scoring** (HubSpot score): +10 рабочий email; +15 `icp_segment` из FX или MT; +10 страна US/UK/CA/AU/DE; +20 форма contact, pricing или meeting; −30 личный email; −50 careers. Порог MQL — 30.
3. **Careers:** контакты из карьерных форм получают `lifecycle = Other`, `icp_segment = Job seeker` и исключаются из маркетинговых отчётов и списков. Если есть ATS, лучше перенести формы туда.
4. **Collected forms.** Логины и регистрации приложения Mobile Tailor (`.signup-form`, `.ng-*`) и Contact Form 7 (`.wpcf7-form`) HubSpot сейчас собирает как «формы». Если эти контакты заводятся через интеграцию приложения, collected forms для них выключить (Marketing → Forms → Non-HubSpot forms) или исключить из отчётов по маркетингу.
5. **Industry:** в свойствах контакта не заполняется (0 из 8 761). Брать `industry` с Company (enrichment HubSpot) и, если нужно, скопировать на контакт workflow.

### B5. Названия форм

Переименовать формы по схеме `{Продукт} | {Где} | {Что}`, например `FX | Pricing | Starter`, `FX | LP | Demo` (одна на все FX-лендинги, вертикаль — в `fx_vertical`), `3DLOOK | Home | Popup`, `MT | Pricing | Enterprise`. Названия с «former Health & Fitness LP» и технические селекторы уйдут из отчётов.

### B6. Отчёт «FitXpress organic» в HubSpot

Дашборд из четырёх отчётов:
1. Контакты по месяцам: `original source` × рабочий или личный email.
2. Контакты с рабочим email по `first_page_seen` (топ-30) и `first_conversion_form`.
3. FX-сделки (pipeline `Health & Fitness`) по `original_traffic_source` × квартал: количество, стадии, выигранные.
4. Контакты и сделки из `AI_REFERRALS` по месяцам.
5. **Связка «статья → лендинг»:** контакты с рабочим email из формы `FX | LP | Demo` по `fx_vertical` × `first_page_seen` (какая статья привела человека на лендинг, где он оставил заявку) и FX-сделки по `fx_vertical`.

### Приёмка блока B

- Тестовая заявка по ссылке с `?utm_source=test&utm_medium=test&utm_campaign=tz-check` после перехода на вторую страницу создаёт контакт с заполненными `utm_*` и `landing_page`.
- Тестовая сделка в `Health & Fitness` за 5 минут получает `original_traffic_source`, `first_page_seen` и `fx_vertical`.
- Форма `FX | LP | Demo`, отправленная с двух разных лендингов, создаёт два контакта с разными `fx_vertical`.
- Отправка popup с gmail-адресом блокируется (если выбран вариант 2).
- Дашборд B6 открывается и показывает данные.

---

## Блок C. Что делаю я после B

- Сверяю GA4 и HubSpot за первые две недели: число `generate_lead` против созданных контактов по каждой форме.
- Правлю UTM в соцпайплайне и аутбаунде (B2, п. 4).
- Делаю Looker Studio дашборд (GA4 + GSC) и отдельный еженедельный отчёт по позициям (план, п. 0.6–0.7).

## Что нужно от тебя или подрядчика

- Список офисных, VPN- и подрядческих IP.
- Тариф HubSpot: есть ли Operations Hub или Marketing Hub Pro (это решает судьбу B3).
- ~~Решение по popup~~: решено, варианты 1 + 2.
