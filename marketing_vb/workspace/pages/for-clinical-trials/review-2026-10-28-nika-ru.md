---
product: fitxpress
type: vertical-page
vertical: clinical-trials
status: review
for: Nika (+ Asselya)
---

# Clinical trials: разбор трёх драфтов (28.10)

> Исправлено 28.10 после отправки: карточка 2 блока проблемы. Вместо одного исследования (5.98 см) — разброс по
> трём источникам, см. раздел 2.

Проверено по пайплайну страниц. Цифры сверены с первоисточниками, claims с `proof-points` / `compliance` /
`tech-spec`, угол с контент-планом хаба и картой ключей. Дальше детектор, рендер на 1280 и 375 px и слепые
судьи, по одному на каждую версию. Версии ниже называю по углу: **A** — v3 Ники (стандартизация по сайтам),
**B** — v2 Ники (дополнительный замер между визитами, white-label), **C** — v4 Асель (B после чата).

## Коротко

1. **Попадаем, но только в одну роль.** Мы модуль замеров внутри DCT-платформы или participant app:
   дополнительные обхваты между визитами, white-label, спонсор сам решает, как использовать данные. «Стандарт
   замера для исследования» мы не вытягиваем (раздел 1). Поэтому базой берём B (твоя v2) и правки C, а не A.
   Hero и value cards пишем для DCT-платформ.
2. **Боль надо переписать.** BELIEVE и 30-45% не держатся (раздел 2). Честная дыра другая: дома исследование
   уже получает вес, а обхваты нет. EMA просит талию как вторичный endpoint, а самозамер расходится с замером
   специалиста в среднем на 1-6 см, и в разных исследованиях в разную сторону. Черновик блока на английском в
   разделе 2.
3. **Что обязательно убрать:** React Native (во всех трёх), offline, webhooks, iOS 15, «2 см», «audit-ready»,
   BMI pre-check. Форму заменить на общую, заглушки удалить. В C вернуть канон «not a medical device» (раздел 3).
4. **Длина:** A ~3 150, B ~2 910, C ~2 070 при бюджете 1 100-1 600 и 4-6 FAQ. План сокращения в разделе 4.
5. **Слепые судьи:** A 48, B 52, C 46 из 100 при пороге 85. У всех трёх hard fails, у всех слабее всего
   sales argument и claims (раздел 6).

## 1. Попадаем ли мы в клинические исследования

Ника, сомнение по делу. Ответ зависит от того, что страница обещает.

**Роль «стандартного замера для спонсора» мы не вытягиваем.** FitXpress не медицинское изделие. В
исследованиях его никто не валидировал, а клиентов в этой вертикали у нас нет. FDA в guidance по digital
health technologies (декабрь 2023) возлагает на спонсора verification и validation, «fit for purpose» под
конкретное использование. Поэтому формулы «стандартизируем замеры по сайтам», «audit-ready records» и
«меньше dropout» спонсор прочитает как обещание, которое мы не докажем. Тем более что FDA сама держит
waist circumference во вторичных endpoints.

**Роль модуля замеров внутри DCT-платформы или participant app — да.** Это ровно версия B: дополнительный
замер между визитами, white-label через SDK, данные уходят в backend платформы, а решает, как их
использовать (exploratory, substudy, follow-up), спонсор. Здесь нам не нужно быть «лучше рулетки».
Нужно быть встраиваемыми, с понятными полями и честными границами. Этот угол защищаем, и хаб его не
занимает: в контент-плане DCT-интеграция стоит отдельной P1-статьёй, она ещё не написана.

**Поэтому базой берём B / C, а не A.** У A две проблемы помимо claims:

- Она пересказывает хаб. Контент-план отдаёт хабу «site-to-site variability, hybrid and remote check-ins,
  operational standardization, structured records, audit-readiness». На лендинге это не проходит blog test
  ни в одном блоке.
- Удалённый BMI pre-check ничего не добавляет. BMI у нас считается из введённых роста и веса, скан на него
  не влияет. Это та же ловушка, что CDC 40% на бариатрии.

**Покупатель.** Реальнее всего платформы: DCT, eCOA и participant-app вендоры как интеграционные
партнёры. Спонсор и CRO приходят через них. Спрос в поиске тоже у платформ: кластер «DCT platform» даёт
~410 запросов в месяц в US, CPC $12. **Решено: hero и value cards пишем для платформы.** Спонсору и CRO
остаются блок проблемы, сравнение методов и FAQ.

## 2. Боль и цифры: что подтверждается источниками

Полный разбор с цитатами и ссылками в файле `sources-problem-block.md` (EN). Сайт FDA режет наш сервер,
поэтому PDF читали с копий в Wayback, тексты совпадают с актуальными. Obesity guidance до сих пор draft.

**Цифры из драфтов:**

| Где | Утверждение | Вердикт |
|---|---|---|
| A | FDA: waist circumference «the procedure is not standardized» | Цитата дословная. Но у FDA три причины, и стандартизация съёмки закрывает только первую. Две другие: подкожный жир и низкая точность при BMI > 35 (в BELIEVE такой BMI был у 63% участников). Строка «with FitXpress, every site… produces the same record» сразу после цитаты читается так, будто мы снимаем возражение FDA. Не снимаем |
| A | 30-45% attrition (JAMA 2016) | Цифра верная, но это 28 исследований 5 старых препаратов. Связь с визитами в статье не показана, это наше додумывание. В свежих исследованиях иначе: STEP 1 (семаглутид) завершили 94.3%. Убрать |
| B | BELIEVE: 92.8% vs 71.8% жира | Это цифры пресс-релиза ADA, их сменила рецензируемая статья: Nature Medicine, март 2026, 92.3% vs 71.1% на 48-й неделе, по DXA, фаза 2. К тому же цифра работает на DXA: состав потерянного веса меряли DXA, а наш body fat — оценка. Как и 25% lean на GLP-1, она аргументирует за метод, которым мы не являемся. Убрать |
| B | FDA: DXA и MRI «expensive… multiple blinded, central readers», body composition в «representative subset» | Верно, но склеено из двух разделов (стр. 3 и 12). У FDA «representative sample» и «by DXA or a suitable alternative». Альтернативу FDA не называет, намекать, что это мы, нельзя |
| B | «Percent change in body weight, measured on a calibrated scale, remains the primary endpoint» | Endpoint верный. «Calibrated scale» в guidance нет ни у FDA, ни у EMA |
| A, B | FDA DHT guidance, декабрь 2023 | Верно, финальная. Термин FDA — «fit-for-purpose» |
| A | ICH E6(R3) | Верно (принят в январе 2025). Но на лендинге он нужен только чтобы сказать, что audit trail у нас нет, а это лишнее |

**Боль, которая подтверждается и подходит под угол B:**

- **Дома уже меряют вес, а талию нет.** FDA в DHT guidance прямо допускает домашний вес для того же endpoint,
  при условии verification и validation (§IV.D.2). Талию EMA просит документировать как вторичный endpoint
  (guideline 2016, §4.2.1). Самозамер её не заменяет: у 622 взрослых талию завышали в среднем на 5.98 см
  (Contardo Ayala 2014), у 1 298 сотрудников на 1.1 см (Dekkers 2008), а в части исследований её занижали на
  1-3 см (обзор IAS/ICCR, Ross 2020). Ошибка непредсказуема даже по знаку. Значит, между визитами у
  исследования есть вес и нет надёжных обхватов. Это наша дыра, и она честная.
- **Удалённые визиты FDA считает вопросом удержания.** Obesity draft guidance советует предлагать транспорт и
  варианты для тех, кто не может ходить на все визиты. DCT guidance: домашние активности «may reduce the
  need for travel and improve engagement, recruitment, and retention». Цитировать можно только с этим «may».
- **Рулетка зависит от того, кто её держит.** Расхождение между измеряющими 1.4-15 см (обзор 9 исследований,
  Verweij 2013). Единого протокола замера талии нет (консенсус IAS/ICCR 2020). Но с письменной инструкцией
  разброс между операторами терял значимость, так что «рулетка ненадёжна» как общий тезис не проходит.
  Это аргумент угла A, и для B он не нужен.

**Чего не писать:** dropout из-за визитов «только на замер» (источника нет); любые цифры снижения dropout
от удалённых визитов (у FDA только «may»); 30-45% как текущий attrition; «FDA требует DXA». И не ставить
рядом ошибку самозамера и наши 1.5-2.0 см: это разные исследования и разные эталоны, а guardrail #2
запрещает их сводить.

### Блок проблемы под угол B: черновик (EN)

> **Eyebrow:** The problem
>
> **H2:** What do remote check-ins miss in obesity and metabolic trials?
>
> Remote check-ins already return body weight. Guidance from the US Food and Drug Administration (FDA) on digital
> health technologies accepts home weight for the same endpoint, provided the device is verified and validated. Waist circumference still needs a site
> visit and a trained measurer. Between visits, the study has weight and no body measurements.
>
> **Card 1: "Secondary endpoint".** The European Medicines Agency asks for waist circumference to be documented
> as a secondary endpoint in weight-management trials. [European Medicines Agency guideline, 2016]
>
> **Card 2: "1 to 6 cm".** Self-measured waist differs from a trained measurer's reading by about 1 to 6 cm on
> average, depending on the study, and the direction of the error varies. [Ross et al., IAS/ICCR consensus, 2020;
> Contardo Ayala et al., 2014; Dekkers et al., 2008]
>
> FitXpress adds waist, hip and 80+ body measurements to the home check-in, captured from two guided phone
> photos inside the study's own app. The sponsor decides how the additional data is used.

Ссылки на подписях карточек — на первоисточники из `sources-problem-block.md`. Вторая фраза абзаца —
пересказ FDA, без кавычек.

## 3. Что исправить обязательно (claims и факты)

**Во всех трёх версиях:**

1. **«React Native».** В `tech-spec.md` прямо: не писать, продукт не подтвердил. Публичная формулировка:
   «web and mobile SDKs, including supported iOS and Android integrations». В C эта фраза тоже осталась
   («native iOS and Android SDKs, React Native, and web capture»).
2. **Форма.** Встроена форма `/contact-us/` (`f227f5ce`). Нужна общая `FX | LP | Demo`, как на страховании и
   бариатрии.
3. **`[PLACEHOLDER]` в HTML-комментарии** (логотипы). Судья считает его hard fail. У A есть второй (ссылка на
   хаб, хотя URL известен: `/content-hub/clinical-trial-anthropometric-measurement-software-obesity-trials/`).
4. **Логотипы** Yazen, UK Meds, Healthyr использовать можно. Но для этой аудитории они ничего не доказывают:
   это не исследования. Подпись «100+ clients… including digital health and weight management programs»
   честная, её оставляем.

4а. **GDPR-строка не по канону** во всех трёх: «the contracting organization acts as data controller and 3DLOOK
   acts as data processor». Канон из `compliance.md`: «In most enterprise deployments, the customer acts as the
   data controller and 3DLOOK acts as the data processor under GDPR.»

**В A и B (из FAQ и блока интеграции, в C уже вырезано):**

5. Нет источника, и 06.10 по той же причине это убрали с фитнес-страницы: offline-съёмка в нативных китах,
   webhooks без ретраев и подписи, iOS 15+, старые Android с низким frame rate, только стоя, без колясок и
   ампутаций, два варианта пола, «разница роста больше 2 см влияет на результат». Если у тебя есть источник
   от продукта, сначала он идёт в `tech-spec.md`, потом на страницу.
6. «Version requirements for the study period are agreed before the study starts» (B). Ты сама пометила, что
   это надо подтвердить. Пока не подтверждено, вопрос с FAQ снимаем.
7. «Supports blinded study designs». Скрывает результаты платформа, а не мы. Достаточно «The study team
   decides which results, if any, participants and site staff see».
8. «Each record shows… how they were captured». Поля capture source продукт не подтверждал.
   Подтверждено: timestamp и scan ID. Флаги pose / clothing хранятся у нас, но возвращаются ли они клиенту
   полем, продукт не подтвердил. Мок «Clothing flag · retake sent» в A показывает именно это.

**Только в A:**

9. «Audit-ready records» и «Timestamped FitXpress records support those documentation expectations» (ICH
   E6(R3)). Audit trail и Part 11 у нас нет. Для спонсора это прямое регуляторное обещание. Убрать.
10. Remote pre-check с BMI: см. раздел 1. Убрать.
11. «Fewer trips… can lower the friction that contributes to dropout» плюс 30-45% attrition. Связь
    «меньше визитов → меньше dropout» в источнике не показана (раздел 2).

**Только в C:**

12. **Регуляторные строки заменены размытыми.** Вместо канона «An independent regulatory assessment concluded
    that FitXpress does not meet the definition of a medical device under UK MDR or EU MDR for its current
    intended purpose» стоит «The current regulatory assessment applies to the product's assessed intended
    purpose». Фразы «FitXpress is not a medical device» на странице нет совсем. Для этой аудитории это самый
    важный ответ, вернуть канон из `compliance.md`.
13. **Блок точности потерял ограничения.** Пропали популяция валидации (16-78 лет, 38-210 кг, 150-220 см, US и
    Европа), «not peer-reviewed» и «methodology available under NDA». Guardrail #4: процент без методологии и
    без NDA — hard fail. Плюс en dash в «96–97%» и «1.5–2.0 cm», а house format — через дефис.
14. **H1 без продукта:** «Remote body measurements for clinical trials». Правило кита: H1 = продукт +
    аудитория + результат.
15. **Title 66 символов, description 160** при лимитах 60 / 155.
16. **Нет ценового сигнала.** Кит требует назвать входной тариф и дать ссылку на `/pricing/`. Сейчас на
    `/pricing/` по-прежнему «scans» (проверил 28.10), переход на requests ещё не выкатили. Значит одна строка
    «Plans from $1,000 per month» и ссылка, без единицы.

## 4. Структура: B / C до 1 100-1 600 слов

Сейчас A ~3 150 слов, B ~2 910, C ~2 070. Бюджет кита 1 100-1 600, FAQ 4-6. Ориентир по порядку —
фитнес-финал 07.10. На GLP-1 оставили твой порядок (проблема сразу после hero), здесь он тоже годится.

**H1** (правило: продукт + аудитория + результат), под платформу:
«FitXpress for DCT platforms: add remote body measurements to the participant app». Главный ключ карты
(«remote anthropometric measurement for clinical trials») тогда идёт в title и первый абзац.

**Title:** «Remote Anthropometric Measurement in Trials | FitXpress» (55 символов, главный ключ карты).
**Description:** «Add waist, hip and 80+ body measurements to remote check-ins in obesity trials. FitXpress runs white-label
inside the study app or DCT platform.» (144).

**Блоки:**

1. Hero + мок записи участника (как в B; подпись мока у B лучше, чем у C).
2. Проблема: новый блок из раздела 2 (~110 слов, две карточки).
3. Value cards, четыре (из B, у каждой выгода): между визитами, внутри своего app, без железа, запись для
   data pipeline.
4. White-label интеграция + мок task list. Для платформы это главный блок. Убрать React Native и offline,
   добавить фразу C «FitXpress does not provide a prebuilt EDC integration»: честная граница, CTO её оценит.
5. Запись и выходные данные: шесть карточек → четыре, у каждой «что это меняет». Мок графика «week 12»
   переносим сюда, а отдельный H2 «Add body measurements between site and imaging visits» убираем: он
   повторяет проблему и карточки.
6. Как работает: три шага + «3DLOOK provides / the study platform controls». Эта таблица ответственности
   для платформы сильная, оставить.
7. Сравнение методов: таблицу оставить, вводный абзац сократить до одной фразы, после таблицы вывод (он у B
   есть).
8. Точность и данные по канону: три цифры + method sentence + популяция + «under NDA» + ссылка на
   accuracy-статью. Пять строк данных + ссылка на trust FAQ. Регуляторные строки дословно из
   `compliance.md`.
9. Пилот и цена: три шага (у B, без списка из шести метрик), одна строка «Plans from $1,000 per month» +
   ссылка на `/pricing/`.
10. FAQ, пять вопросов: каждый либо GEO-фраза карты, либо возражение, которого нет в теле:
    - Is FitXpress a medical device? (канон, для этой аудитории главный вопрос);
    - How can obesity trials collect body measurements between site visits? (GEO-фраза карты);
    - Can FitXpress run white-label inside a DCT platform?;
    - Can scan results stay hidden from participants and site staff?;
    - Does FitXpress measure muscle? (из B: честно про lean mass, это ровно вопрос эпохи GLP-1).
11. Форма.

Уходят: FAQ про обновления SDK, устройства, EDC-вебхуки, хостинг (он в блоке данных), vendor
qualification (одна строка в блоке данных). Отдельный блок «Between visits» тоже уходит. Оценка: ~1 500-1 600
слов.

## 5. Правки Асель: что берём

Выбор B вместо A — верный, с ним согласен. По десяти пунктам:

| # | Правка | Берём? |
|---|---|---|
| 1 | Позиционирование: модуль замеров внутри app и DCT-платформы, без замены методов | да |
| 2 | Убрать BELIEVE и FDA про стоимость DXA из проблемы | да, источники это подтверждают (раздел 2). Но блок остался без боли: «Scheduled site visits… may leave gaps» не говорит, чего стоит дыра. Нужен новый блок |
| 3 | Выгоды: удалённо, внутри app, без железа, структурированные данные | да |
| 4 | Сохранить white-label, моки, сравнение | да. Но H2 по-прежнему 11, отдельный блок «between visits» дублирует проблему |
| 5 | Хеджи по точности и регуляторке | идея верная, исполнение нет: пропали канон «not a medical device», вывод про UK MDR / EU MDR, популяция валидации и «under NDA». Судья дал за это hard fail. Хеджи «depends on the configuration» повторяются пять раз, оставить один |
| 6 | Убрать тарифы и чек-лист пилота | чек-лист да, тарифы нет: кит требует ценовой сигнал. Одна строка + ссылка на `/pricing/` |
| 7 | Title, H1, meta под ключи | ключ в title верный, но 66 символов. H1 без продукта |
| 8 | FAQ до пяти | да. Но все пять повторяют тело страницы, заменить по списку из раздела 4 |
| 9 | Три внутренние ссылки | да. Плюс `/pricing/`; а фраза «3DLOOK's mobile body scanning technology explains…» осталась без своей ссылки |
| 10 | Guardrails | React Native остался, en dash в 96–97%, GDPR-строка не канон (как и у Ники, пункт 4а раздела 3) |

## 6. Слепые судьи

Три свежих субагента, каждый видел только свою версию, кит, скоркард и fact-sheet. Порог 85 и ноль hard fails.

| Ось (вес) | A (v3) | B (v2) | C (v4) |
|---|---|---|---|
| Proof of belonging (15) | 10 | 10 | 9 |
| Claims discipline (15) | 5 | 5 | 5 |
| Sales argument (15) | 4 | 5 | 4 |
| Uniqueness (10) | 6 | 8 | 6 |
| Conversion (10) | 5 | 5 | 5 |
| Buyer language (10) | 7 | 7 | 6 |
| Human copy (10) | 4 | 5 | 4 |
| Search / AI visibility (10) | 5 | 5 | 5 |
| Place / technical (5) | 2 | 2 | 2 |
| **Итого** | **48** | **52** | **46** |

Для сравнения: первые версии бариатрии получили 54 / 53.

**Hard fails:**

- A и B: iOS 15 и «height difference above 2 cm» без источника; `[PLACEHOLDER]` в HTML (у A два, и ссылка на хаб
  ведёт в корень `/content-hub/`).
- C: `[PLACEHOLDER]`; нет «FitXpress is not a medical device», регуляторный вывод заменён размытой фразой.

**Что судьи нашли сверх раздела 3:**

- В A и B детектор ловит «The platform decides…» (anthropomorphism). Правка: «The platform team decides», как
  уже сделано в C.
- В FAQ «Height, weight and gender are required inputs» неверно: вес для замеров необязателен.
- Подпись под логотипами по киту должна заканчиваться на «since 2016», если в ряду нет клиента вертикали. Хвост
  «including digital health and weight management programs» судьи читают как почти-вертикальное доказательство.
- Нет «no integration fee» (это публичный факт и преимущество).
- B: SEO title «White-Label Body Scanning…» и H1 «between site visits» тянут разные ключи. Ссылки на хаб нет вообще.
- C: точность в двух видах на одной странице («96 to 97%» в плитке, «96–97%» в тексте и FAQ).
- Все: вопросы FAQ в `<summary>`, а не в H3; H2 проблемы и точности утверждения, а кит просит вопросы.
- Минус по технике у всех одинаковый: форма, события не проверены, нет ссылок на соседние вертикали и
  `/pricing/`, 768 и 1440 не проверены.

**Одна правка от каждого судьи:** у A сократить три механических блока и FAQ до пяти (~3 150 → бюджет), у B
одним проходом убрать все непроверенные claims, у C переписать H1 по формуле. Совет судьи C («help reduce
measurement-only site visits») не берём: он тянет к углу A, потому что судья сверял страницу с use-case
файлом. Use-case файл не трогаем: страницу держим на угле B, его обещания на неё не переносим.

## Открытые вопросы

**Решено:** hero для DCT-платформ; use-case файл `fx-clinical-trials.md` не переписываем.

**При публикации:**

1. URL: `/fitxpress/` ещё не живой, по прецеденту страхования страница встаёт в корень и
   переезжает 301-м вместе с `/fitxpress/`.

**Продукту:**

2. React Native, offline-съёмка, webhooks (ретраи, подпись), минимальная iOS, ограничения по позе и полу,
   влияние ошибки роста. Это хорошие ответы для технического звонка, но пока без источника.
3. Возвращаются ли клиенту полями флаги pose validation и Clothing Detector.
4. Фиксация версии SDK / модели на время исследования: можем ли мы это обещать?

**BD:**

5. Был ли хоть один разговор с CRO, спонсором или DCT-платформой? Какие возражения?
