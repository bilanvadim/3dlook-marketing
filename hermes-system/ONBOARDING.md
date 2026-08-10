# Установка системы Hermes + Telegram-бот + Claude Code/OpenCode на `vadim_prod`

> Это промпт для твоего Claude Code. Открой Claude Code в корне репозитория и
> скажи: **«прочитай `hermes-system/ONBOARDING.md` и выполни всё по шагам»**.
> Перед этим заполни таблицу в ШАГЕ 0 — без данных установка встанет на первом шаге.

---

## Что это

Полная копия рабочей системы Сергея, собранная в самодостаточный кит. Три слоя:

| Слой | Кто | Что делает |
|---|---|---|
| ① **Hermes Agent** | Telegram-бот (@твой_бот) | менеджер: говорит с тобой, помнит контекст, решает, что запускать |
| ② **Conductor** | сервис на libSQL | автономный воркер A→Z: берёт задачу из очереди, ведёт до конца, спрашивает при риске |
| ③ **Claude Code / OpenCode** | «руки» | делает работу: код, SEO, маркетинг, security — плагинами и субагентами |

В боте внизу две кнопки: **🧑‍💼 Менеджер (Hermes)** и **⚙️ Исполнитель (Claude, OpenCode)**.

### Что уже есть в этом репозитории и что не трогать

- `marketing_vb/` — **твоя** оригинальная система. Не трогается вообще.
- `hermes_agent/` + `claude_code/` — **старая** версия этой же системы (PR #1,
  смёржен в июле). Там живут твои профили `marketing_vb` и `marketing_vb_sm`
  (микс твоих агентов с базой Hermes) — **не удаляй их**, в новом ките их нет.
- `hermes-system/` (эта папка) — **новая, текущая** версия: обновлённый Hermes,
  бесплатный стек моделей, OpenCode как запасной кодер, новые системы
  `dev-sm / seo-sm / marketing-sm / security-sm / sandbox-sm`.

Ставим новый кит рядом со старым. Когда убедишься, что новое работает — старое
можно снести, но сначала перенеси из него профили `marketing_vb*` (это отдельная
задача, спроси Сергея).

---

## ШАГ 0 — собери данные (сделай это ПЕРВЫМ)

Заполни `hermes-system/secrets.env`. Ничего больше искать руками не придётся:

```bash
cd ~/3dlook-marketing/hermes-system
cp secrets.env.example secrets.env && chmod 600 secrets.env
nano secrets.env
```

**Обязательно — без этого установка остановится:**

| Переменная | Что это и где взять |
|---|---|
| `TELEGRAM_BOT_TOKEN` | Токен **своего нового** бота: [@BotFather](https://t.me/BotFather) → `/newbot` → имя → получишь `8123456789:AAF…`. **Не используй бота Сергея** — один токен = один процесс, иначе оба бота начнут отбирать друг у друга сообщения. Можно взять токен своего существующего бота из `marketing_vb/telegram-bot/` |
| `TELEGRAM_ALLOWED_USERS` | **Твой** числовой Telegram user id: напиши [@userinfobot](https://t.me/userinfobot), он ответит `Id: 123456789`. Это весь whitelist — кто не в списке, тому бот не отвечает |
| `OPENCODE_GO_API_KEY` | opencode.ai → войти → Dashboard → API keys. Это мозг менеджера Hermes |

**Очень желательно — иначе часть системы мертва:**

| Переменная | Где взять | Что не работает без него |
|---|---|---|
| `OPENCODE_ZEN_API_KEY` | там же, часто **тот же самый ключ**; пусто → подставится GO | бесплатный тир запасного кодера |
| `GEMINI_API_KEY` | [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) | **долговременная память (mem0) не работает вообще** |
| `GROQ_API_KEY` | [console.groq.com/keys](https://console.groq.com/keys) | голосовые сообщения боту не расшифровываются |
| `NVIDIA_API_KEY` | [build.nvidia.com](https://build.nvidia.com) — нужна верификация по телефону | минус самый широкий бесплатный каталог моделей |
| `MODELSCOPE_API_KEY` | [modelscope.cn/my/myaccesstoken](https://modelscope.cn/my/myaccesstoken) → **потом обязательно** привязать аккаунт Alibaba Cloud на `modelscope.ai/my/settings/account` | 2-й каталог. Без привязки токен валиден, но генерация отвечает 401 — не ищи «битый ключ», причина в непривязанном аккаунте |
| `CLOUDFLARE_API_KEY` | [dash.cloudflare.com/profile/api-tokens](https://dash.cloudflare.com/profile/api-tokens) (Workers AI) | 3-й каталог. Токен `cfat_…` не проходит `/user/tokens/verify` — это нормально, ключ рабочий |
| `OPENROUTER_API_KEY` | [openrouter.ai/keys](https://openrouter.ai/keys) | вне основной ротации, но полезен фолбэком |

**Можно позже:** `TG_API_ID` / `TG_API_HASH` / `TG_PHONE` / `TG_PASSWORD`
([my.telegram.org](https://my.telegram.org) → API development tools) — без них
работает всё, кроме пикера «в какой топик положить форвард».
`GITHUB_PERSONAL_ACCESS_TOKEN`, `POSTGRES_CONNECTION_STRING`, `MAGIC_API_KEY` —
подключают соответствующие MCP-серверы.

**Оставь пустыми** — сгенерируются сами: `MTPROTO_SESSION_KEY`, `CONDUCTOR_BRIDGE_TOKEN`.

---

## ШАГ 1 — установка одной командой

⚠️ **Обязательно смени порты Qdrant.** Это общий VPS: на `sergiy_prod` уже
занят `127.0.0.1:6343/6344`, а установщик берёт их по умолчанию. Без своих портов
твоя память просто не поднимется.

```bash
cd ~/3dlook-marketing/hermes-system
QDRANT_HTTP_PORT=6353 QDRANT_GRPC_PORT=6354 ./install.sh --secrets secrets.env
```

Установщик сам: поставит пакеты, поднимет upstream `hermes-agent`, перепишет все
пути с `sergiy_prod` на `vadim_prod`, разложит и закроет (0600) конфиги, поднимет
Qdrant + OpenCode + systemd-юниты + cron, зарегистрирует Telegram-сессию и
проверит `telegram: connected`. Куда встанет: `/srv/vadim_prod/ai-agents-config`
(изменить — флаг `--dest`).

Полностью без вопросов (для агента): добавь `--yes`. Тогда SMS-код MTProto
получить нельзя — регистрацию сессии сделаешь потом руками.

В конце он напечатает **REMAINING** — список того, что требует живого человека.
Пройди его весь, там обычно 4 пункта:

```bash
sudo npm i -g @anthropic-ai/claude-code && claude    # → /login (подписка Max/Pro; API-ключ НЕ нужен)
curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh | bash -s -- --skip-config
/srv/vadim_prod/ai-agents-config/agents-ai/telegram-bot-agent/claude-code-agent/DEV/switch-profile.sh dev-sm
cp /srv/vadim_prod/ai-agents-config/agents-ai/telegram-bot-agent/hermes-agent/cron/jobs.json.example ~/.hermes/cron/jobs.json  # впиши свой chat_id
```

---

## ШАГ 2 — проверка, что встало

```bash
systemctl --user is-active hermes-gateway hermes-qdrant          # active active
python3 -c "import json,os;print(json.load(open(os.path.expanduser('~/.hermes/gateway_state.json')))['platforms']['telegram']['state'])"
# → connected

curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:6353/collections     # 401 без ключа = Qdrant жив и закрыт
python3 ~/.hermes/model-router/refresh.py --dry-run                            # выбор моделей на день
cd /srv/vadim_prod/ai-agents-config && opencode run 'Reply with exactly: BACKUP-OK'
```

Последняя команда **обязательно внутри git-репозитория** — вне репо `opencode run`
молча выходит с кодом 0. Пустой вывод = одна из трёх причин: нет кредов провайдера
в `~/.local/share/opencode/auth.json`, платная `small_model` в
`~/.config/opencode/opencode.jsonc` (её 401 убивает стрим), запуск вне репо.

Затем напиши своему боту в личку. Он должен показать нижнюю панель:

```
🧑‍💼 Менеджер (Hermes)
⚙️ Исполнитель (Claude, OpenCode)
```

Нажми обе — первая покажет настройки менеджера (совет моделей / одна модель /
learn / journey), вторая — четыре системы. Выбери систему, опиши задачу одним
сообщением — уйдёт в автономный цикл A→Z.

---

## ШАГ 3 — сохрани всё в своей ветке

Ветка `sergiy_config` уже содержит этот кит. Дальше — твой обычный поток:

```bash
cd ~/3dlook-marketing
git checkout -b my-hermes-setup          # или работай прямо в main после мержа PR
# ...правки, которые сделал под себя...
git add -A && git commit -m "hermes-system: настройка под vadim_prod"
git push origin HEAD
```

⚠️ **Не коммить секреты.** `.gitignore` уже блокирует `**/.env`, но
`hermes-system/secrets.env` — файл с токеном бота, api_hash и PAT сразу.
Проверь перед пушем:

```bash
git status --porcelain | grep -i "secrets.env\|config.yaml\|auth.json\|\.session\|\.enc" && echo "СТОП — секрет в индексе"
```

Также перед любым `git add -A` рядом с этим китом убедись, что не затягиваешь
`node_modules` (однажды 238 МБ улетели в ветку и push отклонили):

```bash
git diff --cached --name-only | grep node_modules && echo "СТОП — вычисти node_modules"
```

---

## Грабли, на которые уже наступали

| Симптом | Причина |
|---|---|
| Qdrant не поднимается, память пустая | порты 6343/6344 заняты `sergiy_prod` — задай свои (ШАГ 1) |
| Бот то отвечает, то нет | тот же токен используется вторым процессом. Один токен = один бот |
| `opencode run` печатает пустоту и exit 0 | нет кредов / платная `small_model` / запуск вне git-репо |
| ModelScope: 401 при валидном токене | не привязан аккаунт Alibaba Cloud |
| Cloudflare: `/user/tokens/verify` отказывает | норма для account-scoped токена `cfat_…` |
| Сервисы умирают после выхода из SSH | не включён linger: `loginctl enable-linger vadim_prod` |
| Claude Code «Failed to authenticate / OAuth session expired» | сессия подписки истекла — только `claude` → `/login` руками, само не починится |
| Правки в репо не доезжают до бота | живая копия switcher'а лежит в `~/.hermes/hermes-agent/gateway/`; после правки скопируй туда и `systemctl --user restart hermes-gateway` |

Полная документация: [`README.md`](./README.md) (архитектура + таблица всех
данных) · [`REPRODUCE.md`](./REPRODUCE.md) (пошаговая сборка и проверки).

## Собрать свой ZIP-кит потом

В папке уже лежит готовый архив `ai-agent-bot-ff354b3.zip` (728 КБ, без секретов).
Пересобрать после своих правок:

```bash
cd ~/3dlook-marketing/hermes-system && bash make-release.sh
```
