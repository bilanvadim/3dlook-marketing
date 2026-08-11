#!/usr/bin/env python3
"""pre_llm_call hook: offer the strong chain when the task looks too heavy for the
everyday agentic model.

The escalation target is llm-failover-proxy's STRONG chain (list A), reached with
`/heavy` — the switcher borrows the whole chain for this tab, so the model is chosen
per request by failover instead of being one id that may be dead right now. Returning
is `/normal`, which drops the override back to the everyday agentic chain (list B).

Was the MoA council until 2026-08-10: at the time there was no stronger single target
to point at. Now there is a chain, and it is both faster and cheaper in quota than
running two advisors plus an aggregator on every heavy turn.

Why a hook and not the model's own judgement: the acting model here is small
(`mimo-v2.5-free`). Asking it to notice "this is beyond me" is exactly the
judgement it is least able to make. The heaviness test is therefore mechanical
and lives outside the model, the same way route-profile.sh classifies intent with
a script instead of letting a small model guess.

It SUGGESTS. It never switches: `{"context": ...}` can only add text to the turn,
and silently swapping the model mid-conversation would drop the context anyway.
The user taps or types `/model moa:council`; the turn proceeds regardless.

Latched per session, so a long heavy conversation is offered the council once,
not on every turn.

Contract: reads the pre_llm_call payload on stdin, prints `{"context": "..."}` to
offer, or nothing at all. Any failure prints nothing — a broken suggester must
never cost a turn.
"""

import json
import os
import re
import sys
import time

STATE = os.path.expanduser("~/.hermes/.moa-suggest-state.json")
PICK = os.path.expanduser("~/.hermes/model-router/pick.json")


TARGET = "/heavy"
BACK = "/normal"
RESUGGEST_AFTER_S = 6 * 3600      # same session, only after a long gap
# The heaviness test lives in ops/task-heaviness.py and is shared with the
# claude-switcher. It used to be duplicated here, and the two copies disagreed on
# exactly the traffic that matters — see that file's header. Imported by path because
# a hook has no package to import from.
import importlib.util as _ilu


def _load_scorer():
    for cand in (os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "task-heaviness.py"),
                 os.path.expanduser("~/.hermes/task-heaviness.py")):
        try:
            spec = _ilu.spec_from_file_location("task_heaviness", os.path.normpath(cand))
            if not spec or not spec.loader:
                continue
            mod = _ilu.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod
        except Exception:
            continue
    return None


_TH = _load_scorer()
RESUGGEST_AFTER_S = 6 * 3600      # same session, only after a long gap
MIN_CHARS = getattr(_TH, "MIN_CHARS", 80)
THRESHOLD = getattr(_TH, "THRESHOLD", 3)

def _load_state():
    try:
        with open(STATE, encoding="utf-8") as f:
            d = json.load(f)
        return d if isinstance(d, dict) else {}
    except Exception:
        return {}


def _mark(session_id):
    st = _load_state()
    # Keep the file small: drop anything older than a day.
    now = time.time()
    st = {k: v for k, v in st.items()
          if isinstance(v, (int, float)) and now - v < 86400}
    st[session_id] = now
    tmp = STATE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(st, f)
    os.replace(tmp, STATE)


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return
    if not isinstance(payload, dict):
        return

    msg = str(payload.get("user_message") or "")
    model = str(payload.get("model") or "")
    session_id = str(payload.get("session_id") or "")

    # Already escalated — nothing to offer. Both the MoA presets and the strong
    # chain count: the chain answers as "auto" on port 47822, so the model id alone
    # cannot tell them apart and the base_url is what carries the truth.
    low = model.lower()
    if "moa" in low or "council" in low or "47822" in str(payload.get("base_url") or ""):
        return
    # Gates (floor, acks, forwards) live in the shared scorer — it returns 0 points
    # for all of them, so a single threshold check below covers every case.

    last = _load_state().get(session_id)
    if isinstance(last, (int, float)) and time.time() - last < RESUGGEST_AFTER_S:
        return

    pts, why = (_TH.score(msg) if _TH else (0, []))
    if pts < THRESHOLD:
        return

    _mark(session_id)
    reason = ", ".join(why[:3])
    print(json.dumps({"context": (
        "[Подсказка системы, не от пользователя] Задача оценена как тяжёлая для "
        f"текущей агентной модели ({reason}). ПЕРВОЙ строкой ответа предложи одним "
        f"предложением переключиться на сильную цепочку: `{TARGET}` — модель на "
        "каждый запрос выберет llm-fop перебором по списку A. Упомяни, что "
        f"вернуться можно командой `{BACK}`. Затем ВЫПОЛНЯЙ задачу как обычно — "
        "это предложение, а не блокировка, и ждать ответа не нужно."
    )}, ensure_ascii=False))


if __name__ == "__main__":
    main()
