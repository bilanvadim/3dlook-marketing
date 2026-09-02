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


def scrub(text: str) -> str:
    """Remove the bot token from anything about to be printed.

    requests' HTTPError carries the full request URL in its message, and the URL is
    `https://api.telegram.org/bot<TOKEN>/sendMessage`. So `print(f"...: {e}")` published
    the live bot token — it reached a subagent transcript on 2026-09-02 exactly that way.
    Every diagnostic in this file goes through here.
    """
    out = str(text)
    if BOT_TOKEN:
        out = out.replace(BOT_TOKEN, "<BOT_TOKEN>")
        # the numeric prefix alone is enough to identify the bot, mask it too
        head = BOT_TOKEN.split(":")[0]
        if head and len(head) > 5:
            out = out.replace(head, "<BOT_ID>")
    return out


def _chat_ids() -> list:
    """Recipients. ALLOWED_CHAT_IDS is what this file was written for, but it does not
    exist in ~/.hermes/.env — that file carries TELEGRAM_ALLOWED_USERS and
    TELEGRAM_HOME_CHANNEL. Accept any of the three rather than crashing on import."""
    for key in ("ALLOWED_CHAT_IDS", "TELEGRAM_ALLOWED_USERS", "TELEGRAM_HOME_CHANNEL"):
        raw = os.environ.get(key, "").strip()
        if raw:
            ids = []
            for part in raw.split(","):
                part = part.strip().split(":")[-1]
                if part.lstrip("-").isdigit():
                    ids.append(int(part))
            if ids:
                return ids
    raise SystemExit("no recipients: set ALLOWED_CHAT_IDS or TELEGRAM_ALLOWED_USERS")


ALLOWED_CHAT_IDS = _chat_ids()
WORKSPACE_ROOT = pathlib.Path(os.environ.get("WORKSPACE_ROOT", "/workspace")).resolve()


# --- callback token map (Telegram caps callback_data at 64 bytes) ---
# `approve|<workspace-relative path>` overflows that cap for anything nested: a campaign
# artifact path like
#   outbound/campaigns/2026-07-21-eu-telehealth-weightloss/post-mortem.md
# is 68 characters, so the whole sendMessage came back HTTP 400 and Vadim got NO
# notification at all — not a degraded one. Found 2026-09-02 while notifying a step-9
# post-mortem. So the button carries a short token and the path is looked up here.
CALLBACK_MAP = WORKSPACE_ROOT / ".callback-tokens.json"


def callback_token(artifact_id: str) -> str:
    """Short, stable token for an artifact path, recorded so the handler can resolve it."""
    import hashlib
    tok = hashlib.sha1(artifact_id.encode("utf-8")).hexdigest()[:12]
    try:
        data = json.loads(CALLBACK_MAP.read_text()) if CALLBACK_MAP.exists() else {}
    except (OSError, ValueError):
        data = {}
    if data.get(tok) != artifact_id:
        data[tok] = artifact_id
        try:
            CALLBACK_MAP.parent.mkdir(parents=True, exist_ok=True)
            CALLBACK_MAP.write_text(json.dumps(data, indent=2, sort_keys=True))
        except OSError:
            pass
    return tok


def resolve_callback_token(tok: str) -> str:
    """Token -> artifact path. A plain path is passed through, so old buttons still work."""
    if "/" in tok or tok.endswith(".md"):
        return tok
    try:
        return (json.loads(CALLBACK_MAP.read_text()) or {}).get(tok, tok)
    except (OSError, ValueError):
        return tok


def update_status(artifact_path: pathlib.Path, status: str):
    sidecar = artifact_path.parent / f"{artifact_path.stem}.status.json"
    payload = {
        "artifact": str(artifact_path),
        "status": status,
        "updated_at": datetime.utcnow().isoformat(),
    }
    sidecar.write_text(json.dumps(payload, indent=2))


def send_message(chat_id: int, text: str, artifact_id: str):
    tok = callback_token(artifact_id)
    keyboard = {
        "inline_keyboard": [[
            {"text": "✅ Approve", "callback_data": f"approve|{tok}"},
            {"text": "✏️ Edit", "callback_data": f"edit|{tok}"},
            {"text": "❌ Reject", "callback_data": f"reject|{tok}"},
        ]]
    }
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    body = {"chat_id": chat_id, "text": text, "reply_markup": keyboard}

    # Markdown first, plain text as the fallback. A single underscore anywhere in the
    # summary — `connection_message`, `person_id`, any snake_case field name — makes
    # Telegram reject the whole message with 400, and a post-mortem is full of them. The
    # notification matters more than its formatting.
    r = requests.post(url, json={**body, "parse_mode": "Markdown"}, timeout=10)
    if r.status_code == 400:
        r = requests.post(url, json=body, timeout=10)
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
            print(f"Failed to notify {chat_id}: {scrub(e)}", file=sys.stderr)


if __name__ == "__main__":
    main()
