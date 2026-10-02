---
product: fitxpress
type: page-review
vertical: connected-and-digital-fitness
date: 2026-10-02
compares: живий /fitxpress/for-connected-and-digital-fitness/ · драфт Ніки (Drive doc «FITNESS: Landing, 2-pager, deck», вкладка Landing Page) · її HTML-ітерація (Drive «fitxpress-connected-fitness.html», 10-02)
result: page.md (v2 за кітом page-builder з правилами Асселі від 10-02)
---

# Рев'ю: фітнес-лендинг Ніки → коротка v2

Задача Вадима 10-02: «оціни перший драфт юз-кейсу по фітнесу від Ніки і прогони через пейджбілдер».
Дизайн не оцінюю, лише структуру, текст і факти. У доку Ніки є вкладка «Last final version» з правками
(«H1 more salesy», «найбільша проблема — дуже великий черн», «shorter, more value», «add more numbers»).
HTML-версія вже частково їх виконує, тому за базу взято її.

## 1. Порівняння

| | Живий лендинг (08-23) | Ніка, док | Ніка, HTML | **v2 (`page.md`)** |
|---|---|---|---|---|
| Обсяг видимого тексту | ~1 200 | ~1 860 | ~2 010 | **~1 340** (кіт: 1 100-1 300) |
| H2 / FAQ | 6 / 13 | 9 / 9 | 10 / 7 | **8 / 4** |
| «you / your» на 1 000 слів (поріг 12,5) | — | 15,6 | 14,9 | **0** |
| Головний ключ `gym body scanner` у title / H1 | ні / ні | ні / ні | ні / ні | **так / так** |
| Проблема в цифрах | немає | немає | **7% (Adjust) і 70% (JMIR)** | три: Adjust 24% → 7% (1-й і 30-й день) і 70% (JMIR), усі звірено з першоджерелами |
| Порівняння з тим, як роблять зараз | немає | немає | немає | таблиця: ваги + фото / зальний сканер |
| Ціна | немає | $1 000 / Pro $1 500 | $1 000 / Pro $1 500 | те саме + no integration fee |
| Пілот із метриками | немає | немає | немає | когорта + holdout, day-30 / day-90 |
| Compliance-формулювання | «HIPAA compliance», «no PII» | 3 hard fail | 3 hard fail | з `compliance.md` дослівно |
| Лінк на хаб `ai-in-fitness-industry` | немає | немає | немає | **так, двічі** |
| Schema | WebPage | — | Service + FAQPage + Breadcrumb | те саме, 3 рівні крихт |
| Детектор AI-tells | 3 заборонені слова | чисто | чисто | чисто |

**Висновок.** Ніка написала сильний текст. Детектор не знайшов у ньому жодного AI-tell. Добре
підібрано мову покупця («members quit when they can't see progress», «premium tier»), є KPI-таблиця, а
ілюстративний макет прогресу показує головну ідею продукту за 5 секунд. Слабкі місця не в стилі, а у
фактах і формі. Близько 15 тверджень не мають джерела в `proof-points.md`, `tech-spec.md` чи
`compliance.md`, три з них — жорсткі заборони. Сторінка на 50% довша за бюджет. Головного ключа немає в
title і H1. Canonical веде на інший URL. v2 зберігає її скелет, цифри проблеми, макет, KPI (перенесені в
метрики пілоту) і голос, а факти, ключі й лінки бере з наших джерел.

## 2. Що виправити в драфті Ніки: факти й compliance

| # | Що в тексті | Проблема | Як у v2 |
|---|---|---|---|
| 1 | «No personal identifiers are processed» | **Hard fail** (`compliance.md` §4, детектор `compliance_status`). Фото й виміри можуть бути персональними даними | «Scan records use anonymized, randomly generated identifiers.» |
| 2 | «variance under 1 cm, with **95%+ consistency**» | **Hard fail.** 95%+ — внутрішня цифра, «DO NOT PUBLISH» (`proof-points.md`): у живій статті про точність її немає | `< 1 cm` за `accuracy-formulations.md` §1.2 |
| 3 | Таблиця точності по частинах тіла (chest 0.60 / 1.74 cm, waist 0.89 / 2.14 cm…) | Лише для внутрішніх і технічних матеріалів: жива стаття про точність не публікує цифр по частинах тіла | Прибрано. Деталі методології — під NDA, лінк на статтю |
| 4 | «React Native kit», «web components» | `tech-spec.md`: «Do not write React Native (not confirmed)». Публічне формулювання: «web and mobile SDKs, including supported iOS and Android integrations» | Публічне формулювання |
| 5 | «The scan ships as a wellness feature, with no clinical approval step» | Регуляторне твердження про чужий процес. Писати, що регуляторна рамка «не застосовується», не можна; щодо FDA ми не стверджуємо, чи потрібен клієренс | Прибрано. Залишено «FitXpress is not a medical device.» один раз |
| 6 | GDPR: «Principles applied… purpose limitation, data minimization» | «Follows GDPR principles» як уся відповідь — у списку never-say | Канонічне речення про controller / processor |
| 7 | «Data is processed and stored in AWS US West (Oregon). No European region» | Неповно: основний регіон US-West-2, частково US-East-1. Регіони — у trust-FAQ | Лінк на trust-FAQ |
| 8 | «Self-serve deletion… not available today», «one DPA version covers all countries» | Ні того, ні іншого немає в trust-FAQ. Видалення там — за scan ID | «deletion by scan identifier» → trust-FAQ |
| 9 | «Photos… not used to train the model» | Відходить від канонічного формулювання | «does not use production customer data… without the customer's explicit, documented authorization» |
| 10 | SDK «iOS device binary about 40 MB (arm64 slice about 104 MB)», «On-Demand Resources not supported», «work offline» | Джерела немає в жодному файлі. Числа ще й виглядають суперечливими | Прибрано → open items, питання до продукту |
| 11 | «Webhooks have no automatic retries or signature verification» | Немає джерела, до того ж це публічна слабкість на продажній сторінці | Прибрано → open items |
| 12 | «About 100 requests per hour… autoscaling», «Uptime 99.5% with service credits» | Немає джерела | Прибрано → open items (SLA — для sales-розмови) |
| 13 | «10 hours a month» підтримки, «dedicated customer success manager» на кожному плані | На `/pricing/` для Starter і Pro лише «Guided implementation support»; dedicated support — тільки на Personalized | Не згадується. Ціни й Pro-фічі звірено з `/pricing/` 10-02 |
| 14 | «iOS 15+ and Android, including older models» | Немає джерела (`tech-spec.md`: «works on any smartphone camera») | Смуга фактів: «No hardware» |
| 15 | «Height is entered within 2 cm…», «four conditions» (одяг, захоплення, зріст, умови) | Умов зйомки немає в каноні точності. Чотири умови фреймворку — інші (reference method, protocol, population, workflow) | Одне речення про метод + лінк на фреймворк |
| 16 | «Clothing Detector correct… clothing in real time», «designed to remove manual scan review» | Фінал insurance 10-02: clothing-related information «does not trigger a retake». Друге — обіцянка без джерела | «RTPV pauses capture until…», «Clothing-related information can be surfaced for review» |
| 17 | «Two gender options… because the detectors and neural networks rely on those two categories», «must stand throughout» | Чутлива тема без затвердженого формулювання. Standing-only ще чекає на Вадима (insurance v3) | Затверджене формулювання про людей з інвалідністю + популяція валідації |
| 18 | 70%: «70% of users stopped» | У джерелі — **медіана** 70% | «median share of users…» |
| 19 | Форма: власні поля «Platform type», «Monthly active users», «respond within 1 business day», «30-minute demo» | Рішення 09-29: одна спільна форма `FX \| LP \| Demo`. Тривалість демо й строк відповіді — обіцянки за sales | Спільна форма, без обіцянок |
| 20 | Canonical `…/fitxpress/for-connected-fitness/` | **Живий URL — `/fitxpress/for-connected-and-digital-fitness/`.** Зі старим canonical сторінка ризикує втратити й так слабкий індекс | Canonical на себе, URL не змінюється |
| 21 | Лінки `/fitxpress/for-telehealth-and-weight-loss/`, `/fitxpress/for-health-plans-and-employer-wellness/`, `/content-hub/2-photo-vs-video-vs-hardware/` | Перший — 301, два інші — 404 (перевірено 10-02). Запланований URL не лінкуємо (landing-map) | Живі адреси: telehealth-сторінка, `/for-bmi-verification/`, `body-scanning-technology-comparison` |
| 22 | Шрифти Manrope і Space Grotesk | `DESIGN.md`: тільки Satoshi | Прототип на шаблоні фіналу insurance |
| 23 | FAQ «Does the data sync to Apple Health or Google Fit?» | Google замінив Google Fit APIs на Health Connect; CPO фітнес-застосунку це помітить (зауваження сліпого судді) | «Apple Health or Health Connect», відповідь першим реченням |

**Перевірено й залишено:** 7% активних на 30-й день серед health & fitness застосунків (Adjust, глобальні
дані 2022). Звірено з самою сторінкою Adjust (через reader-проксі, бо напряму сайт віддавав 429). Там же
24% на 1-й день, тож у v2 з'явилась третя цифра: падіння 24% → 7%. Медіана 70% за 100 днів і «lack of personalization» серед причин (Kidman et al.,
JMIR 2024) звірено з повним текстом. Ціни: Starter $1 000 / 500 сканів, Pro $1 500 / 1 000 сканів із
3D body progress tracking і 3D Goal Visualization (живий `/pricing/`, 10-02).

## 3. SEO і структура

- **Головний ключ.** Карта ключів (09-29, §2) ставить `gym body scanner` у title, H1, перший абзац і meta.
  У Ніки title — «Body Composition Tracking for Fitness Apps», H1 — «Body progress tracking built to lift
  retention…». У v2 H1 — «Retain fitness app members with a mobile alternative to the gym body scanner»:
  вигода першим словом (правка Вадима «H1 more salesy», черн — головна проблема) і точний ключ. Перший
  варіант без «Retain» обидва сліпі судді мінусували за те, що H1 веде ключем, а не результатом.
- **GEO-FAQ.** Дослівно як H3 взято «What is a body scan at the gym?» (US 90, KD 0) і «What body scanning
  SDKs work for fitness apps with remote users?» (AEO 81%). FAQ «What's the best alternative to hardware
  3D body scanners…» (AEO 51%) я написав, але прибрав: він повторював висновок порівняльної таблиці, а
  саме такі FAQ Асселя різала на insurance. Його можна повернути, якщо промпт AEO важливіший за дедуп.
- **Блок «Built for how fitness platforms ship».** Вертикальний контекст сильний (growth тримає кейс,
  mobile lead підписує, app store disclosures). Але половина фактів у ньому без джерела (розмір SDK,
  «no clinical approval step»). У v2 лишився один рядок про App Store privacy details і Google Play Data
  safety у блоці даних.
- **KPI-таблиця «Where body data moves the metrics»** — найкраща знахідка драфту. Як окремий блок вона
  читалася як обіцянка результату, тож у v2 її метрики стали тим, що вимірює пілот (day-30 / day-90
  retention, repeat scan rate, free-to-premium).
- **Порівняння.** Блоку «як роблять зараз» у Ніки не було, а кіт його вимагає. Для цього ключа це
  ще й головний аргумент: ваги + фото в галереї проти зального сканера проти FitXpress.

## 4. 2-pager (та сама вкладка доку), коротко

Ті самі факти: «Integration in as Little as 2 Days» (немає джерела; `tech-spec.md` каже «SDK in days,
not months») · «GDPR Principles Applied» (never-say як уся відповідь) · «96 to 97%» → `96-97%` · «Repeat
scans stay within 1 cm of each other» → «typical scan-to-scan differences of less than 1 cm for most
measurements» · «with results in under 45 seconds» → «under 45 seconds from the photos to structured
results» · «Future Body Goal Visualization» є лише з Pro. У ICP-картці «React Native» (див. п. 4).

## 5. Що далі

Відкриті питання — `open-items.md`. Блокери публікації — `TODO.md`. Оцінка сліпого судді —
`judge-round-N.json`.
