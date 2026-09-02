<!-- PROVENANCE, added 2026-09-02 -->
> **This file was written while the replies were misfiled under
> `2026-07-16-au-telehealth`.** Closely campaign 138392 belongs to THIS folder: its
> `contact_source` records the header of `closelyhq-import-v3.csv` (224 rows, every
> `linkedin_url` present), while 07-16's own import is 253 rows with `linkedin_url` blank
> in every one — a file that could never have been uploaded. All 5 repliers are in this
> folder's import and none in 07-16's. The analysis below is about the right people; only
> its filing was wrong, and any sentence that names 07-16 or its 4-touch `messages/`
> should be read against this folder's `messages-v3/` instead.

---
campaign: 2026-07-16-au-telehealth
profile: vadim
product: fitxpress
market: Australia
analyzed: 2026-09-02
metrics_source: metrics-final.json (closely.io drill, pulled 2026-09-02T21:10:36Z, campaign 138392)
list_of_record: ../2026-07-27-australia-telehealth/closelyhq-import-v3.csv (224 строки) — НЕ closelyhq-import.csv из этой папки
status: campaign STILL ACTIVE — 140 of 223 contacts (63%) are mid-sequence
---

# Campaign Post-Mortem — 2026-07-16-au-telehealth

> **Все знаменатели — из `metrics-final.json`** (собственные счётчики событий Closely).
> Колонка `sent` из `outbound-registry.py status` не используется: она показывает 0 для этой
> папки и 224 для папки `2026-07-27-australia-telehealth` — это строки импорта, не отправки.
> Реальные отправки: 220 инвайтов, 61 сообщение.
>
> **Уровень выводов.** Ответов 11 строк от **5 уникальных людей** → полоса «5-14»:
> направленные наблюдения с оговоркой «предварительно, N=X», годятся как гипотеза для
> следующей кампании, не как решение. Исключение — acceptance rate: знаменатель 220 инвайтов,
> вывод статистически прочный. Процентов без знаменателя ниже нет.
>
> **Считаем по людям, не по строкам.** 6 «interested»-строк — это 2 человека из одной
> компании (Mosh). Строчный процент («55% interested») завышает картину примерно втрое.

## TL;DR (3 строки)
1. **Потеря — на стадии инвайта.** 38/220 (17.3%) приняли против цели 25% и против 25-31% у
   трёх других профилей; после принятия всё в норме — 5/38 (13.2%) человек ответили, как
   UK 13/69 (18.8%) и Israel 34/186 (18.3%). Инвайты уходили **без записки**, значит текст
   на acceptance не влиял физически.
2. **Записка не виновата, и это проверяемо:** файл с запиской (`closelyhq-import.csv`,
   253 строки) не содержит ни одного имени и ни одного LinkedIn-URL, то есть загружен быть не
   мог; в Closely на шаге `connection_message` текст пуст — и так во всех семи вытянутых
   кампаниях, включая три с 25-31%. Контроль: US-кампания шла вообще без записки и получила
   ещё более низкие 15.9%.
3. **Весь живой результат — из 22 инвайтов, а не из 202.** Mosh (12 инвайтов) дал двух
   interested (CPO с забронированным звонком с нашим CEO + Medical Director), а 202 инвайта в
   Medibank/Bupa/HCF дали 3 ответа и **ноль** interested. При этом 33 из 224 инвайтов ушли
   людям с явным вердиктом **FAIL** (legal, procurement, property, cyber, dental/optical).

## Hypothesis vs reality

| Metric | Target | Actual | Verdict |
|--------|--------|--------|---------|
| Acceptance rate | ≥ 25% | **38/220 = 17.3%** | ✗ (95% CI 12.3-22.3%) |
| Reply rate (spec: replies/accepted) | ≥ 5% | **5/38 = 13.2%** (люди) | ✓ |
| — то же на отправленных сообщениях | — | 5/61 = 8.2% | справочно (метрика Closely) |
| — то же на инвайтах | — | 5/220 = 2.3% | справочно |
| Positive replies (interested + question) | ≥ 10 | **2 человека** (2/38 accepted = 5.3%); 7 из 11 строк | ✗ |
| Qualified leads | ≥ 3 | **2 человека в 1 аккаунте** (Mosh) | ✗ |
| Negative reply rate | — | **0/38 = 0%** (1 вежливый decline) | нечего диагностировать |
| CPL | — | **нет данных о затратах** | 220 инвайтов / 1 qualified аккаунт |

Полная воронка: 223 контакта → 220 инвайтов (3 `connection_sent_error`) → 38 accepted →
33 человека получили DM-1, 28 получили DM-2 (всего 61 сообщение) → 11 ответов от 5 человек.
Профильных визитов 390, лайков постов 22.

**Кампания не закончена:** завершены 83/223 контакта, 140 (63%) ещё в секвенции.

**Три знаменателя из прошлых файлов надо перестать использовать:**
`responses-summary.md` считает «11 ответов на 443 contacted» — 443 это цифра из гипотезы
(до валидации), реально касаний было 220 инвайтов и 61 сообщение. `hypothesis.md` обещала
443 контакта по 14 компаниям; валидация дала 439 человек, импорт — 224, отправку — 220.

## Что здесь на самом деле запускалось (без этого остальное не читается)

Артефакты в этой папке **не соответствуют** тому, что ушло в LinkedIn. Проверено по
`campaign.contact_source` внутри `metrics-final.json` (это отдаёт сам Closely):

| Что | В этой папке | Что реально в Closely 138392 |
|---|---|---|
| Файл импорта | `closelyhq-import.csv`, 253 строки, колонки `message_step1..4`, **0 имён, 0 URL** | колонки `person_id, first_name, last_name, title, company, linkedin_url, segment, angle, priority, message_m1, message_m2` |
| Совпадает с | — | `../2026-07-27-australia-telehealth/closelyhq-import-v3.csv` — 224 строки, 0 пропущенных URL, header совпадает 1:1 |
| Копия | `messages/*.md` — старая 4-касательная (записка → Welcome → Follow-up → Breakup) | 2 сообщения: `{custom_6711}` и `{custom_6712}` = `message_m1` / `message_m2` |
| Люди | 439 валидированных | 224 импортированных, 220 инвайтов; все 5 ответивших находятся в v3 по URL |
| Реестр | записи о `2026-07-16-au-telehealth` нет | 224 человека записаны под слагом `2026-07-27-australia-telehealth` |

Вывод: **список и копия «of record» для этой кампании лежат в папке `2026-07-27-australia-telehealth`**,
а `messages/` в этой папке — нереализованный черновик. Дальше весь разбор считает по v3.

**Побочная поправка к step 8:** колонка `which_message_replied_to` в `responses-raw.csv`
для James Taylor идёт 3 → 2 → 1 → 1 по возрастанию даты, то есть это не индекс касания, и
«ответил на message 3» из `responses-summary.md` в двухсообщенческой секвенции существовать не
может. Надёжны только шаговые счётчики Closely: DM-1 — 2 ответа на 33 отправки,
DM-2 — 2 на 28, ещё 1 ответ отнесён к шагу `connection_message`.

## Что работало

### Best-performing message angle
Предварительно, N=5 ответивших человек; знаменатели — инвайты (per-angle acceptance Closely
не отдаёт, поэтому angle и acceptance тут не разделить).

| Angle | Инвайтов (v3) | Ответивших | Из них |
|---|---|---|---|
| `clinical-operations` | 28 | **3/28 (10.7%)** | 1 interested (Mosh Medical Director), 1 referral (Bupa GM), 1 decline |
| `product-integration` | 40 | **1/40 (2.5%)** | 1 interested (Mosh CPO) — **лучший лид кампании** |
| `digital-health-strategy` | 80 | **1/80 (1.3%)** | 1 maybe-later (Bupa, P3) |
| `member-retention` | 29 | 0/29 | — |
| `operational-scale` | 18 | 0/18 | — |
| `technical-integration` | 10 | 0/10 | — |
| `wellness-programs` / `executive-outcomes` / `data-privacy` | 7 / 7 / 5 | 0 | — |

- **`clinical-operations` — единственный angle, давший больше одного ответа.** Работающая
  формулировка — прямой вопрос про рабочий процесс, без выдуманного контекста:
  > «Hi Tushar, Quick note - curious how Mosh's clinical operations handle remote patient
  > assessments at scale…» → «I'd be interested to talk on this matter. Are you free 12pm
  > this wednesday for a google meet?»
  Гипотеза почему: у Medical Director вопрос попадает в его собственную операционную боль,
  и ответ не требует принимать решение — только рассказать, как у них устроено.
- **`product-integration` дал самый продвинутый лид** (James Taylor, CPO Mosh →
  забронированный звонок с нашим CEO):
  > «Good timing Vadim - we've been looking at some of the problems your company might be
  > able to help us with recently around ensuring that the right patients are using our
  > services, and helping them understand the progress they've been making in their weight
  > loss journey.»
  Гипотеза почему: «Good timing» — это про внутренний триггер у них, а не про нашу копию.
  Ниже, в оговорке по атрибуции, есть основание считать этот контакт не совсем холодным.

### Best-converting company segments
Предварительно, N=5. Знаменатель — инвайты по сегменту из v3.

| Сегмент | Инвайтов | Ответивших | Interested |
|---|---|---|---|
| **`digital-health`** (Mosh 12, InstantScripts 5, Qoctor 3, Medmate 1, Hopstep 1) | **22** | **2/22 (9.1%)** | **2/22 (9.1%)** |
| `enterprise` (Medibank 92, Bupa 64, HCF 46) | **202** | 3/202 (1.5%) | **0/202 (0%)** |

- **Mosh — 2 ответивших из 12 инвайтов, оба interested, оба P1, из них один довёл до звонка
  с нашим CEO.** Это цифровая GLP-1/telehealth платформа: короткая цепочка принятия решений,
  C-level реально владеет продуктом, и наша ценность у них монетизируется сразу
  (patient-fit verification + прогресс похудения).
- **Три «Big 3» страховщика — 202 инвайта, 0 interested.** Лучшее, что оттуда пришло —
  «I'll send your details across to my product team» (Bridget Lodge, GM Health and Wellbeing,
  Bupa). Гипотеза почему: у страховщика решение размазано по продуктовым командам, вендорский
  инвайт от незнакомого человека — фон, и любое движение идёт через внутренний перевод, а не
  через того, кому написали.
- **Это самое сильное наблюдение кампании по размеру эффекта** (9.1% против 1.5% на ответах;
  9.1% против 0% на interested), но N=5 — поэтому это приоритет следующего списка, а не
  доказанный закон.

### Best-performing personas (titles)
- **Оба interested — C-level/клинический руководитель в компании-платформе:** Chief Product
  Officer и Medical Director, оба P1. Referral пришёл от GM Health and Wellbeing (P2),
  maybe-later — от Group Senior Manager Strategy (P3), decline — от P3.
- **Приоритет сработал в правильном порядке:** P1 → interested, P2 → referral, P3 → maybe-later
  и decline. Предварительно, N=5 — но это ровно то, для чего приоритеты и нужны.
- **Одна компания = два стейкхолдера — рабочая тактика.** Mosh отвечали двое независимо
  (CPO и Medical Director), с разными angle. Именно это и дало аккаунту глубину.

## Что не работало

### Worst-performing angle
- **`digital-health-strategy`: 1 ответ (maybe-later) на 80 инвайтов** — 36% всей ёмкости
  кампании на самый абстрактный из angle. Гипотеза почему: «стратегический дифференциатор»
  адресован роли, которая ничего не внедряет; у страховщика это ещё и типовая тема, которой
  их заваливают все вендоры. Дешёвая замена — переливать эту ёмкость в `clinical-operations`
  (прямой вопрос про процесс).
- **`member-retention` 0/29 и `operational-scale` 0/18** — ноль на заметных знаменателях;
  оба уходили преимущественно в enterprise-сегмент, так что отделить «плохой angle» от
  «плохого сегмента» на этих данных нельзя.

### Pattern in negative responses
- **0 негативных, 1 decline из 11 строк.** Тон и текст диагностировать не на чем.
- **Единственный decline — от человека, которого валидация не должна была пропустить:**
  Maria Ruberto, «Member - Mental Health Reference Group», Medibank, P3 — это место в
  консультативной панели, а не роль в компании. Ответ «No thank you.» — корректная реакция
  на письмо, которое ей не должно было прийти. Это не паттерн по одному человеку, это
  симптом того, что описано ниже.
- **Фабрикованный контекст в 100 из 224 первых сообщений (45%).** Генератор ротировал ~20
  зачинов, из которых «Circling back» (17 писем), «Saw your post» (13), «Noticed your
  background» (12), «Came across your work» (11), «Saw your activity» (10), «Spotted
  something» (10), «Got me thinking» (10) утверждают взаимодействие, которого не было —
  «Circling back» в самом первом сообщении человеку, которому мы никогда не писали. На
  acceptance это повлиять не могло (инвайты без записки), на ответы — могло. Сравните с
  US-кампанией, где зачины привязаны к реальной роли человека («Noticed your research
  background at Noom», «Quick note given your engineering…»).

### Companies / people we shouldn't have included
- **33 из 224 инвайтов (15%) ушли людям, которых валидатор явно завалил (FAIL).** Разбивка:
  legal/privacy 6 (Head of Privacy Legal, Head of Legal - Customer, Head of Legal - Providers,
  Head of Legal Operations, Head of Wellbeing Legal, Head of Legal and Compliance/HCF Privacy
  Officer), procurement 3, communications 3, finance 2, property 1, cyber-defence 1,
  dental/optical/hearing 2, IT/data 4, прочие manager-роли 11. Причина в реестре у каждого
  написана словами: «Director-level non-health role at insurer; not in FitXpress buying chain».
- **Два инвайта прямо противоречат anti-cases собственной гипотезы** («Dental/optical-only
  divisions — excluded»): Director Bupa Dental, Optical & Hearing и Head of Technology,
  Dental Optical and Hearing.
- **Ещё 83 инвайта — WEAK-тир.** Итого PASS всего 108 из 224 (48%): меньше половины ёмкости
  ушло людям, которых валидация признала годными.
- **Hopstep** — платформа рекрутинга в здравоохранении, а не telehealth-провайдер; в реестре
  висит как покрытая `vadim`. Убрать из будущих AU-списков.
- **Расхождение тайтлов между v3 и валидацией.** У «Head of Trust and Ethics» (Medibank) в
  причине записано «National Property Manager, Group Property»; у «Head of Health Policy» —
  «branch manager». То есть в отправку ушёл тайтл, отличный от того, по которому человека
  судили, а тайтл — это ещё и вход для персонализации первой строки.

## Инвайт-стадия: почему 17.3%, а не 25% (главный вопрос кампании)

Единственный раздел с прочной статистикой: знаменатель — сотни инвайтов, не 5 ответов.

| Профиль / кампания | Closely account | Инвайтов | Принято | Acceptance (95% CI) |
|---|---|---|---|---|
| **vadim / AU telehealth** | 25382 | 220 | 38 | **17.3%** (12.3-22.3) |
| **nick / US digital fitness** | 34879 | 245 | 39 | **15.9%** (11.3-20.5) |
| olena / EU weightloss | 35141 | 292 | 73 | 25.0% (20.0-30.0) |
| katerina / UK digital health | 23972 | 258 | 69 | 26.7% (21.3-32.1) |
| katya / Israel telehealth | 25040 | 608 | 186 | 30.6% (26.9-34.3) |

Объединённо: **77/465 (16.6%) с аккаунтов `vadim` + `nick` против 328/1158 (28.3%) с трёх
остальных** — разница 11.8 п.п., z = 5.4, p ≈ 6·10⁻⁸. Не артефакт малой выборки.

### Версия «виновата написанная записка» — не подтверждается
Это была основная рабочая версия по AU, и её надо снять с повестки:
1. **Записки в кампании не видно вообще.** Шаг `connection_message` в 138392 имеет
   `{'connection_message': ''}`. Точно так же — пусто — во всех семи вытянутых кампаниях,
   включая три с acceptance 25-31%. Значит поле либо всегда пустое (тогда оно не различает
   группы и как улика бесполезно), либо записок не было ни у кого.
2. **Файл с запиской физически не мог быть загружен:** `closelyhq-import.csv` в этой папке —
   253 строки, в которых 253 пустых `first_name`, 253 пустых `last_name` и 253 пустых
   `linkedin_url`. Closely без URL профиля инвайт отправить не может. Header реально
   загруженного файла (по `contact_source` самого Closely) — из v3, где записки нет вовсе,
   а есть только `message_m1` / `message_m2`.
3. **Контроль:** US-кампания шла без записки, 2 сообщения, другой профиль — и дала
   **15.9%**, то есть ниже AU. Убрать записку и получить хуже — против версии.
4. **Testable claim, если нужна полная уверенность** (низкий приоритет): 2 плеча по
   **200 инвайтов**, один профиль, один список, одна неделя — с запиской и без. Меньше 200
   на плечо не имеет смысла: ожидаемый эффект меньше разброса.

### Что ещё проверено и разрыв НЕ объясняет
- **Размер и концентрация компаний.** Israel бил в гигантов (Clalit 66 контактов, Maccabi 63)
  и дал 38/127 (29.9%) на своей агентской кампании 138170. AU бил в Big 3 и дал 17.3%.
  Enterprise-состав списка сам по себе группы не разделяет.
- **Сеньорность.** AU 65% VP/Head/Director, UK 74%, Israel 69% — состав похож.
- **Зрелость кампании.** UK 139205 запущена 2026-08-05, завершена на 12%, даёт 24.4%; AU
  запущена 2026-07-28, завершена на 37%, даёт 17.3%. Незрелость не объясняет.
- **Структура секвенции.** У всех семи кампаний в Closely одинаковый каркас:
  `profile_view → connection_message → condition(if_connected) → DM-1 → post_reaction → DM-2`.
- **Копия.** До принятия инвайта её никто не видит. Плюс `reply-on-accepted` у AU
  5/38 (13.2%) статистически неотличим от UK 13/69 (18.8%) и Israel 34/186 (18.3%).

### Что остаётся
**H1 (ведущая): сам отправляющий профиль.** Пять аккаунтов — пять значений acceptance, и
линия разреза проходит ровно по аккаунтам, а не по гео, вертикали, размеру целей или
структуре секвенции. Возраст аккаунта в Closely не причина: у `olena` самый свежий id (35141)
и 25.0%. Для `vadim` есть специфика, которую стоит проверить в первую очередь: это
маркетинговый профиль (`social-profiles-config.md`: «Vadim Bilan (Marketing Manager)»),
который пишет C-level австралийских страховщиков без общего окружения и региональной привязки.

**H2 (неотделимая конкурирующая): рынок/сегмент.** 90% инвайтов ушли сотрудникам трёх
крупнейших страховщиков Австралии — самая «обстрелянная» вендорами аудитория рынка. По нашей
же гео-дисциплине профиль ↔ рынок связаны 1:1, поэтому «профиль» и «AU-страховщики» в этих
данных разделить нельзя, пока один список не уйдёт с двух профилей.

**H3 (аддитивная): качество списка.** 33 FAIL + 83 WEAK из 224. Люди из legal, procurement и
property не принимают вендорские инвайты не потому, что профиль плохой, а потому, что им
писать не следовало. Это не объясняет 11.8 п.п. целиком, но объясняет часть и исправляется
бесплатно.

### Оговорка по атрибуции лучшего лида
`closely_contact_id` в наших выгрузках монотонен по времени: у ответивших в апрельской
израильской кампании 76.5-83.8M, в июльской EU 83.7M, в этой AU 84.03M, в августовской
UK 84.38-84.47M, в US 84.74M. **У James Taylor id = 66 123 540** — то есть его контакт в
Closely создан задолго до всех остальных, включая апрель 2026; у остальных четырёх
ответивших этой кампании id 84 036 5xx. Это согласуется и с тем, что один ответ Closely
отнёс к шагу `connection_message`, чего при инвайте без записки к незнакомому человеку быть
не может. **Предварительно: самый продвинутый лид кампании (CPO Mosh, звонок с CEO) — скорее
повторное касание уже существующего контакта, чем результат холодного инвайта.** Проверяется
за минуту в UI Closely / в его переписке; до проверки не записывать этот звонок в заслугу
холодной части кампании.

## Learnings → next hypothesis

### Confirm
- **AU digital-health / GLP-1 платформы — рабочий подсегмент.** 2/22 инвайтов дали interested,
  оба P1, один довёл до звонка с CEO. Заносим в core ICP приоритетом для профиля `vadim`:
  Mosh-паттерн (телехелс-платформа с GLP-1 программой, C-level владеет продуктом).
- **Копия и таргетинг «после принятия» работают:** 5/38 (13.2%) — на уровне UK и Israel.
- **`clinical-operations` как прямой вопрос про процесс** — единственный angle с более чем
  одним ответом (3/28), и именно он открыл Bupa через referral.
- **Приоритеты P1/P2/P3 предсказывают качество ответа** (P1 → interested, P2 → referral,
  P3 → maybe-later/decline). Предварительно, N=5.
- **Мульти-стейкхолдерный заход в один аккаунт** (2 роли, 2 разных angle) — то, что дало
  Mosh глубину.

### Reject
- **Широкий title-sweep по «Big 3» страховщикам Австралии.** 202 инвайта → 0 interested.
  Не исключать компании, но менять способ входа: только named champion / referral-путь и
  10-15 человек максимум, а не 202.
- **`digital-health-strategy` как основной angle** (1/80 при 36% ёмкости).
- **Отправка людям с вердиктом FAIL.** 33 инвайта, из них единственный decline кампании.
  Это должно быть жёстким гейтом импортёра, а не решением на глазок.
- **Фабрикованные зачины** («Circling back» / «Saw your post» / «Spotted something» в первом
  же сообщении) — 45% первых сообщений. Не доказано, что они вредят, но они уже нарушают
  правило «не заявлять то, чего не было», а альтернатива (вопрос про процесс) — единственное,
  что здесь дало больше одного ответа.
- **Артефакты этой папки как источник правды.** Список, копия и реестр этой кампании живут
  под слагом `2026-07-27-australia-telehealth`.

### New hypotheses to test
- **H1 (главная, дешёвая):** acceptance определяется отправляющим профилем, а не списком.
  Тест: один AU-список делится 50/50 между `vadim` и профилем с 25%+, одинаковая копия,
  одна неделя, **≈200 инвайтов на плечо**. До теста — бесплатный аудит профиля Vadim: число
  связей, headline (Marketing Manager vs BD/партнёрская формулировка), активность,
  объём висящих pending-инвайтов, наличие Sales Nav, доля общих связей в AU.
- **H2:** «digital-health платформы принимают и отвечают, страховщики — нет». Тест: следующая
  AU-кампания целиком из платформ (Eucalyptus/Juniper, Hub Health, Updoc, Doctors on Demand,
  Rosemary Health и т.п.), 120-150 инвайтов, сравнить acceptance и reply-on-accepted с этими
  17.3% / 13.2%.
- **H3:** `clinical-operations`-вопрос про процесс > стратегический angle. Тест: 2 плеча по
  60 человек внутри одного сегмента.
- **H4 (низкий приоритет):** записка на инвайте влияет на acceptance. 2×200, один профиль,
  один список. Ставить только после H1 — сейчас данные против этой версии.
- **H5:** жёсткий гейт «в импорт только PASS» поднимает и acceptance, и долю осмысленных
  ответов. Тест: следующая кампания без FAIL/WEAK в списке, сравнить acceptance с 17.3%.

## Recommendations for next campaign
1. **Не переписывать копию ради acceptance — сначала профиль.** Аудит LinkedIn-профиля Vadim
   до следующего AU-запуска, затем split-тест H1 на 200 инвайтов на плечо.
2. **Перевернуть пропорцию сегментов:** AU-платформы (digital-health / GLP-1 / telehealth) —
   основа списка; страховщики — только через named champion, ≤15 человек на группу.
3. **Гейт импортёра: ни одного FAIL в файле, WEAK — только как помеченный добор.** Сейчас
   PASS всего 48% ёмкости.
4. **Запретить зачины с фабрикованным контекстом** в message-sequencer (это лечится тем же
   механизмом, что уже держит banned-words: `Circling back`, `Saw your post`,
   `Saw your activity`, `Spotted something`, `Came across your work`, `Got me thinking`,
   `Noticed your background`, `Made me think` — в первом сообщении холодному контакту).
5. **Сверять тайтл в файле импорта с тайтлом, по которому валидировали** — сейчас есть
   расхождения, а тайтл идёт в первую строку сообщения.
6. **Закрыть петлю по Mosh:** подтвердить, состоялся ли звонок с CEO (James Taylor), ответить
   Tushar Yadav про James и перебронировать его Google Meet — приглашение до него не дошло,
   интерес не пропадал.
7. **Проверить историю James Taylor в Closely** (id 66 123 540) и решить, считать ли этот лид
   результатом кампании; от этого зависит, чему учит эта кампания.
8. **Свести две AU-папки в одну.** Пока `2026-07-16-au-telehealth` держит гипотезу, ответы и
   метрики, а `2026-07-27-australia-telehealth` — список, копию и запись в реестре, любой
   разбор начинается с 40 минут форензики, а `status` показывает две недоделанные кампании
   вместо одной готовой.

## Updates to `CLAUDE.md`
Конкретный diff (сам файл не правлю — это менеджерское решение):

```diff
 ## 11. Метрики
-- **Outbound:** acceptance rate, reply rate, positive reply rate, qualified leads, передано в sales (per-product)
+- **Outbound:** acceptance rate, reply rate, positive reply rate, qualified leads, передано в sales (per-product)
+  - acceptance rate ведём **per sending profile**, а не только per campaign: инвайты уходят
+    без записки, поэтому это метрика аккаунта, а не копии.
+  - **порог:** acceptance < 20% на ≥150 инвайтах ⇒ кампанию не «лечим текстом», а
+    останавливаем и проверяем профиль (связи, headline, активность, pending-инвайты, Sales Nav).
+    Замер 2026-09-02: vadim 38/220 (17.3%), nick 39/245 (15.9%) против olena 25.0%,
+    katerina 26.7%, katya 30.6% — разрыв 11.8 п.п., p ≈ 6·10⁻⁸.
+  - **reply rate считаем по людям, а не по строкам ответов**, и от `accepted`, а не от
+    «contacted» из гипотезы: 11 строк этой кампании — это 5 человек.
```

```diff
 ### FitXpress ICP
-- **Telehealth & weight loss / GLP-1:** virtual clinics, coaching apps, longitudinal/RPM programs. $2M+ revenue.
+- **Telehealth & weight loss / GLP-1:** virtual clinics, coaching apps, longitudinal/RPM programs. $2M+ revenue.
+  Для AU (профиль `vadim`) приоритет — цифровые платформы (Mosh-паттерн: 2/22 инвайтов →
+  interested, C-level владеет продуктом), а не «Big 3» страховщики: 202 инвайта в
+  Medibank/Bupa/HCF дали 0 interested (2026-07-16-au-telehealth). Страховщиков заводим только
+  через named champion / referral, ≤15 человек на группу.
```

```diff
 ## 5. Профили в социальных сетях
 Гіпотеза й список компаній кампанії мають відповідати ринку профілю (гео-дисципліна).
+**Побочный эффект дисциплины:** профиль ↔ рынок связаны 1:1, поэтому эффект профиля и
+эффект рынка в наших данных статистически неразделимы. Для диагностики acceptance
+разрешается ровно одно исключение: **split-тест одного списка между двумя профилями**
+(≈200 инвайтов на плечо), с явной пометкой в hypothesis.md.
```

## Updates to the exclusion registry

**Запись исходов в реестр по этой кампании ЗАБЛОКИРОВАНА — и это не JSON руками править.**
Проверено обеими штатными командами:

```
python3 scripts/outbound-registry.py reply --campaign 2026-07-16-au-telehealth --profile vadim
→ ✗ 2026-07-16-au-telehealth is not in vadim-registry.json — run `record` first.

python3 scripts/outbound-registry.py record --campaign 2026-07-16-au-telehealth --profile vadim --dry-run
→ import CSV has rows but no LinkedIn URLs — nothing to record.

python3 scripts/outbound-registry.py reply --campaign 2026-07-27-australia-telehealth --profile vadim
→ ✗ .../2026-07-27-australia-telehealth/responses-classified.csv does not exist
```

Причина: **люди записаны под слагом `2026-07-27-australia-telehealth` (224 человека, все 5
ответивших там есть, `reply` у всех пока `null`), а исходы лежат в этой папке.** `reply`
требует, чтобы реестровая запись и `responses-classified.csv` были под одним слагом.

**Что нужно сделать (одно из двух), после чего команда пройдёт:**
- перенести `responses-raw.csv` + `responses-classified.csv` в
  `2026-07-27-australia-telehealth/` и выполнить
  `python3 scripts/outbound-registry.py reply --campaign 2026-07-27-australia-telehealth --profile vadim`
  (в этой папке остаётся post-mortem и гипотеза; я в чужую папку не писал по условию задачи);
- либо добавить в `outbound-registry.py` алиас слагов (07-16 ↔ 07-27) и вызвать `reply` как есть.

**Уже подготовлено здесь:** в `responses-classified.csv` добавлена колонка `linkedin_url`
(значения из `responses-raw.csv` этой кампании по `person_id`, 11/11 совпали). Без неё `reply`
не находил людей вообще и **молча возвращал «0 registry people updated» с кодом выхода 0** —
ровно та тихая неработающая запись, из-за которой в реестрах месяцами стояло
`excluded_people: 0`. Системная правка нужна в пайплайне: `response-classifier` обязан
прокидывать `linkedin_url`, либо `cmd_reply` должен фолбэчить на `responses-raw.csv`
по `person_id`.

**Исходы, которые должны лечь в реестр** (для сверки после запуска команды):

| Человек | Компания | Категория |
|---|---|---|
| James Taylor (CPO) | Mosh | interested |
| Tushar Yadav (Medical Director) | Mosh | interested / question |
| Bridget Lodge (GM Health and Wellbeing) | Bupa Australia | referral |
| Roman Zaytsev (Group Senior Manager, Strategy) | Bupa Australia | maybe-later |
| Maria Ruberto (Member, Mental Health Reference Group) | Medibank | decline |

**Person-level — исключить из будущих кампаний:**
| Кого | Причина |
|---|---|
| Maria Ruberto (Medibank) | явный отказ + роль в консультативной панели, а не в компании |
| 33 контакта с вердиктом FAIL из v3 | legal 6, procurement 3, communications 3, IT/data 4, finance 2, dental/optical 2, property 1, cyber 1, прочие 11 — вне цепочки принятия решений; компании при этом остаются |
| Ben Boom, «Head of Technology, Dental Optical and Hearing» (Bupa) | прямое противоречие anti-cases гипотезы (dental/optical исключены) |

**Company-level:**
- `hopstep` (сейчас `active` под `vadim`) — платформа рекрутинга в здравоохранении, не ICP.
  Пометить как не-ICP, чтобы не всплывала в AU-списках.
- `medibank`, `medibank-private`, `medibank-health-solutions`, `amplar-health`,
  `bupa-australia`, `hcf-australia` — держать под `vadim`, но с пометкой: broad title-sweep
  отработан и дал 0 interested на 202 инвайта; следующий подход — только named champion.
- `mosh` — активный аккаунт с двумя вовлечёнными стейкхолдерами, из outbound вывести в sales.
- `instantscripts`, `qoctor`, `medmate` — 0 ответов на 9 инвайтов суммарно, слишком мало,
  чтобы что-то заключать; в следующем AU-списке дать им нормальный объём касаний.

## Открытые вопросы к Вадиму
1. Сводим две AU-папки в одну (и какая остаётся канонической)? Без этого запись исходов в
   реестр по этой кампании остаётся заблокированной.
2. Проверишь историю James Taylor в Closely (был ли он уже в контактах/связях до кампании)?
   От этого зависит, считаем ли мы лучший лид результатом холодного аутрича.
3. Аудит профиля Vadim делаешь сам, или сразу ставим split-тест H1 на 200 инвайтов на плечо?
4. Mosh: звонок с CEO состоялся? Tushar ждёт ответа и перебронировки — это одно сообщение.
