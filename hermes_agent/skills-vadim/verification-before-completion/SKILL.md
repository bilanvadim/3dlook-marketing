---
name: verification-before-completion
description: "Use before telling Vadim in Telegram that a task is done, fixed, sent, published, scheduled or passing, and whenever an executor (Claude Code, OpenCode, a conductor job, a cron script) reports its own success. Check the claim with a fresh command first; relay the evidence, not the executor's words."
version: 1.0.0
author: Вадим + Claude (adapted from obra/superpowers verification-before-completion, MIT)
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [Verification, Reporting, Conductor, Quality]
    related_skills: [vps-orchestration, systematic-debugging]
---

# Verification Before Completion

An executor's "done" is a claim. Before you relay it to Vadim, check it
yourself with one fresh command. If you can't check it, say so.

```
NO "ГОТОВО" IN TELEGRAM WITHOUT FRESH EVIDENCE FROM THIS TURN
```

## The gate

1. **Identify** the observation that proves the claim (table below).
2. **Run** it now via `terminal` / `read_file`. The executor's summary, an
   old log line or a `Ready: YES` written into a file is not evidence.
3. **Read** the output: exit code, counts, the actual text.
4. **Report**: claim + evidence in one line. Not proven → the real status.
   Can't check → «не перевірено: X, бо Y».

## Evidence

| Executor says | You check | Not enough |
|---|---|---|
| files written / pack ready | the files exist and are non-empty (`ls -la`, `wc -c`), open one | the job summary |
| committed / pushed | `git -C ~/3dlook-marketing fetch -q && git -C ~/3dlook-marketing log origin/main -1 --format='%h %s'` | "commit created" |
| gate / lint passed | rerun the gate script, exit 0 | the gate's verdict from an earlier run |
| page live | `curl -sL -o /dev/null -w '%{http_code}' <url>` = 200 **and** `curl -sL <url> \| grep -c "<changed text>"` ≥ 1 | the draft in the repo |
| cron / service set | `crontab -l \| grep <script>` or `systemctl --user status <unit>` + `journalctl --user -u <unit> --since "-10min"` | "I edited the file" |
| conductor job finished | job status in the conductor DB and the promised artifact on disk | the job's own last message |
| fixed | the original symptom no longer reproduces | the service shows `active` |

## Red flags

- relaying the executor's text as-is
- «Готово!» before the check ran
- checking one item of many and reporting all of them
- "має працювати", "should", "probably"

## Report format (Telegram, Ukrainian)

✅ «Пак готовий: 9/9 post.md на диску, коміт a1b2c3d на origin/main.»
✅ «Не перевірено: імпорт у closely робить Гліб.»
❌ «Готово, все працює.»
