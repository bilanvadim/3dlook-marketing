---
description: "[DEPRECATED] Заменён на /post-from-article. Использовал квартальный план — больше не применяется."
argument-hint: "[week_number]"
---

> **DEPRECATED.** Используй `/post-from-article <article-slug>` вместо этого.
> Посты теперь создаются автоматически из SEO-статьи после апрува publish-package.

---

Готовь черновики постов на неделю $1 (если не указана — текущая ISO-неделя) для всех профилей.

## Шаги

1. Прочитай `CLAUDE.md` и `workspace/social/strategy/` чтобы найти актуальный квартальный план.
2. Определи список профилей из CLAUDE.md секция 3.
3. Для каждого профиля **последовательно** запусти субагент `post-drafter` с параметрами `week_number`, `profile`.
4. **Если `AUTO_QC_ENABLED=true`** в CLAUDE.md секция 14 — после каждого `post-drafter` сразу запусти `quality-controller` на свежий артефакт:
   ```
   Use quality-controller to evaluate workspace/social/{YYYY-Wk}/{profile}/post-N.md.
   Pass: agent_name=post-drafter, track=social, artifact_type=post.
   ```
5. После того как все драфты готовы — обнови `workspace/social/{YYYY-Wk}/manifest.json` с флагом `ready_for_review: true` и QC scores для каждого драфта.
6. Выведи итоговый список: «Готовы N драфтов на неделю W. Avg QC score: XX/20. Telegram-бот пингает Вадима для review».

## Правила

- **Не запускай post-drafter параллельно** — по одному на профиль, чтобы каждый имел чистый контекст.
- Если для какого-то профиля нет темы в плане — пропусти и явно укажи в финале.
- Если квартальный план не найден или устарел — STOP, попроси Вадима запустить `/quarterly-review` сначала.

## После выполнения

Не запускай `visual-brief`. Это последует после того, как Вадим апрувит каждый текст в Telegram.
