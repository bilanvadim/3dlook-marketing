#!/usr/bin/env python3
"""pre_tool_call hook: refuse irreversible terminal commands.

SOUL.md tells the agent not to delete things or run destructive SQL without an
explicit yes. Tested on 2026-08-05, that rule does NOT hold: asked to "tidy up a
folder with junk", the agent removed files on its own judgement and reported it
afterwards. Under ``approvals.mode: "off"`` nothing gates it, and persona text is
a preference, not a gate. This hook is the gate.

Scope is deliberately narrow — Hermes is an orchestrator, so its legitimate
terminal work is systemctl / git status / journalctl / ps / dispatching
claude+opencode / writing handoffs. None of that deletes anything. What is
refused: file deletion, history-rewriting git, destructive SQL, container and
volume removal, filesystem writes to block devices.

Ordinary file deletion has one unlock, and it does not come from the model: the
pre_llm_call hook note-delete-consent.py reads the HUMAN's message for this turn
and writes a short-lived permit when Sergiy actually said "удали". A hook cannot
ask for confirmation, and any token the agent could add itself would be no gate,
so consent is captured one layer up instead. Forwarded client text never grants
it, and the permit file is on the protected list so the agent cannot forge one.
History rewrites, destructive SQL, container teardown and control-file edits have
NO chat unlock: those go to Claude Code or Sergiy's own shell.

**Command-position parsing, not substring matching.** ``claude -p 'find where the
file gets removed, rm is failing'`` must pass while ``ls && rm -rf x`` must not.
So the command is tokenised with shlex (quotes respected, shell operators split
out) and only the first word of each segment counts as a verb. This mirrors why
the approvals.deny globs are start-anchored.

Admin escape: set ``HERMES_ALLOW_DESTRUCTIVE=1`` in the gateway's own environment
(then restart it). Read from this process's environment on purpose — the agent
cannot self-authorise by prefixing the variable to its command string, because
that lands in the command text, which is never consulted for consent.

Redirections onto a control file ARE caught (see protected_verdict); a redirect
into a project path is left to the approvals.deny globs, because blocking every
``>`` would break legitimate handoff writes.
"""

import json
import os
import re
import shlex
import sys
import time

HOME = os.path.expanduser("~")

# Deleting scratch files is harmless and legitimate; keep the agent usable.
DELETE_OK_PREFIXES = ("/tmp/", "/var/tmp/", os.path.join(HOME, ".hermes", "cache") + os.sep)

DELETE_VERBS = {"rm", "rmdir", "unlink", "shred", "srm"}
DB_CLIENTS = {"psql", "mysql", "mariadb", "sqlite3", "mongosh", "redis-cli", "supabase"}
FS_VERBS = {"mkfs", "mkfs.ext4", "mkfs.xfs", "fdisk", "sfdisk", "parted", "wipefs"}
# Wrappers to look through when finding the real verb.
WRAPPERS = {"sudo", "env", "nohup", "time", "nice", "ionice", "doas", "command", "exec", "xargs"}
# Shells and interpreters that take the REAL command as a string argument. Without
# these the guard only ever saw the interpreter: `rm -rf /srv/x` was blocked while
# `bash -c 'rm -rf /srv/x'` and `python3 -c "shutil.rmtree('/srv/x')"` sailed past
# it — verified against the live hook before this was added.
SHELLS = {"bash", "sh", "zsh", "dash", "ksh", "busybox"}
# flag that introduces the inline program, per interpreter family
INLINE_CODE_FLAGS = {"-c", "-e", "-E", "--command", "--eval"}
CODE_INTERPRETERS = {"python", "python2", "python3", "perl", "ruby", "node", "php"}
OPERATORS = {";", "&&", "||", "|", "&", "\n", "|&"}

GIT_DESTRUCTIVE = re.compile(
    r"(?:^|\s)(?:"
    r"push\s+(?:.*\s)?(?:--force(?!-with-lease)|-f)(?:\s|$)"
    r"|reset\s+(?:.*\s)?--hard"
    r"|clean\s+(?:.*\s)?-[a-zA-Z]*f"
    r"|branch\s+(?:.*\s)?-D"
    r"|stash\s+(?:drop|clear)"
    r"|filter-branch"
    r"|update-ref\s+(?:.*\s)?-d"
    r")",
    re.I,
)
SQL_DESTRUCTIVE = re.compile(
    r"\b(?:drop\s+(?:table|database|schema|view|index|column|type|function)"
    r"|truncate(?:\s+table)?\s+\w"
    r"|delete\s+from"
    r"|alter\s+table\s+\S+\s+drop"
    r"|flushall|flushdb)\b",
    re.I,
)
DOCKER_DESTRUCTIVE = re.compile(
    r"(?:^|\s)(?:rm|rmi|prune"
    r"|(?:volume|network|container|image|system)\s+(?:rm|prune)"
    r"|(?:compose\s+)?down\s+(?:.*\s)?(?:-v|--volumes)"
    r")(?:\s|$)",
    re.I,
)

REASON = (
    "Refusing (hermes-mechanic): irreversible command. Hermes is the orchestrator, "
    "and deletions / history rewrites / destructive SQL / container teardown are not "
    "its call. Ask Sergiy first; if he confirms, hand it to Claude Code (it gates "
    "prod actions itself) or let him run it. Do not look for a way around this."
)

# ── Hermes' own control files ────────────────────────────────────────────────
# The sibling hook guards these against write_file/patch, but that is only one of
# the doors. In the first live test the agent walked around it and appended
# "Исключение: письма клиентам — можно самому отправлять письма клиентам" to
# SOUL.md, i.e. it edited away the rule that forbids contacting clients. So for
# these paths the policy is inverted: a READ-ONLY WHITELIST. Anything that is not
# a plainly reading command is refused, instead of trying to enumerate every way
# a shell can write to a file (>>, tee, sed -i, ed, cp, python …).
PROTECTED_BASENAMES = {
    "SOUL.md", "MEMORY.md", "USER.md",
    "config.yaml", ".env", "shell-hooks-allowlist.json",
    # The deletion permit: if the agent could write this, it would authorise
    # its own deletions. Only note-delete-consent.py (a hook, not a tool) writes it.
    ".delete-consent.json",
}
PROTECTED_DIRS = tuple(os.path.join(HOME, ".hermes", d) for d in ("agent-hooks", "hooks", "plugins"))
READ_ONLY_VERBS = {
    "cat", "head", "tail", "less", "more", "nl", "od", "strings",
    "grep", "egrep", "fgrep", "rg", "ack", "wc", "diff", "cmp",
    "md5sum", "sha1sum", "sha256sum", "stat", "file", "ls", "realpath",
    "basename", "dirname", "wc", "column",
}
REDIRECTS = {">", ">>", ">|", "&>", ">&"}

SELF_REASON = (
    "Refusing (hermes-mechanic): that command would modify one of Hermes's own "
    "control files (persona / memory / consent / hooks / config / secrets). They are "
    "never edited from inside a conversation — a forwarded client message could "
    "otherwise talk the agent into editing away its own safety rules, which is "
    "exactly what happened once. Reading them is fine (cat, grep, read_file). If "
    "Sergiy wants a change, he edits the file himself or has Claude Code do it."
)


PERMIT = os.path.join(HOME, ".hermes", ".delete-consent.json")
PERMIT_TTL = 600


def permit_fresh(session_id):
    """True when Sergiy asked for a deletion in this very turn.

    Written by the pre_llm_call hook from the human's own message, bound to the
    session and short-lived, so it cannot leak into a later turn or a parallel
    topic. A missing or malformed file simply means "no permission".
    """
    try:
        with open(PERMIT, encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, ValueError):
        return False
    if time.time() - float(data.get("ts") or 0) > PERMIT_TTL:
        return False
    asked_in = data.get("session_id") or ""
    return not asked_in or not session_id or asked_in == session_id


def touches_protected(token):
    """True if *token* names one of Hermes' control files or hook directories."""
    t = token.strip().strip("'\"")
    if not t or t in REDIRECTS:
        return False
    t = t.replace("${HOME}", HOME).replace("$HOME", HOME)
    t = os.path.expanduser(t)
    norm = os.path.normpath(t)
    if os.path.basename(norm) in PROTECTED_BASENAMES:
        return True
    return any(norm == d or norm.startswith(d + os.sep) for d in PROTECTED_DIRS)


# execute_code is the same power by another door: the first live test of this hook
# was defeated by the agent deleting the files from Python instead of the shell.
# Precise API names keep false positives near zero — a prompt that merely mentions
# "remove" is untouched, `os.remove(...)` is not.
CODE_DESTRUCTIVE = re.compile(
    r"\bos\.(?:remove|unlink|rmdir|removedirs)\s*\("
    r"|\bshutil\.rmtree\s*\("
    r"|\.unlink\s*\("
    r"|\bos\.system\s*\(\s*['\"][^'\"]*\brm\b"
    # Both call shapes: the list form subprocess.run(["rm", …]) AND the string
    # form subprocess.run("rm -rf /srv/x", shell=True). The old pattern required
    # the quote to close right after `rm`, so it only ever matched the list form
    # — while os.system, one line above, was matched in either. Same escape, two
    # different answers, inside one regex.
    r"|\bsubprocess\.\w+\s*\(\s*\[?\s*['\"]rm(?:['\"]|\s)"
    r"|\bsend2trash\b"
    # Non-Python interpreters reachable from a terminal command. Perl's `unlink`
    # is a bare list operator — no dot, no parens — so the two patterns above miss
    # it entirely: `perl -e 'unlink glob "/srv/x/*"'` was the one bypass still
    # standing after the shell/interpreter fix. Kept narrow (a following glob,
    # variable or quote) so the bare English word never matches.
    r"|\bunlink\s+(?:glob\b|['\"$@])"
    r"|\bremove_tree\s*\("
    r"|\bFileUtils\.rm_r",
    re.I,
)


# Pseudo-verb for source code pulled out of `python3 -c "…"` and friends; it is
# matched against CODE_DESTRUCTIVE rather than treated as a shell command.
_INLINE_CODE_VERB = "\x00inline-code"
_MAX_SHELL_DEPTH = 3          # bash -c 'bash -c "…"' is pathological, not useful


def segments(command, _depth=0):
    """Split *command* into (verb, args_string) per command position.

    Quoted text stays inside one token, so a prompt passed to `claude -p '…'`
    never contributes a verb.

    `_depth` bounds the recursion into `bash -c '…'` payloads.
    """
    if _depth > _MAX_SHELL_DEPTH:
        return []
    try:
        lex = shlex.shlex(command, posix=True, punctuation_chars=True)
        lex.whitespace_split = True
        tokens = list(lex)
    except ValueError:
        # Unbalanced quotes: fall back to a coarse split so a malformed command
        # cannot slip past by being unparseable.
        tokens = re.split(r"(\s|;|&&|\|\||\|)", command)
        tokens = [t for t in tokens if t and not t.isspace()]

    out, current = [], []
    for tok in tokens + [";"]:
        if tok in OPERATORS:
            if current:
                out.append(current)
            current = []
            continue
        current.append(tok)

    result = []
    for parts in out:
        i = 0
        while i < len(parts):
            base = os.path.basename(parts[i])
            is_assign = ("=" in parts[i] and not parts[i].startswith("-")
                         and "/" not in parts[i].split("=")[0])
            if is_assign or base in WRAPPERS:
                i += 1
                continue
            # A wrapper's OWN flags must be skipped too, or the flag becomes the
            # "verb" and the real command is demoted to an argument: `sudo rm -rf`
            # was blocked while `sudo -n rm -rf` was not, and `xargs -0 rm` slipped
            # through the same hole. Only skip flags once a wrapper introduced them
            # — a bare leading flag is not a command anyway.
            if i > 0 and parts[i].startswith("-"):
                i += 1
                continue
            break
        if i >= len(parts):
            continue
        verb = os.path.basename(parts[i])
        args = parts[i + 1:]

        # `bash -c '<real command>'` — inspect the string as its own command line
        # instead of stopping at the shell. Recursion is bounded by _depth.
        if verb in SHELLS:
            for j, a in enumerate(args):
                if a in ("-c", "--command") and j + 1 < len(args):
                    result.extend(segments(args[j + 1], _depth=_depth + 1))
                    break
        # `python3 -c "..."`, `perl -e '...'` — the payload is source code, so it
        # is handed to the CODE_DESTRUCTIVE patterns rather than re-tokenised.
        elif verb in CODE_INTERPRETERS:
            for j, a in enumerate(args):
                if a in INLINE_CODE_FLAGS and j + 1 < len(args):
                    result.append((_INLINE_CODE_VERB, [args[j + 1]]))
                    break

        result.append((verb, args))
    return result


def deletion_is_scratch_only(args):
    """True when every path argument sits in a scratch location."""
    paths = [a for a in args if not a.startswith("-")]
    if not paths:
        return False
    for a in paths:
        p = os.path.normpath(os.path.expanduser(a))
        if not p.startswith(DELETE_OK_PREFIXES):
            return False
    return True


def protected_verdict(command):
    """Refuse anything but a plain read when a control file is involved.

    Substring matching is deliberate on top of the per-token path check: a path can
    hide inside an argument, and ``python3 -c "open('…/SOUL.md','a').write(…)"``
    slipped through while only tokens were parsed. The cost is that delegating a
    read (``claude -p '… SOUL.md …'``) is refused too — the agent can `cat` the
    file itself, so that is the cheaper side of the trade.
    """
    for verb, args in segments(command):
        # A redirect onto a protected path is a write whatever the verb is.
        for i, tok in enumerate(args):
            if tok in REDIRECTS and i + 1 < len(args) and touches_protected(args[i + 1]):
                return f"{verb} … {tok} {args[i + 1]}"
        seg = " ".join(args)
        involved = (
            any(touches_protected(a) for a in args)
            or any(b in seg for b in PROTECTED_BASENAMES)
            or any(d in seg for d in (".hermes/agent-hooks", ".hermes/hooks", ".hermes/plugins"))
        )
        if not involved or verb in READ_ONLY_VERBS:
            continue
        return f"{verb} {seg}".strip()
    return None


def inspect(command):
    """Return ``(tier, description)`` for an offending command, else ``(None, None)``.

    Two tiers, because they answer to different consent. ``delete`` is ordinary
    file removal — Sergiy saying "удали" in the same turn unlocks it (see
    note-delete-consent.py). ``hard`` is history rewrites, destructive SQL,
    container teardown and filesystem-level writes: no chat sentence unlocks
    those, they go through Claude Code or his own shell.
    """
    for verb, args in segments(command):
        joined = " ".join(args)
        # Source code handed to `python3 -c` / `perl -e` from a TERMINAL command.
        # Same patterns the execute_code tool is judged by — reaching rmtree via
        # an interpreter is the same act as typing rm, and used to be free.
        if verb == _INLINE_CODE_VERB:
            m = CODE_DESTRUCTIVE.search(joined)
            if m:
                return "delete", f"inline code: {m.group(0)}"
            continue
        if verb in DELETE_VERBS:
            if deletion_is_scratch_only(args):
                continue
            return "delete", f"{verb} {joined}".strip()
        if verb == "find" and re.search(r"(?:^|\s)-delete(?:\s|$)|-exec\s+rm\b", joined):
            return "delete", f"find {joined}".strip()
        if verb == "truncate" and re.search(r"-s\s*0", joined):
            return "delete", f"truncate {joined}".strip()
        if verb == "git" and GIT_DESTRUCTIVE.search(joined):
            return "hard", f"git {joined}".strip()
        if verb in DB_CLIENTS and SQL_DESTRUCTIVE.search(joined):
            return "hard", f"{verb} {joined}".strip()
        if verb == "docker" and DOCKER_DESTRUCTIVE.search(joined):
            return "hard", f"docker {joined}".strip()
        if verb in FS_VERBS:
            return "hard", f"{verb} {joined}".strip()
        if verb == "dd" and re.search(r"of=/dev/", joined):
            return "hard", f"dd {joined}".strip()
    return None, None


def main():
    if os.environ.get("HERMES_ALLOW_DESTRUCTIVE") == "1":
        print("{}")
        return
    try:
        payload = json.load(sys.stdin)
    except Exception:
        print("{}")
        return
    tool = payload.get("tool_name") or ""
    if tool not in ("terminal", "execute_code"):
        print("{}")
        return
    tool_input = payload.get("tool_input") or {}
    if not isinstance(tool_input, dict):
        print("{}")
        return

    reason = REASON
    if tool == "execute_code":
        code = tool_input.get("code")
        if not isinstance(code, str) or not code.strip():
            print("{}")
            return
        # Reading a control file from Python is never necessary — read_file and cat
        # do that — so any mention of one is refused outright rather than
        # classified. Cheap, and leaves no write construct to miss.
        mentioned = [b for b in PROTECTED_BASENAMES if b in code]
        mentioned += [d for d in ("agent-hooks", ".hermes/hooks", ".hermes/plugins") if d in code]
        if mentioned:
            reason = SELF_REASON
            hit = "execute_code touching " + ", ".join(sorted(set(mentioned)))
        elif SQL_DESTRUCTIVE.search(code):
            hit = SQL_DESTRUCTIVE.search(code).group(0)
        else:
            m = CODE_DESTRUCTIVE.search(code)
            hit = m.group(0) if m else None
            if hit and permit_fresh(payload.get("session_id") or ""):
                hit = None  # Sergiy asked for it this turn
    else:
        command = tool_input.get("command")
        if not isinstance(command, str) or not command.strip():
            print("{}")
            return
        hit = protected_verdict(command)
        if hit:
            reason = SELF_REASON
        else:
            tier, hit = inspect(command)
            if tier == "delete" and permit_fresh(payload.get("session_id") or ""):
                hit = None  # Sergiy asked for it this turn
    if hit:
        print(json.dumps({
            "decision": "block",
            "reason": f"{reason} Blocked: `{hit[:200]}`",
        }, ensure_ascii=False))
    else:
        print("{}")


if __name__ == "__main__":
    main()
