# AI Second Brain

Git-backed knowledge base / Obsidian vault — долгосрочная память Hermes Agent
(паттерн [Andrej Karpathy's LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)).

- **Открыть в Obsidian:** добавь этот каталог как vault — `[[wikilinks]]` и Graph View работают из коробки.
- **Hermes:** `WIKI_PATH` (skill `llm-wiki`) и `OBSIDIAN_VAULT_PATH` (skill `obsidian`) указывают сюда.
- **Git:** ветка `second-brain` в репо `SergeMiro/ai-agents-config` (отдельная история, не мерджится в main/fullstack-agents). Авто-синхронизация — `model-router`-стиль таймер `vault-sync` (commit+push изменений).
- Структура и правила — в `SCHEMA.md`; каталог страниц — `index.md`; журнал — `log.md`.
