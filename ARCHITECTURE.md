# Architecture

One repository. Two isolated Linux accounts on one VPS. One Claude Code configuration, one
Hermes configuration, two profiles, two secret sets, two Telegram bots, two runtimes, one update
mechanism, one version.

```
                        github.com/SergeMiro/ai-agents-config          ← single source of truth
                                        │
                        ┌───────────────┴───────────────┐
                    git clone                       git clone (deploy key, read-only)
                        │                                │
        /srv/sergiy_prod/ai-agents-config    /srv/vadim_prod/ai-agents-config
                        │                                │
              render.sh sergiy_prod              render.sh vadim_prod
                        │                                │
        ┌───────────────┼───────────┐        ┌───────────┼───────────┐
   ~/.hermes      conductor    Claude Code   ~/.hermes  conductor  Claude Code
   (gateway,      (queue,      (plugins,     …          …          …
    mem0,          webhook,     profiles)
    qdrant)        snapshots)
```

## The four layers

**① Claude Code** — the interactive agent. Its systems (dev, seo, marketing, security, sandbox,
test) are plugin marketplaces loaded by **absolute path** out of the rendered tree, selected by
`DEV/profiles/<system>.json`. This is why the tree must be rendered: a profile JSON containing
another account's path silently loads another account's plugins.

**② Conductor** — the autonomous worker. Claims jobs from a SQLite/libSQL queue (`ho_jobs`),
opens a Claude Agent SDK session per job, feeds every event to a circuit breaker, and escalates
to Telegram when it needs a human. Durable resume: each run records its SDK `session_id`, so a
job paused by a rate limit or killed with its worker continues where it stopped, hours later.

**③ Hermes gateway** — the Telegram front end and manager. Owns the bot's single allowed
`getUpdates` consumer, routes messages, holds mem0 memory in a per-user Qdrant, and handles
`ho:*` escalation callbacks by writing the decision **straight into the conductor's database**.

**④ llm-failover-proxy** — two OpenAI-compatible chains (agentic, strong) on loopback, each
failing over across providers. Everything model-facing goes through these, so provider choice is
one config file rather than a setting in five places.

## What makes this two systems and not one

The accounts share a kernel, a filesystem and a loopback interface, and **nothing else**. No
credential, no memory store, no queue and no bot is shared. That isolation is enforced by
separate Unix accounts, `0600` secret files, per-profile ports, and one rule with no exceptions:
never copy a home directory or a config between accounts.

Everything that must differ lives in `config/profiles/<user>.vars`. In practice most of it is
**ports** — because both runtimes bind the same loopback, and a shared port does not produce an
error. The second binder simply loses, and its half of the system goes quiet. That is not
hypothetical: while both profiles defaulted to `3001` for the escalation webhook, one account's
Approve/Deny buttons did nothing at all for weeks.

## Template versus runtime

A checkout of this repo is a **template**, and it names nobody: paths appear as `@DEST@`,
`@HOME@` and `@USER@`, which `scripts/render.sh` substitutes from the profile to produce a runtime
tree. A tree that was never rendered is therefore obviously broken rather than subtly wrong — it
contains literal `@DEST@` paths — and rendering is symmetric: ~24 files for either profile. Rendering is a
separate, re-runnable step because `git pull` overwrites tracked files with the author's paths
again — under this model those local modifications are **disposable**, and `update.sh` discards,
pulls and re-renders.

`diff.sh` exists because of this: a deployed tree is never `git`-clean, so plain `git status`
there is unreadable. It re-renders the pristine blob from git and compares, which splits
modifications into **render** (expected) and **drift** (someone edited the runtime).

Identity tokens (`@OWNER@`, `@GH_OWNER@`, `@PROJECT_ROOT@`) are deliberately **not** render.sh's
job. They are substituted when a template is deployed into `~/.hermes`, by `install.sh` and then
by `hermes-update.py` on every update. Two owners for one decision would be bad enough; it is
also actively harmful, because `hermes-update.py` holds `("@OWNER@", "HERMES_OWNER")` as *code*
and a tree-wide substitution rewrites the renderer's own token table.

**Development is separate from every runtime.** Both `/srv/*/ai-agents-config` trees are
**consumer** replicas: read-only in practice, carrying no commits, updated only by `update.sh`.
Commits happen in a development checkout that nothing reads at run time —
`/srv/sergiy_prod/ai-agents-config-dev`, recorded as `PROFILE_DEV_TREE`.

This used to be one directory doing both jobs, and the cost was concrete: an editor and a
production system shared a path, so saving a half-finished edit made it the live config that
Claude Code and the conductor read on their next call. `update.sh --force` would also
`reset --hard` over real work rather than over regenerable render output.

The runtime path deliberately did **not** move — two systemd units and all six
`DEV/profiles/*.json` name it absolutely, so relocating it would be a migration with downtime for
no benefit. Only the place commits happen changed. A `pre-commit` hook installed by `deploy.sh`
refuses commits in a consumer tree and names the dev checkout instead (advisory: `--no-verify`
still works).

The dev checkout lives under `/srv`, not `~/workspaces`, because `repo-manager.sh` deletes a
workspace directory after 72 hours of inactivity.

The template used to carry the author's real paths instead of tokens, so rendering was a no-op for
one profile and a rewrite for the other: the "template" was one user's tree that happened to work
for him, and a copied `settings.json.example` handed out his repo path. `validate.sh` now enforces
the invariant in both directions — no absolute path may name any profile's account, **and** the
tokens must be present, since a tree that merely lost its paths would satisfy the first half while
rendering to a runtime with no paths at all.

The check is about **paths, not mentions**, and that distinction is load-bearing: prose sometimes
has to name the other account on purpose. `vps-maintenance/SKILL.md` says "do not kill processes
owned by other users (vadim_prod, root)" — tokenising that would render to "do not kill processes
owned by *yourself*", inverting the rule. Test fixtures are excluded for the same reason:
`signature.test.ts` asserts that six real 128-character paths share their first 80 characters,
which only holds for a fixed literal.

One consequence to know about: between `update.sh`'s `reset --hard` and its render, a live tree is
in template form and therefore **broken**, not merely stale. An `EXIT` trap re-renders on any exit
path until the render clears it, so a failed pull cannot leave it that way.

## State, and where it lives

| What | Where | In git? | Backed up by |
|---|---|---|---|
| Config, code, profiles | the rendered tree | yes (template) | git |
| Secrets | `~/.config/ai-agent-stack/secrets.env` (0600) | **never** | `backup.sh` |
| Live Hermes config | `~/.hermes/{config.yaml,.env,mem0.json,SOUL.md}` | no | `backup.sh` |
| Job queue + history | `~/.hermes/ho.db` | no | `backup.sh` (sqlite `.backup`) |
| Vector memory | per-user Qdrant | no | `backup.sh` (snapshot API) |
| Knowledge vault | `~/.hermes/AI-Second-Brain` | seed only | `backup.sh` (tar) |
| Unit files + **drop-ins** | `~/.config/systemd/user/`, `/etc/systemd/system/` | template only | `backup.sh` |

The **vault** is the clearest case of that rule being learned the hard way. It used to live inside
the config tree, i.e. inside a repo that `update.sh` resets and re-renders — so anything the agent
wrote there was one update away from being discarded. `vault-sync.sh` existed to paper over that by
committing and pushing *from a runtime replica*, and its `git pull --rebase --autostash` every 30
minutes is what left conflict markers in every `profiles/*.json` on one account. The repo copy is
now a pure **seed** (a schema, a README, empty directories); the live vault is runtime state in
`~/.hermes`, and `vault-sync` is retired.

Runtime state lives in `~/.hermes`, never inside a project checkout. A project repo gets cloned,
moved and cleaned; the queue history must not travel with it. One account had its queue inside a
project tree, which is how a unit and its database came to disagree.

The drop-ins matter as much as the units: that is where a deployment's real paths live
(`WorkingDirectory`, `CONDUCTOR_DIR`, `DATABASE_URL`). A backup without them restores a system
that points somewhere else.

## Failure modes this design assumes

The checks in `doctor.sh` are not a generic health list. Each one corresponds to a failure that
produced **no error message** on this box — both halves of the system working perfectly, on
different assumptions:

- the gateway and the conductor resolving **different** `ho.db` files
- a unit pointing at one tree while the live process runs from another (invisible until a
  restart, which then resolves it silently — possibly onto a tree that cannot start)
- a leftover unit file in the other systemd scope: enable it and two conductors claim one queue
- a port held by the other account
- a secret byte-identical to the other account's
- the pre-run snapshot not actually wired, so an autonomous run has no rollback point

If a problem announces itself in a log, it does not need a check there.

## Reading order

`config/README.md` (the profile model) → `INSTALL.md` → `UPDATE.md` → `SECRETS.md` →
`DISASTER-RECOVERY.md`.

Then the two halves in depth: [`docs/CLAUDE.md`](docs/CLAUDE.md) and
[`docs/HERMES.md`](docs/HERMES.md). Per-component detail lives next to the component, e.g.
`agents-ai/telegram-bot-agent/claude-code-agent/DEV/dev/conductor/{ARCHITECTURE,RUNBOOK}.md`.
