# page-builder — upstream copy, unmodified

Pristine download of Victor Shulga's public `page-builder` skill, kept for diffing when upstream
changes. **Not a live skill** — it sits outside `.claude/skills/`, so Claude Code does not load it.

- Source page: https://victorshulga.com/skills/outbound-agents/page-builder/
- Archive: https://victorshulga.com/skills/downloads/page-builder.zip (35 KB)
- GitHub: https://github.com/victor-shulga/page-builder/tree/main/skills/page-builder
- Installer offered upstream: `npx skills add victor-shulga/page-builder/skills/page-builder`
- Downloaded: 2026-08-23

The live, 3DLOOK-adapted version is `.claude/skills/page-builder/`. It is a rewrite, not a patch:
the Service Page Kit became a vertical/use-case Kit, the Blog Kit was dropped and routed to
`/new-article`, and the gates gained 3DLOOK claims discipline. Diff against this folder before
pulling any upstream update, and never overwrite the live copy with it.
