#!/usr/bin/env python3
"""capture-live.py — snapshot the LIVE article page into `published-live-<date>.md`.

WHY THIS EXISTS
---------------
The article that goes live on 3dlook.ai/content-hub/ is NOT the draft this pipeline
shipped: the editorial side rewrites prose, swaps citations, cuts proof points and adds
its own substance (confirmed on glp-1-market-hub 2026-08-28 and
remote-body-measurement 2026-09-04, end to end). `social_pack.py resolve_source` ranks
`published-live-*` above `publish-package.md` on purpose, so capturing the live page is
the single step that points all nine post drafters at the text of record. Until
2026-09-20 that capture was assembled by hand each time (WebFetch refuses our own pages
as "copyrighted", so it is curl plus an HTML-to-markdown pass); this script is that
pass, mechanised.

WHAT IT KEEPS AND DROPS — same conventions as the hand-made captures:
  keeps  h1-h4, paragraphs, lists (nested), tables, links, bold/italic
  drops  images and figures, the mid-article eBook CTA (div.image-content), author
         bio and related posts (everything from the end marker on), script/style/nav,
         empty anchor-only table rows, the TOC block before the h1

USAGE
    scripts/capture-live.py <url> <seo-article-dir> [--date YYYY-MM-DD] [--stdout]
    scripts/capture-live.py --html <file> <url> <seo-article-dir> [--stdout]

<seo-article-dir> is the article's working dir (absolute, or relative to the repo
root), e.g. workspace/seo/articles/bariatric-hub-refresh. The file is written there as
published-live-<date>.md with the frontmatter `resolve_source` expects
(status: published + published_url), and an existing file for the same date is only
overwritten with --force.
"""
from __future__ import annotations

import argparse
import html
import os
import re
import subprocess
import sys
from datetime import date
from html.parser import HTMLParser

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

# The article body runs from the <h1> to the first of these markers (author bio,
# related posts, footer). Theme-specific by necessity; extend the list, do not
# reorder it — the EARLIEST match wins.
END_MARKERS = ('class="default__author', 'class="d-posts', "<footer")

# Subtrees dropped entirely, by tag or by class fragment.
# figure/picture are NOT here: WordPress serves every table as
# <figure class="wp-block-table"><table>…</figure>, so skipping figure eats the
# tables. Their images still vanish — img and source are void tags in SKIP_TAGS.
SKIP_TAGS = {"script", "style", "svg", "form", "button", "nav", "aside",
             "img", "source", "iframe", "noscript"}
SKIP_CLASS_FRAGMENTS = ("image-content",)          # the eBook CTA wrapper

# Void elements never emit an end tag, so they must not touch skip_depth: one <img>
# or <source> inside a skipped <figure> would otherwise leave the parser skipping
# to the end of the document (that is exactly how draft one of this script lost
# everything after the first figure).
VOID = {"img", "br", "hr", "source", "input", "meta", "link", "wbr", "embed",
        "track", "area", "col", "base", "param"}


class MD(HTMLParser):
    """Linear HTML -> markdown for the sliced article body."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out: list[str] = []
        self.skip_depth = 0
        self.list_stack: list[str] = []            # "ul" | "ol"
        self.ol_counters: list[int] = []
        self.href: str | None = None
        self.link_text: list[str] = []
        # tables
        self.in_table = False
        self.rows: list[list[str]] = []
        self.cell: list[str] | None = None
        self.in_cell_div_break = False

    # -- helpers ----------------------------------------------------------
    def _emit(self, text: str):
        if self.href is not None:
            self.link_text.append(text)
        elif self.cell is not None:
            self.cell.append(text)
        else:
            self.out.append(text)

    def _para_break(self):
        if self.cell is None and self.href is None:
            self.out.append("\n\n")

    # -- parser events ----------------------------------------------------
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "")
        if self.skip_depth:
            if tag not in VOID:
                self.skip_depth += 1
            return
        if tag in SKIP_TAGS or any(f in cls for f in SKIP_CLASS_FRAGMENTS):
            if tag not in VOID:
                self.skip_depth = 1
            return
        if tag in ("h1", "h2", "h3", "h4"):
            self._para_break()
            self.out.append("#" * int(tag[1]) + " ")
        elif tag == "p":
            self._para_break()
        elif tag == "br":
            self._emit("\n")
        elif tag in ("ul", "ol"):
            if not self.in_table:
                self.list_stack.append(tag)
                self.ol_counters.append(0)
                if len(self.list_stack) == 1:
                    self._para_break()
        elif tag == "li" and self.list_stack and not self.in_table:
            depth = len(self.list_stack) - 1
            if self.list_stack[-1] == "ol":
                self.ol_counters[-1] += 1
                marker = f"{self.ol_counters[-1]}. "
            else:
                marker = "- "
            self.out.append("\n" + "  " * depth + marker)
        elif tag == "table":
            self.in_table = True
            self.rows = []
            self._para_break()
        elif tag == "tr" and self.in_table:
            self.rows.append([])
        elif tag in ("td", "th") and self.in_table:
            self.cell = []
        elif tag == "div" and self.cell is None and "default__des" in cls:
            # the theme's description block sits right after the h1 with no <p>
            self._para_break()
        elif tag == "div" and self.cell is not None:
            # theme sometimes stacks divs inside a cell; keep them readable
            if self.cell and "".join(self.cell).strip():
                self.cell.append(" · ")
        elif tag == "a":
            self.href = a.get("href", "")
            self.link_text = []
        elif tag in ("strong", "b"):
            self._emit("**")
        elif tag in ("em", "i"):
            self._emit("*")

    def handle_endtag(self, tag):
        if self.skip_depth:
            if tag not in VOID:
                self.skip_depth -= 1
            return
        if tag in ("ul", "ol") and self.list_stack and not self.in_table:
            self.list_stack.pop()
            self.ol_counters.pop()
            if not self.list_stack:
                self.out.append("\n")
        elif tag in ("td", "th") and self.cell is not None:
            self.rows[-1].append(" ".join("".join(self.cell).split()))
            self.cell = None
        elif tag == "table" and self.in_table:
            self.in_table = False
            rows = [r for r in self.rows if any(c.strip() for c in r)]
            if rows:
                width = max(len(r) for r in rows)
                rows = [r + [""] * (width - len(r)) for r in rows]
                lines = ["| " + " | ".join(r) + " |" for r in rows]
                lines.insert(1, "|" + "---|" * width)
                self.out.append("\n".join(lines) + "\n")
        elif tag == "a" and self.href is not None:
            text = "".join(self.link_text).strip()
            href, self.href = self.href, None
            if text:
                self._emit(f"[{text}]({href})")
        elif tag in ("strong", "b"):
            self._emit("**")
        elif tag in ("em", "i"):
            self._emit("*")

    def handle_data(self, data):
        if self.skip_depth:
            return
        if not data.strip():
            # keep single spaces between inline chunks, drop layout whitespace
            if data and self.out and not self.out[-1].endswith(("\n", " ")):
                self._emit(" ")
            return
        self._emit(re.sub(r"\s+", " ", data))


def meta(h: str, prop: str) -> str:
    m = re.search(rf'<meta property="{re.escape(prop)}" content="([^"]+)"', h)
    return m.group(1) if m else ""


def convert(page_html: str) -> tuple[str, dict]:
    i = page_html.find("<h1")
    if i < 0:
        sys.exit("⚠️ no <h1> on the page — not an article?")
    end = min((j for j in (page_html.find(m, i) for m in END_MARKERS) if j > 0),
              default=len(page_html))
    md = MD()
    md.feed(page_html[i:end])
    body = html.unescape("".join(md.out))
    body = re.sub(r"[ \t]+\n", "\n", body)
    body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"
    # bold/italic runs glued to the next word ("**Bold**text") stay as the theme
    # rendered them; only strip the nbsp the editor leaves at paragraph ends.
    body = body.replace(" ", " ")
    info = {
        "published": meta(page_html, "article:published_time"),
        "modified": meta(page_html, "article:modified_time"),
        "title": (re.search(r"<h1[^>]*>(.*?)</h1>", page_html[i:], re.S) or [None, ""])[1],
    }
    info["title"] = html.unescape(re.sub(r"<[^>]+>", "", info["title"])).strip()
    return body, info


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("article_dir")
    ap.add_argument("--html", help="already-downloaded page instead of fetching")
    ap.add_argument("--date", default=date.today().isoformat())
    ap.add_argument("--stdout", action="store_true")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()

    if a.html:
        page = open(a.html, encoding="utf-8", errors="replace").read()
    else:
        r = subprocess.run(["curl", "-s", "-A", UA, a.url],
                           capture_output=True, text=True, timeout=60)
        if r.returncode != 0 or len(r.stdout) < 10000:
            sys.exit(f"⚠️ curl failed or page too small ({len(r.stdout)} bytes)")
        page = r.stdout

    body, info = convert(page)
    url = a.url.rstrip("/") + "/"
    slug = url.rstrip("/").rsplit("/", 1)[-1]
    words = len(re.findall(r"\b[\w'-]+\b", body))
    fm = (f"---\n"
          f"slug: {slug}\n"
          f'title: "{info["title"]}"\n'
          f"status: published\n"
          f"published_url: {url}\n"
          f"article_published_time: {info['published']}\n"
          f"article_modified_time: {info['modified']}\n"
          f"captured_from_live: {a.date}\n"
          f'capture_method: "scripts/capture-live.py — curl of the live page, body '
          f'converted to markdown; images, eBook CTA and author bio dropped"\n'
          f"source_of_truth: live page\n"
          f"---\n\n")
    doc = fm + body
    if a.stdout:
        print(doc)
        return 0
    root = a.article_dir if os.path.isabs(a.article_dir) else os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), a.article_dir)
    if not os.path.isdir(root):
        sys.exit(f"⚠️ article dir not found: {root}")
    out = os.path.join(root, f"published-live-{a.date}.md")
    if os.path.exists(out) and not a.force:
        sys.exit(f"⚠️ {out} exists — --force to overwrite")
    open(out, "w", encoding="utf-8").write(doc)
    print(f"✓ {os.path.relpath(out)}  ({words} words, modified {info['modified']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
