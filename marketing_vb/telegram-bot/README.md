# Telegram Bot

Single bot, three tracks. Ground truth — файлы в `/workspace/`. Telegram — только UI.

## Что делает

1. **Notify Vadim** — когда какой-то агент написал артефакт, готовый на ревью, runner вызывает `notify.py`, который шлёт в Telegram сообщение с кнопками Approve / Edit / Reject.
2. **Capture decision** — когда Вадим тапает кнопку, бот пишет `feedback.md` рядом с артефактом и обновляет `*.status.json`.
3. **Show pending** — `/pending` показывает все артефакты, ждущие ревью, через все треки.
4. **Show status** — `/status` — высокоуровневый снэпшот.

## Установка

### 1. Создать бота через @BotFather
Получить `TELEGRAM_BOT_TOKEN`.

### 2. Узнать свой `chat_id`
Написать `@userinfobot` в Telegram.

### 3. Заполнить `.env`
```
TELEGRAM_BOT_TOKEN=xxx
ALLOWED_CHAT_IDS=123456789
WORKSPACE_ROOT=/абсолютный/путь/до/marketing-claude-code/workspace
LOG_DIR=/var/log/marketing-bot
```

### 4. Установить deps
```bash
cd telegram-bot
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 5. Запустить бота как сервис

`systemd` unit (рекомендованно):

```ini
# /etc/systemd/system/marketing-bot.service
[Unit]
Description=Marketing Automation Telegram Bot
After=network.target

[Service]
Type=simple
User=vadim
WorkingDirectory=/home/vadim/marketing-claude-code/telegram-bot
EnvironmentFile=/home/vadim/marketing-claude-code/telegram-bot/.env
ExecStart=/home/vadim/marketing-claude-code/telegram-bot/.venv/bin/python bot.py
Restart=on-failure
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable marketing-bot
sudo systemctl start marketing-bot
sudo systemctl status marketing-bot
```

## Как агенты пингуют бота

Агент или slash-command runner после записи артефакта делает:

```bash
python /path/to/telegram-bot/notify.py \
  --track social \
  --artifact "social/2026-W17/linkedin-company/post-1.md" \
  --summary-file /tmp/agent-summary.txt
```

Это:
- Создаёт `post-1.status.json` с `status=awaiting_review`
- Отправляет уведомление в Telegram с кнопками

## Что Вадим видит в Telegram

```
🔔 SOCIAL — review needed
social/2026-W17/linkedin-company/post-1.md

[краткий саммари что в файле — 1-2 параграфа]

[✅ Approve] [✏️ Edit] [❌ Reject]
```

При тапе:
- **Approve** → `feedback.md` ← `APPROVED`, статус → `approved`. Следующий агент в пайплайне может стартовать.
- **Edit** → бот ждёт текст комментария → пишет в `feedback.md`, статус → `edit_requested`. Агент при следующем запуске читает feedback и переделывает.
- **Reject** → `feedback.md` ← `REJECTED`, пайплайн останавливается. Никаких авто-повторов.

## Безопасность

- **Whitelist по `chat_id`.** Любые сообщения от других chat_id игнорируются.
- **Никаких прав постить в соцсети.** Бот не имеет токенов LinkedIn/FB/IG. Только подготовка артефактов + уведомления.
- **Никаких прав запускать кампании.** Closely.io, email-рассылки — Вадим стартует руками.
- **Read-only с точки зрения публикаций.** Единственное, что бот пишет — `feedback.md` и `*.status.json` в workspace.

## Что НЕ нужно делать

- Не делать веб-интерфейс ради веб-интерфейса. Telegram + файлы покрывают 95% потребностей.
- Не давать боту прямой доступ к LinkedIn API. Технически возможно, но любой сбой = публичная катастрофа.
- Не хранить апрувленные посты только в Telegram. Ground truth = файлы.

## Стоимость

При активном использовании Claude API через Claude Code:
- Sonnet ~ $0.003/1K input + $0.015/1K output
- Средний пост ~ 2K input + 1K output → ~$0.02/пост
- Полная неделя (8 постов на 8 профилей × 2 варианта) ~ $0.50
- SEO-статья 2000 слов через весь пайплайн ~ $5-10
- Outbound кампания 30 человек × 4 сообщения ~ $3-5

Резерв: $40-100/мес на правки и итерации.
