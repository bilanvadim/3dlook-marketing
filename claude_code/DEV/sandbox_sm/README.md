# sandbox_sm — trial bench for one candidate at a time

A candidate (plugin, skill, agent, MCP server) installed straight into `full_stack_sm`
cannot be judged: 11 plugins are already competing for selection, so "it did
nothing" is indistinguishable from "it never got picked", and a bad candidate
pollutes real work. This profile is the isolation ward — **`hermes-core` +
`sbx-probe` and nothing else**, so whatever else answers is the candidate.

## Trial loop

```bash
cd /home/vadim_prod/3dlook-marketing/claude_code/DEV

# 1. put the candidate here (or point at its own marketplace — see below)
cp -r /path/to/candidate-plugin sandbox_sm/plugins/<name>

# 2. list it in sandbox_sm/.claude-plugin/marketplace.json  →  plugins[]
# 3. add "<name>@sandbox_sm" to profiles/sandbox_sm.json    →  enabledPlugins[]

./switch-profile.sh sandbox_sm     # registers, installs, rewrites settings.json
# 4. RESTART Claude Code — plugins load only at session start
/sbx-check                         # proves what loaded, then runs the checklist
```

Back to real work: `./switch-profile.sh full_stack_sm-sm` + restart. The candidate stays
here, disabled, until you promote or delete it.

**External marketplace instead of a copy:** add it to `marketplaces` in
`profiles/sandbox_sm.json` and reference the plugin as `<plugin>@<marketplace>`.
The switcher registers it on switch. Prefer this for anything you may want to
`git pull` later; prefer copying for anything you intend to edit.

## Rules that make the sandbox worth having

- **One candidate at a time.** Two candidates and you are back to guessing which
  one acted.
- **Restart, always.** `switch-profile.sh` only rewrites `settings.json`; a
  running session keeps the plugins it started with. `/sbx-check` catches this.
- **Verdict needs a task.** Nothing is promoted because it looks good — it is
  promoted because it did a real task better than the current setup did.
- **Cost is part of the verdict.** Skills and tools that load unconditionally are
  paid in every single turn, forever. Cheap-looking additions are how a prompt
  goes from lean to bloated.
- **Third-party code is not trusted by default.** Read what it runs before the
  first trial: hooks, `postinstall`, network calls, anything reading `.env`. This
  VPS is shared with Vadim and holds live project secrets.

## Not in the routing table — on purpose

`route-profile.sh` maps task intent → `full_stack_sm|seo_sm|marketing_sm|security_sm`,
and the conductor's `ho_jobs.profile` CHECK does not accept `sandbox_sm`. So no
autonomous job and no Hermes routing decision can ever land in an unvetted
profile. Entering the sandbox is a manual act. Keep it that way.
