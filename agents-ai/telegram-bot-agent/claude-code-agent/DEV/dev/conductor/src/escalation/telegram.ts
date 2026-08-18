/**
 * Fullstack agents Conductor — Telegram escalation notifier.
 * Sends the human a message when a run pauses for a decision. The actual approve/deny
 * is recorded back into ho_escalations (by a tiny bot webhook or by n8n); the conductor
 * polls the row via Store.waitEscalation. This module only PUSHES the notification.
 *
 * Kept dependency-free (uses fetch) so it works in any Node 18+ / container.
 */
export interface TelegramConfig {
  botToken: string;
  chatId: string;
}

export function tgConfigFromEnv(): TelegramConfig | null {
  const botToken = process.env.TELEGRAM_BOT_TOKEN;
  const chatId = process.env.TELEGRAM_CHAT_ID;
  if (!botToken || !chatId) return null;
  return { botToken, chatId };
}

/**
 * Reasons raised by the circuit breaker rather than by the agent. For these, "approve" means
 * CONTINUE RUNNING — so the button must not say "Approve", which reads as "yes, it's done" and
 * is exactly how job 37 got closed with zero work on 2026-07-28. Same callback_data either way,
 * so no protocol change and escalations opened by an older build still resolve.
 */
const BREAKER_REASONS = new Set(['stuck', 'turns']);

/**
 * Strip a bot token out of anything on its way to a log.
 *
 * NOT a reproduced leak, and the comment should say so: on this Node/undici, a failed fetch reports
 * `TypeError: fetch failed` with a cause naming only the HOST — DNS failure, TLS failure, connection
 * refused and abort were all checked and none carried the token. The audit's claim was conditional
 * ("when undici attaches the request URL"), and it stays plausible for a future version.
 *
 * It is kept because the realistic path to a leak is not undici, it is a person: the token lives in
 * the URL, and the first thing anyone does while debugging a delivery problem is log the URL. One
 * regex costs nothing and covers both.
 */
export function redactToken(x: unknown): string {
  return String(x).replace(/bot\d{6,}:[A-Za-z0-9_-]{10,}/g, 'bot<redacted>');
}

/**
 * Send one message and CHECK THE ANSWER.
 *
 * An escalation nobody receives is worse than none: waitEscalation then sits out its wait and
 * the job parks or closes as 'escalated'. The response used to go uninspected, so a 400
 * (Markdown that failed to parse — escapeMd covers only _*`[] , which is not enough for legacy
 * Markdown), a 401, or a "chat not found" all looked like success. On a 400 we retry once
 * WITHOUT parse_mode: losing the formatting beats losing the message that is blocking a job.
 */
async function send(cfg: TelegramConfig, text: string, replyMarkup?: unknown): Promise<void> {
  const url = `https://api.telegram.org/bot${cfg.botToken}/sendMessage`;
  const post = (body: unknown) => fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  });
  await post({ chat_id: cfg.chatId, text, parse_mode: 'Markdown', ...(replyMarkup ? { reply_markup: replyMarkup } : {}) })
    .then(async (res) => {
      if (res.ok) return;
      const body = await res.text().catch(() => '');
      console.error(redactToken(`telegram send rejected: HTTP ${res.status} ${body.slice(0, 200)}`));
      if (res.status === 400) {
        await post({ chat_id: cfg.chatId, text, ...(replyMarkup ? { reply_markup: replyMarkup } : {}) })
          .catch((err) => console.error('telegram plain-text retry failed:', redactToken(err)));
      }
    })
    .catch((err) => console.error('telegram notify failed:', redactToken(err)));
}

export async function notifyEscalation(
  cfg: TelegramConfig,
  e: { escalationId: number; jobTitle: string; reason: string; question: string; context?: unknown },
): Promise<void> {
  const ctx = e.context ? '\n\n```\n' + truncate(JSON.stringify(e.context, null, 2), 1200) + '\n```' : '';
  const breaker = BREAKER_REASONS.has(e.reason);
  const hint = breaker
    ? 'approve = keep going · deny = stop and leave it for me · abort = kill the job'
    : 'approve / deny / abort';
  const text =
    `🟡 *Fullstack agents escalation* (#${e.escalationId})\n` +
    `*Job:* ${escapeMd(e.jobTitle)}\n` +
    `*Reason:* ${escapeMd(e.reason)}\n\n` +
    `${escapeMd(e.question)}${ctx}\n\n` +
    `Reply: ${escapeMd(hint)}  (or use the bot buttons)`;

  await send(cfg, text, {
    inline_keyboard: [[
      { text: breaker ? '▶️ Continue' : '✅ Approve', callback_data: `ho:approve:${e.escalationId}` },
      { text: breaker ? '⏸ Stop & keep' : '⛔ Deny',   callback_data: `ho:deny:${e.escalationId}` },
      { text: '🛑 Abort',                              callback_data: `ho:abort:${e.escalationId}` },
    ]],
  });
}

export async function notifyDone(cfg: TelegramConfig, jobTitle: string, status: string, summary: string) {
  const icon = status === 'done' ? '✅' : status === 'aborted' ? '🛑'
    : status === 'paused' ? '⏸' : status === 'escalated' ? '🟡' : '❌';
  await send(cfg,
    `${icon} *Fullstack agents job ${escapeMd(status)}*\n*${escapeMd(jobTitle)}*\n\n${escapeMd(truncate(summary, 1500))}`);
}

function truncate(s: string, n: number) { return s.length > n ? s.slice(0, n) + '…' : s; }
function escapeMd(s: string) { return s.replace(/([_*`\[\]])/g, '\\$1'); }
