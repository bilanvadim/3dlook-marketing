# Tone of Voice и language guardrails — полный текст и история синков

> Вынесено из `CLAUDE.md` §6 2026-09-28 (токен-диета). `CLAUDE.md` грузится в контекст
> каждой сессии и каждого агента, который открыл файл в `marketing_vb/`; полный текст этой
> секции нужен не всем. В `CLAUDE.md` осталась выжимка с правилами, здесь — полный текст,
> дословно, с обоснованиями и историей. **Кто читает:** тот, кто меняет правило или выясняет, почему оно такое; еженедельный синк guards дописывает датированные блоки сюда. Писателям и редакторам достаточно выжимки в `CLAUDE.md`, `hard-bans-card.md` и `terminology-guardrails.md`.
> При расхождении выжимки и этого файла прав этот файл: поправь выжимку.

## 6. Tone of Voice

> **Канонические источники голоса и аудитории (читать перед любой задачей на письмо):**
> - `about-me.md` (корень репо) — brand voice FitXpress: voice fingerprint, register, claims discipline (hard rules), accuracy/repeatability framing, слова которые USE / NEVER use, структура статьи, CTA discipline. Это источник правды по тому, *как* писать health-контент.
> - `audience.md` (корень репо) — *для кого* пишем: shared spine + 7 health-сегментов (who · core pain · hook · «what NOT to say»).
> - **`brand-assets/content-strategy/terminology-guardrails.md`** — *какими словами* писать: General Approach & Language Guardrails, офлайн-копия [Doc Ассель](https://docs.google.com/document/d/1dPNXQL62t_y82MFJblBidEvRgwXjJxzADdapB7Pa214/edit) (doc changed after 2026-09-14, synced 2026-09-28; previous sync 2026-09-14; сырой экспорт для следующего диффа — `terminology-guardrails.source.txt` рядом). Part 1 — десять правил построения фразы, Part 2 — fourteen word rules (§2.14 "Organization" added 2026-09-28), Part 3 — grep-таблица. Действует на ВЕСЬ корпоративный контент: статьи, страницы сайта, посты, outbound, whitepaper, деки. Канальных исключений нет.
>
> Секция 6 ниже — краткое операционное резюме. При конфликте `about-me.md` имеет приоритет по голосу и claims discipline; `terminology-guardrails.md` — по **выбору слов и построению фразы** (он новее и принадлежит редакционному владельцу: две правки переопределили `editorial-guardrails.md`, синк 2026-09-14 поправил строку «Buyer framing» в `about-me.md` и IEEE-строки фактуры — см. блоки ниже). Фактура (числа, кейсы) — всегда из `brand-assets/product-info/`, а не из этих файлов.

**Что мы:**
- Экспертные, опираемся на данные (96-97% accuracy, ±3.5%, 45 sec, 80+ measurements) — формулировки точности дословно из `brand-assets/product-info/accuracy-formulations.md`, не пересобранные из чисел
- Конкретные — числа, проценты, имена клиентов (UK Meds, Safariland, Burlington Medical), market sizing ($25-200M TAM)
- Уважаем время читателя — никаких длинных вступлений
- Outcome-focused — говорим про business KPI клиента, не про features

**Что мы НЕ:**
- Не делаем clickbait
- Не используем emoji-flood (1-2 макс, и только если уместно)
- Не бросаемся buzzwords без подкрепления
- Не пишем «AI помог увеличить X на Y%» без указания методологии
- Не позиционируем себя как «just an API» — мы trusted workflow layer

**No-go фразы / клише:**
- «In today's fast-paced world…»
- «Game-changer», «revolutionary», «cutting-edge», «disrupt»
- «Unlock the power of…»
- «Are you struggling with…?»
- «It's no secret that…»
- «AI-powered» как самостоятельная ценность (нужно дополнять чем именно)

> **Полный каталог AI-tells: `brand-assets/style-guides/ai-tells-sweep.md`** (добавлен 2026-08-23).
> Список ниже — быстрый путь, hard fails, которые агент держит в голове на этапе письма. Каталог —
> все 27 категорий, канальные профили (article / post / dm / page), positive checks и обязательная
> самопроверка «что здесь всё ещё читается как машинный текст?». Плюс детектор
> `brand-assets/style-guides/scripts/detect-ai-tells.py` — щёлкает механические попадания и даёт
> численную оценку. Полный проход делают редакторы (`seo-editor` Pass 3c, `social-editor` Pass 2b,
> `message-sequencer`, `page-builder` Layer 0), не писатели: писать и вычищать одновременно — значит
> делать плохо и то, и другое.

**Запрещённые AI-сигнатуры (важно для SEO + outbound + posts):**
- Em-dash (—) в риторических конструкциях типа «X — это не просто Y»
- «It's not just X, it's Y»
- Тройные параллелизмы (`fast, reliable, scalable`)
- Слова: leverage, utilize, harness, robust, seamless, comprehensive, delve, navigate (в перен. смысле), tapestry, realm
- «Furthermore / Moreover / Additionally» в начале предложений (минимизировать)

> **Операционный источник для агента — сгенерированная карточка, не эта таблица.**
> `brand-assets/style-guides/hard-bans-card.md` (~5,8 КБ, 14 категорий; с 2026-09-18 — `compliance_status` из trust-FAQ) рендерится скриптом
> `scripts/bans-card.py` прямо из паттернов `detect-ai-tells.py`, поэтому разойтись с тем,
> что реально гейтится, она не может. Таблица ниже — читаемое резюме для человека, и она
> может отстать: аудит 2026-09-02 нашёл эти правила в четырёх местах при одном исполнителе,
> и когда Вадим 2026-09-02 откатил правило про medical device, править пришлось пятнадцать
> файлов. Гейт — `python3 scripts/article_lint.py <файл>`; `scripts/bans-card.py --check`
> падает с exit 1, если карточка отстала от детектора.

**Language guardrails — hard bans (`terminology-guardrails.md`, Doc Ассель, синк 2026-09-14):**

| Запрещено | Чем заменить |
|---|---|
| em dash (— –) — **всегда, без исключений** | запятая, точка, скобки |
| `objective` про нашу технологию и выводы | standardized · timestamped · structured · repeatable |
| `the reader` / `the audience` / `the following sections` / `see below` | описывай бизнес-реальность, а не процесс чтения |
| `this article` / `this guide` / `our content` | убрать (допустимо только в scope note) |
| `by hand` | `manually` |
| `let` | `allow` |
| `plus` как коннектор возможностей / выгод / proof points | `including` · `such as` · `along with` · `as well as` · отдельное предложение |
| `so` вводящее результат или выгоду | `reducing…` · `helping to reduce…` · `allowing…` · `which can reduce…` · `thereby reducing…` |
| **`positioned as`** про продукт, intended use, scope, замену или регуляторный статус | формулируй границу напрямую, medical device тоже: **«FitXpress is not a medical device.»** (решение Вадима 2026-09-11, исключений больше нет) |
| presumed reaction: «what trips people up», «the mistake buyers make», «what most teams misunderstand» | назови компоненты проблемы прямо |
| поведение/чувства, приписанные понятиям: «two properties do the heavy lifting» | «two properties matter» |
| **IEEE:** `IEEE-certified` / `-recognized` / `-validated` / `-backed`, `certified / recognized by IEEE`, `IEEE Grand Challenge`, `member of IEEE standards`, логотип IEEE отдельно в полосе наград/сертификаций (синк 2026-09-14) | только две утверждённые фразы, дословно (они же строки `proof-points.md`): «Winner, 2019 Retail Digital Transformation Grand Challenge, run by the 3D Retail Coalition with Kalypso and IEEE.» · «Participant in the IEEE 3D Body Processing working group, which is developing standards for mobile body scanning.» |
| `80+ body metrics`; BMI / BMR / body composition как «body measurements» (синк 2026-09-14) | `80+ body measurements`; body measurements = обхваты, длины, ширины; BMI и BMR = calculated metrics; body composition = estimates; body metrics = зонтичный термин |
| corrective negation «X, not Y» и corrective «rather than» | сначала рекомендуемый подход, ограничение — отдельной фразой. **Исключение (Doc §1.8):** продуктовая, клиническая, юридическая или регуляторная граница, один раз — например «HIPAA is a regulatory framework, not a certification» (trust-FAQ, 2026-09-18) |

Судейские (не механические): `we / our` — только когда речь о claim of ownership; `you` — на лендингах и в практических блоках, не в нейтрально-образовательных; **`buyer`** — только про закупку, критерии выбора, оценку вендора, **`customer`** — только про действующий договор, ответственность за деплой или юридическую роль (GDPR controller), иначе называй актора: program, provider, clinic, employer, operator, procurement team, decision-maker, person being screened; **`organization`** (§2.14, synced 2026-09-28) — only as an umbrella when the entity type is unknown, mixed or broader than a commercial company, or for institution-level governance, policy or legal responsibility; never as a detached swap for "company" or "customer" in product, sales or implementation copy, and never when the actor is known (use company, customer, provider, clinic, pharmacy, employer, program, operator, care team, research sponsor, public institution); **ярлыки контент-плана** (bridge, hub, pillar, cluster, supporting content) не идут в заголовки, анкоры и текст — называй тему, вопрос или решение (исключение: устоявшийся отраслевой термин или видимая фича сайта, например Content Hub; детектор отдаёт их soft-категорией `cluster_labels`).

**Две правки переопределили `editorial-guardrails.md` (2026-08-25):**
1. **Аббревиатуры.** BMI, CEO, UK, US, EU теперь общеизвестные и **не разворачиваются** (`Body Mass Index (BMI)` → `BMI`). M1 в остальном в силе, включая цитируемых регуляторов (FDA, ICH, GCP).
2. **Medical framing — правило в четвёртом состоянии.** Было «not positioned as a medical device» (2026-06-09) → стало «FitXpress is not a medical device» (2026-08-13) → восстановлено «It is not positioned as a medical device.» (2026-09-02, Review 1) → **«FitXpress is not a medical device.» (2026-09-11, решение Вадима по финалу редактора)**. «Positioned as» — hard ban для любого утверждения о продукте (scope, замена, эквивалентность, intended use), medical device включительно. Intended use: «FitXpress does not diagnose conditions, make clinical decisions, or determine treatment eligibility». Опубликованное до 2026-08-25 не переписываем.

**Синк 2026-09-14 (Doc изменён после 2026-08-13): четыре новых правила, два переопределения.**
3. **`about-me.md` «Buyer framing».** Строка предписывала «buyers» как рамку по умолчанию. Doc §2.12: `buyer` только в контексте закупки и оценки вендора, `customer` только для договорной, деплойной или юридической роли, иначе конкретный актор. Строка исправлена с датой.
4. **IEEE в фактуре.** `proof-points.md` и `overview.md` писали «Winner, Retail Digital Transformation Grand Challenge» и «Member of Mobile Body Scanning Standards», ровно формулировки, которые Doc §2.11 запрещает (у IEEE претензия к некорректным claims 3DLOOK). Заменены двумя утверждёнными фразами. Опубликованный пост `3dlook-is-a-member-of-the-mobile-body-scanning-standards-developed-by-ieee/` не переписываем, он помечен в `published-articles-inventory.md`, решение по живой странице за Вадимом.
Новые правила без переопределений: ярлыки контент-плана (§1.10) и body metrics / body measurements (§2.13). Medical framing Doc теперь формулирует сам парой «Avoid: FitXpress is not positioned as a medical device. / Prefer: FitXpress is not a medical device.», то есть решение 2026-09-11 совпадает с источником.

**Sync 2026-09-28 (Doc changed after 2026-09-14): one new rule, one amendment.**
5. **§2.14 "Organization".** Use it only as an umbrella when the entity type is unknown, mixed or broader than a commercial company, or for institution-level governance, policy or legal responsibility. When the actor is known, name it; **company** is the right word for a commercial business or prospect. This amends the 2026-09-14 reading of §2.12, whose fallback list led with "organization": it is no longer the default replacement for "customer". Judgment only, no detector pattern. Nothing published is retro-edited.

