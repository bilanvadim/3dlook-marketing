#!/usr/bin/env python3
"""Hermes Agent morning auto-update.

Pulls the latest upstream (git) + reinstalls deps via `hermes update`, restarts
the gateway to load the new code, and pings Telegram — so each morning the bot
is on a fresh version. Runs headless from a systemd --user timer (08:00 UTC).

- `-y`       : assume-yes for config migration / stash restore (skips API-key entry)
- `--backup` : force a pre-update backup each run (rollback safety; updates.backup_keep=5)
- Notifies Telegram ONLY on an actual version change or on failure (no daily noise).
Reuses router_lib for telegram() + restart_gateway() (same helpers model-router uses).
"""
import os
import re
import shutil
import subprocess
import sys

HOME = os.path.expanduser("~")
# `hermes update`/`hermes setup` can reset SOUL.md back to the generic NousResearch
# default (which makes Hermes code things itself instead of delegating to Claude Code).
# Re-apply the canonical orchestrator persona from the repo after every update.
REPO_SOUL = "@DEST@/agents-ai/telegram-bot-agent/hermes-agent/SOUL.md"
LIVE_SOUL = f"{HOME}/.hermes/SOUL.md"


def _render_identity(text: str) -> str:
    """Substitute the install-time identity tokens in a kit template.

    Values are written to ~/.hermes/.env by install.sh (HERMES_OWNER,
    HERMES_GH_OWNER, HERMES_PROJECT_ROOT). A token with no value is left ALONE
    rather than replaced by an empty string: "merges are 's decision" reads as
    corruption, while an untouched @OWNER@ is visibly an unfinished install.
    """
    env = {}
    try:
        with open(f"{HOME}/.hermes/.env", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env[k.strip()] = v.strip().strip("\"'")
    except OSError:
        pass
    for token, key in (("@OWNER@", "HERMES_OWNER"),
                       ("@GH_OWNER@", "HERMES_GH_OWNER"),
                       ("@PROJECT_ROOT@", "HERMES_PROJECT_ROOT")):
        val = (env.get(key) or os.environ.get(key) or "").strip()
        if val:
            text = text.replace(token, val)
    return text
sys.path.insert(0, f"{HOME}/.hermes/model-router")
import router_lib as rl  # noqa: E402  (telegram, restart_gateway, env)

HERMES = f"{HOME}/.hermes/hermes-agent/venv/bin/hermes"
LOG = f"{HOME}/.hermes/logs/hermes-update.log"
_ENV = dict(os.environ)
_ENV.setdefault("XDG_RUNTIME_DIR", f"/run/user/{os.getuid()}")


def _now():
    return subprocess.run(["date", "-u", "+%F %T"], capture_output=True, text=True).stdout.strip()


def log(msg):
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    with open(LOG, "a") as f:
        f.write(f"{_now()} {msg}\n")


def version():
    """e.g. 'v0.18.2 (2026.7.7.2)' from `hermes --version`."""
    try:
        out = subprocess.run([HERMES, "--version"], capture_output=True, text=True, timeout=60).stdout
        m = re.search(r"v[\d.]+\s*\([\d.]+\)", out)
        return m.group(0) if m else (out.strip().splitlines() or ["unknown"])[0]
    except Exception as e:
        return f"unknown ({e})"


def gateway_active():
    r = subprocess.run(["systemctl", "--user", "is-active", "hermes-gateway.service"],
                       capture_output=True, text=True, env=_ENV)
    return r.stdout.strip()


def main():
    old = version()
    log(f"start; current={old}")

    r = subprocess.run([HERMES, "update", "-y", "--backup"],
                       capture_output=True, text=True, timeout=1800, env=_ENV)
    tail = (r.stdout + r.stderr)[-600:]
    log(f"`hermes update` rc={r.returncode}\n{tail}")

    if r.returncode != 0:
        rl.telegram(f"⚠️ <b>Hermes auto-update FAILED</b> (rc={r.returncode}).\n"
                    f"Версия осталась {old}. Бэкап на месте (rollback возможен).\n"
                    f"<code>{tail[-300:]}</code>")
        return 1

    # Guard against persona drift: restore the orchestrator SOUL.md if update reset it.
    #
    # The repo copy is a TEMPLATE — it carries @OWNER@ / @GH_OWNER@ / @PROJECT_ROOT@
    # so the kit does not ship one person's name as another person's instructions.
    # Rendering here is not cosmetic: this function copies the repo file into the live
    # persona every morning, so an unrendered copy would leave the manager addressing
    # a literal "@OWNER@" and pushing to "@GH_OWNER@". Compare against the RENDERED
    # text too, otherwise every run sees a difference and rewrites the file forever.
    try:
        if os.path.exists(REPO_SOUL):
            soul = _render_identity(open(REPO_SOUL, encoding="utf-8").read())
            same = (os.path.exists(LIVE_SOUL)
                    and open(LIVE_SOUL, encoding="utf-8").read() == soul)
            if not same:
                with open(LIVE_SOUL, "w", encoding="utf-8") as f:
                    f.write(soul)
                log("restored canonical SOUL.md from repo (persona had drifted)")
    except Exception as e:
        log(f"SOUL.md restore failed: {e}")

    # Re-apply the file-tool project-code write guard (vendored patch, wiped by update).
    try:
        guard = "@DEST@/agents-ai/telegram-bot-agent/hermes-agent/ops/apply-file-tool-guard.py"
        if os.path.exists(guard):
            g = subprocess.run(["/usr/bin/python3", guard], capture_output=True, text=True)
            log(f"file-tool guard: {(g.stdout + g.stderr).strip()}")
            if g.returncode == 2:
                rl.telegram("⚠️ Hermes update: file-tool барьер (вендорный патч) НЕ переприменён "
                            "(upstream _check_sensitive_path изменился). Основной барьер — "
                            "shell-хук block-project-writes.py — держит; это была вторая линия. "
                            "Патчер всё равно стоит поправить.")
    except Exception as e:
        log(f"file-tool guard re-apply failed: {e}")

    # Health-check the shell hook that IS the primary file-tool barrier now.
    # A hook lapses differently than a vendored patch: the script can lose its
    # exec bit, consent can vanish from the allowlist, or an upstream change can
    # rename the event — and in a non-TTY gateway that failure is SILENT.
    # `hooks doctor` is the only thing that sees it, so it must alert like the
    # patchers above do.
    try:
        h = subprocess.run([HERMES, "hooks", "doctor"], capture_output=True, text=True, timeout=120)
        out = (h.stdout + h.stderr).strip()
        log(f"hooks doctor: {out.splitlines()[-1] if out else '(no output)'}")
        if "look healthy" not in out:
            rl.telegram("⚠️ <b>Hermes update: shell-хуки нездоровы</b>\n"
                        "Барьер «менеджер, не кодер» на файловых инструментах мог отвалиться "
                        "молча (gateway — non-TTY). Проверь: <code>hermes hooks doctor</code>\n"
                        f"<pre>{out[-500:]}</pre>")
    except Exception as e:
        log(f"hooks doctor failed: {e}")

    # Watch approvals.mode and command_allowlist.
    #
    # An "Always" click on a Telegram approval prompt writes a permanent
    # command_allowlist entry — and those entries are whole PATTERN CATEGORIES,
    # not single commands. On 2026-08-05 three of them were found sitting in
    # config.yaml ("script execution via heredoc", "in-place edit of Hermes
    # config/env", "script execution via -e/-c flag"): a standing, forever
    # bypass of exactly the vectors the agent once used to edit its own SOUL.md.
    # Nothing surfaces them, so they rot silently. Report any entry, and shout
    # if smart approvals got turned off altogether.
    try:
        import yaml as _yaml
        with open(f"{HOME}/.hermes/config.yaml") as _f:
            _cfg = _yaml.safe_load(_f) or {}
        _mode = str((_cfg.get("approvals") or {}).get("mode", "")).strip().lower()
        _allow = _cfg.get("command_allowlist") or []
        log(f"approvals: mode={_mode or '(unset)'} allowlist={len(_allow)}")
        if _mode != "smart":
            rl.telegram("⚠️ <b>Одобрения команд не в режиме smart</b>\n"
                        f"approvals.mode = <code>{_mode or '(не задан)'}</code>. "
                        "Опасные команды больше не проходят через судью и не спрашивают тебя.")
        if _allow:
            _items = "\n".join(f"• {a}" for a in _allow[:10])
            rl.telegram("⚠️ <b>В command_allowlist появились вечные разрешения</b>\n"
                        "Это КАТЕГОРИИ опасных команд, разрешённые навсегда (обычно — "
                        "кнопка «Always» в чате). Проверь, что там не лежит правка "
                        "собственных файлов Hermes:\n"
                        f"<pre>{_items}</pre>"
                        "Убрать: <code>command_allowlist: []</code> в ~/.hermes/config.yaml")
    except Exception as e:
        log(f"approvals watch failed: {e}")

    # Sync the model-router from the repo into ~/.hermes/model-router.
    # Nothing else does this: hermes-update only ever IMPORTED router_lib from the
    # live directory, so a change committed to the repo never reached the 07:00 job
    # and the morning pick silently kept running the old code. Data files
    # (pick.json, coder-history.json, cache/) live only in the live dir and are
    # left alone — copy the sources, never the state.
    try:
        import glob as _glob
        src_dir = ("@DEST@/agents-ai/telegram-bot-agent/"
                   "hermes-agent/ops/model-router")
        dst_dir = f"{HOME}/.hermes/model-router"
        if os.path.isdir(src_dir):
            os.makedirs(dst_dir, exist_ok=True)
            synced = []
            for src in sorted(_glob.glob(f"{src_dir}/*.py") +
                              _glob.glob(f"{src_dir}/*.json")):
                name = os.path.basename(src)
                if name in ("pick.json", "coder-history.json"):
                    continue                      # state, not source
                dst = os.path.join(dst_dir, name)
                if (not os.path.exists(dst)
                        or open(src, "rb").read() != open(dst, "rb").read()):
                    shutil.copyfile(src, dst)
                    synced.append(name)
            log(f"model-router sync: {', '.join(synced) if synced else 'без изменений'}")
    except Exception as e:
        log(f"model-router sync failed: {e}")

    # Re-apply the Claude-Code switcher patch (/dev /seo /marketing /security /hermes
    # sticky mode — vendored inserts in run.py + commands.py, wiped by update).
    try:
        switcher = "@DEST@/agents-ai/telegram-bot-agent/hermes-agent/ops/claude-switcher/apply-claude-switcher-patch.py"
        if os.path.exists(switcher):
            g = subprocess.run(["/usr/bin/python3", switcher], capture_output=True, text=True)
            log(f"claude-switcher: {(g.stdout + g.stderr).strip()}")
            if g.returncode == 2:
                rl.telegram("⚠️ Hermes update: переключатель Claude Code НЕ переприменён "
                            "(анкер в run.py/commands.py сместился) — /dev /seo /marketing "
                            "сейчас не работают, бот остаётся Hermes-менеджером. Нужен фикс патчера.")
    except Exception as e:
        log(f"claude-switcher re-apply failed: {e}")

    # Re-apply the per-turn vision switch (borrow the image reader for the turn
    # that carries a picture — two vendored inserts in run.py, wiped by update).
    try:
        vsw = ("@DEST@/agents-ai/telegram-bot-agent/"
               "hermes-agent/ops/vision-switch/apply-vision-switch-patch.py")
        if os.path.exists(vsw):
            g = subprocess.run(["/usr/bin/python3", vsw], capture_output=True, text=True)
            log(f"vision-switch: {(g.stdout + g.stderr).strip()}")
            if g.returncode == 2:
                rl.telegram("⚠️ Hermes update: переключение на vision-модель НЕ "
                            "переприменено (анкер в run.py сместился). Картинки не "
                            "пропадут — их опишет auxiliary.vision, — но читать их "
                            "будет не сама модель. Нужен фикс патчера.")
    except Exception as e:
        log(f"vision-switch re-apply failed: {e}")

    restarted = rl.restart_gateway()
    st = gateway_active()
    new = version()
    log(f"restarted={restarted} gateway={st} old={old} new={new}")

    if st != "active":
        rl.telegram(f"⚠️ <b>Hermes обновлён до {new}, но gateway НЕ поднялся</b> ({st}).\n"
                    f"Проверь: <code>hermes gateway status</code> / логи.")
        return 1

    if new != old:
        rl.telegram(f"🆕 <b>Hermes обновлён за ночь</b>\n{old} → <b>{new}</b>\nGateway перезапущен ✅")
        log("notified: updated")
    else:
        log("no version change (already latest) — silent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
