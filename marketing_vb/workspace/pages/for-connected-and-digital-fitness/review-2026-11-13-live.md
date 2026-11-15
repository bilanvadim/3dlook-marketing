---
product: fitxpress
type: live-review
vertical: connected-and-digital-fitness
url: https://3dlook.ai/digital-fitness/
compared_with: page-final-2026-10-07.html (Vadim's final) · Kristina's design review 2026-11-06 (Slack #marketing, thread 1793887681.946099) · Vadim's reply in that thread 11-06 («тільки фрази по точності або прайвесі краще не чіпати, а інше на розсуд твій»; «клієнтів давай усіх, лого… однакова стрічка у всіх юз кейсах»)
live_capture: published-live-2026-11-13.md
date: 2026-11-13
---

# Перевірка живої сторінки /digital-fitness/ (2026-11-13)

Перевірено: текст `<main>` проти фіналу 10-07, JSON-LD, `<head>`, редиректи, sitemap, llms.txt, GTM-контейнер
GTM-PW77M7K, форма, усі посилання тіла (28), рендер 1440×900 і 390×844, 197 URL сайту на посилання на стару адресу.

## Треба виправити

1. **GTM не знає нову адресу.** Таблиця `fx_vertical` (lookup за Page Path, без default) має
   `/fitxpress/for-connected-and-digital-fitness/ → fitness`, а рядка `/digital-fitness/` немає. Ліди з цієї
   сторінки йдуть у GA4 `generate_lead` і в приховане поле HubSpot-форми без `fx_vertical`. Фікс: рядок
   `/digital-fitness/ → fitness` (старий лишити) і Publish контейнера. Для root-URL страхової й BMI рядки є.

2. **Тексти точності й приватності не дослівні**, хоча 11-06 у треді Крістини саме їх ти просив не чіпати.
   По суті хибного нічого немає, але це погоджені формулювання. Замінити дослівно з фіналу 10-07:

   | Блок | Зараз на сайті | Має бути (фінал 10-07) |
   |---|---|---|
   | Лід Proof | For progress tracking, consistency matters. Repeated scans typically differ by less than 1 cm for most evaluated measurements, making it possible to track changes against each member's previous scans. | For progress tracking, repeatability is the figure that matters. For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm. The app compares each member with their own earlier scans, which makes repeatability more relevant here than absolute accuracy. |
   | Photos | Photos are deleted after processing or retained for up to 30 days under the customer's policy, with blurring and face obfuscation. | FitXpress deletes photos immediately after processing or retains them for up to 30 days under a customer-specific policy. Retained photos are blurred, and face obfuscation is applied during capture. |
   | Identifiers | Each scan uses a randomly generated, anonymized identifier instead of directly identifying the member whose body data is processed. | Scan records use anonymized, randomly generated identifiers. |
   | GDPR | In most enterprise deployments, the customer acts as data controller and 3DLOOK as data processor, depending on the processing arrangement. | In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR. |
   | Encryption | Data is encrypted both during transmission and while stored, helping protect member information throughout processing and storage. | Data is encrypted in transit and at rest. |
   | Training | Production customer data is not used for model training unless the customer provides explicit, documented authorization for that purpose. | 3DLOOK does not use production customer data to train its models without the customer's explicit, documented authorization. |

   Найважливіші: лід Proof (результат дослідження «showed» став загальною обіцянкою «typically differ»), GDPR
   (канонічна фраза, вже вказана в рев'ю 11-06) і Photos (з «with blurring and face obfuscation» не видно, що
   розмиваються лише збережені фото, а обличчя приховується ще при зйомці).

3. ~~**Стара сторінка досі опублікована у WordPress.**~~ **Зроблено 11-13** (Вадим переніс у чернетки).
   Перевірено: `page-sitemap.xml` має 32 адреси, стара зникла, нова є; стара адреса віддає 301
   (`x-redirect-by: redirection`) на `/digital-fitness/` в один крок, нова 200.
   **Лишилось:** `llms.txt` рядок 30 досі веде на стару адресу. Файл ручний («Last updated: 2026-10-22»,
   last-modified 10-27), сам не оновиться. Замінити URL на `https://3dlook.ai/digital-fitness/` і дату.

4. **Внутрішні посилання на стару адресу** (працюють через 301, краще перелінкувати): див. розділ нижче.

## Рішення для Вадима

5. **URL `/digital-fitness/`.** Затверджена архітектура (10-22): use cases = `/fitxpress/for-{audience}/`,
   а стара адреса сторінки якраз і була цільовою. Страхову й BMI тримають у корені до запуску `/fitxpress/`
   (`/for-insurance-underwriting/`, `/for-bmi-verification/`), а ця пішла в корінь з іншим шаблоном слага
   (без `for-`). Коли `/fitxpress/` запуститься, сторінку повертатимуть на `/fitxpress/for-connected-and-digital-fitness/`.
   Тоді нинішнє правило 301 «стара → нова» треба видалити, інакше буде петля. Питання: адресу з тобою
   погоджували, і вона остаточна до запуску `/fitxpress/`?

   **Відповідь Вадима 11-15:** фінальна адреса `/fitxpress/for-…`, `/digital-fitness/` тимчасова; реліз нової головної й
   `/fitxpress/` ≈ за 2 тижні. Порада: повернути сторінку на стару адресу (= фінальну) одразу, не чекати релізу:
   GTM-рядок, 18 посилань і llms.txt тоді правильні без правок. Порядок: стару чернетку в кошик або інший slug
   (інакше WP дасть `-2`) → видалити 301 стара → нова → сторінці 45555 батька й slug старої → 301
   `/digital-fitness/` → стара (для сторінок WP сам не редиректить) → кеш → перевірка.

## Варто виправити

6. **Логотипи.** Стрічка та сама, що на страховій (як ти просив 11-06), але Zing Coach і Verv (клієнти,
   твоє рішення 10-07) у неї не потрапили. Тоді це не «усі клієнти», а підпис «including fitness teams»
   тримається лише на Erakulis. Додати обидва в спільну стрічку, і вони з'являться на всіх use cases.
   Лого Warrior Consultants досі виглядає як набраний текст.
7. **Картки For Members: опис лише по ховеру** (opacity 0). На десктопі видно тільки заголовки, на телефоні
   описів не видно взагалі, бо ховера немає. Це пункт із рев'ю 11-06.
8. **Таблиця порівняння на мобільному** скролиться вбік (917 px у в'юпорті 390): спочатку видно лише колонку
   FitXpress. У фіналі для екранів < 960 px були картки.
9. **Meta description 167 символів** (обріжеться ~на 155). **og:image** загальний `2024/12/fitxpress.jpg`; стара
   сторінка мала фітнесовий `fitxpress-for-connected-fitness.jpg`.

## Дрібниці (на розсуд дизайнера, не обов'язково)

- Стрічка hero «45sec from scan to results»: загубилось «under» (у ліді та в каноні «under 45 seconds») і пробіл.
- Мокап у hero: Body fat 27 %, lean mass 99.1 lb, weight 143 lb не сходяться (27 % від 143 lb → lean ≈ 104 lb).
- Problem: випало речення-міст «By day 30… members who track only a weight line that barely moves have little
  evidence that the program works». Без нього цифри відтоку не пов'язані з продуктом.
- FAQ: два заголовки поспіль («Frequently asked questions» + «General Questions»).
- `ResizeObserver loop` дає ~30 `gtm.pageError` за перегляд. Це безпечно: GA4-тегу на ці помилки немає.

## Що збігається з фіналом і рев'ю

H1, eyebrow, лід, value-картки, «FitXpress is not a medical device.», 70 % з «median» і «lack of personalization
was among the reasons», Starter/Pro $1,000/$1,500 і «API requests» (= живий /pricing/), Pro-фічі, таймстемпи
10:24:05 → 10:24:35 (30 с), кроки How it works (немає «applicant», крок 3 = телефон із прогресом), RTPV
«gives pose and framing guidance», Recommended setup, таблиця порівняння, картки 96-97 % / 1.5-2.0 cm і абзац
«These figures come from internal validation…» дослівно, посилання на trust FAQ і privacy@, пілот (cohort,
random, evaluate, метрики), 6 FAQ = фінал = JSON-LD FAQPage, спільна форма `11acb23a` з текстом фіналу
(«See FitXpress in the member flow»), canonical на себе, 301 зі старої адреси в один крок, http/www → 301,
усі внутрішні посилання 200, пункт меню Use Cases веде на нову адресу, `@id` у schema з entity inventory,
hero-картинки 38/45 KB, на 390 px сторінка без горизонтального скролу, «Book a Demo» на першому екрані мобільного.

З рев'ю Крістини 11-06 зроблено: Starter, коми в цінах, таймстемпи, стани кроків 2-3, підпис лого, заливка
карток Proof, світліший дрібний синій, рядок medical device, median, регістр заголовків, дата Last updated.
Не зроблено: дослівні тексти приватності й точності (п. 2), Zing/Verv (п. 6), картки по ховеру (п. 7),
White-label і «Under» у стрічці, два заголовки FAQ. Решту ти лишив на її розсуд.

## Внутрішні посилання на стару адресу

Обхід 197 URL з `post-sitemap.xml` + `page-sitemap.xml`: 9 сторінок, 18 посилань на
`/fitxpress/for-connected-and-digital-fitness/` (працюють через 301; меню Use Cases уже веде на нову адресу).

| Посилань | Сторінка |
|---|---|
| 5 | /content-hub/glp-1-muscle-loss-fitness-apps/ |
| 3 | /content-hub/remote-body-measurement-online-fitness-coaching/ |
| 3 | /content-hub/connected-fitness-industry/ |
| 2 | /content-hub/top-fitness-industry-trends/ |
| 1 | /content-hub/ai-in-fitness-industry/ (хаб-стаття сторінки) |
| 1 | /content-hub/ai-body-data-wellness-platforms/ |
| 1 | /content-hub/ai-body-data-health-hub/ |
| 1 | /about-us/ |
| 1 | /sitemap/ (HTML-карта сайту) |

Поза сайтом: `llms.txt` рядок 30. У репо стару адресу ще несуть `landing-map.md` і site-inventory; оновити,
коли ти підтвердиш, що `/digital-fitness/` остаточна (п. 5).

## Відправлено

2026-11-15: Асель у Slack DM, російською (адреса + кроки, 6 дослівних текстів, решта, чекліст на реліз):
https://3dlook.slack.com/archives/D0A1Q2E02P3/p1794736650307869
2026-11-15, пізніше: на прохання Вадима з повідомлення прибрано тексти приватності й дизайн-пункти (лого, картки, таблиця). Лишились адреса, meta/og:image, чекліст на реліз.
