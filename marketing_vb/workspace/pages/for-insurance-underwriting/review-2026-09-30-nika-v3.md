---
product: fitxpress
type: page-review
vertical: insurance-underwriting
date: 2026-09-30
reviews: драфт Ніки v3 (Drive, «fitxpress-insurance-underwriting (3).html», 09:53 UTC)
against: page-v2-short.md, comments-nika-2026-09-30.md, kit-vertical-page.md (Length and order, 2026-09-30)
---

# Рев'ю: insurance-лендинг Ніки, v3

## Обсяг

| | Ніка v1 | **Ніка v3** | Наша v2 | Ціль кіта |
|---|---|---|---|---|
| Слів | ~2 050 | **~2 470** | ~1 250 | 1 100-1 300 |
| H2 | 11 | **12** | 8 | 8-9 |
| FAQ | 9 | **15** | 6 | 5-6 |
| Таблиця порівняння | 8 рядків | **10 рядків** | 5 | 5 |

v3 пішла в протилежний від задачі бік: вона на ~20% довша за v1 і вдвічі довша за ціль.

## Що з 12 коментарів виправлено

| # | Коментар | v3 |
|---|---|---|
| 1 | Довжина | ❌ стало довше |
| 2 | «positioned as» | ✅ «FitXpress is not a medical device.» |
| 3 | 150-205 cm | ✅ прибрано |
| 4 | 67 клієнтів / 112,100 | ✅ прибрано |
| 5 | «No exam» у hero | ❌ лишилось у стрічці, і з'явилось ще «without an exam» у підзаголовку |
| 6 | «Verified» і ключ у H1 | ✅ «Second-source build evidence for accelerated underwriting in life insurance» |
| 7 | «Encrypted and short-lived» | ⚠️ заголовок лишився, але новий FAQ «What stays on file after photos are deleted?» пояснює правильно |
| 8 | HIPAA/BAA | ❌ немає |
| 9 | Власна форма | ❌ лишилась, тепер з полем «annual accelerated application volume» |
| 10 | Лінк на неіснуючий чекліст | ❌ лишився |
| 11 | «30-minute», «not billable» | ❌ «30-minute» двічі; «not billed» уже тричі (ціни, FAQ про вартість, FAQ про збій) |
| 12 | FAQ 5-6 з GEO-фразами | ⚠️ GEO-фрази є, але питань 15 |
| — | «96 to 97%» | ❌ формат не виправлено |

## Що в v3 сильне (варто забрати у v2)

1. **Munich Re з повним джерелом.** «33,000+ lives across 30 accelerated underwriting programs, 2013 to 2023», build/BMI — №1 у random holdouts і post-issue audits, тютюн — №2 у holdouts. Звірено з першоджерелом, усе правильно.
2. **Чесні межі мовою андеррайтера.**
   - Зріст береться з анкети, тому помилка в зрості переходить в обидва BMI.
   - Хто не може пройти скан, лишається на поточному шляху.
   - Особу скан не підтверджує, це робить ID-крок у заявці.
   - Скан не показує прийом GLP-1.

   Саме такі питання ставить underwriting-команда.
3. **Словник вертикалі.** Random holdout як референсна група для shadow evaluation, straight-through processing і referral rate, «how many of those flags hold up», слід для reinsurers.
4. **Вартість на заявника** ($2 на Starter і $1.50 на Pro при повному обсязі) проти ціни paramed-візиту. Це найсильніший комерційний аргумент у всіх версіях.
5. **Ключ `life insurance underwriting software`** стоїть природно: «results land in your life insurance underwriting software».
6. **Вагові цифри під поріг** (76% прогнозів у межах 5% від ваги на вагах, 89% збігу BMI-груп). Саме це потрібно андеррайтеру, щоб поставити поріг. Але джерела поки немає, див. нижче.

## Що не можна публікувати без підтвердження

| Твердження | Статус |
|---|---|
| Вагове дослідження: 1,773 дорослих, 18-75 років, лабораторія 3DLOOK, облягаючий одяг, 50.6% / 49.4%, 76% у межах 5%, ~96% у межах 10%, 89% збігу BMI-груп | **Немає в репо.** `proof-points.md` знає лише «±3.5%, real-world conditions», а v3 пише «lab, tight-fitting clothing». Потрібен документ-джерело і рядок у `proof-points.md` |
| Smart Scales без позначки beta | `how-it-works.md` і `tech-spec.md` називають Smart Scales **beta**. Сторінка будує головну цінність на ньому й про beta не каже. Це стосується і нашої v2 |
| «99.5% uptime SLA» | ✅ `faq.md`. Але в `icp-detail.md` стоїть 99.9%, у репо суперечність |
| «with a public status page» | Джерела немає |
| «Data is processed and stored in AWS US West (Oregon)» | Неповно. Trust-FAQ: «primarily in US-West-2 and partially in US-East-1» |
| «Live capture blocks uploaded, edited or generated images» | В `audience.md` є лише «anti-spoof controls (live capture…)». Про згенеровані зображення треба підтвердження продукту |
| «wheelchair users and amputees can't be scanned today» | Джерела немає. Схоже на правду (скан стоячи), але потрібні підтвердження й обережне формулювання |
| «We don't publish results by body type or skin tone…» | Чесно, але сторінка сама відкриває тему fairness, на яку NAIC зважає. Рішення Вадима / Whitney |
| «customers have their own reasons to misstate build» (про UK-аптеку) | Звучить як звинувачення клієнтів нашого клієнта. Краще прибрати |

## Дрібне

- «lets life insurers» → «allows life insurers» (заборона «let»).
- «…obfuscated at capture, so the scan can't confirm identity» — детектор: hard fail, «so» перед наслідком.
- GDPR не канонічним реченням: «you act as controller…» → «the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR».
- Порожній canonical, хлібні крошки у два рівні, title закінчується «| 3DLOOK» замість FitXpress.
- Картки тарифів дублюють `/pricing/`. На лендингу вистачить одного рядка.

## Рекомендація

За основу v3 не брати. Беремо скелет v2 і вливаємо в нього найкраще з v3, не виходячи за бюджет:

- **Проблема:** повне джерело Munich Re.
- **Як це працює:** рядок «Applicants who can't complete a scan stay on your current evidence path» і `life insurance underwriting software`.
- **Пілот:** random holdout як референсна група; метрики STP / referral rate і «how many flags hold up».
- **Ціна:** «from $2 per applicant at full plan volume» (якщо Вадим дозволить: кіт зараз забороняє per-request ціни).
- **FAQ (6):** замість «What happens when a scan fails?» — «How many cases will it flag?»; у відповідь про зріст — «a misstated height carries into both values».
- **Точність:** вагові цифри під поріг — тільки після того, як вони з'являться в `proof-points.md`.

## Питання до Вадима

1. Звідки дослідження ваги (1,773 людини, 76% / 89%)? Якщо є документ, заносимо в `proof-points.md`, і цифри йдуть у v2.
2. Smart Scales досі beta? Якщо так, чи пишемо це на сторінці.
3. Ціна на заявника ($2 / $1.50) на сторінці — так чи ні.
4. Чи є публічна status page.
5. Хто підтверджує від продукту блокування згенерованих зображень і скан лише стоячи.
