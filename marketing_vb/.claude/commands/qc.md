---
description: Запускает quality-controller на конкретный артефакт. Используется ручно, когда auto-QC отключён или нужна повторная проверка.
argument-hint: "[artifact-path]"
---

Запусти `quality-controller` на артефакте `$1`.

## Что произойдёт

1. quality-controller прочитает артефакт + промпт его автора + контекст
2. Оценит по 20-балльной шкале (см. `docs/quality-rubric.md`)
3. Сохранит отчёт в `workspace/_quality/{track}/{date}-{agent}-{slug}.md`
4. Уведомит Вадима через notify с топ-issue

## Когда использовать

- Когда auto-QC выключен в `CLAUDE.md` секция 14
- Когда нужна повторная проверка после правок
- Когда хочешь оценить старый артефакт ретроспективно

## После QC

Я (координатор) добавлю свою короткую coordinator review в тот же отчёт. Формат:

```
agreement: ✅ agree / ⚠️ disagree (1 line why)
top_issue: [одно предложение или "none"]
```

Когда соберётся достаточно отчётов — запусти `/improve-agents`.
