---
campaign: 2026-08-07-us-digital-fitness
profile: nick
product: fitxpress
market: USA
analyzed: 2026-09-02
metrics_source: metrics-final.json (closely.io drill, pulled 2026-09-02T21:10:33Z, campaign 139642)
status: campaign STILL ACTIVE — 156 of 248 contacts (63%) are mid-sequence
---

# Campaign Post-Mortem — 2026-08-07-us-digital-fitness

> **Все знаменатели — из `metrics-final.json`** (Closely's own event counters).
> Колонка `sent` из `outbound-registry.py status` не используется: она считает строки
> импорта (248), а не отправки (245), и по другим кампаниям расходится в разы.
>
> **Уровень выводов.** Ответов 6 → это полоса «5-14»: направленные наблюдения с оговоркой
> «предварительно, N=X», годятся как гипотеза для следующей кампании, не как решение.
> Единственное исключение — acceptance rate: там знаменатель 245 инвайтов, и вывод по нему
> статистически прочный (см. раздел про инвайт-стадию). Процентов без знаменателя ниже нет.

## TL;DR (3 строки)
1. **Потеря — на стадии инвайта, до того как кто-то прочитал хоть одно слово.** 39/245 (15.9%)
   приняли — вдвое ниже цели 30% и вдвое ниже трёх других кампаний (25-31%); после принятия
   всё нормально: 6/39 (15.4%) ответили — как в UK 13/69 (18.8%) и Israel 34/186 (18.3%).
   Инвайты уходили **без записки**, значит копия на acceptance повлиять не могла физически.
2. **1 qualified lead из 245 инвайтов** (Jeremy McCarty, Chief Subscription & Content Officer,
   iFIT — «Yeah open to hearing more») + 1 живой оценочный вопрос (Christine May, Calibrate).
   Цели «≥4 positive / ≥2 qualified» не выполнены; негатива 0/6.
3. **Ёмкость инвайтов потрачена не туда:** 119/248 (48%) ушли в два аккаунта, 96/248 (39%) —
   в WEAK-тир, 60/248 — на angle `technical-integration` с результатом 0 ответов, а из 27
   исследованных компаний контакты нашлись только по 13 — Noom и WW (обе fit 5) не получили
   ни одного касания.

## Hypothesis vs reality

| Metric | Target | Actual | Verdict |
|--------|--------|--------|---------|
| Acceptance rate | ≥ 30% | **39/245 = 15.9%** | ✗ (половина от цели; 95% CI 11.3-20.5%) |
| Reply rate (spec: replies/accepted) | ≥ 5% | **6/39 = 15.4%** | ✓ |
| — то же на отправленных сообщениях | — | 6/67 = 9.0% | справочно (метрика Closely) |
| — то же на инвайтах | — | 6/245 = 2.4% | справочно |
| Positive replies (interested + question) | ≥ 4 | **2** (2/39 accepted = 5.1%) | ✗ |
| Qualified leads (interested) | ≥ 2 | **1** | ✗ |
| Negative reply rate | — | **0/39 = 0%** | нечего диагностировать |
| CPL | — | **нет данных о затратах** | 245 инвайтов / 1 qualified lead |

Полная воронка: 248 контактов → 245 инвайтов (1 `connection_sent_error`) → 39 accepted →
37 человек получили DM-1, 30 получили DM-2 (всего 67 сообщений) → 6 ответов от 6 человек.
Профильных визитов 449, лайков постов 29.

**Кампания не закончена:** завершены 92/248 контактов, 156 (63%) ещё в секвенции. Acceptance
может подрасти (инвайты принимают и через месяц) — но сравнение честное: UK-кампания 139205
запущена на 6 дней раньше US и завершена всего на 12%, а даёт 43/176 (24.4%).

## Что работало

### Best-performing message angle
Предварительно, N=6 ответов; знаменатели — инвайты (per-angle acceptance Closely не отдаёт,
поэтому angle и acceptance тут не разделить).

| Angle | Инвайтов | Ответов | Из них |
|---|---|---|---|
| `digital-transformation` | 28 | **2/28 (7.1%)** | referral (Chair of the Board) + maybe-later |
| `weight-management` | 30 | **1/30 (3.3%)** | question (Calibrate) |
| `member-engagement` | 129 | **3/129 (2.3%)** | **interested** + referral + stale-list |
| `technical-integration` | 60 | **0/60 (0%)** | — |

- **`member-engagement` дал единственный interested** — и это ровно тот покупатель, что описан
  в гипотезе (владелец подписочной экономики в connected-fitness):
  > «Yeah open to hearing more. Send me a note so we can get something scheduled.
  > Jeremy@ifit.com / Bree McArdle <bree.mcardle@ifit.com>» — Jeremy McCarty, Chief
  > Subscription & Content Officer, iFIT (PASS, P1), ответ на DM-1.
  Гипотеза почему: DM-1 бил в retention без новой фичи контента («Subscription economics tend
  to improve fastest when members have a visible reason to keep renewing, beyond new content»),
  то есть в KPI, который у этого человека в самом тайтле. N=1 — это гипотеза, не подтверждение.
- **`digital-transformation` — лучший процент, но это 2 ответа из 28** и оба из одного
  аккаунта (Personify Health): председатель совета директоров перевёл на Ed Liebowitz,
  Principal PM ответил «Not at this time. Please follow up later.» Ни одного interested.

### Best-converting company segments
Предварительно, N=6. Знаменатель — инвайты по аккаунту.

- **Крупные бренды с реальной подписочной базой дали все 6 ответов:** iFIT 2/56,
  Personify Health 2/63, MyFitnessPal 1/28, Calibrate 1/14.
- **Малые и средние приложения — 0 ответов на 81 инвайт суммарно:** Tonal 0/21, Hydrow 0/17,
  Future 0/13, Echelon 0/10, Ladder 0/9, Fitbod 0/6, Found 0/6, Trainwell 0/3, Shotsy 0/2.
- Гипотеза почему: fit-score не предсказал ответы вообще. iFIT (fit 3, «body-composition
  tracking not currently a named feature») дал единственный interested; fit-5 Future и
  Calibrate — 0 и 1 вопрос. Для §8 «Connected & digital fitness» лучше предсказывает не
  fit-score, а наличие в компании роли, у которой retention/subscription в тайтле.

### Best-performing personas (titles)
- **PASS-тир: 3/152 инвайтов ответили, включая единственный interested и единственный
  оценочный вопрос.** WEAK-тир: 3/96 ответили, из них 0 interested, а 2 из 3 — это флаги
  устаревшего списка («I no longer work at MFP» и «I was laid off from iFIT»).
- **Касание: DM-1 несёт эту секвенцию.** По шаговой статистике Closely: DM-1 — 5 ответов на
  37 отправок (13.5%), DM-2 — 1 на 30 (3.3%). Гипотеза: DM-2 добавляет accuracy+HIPAA, что
  сработало ровно один раз — зато сработало на исследовательском профиле (Christine May,
  Senior Director Clinical Research), то есть proof-точки нужны не всем, а клинико-
  исследовательским ролям.

## Что не работало

### Worst-performing angle
- **`technical-integration`: 0 ответов на 60 инвайтов** — самый большой нулевой блок
  кампании (24% всей ёмкости). Состав: 22 PASS + 38 WEAK, то есть больше половины — это
  инженерные роли ниже порога CTO/VP Eng, которые сама `icp-detail.md` держит на P3.
  Гипотеза почему: в consumer-app кампании технический человек не покупатель и не champion
  до появления интереса у продуктового владельца — на холодном инвайте ему просто нечего
  ответить. Это не про текст, это про то, что 60 инвайтов ушли не тем людям.

### Pattern in negative responses
- **0/6 негативных, 0 declines.** Диагностировать тон и текст не на чем — и это, вместе с
  15.4% ответов на принявших, второй аргумент, что копия не была узким местом.
- **Зато есть паттерн устаревших данных: 2 из 6 ответов (Nicole Landry, MyFitnessPal;
  Nick Karwoski, iFIT) — «я тут больше не работаю».** Оба WEAK-тир, оба из двух самых
  крупных по числу инвайтов аккаунтов. Список валидировался 2026-08-10, импорт ушёл
  2026-08-11, то есть данные устарели не у нас — они уже были устаревшими в Sales Navigator.
  → **Рекомендация:** перед импортом прогонять job-change проверку по всем контактам,
  особенно в компаниях с публичными сокращениями (iFIT).

### Companies / people we shouldn't have included
- **Personify Health — 63 инвайта (25% ёмкости) не по этой гипотезе.** Это employer /
  health-plan wellness платформа (ICP §4 «Health plans / employer wellness», $5M+, покупатель
  CHRO / VP Population Health), а не US-HQ consumer subscription app из sub-segment этой
  гипотезы. Собственные notes в `companies.csv` это и говорят: «Buyer is an enterprise
  wellness/product team, not a founder». Результат: 2 ответа, 0 interested, и средние
  показатели кампании больше не описывают ни одну из двух смешанных гипотез.
  → **не исключать компанию** (она дала referral и door-open), а вынести в отдельную
  employer-wellness кампанию с другими персонами и другой копией.
- **Andrey Patenko (iFIT) — единственный FAIL-тир в импорте**, при валидации помечен как
  вероятный омоним («Owner at Proform Fitness LLC» — независимый франчайзи, не iFIT).
  Попал в рассылку вопреки собственному вердикту.
- **10 инвайтов на partnership / sales / PR тайтлы** (VP Partnerships @ MyFitnessPal,
  Sports Marketing Partnerships Director @ iFIT, Social Media & PR Director @ iFIT,
  CRO @ Tonal, President of SaaS Partnerships & Sales @ Echelon и др.) — это входящий
  BD-канал, не покупатель фичи.
- **Nicole Landry** (ушла из MyFitnessPal) и **Nick Karwoski** (сокращён из iFIT) — исключить
  как людей, но сохранить их подсказки: Mike Hamblin (iFIT) и Ed Liebowitz (Personify) —
  новые контакты, требующие обычной ICP-квалификации.

## Инвайт-стадия: почему 15.9%, а не 30% (главный вопрос кампании)

Это единственный раздел с прочной статистикой: знаменатель — сотни инвайтов, не 6 ответов.

| Профиль / кампания | Closely account | Инвайтов | Принято | Acceptance (95% CI) |
|---|---|---|---|---|
| **nick / US digital fitness** | 34879 | 245 | 39 | **15.9%** (11.3-20.5) |
| **vadim / AU telehealth** | 25382 | 220 | 38 | **17.3%** (12.3-22.3) |
| olena / EU weightloss | 35141 | 292 | 73 | 25.0% (20.0-30.0) |
| katerina / UK digital health | 23972 | 258 | 69 | 26.7% (21.3-32.1) |
| katya / Israel telehealth | 25040 | 608 | 186 | 30.6% (26.9-34.3) |

Объединённо: **77/465 (16.6%) с двух аккаунтов против 328/1158 (28.3%) с трёх** —
разница 11.8 п.п., z = 5.4, p ≈ 6·10⁻⁸. Это не артефакт малой выборки.

**Что проверено и НЕ объясняет разрыв:**
- **Копия и записка.** Все семь Closely-кампаний имеют пустой текст на шаге
  `connection_message` — инвайты шли **без записки** во всех пяти профилях. Значит копия
  вообще не участвует в acceptance. (Заодно это снимает версию «виновата написанная записка»,
  которую предлагали для AU-кампании: у US записки не было и acceptance ещё ниже.)
- **Размер компаний-целей.** Israel бил в гигантов (Clalit 66 контактов, Maccabi 63) и дал
  29.9% на своей агентской кампании 138170 (38/127). US бил в Personify 63 / iFIT 56 и дал
  15.9%. Концентрация и размер аккаунта не разделяют группы.
- **Сеньорность.** Во всех четырёх списках доминирует VP/Head/Director (US 52%, UK 74%,
  IL 69%, AU 65%). US заметно тяжелее по CEO/Founder (60/248 = 24%) — это самая
  инвайт-устойчивая группа, но одного этого на 12 п.п. не хватает.
- **Зрелость кампании.** UK 139205 запущена 2026-08-05 (раньше US), завершена на 12%, а даёт
  24.4%. Незрелость US-кампании разрыв не объясняет.
- **Качество списка.** В US-списке нет мусора уровня AU (там 33 инвайта ушли людям с явным
  вердиктом FAIL). Здесь FAIL всего 1.

**Что остаётся (H1, ведущая гипотеза): сам отправляющий профиль.** Пять аккаунтов —
пять значений acceptance, и линия разреза проходит ровно по аккаунтам, а не по гео,
вертикали, размеру компаний или структуре секвенции. Возраст аккаунта в Closely тут не
причина: у olena самый свежий id (35141) и 25.0%.

**Честная оговорка:** по нашей же гео-дисциплине профиль ↔ рынок связаны 1:1, поэтому
«профиль» и «рынок США» в этих данных неразделимы. US — самый перегретый рынок холодного
LinkedIn-аутрича, и это конкурирующее объяснение H2, которое нельзя опровергнуть, пока
один и тот же список не уйдёт с двух профилей.

## Learnings → next hypothesis

### Confirm
- **§8 «Connected & digital fitness», покупатель = владелец подписки/retention.** Единственный
  interested — Chief Subscription & Content Officer (PASS, P1), ответ на retention-angle.
  Заносить в core ICP как «искать тайтл, где subscription/retention/engagement стоит в самом
  названии роли», а не «CPO вообще». (N=1 — заносим как приоритет поиска, не как правило.)
- **Копия и таргетинг «после принятия» работают.** 6/39 (15.4%) ответов на принявших против
  UK 13/69 (18.8%) и Israel 34/186 (18.3%) — статистически неразличимо, и лучше, чем
  EU 4/73 (5.5%). Переписывать сообщения ради этой кампании не нужно.
- **Оценочные вопросы приходят от клинико-исследовательских ролей на DM-2 с proof-точками**
  (Calibrate, Senior Director Clinical Research → сравнение с Withings Body Pro).

### Reject
- **`technical-integration` как холодный инвайт в consumer-app кампании** — 0/60. Оставить
  angle только для маршрутизации после ответа продуктового владельца.
- **Массовый добор WEAK-тиром.** 96/248 инвайтов (39%) → 0 interested и 2 из 3 ответов —
  устаревшие данные. WEAK — только как добор после исчерпания PASS, и никогда не 39% ёмкости.
- **Fit-score как предиктор ответа** в этом сегменте: fit 3 дал interested, fit 5 — 0 и 1
  вопрос. Не отменять fit-score для отбора компаний, но не сортировать по нему приоритет касаний.
- **Смешивание двух ICP-сегментов в одной кампании** (consumer app §8 + employer wellness §4).

### New hypotheses to test
- **H1 (главная, дешёвая):** acceptance определяется отправляющим профилем, а не списком.
  Тест: один список делится 50/50 между `nick` и профилем с 25%+ (например `katerina`),
  одинаковая копия, одна неделя. Нужно **≈200 инвайтов на плечо** — на 120 мощности не хватит
  (ожидаемый разрыв 11 п.п.). До теста — бесплатный аудит профиля Nick: число связей,
  headline, наличие активности/постов, объём висящих pending-инвайтов, Sales Nav.
- **H2:** acceptance определяется рынком (US перегрет), а не профилем. Отделяется тем же
  тестом: если оба плеча дают ~16%, виноват рынок и надо менять само гео-предположение
  (меньше «холодных» инвайтов, больше warm-intro / referral-пути).
- **H3:** ответы дают только компании, где есть роль с retention/subscription в тайтле.
  Тест: следующий US-список строить по тайтлам, а не по компаниям, и мерить reply-on-accepted
  в двух ветках.
- **H4:** конкурентное сравнение (FitXpress vs smart-scale / BIA) как вариант DM-2 поднимает
  долю оценочных вопросов. Триггер — единственный вопрос кампании был ровно об этом.
- **H5:** job-change проверка перед импортом убирает 5-10% мёртвых контактов. Тест: сравнить
  долю «я тут больше не работаю» в следующей кампании (сейчас 2 из 6 ответов).

## Recommendations for next campaign
1. **Не менять копию — сначала починить инвайт-стадию.** Аудит LinkedIn-профиля Nick
   (связи, headline, активность, pending-инвайты, Sales Nav) до запуска следующей кампании;
   потом split-тест H1 на 200 инвайтов на плечо.
2. **Ввести правило потолка на аккаунт: ≤15 инвайтов на компанию и ≥10 компаний в кампании.**
   Здесь 48% ёмкости ушло в два аккаунта, и оба дали ответы уровня referral/maybe-later.
3. **Инвайтить только PASS, пока acceptance ниже 25%.** WEAK — добор, помеченный как добор.
4. **Убрать `technical-integration` из холодных касаний** consumer-app кампаний.
5. **Прогонять job-change проверку на всех контактах старше 30 дней** и отдельно —
   по компаниям с публичными сокращениями.
6. **Расщепить Personify Health в отдельную employer-wellness кампанию** (ICP §4, покупатели
   CHRO / VP Population Health / Head of Wellness), не смешивать с §8.
7. **Закрыть покрытие компаний:** контакты нашлись только по 13 из 27 исследованных, при этом
   Noom и WW (обе fit 5), Peloton, Ro, Whoop, Strava не получили ни одного касания. Либо
   добрать их через Sales Nav, либо честно вычеркнуть из `companies.csv`, чтобы список компаний
   и список людей перестали расходиться.
8. **Сделать one-pager «FitXpress vs Withings Body Pro / смарт-весы / BIA»** — и ответить
   Christine May сейчас, пока вопрос живой.

## Updates to `CLAUDE.md`
Конкретный diff, который стоит внести (сам файл не правлю — это менеджерское решение):

```diff
 ## 11. Метрики
-- **Outbound:** acceptance rate, reply rate, positive reply rate, qualified leads, передано в sales (per-product)
+- **Outbound:** acceptance rate, reply rate, positive reply rate, qualified leads, передано в sales (per-product)
+  - acceptance rate ведём **per sending profile**, а не только per campaign: это метрика
+    аккаунта, а не кампании. Инвайты уходят без записки, поэтому копия на acceptance не влияет.
+  - **порог:** acceptance < 20% на ≥150 инвайтах ⇒ кампанию не «лечим текстом», а
+    останавливаем и проверяем профиль (связи, headline, активность, pending-инвайты, Sales Nav).
+    Замер 2026-09-02: nick 39/245 (15.9%), vadim 38/220 (17.3%) против olena 25.0%,
+    katerina 26.7%, katya 30.6% — разрыв 11.8 п.п., p ≈ 6·10⁻⁸.
```

```diff
 ## 5. Профили в социальных сетях
 Гіпотеза й список компаній кампанії мають відповідати ринку профілю (гео-дисципліна).
+**Побочный эффект дисциплины:** профиль ↔ рынок связаны 1:1, поэтому эффект профиля и
+эффект рынка в наших данных статистически неразделимы. Для диагностики acceptance
+разрешается ровно одно исключение: **split-тест одного списка между двумя профилями**
+(≈200 инвайтов на плечо), с явной пометкой в hypothesis.md.
```

```diff
 ### FitXpress ICP
+**Одна кампания = один ICP-сегмент.** Смешивание сегментов делает средние показатели
+кампании неинтерпретируемыми (2026-08-07-us-digital-fitness: §8 consumer apps + §4 employer
+wellness в одном списке, 25% инвайтов ушло в Personify Health по копии для §8).
```

## Updates to the exclusion registry

**Уже записано в реестр** (единственный писатель — `scripts/outbound-registry.py`, JSON руками
не правился):

```
python3 scripts/outbound-registry.py reply --campaign 2026-08-07-us-digital-fitness --profile nick
→ 6 classified replies, 6 registry people updated, 0 not matched by URL
```

⚠️ **Починка, без которой эта команда молча ничего не делала.** `reply` ищет человека по
LinkedIn-URL, а `responses-classified.csv` от step 8 URL не содержал (только `person_id`) —
команда возвращала «0 classified replies, 0 registry people updated» и **выходила с кодом 0**,
то есть тихо не работала. Я добавил колонку `linkedin_url` в `responses-classified.csv`
(значения взяты из `responses-raw.csv` этой же кампании по `person_id`, 6/6 совпали).
**Системная правка нужна в пайплайне:** либо `response-classifier` обязан прокидывать
`linkedin_url`, либо `cmd_reply` должен фолбэчить на `responses-raw.csv` по `person_id`.

**Person-level — исключить из будущих кампаний:**
| Человек | Компания | Причина |
|---|---|---|
| Nicole Landry | MyFitnessPal | ушла из компании («I no longer work at MFP»), новый работодатель не подтверждён |
| Nick Karwoski | iFIT | сокращён, покупателем быть не может (его подсказка — Mike Hamblin) |
| Andrey Patenko | iFIT | FAIL при валидации: омоним, «Owner at Proform Fitness LLC» |
| Maria/партнёрские тайтлы (10 чел.) | iFIT, Tonal, MyFitnessPal, Echelon | partnership / sales / PR роли — входящий BD-канал, не покупатель фичи |

**Company-level — менять статус не нужно, но пометить:**
- `personify-health` (сейчас `active` под `nick`) — переклассифицировать как ICP §4
  employer wellness; следующий подход только с employer-wellness гипотезой и персонами.
- `ifit`, `calibrate` — держать под `nick`, это источники обоих живых сигналов кампании.
- `tonal`, `hydrow`, `future`, `echelon`, `ladder`, `fitbod`, `found`, `trainwell`, `shotsy` —
  0 ответов на 81 инвайт. Правило «освобождается через 6 месяцев при `reply = no_reply`»
  теперь применимо: исходы записаны. Досрочно не освобождать, но при следующем подходе менять
  персону, а не текст.
- Новые контакты на квалификацию (не в исключения): **Mike Hamblin** (iFIT, от Nick Karwoski),
  **Ed Liebowitz** (от Chris Michalak, Personify Health).

## Открытые вопросы к Вадиму
1. Аудит профиля Nick — сделаешь сам в LinkedIn (связи / headline / pending-инвайты / Sales Nav)
   или ставим split-тест H1 сразу?
2. Согласен вынести Personify Health в отдельную employer-wellness кампанию?
3. Кампания ещё активна (156/248 в секвенции). Перезамерять метрики через 2-3 недели и
   обновить этот файл, или считать разбор финальным?
4. Christine May (Calibrate) ждёт ответа по сравнению с Withings Body Pro — черновик готов в
   `responses-classified.csv`; отправляешь ты или Nick?
