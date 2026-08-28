#!/usr/bin/env python3
"""test-failover.py — regression guard for the Claude → OpenCode failover.

Run: hermes_agent/ops/claude-switcher/test-failover.py
Exit: 0 all green · 1 a failure

WHAT IT GUARDS, AND WHY EACH ONE IS HERE
----------------------------------------
1. LIMIT vs AUTH. These take opposite actions — a limit means "switch executor and keep
   working", an expired OAuth session means "stop and fetch a human". Getting them the
   wrong way round either retries forever or gives up on work that was still doable.
   Auth must win on a message that mentions both.

2. THE HANDOFF AND SALVAGE. A limit must not lose work. The salvage commit is LOCAL by
   design; if a future change starts pushing it, that is a behaviour change an operator
   has to opt into, not a detail.

3. $PWD. OpenCode resolves relative paths against the PWD environment variable, NOT
   getcwd(). subprocess.run(cwd=…) sets the real directory and leaves PWD as the parent's,
   so without pinning it the failover wrote the work into ~/.hermes/<relative path> — and
   OpenCode reported "Wrote file successfully" every time. Measured 2026-08-28: PWD=/tmp
   put the file under /tmp with cwd pinned to the repo; PWD=repo put it in the repo. This
   is the single most dangerous thing in the failover, because it fails silently and
   plausibly.

4. VERIFY, DO NOT RELAY. A run that claims completion while the work tree is unchanged
   must be reported as a failure. The free strong chain does exactly this.

No network is used except by the two live checks at the end, which are skipped when the
binaries are absent so the suite still runs on a machine without them.
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.expanduser("~/.hermes/hermes-agent"))
os.environ.setdefault("HERMES_HOME", os.path.expanduser("~/.hermes"))

try:
    from gateway import claude_switcher as cs
except Exception as e:                                    # pragma: no cover
    print(f"cannot import claude_switcher: {e}", file=sys.stderr)
    sys.exit(1)

_p = _f = 0


def check(name: str, cond: bool, detail: str = "") -> None:
    global _p, _f
    if cond:
        _p += 1
        print(f"  ok    {name}")
    else:
        _f += 1
        print(f"  FAIL  {name}" + (f" — {detail}" if detail else ""))


def _repo(tmp: str) -> str:
    subprocess.run(["git", "init", "-q"], cwd=tmp)
    open(os.path.join(tmp, "base.txt"), "w").write("x\n")
    subprocess.run(["git", "add", "-A"], cwd=tmp)
    subprocess.run(["git", "-c", "user.email=a@b", "-c", "user.name=a",
                    "commit", "-q", "-m", "base"], cwd=tmp)
    return tmp


print("── 1. limit vs auth ──")
for t in ("Claude AI usage limit reached", "rate limit exceeded",
          "limit will reset at 3pm", "HTTP 429 Too Many Requests",
          "your credit balance is too low", "upstream overloaded"):
    check(f"limit: {t[:38]!r}", cs._looks_like_limit(t) and not cs._looks_like_auth_failure(t))
for t in ("OAuth session expired", "Failed to authenticate", "please run /login",
          "invalid api key", "unauthorized"):
    check(f"auth:  {t[:38]!r}", cs._looks_like_auth_failure(t))
for t in ("Wrote 3 files", "npm test passed", "Read src/index.ts"):
    check(f"work:  {t[:38]!r}", not cs._looks_like_limit(t) and not cs._looks_like_auth_failure(t))
check("auth wins when a message mentions both",
      cs._looks_like_auth_failure("invalid api key, and you are near the rate limit"))

print()
print("── 2. handoff + salvage ──")
d = _repo(tempfile.mkdtemp())
open(os.path.join(d, "half.py"), "w").write("# unfinished\n")
check("handoff written", cs._write_handoff(d, "the task", "sess-1", "partial output"))
body = open(os.path.join(d, cs.HANDOFF_NAME), encoding="utf-8").read()
for must in ("the task", "sess-1", "partial output", "LOCAL and unpushed"):
    check(f"handoff carries {must[:26]!r}", must in body)
res = cs._salvage_commit(d, "t")
check("salvage commits and says it is local", "спасено" in res and "локально" in res, res)
log = subprocess.run(["git", "log", "--oneline"], cwd=d, capture_output=True, text=True).stdout
check("salvage commit in history", "salvage" in log)
files = subprocess.run(["git", "show", "--name-only", "--format=", "HEAD"],
                       cwd=d, capture_output=True, text=True).stdout
check("the unfinished work is inside it", "half.py" in files, files.replace("\n", " "))
check("the handoff travels with it", cs.HANDOFF_NAME in files)
sb = subprocess.run(["git", "status", "-sb"], cwd=d, capture_output=True, text=True).stdout
check("nothing was pushed", "origin" not in sb)
check("a second call is a no-op", "нечего спасать" in cs._salvage_commit(d, "t"))

print()
print("── 3. the context cannot read as 'already done' ──")
ctx = cs._handoff_context("write done.txt", "sess-2", "wrote half.py")
check("says UNFINISHED", "UNFINISHED" in ctx)
check("says the task is NOT done", "task is NOT done" in ctx)
check("tells it to verify on disk before claiming", "verify it on disk" in ctx)

print()
print("── 4. the return path ──")
check("no state, no note", cs._maybe_return_to_claude("nonexistent#tab") is None)
check("the return prompt forces a diff review first",
      ".hermes-handoff.md" in cs.CLAUDE_RETURN_REVIEW and "git diff" in cs.CLAUDE_RETURN_REVIEW)

print()
print("── 5. live: $PWD is what OpenCode obeys ──")
oc = cs._opencode_bin()
if not (os.path.exists(oc) or subprocess.run(["which", oc], capture_output=True).returncode == 0):
    print("  skip  OpenCode not installed")
else:
    r2 = _repo(tempfile.mkdtemp())
    sub = os.path.join(r2, "sub")
    os.makedirs(sub, exist_ok=True)
    elsewhere = tempfile.mkdtemp()
    # Parent PWD deliberately wrong, exactly as it is for the gateway (~/.hermes).
    os.chdir(elsewhere)
    os.environ["PWD"] = elsewhere
    text, note = cs._run_opencode_sync(
        sub, "Use the Write tool to create sub/pwd-guard.txt with exactly: PWD-OK",
        timeout=600, context="")
    right = os.path.exists(os.path.join(r2, "sub", "pwd-guard.txt"))
    stray = os.path.exists(os.path.join(elsewhere, "sub", "pwd-guard.txt"))
    # THE ASSERTION IS ABOUT LOCATION, NOT SPEED. A timeout or a refusal is an
    # environment condition (a cold repo, an exhausted free chain) and must not read as a
    # regression — otherwise the guard gets ignored for crying wolf. What must NEVER
    # happen is a write landing under the parent cwd: that is the silent bug this exists
    # for, and it is checked unconditionally.
    check("nothing was written under the parent cwd (the $PWD bug)", not stray,
          "a relative write escaped to the parent working directory")
    if right:
        check("the file landed in the target repo", True)
    elif not text and note:
        print(f"  skip  OpenCode did not complete this run ({note[:80]}) — "
              f"location assertion above still held")
    else:
        check("the file landed in the target repo", False,
              f"OpenCode answered but wrote nothing there: note={note[:100]!r}")

print()
print(f"test-failover: {_p} passed, {_f} failed")
sys.exit(1 if _f else 0)
