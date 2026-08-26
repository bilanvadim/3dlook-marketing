# Telegram — how to actually drive the system

Bot: **@dlookmarketing_bot**. Everything reaches the system through it.

## Conversation vs job

Two different things happen depending on what you type, and the distinction is
deliberate.

**Conversation** stays with Hermes, the manager. It answers, looks things up,
reports status. It does not write code or content — that is the whole point of the
split.

**A job** is an autonomous run: it opens a Claude Code session, edits files, and
can take hours. Only *you* start one. Hermes will not start a job on its own
initiative, and a phrase like "надо бы посты" is conversation, not an instruction.

## Starting a job

Either the ⚙️ Исполнитель → 📣 Marketing VB buttons, or a keyword at the **start**
of a message:

| Type this | What runs |
|---|---|
| `Стаття <тема>` | SEO article pipeline → stops at checkpoint 1 |
| `Пости <slug>` | Social posts, one job per active profile |
| `Аутбаунд <ринок>` | Outbound campaign pipeline |
| `Кампанія <задача>` | Blended campaign |

Convention: **one topic per autonomous run.** Start a heavy run in a new topic and
its questions, escalations and result come back there rather than mixing into an
unrelated conversation.

## The article pipeline has two checkpoints

```
Стаття <тема>  →  plan  →  ⏸ CHECKPOINT 1 (you approve title + outline)
                            ↓  «Апрув»
                        write → edit → publish  →  ⏸ CHECKPOINT 2 (text + meta)
```

**There is no checkpoint between write, edit and publish.** An approval carries the
run all the way to checkpoint 2 in a single job.

### «Апрув» — what it does and does not mean

Saying «Апрув» approves **the stage the article is standing on**, which is almost
always checkpoint 1. Internally it must reach the pipeline as a token:

```bash
mvb-run.py article "<exact same topic>" approve
```

Without the token the run either re-plans from scratch or walks to checkpoint 1 and
waits for a human who is not there. That mistake cost six jobs for one article on
2026-08-25.

«Апрув» **never** means "now make social posts". Posts need two things: a
`publish-package.md` on disk, and you asking for posts in those words.

Naming a stage means only that stage: `article "<тема>" edit approve` runs `edit`
and stops.

The topic string must match the first launch **verbatim** — it keys the directory
under `workspace/seo/articles/`.

## What comes back, and what it means

| Message | Meaning |
|---|---|
| ✅ + summary | Job finished and produced artifacts |
| ⚠️ + "закрылся без единого артефакта" | Job finished having done **nothing**. Re-enqueue |
| ⏳ + "повтор через ~N мин" | Rate limit, not a failure. It is waiting; do nothing |
| ❓ | A question is blocking the run — answer in the chat |
| ⚠️ + Approve/Deny/Abort buttons | An escalation needs your decision |

The ⚠️-with-no-artifacts case exists because `done` on its own proves nothing: it
only says the session ended cleanly. `mvb-verify-job.py` counts files actually
written, and the notifier downgrades the tick when that count is zero.

## Sending results back to you

The conductor's completion message truncates at 1500 characters, so a real
deliverable never fits. For finished posts:

```bash
mvb-run.py digest <slug>
```

Its stdout **is** the message — one profile per Telegram message, since Telegram
cuts at 4096 characters.

## Under the hood

Gateway long-polls Telegram (no webhook). `claude_switcher` sees each message with
its session key `chat#thread`, matches a leading keyword against the `mvb:*`
routes, and either answers as the manager or calls `mvb-run.py`, which is the only
sanctioned way to create a job. It imports its route table from
`claude_switcher.py`, so the buttons and the script cannot drift apart.

Notifications route back to the originating topic through
`~/.hermes/mvb-job-threads.json`, recorded at enqueue. `message_thread_id` alone is
unreliable in these private-chat topics, so it is paired with
`reply_to_message_id` from the switcher's per-topic anchors.

## Testing the chain without your phone

`bootstrap/e2e-telegram.py` sends **as you**, over the enrolled MTProto session, and
reads the reply:

```bash
~/.hermes/mtproto/venv/bin/python bootstrap/e2e-telegram.py \
    --send "Відповідай рівно одним рядком: PING-OK" --expect "PING-OK"
```

A reply on its own is not proof — a manager answering from memory replies just as
fast as one that really reached Claude Code. To test the full chain, ask for the
per-run marker in `marketing_vb/workspace/_e2e/fixture.md`, which nothing upstream
can know.
