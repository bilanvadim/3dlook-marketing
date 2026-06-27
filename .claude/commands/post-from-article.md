---
description: Создаёт посты для всех профилей соцсетей на основе готовой SEO-статьи
argument-hint: "<article-slug>"
---

Создай посты для всех активных профилей на основе статьи $1.

## Шаги

1. **Найди publish-package.md** статьи:
   `workspace/seo/articles/$1/publish-package.md`
   Если файл не найден — STOP, сообщи Вадиму.
   Если `status` в frontmatter не `approved_for_publish` — STOP, сообщи что статья ещё не прошла апрув.

2. **Определи список профилей** из CLAUDE.md секция 5. Бери только те, у которых `posts_per_week > 0`.

3. **Для каждого профиля последовательно** запусти субагент `post-drafter` с параметрами:
   - `article_path`: `workspace/seo/articles/$1/publish-package.md`
   - `profile`: текущий профиль

4. **Если `AUTO_QC_ENABLED=true`** в CLAUDE.md секция 14 — после каждого `post-drafter` запусти `quality-controller`:
   ```
   Use quality-controller to evaluate workspace/social/articles/$1/{profile}/post.md.
   Pass: agent_name=post-drafter, track=social, artifact_type=post.
   ```

5. **После всех профилей** — убедись что `workspace/social/articles/$1/manifest.json` обновлён с `ready_for_review: true` и QC scores.

6. Выведи итог: «Готовы N постов для статьи $1. Telegram-бот отправит Вадиму на апрув».

## Правила

- **Не запускай post-drafter параллельно** — по одному на профиль, чистый контекст.
- Если для какого-то профиля `posts_per_week = 0` или профиль задизейблен — пропусти, укажи в финале.
- `visual-brief` **не запускать** здесь — только после апрува текста Вадимом в Telegram.
