---
product: fitxpress
type: runbook
date: 2026-09-27
owner: Вадим (исполнение), девелопер (сайт), Claude (п. 0.6–0.7)
related: 2026-09-25-fitxpress-seo-plan.md (фаза 0), 2026-09-27-tz-dev-site.md, 2026-09-27-tz-tracking-hubspot-ga4.md
---

# Фаза 0: пошаговая инструкция

Фаза 0 решает одну задачу: **чтобы каждая заявка доходила до нас, и мы видели, откуда она пришла.** Сейчас не выполнено ни то, ни другое:
- на `/pricing/` и `/contact-us/` JS-ошибки в 21% и 31% сессий;
- GA4 считает конверсией одну форму из десяти;
- в HubSpot у контактов нет UTM, а у сделок нет источника.

Пока это не исправлено, мы не увидим, дала ли что-то вся остальная работа из плана.

Файл самодостаточный: шаги, пути по меню, готовый код, проверка и типичные ошибки. Названия пунктов меню в GA4, GTM и HubSpot иногда немного отличаются от написанного: интерфейсы меняются. Если пункта нет там, где указано, ищи по названию в поиске настроек.

---

## Шаг 0. Подготовка (день 1, ~1 час)

### 0-A. Доступы

Проверь, что у тебя (или у подрядчика) есть:

| Система | Нужный уровень | Где проверить |
|---|---|---|
| Google Tag Manager, контейнер `GTM-PW77M7K` | **Publish** | GTM → Admin → User Management |
| GA4, property 251675969 | **Editor** (для фильтров и key events) | GA4 → Admin → Property access management |
| HubSpot | **Super Admin** или права на Properties, Forms, Workflows | Settings → Users & Teams |
| Microsoft Clarity | **Admin** проекта | Clarity → Settings → Team |
| WordPress | у девелопера — Administrator | — |
| Cloudflare или хостинг | у девелопера | — |

### 0-B. Список IP для фильтров

Собери в один список:
- внешний IP офиса (если есть);
- IP корпоративного VPN;
- домашние IP тех, кто часто заходит на сайт: ты, Ассель, девелопер, дизайнер, sales. Узнать свой IP: открыть <https://ifconfig.me>.

Если у людей динамические IP (меняются), для них используется второй способ — cookie-метка (шаг 0.3, п. 4).

### 0-C. Снимок «до»

Запиши эти цифры в таблицу. Через две недели сравним с ними.

| Метрика | Значение сейчас | Где взять |
|---|---|---|
| JS-ошибки `/pricing/` | 21% сессий | Clarity (72 ч на 2026-09-25) |
| JS-ошибки `/contact-us/` | 31% сессий | Clarity |
| Мёртвые клики `/pricing/` | 10% сессий | Clarity |
| Key events в GA4 в неделю | ~6–7 (только `/contact-us/`) | GA4 → Reports → Engagement → Key events |
| Органические контакты HubSpot с рабочим email | 32 за 2026-Q3 | `data/hubspot-findings.md` (лежит только локально) |
| Контакты с заполненным `utm_source` | 0 из 8 761 | HubSpot → Contacts → фильтр «UTM source is known» |

---

## Порядок работ

| День | Шаг | Кто |
|---|---|---|
| 1 | 0.9 Compliance-текст, 0.8 Редиректы | девелопер |
| 1 | 0.3 Фильтры внутреннего трафика (в режиме «Testing») | ты |
| 1–2 | 0.1 Диагностика в Clarity → задача девелоперу | ты |
| 2–4 | 0.1 Починка `/pricing/` и `/contact-us/`, кнопки demo — ссылками | девелопер |
| 3–5 | 0.2 События в GTM и GA4 | ты или подрядчик |
| 3–6 | 0.4 HubSpot: свойства, UTM, workflow | ты или подрядчик |
| 6–7 | 0.5 Квалификация popup и lead scoring | ты |
| 5–10 | 0.6 Дашборд, 0.7 Трекинг позиций | я |
| 8 | 0.3 Фильтры GA4 → «Active» | ты |
| 10 | Итоговая приёмка (раздел в конце) | ты + я |
| +14 дней | Сверка GA4 и HubSpot | я |

Шаги 0.9 и 0.8 — первыми: это быстро, и 0.9 снимает юридический риск.

---

## 0.9. Compliance: убрать неверные утверждения (день 1, девелопер, ~1 час)

**Зачем.** На главной и, скорее всего, в общем блоке других страниц написано «GDPR & HIPAA Compliant», «FitXpress maintains HIPAA compliance», «never link photos to personal identifiers». Это противоречит нашему опубликованному trust-FAQ. Такие фразы вызывают вопросы у юристов клиентов на этапе закупки.

**Шаги**
1. Отдай девелоперу пункт **P0-3** из `2026-09-27-tz-dev-site.md`. Там готовый текст замены (утверждённые формулировки) и список того, что удалить.
2. Попроси проверить все места: страницы, футер, попапы, глобальные виджеты Elementor (Templates → Saved Templates / Global Widgets).
3. Бейдж-картинку «HIPAA Compliant» удалить совсем. Бейджи GDPR и SSL оставить.

**Проверка.** Открой главную, `/pricing/` и любую статью. Нажми Ctrl+F и поищи `HIPAA Compliant`, `HIPAA compliance`, `personal identifiers`. Совпадений быть не должно. Для полной проверки девелопер делает поиск по базе WordPress, например плагином Better Search Replace в режиме «только поиск».

**Типичная ошибка:** правят страницу, но забывают глобальный виджет. Тогда фраза остаётся в футере на всех страницах.

---

## 0.8. Редиректы (день 1, девелопер, ~1 час)

| Откуда | Сейчас | Куда (301) | Как |
|---|---|---|---|
| `https://3dlook.ai/contact/` | 404 | `/contact-us/` | Yoast Premium → Redirects, или плагин Redirection |
| `http://www.3dlook.ai/*` | 404 | `https://3dlook.ai/$1` | Cloudflare → Rules → Redirect Rules (запись `www` в DNS должна существовать и проксироваться), или на хостинге |
| `https://3dlook.ai/blog/` | 2 редиректа через `3dlook.me` | один 301 → `/content-hub/` | Yoast / Redirection |
| `https://3dlook.ai/fitxpress` | 301 → блог-пост | пока на `/`, **после релиза `/fitxpress/`** → `/fitxpress/` | Yoast / Redirection |

**Проверка.** Каждая команда показывает один `301` и `location:` на цель; цель отвечает `200`:
```
curl -sI https://3dlook.ai/contact/ | grep -iE "^HTTP|^location"
curl -sI http://www.3dlook.ai/ | grep -iE "^HTTP|^location"
curl -sI https://3dlook.ai/blog/ | grep -iE "^HTTP|^location"
```
Если curl не под рукой, пришли мне сообщение — проверю я.

---

## 0.1. `/pricing/` и `/contact-us/`: найти и починить поломки (дни 1–4)

**Зачем.** Через эти страницы приходит основная часть сделок: форма Contact us & Partnership и бронирование встреч дали 260 контактов со сделками. При этом в 21–31% сессий там падает JavaScript, а в 10% сессий на `/pricing/` клик не срабатывает.

### Часть 1. Диагностика в Clarity (ты, ~40 минут)

API Clarity не отдаёт, **какие** элементы и **какие** ошибки, это видно только в интерфейсе.

1. **Тексты ошибок.**
   Clarity → проект 3dlook.ai → **Dashboard** → блок **JavaScript errors** (или «Script errors») → открыть. Период — последние 7 дней. Выпиши топ-5 ошибок: текст, страницу, количество, долю мобильных. Скриншот таблицы.
2. **Записи сессий с ошибками.**
   **Recordings** → **Filters**:
   - `URL` → contains → `/pricing/`;
   - **JavaScript errors** → Yes (фильтр может быть в разделе «Session insights» или «Behaviors»);
   - период — 7 дней.
   
   Посмотри 3–5 записей. Что человек пытался нажать, в какой момент появилась ошибка, отправилась ли форма. Сохрани ссылки на записи (кнопка Share). Повтори для `/contact-us/`.
3. **Мёртвые и rage-клики.**
   **Heatmaps** → URL `/pricing/` → вид **Click** → переключатели слоёв **Dead clicks** и **Rage clicks**. Отдельно desktop и mobile. Сделай скриншоты с отмеченными элементами.
4. Сложи всё в одно сообщение девелоперу: топ ошибок, 5–10 ссылок на записи, скриншоты карт кликов и пункт **P0-1** из `2026-09-27-tz-dev-site.md`.

### Часть 2. Починка (девелопер, 1–3 дня)

Отдай пункты **P0-1** (ошибки и мёртвые клики) и **P0-2** (demo-кнопки — обычные ссылки `<a href>`) из ТЗ девелоперу.

**Вероятные причины** (подсказка девелоперу):
- WP Rocket «Delay JavaScript execution» задерживает скрипт HubSpot-формы или Elementor-попапа;
- конфликт двух версий jQuery;
- попап Elementor открывается раньше, чем загружен скрипт формы.

### Проверка
- Отправь каждую форму на обеих страницах с тестовым адресом (например `test+pricing@3dlook.me`) с десктопа и с телефона. Контакт должен появиться в HubSpot.
- Через 7 дней в Clarity: JS-ошибки на обеих страницах меньше 3% сессий, мёртвые клики на `/pricing/` меньше 3%.
- Открой исходный код главной (Ctrl+U) и найди кнопку «Book a demo»: у неё должен быть `href="..."`.

**Типичная ошибка:** чинят на десктопе, а на мобильном ошибок было больше (27% на `/pricing/`). Проверять обязательно с телефона.

---

## 0.3. Фильтры внутреннего трафика и ботов (день 1 включить в Testing, день 8 — Active)

**Зачем.** Сейчас 562 из 994 просмотров новой telehealth-страницы — это наша команда. 63% сессий в Clarity — боты. С такими данными нельзя понять, работает ли страница.

### 1. GA4: определить внутренний трафик (~10 минут)
1. GA4 → **Admin** → колонка Property → **Data collection and modification** → **Data streams** → поток 3dlook.ai.
2. **Configure tag settings** → **Show more** → **Define internal traffic** → **Create**.
3. Rule name: `Office and team`. `traffic_type` value: `internal`.
4. Условия: **IP address** → **equals** → каждый IP из списка 0-B (кнопка Add condition для каждого). Для диапазона — **is in range (CIDR)**.
5. Save.

### 2. GA4: включить фильтр сначала в режиме Testing
1. **Admin** → **Data collection and modification** → **Data filters**.
2. Найди готовый фильтр **Internal Traffic** (создаётся автоматически; если его нет — Create filter → Internal traffic, parameter `traffic_type = internal`).
3. Filter state → **Testing** → Save.
4. Там же создай или включи фильтр **Developer Traffic** → Testing.

**Проверка (день 2).**
- **Explore** → Blank → добавь dimension **Test data filter name** и metric **Sessions**.
- Зайди на сайт с офисного IP и посмотри Realtime: визит должен появиться с пометкой фильтра.
- Если всё верно, **на день 8** переключи оба фильтра в **Active**.

⚠️ Active-фильтр необратим: отфильтрованные данные удаляются навсегда. Поэтому сначала неделя в Testing.

### 3. GTM: не отправлять данные со staging и из админки (~15 минут)
1. GTM → **Variables** → **Configure** → включи встроенные **Page Hostname** и **Page Path**.
2. **Triggers** → New → тип **Page View** → «Some Page Views»:
   - `Page Hostname` does not equal `3dlook.ai`, **или**
   - `Page Path` starts with `/wp-admin`.
   
   В одном триггере «или» не сделать, поэтому создай два триггера: `Exclude - not production` и `Exclude - wp-admin`.
3. В теге **GA4 Configuration / Google Tag** и в теге **Clarity** → Triggering → **Add Exception** → оба триггера.
4. Submit → Publish.

### 4. Cookie-метка для людей без постоянного IP (~10 минут)
1. GTM → Variables → New → **1st Party Cookie** → Cookie name `internal_user` → имя переменной `Cookie - internal_user`.
2. В теге Google Tag (GA4 config) → **Configuration parameters** (Shared event settings) → добавь параметр `traffic_type` со значением `{{Internal traffic type}}`. Это новая переменная типа **Lookup Table**: вход `{{Cookie - internal_user}}`, строка `1` → `internal`, default пусто.
3. Каждый сотрудник один раз открывает сайт и выполняет в консоли браузера (F12 → Console):
   ```js
   document.cookie = "internal_user=1; path=/; max-age=31536000; SameSite=Lax";
   ```
   Метка живёт год в этом браузере. Повторить на каждом устройстве.

### 5. Clarity (~5 минут)
1. Clarity → **Settings** → **IP blocking** → добавь те же IP.
2. **Settings** → **Setup** → убедись, что **Bot detection** включён.
3. **Settings** → **Setup** → **Google Analytics integration** → подключи GA4 property 251675969. После этого из записи Clarity можно перейти в GA4 и обратно.

### 6. Боты в Direct (разово, ~10 минут)
Полностью отфильтровать ботов в GA4 нельзя. Поэтому в стандартных отчётах смотрим столбец **Engaged sessions**, а не Sessions. Для исследований (Explore) заводим сегмент, который **исключает** ботов:
1. **Explore** → Blank → Segments → **+** → **Session segment** → имя `Без ботов (Direct SG/CN)`.
2. Блок «Include sessions» оставь пустым. Ниже нажми **Add group to exclude**, в этой группе два условия через AND:
   - `Session default channel group` → exactly matches → `Direct`;
   - `Country` → matches regex → `Singapore|China`.
3. **Save and apply**. Дальше в каждом исследовании применяем этот сегмент.

Если GA4 не даёт сохранить сегмент с пустым «Include sessions», добавь туда условие `Session default channel group` → matches regex → `.+`. Оно пропускает все сессии.

_Исправлено 06.10: условия `Engaged sessions = 0` в конструкторе сегментов нет. Оно и не нужно: за 06.09–05.10 у Direct из Сингапура 933 сессии, в среднем 3 секунды, 0 ключевых событий; у Direct из Китая 339 сессий и тоже 0 ключевых событий._

### 7. Google Ads против «paid»-сессий (~10 минут)
В Clarity все 47 сессий `google/cpc` за 3 дня — боты.
1. Google Ads → Campaigns → последние 7 дней: сколько кликов в день.
2. GA4 → Reports → Acquisition → Traffic acquisition → `google / cpc` → сессии в день.
3. Если кампаний нет вовсе — эти сессии фейковые; просто не учитываем их. Если кампании идут и сессий намного больше, чем кликов, проверь в Google Ads **Invalid clicks** (столбец Invalid clicks в Campaigns) и сообщи мне.

✅ **Сделано 06.10.** Клик-фрода нет. За 29.09–5.10 было 146 оплаченных кликов и 119 сессий. Невалидных кликов 4,58% — это норма. 47 «ботов» в Clarity — проверка посадочной страницы на модерации объявлений, за неё не платили. Сессии `google/cpc` с кампанией `(not set)` исключаем. Подробности в `data/ga4-findings.md` §6 и `data/clarity-findings.md` §9.

---

## 0.2. События в GTM и GA4 (дни 3–5, ~1 день)

**Зачем.** Чтобы GA4 видел каждую заявку и знал, какая форма её дала.

### 1. Слушатель отправки HubSpot-форм
GTM → **Tags** → New → **Custom HTML** → имя `HubSpot - form submit listener` → Triggering: **All Pages** (Initialization). Код:

```html
<script>
(function () {
  window.dataLayer = window.dataLayer || [];

  // Старое встраивание HubSpot-форм (hbspt.forms.create, js.hsforms.net)
  window.addEventListener('message', function (e) {
    if (e.data && e.data.type === 'hsFormCallback' && e.data.eventName === 'onFormSubmitted') {
      window.dataLayer.push({ event: 'hs_form_submit', form_id: e.data.id });
    }
    // Бронирование встречи через HubSpot Meetings
    if (e.data && e.data.meetingBookSucceeded) {
      window.dataLayer.push({ event: 'meeting_booked' });
    }
  });

  // Новые формы HubSpot (v4)
  window.addEventListener('hs-form-event:on-submission:success', function (event) {
    var id = '';
    try { id = window.HubSpotFormsV4.getFormFromEvent(event).getFormId(); } catch (err) {}
    window.dataLayer.push({ event: 'hs_form_submit', form_id: id });
  });
})();
</script>
```

### 2. Переменные
- **Data Layer Variable** `form_id` → имя `DLV - form_id`.
- **Lookup Table** `form_name`: вход `{{DLV - form_id}}`, default `other`. Строки ниже. GUID каждой формы: HubSpot → Marketing → Forms → открыть форму → GUID в адресной строке после `/editor/`.

| HubSpot-форма | form_name |
|---|---|
| Contact us & Partnership form | `contact_us` |
| FX Starter | `fx_pricing_starter` |
| FX Pricing - Talk to sales | `fx_pricing_talk_to_sales` |
| Contact Us - Pricing page (Entreprise plan) | `pricing_enterprise` |
| Homepage Popup | `home_popup` |
| Telehealth & Weight Loss (former Health & Fitness LP) | `fx_lp_telehealth` |
| Connected & Digital Fitness (former Health & Fitness LP) | `fx_lp_fitness` |
| Downloadable content (The Next Big Leap in Health) | `ebook_health` |
| …(The Digital Health Revolution) 2025 | `ebook_glp1` |
| Career submit form, Careers | `careers` |

### 3. Триггеры и теги

| Тег (тип GA4 Event) | Event name | Параметры | Триггер |
|---|---|---|---|
| `GA4 - generate_lead` | `generate_lead` | `form_id` = `{{DLV - form_id}}`, `form_name` = `{{form_name}}` | Custom Event `hs_form_submit`, условие `{{form_name}}` does not equal `careers` |
| `GA4 - careers_submit` | `careers_submit` | — | Custom Event `hs_form_submit`, `{{form_name}}` equals `careers` |
| `GA4 - meeting_booked` | `meeting_booked` | — | Custom Event `meeting_booked` |
| `GA4 - demo_click` | `demo_click` | `cta_text` = `{{Click Text}}`, `link_url` = `{{Click URL}}` | **Click - Just Links**, `Click Text` matches RegEx (ignore case) `book a demo\|request a demo\|talk to sales` |
| `GA4 - docs_click` | `docs_click` | `link_url` = `{{Click URL}}` | Click - Just Links, `Click URL` contains `docs.fitxpress.3dlook.me` |
| `GA4 - pricing_plan_click` | `pricing_plan_click` | `plan` = `{{Click Text}}` | Click - All Elements, `Page Path` equals `/pricing/` и `Click Text` matches RegEx по названиям планов на странице |

Встроенные переменные Click (Click Text, Click URL) включаются в Variables → Configure.

⚠️ `demo_click` заработает только после того, как девелопер сделает кнопки обычными ссылками (0.1, P0-2). До этого триггер «Just Links» их не увидит.

### 4. Публикация и настройка GA4
1. GTM → **Preview** → пройди по сайту, отправь тестовые формы и проверь, что события срабатывают → **Submit** → Publish, версия `Phase 0 - lead events`.
2. GA4 → Admin → **Custom definitions** → Create custom dimension (Event scope):
   - `form_name`;
   - `form_id`;
   - `cta_text`;
   - `plan`.
3. GA4 → Admin → **Key events** → **New key event**:
   - `generate_lead`;
   - `meeting_booked`;
   - `demo_click`.
   
   `docs_click` и `pricing_plan_click` оставить обычными событиями. Старое ключевое событие для `/contact-us/` не удалять, чтобы не рвать историю.

### Проверка
- GA4 → Admin → **DebugView**. Открой сайт в режиме GTM Preview. Отправь каждую форму из таблицы — должно прийти `generate_lead` с правильным `form_name`.
- Кликни «Book a demo» → `demo_click`. Забронируй тестовую встречу → `meeting_booked`.
- Через 2–3 дня: GA4 → Reports → Engagement → Events. `generate_lead` есть, `form_name` = `other` почти не встречается. Если встречается — какая-то форма не внесена в Lookup-таблицу.

**Типичные ошибки**
- Форма во всплывающем окне Elementor грузится позже слушателя. Слушатель на All Pages ловит её всё равно, но проверь именно popup.
- GUID перепутан с portal ID.

---

## 0.4. HubSpot: откуда пришёл контакт и сделка (дни 3–6, 1–2 дня)

### 1. Новые свойства (~30 минут)
HubSpot → ⚙️ Settings → **Data Management** → **Properties**.

**Contact properties** → Create property:

| Label | Internal name | Тип | Значения |
|---|---|---|---|
| ICP segment | `icp_segment` | Dropdown select | см. список ниже |
| Landing page (first touch) | `landing_page_first` | Single-line text | — |

**Список значений `icp_segment`.**
- FitXpress: `FX: Telehealth & GLP-1` · `FX: Online pharmacy` · `FX: Life & disability insurance` · `FX: Health plans & employer wellness` · `FX: Bariatric & metabolic` · `FX: Occupational health` · `FX: CROs & clinical trials` · `FX: Connected & digital fitness` · `FX: Plastic surgery` · `FX: BCRL / oncology RPM`.
- Mobile Tailor: `MT: MTM brands & tailors` · `MT: On-demand manufacturers` · `MT: Uniforms` · `MT: Wrist / limb`.
- Прочее: `Consumer` · `Agency / vendor` · `Job seeker` · `Other`.

**Deal properties** → Create property:

| Label | Internal name | Тип |
|---|---|---|
| ICP segment | `icp_segment` | Dropdown select (те же значения) |
| Original traffic source (contact) | `original_traffic_source` | Single-line text |
| First page seen (contact) | `first_page_seen` | Single-line text |
| First conversion form (contact) | `first_conversion_form` | Single-line text |

Отдельное свойство «product» не создаём: у сделок продукт уже задаётся pipeline (`Health & Fitness` = FitXpress) и `product_to_sell`.

### 2. Скрытые поля UTM в формах (~1 час)
Для каждой маркетинговой формы из таблицы 0.2 (кроме careers):
1. Marketing → **Forms** → открыть форму → **Edit**.
2. Добавить поля `UTM source`, `UTM medium`, `UTM campaign`, `UTM content`, `UTM term` и `Landing page (first touch)`. Свойства `utm_*` уже есть в HubSpot, просто пустые. У каждого поля включить **Make this field hidden**.
3. **Update / Publish**.

HubSpot сам заполнит скрытые поля из URL, но только на странице входа. Чтобы UTM «доживали» до формы на другой странице, в GTM нужны два тега.

**Тег 1: запомнить UTM при входе.** Custom HTML → All Pages → имя `UTM - store first touch`:
```html
<script>
(function () {
  var KEYS = ['utm_source','utm_medium','utm_campaign','utm_content','utm_term'];
  function getC(n){ var m = document.cookie.match('(?:^|; )' + n + '=([^;]*)'); return m ? decodeURIComponent(m[1]) : null; }
  function setC(n,v){ document.cookie = n + '=' + encodeURIComponent(v) + '; path=/; max-age=' + (60*60*24*90) + '; SameSite=Lax'; }
  var p = new URLSearchParams(location.search), found = {}, has = false;
  KEYS.forEach(function(k){ if (p.get(k)) { found[k] = p.get(k); has = true; } });
  if (has && !getC('first_utm')) setC('first_utm', JSON.stringify(found));
  if (!getC('landing_page')) setC('landing_page', location.origin + location.pathname);
})();
</script>
```

**Тег 2: подставить в форму.** Custom HTML → All Pages → имя `UTM - fill HubSpot hidden fields`:
```html
<script>
(function () {
  function getC(n){ var m = document.cookie.match('(?:^|; )' + n + '=([^;]*)'); return m ? decodeURIComponent(m[1]) : null; }
  function values(){
    var v = {}; try { v = JSON.parse(getC('first_utm') || '{}'); } catch(e) {}
    if (getC('landing_page')) v.landing_page_first = getC('landing_page');
    return v;
  }
  function fill(){
    var v = values();
    Object.keys(v).forEach(function(k){
      document.querySelectorAll('form.hs-form input[name="' + k + '"]').forEach(function(i){
        if (!i.value) {
          i.value = v[k];
          i.dispatchEvent(new Event('input', {bubbles: true}));
          i.dispatchEvent(new Event('change', {bubbles: true}));
        }
      });
    });
  }
  window.addEventListener('message', function(e){
    if (e.data && e.data.type === 'hsFormCallback' && e.data.eventName === 'onFormReady') fill();
  });
  window.addEventListener('hs-form-event:on-ready', function(event){
    // Для форм v4: они могут рендериться иначе, заполняем через их API
    try {
      var f = window.HubSpotFormsV4.getFormFromEvent(event), v = values();
      Object.keys(v).forEach(function(k){ f.setFieldValue('0-1/' + k, v[k]); });
    } catch (err) { fill(); }
  });
})();
</script>
```

⚠️ **Проверить на каждой форме:** открой сайт по ссылке с UTM, перейди на другую страницу, отправь форму. Если форма рендерится в iframe, тег 2 её не достанет. Тогда подрядчик переключает форму на встраивание без iframe (в настройках формы «Set as raw HTML form» или новый редактор).

**Наша сторона.** Я добавлю UTM во все ссылки на сайт в соцпостах и аутбаунде:
```
utm_source=linkedin|twitter|facebook|instagram|closely|email
utm_medium=social|outbound|email
utm_campaign=<слаг статьи или кампании>
```

### 3. Источник на сделке — workflow (~30 минут)
Сначала проверь тариф: Settings → **Account & Billing** → Products. Действие «Copy property value» есть в workflow на тарифах **Professional** (Marketing, Sales или Operations Hub).

Automation → **Workflows** → Create → From scratch → **Deal-based**.
1. **Trigger:** `Create date` is known (любая новая сделка). При включении отметить **Enroll existing deals** — дозаполнит старые сделки. Ограничь фильтром `Create date is after 2024-09-01`.
2. **Action → Copy property value** (×4). Источник — связанный контакт (Associated contact):
   - `Original Traffic Source` → в сделку `original_traffic_source`;
   - `First Page Seen` → `first_page_seen`;
   - `First Conversion` → `first_conversion_form`;
   - `ICP segment` → `icp_segment`.
3. Turn on.

⚠️ Если у сделки несколько контактов, проверь на 2–3 тестовых сделках, с какого контакта копируется значение. Нам нужен контакт, пришедший первым. Если HubSpot берёт не тот, sales правит вручную: поля видны в карточке сделки.

**Без тарифа Professional.** Добавь эти 4 поля в карточку сделки (Settings → Objects → Deals → Record customization) и сделай обязательными при создании сделки в pipeline `Health & Fitness`. Раз в месяц я сверяю.

### 4. Отделить мусор от маркетинга (~30 минут)
1. **Карьерные формы.** Contact-based workflow:
   - Trigger: `First conversion` contains `Career`.
   - Actions: `Lifecycle stage` = Other, `icp_segment` = Job seeker, add to static list `Exclude - job seekers`.
2. **Логины и регистрации Mobile Tailor и Contact Form 7**, которые HubSpot собирает как формы (`.signup-form`, `.ng-*`, `.wpcf7-form`): Marketing → Forms → **Non-HubSpot forms** (или Settings → Marketing → Forms) → выключить сбор для этих страниц или доменов. Эти контакты и так заводятся интеграцией приложения.
3. **Industry.** Contact-based workflow:
   - Trigger: `Associated company Industry` is known и контакт `Industry` is unknown.
   - Action: Copy property value из компании в контакт.

### 5. Переименовать формы (~15 минут)
Marketing → Forms → у каждой формы **Rename** по схеме `{Продукт} | {Где} | {Что}`:
`FX | Pricing | Starter`, `FX | Pricing | Talk to sales`, `FX | LP Telehealth | Demo`, `FX | LP Fitness | Demo`, `3DLOOK | Home | Popup`, `3DLOOK | Contact | Contact & partnership`, `FX | Ebook | Next big leap in health`, `FX | Ebook | GLP-1`, `MT | Pricing | Enterprise`, `HR | Careers | Apply`.

После переименования таблица GUID в GTM не меняется: GUID остаётся тем же.

### Проверка 0.4
- Открой `https://3dlook.ai/?utm_source=test&utm_medium=test&utm_campaign=phase0-check`, перейди на `/contact-us/` и отправь форму. У контакта в HubSpot заполнены `UTM source/medium/campaign = test / test / phase0-check` и `Landing page (first touch) = https://3dlook.ai/`.
- Создай тестовую сделку в `Health & Fitness` с этим контактом. Через 5 минут в сделке заполнены `original_traffic_source` и `first_page_seen`.
- Удали тестовые записи.

---

## 0.5. Квалификация: popup и lead scoring (дни 6–7, ~1 час)

**Решение 2026-09-27:** обязательные Company и Job title плюс блок бесплатных почтовых доменов.

### 1. Popup на главной
1. Marketing → Forms → `3DLOOK | Home | Popup` → Edit.
2. Добавить поля **Company name** (`company`) и **Job title** (`jobtitle`), оба **Required**.
3. Поле Email → настройки поля (или вкладка Options формы) → **Block free email providers** → On. Текст ошибки:
   > Please use your work email. For personal questions, see our Content Hub.
4. Publish.
5. Если popup — это виджет Elementor со встроенной HubSpot-формой, ничего в Elementor менять не нужно. Если это HubSpot pop-up (Marketing → Lead capture → Pop-up forms), поля и блокировка настраиваются там же, в редакторе pop-up.

Та же настройка потом ставится на формы калькуляторов (фаза 3).

### 2. Lead scoring
HubSpot → Marketing → **Lead Scoring** (новый инструмент) или Settings → Properties → **HubSpot score** (старый). Критерии:

| Условие | Баллы |
|---|---|
| Email не на бесплатном домене | +10 |
| `icp_segment` начинается с `FX:` или `MT:` | +15 |
| Country = United States, United Kingdom, Canada, Australia, Germany | +10 |
| First conversion содержит `Contact`, `Pricing`, `Talk to sales`, `Starter` или бронирование встречи | +20 |
| Email на бесплатном домене | −30 |
| `icp_segment` = Job seeker | −50 |

**Порог MQL — 30.** Contact-based workflow:
- Trigger: score ≥ 30 и `Lifecycle stage` = Subscriber или Lead.
- Action: `Lifecycle stage` = Marketing Qualified Lead.

### Проверка
- Отправь popup с адресом `@gmail.com` — должна появиться ошибка.
- Отправь с рабочим адресом без компании — форма не отправляется.
- Через 30 дней: число заявок из popup упало, доля MQL из popup выросла. Сверю по HubSpot.

---

## 0.6. Дашборд «FitXpress organic» (дни 5–10, я + ты 15 минут)

**Что делаю я**
1. **Еженедельный отчёт в Telegram** (понедельник утром) по GA4, GSC и HubSpot через уже подключённые коннекторы:
   - органические engaged sessions по уровням A/B/C;
   - `generate_lead` по `form_name` и landing page;
   - новые контакты с рабочим email по `landing_page_first`;
   - новые FX-сделки по `original_traffic_source`.
2. **Спецификация HubSpot-дашборда** из 4 отчётов (п. B6 в `2026-09-27-tz-tracking-hubspot-ga4.md`).

**Что делаешь ты** (Looker Studio создать через API нельзя, нужен твой Google-аккаунт):
1. <https://lookerstudio.google.com> → Create → Report.
2. Add data: **Google Analytics** → property 251675969. Затем Add data: **Search Console** → `sc-domain:3dlook.ai` → URL impression.
3. Дай мне доступ Editor (`vadim.bilan@3dlook.me` уже подключён к oo) — дальше страницы отчёта соберу по списку метрик.

---

## 0.7. Трекинг позиций (дни 5–10, я)

**Что делаю я**
- Скрипт по образцу `gsc-indexing-watch.py`: раз в неделю берёт позиции ~60 ключей (уровни A/B/C из плана, US и UK) из GSC (наши позиции) и Ahrefs (выдача). Хранит историю и шлёт в Telegram только изменения на ±3 позиции и выходы в топ-10/топ-3.
- Cron — понедельник, после отчёта по индексации.

**Что нужно от тебя:** ничего, кроме «ок» на расход Ahrefs (оценка ~5–8K units в неделю из 400K в месяц).

---

## Итоговая приёмка фазы 0 (день 10)

Пройди список и отметь. Всё, что не ✅, — пришли мне, разберёмся.

- [ ] На сайте нет «HIPAA Compliant», «HIPAA compliance», «personal identifiers» (0.9)
- [ ] `/contact/`, `http://www…`, `/blog/` отдают один 301 на правильную цель (0.8)
- [ ] Каждая форма на `/pricing/` и `/contact-us/` отправляется с десктопа и телефона; контакт появляется в HubSpot (0.1)
- [ ] Кнопки «Book a demo» — ссылки с `href` (0.1)
- [ ] В GA4 DebugView приходят `generate_lead` (с правильным `form_name`), `demo_click`, `meeting_booked`, `docs_click` (0.2)
- [ ] `generate_lead`, `meeting_booked`, `demo_click` отмечены как Key events (0.2)
- [ ] Фильтр внутреннего трафика в GA4 в режиме Testing, визиты с офисного IP помечаются (0.3)
- [ ] Clarity: IP blocking заполнен, интеграция с GA4 включена (0.3)
- [ ] Тестовая заявка с UTM создаёт контакт с заполненными `utm_*` и `landing_page_first` (0.4)
- [ ] Тестовая сделка в `Health & Fitness` получает `original_traffic_source` (0.4)
- [ ] Popup не принимает gmail и требует Company и Job title (0.5)
- [ ] Lead scoring создан, порог MQL = 30 (0.5)
- [ ] Первый еженедельный отчёт пришёл в Telegram (0.6); трекинг позиций запущен (0.7)

## Через 14 дней после приёмки

**Что проверю я**
- Сверю число `generate_lead` в GA4 с числом созданных контактов по каждой форме. Расхождение больше 20% значит, что какая-то форма не отслеживается.
- Сравню со снимком «до» (0-C): JS-ошибки, key events в неделю, доля контактов с UTM.

**Что делаешь ты**
- Переключи фильтр внутреннего трафика GA4 в **Active**, если не сделал на день 8.

После этого фаза 0 закрыта, и можно запускать фазу 1: `/fitxpress/`, вертикали, перелинковку.
