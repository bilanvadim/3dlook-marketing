#!/usr/bin/env python3
"""
QR-логин в Telegram (Telethon) — БЕЗ кода из приложения.

Почему QR, а не код:
  Telegram включил антифишинг: любой код, который «засветился» в чате аккаунта
  (переслан/скопирован/виден боту), инвалидируется -> PhoneCodeExpiredError и
  уведомление "this code was previously shared by your account".
  QR-логин вообще не использует код: сервер получает login-token, показывает QR,
  вы сканируете его уже авторизованным телефоном (Настройки -> Устройства ->
  Подключить устройство). Облачный пароль (2FA) подставляется автоматически.

Особенность: QR-токен живёт ~30 сек. Скрипт крутит цикл и САМ пересоздаёт токен,
перерисовывая QR, пока вы не отсканируете. Успеть можно с любой попытки.

Запуск:
    export $(grep -v '^#' .env | xargs)   # или скрипт сам прочитает .env
    python3 qr_login.py

Как отсканировать (на телефоне, где Telegram уже залогинен под +00000000000):
    Настройки -> Устройства -> Подключить устройство -> навести камеру на QR.
"""
import asyncio
import os
import sys

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

import qrcode

HERE = os.path.dirname(os.path.abspath(__file__))
SESSION = os.path.join(HERE, "session")   # то же имя сессии, что и в search.py
QR_PNG = os.path.join(HERE, "qr.png")
ENV_FILE = os.path.join(HERE, ".env")

# --- загрузка .env без внешних зависимостей ---
def load_env():
    if not os.path.exists(ENV_FILE):
        return
    with open(ENV_FILE) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())

load_env()

API_ID = int(os.environ["TG_API_ID"])
API_HASH = os.environ["TG_API_HASH"]
PASSWORD = os.environ.get("TG_PASSWORD")  # облачный 2FA-пароль


def render_qr(url: str, attempt: int):
    """Рисуем QR половинными блоками (квадратные модули, узкий — влезает в 80 колонок)
    + сохраняем PNG (qr.png) как запасной вариант."""
    # ERROR_CORRECT_L -> меньше модулей -> QR уже по ширине, не переносится в терминале
    qr = qrcode.QRCode(border=2, error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(url)
    qr.make(fit=True)

    print("\n" + "=" * 60, flush=True)
    print(f"  QR #{attempt}  —  на телефоне: Настройки → Устройства →", flush=True)
    print("             Подключить устройство → навести камеру ниже", flush=True)
    print("=" * 60, flush=True)
    # print_ascii: половинные блоки, 1 символ на модуль по ширине, квадратный QR
    qr.print_ascii(out=sys.stdout, invert=True)
    sys.stdout.flush()
    print("=" * 60, flush=True)
    print(f"  Не сканируется с экрана? PNG сохранён: {QR_PNG}", flush=True)
    print(f"  Или вбей ссылку в любой генератор QR: {url}", flush=True)
    print("=" * 60 + "\n", flush=True)

    try:
        qrcode.make(url).save(QR_PNG)
    except Exception as e:
        print(f"(PNG не сохранён: {e})", flush=True)


async def main():
    client = TelegramClient(SESSION, API_ID, API_HASH)
    await client.connect()

    if await client.is_user_authorized():
        me = await client.get_me()
        print(f"Уже авторизованы: @{me.username} id={me.id} — ничего делать не нужно.", flush=True)
        await client.disconnect()
        return

    qr_login = await client.qr_login()
    attempt = 1
    render_qr(qr_login.url, attempt)

    while True:
        try:
            # ждём скан; при таймауте пересоздаём токен и перерисовываем QR
            await qr_login.wait(timeout=28)
            break  # отсканировано, 2FA не требуется
        except asyncio.TimeoutError:
            attempt += 1
            await qr_login.recreate()
            render_qr(qr_login.url, attempt)
        except SessionPasswordNeededError:
            # QR отсканирован, аккаунт под облачным паролём
            if not PASSWORD:
                print("QR принят, но нужен 2FA-пароль. Добавьте TG_PASSWORD в .env.", flush=True)
                await client.disconnect()
                sys.exit(2)
            print("QR принят ✅  Вводим облачный пароль (2FA)...", flush=True)
            await client.sign_in(password=PASSWORD)
            break

    me = await client.get_me()
    print("\n" + "#" * 72, flush=True)
    print(f"  УСПЕХ! Вошли как @{me.username}  (id={me.id}, {me.first_name})", flush=True)
    print(f"  Сессия сохранена: {SESSION}.session", flush=True)
    print(f"  Теперь работает:  python3 search.py \"запрос\"", flush=True)
    print("#" * 72, flush=True)

    # чистим временный QR-png
    try:
        if os.path.exists(QR_PNG):
            os.remove(QR_PNG)
    except Exception:
        pass

    await client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
