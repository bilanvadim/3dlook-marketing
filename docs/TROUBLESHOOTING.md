# Troubleshooting

Every entry below is a failure that actually happened on this system, with the
symptom as it presented — not a catalogue of what could theoretically go wrong.

**Start here for anything:**
```bash
./bootstrap/verify.sh
```

---

## Telegram is silent

**Check the gateway first.** It is the only thing that talks to Telegram; nothing
else can compensate for it being down.

```bash
systemctl --user status hermes-gateway
tail -50 ~/.hermes/logs/gateway.log
```

Things that have caused this:

- **Gateway wedged after a drain timeout** — it stops responding but does not die,
  so systemd sees a healthy service. Restart it.
- **Two processes polling the same bot token.** Telegram allows one `getUpdates`
  consumer; a second one makes both flap. Look for a stray conductor or a second
  gateway.
- **Config corruption.** The gateway has rewritten `~/.hermes/config.yaml` into
  invalid YAML on restart before, silently ignoring its own overrides and falling
  back to a free-tier model that then 429s. If replies are strange rather than
  absent, validate the YAML.
- `httpx.ReadError` followed by "polling restarted" is normal transient network
  noise — it recovers on its own.

**Exit code 75 alone proves nothing.** It is also the normal planned-restart code.
Look for the `CRITICAL` line before concluding a crash.

---

## A job says `done` but nothing was produced

The status only means the SDK session ended cleanly.

```bash
hermes_agent/ops/mvb-verify-job.py <id>
```

The known cause: the run delegated to a subagent, the Agent tool returned
`Async agent launched successfully`, and the model read that as "started, now I
wait", wrote a status line and **ended its turn**. The session closed, the spawned
agent died with it — job 98's subagent made zero tool calls.

The prompts now forbid this explicitly, but a prompt rule is not a guarantee. The
verifier is, because it counts files rather than trusting a summary. The monitor
downgrades ✅ to ⚠️ when artifacts are zero.

---

## A run reports "sandbox restriction" and estimates a result instead of measuring it

Almost always the permission model, not a sandbox.

The conductor opens sessions with `settingSources: ['project']`, which loads
`.claude/settings.json` and **nothing else**. Allow rules parked in
`settings.local.json` are invisible to every autonomous run, and with
`permissionMode: 'acceptEdits'` only file edits are auto-approved — Bash,
WebSearch and WebFetch fall through to a permission prompt no headless session can
answer. That is a silent deny, and the agent then rationalises it.

Fix: put the rule in `marketing_vb/.claude/settings.json`, scoped narrowly.
Do **not** add a blanket `Bash(python3:*)`: `guard.py` can only pattern-match a
command string, so `python3 -c "..."` sails past every rule in it.

Symptom to be suspicious of in any report: a claim that a tool could not run,
followed by a number that was reasoned out rather than measured. Run the tool
yourself before believing it.

---

## An agent behaves like an older version of itself

Every agent exists in three places: the marketplace source under
`claude_code/DEV/marketing_vb/plugins/`, the installed copy under
`marketing_vb/.claude/plugins/*/0.2.0/`, and the project copy under
`marketing_vb/.claude/agents/`. Nothing keeps them equal, and the project copy and
the plugin copy declare the **same** `name:` — while identical that is harmless,
the moment they diverge which one answers is a coin toss.

```bash
marketing_vb/scripts/check-agent-copies.py
```

Runs daily at 05:55 and pushes to Telegram on drift. It deliberately does not fix
anything: an automatic merge would silently pick a winner, which is the failure it
exists to prevent.

---

## The article pipeline re-plans instead of continuing

«Апрув» on its own does not reach the pipeline. It must carry the token:

```bash
mvb-run.py article "<exact same topic>" approve
```

Without it the run either re-plans from scratch or walks to checkpoint 1 and waits
for a human who is not there. With it and no stage named, the run goes
write → edit → publish in one job and stops only at checkpoint 2.

Related trap: «Апрув» never means "make social posts". Posts require both a
`publish-package.md` on disk and an explicit request for posts. On 2026-08-26 an
approval on a plan-stage article was read as "article approved → make posts", and
when `mvb-run.py posts` correctly refused twice, the run **renamed directories** to
get past the precondition and fanned out nine jobs against a stale draft. A
refusal from `mvb-run.py` is a fact about the state of the work, never an obstacle.

---

## Everything is slow, or a job sits for hours

Look for rate limiting before assuming a hang:

```bash
journalctl --user -u hermes-conductor --since "-2h" | grep "rate limit"
```

`paused: rate limit — streak N, turns this run 2, retry in Ns` means the backoff
ladder is working. Two turns per resume is the signature of an exhausted window:
each resume gets a couple of turns and hits the wall again.

**The conductor shares your Claude usage window.** An autonomous run can lock you
out of your own interactive sessions and vice versa. This is why the social
pipeline fans out per profile — it does not spend less quota, it changes what
hitting a limit costs from a half-finished 200-turn run to "the profiles not
started yet".

Stalls longer than ten minutes now push a ⏳ notice to Telegram, so silence no
longer looks the same as progress.

---

## Notifications arrive in the wrong Telegram topic

Fixed on 2026-08-26; if it recurs, the mapping is
`~/.hermes/mvb-job-threads.json`, written by `mvb-run.py` at enqueue from the
gateway's `HERMES_SESSION_CHAT_ID` / `HERMES_SESSION_THREAD_ID`.

A job started from a plain shell has neither variable and correctly falls back to
General. Note that `message_thread_id` alone is unreliable in these private-chat
topics — it needs pairing with `reply_to_message_id` from the switcher's anchors.

---

## Something reaches for `/srv/…/ai-agents-config`

It should not. That tree is a different system and was cut loose on 2026-08-26.

```bash
./bootstrap/verify.sh    # fails on any live reference
```

The one that matters most is `hermes-update.py`: it runs daily at 06:01 and used
to re-copy SOUL.md, the patch appliers and the model-router out of that tree, so
the dependency came **back on its own** after any manual cleanup. `verify.sh`
checks that file specifically for this reason.

---

## Useful commands

```bash
mvb-run.py status                    # queue + open questions/escalations
mvb-verify-job.py <id>               # did that job produce anything
journalctl --user -u hermes-conductor -f
tail -f ~/.hermes/logs/gateway.log
DRY_RUN=1 bash hermes_agent/ops/conductor-guard/hermes-conductor-guard.sh
sqlite3 ~/.hermes/ho.db "select id,status,title from ho_jobs order by id desc limit 10;"
```
