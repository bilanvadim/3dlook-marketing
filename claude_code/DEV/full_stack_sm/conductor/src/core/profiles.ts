/**
 * Fullstack agents Conductor — profile → plugin resolver.
 *
 * A job's `profile` (hc_jobs.profile: dev|seo|marketing|security|marketing_vb|marketing_vb_sm) selects a
 * MUTUALLY-EXCLUSIVE set of Claude Code plugins, so only that domain system's
 * agents/skills/commands load into the Agent SDK session. This mirrors the
 * interactive switch-profile.sh, but per-session: we resolve the profile's
 * plugins to absolute local dirs and pass them to query({ options.plugins }),
 * independent of the target project's own .claude/.
 *
 * Source of truth = claude_code/DEV/profiles/<profile>.json (same files the
 * interactive switcher reads). Override the dir with HC_PROFILES_DIR.
 */
import { readFileSync, existsSync } from 'node:fs';
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
// profiles live at claude_code/DEV/profiles (four levels up: core→src→conductor→full_stack_sm→DEV)
const DEFAULT_PROFILES_DIR = resolve(HERE, '../../../../profiles');

export function profilesDir(): string {
  return process.env.HC_PROFILES_DIR ?? DEFAULT_PROFILES_DIR;
}

/**
 * Resolve a profile to a list of local plugin dirs for query({ options.plugins }).
 * Returns [] on any problem (unknown/missing profile, bad manifest, missing dirs)
 * — the SDK then falls back to settingSources, which is the safe default.
 */
export function resolveProfilePlugins(profile: string | null | undefined): LocalPlugin[] {
  const name = (profile && profile.trim()) || 'dev';
  const manifestPath = join(profilesDir(), `${name}.json`);
  if (!existsSync(manifestPath)) {
    console.warn(`[profiles] no manifest for '${name}' at ${manifestPath} — falling back to project settings`);
    return [];
  }

  let manifest: ProfileManifest;
  try {
    manifest = JSON.parse(readFileSync(manifestPath, 'utf8')) as ProfileManifest;
  } catch (e) {
    console.warn(`[profiles] unreadable manifest ${manifestPath}: ${String(e)}`);
    return [];
  }

  const marketplaces = manifest.marketplaces ?? {};
  // Marketplace paths in profiles/*.json are relative to claude_code/DEV
  // (= the parent of the profiles dir), matching switch-profile.sh. Absolute
  // paths are honored as-is for backward compatibility.
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
