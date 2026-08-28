/**
 * Fullstack agents Conductor — profile → plugin resolver.
 *
 * A job's `profile` (ho_jobs.profile: dev|seo|marketing|security) selects a
 * MUTUALLY-EXCLUSIVE set of Claude Code plugins, so only that domain system's
 * agents/skills/commands load into the Agent SDK session. This mirrors the
 * interactive switch-profile.sh, but per-session: we resolve the profile's
 * plugins to absolute local dirs and pass them to query({ options.plugins }),
 * independent of the target project's own .claude/.
 *
 * Source of truth = agents-ai/telegram-bot-agent/claude-code-agent/DEV/profiles/<profile>.json (same files the
 * interactive switcher reads). Override the dir with HO_PROFILES_DIR.
 */
import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { dirname, isAbsolute, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

/** SDK local-plugin config (kept structural to avoid coupling to the SDK type shim). */
export type LocalPlugin = { type: 'local'; path: string };

interface ProfileManifest {
  name?: string;
  marketplaces?: Record<string, string>;
  enabledPlugins?: string[];
}

const HERE = dirname(fileURLToPath(import.meta.url)); // .../conductor/src/core
// profiles live at agents-ai/telegram-bot-agent/claude-code-agent/DEV/profiles (four levels up: core→src→conductor→dev→DEV)
const DEFAULT_PROFILES_DIR = resolve(HERE, '../../../../profiles');

export function profilesDir(): string {
  return process.env.HO_PROFILES_DIR ?? DEFAULT_PROFILES_DIR;
}

interface ProfileManifestFull extends ProfileManifest { runFrom?: string }

/** Read a manifest, or null if it is missing/unreadable. */
function readManifest(name: string): ProfileManifestFull | null {
  const p = join(profilesDir(), `${name}.json`);
  if (!existsSync(p)) return null;
  try { return JSON.parse(readFileSync(p, 'utf8')) as ProfileManifestFull; } catch { return null; }
}

/**
 * The directory a profile is BOUND to (`runFrom`), or null when it is free to run
 * anywhere. Resolved relative to the profiles dir's parent — same convention as
 * switch-profile.sh and the marketplace paths below.
 */
export function profileRunFrom(profile: string | null | undefined): string | null {
  const m = readManifest((profile && profile.trim()) || 'dev');
  const v = m?.runFrom;
  if (!v) return null;
  const p = isAbsolute(v) ? v : resolve(dirname(profilesDir()), v);
  return existsSync(p) ? p : null;
}

/**
 * Where the job must actually run.
 *
 * A bound profile (marketing_vb / marketing_vb_sm) has agents that read CLAUDE.md,
 * brand-assets/ and workspace/ by RELATIVE path — from anywhere else they see none of
 * it and the run produces confidently generic output with no error anywhere. Job 88
 * (2026-08-17) was enqueued with work_dir at the repo ROOT, one level above the
 * project, precisely that way.
 *
 * So for a bound profile the manifest wins over whatever the enqueuer wrote, and the
 * substitution is logged. Unbound profiles (dev, seo, …) keep the given work_dir.
 */
export function resolveWorkDir(profile: string | null | undefined, workDir: string): string {
  const bound = profileRunFrom(profile);
  if (!bound) return workDir;
  const given = resolve(workDir || '.');
  if (given === bound || given.startsWith(`${bound}/`)) return workDir;
  console.warn(`[profiles] profile '${profile}' is bound to ${bound} — work_dir `
    + `'${workDir}' is outside it; running from ${bound} instead`);
  return bound;
}

/**
 * Resolve a profile to a list of local plugin dirs for query({ options.plugins }).
 * Returns [] on any problem (unknown/missing profile, bad manifest, missing dirs)
 * — the SDK then falls back to settingSources, which is the safe default.
 */
export function resolveProfilePlugins(profile: string | null | undefined): LocalPlugin[] {
  const name = (profile && profile.trim()) || 'dev';
  const manifestPath = join(profilesDir(), `${name}.json`);
  // THROW, do not fall back.
  //
  // This used to console.warn and return [] — "falling back to project settings" — which
  // means the job runs with NONE of its profile's plugins. For a marketing_vb_sm job that
  // is the entire marketing system silently absent: no error, no failed step, nothing in
  // ho_project_status, one warn line in a log nobody tails, and an agent that cheerfully
  // produces something with no idea what it was supposed to be. 88 of the jobs in this
  // queue are marketing_vb_sm.
  //
  // It is reachable by ordinary means, not just by a typo: ho_jobs' CHECK constraint
  // accepts 'sandbox' and 'test', and neither has a manifest on disk. A job enqueued
  // against either passes every validation there is and then runs empty.
  //
  // Failing here marks the job failed with a message that says exactly what is missing,
  // which the cron monitor pushes to Telegram. A job that cannot load its tools has not
  // got a degraded mode worth having.
  if (!existsSync(manifestPath)) {
    const available = (() => {
      try {
        return readdirSync(profilesDir()).filter((f) => f.endsWith('.json'))
          .map((f) => f.replace(/\.json$/, '')).sort().join(', ');
      } catch { return '(profiles dir unreadable)'; }
    })();
    throw new Error(
      `[profiles] no manifest for '${name}' at ${manifestPath}. Refusing to run with no ` +
      `plugins — that is indistinguishable from a working run until you read the output. ` +
      `Available profiles: ${available}`,
    );
  }

  let manifest: ProfileManifest;
  try {
    manifest = JSON.parse(readFileSync(manifestPath, 'utf8')) as ProfileManifest;
  } catch (e) {
    throw new Error(`[profiles] manifest ${manifestPath} is unreadable or invalid JSON: ${String(e)}`);
  }

  const marketplaces = manifest.marketplaces ?? {};
  // Marketplace paths in profiles/*.json may be relative to agents-ai/telegram-bot-agent/claude-code-agent/DEV
  // (= the parent of the profiles dir), matching switch-profile.sh. Absolute
  // paths are honored as-is.
  const devDir = dirname(profilesDir());
  const out: LocalPlugin[] = [];
  for (const entry of manifest.enabledPlugins ?? []) {
    const [plugName, mkt] = entry.split('@');
    const baseRaw = mkt ? marketplaces[mkt] : undefined;
    if (!baseRaw) {
      console.warn(`[profiles] '${entry}' → no marketplace path for '${mkt}' in ${name}.json — skipped`);
      continue;
    }
    const base = isAbsolute(baseRaw) ? baseRaw : resolve(devDir, baseRaw);
    const path = join(base, 'plugins', plugName);
    if (!existsSync(path)) {
      console.warn(`[profiles] plugin dir missing: ${path} — skipped`);
      continue;
    }
    out.push({ type: 'local', path });
  }
  return out;
}
