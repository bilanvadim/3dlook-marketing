/**
 * Hermes Orchestrator — Telegram callback handler.
 * Run as a tiny webhook (or wire into n8n). When the human taps Approve/Deny/Abort,
 * Telegram sends a callback_query with data "ho:<decision>:<escalationId>".
 * We record the decision into ho_escalations; the conductor's waitEscalation picks it up.
 *
 * The webhook server listens on HO_WEBHOOK_PORT (default 3001) and accepts POST
 * requests at /telegram-webhook containing a standard Telegram Update JSON body.
 */
import { createServer, IncomingMessage, ServerResponse } from 'node:http';
import { createClient } from '@libsql/client';

const db = createClient({ url: process.env.DATABASE_URL ?? 'file:./ho.db' });
const TELEGRAM_TOKEN = process.env.TELEGRAM_BOT_TOKEN;

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

/** Answer a Telegram callback query so the loading spinner on the button disappears. */
async function answerCallbackQuery(callbackQueryId: string, text?: string): Promise<void> {
  if (!TELEGRAM_TOKEN) return;
  await fetch(`https://api.telegram.org/bot${TELEGRAM_TOKEN}/answerCallbackQuery`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ callback_query_id: callbackQueryId, text }),
  }).catch((err) => console.error('telegram answerCallbackQuery failed:', err));
}

/** Parse the raw POST body into a JSON object. */
function readBody(req: IncomingMessage): Promise<string> {
  return new Promise((resolve, reject) => {
    let body = '';
    req.on('data', (chunk: Buffer) => { body += chunk.toString(); });
    req.on('end', () => resolve(body));
    req.on('error', reject);
  });
}

async function handleWebhook(req: IncomingMessage, res: ServerResponse): Promise<void> {
  if (req.method !== 'POST' || req.url !== '/telegram-webhook') {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('not found');
    return;
  }

  try {
    const raw = await readBody(req);
    const update = JSON.parse(raw);
    const callbackQuery = update?.callback_query;
    if (callbackQuery?.data) {
      const who = callbackQuery?.from?.username
        ?? callbackQuery?.from?.id?.toString()
        ?? 'unknown';
      const decision = await handleCallback(callbackQuery.data, who);
      await answerCallbackQuery(callbackQuery.id,
        decision === 'ignored' ? undefined : `Escalation ${decision}`);
    }
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ ok: true }));
  } catch (err) {
    console.error('webhook error:', err);
    res.writeHead(500, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ ok: false, error: String(err) }));
  }
}

/** Start the webhook HTTP server for receiving Telegram callback updates. */
export function startWebhookServer(port = Number(process.env.HO_WEBHOOK_PORT ?? 3001)): void {
  const server = createServer(handleWebhook);
  server.listen(port, () => {
    console.log(`[webhook] listening on :${port} (POST /telegram-webhook)`);
  });
}
