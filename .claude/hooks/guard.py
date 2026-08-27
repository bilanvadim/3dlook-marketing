#!/usr/bin/env python3
"""Hermes safety guard (PreToolUse hook for Bash).
Last-line defense against destructive / secret-leaking commands that pattern-allowlists may miss.
Reads the tool call JSON from stdin. Exit 0 = allow; exit 2 = block (stderr shown to model);
JSON decision on stdout can also 'ask'. Conservative: only blocks clearly dangerous patterns.
"""
import json, re, sys

try:
    payload = json.load(sys.stdin)
except Exception:
    sys.exit(0)  # never break the session on parser issues

cmd = (payload.get("tool_input") or {}).get("command", "")

# Hard blocks: irreversible / exfiltration / pipe-to-shell
# (safety-guard ruleset, adapted from ECC pattern — see security_sm; kept conservative)
BLOCK = [
    (r"\brm\s+-[a-z]*r[a-z]*f?\s+(-[a-z]+\s+)*(/\s*$|/\s|~|\$HOME|\.git|\*)", "recursive delete of root/home/.git/glob"),
    # The pattern above only fires on "/", "~", ".git" or a bare glob, so "rm -rf
    # /home/vadim_prod/3dlook-marketing" used to sail straight through. Any recursive
    # delete of an absolute path, or of anything above the project, is irreversible here.
    (r"\brm\s+-[a-z]*r[a-z]*f?\s+(-[a-z]+\s+)*(/|\.\./)", "recursive delete of an absolute path or above the project"),
    (r"\bgit\s+push\s+(--force\b|--force-with-lease\b|-f\b)", "force push (history rewrite)"),
    (r"\b(curl|wget)\b[^|]*\|\s*(ba|z|k|c)?sh\b", "pipe remote content to shell (supply-chain risk)"),
    (r"\beval\s+[\"']?\$\(\s*(curl|wget)\b", "eval of remote content (supply-chain risk)"),
    (r"<\(\s*(curl|wget)\b", "process-substitution of remote content"),
    (r"\b(DROP\s+(TABLE|DATABASE|SCHEMA)|TRUNCATE)\b", "destructive SQL via CLI — use a reviewed migration"),
    (r":\s*\(\s*\)\s*\{\s*:\|\:&\s*\}\s*;\s*:", "fork bomb"),
    (r"\bchmod\s+(-R\s+|-[a-zA-Z]+\s+)*(0)?777\b", "world-writable chmod (777)"),
    (r"\bmkfs(\.\w+)?\b", "format filesystem"),
    (r"\bdd\b[^\n]*\bof=/dev/", "raw write to block device (dd of=/dev/…)"),
    (r">\s*/dev/(sd|nvme|hd|vd|mmcblk)\w*", "overwrite block device"),
    (r"\b(cat|less|more|head|tail|nl|xxd|od|strings|base64|cp|scp|rsync)\b[^\n]*(id_rsa|id_ed25519|\.ssh/|\.aws/credentials|\.credentials\.json|\.pem\b|\.env(?!\.(?:example|sample|template|dist))(?![a-zA-Z]))",
     "reading/copying secret material — reference var names instead"),
    # An autonomous run must never be able to answer its OWN human gate. The
    # conductor loads settingSources ['project'], so it runs under this hook, and
    # `Bash(sqlite3*)` is on the allow list — which meant a job that hit an ASK
    # escalation could simply UPDATE its own ho_escalations row to 'approved' and
    # walk through. Blocked in BOTH verb orders, because a heredoc can put the
    # table name on a different line from the verb.
    #
    # Reads stay allowed on purpose: a job checking its own status is legitimate,
    # and the whole conductor↔Telegram protocol is built on polling.
    #
    # Not affected, verified 2026-08-27: the Telegram approve/deny path
    # (claude_switcher.py:4670/4785) and mvb-run.py both use the PYTHON sqlite3
    # module, not the CLI, so this hook never sees them. conductor-monitor.sh only
    # reads. `insert into ho_jobs` is deliberately still permitted — enqueueing is
    # not deciding.
    (r"\b(update|replace\s+into|delete\s+from|drop\s+table)\s+(ho_escalations|ho_questions|ho_jobs|ho_runs|ho_steps)\b",
     "writing the orchestrator queue directly — an autonomous job must not decide its own escalation or mark its own job done"),
    (r"\b(ho_escalations|ho_questions)\b[\s\S]{0,200}?\b(set\s+status|update|delete|drop)\b",
     "writing an escalation/question row directly — the human gate is answered in Telegram, not in SQL"),
    (r"\bsqlite3\b[^\n]*\bho\.db\b[\s\S]{0,400}?\b(update|delete\s+from|drop|replace\s+into|attach\b)",
     "direct write to ho.db via the sqlite3 CLI — use mvb-run.py to enqueue, Telegram to decide"),
]
# Confirm (ask the human) — prod-affecting / risky-but-sometimes-legit
ASK = [
# NO blanket "rm -r" entry here, deliberately: in a HEADLESS run an ASK is effectively a DENY, so
# gating every recursive delete would break routine dependency cleanup (rm -rf node_modules).
# A delete that LEAVES the work_dir is a BLOCK above; anything inside it is gated by the
# conductor's own ASK_PATTERNS over Telegram, where a human can actually answer.
    # Any other recursive delete (a relative path inside the project) — legitimate
    # sometimes, but a headless run must not decide this on its own.
    (r"\b(vercel\s+--prod|vercel\s+deploy|wrangler\s+(deploy|publish))\b", "production deploy"),
    (r"\bterraform\s+(apply|destroy)\b", "infrastructure change"),
    (r"\bsupabase\s+db\s+push\b", "applying migrations to a live database"),
    (r"\bgh\s+pr\s+merge\b", "merging a pull request"),
    (r"\bgit\s+clean\s+-[a-z]*f[a-z]*\b", "git clean -f (deletes untracked/ignored files)"),
    (r"\bgit\s+reset\s+--hard\b", "hard reset (discards uncommitted work)"),
    (r"\bdocker\s+(system\s+prune|volume\s+rm|volume\s+prune)\b", "removing Docker volumes/data"),
]

for pat, why in BLOCK:
    if re.search(pat, cmd, re.IGNORECASE):
        print(f"BLOCKED by Hermes guard: {why}. If intentional, run it yourself outside the agent.", file=sys.stderr)
        sys.exit(2)

for pat, why in ASK:
    if re.search(pat, cmd, re.IGNORECASE):
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "ask",
                "permissionDecisionReason": f"Hermes: this is a {why}. Confirm before proceeding."
            }
        }))
        sys.exit(0)

sys.exit(0)
