/**
 * Fullstack agents Conductor — SDK adapter that builds the per-step runner deps.
 *
 * ⚠️ INTEGRATION SEAM (not unit-tested; needs a live SDK + real project to validate).
 * The decision/orchestration logic it feeds (steploop.ts, steprunner.ts) IS tested.
 * Safe-by-default: any unparseable reviewer/runtime output → treated as fail/retry,
 * never a false "done".
 */
import { query } from '@anthropic-ai/claude-agent-sdk';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import {
  StepRecord, StepRunnerDeps, ExecutorResult, GateResult, ReviewResult, RuntimeResult,
} from './steprunner';
import { resolveProfilePlugins, LocalPlugin } from './profiles';

const sh = promisify(execFile);
const SYS =
  'You are the Fullstack-agents orchestrator (this project\'s CLAUDE.md). Work strictly on the ONE ' +
  'step described — do not touch other steps. Follow scratchpad-protocol, the verification-protocol, ' +
  'and the policy packs for the step tags. Never run production-affecting commands without an explicit ask.';

// Autonomous headless worker: no human is there to answer a permission prompt, so the step
// executor runs under 'acceptEdits' — NOT 'bypassPermissions'.
//
// bypassPermissions was the obvious choice and the wrong one: it skips the work_dir's own
// permissions.deny rules and its PreToolUse hooks, which is precisely where the protection now
// lives (a settings.json deny list plus guard.py in every work_dir a conductor job targets).
// Bypassing turned all of that off and left "never run prod-affecting commands" — a sentence in
// a prompt — as the only guard. acceptEdits keeps the deny rules and the hook, while still
// auto-approving the file edits an autonomous run has to make.
//
// allowedTools pre-approves the read-only web tools: under acceptEdits headless auto-DENIES
// them ("you haven't granted it yet"), which silently breaks every research flow. The option is
// ADDITIVE — it auto-allows only these and restricts nothing else. Applies to subagents too.
async function runQuery(prompt: string, workDir: string, plugins: LocalPlugin[], maxTurns = 150): Promise<{ text: string; ok: boolean }> {
  let text = '';
  let ok = false;
  const stream = query({
    prompt,
    options: {
      settingSources: ['project'], plugins,
      permissionMode: 'acceptEdits', allowedTools: ['WebSearch', 'WebFetch'],
      systemPrompt: SYS, cwd: workDir, maxTurns,
    } as any,
  });
  for await (const msg of stream as any) {
    if (msg?.type === 'assistant') {
      for (const b of msg?.message?.content ?? []) if (b?.type === 'text') text += `${b.text}\n`;
    } else if (msg?.type === 'result') {
      ok = msg?.subtype === 'success' || msg?.is_error === false;
      if (typeof msg?.result === 'string') text += msg.result;
    }
  }
  return { text, ok };
}

function extractJson(text: string): Record<string, unknown> | null {
  const fenced = text.match(/```json\s*([\s\S]*?)```/i);
  const raw = fenced ? fenced[1] : (text.match(/\{[\s\S]*\}/)?.[0] ?? '');
  if (!raw) return null;
  try { return JSON.parse(raw) as Record<string, unknown>; } catch { return null; }
}

async function gate(cmd: string, args: string[], cwd: string): Promise<boolean> {
  try { await sh(cmd, args, { cwd, timeout: 10 * 60 * 1000 }); return true; } catch { return false; }
}

export function makeSdkDeps(workDir: string, profile?: string): StepRunnerDeps {
  const plugins = resolveProfilePlugins(profile);
  return {
    async runExecutor(step: StepRecord, critiques: string[]): Promise<ExecutorResult> {
      const crit = critiques.length ? `\n\nPrior critiques to address (cumulative):\n${critiques.join('\n')}` : '';
      const r = await runQuery(
        `Implement step ${step.step_no} "${step.title}" from .claude/scratchpad/*/plan.md. ` +
        `Tags: ${step.tags.join(', ') || 'none'}. On a retry, first reset the working tree to the step baseline. ` +
        `Build TDD, honor the acceptance criteria, then write a handoff report.${crit}`,
        workDir, plugins,
      );
      return { ok: r.ok, detail: r.ok ? undefined : r.text.slice(-300) };
    },

    async runGates(_step: StepRecord): Promise<GateResult> {
      const lint = (await gate('npx', ['ultracite', 'lint'], workDir)) || (await gate('npx', ['biome', 'check', '.'], workDir));
      const types = (await gate('npm', ['run', 'typecheck'], workDir)) || (await gate('npx', ['tsc', '--noEmit'], workDir));
      const tests = await gate('npm', ['test'], workDir);
      return { passed: lint && types && tests, detail: `lint=${lint} types=${types} tests=${tests}` };
    },

    async runReviewer(step: StepRecord): Promise<ReviewResult> {
      const r = await runQuery(
        `Use the code-reviewer agent to review step ${step.step_no}. Re-run the gates yourself and verify each ` +
        `acceptance criterion with evidence. Output ONLY a \`\`\`json block: ` +
        `{"score":0-100,"criticalIssues":n,"verdict":"approve|request_changes|block","retryInstructions":"..."}.`,
        workDir, plugins,
      );
      const j = extractJson(r.text);
      if (!j || typeof j.score !== 'number') {
        return { score: 0, criticalIssues: 1, verdict: 'request_changes', reportJson: { raw: r.text.slice(-500) }, retryInstructions: 'reviewer output was unparseable — re-run review' };
      }
      const verdict = (j.verdict === 'approve' || j.verdict === 'block') ? j.verdict : 'request_changes';
      return {
        score: j.score as number,
        criticalIssues: (j.criticalIssues as number) ?? 0,
        verdict,
        reportJson: j,
        retryInstructions: (j.retryInstructions as string) ?? undefined,
      };
    },

    async runRuntime(step: StepRecord): Promise<RuntimeResult> {
      const r = await runQuery(
        `Use the runtime-verifier agent for step ${step.step_no}: boot the stack (db→back→front) and run ` +
        `e2e/smoke against the live system. Output ONLY a \`\`\`json block: {"verdict":"pass|fail",...}.`,
        workDir, plugins,
      );
      const j = extractJson(r.text);
      return { passed: !!j && j.verdict === 'pass', reportJson: j ?? { raw: r.text.slice(-500) } };
    },
  };
}
