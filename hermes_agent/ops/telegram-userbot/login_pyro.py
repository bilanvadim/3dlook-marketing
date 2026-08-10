#!/usr/bin/env python3
"""Логин через Pyrogram. Принимает код вторым аргументом."""
import asyncio, os, sys
from pyrogram import Client

async def main():
    phone = sys.argv[1]
    code = sys.argv[2]
    
    client = Client(
        "session_pyro",
        api_id=int(os.environ["TG_API_ID"]),
        api_hash=os.environ["TG_API_HASH"],
    )
    
    await client.connect()
    
    try:
        sent = await client.send_code(phone)
        print(f"Код отправлен через: {sent.type}")
        
        try:
            user = await client.sign_in(phone, sent.phone_code_hash, code)
            print(f"OK! @{user.username} id={user.id}")
        except Exception as e:
            if "PASSWORD" in str(e).upper() or "2FA" in str(e).upper():
                print("Нужен 2FA пароль!")
            else:
                print(f"SIGN_IN ошибка: {type(e).__name__}: {e}")
    except Exception as e:
        print(f"Ошибка: {type(e).__name__}: {e}")
    
    await client.disconnect()

asyncio.run(main())
