"""[hermes-vision-switch] Borrow the image-reading model for exactly one turn.

The morning router (ops/model-router/refresh.py) no longer makes vision a hard
gate on the everyday model, because it cost a lot of brain: on a typical morning
the strongest free model scores 82 and the strongest one that can see scores 62.
Wearing the reader all day to stay ready for the occasional screenshot was the
wrong trade.

So the reader is BORROWED instead:

    text message      → today's strongest model (may be blind — fine)
    message + image   → today's proven reader, for that turn only
    next text message → back to the strongest model, automatically

The switch is a per-SESSION model override plus a cached-agent eviction — the
same seam ``/model`` and heavy mode use. Not a config.yaml rewrite: that needs a
gateway restart, and Hermes would be killing the conversation it is answering.

Two things make this land at the right moment:

  * ENGAGE runs inside ``_prepare_inbound_message_text``, BEFORE the gateway
    decides how to feed the image to the model. That ordering is the whole
    point. ``_decide_image_input_mode`` resolves the session's override, so with
    the reader already in place it answers "native" and the reader gets the
    actual pixels. Engage after that call and the gateway would have already
    committed to describing the image with the auxiliary model instead.
  * RELEASE runs in the ``finally`` of the message-handling path, so the reader
    is given back on success, on exception and on interrupt alike. A leaked
    override is the one genuinely bad failure here — it would silently pin the
    session to the weakest model of the day — so release() puts back EVERY
    session it engaged, not just the one whose key the caller passes.

What is deliberately NOT done here: the image is not stripped out of the
conversation history on the way back. Upstream already handles a text-only model
meeting an image in history — it catches the provider's rejection, strips the
image parts and retries the same turn (agent/conversation_loop.py). Re-writing
transcripts from a patch to save that one retry is not worth the blast radius.
The reader's own answer stays in history as plain assistant text, which is what
follow-up questions actually read.
"""

import json
import logging
import os
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

_PICK_JSON = os.path.expanduser("~/.hermes/model-router/pick.json")

# models.dev provider ids -> (hermes provider, base_url). The router picks the
# reader off OpenCode Zen, whose id is already a Hermes provider id, so this map
# only earns its keep if the reader search is ever widened the way the backup
# coder's was. Mirrors the table in claude_switcher.py rather than importing it:
# the two patches must install independently of each other.
_HERMES_PROVIDER = {
    "opencode": ("opencode-zen", None),
    "opencode-zen": ("opencode-zen", None),
    "google": ("gemini", None),
    "nvidia": ("nvidia", None),
    "huggingface": ("huggingface", None),
    "openrouter": ("openai-api", "https://openrouter.ai/api/v1"),
    "groq": ("openai-api", "https://api.groq.com/openai/v1"),
    "cerebras": ("openai-api", "https://api.cerebras.ai/v1"),
    "mistral": ("openai-api", "https://api.mistral.ai/v1"),
}

_PROVIDER_ENV = {
    "opencode": ("OPENCODE_ZEN_API_KEY", "OPENCODE_GO_API_KEY"),
    "opencode-zen": ("OPENCODE_ZEN_API_KEY", "OPENCODE_GO_API_KEY"),
    "google": ("GOOGLE_API_KEY", "GEMINI_API_KEY"),
    "nvidia": ("NVIDIA_API_KEY",),
    "huggingface": ("HF_TOKEN", "HUGGINGFACE_API_KEY"),
    "openrouter": ("OPENROUTER_API_KEY",),
    "groq": ("GROQ_API_KEY",),
    "cerebras": ("CEREBRAS_API_KEY",),
    "mistral": ("MISTRAL_API_KEY",),
}

# session_key -> {"snapshot": …, "task": the asyncio task that borrowed}.
# In-memory only, like heavy mode: a gateway restart mid-turn must come back on
# the everyday model, never on a half-applied borrow.
#
# The task is what makes release() safe. The gateway serves every chat from one
# event loop and the patched release() sits in the finally of EVERY turn, not
# just image turns — so a plain "ок" arriving in chat B while chat A is still
# awaiting its image routing would, on a blind key-less sweep, hand A's reader
# back mid-turn. A's turn had already been routed "native" by then, so the pixels
# would go to the blind everyday model and the provider would reject them.
# Ownership is therefore tracked, not guessed.
_ENGAGED: Dict[str, Dict[str, Any]] = {}


def _current_task():
    """The asyncio task running this turn, or None outside a loop (tests)."""
    try:
        import asyncio
        return asyncio.current_task()
    except Exception:
        return None


def _task_finished(task):
    """True when the turn that borrowed is gone and cannot release its own entry."""
    if task is None:
        return True
    try:
        return bool(task.done())
    except Exception:
        return True


def _read_pick() -> Dict[str, Any]:
    try:
        with open(_PICK_JSON, "r", encoding="utf-8") as f:
            return json.load(f) or {}
    except Exception:
        return {}


def _env_value(var_names) -> Optional[str]:
    """First non-empty value among *var_names*, ai-models.env then .env.
    Mirrors the router's own lookup so one key serves every consumer."""
    for path in (os.path.expanduser("~/.hermes/ai-models.env"),
                 os.path.expanduser("~/.hermes/.env")):
        try:
            lines = open(path, encoding="utf-8").read().splitlines()
        except OSError:
            continue
        for var in var_names:
            for line in lines:
                if line.startswith(var + "="):
                    val = line.split("=", 1)[1].strip().strip('"\'')
                    if val:
                        return val
    return None


def reader() -> Optional[Dict[str, str]]:
    """Today's proven image reader, resolved to something Hermes can talk to.

    ``None`` when the router has never run, or when the last run found nothing
    that could actually name the colour of a red square — in which case the turn
    proceeds on the everyday model and the gateway's own auxiliary-vision path
    describes the image instead. Degraded, but never broken.
    """
    pick = _read_pick()
    model = pick.get("best_vision")
    if not model:
        return None
    pid = (pick.get("best_vision_provider") or "opencode-zen").strip()
    provider, base_url = _HERMES_PROVIDER.get(pid, (None, None))
    if not provider:
        logger.debug("vision-switch: unknown provider id %r in pick.json", pid)
        return None
    out = {"model": model, "provider": provider}
    if base_url:
        out["base_url"] = base_url
    api_key = _env_value(_PROVIDER_ENV.get(pid, ()))
    if api_key:
        out["api_key"] = api_key
    return out


def _acting_model(runner: Any, session_key: str) -> str:
    """The model this session would use if we did nothing."""
    try:
        state = runner._peek_session_state(session_key)
        override = state.conversation.model_override if state else None
        if override and override.get("model"):
            return str(override["model"])
    except Exception:
        pass
    try:
        from hermes_cli.config import load_config_readonly
        model_cfg = (load_config_readonly() or {}).get("model") or {}
        if isinstance(model_cfg, str):
            return model_cfg.strip()
        return str(model_cfg.get("default") or "")
    except Exception:
        return ""


def engage(runner: Any, session_key: str) -> Optional[str]:
    """Put this session on the image reader for the current turn.

    Returns the model name when the switch happened, ``None`` when it was
    unnecessary or impossible. Never raises: a failure here must cost the user
    a worse answer at most, never the turn itself.
    """
    if not session_key:
        return None
    try:
        if session_key in _ENGAGED:
            return None                      # already borrowed for this turn
        rd = reader()
        if not rd:
            return None
        current = _acting_model(runner, session_key)
        if current == rd["model"]:
            return None                      # the everyday model already sees
        snapshot = runner._snapshot_session_model_override(session_key)
        override = {k: v for k, v in rd.items() if k in
                    ("model", "provider", "base_url", "api_key")}
        runner._session_state(session_key).conversation.model_override = override
        runner._evict_cached_agent(session_key)
        _ENGAGED[session_key] = {"snapshot": snapshot, "task": _current_task()}
        logger.info("vision-switch: %s → %s на один ход (пришла картинка)",
                    current or "?", rd["model"])
        return rd["model"]
    except Exception:
        logger.debug("vision-switch: engage failed", exc_info=True)
        return None


def release(runner: Any, session_key: Optional[str] = None) -> None:
    """Give the reader back — but only what THIS turn borrowed.

    Called from the turn's ``finally``, which runs for every message, image or
    not. Three things are released, and nothing else:

      * the entry under *session_key*, the ordinary case;
      * any entry borrowed by the current asyncio task under a different key —
        Telegram topic recovery can rewrite the routing key mid-turn, so the key
        a turn ends on is not always the one it started on;
      * entries whose borrowing task has finished without releasing, which is the
        only way one can leak. Left behind, such an override silently pins a
        session to the weakest model of the day, so it is worth sweeping.

    What it must NOT do is release an entry belonging to a turn still running:
    that turn has already been routed "native" and would end up sending pixels to
    a blind model.
    """
    cur = _current_task()
    mine, stale = [], []
    for key, entry in _ENGAGED.items():
        if session_key and key == session_key:
            mine.append(key)
        elif cur is not None and entry.get("task") is cur:
            mine.append(key)
        elif _task_finished(entry.get("task")):
            stale.append(key)
    for key in mine + stale:
        entry = _ENGAGED.pop(key, None)
        if entry is None:
            continue
        try:
            runner._restore_session_model_override(key, entry["snapshot"])
            logger.info("vision-switch: вернул рабочую модель на сессии %s%s", key,
                        " (осиротевший захват)" if key in stale else "")
        except Exception:
            logger.debug("vision-switch: release failed for %s", key, exc_info=True)


def is_engaged(session_key: str) -> bool:
    return session_key in _ENGAGED
