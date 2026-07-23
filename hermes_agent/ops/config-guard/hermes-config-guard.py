#!/usr/bin/env python3
"""hermes-config-guard: keep ~/.hermes/config.yaml valid & clean.

Hermes's daily session_reset "self-improvement review" periodically rewrites
config.yaml into INVALID YAML — an orphaned `- provider: opencode-zen` sequence
item injected right after `providers: {}`. Invalid config → the gateway
silently ignores every override and falls back to free-tier Gemini
(gemini-3.1-pro-preview, limit 0) → HTTP 429 on every message.
See memory project_hermes_config_corruption_429 / project_hermes_transformed_unbound.

This guard runs on every config write (systemd .path unit) + a 15-min timer:
  1. config parses AND has no opencode-zen fallback (the loaded gun) →
     snapshot it as the rolling last-known-good copy. Done.
  2. config does NOT parse →
       a. back up the corrupt file,
       b. targeted repair: strip orphaned sequence items after an empty-map
          key (`providers: {}`),
       c. if the repaired text parses, also defuse `fallback_providers`
          (drop opencode-zen) so it can't recur,
       d. if repair still fails, restore the last-known-good snapshot,
       e. write, drain-restart the gateway (SIGUSR1 → systemctl fallback),
          ping Telegram.
"""
import json, os, re, shutil, signal, ssl, subprocess, sys, urllib.parse, urllib.request
from datetime import datetime

import yaml

HOME     = os.path.expanduser("~")
HERMES   = f"{HOME}/.hermes"
CONFIG   = f"{HERMES}/config.yaml"
ENVF     = f"{HERMES}/.env"
LASTGOOD = f"{HERMES}/config-guard/config.lastgood.yaml"
LOGF     = f"{HERMES}/logs/config-guard.log"
CTX      = ssl.create_default_context()


def log(msg):
    line = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {msg}"
    print(line)
    try:
        os.makedirs(os.path.dirname(LOGF), exist_ok=True)
        with open(LOGF, "a") as f:
            f.write(line + "\n")
    except Exception:
        pass


def env(key):
    try:
        for line in open(ENVF):
            if line.startswith(key + "="):
                return line.split("=", 1)[1].strip()
    except FileNotFoundError:
        pass
    return ""


def parses(text):
    try:
        yaml.safe_load(text)
        return True
    except yaml.YAMLError:
        return False


def has_zen_fallback(cfg):
    fp = cfg.get("fallback_providers") if isinstance(cfg, dict) else None
    return isinstance(fp, list) and any(
        isinstance(x, dict) and x.get("provider") == "opencode-zen" for x in fp
    )


def repair_orphaned(text):
    """Strip orphaned top-level sequence items that appear right after an
    empty-map literal key (`foo: {}`) — the exact corruption signature."""
    lines = text.split("\n")
    out, i, n, removed = [], 0, len(lines), 0
    while i < n:
        line = lines[i]
        out.append(line)
        i += 1
        if re.match(r'^[A-Za-z0-9_]+:\s*\{\}\s*$', line) and i < n and lines[i].lstrip().startswith("- "):
            while i < n:
                cur = lines[i]
                if cur.strip() == "":
                    break
                if cur[0] not in " \t" and not cur.lstrip().startswith("- "):
                    break  # next real top-level mapping key
                removed += 1
                i += 1
    return "\n".join(out), removed


def strip_zen_fallback(text):
    """Replace the top-level `fallback_providers:` block with `[]`."""
    lines = text.split("\n")
    out, i, n, changed = [], 0, len(lines), False
    while i < n:
        if re.match(r'^fallback_providers:', lines[i]):
            out.append("fallback_providers: []")
            i += 1
            while i < n and lines[i][:1] in (" ", "\t"):
                i += 1
            changed = True
            continue
        out.append(lines[i]); i += 1
    return "\n".join(out), changed


def telegram(text):
    tok = env("TELEGRAM_BOT_TOKEN")
    chat = env("TELEGRAM_HOME_CHANNEL") or env("TELEGRAM_ALLOWED_USERS").split(",")[0].strip()
    if not tok or not chat:
        return False
    body = urllib.parse.urlencode(
        {"chat_id": chat, "text": text, "parse_mode": "HTML", "disable_web_page_preview": "true"}
    ).encode()
    try:
        req = urllib.request.Request(f"https://api.telegram.org/bot{tok}/sendMessage", data=body)
        with urllib.request.urlopen(req, timeout=20, context=CTX) as r:
            return json.loads(r.read()).get("ok", False)
    except Exception as e:
        log(f"telegram notify failed: {e}")
        return False


def _gateway_pid():
    try:
        r = subprocess.run(["systemctl", "--user", "show", "hermes-gateway.service",
                            "-p", "MainPID", "--value"], capture_output=True, text=True, timeout=10)
        pid = int(r.stdout.strip())
        return pid if pid > 0 else None
    except Exception:
        return None


def restart_gateway():
    pid = _gateway_pid()
    if pid:
        try:
            os.kill(pid, signal.SIGUSR1)  # drain-aware restart (systemd Restart= revives it)
            return "sigusr1"
        except OSError:
            pass
    e = dict(os.environ)
    e.setdefault("XDG_RUNTIME_DIR", f"/run/user/{os.getuid()}")
    try:
        subprocess.run(["systemctl", "--user", "restart", "hermes-gateway.service"],
                       env=e, timeout=60, check=False)
        return "systemctl"
    except Exception as ex:
        log(f"restart failed: {ex}")
        return None


def snapshot_lastgood(text):
    try:
        os.makedirs(os.path.dirname(LASTGOOD), exist_ok=True)
        with open(LASTGOOD, "w") as f:
            f.write(text)
    except Exception as e:
        log(f"lastgood snapshot failed: {e}")


def main():
    try:
        text = open(CONFIG).read()
    except FileNotFoundError:
        log("config.yaml missing — nothing to guard")
        return 0

    # --- healthy path ---
    if parses(text):
        if not has_zen_fallback(yaml.safe_load(text) or {}):
            snapshot_lastgood(text)  # keep only clean copies as the baseline
        return 0

    # --- corrupt path ---
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    corrupt_bak = f"{CONFIG}.corrupt-guard.{ts}.bak"
    try:
        shutil.copy2(CONFIG, corrupt_bak)
    except Exception as e:
        log(f"corrupt backup failed: {e}")
    log(f"INVALID config detected → backed up to {os.path.basename(corrupt_bak)}")

    fixed, removed = repair_orphaned(text)
    if removed and parses(fixed):
        source = f"targeted repair (−{removed} orphaned line(s))"
        if has_zen_fallback(yaml.safe_load(fixed) or {}):
            stripped, did = strip_zen_fallback(fixed)
            if did and parses(stripped):
                fixed = stripped
                source += " + defused opencode-zen fallback"
    elif os.path.exists(LASTGOOD) and parses(open(LASTGOOD).read()):
        fixed = open(LASTGOOD).read()
        source = "restored last-known-good snapshot"
    else:
        log("REPAIR FAILED — targeted repair did not parse and no valid lastgood. Leaving file untouched.")
        telegram("⚠️ <b>Hermes config-guard</b>\nconfig.yaml зламався, авто-ремонт НЕ вдався — потрібне ручне втручання. Бот може відповідати помилками (429).")
        return 1

    with open(CONFIG, "w") as f:
        f.write(fixed)
    snapshot_lastgood(fixed)
    how = restart_gateway()
    log(f"repaired via {source}; gateway restart={how}")
    telegram(f"🔧 <b>Hermes config-guard</b>\nconfig.yaml був зламаний — авто-полагоджено ({source}), gateway перезапущено ({how}). Модель повернуто на робочу.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
