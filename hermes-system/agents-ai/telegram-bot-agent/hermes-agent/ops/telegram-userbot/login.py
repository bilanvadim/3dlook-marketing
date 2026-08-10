#!/usr/bin/env python3
"""Логин: python3 login.py +00000000000 12345 [2fa_пароль]"""
import asyncio, os, sys
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

async def main():
    phone = sys.argv[1]
    code = sys.argv[2]
    password = sys.argv[3] if len(sys.argv) > 3 else None

    client = TelegramClient('session', int(os.environ['TG_API_ID']), os.environ['TG_API_HASH'])
    await client.connect()

    try:
        sent = await client.send_code_request(phone)
        print(f"Тип доставки: {sent.type}, hash={sent.phone_code_hash[:8]}...")

        try:
            result = await client.sign_in(phone, code, phone_code_hash=sent.phone_code_hash)
            print(f"SIGN_IN result: {result}")
        except SessionPasswordNeededError:
            if not password:
                print("Нужен 2FA пароль! Третий аргумент: python3 login.py +33... КОД ПАРОЛЬ")
                await client.disconnect()
                sys.exit(2)
            await client.sign_in(password=password)

        me = await client.get_me()
        print(f"OK! @{me.username} id={me.id}")

    except Exception as e:
        print(f"ОШИБКА: {type(e).__name__}: {e}")
        raise

    await client.disconnect()

asyncio.run(main())
