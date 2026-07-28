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

  await fetch(`https://api.telegram.org/bot${cfg.botToken}/sendMessage`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      chat_id: cfg.chatId,
      text,
      parse_mode: 'Markdown',
      reply_markup: {
        inline_keyboard: [[
          { text: breaker ? '▶️ Continue' : '✅ Approve', callback_data: `ho:approve:${e.escalationId}` },
          { text: breaker ? '⏸ Stop & keep' : '⛔ Deny',   callback_data: `ho:deny:${e.escalationId}` },
          { text: '🛑 Abort',                              callback_data: `ho:abort:${e.escalationId}` },
        ]],
      },
    }),
  }).catch((err) => console.error('telegram notify failed:', err));
}

export async function notifyDone(cfg: TelegramConfig, jobTitle: string, status: string, summary: string) {
  const icon = status === 'done' ? '✅' : status === 'aborted' ? '🛑'
    : status === 'paused' ? '⏸' : status === 'escalated' ? '🟡' : '❌';
  await fetch(`https://api.telegram.org/bot${cfg.botToken}/sendMessage`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      chat_id: cfg.chatId,
      text: `${icon} *Fullstack agents job ${escapeMd(status)}*\n*${escapeMd(jobTitle)}*\n\n${escapeMd(truncate(summary, 1500))}`,
      parse_mode: 'Markdown',
    }),
  }).catch((err) => console.error('telegram notify failed:', err));
}

function truncate(s: string, n: number) { return s.length > n ? s.slice(0, n) + '…' : s; }
function escapeMd(s: string) { return s.replace(/([_*`\[\]])/g, '\\$1'); }
