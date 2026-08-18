"""Shared helpers for the (simplified) model-router: daily picker + hourly Go check.
No proxy. Hermes uses one primary Go model + a native free fallback."""
import json, os, re, shutil, ssl, subprocess, tempfile, time, urllib.request, urllib.parse, urllib.error

HOME   = os.path.expanduser("~")
ROOT   = f"{HOME}/.hermes/model-router"
ENVF   = f"{HOME}/.hermes/.env"
CONFIG = f"{HOME}/.hermes/config.yaml"
CTX    = ssl.create_default_context()

GO_BASE  = "https://opencode.ai/zen/go/v1"
ZEN_BASE = "https://opencode.ai/zen/v1"
UA       = "curl/8.5.0"  # default python-urllib UA gets 403'd by Cloudflare

def write_atomic(path, text):
    """Temp file in the same dir + os.replace. NEVER truncate-in-place.

    config.yaml is 16 KB of live Hermes configuration with four writers in this
    module, each of which used `open(path,"w")` — truncate first, write second.
    Any interruption in between (disk full, OOM, the timer being stopped) left the
    gateway's config empty or half-written, with no backup anywhere in the code,
    and the very next line of refresh.py restarts the gateway onto it."""
    d = os.path.dirname(path) or "."
    fd, tmp = tempfile.mkstemp(dir=d, prefix=".rl-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
        try:
            shutil.copymode(path, tmp)
        except OSError:
            pass                      # new file: default mode is fine
        os.replace(tmp, path)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def esc(text):
    """Escape text destined for a parse_mode=HTML Telegram message.

    Provider error strings go straight into the morning report, and urllib spells
    a network failure `<urlopen error timed out>`. Telegram answers 400
    "Unsupported start tag", telegram() swallows it, and the whole report — the
    one for the morning where a provider actually broke — is never delivered."""
    return (str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def env(key):
    try:
        for line in open(ENVF):
            if line.startswith(key + "="):
                # .strip('"\'') like find_key does. Without it a perfectly normal
                # OPENCODE_ZEN_API_KEY="sk-…" makes every Zen probe 401, and the
                # report blames an expired promotion for a quoting problem.
                return line.split("=", 1)[1].strip().strip('"\'')
    except FileNotFoundError:
        pass
    return ""

def zen_key():
    """Key for the free Zen endpoint. Now that Hermes runs fully free, this is the
    key that matters; the Go key is only a legacy fallback for older installs."""
    return env("OPENCODE_ZEN_API_KEY") or env("OPENCODE_GO_API_KEY")

def get_json(url, key=None, timeout=25):
    req = urllib.request.Request(url)
    req.add_header("User-Agent", UA)
    if key:
        req.add_header("Authorization", "Bearer " + key)
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        return json.loads(r.read())

def ids(models_response):
    return [m["id"] for m in models_response.get("data", [])]

def load_catalog():
    cache = f"{ROOT}/cache/modelsdev.json"
    try:
        d = get_json("https://models.dev/api.json", timeout=30)
        os.makedirs(f"{ROOT}/cache", exist_ok=True)
        json.dump(d, open(cache, "w"))
        return d
    except Exception:
        return json.load(open(cache))

def probe_go(key, base, model):
    """True=alive(200), False=limited/error(4xx), None=network unknown (don't act)."""
    body = json.dumps({"model": model, "max_tokens": 5,
                       "messages": [{"role": "user", "content": "ping"}]}).encode()
    req = urllib.request.Request(base + "/chat/completions", data=body)
    req.add_header("User-Agent", UA)
    req.add_header("Authorization", "Bearer " + key)
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=45, context=CTX) as r:
            return r.status == 200
    except urllib.error.HTTPError:
        return False
    except Exception:
        return None

def free_ok(key, model, base=ZEN_BASE):
    """True only if a 'free' Zen model ACTUALLY answers (catalog lists ended
    promotions that return an error body, e.g. 'Free promotion has ended'). $0."""
    body = json.dumps({"model": model, "max_tokens": 30,
                       "messages": [{"role": "user", "content": "ping"}]}).encode()
    req = urllib.request.Request(base + "/chat/completions", data=body)
    req.add_header("User-Agent", UA)
    req.add_header("Authorization", "Bearer " + key)
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=60, context=CTX) as r:
            d = json.loads(r.read())
        return ("error" not in d) and bool(d.get("choices"))
    except Exception:
        return False

# An 8x8 pure-red PNG, inlined as base64 (100 chars). Used to PROVE a model can
# see: the catalog's `modalities`/`attachment` flags are self-reported and stale
# (the same catalog lists ended free promotions as free), so vision is verified
# the same way free-ness is — by asking the model.
RED_PNG_B64 = ("iVBORw0KGgoAAAANSUhEUgAAAAgAAAAICAIAAABLbSncAAAAEklEQVR4nGP4z8CA"
               "FWEXHbQSACj/P8Fu7N9hAAAAAElFTkSuQmCC")
_RED_WORDS = ("red", "красн", "红", "rouge", "rot")

def vision_ok(key, model, base=None, timeout=90):
    """Show the model a red square and ask for the colour.

    Returns {ok, ms, answer, error}. `ok` requires the model to actually NAME the
    colour — a text-only model 400s on the image part, and a model that accepts
    images but can't read an 8x8 solid fill is not something to hand screenshots
    to. max_tokens is generous on purpose: reasoning models spend the first ~25
    tokens thinking and return an EMPTY content if the budget is tight (that is
    what made a working vision model look broken at max_tokens=20)."""
    base = base or ZEN_BASE
    body = json.dumps({
        "model": model, "max_tokens": 300,
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": "What color is this image? Answer with one word."},
            {"type": "image_url",
             "image_url": {"url": "data:image/png;base64," + RED_PNG_B64}}]}],
    }).encode()
    req = urllib.request.Request(base + "/chat/completions", data=body)
    req.add_header("User-Agent", UA)
    req.add_header("Authorization", "Bearer " + key)
    req.add_header("Content-Type", "application/json")
    t0 = time.monotonic()
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
            d = json.loads(r.read())
    except urllib.error.HTTPError as e:
        # 400 here is the normal "this model takes text only" answer.
        return {"ok": False, "ms": int((time.monotonic() - t0) * 1000),
                "answer": "", "error": f"HTTP {e.code}"}
    except Exception as e:
        return {"ok": False, "ms": int((time.monotonic() - t0) * 1000),
                "answer": "", "error": str(e)[:80]}
    ms = int((time.monotonic() - t0) * 1000)
    if "error" in d:
        return {"ok": False, "ms": ms, "answer": "", "error": str(d["error"])[:80]}
    try:
        ans = (d["choices"][0]["message"].get("content") or "").strip()
    except Exception:
        return {"ok": False, "ms": ms, "answer": "", "error": "no choices"}
    low = ans.lower()
    return {"ok": any(w in low for w in _RED_WORDS), "ms": ms,
            "answer": ans[:60], "error": "" if ans else "empty content"}

def telegram(text, parse_mode="HTML"):
    """Send a message. Returns True only if Telegram confirmed it.

    `parse_mode=None` sends plain text — the caller's fallback when HTML is
    rejected. Failures are printed (never the token) instead of vanishing: this
    is the only notification channel the morning run has, so a silent 400 means
    Sergiy learns nothing at all."""
    tok = env("TELEGRAM_BOT_TOKEN")
    chat = (env("TELEGRAM_ALLOWED_USERS").split(",")[0] or "").strip()
    if not tok or not chat:
        print("[router] telegram: нет TELEGRAM_BOT_TOKEN или TELEGRAM_ALLOWED_USERS", flush=True)
        return False
    fields = {"chat_id": chat, "text": text, "disable_web_page_preview": "true"}
    if parse_mode:
        fields["parse_mode"] = parse_mode
    body = urllib.parse.urlencode(fields).encode()
    try:
        req = urllib.request.Request(f"https://api.telegram.org/bot{tok}/sendMessage", data=body)
        with urllib.request.urlopen(req, timeout=20, context=CTX) as r:
            return json.loads(r.read()).get("ok", False)
    except urllib.error.HTTPError as e:
        try:
            detail = json.loads(e.read()).get("description", "")[:160]
        except Exception:
            detail = ""
        print(f"[router] telegram HTTP {e.code}: {detail}", flush=True)
        return False
    except Exception as ex:
        print(f"[router] telegram failed: {ex}", flush=True)
        return False

def restart_gateway():
    """True only when systemctl actually reported success.

    Used to return True for any completed invocation, including a non-zero exit —
    and the caller printed "gateway перезапущен" unconditionally anyway. A unit in
    failed state, or a timer environment without XDG_RUNTIME_DIR, left Hermes on
    the old model while the report said otherwise."""
    e = dict(os.environ)
    e.setdefault("XDG_RUNTIME_DIR", f"/run/user/{os.getuid()}")
    try:
        r = subprocess.run(["systemctl", "--user", "restart", "hermes-gateway.service"],
                           env=e, timeout=60, check=False,
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(f"[router] restart FAILED rc={r.returncode}: "
                  f"{(r.stderr or r.stdout or '').strip()[:200]}", flush=True)
            return False
        return True
    except Exception as ex:
        print(f"[router] restart FAILED: {ex}", flush=True)
        return False

# ---- config.yaml editing (single primary model + fallback chain) ----
def _main_model_is_chain() -> bool:
    """True when config.yaml points the MAIN model at a local failover chain.

    The chain replaces the daily pick outright: it tries a whole list per request,
    hedges and cools down dead entries, so overwriting model.default with one id
    would demote a live router to a frozen guess — and do it at 07:00, silently.
    Detected from the file rather than a flag, so it holds even if the timer comes
    back after an update or a reinstall."""
    try:
        txt = open(CONFIG, encoding="utf-8").read()
    except OSError:
        return False
    import re as _re
    m = _re.search(r"^model:\n(?:[ \t]+.*\n)+", txt, _re.M)
    block = m.group(0) if m else ""
    return ("provider: custom" in block
            and ("127.0.0.1" in block or "localhost" in block)) or "llm-failover-proxy" in txt


def set_model_default(model, provider=None):
    """Rewrite model.default (and model.provider when given) inside config.yaml.

    The provider has to move too now that Hermes is fully free: the old primary
    lived on `opencode-go` (subscription), the free models live on `opencode-zen`.
    Leaving a free model id under the Go provider yields a 'model not found' and a
    silently dead gateway."""
    if _main_model_is_chain():
        return "chain"          # truthy, and distinguishable from a real write
    lines = open(CONFIG).read().split("\n")
    inmodel = False
    done_model = done_prov = False
    for i, l in enumerate(lines):
        if re.match(r'^model:\s*$', l):
            inmodel = True; continue
        if inmodel and re.match(r'^\S', l):
            inmodel = False
        if not inmodel:
            continue
        ind = l[:len(l) - len(l.lstrip())]
        if not done_model and re.match(r'^\s+default:\s', l):
            lines[i] = f"{ind}default: {model}"; done_model = True
        elif provider and not done_prov and re.match(r'^\s+provider:\s', l):
            lines[i] = f"{ind}provider: {provider}"; done_prov = True
    write_atomic(CONFIG, "\n".join(lines))
    return done_model and (done_prov or not provider)

OPENCODE_CFG  = f"{HOME}/.config/opencode/opencode.jsonc"
OPENCODE_AUTH = f"{HOME}/.local/share/opencode/auth.json"

def set_opencode_auth(provider_id, key):
    """Put a provider API key into the OpenCode CLI credential store.

    The CLI reads `~/.local/share/opencode/auth.json`, keyed by the same provider
    ids models.dev uses (`openrouter`, `google`, `nvidia`, `opencode`, …). Writing
    it here (rather than exporting an env var) means the backup agent works no
    matter who launches it — Hermes' terminal tool, a cron job, or a human shell.

    Refuses an empty key instead of storing it. The synthetic Zen fallback row is
    built without the key check the real providers get, and zen_key() accepts
    OPENCODE_GO_API_KEY while PROVIDERS["OpenCode Zen"] lists only the ZEN name —
    so on a machine where only the legacy var survives, find_key returned None and
    this wrote {"key": null}, wiping a working credential and reporting success."""
    if not key:
        return False
    try:
        try:
            data = json.load(open(OPENCODE_AUTH))
        except Exception:
            data = {}
        if data.get(provider_id, {}).get("key") == key:
            return True                      # already current, don't rewrite
        data[provider_id] = {"type": "api", "key": key}
        os.makedirs(os.path.dirname(OPENCODE_AUTH), exist_ok=True)
        with open(OPENCODE_AUTH, "w") as f:
            json.dump(data, f, indent=2)
        os.chmod(OPENCODE_AUTH, 0o600)
        return True
    except Exception:
        return False

def set_opencode_model(model, provider="opencode", base_url=None):
    """Point the OpenCode CLI (the backup coding agent) at `model`.

    `small_model` matters as much as `model`: OpenCode titles every session with
    its built-in small model (gpt-5-nano — PAID on zen). With no balance that
    call 401s with CreditsError, the stream dies, and `opencode run` exits 0
    having printed NOTHING. Both ids are pinned to the same free model.

    `base_url` pins the provider's endpoint explicitly. Needed for Cloudflare
    Workers AI, whose models.dev entry builds its URL from a template —
    `.../accounts/${CLOUDFLARE_ACCOUNT_ID}/ai/v1` — so without either that env var
    or this override the CLI cannot reach the provider at all, and a model that
    measured 65 tok/s in the probe would be unusable in practice. Writing the
    resolved URL removes the dependency on who exported what.

    Note for whoever debugs this next: `opencode run` also prints nothing when it
    is started OUTSIDE a git repo/project — always invoke it with cwd inside the
    target repo."""
    ref = f"{provider}/{model}"
    prov_block = ""
    if base_url:
        prov_block = (',\n  "provider": {\n'
                      f'    "{provider}": {{\n'
                      f'      "options": {{ "baseURL": "{base_url}" }}\n'
                      "    }\n"
                      "  }")
    body = ("{\n"
            '  "$schema": "https://opencode.ai/config.json",\n'
            "  // GENERATED by ops/model-router/refresh.py — edited every morning.\n"
            "  // Backup coding agent, fully free. small_model must ALSO be free:\n"
            "  // OpenCode's built-in small model (gpt-5-nano) is paid, and its 401\n"
            "  // kills the run silently.\n"
            f'  "model": "{ref}",\n'
            f'  "small_model": "{ref}"{prov_block}\n'
            "}\n")
    # HANDS OFF when OpenCode is pointed at the local failover proxy. Then model
    # SELECTION is the proxy's job — it tries a whole chain per request and hedges,
    # which is strictly better than one id picked at 06:00 and frozen for the day
    # (the id we pick can be dead by noon; the chain routes around that live).
    # Rewriting this file from the template below would silently delete the
    # provider block and put the coder back on a single model, so the failover
    # would be gone by morning with nothing in the logs to say why.
    try:
        cur = open(OPENCODE_CFG, encoding="utf-8").read()
        if "llm-fop" in cur or "127.0.0.1:4782" in cur:
            return "proxy"          # truthy, and distinguishable from a real write
    except OSError:
        pass
    try:
        os.makedirs(os.path.dirname(OPENCODE_CFG), exist_ok=True)
        write_atomic(OPENCODE_CFG, body)
        return True
    except Exception:
        return False

def set_moa_council(aggregator, advisors, provider="opencode-zen"):
    """Repoint the moa:council preset at today's models. Returns True if written.

    The preset exists to strengthen a weak primary: two advisors think, the
    PROVEN primary aggregates. That only holds while the aggregator IS the
    primary — and the primary is repicked every morning, so pinning it in the
    config makes the two drift apart within a day.

    Rewritten IN PLACE, unlike set_fallback which lifts its block to the end of
    the file: this block has a comment header above it explaining why the models
    are what they are, and moving the block would strand that comment pointing
    at nothing. Never invents the block — if the user removed `moa:`, that is a
    decision, not a gap to fill.
    """
    block = ["moa:", "  default_preset: council", "  presets:", "    council:",
             "      enabled: true", "      reference_models:"]
    for m in advisors:
        block += [f"        - provider: {provider}", f"          model: {m}"]
    block += ["      aggregator:",
              f"        provider: {provider}",
              f"        model: {aggregator}",
              "      reference_max_tokens: 600",
              "      max_tokens: 4096",
              ""]
    lines = open(CONFIG).read().split("\n")
    out, i, n, seen = [], 0, len(lines), False
    while i < n:
        if re.match(r'^moa:\s*$', lines[i]):
            seen = True
            out += block
            i += 1
            # Same boundary rule as set_fallback: blanks, indented lines and
            # column-0 list markers still belong to the block.
            while i < n:
                l = lines[i]
                if l.strip() == "" or l.startswith((" ", "\t", "-")):
                    i += 1
                    continue
                break
            continue
        out.append(lines[i]); i += 1
    if not seen:
        return False
    write_atomic(CONFIG, "\n".join(out))
    return True


def set_auxiliary_vision(model, provider="opencode-zen"):
    """Point `auxiliary.vision` at today's proven image reader.

    Since the primary stopped being gated on vision, this slot is what keeps
    screenshots working: Hermes pre-analyses an inbound image with it whenever
    the acting model cannot see pixels itself (and ops/vision-switch borrows the
    same model outright for the turn that carries the image).

    Edited IN PLACE, line by line, unlike set_fallback which rebuilds its block:
    `vision:` has a sibling — `approval:`, the smart-approval judge — sitting
    directly below it, and a block-rebuilding draft of this function silently
    deleted that sibling along with everything else indented under `auxiliary:`.
    Only the two lines inside `vision:` are ever rewritten.

    Never invents the block: an absent `auxiliary.vision` is a decision, not a
    gap. Returns True only when BOTH lines were found and written.
    """
    lines = open(CONFIG).read().split("\n")
    in_aux = in_vision = False
    vis_indent = 0
    done_model = done_prov = False
    for i, l in enumerate(lines):
        if re.match(r'^auxiliary:\s*$', l):
            in_aux = True
            continue
        if not in_aux:
            continue
        if l.strip() and re.match(r'^\S', l):
            break                       # next top-level key — auxiliary is over
        if re.match(r'^\s+vision:\s*$', l):
            in_vision = True
            vis_indent = len(l) - len(l.lstrip())
            continue
        if not in_vision or not l.strip():
            continue
        ind = len(l) - len(l.lstrip())
        if ind <= vis_indent:           # a sibling of vision: (approval:, …)
            in_vision = False
            continue
        if re.match(r'^\s+model:\s', l):
            lines[i] = f"{' ' * ind}model: {model}"; done_model = True
        elif re.match(r'^\s+provider:\s', l):
            lines[i] = f"{' ' * ind}provider: {provider}"; done_prov = True
    if not (done_model and done_prov):
        return False
    write_atomic(CONFIG, "\n".join(lines))
    return True


def set_fallback(model, provider="opencode-zen"):
    """Replace the top-level fallback_providers block with a single entry."""
    if _main_model_is_chain():
        # The chain IS the fallback ladder — nine entries deep, with cooldowns.
        # A single daily fallback under it is at best redundant and at worst a
        # dead id nobody probes any more.
        return "chain"
    lines = open(CONFIG).read().split("\n")
    out, i, n = [], 0, len(lines)
    while i < n:
        if re.match(r'^fallback_providers:\s*$', lines[i]):
            i += 1
            # Consume every line still belonging to this block: blank lines,
            # indented continuation lines, and YAML list items — which are
            # valid at column 0 (e.g. "- provider: x"), not just indented.
            # Stop only at the next real top-level key (starts at column 0,
            # non-blank, not a list marker).
            while i < n:
                l = lines[i]
                if l.strip() == "" or l.startswith(" ") or l.startswith("\t") or l.startswith("-"):
                    i += 1
                    continue
                break
            continue
        out.append(lines[i]); i += 1
    while out and out[-1].strip() == "":
        out.pop()
    out += ["fallback_providers:", f"  - provider: {provider}", f"    model: {model}", ""]
    write_atomic(CONFIG, "\n".join(out))
