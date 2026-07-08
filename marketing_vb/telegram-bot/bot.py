"""
Marketing Automation — Telegram Bot

Single bot, three tracks (social / outbound / seo).
- Reads artifacts produced by Claude Code subagents from /workspace/{track}/...
- Pushes notifications to Vadim with Approve / Edit / Reject buttons
- Writes feedback back to /workspace/{track}/.../feedback.md

Ground truth = filesystem. Telegram is only a UI.

Authentication: whitelist by chat_id in ALLOWED_CHAT_IDS.
"""

import os
import json
import logging
import pathlib
from datetime import datetime
from typing import Optional

from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler, CallbackQueryHandler,
    ContextTypes, filters
)

load_dotenv()

# --- config ---
BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
ALLOWED_CHAT_IDS = {int(x) for x in os.environ["ALLOWED_CHAT_IDS"].split(",")}
WORKSPACE_ROOT = pathlib.Path(os.environ.get("WORKSPACE_ROOT", "/workspace")).resolve()
LOG_DIR = pathlib.Path(os.environ.get("LOG_DIR", "/var/log/marketing-bot")).resolve()
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "bot.log"),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger("marketing-bot")


# --- auth ---
def require_auth(handler):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.effective_chat.id not in ALLOWED_CHAT_IDS:
            log.warning(f"Unauthorized access attempt: chat_id={update.effective_chat.id}")
            return
        return await handler(update, context)
    return wrapper


# --- helpers ---
def write_feedback(artifact_path: pathlib.Path, decision: str, comment: str = "", user: str = "vadim"):
    """Append feedback record to feedback.md next to the artifact."""
    fb_path = artifact_path.parent / "feedback.md"
    timestamp = datetime.utcnow().isoformat()
    entry = f"\n---\n## {timestamp} — {user} — {decision}\n"
    entry += f"**Artifact:** `{artifact_path.name}`\n"
    if comment:
        entry += f"\n**Comment:**\n{comment}\n"
    with open(fb_path, "a") as f:
        f.write(entry)
    log.info(f"Feedback written: {fb_path} — {decision}")


def update_status(artifact_path: pathlib.Path, status: str):
    """Mirror status to a sidecar JSON for downstream agents to read."""
    status_path = artifact_path.parent / f"{artifact_path.stem}.status.json"
    payload = {
        "artifact": str(artifact_path),
        "status": status,
        "updated_at": datetime.utcnow().isoformat(),
    }
    with open(status_path, "w") as f:
        json.dump(payload, f, indent=2)


def review_keyboard(artifact_id: str) -> InlineKeyboardMarkup:
    """Standard 3-button review keyboard."""
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("✅ Approve", callback_data=f"approve|{artifact_id}"),
            InlineKeyboardButton("✏️ Edit", callback_data=f"edit|{artifact_id}"),
            InlineKeyboardButton("❌ Reject", callback_data=f"reject|{artifact_id}"),
        ]
    ])


def find_artifact(artifact_id: str) -> Optional[pathlib.Path]:
    """artifact_id is path relative to WORKSPACE_ROOT, e.g. 'social/2026-W17/linkedin-company/post-1.md'."""
    p = (WORKSPACE_ROOT / artifact_id).resolve()
    if not p.is_relative_to(WORKSPACE_ROOT):
        return None
    return p if p.exists() else None


# --- commands ---
@require_auth
async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Marketing automation bot ready.\n\n"
        "Tracks:\n"
        "• /pending — show items awaiting review\n"
        "• /status — current state of all tracks\n"
        "• /help — full command list"
    )


@require_auth
async def cmd_pending(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """List all pending artifacts across tracks."""
    pending = []
    for track in ["social", "outbound", "seo"]:
        track_dir = WORKSPACE_ROOT / track
        if not track_dir.exists():
            continue
        # Look for status sidecars marked 'awaiting_review'
        for status_file in track_dir.rglob("*.status.json"):
            try:
                with open(status_file) as f:
                    data = json.load(f)
                if data.get("status") == "awaiting_review":
                    pending.append((track, pathlib.Path(data["artifact"])))
            except Exception as e:
                log.warning(f"Bad status file {status_file}: {e}")

    if not pending:
        await update.message.reply_text("✅ Nothing pending.")
        return

    msg = f"📋 *{len(pending)} item(s) awaiting review:*\n\n"
    for track, artifact in pending[:20]:
        rel = artifact.relative_to(WORKSPACE_ROOT)
        msg += f"• `{rel}`\n"
    await update.message.reply_text(msg, parse_mode="Markdown")


@require_auth
async def cmd_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """High-level status across all three tracks."""
    summary = {"social": 0, "outbound": 0, "seo": 0}
    for track in summary:
        track_dir = WORKSPACE_ROOT / track
        if track_dir.exists():
            summary[track] = len(list(track_dir.rglob("*.md")))

    msg = "📊 *Status:*\n\n"
    msg += f"• Social: {summary['social']} artifacts\n"
    msg += f"• Outbound: {summary['outbound']} artifacts\n"
    msg += f"• SEO: {summary['seo']} artifacts\n"
    await update.message.reply_text(msg, parse_mode="Markdown")


# --- review notifications (called from agent runners) ---
async def notify_review(application: Application, artifact_path: pathlib.Path,
                        track: str, summary: str):
    """
    Called externally (e.g. from a webhook or polling script) when an agent finishes
    work and writes status=awaiting_review.
    """
    artifact_id = str(artifact_path.relative_to(WORKSPACE_ROOT))
    text = f"🔔 *{track.upper()} — review needed*\n\n"
    text += f"`{artifact_id}`\n\n"
    text += summary[:1500]  # Telegram message limit safety

    for chat_id in ALLOWED_CHAT_IDS:
        await application.bot.send_message(
            chat_id=chat_id,
            text=text,
            parse_mode="Markdown",
            reply_markup=review_keyboard(artifact_id),
        )


# --- callback handlers (button taps) ---
@require_auth
async def on_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    action, artifact_id = query.data.split("|", 1)
    artifact = find_artifact(artifact_id)
    if not artifact:
        await query.edit_message_text(f"⚠️ Artifact not found: `{artifact_id}`",
                                      parse_mode="Markdown")
        return

    user = update.effective_user.username or str(update.effective_user.id)

    if action == "approve":
        write_feedback(artifact, "APPROVED", user=user)
        update_status(artifact, "approved")
        await query.edit_message_text(
            f"✅ Approved: `{artifact_id}`\n\n_Next agent in pipeline can pick up._",
            parse_mode="Markdown"
        )

    elif action == "reject":
        write_feedback(artifact, "REJECTED", user=user)
        update_status(artifact, "rejected")
        await query.edit_message_text(
            f"❌ Rejected: `{artifact_id}`\n\n_Pipeline halted, no auto-retry._",
            parse_mode="Markdown"
        )

    elif action == "edit":
        # Stash artifact_id in user_data, wait for follow-up text message
        context.user_data["awaiting_edit_for"] = artifact_id
        await query.edit_message_text(
            f"✏️ Edit mode for `{artifact_id}`.\n\n"
            "Send your comments as the next message. "
            "They'll be saved to `feedback.md` and the agent will revise.",
            parse_mode="Markdown"
        )


@require_auth
async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Catch follow-up text after Edit button."""
    artifact_id = context.user_data.pop("awaiting_edit_for", None)
    if not artifact_id:
        # Not in edit-flow — ignore or echo help
        await update.message.reply_text(
            "Tap Approve / Edit / Reject on a notification first. /help for commands."
        )
        return

    artifact = find_artifact(artifact_id)
    if not artifact:
        await update.message.reply_text(f"⚠️ Artifact gone: {artifact_id}")
        return

    comment = update.message.text
    user = update.effective_user.username or str(update.effective_user.id)
    write_feedback(artifact, "EDIT_REQUESTED", comment=comment, user=user)
    update_status(artifact, "edit_requested")
    await update.message.reply_text(
        f"📝 Feedback saved to `{artifact.parent.name}/feedback.md`.\n"
        "Agent will pick up on next run.",
        parse_mode="Markdown"
    )


# --- main ---
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("help", cmd_start))
    app.add_handler(CommandHandler("pending", cmd_pending))
    app.add_handler(CommandHandler("status", cmd_status))
    app.add_handler(CallbackQueryHandler(on_button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_message))

    log.info(f"Bot starting. Workspace: {WORKSPACE_ROOT}, Allowed: {ALLOWED_CHAT_IDS}")
    app.run_polling()


if __name__ == "__main__":
    main()
