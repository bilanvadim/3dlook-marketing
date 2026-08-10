---
name: vps-maintenance
description: "Automated VPS health monitoring and process cleanup — zombie reaping, idle high-RAM termination, orphan process cleanup. Use when setting up or modifying automated system maintenance cron jobs, or when diagnosing a VPS with accumulated zombie/idle processes."
version: 1.1.0
author: Hermes Agent + Sergiy
license: MIT
platforms: [linux]
metadata:
  hermes:
    tags: [vps, maintenance, cleanup, cron, monitoring, processes, ram]
    related_skills: [vps-orchestration]
---

# VPS Maintenance — Automated Process Cleanup & Health Monitoring

System-level maintenance for multi-user VPS: identify and safely terminate hanging
processes (zombies, idle high-RAM, orphaned user processes) via automated cron jobs.
Delivers concise Telegram reports after each run.

## Trigger

Load this skill when:
- Setting up automated VPS process cleanup / health monitoring
- Diagnosing accumulated zombie or idle processes on the VPS
- Modifying the cleanup script or cron schedule
- User asks about freeing RAM from hanging processes

## Cron Architecture

Use Hermes cron with `no_agent=True` + `script` — the script IS the job, no LLM
reasoning needed at runtime. This is the right pattern for deterministic,
safety-critical system tasks:

```
cronjob(
  action='create',
  name='Очистка висячих процессов',
  schedule='0 0,12 * * *',        # twice daily: 12:00 and 00:00
  script='cleanup_hanging_procs.py',
  no_agent=True,                    # script produces the report directly
  deliver='origin',                 # back to the chat where it was created
)
```

Why `no_agent=True`:
- The cleanup logic has well-defined safety rules — no LLM judgment needed
- Eliminates API cost per run (the script runs in <2s, no model calls)
- The script's stdout IS the report delivered to the user
- Consistent, auditable behavior every run

See `references/process-cleanup.md` for the full script design and safety rules.

## Script Location

The canonical cleanup script lives at: `~/.hermes/scripts/cleanup_hanging_procs.py`

It is a standalone Python script (no dependencies beyond stdlib) that:
1. Parses `ps` output into structured records
2. Runs four cleanup phases in order
3. Logs all actions to `~/.hermes/logs/cleanup_hanging_procs.log`
4. Prints a concise Russian-language report to stdout

## Safety Rules (non-negotiable)

These are baked into the script and must be preserved in any modification:

1. **Never kill system daemons** — `SYSTEM_USERS` and `SYSTEM_COMMANDS` sets
2. **Never kill server processes** — `SERVER_WHITELIST` + args-based detection
3. **Never kill root-owned zombie parents** — too risky, manual investigation only
4. **SIGTERM first, SIGKILL only as backup** — give processes a chance to exit gracefully
5. **Strike counter for escalation** — aggressive cleanup only after 3 consecutive flags
6. **Never kill other users' processes** — permission boundaries protect cross-user safety
7. **Minimum uptime thresholds** — don't touch processes running <2h (idle) or <72h (orphans)

## Pitfalls

- **Killing servers**: The script's first version lacked `SERVER_WHITELIST` and killed
  `next-server` (1.7GB Next.js dev server). Always check `is_server_process()` for
  known server binaries AND scan args for keywords like `server`, `serve`, `daemon`.
- **Too-broad whitelist**: `node` was initially in `SERVER_WHITELIST`, which blocked
  cleanup of ALL Node.js processes (including abandoned one-off scripts). Removed it;
  rely on args-based detection instead.
- **Zombie parent kills**: The aggressive phase tried to kill a root-owned `node`
  server with 80 zombie children on the second run. Fixed by adding root-owned check
  and requiring 3+ consecutive strikes before escalation.
- **PostgreSQL safety** (2026-07-23): `postgres` added to both `SYSTEM_USERS` and
  `SYSTEM_COMMANDS` — never touch any postgres process even if UID shows as numeric.
- **State file crash** (2026-07-23): State file format changed from space-separated
  to TAB-separated (`PID\\tCOUNT\\tTIMESTAMP\\tPARENT_NAME\\tSTRIKES`) because process
  names with spaces (e.g. `node /path/script.js`) broke parsing. Added backward-compat
  fallback for legacy space-separated lines.
- **Permission failures are expected**: The script runs as the agent's user; it cannot
  kill processes owned by other users (vadim_prod, root). That's intentional — cross-user
  cleanup requires manual intervention.

## Modifying the Schedule

To change frequency:
```
cronjob(action='update', job_id='<id>', schedule='0 */6 * * *')  # every 6 hours
```

To add per-job model override (not needed for `no_agent=True` scripts):
```
cronjob(action='update', job_id='<id>', model={'model': '...'})
```

## Related

- `vps-orchestration` — coding task routing and conductor pipeline management
- `hermes-agent` — Hermes cron and script documentation (bundled skill)
