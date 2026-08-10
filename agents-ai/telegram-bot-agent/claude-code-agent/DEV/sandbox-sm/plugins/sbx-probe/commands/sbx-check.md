---
description: Confirm the sandbox profile really loaded, then walk the trial checklist for the candidate under test
---
You are running inside the **sandbox-sm** profile. Report the facts first, then help
run the trial. Be terse — this is instrumentation, not a report.

**1. Prove what loaded** (do not trust the manifest, read the live state):

- `cat ~/.claude/.active-profile` — what the switcher recorded.
- `python3 -c "import json;print(list(json.load(open('$HOME/.claude/settings.json'))['enabledPlugins']))"`
  — what settings.json actually enables.
- List the plugin commands and agents visible to you in THIS session.

If the session's plugins do not match `.active-profile`, say so plainly: Claude Code
was not restarted after the switch, and any conclusion about the candidate is void.

**2. Identify the candidate.** Everything beyond `hermes-core` and `sbx-probe` is the
thing under trial. Name it and where it came from
(`DEV/sandbox-sm/plugins/`, an external marketplace, or an MCP server).

**3. Run the trial.** Ask for the task to try, then run it and record, in
`.claude/scratchpad/sandbox/<candidate>.md`:

- **Did it get selected?** A skill/agent that never triggers on a task it claims to
  cover is a failure, however good its content is.
- **Did it work?** Evidence, not its own word — a command output, a diff, a test.
- **What does it cost?** New always-loaded skills/tools are paid in every turn.
  Note the size of what it adds.
- **What does it duplicate?** Name the plugin or skill already in `dev-sm` that
  covers the same ground.
- **Risk:** does it run third-party code, reach the network, or touch secrets?

**4. Verdict:** adopt (say into which system) / keep trialling / drop. Nothing gets
promoted out of the sandbox without a task it demonstrably did better than the
current setup.
