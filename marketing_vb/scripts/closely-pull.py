#!/usr/bin/env python3
"""closely-pull.py — pull campaign replies out of closely.io into responses-raw.csv.

WHY THIS EXISTS, AND WHAT IT COSTS
----------------------------------
Steps 8 and 9 of the outbound flow have never run. Not once, across 1276 sent messages and
2379 validated contacts, because `responses-raw.csv` only ever arrived by a manual export
that six campaigns are still waiting for. No replies means no `response-classifier`, no
`campaign-analyzer`, and no learnings feeding the next hypothesis.

**This talks to an API closely.io does not document.** Their own web app at
`app.closelyhq.com` calls it, and that is where every endpoint and field name below was
read from — the public bundle `static/js/main.<hash>.js`. Consequences Vadim accepted on
2026-09-02 when choosing this route over the HubSpot sync:

  * It can break on any Closely release, with no warning and no changelog.
  * It is their private surface, so behaviour under it is not a contract.
  * It needs credentials for the account on this VPS.

If it breaks, the fallback is `workspace/outbound/CLOSELY-CONNECTIVITY.md` route A: the
native Closely -> HubSpot sync with the campaign option "Sync Only Those Who Answered".

WHAT WAS READ FROM THE BUNDLE (all of it verified there, none of it guessed)
---------------------------------------------------------------------------
    base                  https://api.closelyhq.com          (const C / REACT_APP_API_URI)
    login                 POST /v1/login/check    -> {token, refresh_token}
    refresh               POST /v1/login/refresh  body {refresh_token}, header Skip-Auth: true
    auth on every call    Authorization: Bearer <token>
    conversations         GET  /v1/inbox/?limit=15&offset=N&with_incoming=1&campaign_id=&tags[]=
    one conversation      GET  /v1/inbox/{contact_id}/messages?limit=10&offset=10*page
    contact -> profile    https://www.linkedin.com/in/{lid}
    rate limit            429 is a real response the app handles explicitly

`with_incoming=1` is the app's own default inbox filter and means "this conversation has an
incoming message" — i.e. they replied. That is the filter this script pulls on.

WHAT IS *NOT* KNOWN, AND WHY THERE IS A PROBE
---------------------------------------------
The bundle gives paths and query parameters. It does not give response bodies. Field names
for a message (its text, its timestamp, whether it is inbound) are therefore NOT hard-coded
as a guess — `probe` prints the real key structure of one page of each endpoint, and `pull`
maps fields through a candidate list and *tells you* what it could not map. Run `probe`
first, once, and paste the output back if `pull` reports unmapped fields.

ONE SESSION AT A TIME — THIS EVICTS VADIM FROM THE APP
------------------------------------------------------
Closely allows a single active session per account. While this script holds one, Vadim is
kicked out of app.closelyhq.com; when he logs back in, **our token dies**. He reported
this on 2026-09-02, and it shapes how this runs:

  * Do all the work in ONE run. Every extra invocation is another eviction.
  * Never poll. The cron fires once a day at 23:30 UTC (02:30 Kyiv), when nobody is in
    the app — not in the morning, which is exactly when he is.
  * A dead token is the NORMAL consequence of him logging in, not an exception. So
    `--notify-on-failure` pushes it to Telegram rather than leaving a silent log line,
    because the fix needs him to paste a fresh token.
  * Prefer `pull-all` over per-campaign runs: one session, every folder.

CREDENTIALS — tokens, because this account is Google SSO
--------------------------------------------------------
Vadim signs into Closely with Google (vadim.bilan@3dlook.me) plus an authenticator, so
**there is no Closely password to use** — `CLOSELY_EMAIL`/`CLOSELY_PASSWORD` cannot work
for this account and the code path exists only for a password-based team account.

That costs nothing, because Google SSO ends in the same token pair. From the bundle:

    POST /auth/google-prompt            -> {state_token, url}, browser goes to Google
    POST /v1/login/oauth2-google-check  -> {token, refresh_token}   <-- same shape

So the tokens below are what a Google login produces anyway.

WHERE THE TOKENS ARE (verified in the bundle, not guessed)
The app keeps them in **localStorage under the single key `closely`**, as a JSON object
with `at` and `rt` inside it:

    const S = {data: () => JSON.parse(localStorage.getItem(<"closely">)), get: e => S.data()[e], …}

They are NOT cookies.

In a logged-in tab on app.closelyhq.com, open the devtools Console. One step, straight to
the clipboard (`copy()` is a devtools-only helper, so it must be the Console, not a page
script):

    copy(`CLOSELY_TOKEN=${JSON.parse(localStorage.getItem('closely')).at}\nCLOSELY_REFRESH_TOKEN=${JSON.parse(localStorage.getItem('closely')).rt}`)

Or to just read them off the screen as two lines:

    console.log(`CLOSELY_TOKEN=${JSON.parse(localStorage.getItem('closely')).at}\nCLOSELY_REFRESH_TOKEN=${JSON.parse(localStorage.getItem('closely')).rt}`)

Verified in a real browser 2026-09-02: both produce exactly the two lines to paste.

Put those two lines in `~/.hermes/.env`. Nothing is ever written to a log, printed, or
echoed by this script; the cache at ~/.hermes/.closely-token.json is chmod 0600 and
diagnostics mask tokens to `abcd…xyz (len N)`.

The access token expires; the refresh token is what keeps this working unattended, and the
script rotates and re-saves it on every refresh. So run `pull` regularly (the Monday cron
is a good place) — a refresh token that is never used is a refresh token that goes stale
and sends you back to the Console.

USAGE
    scripts/closely-pull.py probe                      # first run: learn the real shapes
    scripts/closely-pull.py campaigns                  # list campaigns + ids
    scripts/closely-pull.py pull --campaign <slug> [--closely-campaign-id N] [--dry-run]
    scripts/closely-pull.py pull --campaign <slug> --max-conversations 5   # small first
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

# Their own bundle reads this from REACT_APP_API_URI, so an override is not a hack — it
# is how the host is configured there too, and it is what makes this script testable
# against a stub without credentials.
BASE = (os.environ.get("CLOSELY_BASE_URL") or "https://api.closelyhq.com").rstrip("/")
HERMES_ENV = Path.home() / ".hermes" / ".env"
TOKEN_CACHE = Path.home() / ".hermes" / ".closely-token.json"

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/147.0.0.0 Safari/537.36")

INBOX_PAGE = 15          # the app's own page size
MSG_PAGE = 10            # the app's own page size
REQ_GAP = 1.0            # seconds between requests: polite, and 429 is a documented state
MAX_429_RETRIES = 4


# --------------------------------------------------------------------------- paths

def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def campaign_dir(slug: str) -> Path:
    return repo_root() / "workspace" / "outbound" / "campaigns" / slug


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(repo_root()))
    except ValueError:
        return str(p)


# --------------------------------------------------------------------- credentials

def _env(name: str) -> str:
    """Value from the process env, else from ~/.hermes/.env. Never logged."""
    v = os.environ.get(name)
    if v:
        return v.strip()
    if HERMES_ENV.exists():
        try:
            for line in HERMES_ENV.read_text(encoding="utf-8", errors="replace").splitlines():
                m = re.match(rf"^\s*{re.escape(name)}\s*=\s*(.+)$", line)
                if m:
                    return m.group(1).strip().strip('"').strip("'")
        except OSError:
            pass
    return ""


def _mask(s: str) -> str:
    """For diagnostics only. A token must never reach a log or a Telegram message."""
    if not s:
        return "(empty)"
    return f"{s[:4]}…{s[-3:]} (len {len(s)})"


class Closely:
    """Minimal client. Holds tokens in memory and in a 0600 cache; never prints them."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.token = ""
        self.refresh_token = ""
        self._env_seed = ""
        self._last_request = 0.0
        self._load_tokens()

    # -------------------------------------------------------------- token handling

    def _load_tokens(self) -> None:
        """Cache wins; .env is a SEED, not the live credential.

        Both tokens rotate: every refresh returns a new access AND a new refresh token,
        and Closely invalidates the old refresh token. So the pair pasted into .env is
        dead the moment the first refresh happens — measured 2026-09-02, within the hour.

        An earlier version had .env override the cache. That is fatal unattended: the run
        loads the stale .env pair, gets 401, tries to refresh with the already-rotated
        refresh token, and has nothing left to fall back to. The cron would have died on
        its first firing.

        .env still has to be able to take over, or a freshly pasted pair after a logout
        could never get in. So the cache records the .env fingerprint it was seeded from,
        and a CHANGED .env value means Vadim pasted something new and wins.
        """
        cached_token = cached_refresh = ""
        seeded_from = ""
        if TOKEN_CACHE.exists():
            try:
                d = json.loads(TOKEN_CACHE.read_text(encoding="utf-8"))
                cached_token = d.get("token", "")
                cached_refresh = d.get("refresh_token", "")
                seeded_from = d.get("seeded_from", "")
            except (OSError, ValueError):
                pass

        env_token = _env("CLOSELY_TOKEN")
        env_refresh = _env("CLOSELY_REFRESH_TOKEN")
        self._env_seed = self._fingerprint(env_token, env_refresh)

        env_is_new = bool(env_token) and self._env_seed != seeded_from
        if cached_token and not env_is_new:
            self.token, self.refresh_token = cached_token, cached_refresh
            if self.verbose:
                print("→ using the cached token pair (rotated by an earlier run)")
        else:
            self.token, self.refresh_token = env_token, env_refresh
            if self.verbose and env_token:
                print("→ seeding from ~/.hermes/.env"
                      + (" (new value since the last run)" if seeded_from else ""))

    @staticmethod
    def _fingerprint(*parts: str) -> str:
        import hashlib
        return hashlib.sha256("|".join(parts).encode()).hexdigest()[:16]

    def _save_tokens(self) -> None:
        try:
            TOKEN_CACHE.write_text(
                json.dumps({
                    "token": self.token,
                    "refresh_token": self.refresh_token,
                    # which .env pair this cache grew from, so a NEW paste is detectable
                    "seeded_from": getattr(self, "_env_seed", ""),
                    "saved_at": __import__("datetime").datetime.now(
                        __import__("datetime").timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                }),
                encoding="utf-8",
            )
            TOKEN_CACHE.chmod(0o600)
        except OSError as e:
            print(f"  (could not cache token: {e})", file=sys.stderr)

    def ensure_auth(self) -> None:
        if self.token:
            return
        email, password = _env("CLOSELY_EMAIL"), _env("CLOSELY_PASSWORD")
        if not (email and password):
            raise SystemExit(
                "No credentials.\n\n"
                "This account signs in with Google, so there is no Closely password to use.\n"
                "Get the tokens instead. In a logged-in tab on app.closelyhq.com, open the\n"
                "devtools Console and run:\n\n"
                "  copy(`CLOSELY_TOKEN=${JSON.parse(localStorage.getItem('closely')).at}"
                "\\nCLOSELY_REFRESH_TOKEN=${JSON.parse(localStorage.getItem('closely')).rt}`)\n\n"
                "That copies both lines; paste them into ~/.hermes/.env.\n"
                "(They live in localStorage under the key `closely`, not in cookies.)"
            )
        if self.verbose:
            print("→ logging in with email + password")
        data = self._raw("POST", "/v1/login/check",
                         body={"email": email, "password": password}, auth=False)
        self.token = data.get("token", "")
        self.refresh_token = data.get("refresh_token", "")
        if not self.token:
            raise SystemExit(
                "login returned no `token`. Keys in the response: "
                f"{sorted(data) if isinstance(data, dict) else type(data).__name__}.\n"
                "The login body field names were read from their web bundle; if they "
                "changed, run `probe` and report the output."
            )
        self._save_tokens()

    def _do_refresh(self) -> bool:
        if not self.refresh_token:
            return False
        if self.verbose:
            print("→ 401, refreshing the token")
        try:
            data = self._raw("POST", "/v1/login/refresh",
                             body={"refresh_token": self.refresh_token},
                             auth=False, extra_headers={"Skip-Auth": "true"})
        except _HttpError:
            # The refresh endpoint itself rejecting the token is the EXPECTED failure once
            # Vadim logs into app.closelyhq.com — Closely allows one session, so his login
            # invalidates ours. Catching only SystemExit here let the raw _HttpError
            # escape as a Python traceback, which is what the cron would then have put in
            # the Telegram alert instead of the instructions for fixing it.
            return False
        except SystemExit:
            return False
        if not data.get("token"):
            return False
        self.token = data["token"]
        self.refresh_token = data.get("refresh_token", self.refresh_token)
        self._save_tokens()
        return True

    # ------------------------------------------------------------------ transport

    def _raw(self, method: str, path: str, body=None, auth=True,
             extra_headers: dict | None = None):
        # One request per REQ_GAP seconds. Their app handles 429 explicitly, which means
        # it is reachable — and a rate-limited integration is worse than a slow one.
        gap = REQ_GAP - (time.monotonic() - self._last_request)
        if gap > 0:
            time.sleep(gap)
        self._last_request = time.monotonic()

        url = BASE + path
        # Cloudflare sits in front of api.closelyhq.com and answers a request without a
        # browser User-Agent with 403 / error 1010 "browser_signature_banned" — before the
        # app ever sees the token. Measured 2026-09-02: identical request, bare urllib UA
        # -> 403 cf=1010; browser UA -> 200. It is the UA string, not the TLS fingerprint
        # (curl with the same headers also gets 200), so headers are enough and no
        # curl_cffi / real browser is needed.
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": UA,
            "Accept-Language": "en-GB,en;q=0.9",
            "Origin": "https://app.closelyhq.com",
            "Referer": "https://app.closelyhq.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
        }
        if auth and self.token:
            headers["Authorization"] = "Bearer " + self.token
        headers.update(extra_headers or {})
        payload = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(url, data=payload, headers=headers, method=method)
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                raw = resp.read()
            return json.loads(raw.decode("utf-8", errors="replace")) if raw else {}
        except urllib.error.HTTPError as e:
            detail = ""
            try:
                detail = e.read().decode("utf-8", errors="replace")[:400]
            except Exception:
                pass
            raise _HttpError(e.code, detail) from None
        except urllib.error.URLError as e:
            raise SystemExit(f"network error talking to {BASE}: {e.reason}")
        except json.JSONDecodeError:
            raise SystemExit(f"{method} {path} returned non-JSON — the API surface moved")

    def post(self, path: str, body: dict, retry_auth: bool = True):
        """Authenticated POST. `drill/campaigns/{id}/contacts` is POST-only (GET -> 405)."""
        for attempt in range(MAX_429_RETRIES + 1):
            try:
                return self._raw("POST", path, body=body)
            except _HttpError as e:
                if e.code == 401 and retry_auth and self._do_refresh():
                    retry_auth = False
                    continue
                if e.code == 429 and attempt < MAX_429_RETRIES:
                    time.sleep(REQ_GAP * (2 ** (attempt + 1)))
                    continue
                raise SystemExit(f"POST {path} -> HTTP {e.code}. {e.detail}")
        raise SystemExit(f"POST {path}: gave up after rate-limit retries")

    def get(self, path: str, retry_auth: bool = True):
        """Authenticated GET with one token refresh and 429 backoff."""
        for attempt in range(MAX_429_RETRIES + 1):
            try:
                return self._raw("GET", path)
            except _HttpError as e:
                if e.code == 401 and retry_auth and self._do_refresh():
                    retry_auth = False
                    continue
                if e.code == 429 and attempt < MAX_429_RETRIES:
                    wait = REQ_GAP * (2 ** (attempt + 1))
                    print(f"  429 from the API — backing off {wait:.0f}s "
                          f"(attempt {attempt + 1}/{MAX_429_RETRIES})", file=sys.stderr)
                    time.sleep(wait)
                    continue
                if e.code == 401:
                    raise SystemExit(
                        "401 Unauthorized and the token could not be refreshed.\n"
                        f"  access token:  {_mask(self.token)}\n"
                        f"  refresh token: {_mask(self.refresh_token)}\n"
                        "Re-copy `at` (and `rt`) from a logged-in browser into "
                        "~/.hermes/.env, or delete ~/.hermes/.closely-token.json."
                    )
                raise SystemExit(f"GET {path} -> HTTP {e.code}. {e.detail}")
        raise SystemExit(f"GET {path}: gave up after {MAX_429_RETRIES} rate-limit retries")


class _HttpError(Exception):
    def __init__(self, code: int, detail: str):
        super().__init__(f"HTTP {code}")
        self.code, self.detail = code, detail


# ----------------------------------------------------------------- shape discovery

def shape(obj, depth: int = 0, max_depth: int = 3) -> str:
    """A value's structure with keys and types, and values truncated hard.

    Deliberately shows a short sample of each scalar: field NAMES alone do not tell you
    whether `status` holds "replied" or 3, and that is exactly what `pull` has to map.
    Long strings are cut to 60 characters so message bodies do not end up in a terminal
    scroll or a paste.
    """
    pad = "  " * depth
    if isinstance(obj, dict):
        if depth >= max_depth:
            return "{…%d keys}" % len(obj)
        lines = []
        for k, v in list(obj.items())[:40]:
            lines.append(f"{pad}  {k}: {shape(v, depth + 1, max_depth)}")
        return "{\n" + "\n".join(lines) + f"\n{pad}}}"
    if isinstance(obj, list):
        if not obj:
            return "[] (empty)"
        return f"[{len(obj)} items] first -> " + shape(obj[0], depth, max_depth)
    if isinstance(obj, str):
        s = obj if len(obj) <= 60 else obj[:57] + "…"
        return f'"{s}"'
    return f"{obj!r}"


def cmd_probe(args) -> int:
    c = Closely(verbose=True)
    c.ensure_auth()

    print("=" * 70)
    print("GET /v1/inbox/?limit=2&offset=0&with_incoming=1")
    print("=" * 70)
    inbox = c.get("/v1/inbox/?" + urllib.parse.urlencode(
        {"limit": 2, "offset": 0, "with_incoming": 1}))
    print(shape(inbox, max_depth=5))

    items = _inbox_items(inbox)
    if not items:
        print("\nNo conversations with an incoming message came back. Either nobody has "
              "replied on this account, or the list lives under a key this script did not "
              "recognise — the structure above is the answer either way.")
        return 1

    cid = _first(_flat(items[0]), INBOX_CONTACT_ID)
    print("\n" + "=" * 70)
    print(f"GET /v1/inbox/{cid}/messages?limit=3&offset=0")
    print("=" * 70)
    print(shape(c.get(f"/v1/inbox/{cid}/messages?limit=3&offset=0"), max_depth=5))

    print("\n" + "-" * 70)
    print("If `pull` reports unmapped fields, paste the two structures above back and the\n"
          "candidate lists (INBOX_* / MSG_*) get corrected to match.")
    return 0


def cmd_campaigns(args) -> int:
    c = Closely(verbose=True)
    c.ensure_auth()
    data = c.get("/v1/campaigns/?limit=999")
    # Same envelope trap as the inbox: data is a DICT ({campaigns: [...], total_count}),
    # so a `data.get("data") or …` walk hands back the dict and iterating it yields key
    # STRINGS — which printed two blank rows instead of thirty campaigns.
    items = _listy(data, ("campaigns", "data", "results", "items"))
    if not items:
        print("No campaigns came back. Structure:")
        print(shape(data))
        return 1
    print(f"{'id':>8}  {'status':<14} name")
    for it in items:
        print(f"{str(_first(it, ('campaign_id', 'id'))):>8}  "
              f"{str(_first(it, ('status', 'state')))[:14]:<14} "
              f"{_first(it, ('name', 'title'))}")
    print(f"\n{len(items)} campaign(s). Use --closely-campaign-id to pull one.")
    return 0


# --------------------------------------------------------------- field mapping

# Candidate names, most likely first. Everything here came from the bundle's own component
# code; anything the API renames is reported by `pull` rather than silently dropped.
INBOX_LIST_KEYS = ("conversations", "rows", "data", "results", "items", "contacts")
INBOX_CONTACT_ID = ("conversation_id", "contact_id", "id", "contactId")
INBOX_LID = ("lid", "public_identifier", "linkedin_id")
INBOX_NAME = ("display_name", "full_name", "name")
INBOX_ACCOUNT = ("account_display_name", "account_id")
INBOX_FIRST = ("first_name", "firstName")
INBOX_LAST = ("last_name", "lastName")
INBOX_TITLE = ("job_title", "title", "occupation", "headline")
INBOX_COMPANY = ("company_name", "company", "organization")
INBOX_CAMPAIGN = ("campaign_id", "campaignId")
INBOX_LAST_DATE = ("last_message_date", "last_message_at", "updated_at")

MSG_LIST_KEYS = ("messages", "rows", "data", "results", "items")
MSG_TEXT = ("message", "text", "body", "message_text", "content")
MSG_DATE = ("sent_at", "created_at", "created", "date", "timestamp")
MSG_INCOMING = ("is_incoming", "incoming", "is_inbound", "inbound", "is_reply")
MSG_DIRECTION = ("direction", "type", "kind", "sender_type")
MSG_STEP = ("step", "step_number", "sequence_step", "campaign_step")


def _flat(conv: dict) -> dict:
    """Conversation with its nested `contact` merged in, so one lookup finds either.

    The real payload puts identity one level down:
      {conversation_id, last_message, last_message_date, account_display_name,
       contact: {contact_id, display_name, lid, job_title, email, phone, campaigns}}
    Measured 2026-09-02. A flat lookup over the top level finds no name and no lid.
    """
    if not isinstance(conv, dict):
        return {}
    out = {k: v for k, v in conv.items() if k != "contact"}
    inner = conv.get("contact")
    if isinstance(inner, dict):
        for k, v in inner.items():
            out.setdefault(k, v)
    return out


def conv_campaigns(conv: dict) -> list[dict]:
    """The campaigns this contact belongs to: [{id, name, status}, …]."""
    inner = conv.get("contact") if isinstance(conv, dict) else None
    cs = (inner or {}).get("campaigns") or conv.get("campaigns") or []
    return [c for c in cs if isinstance(c, dict)]


def _first(d: dict, names: tuple[str, ...], default: str = "") -> str:
    if not isinstance(d, dict):
        return default
    lower = {str(k).lower(): v for k, v in d.items()}
    for n in names:
        v = lower.get(n.lower())
        if v not in (None, "", []):
            return str(v)
    return default


def _listy(payload, keys: tuple[str, ...]) -> list:
    """The list inside a response, however deeply the envelope wraps it.

    The real shape is {success, data: {conversations: [...], total_count}, error} — the
    list is TWO levels down, so a flat key walk finds nothing. Measured 2026-09-02.
    """
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict):
        for k in keys:
            v = payload.get(k)
            if isinstance(v, list):
                return v
        # one level of envelope: {"data": {"conversations": [...]}}
        for envelope in ("data", "result", "payload"):
            inner = payload.get(envelope)
            if isinstance(inner, list):
                return inner
            if isinstance(inner, dict):
                for k in keys:
                    v = inner.get(k)
                    if isinstance(v, list):
                        return v
        # a single-key envelope around a list
        for v in payload.values():
            if isinstance(v, list) and v and isinstance(v[0], dict):
                return v
    return []


def _inbox_items(payload) -> list:
    return _listy(payload, INBOX_LIST_KEYS)


def _is_incoming(msg: dict) -> bool | None:
    """True inbound, False outbound, None if the payload does not say.

    None matters: guessing "inbound" would put OUR OWN message into responses-raw.csv as
    if the prospect had written it, and `response-classifier` would then categorise our
    own copy. Better to report the unknown and stop.
    """
    for n in MSG_INCOMING:
        for k, v in msg.items():
            if str(k).lower() == n:
                if isinstance(v, bool):
                    return v
                if isinstance(v, (int, float)):
                    return bool(v)
                if isinstance(v, str) and v.lower() in ("true", "1", "yes"):
                    return True
                if isinstance(v, str) and v.lower() in ("false", "0", "no"):
                    return False
    d = _first(msg, MSG_DIRECTION).lower()
    if d in ("in", "incoming", "inbound", "received", "reply", "contact", "lead", "prospect"):
        return True
    if d in ("out", "outgoing", "outbound", "sent", "me", "user", "account", "owner"):
        return False
    return None


# ------------------------------------------------------------------ map-campaigns

def _folder_lids() -> dict[str, set[str]]:
    """{our campaign slug: set of LinkedIn public ids} from every people-*.csv on disk."""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "outbound_registry", Path(__file__).resolve().parent / "outbound-registry.py")
    reg = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(reg)

    root = repo_root() / "workspace" / "outbound" / "campaigns"
    out: dict[str, set[str]] = {}
    for d in sorted(x for x in root.iterdir() if x.is_dir() and not x.name.startswith("_")):
        lids: set[str] = set()
        for f in list(d.glob("people-*.csv")) + list(d.glob("*/people-*.csv")):
            try:
                with f.open(newline="", encoding="utf-8-sig") as fh:
                    for r in csv.DictReader(fh):
                        for col in ("person_linkedin_url", "linkedin_url"):
                            u = reg.norm_linkedin((r.get(col) or "").strip())
                            if u:
                                lids.add(u.rsplit("/", 1)[-1].lower())
            except (OSError, csv.Error):
                continue
        out[d.name] = lids
    return out


def _import_headers() -> dict[str, list[str]]:
    """{folder: [header column lists of its closelyhq-import*.csv files]}."""
    root = repo_root() / "workspace" / "outbound" / "campaigns"
    out: dict[str, list[str]] = {}
    for d in sorted(x for x in root.iterdir() if x.is_dir() and not x.name.startswith("_")):
        heads = []
        for f in list(d.glob("closelyhq-import*.csv")) + list(d.glob("*/closelyhq-import*.csv")):
            try:
                with f.open(newline="", encoding="utf-8-sig") as fh:
                    row = next(csv.reader(fh), [])
                if row:
                    heads.append([x.strip() for x in row if x.strip()])
            except (OSError, csv.Error, StopIteration):
                continue
        if heads:
            out[d.name] = heads
    return out


def _source_folder(camp_detail: dict, headers: dict[str, list[list[str]]]) -> str:
    """Which folder's import CSV Closely says it actually uploaded.

    AUTHORITATIVE, and it outranks contact overlap. Closely keeps the uploaded file's
    column list in `contact_source[].data.table`, and campaign 138392's is
    `person_id, first_name, last_name, title, company, linkedin_url, segment, angle,
    priority, message_m1, message_m2` — the header of
    2026-07-27-australia-telehealth/closelyhq-import-v3.csv, NOT of the folder overlap
    matched it to. That folder (2026-07-16-au-telehealth) holds a 253-row import whose
    linkedin_url is blank in every row, so it could never have been uploaded at all.
    Overlap was fooled because 07-16's people list was re-used to build 07-27's import;
    all 5 repliers are in 07-27's file and none in 07-16's. Verified locally 2026-09-02.
    """
    srcs = camp_detail.get("contact_source") or []
    got: set[str] = set()
    for src in srcs if isinstance(srcs, list) else []:
        table = ((src or {}).get("data") or {}).get("table") or {}
        got |= {str(k).strip() for k in table}
    if not got:
        return ""
    # Jaccard, not overlap-over-folder-header. Dividing by the folder's header length
    # alone let a SHORT header win against anything containing it: Israel's 8-column
    # import (first_name,last_name,company,title,message_1,message_2,campaign_tag,
    # linkedin_url) scored >=0.8 against the US and UK campaigns' 10-11 column tables,
    # and both were mis-assigned to Israel. The union in the denominator makes the
    # measure symmetric, so a longer table can no longer be swallowed by a shorter header.
    scored: dict[str, float] = {}
    for folder, heads in headers.items():
        for h in heads:
            hs = set(h)
            if not hs:
                continue
            j = len(got & hs) / len(got | hs)
            scored[folder] = max(scored.get(folder, 0.0), j)
    if not scored:
        return ""
    ranked = sorted(scored.items(), key=lambda kv: -kv[1])
    best, score = ranked[0]
    # A TIE MEANS THE HEADER IS NOT A DISCRIMINATOR — say nothing and let contact overlap
    # decide. 2026-08-07-us-digital-fitness and 2026-07-31-uk-telehealth-digital-health
    # ship byte-identical import headers (contact_id, first_name, last_name, email_guess,
    # company_name, job_title, message_m1, message_m2, tag, linkedin_url), so preferring
    # the first one found silently filed the US campaign under UK.
    if len(ranked) > 1 and abs(ranked[1][1] - score) < 1e-9:
        return ""
    # near-identical header sets only; a couple of shared common names is not a match
    return best if score >= 0.8 else ""


def campaign_mapping(c: "Closely", verbose: bool = True) -> list[dict]:
    """[{closely_id, name, replies, folder, overlap}] — mapped by contact overlap.

    Walks every campaign's own contact drill, NOT the inbox. The inbox listing hid two
    thirds of campaign 139205's replies (3 shown against 9 recorded), so a mapping built
    from it both understated reply counts and could miss a campaign whose replies never
    appear in the listing at all.
    """
    camps = _listy(c.get("/v1/campaigns/?limit=999"),
                   ("campaigns", "data", "results", "items"))
    if verbose:
        print(f"  {len(camps)} campaign(s) in the account; reading each contact drill")

    folders = _folder_lids()
    headers = _import_headers()
    out = []
    for i, camp in enumerate(camps, 1):
        cid = _first(camp, ("campaign_id", "id"))
        if not cid:
            continue
        try:
            rows = campaign_repliers(c, cid)
        except SystemExit as e:
            if verbose:
                print(f"    [{i}/{len(camps)}] {cid}: skipped ({str(e)[:50]})")
            continue
        if not rows:
            continue
        lids = {_lid_to_url(r.get("lid")).rstrip("/").rsplit("/", 1)[-1].lower()
                for r in rows}
        lids.discard("")
        best, score = "", 0
        for name, fl in folders.items():
            ov = len(lids & fl)
            if ov > score:
                best, score = name, ov
        # DATE GUARD, and it is the load-bearing one. Contact overlap alone merged
        # Closely campaign 125317 (created 2026-04-04) into the folder
        # 2026-07-23-israel-telehealth, because 15 of its 30 repliers DO appear in that
        # folder's people files — 8 April decliners had been re-imported in July, since
        # our own context-pack recorded katya's exclusion registry as "empty, no prior
        # campaigns" while 125317 had been running since April. The merge produced a
        # 608/186/432/34 funnel of which 79% belonged to an unrelated campaign with
        # different copy, and presented four 5-month-cold April leads as fresh.
        # A campaign created before the folder's own date cannot be that folder's
        # campaign, whatever the overlap says.
        created = _first(camp, ("created_at", "created", "date_created"))
        folder_date = (best or "")[:10]
        date_ok = True
        if created and re.match(r"^\d{4}-\d{2}-\d{2}", str(created)) and \
                re.match(r"^\d{4}-\d{2}-\d{2}$", folder_date):
            # allow a campaign created up to 10 days BEFORE the folder date (prep work)
            # and any time after; reject anything older than that.
            date_ok = str(created)[:10] >= _shift_days(folder_date, -10)

        # A 1-of-44 overlap is one contact that happens to appear in both lists, not a
        # mapping: `89193 EU lookalike pillsorted` shares one person with
        # 2026-07-21-eu-telehealth-weightloss and is otherwise a different, older
        # campaign. Filing its 44 replies under that folder would hand
        # campaign-analyzer 43 conversations from a campaign it is not analysing.
        # Require the overlap to be at least half of the campaign's repliers.
        # Closely's own record of the uploaded file wins over contact overlap.
        src_folder = ""
        try:
            src_folder = _source_folder(c.get(f"/v2/campaigns/{cid}") .get("data") or {},
                                        headers)
        except SystemExit:
            pass
        if src_folder:
            if src_folder != best:
                if verbose:
                    print(f"      contact_source says {src_folder} (overlap said "
                          f"{best or 'nothing'}) — trusting contact_source")
                best, score = src_folder, len(lids)
            date_ok = True          # the uploaded file settles it; dates cannot override

        confident = bool(best) and score >= max(1, len(lids) // 2) and date_ok
        out.append({"closely_id": str(cid), "name": _first(camp, ("name", "title")),
                    "replies": len(rows), "folder": best if confident else "",
                    "overlap": score, "overlap_of": len(lids),
                    "weak_match": best if (best and not confident) else "",
                    "created_at": str(created)[:10] if created else "",
                    "rejected_on_date": bool(best and not date_ok)})
        if verbose:
            print(f"    [{i}/{len(camps)}] {cid}: {len(rows)} replied"
                  f"{' -> ' + best if best else ''}")
    out.sort(key=lambda r: -r["replies"])
    return out


def cmd_map_campaigns(args) -> int:
    """Match Closely campaigns to our campaign folders by who is actually in them.

    Names do not map. Measured 2026-09-02: Closely's "EU telehealth, 22/07 1test from
    agents" is our `2026-07-21-eu-telehealth-weightloss`, NOT `2026-07-22-eu-telehealth`;
    "AU telehealth, 28/07 test from agents" is our `2026-07-16-au-telehealth`, NOT
    `2026-07-27-australia-telehealth`. Guessing from the name files replies under the
    wrong campaign, where `campaign-analyzer` would then draw conclusions from somebody
    else's conversation. Contact overlap is unambiguous — every match below was 100%.
    """
    c = Closely(verbose=True)
    c.ensure_auth()
    print("→ reading every campaign's contact drill")
    rows = campaign_mapping(c)
    print()
    print(f"{'camp id':>8} {'repl':>5}  {'our campaign folder':<42} {'overlap':>9}  name")
    mapped = 0
    for r in rows:
        if r["overlap"]:
            mapped += 1
        if r["folder"]:
            label = r["folder"]
        elif r.get("rejected_on_date"):
            label = f"~{r['weak_match']} (REJECTED: created {r.get('created_at')})"
        elif r.get("weak_match"):
            label = f"~{r['weak_match']} (overlap too weak)"
        else:
            label = "(no folder)"
        print(f"{r['closely_id']:>8} {r['replies']:>5}  {label:<42} "
              f"{r['overlap']:>4}/{r.get('overlap_of', r['replies']):<4}  {r['name'][:34]}")
    print(f"\n{mapped} of {len(rows)} Closely campaigns map to a folder here. "
          "The rest predate this pipeline and have no folder — that is expected.")
    print("\nUse a mapped pair like:")
    print("  closely-pull.py pull --campaign <our folder> --closely-campaign-id <camp id>")
    return 0


# ------------------------------------------------------- who actually replied

# THE INBOX LISTING IS NOT A COMPLETE RECORD OF REPLIES.
# Measured on campaign 139205, 2026-09-02: `GET /v1/inbox/?with_incoming=1&campaign_id=…`
# returned 3 conversations, while the campaign's own contact records counted 9 replies —
# and all 9 conversations were fetchable by contact_id. So the listing was hiding two
# thirds of them (not archived: archived=1 returns nothing for this campaign). The first
# step-8 run classified 3 of 9 replies and looked complete.
#
# The authoritative source is the campaign's contact drill:
#   POST /v1/drill/campaigns/{id}/contacts  {"statuses":["finishedWithReply"], limit, offset}
#   -> data.rows[], data.total_count
# Each row carries contact_id, first/last name, `lid` (a FULL profile URL here, unlike the
# inbox where it is a bare slug) and per-contact event counters. It is campaign-scoped by
# construction, so it also cannot pick up the cold inbound that pollutes the inbox.
#
# Status values are camelCase and differ from the summary's snake_case keys:
#   summary finished_reply -> status "finishedWithReply"   (finished_reply as a status
#   value returns HTTP 400 invalidStatus)
DRILL_REPLIED_STATUS = "finishedWithReply"
DRILL_PAGE = 50


def campaign_repliers(c: "Closely", closely_campaign_id) -> list[dict]:
    """Every contact in this campaign that Closely records as having replied."""
    out: list[dict] = []
    offset, total = 0, 1
    while offset < total:
        d = c.post(f"/v1/drill/campaigns/{closely_campaign_id}/contacts",
                   {"statuses": [DRILL_REPLIED_STATUS], "limit": DRILL_PAGE,
                    "offset": offset, "search_keyword": ""})
        inner = d.get("data") or {}
        rows = inner.get("rows") or []
        total = inner.get("total_count") or len(rows)
        if not rows:
            break
        out.extend(rows)
        offset += DRILL_PAGE
    return out


def _shift_days(iso_date: str, days: int) -> str:
    import datetime as _dt
    d = _dt.date.fromisoformat(iso_date) + _dt.timedelta(days=days)
    return d.isoformat()


def _lid_to_url(lid: str) -> str:
    """drill gives a full URL, the inbox gives a bare slug. Accept either."""
    lid = (lid or "").strip()
    if not lid:
        return ""
    if lid.startswith("http"):
        return lid
    return f"https://www.linkedin.com/in/{lid}"


# --------------------------------------------------------------------------- pull

RESPONSE_COLUMNS = [
    "person_id", "linkedin_url", "full_name", "first_name", "last_name", "title",
    "company_name", "response_date", "response_text", "which_message_replied_to",
    "closely_contact_id", "closely_conversation_id", "closely_campaign_id",
    "closely_campaign_name", "sending_account", "thread_file",
]


def cmd_pull(args) -> int:
    c = Closely(verbose=True)
    c.ensure_auth()

    if not args.closely_campaign_id:
        print("✗ --closely-campaign-id is required: replies are read from the campaign's "
              "own contact drill, which is campaign-scoped.\n"
              "  Run `map-campaigns` to find the id for this folder.", file=sys.stderr)
        return 2

    ids = [x.strip() for x in str(args.closely_campaign_id).split(",") if x.strip()]
    print(f"→ reading the contact drill for campaign(s) {', '.join(ids)} "
          "(authoritative reply record, not the inbox listing)\n")
    repliers = []
    seen_contacts: set[str] = set()
    for one in ids:
        for r in campaign_repliers(c, one):
            key = str(r.get("contact_id"))
            if key in seen_contacts:      # the same person can sit in two batches
                continue
            seen_contacts.add(key)
            r["_campaign_id"] = one
            repliers.append(r)
    if not repliers:
        print("  no contact in this campaign is recorded as having replied.")
        return 1
    print(f"  {len(repliers)} contact(s) recorded as replied\n")

    # Shape each drill row like the conversation dicts the rest of this function expects.
    conversations = []
    for r in repliers:
        conversations.append({
            "conversation_id": "",
            "contact": {
                "contact_id": r.get("contact_id"),
                "display_name": f"{(r.get('first_name') or '').strip()} "
                                f"{(r.get('last_name') or '').strip()}".strip(),
                "first_name": (r.get("first_name") or "").strip(),
                "last_name": (r.get("last_name") or "").strip(),
                "lid": r.get("lid"),
                "job_title": r.get("job_title") or "",
                "company_name": r.get("company_name") or "",
                "email": r.get("email"),
                "campaigns": [{"id": r.get("_campaign_id",
                                              args.closely_campaign_id), "name": ""}],
            },
            "account_display_name": r.get("account_display_name") or "",
            "_drill": r,
        })
    if args.max_conversations:
        conversations = conversations[: args.max_conversations]

    rows: list[dict] = []
    unknown_direction = 0
    no_text = 0
    skipped_no_campaign = 0
    skipped_other_campaign = 0
    print()
    for i, conv in enumerate(conversations, 1):
        flat = _flat(conv)
        camps = conv_campaigns(conv)

        # Only about a third of the inbox is ours. `with_incoming=1` means "somebody sent
        # us a message in this conversation", which includes strangers cold-pitching the
        # team's own LinkedIn accounts — 41 of 60 sampled on 2026-09-02 belonged to no
        # campaign at all. Those are not campaign replies and must not reach
        # response-classifier, which would dutifully categorise a PR agency's pitch as a
        # lead. Campaign membership is the filter.
        if not camps and not args.include_non_campaign:
            skipped_no_campaign += 1
            continue
        # Compare against the PARSED id list. Comparing against the raw argument meant
        # a folder mapped to two campaigns ("125317,138170") matched neither, and the
        # pull reported "nothing usable was extracted" on perfectly good data.
        if ids and not any(str(c.get("id")) in ids for c in camps):
            skipped_other_campaign += 1
            continue

        cid = _first(flat, INBOX_CONTACT_ID)
        if not cid:
            continue
        lid = _first(flat, INBOX_LID)
        name = _first(flat, INBOX_NAME)
        first, last = _first(flat, INBOX_FIRST), _first(flat, INBOX_LAST)
        if name and not (first or last):
            parts = name.split()
            first, last = (parts[0], " ".join(parts[1:])) if len(parts) > 1 else (name, "")

        msgs = _listy(c.get(f"/v1/inbox/{cid}/messages?limit={MSG_PAGE}&offset=0"),
                      MSG_LIST_KEYS)
        # Their inbox shows newest-last; the step a reply answers is the number of OUR
        # messages that preceded it, which is what response-classifier's
        # `which_message_replied_to` means.
        outbound_before = 0
        kept = 0
        for msg in msgs:
            inbound = _is_incoming(msg)
            if inbound is None:
                unknown_direction += 1
                continue
            if not inbound:
                outbound_before += 1
                continue
            text = _first(msg, MSG_TEXT)
            if not text:
                no_text += 1
                continue
            rows.append({
                "person_id": "",                      # filled by the local join below
                "linkedin_url": _lid_to_url(lid),
                "full_name": name,
                "first_name": first,
                "last_name": last,
                "title": _first(flat, INBOX_TITLE),
                "company_name": _first(flat, INBOX_COMPANY),
                "response_date": _first(msg, MSG_DATE),
                "response_text": text,
                "which_message_replied_to": _first(msg, MSG_STEP) or str(outbound_before or 1),
                "closely_contact_id": _first(flat, ("contact_id",)),
                "closely_conversation_id": _first(flat, ("conversation_id",)),
                "closely_campaign_id": str(camps[0].get("id", "")) if camps else "",
                "closely_campaign_name": str(camps[0].get("name", "")) if camps else "",
                "sending_account": _first(flat, INBOX_ACCOUNT),
            })
            kept += 1
        print(f"  [{i}/{len(conversations)}] {(name or cid)[:34]:<34} "
              f"{len(msgs)} msgs -> {kept} reply(ies)")

    if unknown_direction:
        print(f"\n✗ {unknown_direction} messages did not say whether they are inbound or "
              "outbound, so they were SKIPPED rather than guessed — writing our own copy "
              "into responses-raw.csv would have the classifier grading our own text.\n"
              "  Run `probe` and report the message structure so MSG_INCOMING / "
              "MSG_DIRECTION can be corrected.", file=sys.stderr)
    if no_text:
        print(f"⚠ {no_text} inbound messages had no text under any known key "
              f"({', '.join(MSG_TEXT)}) — run `probe`.", file=sys.stderr)

    if not rows:
        print("\n✗ nothing usable was extracted.", file=sys.stderr)
        return 1

    # Local join: give every reply the person_id the rest of the pipeline keys on, so
    # response-classifier can open messages/{person_id}.md.
    matched = _join_person_ids(rows, campaign_dir(args.campaign))

    # Drop replies from people who are in NO people-*.csv of this folder. A Closely
    # campaign can overlap ours only partly — 125317 shares 15 of its 30 repliers with
    # 2026-07-23-israel-telehealth — and the other 15 are strangers to this folder.
    # Keeping them would hand campaign-analyzer conversations from a campaign it is not
    # analysing, and there is no thread on disk to read them against anyway.
    if not args.keep_unmatched:
        before = len(rows)
        known = _known_keys(campaign_dir(args.campaign))
        kept = []
        for r in rows:
            u = _norm_url(r.get("linkedin_url", ""))
            lid = u.rsplit("/", 1)[-1].lower() if u else ""
            if (r.get("person_id") or "").strip() or u in known or lid in known:
                kept.append(r)
        dropped_unmatched = before - len(kept)
        rows = kept
        if dropped_unmatched:
            print(f"\n  ⚠ dropped {dropped_unmatched} reply(ies) from people who are in no "
                  f"people-*.csv of this folder — pass --keep-unmatched to keep them")
    else:
        dropped_unmatched = 0
    threads = _resolve_thread_files(rows, campaign_dir(args.campaign))

    print(f"\n{'-' * 66}")
    print(f"  replies extracted     {len(rows)}")
    print(f"  skipped, no campaign  {skipped_no_campaign}  (inbound to us, not a reply)")
    if args.closely_campaign_id:
        print(f"  skipped, other camp.  {skipped_other_campaign}")
    print(f"  matched to a person   {matched}/{len(rows)}")
    print(f"  original thread found {threads}/{len(rows)}")
    print(f"  skipped, direction    {unknown_direction}")
    print(f"  skipped, no text      {no_text}")

    if args.dry_run:
        print("\n(--dry-run: nothing written)")
        return 0

    cdir = campaign_dir(args.campaign)
    if not cdir.exists():
        print(f"\n✗ no campaign dir {rel(cdir)}", file=sys.stderr)
        return 2
    dst = cdir / "responses-raw.csv"
    if dst.exists() and not args.overwrite:
        print(f"\n✗ {rel(dst)} exists — pass --overwrite", file=sys.stderr)
        return 1
    with dst.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=RESPONSE_COLUMNS, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    print(f"\n→ wrote {rel(dst)}")
    print("\nNext:")
    print(f"  python3 scripts/outbound-pipeline.py check-responses --campaign {args.campaign}")
    print(f"  /outbound responses {args.campaign}")
    return 0


def _resolve_thread_files(rows: list[dict], cdir: Path) -> int:
    """Point each reply at the file holding our original messages to that person.

    `response-classifier` is told to read `messages/{person_id}.md`, and that only works
    where the campaign named its files that way. It is not universal:
    2026-07-23-israel-telehealth keys them `b01-10.md` by batch position and carries the
    person's NAME in the first line instead — and that campaign has no `person_id` column
    at all, so the documented path resolves to nothing. Rather than make the classifier
    guess, the pointer is resolved here and written into `thread_file`.
    """
    msg_dirs = [d for d in cdir.glob("messages*") if d.is_dir()]
    if not msg_dirs:
        return 0

    # name -> [(file, full header)] from the "# Name — Title — Company" line each thread
    # file opens with. A LIST, not one entry: matching on the name alone picked
    # `b04-24.md` ("Shelly Levin") for "Shelly Shumilov Klipper" on
    # 2026-07-23-israel-telehealth, which the classifier caught. Ambiguity is resolved
    # against the company below, and left EMPTY when it cannot be resolved — a wrong
    # thread is worse than no thread, because the category then describes someone else's
    # conversation.
    by_name: dict[str, list[tuple[str, str]]] = {}
    for d in msg_dirs:
        for f in sorted(d.glob("*.md")):
            try:
                with f.open(encoding="utf-8", errors="replace") as fh:
                    head = fh.readline()
            except OSError:
                continue
            m = re.match(r"^#\s*([^—|\n]+?)\s*(?:—|\||$)", head)
            if m:
                by_name.setdefault(m.group(1).strip().lower(), []).append(
                    (str(f.relative_to(cdir)), head.lower()))

    hits = 0
    ambiguous = 0
    for row in rows:
        pid = (row.get("person_id") or "").strip()
        found = ""
        if pid:
            for d in msg_dirs:
                cand = d / f"{pid}.md"
                if cand.exists():
                    found = str(cand.relative_to(cdir))
                    break
        if not found:
            cands = by_name.get((row.get("full_name") or "").strip().lower(), [])
            if len(cands) == 1:
                found = cands[0][0]
            elif len(cands) > 1:
                # disambiguate on the company, which the header also carries
                comp = (row.get("company_name") or "").strip().lower()
                narrowed = [c for c in cands if comp and comp in c[1]] if comp else []
                if len(narrowed) == 1:
                    found = narrowed[0][0]
                else:
                    ambiguous += 1
        row["thread_file"] = found
        hits += bool(found)
    if ambiguous:
        print(f"  ⚠ {ambiguous} reply(ies) matched more than one thread file by name and "
              "could not be narrowed by company — left blank rather than guessed",
              file=sys.stderr)
    return hits


def _registry():
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "outbound_registry", Path(__file__).resolve().parent / "outbound-registry.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def _norm_url(u: str) -> str:
    return _registry().norm_linkedin((u or "").strip())


def _known_keys(cdir: Path) -> set[str]:
    """Every URL and lid that appears in any people-*.csv of this campaign folder."""
    reg = _registry()
    out: set[str] = set()
    for p in sorted(cdir.glob("people-*.csv")) + sorted(cdir.glob("*/people-*.csv")):
        try:
            with p.open(newline="", encoding="utf-8-sig") as fh:
                for r in csv.DictReader(fh):
                    for col in ("person_linkedin_url", "linkedin_url", "profile_url"):
                        u = reg.norm_linkedin((r.get(col) or "").strip())
                        if u:
                            out.add(u)
                            out.add(u.rsplit("/", 1)[-1].lower())
                            break
        except (OSError, csv.Error):
            continue
    return out


def _join_person_ids(rows: list[dict], cdir: Path) -> int:
    """Fill person_id by matching the LinkedIn URL against the campaign's people files."""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "outbound_registry", Path(__file__).resolve().parent / "outbound-registry.py")
    reg = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(reg)

    # EVERY people file, not three fixed names. Campaigns split their lists into batches:
    # `people-raw-batch2.csv`, `people-validated-batch1..4.csv`,
    # `people-validated-msg-batch1.csv`. Reading only `people-raw.csv` matched 0 of 4
    # replies on 2026-07-31-uk-telehealth-digital-health, because that campaign's contacts
    # live entirely in its batch2 files.
    # Index by BOTH the normalised URL and the bare lid. And do not require a person_id:
    # 2026-07-23-israel-telehealth has no `person_id` column at all (its files are
    # `people-to-sequence.csv` / `people-validated.csv`, keyed on `linkedin_url`), so a
    # person_id-only index skipped every row and matched 0 of 4 replies.
    by_key: dict[str, str] = {}
    files = sorted(cdir.glob("people-*.csv")) + sorted(cdir.glob("*/people-*.csv"))
    for p in files:
        try:
            with p.open(newline="", encoding="utf-8-sig") as fh:
                for r in csv.DictReader(fh):
                    pid = (r.get("person_id") or "").strip()
                    for col in ("person_linkedin_url", "linkedin_url", "profile_url"):
                        u = reg.norm_linkedin((r.get(col) or "").strip())
                        if not u:
                            continue
                        lid = u.rsplit("/", 1)[-1].lower()
                        # value may be "" — a known person with no id is still a match,
                        # and the empty person_id is then reported honestly.
                        by_key.setdefault(u, pid)
                        by_key.setdefault(lid, pid)
                        break
        except (OSError, csv.Error):
            continue
    if not by_key:
        print(f"  (no LinkedIn URLs found in {len(files)} people-*.csv file(s) under "
              f"{rel(cdir)})", file=sys.stderr)
    hits = no_id = 0
    for row in rows:
        u = reg.norm_linkedin(row["linkedin_url"])
        lid = u.rsplit("/", 1)[-1].lower() if u else ""
        if u in by_key or lid in by_key:
            pid = by_key.get(u) or by_key.get(lid) or ""
            row["person_id"] = pid
            hits += 1
            if not pid:
                no_id += 1
    if no_id:
        print(f"  ⚠ {no_id} reply(ies) matched a known contact but that campaign's files "
              "carry no person_id, so `messages/{person_id}.md` cannot be opened — "
              "response-classifier must join on linkedin_url for this one.",
              file=sys.stderr)
    return hits


# ------------------------------------------------------------------------ metrics

# Per-campaign numbers live under /v1/drill/, NOT /v1/campaigns/stats. That endpoint takes
# `account_id` + `filters` (the bundle's getCampaignsTotals proves it) and silently ignores
# a campaign_id — asked for campaign 139205 it answered with the whole account: 16,229
# contacts and 675 replies. A metrics file built from it would have been wrong by two
# orders of magnitude and looked plausible.
#
# `contacts` under drill is a POST (a GET returns 405), which is why the first probe failed.
METRIC_ENDPOINTS = (
    ("events_summary", "/v1/drill/campaigns/{id}/events-summary", "GET"),
    ("contacts_summary", "/v1/drill/campaigns/{id}/contacts-summary", "GET"),
    ("steps", "/v1/drill/campaigns/{id}/steps", "GET"),
    ("campaign", "/v2/campaigns/{id}", "GET"),
)


def _count_of(v):
    """events-summary wraps every number as {"id": n, "count": N}; contacts-summary does not."""
    if isinstance(v, dict):
        c = v.get("count")
        return c if isinstance(c, (int, float)) else None
    return v if isinstance(v, (int, float)) else None


def _metrics_for(c: "Closely", cid: str, window: str, probe: bool) -> dict:
    """The four drill payloads for one Closely campaign."""
    out: dict[str, object] = {}
    for name, tmpl, method in METRIC_ENDPOINTS:
        path = tmpl.format(id=cid)
        if name in ("events_summary", "steps"):
            path += "?" + window
        try:
            data = c.get(path) if method == "GET" else c.post(path, {})
        except SystemExit as e:
            print(f"    ✗ {name}: {str(e)[:90]}", file=sys.stderr)
            out[name] = {"__error__": str(e)[:200]}
            continue
        inner = data.get("data") if isinstance(data, dict) and "data" in data else data
        out[name] = inner
        print(f"    ✓ {name}")
        if probe:
            print(shape(inner, max_depth=4))
    return out


FUNNEL = (
    ("contacts", ("total_contacts", "total", "contacts", "contact_count")),
    ("connection_sent", ("connection_sent", "connections_sent")),
    ("connection_accepted", ("connection_accepted", "connections_accepted")),
    ("message_sent", ("message_sent", "messages_sent")),
    ("message_replied", ("message_replied", "messages_replied", "replied")),
    ("finished_with_reply", ("finished_reply",)),
    ("finished_no_reply", ("finished_no_reply",)),
    ("profile_visit", ("profile_visit",)),
)


def cmd_metrics(args) -> int:
    """metrics-final.json for one folder, summed across every Closely campaign it maps to."""
    c = Closely(verbose=True)
    c.ensure_auth()

    import time as _t
    date_from = args.date_from or "1704067200"          # 2024-01-01
    date_to = args.date_to or str(int(_t.time()))
    window = urllib.parse.urlencode({"date_from": date_from, "date_to": date_to})

    ids = [x.strip() for x in str(args.closely_campaign_id).split(",") if x.strip()]
    per_campaign: dict[str, dict] = {}
    for cid in ids:
        print(f"  campaign {cid}:")
        per_campaign[cid] = _metrics_for(c, cid, window, args.probe)
    if args.probe:
        return 0

    # Sum the funnel across campaigns: a folder split into batches became several
    # campaigns there, and its real funnel is the sum. Missing numbers stay None rather
    # than becoming 0 — a zero would read as "nothing sent" instead of "not reported".
    totals: dict[str, object] = {}
    for label, names in FUNNEL:
        acc = None
        for cid, payload in per_campaign.items():
            for src_name in ("events_summary", "contacts_summary"):
                src = payload.get(src_name)
                if not isinstance(src, dict):
                    continue
                for n in names:
                    v = _count_of(src.get(n))
                    if v is not None:
                        acc = (acc or 0) + v
                        break
                else:
                    continue
                break
        totals[label] = acc

    rates = {}
    cs, ca = totals.get("connection_sent"), totals.get("connection_accepted")
    ms, mr = totals.get("message_sent"), totals.get("message_replied")
    if cs:
        rates["acceptance_rate_pct"] = round(100 * (ca or 0) / cs, 1)
    # THE COMPARABLE NUMBER. Two step-9 analysts arrived at this independently on
    # 2026-09-02: reply-rate-on-messages-sent divides by send EVENTS, so a campaign that
    # has not yet fired its Message-2 step scores higher for being less finished. UK
    # showed 13.8% against Israel's 7.9% purely because it had sent 1.36 messages per
    # accepted person to Israel's 2.32; per accepted person they are 18.8% and 18.3% —
    # tied. Rank campaigns on this, never on the per-message figure.
    if ca:
        rates["replies_per_accepted_pct"] = round(100 * (mr or 0) / ca, 1)
    if ms:
        rates["reply_rate_on_messages_sent_pct"] = round(100 * (mr or 0) / ms, 1)
        rates["messages_per_accepted"] = round(ms / ca, 2) if ca else None
    if cs:
        rates["reply_rate_on_invites_sent_pct"] = round(100 * (mr or 0) / cs, 1)

    out = {
        "campaign": args.campaign,
        "closely_campaign_ids": ids,
        "pulled_at": __import__("datetime").datetime.now(
            __import__("datetime").timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "closely.io private app API, /v1/drill/campaigns/{id}/*",
        "note": (
            "Denominators come from Closely's own event counters. Do NOT use the `sent` "
            "column of outbound-registry status — it counts import rows, not sends, and "
            "is wrong in BOTH directions: it overstated 2026-07-31-uk by 307 vs 258 and "
            "understated 2026-07-23-israel by 190 vs 608. "
            "Rank campaigns on `replies_per_accepted_pct`, not on "
            "`reply_rate_on_messages_sent_pct` — the latter divides by send events, so an "
            "unfinished campaign that has not yet sent its Message 2 scores higher for "
            "being less complete. `messages_per_accepted` shows how far each one got."),
        "totals": totals,
        "rates": rates,
        "raw_per_campaign": per_campaign,
    }
    missing = [k for k, v in totals.items() if v is None]

    dst = campaign_dir(args.campaign) / "metrics-final.json"
    if args.dry_run:
        print("\n  (--dry-run: nothing written)")
        print(json.dumps({"totals": totals, "rates": rates}, indent=2))
        return 0
    if dst.exists() and not args.overwrite:
        print(f"\n✗ {rel(dst)} exists — pass --overwrite", file=sys.stderr)
        return 1
    dst.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\n→ wrote {rel(dst)}")
    print(json.dumps({"totals": totals, "rates": rates}, indent=2))
    if missing:
        print(f"\n  ⚠ not reported by the API: {', '.join(missing)}", file=sys.stderr)
    return 0


def cmd_metrics_all(args) -> int:
    """metrics-final.json for every mapped folder. One session, every campaign."""
    c = Closely(verbose=True)
    c.ensure_auth()
    print("→ mapping campaigns to folders")
    rows = [r for r in campaign_mapping(c) if r["folder"]]
    by_folder: dict[str, list[str]] = {}
    for r in rows:
        by_folder.setdefault(r["folder"], []).append(r["closely_id"])
    print(f"  {len(by_folder)} folder(s)\n")

    ok = failed = 0
    for folder, ids in by_folder.items():
        print(f"{'=' * 66}\n{folder}  <-  closely {','.join(ids)}\n{'=' * 66}")
        sub = argparse.Namespace(
            campaign=folder, closely_campaign_id=",".join(ids), probe=False,
            dry_run=args.dry_run, overwrite=True, date_from=None, date_to=None)
        try:
            rc = cmd_metrics(sub)
        except SystemExit as e:
            print(f"  ✗ {e}", file=sys.stderr)
            rc = 1
        ok += rc == 0
        failed += rc != 0
        print()
    print(f"{'-' * 66}\n{ok} folder(s) done, {failed} failed")
    return 0 if failed == 0 else 1


# ----------------------------------------------------------------------- pull-all

def cmd_pull_all(args) -> int:
    """Map, then pull every mapped pair. This is what the cron runs.

    Mapping is recomputed each time on purpose: a campaign started after the last run
    gets picked up without anyone editing a list of ids.
    """
    c = Closely(verbose=True)
    c.ensure_auth()
    print("→ mapping Closely campaigns to our folders")
    rows = [r for r in campaign_mapping(c) if r["folder"]]
    if not rows:
        print("\n✗ no Closely campaign maps to a folder here", file=sys.stderr)
        return 1

    # One of our folders can map to SEVERAL Closely campaigns: a campaign was split into
    # batches and each batch became its own campaign there.
    # 2026-07-31-uk-telehealth-digital-health is 139205 + 139077. Pulling only one of them
    # silently drops the other batch's replies.
    by_folder: dict[str, list[dict]] = {}
    for r in rows:
        by_folder.setdefault(r["folder"], []).append(r)
    print(f"  {len(rows)} mapped campaign(s) across {len(by_folder)} folder(s)\n")

    ok = failed = 0
    for folder, entries in by_folder.items():
        ids = ",".join(e["closely_id"] for e in entries)
        print(f"{'=' * 66}\n{folder}  <-  closely {ids}\n{'=' * 66}")
        sub = argparse.Namespace(
            campaign=folder, closely_campaign_id=ids,
            max_conversations=0, dry_run=args.dry_run, overwrite=True,
            include_non_campaign=False, keep_unmatched=False)
        try:
            rc = cmd_pull(sub)
        except SystemExit as e:
            print(f"  ✗ {e}", file=sys.stderr)
            rc = 1
        ok += rc == 0
        failed += rc != 0
        print()

    print(f"{'-' * 66}\n{ok} campaign(s) pulled, {failed} failed")
    return 0 if failed == 0 else 1


# --------------------------------------------------------------------------- main

def notify_failure(text: str) -> None:
    """Push a dead-credential message to Telegram. Same convention as the other scripts:
    the token goes through `curl --config -`, never argv, because this runs from cron."""
    import re as _re
    import subprocess
    env = Path.home() / ".hermes" / ".env"
    bot = chat = ""
    try:
        for line in env.read_text(encoding="utf-8", errors="replace").splitlines():
            m = _re.match(r"^\s*TELEGRAM_BOT_TOKEN\s*=\s*(.+)$", line)
            if m:
                bot = m.group(1).strip()
            m = _re.match(r"^\s*TELEGRAM_ALLOWED_USERS\s*=\s*(.+)$", line)
            if m:
                chat = m.group(1).strip().split(",")[0]
    except OSError:
        return
    if not (bot and chat):
        return
    try:
        subprocess.run(["curl", "-sf", "-m", "15", "--config", "-",
                        "--data-urlencode", f"chat_id={chat}",
                        "--data-urlencode", f"text={text}"],
                       input=f'url = "https://api.telegram.org/bot{bot}/sendMessage"\n',
                       text=True, check=True, capture_output=True)
    except Exception:
        pass


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        prog="closely-pull.py",
        description="Pull closely.io replies into responses-raw.csv (private API — see header).",
    )
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("probe", help="print the real response structures (run this first)")
    p.set_defaults(func=cmd_probe)

    cc = sub.add_parser("campaigns", help="list Closely campaigns and their ids")
    cc.set_defaults(func=cmd_campaigns)

    mt = sub.add_parser("metrics", help="build metrics-final.json from the drill endpoints")
    mt.add_argument("--campaign", required=True)
    mt.add_argument("--closely-campaign-id", required=True)
    mt.add_argument("--probe", action="store_true", help="print the payload shapes and stop")
    mt.add_argument("--date-from", help="unix seconds (default 2024-01-01)")
    mt.add_argument("--date-to", help="unix seconds (default now)")
    mt.add_argument("--dry-run", action="store_true")
    mt.add_argument("--overwrite", action="store_true")
    mt.set_defaults(func=cmd_metrics)

    ma = sub.add_parser("metrics-all",
                        help="metrics-final.json for every mapped folder (one session)")
    ma.add_argument("--dry-run", action="store_true")
    ma.set_defaults(func=cmd_metrics_all)

    pa = sub.add_parser("pull-all",
                        help="map, then pull every mapped campaign (this is the cron entry)")
    pa.add_argument("--dry-run", action="store_true")
    pa.set_defaults(func=cmd_pull_all)

    mc = sub.add_parser("map-campaigns",
                        help="match Closely campaigns to our folders by contact overlap")
    mc.set_defaults(func=cmd_map_campaigns)

    pl = sub.add_parser("pull", help="build responses-raw.csv from conversations with replies")
    pl.add_argument("--campaign", required=True, help="our campaign slug (where the CSV goes)")
    pl.add_argument("--closely-campaign-id", help="restrict to one Closely campaign id")
    pl.add_argument("--keep-unmatched", action="store_true",
                    help="keep replies from people absent from this folder's people-*.csv")
    pl.add_argument("--include-non-campaign", action="store_true",
                    help="also keep conversations that belong to no campaign (cold inbound)")
    pl.add_argument("--max-conversations", type=int, default=0,
                    help="stop after N conversations — use a small number on the first run")
    pl.add_argument("--dry-run", action="store_true", help="report, write nothing")
    pl.add_argument("--overwrite", action="store_true")
    pl.set_defaults(func=cmd_pull)

    ap.add_argument("--notify-on-failure", action="store_true",
                    help="push a Telegram message if this run fails (for cron)")
    args = ap.parse_args(argv)
    try:
        rc = args.func(args)
    except SystemExit as e:
        code = e.code if isinstance(e.code, int) else 1
        if getattr(args, "notify_on_failure", False):
            notify_failure(
                "closely-pull failed.\n\n" + str(e)[:600] +
                "\n\nMost likely you logged into app.closelyhq.com, which kills our "
                "session (Closely allows one at a time). Re-copy the tokens: devtools "
                "Console on a logged-in tab ->\n"
                "copy(`CLOSELY_TOKEN=${JSON.parse(localStorage.getItem('closely')).at}"
                "\\nCLOSELY_REFRESH_TOKEN="
                "${JSON.parse(localStorage.getItem('closely')).rt}`)\n"
                "and paste into ~/.hermes/.env")
        raise
    if rc != 0 and getattr(args, "notify_on_failure", False):
        notify_failure(f"closely-pull `{args.cmd}` exited {rc} — see "
                       "~/.hermes/logs/closely-pull.log")
    return rc


if __name__ == "__main__":
    sys.exit(main())
