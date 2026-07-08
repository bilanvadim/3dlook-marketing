# Attribution — ECC (everything-claude-code)

The following components were adopted (copied, with minor local edits) from the
**ECC — everything-claude-code** project by **Affaan Mustafa**, MIT-licensed.

- Source: https://github.com/affaan-m/everything-claude-code  (https://ecc.tools)
- Commit: `49128b5763b7ac0b50acef35ac0bcca08d1576af`
- License: MIT (see full text below)

## Adopted into this plugin (`sec-core`, security profile)
| File | ECC source | Local edits |
|---|---|---|
| `skills/security-bounty-hunter/SKILL.md` | `skills/security-bounty-hunter/SKILL.md` | none |
| `agents/silent-failure-hunter.md` | `agents/silent-failure-hunter.md` | `model: sonnet → opus` (our tiering) |

Vetted before adoption via `hermes_agent/ops/skill-guard` + manual review;
scanner flags confirmed false positives (descriptive text naming attack patterns,
e.g. "data exfiltration" in a consequences table — not payloads).

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
