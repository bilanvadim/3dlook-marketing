---
product: fitxpress
type: vertical-page
vertical: wellness-programs
status: review
for: Nika (+ Asselya)
---

# Wellness: разбор трёх драфтов (28.10)

Проверено тем же пайплайном, что clinical trials: цифры по первоисточникам, claims по `proof-points` /
`compliance` / `tech-spec`, угол по карте лендингов и ключей, детектор, рендер на 1280 и 375 px, три слепых судьи.
Версии: **A** — v1 Ники (wellness-приложения, прогресс участника), **B** — v2 Ники (rewards verification для
работодателей и страховщиков), **C** — v3 Асель (remote biometric screening для корпоративных программ).

## Коротко

1. **Разница с фитнесом:** фитнес — приложения, где человек сканирует себя ради прогресса. Wellness — программы
   работодателя и страховщика: скрининг сотрудников и подтверждение прогресса для поощрений. Wellness-приложения для
   людей (твоя v1) — покупатель фитнес-страницы (раздел 1).
2. **Базой берём C (v3 Асель).** Только она стоит на утверждённом URL `/fitxpress/for-wellness-programs/` и угле
   remote biometric screening и уже укладывается в бюджет (~1 470 слов). Из B переносим аргумент про порог награды выше
   разброса сканов, блок против фрода и метрики пилота (раздел 4).
3. **Цифры B:** CDC 40% убрать (та же ловушка, что на бариатрии). 62% — поощрение за *прохождение* скрининга, а не за
   результат. 78% — только те, кто может работать удалённо. Черновик блока проблемы для C — в разделе 2.
4. **Что обязательно исправить:** в A и B снова iOS 15, «2 cm», пол, webhooks. В C — «photos are not stored»
   (противоречит канону), H1 без продукта, блок точности без NDA и популяции, нет «100+ clients». Во всех — форма
   (раздел 3).
5. **Слепые судьи:** A 43, B 41, C 46 из 100 при пороге 85. У C hard fails нет, слабее всего sales argument (раздел 5).

## 1. Фитнес и wellness: в чём разница

Ника, путаница понятная: хаб называется «AI Body Data for Wellness Platforms», и он широкий, от приложений до
программ работодателей. Лендинг уже. Под этот слот 29.09 утвердили отдельный угол (`landing-map.md`, Hub 5):

| | Фитнес-лендинг | Wellness-лендинг |
|---|---|---|
| Кто платит | фитнес- и коучинг-приложение, студия | работодатель, health plan, корпоративная wellness-платформа |
| Кто сканируется | пользователь приложения, для себя | сотрудник или застрахованный, в рамках программы |
| Зачем | прогресс и удержание пользователя | biometric screening без выездного дня и подтверждение прогресса для поощрений |
| Главный риск в тексте | обещать retention | обещать то, чего мы не меряем (давление, кровь), и решения, которых мы не принимаем (награда, допуск) |
| Ключи | body scanning for fitness apps, gym body scanner | at home / remote biometric screening, company biometric screening, wellness rewards program |

Отсюда:

- **A — это фитнес-страница под другим названием.** Wellness- и коучинг-приложения для людей — тот же
  покупатель, что у фитнес-лендинга, и та же задача (прогресс, который не видно на весах). Второй лендинг
  будет есть фитнес-страницу и хаб. Таких покупателей закрывают фитнес-лендинг и wellness-хаб.
- **B — правильный покупатель, но не тот угол и не тот URL.** Title «Wellness Rewards Verification» совпадает
  с живой статьёй про rewards, а карта ключей оставляет «wellness incentives» ей. Rewards на лендинге — один из
  сценариев, как у C.
- **C — единственная версия на утверждённом URL (`/fitxpress/for-wellness-programs/`) и угле, и уже в бюджете
  (~1 470 слов).** Берём её базой и переносим в неё сильное из B (раздел 4).

## 2. Цифры из B: что подтверждается источниками

Полный разбор с цитатами в `sources-problem-block.md` (EN). Все четыре цифры настоящие, но три карточки говорят
больше, чем источник.

| Карточка | Вердикт |
|---|---|
| **40%** (CDC) | Цитата верная (Zhao, Preventing Chronic Disease 2023). Но это разница в распространённости тяжёлого ожирения по стране (5.3% против 8.8%), а не ошибка конкретного человека. И она бьёт по нам: BMI у нас считается из введённых роста и веса. Та же ловушка, что на бариатрии 16.10. Убрать |
| **43%** (KFF) | Верно, KFF 2025: компании от 200 сотрудников, которые *предлагают* скрининг. «Recurring verification workload for HR» — наша приписка, в источнике её нет |
| **62%** (KFF) | Цифра верная, смысл нет: это поощрение за то, что сотрудник *прошёл* скрининг. За *результат* поощряют только 14% крупных компаний. Фраза «When money depends on the result, the record has to hold up» к 62% не относится |
| **78%** (Gallup) | Верно (май 2026: 52% гибрид, 26% удалённо), но это 78% тех, чья работа вообще может быть удалённой, а это около половины работников США. «Onsite screening days miss many of them» — наш вывод: по KFF половина крупных компаний со скринингом уже даёт пройти его удалённо |

**Ещё три вещи из проверки, которые меняют текст:**

- **Biometric screening по KFF — очный осмотр медика:** BMI, давление, холестерин, глюкоза. FitXpress не скрининг, а
  замер тела для одной его части. C это формулирует правильно, H1 и FAQ должны держать ту же границу.
- **«Self-report is unreliable» в лоб не проходит.** В исследовании 1 298 сотрудников (Dekkers 2008) самоотчёт BMI
  ошибался в среднем на 0.7 кг/м², талия — на 1.1 см. Авторы называют его достаточно точным *для статистики*,
  хотя ошибка росла с весом. Аргумент не в том, что люди врут, а в том, что вписанное число нечем подтвердить, когда
  от него зависит выплата.
- **Юридически:** лимит EEOC в 30% отменён судом (AARP v. EEOC) с 2019 года, новых правил нет. Поэтому никаких
  «EEOC-compliant», «ADA/GINA-safe», «30% safe harbor». У C эта граница соблюдена, у B тоже.

**Чего не писать:** CDC 40% как ошибку человека; 62% как «награду за результат»; 78% как «всех работников»; что
удалённого скрининга нет; цифру админской нагрузки HR (первоисточника не нашли).

### Блок проблемы для C: черновик (EN)

> **Eyebrow:** The problem
>
> **H2:** Why does the body-measurement step still wait for a screening day?
>
> Biometric screening is built around an in-person check: body mass index, blood pressure, cholesterol and glucose,
> taken by a medical professional. Half of large employers with a screening program offer no remote way to complete
> it. At those firms, hybrid and remote employees have to come in for the measurement.
>
> **Card 1: "62%".** Share of US firms with 200 or more workers and a biometric screening program that use incentives
> or penalties to get employees to complete it. [KFF Employer Health Benefits Survey, 2025]
>
> **Card 2: "78%".** Share of US employees with remote-capable jobs who work hybrid (52%) or fully remote (26%).
> [Gallup, May 2026]
>
> FitXpress moves the body-measurement part of the screening to the employee's phone: waist and 80+ body
> measurements, BMI from entered height and weight, and body composition estimates. Blood pressure and blood tests
> stay with the screening provider.

Цифру участия (46% сотрудников проходят скрининг, когда его предлагают, RAND 2013) сюда не ставим: причины
неучастия там не разобраны, связывать её с очным форматом нельзя.

## 3. Что исправить обязательно (claims и факты)

**Во всех трёх:**

1. **Форма** `/contact-us/` (`f227f5ce`) → общая `FX | LP | Demo`.
2. **GDPR-строка не по канону.** Канон из `compliance.md`: «In most enterprise deployments, the customer acts as the
   data controller and 3DLOOK acts as the data processor under GDPR.»

**В A и B:**

3. Опять без источника (тот же список, что в clinical trials и на фитнесе 06.10): iOS 15+, старые Android, только стоя,
   без колясок и ампутаций, два варианта пола, «height within 2 cm». «Height, weight and gender are required inputs»
   неверно: вес для замеров необязателен. В B ещё webhooks без ретраев и подписи.
4. **Цифры по отдельным замерам** (талия: повторяемость 0.89 см, ошибка 2.14 см). Цифры верные, но по
   `accuracy-formulations.md` (правило 6) они для технических материалов. Из wellness-хаба их убрали по этой же
   причине. На лендинге оставляем общие: 96-97%, 1.5-2.0 см, `< 1 cm`.
5. `[PLACEHOLDER]` в HTML-комментариях (по два).

**Только в B:**

6. Ссылки `/fitxpress/for-connected-fitness/` и `/fitxpress/for-telehealth-and-weight-loss/` ведут в никуда. Фитнес
   живёт на `/fitxpress/for-connected-and-digital-fitness/`, телехелс ещё не опубликован.
7. «Pose check passed / Clothing check passed», «Clothing Detector… before the scan is accepted», флаги «stored with
   each scan». Утверждённая формулировка: «The Clothing Detector identifies clothing conditions that may interfere with
   capture and can prompt corrective action». Что флаги возвращаются клиенту полем, продукт не подтверждал.
8. «Reviewers compare each scan with earlier ones for the same participant»: связывает сканы с человеком программа,
   не мы. Так и написать.

**Только в C:**

9. **«For the FitXpress health workflow, input photos are not stored after processing»** противоречит `compliance.md`:
   фото удаляются сразу или хранятся до 30 дней по политике клиента, размыты, лицо скрыто. Вернуть канон.
10. Блок точности без популяции валидации (16-78 лет, 38-210 кг, 150-220 см), без «not peer-reviewed» в форме канона
    и без «methodology available under NDA». Плюс «96–97%» с en dash в плитке и «96 to 97%» в FAQ: один формат,
    `96-97%`.
11. **H1 без продукта:** «Remote Biometric Screening for Employee Wellness: Body Measurements at Home». Title кончается
    на «| 3DLOOK», description 161 символ (лимит 155).
12. «Smart Scales is in beta»: с 21.10 на страницах пишем «Smart Scales» без пометки beta.
13. В Service-схеме нет `audience` и `areaServed`.
14. **Нет ни одного доказательства:** ни «100+ clients», ни логотипов. Строка «FitXpress by 3DLOOK brings mobile body
    measurement technology to health, fitness and wellness workflows» ничего не доказывает. Вернуть строку
    «3DLOOK has worked with 100+ clients since 2016» (логотипы можно, клиентов вертикали нет, подпись кончается на
    «since 2016»).

**Нужно подтвердить у продукта (в B и C):** voice guidance и запрет загрузки из галереи. Галерея есть в живой статье про
rewards, но в `tech-spec.md` нет ни того, ни другого. Если подтвердят, это хороший аргумент против фрода, его стоит
оставить.

## 4. Структура: C плюс сильное из B

C ~1 470 слов при бюджете 1 100-1 600, так что добавлять можно только взамен. Порядок по фитнес-финалу.

**H1** (продукт + аудитория + результат, и без обещания всего скрининга):
«FitXpress for employee wellness programs: at-home body measurements for biometric screening».
**Title:** «At-Home Biometric Screening: Body Measurements | FitXpress» (58 символов, главный ключ карты).
**Description:** «Add at-home body measurements to employee biometric screening. Waist, 80+ body measurements and body
composition estimates from two smartphone photos.» (150).

**Что меняем в C:**

1. **Hero:** новый H1; под ним полоса доказательств: «3DLOOK has worked with 100+ clients since 2016» вместо
   строки «FitXpress by 3DLOOK brings…».
2. **Блока проблемы в C нет вообще,** страница сразу идёт в «Screening scope». Нужен короткий блок (~100 слов, две
   карточки), черновик в разделе 2.
3. **«What FitXpress adds to a biometric screening program»** — оставить как есть. Это лучший блок страницы: честно
   говорит, что мы меряем, что считаем, что оцениваем и что делаем не мы (давление, кровь).
4. **Три аудитории** (работодатели, wellness-платформы, health plans) — оставить. Из B добавить по одной строке, что
   каждая получает.
5. **How it works:** пять шагов → три, и колонка «FitXpress / your platform» как у B.
6. **Сценарии:** в карточку rewards перенести мысль из блока B «Set milestone thresholds above scan-to-scan
   variation», одним предложением: порог награды ставят заметно выше разброса повторных сканов (`< 1 cm`), тогда
   награда идёт за реальное изменение. Это сильный аргумент для того, кто отвечает за честность выплат. Полный
   блок B с таблицей не нужен.
7. **Product capabilities** объединить с «program integrity» из B: camera-only (если продукт подтвердит), проверки при
   съёмке, датированная запись, и граница «support fraud review, do not replace program rules».
8. **Точность и данные:** канон (три цифры, method sentence, популяция, «under NDA», ссылка на accuracy-статью), пять
   строк данных + trust FAQ. Фото по канону (пункт 9 раздела 3).
9. **Пилот:** три шага C + из B четыре метрики: checkpoint completion, disputed reward decisions, administrator time per
   validated checkpoint, days from scan to reward decision. И сравнение с текущим способом проверки на той же группе
   (так в фитнес-финале).
10. **Цена:** у C «requests», на живом `/pricing/` пока «scans». Переход на requests решён 16.10, так что страница
    выходит вместе с обновлённым `/pricing/` (как бариатрия) или до тех пор пишет «scans».
11. **FAQ, пять** (сейчас шесть): убрать «What data does FitXpress collect…», он повторяет блок «What FitXpress
    adds». Остальные пять хорошие и закрывают GEO-фразы карты. Вопросы оформить H3.

## 5. Слепые судьи

Три свежих субагента, каждый видел только свою версию, кит, скоркард и fact-sheet. Порог 85 и ноль hard fails.

| Ось (вес) | A (v1) | B (v2) | C (v3) |
|---|---|---|---|
| Proof of belonging (15) | 8 | 9 | 7 |
| Claims discipline (15) | 5 | 3 | 6 |
| Sales argument (15) | 6 | 4 | 4 |
| Uniqueness (10) | 4 | 4 | 6 |
| Conversion (10) | 5 | 5 | 5 |
| Buyer language (10) | 5 | 7 | 6 |
| Human copy (10) | 5 | 5 | 4 |
| Search / AI visibility (10) | 3 | 3 | 6 |
| Place / technical (5) | 2 | 1 | 2 |
| **Итого** | **43** | **41** | **46** |

**Hard fails:**

- A: iOS 15, «height within 2 cm» и «4 to 12 weeks between scans» без источника; `[PLACEHOLDER]`.
- B: iOS 15, «2 cm», пол и обязательные поля без источника; `[PLACEHOLDER]`; триада «Your program keeps the rules,
  the review and the reward».
- C: hard fails нет. Но судья отдельно назвал «input photos are not stored» ложным заявлением о хранении.

**Что судьи нашли сверх раздела 3:**

- A и B: на странице ни разу нет «biometric screening», ключей слота нет ни в H1, ни в title, ни в FAQ. Поэтому у обеих
  поиск 3 из 10.
- A: you/your 14.2 на 1 000 слов при лимите 12.5; «The capture flow is white-label» переворачивает границу (съёмка у нас
  фиксированная, white-label — интерфейс вокруг).
- B: механика (how it works, review, правила, integrity) идёт раньше ценности; граница «решение о награде за
  администратором» повторена четыре раза; «Large employer and plan populations usually start here» звучит как
  клиентский опыт, которого у нас нет.
- C: «Under 45 sec — measurement processing after photo capture» — запрещённый вариант, канон «under 45 seconds from the
  photos to structured results»; ADA, GINA, EEOC, API, SDK не раскрыты при первом упоминании; к фразе «not a medical
  device» пристёгнута цепочка отрицаний; почти каждый блок кончается передачей ответственности, и страница читается как
  дисклеймер, а не как продажа.
- Все: FAQ в `<summary>`, а не H3; нет «no integration fee»; форма не та; события не проверены.

**Одна правка от каждого судьи:** A — перенацелить на слот (H1, title, canonical, FAQ под ключи); B — переписать карточки
статистики по первоисточникам, CDC убрать; C — заменить сетку «Screening scope» таблицей «что получаете → что это меняет
для программы». Правку судьи C берём: блок «What FitXpress adds» остаётся, но у каждой строки появляется колонка
«что это меняет» (участие, время администратора, запись для проверки награды).

## Открытые вопросы

**Продукту:**

1. Voice guidance и запрет загрузки фото из галереи: подтверждаем?
2. Возвращаются ли клиенту полями флаги pose validation и Clothing Detector.
3. Тот же список без источника (iOS, Android, поза, пол, рост).

**BD:**

4. Был ли разговор с работодателем, health plan или корпоративной wellness-платформой? Какие возражения?
