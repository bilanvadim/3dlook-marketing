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
