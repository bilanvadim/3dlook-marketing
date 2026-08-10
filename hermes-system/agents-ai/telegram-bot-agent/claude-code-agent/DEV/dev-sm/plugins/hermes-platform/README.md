# hermes-platform
MCP — add only what matches your infra, per-project:
- Cloudflare (exemplary token design: search()/execute() over 2500+ endpoints) — Workers/R2/D1/CDN/rate-limiting/LB
- Vercel MCP — deploys, build & runtime logs
- awslabs/mcp (API + Knowledge servers) — ONLY with scoped-down IAM
Requires: gh CLI authenticated (gh auth login).
