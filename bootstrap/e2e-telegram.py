#!/usr/bin/env python3
"""e2e-telegram.py — send a message to the Hermes bot AS VADIM and read the reply.

WHY NOT PLAYWRIGHT + TELEGRAM WEB
---------------------------------
Driving Telegram Web proves the browser can talk to Telegram, then hopes the rest
follows. This sends the message through Telegram's own API from Vadim's account,
so the bot receives something byte-identical to a real message — the same update,
the same chat, the same session key. It needs no login flow, no browser, and it
cannot pass for the wrong reason (a UI that rendered but never delivered).

It uses the ALREADY-ENROLLED MTProto session at ~/.hermes/mtproto/session.enc,
decrypted with MTPROTO_SESSION_KEY. If that session is ever revoked, re-enrol with
~/.hermes/mtproto/enroll.sh — that step is interactive by nature (Telegram sends a
login code) and no script should pretend otherwise.

WHAT COUNTS AS A PASS
---------------------
"The bot replied" is not a pass. A manager that answers from memory replies just as
fast as one that actually reached Claude Code. So a test that means to prove the
full chain asks for something only the far end can know — the marker inside
workspace/_e2e/fixture.md — and --expect fails the test unless that exact string
comes back.

USAGE
    e2e-telegram.py --send "text" [--expect STRING] [--timeout 180] [--label NAME]
    e2e-telegram.py --send "a" --send "b"        # concurrency: sent together
Exit: 0 pass · 1 fail (no reply, or --expect missing) · 3 setup broken.
"""
from __future__ import annotations

import argparse
import asyncio
import os
import sys
import time

CREDS = os.path.expanduser("~/.hermes/mtproto/creds.env")
SESSION_ENC = os.path.expanduser("~/.hermes/mtproto/session.enc")
BOT = "dlookmarketing_bot"


def load_creds() -> None:
    """creds.env is a plain KEY=VALUE file, 0600. Only fills what is not already set."""
    try:
        for line in open(CREDS, encoding="utf-8"):
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip("\"'"))
    except OSError:
        sys.exit(f"⚠️ cannot read {CREDS}")


async def run(args) -> int:
    from telethon import TelegramClient
    from telethon.sessions import StringSession
    from cryptography.fernet import Fernet

    try:
        raw = open(SESSION_ENC, "rb").read()
        sess = Fernet(os.environ["MTPROTO_SESSION_KEY"].encode()).decrypt(raw).decode()
    except KeyError:
        sys.exit("⚠️ MTPROTO_SESSION_KEY missing")
    except Exception as e:
        sys.exit(f"⚠️ cannot decrypt session.enc: {type(e).__name__}")

    client = TelegramClient(StringSession(sess), int(os.environ["TG_API_ID"]),
                            os.environ["TG_API_HASH"])
    await client.connect()
    if not await client.is_user_authorized():
        sys.exit("⚠️ MTProto session revoked — re-enrol: ~/.hermes/mtproto/enroll.sh")

    me = await client.get_me()
    bot = await client.get_entity(BOT)
    label = args.label or "e2e"
    print(f"[{label}] as {me.first_name} (@{me.username}) → @{BOT}")

    # Baseline: only messages the bot sends AFTER this point count as the answer.
    # Without it a stale reply still sitting in the dialog passes the test for free.
    since = int(time.time())
    sent_ids = []
    for text in args.send:
        m = await client.send_message(bot, text)
        sent_ids.append(m.id)
        print(f"[{label}] sent #{m.id}: {text[:70]}")

    # Hermes answers in two stages: a progress placeholder first ("✨ Свожу всё
    # воедино…"), the real answer later. An early return catches the placeholder and
    # calls it a pass, which is how a broken chain looks identical to a working one.
    # So: ignore placeholders, and once a REAL message lands wait for the stream to
    # settle before deciding, since a long answer arrives in several parts.
    # Detect placeholders STRUCTURALLY, not with a word list. The wording is
    # randomised ("Свожу всё воедино…", "Разгоняю движок…", "Мои нейроны созвали
    # совещание…") so any vocabulary is a losing game — the first version of this
    # check missed the second phrasing and passed a test on a progress message.
    # What they share is shape: short, wrapped in backticks, trailing ellipsis.
    def is_progress(t: str) -> bool:
        x = t.strip()
        if len(x) >= 90:
            return False
        # The trailing ellipsis is the signal, NOT the backticks. Requiring only
        # backticks threw away a correct one-word answer (`mvb-run.py`) and failed a
        # test the system had actually passed — a filter that hides real answers is
        # worse than one that lets a placeholder through, because it invents failures.
        return x.rstrip("`").rstrip().endswith(("…", "..."))

    deadline = time.time() + args.timeout
    seen: dict[int, str] = {}
    last_new = 0.0
    while time.time() < deadline:
        await asyncio.sleep(5)
        fresh = 0
        async for msg in client.iter_messages(bot, limit=25):
            if msg.out or not msg.text:
                continue
            if msg.date.timestamp() < since:
                break                         # newest-first, so this is the end of our window
            if msg.id not in seen:
                seen[msg.id] = msg.text
                fresh += 1
        if fresh:
            last_new = time.time()
        real = [t for t in seen.values() if not is_progress(t)]
        # settled = something real arrived and nothing new for 8s
        if real and last_new and time.time() - last_new >= 12:
            break

    replies = [seen[k] for k in sorted(seen)]
    real_replies = [t for t in replies if not is_progress(t)]

    await client.disconnect()

    if not replies:
        print(f"[{label}] ❌ FAIL — no reply within {args.timeout}s")
        return 1
    if not real_replies:
        print(f"[{label}] ❌ FAIL — only progress placeholders arrived in {args.timeout}s: {replies}")
        return 1

    joined = "\n---\n".join(real_replies)
    print(f"[{label}] reply ({len(real_replies)} real message(s), "
          f"{len(replies)-len(real_replies)} placeholder(s) ignored):")
    for line in joined.splitlines()[:24]:
        print(f"    {line[:160]}")
    if len(joined.splitlines()) > 24:
        print(f"    … (+{len(joined.splitlines())-24} lines)")

    if args.expect:
        if args.expect in joined:
            print(f"[{label}] ✅ PASS — reply contains {args.expect!r}")
            return 0
        print(f"[{label}] ❌ FAIL — reply does NOT contain {args.expect!r}")
        return 1
    print(f"[{label}] ✅ PASS — got a reply")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--send", action="append", required=True,
                    help="message text; repeat to send several at once")
    ap.add_argument("--expect", default="", help="substring the reply MUST contain")
    ap.add_argument("--timeout", type=int, default=180)
    ap.add_argument("--label", default="")
    args = ap.parse_args()
    load_creds()
    return asyncio.run(run(args))


if __name__ == "__main__":
    sys.exit(main())
