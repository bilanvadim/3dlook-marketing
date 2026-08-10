---
name: telegram-userbot-vps
description: "Telegram userbot on VPS: auth, anti-phishing, search."
version: 0.1.0
metadata:
  hermes:
    tags: [Telegram, Userbot, Telethon, Pyrogram, Search, VPS]
---

# Telegram Userbot на VPS

Настройка и использование Telegram userbot (MTProto-клиента) на VPS для поиска по всем чатам, каналам и топикам пользователя.

## Установка

```bash
pip3 install telethon pyrogram tgcrypto
```

Скрипты лежат в `~/.hermes/telegram-userbot/`:
- `login_file.py` — интерактивный логин с чтением кода из файла
- `search.py` — поиск по чатам (Telethon)
- `search.sh` — враппер для поиска
- `.env` — api_id и api_hash

## Креды

Нужны `api_id` и `api_hash` с https://my.telegram.org/apps. Хранятся в `~/.hermes/telegram-userbot/.env`:
```
TG_API_ID=число
TG_API_HASH=32-символьный_hex
```

## Главный подводный камень: антифишинг-защита Telegram

**Коды подтверждения, пересланные в Telegram-чате, автоматически инвалидируются.**

Telegram (с 2024+) блокирует `sign_in` если код был отправлен через `SentCodeTypeApp` (в приложение) и затем скопирован/переслан в другой чат. Сервер возвращает `PhoneCodeExpiredError`, хотя код правильный. Telegram явно предупреждает:
> "The code was entered correctly, but sign in was not allowed, because this code was previously shared."

### Обходные пути (в порядке предпочтения)

1. **QR-логин** (`client.qr_login()` в Telethon) — не требует кода. Генерирует ссылку `tg://login?token=...`, пользователь открывает её в Telegram и подтверждает. **Проблема:** таймаут ~45 секунд, нужно действовать быстро.

2. **Облачный пароль (2FA)** — если настроен, можно войти с кодом + паролем. Код всё равно нужен, но с паролем проверка на "shared" может пропускаться (не подтверждено).

3. **SMS вместо приложения** — `force_sms=True` в Telethon. **DEPRECATED**, больше не работает.

4. **Код через другой канал** — если код передан не через Telegram-чат (голосом, через SMS на телефон VPS, через другого мессенджера), антифишинг не срабатывает.

## Техника: передача кода через файл

Проблема: `process submit` через pty искажает ввод в `input()`. 
Решение: скрипт ждёт появления файла `code.txt`, читает код оттуда.

```python
# В скрипте:
while not os.path.exists(CODE_FILE):
    await asyncio.sleep(0.5)
with open(CODE_FILE) as f:
    code = f.read().strip()
```

Агент пишет код в файл через `write_file`, скрипт подхватывает — без проблем с pty.

## Поиск по чатам

После успешного логина (файл сессии `session.session` создан):

```bash
cd ~/.hermes/telegram-userbot
source .env
python3 search.py "запрос" --limit 20           # поиск по всем своим чатам
python3 search.py "запрос" --global --limit 20   # глобальный поиск по публичным каналам
python3 search.py "запрос" --chat "название"     # поиск в конкретном чате
```

## Поиск по публичному Телеграму (без userbot)

Для каналов, куда пользователь не вступил:
- Google: `site:t.me "запрос"`
- Telegago (веб-поисковик по Telegram)
- Tgstat API (платный)

## Текущее состояние

- [x] Telethon 1.44.0 установлен
- [x] Pyrogram 2.0.106 установлен
- [x] api_id/api_hash сохранены в `.env`
- [x] Скрипт поиска готов (`search.py`)
- [ ] Логин НЕ завершён — антифишинг блокирует коды из чата
- [ ] QR-логин: истекает по таймауту
- [ ] Облачный пароль: получен, ждёт кода для проверки

## Библиотеки

| Библиотека | Версия | Статус |
|---|---|---|
| telethon | 1.44.0 | установлен |
| pyrogram | 2.0.106 | установлен |
| tgcrypto | 1.2.5 | установлен |
| python-telegram-bot | 22.6 | установлен (Bot API, не для userbot) |
