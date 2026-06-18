# 3DLOOK Marketing Automation

Multi-agent система маркетинговой автоматизации на Claude Code. Три параллельных трека: **social** (контент в соцсети), **outbound** (B2B-кампании в LinkedIn / closely.io), **SEO** (статьи на сайт).

Все этапы где нужно решение Вадима — апрув через Telegram-бота. Никаких прямых публикаций — система готовит артефакты, Вадим смотрит и публикует.

---

## Что готово (на момент сборки)

- ✅ **CLAUDE.md** — заполнен под 3DLOOK с реальной фактурой
- ✅ **Продуктовая база знаний** в `brand-assets/product-info/` — 30 файлов (overview, proof-points, ICP по обоим продуктам, 12 use cases, 6 case studies, FAQ, messaging, compliance, tech-spec, competitors)
- ✅ **21 агент** — 4 social, 8 outbound, 4 SEO (было 9), 5 shared (orchestrator, context-pack-builder, brand-checker, quality-controller, agent-improver)
- ✅ **Orchestrator** — единая точка входа, выбирает workflow и координирует
- ✅ **Context Pack Builder** — компактный контекст перед каждым агентом (не весь CLAUDE.md)
- ✅ **Facts → Copy → Review** — разделение фактов и текстов, снижает hallucinations
- ✅ **Exclusion registry** — per-profile (4 профиля) + cross-profile, нет повторных рассылок
- ✅ **Per-profile social config** — регулируемое кол-во постов и product bias
- ✅ **6 slash-команд** — `/weekly-posts`, `/outbound`, `/new-article`, `/quarterly-review`, `/qc`, `/improve-agents`
- ✅ **QC петля** — quality-controller (20 баллов) + agent-improver (правит промпты)
- ✅ **Runner-ы** — bash для social, subagent-runners для outbound и SEO
- ✅ **Telegram-бот** — `bot.py` с whitelist + Approve/Edit/Reject
- ✅ **Цвет, шрифт, конкуренты** — приблизительные данные (Vadim confirm точные HEX из Figma)

## Что Вадиму нужно залить

| Что | Куда | Зачем | Приоритет |
|-----|------|-------|-----------|
| Логотипы (SVG / PNG) | `brand-assets/logos/` | visual-brief | 🔴 критично |
| Бренд-гайдлайны (PDF) | `brand-assets/brand-guidelines/` | visual-brief, brand-checker | 🟡 если есть |
| Топ-10 banner'ов из Blog banners Figma | `brand-assets/past-posts/_figma-exports/blog-banners/` | visual-brief | 🔴 критично |
| Топ-5 страниц website Figma | `brand-assets/past-posts/_figma-exports/website/` | visual-brief | 🟡 желательно |
| 10+ постов на каждый активный профиль | `brand-assets/past-posts/{profile}/` | post-drafter, brand-checker | 🔴 критично |
| Точные HEX в `colors.md` | `brand-assets/color-palette/colors.md` | visual-brief | 🟢 обновить |
| Список активных соцпрофилей и кто их ведёт | `CLAUDE.md` секция 5 | quarterly-strategist, post-drafter | 🟡 уточнить |
| Telegram bot token + chat_id | `telegram-bot/.env` | bot.py | 🔴 для запуска |

---

## Порядок запуска (рекомендация)

### Шаг 1 — Базовое заполнение (1-2 часа Вадима)
1. Залить логотипы в `brand-assets/logos/`
2. Залить топ-10 баннеров из Figma в `brand-assets/past-posts/_figma-exports/blog-banners/`
3. Уточнить точные HEX в `colors.md` из Figma
4. Обновить секцию 5 в `CLAUDE.md` (профили — кто и где)

### Шаг 2 — Telegram bot (30 мин)
1. Создать бота через @BotFather, получить token
2. Запустить бота локально, узнать свой chat_id
3. Заполнить `telegram-bot/.env`
4. Запустить `python bot.py`
5. См. `telegram-bot/README.md` — там systemd unit для постоянного запуска

### Шаг 3 — Первая outbound кампания (1 неделя до результата)
**Это самый ROI-positive трек — экономит время Вадима лично.**
1. Запустить `/outbound` в Claude Code
2. Получить гипотезу в Telegram → одобрить или скорректировать
3. company-researcher предложит топ компаний → одобрить
4. Вадим выгружает контакты из Sales Navigator (один раз руками)
5. icp-validator валидирует → одобрить список
6. message-sequencer пишет цепочки → одобрить
7. closelyhq-importer формирует CSV → Вадим импортирует в closely.io

### Шаг 4 — Past posts (когда есть время)
1. Залить минимум 10 постов на каждый профиль с метриками
2. Это разблокирует social-трек

### Шаг 5 — Social трек
1. Запустить `/quarterly-review` — получит план на Q
2. Каждую неделю — `/weekly-posts`
3. Получит черновики постов и брифы → одобрить → отдать дизайнеру

### Шаг 6 — SEO трек (последний)
1. Запустить `/new-article` с темой
2. Пройти все этапы с апрувами
3. Получить готовую статью под публикацию

---

## Файловая структура

```
marketing-claude-code/
├── CLAUDE.md                       ← главный контекст для всех агентов
├── README.md                       ← этот файл
├── QUICKSTART.md                   ← быстрый старт (5 шагов)
├── .claude/
│   ├── agents/                     ← 22 агента
│   │   ├── social/                 4 агента
│   │   ├── outbound/               8 агентов
│   │   ├── seo/                    4 агента (was 9)
│   │   └── _shared/                5 (orchestrator, context-pack-builder, brand-checker, QC, improver)
│   └── commands/                   ← 6 slash-команд
├── brand-assets/                   ← бренд + продукт + история
│   ├── README.md
│   ├── product-info/               ← ПОЛНОСТЬЮ ЗАПОЛНЕНО под 3DLOOK
│   ├── color-palette/
│   ├── fonts/
│   ├── past-posts/                 ← Vadim заполняет
│   ├── logos/                      ← Vadim заполняет
│   └── competitors/
├── workspace/                      ← все артефакты создаются здесь
│   ├── social/
│   ├── outbound/
│   └── seo/
├── runners/                        ← bash + subagent runners
├── telegram-bot/                   ← Python bot для апрувов
└── docs/
    └── architecture.md             ← диаграмма агентов
```

---

## Документация

- **`docs/architecture.md`** — диаграмма агентов, иерархия, runner логика
- **`brand-assets/README.md`** — что лежит в brand-assets и что нужно залить
- **`brand-assets/product-info/INDEX.md`** — карта продуктовой базы
- **`telegram-bot/README.md`** — настройка бота
- **`runners/README.md`** — как работают runner-ы

---

## Принципы дизайна

1. **Один артефакт = один файл.** Никакого ответа в чат вместо файла.
2. **Frontmatter всегда** с `product:` для контентных артефактов.
3. **Все числа — из `proof-points.md`.** Не выдумывать.
4. **Чекпоинты Вадима — не пропускаются.** Никогда не публиковать без апрува.
5. **Контекст в `CLAUDE.md` + `brand-assets/`.** Агент сам читает что нужно.
6. **Минимум preamble в чате.** Агент работает молча, в чат — только статус.

---

## Лидерство 3DLOOK

- Katerina Galich — CEO (katerina@3dlook.me)
- Whitney Cathcart — Co-founder & CCO (whitney@3dlook.me)
- Privacy: privacy@3dlook.me
- Сайт: https://3dlook.ai/
