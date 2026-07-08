# Log

Хронологический журнал действий над wiki (append-only, ротация по годам).

## [2026-06-26] create | vault инициализирован
- Создана структура vault (SCHEMA.md, index.md, log.md, raw/, entities/, concepts/, comparisons/, queries/).
- Git: ветка `second-brain` в репо SergeMiro/ai-agents-config; авто-синхронизация commit+push.
- Подключено к Hermes через `WIKI_PATH` и к obsidian-skill через `OBSIDIAN_VAULT_PATH` (один каталог).
