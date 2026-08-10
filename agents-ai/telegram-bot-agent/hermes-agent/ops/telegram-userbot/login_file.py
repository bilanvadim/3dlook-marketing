#!/usr/bin/env python3
"""Логин через Telethon с SMS (не App) — чтобы код не инвалидировался при пересылке.

Headless-friendly: запускается на VPS, отправляет запрос кода по SMS, затем ждёт,
пока код появится в файле code.txt (рядом со скриптом). Так код можно переслать
себе в Telegram и просто вписать в файл — сессия не инвалидируется пересылкой.

Требует переменные окружения (см. .env.example): TG_API_ID, TG_API_HASH, TG_PHONE.
"""
import asyncio, os, sys, time
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

CODE_FILE = os.path.join(os.path.dirname(__file__), "code.txt")

async def main():
    phone = os.environ["TG_PHONE"]  # e.g. +3370000000 — set in .env, never hardcode

    client = TelegramClient('session', int(os.environ['TG_API_ID']), os.environ['TG_API_HASH'])
    await client.connect()

    # force_sms=True — код придёт по SMS, его можно пересылать
    sent = await client.send_code_request(phone, force_sms=True)
    print(f"CODE_SENT|type={sent.type}|hash={sent.phone_code_hash}")

    if os.path.exists(CODE_FILE):
        os.remove(CODE_FILE)

    print("WAITING_FOR_CODE_FILE ...")
    timeout = 180
    start = time.time()
    while not os.path.exists(CODE_FILE):
        if time.time() - start > timeout:
            print("TIMEOUT")
            await client.disconnect()
            sys.exit(1)
        await asyncio.sleep(0.5)

    with open(CODE_FILE) as f:
        code = f.read().strip()
    os.remove(CODE_FILE)

    print(f"GOT_CODE: {code}")

    try:
        await client.sign_in(phone, code, phone_code_hash=sent.phone_code_hash)
    except SessionPasswordNeededError:
        print("NEED_2FA")
        await client.disconnect()
        sys.exit(2)
    except Exception as e:
        print(f"SIGN_IN_FAIL: {type(e).__name__}: {e}")
        await client.disconnect()
        sys.exit(3)

    me = await client.get_me()
    print(f"OK! @{me.username} id={me.id}")
    await client.disconnect()

asyncio.run(main())
