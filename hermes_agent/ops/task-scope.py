#!/usr/bin/env python3
"""Deterministic scope classifier: is this task an ad-hoc `claude -p` call, or a
conductor job?

Why a script and not the manager's judgement: Hermes runs the strongest FREE model
that can see images, which is a small one. Asked to weigh "is this a whole feature?"
it guesses — and it guessed wrong on "сделай вкладку каналов с товарами: фильтры,
динамический поиск, В НАЯВНОСТІ выделен, стиль как у Chanel/Hermès", sending a
multi-file UI+logic+design task into a single 40-turn `claude -p`. That run burned
its budget and came back as `error_max_turns`. The routing tree already says such
work belongs to the conductor (300 steps, split into stages, verified); the missing
piece was a reliable way to recognise it.

Same shape as route-profile.sh: mechanical, explainable, callable from both the
skill and the switcher, so the answer never depends on which model is loaded.

    python3 task-scope.py "<task text>"        → conductor | adhoc | ambiguous
    python3 task-scope.py --json "<task>"      → full reasoning
    python3 task-scope.py --explain "<task>"   → human-readable verdict

Exit code mirrors the verdict (0 adhoc, 1 conductor, 2 ambiguous) so shell callers
can branch without parsing.
"""
import json
import re
import sys

# --- signals that the work is a PROJECT, not an edit -------------------------
# Deliverables that mean "a whole thing", not "a change to a thing".
_BIG_NOUNS = (
    "вкладк", "страниц", "раздел", "модул", "приложени", "сайт", "лендинг",
    "дашборд", "панел", "личный кабинет", "интернет-магазин", "магазин",
    "бот с нул", "апи с нул", "микросервис", "пайплайн", "воронк",
    "page", "screen", "dashboard", "landing", "app", "module", "feature",
)
# Explicit end-to-end intent.
_TURNKEY = (
    "под ключ", "с нуля", "целиком", "полностью", "от а до я", "от начала до конца",
    "end-to-end", "a→z", "a->z", "с нуля до", "весь функционал", "всё вместе",
)
# Layers: a task touching several of these at once is a project by definition.
_LAYERS = {
    "ui": ("вёрстк", "верстк", "дизайн", "стил", "адаптив", "анимаци", "компонент",
           "ui", "ux", "layout", "styling", "тем", "шрифт", "цвет"),
    "логика": ("логик", "фильтр", "поиск", "сортировк", "пагинац", "валидац",
               "состояни", "стейт", "роутинг", "logic", "search", "filter"),
    "данные": ("бд", "база данных", "схем", "миграц", "supabase", "postgres",
               "таблиц", "модел данных", "api", "endpoint", "запрос", "кэш"),
    "интеграции": ("оплат", "stripe", "платёж", "платеж", "авториз", "auth",
                   "вебхук", "webhook", "телеграм-бот", "уведомлени", "почт",
                   "интеграц", "oauth"),
    "качество": ("тест", "e2e", "playwright", "покрыти", "ci", "деплой", "deploy",
                 "верификац", "аудит"),
}
# Signals of a small, surgical change.
_SMALL = (
    "почини", "пофикс", "исправь", "поправь", "багфикс", "найди баг", "найди причину",
    "объясни", "покажи", "посмотри", "проверь", "статус", "прочитай", "grep",
    "переименуй", "удали", "добавь кнопк", "поменяй текст", "поменяй цвет",
    "обнови зависимост", "подними версию", "одну строк", "опечатк", "typo",
    "почему падает", "почему не работает", "залей", "закоммить", "запушь",
)
# Words that make it a REQUEST TO BUILD rather than a question or an ops chore.
_BUILD_VERBS = (
    "сделай", "создай", "сверстай", "напиши", "реализуй", "разработай", "собери",
    "добавь", "внедри", "построй", "перепиши", "отрефактор", "спроектируй",
    "build", "create", "implement", "make", "develop", "add",
)
# Requests are just as often stated as REQUIREMENTS, with no imperative anywhere:
# "надо чтобы все каналы были хорошо отображены в первой вкладке, с фильтрами…".
# The first version of this classifier gated every scope signal on an imperative and
# therefore called that exact message "adhoc" — the very task whose 40-turn run died
# on error_max_turns. Intent is imperative OR requirement phrasing.
_REQUIREMENT = (
    "надо чтобы", "нужно чтобы", "хочу чтобы", "хотел бы чтобы", "должно быть",
    "должен быть", "должна быть", "должны быть", "чтобы было", "требуется",
    "надо сделать", "нужно сделать", "как договаривались", "как мы договаривались",
    "should be", "must be", "needs to be", "i want",
)
# A style reference ("под стиль Chanel", "в стиле …") means a design system has to be
# derived and applied consistently — never a one-file edit.
_STYLE_REF = ("под стиль", "в стиле", "как у ", "стиль вэб", "стиль веб",
              "style of", "look like", "дизайн-систем", "design system")

_LONG_BRIEF = 260          # a brief this long is describing a scope, not a fix
_MANY_ITEMS = 3            # enumerated deliverables ("фильтры, поиск, логика, стиль")


def _has(text, needles):
    return [n for n in needles if n in text]


def _enumerated(text):
    """Count comma/'и'-separated deliverables in the longest enumeration."""
    best = 0
    for chunk in re.split(r"[.;\n]", text):
        parts = [p for p in re.split(r",| и | plus |\+", chunk) if len(p.strip()) > 2]
        best = max(best, len(parts))
    return best


def classify(text):
    """→ {scope, score, reasons, layers, build_intent}"""
    t = (text or "").lower()
    reasons, score = [], 0

    build = _has(t, _BUILD_VERBS)
    requirement = _has(t, _REQUIREMENT)
    intent = build or requirement          # imperative OR "надо чтобы …"
    small = _has(t, _SMALL)

    big_nouns = _has(t, _BIG_NOUNS)
    if big_nouns and intent:
        score += 2
        reasons.append(f"целый объект работы: {', '.join(big_nouns[:3])}")

    turnkey = _has(t, _TURNKEY)
    if turnkey:
        score += 2
        reasons.append(f"«под ключ»: {', '.join(turnkey[:2])}")

    layers = [name for name, words in _LAYERS.items() if _has(t, words)]
    if len(layers) >= 2:
        score += len(layers) - 1
        reasons.append(f"слоёв затронуто {len(layers)}: {', '.join(layers)}")

    items = _enumerated(t)
    if items >= _MANY_ITEMS and intent:
        score += 1
        reasons.append(f"перечислено требований: {items}")

    if len(t) >= _LONG_BRIEF and intent:
        score += 1
        reasons.append(f"длинный бриф ({len(t)} символов)")

    style = _has(t, _STYLE_REF)
    if style and intent:
        score += 1
        reasons.append(f"требуется дизайн-система: {', '.join(style[:2])}")

    if small:
        score -= 2
        reasons.append(f"признаки точечной правки: {', '.join(small[:3])}")

    if not intent:
        score -= 2
        reasons.append("нет ни приказа, ни требования — вопрос или ops-задача")

    if score >= 3:
        scope = "conductor"
    elif score <= 0:
        scope = "adhoc"
    else:
        scope = "ambiguous"
    return {"scope": scope, "score": score, "reasons": reasons,
            "layers": layers, "build_intent": bool(intent)}


_EXIT = {"adhoc": 0, "conductor": 1, "ambiguous": 2}


def main(argv):
    mode = "plain"
    args = list(argv[1:])
    if args and args[0] in ("--json", "--explain"):
        mode = args.pop(0).lstrip("-")
    text = " ".join(args)
    if not text.strip():
        print("usage: task-scope.py [--json|--explain] \"<task text>\"",
              file=sys.stderr)
        return 3
    r = classify(text)
    if mode == "json":
        print(json.dumps(r, ensure_ascii=False, indent=2))
    elif mode == "explain":
        verdict = {"conductor": "ДИРИЖЁР (сложная фича)",
                   "adhoc": "claude -p (точечная задача)",
                   "ambiguous": "НЕЯСНО — спроси одним вопросом"}[r["scope"]]
        print(f"{verdict}  [вес {r['score']}]")
        for x in r["reasons"]:
            print(f"  · {x}")
    else:
        print(r["scope"])
    return _EXIT[r["scope"]]


if __name__ == "__main__":
    sys.exit(main(sys.argv))
