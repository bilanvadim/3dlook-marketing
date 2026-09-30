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

**Точность:** 96-97% vs expert manual measurement, typical absolute error 1.5-2.0 cm, scan-to-scan repeatability `< 1 cm`. Weight estimation ±3.5%.
> **Формулировки — только дословно из `brand-assets/product-info/accuracy-formulations.md`** (канон живой framework-статьи, перенесён 2026-09-02). Не пересобирай предложение из цифр. Два бенчмарка не совмещаются. `95%+ repeatability`, которое стояло здесь до 2026-09-02, **не публикуется**: живая статья такой цифры не даёт.

**Текущая ARR:** $1.084M (2025), 67 клиентов, 112K сканов/год. *(Внутреннее. Публично — только «100+ clients», везде; решение Вадима 2026-09-30.)*

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

**Per-profile config:** `brand-assets/social-profiles-config.md` (posts_per_week, product_bias, tone, content_types, length). **LinkedIn-промпты:** мастер `brand-assets/linkedin-post-prompts.md` (офлайн-копия Google Doc Вадима) и сгенерированные из него `brand-assets/linkedin-prompts/{profile}.md` (`scripts/split-linkedin-prompts.py`, правится мастер); `post-drafter` читает файл своего профиля. Что побеждает при конфликте и полные правила пяти личных профилей — **`docs/social-profiles.md`** (читать, когда меняешь правила профилей или разбираешь спорный пост).

**House rules, действуют всегда:** хештегов нет ни на одном профиле · 1-2 эмодзи максимум · пять личных LinkedIn-профилей (Katerina · Katya · Nick · Olena · Vadim) — 100-170 слов, 170 жёсткий потолок, ничего длиннее 30 слов в предложении, локация не объявляется, хук — утверждение, не вопрос · `linkedin-company` — 180-280 слов и корпоративный регистр. Рынок профиля — это **для кого** пост, а не про что. Механику гейтит `scripts/post-lint.py`, судейскую часть — `post-brand-checker`.

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

> **Канонические источники (читать перед любой задачей на письмо):** `about-me.md` (корень репо) — голос и claims discipline FitXpress; `audience.md` — для кого пишем: 7 health-сегментов, hook и «what NOT to say»; **`brand-assets/content-strategy/terminology-guardrails.md`** — выбор слов и построение фразы, офлайн-копия Doc Ассель (synced 2026-09-28), действует на ВЕСЬ корпоративный контент, канальных исключений нет. При конфликте: `about-me.md` выигрывает по голосу и claims discipline, `terminology-guardrails.md` — по словам и построению фразы, фактура (числа, кейсы) всегда из `brand-assets/product-info/`. **История синков и переопределений правил — `docs/language-guardrails.md`.**

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

> **Полный каталог AI-tells:** `brand-assets/style-guides/ai-tells-sweep.md` (27 категорий, канальные профили article / post / dm / page) и детектор `brand-assets/style-guides/scripts/detect-ai-tells.py`. Полный проход делают редакторы и гейты, не писатели: писать и вычищать одновременно значит делать плохо и то, и другое. Список ниже — hard fails, которые держишь в голове при письме.

**Запрещённые AI-сигнатуры (важно для SEO + outbound + posts):**
- Em-dash (—) в риторических конструкциях типа «X — это не просто Y»
- «It's not just X, it's Y»
- Тройные параллелизмы (`fast, reliable, scalable`)
- Слова: leverage, utilize, harness, robust, seamless, comprehensive, delve, navigate (в перен. смысле), tapestry, realm
- «Furthermore / Moreover / Additionally» в начале предложений (минимизировать)

> **Операционный источник для агента — сгенерированная карточка** `brand-assets/style-guides/hard-bans-card.md` (`scripts/bans-card.py` рендерит её из паттернов детектора, `--check` падает с exit 1 при расхождении). Таблица ниже — резюме для человека и может отстать. Гейты: `scripts/article_lint.py`, `scripts/post-lint.py`, `scripts/outbound_pack.py check-messages`.

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

**Medical framing — короткая форма: «FitXpress is not a medical device.»** (решение Вадима 2026-09-11, четвёртое состояние правила; «positioned as» — hard ban для любого утверждения о продукте). **Аббревиатуры** BMI, CEO, UK, US, EU не разворачиваются. Опубликованное до смены правила не переписываем. Даты, прежние формулировки и что именно переопределил каждый синк — `docs/language-guardrails.md`.

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
| Дизайнер | Человек | Делает визуал сам, по `### Design tip` каждого поста в дайджесте (шаг `visual-brief` удалён 2026-09-20, решение Вадима: «дизайнер сам это делает») |
| Апрувер | Вадим (через Telegram) | Чекпоинты social и outbound. **SEO-статьи с 2026-09-21 идут без остановок** (plan → publish → git commit+push одним прогоном); Вадим ревьюит пост-фактум по финальному дайджесту и коммиту — см. `.claude/commands/new-article.md` «Режим без чекпоинтов» |
| Outbound | пайплайн `outbound/*` | Hypothesis → ... → Campaign analysis |
| SEO | пайплайн `seo/*` | Keywords → ... → Publish → trigger social |
| Brand guardian | `brand-checker` (shared) | Проверка тона / no-go / AI-сигнатур |

**Social, основной режим — БАТЧ** (решение Вадима 2026-09-20): `mvb-run.py posts {slug} --batch` → одна job `/post-batch` → один `post-drafter` (opus) пишет весь пак → `post-lint.py` с гейтом по НАПИСАННЫМ профилям → `post-brand-checker` и `post-quality-controller` по выборке → manifest / digest / report скриптом → апрув Вадима в Telegram → дизайнер по `### Design tip`. Fan-out (`posts {slug}` без флага) — для точечных пересборов: job'ы только на профили без post.md. `/post-from-article` — интерактивный fallback. Квартальный план для соцсетей не используется.

**Механика — скриптами, не агентами:** `scripts/social_pack.py`, `scripts/post-lint.py`, `scripts/article_package.py`, `scripts/outbound_pack.py`. Агенты пишут и судят; разрешение источника, сборка промптов, длины, числа, манифесты и импорты — код. Stop-hook `.claude/hooks/posts-artifact-gate.py` не даёт social-сессии завершиться без обещанных post.md.

**Модели:** координаторы job'ов — sonnet (`model:` во frontmatter команды), пишущие стадии (`post-drafter`, `seo-writer`, `seo-editor`) — opus и меняются только по A/B (`docs/model-ab-protocol.md`), чекеры — sonnet, механика — код.

**Social workspace:** `workspace/social/articles/{slug}/{profile}/post.md`. Замеры, обоснования и таблица моделей по стадиям — **`docs/social-workflow.md`**.

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

**Источник правды — живая [FAQ-статья](https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/)
(опубл. 2026-09-16), решение Вадима 2026-09-18: «самая точная информация, обнови везде».** Операционная
выжимка с формулировками «говори / никогда не говори» — `brand-assets/product-info/compliance.md`;
дословная копия страницы — `workspace/seo/articles/2026-07-14-fitxpress-privacy-security-faq/published-live-2026-09-18.md`.
В контенте ставь короткую контекстную заметку и **ссылку на FAQ**, ответы FAQ не пересказывай.

- **HIPAA — это рамка, не сертификат.** Пиши: «FitXpress can support HIPAA-governed deployments where
  3DLOOK acts as a business associate under an executed BAA». BAA — для qualifying enterprise
  deployments. **«HIPAA compliant» / «HIPAA-compliant» / «HIPAA certified» — запрещено.**
- **GDPR — каноническая фраза, дословно:** «In most enterprise deployments, the customer acts as the
  data controller and 3DLOOK acts as the data processor under GDPR.» (формулировка FAQ, заменила
  вариант 2026-09-07 без «the data»; хедж не срезается). DPA с SCC и UK Addendum теперь можно называть
  — FAQ их публикует. «Article 28» / «Article 9» номерами — нет.
- **CCPA/CPRA:** 3DLOOK — service provider or contractor; не продаёт персональные данные.
- **SOC 2 — НЕ сертифицированы:** «working toward obtaining a SOC 2 Attestation Report», initial
  readiness assessment пройден. «SOC 2 certified / compliant» — запрещено.
- **Medical device:** независимая регуляторная оценка — FitXpress не подпадает под определение medical
  device по UK MDR и EU MDR (для текущего intended purpose). Короткая форма — «FitXpress is not a medical
  device.» **FDA:** not cleared, authorized, or approved; 3DLOOK не утверждает, нужна ли клиренс
  конкретному клиенту. «Сертификации не применимы» / «FDA does not apply» — нельзя.
- **Хранение:** AWS, основной регион US-West-2, частично US-East-1. TLS в пути, SSE-S3 (ключи S3) в
  покое, включено всегда.
- **Фото** удаляются сразу после обработки или в течение 30 дней (по политике клиента); сохранённые
  фото автоматически размываются, лицо скрывается ещё при съёмке. **Измерения, body composition и
  3D-модели хранятся бессрочно** (если договор не говорит иначе) — «processed, not stored» писать нельзя.
- **Идентификаторы:** скан-записи привязаны к случайным ID, 3DLOOK не может опознать человека по
  сохранённым данным. «Не процессим personal identifiers» / «no personal data» — **больше не пишем**:
  фото и измерения могут быть персональными данными. Body Progress сравнивает два скана, выбранные
  клиентом; **3DLOOK не отслеживает людей** — не пиши «FitXpress tracks each patient over time».
- **AI training:** production-данные клиентов на обучение моделей не идут (без явного письменного
  разрешения клиента).
- **Контакты:** документы для procurement/legal/security — `legal@3dlook.me`; privacy-права конечных
  пользователей — `privacy@3dlook.me` (так в Privacy Policy).

В outbound и контенте — compliance points критичны для insurance, telehealth, clinical trials
аудитории; готовые строки для outbound и соцсетей — `compliance.md` §9.

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

Независимый QC (рубрика — `docs/quality-rubric.md`, отчёты — `workspace/_quality/`):

- **`quality-controller`** (mvb-core, opus) оценивает артефакты по 20-балльной шкале: статьи, брифы, outbound.
- **`post-quality-controller`** (mvb-social, sonnet) — соцпосты; вход готовым от `scripts/social_pack.py qc-prompt`; выборка 3 из 9 профилей (`qc-plan`) плюс безусловно каждый профиль, где упал линтер.
- **Координатор** после каждого авто-QC дописывает в отчёт `coordinator_review`.
- **`agent-improver`** анализирует QC + coordinator notes и предлагает правки промптов: каждые 2 недели или после 20+ артефактов.

### Auto-QC флаг

`AUTO_QC_ENABLED = true` (default)

Когда `true`, QC запускается после: `hypothesis-generator`, `icp-validator`, `message-sequencer` (outbound) · `post-drafter` (выборочно) · outline, секции, meta и финальный драфт статьи (SEO). Не запускается после механических шагов: people-extractor, importer, линтеры, сборка пакетов.

### Coordinator review

```
agreement: ✅ agree | ⚠️ disagree (1 line why)
top_issue: [1 sentence] | none
```

Замеры, почему выборка, и что QC по соцпостам проверяет, а что берёт от линтера — **`docs/qc-loop.md`**.

---

## 15. Blog Authoring Standards

**Default blog author:** Assel Sekerova (`brand-assets/team/assel-sekerova.md`). **Style guide:** `brand-assets/style-guides/blog-style-guide.md`. Полный текст требований с обоснованиями — **`docs/blog-authoring.md`**. SEO-агенты несут свои списки чтения в собственных промптах; этот раздел — политика, по которой те списки составлены, и его правят вместе с ними.

### Hard requirements for new SEO / blog articles (выжимка)

0. **`about-me.md` и `audience.md` первыми**: голос, claims discipline, сегмент и его «what NOT to say».
1. **`blog-style-guide.md` целиком, затем `editorial-rewrites.md`.** Длина предложения — gate 10 `article_lint.py` (среднее ≤ 16 слов, ≤ 6% предложений длиннее 25, максимум одно длиннее 35). Исключение для `seo-planner` (прозу не пишет): `about-me.md` + `hard-bans-card.md` + §7 `editorial-rewrites.md`.
2. **2-3 past-articles под вертикаль** из `brand-assets/past-articles/blog/`. Любая FitXpress comparison / workflow статья → сначала `manual-vs-digital-intake-occupational-health-screening.md` (финал редактора, эталон длины предложения). Trust / privacy FAQ (Type G) → `fitxpress-data-privacy-security-regulatory-faq.md`. Полный список по вертикалям — в `docs/blog-authoring.md`.
3. **Автор по умолчанию — Assel Sekerova**, если бриф не говорит иначе.
4. **Тон 2026** (measured, hedged, stats-first, workflow-framed), не индустриальный тон статей 2024 года.
5. **`editorial-guardrails.md`, 11 принципов, от начала до конца.** Жёстче всего: #1 substantiation, #2 одно число везде одинаково, #3 reserved words без доказательства нельзя, #4 никаких голых «>X%», #6 medical framing («FitXpress is not a medical device.»). Отступление выносится в Open Items, молча не правится.
6. **Phase 0: тема сверяется с `brand-assets/content-strategy/content-plan.md` ДО всего остального** (FitXpress health). Дальше идёт только безусловный `create net-new` или `publish planned hub`; условный create → вопрос Вадиму; `published`, `refresh/expand`, `merge`, `review/decide` и прочие → рекомендация и STOP. Темы без строки в плане → STOP и вопрос. Перед тем как верить приоритету, проверь дату `Last synced from source:`; таблица выигрывает по приоритету и action type, репо — по тому, что опубликовано.
7. **`terminology-guardrails.md` отдельным проходом.** Писатель держит в голове hard bans, полный проход делает редактор (`seo-editor` Pass 4 + Pass 3c, `social-editor` Pass 2b, `page-builder` Layer 2).

**Founder voice:** статьи за подписью Katerina Galich (CEO) — только thought leadership, личные эксперименты, стратегический комментарий, рефлексии после конференций. Бриф неоднозначен → спроси Вадима.

**Style guide drift:** если вышедшая статья заметно отходит от style guide, обнови `blog-style-guide.md` со ссылкой на статью.

---

## 16. Website page pipeline (`page-builder` / `/page`)

> Вынесено в `docs/page-pipeline.md` (2026-09-21, токен-диета: секция нужна только /page-прогонам,
> а грузилась каждому агенту каждой сессии). Там: scope split /page vs /new-article, четыре гейта
> G-I/G-A/G-T/G-J, бенчмарк-страница, иерархия путей (с 2026-09-27: `/fitxpress/` — родитель FX, вертикали `/fitxpress/for-{vertical}/`, главная — общая),
> общий waiver G-I по кейсам для FX-вертикалей, G-I reality check и non-negotiables. Скилл `page-builder` и команда `/page` читают его сами.
> Быстрая развилка: сторінка на 3dlook.ai → `/page`; блог/хаб/comparison → `/new-article`.
