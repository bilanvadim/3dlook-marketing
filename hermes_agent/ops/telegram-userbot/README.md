# telegram-userbot — Telethon userbot helpers

A Telethon **userbot** (logs in as the human account, `session.session`) used for
tasks the Bot API can't do — enrolling the MTProto session, searching chats, etc.
Paired with the `telegram-userbot-vps` skill (auth flow + anti-phishing + search).

## Files
| File | Role |
|---|---|
| `login.py` | standard interactive Telethon login (phone → code → optional 2FA). |
| `login_file.py` | **headless SMS login**: requests the code by SMS, then waits for it to appear in `code.txt` beside the script — so you can forward the SMS to yourself and paste it in without the code being invalidated. Phone from `TG_PHONE`. |
| `login_pyro.py` | Pyrogram-based login variant. |
| `qr_login.py` | QR-code login (writes `qr.png` to scan from the Telegram app). |
| `search.py` / `search.sh` | search dialogs/messages via the userbot session. |
| `.env` (from `.env.example`, **chmod 600**) | `TG_API_ID/HASH/PHONE/PASSWORD`. |
| `session.session` (**generated, never commit**) | the live Telethon session. |

## Enroll on a fresh VPS
```bash
cd ~/.hermes/telegram-userbot
python3 -m venv venv && ./venv/bin/pip install telethon pyrogram tgcrypto
cp /path/to/repo/.../ops/telegram-userbot/.env.example .env   # fill + chmod 600
set -a; . ./.env; set +a
# pick ONE login method:
./venv/bin/python login.py            # interactive
# or headless SMS (paste the code into code.txt when prompted):
./venv/bin/python login_file.py
# or QR (scan qr.png from your phone):
./venv/bin/python qr_login.py
chmod 600 session.session
```

> ⚠️ On the current box `session.session` was world-readable (644) — always
> `chmod 600 session.session` after login. Never commit sessions or `.env`.
