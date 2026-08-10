# hermes_agent

Всё, что относится к **Hermes Agent AI** (внешний оркестратор-менеджер на VPS, продукт NoSearch).

## Документация

| Документ | Что |
|---|---|
| **[`SETUP.md`](./SETUP.md)** | Полная установка с нуля на новом VPS — пошаговый гайд для любого AI-агента |
| **[`CONFIG.md`](./CONFIG.md)** | Reference по `config.yaml` + `.env` + `SOUL.md` — все секции, ключи, значения |
| **[`MODEL-ROUTER.md`](./MODEL-ROUTER.md)** | Логика «Модели дня»: формула, веса, формат утреннего Telegram-сообщения |

## ops/
Операционная автоматизация Hermes с VPS (без секретов — `.env` НЕ коммитится):
- `model-router/` — ежедневный выбор рабочей Go-модели по формуле (`refresh.py`,
  `router_lib.py`, `model-strength.json`); primary = сильная-но-бережёт-лимит Go,
  fallback = лучшая бесплатная (нативный fallback Hermes). Детально: [`MODEL-ROUTER.md`](./MODEL-ROUTER.md).
- `conductor-monitor.sh` — push-нотификатор: читает SQLite конду́ктора (`ho_*`),
  пушит в Telegram новые вопросы/эскалации/завершённые джобы. Dedup через state-файл.
  Cron каждые 5 мин. `--init` — отметить текущее как уже-виденное (при установке).
- `conductor-run.sh` — запуск конду́ктора (ExecStart для `hermes-conductor.service`).
- `vault-sync.sh` — авто-commit+push изменений базы знаний.
- `skill-guard/` — gated-установка скиллов для Claude Code (AgentShield + content scan).
- `systemd/` — user-юниты: `hermes-gateway.service` (бот 24/7), `model-router-refresh.{service,timer}` (07:00),
  `vault-sync.{service,timer}` (30 мин), `hermes-conductor.service` (автономный runner).

## Команды в боте, которыми стоит пользоваться

| Команда | Когда | Чего стоит |
|---|---|---|
| `/learn <источник>` | после решённой нетривиальной задачи | скилл живёт в индексе промпта: ~100 Б в КАЖДОМ ходе |
| `/journey` | ревизия памяти | ноль (только CLI/TUI/dashboard, в боте нет) |
| `/moa <вопрос>` | тяжёлый разбор, где хочется нескольких мнений | несколько параллельных вызовов = квота free-моделей |

**`/learn` — правило: только «победа → навык».** Команда открытая: источником может быть
папка, URL, вставленный текст или **сам этот разговор** — агент соберёт материал своими
инструментами и напишет `SKILL.md` через `skill_manage`. Отсюда рабочий приём: разобрались
с чем-то тяжёлым — `/learn` из разговора, и в следующий раз это процедура, а не импровизация.
Обратная сторона: каждый скилл платится байтами в каждом ходе, поэтому «на всякий случай»
не учим. Раз в месяц — ревизия: `hermes journey --json` показывает `useCount`, а
`hermes curator archive <skill>` убирает то, что не сработало (обратимо: `curator restore`).

**Одобрения в чате: жми «Once» или «Session», НИКОГДА «Always».** «Always» пишет запись в
`command_allowlist`, а это не команда, а целая КАТЕГОРИЯ опасных команд, разрешённая
навсегда. Утренний `hermes-update.py` алертит, если там что-то появилось.

## skills/
- `vps-orchestration/` — операционная политика Hermes: маршрутизация задач в Claude Code,
  failover на OpenCode при лимите Claude, управление конду́ктором, relay вопросов/эскалаций,
  git ownership. Устанавливается в `~/.hermes/skills/autonomous-ai-agents/vps-orchestration/`.

## AI-Second-Brain/
Долгосрочная память Hermes — Obsidian/LLM-wiki vault (паттерн Karpathy's LLM Wiki):
`[[wikilinks]]`, `index.md`, `log.md`, `SCHEMA.md`, слои `raw/ entities/ concepts/ comparisons/ queries/`.
Hermes ведёт его через встроенные скиллы `llm-wiki` + `obsidian` (`WIKI_PATH`/`OBSIDIAN_VAULT_PATH`).
Авто-синк в git через `vault-sync.timer` (каждые 30 мин).
