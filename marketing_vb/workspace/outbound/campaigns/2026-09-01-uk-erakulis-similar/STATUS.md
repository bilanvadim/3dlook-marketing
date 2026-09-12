# STATUS — 2026-09-01-uk-erakulis-similar

**Шаг 2 (company-researcher) перезапущен 2026-09-12 под переписанную гипотезу.**
Блокер 2026-09-02 «Вадим выбирает гипотезу» — снят.

---

## Решение Вадима 2026-09-12

| | |
|---|---|
| **Сегмент** | consumer wellness / fitness / nutrition апки — Erakulis look-alike |
| **Гео** | вся UK: England + Scotland + Wales + NI |
| **Профиль** | `katerina` |

Erakulis — **действующий клиент 3DLOOK** (приложение CR7: fitness + nutrition + mind,
BodyScan по двум фото). «Erakulis-similar» значит look-alike кампанию под клиента, а не
GLP-1 вертикаль. Старая гипотеза этого даже не упоминала.

Это UK-сестра закрытых `2026-08-07-us-digital-fitness` (nick, 248 отправлено) и
`2026-08-14-au-digital-fitness` (vadim). ICP-сегмент один и тот же — `icp-detail.md` §8.

## Почему списки пересобираются, а не чинятся

Кампания несла три несовместимых определения сегмента: гипотезу (GLP-1 telehealth,
England), запрос Вадима в Telegram 02.09 в 03:23 («фітнес епки та нутрішн епки») и сам сид
Erakulis (general wellness). Разбор верифицированного GLP-1 списка против его же
anti-cases: 13 строк из 30 — аптеки без приложения, 12 — без коучинга, 3 — не England.
Реально проходили гипотезу 12 строк, из них Oviva (NHS) и Hims & Hers UK (US parent) —
прямые anti-cases, то есть ~11 при собственном floor в 15.

Плюс ни в одном списке не было `icp_fit`, `linkedin_url`, `hq_city`, `employees` — то есть
приоритизировать нечем и Sales Navigator строить не из чего.

Полный разбор и все старые артефакты: `_superseded-2026-09-12/README.md`. Ничего не удалено.

## Что сделано 2026-09-12

- Старые списки (`companies_filtered.csv`, `companies-glp1-telehealth*.csv|md`) и карантин
  02.09 убраны в `_superseded-2026-09-12/`, туда же копия старой гипотезы.
- `hypothesis.md` переписан: вертикаль, под-сегмент (4 «вкуса»), use case, персоны,
  anti-cases, validation criteria. Status `approved`.
- `hypothesis-gate --stamp` → `.hypothesis-lock.json`, scope hash `f84525ccc0901505`,
  6 scope-секций. Список теперь привязан к версии гипотезы.
- `search-health.py` — зелёный (20-29 результатов на контрольный запрос). 02.09 он был
  слепым с 03:50 до 05:08, и именно поэтому старый список писался по памяти модели.
- Запущен `company-researcher`: 25-30 компаний, полная step-2 схема, `web-verify` на
  каждой строке, exclusions по `katerina` проверяются кодом.

## Дальше

1. `company-researcher` отдаёт `companies.csv` + `companies.md` (канонические имена —
   старый список назывался иначе, поэтому трекер и показывал кампанию на стадии 1).
2. Апрув списка Вадимом.
3. **Вадим**: выгрузка людей из Sales Navigator в `sales-nav-raw/` — шаг 3 без неё не идёт.
4. `/outbound extract 2026-09-01-uk-erakulis-similar` → `validate` → чекпоинт менеджера.

## Открытые вопросы к Вадиму

1. **Можно ли называть Erakulis в холодных сообщениях?** Это сильнейший аргумент
   кампании, и без имени он не работает. Нужно к шагу 5, не раньше.
2. **Fiit и Flo Health** были в списке `2026-07-31-uk-telehealth-digital-health`, но в
   registry контактов по ним нет. Считать их свободными?
3. **Прайсинг под консьюмерский ARPU.** £10-30/месяц — другая экономика, чем £100-300 у
   GLP-1 провайдеров, под которые писалась старая гипотеза.

## Перед шагом 3 — обязательное

```bash
python3 scripts/search-health.py          # exit 1 = поиск слепой, ничего не запускать
python3 scripts/outbound-pipeline.py validate-companies \
        --campaign 2026-09-01-uk-erakulis-similar --profile katerina --write-routed
python3 scripts/outbound-pipeline.py extract-people \
        --campaign 2026-09-01-uk-erakulis-similar --dry-run
```

---

## Обновление 2026-09-12 (после прогона company-researcher)

**Результат: 4 компании прошли гейт, не 25-30.** Это не сбой поиска (`search-health.py`
зелёный весь прогон, 20-32 результата) и не лень — это ответ рынка после ре-верификации.
Полный разбор в `companies.md` (`## Coverage gaps / risks`).

| | |
|---|---|
| Найдено и проверено `web-verify` | 7 (6 `verified-live`, 1 `blocked:js-challenge` — Voy) |
| Проходят gate для `katerina` | **4**: Second Nature, Numan, NowPatient, Voy |
| Роздано в другие профілі | Freeletics → `olena` (Germany), Juniper → `vadim` (Australia — виявилось брендом Eucalyptus Health, Sydney, хоча стара `evidence_geo` це вже показувала) |
| Відкинуто по fit | Flo Health (fit 2 — велика, UK, але продукт не про body-transformation) |
| Перевірено і НЕ пройшло | Fiit, WithU, Hussle, MoveGB, Runna, Wild.AI, DNAfit, Nutracheck, CheqUp, Medicspot, Dr Frank's, Jood Life, heySlim, Piko, YuLife, Vitality, Healf, Gymshark, Medichecks, Reset Health, REVOOLA, GoJoe, Unmind, Reward Gateway, Wellhub, Habitual — з причиною по кожній в `companies.md` |

**Відповідь на відкриті питання вище:**
- Fiit: перевірено, 32 співробітники — не проходить floor 50+. Найближчий "near miss" у
  всьому пошуку по flavour 2.
- Flo Health: перевірено, у реєстрі виключень немає, вільна — але fit=2, не проходить
  High/Medium bar. Велика (672-685 співробітників, $157.6M ARR), просто продукт не про те.

**Це відповідає власному "Falsified if" критерію гіпотези** (`hypothesis.md`): менше 15
компаній → UK-зріз занадто тонкий, кампанія належить на pan-European `olena`. Три варіанти
для Вадима — в `companies.md` розділ Coverage gaps, пункт 5.

Гейти пройдено в порядку: `search-health` (exit 0) → `hypothesis-gate` (exit 0, scope не
змінився) → `web-verify` (7/7 оброблено) → `validate-companies --write-routed` (exit 0, 0
errors). Трекер (`outbound-registry.py status`) тепер показує кампанію на стадії
`2 · companies`, блокер — виписка Sales Navigator від Вадима.

Файли: `companies.csv` (сирий, 7 рядків), `companies-verified.csv` (з web-verify),
`companies-routed-out.csv` (3 рядки для `olena`/`vadim`/low-fit), `companies.md` (повний
розбір, зокрема хто не пройшов і чому).

---

## Обновление 2026-09-12, третий проход (floor 50 → 25, extend not rebuild)

Вадим: гео не меняем, floor снижаем 50 → 25 (это правило только для этой кампании — не
трогает `icp-detail.md` и не переносится на другие профили без отдельного решения).
`hypothesis.md` переписан ещё раз (Sub-segment + Anti-cases), передан на апрув и
переапрув, `hypothesis-gate --stamp` заново → scope hash `552020f56f38a8cb`.

**Список расширен, не пересобран** — 4 исходные строки (Second Nature, Numan, Voy,
NowPatient) не тронуты.

| | |
|---|---|
| Было (floor 50) | 4 проходят gate |
| Стало (floor 25) | **10** проходят gate |
| Добавлено из 7 названных кандидатов | Fiit (32), WithU (31), CheqUp (<50, judgement call), Medicspot (34), Nutracheck (36, acquisition 2022 ruled not-recent) |
| Остались исключены из тех 7 | Habitual (2-10 — не проходит даже 25), DNAfit (32 — проходит по headcount, но исключён за business model: разовая покупка DNA-теста, нет подписки) |
| Найдено пере-разведкой (re-sweep) | Coopah (27, новый кандидат, AI run-coaching, TCS London Marathon partner) — единственная новая находка из 9+ индивидуально проверенных (BUA Fit, VEYR, ROXFIT, REVOOLA, TrainAsONE, Sleepstation, Hevy, Pillar App, Hussle/MoveGB re-check) |

Гейти пройдено в тому ж порядку: `search-health` (exit 0) → `hypothesis-gate` (exit 0,
scope = `552020f56f38a8cb`) → `web-verify` (12/13 verified-live, Voy — той же
`blocked:js-challenge`) → `outbound-registry.py check --profile katerina` (0 must-exclude
серед нових 6) → `validate-companies --write-routed` (exit 0, 0 errors, 10 proceed / 3
routed, розподіл той самий: Flo Health low-fit, Freeletics → olena, Juniper → vadim).

Повний розбір по кожній з 7 названих кандидатів і по re-sweep — `companies.md`, розділи
`## Re-admitted at the 25-employee floor` і `## Re-sweep findings`.

Файли оновлені: `companies.csv` (13 рядків, 6 нових додано в кінець, оригінальні 7 не
чіпались), `companies-verified.csv`, `companies-routed-out.csv` (без змін, 3 рядки),
`companies.md` (Excluded candidates розділений на headcount-independent і
still-below-25-floor; Coverage gaps переписаний під нову картину).

---

## Рішення Вадима 2026-09-12 (вечір) — до кроку 5

**1. Erakulis прямо називати НЕ можна.** Його і не було в затверджених пруфах: у
`brand-assets/product-info/` немає ні кейсу, ні рядка в proof-points, ні згадки в
«Trusted by». Лишається внутрішнім патерном кампанії.

Заміна — **Yazen**: «Yazen uses FitXpress for member progress tracking, with 34K scans in
2025» (`case-studies/yazen.md` прямо дозволяє це в аутбаунді по telehealth / weight-loss).

⚠️ **Покриває тільки половину списку.** Yazen — клінічна weight-loss платформа, тому
працює на Voy, Numan, CheqUp, Medicspot, NowPatient. На Fiit, Coopah, WithU, Nutracheck і
Second Nature — ні: це споживчі фітнес/нутришн апки, і іменованого референсу в їхній формі
в нас немає взагалі. Для них повідомлення спирається на швидкість інтеграції і аргумент
про churn, не на пруф.

**2. Прайсинг у холодних повідомленнях — заборонено повністю.** Ні ціни, ні тарифу, ні
range hint, ні «from $X» — у жодному повідомленні послідовності, включно з фолоу-апом.
`pricing.md` дозволяв range hint, якщо байєр сам підняв бюджет; на цій кампанії вимкнено і
це. Питання про ціну = дзвінок, не відповідь у чаті. Для `message-sequencer`: будь-яке
число з прайсу — hard fail, як вигаданий клейм.

Контекст для дзвінка (не для копії) — в `hypothesis.md`, Open questions #3: опублікована
таблиця закінчується на 20K запитів/міс, а Voy при 5% активності від >1M учасників дає
~50K/міс, тобто 18 річних обсягів Yazen щомісяця. Важіль — квартальна каденція сканів
замість місячної: вчетверо дешевше на користувача і ближче до того, як працює сам Yazen.

---

## Кроки 3-4 пройдено 2026-09-12 — і інцидент з Hermes

### Що зробив Hermes (і чому це довелось переробити)

Вадим залив виписку Sales Navigator у `sales-nav-raw/people_raw.csv` (342 рядки) і попросив
Hermes підхопити. Hermes **не зміг прочитати власний пайплайн**: у `~/.hermes/config.yaml`
292 deny-правила і жодного allow, весь `~/3dlook-marketing` закритий для `grep` / `find` /
`sed` / `awk` / `rg`. У логу гейтвею видно блокування на `outbound-pipeline.py`, на
`scripts/`, на `brand-assets/`. Далі він шукав неіснуючі `icp_validate.py` і
`generate_messages.py`, о 07:27 вичерпав бюджет ітерацій (60/60) і був попрошений
підсумувати. Плюс `turn lease contention` — два routing key на одну сесію, черга 729 с.

Не знайшовши інструментів, він написав пайплайн сам: власні `people-raw.csv`,
`people-validated.csv`, `people-validated-scored.csv` і **218 файлів повідомлень на 109
людей**. Жоден справжній скрипт і жоден справжній агент не запускались. Усе це прибрано в
`_hermes-improvised-2026-09-12/`, не видалено.

Два висновки. **Права:** це «config carve-out reverts on update» — виняток для
маркетингового репо знімається кожним `hermes update`. **Маршрутизація, і вона важливіша:**
з телеграма аутбаунд запускається тільки через `mvb-run.py outbound`, який ставить job у
conductor. Вести пайплайн руками в DM — помилка маршруту, а не тільки прав.

### Крок 3 (extract-people) — справжній

`NowPatient` перейменовано в `NowPatient (Infohealth)`: у виписці компанія називається
Infohealth Ltd, і без аліаса джойн губив 19 живих людей. Скрипт коректно відкинув
Freeletics (80 рядків → `olena`) і ONE FIIT / FIIT Institute (26, інші компанії).

**Колонка `location_country` у виписці бреше** — несе країну фільтра пошуку, а не людини.
31 рядок каже «United Kingdom», а `location_city` — Індія, Гватемала, Туреччина,
Бангладеш. Це хвіст колізії по слову «FIIT». Відфільтровано по місту →
`people-dropped-nonuk.csv`.

Лишилось **98 людей у 6 компаніях**, усі чисті по exclusions (`outbound-registry.py check`).

Чотири компанії зі списку дали нуль людей — CheqUp, Numan, Second Nature, Voy. Вадим:
їх уже аутрічили або контактували раніше. **У registry виключень їх немає** — там записана
тільки кампанія 2026-07-31. Треба внести, інакше наступний пошук їх знову підніме.

### Крок 4 (icp-validator)

**PASS 9 · WEAK 17 · FAIL 72.** Виключено по registry: 0.

| Компанія | Рядків | PASS | WEAK | FAIL | покриття штату |
|---|---:|---:|---:|---:|---:|
| Nutracheck | 31 | 4 | 3 | 24 | 86% |
| Medicspot | 22 | 2 | 3 | 17 | 65% |
| NowPatient (Infohealth) | 19 | 0 | 6 | 13 | 36% |
| Coopah | 10 | 2 | 1 | 7 | 37% |
| Fiit | 8 | 1 | 2 | 5 | **25%** |
| WithU | 8 | 0 | 2 | 6 | 26% |

Дев'ять PASS: Ryan Sherreard (Head of Product, Coopah), Pete Cooper (Co-Founder, Coopah),
Dr Zubair A. (Founder/CEO, Medicspot), Daniel Hutson (MD, Nutracheck), James Charalambous
(MD, Fiit) — P1; Oliver Brooks (CTO **і** співзасновник, Medicspot), Eleanor Bennett (Head
of Data Product) і Jack Yaxley (Product Manager, Nutracheck) — P2; Daisy Ford
(Partnerships, Nutracheck) — P3.

17 WEAK розбито на три купи для окремого апруву: 8 інженерних (P3
`technical-integration`), 5 owner-level що потребують перевірки очима, 4 суміжних
комерційних.

### Блокер: контактів не вистачає, і причина не в кількості компаній

Validation criteria гіпотези вимагають **≥40 контактів**, ціль 60+. Є 9, або 26 якщо взяти
всі WEAK.

Дві причини. **Виправна:** виписка робилась по компанії, а не по посадах, тому повернула
цілі штати — 72 зі 98 (підтримка, аптечна стійка, аудіопродюсери) не були кандидатами
ніколи. Плюс квота з'їдена колізією по «FIIT»: 68 сирих рядків, з них справжніх людей
Fiit — 8. Покриття Fiit 25%, WithU 26%, Coopah 37%, NowPatient 36% — там є ненайдені люди.
**Невиправна пошуком:** чотири відсутні компанії — саме ті, що мають справжні продуктові
організації. Voy один більший за ці шість разом узяті. Лишились п'ять компаній по 27-36
людей, де весь продуктовий відділ це двоє-троє, плюс аптека без продуктового відділу.

---

## Крок 5 пройдено 2026-09-12 — 26 контактів, 52 повідомлення

Вадим на чекпоінті кроку 4 апрувнув PASS + WEAK разом → `people-approved.csv` (26).

`message-sequencer` написав по 2 повідомлення на людину (opener + фолоу-ап через 5 днів,
без note до запиту в друзі). Файли — `messages/{person_id}.md`, зведення — `messages/_summary.md`.

### Перевірено механічно, не зі слів агента

| Перевірка | Результат |
|---|---|
| Erakulis / CR7 / Ronaldo в тексті повідомлень | **0** (у `_summary.md` згадки є — це слаг кампанії і сам опис правила) |
| Прайсинг: `$`/`£`/`€`, «pricing», «free trial», тарифи | **0** |
| Yazen — тільки для Medicspot і Infohealth | **9 файлів, усі в межах**. Ще в 6 файлах Yazen згадано лише в блоці Context — як пояснення, ЧОМУ його не взяли |
| `detect-ai-tells.py --channel dm` по тілах повідомлень | 26 із 26 CLEAN |
| Ліміти 600 / 550 символів | усі в межах (у середньому 419 / 375) |

⚠️ **Детектор треба ганяти по тілах повідомлень, а не по файлу.** Файл містить заголовок
`# Ім'я — Посада — Компанія` і блок Context — em dash у заголовку дає 5 фальшивих
спрацювань на кожному файлі. Перший прогін по цілих файлах показав «26 із 26 брудні»,
і це була неправда.

Три файли реально мали зауваження — corrective «rather than», заборонений
`terminology-guardrails.md` Part 1: `daisy-ford`, `ellie-hitchmough`, `rajive-patel`.
Виправлено (5 конструкцій), після правки всі 26 чисті.

### Що в повідомленнях

- 9 `technical-integration` контактів написані як імплементаторам — SDK, строки інтеграції,
  потік даних, без пітчу про retention-економіку, якою вони не володіють.
- Oliver Brooks (Medicspot) — виняток: CTO **і** співзасновник, тому одна лінія build-vs-buy
  є, але текст лишається технічним.
- Navin Khosla (комплаєнс Infohealth) — єдиний, у кого стоїть «The BodyScan feature itself is
  not a medical device», і саме на фічу, а не на застосунок: у NowPatient реєстрація MHRA
  Class I. У решти контактів Infohealth цієї фрази немає.
- Там, де в одній компанії кілька контактів (Nutracheck ×7, Infohealth ×6, Medicspot ×5,
  Fiit ×3, Coopah ×3), гачки і центральні аргументи різні — щоб переслані скріншоти не
  читались як розсилка.

### Чесний мінус кампанії

**15 із 26 контактів не мають жодного іменованого референсу.** Nutracheck, Fiit, Coopah і
WithU — споживчі фітнес/нутришн апки: Erakulis заборонений, Yazen не тієї форми. Їхні
послідовності спираються на цифри з `proof-points.md` і на логіку churn / build-vs-buy, але
без стороннього підтвердження масштабу. Це структурна діра в доказовій базі кампанії, а не
проблема копірайту, і вона винесена в `_summary.md`, а не замаскована натяком на референс,
якого немає.

### Далі

Чекпоінт Вадима по текстах → `/outbound import 2026-09-01-uk-erakulis-similar`
(`closelyhq-importer`) → імпорт у closely.io руками.

---

## Правило Вадима 2026-09-12 (пізній вечір): клієнтів не називати взагалі

Попереднє рішення дозволяло Yazen для GLP-1 половини списку. **Скасовано: жодного імені
клієнта в копії повідомлень.** Знеособлений пруф — дозволено, формулювання Вадима:
«можна казати одна з юк компаній зробила х сканів».

### Два факти і точні межі кожного

| Факт | Звідки | Що можна сказати | Чого НЕ можна |
|---|---|---|---|
| 34 000 сканів за 2025 | `case-studies/yazen.md` | «one platform», «a weight-loss platform» | **гео** — країни в доках немає, UK приписувати не можна |
| 7 500 сканів за 2025, BMI verification, at checkout, compliance audit trail | `case-studies/uk-meds.md` | «a UK online pharmacy» — гео тут ліцензоване, кейс прямо каже «UK-based» | вживати поза клінічними компаніями |

`uk-meds.md` підтверджує дослівно і «integrated as a verification step in checkout», і
«Compliance team has audit trail» — обидва формулювання в листах Jeff Hadaway і Navin
Khosla чесні.

### Що це заодно полагодило

Діра «15 із 26 контактів без жодного пруфу» здебільшого закрилась: знеособлене «одна
платформа робить 34 000 сканів на рік» — це доказ масштабу без претензії на вертикаль чи
гео. Тепер **усі 26** несуть цифру з джерела. Розподіл: 24 — факт 34К без гео, 2 — факт
7,5К з UK (Medicspot і Infohealth).

Лишається чесне застереження: для споживчих фітнес/нутришн апок 34К — це все ще суміжна
вертикаль (weight-loss), просто вже без імені. Записано в `_summary.md`.

### Що довелось виправити після агента

Два речення claim'или більше, ніж є в кейсі: «ships this as a live, **named** feature»
(Daisy Ford) і «shipped as a **co-branded partnership** feature» (Ellie Hitchmough).
`yazen.md` не каже ні про named, ні про co-branded — там «FitXpress integrated into the
patient app». Переписано на те, що джерело підтверджує. Це рівно та помилка, від якої
застерігає `editorial-guardrails` #3: reserved words без доказу.

Агент також підчистив corrective «rather than» ще в 6 файлах понад ті 3, що я правив
раніше.

### Фінальна перевірка — 26 файлів, 52 повідомлення, 0 зауважень

імена клієнтів 0 · прайсинг 0 · em dash 0 · ліміти 600/550 витримані · CTA-лінк у кожному
Message 2 · `detect-ai-tells --channel dm` CLEAN на всіх тілах · цифра з джерела в кожному
· гео-претензії тільки там, де джерело їх ліцензує.
