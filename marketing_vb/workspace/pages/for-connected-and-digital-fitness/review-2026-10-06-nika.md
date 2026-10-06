---
product: fitxpress
type: page-review
vertical: connected-and-digital-fitness
date: 2026-10-06
compares: Ніка, фінальна ітерація (Drive «fitxpress-connected-fitness-final.html», 10-06, збережено як nika-final-2026-10-06.html + .md) · наша v2 (page.md, 10-02)
result: page-v3-2026-10-06.md (кіт page-builder із правилами «Sell, not educate» від 10-06)
previous_review: review-2026-10-02-nika.md (нумерація правок 1–23 нижче посилається на нього)
---

# Рев'ю: фінальна ітерація фітнес-лендингу від Ніки → v3

Задача Вадима 10-06: «Ніка підготувала новий варіант фітнес, прогони його». Ніка взяла за основу нашу
v2 (той самий макет прогресу, кроки, FAQ слово в слово) і зробила сторінку продажнішою. У той самий день
команда затвердила правила для лендингів («Sell, not educate»), і v3 зібрано вже за ними. Дизайн не
оцінюю, лише структуру, текст і факти.

## 1. Порівняння

| | v2 (10-02) | **Ніка, фінал (10-06)** | **v3 (`page-v3-2026-10-06.md`)** |
|---|---|---|---|
| Обсяг видимого тексту | ~1 270 | ~1 700 | **~1 315** (бюджет 1 100–1 300) |
| H2 / FAQ | 8 / 4 | 10 / 7 | **8 / 4** |
| «you / your» на 1 000 слів (поріг 12,5) | 0 | **22,3** | 0,6 |
| H1: продукт + аудиторія + результат (правило 1) | ні продукту | ні продукту, ні ключа | **так, з ключем `gym body scanner`** |
| Порядок: «що отримуєте» перед «як працює» (правило 2) | ні | так (блок вигод) | так |
| Проблема в цифрах (черн) | 24% → 7%, 70% | **прибрано** | повернуто |
| Вигоди поруч із функціями (правило 5) | ні | так, окремий блок | так, колонка «What it changes for the app» |
| Пілот із holdout і метриками | так | **прибрано** | так |
| Проблеми з фактами й формулюваннями (§3, пп. 1–14) | 0 | **14** | 0 |
| Детектор `--channel page` | чисто | 5 en dash, 3 house rules | **чисто** |

**Висновок.** Продажний кут у Ніки сильніший, ніж у v2, і v3 бере його майже весь. Але разом із ним
повернулися 14 проблем із фактами й формулюваннями. Більшість із них рев'ю 10-02 вже прибирало, а одна
є hard fail («95%+ consistency»). Через них цю версію не можна віддавати в дизайн як є. Також зник блок із цифрами
черну, а саме черн Вадим назвав головною проблемою.

## 2. Що з версії Ніки взято у v3

- **Блок вигод «For your members»** став таблицею «Returned output → What it changes for the app».
  Так кожна функція має свою вигоду в одному рядку, і окремий блок не потрібен.
  Її формулювання в основі рядків: «Change the scale can't show», «Programs built on body data»,
  «A premium feature of its own» (3D-прогрес як причина перейти на платний тариф).
- **H2 «Each scan shows members the change the scale can't»** походить від її H3.
- **FAQ «Will adding a scan step reduce onboarding completion?»** — справжнє заперечення CPO. Відповідь
  у v3 чесніша: місце скану вибирає платформа, а пілот вимірює completion до повного запуску.
  Обіцянки «не знизить» там немає.
- **Колонка «Standalone scanning app»** у порівнянні, рядки «Brand the member sees» і «Data back to the
  platform». Після таблиці v3 одним реченням каже висновок (правило 4).
- **H2 пілоту «Start with a pilot, then scale on a fixed monthly plan»** — заголовок із вигодою, без образності.
- **«100+ clients since 2016»** як сигнал довіри. Це єдине публічне число клієнтів, і рік заснування теж
  публічний. У v3 він стоїть у блоці пілоту, поруч із реченням про готовність.
- **Ціни Starter і Pro** збігаються з живим `/pricing/` (перевірено 10-06). «Custom plans» = Personalized.
- **Canonical** тепер правильний (`/for-connected-and-digital-fitness/`). Форма не має власних полів.

## 3. Що виправити у версії Ніки

Номери в дужках відсилають до рев'ю 10-02, де ці самі пункти вже розбиралися.

| # | Що в тексті | Проблема | Як у v3 |
|---|---|---|---|
| 1 | «< 1 cm… with **95%+ consistency**» | **Hard fail** (п. 2). У `proof-points.md` позначено «INTERNAL ONLY, DO NOT PUBLISH». У живій статті про точність такої цифри немає | `< 1 cm` за каноном |
| 2 | Таблиця точності по частинах тіла (chest 0.60 / 1.74 cm…) | Лише для внутрішніх матеріалів (п. 3) | Прибрано. Методологія під NDA, далі лінк на фреймворк |
| 3 | «Conditions: … height entered within 2 cm…» | Цих умов немає в каноні точності (п. 15) | Прибрано |
| 4 | «a React Native kit and web components» | `tech-spec.md`: «Do not write React Native (not confirmed)» (п. 4) | «web and mobile SDKs, including supported iOS and Android integrations» |
| 5 | «99.5% uptime SLA, with service credits» | Немає джерела (п. 12) | Прибрано → питання до продукту |
| 6 | «2 days integration at its fastest» | Немає джерела (2-pager, 10-02) | Прибрано → питання до продукту |
| 7 | «iOS 15+ and Android, including older models» | Немає джерела (п. 14) | «on their own phone, with no hardware» |
| 8 | «Guided implementation on every plan, with a dedicated customer success manager» | За живим `/pricing/` dedicated support є лише на Personalized (п. 13) | «Both include guided implementation support» |
| 9 | RTPV «with no manual review on your side» | Обіцянка без джерела (п. 16) | «which helps avoid retakes» (`tech-spec.md`, з обережним дієсловом) |
| 10 | FAQ про розмір SDK (40 MB / 104 MB) | Немає джерела (п. 10) | Прибрано → питання до продукту |
| 11 | FAQ «Webhooks have no automatic retries or signature verification» | Немає джерела, і це публічна слабкість на продажній сторінці (п. 11) | Прибрано → питання до продукту |
| 12 | «Data is processed and stored in AWS US West (Oregon)» | Неповно: основний регіон US-West-2, частково US-East-1 (п. 7) | Регіони покриває лінк на trust-FAQ |
| 13 | «In most deployments, you act as data controller and 3DLOOK as processor» | Канон GDPR дослівний, хедж «enterprise» не зрізається (CLAUDE.md §12) | Канонічне речення |
| 14 | «A 30-minute demo» | Тривалість демо — обіцянка за sales (п. 19) | «We walk the member flow…» без тривалості |
| 15 | H1 «Accurate body scanning for fitness apps that makes member progress measurable» | Немає продукту (правило 1), немає ключа `gym body scanner` (карта ключів §2). Сторінка починається з точності, хоча продаємо результат (CLAUDE.md §3, «пастка» з кіта) | «FitXpress for fitness apps: help retain members with in-app body scanning» (рішення Вадима 10-06: H1 мовою застосунків, а не «gym body scanner»; «help» — guardrail #1, бо внутрішньої цифри про утримання немає) |
| 16 | Блок точності на третьому екрані | Сторінка спершу доводить точність, і лише потім пояснює, навіщо вона застосунку | Точність стоїть після вигод і порівняння, як доказ (правило 9) |
| 17 | Прибрано цифри черну (Adjust 24% → 7%, JMIR 70%) | Черн — головна проблема за Вадимом, а без цифр читач сам має додумати, навіщо це все (правило 4) | Повернуто з висновком: «Every member lost in the first month is acquisition spend…» |
| 18 | Прибрано holdout і метрики пілоту | Кіт (блок 7) вимагає написати, що пілот має виміряти, бо CPO купує саме цифри для рішення | Повернуто: completion, repeat scans, day-30 / day-90 retention, free-to-premium |
| 19 | «you / your» 22,3 на 1 000 слів | Поріг 12,5 (Асселя, 10-02). «Your app», «your platform», «your members» по всій сторінці | У поясненнях названо актора: «the platform», «the app», «the product team» |
| 20 | `96–97%`, `1.5–2.0 cm` через en dash | Канон пише через дефіс; en dash — hard ban | `96-97%`, `1.5-2.0 cm` |
| 21 | SLA, API, ID, TLS, AWS, JSON, CSV без розшифровки | M1: кожна абревіатура розшифровується при першій згадці | Розшифровано або прибрано разом із реченням |
| 22 | ~1 700 слів, 7 FAQ | Бюджет 1 100–1 300 і 4–6 FAQ | ~1 315 і 4 FAQ |
| 23 | Блок «Why 3DLOOK» (9 фактів) | Блок робить кілька робіт одразу (правило 6), і 5 із 9 фактів не мають джерела | Перевірені факти розкладено по місцях: white-label у смугу фактів, SDK у кроки, підтримку в ціни, «100+ clients» у пілот |
| 24 | Рядок «3D body model: A 3D model per scan» (так було й у v2) | На живому `/pricing/` (10-06) Starter не має 3D-моделі. 3D Body progress tracking і 3D Goal Visualization є лише в Pro | 3D-функції згадано тільки з «on the FitXpress Pro plan» |

**Погоджуюсь із Нікою:** рядок про App Store і Google Play з блоку даних вона прибрала правильно. Він не
проходить blog test, і відкрите питання 7 до Асселі закрито. `privacy@3dlook.me` у v3 не потрапив: це
контакт для прав кінцевих користувачів, а документи для закупівлі йдуть на `legal@3dlook.me` у футері.

## 4. Як v3 застосовує правила «Sell, not educate» (10-06)

- **H1** = FitXpress + fitness apps + help retain members + in-app body scanning. Title «In-App Body
  Scanning for Fitness Apps | FitXpress». `gym body scanner` лишився вторинним ключем у порівнянні й FAQ.
- **Логотипи:** під смугою фактів іде рядок логотипів усіх клієнтів 3DLOOK (рішення Вадима 10-06) з підписом
  «100+ clients have used 3DLOOK body scanning since 2016.» Довший H1 у
  прототипі потребує меншого кегля: 50 px на десктопі (на 65 px він займав шість рядків і виштовхував
  кнопку за перший екран), 30 px на мобільному. Це для дизайнера.
- **Перший абзац** відповідає на «що отримує застосунок»: «Show members the progress the scale misses at every
  check-in». Механіка (два фото, 45 секунд) іде другим реченням і в смузі фактів.
- **Порядок:** спершу проблема, потім що повертає скан (з вигодою в кожному рядку), а «як працює» йде
  лише після цього.
- **Висновки:** кожна таблиця й кожна цифра мають речення «що це означає» для застосунку.
- **Blog test:** вирізано FAQ «How often should members scan?» (порада щодо використання, яка без втрат
  переїжджає в статтю), рядок про App Store, умови зйомки і пояснення розміру SDK.
- **Застереження гардрейлів лишились:** речення про методику біля цифр точності, межа «FitXpress is not
  a medical device.», обережне «can give members a reason to stay».

## 5. Що далі

Оцінка сліпого судді — у `judge-round-N.json` (раунди 10-06 мають суфікс `v3`). Відкриті питання —
у `open-items.md`, блокери — у `TODO.md`.
