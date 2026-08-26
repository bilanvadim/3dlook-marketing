# Configuration — what lives where, and which copy wins

The rule: **git is the source of truth, runtime locations receive copies through an
install step.** Nothing is edited in place at runtime. When you find yourself
editing a file under `~/.hermes` or `~/.config`, you are editing something that
`bootstrap/install.sh` will overwrite — change it here instead.

```
this repo  ──bootstrap/install.sh──►  ~/.config/systemd/user/   units, drop-ins
                                      crontab                    scheduled checks
           ──hermes-update.py──────►  ~/.hermes/                 SOUL, patches, router
                                      ~/.hermes/hermes-agent/gateway/  claude_switcher.py
```

## Deliberately NOT in git

| Path | Why |
|---|---|
| `~/.hermes/ho.db` | Job queue. Per-machine state; a live SQLite file in WAL mode is not one file, and committing it produces torn snapshots. |
| `~/.config/ai-agent-stack/secrets.env` | Real credentials. `secrets.env.example` documents all 26 keys with empty values. |
| `~/.hermes/mtproto/session.enc` | A Telegram login. Re-enrol rather than copy. |
| `node_modules/` | Rebuilt by `npm install`; `better-sqlite3` is native and must be built on the target machine anyway. |

## Where each piece of configuration lives

| What | Source of truth | Reaches runtime by |
|---|---|---|
| systemd units and drop-ins | `hermes_agent/ops/systemd/vadim-user/` | `install.sh` copies to `~/.config/systemd/user/` |
| Cron schedule | `install.sh` (between managed markers) | rewritten on install; other entries preserved |
| Routing, `mvb:*` routes, prompts, preconditions | `hermes_agent/ops/claude-switcher/claude_switcher.py` | `hermes-update.py` applies it to the gateway |
| Hermes persona | `hermes_agent/SOUL.md` | `hermes-update.py` → `~/.hermes/SOUL.md` |
| Vendored gateway patches | `hermes_agent/ops/*/apply-*-patch.py` | re-applied daily after `hermes update` |
| Model router | `hermes_agent/ops/model-router/` | copied to `~/.hermes/model-router/` |
| Claude Code permissions for autonomous runs | `marketing_vb/.claude/settings.json` | read directly by the SDK |
| Agents, skills, commands | `marketing_vb/.claude/`, `claude_code/DEV/marketing_vb/plugins/` | read directly |
| Brand assets, content strategy | `marketing_vb/brand-assets/` | read directly |

### Why units are copied and not symlinked

A symlink into a git repo means a `git checkout` of a branch without that file
pulls the unit out from under a running service. The copy is the safer half of the
trade; the cost is that `install.sh` is the only correct way to deploy a unit
change.

## The permission model, which is easy to get wrong

The conductor opens SDK sessions with `settingSources: ['project']`. That loads
`.claude/settings.json` **and nothing else**. `settings.local.json` is a separate
source it does not pass.

So: allow rules for autonomous runs must live in `settings.json`. Rules in
`settings.local.json` apply only to your interactive sessions. With
`permissionMode: 'acceptEdits'`, only file edits are auto-approved — everything
else without a matching allow rule becomes a permission prompt that a headless run
cannot answer, which is a silent deny.

Keep the allow list narrow. `guard.py` (the PreToolUse hook) can only pattern-match
a command string, so a blanket `Bash(python3:*)` would let `python3 -c "..."` past
every rule it has. Name specific scripts instead, in both bare and `./`-prefixed
form — a blocked path variant fails the same silent way.

## MCP

There are **no MCP servers declared in files in this repo**, and none in
`~/.hermes/config.yaml`. The connectors Claude Code uses (Google Drive, Atlassian,
Slack and so on) come from the **claude.ai account**, not from project
configuration, so they follow the login rather than the machine.

Practical consequence, observed: Hermes itself has no Google OAuth. Asked to read a
private Google Doc, it correctly delegates to Claude Code under the `marketing_vb`
profile, which does have the Drive connector. If Drive access breaks, check the
account's connectors, not this repository.

## Profiles

Claude Code hosts several mutually exclusive systems, one active at a time — too
many agents and skills dilute selection and context. Manifests live in
`claude_code/DEV/profiles/`: `dev`, `marketing`, `marketing_vb`, `marketing_vb_sm`,
`sandbox_sm`, `security`, `seo`.

Marketing pipelines run under `marketing_vb_sm`. You do not switch by hand for
those — `mvb-run.py` sets the profile per job, and a profile with `runFrom` in its
manifest overrides the enqueued `work_dir`.

## Secrets

`secrets.env.example` is the contract: every key that exists, with an empty value
and a note on what breaks without it. Some are hard requirements
(`TELEGRAM_BOT_TOKEN`, `TELEGRAM_ALLOWED_USERS`); others degrade rather than break
— without `AHREFS_API_KEY` the SEO planner marks keyword volume `TBD` instead of
inventing figures, which is the correct behaviour, just less useful.

`verify.sh` checks that the real file is mode 600 and that no secrets file is
tracked in git.
