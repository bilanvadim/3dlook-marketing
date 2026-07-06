"""Shared helpers for the (simplified) model-router: daily picker + hourly Go check.
No proxy. Hermes uses one primary Go model + a native free fallback."""
import json, os, re, ssl, subprocess, urllib.request, urllib.parse, urllib.error

HOME   = os.path.expanduser("~")
ROOT   = f"{HOME}/.hermes/model-router"
ENVF   = f"{HOME}/.hermes/.env"
CONFIG = f"{HOME}/.hermes/config.yaml"
CTX    = ssl.create_default_context()

GO_BASE  = "https://opencode.ai/zen/go/v1"
ZEN_BASE = "https://opencode.ai/zen/v1"
UA       = "curl/8.5.0"  # default python-urllib UA gets 403'd by Cloudflare

def env(key):
    try:
        for line in open(ENVF):
            if line.startswith(key + "="):
                return line.split("=", 1)[1].strip()
    except FileNotFoundError:
        pass
    return ""

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

def telegram(text):
    tok = env("TELEGRAM_BOT_TOKEN")
    chat = (env("TELEGRAM_ALLOWED_USERS").split(",")[0] or "").strip()
    if not tok or not chat:
        return False
    body = urllib.parse.urlencode({"chat_id": chat, "text": text, "parse_mode": "HTML",
                                   "disable_web_page_preview": "true"}).encode()
    try:
        req = urllib.request.Request(f"https://api.telegram.org/bot{tok}/sendMessage", data=body)
        with urllib.request.urlopen(req, timeout=20, context=CTX) as r:
            return json.loads(r.read()).get("ok", False)
    except Exception:
        return False

def restart_gateway():
    e = dict(os.environ)
    e.setdefault("XDG_RUNTIME_DIR", f"/run/user/{os.getuid()}")
    try:
        subprocess.run(["systemctl", "--user", "restart", "hermes-gateway.service"],
                       env=e, timeout=60, check=False)
        return True
    except Exception:
        return False

# ---- config.yaml editing (single primary model + fallback chain) ----
def set_model_default(model):
    lines = open(CONFIG).read().split("\n")
    inmodel = done = False
    for i, l in enumerate(lines):
        if re.match(r'^model:\s*$', l):
            inmodel = True; continue
        if inmodel and re.match(r'^\S', l):
            inmodel = False
        if inmodel and not done and re.match(r'^\s+default:\s', l):
            ind = l[:len(l) - len(l.lstrip())]
            lines[i] = f"{ind}default: {model}"; done = True
    open(CONFIG, "w").write("\n".join(lines))
    return done

def set_fallback(model, provider="opencode-zen"):
    """Replace the top-level fallback_providers block with a single entry."""
    lines = open(CONFIG).read().split("\n")
    out, i, n = [], 0, len(lines)
    while i < n:
        if re.match(r'^fallback_providers:\s*$', lines[i]):
            i += 1
            while i < n and (lines[i].startswith(" ") or lines[i].startswith("\t")):
                i += 1
            continue
        out.append(lines[i]); i += 1
    while out and out[-1].strip() == "":
        out.pop()
    out += ["fallback_providers:", f"  - provider: {provider}", f"    model: {model}", ""]
    open(CONFIG, "w").write("\n".join(out))
