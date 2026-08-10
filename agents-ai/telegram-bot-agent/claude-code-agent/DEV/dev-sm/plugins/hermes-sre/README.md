# hermes-sre
MCP companions (add per-project):
- Sentry MCP (official, OAuth, includes Seer root-cause AI): claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
- Grafana MCP if you run Grafana Cloud (also proxies Datadog/Honeycomb/New Relic connections)
- Redis MCP (official redis/mcp-redis) or your Valkey endpoint for cache inspection
