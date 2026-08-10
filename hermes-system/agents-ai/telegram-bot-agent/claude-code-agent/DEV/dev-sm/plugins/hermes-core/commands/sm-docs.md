---
description: Generate/update project documentation (README, CHANGELOG, runbook) from repo state and scratchpad
---
Generate or update documentation for this project. Read .claude/scratchpad/*/decisions.log and recent git history (Bash: git log --oneline -30). Be concise and factual, no marketing language. Update: README.md (if stale), CHANGELOG.md (from commits since last entry), docs/runbook.md (if infra changed). Never document features that do not exist in code.
