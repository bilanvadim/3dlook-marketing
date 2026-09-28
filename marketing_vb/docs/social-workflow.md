# Воркфлоу и роли, social-пайплайн — полный текст

> Вынесено из `CLAUDE.md` §9 2026-09-28 (токен-диета). `CLAUDE.md` грузится в контекст
> каждой сессии и каждого агента, который открыл файл в `marketing_vb/`; полный текст этой
> секции нужен не всем. В `CLAUDE.md` осталась выжимка с правилами, здесь — полный текст,
> дословно, с обоснованиями и историей. **Кто читает:** тот, кто меняет social-пайплайн или его команды. Координаторы `/post-batch` и `/post-one-profile` несут свои инструкции в файлах команд.
> При расхождении выжимки и этого файла прав этот файл: поправь выжимку.

## 9. Воркфлоу и роли

| Роль | Кто | Что делает |
|------|-----|------------|
| Копирайтер | `post-drafter` | 1 пост per профиль на основе SEO-статьи |
| Механический гейт | `scripts/post-lint.py` | Длина, хештеги, эмодзи, em dash, запрещённые слова, плейсхолдеры, published slug, числа против статьи и `proof-points.md`. Ноль токенов |
| Brand voice (пост) | `post-brand-checker` | 10/13-пунктный чек одного поста |
| QC (пост) | `post-quality-controller` | 20-балльная рубрика, выборка 3 из 9, sonnet, §14 |
| Сборка пака | `scripts/social_pack.py` | source · brief · prompt · qc-prompt · qc-plan · manifest · digest · report · scores |
| Дизайнер | Человек | Делает визуал сам, по `### Design tip` каждого поста в дайджесте (шаг `visual-brief` удалён 2026-09-20, решение Вадима: «дизайнер сам это делает») |
| Апрувер | Вадим (через Telegram) | Чекпоинты social и outbound. **SEO-статьи с 2026-09-21 идут без остановок** (plan → publish → git commit+push одним прогоном); Вадим ревьюит пост-фактум по финальному дайджесту и коммиту — см. `.claude/commands/new-article.md` «Режим без чекпоинтов» |
| Outbound | пайплайн `outbound/*` | Hypothesis → ... → Campaign analysis |
| SEO | пайплайн `seo/*` | Keywords → ... → Publish → trigger social |
| Brand guardian | `brand-checker` (shared) | Проверка тона / no-go / AI-сигнатур |

**Social workflow (основной режим — БАТЧ, решение Вадима 2026-09-20):** SEO-статья
готова → `mvb-run.py posts {slug} --batch` → ОДНА conductor-job `/post-batch {slug}` →
`social_pack.py batch-prompt --write` (только недостающие профили) → один `post-drafter`
(opus) пишет весь пак за заход → `post-lint.py` с гейтом ПО НАПИСАННЫМ профилям
(не `--all --gate`: ретро-правила валят shipped-посты — урок job #160) → `post-brand-checker` и
`post-quality-controller` по выборке qc-plan → manifest / digest / report скриптом →
Telegram апрув Вадима → дизайнер делает визуалы по `### Design tip` из дайджеста
(шага `visual-brief` больше нет, 2026-09-20). Основание: A/B по протоколу ниже
(bariatric-hub-refresh, коммит 1f2aea5) — батч 18.78/20 против 18.00 у fan-out при
полном слепом QC, линт 9/9 с первого прохода, ~$9-10 за пак против измеренных $25.
**Fan-out (`mvb-run.py posts {slug}` без флага) остаётся** для точечных пересборов:
он ставит job'ы только на профили без post.md. `/post-from-article {slug}` —
интерактивный fallback. Квартальный план для соцсетей не используется.

**Гейт «нет артефакта — нет done»:** Stop-hook `.claude/hooks/posts-artifact-gate.py`
не даёт сессии `/post-one-profile` и `/post-batch` завершиться, пока обещанные
post.md не на диске (класс job'ов #136/#158 от 2026-09-20: «жду драфтера» → done без
поста). Блокирует максимум дважды за сессию; дальше дыру закрывает re-run фильтр
`posts <slug>`.

`/post-from-article {slug}` делает то же в **одной** сессии и оставлен как fallback для
интерактивного прогона: замер 2026-08-28 показал, что координация в одной толстой сессии —
59% стоимости пака (25,5M токенов из 42,9M). Подробности и цифры — в шапках обоих файлов
команд.

**Механика — скриптами, не агентами.** `scripts/social_pack.py` (source · brief · prompt ·
qc-prompt · qc-plan · manifest · digest · report · scores) и `scripts/post-lint.py`.
Агенты пишут и судят; разрешение источника, сборка промптов, длины, числа, манифест и
дайджест — код. Промпт для `post-drafter` берётся **дословно** из
`social_pack.py prompt`: его первая секция байт-в-байт одинакова для всех девяти профилей,
и на этом держится общий кеш промпта (`subagentPromptCacheTtl: "1h"` в
`.claude/settings.json` — дефолт для сабагентов 5 минут, а профили идут с интервалом 4-6).

**Social workspace:** `workspace/social/articles/{slug}/{profile}/post.md`
`_run-brief.md` в той же папке генерируется (`social_pack.py brief`); руками правится
только секция между `HUMAN:START` / `HUMAN:END` — claims discipline и реальные визуалы
статьи.

### Модель по стадиям social-пайплайна

| Стадия | Модель | Почему |
|---|---|---|
| координатор job'а (`/post-batch`, `/post-one-profile`) | sonnet | `model:` во frontmatter команды; чистый диспетчер, текста не пишет (замер 2026-09-20: opus-координаторы были 82% стоимости пака) |
| `post-drafter` | **opus** | Единственная стадия, где пишется текст. Меняется только через A/B ниже |
| `post-brand-checker` | sonnet | Чек-лист по готовому тексту |
| `post-quality-controller` | sonnet | Вход компактный, механика уже проверена линтером |
| lint / manifest / digest / report | код | Токенов не тратит |

**Модель пишущей стадии меняется только по данным** — полный протокол A/B (5 шагов, решение принимает Вадим по дайджесту, не по среднему баллу) вынесен в `docs/model-ab-protocol.md` (2026-09-21). Это касается post-drafter, seo-writer и seo-editor одинаково: единственный рычаг, способный испортить текст.

