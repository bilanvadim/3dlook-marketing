# Superseded 2026-09-12

Всё, что лежало в кампании до перезапуска шага 2. Ничего не удалено — это запись
о том, что было заявлено.

## Почему списки заменены

Кампания несла три несовместимых определения сегмента одновременно:

1. `hypothesis-glp1-2026-09-01.md` — private GLP-1 / weight-loss telehealth, England-HQ, cash-pay
2. запрос Вадима в Telegram 2026-09-02 03:23 — «додати епки з фізичними вправами, фітнес епки та нутрішн епки»
3. сам сид **Erakulis** — general wellness app (fitness + nutrition + mind) и **действующий клиент 3DLOOK**
   с BodyScan по фото; «erakulis-similar» = look-alike кампания под клиента, а не GLP-1 вертикаль

Разбор верифицированного GLP-1 списка (30 строк) против его же anti-cases:

| Нарушение | Строк |
|---|---|
| нет приложения вообще («pure dispensing pharmacies» — прямой anti-case) | 13 |
| coaching отсутствует или `Basic` | 12 |
| нет подписки | 5 |
| `app_first = Partial` | 14 |
| HQ не England (Wales, US parent) | 3 |
| **реально проходят гипотезу** | **12**, из них Oviva (NHS tier-3) и Hims & Hers UK (US parent) — anti-cases → **~11** |

Собственные validation criteria гипотезы: «меньше 15 → сегмент слишком тонкий, остановиться
на шаге 2». Список добирал до 30 только за счёт аптек, которые гипотеза исключает.

Плюс `validate-companies` на нём: нет `icp_fit`, `linkedin_url`, `hq_city`, `employees` —
то есть приоритизировать нечем и строить поиск в Sales Navigator не из чего.

Отдельно: расширенный список в `quarantine-2026-09-02/` собран в окно, когда SearXNG был
слепым (03:50–05:08, все апстрим-движки в suspend по rate-limit и CAPTCHA) — он написан
по памяти модели, а не найден.

## Решение Вадима 2026-09-12

Сегмент: **wellness / fitness / nutrition апки (Erakulis-like)**. Гео: **вся UK**
(England + Scotland + Wales + NI). `hypothesis.md` переписан, шаг 2 перезапущен.

## Что отсюда ещё пригодится

- `companies-glp1-telehealth-verified.csv` — 11-12 чистых app-first GLP-1 провайдеров
  (Juniper, Second Nature, Voy, Numan, Piko, CheqUp, NowPatient, Medicspot, heySlim,
  Jood Life, Dr Frank's). Это законный под-срез новой гипотезы; researcher может взять
  их как стартовые кандидаты, но должен пере-верифицировать и проставить fit.
- `quarantine-2026-09-02/companies-routed-out.csv` — Lose It! / MyFitnessPal / Noom → `nick`,
  Lifesum → `olena`. Их профильные кампании, не эта.
- Bupa Global и Aetna UK — реальный ICP (§4 health plans), но другой buyer и другое
  сообщение. Своя гипотеза.
