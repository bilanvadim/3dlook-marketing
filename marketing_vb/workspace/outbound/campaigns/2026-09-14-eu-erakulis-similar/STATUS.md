# STATUS — 2026-09-14-eu-erakulis-similar

**Крок 4 v4 (validate, пули I–M) пройдено 2026-09-28: 125 SEND (хвиля 1 — 106, хвиля 2 — 19), 0 WEAK. Чекпоінт менеджера: апрув Вадима до кроку 5 (messages).**

Континентальна європейська сестра `2026-09-01-uk-erakulis-similar` (`katerina`). Та сама
ідея: консьюмерські fitness / nutrition / wellness апки, look-alike під клієнта Erakulis.
Профіль `olena`.

---

## Рішення Вадима 2026-09-14 (апрув гіпотези)

| # | Питання | Рішення |
|---|---|---|
| 1 | Поріг штату | **25+**, тільки для цієї кампанії, `icp-detail.md` не змінюється |
| 2 | Ексклюзивність з Erakulis | **немає** — його конкуренти законні цілі |
| 3 | Українські апки з продуктом у Києві | **беремо на `olena`**, тег `product_hq=UA`; це виняток з `icp-detail.md:563` (ринки без комплаєнс-ліцензії), тільки для цієї кампанії |
| 4 | Кіпр, Мальта, Люксембург, Ісландія, Ліхтенштейн | **до `olena`** — додано в `PROFILE_GEO` (`scripts/outbound-pipeline.py`) |
| 5 | Flavour 4 (app-first weight-management / GLP-1) | **прибрано** — анти-кейс, територія `2026-07-21`; GLP-1 mode лишається сигналом скорингу у flavour 3 |
| 6 | Мова | **тільки англійська** |
| 7 | «112,100 scans in 2025» (`proof-points.md:113`) | **дозволено** в холодній копії як загальний масштаб 3DLOOK |

Правила з UK-кампанії, що діють і тут: **жодного імені клієнта** в копії, **жодного
прайсингу** в усій послідовності, «FitXpress is not a medical device.», GDPR-роль дослівно.
Дозволені пруфи: «one platform ran 34,000 scans in 2025» (без гео) і 112,100 сканів за
2025 (без клієнтів і гео). UK Meds 7,5К тут не використовується.

Відкрите: **OQ#7** — затверджених відповідей на Article 9, DPA, SCC, EU AI Act немає.
Потрібно до discovery-дзвінків, не до кроку 2.

## Що зроблено 2026-09-14

- `hypothesis-generator` написав гіпотезу. Auto-QC **13/20**, «fix first»:
  розрив у гейтах розміру (10-14 не визначено), Kilo €404M «за 2025» з релізу від листопада
  2025, непідтверджене «Freeletics camera rep counting», хибні внутрішні числа. Звіт:
  `workspace/_quality/outbound/2026-09-14-hypothesis-generator-eu-erakulis-similar.md`
  (з `coordinator_review`). Усі 8 пунктів виправлено тим самим агентом точковими правками.
  Kilo тепер: «surpass €233 million this year» (in-year прогноз). Freeletics-камера прибрана.
- Рішення Вадима внесено в гіпотезу, `status: approved`.
- `hypothesis-gate --stamp` → scope hash **`abe517aedf7a6f0f`**, 9 scope-секцій.
- `search-health.py` — зелений (20 результатів).
- `PROFILE_GEO` для `olena` + cyprus, malta, luxembourg, iceland, liechtenstein. Перевірено
  `geo_profile()`: усі п'ять → `olena`, Northern Ireland і «England (US parent)» лишились
  `katerina`.

### Регресія: `test-outbound-pipeline.sh` — полагоджено, **63 passed, 0 failed**

Перший прогін після правки гео дав 56/4. Падіння були не від неї: чотири перевірки
`validate-companies` читали списки живої UK-кампанії, які 2026-09-12 переїхали в
`_superseded-2026-09-12/` (exit 2, `no companies CSV`). Полагоджено за Вадимовим проханням:

- `validate-companies` тепер на inline-фікстурах у тимчасовій кампанії `_test-validate`
  (та сама схема, що `check-responses`), не залежить від того, де живі кампанії тримають файли.
- Знайдено і закрито вхолосту зелений тест: «unapproved status -> 1» шукав
  `- **Status:** approved`, а гіпотеза тримає `status:` у frontmatter. Заміна нічого не
  міняла, exit 1 давав попередній sub-segment edit. Новий хелпер `mutate` рахує промах
  правки фікстури як падіння; плюс перевірка, що причина саме `status is draft`.
- Додано дві перевірки на scope lock усередині `validate-companies` (раніше не покрито).

## Гейти кроку 2 (з гіпотези)

- **≥12 компаній на 25+ → крок 3**; менше 12 → стоп на кроці 2, звіт Вадиму, гіпотеза
  фальсифікована. Ціль 15-20. Реалістична оцінка агента: 8-18.
- Повна step-2 схема + `notes`: `flavour`, `body_metrics`, `glp1_mode`, `parent`,
  `legal_hq/product_hq/hq_basis`.
- `web-verify` на кожному рядку; `blocked` → лише `verified-manual` після реальної ручної
  перевірки. `validate-companies --profile olena --write-routed` exit 0.

## Крок 2 пройдено 2026-09-14 — 15 рядків, але 10 незалежних компаній

`validate-companies --profile olena` — exit 0 (перезапущено координатором): 15 proceed,
1 routed (Simple → `katerina`, продуктовий HQ London), 0 errors, 0 warnings. Звірка з
`olena-registry.json` і `global-company-registry.json` — 0 збігів. Верифікація: 14
`verified-live`, 2 `verified-manual` (Lifesum, DoFasting — Google Play + jobs page у `notes`).

| Група / компанія | Рядків | Країна | Штат |
|---|---:|---|---|
| Welltech (FitCoach, Muscle Booster, WalkFit, Yoga-Go, Omo) | 5 | Ukraine (legal Cyprus) | 793-810 група |
| Kilo Health (DoFasting, Keto Cycle) | 2 | Lithuania | 500+ група |
| BetterMe | 1 | Ukraine | 736-766 |
| Gymondo | 1 | Germany | 82-100 |
| Yazio | 1 | Germany | 144 |
| Freeletics | 1 | Germany | 103-120 |
| Fastic | 1 | Germany | 51-100 |
| Lifesum | 1 | Sweden | 50-70 |
| Activerse (Diet & Training by Ann) | 1 | Poland | 37 |
| Fitify | 1 | Czech Republic | 27-29 |

**⚠ Рішення Вадима:** гейт «≥12 companies» агент порахував по брендах. Гіпотеза прямо
каже, що рядок для групи — бренд (L69, L212), тож формально 15 ≥ 12. Але незалежних
організацій **10 < 12**, і Welltech — третина рядків. Кепи з гіпотези все одно тримають
інвайти: ≤5 на бренд, ≤12 на групу, ≤15% кампанії на групу.

## Дальше

1. ~~`company-researcher`~~ — готово, див. вище.
2. ~~15 брендів чи 10 компаній проти гейта 12~~ — **Вадим 2026-09-14: йдемо далі з цим
   списком** (15 брендів / 10 компаній), не добираємо. Кепи інвайтів на групу лишаються.
3. ~~Виписка Sales Navigator~~ — 2026-09-28, але **за компанією, не за посадами** (344 рядки).
4. ~~`extract` → `validate`~~ — готово 2026-09-28, див. нижче. **Чекпоінт менеджера.**
5. Після апруву Вадима: `message-sequencer` (крок 5) на затверджений SEND-список.

## Крок 4 (validate) — 2026-09-28

Вхід: `people-raw.csv`, 321 людина (`extract-people` з `sales-nav-raw/2026-09-28-sales-nav-olena.csv`).
Реєстр: `outbound-registry.py check --profile olena` → **321 clear, 0 excluded** (`people-checked.csv`).
Вихід: `people-validated.csv` (ідентичність збережена: `first_name`, `last_name`, `linkedin_url`,
0 рядків без URL; додано колонки `group`, `product_hq_tag`, `send`) і `icp-validation-summary.md`.

| | Кількість |
|---|---:|
| PASS | 36 (P1 12, P2 11, P3 13) |
| — SEND (хвиля 1, у кепах) | **22** |
| — HOLD (CTO / Head of Technology, P3, не холодний перший дотик) | 7 |
| — RESERVE (Yazio понад кеп 5) | 7 |
| WEAK → рев'ю Вадима | 9 |
| FAIL | 276 (з них 2 UK → `ROUTE-katerina`, 8 колізій імен / порожніх профілів) |

SEND по групах: Welltech 5, Yazio 5, Gymondo 4, BetterMe 3, Freeletics 3, Lifesum 1, Fitify 1.
Kilo — **0 покупців з 31** (тільки груповий рівень, Bioma-добавки, фінанси). Fastic і Activerse —
лише співзасновники-CTO (WEAK).

**Що вирішує Вадим:**

1. SEND 22 — апрув як хвиля 1?
2. Кеп 15% на цьому розмірі не виконується (Welltech і Yazio по 23%, Gymondo 18%): при 7
   компаніях він тримається лише на 1 інвайті на компанію. Вейвер для хвилі 1 чи урізати
   Welltech і Yazio до 3 (19 інвайтів)?
3. WEAK 9 — кого беремо (головне: Ugnius Zykas — єдиний вхід у Kilo, Thomas Adam — Fastic,
   Tomasz Gałczyński — Activerse).
4. Elle Pope (Director of Engagement & Retention) і Shimrit Shiran (Head of Growth), Welltech,
   обоє в UK: до `katerina` (ламає «одна компанія = один профіль»), вейвер на `olena` чи викинути?
5. Перевиписка Sales Navigator **за посадами** до відправки чи хвиля 1 зараз + хвиля 2 пізніше.
   22 інвайти ≈ 6 прийнятих; тест фальсифікації потребує ≥30 прийнятих, тож без добору
   кампанія буде inconclusive за конструкцією.

**Знахідки:** виписка за компанією дала 86% не-покупців (276/321). Немає бренд-GM для Muscle
Booster / WalkFit / Yoga-Go, CPO BetterMe, CPO Yazio, GM DoFasting / Keto Cycle. Welltech на
LinkedIn називає лише 3 апки (Muscle Booster, Yoga-Go, WalkFit): FitCoach і Omo з кроку 2
треба перевірити до того, як `message-sequencer` їх згадає. Найточніші попадання — Bogdan
Rogovchenko (BetterMe, Lead PO «Hardware & Wearable Ecosystems», смарт-ваги) і Talita Morato
(Yazio, Product Lead «Tracking Experience»).

## Крок 4 v2 — 2026-09-28 (персона розширена)

Вадим переглянув `skipped-detail.md` і взяв **усі шість пулів A-F**. Гіпотезу оновлено й
перештамповано (scope hash **`4fab53d0c269ea3a`**, секція «Vadim's decisions 2026-09-28»).
Нові кепи: **≤25 на компанію / групу**, правило 15% знято. CTO тепер можна брати холодним
першим дотиком (кут technical-integration). UK-люди Welltech (Elle Pope, Shimrit Shiran)
лишаються на `olena` як виняток. v1 збережено як `people-validated-v1-2026-09-28.csv`.

Реєстр: 321 clear, 0 excluded. `people-validated.csv` переписано (ідентичність на місці, 0 без
URL; нова колонка `pool`). **PASS 86 = SEND 86** (P1 13, P2 53, P3 20), **WEAK 0**, **FAIL 235**.

| Група | SEND | Частка | Кеп 25 |
|---|---:|---:|---|
| BetterMe | 25 | 29% | **впритул** |
| Welltech | 21 | 24% | 4 вільних |
| Yazio | 15 | 17% | |
| Freeletics | 9 | 10% | |
| Gymondo | 5 | 6% | |
| Kilo | 4 | 5% | |
| Lifesum | 3 | 3% | |
| Fitify | 2 | 2% | |
| Fastic | 1 | 1% | |
| Activerse | 1 | 1% | |

Кути: product 41, retention 28, technical-integration 11, referral 6.
Джерела: v1 22 + A 30 + B 7 + C 5 + D 9 + E 5 + F 7 + **1 поза пулами** (Lina Jasaite,
Managing Director Kilo, P3 referral: MD є в include-списку, у Kilo немає власника продукту
DoFasting / Keto Cycle).

**Що вирішує Вадим:** (1) Lina Jasaite — лишаємо? (2) BetterMe на кепі 25: кого знімаємо, якщо
перевиписка знайде CPO / Head of Product? (3) Referral-запити пулу C (Weber, Gners, O'Connell)
не слати раніше за продуктових лідів тієї ж компанії: персона каже «тільки де немає
product lead», а в цих трьох компаніях він є.

Не взято: UA / ASO / paid media, BD і партнерства, user success, фінанси, HR, інженерія нижче
CTO, дизайн, контент-продюсери, коучі й клініцисти, колізії імен, Bioma / добавки, платіжні
й фізичні PM. Концентрація BetterMe + Welltech = 53% — прийнята свідомо, `analyze` звітує по
групах. Повідомлення (крок 5) не починались.

## Крок 4 v3 — 2026-09-28 (адендум: пули G і H)

Вадим узяв усіх додатково запропонованих. Гіпотеза перештампована (scope hash
**`715a0f49ebdffa69`**, блок «Addendum, same day»). Кеп тепер **≤30 на компанію / групу**.
Referral-люди йдуть лише після продуктових і retention-людей тієї ж компанії. v2 збережено як
`people-validated-v2-2026-09-28.csv`. У `people-validated.csv` нова колонка `wave`: 1 —
product / retention / technical-integration, 2 — referral.

Компанію кожного з 19 доданих звірено з сирою випискою: `Company linkedin_url` збігається зі
сторінкою компанії зі списку кроку 2. 18 → SEND (P3). **elisa knowles → FAIL:** це не колізія
імені (вона прив'язана до сторінки kilo-health), але профіль в один рядок, без історії, UK, а
CEO Kilo Žygimantas Surintas є в тій самій виписці з повним профілем.

**Підсумок v3:** PASS = SEND **104** (P1 13, P2 53, P3 38), WEAK 0, FAIL 217. Кути: product 45,
retention 28, technical-integration 15, referral 16. Хвиля 1 — 88, хвиля 2 — 16.
По групах (кеп 30): Welltech 27, BetterMe 25, Yazio 17, Freeletics 11, Kilo 7, Gymondo 6,
Lifesum 6, Fastic 2, Fitify 2, Activerse 1.

**Увага:** у Kilo хвиля 1 — лише одна PM (Renata Roze), решта 6 — referral. У Fastic хвиля 1 —
лише співзасновник-CTO. Застереження в `reason`: Stovpova (заголовок «User Acquisition Lead»),
Mohammad A. (заголовок «Advisor / Angel Investor»), Cristina G. (порожній профіль).
Повідомлення (крок 5) не починались.

## Крок 4 v4 — 2026-09-28 (другий адендум: пули I–M)

Вадим узяв обидва додаткові яруси. Гіпотеза перештампована (scope hash **`4225612978b5c6d6`**,
блок «Second addendum, same day»). Кеп тепер **≤35 на компанію / групу**. Новий кут
`insurer-prevention` (Gymondo, канал профілактики через страховики). Перевиписки Sales
Navigator за посадами поки не буде. **Хвиля 2 Kilo виходить за датою** — через тиждень після її
хвилі 1, а не за прийняттям інвайту Renata Roze; це записано в новій колонці `release_note`
(7 рядків). v3 збережено як `people-validated-v3-2026-09-28.csv`, усі 321 рядки на місці.

Усіх 21 доданих звірено з сирою випискою: `Company linkedin_url` збігається зі сторінкою
компанії, і сторінка записана в `reason`. **21 з 21 — SEND, відмов немає.**

**Підсумок v4:** PASS = SEND **125** (P1 13, P2 55, P3 57), WEAK 0, FAIL 196. Кути: product 52,
retention 34, referral 19, technical-integration 18, insurer-prevention 2. Хвиля 1 — 106,
хвиля 2 — 19. По групах (кеп 35): **Welltech 35 (впритул)**, BetterMe 30, Yazio 22, Freeletics 11,
Gymondo 8, Kilo 8, Lifesum 6, Fastic 2, Fitify 2, Activerse 1.

**Увага:** UK-винятків на `olena` тепер 6 (Pope, Shiran, Schwartz, Freeth, Domínguez,
Goncharenko). Для кута `insurer-prevention` ще немає затвердженої копії: лише твердження з
`compliance.md` / `proof-points.md`, жодних тверджень про правила відшкодування страховиків.
Повідомлення (крок 5) не починались.

---

## Крок 5 пройдено 2026-09-28 — 125 контактів, 250 повідомлень

`message-sequencer` у чотири паралельні пачки (Welltech 35 · BetterMe 30 · Yazio 22 · решта 38).
Файли — `messages/{person_id}.md`, зведення — `messages/_summary.md` (+ `_summary-{batch}.md`).
Список до розсилки — `people-approved.csv` (125 SEND з v4).

Перевірено скриптом координатора: 125/125 файлів, ліміти 600/550, детектор 250/250 CLEAN,
0 клієнтів / конкурентів / цін / тире, FitCoach і Omo не згадано. Координатор виправив:
«80+ measurements» → «80+ body measurements» (30 файлів), 11 шаблонних вступів.
Welltech-пачка спершу загубила Stan Gladkov (кома в посаді зламала `awk`-розбір) — дописано.

**Далі:** чекпоінт Вадима по текстах → `/outbound import 2026-09-14-eu-erakulis-similar`
(`closelyhq-importer`, дві хвилі; Kilo хвиля 2 — через тиждень) → `check-import` → імпорт руками.

---

## Крок 6 зібрано 2026-09-28 — три CSV для closely.io, `check-import` exit 0

Вадим апрувнув тексти. `closelyhq-import.csv` (хвиля 1, 106) · `closelyhq-import-wave2.csv`
(12 рефералів, після хвилі 1) · `closelyhq-import-wave2-kilo.csv` (7, через тиждень після Kilo хвилі 1).
Деталі й кроки — `import-log.md`. **Далі — Вадим:** імпорт у closely.io руками →
`outbound-registry.py record --campaign 2026-09-14-eu-erakulis-similar --profile olena`.

---

## 2026-09-28 (вечір): гейти переведено на `scripts/outbound_pack.py`

У frontmatter гіпотези додано `use_case: fx-digital-fitness`, `cap_per_group: 35` і
`banned_terms: [FitCoach, Omo]`. Це ті самі рішення Вадима від 09-28, тепер у формі, яку
читає код; скоуп гіпотези не змінився (`hypothesis-gate` зелений). `check-messages` по
кампанії: 125 людей, 250 повідомлень, 0 провалів, 15 заміток (`messages/_check.json`).
`build-import` у тимчасову папку дав файли, байт-у-байт однакові з імпортованими.
