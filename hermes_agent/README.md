# hermes_agent

Всё, что относится к **Hermes Agent AI** (внешний оркестратор-менеджер на VPS, продукт NoSearch).

## ops/
Операционная автоматизация Hermes с VPS (без секретов — `.env` НЕ коммитится):
- `model-router/` — ежедневный выбор рабочей Go-модели по формуле (`refresh.py`,
  `router_lib.py`, `model-strength.json`); primary = сильная-но-бережёт-лимит Go,
  fallback = лучшая бесплатная (нативный fallback Hermes).
- `vault-sync.sh` — авто-commit+push изменений базы знаний.
- `systemd/` — user-юниты таймеров (`model-router-refresh`, `vault-sync`).

## AI-Second-Brain/
Долгосрочная память Hermes — Obsidian/LLM-wiki vault (паттерн Karpathy's LLM Wiki):
`[[wikilinks]]`, `index.md`, `log.md`, `SCHEMA.md`, слои `raw/ entities/ concepts/ comparisons/ queries/`.
Hermes ведёт его через встроенные скиллы `llm-wiki` + `obsidian` (`WIKI_PATH`/`OBSIDIAN_VAULT_PATH`).
