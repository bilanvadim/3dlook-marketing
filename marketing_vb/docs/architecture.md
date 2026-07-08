# Архитектура системы — 3DLOOK Marketing Automation v3

## Новая архитектура (post-Vadim feedback)

```
Vadim Request
     ↓
📋 Orchestrator
     ↓
📦 Context Pack Builder → compact YAML для агента
     ↓
┌─────────────────┬──────────────────┬────────────────┐
│  📣 SOCIAL      │  📨 OUTBOUND     │  📰 SEO        │
│  4 агента       │  8 агентов       │  4 агента      │
│                 │  + exclusion     │  (was 9)       │
│                 │  registry        │                │
└─────────────────┴──────────────────┴────────────────┘
     ↓                   ↓                  ↓
🛡 brand-checker (review: no unsupported claims)
📊 quality-controller (score 20 pts)
     ↓
📱 Telegram → Vadim: ✅ / ✏️ / ❌
     ↓
🔧 agent-improver (раз в 2 недели)
```

## Ключевые изменения vs v2

| Что | Было | Стало | Почему |
|-----|------|-------|--------|
| SEO | 9 агентов | 4 (Planner, Writer, Editor, Publisher) | Проще поддерживать, дешевле |
| AI-detector-rewriter | Цель «снизить AI-score до 25%» | Цель «сделать текст экспертным и живым» | AI detectors нестабильны |
| Entry point | Агенты напрямую | Orchestrator → Context Pack → Agent | Стабильность и single entry |
| Context | Каждый агент сам читает всё | Context Pack Builder даёт compact YAML | Меньше шума, стабильнее |
| Facts vs Copy | Смешано | Research → Content → Review pattern | Меньше hallucinations |
| Outbound profiles | 1 | 4 (vadim, katerina, whitney, profile4) | Реальная setup Вадима |
| Exclusion registry | Нет | Per-profile + cross-profile | Нет повторных рассылок |
| Social profiles | Generic | Per-profile config с posts_per_week | Регулируемое кол-во |

## Все агенты (22)

### 📣 Social (4)
- **quarterly-strategist** — Планирует темы постов на квартал для каждого профиля
- **post-drafter** — Пишет текст поста на основе context pack
- **visual-brief** — Инструкция дизайнеру что нарисовать
- **social-analytics** — Метрики прошлых постов

### 📨 Outbound (8)
- **hypothesis-generator** — Придумывает «кому продаём» по продукту и вертикали
- **company-researcher** — Находит 30 компаний (с учётом exclusion registry)
- **people-extractor** — Чистит CSV из Sales Navigator
- **icp-validator** — Отсеивает неподходящих (с учётом exclusions)
- **message-sequencer** — Персональные цепочки из 4 сообщений
- **closelyhq-importer** — CSV для closely.io + обновляет exclusion registry
- **response-classifier** — Сортирует ответы
- **campaign-analyzer** — Выводы + обновляет reply status в registry

### 📰 SEO (4 — было 9)
- **seo-planner** — Keywords + title + outline (3-in-1)
- **seo-writer** — Пишет секции по approved плану
- **seo-editor** — 4 прохода: dedup, structure, expert voice, polish
- **seo-publisher** — Meta + checklist + CMS package

### 🔧 Shared (6)
- **orchestrator** — Главный координатор всех workflows
- **context-pack-builder** — Compact context YAML перед каждым агентом
- **brand-checker** — Review: тон, banned words, unsupported claims
- **quality-controller** — Оценка 20 баллов
- **agent-improver** — Правит промпты на основе QC данных

## Facts → Copy → Review pattern

Во всех workflows:

```
Research (produces facts only)
     ↓
approved_claims in context pack
     ↓
Content (writes copy ONLY from approved facts)
     ↓
Review (checks no unsupported claims added)
```

| Track | Research | Content | Review |
|-------|----------|---------|--------|
| Social | quarterly-strategist picks topics from product-info | post-drafter writes from context pack | brand-checker + QC |
| Outbound | hypothesis-generator + company-researcher | message-sequencer | brand-checker + QC |
| SEO | seo-planner (keywords + outline) | seo-writer | seo-editor + brand-checker + QC |

## Exclusion Registry (outbound)

```
workspace/outbound/exclusions/
├── vadim-registry.json          per-profile: companies + people
├── katerina-registry.json
├── whitney-registry.json
├── profile4-registry.json
└── global-company-registry.json cross-profile coordination
```

Rules:
- One company = one profile (no overlap)
- Existing customers always excluded (9 companies)
- After 6 months of no-reply → company released for other profile

## Social Profiles Config

`brand-assets/social-profiles-config.md` — per-profile:
- `posts_per_week` (0-5, configurable)
- `product_bias` (% FX / MT / mixed)
- `icp_focus`
- `tone` + `avoid`
- `content_types`

## QC Loop

Same as before:
```
Agent creates artifact → QC scores (20 pts) → coordinator review → Vadim approve
→ [biweekly] agent-improver → proposes prompt diffs → Vadim applies
```

5 categories: Adherence (5) + Factual (5) + Brand (3) + Format (3) + Quality (4) = 20.

## 6 Slash Commands

| Command | What | Workflow |
|---------|------|---------|
| `/weekly-posts [week]` | Посты на неделю | Social |
| `/outbound [stage] [slug] [profile]` | Холодная кампания | Outbound |
| `/new-article [topic] [stage]` | SEO статья | SEO |
| `/quarterly-review` | План на квартал | Strategy |
| `/qc [artifact-path]` | Оценка качества | QC |
| `/improve-agents [days] [agent]` | Улучшение промптов | Meta |

All commands go through Orchestrator which calls Context Pack Builder first.
