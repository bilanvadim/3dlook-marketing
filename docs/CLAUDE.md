# Claude Code — the interactive half

Entry point for the Claude Code side of the platform. Per-component detail lives beside the
component; this is the map and the parts that only make sense at platform level.

- [`agents-ai/telegram-bot-agent/claude-code-agent/README.md`](../agents-ai/telegram-bot-agent/claude-code-agent/README.md) — the component itself
- [`.../DEV/SYSTEMS.md`](../agents-ai/telegram-bot-agent/claude-code-agent/DEV/SYSTEMS.md) — what each system is for
- [`.../DEV/dev/conductor/{ARCHITECTURE,RUNBOOK}.md`](../agents-ai/telegram-bot-agent/claude-code-agent/DEV/dev/conductor/) — the autonomous worker

## Systems are plugin marketplaces, selected by a profile

A "system" (dev, seo, marketing, security, sandbox, test) is a **marketplace directory** of
plugins, chosen by `DEV/profiles/<system>.json`:

```json
{ "name": "dev",
  "marketplaces": { "dev": "@DEST@/agents-ai/.../DEV/dev" },
  "enabledPlugins": ["hermes-core@dev", "hermes-design@dev", …] }
```

Two consequences that generate most of the platform's rules:

**The path is absolute**, so the tree must be rendered. `@DEST@` is a template token; an
unrendered tree makes Claude Code resolve a literal `@DEST@/…` and the profile loads **nothing**.
`render.sh` substitutes it, `doctor.sh` checks the result, and CI proves both profiles render with
no token surviving. See [`../ARCHITECTURE.md`](../ARCHITECTURE.md).

**The path names an account.** A profile JSON carrying the other user's path silently loads the
other user's plugins — which is why no absolute path may name any account in the template, and why
`validate.sh` fails the build if one appears.

Today: 11 plugins in the `dev` marketplace, 19 agent definitions, 7 skills, 8 MCP servers.

## What is shared and what is not

| | |
|---|---|
| Shared (from this repo) | systems, plugins, agents, skills, `CLAUDE.md`, settings baseline, hooks |
| Per-user | `~/.claude/` (auth, history, sessions), `~/.claude.json`, MCP credentials |

`~/.claude` is **never** copied between accounts. It holds the login, the conversation history and
session state; a copy hands one person's authenticated session to another. This is not a
theoretical rule — see [`../SECRETS.md`](../SECRETS.md).

## Autonomous runs (the conductor)

Jobs arrive in `~/.hermes/ho.db`; the conductor claims one, resolves the profile to plugin
directories, and opens a Claude Agent SDK session with `cwd = work_dir`.

Two things worth knowing before trusting an autonomous run:

**Permission mode is `acceptEdits`, deliberately not `bypassPermissions`.** Bypassing skips the
work directory's own `permissions.deny` rules *and* its `PreToolUse` hooks — exactly where the
protection lives — leaving a sentence in a prompt as the only guard. Read-only web tools are
pre-approved via `allowedTools` because headless auto-denies them.

**Settings come from the work directory**, not from the system's own `.claude/`. The SDK opens
sessions with `settingSources: ['project']` and `cwd = work_dir`, so a job whose work_dir has no
`.claude/settings.json` runs with no deny list and no guard hook at all. Every work directory a
conductor job targets needs its own.

Before each run the conductor writes `refs/hermes/snapshots/job-<id>` — a real commit of the work
tree, made without touching HEAD, the branch, the index or the working tree. It exists because
autocommit skips main/master and these repos work on main, so an autonomous run otherwise has no
rollback point. Recover with `git show refs/hermes/snapshots/job-42:path/to/file`.

## What a job can and cannot reach

Two limits shape every job prompt, and both were learned by writing prompts that ignored them.

**A job sees only its `work_dir`.** The session's filesystem sandbox is the working directory, not
the permission list. A security audit pointed at
`.../DEV/dev/conductor/src` got four refusals — `ls`, `find`, `grep` and `Read` all answered *"may
only search files in the allowed working directories"* — and correctly produced a report saying it
had audited nothing rather than inventing findings. Code to be audited must be **staged inside** the
work_dir (a read-only copy works well: `chmod -R a-w`), or the work_dir must be the tree itself.

**The baseline allows no fetch command.** There is no `curl`/`wget` rule in it, deliberately. The
pre-approved path is `WebFetch` (the conductor adds it via `allowedTools` because headless
auto-denies read-only web tools), and it returns **markdown**, stripping `<head>`. So titles, meta
descriptions, canonicals, `hreflang`, Open Graph and JSON-LD are unreadable by default — an SEO audit
run this way can verify `robots.txt`, the sitemap, headings and body links, and must declare the
`<head>` unchecked. If a job genuinely needs raw HTML or response headers, add a narrow rule to
**that** work_dir's `settings.json` on purpose; do not widen the shared baseline, where `curl` also
means a POST that can carry data off the box.

Related: a compound command is split and each part matched separately, so
`cd /tmp && curl …` needs approval for `cd` as well — and in a headless run approval is refusal. A
job already runs in its work_dir; prompts should not ask it to `cd` elsewhere.

## Switching systems

Hermes's switcher maps a Telegram thread to a system and a session id
(`~/.hermes/claude-switcher-state.json`), so a thread resumes where it stopped. The keys are system
names — after a rename, stale keys orphan a session and the switcher silently starts a fresh one
instead of resuming.

## Checks that apply here

```bash
./scripts/doctor.sh      # among other things: is the tree rendered, do the marketplaces resolve
./scripts/validate.sh    # no account-specific path in the template; JSON parses; tokens present
```
