---
name: session-handoff
description: Save and restore working context ACROSS sessions / across /clear / across auto-compaction, so nothing is lost when the context window is reset. Two tiers — an automatic safety-net (a PreCompact/SessionEnd hook snapshots recent messages) and an on-demand structured handoff (/sm-handoff). Use before /clear, when wrapping up a session, or when the context is about to compact. Complements (does not replace) scratchpad-protocol.
---

# Session handoff — never lose context to /clear or compaction

`scratchpad-protocol` carries context **between agents within a feature**. This skill carries context **between sessions / across a context reset** (a `/clear`, an auto-compaction, or just opening a new session tomorrow). Two tiers:

## Tier 1 — automatic safety-net (no action needed)
A hook (`.claude/hooks/session-handoff.py`, wired on `PreCompact` + `SessionEnd`) snapshots the last ~20 messages to `.claude/scratchpad/_handoff/latest.md` *before* the context is compacted or the session ends. On the next `SessionStart` after a compact/clear/resume, the same hook injects that snapshot as `additionalContext`, so the new session picks up the thread. Mechanical and lossy-but-reliable — you can't forget it.

## Tier 2 — on-demand structured handoff (`/sm-handoff`)
When you deliberately hand off (before a planned `/clear`, end of a work block, switching machines), run `/sm-handoff`. The orchestrator writes a RICH, structured doc to `.claude/scratchpad/_handoff/latest.md` (overwriting the auto-snapshot with something better):

```
# Handoff — <feature/topic> — <when>
## Goal            — what we're ultimately trying to do
## Done            — what's finished & verified (with evidence/paths)
## Tried & rejected — approaches that failed + WHY (so they aren't retried)
## Key decisions   — chosen + the rejected alternative + rationale
## Next steps      — the concrete next 3-5 actions, in order
## Watch out       — traps, gotchas, fragile spots
## Files & state   — key paths, branch, what's committed/pushed, open scratchpads
```

Because Tier-1 restore reads the same `latest.md`, a `/sm-handoff` you wrote is what the next session sees first.

## Rules
- Handoffs live under `.claude/scratchpad/_handoff/` (gitignored, transient — not source of truth).
- The authoritative project state is still the feature scratchpad (`spec.md`/`plan.md`/`handoff/`) + the repo. A handoff is a *pointer + summary*, not the truth.
- The receiving session treats handoff claims as **context to verify against code**, not facts to trust blindly.
- Keep it tight: a handoff that's longer than scrolling the code it describes is useless.
