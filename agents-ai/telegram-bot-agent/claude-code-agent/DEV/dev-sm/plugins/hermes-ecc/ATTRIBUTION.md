# Attribution — ECC (everything-claude-code)

The following components were adopted (copied, with minor local edits) from the
**ECC — everything-claude-code** project by **Affaan Mustafa**, MIT-licensed.

- Source: https://github.com/affaan-m/everything-claude-code  (https://ecc.tools)
- Commit: `49128b5763b7ac0b50acef35ac0bcca08d1576af`
- License: MIT (see full text below)

## Adopted into this plugin (`hermes-ecc`, dev profile)
| File | ECC source | Local edits |
|---|---|---|
| `agents/silent-failure-hunter.md` | `agents/silent-failure-hunter.md` | `model: sonnet → opus` (our tiering) |
| `agents/react-reviewer.md` | `agents/react-reviewer.md` | `model: sonnet → opus` |
| `agents/typescript-reviewer.md` | `agents/typescript-reviewer.md` | `model: sonnet → opus` |
| `agents/performance-optimizer.md` | `agents/performance-optimizer.md` | `model: sonnet → opus`; **tools → read-only** (removed Write/Edit) so it advises/proposes patches rather than applying them — TRIAL gate |
| `agents/refactor-cleaner.md` | `agents/refactor-cleaner.md` | `model: sonnet → opus`; **tools → read-only** (removed Write/Edit); rewritten to ADVISORY — added a hard "advisory mode" rule and changed the "remove/commit" steps to "propose a removal plan", so it never deletes/commits itself — TRIAL gate |
| `agents/database-reviewer.md` | `agents/database-reviewer.md` | `model: sonnet → opus`; **tools → read-only** (removed Write/Edit; Bash kept for EXPLAIN/read only); added "advisory mode" rule — reviews + recommends migrations, never applies DDL/DML — TRIAL gate |
| `agents/type-design-analyzer.md` | `agents/type-design-analyzer.md` | `model: sonnet → opus` (already read-only) |
| `skills/context-budget/SKILL.md` | `skills/context-budget/SKILL.md` | none |
| `skills/codebase-onboarding/SKILL.md` | `skills/codebase-onboarding/SKILL.md` | none |

Each was vetted before adoption via `agents-ai/telegram-bot-agent/hermes-agent/ops/skill-guard` (deterministic
content scan) + manual review; the scanner's flags on these files were confirmed
false positives (descriptive text naming attack/secret patterns, not payloads).

---

## MIT License

Copyright (c) 2026 Affaan Mustafa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
