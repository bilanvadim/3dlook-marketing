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
>
> Секция 6 ниже — краткое операционное резюме. При конфликте `about-me.md` имеет приоритет по голосу и claims discipline. Фактура (числа, кейсы) — всегда из `brand-assets/product-info/`, а не из этих файлов.

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

**Запрещённые AI-сигнатуры (важно для SEO + outbound + posts):**
- Em-dash (—) в риторических конструкциях типа «X — это не просто Y»
- «It's not just X, it's Y»
- Тройные параллелизмы (`fast, reliable, scalable`)
- Слова: leverage, utilize, harness, robust, seamless, comprehensive, delve, navigate (в перен. смысле), tapestry, realm
- «Furthermore / Moreover / Additionally» в начале предложений (минимизировать)

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
| Бриф-мейкер | `visual-brief` | Бриф для дизайнера в Canva |
| Дизайнер | Человек | Делает визуал |
| Апрувер | Вадим (через Telegram) | Все чекпоинты |
| Outbound | пайплайн `outbound/*` | Hypothesis → ... → Campaign analysis |
| SEO | пайплайн `seo/*` | Keywords → ... → Publish → trigger social |
| Brand guardian | `brand-checker` (shared) | Проверка тона / no-go / AI-сигнатур |

**Social workflow:** SEO publish-package апрувлен → `/post-from-article {slug}` → `post-drafter` × N профилей → Telegram апрув → `visual-brief`. Квартальный план для соцсетей не используется.

**Social workspace:** `workspace/social/articles/{slug}/{profile}/post.md`

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

| Дата | Изменение | Кто |
|------|-----------|-----|
| 2026-04-28 | Initial setup, populated product info from decks | Claude / Vadim |
| 2026-04-30 | Added quality control loop (quality-controller + agent-improver) | Claude |
| 2026-05-20 | Changed 3DLOOK Company product_bias: 50/30/20 → 70/10/20 (FX/MT/mixed) | Claude / Vadim |
| 2026-05-22 | Built blog style infrastructure: 9 past-articles saved, blog-style-guide.md created, Assel Sekerova author profile added, section 15 (Blog Authoring Standards) added | Claude / Vadim |
| 2026-06-09 | Added `editorial-guardrails.md` (11 principles from v2-asselya FAQ-article review cycle with Whitney + Asselya) and referenced it as hard requirement #5 in section 15 — applies to ALL 3DLOOK content, not just blog/SEO | Claude / Vadim |
| 2026-06-27 | Reworked social pipeline: removed quarterly plan dependency. Posts now created from SEO articles via `/post-from-article`. post-drafter rewritten, seo-runner updated to trigger social after publish-package approval, /weekly-posts deprecated | Claude / Vadim |
| 2026-06-27 | Expanded social profiles from 4 LinkedIn to 9 profiles across 4 platforms. Added Twitter, Instagram, Facebook company accounts. Added BD profiles: Nick Omelchak (USA), Olena Kudryavtseva (Europe), Kateryna Boichuk (Israel). Whitney disabled. post-drafter updated with platform-specific rules. | Claude / Vadim |
| 2026-07-01 | linkedin-katerina reworked: product_bias → 100% FitXpress, market → UK only. ICP focus updated to UK telehealth, UK pharmacies, UK insurers, UK employer health. Tone updated with UK regulatory context (MHRA, CQC, NHS). MT topics and US/EU regulatory framing added to avoid list. | Claude / Vadim |
| 2026-07-01 | All active profiles: product_bias → 100% FitXpress across all 9 profiles. Mobile Tailor and mixed content removed from social pipeline entirely. | Claude / Vadim |
| 2026-07-01 | Hashtags removed from all profiles. hashtags: none in social-profiles-config.md. Hashtag instructions removed from post-drafter.md (Instagram, Facebook, LinkedIn sections + post template). | Claude / Vadim |
| 2026-07-01 | /post-from-article now assembles review-digest.md after all drafts — one file per article slug with all posts in read order for copywriter review. Design tips added: post-drafter generates a 3-line design tip (format / visual idea / notes) per post; digest includes it as a blockquote under each post. | Claude / Vadim |
| 2026-07-01 | post-drafter.md and post-from-article.md rewritten in English. Hard rule added: all output (post text, angle, design tip, CTA) must be in English. | Claude / Vadim |
| 2026-07-01 | Design tip logic reworked: social post visuals now adapt from the article's OG image direction (publish-package.md section 4). Fields: article visual / format / adaptation / keep. Designer adapts one asset, not creates from scratch. | Claude / Vadim |
| 2026-07-01 | Post formats defined: text, text + photo, carousel, infographic, lead magnet, poll, screenshot. post-drafter selects format per post with platform constraints (poll: LinkedIn/Twitter only; lead magnet: LinkedIn/Facebook only). | Claude / Vadim |
| 2026-07-05 | `icp-detail.md` rewritten from internal ICP/Sales Google Doc (12-segment playbook): added precise buyer titles, categorized pain points, revenue thresholds, named company examples, and buying signals for every existing FitXpress/Mobile Tailor segment. Added 2 new segments: FitXpress Plastic Surgery (Turkey-first geo) and FitXpress BCRL Detection & Monitoring. Section 4 summary and geo list updated. `context-pack-builder.md` updated to pull segment-specific ICP context (persona + pain points) for SEO/social, not just outbound. | Claude / Vadim |
| 2026-07-06 | Added 3 canonical top-level docs — `about-me.md` (FitXpress brand voice + claims discipline), `audience.md` (7 health segments: hook + what-not-to-say), `DESIGN.md` (confirmed Figma design system). Wired them into the agent system: section 6 now points to about-me/audience as voice source of truth; section 7 makes DESIGN.md the single design source of truth; section 15 adds them as mandatory read #0 for seo-planner/seo-writer. **Resolved stale-token conflict:** `DESIGN.md` (`#143DFF`, Satoshi) supersedes placeholder `colors.md` (`#2962FF`) and `fonts.md` (Inter) — both converted to redirect stubs. Updated `context-pack-builder` (voice_fingerprint + audience-layer fields sourced from about-me/audience), `brand-checker` (checks against about-me claims discipline + DESIGN tokens), `post-drafter` (reads about-me/audience), `visual-brief` (reads DESIGN.md, correct tokens). | Claude / Vadim |
| 2026-07-07 | Fed the finalized **Clinical Trials use-case article** into the agent system as a reference and encoded two recurring drafting anti-patterns Vadim flagged. Saved the clean v3 body to `brand-assets/past-articles/blog/clinical-trials-anthropometric-measurement.md` (with `known_issues` frontmatter) and wired it into §15 hard-req #2 as the model for clinical-trials / CRO-pharma / regulated verticals. Added two **mechanical writing rules** to `editorial-guardrails.md` — **M1** (expand every abbreviation at first use, incl. BMI and cited regulators FDA/ICH/GCP) and **M2** (prefer positive scoping over stacked/interrupted negation) — enforced them in `seo-writer` (Стиль), `seo-editor` (Pass 4), and `brand-checker` (new check 3b), and referenced them in the guardrails How-to-apply table. Repeated compliance disclaimer left as-is (Vadim: fits each section; M2 governs per-sentence negation density, not disclaimer frequency). Also flagged: `utilize/utilizing` shipped in the final copy (banned word) — added to `seo-editor` Pass 4 banned-word check. | Claude / Vadim |
| 2026-07-07 | Wired the **Health content strategy** into the SEO/blog agent system. Materialized two canonical docs in `brand-assets/content-strategy/`: `content-plan.md` (offline copy of the hub-and-cluster editorial matrix from the [strategy spreadsheet](https://docs.google.com/spreadsheets/d/1Sy7EzzZZvCKyrD30pbhElEpCZDbzuMtMkxdiDTIP8AE/edit) — 9 hubs × clusters, with intent/action-type/priority/existing-URL/cannibalization guardrail per row) and `content-strategy-guidelines.md` (16-section placement rules from the [guidelines Doc](https://docs.google.com/document/d/18twJmZ3wt2MRe9lQbfLhjJ9CwqKT60pzwCJMRpSrfvo/edit)). Added **Phase 0 strategy gate** to `seo-planner` (resolves the strategy row before keywords; only `create net-new`/`publish planned hub` proceed — refresh/section-first/review-decide/lead-magnet return a recommendation and STOP; no row → ask Vadim). `context-pack-builder` now emits a `content_strategy` block (hub, cluster, intent, action_type, existing_urls, cannibalization_guardrail, vertical_boundary, internal_link_targets) for track=seo FitXpress. `seo-writer` enforces positioning (§8), vertical boundaries (§9), 4-direction internal links (§11), FAQ (§14), CTA-by-intent (§15). `seo-editor` gained a Pass 3b strategy-compliance check; `seo-publisher` gained a 9-point strategy checklist. `quality-controller` checks articles against the strategy; `orchestrator` SEO workflow documents the gate; section 15 hard requirement #6 added. FitXpress-only — Mobile Tailor unaffected. | Claude / Vadim |
| 2026-07-21 | **Outbound profiles reworked: 4 → 5, aligned to social-pipeline owners + markets.** Replaced the old set (`vadim, katerina, whitney, profile4`) with 5 geo-scoped profiles taken from `social-profiles-config.md`: `katerina`/UK (CEO), `nick`/USA (BD), `olena`/Europe-EU (BD), `katya`/Israel (BD), `vadim`/Australia (Marketing — geo not defined in social, assigned by Vadim). Added a profile→market table + geo-discipline rule to `runners/outbound-runner.md` (§Multi-profile) and to CLAUDE.md §5. Created `nick/olena/katya-registry.json`, added `market` field to `vadim/katerina-registry.json`, deleted empty `whitney/profile4-registry.json`. Updated `exclusions/README.md`, `docs/architecture.md`, project `README.md`. Updated the shared `profile:` enum and per-profile voice hints in `orchestrator` + `context-pack-builder` (both `.claude/agents/_shared/` and `.claude/plugins/mvb-core/0.2.0/agents/`). | Claude / Vadim |
| 2026-07-21 | **Outbound message sequence simplified: 4 steps → 2 messages, note-less invite.** Per Vadim: connection request now sent WITHOUT a note; Message 1 goes out immediately after the invite is accepted; Message 2 follows +5 days. Removed the old 4-step sequence (note ≤300 / welcome +3d / follow-up +7d / breakup +14d). Rewrote `message-sequencer` (structure table, algorithm → 2 messages, output template `## Message 1/2`, char limits 1000/800, compliance-mention rule, `_summary` stats N×2), `closelyhq-importer` (parse `## Message N` blocks → CSV columns `connection_note` empty / `message_1` / `message_2`; checks + import-log + Vadim steps), and `response-classifier` (`which_message_replied_to` 1-2, "Replied to: Message N"). Propagated across all 4 agent copies (`.claude/agents/outbound/`, project plugin `mvb-outbound/0.2.0`, global cache, DEV source). Updated the Hermes `outbound-pipeline.md` reference. Past AU-telehealth campaign message artifacts left untouched (historical). | Claude / Vadim |
| 2026-07-21 | **Outbound Message 1 spec/template added.** Created `brand-assets/product-info/outbound-message1-template.md` as the source of truth for the LinkedIn opener sent right after a connection is accepted: English, ≤600 chars, first person, confident-not-pompous tone framed from experience (not selling), named-cliché ban ("I admire your mission" / "excited about your journey"), fixed structure (Hi {name} → light hook → specific observation/question → product intro anchored on the "mobile body scanning layer … structured, trackable metrics that drop into the patient record" framing → soft CTA → first-name-only signature), a hook bank + fitting style phrases + 2 Katerina examples. Per Vadim the template **hard-bans long dashes (— / –) and triple parallelisms** (§6 AI-signatures, already enforced by `brand-checker` check 3) across both messages; the template's own examples/style phrases were rewritten dash-free and triple-free so the agent can't imitate a violation. Wired into `message-sequencer` (input list, structure table row 1 = ≤600 + template ref, algorithm, output `Char count / 600`, English + signature rule) and dropped Message 1 char cap 1000→600 in `closelyhq-importer`. Added to product-info `INDEX.md`. Propagated across all 4 message-sequencer/importer copies. | Claude / Vadim |
| 2026-07-21 | **Outbound Message 2 spec/template added.** Created `brand-assets/product-info/outbound-message2-template.md` for the +5-day follow-up sent only when Message 1 got no reply: English, ≤550 chars, conversational/honest/expert, first person, value-led (concrete outcome for the prospect + their company, not features), ends with a demo-call offer + calendar link as plain text, first-name-only signature. Same §6 hard-bans as Message 1 (no long dash, no triple parallelisms, no clichés/banned words). **Per-profile calendar-link map** in the template: `katerina` = https://meetings.hubspot.com/katerina-galich; `nick`/`olena`/`katya`/`vadim` = TBD — agent must use the sending profile's own link and STOP-and-ask Vadim if it's TBD (never reuse another person's link or invent one). Wired into `message-sequencer` (input, structure row 2 = ≤550 + template ref + "only if no reply", algorithm, output `Char count / 550`), dropped Message 2 cap 800→550 in `closelyhq-importer`, added to `INDEX.md`, updated the Hermes `outbound-pipeline.md` message table (also corrected Message 1 limit there to ≤600). Propagated across all 4 agent copies. | Claude / Vadim |
| 2026-08-07 | **LinkedIn post prompts wired into the social pipeline from Vadim's Google Doc.** Materialized `brand-assets/linkedin-post-prompts.md` — offline copy of the [LinkedIn prompts Doc](https://docs.google.com/document/d/19KKWLtJv4Jx_hKbgxy0TCWnLXgnHe0-gxGuDj9vA2WQ/edit) with a per-profile brief for all 6 active LinkedIn profiles (company page, Katerina, Katya, Vadim, Nick, Olena). It is now the source of truth for LinkedIn audience / market / focus / tone / structure / word count / closing move; `social-profiles-config.md` blocks are the operational summary and lose on conflict. **Two house-rule overrides decided by Vadim beat the Doc:** (1) **no hashtags on any profile** — the Doc asks for 6–8 on the company page and Katya, but hashtags were removed org-wide on 2026-07-01; (2) **1–2 emoji max** per CLAUDE.md §6 — the Doc's 3–5 / max-5 is read as a ceiling, not a target. Other resolutions: **`linkedin-vadim` audience switched from marketing/growth community + GTM to Australian telehealth / digital health / fitness platforms / enterprise health operators** (ops, privacy, scalability, implementation, procurement) — now aligned with his outbound market; `linkedin-katya` widened Israel → **Israel + Gulf**; `linkedin-olena` scoped to **Continental Europe excluding the UK**, country-specific regulation banned unless the article raises it, and her stale Mobile Tailor / fashion-tech content types dropped (all profiles have been 100% FitXpress since 2026-07-01); `linkedin-katerina` keeps her UK lens (MHRA/CQC/NHS) layered on top of the Doc's founder-voice brief, since the Doc is silent on geo; LinkedIn length switched to the Doc's **word counts** (company 180–280, personal 180–250) with char approximations kept for counting. Wired into `post-drafter` (mandatory read step 2b, rewritten LinkedIn platform rules + per-profile angles, hard rule #5), `social-planner` (input list, regional-lens line, dedup checklist row for Vadim/AU), `context-pack-builder` (per-profile voice hints + LinkedIn precedence note), `brand-checker` (new LinkedIn-only checks 11–13: zero hashtags / ≤2 emoji as an automatic FAIL, word count, brief compliance; verdict scale 13 for LinkedIn). Propagated across all 4 agent copies. | Claude / Vadim |
| 2026-07-21 | **Outbound calendar links filled in (3 of 4 TBDs resolved) + `vadim` no-CTA rule.** Set the per-profile HubSpot meeting links in `outbound-message2-template.md`: `nick` = https://meetings.hubspot.com/nick-omelchak, `olena` = https://meetings.hubspot.com/olena-kudriavtseva, `katya` = https://meetings.hubspot.com/kateryna-boichuk (`katerina` unchanged). **`vadim` has no calendar account**, so per Vadim his Message 2 uses **no demo-call offer and no calendar link — instead it closes with a short soft conversational ask in Message 1 style ("Might be worth a quick chat?")** + first-name signature. Updated the template (calendar table, the rule note under it, Purpose, Structure step 3) and propagated the `vadim` exception across all 4 `message-sequencer` copies (structure table row 2 + algorithm Message 2 bullet). Updated `INDEX.md`. Message 1's soft ask is calendar-independent and left unchanged for all profiles. | Claude / Vadim |

---

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
- `post-drafter` (social)
- `seo-outline-builder` (SEO шаг 3)
- `seo-section-writer` (по каждой секции)
- `seo-meta-generator` (SEO шаг 8)
- Финальный `draft-v3-final.md` после ai-rewrite

QC НЕ запускается после механических шагов: people-extractor, citation-deduper, readability-editor (они не несут creative качества).

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
5. **Read `brand-assets/style-guides/editorial-guardrails.md` and apply the 11 principles end-to-end.** These guardrails apply to **ALL 3DLOOK content** — blog, SEO, outbound, social, whitepaper, deck — not just SEO articles. Established 2026-06-09 from the v2-asselya FAQ-article review cycle (Whitney + Asselya editorial pass). Phase 1 fact-check runs the 11 as an explicit checklist; Phase 3 writing enforces them throughout; Phase 4 self-critique surfaces any bent guardrail to an Open Items block for Asselya per principle #11 — no silent edits. Hardest-binding principles: #1 (substantiation — cut what you can't back), #2 (one number, everywhere the same), #3 (reserved words "independent" / "validated" / "third-party" off-limits without proof), #4 (no bare ">X%" without methodology — use "available under NDA" instead), #6 (medical framing is "not positioned as," never "does not apply").
6. **Resolve the topic against `brand-assets/content-strategy/content-plan.md` BEFORE anything else (FitXpress health only).** `seo-planner` runs this as a Phase 0 gate: locate the topic's row (hub · cluster · intent · action type · priority · existing-URL · cannibalization guardrail), and **act on the action type** — only `create net-new` / `publish planned hub` proceed to a new article; `refresh/expand`, `section first`, `review/decide`, and `lead magnet` return a recommendation and STOP (no new article). A topic with no row → stop and ask Vadim where it belongs. The rules that govern placement, positioning language, vertical boundaries, internal linking (4 directions), FAQ, and CTA-by-intent live in `brand-assets/content-strategy/content-strategy-guidelines.md`. `content-plan.md` is the offline copy of the [strategy spreadsheet](https://docs.google.com/spreadsheets/d/1Sy7EzzZZvCKyrD30pbhElEpCZDbzuMtMkxdiDTIP8AE/edit); re-sync it when the sheet changes. This is a hub-and-cluster system: **a title without its strategy row is not a brief.**

### Founder-voice exception

Articles signed by **Katerina Galich (CEO)** are reserved for:
- Thought-leadership and opinion pieces
- Personal experiments (e.g., the AI photo-manipulation experiment narrative)
- Strategic commentary on AI risk and industry direction
- Conference reflections and post-event reactions

Default to Assel for everything else. If a brief is ambiguous, ask Vadim before deciding the byline.

### Style guide drift policy

If a new production article significantly departs from the style guide (e.g., a deliberate experiment), update `brand-assets/style-guides/blog-style-guide.md` to record the new pattern with the source article cited. The style guide is a living document driven by what actually ships, not a frozen rulebook.

