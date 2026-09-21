#!/usr/bin/env python3
"""article_package.py — механика publish-package, вынутая из seo-publisher.

WHY THIS EXISTS
---------------
Замер прогона Telehealth Documentation (2026-09-21): seo-publisher (sonnet) сжёг
143K токенов и 31 tool-вызов, и почти всё это — грепы чек-листа, которые уже
считает (или тривиально может считать) article_lint.py + detect-ai-tells.py.
Тот же урок social-пайплайн выучил в августе: «механика — скриптами, не
агентами» (social_pack.py убрал ~59% координационной стоимости пака).

Новый контракт стадии publish:
  * seo-publisher пишет ТОЛЬКО суждение — workspace/seo/articles/<slug>/meta.md
    (meta title/description + варианты, slug, category, judgment-чеклист,
    open items, image/alt-концепты);
  * этот скрипт собирает publish-package.md: механический чек-лист считается
    кодом, lint и детектор прогоняются реально (не «оценкой» — урок 2026-08-25),
    их вывод вставляется verbatim ОДИН раз, STOP-правило применяется кодом.

Команды:
    checklist <slug> [--json]   механический чек-лист, без meta.md
    assemble  <slug> [--out F]  полный publish-package.md (требует meta.md)
    qc-prompt <slug>            компактный промпт для sonnet-QC (см. WHY ниже)

qc-prompt: в режиме без чекпоинтов (2026-09-21) единственный судья до
пост-фактум ревью Вадима — линт, а он судит механику, не аргумент. Полный
opus quality-controller сам ходит по файлам (~100K+ токенов). Этот режим
собирает ему готовый вход (рубрика + статья + факты линта + claims пака)
одним куском ~8-10K токенов — тот же приём, что social_pack.py qc-prompt.

Exit: 0 ok · 1 checklist STOP (вернуть в seo-editor) · 2 refused (нет входа,
причина на stdout) · 3 broken setup.
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART_ROOT = os.path.join(ROOT, "workspace", "seo", "articles")
PACK_ROOT = os.path.join(ROOT, "workspace", "seo", "_context-packs")
LINT = os.path.join(ROOT, "scripts", "article_lint.py")
DETECTOR = os.path.join(ROOT, "brand-assets", "style-guides", "scripts",
                        "detect-ai-tells.py")
RUBRIC = os.path.join(ROOT, "docs", "quality-rubric.md")

# Имена, которых не должно быть в статье без явного решения Вадима.
# Источник: CLAUDE.md §2 (live customers) + §8 (конкуренты). Список дублируется
# здесь сознательно: скрипт должен работать и тогда, когда агент «забыл»
# прочитать CLAUDE.md — это последний рубеж, а не первый.
NAMED_ENTITIES = [
    "UK Meds", "Yazen", "Healthyr", "Safariland", "Burlington Medical",
    "Jim's Formal Wear", "Generation Tux", "Tailoor", "Redthread",
    "Prism Labs", "Bodygram", "Size Stream",
]

# Устаревший телехелс-URL: 301 на structured-body-data-...; в brand-assets ещё
# встречается старая форма, и паки её наследуют (память 2026-09-19).
STALE_URLS = ["/fitxpress/for-telehealth-and-weight-loss/"]


def _die(code: int, msg: str) -> "None":
    print(msg)
    sys.exit(code)


def _read(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def _split_frontmatter(text: str):
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\n(.*?)\n---\n?", text, re.S)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t", "#")):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm, text[m.end():]


def _paths(slug: str):
    art_dir = os.path.join(ART_ROOT, slug)
    if not os.path.isdir(art_dir):
        _die(2, f"нет каталога статьи workspace/seo/articles/{slug}")
    final = os.path.join(art_dir, "final.md")
    if not os.path.isfile(final):
        _die(2, f"нет final.md в {slug} — publish собирается после edit-стадии")
    plan = os.path.join(art_dir, "plan.md")
    pack = os.path.join(PACK_ROOT, slug + ".yaml")
    meta = os.path.join(art_dir, "meta.md")
    return art_dir, final, plan, pack, meta


def _run_lint(final: str, pack: str):
    cmd = [sys.executable, LINT, os.path.relpath(final, ROOT),
           "--no-exit-code"]
    if os.path.isfile(pack):
        cmd += ["--pack", os.path.relpath(pack, ROOT)]
    txt = subprocess.run(cmd + [], cwd=ROOT, capture_output=True,
                         text=True).stdout
    js = subprocess.run(cmd + ["--json"], cwd=ROOT, capture_output=True,
                        text=True).stdout
    try:
        data = json.loads(js)
    except json.JSONDecodeError:
        _die(3, "article_lint.py --json вернул не-JSON:\n" + js[:500])
    return data, txt.rstrip()


def _run_detector(final: str):
    p = subprocess.run(
        [sys.executable, DETECTOR, final, "--channel", "article"],
        cwd=ROOT, capture_output=True, text=True)
    try:
        data = json.loads(p.stdout)
    except json.JSONDecodeError:
        _die(3, "detect-ai-tells.py вернул не-JSON:\n" + p.stdout[:500])
    summary = subprocess.run(
        [sys.executable, DETECTOR, final, "--channel", "article", "--summary"],
        cwd=ROOT, capture_output=True, text=True).stdout.rstrip()
    return data, summary


def _gate(lint: dict, name_part: str) -> dict:
    for g in lint.get("gates", []):
        if name_part in g.get("gate", ""):
            return g
    return {"ok": None, "info": {}, "problems": [f"gate '{name_part}' absent"]}


def _load_pack_bits(pack_path: str):
    """product / primary claims list / banned_words — без PyYAML-зависимости
    наружу: yaml есть в системе (пак им и валидируется)."""
    if not os.path.isfile(pack_path):
        return {}, [], []
    import yaml
    cp = yaml.safe_load(_read(pack_path)).get("context_pack", {})
    claims = [(c.get("id"), c.get("text", "")) for c in
              cp.get("approved_claims", [])]
    return cp, claims, cp.get("banned_words", []) or []


# --------------------------------------------------------------------------
# Механический чек-лист
# --------------------------------------------------------------------------

def build_checklist(slug: str):
    art_dir, final, plan, pack_path, _meta = _paths(slug)
    body_full = _read(final)
    fm, body = _split_frontmatter(body_full)
    plan_fm = _split_frontmatter(_read(plan))[0] if os.path.isfile(plan) else {}
    cp, claims, banned_words = _load_pack_bits(pack_path)
    lint, lint_text = _run_lint(final, pack_path)
    det, det_summary = _run_detector(final)

    kw = (plan_fm.get("primary_keyword") or
          _gate(lint, "keyword").get("info", {}).get("keyword") or "")
    kw_l = kw.lower()

    h1 = next((l[2:].strip() for l in body.splitlines()
               if l.startswith("# ")), "")
    h2s = [l[3:].strip() for l in body.splitlines() if l.startswith("## ")]
    kw_in_h2 = sum(1 for h in h2s if kw_l and kw_l in h.lower())

    text_l = body.lower()
    named_hits = sorted({n for n in NAMED_ENTITIES if n.lower() in text_l})
    stale_hits = [u for u in STALE_URLS if u in body]
    med = body.count("FitXpress is not a medical device.")
    positioned = len(re.findall(r"positioned as", body, re.I))
    faq_qs = 0
    faq_at = body.find("## FAQ")
    if faq_at >= 0:
        faq_qs = len(re.findall(r"^### ", body[faq_at:], re.M))
    not_do = bool(re.search(r"^##.*does not do", body, re.M | re.I))
    # scope note: курсивный абзац в первых ~20 строках тела
    top = [l.strip() for l in body.splitlines()[:22] if l.strip()]
    scope_note = any(l.startswith("*") and l.endswith("*") and len(l) > 40
                     for l in top)

    g_len = _gate(lint, "prose length").get("info", {})
    words, target = g_len.get("prose_words"), g_len.get("target")
    g_links = _gate(lint, "internal links").get("info", {}).get("directions", {})

    def item(key, ok, note, block="seo"):
        return {"key": key, "ok": bool(ok), "note": note, "block": block}

    items = [
        item("lint_verdict", lint.get("verdict") == "PASS",
             f"article_lint: {lint.get('verdict')}"),
        item("detector_clean", not det.get("hard_fails")
             and not det.get("house_rule_violations"),
             f"ai_density {det.get('ai_density_per_1000_words')}/1000, "
             f"hard_fails {det.get('hard_fails')}, "
             f"house_rules {det.get('house_rule_violations')}"),
        item("keyword_h1", bool(kw_l) and kw_l in h1.lower(),
             f"«{kw}» в H1: «{h1}»"),
        item("keyword_h2", 1 <= kw_in_h2 <= 2,
             f"keyword в {kw_in_h2} H2 (норма 1-2)"),
        item("claims_traceable", _gate(lint, "claim").get("ok"),
             f"claims_used: {_gate(lint, 'claim').get('info', {}).get('claims_used')}"),
        item("no_banned_claims",
             _gate(lint, "banned").get("ok") and _gate(lint, "superseded").get("ok"),
             "banned claims + superseded figures gates", block="compliance"),
        item("word_count", bool(words and target) and
             abs(words - target) / target <= 0.15,
             f"{words} слов против target {target} (полоса линтера ±15%; "
             f"жёсткие ±10% = {'ok' if words and target and abs(words-target)/target <= 0.10 else 'MISS — отметить в open items'})"),
        item("links_4_directions",
             all(g_links.get(d, 0) >= 1 for d in ("up", "sideways", "down", "trust")),
             f"направления: {g_links}"),
        item("medical_framing", med >= 1 and positioned == 0,
             f"«FitXpress is not a medical device.» ×{med}; "
             f"«positioned as» ×{positioned}", block="compliance"),
        item("no_named_entities", not named_hits,
             "клиенты/конкуренты: " + (", ".join(named_hits) or "нет"),
             block="compliance"),
        item("no_stale_urls", not stale_hits,
             "устаревшие URL: " + (", ".join(stale_hits) or "нет")),
        item("accuracy_discipline", _gate(lint, "accuracy").get("ok"),
             str(_gate(lint, "accuracy").get("info", {})), block="compliance"),
        item("m1_abbreviations", _gate(lint, "abbrev").get("ok"),
             "gate 8 (M1)"),
        item("sentence_length", _gate(lint, "sentence").get("ok"),
             f"mean {_gate(lint, 'sentence').get('info', {}).get('mean_words')}"),
        item("faq_present", faq_at >= 0 and faq_qs >= 2,
             f"FAQ: {faq_qs} вопросов"),
        item("boundary_section", not_do or scope_note,
             f"«does not do»-секция: {not_do}; scope note сверху: {scope_note}"),
        item("scope_note_early", scope_note,
             "курсивная scope note в первых строках"),
    ]
    ctx = {
        "slug": slug, "keyword": kw, "h1": h1, "h2s": h2s,
        "word_count": words, "target": target,
        "lint_text": lint_text, "lint_json": lint,
        "detector": det, "detector_summary": det_summary,
        "plan_fm": plan_fm, "final_fm": fm, "pack": cp,
        "claims": claims, "banned_words": banned_words,
        "art_dir": art_dir, "final": final, "meta": _meta,
    }
    return items, ctx


def _stop_rule(items, judgment_fails=0):
    fails = [i for i in items if not i["ok"]]
    comp = [i for i in fails if i["block"] == "compliance"]
    total = len(fails) + judgment_fails
    if comp:
        return ("STOP", "❌ в блоке positioning/compliance: "
                + ", ".join(i["key"] for i in comp))
    if total >= 2:
        return ("STOP", f"{total} ❌ суммарно (порог 2)")
    return ("OK", "")


def _fmt_items(items):
    out = []
    for i in items:
        out.append(f"- [{'x' if i['ok'] else '✗'}] **{i['key']}** — {i['note']}")
    return "\n".join(out)


# --------------------------------------------------------------------------
# meta.md — суждение агента
# --------------------------------------------------------------------------

META_REQUIRED = ("meta_title", "meta_description", "url_slug")


def parse_meta(meta_path: str):
    if not os.path.isfile(meta_path):
        _die(2, f"нет {os.path.relpath(meta_path, ROOT)} — стадия publish "
                "теперь пишет meta.md (суждение), пакет собирает скрипт. "
                "См. .claude/agents/seo/seo-publisher.md")
    fm, body = _split_frontmatter(_read(meta_path))
    missing = [k for k in META_REQUIRED if not fm.get(k)]
    if missing:
        _die(2, "meta.md без полей: " + ", ".join(missing))
    judgment = re.findall(r"^- \[( |x|✗)\] ?(.+)$", body, re.M)
    j_items = [(mark == "x", text) for mark, text in judgment]
    return fm, body, j_items


def check_meta(fm: dict, keyword: str, banned_words):
    """Механическая часть проверки меты. Судейскую (hook, не повторяет title
    смыслово) держит агент."""
    t, d = fm["meta_title"], fm["meta_description"]
    probs = []
    if len(t) > 60:
        probs.append(f"meta title {len(t)} chars (>60)")
    if not (140 <= len(d) <= 160):
        # Полоса из промпта publisher-а; лёгкий недобор не валит, но виден.
        probs.append(f"meta description {len(d)} chars (норма 140-160)")
    if keyword and keyword.lower() not in t.lower():
        probs.append("primary keyword не в meta title")
    elif keyword and t.lower().find(keyword.lower()) > len(t) / 2:
        probs.append("primary keyword во второй половине title")
    if keyword and d.lower().count(keyword.lower()) != 1:
        probs.append(f"keyword в description ×{d.lower().count(keyword.lower())} (норма 1)")
    for ch in "—–":
        if ch in t + d:
            probs.append("em/en dash в мете")
    low = (t + " " + d).lower()
    hits = [w for w in banned_words if re.search(rf"\b{re.escape(str(w))}\b", low)]
    if hits:
        probs.append("banned words в мете: " + ", ".join(map(str, hits)))
    return probs


# --------------------------------------------------------------------------
# assemble
# --------------------------------------------------------------------------

def cmd_assemble(a):
    items, ctx = build_checklist(a.slug)
    meta_fm, meta_body, j_items = parse_meta(ctx["meta"])
    meta_probs = check_meta(meta_fm, ctx["keyword"], ctx["banned_words"])
    j_fails = sum(1 for ok, _ in j_items if not ok)
    verdict, why = _stop_rule(items, j_fails)
    today = _dt.date.today().isoformat()

    mech_ok = sum(1 for i in items if i["ok"])
    lines = [
        "---",
        f"slug: {a.slug}",
        f"product: {ctx['pack'].get('product', 'fitxpress')}",
        "status: ready_for_review",
        f"created: {today}",
        f"generated_by: scripts/article_package.py (mechanics) + seo-publisher meta.md (judgment)",
        f"source_final: \"final.md ({ctx['word_count']} prose words, lint {ctx['lint_json'].get('verdict')})\"",
        f"word_count: {ctx['word_count']}",
        f"stop_rule: {verdict}" + (f"  # {why}" if why else ""),
        "---",
        "",
        f"# Publish Package — {a.slug}",
        "",
        "## Meta",
        "",
        f"**Title:** {meta_fm['meta_title']} ({len(meta_fm['meta_title'])}/60 chars)",
        f"**Description:** {meta_fm['meta_description']} ({len(meta_fm['meta_description'])}/160 chars)",
        f"**Slug:** `{meta_fm['url_slug']}`",
        f"**Category:** {meta_fm.get('category', '(не задана)')}",
    ]
    if meta_probs:
        lines += ["", "⚠️ Механические замечания к мете:"] + \
                 [f"- {p}" for p in meta_probs]
    lines += [
        "",
        f"## Механический чек-лист ({mech_ok}/{len(items)}, считал скрипт)",
        "",
        _fmt_items(items),
        "",
        f"## Суждение seo-publisher — {len(j_items) - j_fails}/{len(j_items)} "
        "judgment-пунктов ok (meta.md, verbatim без frontmatter)",
        "",
        meta_body.strip() if j_items else
        "(meta.md не содержит judgment-пунктов `- [x] …` — это дыра, не норма)",
        "",
        "## article_lint.py, verbatim",
        "",
        "```",
        ctx["lint_text"],
        "```",
        "",
        "## detect-ai-tells.py, verbatim (--summary)",
        "",
        "```",
        ctx["detector_summary"],
        "```",
        "",
        "## Article",
        "",
        f"Текст НЕ дублируется в пакете: единственный источник — `final.md` "
        f"({ctx['word_count']} prose words) рядом с этим файлом.",
        "",
    ]
    out = a.out or os.path.join(ctx["art_dir"], "publish-package.md")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"💾 {os.path.relpath(out, ROOT)}")
    print(f"механика {mech_ok}/{len(items)} · суждение "
          f"{len(j_items) - j_fails}/{len(j_items)} · STOP-rule: {verdict}"
          + (f" ({why})" if why else ""))
    if verdict == "STOP":
        print("→ вернуть в seo-editor, пакет собран для разбора, не для CMS")
        sys.exit(1)


def cmd_checklist(a):
    items, ctx = build_checklist(a.slug)
    verdict, why = _stop_rule(items)
    if a.json:
        print(json.dumps({"slug": a.slug, "items": items,
                          "stop_rule": verdict, "why": why},
                         ensure_ascii=False, indent=1))
    else:
        print(_fmt_items(items))
        ok = sum(1 for i in items if i["ok"])
        print(f"\n{ok}/{len(items)} · STOP-rule (механика): {verdict}"
              + (f" ({why})" if why else ""))
    sys.exit(1 if verdict == "STOP" else 0)


# --------------------------------------------------------------------------
# qc-prompt
# --------------------------------------------------------------------------

def cmd_qc_prompt(a):
    items, ctx = build_checklist(a.slug)
    rubric = _read(RUBRIC) if os.path.isfile(RUBRIC) else "(рубрика не найдена)"
    plan_outline = "\n".join(
        l for l in _read(os.path.join(ctx["art_dir"], "plan.md")).splitlines()
        if l.startswith("### Section")) if os.path.isfile(
        os.path.join(ctx["art_dir"], "plan.md")) else "(plan.md нет)"
    claims = "\n".join(f"- {cid}: {txt[:160]}" for cid, txt in ctx["claims"])
    fails = [i for i in items if not i["ok"]]
    # slug уже несёт дату-префикс — не дублировать её в имени отчёта
    # (та же ловушка, что в ahrefs-keywords.py, память 2026-09-21)
    report_name = a.slug if re.match(r"\d{4}-\d{2}-\d{2}-", a.slug) \
        else _dt.date.today().isoformat() + "-" + a.slug
    print(f"""Ты — QC-инспектор SEO-статьи. Весь вход в этом сообщении, по файлам НЕ ходи.
Оцени статью по 20-балльной рубрике ниже. Категории B (факты/цифры) и D
(формат/механика) УЖЕ проверены кодом — прими вердикты как данность и оценивай
A (соответствие плану и интенту), C (голос, читабельность, аргумент) и E
(позиция/ценность: говорит ли статья что-то, чего не сказал бы шаблон).
Отчёт запиши в workspace/_quality/seo/{report_name}.md
в формате рубрики (категории, баллы, 2-3 конкретных примера с цитатами,
verdict, actionable-замечания для agent-improver).

=== РУБРИКА (docs/quality-rubric.md) ===
{rubric}

=== ФАКТЫ ОТ КОДА (не перепроверяй) ===
lint verdict: {ctx['lint_json'].get('verdict')} · слова: {ctx['word_count']} / target {ctx['target']}
детектор: {ctx['detector'].get('ai_density_per_1000_words')}/1000, hard_fails {ctx['detector'].get('hard_fails')}
механический чек-лист: {sum(1 for i in items if i['ok'])}/{len(items)} ok"""
          + ("; провалы: " + "; ".join(f"{i['key']} ({i['note']})" for i in fails)
             if fails else "")
          + f"""

=== ПЛАН (аутлайн, для категории A) ===
primary keyword: {ctx['keyword']}
{plan_outline}

=== APPROVED CLAIMS (id: суть) ===
{claims}

=== СТАТЬЯ (final.md, полностью) ===
{_read(ctx['final'])}""")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("checklist")
    p.add_argument("slug")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=cmd_checklist)
    p = sub.add_parser("assemble")
    p.add_argument("slug")
    p.add_argument("--out", help="куда писать (default: publish-package.md рядом со статьёй)")
    p.set_defaults(fn=cmd_assemble)
    p = sub.add_parser("qc-prompt")
    p.add_argument("slug")
    p.set_defaults(fn=cmd_qc_prompt)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
