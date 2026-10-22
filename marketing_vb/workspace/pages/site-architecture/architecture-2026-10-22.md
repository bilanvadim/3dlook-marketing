---
product: all
type: site-architecture
status: v1 approved by Vadim 2026-10-22 («ок»)
date: 2026-10-22
files: nav-prototype-2026-10-22.html (прототип меню, перемикач 3 / 5 / 8 продуктів) · research-navigation-2026-10-22.md · screenshot-*.jpeg
related: ../homepage/spec-2026-10-21.md (реєстр продуктів), .claude/skills/page-builder/references/site-inventory.md
---

# Структура сайту 3dlook.ai і меню: рекомендація

## Коротко

- **У шапці 5 пунктів, і їх стільки ж лишається при будь-якій кількості продуктів:** `Products · Industries · Pricing · Resources · Company`. Праворуч одна кнопка `Book a demo`. Входу в шапці немає (рішення 10-22): вхід у Mobile Tailor живе у футері й на сторінці продукту. Нові продукти змінюють лише вміст двох мега-меню.
- **Два виміри, кожен пункт один раз.** Products відповідає на питання «що», Industries — «для кого». Сторінки use case показуються тільки в Industries, продукти тільки в Products.
- **Меню будується з того самого реєстру продуктів, що й головна.** До 6 продуктів це сітка карток, з 7-го — колонки за сімействами (Body · Hand and wrist · Head). Прототип показує це перемикачем 3 / 5 / 8.
- **URL не міняємо заради SEO.** Google визначає структуру сайту за посиланнями, а не за папками. Продукти лишаються в корені (`/fitxpress/`, `/mobile-tailor/`, `/wrist-measurement/`), use cases — `/{product}/for-{audience}/`. Переїжджає лише те, що вже вирішено з релізом `/fitxpress/`.
- **Сьогоднішня шапка ламає три правила:** осі змішані, 4 верхні пункти ведуть на `#` (Clarity бачить на них «мертві» кліки), а вхід є тільки для Mobile Tailor, ще й захований у меню «Made-to-Measure».

---

## 1. Дані

**Сайт:** 32 сторінки (page-sitemap) і 162 статті (post-sitemap), знято 22.10.

**Куди люди переходять зсередини сайту** (GA4, 22.07–21.10; «через сайт» = перегляди мінус сесії, що почалися на цій сторінці):

| Сторінка | Перегляди | Через сайт | Що це означає для меню |
|---|---|---|---|
| `/pricing/` | 5 064 | 2 791 (55%) | Найпопулярніша ціль навігації: окремий пункт у шапці |
| `/mobile-tailor/` | 6 910 | 1 787 (26%) | Продукт, який шукають: перший рівень у Products |
| `/` | 15 432 | 1 803 (12%) | — |
| `/wrist-measurement/` | 1 329 | 799 (60%) | Wrist знаходять через меню, хоча він стоїть серед «Use Cases» |
| `/technology/` | 1 349 | 680 (50%) | Помітно, але не на рівні Pricing: перший рядок у Products |
| `/contact-us/` | 1 118 | 550 (49%) | Покриває кнопка `Book a demo` і Company |
| telehealth-сторінка | 764 | 496 (65%) | Industries |
| `/mobile-tailor/for-made-to-measure/` | 1 030 | 411 (40%) | Industries |
| `/about-us/` | 900 | 408 (45%) | Company лишається в шапці |
| `/case-studies/` | 328 | 210 (64%) | Resources |
| `/careers/` | 1 124 | 222 (20%) | Здебільшого прямий трафік: Company і футер |
| `/partners/` | 188 | 116 (62%) | Company |

**Сьогоднішня шапка:** `Use Cases ▾` (telehealth, fitness, BMI, insurance, **Wrist**) · `Made-to-Measure ▾` (Mobile Tailor, MT pricing, 3 use cases, **Sign In**) · `Pricing` · `Technology` · `Resources ▾` (Case Studies, Content Hub, **Terms & Policies**, промо Safariland) · `About 3DLOOK ▾` (About, Partners, Careers, Contact, промо Digiday) · `Let's talk`.
- «Use Cases» — це лише FitXpress плюс продукт Wrist. «Made-to-Measure» — це насправді продукт Mobile Tailor, підписаний назвою галузі.
- Wrist як продукт стоїть серед use cases, а FitXpress як продукту в меню немає взагалі (`/fitxpress/` поки редиректить на головну).
- 4 верхні пункти мають `href="#"` (ранбук 0.1: «В шапке по-прежнему 4 пункта с href="#"»).

---

## 2. Що роблять інші

Повний розбір: `research-navigation-2026-10-22.md` (15 сайтів: Stripe, Twilio, Datadog, Veriff, Persona, Yoti, Mitek, Perfect Corp, Banuba, NuraLogix, Styku, Size Stream, Prism, Bodygram, Fit3D).

| Що бачимо | У кого | Що беремо |
|---|---|---|
| 5 пунктів у шапці — найчастіше | Stripe, Twilio, Veriff, Yoti, Mitek | 5 пунктів |
| Продукти + окреме меню галузей, коли продуктів 3+ | Stripe, Twilio, Veriff, Mitek, Datadog | Products + Industries |
| Оглядовий пункт першим у меню продуктів | «Twilio Platform», Persona «Platform», Size Stream «Overview» | Technology першим рядком у Products |
| Колонки сімейств і бейдж «New» для нових продуктів | Stripe, Veriff, Mitek, Twilio | Сімейства з 7-го продукту, бейдж New |
| Вибір входу, коли застосунків кілька | Twilio («Or log in to access…»), Yoti («Business login») | Не беремо: публічний вхід є лише в Mobile Tailor, і з сайту ним не користуються (див. §4a) |
| Одна головна CTA | усі | `Book a demo` |
| Developers у шапці лише в API-first компаній з відкритим самообслуговуванням | Stripe, Prism | У нас доступ через демо і NDA, тож Developers іде в Resources |

**Антипатерни, яких уникаємо:** окремий пункт шапки на кожен продукт (Banuba), «Products» → `#` без огляду (NuraLogix), меню-смітник «More» з захованим входом (Styku), вхід лише у футері (Bodygram), той самий пункт у кількох місцях (Datadog, Perfect Corp), два меню, що обидва відповідають «для кого» (Size Stream: Solutions + Industries), гамбургер на десктопі (Perfect Corp), меню, яких немає в серверному HTML (Persona).

---

## 3. Принципи

1. **Шапка не росте з продуктами.** 5 пунктів; новий продукт змінює вміст Products і Industries.
2. **Кожен пункт один раз** (NN/g). Продукт — у Products, сторінка use case — в Industries, точність і приватність — у нижньому рядку Products, контент — у Resources.
3. **Одне джерело.** Меню, футер, мобільне меню, головна, опції форми і `llms.txt` беруть продукти з реєстру (`../homepage/spec-2026-10-21.md` §3).
4. **Назви — звичайні слова, ключ першим.** «Industries», а не «Solutions» (NN/g: розмиті ярлики не працюють). Пункти галузей названі аудиторією («Fitness apps», «Life insurance underwriting»).
5. **Справжні посилання.** Усі пункти меню — `<a href>` у серверному HTML. Верхні пункти з підменю — `<button aria-expanded>`, ніколи `href="#"`.
6. **URL — для людей і аналітики.** Google не рахує слеші і не виводить ієрархію з папок, тож існуючі адреси з трафіком не чіпаємо.
7. **Одна CTA, вхід не в шапці.** `Book a demo` — кнопка. Вхід у кабінети — у футері і на сторінці продукту (§4a).

---

## 4. Шапка, десктоп

| Пункт | Тип | Що всередині |
|---|---|---|
| **Products ▾** | мега-меню | Перший рядок: «How 3DLOOK body scanning works» → `/technology/`. Далі картка на кожен продукт: назва, опис в одному рядку, бейдж (New / Beta). Нижній рядок: Accuracy · Privacy and security · Compare all products (`/#products`) |
| **Industries ▾** | мега-меню | Колонка на кожну галузь: заголовок, під ним продукт(и), до 6 опублікованих сторінок, далі «All … use cases →» на розділ use cases продукту |
| **Pricing** | посилання | `/pricing/` (вкладки продуктів `?product=`, редизайн 10-14) |
| **Resources ▾** | невелике меню | Content Hub · Case studies · eBooks (`/content-hub/category/ebooks/`) · Developers |
| **Company ▾** | невелике меню | About us · Careers · Partners · Contact |
| **Book a demo** | кнопка | Відкриває форму (на головній — `Home | Demo`, на FX-лендингах — `FX | LP | Demo`) |

**Чому так:**
- **Technology** переходить із верхнього рівня в перший рядок Products. Це один клік, як і зараз, і рядок видно одразу при відкритті меню. Також вона є у футері і в блоці How it works на головній. Через місяць після релізу перевірити в GA4, чи не впали переходи на `/technology/`.
- **Developers** не виходить на верхній рівень. Доступ до API у нас через демо і NDA, сторінки `/developers/` ще немає (план, п. 1.3). Коли вона з'явиться, пункт стоїть у Resources. Якщо документація стане відкритою для самообслуговування, тоді варто перевірити, чи виносити Developers вгору.
- **Terms & Policies** йде з Resources у футер. Промо-картки (Safariland, Digiday) з меню прибираємо: NN/g радить місце для вибору, а не для реклами.

**Поведінка:** відкриття кліком (клавіатура, тач) і при наведенні із затримкою 300 мс; Escape і клік поза меню закривають; поточний розділ підсвічено (`aria-current`); меню не перекриває фокус.

Прототип: `nav-prototype-2026-10-22.html`. Скріншоти: `screenshot-products-3.jpeg`, `screenshot-industries-3.jpeg`, `screenshot-products-5.jpeg`, `screenshot-industries-5.jpeg`, `screenshot-products-8.jpeg`.

### 4a. Вхід у кабінети (рішення 10-22)

- **У шапці входу немає.** У FitXpress немає публічного входу в адмінку: доступ видається окремо деяким клієнтам (Вадим, 10-22). Отже, вибирати з одного пункту нічого.
- **Mobile Tailor:** посилання «Mobile Tailor login» → `https://mtm.3dlook.me/` у нижньому рядку футера і на сторінці `/mobile-tailor/` (біля першого екрана, «Already a customer? Log in»).
- **Чому так:** GA4 за 22.07–21.10 не записав жодного кліку з сайту на `mtm.3dlook.me`, хоча вихідні кліки на інші піддомени 3dlook.me записує. Клієнти Mobile Tailor заходять у кабінет напряму.
- Якщо з'явиться продукт із публічним кабінетом, його вхід іде в той самий рядок футера (поле `login` у реєстрі).

---

## 5. Мобільна версія

- Кнопка з підписом **«Menu»** (не голий гамбургер) відкриває панель на весь екран.
- Те саме дерево акордеонами: Products · Industries · Pricing · Resources · Company.
- `Book a demo` закріплена внизу панелі.
- Скріншот: `screenshot-390-menu.jpeg`.

---

## 6. Футер

| Колонка | Вміст |
|---|---|
| Logo + бейджі | HIPAA Compliant, GDPR (рішення 10-19, лишаються) |
| Products | з реєстру |
| Industries | групи галузей → сторінки продуктів |
| Resources | Technology · Pricing · Content Hub · Case studies · Developers · Accuracy · Privacy and security |
| Company | About us · Careers · Partners · Contact |
| Нижній рядок | Terms and policies · Privacy policy · Cookie settings · Sitemap · Mobile Tailor login · © 3DLOOK Inc. |

---

## 7. Дерево сайту і URL

### 7.1 Цільове дерево (після релізу `/fitxpress/`)

```
/                                      головна, сторінка компанії
├── /fitxpress/                        продукт
│   ├── /fitxpress/for-insurance-underwriting/      use case (переїзд з кореня, 301)
│   ├── /fitxpress/for-connected-and-digital-fitness/
│   ├── /fitxpress/for-glp-1-programs/              планується
│   ├── /fitxpress/for-bariatric-programs/          планується
│   ├── /fitxpress/for-wellness-programs/           планується
│   ├── /fitxpress/for-occupational-health/         планується
│   ├── /fitxpress/for-clinical-trials/             планується
│   └── /fitxpress/bmi-verification/                сторінка функції (переїзд з /for-bmi-verification/ при перезбірці)
├── /structured-body-data-for-telehealth-digital-health-programs/   лишається до кінця Q4 (рішення 10-06)
├── /mobile-tailor/                    продукт
│   ├── /mobile-tailor/for-made-to-measure/
│   ├── /mobile-tailor/for-on-demand-manufacturing/
│   └── /mobile-tailor/for-uniforms/
├── /wrist-measurement/                продукт
├── /technology/ · /pricing/ · /developers/ (планується) · /case-studies/ · /content-hub/…
├── /about-us/ · /careers/ · /partners/ · /contact-us/
└── юридичні сторінки (11) у корені, зібрані на /terms-and-policies/
```

### 7.2 Правила URL

| Що | Правило | Приклад |
|---|---|---|
| Продукт | Корінь, без `/products/`. Назва бренду, якщо продукт має бренд; ключове слово, якщо назва описова | `/fitxpress/`, `/mobile-tailor/`, `/wrist-measurement/`, далі `/head-measurement/` |
| Use case | `/{product}/for-{audience}/` (рішення 09-27) | `/fitxpress/for-insurance-underwriting/` |
| Сторінка функції | `/{product}/{feature}/`, без `for-` | `/fitxpress/bmi-verification/` |
| Галузь, яку обслуговують 2+ продукти | `/industries/{industry}/` — хаб, що посилається на сторінки продуктів, а не копіює їх. Робимо лише тоді, коли в одного покупця одна задача на два продукти | ювелірка: wrist + ring sizing |
| Каталог продуктів | `/products/` — лише з 7+ продуктів; до того каталогом є блок продуктів на головній (`/#products`) | — |
| Платформа | у корені | `/technology/`, `/pricing/`, `/developers/` |

**Чому не `/products/fitxpress/`:** Google прямо пише, що структуру він бере з посилань, а слова в URL майже нічого не дають. Сторінки Mobile Tailor приносять найбільше релевантного трафіку (3 007 кліків за Q3), і переносити їх заради папки — ризик без вигоди.

**Хлібні крихти:** `Home › FitXpress › Life insurance underwriting` з `BreadcrumbList`. За Google вони показують шлях людини, а не обов'язково URL. Тому telehealth-сторінка в корені все одно отримує крихти `Home › FitXpress › Telehealth`.

### 7.3 Переїзди (усе вже вирішено раніше, нічого нового)

| Що | Куди | Коли |
|---|---|---|
| `/fitxpress/` (зараз 301 → `/`) | зняти редирект, опублікувати сторінку продукту | реліз `/fitxpress/` |
| `/for-insurance-underwriting/` | `/fitxpress/for-insurance-underwriting/`, 301 | той самий реліз (рішення 10-21) |
| `/for-bmi-verification/` | `/fitxpress/bmi-verification/`, 301 | коли сторінку перезбирають |
| telehealth | лишається | Q4 (рішення 10-06) |
| `/fitxpress` без слеша | зараз веде на статтю про Admin Panel; має вести на `/fitxpress/` | реліз (ТЗ) |
| `http://www.3dlook.ai/*` | 404 → 301 на https | зараз (ранбук 0.8) |

**Що не чіпаємо:** `/mobile-tailor/*`, `/wrist-measurement/`, юридичні сторінки, сторінки компанії.

---

## 8. Що відбувається з новим продуктом

| | 3 продукти (зараз) | 5 продуктів | 7–8 продуктів |
|---|---|---|---|
| Шапка | 5 пунктів | 5 пунктів | 5 пунктів |
| Products | 3 картки в ряд | сітка 3 + 2 | колонки сімейств: Body · Hand and wrist · Head |
| Industries | 3 колонки | 4 колонки (нова галузь — нова колонка) | до 4 колонок; далі галузі групуються |
| Вхід | Mobile Tailor у футері | + посилання у футері, якщо в продукту є публічний кабінет | так само |
| URL | `/{product}/` | `/{product}/` | `/{product}/` + `/products/` як каталог |
| Футер | з реєстру | з реєстру | з реєстру |

Покроковий чекліст нового продукту — у специфікації головної (`../homepage/spec-2026-10-21.md` §3.5). Для меню з нього потрібні:
- запис у реєстрі з полями `family`, `label`, `industry`, `useCases`, `login`;
- бейдж New на перші 90 днів;
- `/industries/{industry}/` — лише якщо нова галузь спільна з іншим продуктом.

---

## 9. SEO і ІІ-пошук

- **Меню — це внутрішні посилання.** Google оцінює важливість сторінки за глибиною кліків і кількістю посилань на неї. Шапка ставить кожен продукт і кожен опублікований use case на відстань одного кліку з будь-якої сторінки.
- **Тільки серверний HTML.** GPTBot, ClaudeBot і PerplexityBot не виконують JavaScript. Меню, зібране скриптом, вони не побачать, як сталось у Persona, де посилання меню видно краулерам лише через футер.
- **Одна назва скрізь:** назва продукту в меню = H1 сторінки = `name` у schema = рядок у `llms.txt`. Це допомагає і Google (sitelinks), і асистентам.
- **`llms.txt` за тією ж структурою:** секції Products · Industries · Resources. Великого ефекту не чекаємо (Google його не використовує), але файл дешевий.

---

## 10. Відкриті питання

**10-22, після «ок» Вадима:** A-1 «Industries», A-2 Technology у Products, A-4 `/fitxpress/bmi-verification/` (виправлено в `site-inventory.md`) і A-7 (шапка в прототипі головної і у Figma) закрито. Відкриті A-3, A-5, A-6.

| # | Питання | Пропозиція |
|---|---|---|
| A-1 | Назва другого пункту: «Industries» чи «Use cases» (як зараз) | «Industries»: так підписують Styku і Size Stream; «Use cases» — внутрішній термін |
| A-2 | Прибрати Technology з верхнього рівня | Так, перший рядок Products + футер; перевірити GA4 через місяць |
| A-3 | ~~Адреса входу у FitXpress Admin Panel~~ | **Закрито 10-22:** публічного входу немає, вхід прибрано з шапки (§4a) |
| A-4 | Адреса BMI-сторінки: `landing-map.md` (09-29) каже `/fitxpress/bmi-verification/`, `site-inventory.md` — `/fitxpress/for-online-pharmacies/` | Взяти `landing-map` (новіше, і за твоїм рішенням це сторінка функції, а не use case); виправити `site-inventory.md` |
| A-5 | eBooks у Resources | **Закрито 10-22:** eBooks три («The Next Big Leap in Health» — сторінка, «The Digital Health Revolution» і «The AI Advantage» — пости). Пункт меню веде на `/content-hub/category/ebooks/`. Зараз категорія показує лише «The Digital Health Revolution»: Асель додає в неї «The AI Advantage» і картку-посилання на «The Next Big Leap in Health» |
| A-6 | Head і ring у меню | **Закрито 10-22:** продукти з'являться у 2027, продуктова команда лише вивчає питання. До запуску на сайті їх не називаємо; у прототипах вони лишаються тільки як приклади для перевірки сітки |
| A-7 | Шапку прототипу головної (6 пунктів із Technology) привести до цієї схеми | Після твого апруву, разом з оновленням кадру у Figma |
