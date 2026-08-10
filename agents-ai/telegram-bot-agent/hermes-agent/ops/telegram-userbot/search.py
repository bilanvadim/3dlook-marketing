#!/usr/bin/env python3
"""
Поиск по всем чатам/каналам/топикам Telegram через userbot.
Использование: python3 search.py "запрос" [--limit 20] [--chat "название"]
"""
import argparse
import asyncio
import os
import sys
from telethon import TelegramClient
from telethon.tl.functions.messages import SearchGlobalRequest
from telethon.tl.types import InputMessagesFilterEmpty

SESSION_FILE = os.path.join(os.path.dirname(__file__), "session")
API_ID = int(os.environ["TG_API_ID"])
API_HASH = os.environ["TG_API_HASH"]


async def search_all(client, query, limit=20):
    """Поиск по всем диалогам."""
    results = []
    async for msg in client.iter_messages(None, search=query, limit=limit):
        chat = await msg.get_chat()
        chat_name = getattr(chat, "title", None) or getattr(chat, "first_name", None) or str(chat.id)
        results.append({
            "chat": str(chat_name),
            "chat_id": msg.chat_id,
            "msg_id": msg.id,
            "date": str(msg.date),
            "sender": getattr(msg.sender, "first_name", "?") if msg.sender else "?",
            "text": msg.text[:300] if msg.text else "[не текст]",
        })
    return results


async def search_global(client, query, limit=20):
    """Глобальный поиск (включая публичные каналы вне подписок)."""
    results = []
    try:
        resp = await client(SearchGlobalRequest(
            q=query,
            filter=InputMessagesFilterEmpty(),
            min_date=None,
            max_date=None,
            offset_rate=0,
            offset_peer=None,
            offset_id=0,
            limit=limit,
        ))
        for msg in resp.messages:
            chat = None
            try:
                chat = await client.get_entity(msg.peer_id)
            except Exception:
                pass
            chat_name = getattr(chat, "title", None) or str(msg.peer_id)
            results.append({
                "chat": chat_name,
                "msg_id": msg.id,
                "date": str(msg.date),
                "text": msg.message[:300] if msg.message else "[не текст]",
            })
    except Exception as e:
        print(f"Глобальный поиск не удался: {e}", file=sys.stderr)
    return results


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="Поисковый запрос")
    parser.add_argument("--limit", type=int, default=20, help="Макс. результатов (default: 20)")
    parser.add_argument("--global", dest="global_search", action="store_true", help="Глобальный поиск (публичные каналы)")
    parser.add_argument("--chat", help="Искать только в конкретном чате (название или ID)")
    args = parser.parse_args()

    client = TelegramClient(SESSION_FILE, API_ID, API_HASH)
    await client.start()

    # Если указан конкретный чат — ищем в нём
    if args.chat:
        try:
            entity = await client.get_entity(args.chat)
        except Exception as e:
            print(f"Чат не найден: {e}")
            await client.disconnect()
            sys.exit(1)

        results = []
        async for msg in client.iter_messages(entity, search=args.query, limit=args.limit):
            results.append({
                "chat": args.chat,
                "msg_id": msg.id,
                "date": str(msg.date),
                "text": msg.text[:300] if msg.text else "[не текст]",
            })
    elif args.global_search:
        results = await search_global(client, args.query, args.limit)
    else:
        results = await search_all(client, args.query, args.limit)

    await client.disconnect()

    # Вывод результатов
    if not results:
        print("Ничего не найдено.")
        sys.exit(0)

    for i, r in enumerate(results, 1):
        print(f"{i}. [{r['chat']}] {r['date']}")
        print(f"   {r['text']}")
        print(f"   t.me/c/{r.get('chat_id','')}/{r['msg_id']}" if r.get('chat_id') else f"   msg_id={r['msg_id']}")
        print()


if __name__ == "__main__":
    asyncio.run(main())
