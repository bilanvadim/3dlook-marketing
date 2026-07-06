/**
 * Fullstack agents Conductor — Telegram callback handler.
 * Run as a tiny webhook (or wire into n8n). When the human taps Approve/Deny/Abort,
 * Telegram sends a callback_query with data "hc:<decision>:<escalationId>".
 * We record the decision into hc_escalations; the conductor's waitEscalation picks it up.
 */
import pg from 'pg';

const pool = new pg.Pool({ connectionString: process.env.DATABASE_URL });

export async function handleCallback(data: string, who: string): Promise<string> {
  const m = /^hc:(approve|deny|abort):(\d+)$/.exec(data);
  if (!m) return 'ignored';
  const decision = m[1] === 'approve' ? 'approved' : m[1] === 'deny' ? 'denied' : 'aborted';
  const id = Number(m[2]);
  // only the first decision wins (status='open' guard)
  await pool.query(
    "update hc_escalations set status=$1, decided_by=$2, decided_at=now() where id=$3 and status='open'",
    [decision, who, id],
  );
  return decision;
}
