#!/usr/bin/env python3
"""
Hermes Orchestrator — Telegram chat bridge.

Two-way chat between Vadim and the Claude Code orchestrator. Every text message
is handed to `claude -p` running in the marketing working dir under the active
profile (marketing_vb_sm by default); the reply is sent straight back to Telegram.
This is the CONVERSATIONAL orchestrator (like DMing Claude), NOT the autonomous
conductor — the conductor keeps running separately for A→Z jobs.

Design:
- Auth: strict chat_id whitelist (ALLOWED_CHAT_IDS). Anyone else is ignored.
- Continuity: the claude session_id is persisted per chat; each message resumes
  the same session so it's a real conversation. /new starts a fresh one.
- One run at a time (asyncio.Lock) so concurrent messages can't corrupt --resume.
- Long tasks: a placeholder + typing action while claude runs in a worker thread
  (event loop stays responsive); hard timeout to avoid a hung run.
- Headless claude uses --dangerously-skip-permissions (the box's established
  convention for headless runs); the workspace is trusted so the profile's own
  hooks still gate prod-affecting actions.
"""
import os
import json
import asyncio
import logging
import pathlib
import sqlite3
import subprocess
import functools

from dotenv import load_dotenv
from telegram import Update, constants, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler, CallbackQueryHandler,
    ContextTypes, filters,
)

load_dotenv()

# --- config ---
BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
ALLOWED = {int(x) for x in os.environ["ALLOWED_CHAT_IDS"].split(",") if x.strip()}
WORKDIR = pathlib.Path(os.environ.get(
    "ORCH_WORKDIR", "/home/vadim_prod/3dlook-marketing/marketing_vb")).resolve()
CLAUDE_BIN = os.environ.get("CLAUDE_BIN", "/home/vadim_prod/.local/bin/claude")
MAX_TURNS = int(os.environ.get("ORCH_MAX_TURNS", "60"))
RUN_TIMEOUT = int(os.environ.get("ORCH_TIMEOUT", "1800"))  # 30 min hard cap
STATE_DIR = pathlib.Path(os.environ.get(
    "ORCH_STATE_DIR", "/home/vadim_prod/.hermes/tg-bridge")).resolve()
LOG_DIR = pathlib.Path(os.environ.get(
    "LOG_DIR", "/home/vadim_prod/3dlook-marketing/logs")).resolve()
ACTIVE_PROFILE_FILE = pathlib.Path("/home/vadim_prod/.claude/.active-profile")
HO_DB = os.environ.get(
    "HO_DB", "/home/vadim_prod/3dlook-marketing/claude_code/DEV/full_stack_sm/conductor/ho.db")

STATE_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.FileHandler(LOG_DIR / "tg-bridge.log"), logging.StreamHandler()],
)
log = logging.getLogger("tg-bridge")
# httpx/telegram log the full request URL (which embeds the bot token) at INFO — silence them.
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)
logging.getLogger("telegram").setLevel(logging.WARNING)

TG_CHUNK = 3900  # keep under Telegram's 4096 hard limit
_run_lock = asyncio.Lock()  # serialize claude runs (protects --resume)

# Conductor profiles the user can enqueue a job under (see claude_code/DEV/SYSTEMS.md).
# marketing_vb_sm first = Vadim's default. Marketing jobs run in marketing_vb/.
JOB_PROFILES = ["marketing_vb_sm", "marketing_vb", "dev", "seo", "security"]
JOB_WORKDIR = os.environ.get("ORCH_JOB_WORKDIR", str(WORKDIR))
JOB_MAX_TURNS = int(os.environ.get("ORCH_JOB_MAX_TURNS", "80"))


# --- conductor DB (ho.db) — small read/write helpers ---
def _db():
    con = sqlite3.connect(HO_DB, timeout=15)
    con.execute("PRAGMA busy_timeout=15000;")
    return con


def enqueue_job(title: str, prompt: str, profile: str) -> int:
    con = _db()
    try:
        cur = con.execute(
            "INSERT INTO ho_jobs(kind, title, prompt, profile, work_dir, max_turns) "
            "VALUES('feature', ?, ?, ?, ?, ?)",
            (title[:120], prompt, profile, JOB_WORKDIR, JOB_MAX_TURNS),
        )
        con.commit()
        return cur.lastrowid
    finally:
        con.close()


def decide_escalation(esc_id: int, status: str) -> bool:
    """Record approve/deny/abort; only the first decision on an open row wins."""
    con = _db()
    try:
        cur = con.execute(
            "UPDATE ho_escalations SET status=?, decided_by='vadim-tg', "
            "decided_at=datetime('now') WHERE id=? AND status='open'",
            (status, esc_id),
        )
        con.commit()
        return cur.rowcount > 0
    finally:
        con.close()


# --- session persistence (per chat) ---
def _session_file(chat_id: int) -> pathlib.Path:
    return STATE_DIR / f"session-{chat_id}.txt"


def get_session(chat_id: int):
    f = _session_file(chat_id)
    return f.read_text().strip() if f.exists() else None


def set_session(chat_id: int, sid: str):
    if sid:
        _session_file(chat_id).write_text(sid)


def clear_session(chat_id: int):
    _session_file(chat_id).unlink(missing_ok=True)


# --- auth ---
def auth(fn):
    @functools.wraps(fn)
    async def wrap(update: Update, context: ContextTypes.DEFAULT_TYPE):
        cid = update.effective_chat.id if update.effective_chat else None
        if cid not in ALLOWED:
            log.warning(f"unauthorized chat_id={cid}")
            return
        return await fn(update, context)
    return wrap


# --- claude runner (blocking; called via run_in_executor) ---
def _parse_json(out: str):
    out = out.strip()
    if not out:
        return None
    try:
        return json.loads(out)
    except Exception:
        for line in reversed(out.splitlines()):
            line = line.strip()
            if line.startswith("{"):
                try:
                    return json.loads(line)
                except Exception:
                    continue
    return None


def run_claude(prompt: str, session: str | None) -> dict:
    """Run claude -p once; on a resume failure, retry once fresh."""
    def _invoke(sess):
        cmd = [CLAUDE_BIN, "-p", prompt, "--output-format", "json",
               "--max-turns", str(MAX_TURNS), "--dangerously-skip-permissions"]
        if sess:
            cmd += ["--resume", sess]
        proc = subprocess.run(
            cmd, cwd=str(WORKDIR), capture_output=True, text=True, timeout=RUN_TIMEOUT)
        return proc

    proc = _invoke(session)
    data = _parse_json(proc.stdout)

    # resume can fail if the session is gone → retry once without it
    if data is None and session:
        log.warning("parse failed with --resume; retrying fresh")
        proc = _invoke(None)
        data = _parse_json(proc.stdout)
        session = None

    if data is None:
        tail = (proc.stderr or proc.stdout or "").strip()[-600:]
        return {"ok": False,
                "text": f"⚠️ Не разобрал ответ claude (rc={proc.returncode}).\n{tail}",
                "session": session}

    is_err = bool(data.get("is_error")) or data.get("subtype") not in (None, "success")
    text = data.get("result") or data.get("error") or "(пустой ответ)"
    sid = data.get("session_id") or session
    return {"ok": not is_err, "text": str(text), "session": sid}


def chunk(text: str, n: int = TG_CHUNK):
    for i in range(0, len(text), n):
        yield text[i:i + n]


# --- commands ---
@auth
async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prof = ACTIVE_PROFILE_FILE.read_text().strip() if ACTIVE_PROFILE_FILE.exists() else "?"
    await update.message.reply_text(
        "👋 Оркестратор на связи.\n\n"
        f"💬 Чат: пиши задачу/вопрос обычным текстом — запущу Claude Code в профиле «{prof}» "
        f"({WORKDIR.name}) и верну ответ (диалог с памятью).\n\n"
        "🤖 Автономная джоба в дирижёр:\n"
        "• /job <что сделать> — поставить джобу (выберешь профиль кнопкой). Дирижёр сделает A→Z сам, "
        "спросит решения по merge/деструктивным операциям кнопками, отпишет о завершении.\n\n"
        "Прочее:\n"
        "• /status — что в работе/очереди + что ждёт решения\n"
        "• /approve <id>, /deny <id>, /abort <id> — решить эскалацию (или жми кнопки)\n"
        "• /new — новый диалог (сброс контекста чата)\n"
        "• /profile — активный профиль\n"
        "• /help — справка"
    )


@auth
async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await cmd_start(update, context)


@auth
async def cmd_new(update: Update, context: ContextTypes.DEFAULT_TYPE):
    clear_session(update.effective_chat.id)
    await update.message.reply_text("🆕 Новый диалог. Прошлый контекст сброшен.")


@auth
async def cmd_profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prof = ACTIVE_PROFILE_FILE.read_text().strip() if ACTIVE_PROFILE_FILE.exists() else "(unknown)"
    await update.message.reply_text(f"🧭 Активный профиль: {prof}\n📁 Рабочая папка: {WORKDIR}")


@auth
async def cmd_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not pathlib.Path(HO_DB).exists():
        await update.message.reply_text("📊 БД дирижёра не найдена — джоб нет.")
        return
    try:
        con = _db()
        try:
            active = con.execute(
                "SELECT id, status, substr(title,1,45) FROM ho_jobs "
                "WHERE status NOT IN ('done','failed','aborted') ORDER BY id"
            ).fetchall()
            esc = con.execute(
                "SELECT id, job_id, reason, substr(question,1,70) FROM ho_escalations "
                "WHERE status='open' ORDER BY id"
            ).fetchall()
            recent = con.execute(
                "SELECT id, status, substr(title,1,45) FROM ho_jobs "
                "WHERE status IN ('done','failed','aborted') ORDER BY id DESC LIMIT 5"
            ).fetchall()
        finally:
            con.close()
    except Exception as e:
        await update.message.reply_text(f"⚠️ Не смог прочитать БД: {e}")
        return

    lines = ["📊 Дирижёр", "\nВ работе / в очереди:"]
    lines += [f"• #{i} [{s}] {t}" for i, s, t in active] or ["• (пусто)"]
    if esc:
        lines.append("\nЖдут решения:")
        lines += [f"• эск. #{eid} (job {jid}) [{r}]: {q}" for eid, jid, r, q in esc]
        lines.append("Реши кнопками под сообщением дирижёра, или: /approve <id>, /deny <id>, /abort <id>")
    lines.append("\nПоследние завершённые:")
    lines += [f"• #{i} [{s}] {t}" for i, s, t in recent] or ["• (пусто)"]
    await update.message.reply_text("\n".join(lines))


# --- enqueue a conductor job ---
@auth
async def cmd_job(update: Update, context: ContextTypes.DEFAULT_TYPE):
    desc = (update.message.text or "").partition(" ")[2].strip()
    if not desc:
        await update.message.reply_text(
            "Как ставить джобу дирижёру:\n/job <что нужно сделать>\n\n"
            "Пример: /job собери outbound-кампанию под UK telehealth, 25 компаний\n"
            "После этого выберешь профиль кнопкой.")
        return
    context.user_data["pending_job"] = desc
    kb = InlineKeyboardMarkup(
        [[InlineKeyboardButton(p, callback_data=f"job:{p}")] for p in JOB_PROFILES])
    await update.message.reply_text(
        f"📌 Джоба:\n{desc[:300]}\n\nВ каком профиле запустить?",
        reply_markup=kb)


# --- text approve/deny/abort fallbacks (buttons are the main path) ---
def _decide_cmd(cmd: str, status: str):
    @auth
    async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        args = context.args
        if not args or not args[0].isdigit():
            await update.message.reply_text(f"Формат: /{cmd} <id эскалации> (id смотри в /status)")
            return
        ok = decide_escalation(int(args[0]), status)
        await update.message.reply_text(
            f"✅ Эскалация #{args[0]} → {status}. Дирижёр продолжит." if ok
            else f"⚠️ Эскалация #{args[0]} не найдена или уже решена.")
    return handler


# --- inline button callbacks: job profile pick + escalation decisions ---
@auth
async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    data = q.data or ""
    await q.answer()

    if data.startswith("job:"):
        profile = data.split(":", 1)[1]
        desc = context.user_data.pop("pending_job", None)
        if not desc:
            await q.edit_message_text("⚠️ Текст джобы потерялся (бот перезапускался?). Пришли /job ещё раз.")
            return
        if profile not in JOB_PROFILES:
            await q.edit_message_text("⚠️ Неизвестный профиль.")
            return
        try:
            job_id = enqueue_job(desc.splitlines()[0], desc, profile)
        except Exception as e:
            log.exception("enqueue failed")
            await q.edit_message_text(f"❌ Не смог поставить джобу: {e}")
            return
        await q.edit_message_text(
            f"✅ Джоба #{job_id} в очереди дирижёра (профиль {profile}, {pathlib.Path(JOB_WORKDIR).name}).\n"
            "Дирижёр подхватит за ~10с. Вопросы/эскалации придут сюда кнопками; статус — /status.")
        log.info(f"enqueued job {job_id} profile={profile}: {desc[:80]!r}")
        return

    m = data.split(":")
    if len(m) == 3 and m[0] == "ho" and m[1] in ("approve", "deny", "abort"):
        status = {"approve": "approved", "deny": "denied", "abort": "aborted"}[m[1]]
        try:
            ok = decide_escalation(int(m[2]), status)
        except Exception as e:
            await q.edit_message_text(f"❌ Ошибка записи решения: {e}")
            return
        icon = {"approved": "✅", "denied": "⛔", "aborted": "🛑"}[status]
        if ok:
            await q.edit_message_text(f"{icon} Эскалация #{m[2]} → {status}. Дирижёр продолжит.")
        else:
            await q.edit_message_text(f"⚠️ Эскалация #{m[2]} уже была решена или закрыта.")
        log.info(f"escalation {m[2]} -> {status} (ok={ok})")
        return


# --- free-form chat ---
@auth
async def on_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cid = update.effective_chat.id
    prompt = update.message.text
    log.info(f"msg from {cid}: {prompt[:120]!r}")

    placeholder = await update.message.reply_text("🔄 Оркестратор думает…")
    try:
        await context.bot.send_chat_action(cid, constants.ChatAction.TYPING)
    except Exception:
        pass

    async with _run_lock:
        session = get_session(cid)
        loop = asyncio.get_event_loop()
        try:
            res = await loop.run_in_executor(None, run_claude, prompt, session)
        except subprocess.TimeoutExpired:
            await placeholder.edit_text(
                "⏱️ Задача идёт дольше 30 мин — прервал запуск. "
                "Разбей на шаги или запусти как джобу дирижёра.")
            return
        except Exception as e:
            log.exception("run failed")
            await placeholder.edit_text(f"❌ Ошибка запуска: {e}")
            return

    set_session(cid, res["session"])
    text = res["text"] if res["text"].strip() else "(пустой ответ)"
    try:
        await placeholder.delete()
    except Exception:
        pass
    for part in chunk(text):
        await update.message.reply_text(part)


async def on_error(update: object, context: ContextTypes.DEFAULT_TYPE):
    log.error("handler error", exc_info=context.error)
    try:
        cid = update.effective_chat.id if isinstance(update, Update) and update.effective_chat else None
        if cid in ALLOWED:
            await context.bot.send_message(cid, "⚠️ Внутренняя ошибка обработчика — записал в лог.")
    except Exception:
        pass


async def _post_init(app: Application):
    from telegram import BotCommand
    await app.bot.set_my_commands([
        BotCommand("job", "поставить автономную джобу дирижёру"),
        BotCommand("status", "джобы дирижёра + что ждёт решения"),
        BotCommand("approve", "одобрить эскалацию <id>"),
        BotCommand("deny", "отклонить эскалацию <id>"),
        BotCommand("abort", "прервать эскалацию <id>"),
        BotCommand("new", "новый диалог (сброс контекста)"),
        BotCommand("profile", "активный профиль"),
        BotCommand("help", "справка"),
    ])


def main():
    app = Application.builder().token(BOT_TOKEN).post_init(_post_init).build()
    app.add_handler(CommandHandler("start", cmd_start))
    app.add_handler(CommandHandler("help", cmd_help))
    app.add_handler(CommandHandler("new", cmd_new))
    app.add_handler(CommandHandler("status", cmd_status))
    app.add_handler(CommandHandler("profile", cmd_profile))
    app.add_handler(CommandHandler("job", cmd_job))
    app.add_handler(CommandHandler("approve", _decide_cmd("approve", "approved")))
    app.add_handler(CommandHandler("deny", _decide_cmd("deny", "denied")))
    app.add_handler(CommandHandler("abort", _decide_cmd("abort", "aborted")))
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))
    app.add_error_handler(on_error)

    log.info(f"orchestrator bridge up. workdir={WORKDIR} allowed={ALLOWED} db={HO_DB}")
    app.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)


if __name__ == "__main__":
    main()
