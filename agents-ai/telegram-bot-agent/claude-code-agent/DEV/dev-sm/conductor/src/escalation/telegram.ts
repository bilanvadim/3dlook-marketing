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
          { text: '✅ Approve', callback_data: `ho:approve:${e.escalationId}` },
          { text: '⛔ Deny',    callback_data: `ho:deny:${e.escalationId}` },
          { text: '🛑 Abort',   callback_data: `ho:abort:${e.escalationId}` },
        ]],
      },
    }),
  }).then(async (res) => {
    // An escalation nobody receives is worse than none: waitEscalation then sits
    // out its 30 minutes and the job closes as 'escalated', with finishJob
    // clearing resume_session_id so it cannot even be resumed. The response was
    // never inspected, so a 400 (Markdown that failed to parse — escapeMd covers
    // only _*`[] , which is not enough for legacy Markdown), a 401 or a
    // "chat not found" all looked like success.
    if (!res.ok) {
      const body = await res.text().catch(() => '');
      console.error(`telegram send rejected: HTTP ${res.status} ${body.slice(0, 200)}`);
      // Retry once WITHOUT parse_mode — losing the formatting beats losing the
      // message that is blocking a job.
      if (res.status === 400) {
        await fetch(`https://api.telegram.org/bot${cfg.botToken}/sendMessage`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ chat_id: cfg.chatId, text }),
        }).catch((err) => console.error('telegram plain-text retry failed:', err));
      }
    }
  }).catch((err) => console.error('telegram notify failed:', err));
}

export async function notifyDone(cfg: TelegramConfig, jobTitle: string, status: string, summary: string) {
  const icon = status === 'done' ? '✅' : status === 'aborted' ? '🛑' : '❌';
  const text = `${icon} *Fullstack agents job ${escapeMd(status)}*\n*${escapeMd(jobTitle)}*\n\n${escapeMd(truncate(summary, 1500))}`;
  await fetch(`https://api.telegram.org/bot${cfg.botToken}/sendMessage`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      chat_id: cfg.chatId,
      text,
      parse_mode: 'Markdown',
    }),
  }).then(async (res) => {
    // Same reason as the escalation sender: the response was never inspected, so
    // a 400 from Markdown that failed to parse (escapeMd covers only _*`[] ,
    // which is not enough for legacy Markdown), a 401, or "chat not found" all
    // looked like a delivered message.
    if (!res.ok) {
      const body = await res.text().catch(() => '');
      console.error(`telegram send rejected: HTTP ${res.status} ${body.slice(0, 200)}`);
      // Retry once WITHOUT parse_mode — losing the formatting beats losing the
      // message that is blocking a job.
      if (res.status === 400) {
        await fetch(`https://api.telegram.org/bot${cfg.botToken}/sendMessage`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ chat_id: cfg.chatId, text }),
        }).catch((err) => console.error('telegram plain-text retry failed:', err));
      }
    }
  }).catch((err) => console.error('telegram notify failed:', err));
}

function truncate(s: string, n: number) { return s.length > n ? s.slice(0, n) + '…' : s; }
function escapeMd(s: string) { return s.replace(/([_*`\[\]])/g, '\\$1'); }
