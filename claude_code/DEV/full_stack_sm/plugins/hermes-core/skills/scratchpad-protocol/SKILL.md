---
name: scratchpad-protocol
description: Fullstack agents inter-agent handoff protocol. Use whenever delegating work to a subagent, receiving results from a subagent, or coordinating multi-agent work on a feature. Ensures context survives between isolated agent context windows via structured files instead of lossy summaries.
---

# Scratchpad Protocol

Subagents cannot talk to each other and their return values are lossy summaries. All real context flows through files.

## Layout
```
.claude/scratchpad/<task-slug>/
├── spec.md            # from product-architect
├── architecture.md
├── plan.md            # task list with statuses
├── handoff/
│   ├── 01-design.md   # each agent writes its report here
│   ├── 02-frontend.md
│   └── ...
└── decisions.log      # append-only: DATE | AGENT | DECISION | WHY
```

## Rules for the orchestrator (main session)
1. Before delegating: ensure spec.md and plan.md exist. If not, run product-architect first.
2. In every Task prompt to a subagent include: (a) the scratchpad dir path, (b) the exact task number from plan.md, (c) instruction to write a structured report to `handoff/NN-<role>.md` before finishing.
3. After a subagent returns: read its handoff file, not just its summary. Update plan.md statuses.
4. Parallelize only tasks with no shared files and no dependency edges. Max 3-4 parallel for code-writing tasks (merge conflicts), up to 10 for read-only research.

## Rules for subagents (include in their Task prompts)
- Read spec.md + your task from plan.md first.
- Write your report to handoff/: what was done, files touched, decisions made (also append one line to decisions.log), open questions, what the next agent needs.
- Never overwrite another agent's handoff file.
