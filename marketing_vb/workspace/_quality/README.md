# Quality Control Workspace

Здесь живут все QC отчёты и improvement proposals.

## Структура

```
_quality/
├── README.md                              (этот файл)
├── social/
│   ├── 2026-04-28-post-drafter-w17-li.md
│   ├── 2026-04-28-visual-brief-w17-li.md
│   └── ...
├── outbound/
│   ├── 2026-04-15-hypothesis-generator-insurance-uw.md
│   ├── 2026-04-16-icp-validator-insurance-uw.md
│   ├── 2026-04-17-message-sequencer-insurance-uw.md
│   └── ...
├── seo/
│   ├── 2026-04-20-seo-outline-builder-bmi-verification.md
│   ├── 2026-04-22-seo-meta-generator-bmi-verification.md
│   └── ...
└── improvements/
    ├── 2026-04-30-summary.md
    ├── 2026-04-30-message-sequencer-proposal.md
    ├── 2026-04-30-post-drafter-proposal.md
    └── ...
```

## Как работает loop

```
Agent X создаёт артефакт
        ↓
quality-controller оценивает (auto или /qc)
        ↓
Telegram notify Вадиму: «{agent} → {score}/20, top issue: {...}»
        ↓
Я (Claude в чате) добавляю coordinator_review в QC отчёт
   (короткий agree/disagree + top issue одной строкой)
        ↓
Вадим Approve/Edit/Reject артефакт как обычно
        ↓
[раз в 2 недели] /improve-agents → agent-improver читает все отчёты
        ↓
Proposals в improvements/ — Вадим смотрит, апрувит, применяет diff
        ↓
Промпт агента улучшен → следующая итерация даст score выше
```

## Включение / выключение auto-QC

В `CLAUDE.md` секция 14 (или в `.env` runner-ов) есть флаг `AUTO_QC_ENABLED`:
- `true` — runners запускают quality-controller автоматически после ключевых артефактов
- `false` — QC только по команде `/qc`

Auto-QC запускается после: hypothesis, icp-validation, message-sequence, post-draft, seo-outline, seo-final, seo-meta. НЕ запускается после: people-extractor (механический шаг), citation-deduper, readability-editor, ai-detector-rewriter (промежуточные шаги).

## Coordinator review — что от меня требуется

Когда QC выдаёт отчёт, я в чате должен короткой строкой добавить мнение в `coordinator_review` поле отчёта. Формат:

```
agreement: ✅ agree / ⚠️ disagree
top_issue: [1 строка] | none
```

**Не расписывать.** Если согласен с QC и top issue — просто `agree, top_issue: as noted`.
Если QC что-то пропустил или переоценил — `disagree (X пропустил Y)` или `agree but also Z`.

Эта инфа — основной сигнал для improver-а, потому что я вижу контекст всей конверсации, а QC только артефакт.

## Метрики системы

Можно периодически смотреть тренды через `/improve-agents` summary:
- Avg score по агентам
- Trend (↑ ↓ →)
- Top systemic issues across all agents

Если avg по системе < 15 — это flag, что product-info или CLAUDE.md не покрывают что-то важное.
