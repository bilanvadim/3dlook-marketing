# Conductor patches (live tree is Sergiy's repo)

The conductor that actually runs is `/srv/vadim_prod/ai-agents-config/agents-ai/telegram-bot-agent/claude-code-agent/DEV/dev/conductor` — a checkout of `SergeMiro/ai-agents-config`. Edits there are **local modifications on `main`**, the same way the other 30-odd local edits in that checkout are. A `git pull` (or `update.sh`) can therefore revert them, and nothing in this repo would know.

So every conductor fix made for Vadim's stack is also saved here as a patch. This directory is the recovery path, not the source of truth: the source of truth is the live tree.

## Re-apply after an update wiped them

```bash
cd /srv/vadim_prod/ai-agents-config
for p in ~/3dlook-marketing/hermes_agent/ops/conductor-patches/*.patch; do
  git apply --check "$p" && git apply "$p" && echo "applied $(basename "$p")"
done
cd agents-ai/telegram-bot-agent/claude-code-agent/DEV/dev/conductor && npx tsc --noEmit && npm test
systemctl --user restart hermes-conductor.service
```

`git apply --check` failing means upstream changed the same lines — read the patch and port it by hand rather than forcing it.

## The patches

### `0001-marketing-off-the-dev-step-loop.patch` (2026-08-17)

Two changes, one cause — job 88 (social posts for `mobile-body-scanning-patient-engagement`) reported `done — all 2 steps done` having written no posts at all:

1. **`conductor.ts` — step mode is for software profiles only** (`HO_STEP_PROFILES`, default `dev,security`). The step loop never passes the job's prompt to the executor (it says "implement step N from `.claude/scratchpad/*/plan.md`") and gates on `npx ultracite lint` / `npm run typecheck` / `npm test`. In a content repo that scores 0 forever: 3 attempts per step → `blocked` → a Telegram escalation whose Approve means "skip the step" → a `done` job with nothing in it. Jobs on other profiles now ignore any `ho_steps` rows and run their prompt as one run, with a loud log line.
2. **`profiles.ts` — a bound profile's `runFrom` wins over the enqueued `work_dir`** (`resolveWorkDir`). `marketing_vb` / `marketing_vb_sm` agents read `CLAUDE.md`, `brand-assets/` and `workspace/` by relative path; job 88 was enqueued with `work_dir` at the repo root, one level above them, where those reads resolve to nothing and no error is raised anywhere.

Prevention lives on the enqueue side too: `hermes_agent/ops/mvb-run.py` is now the only sanctioned way for Hermes to start a marketing pipeline, and it never writes `ho_steps`.
