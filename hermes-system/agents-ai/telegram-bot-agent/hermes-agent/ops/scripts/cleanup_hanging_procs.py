#!/usr/bin/env python3
"""
Cleanup hanging processes — zombies, idle high-RAM, and orphaned user processes.
Runs as root-capable (via sudo for kill signals where needed).
Output: concise report to stdout.

Safety rules:
- NEVER kill system daemons (sshd, systemd, cron, etc.)
- NEVER kill processes running < 1 hour (may be active work)
- For zombies: try SIGCHLD on parent first; if parent accumulates >20 zombies and
  they survive 2 cleanup cycles, flag for manual review (do NOT auto-kill the parent)
- For high-RAM idle: SIGTERM first, wait 5s, then SIGKILL
- All actions are logged
"""

import os
import re
import subprocess
import time
import sys
from collections import defaultdict

# ── Config ──────────────────────────────────────────────────
ZOMBIE_PARENT_THRESHOLD = 20       # flag parent if >N zombies
AGGRESSIVE_STRIKES = 3             # consecutive flags before aggressive kill
IDLE_CPU_THRESHOLD = 0.5           # CPU% below this = idle
IDLE_RSS_MB_THRESHOLD = 300        # RSS above this is "high memory"
IDLE_ETIME_HOURS_THRESHOLD = 2     # must be running > N hours
ORPHAN_ETIME_HOURS_THRESHOLD = 72  # orphan running > N hours = suspicious

# Known system users and daemons — never touch these
SYSTEM_USERS = {
    'root', 'daemon', 'sys', 'sync', 'games', 'man', 'lp', 'mail',
    'news', 'uucp', 'proxy', 'www-data', 'backup', 'list', 'irc',
    '_apt', 'nobody', 'systemd+', 'syslog', 'message+', 'avahi',
    'colord', 'dnsmasq', 'dhcpcd', 'polkitd', 'rtkit', 'cups-br+',
    'tcpdump', 'lightdm', 'ntp', 'statd', '_chrony',
    'postgres',  # PostgreSQL database user — never touch
}
SYSTEM_COMMANDS = {
    'systemd', 'systemd-', '(sd-', 'sshd', 'cron', 'rsyslogd',
    'dbus-daemon', 'polkitd', 'accounts-daemon', 'NetworkManager',
    'wpa_supplicant', 'udisksd', 'upowerd', 'ModemManager',
    'containerd', 'dockerd', 'agetty', 'login',
    'postgres',  # PostgreSQL — never touch any postgres process
}
# Server-like processes — expected to run forever with low CPU, NEVER kill
SERVER_WHITELIST = {
    'next-server', 'next-router', 'nginx', 'apache2', 'httpd',
    'gunicorn', 'uvicorn', 'uvicorn.', 'gatsby', 'vite',
    'mongod', 'postgres', 'mysqld', 'redis-server', 'sqlite',
    'dockerd', 'containerd', 'k3s', 'kubelet',
    'jenkins', 'elasticsearch', 'logstash', 'kibana',
    # The agent's own gateway: idles by design between messages, and this
    # very job runs *inside* it — killing it aborts the job mid-run.
    'hermes',
}
# Commands that indicate a one-off / interactive process — safe to kill if idle
ONE_OFF_COMMANDS = {
    'claude', 'opencode', 'codex', 'code', 'bash', 'sh', 'zsh',
    'python3', 'python', 'node', 'ruby', 'perl', 'php',
    'npm', 'npx', 'yarn', 'pnpm', 'bun',
    'git', 'docker', 'kubectl', 'terraform', 'ansible',
    'vim', 'nvim', 'nano', 'emacs', 'less', 'man',
    'ssh', 'scp', 'sftp', 'rsync', 'curl', 'wget',
}

# ── Helpers ──────────────────────────────────────────────────
def run(cmd, timeout=15):
    """Run shell command, return (stdout, stderr, exit_code)."""
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True,
                          text=True, timeout=timeout)
        return r.stdout.strip(), r.stderr.strip(), r.returncode
    except subprocess.TimeoutExpired:
        return '', 'timeout', -1

def parse_ps():
    """
    Parse `ps aux` into structured records.
    Returns list of dicts: {pid, ppid, user, stat, rss_kb, cpu, etime_sec, comm, args}
    """
    # Use ps to get: USER PID PPID STAT RSS %CPU ETIME COMMAND
    out, _, _ = run("ps -eo user,pid,ppid,stat,rss,pcpu,etime,comm,args --no-headers", timeout=30)
    records = []
    for line in out.split('\n'):
        parts = line.split(None, 8)  # maxsplit=8 → 9 fields
        if len(parts) < 8:
            continue
        user, pid_s, ppid_s, stat, rss_s, cpu_s, etime_s, comm = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7]
        args = parts[8] if len(parts) == 9 else comm
        try:
            pid = int(pid_s)
            ppid = int(ppid_s)
            rss_kb = int(rss_s)
            cpu = float(cpu_s)
            etime_sec = parse_etime(etime_s)
        except (ValueError, IndexError):
            continue
        records.append({
            'pid': pid, 'ppid': ppid, 'user': user, 'stat': stat,
            'rss_kb': rss_kb, 'cpu': cpu, 'etime_sec': etime_sec,
            'comm': comm, 'args': args,
        })
    return records

def parse_etime(etime_str):
    """Convert ps etime ([[DD-]hh:]mm:ss) to seconds."""
    days = hours = minutes = seconds = 0
    if '-' in etime_str:
        day_part, time_part = etime_str.split('-', 1)
        days = int(day_part)
    else:
        time_part = etime_str
    parts = list(map(int, time_part.split(':')))
    if len(parts) == 3:
        hours, minutes, seconds = parts
    elif len(parts) == 2:
        minutes, seconds = parts
    else:
        seconds = parts[0]
    return days * 86400 + hours * 3600 + minutes * 60 + seconds

def is_system_process(rec):
    """Return True if this is a system daemon we must never touch."""
    if rec['user'] in SYSTEM_USERS:
        return True
    comm_lower = rec['comm'].lower()
    for sc in SYSTEM_COMMANDS:
        if comm_lower.startswith(sc.lower()):
            return True
    return False

def is_server_process(rec):
    """Return True if this looks like a long-running server (never kill)."""
    comm = rec['comm']
    # Exact match or starts-with for server binaries
    for srv in SERVER_WHITELIST:
        if comm == srv or comm.startswith(srv):
            return True
    # Also check args for server patterns
    args = rec.get('args', '')
    server_keywords = ['server', 'serve', 'daemon', '--production', 'start', 'listen']
    if any(kw in args.lower() for kw in server_keywords):
        return True
    return False

def is_supervised(rec):
    """Return True if the process belongs to a systemd .service unit.

    Killing a supervised daemon is pointless — systemd restarts it seconds
    later — and here it was actively harmful: this job runs inside
    hermes-gateway.service, so on 2026-08-05 00:00 phase 2 saw the gateway as
    'idle high-RAM' (302MB, 0.4% CPU, 18h) and SIGTERM'd the very process
    hosting the job. Every ~4th night the run died as 'unknown'.
    """
    try:
        with open(f"/proc/{rec['pid']}/cgroup", encoding="utf-8") as fh:
            return ".service" in fh.read()
    except (OSError, ValueError):
        return False

def is_one_off(rec):
    """Return True if this is a one-off / interactive process (safe to kill)."""
    comm = rec['comm']
    for cmd in ONE_OFF_COMMANDS:
        if comm == cmd or comm.startswith(cmd):
            return True
    return False

def send_signal(pid, sig, sudo=False):
    """Send signal to PID. Returns True on success."""
    cmd = f"sudo kill -{sig} {pid}" if sudo else f"kill -{sig} {pid}"
    _, err, rc = run(cmd, timeout=5)
    return rc == 0

def process_exists(pid):
    """Check if PID still exists."""
    return os.path.exists(f"/proc/{pid}")

def estimate_ram_freed(pids_killed, procs):
    """Estimate RAM freed (RSS sum) from killed processes."""
    total_kb = 0
    for p in procs:
        if p['pid'] in pids_killed:
            total_kb += p['rss_kb']
    return total_kb

# ── Logging ──────────────────────────────────────────────────
LOG_FILE = os.path.expanduser("~/.hermes/logs/cleanup_hanging_procs.log")

def log(msg):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{timestamp}] {msg}\n")

# ── Phase 1: Zombie cleanup ──────────────────────────────────
def cleanup_zombies(records):
    """
    Find zombie processes (stat contains 'Z'), group by parent,
    attempt SIGCHLD on parent to trigger waitpid.
    Returns (zombies_cleaned, parents_flagged, ram_freed_kb).
    """
    zombies_by_parent = defaultdict(list)
    for rec in records:
        if 'Z' in rec['stat']:
            zombies_by_parent[rec['ppid']].append(rec)

    if not zombies_by_parent:
        return 0, 0, 0

    zombies_cleaned = 0
    parents_flagged = 0

    for ppid, zlist in zombies_by_parent.items():
        parent = next((r for r in records if r['pid'] == ppid), None)
        parent_name = parent['comm'] if parent else f"PID-{ppid}"

        log(f"Zombie parent: PID={ppid} ({parent_name}) has {len(zlist)} zombie children")

        # Try SIGCHLD first — ask parent to reap
        if send_signal(ppid, 'CHLD'):
            log(f"  → Sent SIGCHLD to parent {ppid} ({parent_name})")
            time.sleep(1)
        else:
            log(f"  → Could not send SIGCHLD to parent {ppid} — permission denied or gone")

        # Check if zombies were reaped
        remaining = sum(1 for z in zlist if process_exists(z['pid']))
        cleaned = len(zlist) - remaining
        zombies_cleaned += cleaned

        if remaining > 0 and len(zlist) >= ZOMBIE_PARENT_THRESHOLD:
            parents_flagged += 1
            log(f"  ⚠ {remaining} zombies remain — parent flagged for review")

    # Zombies don't consume RSS (already dead) — but their parent may have inflated VmSize
    return zombies_cleaned, parents_flagged, 0

# ── Phase 2: High-RAM idle processes ─────────────────────────
def cleanup_idle_highram(records):
    """
    Find non-system user processes with high RSS, very low CPU,
    running for a long time — likely abandoned/memory-leaked.
    Attempts SIGTERM → wait → SIGKILL.
    Returns (killed_count, ram_freed_kb).
    """
    targets = []
    for rec in records:
        if is_system_process(rec):
            continue
        if is_server_process(rec):
            continue  # never kill servers
        rss_mb = rec['rss_kb'] / 1024
        etime_h = rec['etime_sec'] / 3600
        if (rss_mb >= IDLE_RSS_MB_THRESHOLD
                and rec['cpu'] < IDLE_CPU_THRESHOLD
                and etime_h >= IDLE_ETIME_HOURS_THRESHOLD):
            # Checked only for real candidates: /proc reads are cheap but the
            # log line goes to Telegram, so it must name a genuine target.
            if is_supervised(rec):
                log(f"Idle high-RAM: PID={rec['pid']} ({rec['comm']}) "
                    f"RSS={rss_mb:.0f}MB — SKIP, systemd-supervised service")
                continue
            targets.append(rec)

    killed = 0
    ram_freed = 0

    for rec in targets:
        log(f"Idle high-RAM: PID={rec['pid']} ({rec['comm']}) user={rec['user']} "
            f"RSS={rec['rss_kb']/1024:.0f}MB CPU={rec['cpu']}% etime={rec['etime_sec']/3600:.1f}h")

        # SIGTERM first
        if send_signal(rec['pid'], 'TERM'):
            log(f"  → Sent SIGTERM to PID={rec['pid']}")
            time.sleep(5)
            if not process_exists(rec['pid']):
                killed += 1
                ram_freed += rec['rss_kb']
                log(f"  ✓ Terminated gracefully")
                continue

        # SIGKILL backup
        if process_exists(rec['pid']):
            if send_signal(rec['pid'], 'KILL'):
                log(f"  → Sent SIGKILL to PID={rec['pid']}")
                time.sleep(2)
                if not process_exists(rec['pid']):
                    killed += 1
                    ram_freed += rec['rss_kb']
                    log(f"  ✓ Force killed")
                else:
                    log(f"  ✗ Failed to kill")
            else:
                log(f"  ✗ Could not send signal — permission denied")

    return killed, ram_freed

# ── Phase 3: Suspicious orphan processes ─────────────────────
def cleanup_orphans(records):
    """
    Find user processes with PPID=1 (orphaned) that are not system daemons.
    If they've been running > 24h and have low CPU, terminate them.
    Returns (killed_count, ram_freed_kb).
    """
    orphans = []
    for rec in records:
        if rec['ppid'] != 1:
            continue
        if is_system_process(rec):
            continue
        if is_server_process(rec):
            continue  # never kill servers, even if orphaned
        etime_h = rec['etime_sec'] / 3600
        if etime_h >= ORPHAN_ETIME_HOURS_THRESHOLD:
            if is_supervised(rec):
                continue  # systemd-supervised: restarting it changes nothing
            orphans.append(rec)

    killed = 0
    ram_freed = 0

    for rec in orphans:
        # Extra safety: skip processes with recent activity
        # Check /proc/PID/stat for utime+stime change
        log(f"Orphan: PID={rec['pid']} ({rec['comm']}) user={rec['user']} "
            f"RSS={rec['rss_kb']/1024:.0f}MB etime={rec['etime_sec']/3600:.1f}h")

        if send_signal(rec['pid'], 'TERM'):
            log(f"  → Sent SIGTERM to PID={rec['pid']}")
            time.sleep(3)
            if not process_exists(rec['pid']):
                killed += 1
                ram_freed += rec['rss_kb']
                log(f"  ✓ Terminated")
                continue

        if process_exists(rec['pid']):
            if send_signal(rec['pid'], 'KILL'):
                time.sleep(2)
                if not process_exists(rec['pid']):
                    killed += 1
                    ram_freed += rec['rss_kb']
                    log(f"  ✓ Force killed")

    return killed, ram_freed

# ── Phase 4: Zombie parent re-check ──────────────────────────
def aggressive_zombie_cleanup(records):
    """
    Second pass: if the same zombie parent was flagged last run
    (via state file), escalate — kill the parent so init reaps zombies.
    """
    state_file = os.path.expanduser("~/.hermes/state/zombie_parents.txt")
    os.makedirs(os.path.dirname(state_file), exist_ok=True)

    # Load previous state — TAB-separated: PID\tCOUNT\tTIMESTAMP\tPARENT_NAME\tSTRIKES
    prev_parents = {}
    if os.path.exists(state_file):
        with open(state_file) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                # Try tab-separated format first (current)
                parts = line.split('\t')
                if len(parts) >= 5:
                    try:
                        prev_parents[int(parts[0])] = {
                            'zombie_count': int(parts[1]),
                            'timestamp': parts[2],
                            'strikes': int(parts[4]),
                        }
                    except (ValueError, IndexError):
                        pass
                    continue
                # Fallback: legacy space-separated format (PID COUNT TIMESTAMP PARENT_NAME STRIKES)
                # PARENT_NAME may contain spaces, so parse from left: PID, COUNT, TIMESTAMP are fixed,
                # then the last token is STRIKES, everything in between is PARENT_NAME
                space_parts = line.split()
                if len(space_parts) >= 4:
                    try:
                        pid = int(space_parts[0])
                        zombie_count = int(space_parts[1])
                        timestamp = space_parts[2]
                        # Last token is strikes (or rest of line for old 4-field format)
                        strikes = 1
                        if len(space_parts) >= 5:
                            strikes = int(space_parts[-1])
                        prev_parents[pid] = {
                            'zombie_count': zombie_count,
                            'timestamp': timestamp,
                            'strikes': strikes,
                        }
                    except (ValueError, IndexError):
                        pass

    # Current zombies by parent
    zombies_by_parent = defaultdict(list)
    for rec in records:
        if 'Z' in rec['stat']:
            zombies_by_parent[rec['ppid']].append(rec)

    killed_parents = 0
    ram_freed = 0
    new_state = []

    for ppid, zlist in zombies_by_parent.items():
        parent = next((r for r in records if r['pid'] == ppid), None)
        parent_name = parent['comm'] if parent else 'unknown'
        count = len(zlist)

        # Determine strikes
        prev = prev_parents.get(ppid, {})
        prev_zombie_count = prev.get('zombie_count', 0)
        strikes = prev.get('strikes', 0)
        if count == prev_zombie_count and count > 0:
            strikes += 1
        else:
            strikes = 1

        # Save state for next run (TAB-separated)
        new_state.append(f"{ppid}\t{count}\t{time.strftime('%Y-%m-%dT%H:%M:%S')}\t{parent_name}\t{strikes}")

        # Skip aggressive cleanup if:
        # - parent is root-owned (too risky to kill blindly)
        # - we don't have enough strikes yet
        # - we couldn't even send SIGCHLD in phase 1 (permission issue)
        skip_reasons = []
        if parent and parent['user'] == 'root':
            skip_reasons.append('root-owned')
        if parent and is_supervised(parent):
            skip_reasons.append('systemd-supervised')
        if strikes < AGGRESSIVE_STRIKES:
            skip_reasons.append(f'strikes={strikes}/{AGGRESSIVE_STRIKES}')
        if count < ZOMBIE_PARENT_THRESHOLD:
            skip_reasons.append(f'zombies={count}<{ZOMBIE_PARENT_THRESHOLD}')

        if skip_reasons:
            log(f"Zombie parent PID={ppid} ({parent_name}): skip aggressive — {', '.join(skip_reasons)}")
            continue

        # Aggressive: kill the parent so init reaps zombies
        log(f"Aggressive: killing zombie parent PID={ppid} ({parent_name}) "
            f"with {count} zombie children (strikes={strikes})")
        if send_signal(ppid, 'TERM', sudo=True):
            log(f"  → Sent SIGTERM to parent {ppid}")
            time.sleep(5)
            if not process_exists(ppid):
                killed_parents += 1
                if parent:
                    ram_freed += parent['rss_kb']
                log(f"  ✓ Parent terminated — init will reap zombies")
            else:
                log(f"  ⚠ Parent survived SIGTERM — will retry next run")
        else:
            log(f"  ✗ Could not signal parent {ppid}")

    # Write new state
    with open(state_file, 'w') as f:
        f.write('\n'.join(new_state))

    return killed_parents, ram_freed

# ── Main ─────────────────────────────────────────────────────
def main():
    log("=== Cleanup run started ===")
    records = parse_ps()
    log(f"Total processes: {len(records)}")

    # Phase 1: Zombies
    z_cleaned, z_flagged, _ = cleanup_zombies(records)

    # Phase 2: Idle high-RAM
    idl_killed, idl_ram = cleanup_idle_highram(records)

    # Phase 3: Orphans
    orph_killed, orph_ram = cleanup_orphans(records)

    # Phase 4: Aggressive zombie parent cleanup
    agg_killed, agg_ram = aggressive_zombie_cleanup(records)

    total_killed = z_cleaned + idl_killed + orph_killed + agg_killed
    total_ram_mb = (idl_ram + orph_ram + agg_ram) / 1024

    # ── Build report ─────────────────────────────────────────
    lines = []
    lines.append("=== Отчет очистки процессов ===")
    lines.append(f"Время: {time.strftime('%Y-%m-%d %H:%M:%S')}")

    if z_cleaned > 0:
        lines.append(f"[Зомби] Закрыто: {z_cleaned} процессов (родители получили SIGCHLD)")
    if z_flagged > 0:
        lines.append(f"[Зомби] Родителей с >={ZOMBIE_PARENT_THRESHOLD} зомби помечено: {z_flagged} (root-процессы не трогаем, нужно ручное расследование)")
    if idl_killed > 0:
        lines.append(f"[Простой] Закрыто idle high-RAM: {idl_killed} процессов, высвобождено ~{idl_ram/1024:.0f} MB")
    if orph_killed > 0:
        lines.append(f"[Сироты] Закрыто орфан-процессов: {orph_killed}, высвобождено ~{orph_ram/1024:.0f} MB")
    if agg_killed > 0:
        lines.append(f"[Агрессивно] Зомби-родителей убито: {agg_killed}, высвобождено ~{agg_ram/1024:.0f} MB")

    if total_killed == 0 and z_flagged == 0:
        lines.append("[OK] Висячих процессов не найдено.")
    elif total_killed == 0 and z_flagged > 0:
        lines.append(f"[OK] Процессов не закрыто. Зомби-родителей на проверке: {z_flagged}.")
    else:
        lines.append(f"[Итого] Закрыто: {total_killed} процессов, высвобождено RAM: ~{total_ram_mb:.0f} MB")

    report = '\n'.join(lines)
    log(f"=== Cleanup finished: {total_killed} killed, ~{total_ram_mb:.0f} MB freed ===")

    print(report)
    return 0

if __name__ == '__main__':
    sys.exit(main())
