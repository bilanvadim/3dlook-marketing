/**
 * Fullstack agents Conductor — Telegram callback handler.
 * When the human taps Approve/Deny/Abort, Telegram sends a callback_query with data
 * "ho:<decision>:<escalationId>". We record the decision into ho_escalations; the conductor's
 * waitEscalation polls the row and picks it up.
 *
 * Two ways in, and they are mutually exclusive by design:
 *
 *  - WEBHOOK (default): a tiny HTTP server on HO_WEBHOOK_PORT accepting
 *    POST /telegram-webhook with a standard Telegram Update body. The Hermes gateway owns the
 *    bot's single allowed getUpdates consumer and forwards `ho:*` callback_query updates here.
 *  - POLLING (HO_TELEGRAM_POLLING=1): the conductor calls getUpdates itself. Only for standalone
 *    runs where NOTHING else consumes that bot — Telegram allows exactly one getUpdates reader
 *    per token, so enabling this alongside the gateway makes both lose updates at random.
 *
 * HO_WEBHOOK_PORT IS PER-USER, NOT A CONSTANT. Every runtime on the box binds it on loopback,
 * so two users sharing the default silently gave the port to whichever conductor started first —
 * the second one's Approve/Deny taps went nowhere. It therefore lives in the PROFILE (rendered
 * into each user's .env), and a bind failure is reported loudly instead of taking the worker
 * down with it.
 */
import { createServer, IncomingMessage, ServerResponse } from 'node:http';
import { timingSafeEqual } from 'node:crypto';
import { Store } from '../core/store';
import { redactToken } from './telegram';

// One Store, not a second raw libSQL client. The old client had no WAL, no busy_timeout and no
// retry, so a callback landing while the workers were writing threw SQLITE_BUSY and the human's
// decision was dropped with an HTTP 500. See Store.decideEscalation.
let _store: Store | null = null;
function store(): Store {
  if (!_store) _store = new Store(process.env.DATABASE_URL ?? 'file:./ho.db');
  return _store;
}
const TELEGRAM_TOKEN = process.env.TELEGRAM_BOT_TOKEN;

export async function handleCallback(data: string, who: string): Promise<string> {
  const m = /^ho:(approve|deny|abort):(\d+)$/.exec(data);
  if (!m) return 'ignored';
  const decision = m[1] === 'approve' ? 'approved' : m[1] === 'deny' ? 'denied' : 'aborted';
  const id = Number(m[2]);
  // Through the Store: WAL, busy_timeout and the retry ladder. The `status='open'` guard lives
  // there too, so the first decision still wins.
  const outcome = await store().decideEscalation(id, decision, who);
  if (outcome === 'applied') return decision;
  // Say which non-decision happened. Reporting the decision regardless told the human "approved"
  // for an escalation that was already resolved or had never existed.
  console.warn(`callback for escalation ${id}: ${outcome}`);
  return outcome;
}

/** Answer a Telegram callback query so the loading spinner on the button disappears. */
async function answerCallbackQuery(callbackQueryId: string, text?: string): Promise<void> {
  if (!TELEGRAM_TOKEN) return;
  await fetch(`https://api.telegram.org/bot${TELEGRAM_TOKEN}/answerCallbackQuery`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ callback_query_id: callbackQueryId, text }),
  }).catch((err) => console.error('telegram answerCallbackQuery failed:', redactToken(err)));
}

/** Record one callback_query and acknowledge it. Shared by the webhook and the poller. */
async function applyCallbackQuery(cb: any): Promise<void> {
  if (!cb?.data) return;
  const who = cb?.from?.username ?? cb?.from?.id?.toString() ?? 'unknown';
  const decision = await handleCallback(cb.data, who);
  // The toast the human sees must say what actually happened. "Escalation approved" for a row that
  // was already resolved — or that does not exist — is a lie told by a button.
  const toast = decision === 'ignored' ? undefined
    : decision === 'already-decided' ? 'Already decided by someone else'
    : decision === 'missing' ? 'That escalation no longer exists'
    : `Escalation ${decision}`;
  await answerCallbackQuery(cb.id, toast);
}

/** Read the raw POST body. */
function readBody(req: IncomingMessage): Promise<string> {
  return new Promise((resolve, reject) => {
    let body = '';
    req.on('data', (chunk: Buffer) => { body += chunk.toString(); });
    req.on('end', () => resolve(body));
    req.on('error', reject);
  });
}

/**
 * The shared secret every callback must carry.
 *
 * `X-Telegram-Bot-Api-Secret-Token` is Telegram's own header name, set via setWebhook's
 * `secret_token`, so the same check works whether the update comes from Telegram directly or is
 * forwarded by the Hermes gateway.
 */
const WEBHOOK_SECRET = (process.env.HO_WEBHOOK_SECRET ?? '').trim();

/** Constant-time comparison. A length check first, because timingSafeEqual throws on a mismatch. */
function secretOk(given: string | undefined): boolean {
  if (!WEBHOOK_SECRET) return false;
  const a = Buffer.from(given ?? '');
  const b = Buffer.from(WEBHOOK_SECRET);
  return a.length === b.length && timingSafeEqual(a, b);
}

async function handleWebhook(req: IncomingMessage, res: ServerResponse): Promise<void> {
  if (req.method !== 'POST' || req.url !== '/telegram-webhook') {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('not found');
    return;
  }

  // CLOSED BY DEFAULT. This endpoint decides gated actions — approve, deny, ABORT — for any
  // escalation id, and until now it trusted any POST that reached the port. Loopback was the only
  // control, and loopback does not separate the other accounts on a shared box: a forged
  // `{"callback_query":{"data":"ho:approve:<id>"}}` was accepted with {"ok":true}, forging
  // `decided_by` along the way. Verified against the running service before this was added.
  //
  // Unset secret means REFUSE, not "allow for compatibility": an endpoint that approves production
  // actions must not be open because a variable is missing. Nothing depended on the open behaviour —
  // the gateway records decisions straight into the queue database, so this path was unused.
  const header = req.headers['x-telegram-bot-api-secret-token'];
  if (!secretOk(Array.isArray(header) ? header[0] : header)) {
    if (!WEBHOOK_SECRET) {
      console.error('[webhook] HO_WEBHOOK_SECRET is not set — refusing every callback. '
        + 'Generate one into this profile\'s conductor .env (deploy.sh does it) and restart.');
    } else {
      console.warn('[webhook] rejected a callback with a missing or wrong secret token');
    }
    res.writeHead(401, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ ok: false, error: 'unauthorized' }));
    return;
  }

  try {
    const update = JSON.parse(await readBody(req));
    await applyCallbackQuery(update?.callback_query);
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ ok: true }));
  } catch (err) {
    console.error('webhook error:', err);
    res.writeHead(500, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ ok: false, error: String(err) }));
  }
}

/** Port for the callback webhook. Per-user — see the header note. */
export function webhookPort(): number {
  const raw = (process.env.HO_WEBHOOK_PORT ?? '').trim();
  const n = Number(raw);
  if (raw === '' || !Number.isInteger(n) || n < 1 || n > 65535) {
    console.warn(`[webhook] HO_WEBHOOK_PORT=${JSON.stringify(raw)} is not a usable port — falling back to 3001. `
      + 'Set it in this profile\'s .env; the default collides with any other runtime on this box.');
    return 3001;
  }
  return n;
}

/**
 * Start the webhook HTTP server. Bound to loopback: the only client is the local gateway, and
 * an escalation endpoint that anyone on the network can POST to would let them approve a
 * gated action.
 */
export function startWebhookServer(port = webhookPort(), host = process.env.HO_WEBHOOK_HOST ?? '127.0.0.1'): void {
  const server = createServer(handleWebhook);
  // Without this, EADDRINUSE surfaces as an unhandled 'error' event and takes the whole
  // conductor process down — the queue stops for a port clash. Jobs matter more than buttons:
  // log it loudly and keep working, with escalations answerable via the DB in the meantime.
  server.on('error', (err) => {
    console.error(`[webhook] cannot listen on ${host}:${port} — ${String(err)}. `
      + 'Escalation buttons will NOT work in this process until HO_WEBHOOK_PORT is fixed.');
  });
  server.listen(port, host, () => {
    console.log(`[webhook] listening on ${host}:${port} (POST /telegram-webhook)`);
  });
}

/** Poll Telegram for callback queries. Fallback for standalone runs — see the header note. */
let pollingOffset = 0;
async function pollTelegramCallbacks(): Promise<void> {
  if (!TELEGRAM_TOKEN) return;
  try {
    const url = `https://api.telegram.org/bot${TELEGRAM_TOKEN}/getUpdates`
      + `?offset=${pollingOffset}&timeout=2&allowed_updates=["callback_query"]`;
    const res = await fetch(url);
    const data = await res.json() as any;
    if (!data?.ok || !Array.isArray(data?.result)) return;
    for (const update of data.result) {
      pollingOffset = (update.update_id as number) + 1;
      await applyCallbackQuery(update?.callback_query);
    }
  } catch {
    // transient network error — retry next poll
  }
}

/** Start long-polling for Telegram callbacks. */
export function startTelegramPolling(intervalMs = 2000): void {
  pollTelegramCallbacks(); // immediate first poll
  setInterval(pollTelegramCallbacks, intervalMs);
  console.log(`[telegram] polling for callback queries every ${intervalMs}ms`);
}
