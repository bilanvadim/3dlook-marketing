---
product: fitxpress
type: page-review
vertical: glp-1-programs
language: ru
date: 2026-10-07
for: Nika (её просьба «посмотрите эту страницу и дайте свои инпуты, можно лучше описать проблему и боль индустрии»)
source: nika-draft-2026-10-07.html (Drive "fitxpress-glp1-landing1.html", 2026-10-07 17:07 UTC)
benchmark: workspace/pages/for-connected-and-digital-fitness/page-final-2026-10-07.html (структура), kit-vertical-page.md
---

# GLP-1 лендинг: инпуты по версии от 07.10

Ника, посмотрели страницу. Ниже разбор, а в приложенном HTML (`page-v2-2026-10-07.html`) эти правки уже
применены на шаблоне утверждённого фитнес-финала, чтобы было видно, как это выглядит целиком.

## Что в HTML (v2)

- **Новый блок проблемы** после карточек ценности: «What does a GLP-1 program miss when it tracks only
  weight?», три цифры из первоисточников (64,8% бросают терапию за год, ~25% потерянного веса — lean mass,
  34% работодателей ставят условия покрытия) и вывод для программы. Почему именно эти цифры — ниже.
- **H1** «FitXpress for GLP-1 programs: body composition tracking at every remote check-in» (продукт +
  аудитория + главный ключ из карты). Title «Body Composition Tracking for GLP-1 Programs | FitXpress».
  URL по карте лендингов: `/fitxpress/for-glp-1-programs/`. H1 и URL ещё подтверждаем.
- **Порядок как в фитнес-финале:** hero → логотипы → ценность → проблема → запись скана → как работает →
  сравнение → точность и данные → пилот и цены → FAQ → форма. Блок «Why 3DLOOK» разложен по местам.
- **Логотипы:** Yazen, UK Meds, Healthyr первыми, подпись «100+ clients have used 3DLOOK body scanning since
  2016, including weight management programs.» Остальные логотипы даст дизайн.
- **Ценность:** 4 карточки. **Запись скана:** 4 строки с колонкой «What it changes for the program»
  (predicted weight вместо Smart Scales с «before the prescriber approves»; Pro-функции в ценах).
- **Сравнение:** 4 варианта (FitXpress, self-reported weight, connected scale, clinic BIA или DXA), на
  мобильном карточки.
- **Точность и данные на одном экране:** < 1 cm и 96-97%, одно предложение о методе; 6 строк данных
  (Photos, Identifiers, HIPAA, GDPR, Encryption, Model training) дословно из канона, ссылка на trust FAQ и
  privacy@3dlook.me.
- **Пилот:** сравнительная когорта, рандомизация где возможно, шаг «Evaluate and roll out»; к твоим трём
  метрикам добавлено удержание в программе против сравнительной когорты. Тарифы как на /pricing/ (Custom
  там называется Personalized).
- **FAQ: 5.** GEO-вопрос из карты ключей («How can a GLP-1 weight-loss clinic track patient body composition
  remotely?»), мышцы, DXA, BMI-eligibility, доставка результатов со ссылкой на API-документацию. FDA, BAA,
  SOC 2 закрывает ссылка на trust FAQ.
- **Техника:** шрифт Satoshi и токены DESIGN.md, общая форма `FX | LP | Demo`, мёртвые ссылки заменены,
  FAQ в JSON-LD совпадает с текстом. ~1 620 видимых слов (было ~2 150), «you/your» 0, детектор без жёстких
  нарушений. Hero влезает в 1280×800; на 375 px кнопка hero ниже первого экрана, «Book a demo» есть в шапке.
- Слепым судьёй не прогоняли: это ответ на твой запрос, а не сборка к публикации.

## Главное: проблемы на странице сейчас нет совсем

Порядок сейчас такой: hero → ценность → точность → «Why 3DLOOK» → как работает → запись скана → данные →
сравнение → пилот и цены → FAQ → форма. Ни один блок не говорит, что программа теряет без FitXpress.
Боль есть только намёком в hero («even when the scale stalls») и в сравнении.

Покупатель здесь — VP Product, Head of Clinical Operations или CMO GLP-1 платформы. Ему нужно на втором
экране увидеть свою проблему в цифрах, которые он сам приносит на совещание. Предлагаю блок «The problem»
сразу после карточек ценности (так стоит в утверждённом фитнес-финале): вопросный H2, одно предложение о
том, во что программе обходится пробел, две-три цифры из первоисточников и одно предложение-вывод.

### Какую боль берём (и какую нельзя)

Все цифры ниже проверены по первоисточникам 07.10 (полный список с оговорками: `sources-problem-block.md`).
Три боли, которые выдерживают проверку:

1. **Пациенты уходят с терапии в первый год.** 64,8% взрослых в США без диабета 2 типа, начавших GLP-1,
   прекратили его в течение года (JAMA Network Open, 2025). Для программы, которая получает деньги за
   активного пациента, это прямая потеря выручки.
2. **Весы не показывают, из чего состоит потеря.** В DXA-подисследовании 72-недельного исследования около
   25% потерянного веса пришлось на lean mass, около 75% на жир. Совместный advisory четырёх американских
   обществ по ожирению и питанию (2025) включает оценку состава тела в обследование перед GLP-1 терапией.
   Между визитами в клинику или на DXA у удалённой программы есть только одно введённое число.
3. **Работодатели ставят условия покрытия.** 34% компаний с 200+ сотрудниками, которые покрывают GLP-1 для
   снижения веса, требуют программу вокруг препарата (диетолог, кейс-менеджер, lifestyle-программа) как
   условие покрытия (KFF, 2025).

**Чего на странице утверждать нельзя:**
- **«Пациенты бросают, потому что не видят прогресса».** Данные этого не подтверждают: в исследовании, где
  классифицировали причины, из-за недостаточной потери веса бросили 1,7%, из-за цены или страховки 47,6%,
  из-за побочных эффектов 14,6%. Можно только «greater weight loss was associated with staying on
  treatment», и обещать, что FitXpress снижает отток, нельзя (нет внутренней цифры, guardrail #1).
- **«GLP-1 съедает мышцы».** У плацебо в том же исследовании такое же соотношение 75/25: так выглядит любое
  снижение веса. И lean mass ≠ мышцы (наш же FAQ).
- **Что advisory одобряет сканирование телефоном.** Там одна фраза о том, что такие методы «being developed
  and validated», со ссылкой на чужое исследование, не на FitXpress.
- **GPhC.** Требование независимой проверки веса и BMI (февраль 2025) — это боль страницы BMI verification,
  не GLP-1 страницы. И осторожно: в обзоре GPhC за апрель 2026 жалобы на «photographs that could be easily
  manipulated» и на просьбы прислать фото в обтягивающей одежде записаны как проблемы. Никаких «meets GPhC
  requirements».
- **«43% of employers cover GLP-1s»** (это только компании с 5 000+ сотрудников) и **«1 in 12 stay on
  treatment»** (данные 2021 года, сейчас удержание выше) как текущие цифры.

### Блок проблемы (EN, так он стоит в HTML)

**Eyebrow:** The problem

## What does a GLP-1 program miss when it tracks only weight?

Most patients stop GLP-1 treatment within a year. While they stay, a weight entered at home shows how much
a patient lost, but not how much of that loss was fat and how much was lean mass.

| 64.8% | About 25% | 34% |
|---|---|---|
| of US adults without type 2 diabetes who started a GLP-1 medication stopped within one year. Greater weight loss was associated with staying on treatment. [JAMA Network Open, "Discontinuation and Reinitiation of Dual-Labeled GLP-1 Receptor Agonists Among US Adults With Overweight or Obesity"](https://pmc.ncbi.nlm.nih.gov/articles/PMC11786232/) | of the weight participants lost in a 72-week trial was lean mass, and about 75% was fat mass, measured by dual-energy X-ray absorptiometry (DXA). [Diabetes, Obesity and Metabolism, "Body composition changes during weight reduction with tirzepatide in the SURMOUNT-1 study"](https://pmc.ncbi.nlm.nih.gov/articles/PMC11965027/) | of US employers with 200 or more workers that cover GLP-1s for weight loss require a dietitian, case manager, therapist or lifestyle program for coverage. [KFF, 2025 Employer Health Benefits Survey](https://www.kff.org/health-costs/2025-employer-health-benefits-survey/) |

A 2025 [joint advisory](https://pmc.ncbi.nlm.nih.gov/articles/PMC12304835/) from four US obesity and
nutrition societies includes body composition assessment in the exam before GLP-1 therapy. Between clinic
or DXA visits, a remote program that tracks only weight has one number per check-in to work with. For a
program paid per active patient, each patient who stops in the first year is revenue it does not earn
back.


*Почему так:* вопросный H2 (правило регистра), первое предложение — ответ, каждая цифра с выводом для
покупателя, подпись источника в формате «Publisher, study name» со ссылкой на первоисточник, последнее
предложение — во что пробел обходится программе. Препарат назван только в подписи источника (название статьи), в самом тексте его нет, как в статье
19.09. Если нужен UK-акцент, третья карточка меняется на ссылку на страницу BMI verification.

### Куда ещё протянуть боль по странице

- **Hero**: первое предложение сейчас про точность. Лучше про то, что программа получает: «Show patients
  and care teams measured change at every check-in, including waist and body composition estimates the
  scale cannot show.»
- **Мок записи**: строка «The scale moved 0.3 kg. The waist moved 3.4 cm» — это и есть боль №2 в одной
  картинке. Пусть блок проблемы на неё опирается, а не повторяет.
- **Карточка «Records ready for outcomes reporting»** держится на боли №3, но со смягчением: «Structured,
  timestamped records the program can use when reporting to employers and payers.»
- **Пилот**: добавить метрику, которая отвечает на боль №1 — удержание на терапии против сравнительной
  когорты, критерии согласованы до старта (как в фитнес-финале).

## Структура: что сократить

Сейчас ~2 150 видимых слов при бюджете 1 100–1 600 и 11 FAQ при норме 4–6. Страница делает работу статьи.

1. **«Why 3DLOOK» (9 карточек) разложить по местам и убрать блок.** «Since 2016» и «100+ clients» уходят в
   подпись под логотипами, white-label в полосу фактов, поддержка в цены. «99.5% uptime», «2 days» и
   «9+ years / 150,000+ photographs» в блоке не продают GLP-1 программе (blog test), а у первых двух нет
   источника (см. ниже).
2. **Точность после «как работает» и записи скана, вместе с данными на одном экране**, как в фитнесе:
   вопросный H2 «How accurate is FitXpress for progress tracking, and how is patient data handled?»,
   ответ первым предложением, две цифры (< 1 cm и 96-97%), одно предложение о методе, ссылка на статью о
   точности.
3. **Данные: 7 карточек → 5 строк** (Photos · Identifiers · HIPAA/BAA для US или GDPR · Encryption ·
   Model training) и ссылка на trust FAQ с privacy-контактом. Регион, удаление по scan ID, SOC 2, FDA и
   DPA живут в trust FAQ.
4. **Сравнение: 7 колонок → 4-5.** Self-reported weight, connected scale, clinic BIA или DXA, FitXpress.
   Tape and calipers и progress photos можно слить или убрать. На мобильном таблица становится карточками.
5. **FAQ: 11 → 4-6** (в HTML 5). Оставить: «Does FitXpress measure muscle loss?» (честный ответ, мостик к
   статье о потере мышц), «Does FitXpress replace DXA or clinic body composition checks?», «Can FitXpress
   confirm BMI eligibility for a prescription?» (хорошо: отправляет на страницу BMI verification, один интент
   на один URL) и одну интеграционную со ссылкой на API-документацию. Добавить GEO-вопрос из карты ключей:
   «How can a GLP-1 weight-loss clinic track patient body composition remotely?». FDA, BAA и SOC 2 закрывает
   ссылка на trust FAQ.
6. **Карточки ценности: 6 → 4.** «A baseline for every follow-up» повторяет шаги, Smart Scales уходит в
   запись скана как predicted weight.

## Факты: жёсткие запреты и то, чему нет источника

Почти всё это уже было в фитнес-разборе 02.10 и 06.10, поэтому коротко:

1. **«with 95%+ consistency»** — жёсткий запрет (proof-points: INTERNAL ONLY, DO NOT PUBLISH). Остаётся
   < 1 cm.
2. **«No personal identifiers are processed»** — запрещено с 18.09 (trust FAQ: фото и измерения могут быть
   персональными данными). Каноническая строка: «Scan records use anonymized, randomly generated
   identifiers.»
3. **99.5% uptime, «2 days», React Native, вебхуки без ретраев, «no separate sandbox / trial account»** —
   источника нет; React Native tech-spec прямо запрещает. Публичный триал мы не предлагаем (с 27.09 только
   «Book a demo»).
4. **Бейдж «HIPAA Pending confirmation»** — внутренняя пометка попала в вёрстку.
5. **Захват:** «RTPV corrects framing… reduces retakes», «Clothing Detector correct pose, framing and
   clothing… with no manual review», «Pose, framing and clothing checks passed» в подписи мока, «clothing
   classification» в записи. С 07.10 до ответа продукта пишем: RTPV «gives pose and framing guidance during
   capture», а запись возвращает «processing status and timestamps». Классы одежды — внутренние.
6. **«3D body model for each scan»** — на живом /pricing/ в Starter 3D-модели нет; 3D Body progress
   tracking и 3D Goal Visualization только в Pro.
7. **Smart Scales** («Misreported weight flagged… before the prescriber approves») — функция в бете, а
   проверка перед назначением — это работа страницы BMI verification. На GLP-1 странице: «predicted weight»
   как в /pricing/, без «before the prescriber approves», со ссылкой на BMI verification.
8. **GDPR** — каноническое предложение дословно: «In most enterprise deployments, the customer acts as the
   data controller and 3DLOOK acts as the data processor under GDPR.» Сейчас хедж срезан во втором месте.
9. **Регион** — «primarily in US-West-2 and partially in US-East-1», или просто ссылка на trust FAQ. «No
   European region is available today» и «Self-serve deletion isn't available today» на продающей странице
   не нужны.
10. **Условия точности**: «height entered within 2 cm», «not published by body shape or skin tone», «Lean
    mass has not been validated against DXA in a published study», «Two gender options», «wheelchair users
    or amputees» — этого нет в каноне точности. Канон: популяция 16-78 лет, 150-220 cm, 38-210 kg, US и
    Европа, «Performance outside this scope has not been characterized.»
11. **«FitXpress is the only method here…»**, «replacing tape and caliper checks», «Records ready for
    outcomes reporting… to payers and employers» — утверждения без доказательства. Первое убрать, второе и
    третье смягчить (guardrail #1: «can support outcomes reporting»).
12. **«A 30-minute walkthrough / demo»** — длительность обещает sales, не страница (как в фитнесе).

## Форма, SEO, техника

- **H1** «Accurate at-home body measurements…» продаёт точность (CLAUDE.md §3: продаём результат и
  workflow, не точность) и без продукта. Два утверждённых варианта: «FitXpress for GLP-1 programs: [результат]»
  или форма «мобильная альтернатива известному методу» (как в фитнесе). Главный ключ по карте:
  `body composition tracking for GLP-1 programs`, его нет ни в title, ни в H1.
- **URL**: в черновике `/fitxpress/for-glp-1-weight-management/`, в карте лендингов
  `/fitxpress/for-glp-1-programs/`. Статьи хаба ссылаются по карте, нужен один вариант.
- **3 мёртвые ссылки (404)**: `body-composition-tools-remote-glp-1-clinics` → живая
  `/content-hub/top-7-remote-body-composition-tools-glp-1-clinics/` (якоря `#buyer-checklist` там нет);
  `data-privacy-security-regulatory-faq-fitxpress` → `/content-hub/fitxpress-data-privacy-security-regulatory-faq/`;
  `glp-1-market-growth-patient-progress-tracking` → хаб `/content-hub/glp-1-market/`.
- **«You/your» 19,8 на 1 000 слов** при лимите 12,5. Не расшифрованы при первом упоминании GLP-1 (в H1),
  ID, FDA, SOC 2.
- **Шрифты** Manrope и Space Grotesk → Satoshi (DESIGN.md).
- **Форма**: поля «program type» и «approximate active patients» — это своя форма. Все FX-страницы
  используют общую `FX | LP | Demo` (там уже есть «Expected monthly scan volume»).

## Что хорошо, оставить

- Мок записи пациента: «The scale moved 0.3 kg. The waist moved 3.4 cm» — лучший носитель боли на
  странице, он же подводка к блоку проблемы.
- Честный FAQ про мышцы: lean mass ≠ muscle. Это и граница, и GEO-ответ.
- Рамка «DXA и BIA на milestone-визитах, FitXpress между ними» — снимает главное возражение клинической
  команды.
- Метрики пилота: capture completion, record consistency, clinician review time. Добавить к ним
  удержание против сравнительной когорты, как в фитнесе.
- Граница «FitXpress is not a medical device… treatment decisions remain with the care team».
- Цены Starter и Pro совпадают с живым /pricing/ (проверено 07.10); Custom стоит назвать как на сайте —
  Personalized.

## Вопросы

- Ника: откуда снова 95%+, 99.5%, «2 days», React Native, вебхуки и условия точности? Если есть
  подтверждение продукта, сначала вносим в tech-spec и proof-points, потом на страницу.
- Открыто: URL (`for-glp-1-programs` по карте или `for-glp-1-weight-management`) и H1.
