#!/usr/bin/env python3
"""pre_llm_call hook: offer the council when the task looks too heavy for one small model.

Sergiy's stack is free-only (see the 2026-07-31 decision), so "a stronger model"
is not a bigger single model — there isn't one available. The escalation target
is the MoA preset `council`: two free advisors plus the proven primary acting as
aggregator. This hook is the trigger that was missing; the target already exists.

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


def _primary():
    """Today's model, read fresh. Hardcoding it made the way-back advice wrong
    within a day: the morning router repicks the primary."""
    try:
        with open(PICK, encoding="utf-8") as f:
            return json.load(f).get("primary") or "модель дня"
    except Exception:
        return "модель дня"
TARGET = "moa:council"
RESUGGEST_AFTER_S = 6 * 3600      # same session, only after a long gap
MIN_CHARS = 80                    # below this nothing is heavy, whatever it says
THRESHOLD = 3

# Verbs that describe work spanning many files/sources, not a single edit.
_HEAVY = re.compile(
    r"(?:^|\W)(?:"
    r"спроектир|архитектур|мигрир|миграци|рефактор|аудит|проанализир|"
    r"сравн|исследу|разбер|собер[иь]|реестр|каталог|стратеги|"
    r"design|architect|migrat|refactor|audit|analy[sz]e|compare|research|"
    r"investigat|inventory|catalog"
    r")", re.I)

# "all/every" turns one item into a sweep.
_SWEEP = re.compile(
    r"(?:^|\W)(?:вес[ьяео]|всех|все|всё|каждо?[йгеюм]|полност|"
    r"\ball\b|\bevery\b|\bentire\b|\bwhole\b)", re.I)

_PATHISH = re.compile(r"(?:https?://\S+|(?:/[\w.-]+){2,}|\b[\w-]+\.(?:ts|tsx|py|md|json|ya?ml|sql)\b)")
_LIST_ITEM = re.compile(r"^\s*(?:\d+[.)]|[-*•])\s+\S", re.M)

# Control traffic and one-word replies are never tasks.
_NOT_A_TASK = re.compile(
    r"^\s*(?:/|стоп|останов|отмен|пауза|продолж|поехали|go\b|да\b|нет\b|ок\b|ok\b)", re.I)


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


def score(text):
    """Mechanical heaviness score. Every point is something you can point at."""
    pts = 0
    why = []
    n = len(text)
    if n > 1200:
        pts += 2; why.append("очень длинный запрос")
    elif n > 400:
        pts += 1; why.append("длинный запрос")

    heavy = len(set(m.group(0).strip().lower() for m in _HEAVY.finditer(text)))
    if heavy:
        pts += min(heavy, 2); why.append("работа сразу по многим объектам")

    paths = len(_PATHISH.findall(text))
    if paths >= 3:
        pts += 1; why.append(f"{paths} путей/ссылок")

    if len(_LIST_ITEM.findall(text)) >= 3:
        pts += 1; why.append("список из нескольких пунктов")

    # The strongest single signal, and worth two on its own: a sweeping verb
    # plus "all/every" is a task that repeats over a set, and length says
    # nothing about how big that set is. "Обойди все страны ЕС" is 25 words and
    # weeks of work; a 1200-character bug report is one fix.
    if heavy and _SWEEP.search(text):
        pts += 2; why.append("«все/каждый» — это обход множества, а не один случай")

    return pts, why


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

    # Already on the council (or any MoA preset) — nothing to offer.
    if "moa" in model.lower() or "council" in model.lower():
        return
    if len(msg.strip()) < MIN_CHARS or _NOT_A_TASK.match(msg):
        return

    # A forwarded client message is not Sergiy choosing to start heavy work; the
    # switcher marks those, and the offer would land on the wrong decision.
    if msg.lstrip().startswith("↪️") or "[Пересланное сообщение" in msg:
        return

    last = _load_state().get(session_id)
    if isinstance(last, (int, float)) and time.time() - last < RESUGGEST_AFTER_S:
        return

    pts, why = score(msg)
    if pts < THRESHOLD:
        return

    _mark(session_id)
    reason = ", ".join(why[:3])
    print(json.dumps({"context": (
        "[Подсказка системы, не от пользователя] Задача оценена как тяжёлая для "
        f"текущей модели ({reason}). ПЕРВОЙ строкой ответа предложи одним "
        f"предложением переключиться на совет моделей: `/model {TARGET}` "
        "(два советника + агрегатор), и упомяни, что вернуться можно через "
        f"`/model {_primary()}`. Затем ВЫПОЛНЯЙ задачу как обычно — это "
        "предложение, а не блокировка, и ждать ответа не нужно."
    )}, ensure_ascii=False))


if __name__ == "__main__":
    main()
