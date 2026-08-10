# Process Cleanup Script — Design & Safety

The canonical script: `~/.hermes/scripts/cleanup_hanging_procs.py` (~460 lines).

## Phase Architecture

### Phase 1: Zombie Cleanup
- Finds all processes with `Z` in `STAT` column
- Groups zombies by parent PID
- Sends `SIGCHLD` to each parent, asking it to `waitpid()` and reap children
- Zombies consume no RSS (they're already dead) but bloat the parent's VmSize
  and consume PID table entries
- Flags parents accumulating ≥20 zombie children for later escalation

### Phase 2: Idle High-RAM
- Finds non-system, non-server user processes where:
  - RSS ≥ 300 MB
  - CPU < 0.5%
  - Running > 2 hours
- Attempts `SIGTERM` → waits 5s → `SIGKILL` if still alive
- Skips processes owned by other users (permission boundary)
- Skips server processes (checked via `is_server_process()`)

### Phase 3: Orphaned User Processes
- Finds processes with PPID=1 (adopted by init) that are NOT system daemons
- Must have been running > 72 hours (to avoid killing recently-started sessions)
- Skips system users, server processes
- Same SIGTERM → SIGKILL escalation

### Phase 4: Aggressive Zombie Parent Cleanup
- Reads state from `~/.hermes/state/zombie_parents.txt`
- Tracks consecutive runs where a parent has the same zombie count (strike counter)
- Only escalates after ≥3 strikes (i.e., zombie count unchanged across 3 cleanup runs)
- **Never kills root-owned zombie parents** — manual investigation required
- Kills the parent with SIGTERM; init (PID 1) then adopts and reaps all zombies

## Whitelists & Detection

### SYSTEM_USERS
Users whose processes are never touched: root, daemon, sys, www-data, systemd+, avahi,
dnsmasq, dhcpcd, polkitd, rtkit, tcpdump, lightdm, cups-br+, etc.

### SYSTEM_COMMANDS
Commands that are never killed: systemd, sshd, cron, rsyslogd, dbus-daemon, polkitd,
NetworkManager, containerd, dockerd, agetty, login.

### SERVER_WHITELIST
Known server binaries that should run forever: next-server, nginx, gunicorn, uvicorn,
mongod, postgres, mysqld, redis-server, dockerd, containerd, jenkins, elasticsearch.

Note: `node`, `python`, `java` are intentionally NOT in the whitelist (too broad).
Instead, server detection also scans process args for keywords: `server`, `serve`,
`daemon`, `--production`, `start`, `listen`.

### ONE_OFF_COMMANDS
Commands that indicate interactive / one-off processes — safe to kill if idle:
claude, opencode, codex, bash, sh, npm, npx, yarn, git, ssh, curl, vim, etc.

## State Files

| File | Purpose |
|------|---------|
| `~/.hermes/logs/cleanup_hanging_procs.log` | Full action log with timestamps |
| `~/.hermes/state/zombie_parents.txt` | Per-parent zombie count + strike counter |

## Report Format (Russian, to Telegram)

```
=== Отчет очистки процессов ===
Время: 2026-07-13 12:00:00
[Зомби] Родителей с >=20 зомби помечено: 1 (root-процессы не трогаем, нужно ручное расследование)
[Простой] Закрыто idle high-RAM: 1 процессов, высвобождено ~322 MB
[Сироты] Закрыто орфан-процессов: 1, высвобождено ~145 MB
[Итого] Закрыто: 2 процессов, высвобождено RAM: ~467 MB
```

Or when nothing found:
```
=== Отчет очистки процессов ===
Время: 2026-07-13 00:00:00
[OK] Висячих процессов не найдено.
```

## Testing the Script

```bash
# Dry-run detection only (no kills) — modify main() to skip kill phases
python3 ~/.hermes/scripts/cleanup_hanging_procs.py

# Check log
tail -30 ~/.hermes/logs/cleanup_hanging_procs.log

# Check zombie state
cat ~/.hermes/state/zombie_parents.txt

# Manually trigger cron job
cronjob(action='run', job_id='<job_id>')
```

## Common Scenarios

### 80 zombie node processes from one root parent
- Parent: `node dist/server/server.js` (root, sleeping)
- SIGCHLD to parent fails (permission denied / no handler)
- Root-owned → aggressive kill blocked
- Resolution: manually investigate and restart the service, or accept the zombies
  (they consume no RSS, just PID table entries)

### vadim_prod 3.6GB node process
- Running as vadim_prod user, CPU 0.1%, 26h uptime
- Cannot kill (permission denied) — intentional cross-user boundary
- Flag it in the report? Currently skipped silently.

### next-server killed accidentally (v1 bug, since fixed)
- `next-server` was not in SERVER_WHITELIST in v1
- Killed as "idle high-RAM" — 1.7GB, CPU 0.2%, 47h uptime
- Fixed by adding `next-server` to SERVER_WHITELIST + args-based detection
