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

> **Проверка 2026-10-14: пункт заменён на `2026-10-14-p0-1-ticket-v2.md`.** Гипотезы ниже не подтвердились. 446 из 519 JS-ошибок сайта (7–13 окт.) даёт cookie-баннер WebToffee: плагин **Flying Scripts** (не WP Rocket, его Delay JS выключен) запускает конфиг и скрипты баннера в случайном порядке. Ещё 37 ошибок даёт GTM-тег HubSpot chat tracker (`JSON.parse` без проверки). Elementor-попапов на этих страницах нет (remodal), HubSpot-формы грузятся нормально, jQuery один. Доказательства: `data/2026-10-14-p0-1-*.md`.

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

> **2026-10-19:** бейдж «HIPAA Compliant» в футере остаётся на всех страницах (решение Вадима), из задачи убран. Остальное в силе.

**Проблема:** на главной (и, видимо, в общем блоке на других страницах) есть блок, который противоречит нашему опубликованному trust-FAQ. Это юридический риск.

| Сейчас на сайте | Статус |
|---|---|
| Заголовок «GDPR & HIPAA Compliant» | запрещено |
| «FitXpress maintains HIPAA compliance and follows GDPR principles…» | запрещено |
| «…never link photos to personal identifiers…» | запрещено |
| «3DLOOK does not process personal identifiers or contact details that could link photos to specific individuals.» | запрещено |
| «FitXpress maintains HIPAA compliance and adheres to GDPR principles…» (FAQ на `/pricing/`) | запрещено |
| Бейдж-картинка «HIPAA Compliant» в футере | **оставить**, не трогать |

**Заменить на** (текст дословно, это утверждённые формулировки из FAQ):

> **Security and compliance at the core**
>
> FitXpress can support HIPAA-governed deployments where 3DLOOK acts as a business associate under an executed BAA, where applicable. In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR.
>
> Scan records are associated with anonymized, randomly generated IDs, and 3DLOOK cannot identify a specific individual from the stored data. Photos are deleted immediately after processing or within 30 days, per the customer's instructions, and face obfuscation is applied at capture. Data is encrypted in transit with TLS and at rest in Amazon S3 with server-side encryption.
>
> [Read the Data, Privacy, Security & Regulatory FAQ →](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/)

- Заголовок блока на главной вместо «GDPR & HIPAA Compliant»: «Privacy & Security».
- Футер не трогать: бейджи там остаются как есть, включая «HIPAA Compliant».

**Приёмка:** поиск по исходнику всех страниц (или по экспорту БД) не находит `GDPR & HIPAA Compliant`, `HIPAA compliance`, `personal identifiers`. Бейдж в футере (картинка и её alt «HIPAA Compliant») остаётся. Проверить также попапы и шаблоны Elementor (Global widgets).

## P0-4. GPTBot получает 403

> **Перепроверено 2026-10-14: задача актуальна, инструкция исправлена** (отправлено Асель в Slack). 403 по-прежнему отдаётся на любой User-Agent с «GPTBot» без учёта регистра, в том числе на `/robots.txt`. Ответ — стандартная страница nginx (146 байт), то есть блок срабатывает до WordPress. Обновлённый robots.txt (одна группа `User-agent: *`) GPTBot разрешает и на 403 не влияет. OAI-SearchBot, ChatGPT-User, ClaudeBot, PerplexityBot, Googlebot, CCBot и Bytespider получают 200. **Cloudflare нет** (DNS на GoDaddy `domaincontrol.com`, сервер AWS 52.89.180.242, без `cf-ray`), Wordfence ни при чём. Искать правило в конфиге nginx (`grep -rni gptbot /etc/nginx/`: server-блок, include, списки bad bots) или в настройке блокировки ботов в панели хостинга. Google-Extended — токен robots.txt, а не User-Agent, curl'ом не проверяется. Приёмка: полный UA `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.2; +https://openai.com/gptbot` → 200 на `/` и на `/robots.txt`. Пункты 1–2 ниже (Cloudflare, Wordfence) не актуальны.

**Проблема:** `curl -A "GPTBot" https://3dlook.ai/` возвращает **403**, хотя robots.txt его разрешает. Решение Вадима — пускаем.

**Сделать:** найти, где рождается 403. Проверить по порядку:
1. Cloudflare → Security → Bots → «Block AI bots» / Bot Fight Mode / WAF custom rules;
2. Wordfence или другой security-плагин (правила по User-Agent);
3. WAF хостинга.

Разрешить User-Agent `GPTBot`. Остальных ботов (OAI-SearchBot, ChatGPT-User, ClaudeBot, PerplexityBot, Google-Extended) не трогать: они уже получают 200.

**Приёмка:** `curl -s -o /dev/null -w "%{http_code}" -A "GPTBot" https://3dlook.ai/` → `200`.

**В тот же заход в конфиге nginx:** включить HTTP/2 (P2-1, п. 1).

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

## P1-2. ~~FAQ-schema на trust-FAQ невалидна~~ — передан маркетингу 2026-10-28

**Проблема (перепроверено 2026-10-28):** на `/content-hub/fitxpress-data-privacy-security-regulatory-faq/` JSON-LD FAQPage стоит в классическом блоке статьи, WordPress вставляет в него `<br />`, и JSON не парсится. На `/content-hub/fitxpress-capture-quality-user-experience-faq/` FAQPage нет вовсе.

**Что изменилось:** Google с 7 мая 2026 не показывает FAQ rich results ни одному сайту, а 15 июня снял документацию ([changelog](https://developers.google.com/search/updates#removing-faq-rich-result)). FAQPage оставляем как корректную разметку для Bing и ИИ-ассистентов, но сниппет больше не цель, и Rich Results Test для приёмки не годится.

**Сделать (маркетинг, Асель; девелопер не нужен):** в обеих статьях JSON-LD вставить блоком «Custom HTML», в нём WordPress не ставит `<br />`. В trust-FAQ текущий блок с кодом заменить на Custom HTML. Готовые блоки отправлены Асель в Slack 28.10:
- `trust-faq-faqpage-custom-html.txt` — прежний JSON без `<br />`, 14 вопросов, совпадают с H3;
- `capture-quality-faq-faqpage-custom-html.txt` — новый, 13 вопросов по живому тексту статьи.

У обоих `@id` = адрес страницы + `#faq` и `isPartOf` → страница, чтобы FAQ был связан с графом Yoast. Если текст ответов в статье поменяется, JSON пересобрать.

Блок FAQ Yoast в FAQ-статьях не используем: он видимый и продублировал бы вопросы, которые уже стоят в теле статьи как H3. В обычных статьях с коротким FAQ внизу блок Yoast — правильный вариант (так сделаны wellness-hub, occ-health, remote-measurement).

Отдельный schema-плагин (Schema Pro, Schema App, Rank Math Pro) не берём, разобрано 28.10: P1-2 — баг блока, P1-4 — данные пользователей, а ручная разметка лендингов уже работает. `@id` сущностей берутся из файла сущностей Асель (копия: `docs/schema-entities.csv`).

**Приёмка:** в исходном коде обеих страниц внутри `<script type="application/ld+json">` нет `<br />`; [validator.schema.org](https://validator.schema.org/) — 0 ошибок, FAQPage с 14 и 13 вопросами. Если `<br />` всё же появится, тогда к девелоперу: вывод через `wp_head`.

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

> **Перепроверено 2026-10-19, задача переписана** (отправлено Асель в Slack). Асель спросила, нужны ли архивы авторов, если Yoast предупреждает о дублях. Нужны. Предупреждение касается блогов, у которых лента постов стоит на главной, а у нас главная продуктовая, статьи живут в `/content-hub/`. Авторов у сайта несколько, и страница автора показывает только его статьи. Без неё у `Person` в schema нет `url`. Новое в задаче: порядок шагов, slug пользователей, подпись в статьях отдельно от пользователя WordPress, фото в schema.

**Проблема:**
- Страниц авторов нет: `/author/...` → 404. Ни у одного `Person` в schema нет `url`.
- Автор в schema статей — «admin» (32 поста), сырой email сотрудника (13 постов), чужой gmail (1 пост), «Nadya» без фамилии (13 постов).
- Подпись «By …» и фото в статье берутся не из пользователя WordPress, а из отдельного поля темы. Поэтому на странице «By Oleksii Kaplanskyi» с фото, а в schema того же поста — его email. У Асель на странице «Assel Sekerova», а в schema «Asselya Sekerova».
- Фото в schema у всех авторов — серая заглушка Gravatar (`d=mm`).

**Сделать — строго по порядку.** Если включить архивы до шагов 1–3, в индекс и в `author-sitemap.xml` уйдут `/author/admin/` и адреса, собранные из email.

1. **Посты.** Переназначить посты с «admin», email- и gmail-авторами на реальных авторов: Записи → клик по имени автора в списке → выбрать все → Bulk Edit → Author. Кому отдать посты с неизвестным автором, маркетинг решает до начала работ. Человека не подписываем под текстом, который он не писал и не вычитывал.
2. **Профили** (Users → Profile) каждого автора с постами:
   - First name, Last name и «Display name publicly as» — имя и фамилия, в том же написании, что в подписи статей и в LinkedIn. Для Асель выбрать одно: Assel или Asselya. Nadya — дописать фамилию.
   - Biographical Info — био (тексты пришлёт Вадим). В schema уходят первые 250 символов, главное — в начало.
   - LinkedIn — в поле LinkedIn профиля (его добавляет Yoast). Оттуда он попадает в `sameAs`.
   - Фото. Yoast берёт аватар WordPress, то есть Gravatar. Поставить плагин локальных аватаров (например, Simple Local Avatars) и загрузить те же фото, что в подписи статей.
   - Slug (`user_nicename`) — имя и фамилия латиницей: `assel-sekerova`. Из админки он не меняется: `wp user update <ID> --user_nicename=assel-sekerova` или плагин Edit Author Slug. Slug не должен совпадать с логином и не должен быть собран из email.
   - Учётке `admin` тоже сменить slug. WordPress открывает страницу автора и без постов, и логин оказался бы в URL.
3. **Подпись в статьях.** Шаблон темы должен брать имя, фото и био из автора поста (пользователя WordPress), а не из отдельного поля. Имя в подписи — ссылка на `/author/<slug>/`. Если оставить два источника, подпись и schema разойдутся при следующей правке.
4. **Включить архивы:** Yoast → Settings → Advanced → Author archives. Enable author archives — On, Show author archives in search results — On, Show archives for authors without posts in search results — Off.
5. **Страница автора.** Проверить `/author/assel-sekerova/`. Сейчас `/author/...` отдаёт 404, хотя Yoast при выключенных архивах делает редирект на главную. Значит, авторские URL, скорее всего, отключает тема или другой плагин. Если после шага 4 остаётся 404 — найти, что отключает. На странице: фото, имя, должность, био, LinkedIn и список статей автора. Если у темы нет `author.php`, сделать его (или шаблон архива автора в Elementor). Голый список заголовков не подходит.

**Приёмка:**
- На любом посте `Person.name` в schema — имя и фамилия человека: не «admin», не email, не одно имя.
- `Person.url` = `https://3dlook.ai/author/<slug>/`. У авторов с LinkedIn есть `sameAs`, в `image` — реальное фото, а не заглушка `d=mm`.
- Имя в подписи «By …» совпадает с `Person.name` и ведёт на страницу автора.
- `/author/<slug>/` каждого автора с постами отдаёт 200 и есть в `author-sitemap.xml`. `/author/admin/` в sitemap нет.
- [Rich Results Test](https://search.google.com/test/rich-results) по двум-трём статьям — 0 ошибок.

**Schema aggregation endpoint** (Yoast → Settings → Site features → AI tools) включать после P1-4. Это не редактор разметки, а выдача уже готовой разметки Yoast одним фидом для ИИ-систем (`/wp-json/yoast/v1/schema-aggregator/...`). Разметку на страницах он не меняет. Каждый автор там собирается в один `Person` на весь сайт. До P1-4 туда ушёл бы email сотрудника как имя автора 13 статей.

## P1-5. Breadcrumb на fitness-странице

**Проблема:** на `/fitxpress/for-connected-and-digital-fitness/` breadcrumb ведёт на `?page_id=36425` (404).

**Сделать** (**с релизом /fitxpress/**): breadcrumb Home → FitXpress (`/fitxpress/`) → текущая страница. До релиза временно убрать средний уровень, чтобы не вести на 404.

**Вместе с пересборкой страницы (добавлено 2026-10-28):** сейчас на живой странице только граф Yoast, без `Service` и `FAQPage`. Полный граф ставится так же, как на insurance и wrist: JSON — из `workspace/pages/for-connected-and-digital-fitness/page-final-2026-10-07.html` (WebPage, Service, FAQPage, BreadcrumbList), `@id` сверить с `docs/schema-entities.csv`, Organization = `https://3dlook.ai/#organization`. Приёмка — validator.schema.org, 0 ошибок.

## P1-6. ~~`/content-hub/`: пагинация и фильтры~~ — снят 2026-10-19, перенесён в перелинковку (план, п. 1.5)

Перепроверено 2026-10-19 на живом сайте, в GSC и по свежему обходу всех URL из sitemap (отправлено Асель в Slack). В мае 2026 девелоперы на ту же просьбу ответили, что кнопку Show More оставили намеренно (так просил прошлый SEO), и вместо пагинации сделали HTML-карту `/sitemap/`. Она закрывает то, ради чего задумывалась пагинация:
- `/sitemap/` стоит в футере каждой страницы и ссылается на все посты.
- Из 60 постов, на которые ссылается только `/sitemap/`, 53 в индексе, и почти все Google переобходил в октябре. Вне индекса 7 fashion-новостей 2019–2020, их пагинация не вытащит.
- Фильтры на `/content-hub/` — типы материалов (All / Blog / Case Studies / eBooks / Webinars), а не темы. Ссылки на них дали бы почти тот же список (`/content-hub/category/blog/`).
- `/content-hub/page/2/` отдаёт 200 с теми же 10 постами, что и первая страница, и canonical на `/content-hub/`. Вреда нет.

Настоящая проблема другая: на эти 60 постов не ссылается ни одна статья, и с 2026-09-25 список не изменился. Среди них сильные по показам страницы (GSC, 18.07–16.10): `visible-abs-myths-…` 70,7 тыс. показов, `the-enormous-impact-of-daily-physiological-changes-…` 49,8 тыс., `3d-body-scanning` 14,3 тыс. (одна из упавших статей в плане восстановления). На 60 «сирот» приходится 27% показов всех постов. Ссылка со страницы, где 165 ссылок, передаёт мало, и седьмая страница пагинации передавала бы столько же. Нужны контекстные ссылки из хабов и близких статей. Это работа контента, девелоперу здесь делать нечего.

**Перелинковка (п. 1.5 плана):** по 2–3 контекстные ссылки из хабов и близких статей на каждый из 11 health/body-comp постов. Начать с `visible-abs-myths-…`, `the-enormous-impact-of-daily-physiological-changes-…`, `3d-body-scanning`, `body-fat-percentage-men-women-ai-3d-scanning-goals`, `fit3d-vs-3dlook`, `top-7-remote-body-composition-tools-glp-1-clinics`. Дальше `body-fat-percentage`, `top-health-tech-companies`, `3d-body-scanning-apps-market-analysis-…`, `body-composition-activities-…`, `breast-cancer-related-lymphedema-…`. Остальные 49 (fashion и новости) не трогаем.

**Приёмка:** на каждый из 11 постов есть хотя бы одна ссылка из текста статьи или хаба (не считая `/sitemap/` и виджета последних постов).

## P1-7. `llms.txt`

Текст готов: `2026-09-27-llms.txt` в этой папке. Выкладывать **с релизом /fitxpress/**, потому что в нём уже новая структура. Девелоперу — только заменить `https://3dlook.ai/llms.txt`.

---

## P2-1. Скорость

> **Перепроверено 2026-10-19, задача переписана** (отправлено Асель в Slack). Исходный диагноз неверен. TTFB 0,7 с — это расстояние от сервера, с которого мерили (Германия), до сервера сайта (AWS, Орегон): статичная картинка отдаётся с тем же TTFB 0,70 с, что и HTML, то есть страница отдаётся из кеша почти мгновенно. Gzip включён: главная весит 56 КБ при передаче, 320 КБ — это без сжатия. Elementor на этих страницах почти не используется, тема своя. Наш клиент приходит с десктопа: по FX- и health-страницам, `/pricing/` и `/contact-us/` десктопных показов в GSC втрое больше мобильных (18.07–16.10). Core Web Vitals в GSC на 19.10: десктоп — 95 URL Good, 15 Needs improvement, Poor нет; мобайл — 19 Poor, 91 Needs improvement. Отдельной задачи на скорость не ставим, мобайл отдельной целью тоже.

**Сделать:**
1. **Вместе с P0-4:** включить HTTP/2 в nginx (`listen 443 ssl http2;` или `http2 on;` для nginx 1.25.1+). Сейчас сайт отвечает только по HTTP/1.1, а на страницу идёт 35–54 запроса к `3dlook.ai`. Lighthouse (десктоп) оценивает выигрыш в 0,8–1 с на главной, `/pricing/` и статье.
2. **В приёмку редизайна `/pricing/`:** CLS на десктопе меньше 0,1. Сейчас 0,29 (Lighthouse, порог «плохо» 0,25): при загрузке прыгает блок `div.content-for_mt` (переключатель FX/MT).
3. **Бэклог, только после релиза и проверки P0-1:** в WP Rocket — Remove Unused CSS (или асинхронная загрузка CSS) и отложенный jQuery. Сейчас обе опции выключены. Отрисовку блокируют CSS темы (`main.min.css`, `custom.css`, `home-2025.css`), jQuery 3.6.0 и скрипты баннера WebToffee из P0-1, поэтому любая правка отложенной загрузки JS может снова сломать баннер и формы. Возвращаемся, если в отчёте GSC для десктопа появятся Poor или вырастет Needs improvement.

**Приёмка (п. 1):** `curl -sI --http2 https://3dlook.ai/` → `HTTP/2 200`.

**Важно:** после любых изменений WP Rocket перепроверить P0-1 — отложенная загрузка JS может снова сломать формы. На 2026-10-14 скрипты откладывает не WP Rocket, а плагин Flying Scripts; скрипты cookie-баннера WebToffee из него нужно исключить (см. `2026-10-14-p0-1-ticket-v2.md`).

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
