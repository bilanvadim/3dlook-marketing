# Стек: Hermes Agent + Claude Code + OpenCode — кто за что отвечает

Три инструмента с разными ролями. Путаница между ними — источник почти всех
неочевидных поломок, поэтому здесь одна страница про то, что где живёт.

| | Роль | Модель | Откуда берётся модель |
|---|---|---|---|
| **Hermes Agent** | менеджер в Telegram: маршрутизирует, мониторит, отчитывается. **Код не пишет** | бесплатная OpenCode Zen с **доказанным vision** (скриншоты!) | `model-router` → `config.yaml` |
| **Claude Code** | ОСНОВНОЙ исполнитель: код, анализ, деплой | подписка Claude | `~/.claude/settings.json` + профиль |
| **OpenCode** | ЗАПАСНОЙ исполнитель, когда Claude в лимите | самая быстрая пригодная бесплатная из топ-3 провайдеров | `model-router` → `opencode.jsonc` |

Полностью бесплатный стек: платный тир `opencode-go` выведен из эксплуатации,
у Claude Code — своя подписка.

## Где что лежит

```
~/.hermes/                          Hermes Agent
  config.yaml                       model.default + model.provider + fallback_providers  ← роутер
  .env                              секреты Hermes (Telegram, провайдеры)
  ai-models.env                     ключи сторонних free-провайдеров (0600)              ← бот просит
  mem0.json                         память: Qdrant-сервер + модели (0600)
  qdrant-server/qdrant.env          порт + API-ключ Qdrant (0600)
  model-router/                     утренний выбор моделей (синкается из репо в 06:00)
    pick.json                       результат выбора · coder-history.json — эталоны скорости
  hermes-agent/gateway/claude_switcher.py   вкладки, /heavy, кнопки          ← из репо патчем
  skills/…/vps-orchestration/       политика маршрутизации                   ← из репо

~/.claude/                          Claude Code
  settings.json                     личные настройки + marketplaces/plugins  ← switch-profile.sh

~/.config/opencode/opencode.jsonc   model + small_model                      ← роутер
~/.local/share/opencode/auth.json   ключи провайдеров (0600)                 ← роутер
```

Всё, что помечено «← из репо» или «← роутер», **не правится руками** — перезапишется.

## Что синкается автоматически

| Когда | Что |
|---|---|
| 06:00 `hermes-update.timer` | `git pull` upstream Hermes → переприменение патча свитчера → **синк `ops/model-router/*` в `~/.hermes/model-router`** |
| 07:00 `model-router-refresh.timer` | выбор трёх моделей → `config.yaml`, `opencode.jsonc`, `auth.json` → отчёт в Telegram |

Порядок важен: синк раньше выбора, иначе утренний прогон работал бы на старом коде.

## Ручная установка с нуля

1. `hermes-agent/SETUP.md` — Hermes, его конфиг, секреты, юниты.
2. Юниты из `hermes-agent/ops/systemd/` (шаблоны на `%h`), включая
   **`hermes-qdrant.service`** — без него память мертва.
3. `hermes-agent/ops/claude-switcher/apply-claude-switcher-patch.py` — вкладки,
   `/heavy`, кнопки систем в Telegram.
4. `claude-code-agent/DEV/switch-profile.sh dev-sm-sm` — профиль Claude Code.
5. `opencode-agent/README.md` — три условия, без которых запасной агент молча
   возвращает пустоту.
6. Первый прогон роутера: `python3 ~/.hermes/model-router/refresh.py --dry-run`.

## Проверки живости

```bash
systemctl --user is-active hermes-gateway hermes-qdrant hermes-conductor
python3 ~/.hermes/model-router/refresh.py --dry-run          # выбор моделей, без записи
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:6343/collections   # → 401 (ключ обязателен)
cd /srv/sergiy_prod/ai-agents-config && opencode run 'Reply with exactly: BACKUP-OK'
claude -p 'ping' --max-turns 1
```

## Грабли, на которые уже наступили

- **Память Hermes** молча пуста, если mem0 указывает на embedded-qdrant (`path`):
  клиент лочит папку, второй процесс не может открыть → mem0 не инициализируется.
  И отдельно: устаревший id модели извлечения даёт 404 при живом хранилище.
  В `mem0.json` обязателен **`"https": false`**.
- **`opencode run` возвращает пустоту с кодом 0** по трём причинам сразу — см.
  `opencode-agent/README.md`.
- **Патчер свитчера marker-guarded**: новая команда не доезжает до уже пропатченной
  машины без `_refresh_commands`, и тот обязан трогать только свои строки.
- **Роутер и картинки**: флаги vision в каталоге моделей — самоописание провайдера;
  проверяется пробой (красный квадрат), иначе Hermes теряет скриншоты.
- Подробности каждой — в `hermes-agent/MODEL-ROUTER.md` и
  `hermes-agent/ops/claude-switcher/README.md`.
