#!/usr/bin/env python3
"""MV-Link MTProto bridge — list the LIVE forum topics of the user's chat with
the Ivan Djedaev bot, so the forward-picker only ever offers topics that still
exist (Telegram's Bot API cannot tell a bot that a topic was deleted/closed; the
user's own MTProto session can, via messages.GetForumTopics).

Read-only. Connects on demand, fetches once, writes an atomic JSON cache, and
disconnects. The session string (== the account) is Fernet-encrypted at rest and
only decrypted in memory here; it is never printed. Prints a small JSON summary
to stdout and exits 0 on success, non-zero on failure (without clobbering a good
cache).

Usage: python list_topics.py [bot_username_or_id]
"""
from __future__ import annotations
import asyncio
import json
import os
import sys
import time

MT_DIR = os.path.dirname(os.path.abspath(__file__))
CREDS = os.path.expanduser("~/.hermes/mtproto/creds.env")
SESSION_ENC = os.path.expanduser("~/.hermes/mtproto/session.enc")
CACHE = os.path.expanduser("~/.hermes/mtproto-topics.json")
BOT = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("MT_BOT", "ivan_djedaev_bot")
CONNECT_TIMEOUT = 20


def _load_creds() -> dict:
    d = {}
    with open(CREDS) as f:
        for ln in f:
            ln = ln.strip()
            if "=" in ln and not ln.startswith("#"):
                k, v = ln.split("=", 1)
                d[k.strip()] = v.strip()
    return d


def _fail(msg: str) -> None:
    print(json.dumps({"ok": False, "error": msg}))
    sys.exit(1)


async def _run() -> None:
    creds = _load_creds()
    from cryptography.fernet import Fernet
    from telethon import TelegramClient
    from telethon.sessions import StringSession
    from telethon.tl.functions.messages import GetForumTopicsRequest

    try:
        session = Fernet(creds["MTPROTO_SESSION_KEY"].encode()).decrypt(
            open(SESSION_ENC, "rb").read()
        ).decode()
    except Exception as e:  # noqa: BLE001
        _fail(f"session decrypt failed: {e!r}")

    client = TelegramClient(StringSession(session), int(creds["TG_API_ID"]),
                            creds["TG_API_HASH"])
    try:
        await asyncio.wait_for(client.connect(), CONNECT_TIMEOUT)
    except Exception as e:  # noqa: BLE001
        _fail(f"connect failed: {e!r}")
    try:
        if not await client.is_user_authorized():
            _fail("session not authorized")
        bot = await client.get_entity(int(BOT) if str(BOT).isdigit() else BOT)
        res = await client(GetForumTopicsRequest(
            peer=bot, offset_date=0, offset_id=0, offset_topic=0, limit=200, q=None))
        topics = {}
        for t in getattr(res, "topics", []):
            tid = getattr(t, "id", None)
            if tid is None:
                continue
            # Skip the built-in General topic (id 1) — it is the lobby, never a
            # forward destination.
            if int(tid) == 1:
                continue
            topics[str(tid)] = {
                "title": getattr(t, "title", None),
                "closed": bool(getattr(t, "closed", False)),
                "hidden": bool(getattr(t, "hidden", False)),
                "top_message": getattr(t, "top_message", None),
            }
        payload = {
            "ok": True,
            "fetched_at": int(time.time()),
            "bot": str(BOT),
            "topics": topics,
        }
        tmp = CACHE + ".tmp"
        os.makedirs(os.path.dirname(CACHE), exist_ok=True)
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False)
        os.replace(tmp, CACHE)
        print(json.dumps({"ok": True, "count": len(topics),
                          "ids": sorted(topics, key=int)}))
    finally:
        try:
            await client.disconnect()
        except Exception:  # noqa: BLE001
            pass


if __name__ == "__main__":
    try:
        asyncio.run(_run())
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001
        _fail(f"unexpected: {e!r}")
