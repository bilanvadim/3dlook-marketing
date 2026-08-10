# Установка: ветка `v2` = система Сергея + твоя маркетинговая система

> Это промпт для твоего Claude Code. Открой Claude Code в корне репозитория на
> ветке `v2` и скажи: **«прочитай `ONBOARDING.md` и выполни всё по шагам»**.
> Сначала заполни данные из ШАГА 0 — без них установка встанет на первом шаге.

---

## Что тут собрано

Три слоя системы Сергея:

| Слой | Кто | Что делает |
|---|---|---|
| ① **Hermes Agent** | Telegram-бот (твой) | менеджер: говорит с тобой, помнит контекст, решает, что запускать |
| ② **Conductor** | сервис на libSQL | автономный воркер A→Z: берёт задачу из очереди, ведёт до конца, спрашивает при риске |
| ③ **Claude Code / OpenCode** | «руки» | делает работу агентами и плагинами |

Плюс **твоя система** — целиком, в двух видах:

- `marketing_vb/` — твой проект как есть, байт-в-байт с `main`: `CLAUDE.md`,
  `about-me.md`, `audience.md`, `DESIGN.md`, `QUICKSTART.md`, `brand-assets/`,
  `workspace/`, `docs/`, `runners/`, `telegram-bot/`, `.claude/`.
- `agents-ai/…/DEV/marketing_vb/` — те же 28 агентов и 7 команд, упакованные в
  4 плагина (`mvb-core`, `mvb-social`, `mvb-seo`, `mvb-outbound`), чтобы система
  включалась переключателем профиля.

`marketing_vb_sm` — **строгое надмножество** `marketing_vb`: те же 4 твоих плагина
плюс маркетологи Сергея, база Hermes и мост `/vbsm-campaign`. Исполнение микс
**делегирует твоим точкам входа** (`/new-article`, `/post-from-article`,
`/outbound`, твой `orchestrator`), а не переписывает их у себя — иначе он отстаёт
от твоей системы, как уже отстал один раз: жил на 21 агенте и звал
`/weekly-posts`, который ты давно заменил на `/post-from-article`.

Семь профилей, активен ровно один:

```
dev-sm            код, фичи, деплой                  ← Сергея
seo-sm            SEO-аудит, семантика               ← Сергея
marketing-sm      маркетинг общего профиля           ← Сергея
security-sm       уязвимости, харденинг              ← Сергея
sandbox-sm        стенд для обкатки одного кандидата ← Сергея
marketing_vb      ТВОЯ система, без чужой базы       ← твоя
marketing_vb_sm   МИКС: твоя + маркетологи Сергея    ← общее, вход /vbsm-campaign
```

---

## ШАГ 0 — собери данные (сделай это ПЕРВЫМ)

```bash
cd ~/3dlook-marketing            # на ветке v2
cp secrets.env.example secrets.env && chmod 600 secrets.env
nano secrets.env
```

**Обязательно — без этого установка остановится:**

| Переменная | Что это и где взять |
|---|---|
| `TELEGRAM_BOT_TOKEN` | Токен **своего** бота: [@BotFather](https://t.me/BotFather) → `/newbot` → получишь `8123456789:AAF…`. Можно взять токен уже существующего бота из `marketing_vb/telegram-bot/`. **Не переиспользуй бота Сергея** — один токен = один процесс, иначе оба бота начнут отбирать друг у друга сообщения |
| `TELEGRAM_ALLOWED_USERS` | **Твой** числовой Telegram id: напиши [@userinfobot](https://t.me/userinfobot) → `Id: 123456789`. Это весь whitelist — кого нет в списке, того бот игнорирует |
| `OPENCODE_GO_API_KEY` | opencode.ai → войти → Dashboard → API keys. Это мозг менеджера Hermes |

**Очень желательно — иначе часть системы мертва:**

| Переменная | Где взять | Что не работает без него |
|---|---|---|
| `OPENCODE_ZEN_API_KEY` | там же, часто **тот же ключ**; пусто → подставится GO | бесплатный тир запасного кодера |
| `GEMINI_API_KEY` | [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey) | **долговременная память (mem0) не работает вообще** |
| `GROQ_API_KEY` | [console.groq.com/keys](https://console.groq.com/keys) | голосовые сообщения боту не расшифровываются |
| `NVIDIA_API_KEY` | [build.nvidia.com](https://build.nvidia.com) — нужна верификация по телефону | минус самый широкий бесплатный каталог моделей |
| `MODELSCOPE_API_KEY` | [modelscope.cn/my/myaccesstoken](https://modelscope.cn/my/myaccesstoken), потом **обязательно** привязать аккаунт Alibaba Cloud на `modelscope.ai/my/settings/account` | 2-й каталог. Без привязки токен валиден, но генерация отдаёт 401 — не ищи «битый ключ» |
| `CLOUDFLARE_API_KEY` | [dash.cloudflare.com/profile/api-tokens](https://dash.cloudflare.com/profile/api-tokens) (Workers AI) | 3-й каталог. Токен `cfat_…` не проходит `/user/tokens/verify` — это норма |
| `OPENROUTER_API_KEY` | [openrouter.ai/keys](https://openrouter.ai/keys) | вне основной ротации, но полезен фолбэком |

**Можно позже:** `TG_API_ID` / `TG_API_HASH` / `TG_PHONE` / `TG_PASSWORD`
([my.telegram.org](https://my.telegram.org) → API development tools) — без них
работает всё, кроме пикера «в какой топик положить форвард».
`GITHUB_PERSONAL_ACCESS_TOKEN`, `POSTGRES_CONNECTION_STRING`, `MAGIC_API_KEY` —
включают соответствующие MCP-серверы.

**Оставь пустыми** — сгенерируются сами: `MTPROTO_SESSION_KEY`, `CONDUCTOR_BRIDGE_TOKEN`.

---

## ШАГ 1 — установка одной командой

⚠️ **Обязательно смени порты Qdrant.** VPS общий: на `sergiy_prod` уже занято
`127.0.0.1:6343/6344`, а установщик берёт их по умолчанию — без своих портов
твоя память просто не поднимется.

```bash
cd ~/3dlook-marketing
QDRANT_HTTP_PORT=6353 QDRANT_GRPC_PORT=6354 ./install.sh --secrets secrets.env \
  --owner "Vadim" --gh-owner bilanvadim
```

Про эти два флага: в системе есть файлы, которые агент читает **как инструкции** —
`SOUL.md` («менеджер владельца», «наружу от лица владельца — ничего») и скилл
`vps-orchestration` («мёрж — решение владельца», «новый репо → `gh repo create
<аккаунт>/<name>`»). В ките там стоят токены `@OWNER@` / `@GH_OWNER@`, установщик
подставляет твои значения. Без флагов он возьмёт их из `gh api user` — если ты уже
залогинен как `bilanvadim`, можно не указывать. Проверить после установки:

```bash
grep -m1 оркестратор ~/.hermes/SOUL.md        # → «владельца этого VPS (Vadim)»
grep -m1 "gh repo create" /srv/vadim_prod/ai-agents-config/agents-ai/telegram-bot-agent/hermes-agent/skills/vps-orchestration/SKILL.md
```

**Корень проектов** установщик определяет сам: видит `marketing_vb/` рядом с китом
→ берёт папку репозитория. Переопределить — `--project-root <путь>`. От него зависят
`runFrom` профилей и дефолтная папка задач, так что мимо — и профили загрузятся, но
ничего не увидят.

Установщик сам: поставит пакеты, поднимет upstream `hermes-agent`, перепишет все
пути и имя аккаунта с `sergiy_prod` на `vadim_prod`, разложит и закроет (0600)
конфиги, поднимет Qdrant + OpenCode + systemd + cron, зарегистрирует
Telegram-сессию и проверит `telegram: connected`.

Куда встанет система: `/srv/vadim_prod/ai-agents-config` (меняется флагом
`--dest`). Твой контент остаётся жить здесь, в репозитории.

В конце он напечатает **REMAINING** — то, что требует живого человека:

```bash
sudo npm i -g @anthropic-ai/claude-code && claude    # → /login (подписка Max/Pro; API-ключ НЕ нужен)
curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh | bash -s -- --skip-config
cp /srv/vadim_prod/ai-agents-config/agents-ai/telegram-bot-agent/hermes-agent/cron/jobs.json.example ~/.hermes/cron/jobs.json   # впиши свой chat_id
```

## ШАГ 2 — включи свою систему

```bash
cd /srv/vadim_prod/ai-agents-config/agents-ai/telegram-bot-agent/claude-code-agent/DEV
./switch-profile.sh --list                 # покажет все 7 и активный
./switch-profile.sh marketing_vb_sm        # микс: твои команды + маркетологи Сергея
# или ./switch-profile.sh marketing_vb     # только твоя система, без чужой базы
```

Переключатель сам скажет, откуда запускаться, и запишет это для бота:

```
runFrom: /home/vadim_prod/3dlook-marketing/marketing_vb  (recorded → ~/.claude/.active-profile-cwd)
→  Start it from there:  cd /home/vadim_prod/3dlook-marketing/marketing_vb && claude
```

Этот файл читает Telegram-switcher: вкладка без явного `/cwd` теперь по умолчанию
уезжает **в папку активного профиля**, а не в общий корень проектов. Если папки нет
— переключатель громко предупредит и не станет врать, что всё в порядке.

Затем **перезапусти Claude Code** — плагины грузятся только при старте сессии.

⚠️ И запускай Claude Code **из папки `marketing_vb/`**:

```bash
cd ~/3dlook-marketing/marketing_vb && claude
```

Твои агенты читают `brand-assets/`, `workspace/`, `about-me.md`, `CLAUDE.md`
относительными путями — они резолвятся от рабочей папки сессии, а не от места
плагина. Из корня репо агенты не увидят ни бренд-контекст, ни прошлые посты.

## ШАГ 3 — проверка

```bash
systemctl --user is-active hermes-gateway hermes-qdrant          # active active
python3 -c "import json,os;print(json.load(open(os.path.expanduser('~/.hermes/gateway_state.json')))['platforms']['telegram']['state'])"
# → connected
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:6353/collections   # 401 без ключа = Qdrant жив и закрыт
python3 ~/.hermes/model-router/refresh.py --dry-run             # выбор моделей на день
cd /srv/vadim_prod/ai-agents-config && opencode run 'Reply with exactly: BACKUP-OK'
```

`opencode run` — **только внутри git-репозитория**: вне репо он молча выходит с
кодом 0. Пустой вывод = нет кредов провайдера в
`~/.local/share/opencode/auth.json`, либо платная `small_model` в
`~/.config/opencode/opencode.jsonc` (её 401 убивает стрим), либо запуск вне репо.

Проверка твоей системы после переключения профиля:

```bash
cd ~/3dlook-marketing/marketing_vb && claude
# в сессии: /qc     и    /weekly-posts   — должны найтись, как и раньше
```

Затем напиши своему боту в личку. Он покажет нижнюю панель:

```
🧑‍💼 Менеджер (Hermes)
⚙️ Исполнитель (Claude, OpenCode)
```

## ШАГ 4 — работай в своей ветке

```bash
cd ~/3dlook-marketing && git checkout v2
# ...правки под себя...
git add -A && git commit -m "v2: настройка под vadim_prod"
git push origin v2
```

Перед пушем проверь, что не тащишь секрет или мусор:

```bash
git status --porcelain | grep -iE "secrets\.env|config\.yaml|auth\.json|\.session|\.enc|\.db$" && echo "СТОП — секрет/состояние в индексе"
git diff --cached --name-only | grep node_modules && echo "СТОП — вычисти node_modules"
```

`.gitignore` в ветке это уже блокирует, но проверка стоит одну секунду.

---

## Если менял агентов — синхронизируй плагины

Плагины `agents-ai/…/DEV/marketing_vb/plugins/mvb-*` — это **копии** твоих файлов
из `marketing_vb/.claude/`. Правишь агента у себя — обнови копию, иначе профиль
поедет на старой версии (именно так и разошлось: в июле было 21 агент, сейчас 28).

```bash
cd ~/3dlook-marketing
SRC=marketing_vb/.claude
DST=agents-ai/telegram-bot-agent/claude-code-agent/DEV/marketing_vb/plugins
for p in mvb-core mvb-social mvb-seo mvb-outbound; do rm -rf $DST/$p/agents; mkdir -p $DST/$p/agents; done
rm -rf $DST/mvb-core/commands && mkdir -p $DST/mvb-core/commands
cp $SRC/agents/_shared/*.md  $DST/mvb-core/agents/
cp $SRC/agents/social/*.md   $DST/mvb-social/agents/
cp $SRC/agents/seo/*.md      $DST/mvb-seo/agents/
cp $SRC/agents/outbound/*.md $DST/mvb-outbound/agents/
cp $SRC/agents/*.md          $DST/mvb-seo/agents/     # writers, что лежат в корне agents/
cp $SRC/commands/*.md        $DST/mvb-core/commands/
```

Заметка: у тебя `brand-checker` существует дважды с **разным** содержимым —
`_shared/` (проверка бренда, русский) и `social/` (проверка поста, украинский).
В одной папке `.claude/agents/` они конфликтуют по имени, а как плагины
разъезжаются в `mvb-core:brand-checker` и `mvb-social:brand-checker`. Оба
сохранены.

---

## Грабли, на которые уже наступали

| Симптом | Причина |
|---|---|
| Твои агенты не видят бренд-контекст | Claude Code запущен не из `marketing_vb/` |
| Qdrant не поднимается, память пустая | порты 6343/6344 заняты `sergiy_prod` — задай свои |
| Бот то отвечает, то нет | тот же токен используется вторым процессом |
| `opencode run` печатает пустоту и exit 0 | нет кредов / платная `small_model` / запуск вне git-репо |
| ModelScope: 401 при валидном токене | не привязан аккаунт Alibaba Cloud |
| Cloudflare: `/user/tokens/verify` отказывает | норма для account-scoped токена `cfat_…` |
| Сервисы умирают после выхода из SSH | `loginctl enable-linger vadim_prod` |
| Claude Code «OAuth session expired» | только `claude` → `/login` руками, само не починится |
| Заголовки сессий не генерируются (401 CreditsError) | титловка уходила на платную модель; в `config.yaml.example` уже прибита бесплатная — если правил конфиг руками, сверься с шаблоном |
| Правки в репо не доезжают до бота | живая копия switcher'а в `~/.hermes/hermes-agent/gateway/` — скопируй туда и `systemctl --user restart hermes-gateway` |

Полная документация: [`README.md`](./README.md) (архитектура + таблица ключей) ·
[`REPRODUCE.md`](./REPRODUCE.md) (пошаговая сборка) ·
[`agents-ai/…/DEV/SYSTEMS.md`](./agents-ai/telegram-bot-agent/claude-code-agent/DEV/SYSTEMS.md)
(все 7 профилей) · `marketing_vb/README.md` и `QUICKSTART.md` (твоя система, не тронуты).
