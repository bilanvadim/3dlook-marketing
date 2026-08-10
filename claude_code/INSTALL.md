# Claude Code Agent — install on a fresh VPS

Everything Claude Code needs: the 4 systems (Dev/SEO/Marketing/Security) + the
experimental **test** system, MCP servers, skills, and settings. The bot's Claude
runs happen inside `~/.claude`; this folder is the versioned source for it.

## 0. Prereqs
- Node.js + `npx` (for the MCP servers and Claude Code).
- Claude Code CLI: `sudo npm i -g @anthropic-ai/claude-code` (the crontab also keeps it updated: `0 4 * * * npm update -g @anthropic-ai/claude-code`).

## 1. Settings + MCP
```bash
# user settings (model, plugins, marketplaces) — edit YOUR_USER paths first
cp config/settings.json.example        ~/.claude/settings.json
cp config/settings.local.json.example  ~/.claude/settings.local.json
# project MCP (8 servers) + user MCP (magic, context7) — fill token placeholders
cp config/project-mcp.json.example     ~/.mcp.json
#   merge config/user-mcp.json.example → ~/.claude.json "mcpServers", or:
claude mcp add magic    -s user -- npx -y @21st-dev/magic@latest        # then set API_KEY
claude mcp add context7 -s user -- npx -y @upstash/context7-mcp@latest
printf 'full_stack_sm\n' > ~/.claude/.active-profile
```
Secrets referenced by env keys (not in git): `GITHUB_PERSONAL_ACCESS_TOKEN`,
`POSTGRES_CONNECTION_STRING`, magic `API_KEY` — export them or put them in the MCP `env` blocks.

## 2. codebase-memory MCP binary (shared base, once per machine)
```bash
curl -fsSL https://raw.githubusercontent.com/DeusData/codebase-memory-mcp/main/install.sh | bash -s -- --skip-config
codebase-memory-mcp config set auto_index true
codebase-memory-mcp config set auto_watch false
```
> ⚠️ Always pass `--skip-config` — a bare `install` overwrites the pre-tool hooks/instructions.

## 3. Systems / plugins (the switcher IS the installer)
`DEV/switch-profile.sh <system>` registers each marketplace and installs its plugins,
then rewrites `~/.claude/settings.json → enabledPlugins` and `~/.claude/.active-profile`.
```bash
DEV/switch-profile.sh full_stack_sm        # default — 11 hermes-* plugins + codebase-memory
# others: seo | marketing | security | test    (one active at a time; restart Claude Code after)
```
Profiles live in `DEV/profiles/*.json`. Headless dispatch under a profile:
`DEV/dispatch-in-profile.sh <profile> -- claude -p '<task>' --workdir <proj>`.

## Systems
| Profile | Marketplace(s) | Entry |
|---|---|---|
| `dev` | full_stack_sm (11 hermes-*) | `/sm-feature` `/sm-verify` `/sm-docs` |
| `seo` | dev base + seo_sm | `/seo-audit` |
| `marketing` | dev base + marketing_sm | `/mkt-campaign` |
| `security` | dev base + security_sm | agents · `/sm-verify` |
| `test` | dev base + marketing_sm + marketing_vb + marketing_vb_sm | `/vbsm-campaign` |

## Hooks & permission baseline
`DEV/full_stack_sm/.claude/settings.json` defines the project permission baseline
(allow safe read/build/test/git; ask for deploy/force-push/db push; deny reading
secrets + `rm -rf`) and wires the hooks (`guard.py`, `autocommit.py`,
`clear-counter.py`, `session-handoff.py`). Copy `DEV/full_stack_sm/.claude/` into each
working project so those apply there.
