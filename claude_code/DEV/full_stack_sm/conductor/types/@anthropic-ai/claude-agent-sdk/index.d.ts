// Minimal type shim for @anthropic-ai/claude-agent-sdk (typecheck only; real pkg bundles the binary).
export interface QueryOptions {
  settingSources?: string[];
  permissionMode?: 'default' | 'acceptEdits' | 'bypassPermissions';
  systemPrompt?: string;
  cwd?: string;
  resume?: string;        // SDK session id to resume (durable resume)
  [k: string]: unknown;
}
export interface QueryParams { prompt: string; options?: QueryOptions; }
export function query(params: QueryParams): AsyncIterable<any>;
