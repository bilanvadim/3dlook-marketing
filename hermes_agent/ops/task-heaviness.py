#!/usr/bin/env python3
"""The ONE mechanical test for "is this task too heavy for the everyday model".

Two callers used to answer that question with two different implementations, and
they disagreed:

  * ops/agent-hooks/suggest-stronger-model.py — a weighted score with reasons, an
    80-character floor and a "not a task" gate. Careful, explainable, hard to fool.
  * ops/claude-switcher/claude_switcher.py::looks_heavy() — an OR over a verb list
    plus "longer than 320 chars". No floor, no gate: "ок, а почему падает?" scored
    heavy, and every 320-character paste did too.

The switcher used its version for BOTH offering heavy mode and deciding whether a
follow-up is still on-topic, so the loose version was the one steering the model.
This module is the merged, stricter answer, imported by both — the same pattern
task-scope.py and route-profile.sh already use for intent and profile, and for the
same reason: two copies of a rule are two rules.

Scoring is mechanical on purpose. Asking the small everyday model "is this beyond
you?" asks it for exactly the judgement it is least able to make.

Usage:
    from task_heaviness import score, looks_heavy      # in-process
    python3 task-heaviness.py "<text>"                 # prints verdict + reasons
"""

import re
import sys

# Below this nothing counts, whatever words it contains: a one-line question is a
# question. This floor is what the switcher lacked.
MIN_CHARS = 80
# Points needed to call a task heavy. 3 means at least two independent signals, or
# one strong one plus length — a single verb never carries it alone.
THRESHOLD = 3

# Verbs describing work that spans many files, sources or decisions — not one edit.
# Merged from both callers; the switcher contributed the root-cause and planning
# intents, the hook the sweep/inventory ones.
# NO leading (?:^|\W) on the Russian stems: Russian prefixes verbs, so that anchor
# silently killed the most common forms — "Отрефактори" scored ZERO because "рефактор"
# is preceded by a letter, not a boundary. Inherited from the hook and measured on a
# labelled set. English words keep \b, where a bare substring WOULD overmatch.
_HEAVY = re.compile(
    r"(?:"
    r"спроектир|проектир|архитектур|мигрир|миграци|рефактор|переработа|перепиш|"
    r"аудит|проанализир|анализ|сравн|исследу|разбер|собер[иь]|"
    r"реестр|каталог|стратеги|спланир|распланир|составь план|продума|оптимизир"
    r")|\b(?:"
    r"design|architect|migrat|refactor|audit|analy[sz]e|compare|research|"
    r"investigat|inventory|catalog|plan|strateg"
    r")", re.I)

# Debugging a system, as opposed to fixing a known line. These read as heavy even
# in a short message, because the work is the search, not the edit.
_DEBUG = re.compile(
    r"(?:"
    r"перв(?:опричин|ая причина)|найди причину|разбери причин|"
    r"почему (?:не работает|падает|медленн|не запускается|ломается)|"
    r"не понимаю почему|непонятно почему|дедлок|гонк[аи]|утечк[аи]|"
    r"тормозит|производительн|флак|через раз|воспроизв|регресс"
    r")|\b(?:"
    r"root cause|deadlock|race condition|memory leak|leak|flaky|reproduc|regress"
    r")", re.I)

# "all / every / everywhere" turns one item into a sweep of unknown size.
_SWEEP = re.compile(
    r"(?:^|\W)(?:вес[ьяео]|всех|все|всё|каждо?[йгеюм]|полност|повсюду|везде|"
    r"\ball\b|\bevery\b|\bentire\b|\bwhole\b|\beverywhere\b)", re.I)

# "по 4 файлам", "в трёх сервисах" — an explicit COUNT of things to touch. This is
# the module's own definition of heavy ("work spanning many files") stated in plain
# words, and nothing else was catching it: a cross-file refactor is routinely short
# and names exactly one heavy verb, so it scored 1 and read as light. Requires 2+,
# because "в 1 файле" is the opposite signal.
_MULTI = re.compile(
    r"\b(?:[2-9]|\d{2,}|дв(?:а|ух|е)|тр(?:и|ёх|ех)|четыр|пят[ьи]|шест[ьи]|семи?|"
    r"нескольк|множеств)\w*\s+(?:файл|модул|сервис|компонент|табли|мест|"
    r"репозитор|проект|страниц|эндпоинт|метод|класс)", re.I)

_PATHISH = re.compile(r"(?:https?://\S+|(?:/[\w.-]+){2,}|\b[\w-]+\.(?:ts|tsx|py|md|json|ya?ml|sql|sh|toml)\b)")
_LIST_ITEM = re.compile(r"^\s*(?:\d+[.)]|[-*•])\s+\S", re.M)
# A pasted stack trace / log / diff is a debugging task by itself.
_FENCE = re.compile(r"```|^\s{4,}(?:at |File \"|Traceback|\+\+\+|---)", re.M)
_TRACE = re.compile(r"Traceback \(most recent call last\)|^\s*at [\w$.]+\(|Exception in thread|panic:", re.M)

# Control traffic, acks and one-word replies are never tasks.
_NOT_A_TASK = re.compile(
    r"^\s*(?:/|стоп|останов|отмен|пауза|продолж|поехали|давай\b|go\b|да\b|нет\b|"
    r"ок\b|ok\b|окей\b|спасибо|благодар|пон(?:ял|ятно)\b|ага\b|ясно\b)", re.I)
# A forwarded client message is not the owner choosing to start heavy work.
_FORWARDED = ("↪️", "[Пересланное сообщение")


def is_task(text: str) -> bool:
    """False for control traffic, acks, forwards and anything under the floor.

    Checked before scoring, never after: a 200-character "спасибо, всё понятно,
    давай потом разберёмся со всеми остальными" would otherwise collect points for
    length and for "всеми".
    """
    t = (text or "").strip()
    if len(t) < MIN_CHARS:
        return False
    if _NOT_A_TASK.match(t):
        return False
    if t.startswith(_FORWARDED[0]) or _FORWARDED[1] in t:
        return False
    return True


def score(text: str):
    """(points, reasons). Every point is something you can point at in the text."""
    text = text or ""
    if not is_task(text):
        return 0, []
    pts = 0
    why = []
    n = len(text)
    if n > 1200:
        pts += 2; why.append("очень длинный запрос")
    elif n > 400:
        pts += 1; why.append("длинный запрос")

    heavy = len({m.group(0).strip().lower() for m in _HEAVY.finditer(text)})
    if heavy:
        # Cap at 3, not 2: a brief that names three different heavy intents at once
        # ("спроектируй архитектуру … миграция существующих подписок") is heavy on
        # that alone, and it is routinely SHORT — so the length points never arrive
        # to push it over. Measured: with a cap of 2 that exact brief scored 2/3.
        pts += min(heavy, 3)
        why.append(f"тяжёлых интентов: {heavy}")

    debug = len({m.group(0).strip().lower() for m in _DEBUG.finditer(text)})
    if debug:
        # Root-cause work is the case where a small model fails most visibly: it
        # guesses a plausible cause and stops. Worth two on its own.
        pts += 2 if debug > 1 else 1
        why.append("поиск причины, а не правка известной строки")

    if _MULTI.search(text):
        pts += 1; why.append("названо несколько объектов работы")

    paths = len(_PATHISH.findall(text))
    if paths >= 3:
        pts += 1; why.append(f"{paths} путей/ссылок")

    if len(_LIST_ITEM.findall(text)) >= 3:
        pts += 1; why.append("список из нескольких пунктов")

    if _TRACE.search(text):
        pts += 2; why.append("вставлен стектрейс")
    elif _FENCE.search(text):
        pts += 1; why.append("вставлен код или лог")

    # The strongest single signal, and worth two on its own: a sweeping verb plus
    # "all/every" is a task that repeats over a set, and length says nothing about
    # how big that set is. "Обойди все страны ЕС" is 25 words and weeks of work; a
    # 1200-character bug report is one fix.
    if (heavy or debug) and _SWEEP.search(text):
        pts += 2; why.append("«все/каждый» — это обход множества, а не один случай")

    return pts, why


def looks_heavy(text: str) -> bool:
    """Boolean form for callers that only need the verdict."""
    return score(text)[0] >= THRESHOLD


def main() -> int:
    text = " ".join(sys.argv[1:])
    if not text:
        print("usage: task-heaviness.py <text>", file=sys.stderr)
        return 2
    pts, why = score(text)
    print(f"{'heavy' if pts >= THRESHOLD else 'light'} {pts} {'; '.join(why) or '—'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
