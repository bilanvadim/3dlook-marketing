#!/usr/bin/env python3
"""Stop hook: a posts session may not end while its promised post.md is missing.

THE FAILURE THIS BLOCKS — seen twice on 2026-09-20:
  job #136 (fitxpress, linkedin-nick) and job #158 (bariatric, linkedin-katya) both
  ended their session with the words "waiting for the post-drafter to finish" — the
  session terminated, the subagent died with it, and ho_jobs recorded `done` over
  zero artifacts. The conductor's own "no done without an SDK result" gate
  (2026-07-28) does not catch this: an SDK result EXISTS (the model's farewell), the
  artifact doesn't. The artifact contract lives in this repo, so the gate does too.

HOW: on Stop, if this session was started by `/post-one-profile <slug> <profile>` or
`/post-batch <slug>` (read from the transcript's first user message), verify:
  1. the promised post.md file(s) exist — the #136/#158 failure;
  2. when the pack is COMPLETE, that manifest.json is no older than the newest
     post.md — job #160 (2026-09-20) wrote its posts, then ended with "I'll resume
     once the brand checks complete": children died, assembly never ran, manifest
     stayed stale. Posts existed, so check 1 passed; this check catches it.
Missing / stale → block the stop with a reason the model can act on. Any other
session — every non-posts job, every interactive session here — matches nothing and
exits 0 in microseconds.

LOOP GUARD: blocks at most twice per session (marker file keyed by session_id in
/tmp), so a genuinely stuck drafter cannot ping-pong the session forever; after two
blocks the stop is allowed and the missing profiles are simply still missing, which
`mvb-run.py posts <slug>` re-queues exactly (the 2026-09-20 filter).

Exit 0 = allow. Block = JSON {"decision":"block","reason":...} on stdout, exit 0.
"""
import json
import os
import re
import sys

PROJ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HEAD_LINES = 60          # the command invocation is in the first user message


def read_head(path: str) -> str:
    out = []
    with open(path, encoding="utf-8", errors="replace") as f:
        for i, line in enumerate(f):
            if i >= HEAD_LINES:
                break
            out.append(line)
    return "".join(out)


def main() -> int:
    try:
        h = json.load(sys.stdin)
    except Exception:
        return 0
    tp = h.get("transcript_path") or ""
    if not tp or not os.path.exists(tp):
        return 0
    head = read_head(tp)
    m = re.search(r"<command-name>/post-(one-profile|batch)</command-name>", head)
    if not m:
        return 0
    mode = m.group(1)
    ma = re.search(r"<command-args>([^<]*)", head)
    if not ma:
        return 0
    # transcript is JSONL, so a newline inside the prompt appears as literal \n;
    # the slug (and profile) are the first whitespace-ish tokens of the args
    args = re.split(r"\s+|\\+n", ma.group(1).strip())
    # tokens must look like slugs/profile ids; a stray backslash or tag fragment
    # must never become a "missing profile" that blocks forever
    args = [a.strip("\\") for a in args]
    args = [a for a in args if a and re.fullmatch(r"[A-Za-z0-9._-]+", a)]
    if not args:
        return 0
    slug = args[0]
    root = os.path.join(PROJ, "workspace", "social", "articles", slug)
    if not os.path.isdir(root):
        return 0                     # bad slug is the command's problem, not ours

    if mode == "one-profile":
        if len(args) < 2:
            return 0
        expected = [args[1]]
    else:
        # batch: every profile section the assignment file promised. The file is
        # written by `social_pack.py batch-prompt --write` in step 2; before it
        # exists the session hasn't promised anything file-checkable yet.
        bp = os.path.join(root, "_batch-prompt.md")
        if not os.path.exists(bp):
            return 0
        expected = re.findall(r"^===== PROFILE \d+ of \d+: `([^`]+)` =====",
                              open(bp, encoding="utf-8", errors="replace").read(),
                              re.M)
        if not expected:
            return 0

    missing = [p for p in expected
               if not os.path.exists(os.path.join(root, p, "post.md"))]

    reason = None
    if missing:
        reason = (
            f"post.md отсутствует для: {', '.join(missing)} "
            f"(workspace/social/articles/{slug}/<профиль>/post.md). Сессия шла к "
            "завершению без артефакта — это класс job'ов #136/#158, которые "
            "закрылись done со словами «жду драфтера». Дождись результата "
            "post-drafter (или перезапусти его), прогони "
            f"`python3 scripts/post-lint.py {slug} <профиль> --summary --gate`, "
            "и только когда файлы на диске — заканчивай по шагам команды."
        )
    else:
        # every promised post exists — is the ASSEMBLY done? Only meaningful when
        # the whole pack is complete (a non-last fan-out profile never assembles).
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location(
                "sp", os.path.join(PROJ, "scripts", "social_pack.py"))
            sp = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(sp)
            _all_done, all_missing = sp.pack_state(slug)
        except Exception:
            all_missing = ["?"]          # cannot tell — never block on a hook bug
        if not all_missing:
            newest = max((os.path.getmtime(os.path.join(root, d, "post.md"))
                          for d in os.listdir(root)
                          if os.path.isfile(os.path.join(root, d, "post.md"))),
                         default=0)
            man = os.path.join(root, "manifest.json")
            if not os.path.exists(man) or os.path.getmtime(man) + 5 < newest:
                reason = (
                    f"пак `{slug}` полный, но сборка не выполнена: manifest.json "
                    "старее новейшего post.md (или отсутствует). Это класс job'а "
                    "#160 — «I'll resume once the checks complete» и конец сессии. "
                    "Никакого «потом» нет: заверши шаги сейчас — "
                    f"`python3 scripts/social_pack.py manifest {slug} --write`, "
                    f"`digest {slug} --write`, `report {slug} --write` (и "
                    "brand-checker/QC по qc-plan, если ещё не сделаны)."
                )
    if reason is None:
        return 0

    marker = f"/tmp/posts-artifact-gate-{h.get('session_id', 'unknown')}"
    try:
        n = int(open(marker).read())
    except Exception:
        n = 0
    if n >= 2:
        return 0                     # loop guard: after two blocks, let it end
    try:
        open(marker, "w").write(str(n + 1))
    except Exception:
        pass
    print(json.dumps({"decision": "block", "reason": reason}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
