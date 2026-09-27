---
product: fitxpress
type: tech-spec
date: 2026-09-27
owner: Вадим или подрядчик (админ HubSpot, доступ к GTM и GA4)
related: 2026-09-25-fitxpress-seo-plan.md (фаза 0, п. 0.2–0.6)
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

---

## Блок A. GA4 и GTM (1–1,5 дня)

### A1. Событие отправки каждой HubSpot-формы

1. В GTM создать тег Custom HTML на All Pages. Он слушает события отправки HubSpot-форм и отправляет в `dataLayer` `{event: 'hs_form_submit', form_id: <GUID формы>}`. Какое событие слушать, зависит от версии встраивания:
   - **Legacy-встраивание** (`hbspt.forms.create`, сейчас на сайте используется `js.hsforms.net`): `message`-событие, где `event.data.type === 'hsFormCallback' && event.data.eventName === 'onFormSubmitted'`. `id` формы — в `event.data.id`.
   - **Новые формы (v4):** window-событие `hs-form-event:on-submission:success`.
   
   Слушать оба варианта. Проверить в DebugView на каждой форме.
2. В GTM завести Lookup-таблицу `form_id → form_name` по списку ниже. Реальные ID взять в HubSpot → Marketing → Forms.
3. GA4-тег события `generate_lead` с параметрами `form_id`, `form_name`, `page_location`.
4. В GA4 → Admin → Custom definitions зарегистрировать `form_name` и `form_id` как event-scoped dimensions.
5. В GA4 → Admin → Key events отметить `generate_lead` ключевым событием. Старое событие для `/contact-us/` оставить, чтобы не рвать историю, но отчитываться по `generate_lead`.

**Названия форм** (выровнять с HubSpot, см. блок B5):

| Форма в HubSpot | form_name |
|---|---|
| Contact us & Partnership form | `contact_us` |
| FX Starter | `fx_pricing_starter` |
| FX Pricing - Talk to sales | `fx_pricing_talk_to_sales` |
| Contact Us - Pricing page (Entreprise plan) | `pricing_enterprise` |
| Homepage Popup | `home_popup` |
| Telehealth & Weight Loss (former Health & Fitness LP) | `fx_lp_telehealth` |
| Connected & Digital Fitness (former Health & Fitness LP) | `fx_lp_fitness` |
| Downloadable content (The Next Big Leap in Health) | `ebook_health` |
| … (The Digital Health Revolution) 2025 | `ebook_glp1` |
| Career forms | `careers`. **Не** ключевое событие |

### A2. Клики и бронирование встреч

- **`demo_click`:** клик по любой кнопке и ссылке «Book a demo», «Request a demo», «Talk to sales». Параметры `cta_text` и `page_location`. Сейчас эти кнопки работают на JS. После того как девелопер сделает их обычными `<a href>` (фаза 0, п. 0.1), триггер — Click URL или Click Text.
- **`meeting_booked`:** HubSpot Meetings присылает `postMessage` с `meetingBookSucceeded`. Тот же приём, что в A1; это тоже ключевое событие.
- **`docs_click`:** исходящий клик на `docs.fitxpress.3dlook.me`.
- **`pricing_plan_click`:** клик по плану на `/pricing/` с параметром `plan`.

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
- Визит с офисного IP не попадает в Realtime после активации фильтра.

---

## Блок B. HubSpot (1–2 дня)

### B1. Новые свойства

| Объект | Свойство | Тип | Значения | Кто заполняет |
|---|---|---|---|---|
| Contact | `icp_segment` | Dropdown | FX: Telehealth & GLP-1 · Online pharmacy · Life & disability insurance · Health plans & employer wellness · Bariatric & metabolic · Occupational health · CROs & clinical trials · Connected & digital fitness · Plastic surgery · BCRL / oncology RPM. MT: MTM brands & tailors · On-demand manufacturers · Uniforms · Wrist / limb. Прочее: Consumer · Agency / vendor · Job seeker · Other | Поле формы (если есть) или sales при квалификации |
| Deal | `icp_segment` | Dropdown | те же значения | Workflow копирует из контакта; sales правит |
| Deal | `original_traffic_source` | Dropdown | как `hs_analytics_source` у контакта | Workflow (B3) |
| Deal | `first_page_seen` | Single-line text | URL | Workflow (B3) |
| Deal | `first_conversion_form` | Single-line text | название формы | Workflow (B3) |

**Отдельное поле «product» не создавать.** У сделок продукт уже задаётся pipeline (`Health & Fitness` = FitXpress) и `product_to_sell`. У контактов уже есть поле «The solution I'm interested in» (заполнено 13 раз), его и использовать в формах.

### B2. UTM и страница входа в каждой форме

1. Во все маркетинговые формы добавить скрытые поля: `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`. Свойства в HubSpot уже существуют, но пустые.
2. Заполнение: HubSpot сам подставляет скрытые поля из query string, но только на странице первого входа. Поэтому GTM-скрипт при входе сохраняет UTM в cookie `first_utm` на 90 дней и подставляет значения в скрытые поля формы на любой странице (`onFormReady`).
3. Поле `landing_page` (скрытое) — первая страница визита из того же cookie.
4. **Наша сторона:** все ссылки на сайт в соцпостах, аутбаунде и email получают UTM по схеме `utm_source={linkedin|twitter|facebook|instagram|closely|email}&utm_medium={social|outbound|email}&utm_campaign={slug статьи или кампании}`. Это правка в наших пайплайнах: `post-lint` и `message-sequencer`. Её делаю я.

### B3. Источник на сделке (workflow)

Нужен HubSpot Operations Hub Pro или Marketing Hub Pro и выше (действие «Copy property value»).

- **Триггер:** сделка создана в pipeline `Health & Fitness` (и любом другом).
- **Действия:** у **первой созданной** ассоциированной контакт-записи скопировать:
  - `hs_analytics_source` → `original_traffic_source`;
  - `hs_analytics_first_url` → `first_page_seen`;
  - `first_conversion_event_name` → `first_conversion_form`;
  - `icp_segment` → `icp_segment`.
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

Переименовать формы по схеме `{Продукт} | {Где} | {Что}`, например `FX | Pricing | Starter`, `FX | LP Telehealth | Demo`, `3DLOOK | Home | Popup`, `MT | Pricing | Enterprise`. Названия с «former Health & Fitness LP» и технические селекторы уйдут из отчётов.

### B6. Отчёт «FitXpress organic» в HubSpot

Дашборд из четырёх отчётов:
1. Контакты по месяцам: `original source` × рабочий или личный email.
2. Контакты с рабочим email по `first_page_seen` (топ-30) и `first_conversion_form`.
3. FX-сделки (pipeline `Health & Fitness`) по `original_traffic_source` × квартал: количество, стадии, выигранные.
4. Контакты и сделки из `AI_REFERRALS` по месяцам.

### Приёмка блока B

- Тестовая заявка по ссылке с `?utm_source=test&utm_medium=test&utm_campaign=tz-check` после перехода на вторую страницу создаёт контакт с заполненными `utm_*` и `landing_page`.
- Тестовая сделка в `Health & Fitness` за 5 минут получает `original_traffic_source` и `first_page_seen`.
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
