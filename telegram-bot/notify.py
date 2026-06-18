"""
notify.py — minimal helper script called by agent runners (or directly from agents
via Bash) to push a review notification to Vadim's Telegram.

Usage:
    python notify.py --track social --artifact "social/2026-W17/linkedin-company/post-1.md" \
                     --summary-file "/tmp/summary.txt"

Or from bash:
    python notify.py --track outbound --artifact "..." --summary "TL;DR text here"

This script:
1. Writes status=awaiting_review next to the artifact.
2. Pushes a Telegram message with Approve/Edit/Reject buttons.

It does NOT keep a long-running process. Use bot.py for that.
"""

import argparse
import asyncio
import json
import os
import pathlib
import sys
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
ALLOWED_CHAT_IDS = [int(x) for x in os.environ["ALLOWED_CHAT_IDS"].split(",")]
WORKSPACE_ROOT = pathlib.Path(os.environ.get("WORKSPACE_ROOT", "/workspace")).resolve()


def update_status(artifact_path: pathlib.Path, status: str):
    sidecar = artifact_path.parent / f"{artifact_path.stem}.status.json"
    payload = {
        "artifact": str(artifact_path),
        "status": status,
        "updated_at": datetime.utcnow().isoformat(),
    }
    sidecar.write_text(json.dumps(payload, indent=2))


def send_message(chat_id: int, text: str, artifact_id: str):
    keyboard = {
        "inline_keyboard": [[
            {"text": "✅ Approve", "callback_data": f"approve|{artifact_id}"},
            {"text": "✏️ Edit", "callback_data": f"edit|{artifact_id}"},
            {"text": "❌ Reject", "callback_data": f"reject|{artifact_id}"},
        ]]
    }
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    r = requests.post(url, json={
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "reply_markup": keyboard,
    }, timeout=10)
    r.raise_for_status()
    return r.json()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--track", required=True, choices=["social", "outbound", "seo"])
    parser.add_argument("--artifact", required=True,
                        help="Path relative to WORKSPACE_ROOT")
    parser.add_argument("--summary", default="", help="Inline summary text")
    parser.add_argument("--summary-file", default=None,
                        help="Read summary from file (overrides --summary)")
    args = parser.parse_args()

    artifact = (WORKSPACE_ROOT / args.artifact).resolve()
    if not artifact.is_relative_to(WORKSPACE_ROOT):
        sys.exit(f"Artifact path escapes workspace: {artifact}")
    if not artifact.exists():
        sys.exit(f"Artifact not found: {artifact}")

    summary = args.summary
    if args.summary_file:
        summary = pathlib.Path(args.summary_file).read_text()

    update_status(artifact, "awaiting_review")

    text = f"🔔 *{args.track.upper()} — review needed*\n\n"
    text += f"`{args.artifact}`\n\n"
    text += summary[:3500]  # Telegram limit ~4096

    for chat_id in ALLOWED_CHAT_IDS:
        try:
            send_message(chat_id, text, args.artifact)
        except Exception as e:
            print(f"Failed to notify {chat_id}: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
