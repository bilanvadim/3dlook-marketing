---
product: fitxpress
type: tech-spec
date: 2026-09-27
owner: девелопер сайта 3dlook.ai (WordPress, Elementor, Yoast, WP Rocket)
related: 2026-09-25-fitxpress-seo-plan.md (фазы 0 и 2), 2026-09-27-tz-tracking-hubspot-ga4.md
---

# ТЗ девелоперу: правки на 3dlook.ai

Все пункты проверены на живом сайте 2026-09-25…27.

**Порядок работы:**
- **P0** — сделать на этой неделе, это прямые потери лидов или юридический риск.
- **P1** — в течение 2–3 недель.
- **P2** — по мере возможности.

**Иерархия утверждена 2026-09-27:** `/fitxpress/` — страница продукта FitXpress, вертикали `/fitxpress/for-{vertical}/`, главная — общая страница продуктов 3DLOOK. Пункты, помеченные «**с релизом /fitxpress/**», делаются в момент запуска этой страницы, не раньше.

---

## P0-1. `/pricing/` и `/contact-us/`: JS-ошибки и мёртвые клики

**Проблема (Microsoft Clarity, 72 часа):**

| Страница | JS-ошибки | Прочее |
|---|---|---|
| `/pricing/` | 21% сессий, на мобильных 27% | Мёртвые клики в 10% сессий, больше всех на сайте |
| `/contact-us/` | 31% сессий, на десктопе 42% | — |

Это две страницы, через которые приходит большая часть сделок.

**Сделать:**
1. В Clarity → Dashboard → «JavaScript errors» взять тексты ошибок. В Recordings отфильтровать по `/pricing/` и `/contact-us/` + «JS errors» и воспроизвести.
2. В Clarity → Heatmaps → `/pricing/` → слой «Dead clicks»: найти элементы, которые выглядят кликабельными, но не реагируют, и починить или убрать.
3. Исправить ошибки. Вероятные источники: скрипты Elementor-попапов, встраивание HubSpot-форм, конфликт с WP Rocket (отложенная загрузка JS).

**Приёмка:** через неделю после выката в Clarity доля сессий с JS-ошибками на обеих страницах меньше 3%, мёртвые клики на `/pricing/` меньше 3%. Тестовая отправка каждой формы на обеих страницах проходит на десктопе и на мобильном.

## P0-2. ~~Кнопки demo — обычные ссылки~~ — снят 2026-10-08

Девелопер ответил, что кнопки уже сделаны ссылками. Это подтвердилось на живом HTML 2026-10-08. На главной, `/pricing/`, `/for-bmi-verification/` и `/fitxpress/for-connected-and-digital-fitness/` каждая demo-кнопка — `<a href="#bd-modal…">` (попап remodal) со своим классом: `bd-hero__btn`, `u-hero__link`, `u-features__link`. На `/pricing/` у кнопок есть ещё `data-event-name`. Кнопки «Let's talk» в шапке и «Book a Demo» в футере ведут на `/contact-us/`. Кнопок на `onclick` нет. Посылка пункта («сделаны через JS») не подтвердилась.

Девелоперу здесь делать нечего. `demo_click` настраивается в GTM по Click URL (`#bd-modal`), см. runbook 0.2.

## P0-3. Compliance: убрать неверные утверждения со всех страниц

**Проблема:** на главной (и, видимо, в общем блоке на других страницах) есть блок, который противоречит нашему опубликованному trust-FAQ. Это юридический риск.

| Сейчас на сайте | Статус |
|---|---|
| Заголовок «GDPR & HIPAA Compliant» | запрещено |
| «FitXpress maintains HIPAA compliance and follows GDPR principles…» | запрещено |
| «…never link photos to personal identifiers…» | запрещено |
| «3DLOOK does not process personal identifiers or contact details that could link photos to specific individuals.» | запрещено |
| Бейдж-картинка «HIPAA Compliant» (alt «White logo with a caduceus symbol next to the text "HIPAA Compliant"…») | убрать бейдж |

**Заменить на** (текст дословно, это утверждённые формулировки из FAQ):

> **Security and compliance at the core**
>
> FitXpress can support HIPAA-governed deployments where 3DLOOK acts as a business associate under an executed BAA, where applicable. In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR.
>
> Scan records are associated with anonymized, randomly generated IDs, and 3DLOOK cannot identify a specific individual from the stored data. Photos are deleted immediately after processing or within 30 days, per the customer's instructions, and face obfuscation is applied at capture. Data is encrypted in transit with TLS and at rest in Amazon S3 with server-side encryption.
>
> [Read the Data, Privacy, Security & Regulatory FAQ →](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/)

- Заголовок бейджей вместо «GDPR & HIPAA Compliant»: «Privacy & Security».
- Бейджи оставить: GDPR (как регламент, без слова «compliant»), SSL. Бейдж HIPAA убрать совсем.

**Приёмка:** поиск по исходнику всех страниц (или по экспорту БД) не находит `HIPAA Compliant`, `HIPAA compliance`, `personal identifiers`. Проверить также футер, попапы и шаблоны Elementor (Global widgets).

## P0-4. GPTBot получает 403

**Проблема:** `curl -A "GPTBot" https://3dlook.ai/` возвращает **403**, хотя robots.txt его разрешает. Решение Вадима — пускаем.

**Сделать:** найти, где рождается 403. Проверить по порядку:
1. Cloudflare → Security → Bots → «Block AI bots» / Bot Fight Mode / WAF custom rules;
2. Wordfence или другой security-плагин (правила по User-Agent);
3. WAF хостинга.

Разрешить User-Agent `GPTBot`. Остальных ботов (OAI-SearchBot, ChatGPT-User, ClaudeBot, PerplexityBot, Google-Extended) не трогать: они уже получают 200.

**Приёмка:** `curl -s -o /dev/null -w "%{http_code}" -A "GPTBot" https://3dlook.ai/` → `200`.

## P0-5. Редиректы и 404

| URL | Сейчас | Нужно |
|---|---|---|
| `https://3dlook.ai/contact/` | 404 (111 заходов за 90 дней) | 301 → `/contact-us/` |
| `http://www.3dlook.ai/` | 404 | 301 → `https://3dlook.ai/` (и все пути `www` → без `www`) |
| `https://3dlook.ai/blog/` | два редиректа через `3dlook.me` | один 301 → `/content-hub/` |
| `https://3dlook.ai/fitxpress` (без слеша) | 301 → блог-пост `fitxpress-admin-panel-launch` | **с релизом /fitxpress/**: 301 → `/fitxpress/` (до релиза — временно на `/`) |

**Приёмка:** `curl -sI` по каждому URL показывает один 301 на целевой адрес с кодом 200.

---

## P1-1. robots.txt

**Проблема:** плагин Virtual Robots.txt собрал файл так, что все `Disallow` оказались внутри последней группы `User-agent: anthropic-ai`. Для Googlebot (группа `*`) нет ни одного запрета: поиск по сайту (`/?s=`), `/author/`, UTM-дубли открыты для сканирования.

**Заменить содержимое целиком на:**

```
User-agent: *
Disallow: /cgi-bin
Disallow: /?s=
Disallow: /*?s=
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
Disallow: /wp/
Disallow: /users/
Disallow: */trackback
Disallow: */embed
Disallow: /xmlrpc.php
Disallow: /*utm_
Disallow: /*openstat=
Allow: /wp-content/uploads/

Sitemap: https://3dlook.ai/sitemap_index.xml
```

**Примечания:**
- Отдельные группы для OAI-SearchBot, GPTBot, Google-Extended, ClaudeBot и anthropic-ai больше не нужны: группа `*` распространяется на них. Если отдельная группа есть, бот читает **только её**, поэтому старые группы с одним `Allow: /` и создавали проблему.
- `/author/` сейчас не закрываем: по плану (P1-4) там появятся страницы авторов.
- Строку `Disallow: /?` из старого файла не переносим: она закрывала бы любые URL с параметрами на главной.

**Приёмка:** Search Console → Settings → robots.txt показывает новую версию без ошибок. URL `https://3dlook.ai/?s=test` в тесте robots.txt — «Blocked».

## P1-2. FAQ-schema на trust-FAQ невалидна

**Проблема:** на `/content-hub/fitxpress-data-privacy-security-regulatory-faq/` WordPress (`wpautop`) вставляет `<br />` внутрь JSON-LD FAQPage. Разметка ломается, rich result не показывается.

**Сделать:** вывести JSON-LD так, чтобы его не трогал `wpautop`: через Yoast FAQ-блок, через Custom HTML-блок с отключённым autop или хуком в `wp_head`. Проверить все страницы с FAQPage.

**Приёмка:** [Rich Results Test](https://search.google.com/test/rich-results) по странице — «FAQ: valid items detected», 0 ошибок.

## P1-3. Alt-тексты логотипов на главной

**Проблема:** alt-тексты сгенерированы ИИ и описывают не то:

| Сейчас | Нужно |
|---|---|
| «The logo showcases "Reddit" in stylized white text…» | название реального клиента, например `Healthyr logo` (сверить по картинке) |
| «Logo featuring the text "vevo"…» | `<реальное название> logo` |
| «…the Gartner logo…, hinting at the future collaboration with New 2025 Home» | `Gartner logo` |
| «GDPR logo… next to the white IBM logo» | `GDPR` |
| «GDRP logo» (опечатка) | `GDPR` |

**Сделать:** пройти все логотипы в медиатеке, которые используются на главной и страницах FitXpress. Alt = «<Компания> logo», без описаний. Раньше в аудите встречалось и «Dannebrog flag, perfect for home decor» — найти и исправить тоже.

## P1-4. Авторы и schema автора

**Проблема:** страниц авторов нет (`/author/...` → 404). В schema статей автор указан как «admin» (32 поста), как сырой email сотрудника (13 постов) и как чужой gmail (1 пост).

**Сделать:**
1. Включить author archives в Yoast (Search Appearance → Archives → Author archives: enabled, indexable).
2. Создать или привести в порядок профили WP-пользователей: Assel Sekerova (основной автор health-статей) и остальные реальные авторы. Display name — имя и фамилия, био (Вадим пришлёт тексты), фото.
3. Переназначить посты с «admin», email- и gmail-авторами на реальных авторов. Список постов — в `data/onsite-findings.md`.

**Приёмка:** в schema `Person.name` на любом посте — имя человека. `/author/<slug>/` отдаёт 200.

## P1-5. Breadcrumb на fitness-странице

**Проблема:** на `/fitxpress/for-connected-and-digital-fitness/` breadcrumb ведёт на `?page_id=36425` (404).

**Сделать** (**с релизом /fitxpress/**): breadcrumb Home → FitXpress (`/fitxpress/`) → текущая страница. До релиза временно убрать средний уровень, чтобы не вести на 404.

## P1-6. `/content-hub/`: пагинация и фильтры

**Проблема:** `/content-hub/` показывает 10 постов, ссылки на страницу 2 нет, фильтры тем не являются ссылками. 60 из 160 постов доступны только со страницы `/sitemap/`.

**Сделать:**
- Пагинация обычными ссылками (`/content-hub/page/2/` …).
- Фильтры тем — ссылки на страницы категорий (`/content-hub/category/<slug>/` или как настроено), а не JS-переключатели.

**Приёмка:** из `/content-hub/` по ссылкам (без JS) можно дойти до любого поста.

## P1-7. `llms.txt`

Текст готов: `2026-09-27-llms.txt` в этой папке. Выкладывать **с релизом /fitxpress/**, потому что в нём уже новая структура. Девелоперу — только заменить `https://3dlook.ai/llms.txt`.

---

## P2-1. Скорость

**Сейчас:** TTFB ~0,7 с, HTML ~320 КБ без сжатия.

**Сделать** (WP Rocket и Elementor):
- critical CSS;
- убрать неиспользуемые виджеты и глобальные скрипты Elementor на страницах, где они не нужны;
- проверить, что HTML-кеш реально отдаётся (заголовки);
- сжатие Brotli/Gzip.

**Цель:** TTFB меньше 0,4 с, LCP на мобильном меньше 2,5 с (PageSpeed Insights для главной, `/pricing/` и одной статьи).

**Важно:** после любых изменений WP Rocket перепроверить P0-1 — отложенная загрузка JS может снова сломать формы.

## P2-2. Мобильные JS-ошибки по сайту

**Сейчас:** 12% мобильных сессий с JS-ошибками против 8% на десктопе.

**Сделать:** после P0-1 пройтись по топ-ошибкам Clarity (фильтр Device = Mobile) по всему сайту.

---

## Релиз /fitxpress/ (иерархия утверждена 2026-09-27)

- `/fitxpress/`: снять 301 на `/`, опубликовать страницу (текст готовим через `page-builder`).
- Страницы вертикалей: переезд с 301 в момент пересборки (список — в плане, п. 1.2).
- Меню, футер, внутренние ссылки «FitXpress» → на `/fitxpress/`.
- Новая главная (текст готовим мы).
- Обновить sitemap и `llms.txt`, затем в Search Console нажать «Request indexing» для `/fitxpress/` и новых страниц.
