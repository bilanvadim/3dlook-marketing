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

## Статус на 2026-10-19

Фазу 0 исполняет Асель с 29.09, её трекер: таблица «Q4 SEO/GEO Plan based on AI Audit» (вкладка «Proposed Plan»; фаза 0 стоит на первые две недели октября). Задачи девелоперам она ведёт в таблице «Q4. Tech SEO/GEO». Статус ниже собран из переписки с ней в Slack (28.09–19.10) и проверен 19.10 на живом сайте, в GA4, HubSpot, опубликованном контейнере GTM и Clarity (только чтение). **Шагов 0.9 и 0.10 нет ни в её трекере, ни в таблице для девелоперов.**

| Шаг | Статус | Сделано | Осталось |
|---|---|---|---|
| 0.9 Compliance | ❌ | Ничего. В переписке P0-3 девелоперу не упоминается, в трекере Асель шага нет. | Бейдж «HIPAA Compliant» в футере остаётся на всех страницах (решение Вадима 19.10) и в задачу не входит. 19.10 на главной блок «GDPR & HIPAA Compliant» с «FitXpress maintains HIPAA compliance» и «never link photos to personal identifiers», ниже «does not process personal identifiers»; в FAQ `/pricing/` «FitXpress maintains HIPAA compliance». |
| 0.8 Редиректы | 🟡 | 19.10 без изменений. `/contact/` → `/contact-us/` и `/blog/` → `/content-hub/` одним 301. `/pricing` без слеша теперь ведёт на `/pricing/`, раньше уводил на главную. `https://www` → `/`. | `http://www.3dlook.ai/*` всё ещё 404. `/fitxpress` → `/`, как и задумано до релиза `/fitxpress/`. |
| 0.1 `/pricing/`, `/contact-us/` | 🟡 фикс выкачен | **19.10 фикс на сайте:** скрипты WebToffee больше не задерживаются Flying Scripts (исходник страницы), тег chat tracker в GTM исправлен (проверка типа и try/catch). Clarity за 72 ч до 19.10: ошибки в 0,86% сессий по сайту (3 ошибки), на `/pricing/` 0 из 60 сессий, на `/contact-us/` 0 из 16 (окно с выходными). Диагностика в Clarity собрана в таблицу (13.10). Тикет перепроверен 14.10 (`2026-10-14-p0-1-ticket-v2.md`): 86% JS-ошибок сайта дают WebToffee и Flying Scripts. 15.10 тикет ушёл девелоперам. Асель перенесла чат-бабл влево, он больше не закрывает «Accept All». 16.10 Асель отклонила находку «v2.js грузится 4 раза»: скриншоты её не подтверждают. Редизайн прайсинга и его релиз ведёт Асель (с 15.10), финальный макет 16.10 ушёл в дизайн. | Узнать у Асель дату релиза и через 7 дней (по `/contact-us/` через 14) замерить в Clarity. Dead clicks на `/pricing/` 6,7% (цель меньше 3%) закрывает редизайн. В шапке по-прежнему 4 пункта с `href="#"`. Тест 5 форм × 2 устройства не подтверждён. |
| 0.3 Фильтры | 🟡 | Internal Traffic и Developer Traffic в режиме Testing: с 01.10 GA4 пометил 62 и 29 сессий. П. 7 (Ads против `google/cpc`) закрыт 06.10, инструкция п. 6 исправлена 06.10. | После 13.10 GA4 не пометил ни одной сессии: скорее всего, оба фильтра около 14.10 переведены в Active, подтвердить у Асель. В GTM есть cookie `internal_user` и исключение `wp-admin`. В переписке нет подтверждения по GTM-исключениям staging и wp-admin, cookie `internal_user`, IP blocking и связке Clarity с GA4, сохранённому сегменту «Без ботов». |
| 0.2 События | ✅ | 19.10: за 08–18.10 `generate_lead` 28 (contact_us 15, fx_pricing_starter 5, home_popup 4, fx_pricing_talk_to_sales 2, fx_lp_telehealth 1, pricing_enterprise 1, `other` ни разу), `demo_click` 170, `pricing_plan_click` 58 (с 15.10 каждый день, триггер исправлен), форма Pro в Lookup-таблице. Асель закончила 07.10. В GA4 за 08–15.10: `generate_lead` 23 (contact_us 13, fx_pricing_starter 4, home_popup 3, fx_pricing_talk_to_sales 2, pricing_enterprise 1, `other` ни разу), `demo_click` 128, `careers_submit` 2. `generate_lead` и `demo_click` отмечены как key events. | Ничего. `meeting_booked` убран из приёмки (Meetings на страницах нет). `docs_click` = 0, потому что на сайте нет ссылок на `docs.fitxpress.3dlook.me`; событие понадобится с `/developers/` (п. 1.3 плана). |
| 0.4 HubSpot | 🟡 | Свойства созданы на контакте и сделке; `icp_segment` из 7 значений (см. 0.4 п. 1). Скрытые UTM-поля стоят во всех формах с просмотрами (02.10). `landing_page_first` заполняется в Contact, Pricing и с 15.10 в Popup. Workflow источника на сделке работает: `original_traffic_source` у 424 из 425 сделок с 2024-09 (19.10). Workflow соискателей включён. Формы переименованы по схеме (около 13.10). П. 4.2 и 4.3 сняты 12.10. **Тест с UTM пройден:** 15.10 Асель отправила форму со своего контакта (`test / test / phase0-check`), плюс две реальные заявки с `utm_source=chatgpt.com` (16.10, 08.10) пронесли UTM со страницы входа до формы на `/contact-us/`. Источник у всех 10 новых сделок с 02.10. | Старые соискатели не импортированы: `Job seeker` у 508 (19.10), а по разбору 12.10 их около 1 110 (`job-seekers-legacy-import.csv`, 606 строк). Ветка-защита для MQL+ и контактов со сделками не подтверждена. `icp_segment` стоит только у соискателей: FX, MT и WM никто не проставляет, у сделок он пуст. За 02–19.10 `utm_source` пришёл у 2 из 122 новых контактов (оба ChatGPT): в наших ссылках из соцпостов и аутбаунда UTM пока нет (см. 0.4.2, «Наша сторона»). |
| 0.5 Квалификация | ✅ | Company и Job title в popup уже были обязательными. Бесплатные почтовые домены заблокированы на всех формах, кроме MT, двух ebook и Career (13.10). Lead scoring снят 13.10, см. 0.5 п. 2. | Домена `gmail.co.in` нет в стандартном списке HubSpot. Решили не добавлять (14.10). |
| 0.6 Дашборд | ✅ 16.10 | Google Sheet «3DLOOK Organic Dashboard» на весь сайт (FitXpress, Mobile Tailor, Wrist), с 2025-09-29 по неделям, плюс отчёт в Telegram. Скрипт `scripts/organic-dashboard.py`, cron вт и ср 06:20 UTC. Цифры сверены с GSC, GA4, HubSpot и листом MT self-serve 16.10. | Таблица открыта на чтение всему домену 3dlook.me. Отчёт B6 в HubSpot не собран: решить, нужен ли он поверх таблицы. |
| 0.10 Одна форма FX-лендингов | 🟡 начат 19.10 | Свойство `fx_vertical` создано на контакте и сделке (10 значений, совпадают с GTM). У `expected_monthly_scan_volume` новые варианты (старое `501-1000` ещё в списке). Форму `11acb23a` Асель собрала 19.10, добавляет имя и фамилию. До этого в HubSpot были три отдельные формы лендингов: шаг про одну форму в ранбук не попал. | Переименовать форму в `FX \| LP \| Demo`, необязательная галочка на рассылку, кнопка «Book a demo», уведомления. В GTM по шагу ещё ничего нет. Workflows, переключение трёх страниц, проверки, пометка `\| OLD`. |
| 0.7 Позиции | ✅ 16.10 | 86 пар ключ × страна (`rank-keywords.csv`): средняя позиция в Google из Search Console и позиция в Ahrefs, история за 54 недели, изменения в Telegram. | — |

**Остальной план, что движется параллельно:**
- 2.2 robots.txt исправлен, Google перечитал его к 07.10.
- 2.3 GPTBot (P0-4): 16.10 всё ещё 403 на `/` и на `/robots.txt`. 14.10 инструкцию поправили: правило стоит в nginx на сервере (AWS), Cloudflare и robots.txt тут ни при чём.
- 2.4 llms.txt лежит на сайте (Last updated 2026-09-18).
- 2.1 FAQ JSON-LD: FAQPage есть на trust-FAQ и `/wrist-measurement/`, на Capture Quality FAQ (опубликована 14.10) его нет.
- Контент: пресс-релиз Wrist Measurement опубликован 08.10, Capture Quality FAQ опубликована 14.10, Асель делает перелинковку.
- Фаза 1: фитнес-лендинг живой (`/fitxpress/for-connected-and-digital-fitness/`), сам `/fitxpress/` пока 301 на главную. GLP-1 и бариатрию делает Ника, Асель ревьюит (15.10). BMI verification остаётся на `/for-bmi-verification/` и расширяется Smart Scales и антифродом (07.10).
- Порядок от Асель: закончить фазу 0, перекалибровать аудит на новых данных, потом фаза 1. Ссылочный план она разбирает после фазы 0.
- P1-6 и P2-1 перепроверены 19.10 (ТЗ переписано, ответ Асель в Slack). Пагинацию `/content-hub/` девелоперам не отдаём: `/sitemap/` из мая уже даёт Google путь ко всем постам, а 60 «сирот» лечатся контекстными ссылками (п. 1.5). По скорости только HTTP/2 вместе с P0-4 и CLS в приёмку редизайна `/pricing/`.

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
| 2–4 | 0.1 Починка `/pricing/` и `/contact-us/` | девелопер |
| 3–5 | 0.2 События в GTM и GA4 | ты или подрядчик |
| 3–6 | 0.4 HubSpot: свойства, UTM, workflow | ты или подрядчик |
| 6–7 | 0.5 Квалификация popup и lead scoring | ты |
| 5–10 | 0.6 Дашборд, 0.7 Трекинг позиций | я |
| 8 | 0.3 Фильтры GA4 → «Active» | ты |
| после 0.2 и 0.4 | 0.10 Одна демо-форма на все FX-лендинги | ты + девелопер |
| 10 | Итоговая приёмка (раздел в конце) | ты + я |
| +14 дней | Сверка GA4 и HubSpot | я |

Шаги 0.9 и 0.8 — первыми: это быстро, и 0.9 снимает юридический риск.

---

## 0.9. Compliance: убрать неверные утверждения (день 1, девелопер, ~1 час)

**Зачем.** На главной и, скорее всего, в общем блоке других страниц написано «GDPR & HIPAA Compliant», «FitXpress maintains HIPAA compliance», «never link photos to personal identifiers». Это противоречит нашему опубликованному trust-FAQ. Такие фразы вызывают вопросы у юристов клиентов на этапе закупки.

**Шаги**
1. Отдай девелоперу пункт **P0-3** из `2026-09-27-tz-dev-site.md`. Там готовый текст замены (утверждённые формулировки) и список того, что удалить.
2. Попроси проверить все места: страницы, попапы, глобальные виджеты Elementor (Templates → Saved Templates / Global Widgets).
3. Футер не трогать. Бейдж «HIPAA Compliant» в футере остаётся на всех страницах (решение Вадима 2026-09-18, подтверждено 2026-10-19). Задача только про текст на страницах.

**Проверка.** Открой главную, `/pricing/` и любую статью. Нажми Ctrl+F и поищи `GDPR & HIPAA Compliant`, `HIPAA compliance`, `personal identifiers`. Совпадений быть не должно. Бейдж в футере (картинка с alt «HIPAA Compliant») остаётся, его не считаем. Для полной проверки девелопер делает поиск по базе WordPress, например плагином Better Search Replace в режиме «только поиск».

**Типичная ошибка:** правят страницу, но забывают глобальный виджет. Тогда фраза остаётся в общем блоке на всех страницах.

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

Отдай пункт **P0-1** (ошибки и мёртвые клики) из ТЗ девелоперу. P0-2 снят 2026-10-08: demo-кнопки уже ссылки.

**Вероятные причины** (подсказка девелоперу):
- WP Rocket «Delay JavaScript execution» задерживает скрипт HubSpot-формы или Elementor-попапа;
- конфликт двух версий jQuery;
- попап Elementor открывается раньше, чем загружен скрипт формы.

### Проверка
- Отправь каждую форму на обеих страницах с тестовым адресом (например `test+pricing@3dlook.me`) с десктопа и с телефона. Контакт должен появиться в HubSpot.
- Через 7 дней в Clarity: JS-ошибки на обеих страницах меньше 3% сессий, мёртвые клики на `/pricing/` меньше 3%.

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
| `FX \| LP \| Demo` — общая форма FX-лендингов (шаг 0.10, с 19.10) | `fx_lp_demo` |
| Downloadable content (The Next Big Leap in Health) | `ebook_health` |
| …(The Digital Health Revolution) 2025 | `ebook_glp1` |
| Career submit form, Careers | `careers` |

### 3. Триггеры и теги

| Тег (тип GA4 Event) | Event name | Параметры | Триггер |
|---|---|---|---|
| `GA4 - generate_lead` | `generate_lead` | `form_id` = `{{DLV - form_id}}`, `form_name` = `{{form_name}}` | Custom Event `hs_form_submit`, условие `{{form_name}}` does not equal `careers` |
| `GA4 - careers_submit` | `careers_submit` | — | Custom Event `hs_form_submit`, `{{form_name}}` equals `careers` |
| `GA4 - meeting_booked` | `meeting_booked` | — | Custom Event `meeting_booked` |
| `GA4 - demo_click` | `demo_click` | `cta_text` = `{{Click Text}}`, `link_url` = `{{Click URL}}` | Два триггера **Click - Just Links** на один тег: (1) `Click URL` contains `#bd-modal`, ловит все demo-попапы, включая `#bd-modal-starter`, `-pro` и `-personalized` на `/pricing/`; (2) `Click URL` contains `/contact-us/` и `Click Text` matches RegEx (ignore case) `book a demo\|let.?s talk\|request a demo\|talk to sales` |
| `GA4 - docs_click` | `docs_click` | `link_url` = `{{Click URL}}` | Click - Just Links, `Click URL` contains `docs.fitxpress.3dlook.me` |
| `GA4 - pricing_plan_click` | `pricing_plan_click` | `plan` = `{{Click Text}}` | Click - All Elements, `Page Path` equals `/pricing/` и `Click Text` matches RegEx по названиям планов на странице |

Встроенные переменные Click (Click Text, Click URL) включаются в Variables → Configure.

Demo-кнопки уже сделаны ссылками `<a href="#bd-modal…">` (проверено 2026-10-08), поэтому триггер «Just Links» ловит их сразу и девелопер не нужен. Триггер по тексту не годится: на `/for-bmi-verification/` кнопка в тот же попап называется «Get Started», на главной — «Let's talk».

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

**Список значений `icp_segment`:** `FX` · `MT` · `WM` · `Consumer` · `Agency / vendor` · `Job seeker` · `Other`.

_Изменено 30.09: поле в HubSpot держит не больше 10 значений, поэтому сегменты внутри FX и MT в него не попадают (решение Вадима, `WM` добавила Асель). Первоначальный список из 18 значений: FX × 10 вертикалей, MT × 4, плюс Consumer, Agency / vendor, Job seeker, Other._

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

**Наша сторона.** Я добавлю UTM во все ссылки на сайт в соцпостах и аутбаунде (_на 19.10 не сделано: пайплайны постов и аутбаунда UTM не ставят_):
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
2. ~~Выключить сбор Non-HubSpot forms для Mobile Tailor и Contact Form 7~~. **Снято 2026-10-12, сбор НЕ выключать.** Большинство контактов MT создаёт сама собранная форма, а не интеграция приложения. Она же связывает cookie с контактом и даёт источник (органика, прямые заходы) и историю страниц. Если выключить, новые self-serve пользователи станут Offline. Вред только косметический: логин в MT перезаписывает recent conversion. В маркетинговых отчётах исключай формы с префиксом `MTM.3DLOOK`. Contact Form 7 уже не используется (одна отправка за 12 месяцев).
3. ~~Копировать Industry с компании на контакт~~. **Снято 2026-10-12.** Industry у контакта — старый список из 4 значений времён fashion (Ecommerce/Retailer × Brand/Multibrand), у компании — стандартный список HubSpot (~150 значений), поэтому Copy property value падает с «internal values are missing». Копировать и не нужно: списки, workflow и custom report builder берут Industry связанной компании напрямую. Сегменты ICP — в `icp_segment`.

### 5. Переименовать формы (~15 минут)
Marketing → Forms → у каждой формы **Rename** по схеме `{Продукт} | {Где} | {Что}`:
`FX | Pricing | Starter`, `FX | Pricing | Talk to sales`, `FX | LP | Demo`, `3DLOOK | Home | Popup`, `3DLOOK | Contact | Contact & partnership`, `FX | Ebook | Next big leap in health`, `FX | Ebook | GLP-1`, `MT | Pricing | Enterprise`, `HR | Careers | Apply`.

После переименования таблица GUID в GTM не меняется: GUID остаётся тем же.

_Исправлено 19.10:_ до этой даты здесь стояли `FX | LP Telehealth | Demo` и `FX | LP Fitness | Demo`, то есть форма под каждый лендинг. Это расходилось с решением от 29.09: на всех FX-лендингах одна форма `FX | LP | Demo`, вертикаль — в `fx_vertical`. Переход — шаг 0.10.

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

**Снято 2026-10-13 (Вадим и Асель).** Лидов квалифицируют sales вручную, при нынешних объёмах scoring им не нужен. Вернёмся, когда этого потребует операционка. Ниже исходный вариант на этот случай. Критерий `icp_segment` начинается с `FX:` или `MT:` устарел: теперь значения просто `FX`, `MT` и `WM`.

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

**Сделано 2026-10-16, но иначе, чем описано ниже.** Looker Studio в регионе Вадима не даёт создавать отчёты, а у Looker Studio нет API, через который отчёт мог бы собрать я. Поэтому дашборд сделан как Google Sheet «3DLOOK Organic Dashboard» (владелец vadim.bilan@3dlook.me) и сразу на весь сайт: FitXpress, Mobile Tailor, Wrist Measurement.
- Вкладки: Dashboard (последние 4 недели против предыдущих 4, кварталы против целей плана, ключевые запросы, шесть графиков), Weekly, Monthly, Leads by form, Rankings, Rank history, Top pages, About.
- Источники и определения описаны в docstring `scripts/organic-dashboard.py` и на вкладке About.
- Cron: вт 06:20 UTC, в ср повтор на случай, если GSC ещё не отдал воскресенье как финальные данные. Отчёт в Telegram уходит раз в неделю.
- GA4 почти ничего не записывал с 05.02 по 25.06.2026 (`data/ga4-findings.md` §0.1). Всё из GA4 за эти даты показано как «GA4 gap», а не как ноль.

План ниже оставлен как исходный.

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

**Сделано 2026-10-16, в том же скрипте и той же таблице (вкладки Rankings и Rank history).** Список ключей: `rank-keywords.csv` рядом с этим файлом, правится там. Главная цифра — средняя позиция в Google из Search Console, взвешенная по показам. Ahrefs оказался узким: из 86 пар ключ × страна он видит наш сайт в 7, Search Console — в 31. Ahrefs стоит второй колонкой и стоит ~100 юнитов в неделю (бэкфилл 54 недель обошёлся в ~7K).

**Что делаю я**
- Скрипт по образцу `gsc-indexing-watch.py`: раз в неделю берёт позиции ~60 ключей (уровни A/B/C из плана, US и UK) из GSC (наши позиции) и Ahrefs (выдача). Хранит историю и шлёт в Telegram только изменения на ±3 позиции и выходы в топ-10/топ-3.
- Cron — понедельник, после отчёта по индексации.

**Что нужно от тебя:** ничего, кроме «ок» на расход Ahrefs (оценка ~5–8K units в неделю из 400K в месяц).

---

## 0.10. Одна демо-форма на все FX-лендинги и поле `fx_vertical` (~1 день: ты ~4 часа, девелопер ~1 час)

_Добавлено 2026-10-19._ Решение принято 29.09 и записано в ТЗ по трекингу (`2026-09-27-tz-tracking-hubspot-ga4.md`, B1, B2.5, B5) и в ките лендингов, а в этот ранбук не попало. Шаг 0.4.5 до 19.10 даже называл формы под каждую посадку. Поэтому в HubSpot сейчас три отдельные формы лендингов:

| Форма | GUID | Где стоит |
|---|---|---|
| `FX \| LP Connected & Digital Fitness \| Demo` | `887dc2d4-6427-4a4a-a02e-9c2a82b6aa6e` | `/fitxpress/for-connected-and-digital-fitness/` |
| `FX \| LP Telehealth & Digital Health \| Demo` | `5191936a-a8dc-41eb-8c2d-facfe0abf1f9` | telehealth-страница и `/for-bmi-verification/` |
| `FX \| LP Insurance Underwriting \| Demo` | `11acb23a-e81c-46ee-bb23-4d47a0ef0125` | insurance-лендинг (ещё не опубликован), создана 19.10 |

**Зачем.** Каждая новая форма — ещё одна копия согласия, блокировки gmail, уведомлений, workflows и строки в GTM. Копии расходятся: у insurance-формы поле объёма, у fitness и telehealth вместо него сайт. Telehealth-форма стоит и на BMI verification, поэтому по названию формы вертикаль там уже определяется неверно. С одной формой новый лендинг — это одна строка в GTM, а в HubSpot ничего не меняется.

**Как устроено после перехода.** На всех FX-лендингах стоит одна форма `FX | LP | Demo` с одним дизайном. Различаются только заголовок над формой и текст вокруг неё, а они живут на странице, а не в HubSpot. Вертикаль GTM определяет по адресу страницы и записывает в скрытое поле `fx_vertical` формы, а также в параметр события `generate_lead` в GA4. Все три формы встроены как raw HTML (`renderRawHtml: true`), поэтому GTM может заполнить поле. UTM он заполняет тем же способом с 02.10.

### 1. Свойство `fx_vertical` (~10 минут)
HubSpot → Settings → Properties.
- **Contact** → Create property: Label `FX vertical`, internal name `fx_vertical`, Dropdown select. Значения задать так, чтобы **internal value** совпадало с тем, что пишет GTM: `fitxpress_parent` · `bmi_verification` · `fitness` · `telehealth` · `glp1` · `insurance` · `wellness` · `bariatric` · `clinical_trials` · `occupational_health`.
- **Deal** → такое же свойство с теми же значениями.

Это страница, на которой оставили заявку, а не сегмент клиента: на wellness-лендинг может прийти страховщик. `icp_segment` по-прежнему ставит sales, и из `fx_vertical` его не заполняем.

### 2. Сделать общую форму (~30 минут)
Общей становится insurance-форма `11acb23a`: в ней уже нужные поля, а страница ещё не опубликована, так что история заявок не теряется. Marketing → Forms → открыть её:
1. **Rename** → `FX | LP | Demo`.
2. Видимые поля: First name, Last name, Business email, Company, Job title — обязательные. Expected monthly scan volume — необязательное. Варианты (по ТЗ от 30.09): Under 500 · 500–1,000 · 1,000–5,000 · Over 5,000 · Not sure yet. Сейчас там 1-500 / 501-1000 / More than 1000. Варианты меняются в свойстве `expected_monthly_scan_volume` (Settings → Properties).
3. Скрытые поля: UTM (5 шт.), Landing page (first touch) — уже есть. Добавить `FX vertical`, **Make this field hidden**, значение по умолчанию не ставить.
4. **Согласие** (Options → Data privacy and consent): галочка на обработку данных — обязательная, текст как в дизайне: «I agree to 3DLOOK processing my details to respond to this request, as described in the privacy policy.» Галочка на рассылку — **необязательная**. Сейчас обязательная галочка на рассылку стоит во всех трёх формах. Если без согласия на рассылку нельзя запросить демо, по GDPR такое согласие не считается добровольным, а UK и ЕС — наши рынки.
5. Кнопка: `Book a demo` (как на страницах и в дизайне; сейчас `Let's talk`).
6. **Уведомления и автоответ** (Options → Notifications, Follow-up email): открыть fitness- и telehealth-формы, посмотреть, кому уходят уведомления о заявке и есть ли follow-up email, и выставить то же в новой форме.
7. **Publish / Update.**

### 3. GTM (~30 минут)
1. **Variables → New → Lookup Table**, имя `fx_vertical`. Input: `{{Page Path}}`. Default: оставить пустым. Строки (слеш в конце обязателен, Page Path отдаёт путь со слешем):

   | Page Path | fx_vertical |
   |---|---|
   | `/fitxpress/` | `fitxpress_parent` |
   | `/for-bmi-verification/` (потом и `/fitxpress/bmi-verification/`) | `bmi_verification` |
   | `/fitxpress/for-connected-and-digital-fitness/` | `fitness` |
   | `/structured-body-data-for-telehealth-digital-health-programs/` (потом и `/fitxpress/for-telehealth/`) | `telehealth` |
   | `/fitxpress/for-glp-1-programs/` | `glp1` |
   | `/fitxpress/for-insurance-underwriting/` | `insurance` |
   | `/fitxpress/for-wellness-programs/` | `wellness` |
   | `/fitxpress/for-bariatric-programs/` | `bariatric` |
   | `/fitxpress/for-clinical-trials/` | `clinical_trials` |
   | `/fitxpress/for-occupational-health/` | `occupational_health` |

   Строки для ещё не опубликованных страниц можно завести сразу. Перед публикацией каждой страницы сверить её финальный URL с таблицей.
2. **Тег `UTM - fill HubSpot hidden fields`** (из 0.4.2): в функции `values()` перед `return v;` добавить строки:
   ```js
   var fv = '{{fx_vertical}}';
   if (fv && fv !== 'undefined') v.fx_vertical = fv;
   ```
   Остальное в теге не меняется: он уже заполняет пустые скрытые поля при `onFormReady` и в формах v4.
3. **Lookup `form_name`** (из 0.2.2): добавить строку `FX | LP | Demo` (GUID `11acb23a-e81c-46ee-bb23-4d47a0ef0125`) → `fx_lp_demo`. Строки старых LP-форм не удалять: на них держится история в GA4.
4. **Тег `GA4 - generate_lead`**: добавить параметр `fx_vertical` = `{{fx_vertical}}`.
5. Preview → проверка (п. 6) → Publish, версия `Phase 0 - one FX form`.
6. GA4 → Admin → Custom definitions → Create custom dimension: `fx_vertical`, Event scope.

### 4. HubSpot: перенести на новую форму всё, что висит на старых (~1 час)
1. **Workflows.** Automation → Workflows: найти все workflows, у которых в триггере или в ветках стоят fitness- или telehealth-форма: назначение owner, автоответ, sequence, списки. В каждый добавить `FX | LP | Demo` рядом со старой формой (через OR). Старую не убирать до конца перехода.
2. **Workflow источника сделки** (0.4.3): добавить пятое действие Copy property value: `fx_vertical` контакта → `fx_vertical` сделки.
3. **Списки и отчёты**, где фильтр стоит по старым формам: добавить новую форму.

### 5. Переключить страницы (девелопер, ~1 час)
По одной странице, после каждой — проверка (п. 6):
1. `/fitxpress/for-connected-and-digital-fitness/`: в встраивании формы заменить `formId` `887dc2d4-…` на `11acb23a-e81c-46ee-bb23-4d47a0ef0125`.
2. Telehealth-страница: `5191936a-…` → `11acb23a-…`.
3. `/for-bmi-verification/`: `5191936a-…` → `11acb23a-…`.

Если форма стоит в попапе Elementor, заменить в попапе. Новые лендинги (insurance, GLP-1, бариатрия) сразу встраивают `11acb23a-…`: в HTML-прототипах стоит заглушка с `/contact-us/`, её девелопер меняет на этот ID.

### 6. Проверка на каждой странице
1. Открой страницу с `?utm_source=test&utm_medium=test&utm_campaign=one-form-check` в режиме GTM Preview.
2. Отправь форму с адресом `test+fx-<вертикаль>@3dlook.me`.
3. Проверь:
   - в GTM Preview на теге `GA4 - generate_lead` стоят `form_name = fx_lp_demo` и правильный `fx_vertical`; то же видно в GA4 DebugView;
   - у контакта в HubSpot заполнены `fx_vertical`, `utm_*` и `landing_page_first`;
   - пришло уведомление о заявке, сработали назначение owner и автоответ;
   - на форме видны две галочки, и форма отправляется без галочки на рассылку.
4. Удали тестовые контакты.

### 7. Старые формы
- Не удалять: в них история заявок, и на них ссылаются старые отчёты. Переименовать с пометкой `| OLD` в конце, чтобы их не выбрали для новой страницы.
- У заявок, пришедших до перехода, `fx_vertical` пустой. Для истории вертикаль берётся по старой форме. Заявки telehealth-формы со страницы `/for-bmi-verification/` различаются по URL отправки (Forms → Submissions → столбец Page URL). Если нужно в отчётах — один раз проставить `fx_vertical` старым контактам массовой правкой.

**Типичные ошибки**
- `fx_vertical` не доходит до контакта, хотя в GTM Preview значение есть. Internal value в свойстве HubSpot не совпадает с тем, что пишет GTM (`Fitness` вместо `fitness`), и HubSpot отбрасывает значение.
- Страница открыта без слеша в конце или с другим путём, и Lookup Table отдаёт пустое значение. Проверь `{{Page Path}}` в Preview и добавь строку.
- После переключения перестали приходить уведомления sales: workflows или уведомления остались только на старой форме (п. 2.6 и 4.1).

---

## Итоговая приёмка фазы 0 (день 10)

Пройди список и отметь. Всё, что не ✅, — пришли мне, разберёмся.

Отметки на 2026-10-19 (проверено на сайте, в GA4, HubSpot, GTM и Clarity):

- [ ] В тексте страниц нет «GDPR & HIPAA Compliant», «HIPAA compliance», «personal identifiers» (0.9); бейдж в футере остаётся. _16.10: все три фразы на месте. 19.10: на месте на главной и в FAQ `/pricing/`._
- [ ] `/contact/`, `http://www…`, `/blog/` отдают один 301 на правильную цель (0.8). _16.10: `/contact/` и `/blog/` в порядке, `http://www` 404._
- [ ] Каждая форма на `/pricing/` и `/contact-us/` отправляется с десктопа и телефона; контакт появляется в HubSpot (0.1). _19.10: фикс выкачен; реальные заявки 08–18.10 пришли с Contact, FX Starter, Talk to sales и MT Enterprise, с FX Pro только тест Асель. Формальный тест 10 отправок не подтверждён. JS-ошибки 0% за 72 ч, замер через неделю после релиза._
- [x] В GA4 приходят `generate_lead` (с правильным `form_name`) и `demo_click` (0.2). _С 07–08.10. `meeting_booked` из критерия убран: Meetings на этих страницах нет. `docs_click` пока 0._
- [x] `generate_lead` и `demo_click` отмечены как Key events (0.2)
- [x] Фильтр внутреннего трафика в GA4 в режиме Testing, визиты помечаются (0.3). _С 01.10 помечено 62 сессии Internal и 29 Developer, после 13.10 ни одной: скорее всего, Active с ~14.10, подтвердить._
- [ ] Clarity: IP blocking заполнен, интеграция с GA4 включена (0.3). _Подтверждения нет._
- [x] Тестовая заявка с UTM создаёт контакт с заполненными `utm_*` и `landing_page_first` (0.4). _15.10 тест Асель (`phase0-check`) и две реальные заявки с `utm_source=chatgpt.com`._
- [x] Сделки получают `original_traffic_source` (0.4). _423 из 424 сделок с 2024-09._
- [x] Popup не принимает gmail и требует Company и Job title (0.5)
- [ ] На всех FX-лендингах одна форма `FX | LP | Demo`; тестовая заявка с каждой страницы даёт контакт с `fx_vertical` и `generate_lead` с `fx_vertical` в GA4 (0.10). _Добавлено 19.10, начато: свойство `fx_vertical` есть, форма в работе._
- [ ] ~~Lead scoring создан, порог MQL = 30 (0.5)~~ _Снято 13.10._
- [x] Первый еженедельный отчёт пришёл в Telegram (0.6); трекинг позиций запущен (0.7). _16.10: таблица на весь сайт, отчёт за неделю 5–11.10 отправлен, cron вт/ср._

## Через 14 дней после приёмки

**Что проверю я**
- Сверю число `generate_lead` в GA4 с числом созданных контактов по каждой форме. Расхождение больше 20% значит, что какая-то форма не отслеживается.
- Сравню со снимком «до» (0-C): JS-ошибки, key events в неделю, доля контактов с UTM.

**Что делаешь ты**
- Переключи фильтр внутреннего трафика GA4 в **Active**, если не сделал на день 8.

После этого фаза 0 закрыта, и можно запускать фазу 1: `/fitxpress/`, вертикали, перелинковку.
