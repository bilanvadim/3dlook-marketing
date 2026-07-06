# marketing_vb — Vadim's marketing system as switchable plugins

This marketplace (`ai-agents-mvb`) packages Vadim's original 3DLOOK
marketing-automation system into Claude Code plugins so it can be activated
uniformly through `switch-profile.sh` alongside the other systems.

**The source of truth is untouched** — the pristine project lives at the repo
root under [`/marketing_vb`](../../../marketing_vb) (agents, commands,
`brand-assets/`, `workspace/`, `about-me.md`, `audience.md`, docs). The agents
and commands here are copies of that project's `.claude/` wrapped as plugins;
edit the originals and re-sync if the source changes.

## Plugins

| Plugin | Agents / commands |
|---|---|
| `mvb-core` | orchestrator, brand-checker, quality-controller, context-pack-builder, agent-improver + commands `/new-article` `/weekly-posts` `/outbound` `/post-from-article` `/qc` `/quarterly-review` `/improve-agents` |
| `mvb-social` | post-drafter, quarterly-strategist, social-analytics, visual-brief |
| `mvb-seo` | seo-planner, seo-writer, seo-editor, seo-publisher |
| `mvb-outbound` | hypothesis-generator, icp-validator, company-researcher, people-extractor, message-sequencer, closelyhq-importer, campaign-analyzer, response-classifier |

## Working directory / brand context

These agents read brand context by **relative path** (`brand-assets/`,
`workspace/`, `about-me.md`, `audience.md`) exactly as in the original
project. Run Claude Code from a working directory that contains those assets —
the simplest option is to work inside `/marketing_vb` (or a copy of its
`brand-assets/` + `workspace/`). The plugins provide the *agents and commands*;
the *content/context* comes from your working project.

## Activate

```bash
claude_code/DEV/switch-profile.sh marketing_vb   # then restart Claude Code
```

This profile is **pure** (no Hermes base). For Vadim's brand workflow blended
with Sergiy's strategy/content/paid/lifecycle/analytics specialists, use the
`marketing_vb_sm` profile instead.
