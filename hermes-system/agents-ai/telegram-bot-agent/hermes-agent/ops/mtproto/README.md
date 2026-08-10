# mtproto — live topic lister for the forward-picker

The Telegram **Bot API cannot tell which forum topics the user deleted or
closed** — a deleted DM-topic still returns as valid to the bot. The forward-picker
must only ever offer **live** topics, so the switcher shells out to `list_topics.py`,
which uses the **user's own MTProto session** (`messages.GetForumTopics`) — the only
API that reports true topic liveness — and writes the result to
`~/.hermes/mtproto-topics.json` (a short-TTL cache the switcher reads).

## Files
| File | Role |
|---|---|
| `list_topics.py` | connects with the encrypted session, lists live topics of the bot chat, writes `~/.hermes/mtproto-topics.json`, disconnects. Prints only a small JSON summary. |
| `creds.env` (from `creds.env.example`, **chmod 600**) | `TG_API_ID`, `TG_API_HASH`, `MTPROTO_SESSION_KEY` (Fernet key). |
| `session.enc` (**generated, never commit**) | the account's StringSession, **Fernet-encrypted at rest**; decrypted only in memory. |
| `venv/` (generated) | `telethon` + `cryptography`. |

## Enroll on a fresh VPS
```bash
cd ~/.hermes/mtproto
python3 -m venv venv && ./venv/bin/pip install telethon cryptography
cp /path/to/repo/.../ops/mtproto/creds.env.example creds.env   # then fill + chmod 600
# 1) generate the Fernet key and put it in creds.env as MTPROTO_SESSION_KEY:
./venv/bin/python -c "from cryptography.fernet import Fernet;print(Fernet.generate_key().decode())"
# 2) mint a StringSession interactively (Telethon login), then encrypt it to session.enc:
./venv/bin/python - <<'PY'
import os
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from cryptography.fernet import Fernet
# load creds.env
for line in open("creds.env"):
    if "=" in line and not line.strip().startswith("#"):
        k,v=line.strip().split("=",1); os.environ[k]=v
with TelegramClient(StringSession(), int(os.environ["TG_API_ID"]), os.environ["TG_API_HASH"]) as c:
    s=c.session.save()                      # interactive: phone → code → (2FA)
enc=Fernet(os.environ["MTPROTO_SESSION_KEY"].encode()).encrypt(s.encode())
open("session.enc","wb").write(enc); os.chmod("session.enc",0o600)
print("session.enc written")
PY
# 3) smoke test — should print {"ok": true, "count": N, ...}
./venv/bin/python list_topics.py ivan_djedaev_bot
```

> The switcher passes the bot username as `argv[1]` (default `MT_BOT` env or
> `ivan_djedaev_bot`). The session account must be a member of / have opened the
> bot chat for `GetForumTopics` to succeed.
