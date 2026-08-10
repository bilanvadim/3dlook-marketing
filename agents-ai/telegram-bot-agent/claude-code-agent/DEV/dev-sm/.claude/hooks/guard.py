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
# (safety-guard ruleset, adapted from ECC pattern — see security-sm; kept conservative)
BLOCK = [
    (r"\brm\s+-[a-z]*r[a-z]*f?\s+(-[a-z]+\s+)*(/\s*$|/\s|~|\$HOME|\.git|\*)", "recursive delete of root/home/.git/glob"),
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
]
# Confirm (ask the human) — prod-affecting / risky-but-sometimes-legit
ASK = [
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
