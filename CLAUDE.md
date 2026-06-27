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

См. полные документы в `brand-assets/product-info/icp-detail.md`. Краткое резюме:

### FitXpress ICP
- **Telehealth & weight loss / GLP-1:** virtual clinics, coaching apps. Buyer: VP Product / Chief Medical Officer / Head of Clinical Operations
- **Online pharmacies / digital prescribers:** BMI verification. Buyer: Head of Compliance / Chief Pharmacist
- **Life & disability insurers:** underwriting verification. Buyer: VP Underwriting / Chief Underwriting Officer
- **Health plans / employer wellness:** rewards programs. Buyer: VP Member Engagement / Head of Wellness
- **Bariatric / metabolic clinics:** pre-qualification. Buyer: Director of Operations / Medical Director
- **Occupational health providers:** screening. Buyer: VP Operations / Chief Medical Officer
- **CROs / pharma sponsors:** clinical trials. Buyer: Director of Clinical Operations / Head of DCT

### Mobile Tailor ICP
- **MTM brands & tailors:** menswear, womenswear, bridal, formalwear. Buyer: Founder / Head of E-commerce / VP Operations
- **On-demand manufacturers:** integrating scans в pattern-making. Buyer: VP Manufacturing / Head of Product Development
- **Uniform companies:** workwear, healthcare, public safety. Buyer: VP Operations / Director of Procurement

---

## 5. Профили в социальных сетях

**Детальная per-profile config: `brand-assets/social-profiles-config.md`** — posts_per_week, product_bias, tone, content_types, length, hashtags.

**Активные профили (9 штук):**

| profile_id | Платформа | Owner | Product bias |
|------------|-----------|-------|--------------|
| `twitter-company` | Twitter / X | Vadim manages | 70% FX / 10% MT / 20% mixed |
| `instagram-company` | Instagram | Vadim manages | 70% FX / 10% MT / 20% mixed |
| `facebook-company` | Facebook | Vadim manages | 70% FX / 10% MT / 20% mixed |
| `linkedin-company` | LinkedIn Company | Vadim manages | 70% FX / 10% MT / 20% mixed |
| `linkedin-katerina` | LinkedIn Personal | Katerina Galich (CEO) | 70% FX / 10% MT / 20% mixed |
| `linkedin-vadim` | LinkedIn Personal | Vadim Bilan (Marketing) | 50% FX / 30% MT / 20% mixed |
| `linkedin-nick` | LinkedIn Personal | Nick Omelchak (BD, USA) | 80% FX / 10% MT / 10% mixed |
| `linkedin-olena` | LinkedIn Personal | Olena Kudryavtseva (BD, Europe) | 55% FX / 30% MT / 15% mixed |
| `linkedin-katya` | LinkedIn Personal | Katya Boychuk (BD, Israel) | 75% FX / 10% MT / 15% mixed |

**Вимкнені:** `linkedin-whitney` (Whitney Cathcart, CCO) — posts_per_week: 0.

**Активувати/вимкнути профіль:** зміни `posts_per_week` в `brand-assets/social-profiles-config.md`.
**Для outbound:** LinkedIn-профілі використовуються для рассылок з exclusion registry (см. `workspace/outbound/exclusions/`).

---

## 6. Tone of Voice

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

См. `brand-assets/`. Перед визуальным брифом или постом агент **обязательно** читает:
- `brand-assets/brand-guidelines/` — гайдлайны (если есть PDF)
- `brand-assets/color-palette/colors.md` — точные HEX
- `brand-assets/fonts/fonts.md` — шрифты
- `brand-assets/past-posts/` — последние посты под каждый профиль

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
| 2026-06-27 | Expanded social profiles from 4 LinkedIn to 9 profiles across 4 platforms. Added Twitter, Instagram, Facebook company accounts. Added BD profiles: Nick Omelchak (USA), Olena Kudryavtseva (Europe), Katya Boychuk (Israel). Whitney disabled. post-drafter updated with platform-specific rules. | Claude / Vadim |

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

1. **Read `brand-assets/style-guides/blog-style-guide.md` in full** — the voice, structural templates (Article Types A–F), banned patterns, and per-vertical vocabulary are not optional.
2. **Read 2–3 relevant past-articles from `brand-assets/past-articles/blog/`** that match the target vertical:
   - FitXpress topics → read at least one of: `mobile-body-scanning-insurance-underwriting.md`, `wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning.md`, `3dlook-turns-two-photos-structured-body-data.md`
   - Mobile Tailor topics → read at least one of: `on-demand-clothing-manufacturing.md`, `sustainable-fashion-manufacturing.md`, `the-future-of-fashion-retail.md`
   - Comparison / buyer's-guide topics → `body-scanning-technology-comparison.md`
3. **Apply Assel Sekerova as author** by default in the article frontmatter, unless Vadim specifies otherwise in the brief.
4. **Match the 2026 tone** (measured, hedged, stats-first, workflow-framed) — not the 2024 industry-trend tone present in older MT articles. The 2024 articles use phrases now banned by CLAUDE.md section 6 (leverage / revolutionize / harness / etc.); do NOT mimic their phrasing even though they are in the corpus.
5. **Read `brand-assets/style-guides/editorial-guardrails.md` and apply the 11 principles end-to-end.** These guardrails apply to **ALL 3DLOOK content** — blog, SEO, outbound, social, whitepaper, deck — not just SEO articles. Established 2026-06-09 from the v2-asselya FAQ-article review cycle (Whitney + Asselya editorial pass). Phase 1 fact-check runs the 11 as an explicit checklist; Phase 3 writing enforces them throughout; Phase 4 self-critique surfaces any bent guardrail to an Open Items block for Asselya per principle #11 — no silent edits. Hardest-binding principles: #1 (substantiation — cut what you can't back), #2 (one number, everywhere the same), #3 (reserved words "independent" / "validated" / "third-party" off-limits without proof), #4 (no bare ">X%" without methodology — use "available under NDA" instead), #6 (medical framing is "not positioned as," never "does not apply").

### Founder-voice exception

Articles signed by **Katerina Galich (CEO)** are reserved for:
- Thought-leadership and opinion pieces
- Personal experiments (e.g., the AI photo-manipulation experiment narrative)
- Strategic commentary on AI risk and industry direction
- Conference reflections and post-event reactions

Default to Assel for everything else. If a brief is ambiguous, ask Vadim before deciding the byline.

### Style guide drift policy

If a new production article significantly departs from the style guide (e.g., a deliberate experiment), update `brand-assets/style-guides/blog-style-guide.md` to record the new pattern with the source article cited. The style guide is a living document driven by what actually ships, not a frozen rulebook.

