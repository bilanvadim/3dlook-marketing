# claude_code

Всё, что относится к Claude Code.

## DEV/full_stack_sm
Система **Fullstack agents** (Claude Code plugin marketplace: 10 агентов + команды `/sm-*`
+ скиллы + `conductor/`) — перенесена сюда из бывшей ветки `fullstack-agents`
(теперь всё живёт в единственной ветке `main`).

⚠️ Это был marketplace-репозиторий: `.claude-plugin/marketplace.json` и пути
`./plugins/...` рассчитаны на корень. После переезда в подпапку маркетплейс как
точка установки из корня не работает — это снимок логики, а не активный marketplace-root.
