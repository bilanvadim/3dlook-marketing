#!/usr/bin/env python3
"""make-templates.py — regenerate the repo's *.example files FROM THE LIVE SYSTEM.

WHY A GENERATOR AND NOT HAND-EDITED TEMPLATES
---------------------------------------------
Hand-written templates rot, silently and in the worst possible direction. Measured in this
repo on 2026-08-28, before this script existed:

  hermes_agent/config.yaml.example      the OTHER account's live config, copied verbatim —
                                        no proxy wiring at all, and it froze the barrier
                                        pointing at /srv/vadim_prod, which is empty
  hermes_agent/.env.example             14 of the live 34 variables missing, including
                                        every proxy pointer and the project root
  claude_code/config/settings.json.example   every marketplace path aimed at the retired
                                        /srv tree, so a fresh install would load nothing
  hermes_agent/ops/qdrant.env.example   hardcoded :6343 — the OTHER account's live port —
                                        while claiming to be ours
  llm-failover-proxy                    no template of any kind, for the single most
                                        load-bearing config in the stack

A template nobody regenerates describes a machine that no longer exists, and it does so
confidently. Run this after any change to the live configuration; bootstrap/verify.sh
reports drift between the two.

WHAT IT DOES
------------
Reads each live file, replaces per-account values with @TOKENS@ from
config/profiles/<user>.vars, and BLANKS every secret. It refuses to write a file that
still smells of a credential — a template that leaks a key is worse than no template.

Usage:  bootstrap/make-templates.py [--profile vadim_prod] [--check]
        --check  compare only, write nothing, exit 1 on drift (for CI / verify.sh)
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HOME = os.path.expanduser("~")

# Anything matching these is a credential and must never reach a template.
SECRET_SHAPES = re.compile(
    r"(sk-[A-Za-z0-9]{20,}|sk-or-v1-[A-Za-z0-9]{20,}|nvapi-[A-Za-z0-9_-]{20,}"
    r"|AIza[A-Za-z0-9_-]{30,}|vfp_[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{30,}"
    r"|xox[baprs]-[A-Za-z0-9-]{10,}|[0-9]{8,10}:AA[A-Za-z0-9_-]{30,}|gsk_[A-Za-z0-9]{30,})")

# Env keys whose VALUE is a secret. Emitted as KEY= with the comment intact.
SECRET_KEYS = re.compile(
    r"(TOKEN|KEY|SECRET|PASSWORD|API_HASH|SESSION|PHONE|_ID)$|^TELEGRAM_ALLOWED_USERS$")


def load_vars(profile: str) -> dict[str, str]:
    p = os.path.join(REPO, "config", "profiles", f"{profile}.vars")
    out = {}
    with open(p, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                # Strip a trailing inline comment. Without this the value of
                # `PROFILE_QDRANT_HTTP_PORT=6353   # mem0 vector store` is the whole
                # right-hand side, which matches nothing — so the port stayed HARDCODED
                # in the generated template while the neighbouring GRPC port (no comment)
                # tokenised correctly. Exactly the silent per-account leak this file
                # exists to prevent, and visible only as an asymmetry between two
                # adjacent lines.
                v = re.sub(r"\s+#.*$", "", v)
                out[k.strip()] = v.strip()
    return out


def tokenise(text: str, v: dict[str, str]) -> str:
    """Longest values first, so /home/x/3dlook-marketing becomes @PROJECT_ROOT@ rather
    than @HOME@/3dlook-marketing — a token that expands to the same string either way is
    fine, but the more specific one documents intent."""
    subs = [
        (v.get("PROFILE_PROJECT_ROOT", ""), "@PROJECT_ROOT@"),
        (v.get("PROFILE_WORKSPACES", ""), "@WORKSPACES@"),
        (v.get("PROFILE_HERMES_HOME", ""), "@HERMES_HOME@"),
        (v.get("PROFILE_LLMFP_PREFIX", ""), "@LLMFP_PREFIX@"),
        (v.get("PROFILE_HOME", ""), "@HOME@"),
        (v.get("PROFILE_OWNER", ""), "@OWNER@"),
        (v.get("PROFILE_GH_OWNER", ""), "@GH_OWNER@"),
        (v.get("PROFILE_USER", ""), "@USER@"),
        (v.get("PROFILE_AGENTIC_PORT", ""), "@AGENTIC_PORT@"),
        (v.get("PROFILE_STRONG_PORT", ""), "@STRONG_PORT@"),
        (v.get("PROFILE_QDRANT_HTTP_PORT", ""), "@QDRANT_HTTP_PORT@"),
        (v.get("PROFILE_QDRANT_GRPC_PORT", ""), "@QDRANT_GRPC_PORT@"),
        (v.get("PROFILE_TELEGRAM_BOT", ""), "@TELEGRAM_BOT@"),
    ]
    subs = [(a, b) for a, b in subs if a]
    subs.sort(key=lambda t: -len(t[0]))
    for old, new in subs:
        text = text.replace(old, new)
    return text


def redact_env(text: str) -> str:
    out = []
    for line in text.split("\n"):
        if not line or line.lstrip().startswith("#") or "=" not in line:
            out.append(line); continue
        k, _, _val = line.partition("=")
        out.append(f"{k}=" if SECRET_KEYS.search(k.strip()) else line)
    return "\n".join(out)


def redact_yaml(text: str) -> str:
    text = re.sub(r"(\bapi_key:\s*)\S+", r"\1@LLMFP_LOCAL_KEY@", text)
    return text


def redact_json_secrets(obj):
    if isinstance(obj, dict):
        return {k: ("@REDACTED@" if isinstance(v, str) and SECRET_SHAPES.search(v)
                    else redact_json_secrets(v)) for k, v in obj.items()}
    if isinstance(obj, list):
        return [redact_json_secrets(x) for x in obj]
    if isinstance(obj, str) and SECRET_SHAPES.search(obj):
        return "@REDACTED@"
    return obj


def build(profile: str):
    v = load_vars(profile)
    hh = v["PROFILE_HERMES_HOME"]
    jobs = []

    def add(live, tmpl, transform=None):
        jobs.append((live, os.path.join(REPO, tmpl), transform))

    add(f"{hh}/config.yaml", "hermes_agent/config.yaml.example", redact_yaml)
    add(f"{hh}/.env", "hermes_agent/.env.example", redact_env)
    add(f"{hh}/qdrant-server/qdrant.env", "hermes_agent/ops/qdrant.env.example", redact_env)
    add(f"{HOME}/.config/opencode/opencode.jsonc", "opencode_agent/opencode.jsonc.example")
    add(f"{HOME}/.claude/settings.json", "claude_code/config/settings.json.example",
        lambda t: json.dumps(redact_json_secrets(json.loads(t)), indent=2, ensure_ascii=False) + "\n")
    add(f"{hh}/mem0.json", "hermes_agent/mem0.json.example",
        lambda t: json.dumps(redact_json_secrets(json.loads(t)), indent=2, ensure_ascii=False) + "\n")
    return v, jobs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", default=os.environ.get("USER", "vadim_prod"))
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    v, jobs = build(a.profile)
    drift = wrote = 0
    for live, tmpl, transform in jobs:
        if not os.path.isfile(live):
            print(f"  skip   {os.path.relpath(tmpl, REPO)} — live file absent ({live})")
            continue
        text = open(live, encoding="utf-8").read()
        if transform:
            try:
                text = transform(text)
            except Exception as e:
                print(f"  FAIL   {os.path.relpath(tmpl, REPO)}: {e}", file=sys.stderr)
                return 1
        text = tokenise(text, v)
        leak = SECRET_SHAPES.search(text)
        if leak:
            print(f"  REFUSED {os.path.relpath(tmpl, REPO)}: still contains something "
                  f"credential-shaped ({leak.group(0)[:6]}…) — fix the redactor, do not commit",
                  file=sys.stderr)
            return 1
        old = open(tmpl, encoding="utf-8").read() if os.path.isfile(tmpl) else None
        if old == text:
            print(f"  ok     {os.path.relpath(tmpl, REPO)}")
            continue
        drift += 1
        if a.check:
            print(f"  DRIFT  {os.path.relpath(tmpl, REPO)} differs from the live file")
        else:
            os.makedirs(os.path.dirname(tmpl), exist_ok=True)
            open(tmpl, "w", encoding="utf-8").write(text)
            wrote += 1
            print(f"  wrote  {os.path.relpath(tmpl, REPO)}")
    if a.check and drift:
        print(f"\n{drift} template(s) out of date — run bootstrap/make-templates.py")
        return 1
    print(f"\n{'checked' if a.check else 'regenerated'}: {len(jobs)} template(s)"
          + (f", {wrote} written" if wrote else ", all current"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
