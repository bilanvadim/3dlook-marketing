# config/ — one repo, two runtimes

This repo is the single source of truth for two isolated Linux users on one VPS
(`sergiy_prod`, `vadim_prod`). It holds **one** Claude Code config and **one** Hermes
config; everything that must differ between the two lives here, in a profile.

## The model: clean clone → render

```
git clone <repo>  →  scripts/render.sh <profile>  →  a user's runtime tree
```

A checkout of this repo is a **template**, not a runtime. It carries the author's absolute
paths, and `scripts/render.sh` substitutes the values from `config/profiles/<profile>.vars`
to produce one user's tree — the tree Claude Code loads plugin marketplaces and profiles
from, by absolute path.

Rendering is a separate, re-runnable step on purpose: `git pull` overwrites tracked files
with the author's paths again, and nothing else puts the user's values back. Under this model
those local modifications are **disposable** — an update discards them, pulls, and re-renders.

`render.sh` is idempotent and `--check` reports what would change without touching anything,
so update/doctor can tell a **missed render** apart from **real drift**.

### What render.sh does NOT do

It does not touch the identity tokens `@OWNER@` / `@GH_OWNER@` / `@PROJECT_ROOT@`. Those are
substituted where they belong — when a repo template is deployed into `~/.hermes`, by
`install.sh` and then by `hermes-update.py`'s `_render_identity()` on every update, reading
`HERMES_OWNER` / `HERMES_GH_OWNER` / `HERMES_PROJECT_ROOT` from `~/.hermes/.env`.

Duplicating that here would be two owners for one decision, and it would break things:
`hermes-update.py` contains `("@OWNER@", "HERMES_OWNER")` as *code*, so a blind tree-wide
substitution rewrites the renderer's own token table and every later update with it. It also
leaves `*.example` files alone for the same reason.

## What belongs in a profile

Only values that must differ per user, and only non-secret ones:

- identity: user, home, destination tree, owner display name, GitHub account, project root
- **ports** — the main reason profiles exist. Both runtimes share one loopback, so every
  port is bound for real and a shared value means the second service to start silently
  loses. That is exactly how the conductor's escalation webhook lost every Approve/Deny
  tap while both users defaulted to `3001`.
- conductor state path — runtime state belongs in `~/.hermes`, not inside a project
  checkout, because a project repo gets cloned, moved and cleaned, and the queue history
  must not travel with it.

## What must NEVER be here

Secrets. Not one. They live in `~/.config/ai-agent-stack/secrets.env` (0600, outside git):
API keys, Telegram bot tokens, MTProto credentials, GitHub PATs. Each user's set is
entirely their own — separate Telegram bots, separate provider keys, separate memory
stores. Nothing is ever copied between the two accounts.

## Adding a user

1. `config/profiles/<user>.vars` — copy an existing one, change every value; ports must
   not collide with any profile already present.
2. `git clone` the repo to their `/srv/<user>/ai-agents-config`, as that user.
3. `scripts/render.sh <user>`.
4. Their own `~/.config/ai-agent-stack/secrets.env`, filled by them.
5. `install.sh` for the runtime pieces (services, deps, unit files).
