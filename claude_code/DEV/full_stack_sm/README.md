# ai-agents-config

Этот репозиторий — **Claude Code plugin marketplace** (подключается напрямую) **плюс** автономный дирижёр в подпапке `orchestrator/`.

> Полное описание всей системы и порядка работы — в **FULLSTACK-AGENTS.md**. Прочитай его первым.

## Две зоны репозитория

| Зона | Что это | Как используется |
|---|---|---|
| Корень (`.claude-plugin/`, `plugins/`, `CLAUDE.md`, `.claude/`) | Claude Code plugin marketplace: 9 агентов + trend-scout, правила оркестрации, enforcement безопасности | `/plugin marketplace add <repo>` в Claude Code |
| `orchestrator/` | Автономный дирижёр (TypeScript-сервис вокруг Agent SDK) | `npm install && npm test`, затем Docker — см. `orchestrator/README.md` |

## Быстрый старт (marketplace)
```
/plugin marketplace add <your-org>/ai-agents-config
/plugin install hermes-core@ai-agents-config
# далее нужные слои: hermes-design, hermes-frontend, hermes-backend, hermes-data,
#                    hermes-platform, hermes-quality, hermes-sre, hermes-scout
```
Внешние компаньоны (ставятся отдельно): `frontend-design@claude-plugins-official`, `superpowers@claude-plugins-official`, `trailofbits/skills`.

## Быстрый старт (дирижёр)
```
cd orchestrator
cp .env.example .env   # заполнить Postgres + (опц.) Telegram
npm install && npm test
```

## Состав плагинов
product-architect · design-director · frontend-engineer · backend-engineer · database-engineer · platform-engineer · qa-engineer · security-auditor · sre-engineer · trend-scout. Покрывают все 14 слоёв production full-stack + дизайн.

**Модели:** все 10 агентов — на Opus последней (`claude-opus-4-8`); Sonnet — только для рутины (explore/grep/форматирование). Затраты не оптимизируются. Защита от пережигания токенов — детект зацикливания в дирижёре, не лимит бюджета.

**Git/деплой:** после каждого хода `Stop`-хук авто-коммитит и пушит ветку → Vercel деплоит сам (Git-интеграция). `merge` всегда требует человека. На `main`/`master` авто-push отключён.
