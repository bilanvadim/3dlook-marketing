#!/usr/bin/env python3
"""The social pack's short brand video: on-screen copy → HyperFrames → MP4.

Added 2026-11-02 (Vadim: «додай в соцпак» after the HyperFrames install). One video
per pack, 15-20 s, silent, text only, rendered in two shapes from one copy:

    reel  1080×1920 (9:16)  Instagram Reels / Stories
    feed  1080×1350 (4:5)   LinkedIn company page, Facebook, Instagram feed

The words are written by `post-drafter` from the pack's FINAL posts (after lint,
brand check and QC), so the video never says anything the posts did not already
say and pass. Everything else is code, same rule as social_pack.py:

    prompt <slug> [--write]   the drafter's assignment → _video-prompt.md
    lint   <slug> [--json]    shape, lengths, numbers vs the pack's posts, AI-tells
    build  <slug>             fill the template into the build dir (no render)
    render <slug> [--format reel|feed|all] [--quality draft|looks|delivery]
    notify <slug>             send the rendered MP4s to Vadim's Telegram
    status <slug>             JSON: copy / renders / stale

Files:
    workspace/social/articles/<slug>/_video/video.json         the copy (drafter)
    workspace/social/articles/<slug>/_video/<fmt>-sheet.jpg    one frame per card
    workspace/social/articles/<slug>/_video/render.json        what was rendered, from what
    brand-assets/video/stat-reel.html                          the template (edit THIS)
    ~/3dlook-marketing-private/social-video/<slug>/<slug>-<fmt>.mp4   the renders

The MP4s go to the PRIVATE repo and `render` commits and pushes them there itself
(Vadim, 2026-11-02: «в гіт треба все додавати. у нас же є закритий репо»): binaries
stay out of the public repo's history, and nothing rendered lives only on the VPS.
`--no-commit` skips that while iterating. No private checkout → the MP4s fall back to
`_video/` here, which .gitignore keeps out of the public repo.

Build dirs live outside the repo (~/.cache/mvb-social-video/<slug>/<fmt>/): the
template resolves Satoshi through local(). The official font files are kept in the
private repo (`brand/fonts/satoshi/`, internal storage is allowed by ITF FFL §01) and
installed into ~/.local/share/fonts from there when missing; they must never be
copied into the public repo (§02). Telemetry is switched off in the subprocess env
because conductor jobs load project settings only, not the user env.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.dirname(HERE)                                  # …/marketing_vb
sys.path.insert(0, HERE)
from social_pack import (                                     # noqa: E402
    extract_body, pack_meta, pack_profiles, pack_root, published_url,
    split_frontmatter,
)

TEMPLATE = os.path.join(PROJ, "brand-assets", "video", "stat-reel.html")
LOGO = os.path.join(PROJ, "brand-assets", "video", "3dlook-logo-white.svg")
BUILD_ROOT = Path(os.environ.get("XDG_CACHE_HOME") or Path.home() / ".cache") / "mvb-social-video"
TELEGRAM_ENV = Path.home() / ".hermes" / ".env"
PRIVATE_ROOT = Path(os.environ.get("MVB_PRIVATE_REPO") or Path.home() / "3dlook-marketing-private")
PRIVATE_VIDEO = "social-video"                      # <private>/social-video/<slug>/
PRIVATE_FONTS = PRIVATE_ROOT / "brand" / "fonts" / "satoshi"
USER_FONTS = Path.home() / ".local" / "share" / "fonts" / "satoshi"
SATOSHI = ("Regular", "Medium", "Bold", "Black")    # the weights the template uses

HF_VERSION = "0.9.1"            # pinned: a CLI upgrade changes renders; bump deliberately
FPS = 30
DEFAULT_CTA = "Read the full article"

FORMATS = {
    # safe_* keep copy clear of the platform's own UI (Reels: top bar, caption + buttons)
    "reel": {"w": 1080, "h": 1920, "safe_top": 250, "safe_bottom": 420,
             "ratio": "9:16", "use": "Instagram Reels / Stories"},
    "feed": {"w": 1080, "h": 1350, "safe_top": 96, "safe_bottom": 96,
             "ratio": "4:5", "use": "LinkedIn company page, Facebook, Instagram feed"},
}

# (min words, max words, max chars) per field. The template's type sizes were set
# against these ceilings; `check` in render() is the backstop for layout.
LIMITS = {
    "eyebrow": (1, 4, 32),
    "hook": (3, 12, 80),
    "point": (2, 8, 48),
    "close": (3, 10, 64),
    "stat_value": (1, 3, 8),
    "stat_label": (3, 14, 100),
    "stat_source": (2, 10, 70),
    "cta": (2, 5, 28),
}

_EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿⬀-⯿️]")


def _post_lint():
    """post-lint.py has a hyphen in its name, so it is loaded by path."""
    spec = importlib.util.spec_from_file_location("post_lint", os.path.join(HERE, "post-lint.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------------------------------------------------------------------------
# paths and inputs
# ---------------------------------------------------------------------------

def video_dir(slug: str) -> str:
    return os.path.join(pack_root(slug), "_video")


def spec_path(slug: str) -> str:
    return os.path.join(video_dir(slug), "video.json")


def render_meta_path(slug: str) -> str:
    return os.path.join(video_dir(slug), "render.json")


def private_ok() -> bool:
    return (PRIVATE_ROOT / ".git").is_dir()


def mp4_dir(slug: str) -> str:
    """Where the renders live: the private repo, or `_video/` when there is none."""
    if private_ok():
        return str(PRIVATE_ROOT / PRIVATE_VIDEO / slug)
    return video_dir(slug)


def out_path(slug: str, fmt: str) -> str:
    return os.path.join(mp4_dir(slug), f"{slug}-{fmt}.mp4")


def mp4_display(slug: str, fname: str) -> str:
    """How the digest and the report name a render's location."""
    if private_ok():
        return f"3dlook-marketing-private/{PRIVATE_VIDEO}/{slug}/{fname}"
    return f"_video/{fname}"


def _sha(path_or_text: str, is_text: bool = False) -> str:
    data = path_or_text.encode("utf-8") if is_text else open(path_or_text, "rb").read()
    return hashlib.sha256(data).hexdigest()[:16]


def final_posts(slug: str):
    """[(profile, format, angle, claims, body)] for every post on disk in this pack."""
    out = []
    root = pack_root(slug)
    for pid, _plat, _h in pack_profiles(slug):
        p = os.path.join(root, pid, "post.md")
        if not os.path.exists(p):
            continue
        text = open(p, encoding="utf-8", errors="replace").read()
        fm, _ = split_frontmatter(text)
        body, _cta, _design = extract_body(text)
        if not body:
            continue
        angle = re.search(r"^\*\*Angle:\*\*\s*(.+)$", text, re.M)
        claims = re.search(r"^\*\*Claims used:\*\*\s*(.+)$", text, re.M)
        out.append((pid, fm.get("format", ""), angle.group(1).strip() if angle else "",
                    claims.group(1).strip() if claims else "", body))
    return out


def article_url(slug: str) -> str:
    """Published URL from the package; else the first 3dlook.ai link the posts carry."""
    url = published_url(slug)
    if url:
        return url
    for _pid, _f, _a, _c, body in final_posts(slug):
        m = re.search(r"https?://(?:www\.)?3dlook\.ai/[^\s)\]>\"']+", body)
        if m:
            return m.group(0).rstrip(".,;")
    return ""


def display_url(url: str) -> str:
    if not url:
        return "3dlook.ai"
    short = re.sub(r"^https?://(www\.)?", "", url).rstrip("/")
    return short if len(short) <= 56 else "3dlook.ai/content-hub"


def load_spec(slug: str):
    p = spec_path(slug)
    if not os.path.exists(p):
        return None, f"no copy yet: {os.path.relpath(p, PROJ)} (run `prompt {slug} --write` → post-drafter)"
    try:
        return json.load(open(p, encoding="utf-8")), None
    except ValueError as e:
        return None, f"video.json is not valid JSON: {e}"


# ---------------------------------------------------------------------------
# prompt
# ---------------------------------------------------------------------------

def build_prompt(slug: str):
    posts = final_posts(slug)
    if not posts:
        return None, f"pack `{slug}` has no posts on disk — the video is written from the final posts"
    meta = pack_meta(slug)
    aeo = meta.get("aeo") or {}
    rel_spec = os.path.relpath(spec_path(slug), PROJ)
    parts = [f"""# Video assignment: `{slug}`

You are writing the on-screen words for ONE short brand video (15-20 seconds, silent,
text only) that goes out next to this pack. A script renders it in the house template
in two shapes (9:16 for Instagram Reels, 4:5 for LinkedIn company, Facebook and
Instagram feed). You write words only, as JSON. Read nothing else first: everything
you need is in this file.

## Where the words come from

Only from the FINAL posts below. They already passed the number lint, the brand check
and QC. Shorten, cut and reorder their wording; never add a fact, a number, a product
capability, a customer or a claim that no post makes. Every number you use must appear
in a post below in the same digits (a script compares them). Wording about accuracy,
compliance or FitXpress's scope is taken exactly as a post words it, or left out.

## What the video is for

A teaser that stops the scroll and sends people to the article. One angle, not a
summary of the pack. Take the strongest angle the company accounts use
(`linkedin-company`, `instagram-company`, `facebook-company`) unless a personal post
carries a sharper, still company-safe point. The video speaks as 3DLOOK, never as a
person: no "I", no names, no market a personal profile is written for.

## The six fields

- `eyebrow`: the subject in 1-4 words, plain ("GLP-1 programs", "Occupational health").
- `hook`: one claim, never a question. 3-12 words, at most 80 characters. A viewer who
  sees only this line must know what the subject is.
- `stat` (optional object, omit it when no post carries a sourced figure; no stat beats
  a weak one): `value` at most 8 characters ("43%", "<1 cm"), `label` 3-14 words that
  make the number self-explanatory, `source` 2-10 words naming the source exactly as
  the post does ("KFF 2025 Employer Health Benefits Survey"). A figure from 3DLOOK's
  own validation uses the post's own wording and source line.
- `points`: 2 or 3 lines, each 2-8 words and at most 48 characters, parallel in form.
  Checklist questions are allowed here (they are the one place a question fits).
- `close`: 3-10 words, at most 64 characters: what the article gives the viewer.
- `cta`: leave out (the template says "{DEFAULT_CTA}").

House rules that hold on screen too: no em dash or en dash, no hashtags, no emoji, no
exclamation marks, English only. The house word bans hold exactly as in the posts
(they are checked mechanically after you save, along with every limit above).

## Output

Write exactly this shape to `{rel_spec}` (UTF-8 JSON, no comments, no trailing text):

```json
{{
  "eyebrow": "…",
  "hook": "…",
  "stat": {{"value": "…", "label": "…", "source": "…"}},
  "points": ["…", "…", "…"],
  "close": "…",
  "from_profiles": ["linkedin-company"]
}}
```

`from_profiles` lists the posts whose wording you used. When the file is saved, reply
with one line: the hook, and which profile's angle it comes from.
"""]
    if aeo.get("question"):
        parts.append(f"## The question this pack answers\n\n{aeo['question']}\n")
    parts.append("## The final posts\n")
    for pid, fmt, angle, claims, body in posts:
        parts.append(f"### {pid}" + (f" ({fmt})" if fmt else "") + "\n")
        if angle:
            parts.append(f"**Angle:** {angle}\n")
        if claims:
            parts.append(f"**Claims used:** {claims}\n")
        parts.append(body.strip() + "\n")
    return "\n".join(parts), None


# ---------------------------------------------------------------------------
# lint
# ---------------------------------------------------------------------------

def _words(s: str) -> int:
    return len(s.split())


def lint(slug: str):
    spec, err = load_spec(slug)
    if err:
        return {"verdict": "FAIL (1)", "hard_fails": [{"check": "missing", "detail": err}],
                "warnings": []}
    hard, warn = [], []

    def H(check, detail):
        hard.append({"check": check, "detail": detail})

    def W(check, detail):
        warn.append({"check": check, "detail": detail})

    def field(name, value, limit_key):
        if not isinstance(value, str) or not value.strip():
            H(f"shape:{name}", "missing or empty")
            return
        lo, hi, chars = LIMITS[limit_key]
        n = _words(value)
        if not lo <= n <= hi:
            H(f"length:{name}", f"{n} words (want {lo}-{hi}): {value!r}")
        if len(value) > chars:
            H(f"length:{name}", f"{len(value)} chars (max {chars}): {value!r}")

    if not isinstance(spec, dict):
        H("shape", "video.json must be an object")
        spec = {}
    known = {"eyebrow", "hook", "stat", "points", "close", "cta", "from_profiles"}
    for k in spec:
        if k not in known:
            W("shape:unknown-key", f"`{k}` is ignored by the template")
    field("eyebrow", spec.get("eyebrow"), "eyebrow")
    field("hook", spec.get("hook"), "hook")
    if "?" in str(spec.get("hook", "")):
        H("hook:question", "the hook is a claim, not a question")
    pts = spec.get("points")
    if not isinstance(pts, list) or not 2 <= len(pts) <= 3:
        H("shape:points", "points must be a list of 2 or 3 lines")
        pts = pts if isinstance(pts, list) else []
    for i, p in enumerate(pts):
        field(f"points[{i}]", p, "point")
    field("close", spec.get("close"), "close")
    if "cta" in spec:
        field("cta", spec.get("cta"), "cta")
    stat = spec.get("stat")
    if stat is not None:
        if not isinstance(stat, dict):
            H("shape:stat", "stat must be an object or left out")
        else:
            field("stat.value", stat.get("value"), "stat_value")
            field("stat.label", stat.get("label"), "stat_label")
            field("stat.source", stat.get("source"), "stat_source")
            if not re.search(r"\d", str(stat.get("value", ""))):
                H("stat:value", "a stat value carries a number")

    texts = [str(spec.get(k, "")) for k in ("eyebrow", "hook", "close", "cta")]
    texts += [str(p) for p in pts]
    if isinstance(stat, dict):
        texts += [str(stat.get(k, "")) for k in ("value", "label", "source")]
    joined = "\n".join(t for t in texts if t)

    for ch, name in (("—", "em dash"), ("–", "en dash"), ("#", "hashtag"), ("!", "exclamation mark")):
        if ch in joined:
            H("house:" + name.replace(" ", "-"), f"{name} on screen")
    if _EMOJI.search(joined):
        H("house:emoji", "emoji on screen")

    # numbers: every figure on screen must already be in a post of this pack, which in
    # turn passed post-lint's check against the article and proof-points.md
    PL = _post_lint()
    posts = final_posts(slug)
    post_digits = PL._num_tokens("\n".join(b for *_x, b in posts))
    for token, _val, _unit, _ in PL.numeric_claims(joined):
        d = re.findall(r"\d[\d,]*\.?\d*", token)
        if d and d[0].replace(",", "").rstrip(".") not in post_digits:
            H("numbers", f"`{token}` is not in any post of this pack")

    # the house detector, on the copy as sentences (same gate the posts went through)
    det = PL.run_detector(".\n".join(t.rstrip(".") for t in texts if t) + ".", "linkedin-company")
    if det.get("error"):
        W("ai-tells", det["error"])
    for hf in det.get("hard_fails", []) or []:
        ex = (hf.get("hits") or [{}])[0].get("example", "")
        H(f"ai-tells:{hf.get('category')}", f"{hf.get('count')}× — {ex[:120]}")
    for v in det.get("house_rule_violations", []) or []:
        if re.search(r"hashtag|emoji", str(v), re.I):
            H("ai-tells:house_rule", str(v)[:160])

    have = {p[0] for p in posts}
    for p in spec.get("from_profiles") or []:
        if p not in have:
            W("from_profiles", f"`{p}` has no post in this pack")
    if not article_url(slug):
        W("url", "no published URL found; the closing card shows 3dlook.ai")
    return {"video": os.path.relpath(spec_path(slug), PROJ),
            "verdict": "PASS" if not hard else f"FAIL ({len(hard)})",
            "hard_fails": hard, "warnings": warn}


# ---------------------------------------------------------------------------
# build
# ---------------------------------------------------------------------------

def _clamp(x, lo, hi):
    return max(lo, min(hi, x))


def _r(x):
    return round(x * 10) / 10


def timings(spec):
    """Card windows from word counts: longer copy stays longer on screen."""
    w = _words
    pts = spec["points"]
    # ceilings keep the longest legal copy at ~19.5 s (first render, 2026-11-02, ran 22.2 s)
    hook = _clamp(1.6 + 0.30 * w(spec["hook"]) + 0.1 * w(spec["eyebrow"]), 3.2, 4.6)
    stat = spec.get("stat")
    st = _clamp(2.2 + 0.26 * w(stat["label"]) + 0.1 * w(stat["source"]), 3.8, 5.0) if stat else 0
    step = 1.0
    pdur = _clamp(0.35 + step * (len(pts) - 1) + 1.0 + 0.2 * sum(w(p) for p in pts), 4.0, 6.0)
    close = 3.8
    t, out = 0.0, {}
    for name, d in (("hook", hook), ("stat", st), ("points", pdur), ("close", close)):
        if not d:
            continue
        d = _r(d)
        out[name] = {"start": _r(t), "end": _r(t + d), "dur": d}
        t += d
    out["points"]["items"] = [_r(out["points"]["start"] + 0.35 + i * step) for i in range(len(pts))]
    out["total"] = _r(t)
    return out


def fill(spec, fmt: str, url: str) -> tuple[str, dict]:
    f = FORMATS[fmt]
    T = timings(spec)
    e = lambda s: html.escape(str(s), quote=True)  # noqa: E731
    tpl = open(TEMPLATE, encoding="utf-8").read()
    stat = spec.get("stat")
    if not stat:
        tpl = re.sub(r"\s*<!--STAT:START-->.*?<!--STAT:END-->", "", tpl, flags=re.S)
    pts_html = "\n".join(
        f'          <li id="pt-{i}" class="pt"><span class="pt-dot"></span>'
        f'<span class="pt-text">{e(p)}</span></li>' for i, p in enumerate(spec["points"]))
    logo = re.sub(r'\s(width|height)="[^"]*"', "", open(LOGO, encoding="utf-8").read().strip(), count=2)
    hook_len = len(spec["hook"])
    pmax = max(len(p) for p in spec["points"])
    du = display_url(url)
    vals = {
        "W": f["w"], "H": f["h"], "SAFE_TOP": f["safe_top"], "SAFE_BOTTOM": f["safe_bottom"],
        "DURATION": T["total"],
        "HOOK_SIZE": 92 if hook_len <= 50 else 84 if hook_len <= 66 else 76,
        # 904 px = content width (1080 - 2 × 88). Satoshi Black digits and "%" measure
        # ~0.67 em, not 0.6: at 0.6 "40-60%" rendered 999 px and failed `check`
        # (text_box_overflow, 2026-11-06). 0.75 keeps a 0.8 em worst case on canvas.
        "STAT_SIZE": int(min(300, 904 / (0.75 * max(3, len(stat["value"]))))) if stat else 300,
        "POINT_SIZE": 58 if pmax <= 32 else 52 if pmax <= 42 else 48,
        "CLOSE_SIZE": 76 if len(spec["close"]) <= 40 else 66,
        "URL_SIZE": 30 if len(du) <= 44 else 26,
        "HOOK_START": T["hook"]["start"], "HOOK_DUR": T["hook"]["dur"],
        "POINTS_START": T["points"]["start"], "POINTS_DUR": T["points"]["dur"],
        "CLOSE_START": T["close"]["start"], "CLOSE_DUR": T["close"]["dur"],
        "EYEBROW": e(spec["eyebrow"]), "HOOK": e(spec["hook"]),
        "POINTS_HTML": pts_html, "CLOSE": e(spec["close"]),
        "CTA": e(spec.get("cta") or DEFAULT_CTA), "URL": e(du),
        "LOGO_SVG": logo, "TIMES_JSON": json.dumps(T),
    }
    if stat:
        vals.update({"STAT_START": T["stat"]["start"], "STAT_DUR": T["stat"]["dur"],
                     "STAT_VALUE": e(stat["value"]), "STAT_LABEL": e(stat["label"]),
                     "STAT_SOURCE": e(stat["source"])})
    out = re.sub(r"\{\{([A-Z_]+)\}\}", lambda m: str(vals[m.group(1)]), tpl)
    return out, T


def build(slug: str, fmt: str, spec) -> tuple[Path, dict]:
    d = BUILD_ROOT / slug / fmt
    if d.exists():
        assert BUILD_ROOT in d.parents, d          # never delete outside our cache
        shutil.rmtree(d)
    d.mkdir(parents=True)
    page, T = fill(spec, fmt, article_url(slug))
    (d / "index.html").write_text(page, encoding="utf-8")
    (d / "hyperframes.json").write_text(json.dumps({
        "$schema": "https://hyperframes.heygen.com/schema/hyperframes.json",
        "paths": {"blocks": "compositions", "components": "compositions/components", "assets": "assets"},
        "media": {"autoProxy": True}}, indent=2), encoding="utf-8")
    (d / "meta.json").write_text(json.dumps({"id": f"{slug}-{fmt}", "name": f"{slug} {fmt}"}), encoding="utf-8")
    return d, T


# ---------------------------------------------------------------------------
# render
# ---------------------------------------------------------------------------

def _hf(args, cwd, timeout):
    env = dict(os.environ, HYPERFRAMES_NO_TELEMETRY="1", NPM_CONFIG_UPDATE_NOTIFIER="false",
               NO_UPDATE_NOTIFIER="1")
    return subprocess.run(["npx", "--yes", f"hyperframes@{HF_VERSION}", *args], cwd=str(cwd),
                          env=env, capture_output=True, text=True, timeout=timeout)


def _json_tail(text: str):
    i = text.find("{")
    try:
        return json.loads(text[i:]) if i >= 0 else None
    except ValueError:
        return None


def _check_findings(d):
    """Error-level findings from `check --json`, whatever list they arrive in."""
    out = []
    def walk(x):
        if isinstance(x, dict):
            sev = str(x.get("severity") or x.get("level") or "").lower()
            msg = x.get("message") or x.get("detail")
            if msg and sev in ("error", "fail", "critical"):
                out.append(f"{x.get('code') or x.get('rule') or x.get('id') or '?'}: {str(msg)[:200]}")
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(d)
    return out


def _probe(path: str):
    p = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=width,height",
                        "-of", "json", path], capture_output=True, text=True)
    d = json.loads(p.stdout or "{}")
    st = (d.get("streams") or [{}])[0]
    return float(d.get("format", {}).get("duration", 0)), st.get("width"), st.get("height")


def _sheet(mp4: str, T: dict, dest: str):
    """One frame from the middle of each card, side by side: the reviewable still."""
    marks = [(T[k]["start"] + T[k]["end"]) / 2 + (0.4 if k == "close" else 0)
             for k in ("hook", "stat", "points", "close") if k in T]
    frames = "+".join(f"eq(n\\,{int(t * FPS)})" for t in marks)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", mp4, "-vf",
                    f"select='{frames}',scale=360:-1,tile={len(marks)}x1:padding=8:color=white",
                    "-frames:v", "1", "-q:v", "3", dest], check=True)


def ensure_fonts():
    """Satoshi must resolve through local(), or Chrome silently renders a fallback face.

    Installs the official OTFs from the private repo when fontconfig does not know
    them (a fresh box, a wiped ~/.local). Returns an error string or None."""
    have = subprocess.run(["fc-list", ":", "fullname"], capture_output=True, text=True).stdout
    missing = [w for w in SATOSHI if f"Satoshi {w}" not in have]
    if not missing:
        return None
    src = [PRIVATE_FONTS / f"Satoshi-{w}.otf" for w in SATOSHI]
    if not all(p.exists() for p in src):
        return (f"Satoshi {', '.join(missing)} not installed and not found in {PRIVATE_FONTS}. "
                "Download the official zip from fontshare.com/fonts/satoshi into that folder.")
    USER_FONTS.mkdir(parents=True, exist_ok=True)
    for p in src:
        shutil.copyfile(p, USER_FONTS / p.name)
    subprocess.run(["fc-cache", "-f", str(USER_FONTS)], capture_output=True)
    return None


def _git(*args, timeout=120):
    return subprocess.run(["git", "-C", str(PRIVATE_ROOT), *args],
                          capture_output=True, text=True, timeout=timeout)


def commit_private(slug: str, report: dict):
    """Commit and push this pack's renders in the private repo, and nothing else.

    `git commit -- <path>` takes only our folder even if someone left other changes
    staged there. A rejected push is retried once after `pull --rebase`; a failure is
    reported, never raised: the render itself is done and the file is on disk."""
    rel = f"{PRIVATE_VIDEO}/{slug}"
    if not private_ok():
        return {"status": "skipped", "why": f"no private checkout at {PRIVATE_ROOT}"}
    _git("add", "--", rel)
    if not _git("diff", "--cached", "--quiet", "--", rel).returncode:
        return {"status": "unchanged"}
    ok = [f"{e['ratio']} {e['duration']} s" for e in report["formats"].values() if e.get("status") == "ok"]
    msg = (f"social-video: {slug} ({', '.join(ok)})\n\n"
           f"Rendered by marketing_vb/scripts/social_video.py from "
           f"workspace/social/articles/{slug}/_video/video.json (public repo).")
    c = _git("commit", "-m", msg, "--", rel)
    if c.returncode:
        return {"status": "commit failed", "log": (c.stdout + c.stderr)[-400:]}
    sha = _git("rev-parse", "--short", "HEAD").stdout.strip()
    p = _git("push", "origin", "HEAD", timeout=300)
    if p.returncode:
        _git("pull", "--rebase", "--autostash", "origin", "main", timeout=300)
        p = _git("push", "origin", "HEAD", timeout=300)
        sha = _git("rev-parse", "--short", "HEAD").stdout.strip()
    return {"status": "pushed" if not p.returncode else "committed, push failed",
            "commit": sha, **({"log": (p.stdout + p.stderr)[-400:]} if p.returncode else {})}


def render(slug: str, fmts, quality: str, commit: bool = True):
    res = lint(slug)
    if res["hard_fails"]:
        return res, 1
    ferr = ensure_fonts()
    if ferr:
        return {"error": ferr}, 1
    spec, _ = load_spec(slug)
    os.makedirs(video_dir(slug), exist_ok=True)
    os.makedirs(mp4_dir(slug), exist_ok=True)
    meta_p = render_meta_path(slug)
    meta = json.load(open(meta_p, encoding="utf-8")) if os.path.exists(meta_p) else {}
    meta.setdefault("formats", {})
    report = {"video": os.path.relpath(spec_path(slug), PROJ), "formats": {}}
    rc = 0
    for fmt in fmts:
        d, T = build(slug, fmt, spec)
        chk = _hf(["check", "--json"], d, 300)
        cj = _json_tail(chk.stdout) or {}
        if chk.returncode != 0 or cj.get("ok") is False:
            report["formats"][fmt] = {"status": "check failed",
                                      "findings": _check_findings(cj)[:12] or [chk.stdout[-800:] or chk.stderr[-800:]]}
            rc = 1
            continue
        r = _hf(["render", "--quality", quality, "-o", "out.mp4"], d, 900)
        src = d / "out.mp4"
        if r.returncode != 0 or not src.exists() or src.stat().st_size == 0:
            report["formats"][fmt] = {"status": "render failed", "log": (r.stdout + r.stderr)[-1200:]}
            rc = 1
            continue
        dst = out_path(slug, fmt)
        shutil.copyfile(src, dst)
        dur, w, h = _probe(dst)
        if abs(dur - T["total"]) > 0.15 or (w, h) != (FORMATS[fmt]["w"], FORMATS[fmt]["h"]):
            report["formats"][fmt] = {"status": "probe mismatch",
                                      "detail": f"{dur:.2f}s {w}x{h}, want {T['total']}s "
                                                f"{FORMATS[fmt]['w']}x{FORMATS[fmt]['h']}"}
            rc = 1
            continue
        sheet = os.path.join(video_dir(slug), f"{fmt}-sheet.jpg")
        _sheet(dst, T, sheet)
        entry = {
            "file": os.path.basename(dst), "where": mp4_display(slug, os.path.basename(dst)),
            "sheet": os.path.basename(sheet),
            "ratio": FORMATS[fmt]["ratio"], "use": FORMATS[fmt]["use"],
            "width": w, "height": h, "duration": round(dur, 2),
            "bytes": os.path.getsize(dst), "sha256": _sha(dst),
            "quality": quality,
            # per format, so re-rendering one shape never vouches for the other
            "spec_sha": _sha(spec_path(slug)), "template_sha": _sha(TEMPLATE),
        }
        meta["formats"][fmt] = entry
        report["formats"][fmt] = {"status": "ok", **entry}
    meta.update({
        "rendered_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "hyperframes": HF_VERSION,
        "url": display_url(article_url(slug)),
    })
    if any(v.get("status") == "ok" for v in report["formats"].values()):
        json.dump(meta, open(meta_p, "w", encoding="utf-8"), indent=2)
        open(meta_p, "a").write("\n")
        if commit:
            report["private_repo"] = commit_private(slug, report)
            if report["private_repo"]["status"] not in ("pushed", "unchanged", "skipped"):
                rc = 1
    return report, rc


# ---------------------------------------------------------------------------
# status (also read by social_pack.py for manifest / digest / report)
# ---------------------------------------------------------------------------

def summary(slug: str) -> dict:
    """What exists for this pack's video. Empty dict when the pack has no copy."""
    if not os.path.exists(spec_path(slug)):
        return {}
    spec, err = load_spec(slug)
    out = {"copy": os.path.relpath(spec_path(slug), PROJ), "spec": spec if not err else None,
           "error": err, "formats": {}, "stale": False}
    mp = render_meta_path(slug)
    if os.path.exists(mp):
        try:
            meta = json.load(open(mp, encoding="utf-8"))
        except ValueError:
            meta = {}
        spec_now, tpl_now = _sha(spec_path(slug)), _sha(TEMPLATE)
        for fmt, e in (meta.get("formats") or {}).items():
            if os.path.exists(os.path.join(mp4_dir(slug), e.get("file", ""))):
                out["formats"][fmt] = e
                if e.get("spec_sha") != spec_now or e.get("template_sha") != tpl_now:
                    out["stale"] = True
        out["rendered_at"] = meta.get("rendered_at")
    return out


# ---------------------------------------------------------------------------
# notify
# ---------------------------------------------------------------------------

def _tg_creds():
    bot = chat = ""
    try:
        for line in TELEGRAM_ENV.open(encoding="utf-8"):
            if line.startswith("TELEGRAM_BOT_TOKEN="):
                bot = line.split("=", 1)[1].strip()
            elif line.startswith("TELEGRAM_ALLOWED_USERS="):
                chat = line.split("=", 1)[1].strip().split(",")[0]
    except OSError:
        pass
    return bot, chat


def notify(slug: str) -> int:
    s = summary(slug)
    if not s.get("formats"):
        print(f"✗ nothing rendered for `{slug}`", file=sys.stderr)
        return 1
    if s.get("stale"):
        print("✗ the renders are older than video.json or the template — render again first", file=sys.stderr)
        return 1
    bot, chat = _tg_creds()
    if not bot or not chat:
        print("(no TELEGRAM creds in ~/.hermes/.env — not sending)", file=sys.stderr)
        return 1
    spec = s.get("spec") or {}
    ok = True
    for fmt in ("reel", "feed"):
        e = s["formats"].get(fmt)
        if not e:
            continue
        cap = (f"🎬 {slug}: {e['ratio']}, {e['duration']:.0f} с, для {e['use']}.\n"
               f"Хук: {spec.get('hook', '')}\n"
               f"Текст: workspace/social/articles/{slug}/_video/video.json. Апрув разом з дайджестом.")
        # token through --config on stdin, never argv: /proc is world-readable
        r = subprocess.run(
            ["curl", "-s", "-m", "120", "--config", "-",
             "-F", f"chat_id={chat}", "-F", f"caption={cap[:1000]}",
             "-F", f"width={e['width']}", "-F", f"height={e['height']}",
             "-F", f"duration={int(round(e['duration']))}", "-F", "supports_streaming=true",
             "-F", f"video=@{os.path.join(mp4_dir(slug), e['file'])};type=video/mp4"],
            input=f'url = "https://api.telegram.org/bot{bot}/sendVideo"\n',
            text=True, capture_output=True)
        try:
            sent = json.loads(r.stdout).get("ok") is True
        except ValueError:
            sent = False
        print(f"{'✓' if sent else '✗'} {fmt} → Telegram")
        ok = ok and sent
    return 0 if ok else 1


# ---------------------------------------------------------------------------
# cli
# ---------------------------------------------------------------------------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("prompt"); p.add_argument("slug"); p.add_argument("--write", action="store_true")
    p = sub.add_parser("lint"); p.add_argument("slug"); p.add_argument("--json", action="store_true")
    p = sub.add_parser("build"); p.add_argument("slug")
    p.add_argument("--format", choices=[*FORMATS, "all"], default="all")
    p = sub.add_parser("render"); p.add_argument("slug")
    p.add_argument("--format", choices=[*FORMATS, "all"], default="all")
    p.add_argument("--quality", choices=["draft", "looks", "delivery"], default="delivery")
    p.add_argument("--no-commit", action="store_true",
                   help="do not commit+push the MP4s in the private repo (iterating)")
    p = sub.add_parser("notify"); p.add_argument("slug")
    p = sub.add_parser("status"); p.add_argument("slug")
    a = ap.parse_args(argv)

    if not os.path.isdir(pack_root(a.slug)):
        print(f"✗ no pack at workspace/social/articles/{a.slug}", file=sys.stderr)
        return 2

    if a.cmd == "prompt":
        text, err = build_prompt(a.slug)
        if err:
            print(f"✗ {err}", file=sys.stderr)
            return 1
        if a.write:
            dest = os.path.join(pack_root(a.slug), "_video-prompt.md")
            open(dest, "w", encoding="utf-8").write(text)
            os.makedirs(video_dir(a.slug), exist_ok=True)
            print(f"wrote {os.path.relpath(dest, PROJ)} ({len(text)} chars, "
                  f"{len(final_posts(a.slug))} posts); the drafter saves "
                  f"{os.path.relpath(spec_path(a.slug), PROJ)}")
        else:
            print(text)
        return 0

    if a.cmd == "lint":
        res = lint(a.slug)
        if a.json:
            print(json.dumps(res, indent=2, ensure_ascii=False))
        else:
            print(f"{res.get('video', a.slug)}: {res['verdict']}")
            for h in res["hard_fails"]:
                print(f"  ✗ {h['check']}: {h['detail']}")
            for w in res["warnings"]:
                print(f"  ⚠ {w['check']}: {w['detail']}")
        return 1 if res["hard_fails"] else 0

    if a.cmd == "build":
        spec, err = load_spec(a.slug)
        if err:
            print(f"✗ {err}", file=sys.stderr)
            return 1
        for fmt in (FORMATS if a.format == "all" else [a.format]):
            d, T = build(a.slug, fmt, spec)
            print(f"{fmt}: {d}/index.html ({T['total']} s)")
        return 0

    if a.cmd == "render":
        fmts = list(FORMATS) if a.format == "all" else [a.format]
        rep, rc = render(a.slug, fmts, a.quality, commit=not a.no_commit)
        print(json.dumps(rep, indent=2, ensure_ascii=False))
        return rc

    if a.cmd == "notify":
        return notify(a.slug)

    if a.cmd == "status":
        print(json.dumps(summary(a.slug), indent=2, ensure_ascii=False))
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
