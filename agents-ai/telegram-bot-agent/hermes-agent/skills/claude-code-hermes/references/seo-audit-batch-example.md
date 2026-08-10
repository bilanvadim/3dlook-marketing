# Пример: SEO-аудит ASCoFaçade — полная разбивка на батчи

## Контекст
Полный SEO-аудит на 18 разделов (P0/P1/P2), ~8,500 знаков техзадания.
Проект: Next.js App Router, ~50 файлов, большие CLAUDE.md.
Дата: 2026-07-21. Модель: claude-opus-4-8.

## Стратегия: 7 батчей, 7 коммитов

### Батч 1: P0 — canonical + H1 + title (success, $1.08, 27 turns)
- canonical ascofacade.fr, double branding fix в 6+ страницах, H1 homepage, title/meta главной
- 21 файл изменён (часть была pre-modified до аудита)
- Промпт inline: короткий, без спецсимволов — прошёл без файла

### Батч 2: P0 — contact + blog + email (success, $0.87, 18 turns)
- email → contact@ascofacade.fr (constants.ts + legalConfig + sendEmail.ts)
- contact metadata/H1, инфо-блок (адрес, SIRET, décennale, WhatsApp, horaires)
- Блог уже существует (app/(marketing)/blog/), гео Domaine des Oliviers = Goudargues везде
- 3 файла изменено

### Батч 3: P0 — sitemap + robots + structured data (success, $0.86, 17 turns)
- robots.ts (новый), sitemap.ts (динамический: статика + portfolio-catalog + блог из БД)
- JsonLd: HomeAndConstructionBusiness→LocalBusiness, убран AggregateRating (Google self-serving), sameAs/logo/image
- Gmail cleanup по всему проекту — остатков не найдено

### Батч 4: P1 — 4 service pages (таймаут 600s, но ВСЁ создано)
- 4 новых страницы услуг по 22-24 KB каждая + улучшение rejointoiement
- Промпт через файл `/tmp/claude-p1-services.txt` (4.5 KB)
- Прямой `claude -p "$(cat ...)"` дал syntax error → вторая попытка с `$(cat file)` сработала
- Результат: 4 page.tsx + 4 layout.tsx + rejointoiement улучшен (+136 строк)

### Батч 5: P1 — 6 city pages (3 таймаута, добивка)
- Первый запуск: 600s таймаут → 4/6 готовы (bagnols, uzes, orange, pont-saint-esprit)
- Goudargues и Saint-Gervais: layout.tsx есть, page.tsx нет
- Второй запуск: cp шаблона Bagnols → адаптация узким промптом → всё равно max_turns
- Saint-Gervais добит python3-heredoc: замена Bagnols→Saint-Gervais в 17 местах

### Батч 6: P1 — Case studies (success, $2.58, 30 turns)
- Claude создал `lib/case-study.ts`: projectH1, metaTitle, serviceLink, zoneHref, buildCaseStudy, relatedProjects
- 3 файла (+572 строки). Все 11 реализаций получили секции через один модуль.
- BreadcrumbList JSON-LD на каждую реализацию

### Батч 7: P2 — блог + перелинковка (max_turns на 31 ходе, $3.40)
- lib/blog-fallback.ts с 8 SEO-статьями
- Внутренняя перелинковка: ServicesGrid, Footer, все 6 city pages
- 14 файлов (+634 строки, включая BlogLinks.tsx)

### Экстренный fix: FilterBar.tsx + Supabase (2 доп. батча)
- Предсуществующая ошибка `STATUS_TABS` undefined валила ВСЕ деплои Vercel (5 подряд Error)
- Добавлены STATUS_TABS, activeStatus/onSetStatus пропсы
- Позже: убрана логика разделения Tous/Terminés/En Cours — один unified список
- Supabase: pavillon-naturea + maison-beauregard → "termine" через временный API-роут
- Данные в Supabase ≠ данные в локальном JSON-каталоге

## Ключевые выводы
1. Батчи по 3-5 задач оптимальны ($0.85-$1.40, 15-27 turns)
2. 4+ новых страниц → таймаут 600s вероятен, закладывай добивку
3. При таймауте проверяй `git status --short` — работа часто сделана
4. Не перезапускай тот же промпт — добей недостающее узким промптом или python3
5. Файловые промпты через /tmp/ обязательны для скобок `()` и акцентов
6. Claude создаёт абстракции (lib/case-study.ts) — дай ему свободу, не требуй буквально «каждый файл»
7. `npx tsc --noEmit` перед ПЕРВЫМ пушем — предсуществующие ошибки валят деплой
8. `&apos;` в JSX от Claude — заменять на `'` через grep + python3
9. Коммить после каждого батча, Vercel проверять только в конце (экономит ~90s × N)
10. execute_code sandbox не видит файлы проекта — только terminal+python3
11. Supabase-данные на Vercel приоритетнее JSON-fallback локально: обновлять через временный API-роут
12. Суммарно: ~$11 за 7 батчей + 2 доп. Среднее ~$1.20/батч
