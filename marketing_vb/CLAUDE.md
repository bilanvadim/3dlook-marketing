# 3DLOOK — Marketing Automation Project Context

> Этот файл — главный источник правды для всех субагентов. Перед работой агент обязан его прочитать. Если нужной фактуры нет — спросить через Telegram, не выдумывать.

---

## 1. Компания

**Название:** 3DLOOK Inc
**Сайт:** https://3dlook.ai/
**Founded:** 2016
**Размер:** 28 сотрудников, $16.2M raised, 100+ клиентов
**Лидеры:**
- Katerina Galich — CEO (katerina@3dlook.me)
- Whitney Cathcart — Co-founder & CCO (whitney@3dlook.me)

**Что делаем (одно предложение):** Mobile body scanning от двух фото со смартфона — 80+ измерений, 3D модель, и body composition за 45 секунд через API/SDK.

**Технология:** Patented statistical generative human body model, обученная на 9+ годах данных (150K+ photos, 30K+ 3D scans, 430K+ measurements).

**Точность:** 96-97% accuracy vs manual measurements, error margin 1.5-2.0 cm, 95%+ repeatability. Weight estimation ±3.5%.

**Текущая ARR:** $1.084M (2025), 67 клиентов, 112K сканов/год.

---

## 2. Два продукта (КРИТИЧНО — у них разные ICP и outbound)

### Product 1: FitXpress (Health & Fitness)
- **Целевые рынки:** telehealth, weight loss / GLP-1, online pharmacy, insurance underwriting, wellness rewards, occupational health, clinical trials, bariatric clinics, digital fitness
- **Что делает:** verified BMI / body composition / measurements для compliance, retention, eligibility screening
- **Ценность:** anti-fraud (AI Smart Scales detects mismatch), engagement (3D goal visualization, side-by-side progress), workflow efficiency
- **Live customers:** UK Meds (online pharmacy BMI verification), Yazen (weight loss, 34K сканов/год), Healthyr (patient profile)
- **Pricing tiers:** $1K / 500 req, $1.5K / 1K req, $3.1K / 2.5K req, $5K / 5K req, $7.5K / 10K req, $10K / 20K req. Free trial: 200 requests / 1 month.

### Product 2: Mobile Tailor (Apparel & Uniforms)
- **Целевые рынки:** made-to-measure apparel, on-demand manufacturing, uniform companies (PPE, medical, public safety), bridal/formalwear, custom alterations
- **Что делает:** 80+ body measurements для precise custom fit, reduce returns/remakes
- **Ценность:** measurement consistency, remote measuring at scale, integration в OMS/3D config
- **Live customers:** Safariland (custom-fit PPE, 15.5K сканов/год), Burlington Medical (radiation aprons, 11.5K), Jim's Formal Wear, Generation Tux, Tailoor, Redthread
- **Lifetime metrics:** 4 legacy MT клиентов с 5+ лет retention

**Когда какой продукт:** в каждой outbound-кампании / SEO-статье / посте — указывай явно `product: fitxpress | mobile_tailor` в frontmatter артефакта. Агенты используют разный ICP и фактуру в зависимости от продукта.

---

## 3. Стратегический контекст (читать перед позиционированием)

**AI Risk:** Body scanning коммодитизируется в 12-36 месяцев — vision foundation models станут common, Apple/Google могут выпустить native primitives. Поэтому **позиционирование смещается с «лучшая модель» на outcomes + workflow + governance + auditability**.

**Что это значит для контента:**
- Не продаём «accurate measurements» — продаём бизнес-результаты (retention, conversion, faster underwriting, fewer remakes)
- Подчёркиваем workflow integration, audit logs, longitudinal tracking, HIPAA/GDPR
- В outbound: hero message — про outcome, не про точность
- В SEO: статьи про use case, не про technology

**No-go positioning:**
- НЕ конкурируем по «accuracy» с future Apple/Google primitives
- НЕ позиционируем как commodity API — мы trusted workflow layer

---

## 4. ICP — детально по каждому продукту

См. полные документы в `brand-assets/product-info/icp-detail.md` (обновлено 2026-07-05, 10 сегментов FX + 4 сегмента MT, revenue-пороги и named company examples по каждому). Краткое резюме:

### FitXpress ICP
- **Telehealth & weight loss / GLP-1:** virtual clinics, coaching apps, longitudinal/RPM programs. $2M+ revenue. Buyer: Founder/CEO / Chief Medical Officer / Head of Clinical Operations / Head of Member Engagement
- **Online pharmacies / digital prescribers:** BMI verification, UK — приоритетный рынок. $2M+ revenue. Buyer: Head of Compliance & Risk / Chief Medical Officer / Clinical Operations Director
- **Life & disability insurers:** underwriting verification. $5M+ revenue, enterprise. Buyer: Chief Underwriting Officer / Chief Risk Officer
- **Health plans / employer wellness:** rewards & verification programs. $5M+ revenue, enterprise. Buyer: CHRO / Head of Wellness / VP Population Health
- **Bariatric / metabolic clinics:** pre-qualification. Buyer: Director of Operations / Medical Director
- **Occupational health providers:** screening. Buyer: VP Operations / Chief Medical Officer
- **CROs / pharma sponsors:** clinical trials. Buyer: Director of Clinical Operations / Head of DCT
- **Connected & digital fitness:** $1M+ revenue. Buyer: Founder/CEO / CPO / Head of Growth
- **Plastic surgery clinics (новый, 2026-07):** Turkey — приоритетное гео (медтуризм), $1M+ revenue. Buyer: Clinic Owner/Director / Plastic Surgeon
- **BCRL detection & monitoring (новый, 2026-07):** oncology/survivorship RPM. $2M+ revenue. Buyer: Chief Medical Officer / Oncology Program Director / RPM Director

### Mobile Tailor ICP
- **MTM brands & tailors:** menswear, womenswear, bridal, formalwear. $1M+ revenue. Buyer: Founder / Head of E-commerce / VP Operations
- **On-demand manufacturers:** integrating scans в pattern-making. $2M+ revenue. Buyer: VP Manufacturing / Head of Product Development
- **Uniform companies:** workwear, healthcare, public safety. $2M+ revenue. Buyer: VP Operations / Director of Procurement
- **Wrist / limb measurement (nishe):** wearables, jewelry, medical devices. Buyer: VP Product / Head of Customization

**Гео-расширение (2026-07):** новый ICP-документ добавляет Canada, Germany, UAE, Australia, Nordics, Turkey как целевые гео по разным сегментам — до первой кампании в новом гео проверить compliance-статус с Вадимом (см. секцию 12).

---

## 5. Профили в социальных сетях

**Детальная per-profile config: `brand-assets/social-profiles-config.md`** — posts_per_week, product_bias, tone, content_types, length, hashtags.

**`post-drafter` читает не весь этот файл, а свой профиль.**
`scripts/split-linkedin-prompts.py` разрезает мастер на
`brand-assets/linkedin-prompts/{profile}.md` (общие правила + секция профиля, ~4 КБ вместо
11,8 КБ). Эти шесть файлов **генерируются** — правится мастер, потом скрипт;
`--check` падает с exit 1 при расхождении. Мастер остаётся источником правды.

**Для 6 LinkedIn-профилей источник правды по промпту — `brand-assets/linkedin-post-prompts.md`** (офлайн-копия [Google Doc Вадима](https://docs.google.com/document/d/19KKWLtJv4Jx_hKbgxy0TCWnLXgnHe0-gxGuDj9vA2WQ/edit), синк 2026-08-07): аудитория, рынок, фокус-лист, тон, структура, word count и закрытие для каждого профиля. `post-drafter` обязан прочитать нужную секцию перед написанием любого `linkedin-*` поста. При конфликте с `social-profiles-config.md` выигрывает этот файл — кроме двух house rules, которые выигрывают всегда: **хештегов нет ни на одном профиле** и **1-2 эмодзи максимум**. Twitter / Instagram / Facebook документ не затрагивает.

**Активные профили (9 штук):**

| profile_id | Платформа | Owner | Рынок | Product bias |
|------------|-----------|-------|-------|--------------|
| `twitter-company` | Twitter / X | Vadim manages | — | 100% FX |
| `instagram-company` | Instagram | Vadim manages | — | 100% FX |
| `facebook-company` | Facebook | Vadim manages | — | 100% FX |
| `linkedin-company` | LinkedIn Company | Vadim manages | глобально | 100% FX |
| `linkedin-katerina` | LinkedIn Personal | Katerina Galich (CEO) | UK | 100% FX |
| `linkedin-vadim` | LinkedIn Personal | Vadim Bilan (Marketing) | **Australia** | 100% FX |
| `linkedin-nick` | LinkedIn Personal | Nick Omelchak (BD, USA) | USA | 100% FX |
| `linkedin-olena` | LinkedIn Personal | Olena Kudryavtseva (BD, Europe) | Continental Europe (без UK) | 100% FX |
| `linkedin-katya` | LinkedIn Personal | Kateryna Boichuk (BD, Israel) | Israel + Gulf | 100% FX |

Рынки social-профилей теперь совпадают с outbound-рынками из таблицы ниже.

**Вимкнені:** `linkedin-whitney` (Whitney Cathcart, CCO) — posts_per_week: 0.

**Активувати/вимкнути профіль:** зміни `posts_per_week` в `brand-assets/social-profiles-config.md`.
**Для outbound:** 5 профілів для рассылок, кожен прив'язаний до свого ринку (гео) + свій exclusion registry (`workspace/outbound/exclusions/`):

| profile | Owner | Ринок |
|---------|-------|-------|
| `katerina` | Katerina Galich (CEO) | UK |
| `nick` | Nick Omelchak (BD) | USA |
| `olena` | Olena Kudryavtseva (BD) | Europe / EU |
| `katya` | Kateryna Boichuk (BD) | Israel |
| `vadim` | Vadim Bilan (Marketing) | Australia |

Гіпотеза й список компаній кампанії мають відповідати ринку профілю (гео-дисципліна). Деталі — `runners/outbound-runner.md`.

---

## 6. Tone of Voice

> **Канонические источники голоса и аудитории (читать перед любой задачей на письмо):**
> - `about-me.md` (корень репо) — brand voice FitXpress: voice fingerprint, register, claims discipline (hard rules), accuracy/repeatability framing, слова которые USE / NEVER use, структура статьи, CTA discipline. Это источник правды по тому, *как* писать health-контент.
> - `audience.md` (корень репо) — *для кого* пишем: shared spine + 7 health-сегментов (who · core pain · hook · «what NOT to say»).
> - **`brand-assets/content-strategy/terminology-guardrails.md`** — *какими словами* писать: General Approach & Language Guardrails, офлайн-копия [Doc Ассель](https://docs.google.com/document/d/1dPNXQL62t_y82MFJblBidEvRgwXjJxzADdapB7Pa214/edit) (doc изменён 2026-08-13, синк 2026-08-25). Part 1 — девять правил построения фразы, Part 2 — десять словарных запретов, Part 3 — grep-таблица. Действует на ВЕСЬ корпоративный контент: статьи, страницы сайта, посты, outbound, whitepaper, деки. Канальных исключений нет.
>
> Секция 6 ниже — краткое операционное резюме. При конфликте `about-me.md` имеет приоритет по голосу и claims discipline; `terminology-guardrails.md` — по **выбору слов и построению фразы** (он новее и принадлежит редакционному владельцу: две правки уже переопределили `editorial-guardrails.md` — см. блок ниже). Фактура (числа, кейсы) — всегда из `brand-assets/product-info/`, а не из этих файлов.

**Что мы:**
- Экспертные, опираемся на данные (96-97% accuracy, ±3.5%, 45 sec, 80+ measurements)
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
> `brand-assets/style-guides/hard-bans-card.md` (~4,4 КБ) рендерится скриптом
> `scripts/bans-card.py` прямо из паттернов `detect-ai-tells.py`, поэтому разойтись с тем,
> что реально гейтится, она не может. Таблица ниже — читаемое резюме для человека, и она
> может отстать: аудит 2026-09-02 нашёл эти правила в четырёх местах при одном исполнителе,
> и когда Вадим 2026-09-02 откатил правило про medical device, править пришлось пятнадцать
> файлов. Гейт — `python3 scripts/article_lint.py <файл>`; `scripts/bans-card.py --check`
> падает с exit 1, если карточка отстала от детектора.

**Language guardrails — hard bans (`terminology-guardrails.md`, Doc Ассель 2026-08-13):**

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
| **`positioned as`** про продукт, intended use, scope, замену или регуляторный статус | формулируй границу напрямую. **Единственное исключение (восстановлено 2026-09-02): medical device — «It is not positioned as a medical device.»** |
| presumed reaction: «what trips people up», «the mistake buyers make», «what most teams misunderstand» | назови компоненты проблемы прямо |
| поведение/чувства, приписанные понятиям: «two properties do the heavy lifting» | «two properties matter» |
| corrective negation «X, not Y» и corrective «rather than» | сначала рекомендуемый подход, ограничение — отдельной фразой |

Судейские (не механические): `we / our` — только когда речь о claim of ownership; `you` — на лендингах и в практических блоках, не в нейтрально-образовательных.

**Две правки переопределили `editorial-guardrails.md` (2026-08-25):**
1. **Аббревиатуры.** BMI, CEO, UK, US, EU теперь общеизвестные и **не разворачиваются** (`Body Mass Index (BMI)` → `BMI`). M1 в остальном в силе, включая цитируемых регуляторов (FDA, ICH, GCP).
2. **Medical framing — правило в третьем состоянии.** Было «not positioned as a medical device» (2026-06-09) → стало «FitXpress is not a medical device» (2026-08-13) → **восстановлено обратно на «It is not positioned as a medical device.» (2026-09-02, Review 1, решение Вадима)**. «Positioned as» про всё ОСТАЛЬНОЕ (scope, замена, эквивалентность, intended use) по-прежнему hard ban. Intended use: «FitXpress does not diagnose conditions, make clinical decisions, or determine treatment eligibility». Опубликованное до 2026-08-25 не переписываем.

---

## 7. Бренд-ассеты

**Дизайн — единый источник правды: `DESIGN.md` (корень репо).** Подтверждённый экспорт из официальной Figma: цвета (electric blue `#143DFF`, navy `#050F40`, полные blue/gray/neutral шкалы), типографика (**Satoshi**), spacing, border-radius, кнопки, header/footer, motion, art direction, copy-paste `:root` CSS. Читать перед любым визуальным артефактом (бриф, лендинг, HTML-прототип, 2-pager, deck, email).

См. также `brand-assets/`. Перед визуальным брифом или постом агент **обязательно** читает:
- `DESIGN.md` — **все токены дизайна** (заменяет старые `colors.md` / `fonts.md`)
- `brand-assets/brand-guidelines/` — гайдлайны (если есть PDF)
- `brand-assets/past-posts/` — последние посты под каждый профиль

> ⚠️ `brand-assets/color-palette/colors.md` (`#2962FF`) и `brand-assets/fonts/fonts.md` (Inter) — **устарели** (это были placeholder-ы до получения Figma). Каноничны `#143DFF` и **Satoshi** из `DESIGN.md`. Оба старых файла переведены в redirect-заглушки. Не воскрешать `#2962FF` / Inter (см. `DESIGN.md` §15 superseded).

**Visual references (Figma):**
- Blog banners: https://www.figma.com/design/zWV1W9fs7cbp7Jc0pVDTDX/Blog-banners
- Website pages: https://www.figma.com/design/yQlvzqLeCJAAQjaHSKIduC/3DLOOK-website

Если в `brand-assets/past-posts/` пусто — STOP, прошу Вадима залить минимум 10 экспортов из Figma + 10 постов под каждый активный профиль.

---

## 8. Конкуренты

См. `brand-assets/product-info/competitors.md` и `brand-assets/competitors/list.md`. Краткое:

- **Prism Labs** — главный конкурент в FitXpress space. Сильны в insurance / population health / GLP-1.
- **Bodygram** — fitness trainers / dieticians / health professionals. Похожий продукт, слабее в clinical workflows.
- **Size Stream** — clinical research / hardware-based + smartphone. Сильны в hybrid (on-prem + at-home).
- **Apple/Google native primitives (future)** — главный долгосрочный риск.

---

## 9. Воркфлоу и роли

| Роль | Кто | Что делает |
|------|-----|------------|
| Копирайтер | `post-drafter` | 1 пост per профиль на основе SEO-статьи |
| Механический гейт | `scripts/post-lint.py` | Длина, хештеги, эмодзи, em dash, запрещённые слова, плейсхолдеры, published slug, числа против статьи и `proof-points.md`. Ноль токенов |
| Brand voice (пост) | `post-brand-checker` | 10/13-пунктный чек одного поста |
| QC (пост) | `post-quality-controller` | 20-балльная рубрика, выборка 3 из 9, sonnet, §14 |
| Сборка пака | `scripts/social_pack.py` | source · brief · prompt · qc-prompt · qc-plan · manifest · digest · report · scores |
| Бриф-мейкер | `visual-brief` | Бриф для дизайнера в Canva |
| Дизайнер | Человек | Делает визуал |
| Апрувер | Вадим (через Telegram) | Все чекпоинты |
| Outbound | пайплайн `outbound/*` | Hypothesis → ... → Campaign analysis |
| SEO | пайплайн `seo/*` | Keywords → ... → Publish → trigger social |
| Brand guardian | `brand-checker` (shared) | Проверка тона / no-go / AI-сигнатур |

**Social workflow:** SEO-статья готова → `mvb-run.py posts {slug}` (fan-out: одна
conductor-job на профиль, с шагом 4 мин) → в каждой job `/post-one-profile {slug} {profile}`
→ `post-drafter` → `scripts/post-lint.py` → `post-brand-checker` → `post-quality-controller`
(если профиль в выборке) → последний профиль собирает manifest / digest / report скриптом →
Telegram апрув Вадима → `visual-brief`. Квартальный план для соцсетей не используется.

`/post-from-article {slug}` делает то же в **одной** сессии и оставлен как fallback для
интерактивного прогона: замер 2026-08-28 показал, что координация в одной толстой сессии —
59% стоимости пака (25,5M токенов из 42,9M). Подробности и цифры — в шапках обоих файлов
команд.

**Механика — скриптами, не агентами.** `scripts/social_pack.py` (source · brief · prompt ·
qc-prompt · qc-plan · manifest · digest · report · scores) и `scripts/post-lint.py`.
Агенты пишут и судят; разрешение источника, сборка промптов, длины, числа, манифест и
дайджест — код. Промпт для `post-drafter` берётся **дословно** из
`social_pack.py prompt`: его первая секция байт-в-байт одинакова для всех девяти профилей,
и на этом держится общий кеш промпта (`subagentPromptCacheTtl: "1h"` в
`.claude/settings.json` — дефолт для сабагентов 5 минут, а профили идут с интервалом 4-6).

**Social workspace:** `workspace/social/articles/{slug}/{profile}/post.md`
`_run-brief.md` в той же папке генерируется (`social_pack.py brief`); руками правится
только секция между `HUMAN:START` / `HUMAN:END` — claims discipline и реальные визуалы
статьи.

### Модель по стадиям social-пайплайна

| Стадия | Модель | Почему |
|---|---|---|
| `post-drafter` | **opus** | Единственная стадия, где пишется текст. Меняется только через A/B ниже |
| `post-brand-checker` | sonnet | Чек-лист по готовому тексту |
| `post-quality-controller` | sonnet | Вход компактный, механика уже проверена линтером |
| lint / manifest / digest / report | код | Токенов не тратит |

**Протокол A/B, прежде чем снимать opus с `post-drafter`.** Соблазн понятен: три
компанийских аккаунта короткие и идут по жёсткому брифу. Но это единственный рычаг из всех
внедрённых, который может испортить текст, поэтому меняется он только по данным:

1. Прогнать один полный пак с `model: sonnet` в `post-drafter` (правится во **всех трёх**
   копиях агента, иначе `check-agent-copies.py` упадёт — и правильно).
2. Прогнать QC по **всем девяти** профилям этого пака, а не по выборке — сравнение
   требует полного набора.
3. `python3 scripts/social_pack.py scores` — сравнить среднее и разброс с базой:
   паки на opus дают 15-19/20, `glp-1-market-hub` в среднем 16,4.
4. Решение принимает Вадим по дайджесту, а не по среднему баллу. Падение среднего меньше
   чем на балл при живом тексте — это выигрыш; потеря позиции в тексте — нет, даже при том
   же балле.
5. `_pack.json` в папке пака пишет, под какой политикой шёл прогон (`drafter_model`,
   `qc_policy`), чтобы сравнение потом можно было воспроизвести.

Промежуточный вариант, если полный переход не пройдёт: opus на первый профиль пака (он
задаёт карту углов) и на шесть LinkedIn, sonnet на twitter / instagram / facebook.

---

## 10. Технические правила для всех агентов

1. **Артефакты — в файлы, не в чат.** Всё в `workspace/{track}/{task_id}/`.
2. **Никаких прямых публикаций.** Бот не имеет ключей LinkedIn / FB / IG / closely.io. Только подготовка артефактов.
3. **Если контекста не хватает — стоп и вопрос.** Не выдумывать числа, кейсы, имена.
4. **Каждый артефакт имеет frontmatter** с полем `product: fitxpress | mobile_tailor` (для outbound и contentful артефактов).
5. **Логирование** — `workspace/{track}/{task_id}/log.md`.
6. **Имена файлов** — kebab-case с датой: `2026-04-28-fitxpress-insurance-week17.md`.

---

## 11. Метрики

- **Соцсети:** охват, ER, клики на сайт, follower growth (per-profile, per-product tag)
- **Outbound:** acceptance rate, reply rate, positive reply rate, qualified leads, передано в sales (per-product)
- **SEO:** позиции по ключам, organic traffic, time-on-page, конверсия в trial signup или contact form

---

## 12. Compliance

- **HIPAA compliant** — для FitXpress в US healthcare контекстах
- **GDPR principles** — для EU
- **AWS S3 SSE-S3 encryption** для всех данных
- **Photos удаляются** immediately или within 30 days (по политике клиента)
- **Не процессим personal identifiers**
- **Privacy contact:** privacy@3dlook.me

В outbound и контенте — compliance points критичны для insurance, telehealth, clinical trials аудитории.

---

## 13. История изменений

**Вынесена в `docs/changelog.md`** (2026-09-01) — 33 записи с 2026-04-28.

Причина: этот файл грузится в контекст каждой сессии целиком, и история занимала 11 800
токенов из 20 700, то есть 56% файла. Правила и фактура нужны агенту в каждом прогоне,
журнал — только когда кто-то выясняет, почему правило такое.

- **Новую строку писать в `docs/changelog.md`**, в конец таблицы, в том же формате
  (дата · что изменено и почему · кто). Здесь дублировать не нужно.
- Если изменение **переопределяет** действующее правило, строки в журнале недостаточно:
  правится и тот раздел этого файла, который правило описывает. Журнал объясняет, как
  правила стали такими, а не какие они сейчас.
- Ссылки вида «CLAUDE.md §13» из других файлов ведут сюда и дальше в журнал.

## 14. Quality Control loop

Система имеет независимый QC механизм (см. `docs/quality-rubric.md` и `workspace/_quality/README.md`):

- **`quality-controller`** оценивает артефакты по 20-балльной шкале
- **Я (координатор)** добавляю короткий coordinator_review в каждый QC отчёт
- **`agent-improver`** анализирует QC + coordinator notes, предлагает правки промптов

### Auto-QC флаг

`AUTO_QC_ENABLED = true` (default)

Когда `true`, runners автоматически запускают quality-controller после следующих артефактов:
- `hypothesis-generator` (outbound шаг 1)
- `icp-validator` (outbound шаг 4)
- `message-sequencer` (outbound шаг 5)
- `post-drafter` (social) — **выборочно, см. ниже**
- `seo-outline-builder` (SEO шаг 3)
- `seo-section-writer` (по каждой секции)
- `seo-meta-generator` (SEO шаг 8)
- Финальный `draft-v3-final.md` после ai-rewrite

QC НЕ запускается после механических шагов: people-extractor, citation-deduper, readability-editor (они не несут creative качества).

### Social: другой агент и выборка 3 из 9 (2026-09-01)

**Агент.** Соцпосты инспектирует `post-quality-controller` (mvb-social, sonnet), а не
`quality-controller` (mvb-core, opus). Вход ему приходит готовым от
`scripts/social_pack.py qc-prompt` — тело поста, полный JSON `scripts/post-lint.py`, бриф
профиля, уже занятые в паке углы. Он читает только `docs/quality-rubric.md` и не ходит по
файлам. Категории **B (факты) и D (формат) уже проверены механически** — он берёт вывод
линтера как факт и оценивает A, C, E, то есть соответствие брифу профиля, тон и наличие
позиции в тексте.

**Выборка.** `scripts/social_pack.py qc-plan <slug>` выбирает три профиля из девяти:
первый профиль пака (он задаёт карту углов, и плохой угол там расходится по остальным),
плюс наименее давно инспектированный компанийский аккаунт и наименее давно
инспектированный личный (по датам отчётов в `workspace/_quality/social`). Сверх выборки QC
запускается **безусловно** на любом профиле, у которого упал линтер.

**Почему.** Замер пака `glp-1-market-hub` (2026-08-28, 9 постов): девять прогонов
`quality-controller` на Opus дали 7,1M токенов контекста, 112 turns и ~$36 — столько же,
сколько всё написание постов, — и выдали девять отчётов по 16-19/20. Три дефекта, которые
он действительно нашёл, теперь ловит линтер бесплатно: «under a minute» против джерельных
«Under 45 seconds» (`number_drift`), `article_slug` с именем рабочей папки вместо
опубликованного слага, и поля design tip. Смысл QC по этой секции — кормить
`agent-improver`, а не пропускать каждый артефакт; **гейт на паке — апрув Вадимом
дайджеста**, и он не изменился. Выборка по «наименее давно проверялся» даёт improver-у
покрытие по всем профилям со временем: хеш-выборка оставляла `linkedin-nick` непроверенным
во всех девяти паках на диске, пока `linkedin-vadim` попадался четыре раза.

### Coordinator review требование

После каждого автоматического QC я в чате добавляю одну строку в поле `coordinator_review` отчёта:

```
agreement: ✅ agree | ⚠️ disagree (1 line why)
top_issue: [1 sentence] | none
```

Это короткое — критичный сигнал для improver-а, который видит мою perspective + QC одновременно.

### Когда запускать improver

Каждые 2 недели или после 20+ артефактов прошедших QC.

---

## 15. Blog Authoring Standards

> Note: numbered as section 15 because existing section 11 is "Метрики". Vadim asked for this to be "section 11" — flagged in the 2026-05-22 report. Renumbering all sections is risky; this section is appended at the end to avoid breaking external references.

**Default blog author:** Assel Sekerova — see `brand-assets/team/assel-sekerova.md`.

**Style guide:** `brand-assets/style-guides/blog-style-guide.md` — built from analysis of 9 production articles in `brand-assets/past-articles/blog/`.

### Hard requirements for new SEO / blog articles

`seo-planner` and `seo-writer` MUST, before planning or writing:

0. **Read `about-me.md` and `audience.md` (repo root) first.** `about-me.md` governs voice and claims discipline (the reframe move, "accurate enough for which decision?", the two-benchmarks rule, repeatability written as `< 1 cm`, the standard 12-part article structure, CTA-by-funnel-stage). `audience.md` fixes the target segment and its hook + "what NOT to say" before a single line is written. These override generic product tone. On any conflict with the summary in section 6, these files win on voice/audience; facts still come from `brand-assets/product-info/`.
1. **Read `brand-assets/style-guides/blog-style-guide.md` in full** — the voice, structural templates (Article Types A–F), banned patterns, and per-vertical vocabulary are not optional.
2. **Read 2–3 relevant past-articles from `brand-assets/past-articles/blog/`** that match the target vertical:
   - FitXpress topics → read at least one of: `mobile-body-scanning-insurance-underwriting.md`, `wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning.md`, `3dlook-turns-two-photos-structured-body-data.md`
   - Clinical trials / CRO-pharma / heavily-regulated FitXpress verticals → read `clinical-trials-anthropometric-measurement.md` (the finalized clinical-trials use-case article — best model for compliance-scoping, "operational not clinical" framing, and the scope-note/FAQ structure; see its `known_issues` frontmatter for the M1/M2 slips NOT to replicate)
   - Mobile Tailor topics → read at least one of: `on-demand-clothing-manufacturing.md`, `sustainable-fashion-manufacturing.md`, `the-future-of-fashion-retail.md`
   - Comparison / buyer's-guide topics → `body-scanning-technology-comparison.md`
3. **Apply Assel Sekerova as author** by default in the article frontmatter, unless Vadim specifies otherwise in the brief.
4. **Match the 2026 tone** (measured, hedged, stats-first, workflow-framed) — not the 2024 industry-trend tone present in older MT articles. The 2024 articles use phrases now banned by CLAUDE.md section 6 (leverage / revolutionize / harness / etc.); do NOT mimic their phrasing even though they are in the corpus.
5. **Read `brand-assets/style-guides/editorial-guardrails.md` and apply the 11 principles end-to-end.** These guardrails apply to **ALL 3DLOOK content** — blog, SEO, outbound, social, whitepaper, deck — not just SEO articles. Established 2026-06-09 from the v2-asselya FAQ-article review cycle (Whitney + Asselya editorial pass). Phase 1 fact-check runs the 11 as an explicit checklist; Phase 3 writing enforces them throughout; Phase 4 self-critique surfaces any bent guardrail to an Open Items block for Asselya per principle #11 — no silent edits. Hardest-binding principles: #1 (substantiation — cut what you can't back), #2 (one number, everywhere the same), #3 (reserved words "independent" / "validated" / "third-party" off-limits without proof), #4 (no bare ">X%" without methodology — use "available under NDA" instead), #6 (medical framing: **«It is not positioned as a medical device.»** — restored 2026-09-02 by Review 1 and Vadim's call, after the 2026-08-13 terminology guardrails had banned it. «Positioned as» remains banned for every other product, scope, intended-use and regulatory statement, and «does not apply» about a regulatory framework is still never allowed).
6. **Resolve the topic against `brand-assets/content-strategy/content-plan.md` BEFORE anything else (FitXpress health only).** `seo-planner` runs this as a Phase 0 gate: locate the topic's row (hub · cluster · intent · action type · priority · existing-URL · cannibalization guardrail), and **act on the action type** — only `create net-new` / `publish planned hub` proceed to a new article; `refresh/expand`, `section first`, `review/decide`, and `lead magnet` return a recommendation and STOP (no new article). A topic with no row → stop and ask Vadim where it belongs. The rules that govern placement, positioning language, vertical boundaries, internal linking (4 directions), FAQ, and CTA-by-intent live in `brand-assets/content-strategy/content-strategy-guidelines.md`. `content-plan.md` is the offline copy of the [strategy spreadsheet](https://docs.google.com/spreadsheets/d/1Sy7EzzZZvCKyrD30pbhElEpCZDbzuMtMkxdiDTIP8AE/edit); re-sync it when the sheet changes. This is a hub-and-cluster system: **a title without its strategy row is not a brief.**

7. **Read `brand-assets/content-strategy/terminology-guardrails.md` and run it as its own pass.** Офлайн-копия [Doc Ассель](https://docs.google.com/document/d/1dPNXQL62t_y82MFJblBidEvRgwXjJxzADdapB7Pa214/edit) (doc изменён 2026-08-13, синк 2026-08-25) — источник правды по **выбору слов и построению фразы** для всего корпоративного контента, не только SEO. Part 1 — девять правил построения фразы (аббревиатуры и их исключения, анкорные ссылки, качество сторонних источников, явные отношения, никаких presumed reactions, никакого поведения приписанного понятиям, em dash, corrective negation, corrective «rather than»). Part 2 — десять словарных запретов (`objective`, `we/our`, `you`, `reader/audience/below`, `this article`, `by hand`, `plus`, `let`, `so`, **`positioned as`**). Сводка hard bans — §6 выше. **Писатель держит в голове только hard bans; полный проход делает редактор** (`seo-editor` Pass 4 + Pass 3c детектор, `social-editor` Pass 2b, `page-builder` Layer 2), потому что писать и вычищать одновременно — значит делать плохо и то, и другое. Механические попадания щёлкает `brand-assets/style-guides/scripts/detect-ai-tells.py`; судейские строки (corrective negation, corrective «rather than», `we/our`, `you`, vendor-блог в цитате) остаются за человеком или редактором. **Этот файл переопределил два правила `editorial-guardrails.md`** — M1 (BMI/CEO/UK/US/EU не разворачиваются) и #6 (medical framing напрямую, без «positioned as»); переопределения записаны в обоих файлах с датами.

### Founder-voice exception

Articles signed by **Katerina Galich (CEO)** are reserved for:
- Thought-leadership and opinion pieces
- Personal experiments (e.g., the AI photo-manipulation experiment narrative)
- Strategic commentary on AI risk and industry direction
- Conference reflections and post-event reactions

Default to Assel for everything else. If a brief is ambiguous, ask Vadim before deciding the byline.

### Style guide drift policy

If a new production article significantly departs from the style guide (e.g., a deliberate experiment), update `brand-assets/style-guides/blog-style-guide.md` to record the new pattern with the source article cited. The style guide is a living document driven by what actually ships, not a frozen rulebook.

---

## 16. Website page pipeline (`page-builder` / `/page`)

> Added 2026-08-23. Owns **marketing pages on 3dlook.ai**, not articles.

**Skill:** `.claude/skills/page-builder/SKILL.md` — one canonical copy, no plugin mirror. Adapted from
Victor Shulga's public `page-builder` skill.

**Command:** `/page [vertical|URL] [gate|build|judge|handoff|full]`. Artifacts in
`workspace/pages/{slug}/`.

**Scope split — read this before routing a request:**

| Request | Owner |
|---|---|
| Use-case / vertical page, campaign landing, product page, case-study page | `/page` |
| Blog article, hub, comparison, buyer guide | `/new-article` (mvb-seo) |
| Social posts from a published article | `/post-from-article` |
| 20-point QC of a pipeline artifact | `/qc` |

**Four gates.** G-I decides whether a vertical page should exist at all (use-case file + **2 or more
publishable cases from that vertical** + demand + 5 facts absent from the parent + the 60% uniqueness
rule). G-A blocks writing until placement, URL, cannibalisation and the Search Console baseline are
settled. G-T blocks publishing on technical grounds. G-J is a **blind judge in a fresh subagent**,
100-point page scorecard, threshold 85, maximum 3 rounds, and publishing below 85 without flagging it
is forbidden. `quality-controller` does not substitute for G-J — it is neither blind nor page-shaped.

**The benchmark:** `/structured-body-data-for-telehealth-digital-health-programs/` (July 2026) is the
one vertical page already built to the current standard — scoped accuracy, a real comparison block, a
13-question FAQ with FAQPage schema, Service schema with `audienceType` + `areaServed`, ~1,600 words,
no banned words in the headings. The Kit tells writers to match it. `/for-bmi-verification/` (~659
words, no FAQ, no cases) is the first rewrite candidate.

**Two hierarchies, different depths** (corrected 2026-08-23 by Vadim, and the site agrees —
`/fitxpress/` 301s to `/`): the **homepage is the FitXpress parent**, so FX verticals are its children
at `/for-{vertical}/`, while Mobile Tailor has its own parent at `/mobile-tailor/` with
`/mobile-tailor/for-{vertical}/` underneath. Never invent a `/fitxpress/` path level. Two open debts:
`/fitxpress/for-connected-and-digital-fitness/` uses that non-existent level and declares a breadcrumb
pointing at a redirect, and **neither parent links down to its verticals in the body** — both do it
only through the header nav dropdown.

**The G-I reality check:**

1. **Only Mobile Tailor verticals clear G-I today.** Uniforms has Safariland + Burlington Medical;
   made-to-measure has Generation Tux + Jim's Formal Wear if formal-wear rental counts as the same
   vertical. Every FitXpress vertical has at most one case, so it needs a second case, an approved
   reference, or a recorded G-I waiver.

**Non-negotiables inside the skill:** every number from `proof-points.md`; client names and metrics
only from `case-studies/`; Mobile Tailor customer ARRs never published; the 11 editorial guardrails
along with M1/M2/M3 run as their own pass, not as a habit while drafting; `terminology-guardrails.md`
Part 1 and Part 2 as Layer 2 of the humanisation pass; accuracy always scoped through
"accurate enough for which decision?" and its four conditions; medical framing stated directly
(**"It is not positioned as a medical device."** — restored 2026-09-02; "positioned as" stays banned for every other product, scope and regulatory statement);
`DESIGN.md` decides every token; a price signal and a link to `/pricing/` on every commercial page.
