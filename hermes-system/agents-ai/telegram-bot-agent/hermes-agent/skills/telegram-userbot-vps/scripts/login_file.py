#!/usr/bin/env python3
"""
Логин с чтением кода из файла code.txt (Telethon).
Использование: запустить скрипт, он отправит код в Telegram,
затем ждёт появления code.txt в той же директории.
"""
import asyncio, os, sys, time
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

CODE_FILE = os.path.join(os.path.dirname(__file__), "code.txt")
PHONE = '+00000000000'

async def main():
    client = TelegramClient('session', int(os.environ['TG_API_ID']), os.environ['TG_API_HASH'])
    await client.connect()
    
    # force_sms=True — deprecated, не работает
    sent = await client.send_code_request(PHONE)
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
        await client.sign_in(PHONE, code, phone_code_hash=sent.phone_code_hash)
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
