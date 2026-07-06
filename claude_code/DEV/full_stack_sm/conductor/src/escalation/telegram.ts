/**
 * Fullstack agents Conductor — Telegram escalation notifier.
 * Sends the human a message when a run pauses for a decision. The actual approve/deny
 * is recorded back into hc_escalations (by a tiny bot webhook or by n8n); the conductor
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

export async function notifyEscalation(
  cfg: TelegramConfig,
  e: { escalationId: number; jobTitle: string; reason: string; question: string; context?: unknown },
): Promise<void> {
  const ctx = e.context ? '\n\n```\n' + truncate(JSON.stringify(e.context, null, 2), 1200) + '\n```' : '';
  const text =
    `🟡 *Fullstack agents escalation* (#${e.escalationId})\n` +
    `*Job:* ${escapeMd(e.jobTitle)}\n` +
    `*Reason:* ${escapeMd(e.reason)}\n\n` +
    `${escapeMd(e.question)}${ctx}\n\n` +
    `Reply: approve / deny / abort  (or use the bot buttons)`;

  await fetch(`https://api.telegram.org/bot${cfg.botToken}/sendMessage`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      chat_id: cfg.chatId,
      text,
      parse_mode: 'Markdown',
      reply_markup: {
        inline_keyboard: [[
          { text: '✅ Approve', callback_data: `hc:approve:${e.escalationId}` },
          { text: '⛔ Deny',    callback_data: `hc:deny:${e.escalationId}` },
          { text: '🛑 Abort',   callback_data: `hc:abort:${e.escalationId}` },
        ]],
      },
    }),
  }).catch((err) => console.error('telegram notify failed:', err));
}

export async function notifyDone(cfg: TelegramConfig, jobTitle: string, status: string, summary: string) {
  const icon = status === 'done' ? '✅' : status === 'aborted' ? '🛑' : '❌';
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
