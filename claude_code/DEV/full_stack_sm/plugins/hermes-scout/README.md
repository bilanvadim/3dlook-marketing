# hermes-scout

Ecosystem intelligence for Fullstack agents — two agents:
- **trend-scout** — daily scanner of the Claude Code ecosystem (new agents/skills/plugins/MCP), scored, security-gated, reported. **Never installs anything.**
- **solution-evaluator** — on-demand evaluator of ONE specific solution you point at.

## `/sm-evaluate <url | repo | plugin/skill/MCP/package name>`
Hand it a GitHub repo, a plugin/skill/MCP/npm name, a library, or just a URL. The evaluator:
1. resolves & studies the solution (reads the source, not just the pitch);
2. **researches real developer feedback online** (HN, Reddit, dev.to, GitHub issues, comparison posts) — pros AND cons;
3. runs a security gate;
4. checks fit against our stack & incumbents (`CLAUDE.md`/`FULLSTACK-AGENTS.md` + `plugins/hermes-*`);
5. gives a decisive verdict — **REPLACE `<incumbent>` / ADD / TRIAL / SKIP**;
6. drafts a concrete integration plan (proposes only — never modifies the system);
7. saves the full report to `.claude/scratchpad/evaluate/<slug>-YYYY-MM-DD.md` and prints a short verdict.

Examples: `/sm-evaluate better-auth`, `/sm-evaluate https://github.com/org/repo`, `/sm-evaluate some-mcp-server`.

---

## trend-scout (daily scan)

## Run modes
1. Manual: in Claude Code → `use the trend-scout agent to run today's scan`
2. Scheduled (your n8n/cron): `claude -p "Run trend-scout daily scan per the trend-scan skill" --permission-mode acceptEdits`
   Add `GITHUB_TOKEN` env for sane rate limits. Pipe the digest to your Telegram bot from n8n.

## State
- Lightweight: agent memory (`seen.md`) — works out of the box.
- Full: apply `sql/schema.sql` to Postgres → velocity is computed across runs (stars/installs deltas), digests archived.

## Honest limitations (read this)
- X/Twitter: no free API; trends from X are caught indirectly (HN/Reddit reposts) with 1-3 days lag.
- TikTok: intentionally excluded — no API, signal density too low for dev tooling.
- Reddit API requires OAuth; fallback is WebSearch site:reddit.com (good enough for weekly tops).
- Install counts exist ONLY for the official plugin directory; everything else is stars-proxy.
- Velocity needs ≥2 runs to compute. Day 1 digest will be cold-start (absolute numbers only).
