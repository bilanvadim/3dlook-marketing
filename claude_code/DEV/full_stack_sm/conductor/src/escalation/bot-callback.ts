/**
 * Hermes Orchestrator — Telegram callback handler.
 * Run as a tiny webhook (or wire into n8n). When the human taps Approve/Deny/Abort,
 * Telegram sends a callback_query with data "ho:<decision>:<escalationId>".
 * We record the decision into ho_escalations; the conductor's waitEscalation picks it up.
 */
import { createClient } from '@libsql/client';

const db = createClient({ url: process.env.DATABASE_URL ?? 'file:./ho.db' });

export async function handleCallback(data: string, who: string): Promise<string> {
  const m = /^ho:(approve|deny|abort):(\d+)$/.exec(data);
  if (!m) return 'ignored';
  const decision = m[1] === 'approve' ? 'approved' : m[1] === 'deny' ? 'denied' : 'aborted';
  const id = Number(m[2]);
  // only the first decision wins (status='open' guard)
  await db.execute({
    sql: "update ho_escalations set status=?, decided_by=?, decided_at=datetime('now') where id=? and status='open'",
    args: [decision, who, id],
  });
  return decision;
}
