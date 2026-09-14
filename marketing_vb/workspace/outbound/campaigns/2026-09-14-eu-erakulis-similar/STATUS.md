# STATUS — 2026-09-14-eu-erakulis-similar

**Крок 2 пройдено 2026-09-14: 15 рядків / 10 незалежних компаній. Блокер — рішення Вадима по гейту 12, потім виписка Sales Navigator.**

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
3. **Вадим**: виписка Sales Navigator у `sales-nav-raw/` — **за посадами, не за компанією**
   (список посад і кепи інвайтів — гіпотеза, «Sales Navigator pull for step 3»). UK-виписка
   за компанією дала 72 з 98 людей, які кандидатами не були ніколи.
4. `/outbound extract 2026-09-14-eu-erakulis-similar` → `validate` → чекпоінт менеджера.
