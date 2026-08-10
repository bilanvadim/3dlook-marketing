# OpenCode as batch step executor (when Claude is limited)

When Claude hits its usage limit and you have a multi-step plan to execute
(scratchpad with step1..stepN), run OpenCode as a sequential batch executor.

## Pattern (per step)

1. **Write prompt to temp file** — avoids shell escaping issues:
   ```
   cat > /tmp/prompts/<project>-stepN.txt << 'EOF'
   Execute Step N from scratchpad/.../plan.md.
   ...specific instructions...
   After completion: handoff, decisions.log, plan.md status.
   Do NOT redesign. Follow existing patterns exactly.
   EOF
   ```

2. **Run OpenCode** with the prompt via `$(cat ...)`:
   ```
   opencode run -m "opencode-go/$MODEL" "$(cat /tmp/prompts/stepN.txt)"
   ```
   `$MODEL` from today's pick.json: `python3 -c "import json;print(json.load(open('$HOME/.hermes/model-router/pick.json'))['go'])"`

3. **OpenCode self-debugs**: reads code → writes → runs tests → fixes failures → re-runs.
   Expect 2-3 iterations. Let it run — do NOT interrupt.

4. **Timeout (exit 124) is NORMAL.** Code is usually complete. Check:
   ```bash
   git diff --stat              # files created/modified
   ls scratchpad/*/handoff/     # handoff written?
   tail -1 decisions.log        # log appended?
   grep "status: done" plan.md  # status updated?
   ```

5. **Manually finish ceremony** for anything missed:
   - Write missing handoff: `write_file(path="handoff/0N-module.md", ...)`
   - Append decisions.log: `patch(path="decisions.log", ...)`
   - Mark plan step done: use `patch` with enough context to match the exact `- status: pending` line

6. **Commit and continue**: `git add -A && git commit -m "Step N done: <title>"`

## Observations

- 600s timeout is the main constraint — complex steps (scheduler, agent) hit it
- Self-correcting: OpenCode reads test output, fixes bugs, re-runs iteratively
- Works best with well-scoped, single-step prompts (NOT "steps 4-7 at once")
- Full path: `~/.opencode/bin/opencode` (not on PATH)

## Example: way2buy-miniapp (Steps 3-7, July 2026)

Claude hit weekly limit (resets 11am UTC). Ran 5 backend steps through OpenCode:
Step 3 (loyalty, 36 tests), Step 4 (campaigns, 52 tests), Step 5 (notifications, 20 tests),
Step 6 (scheduler, 11/12 tests — timed out, ceremony done manually),
Step 7 (AI agent, 26 tests). Each step committed separately.
Total: ~5 steps in ~40 minutes, all tests green (except 3 pre-existing loyalty + 1 scheduler mock).
