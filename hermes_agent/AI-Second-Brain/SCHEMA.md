# Wiki Schema

## Domain
Долгосрочная база знаний Hermes Agent / «второй мозг» Сергея: проекты и инфраструктура,
принятые решения, research и заметки, сущности (люди, компании, модели, сервисы), сравнения.
Источник истины для кросс-проектной памяти (паттерн Andrej Karpathy's LLM Wiki).

## Conventions
- Имена файлов: lowercase, через дефис, без пробелов (`supabase-vps.md`).
- Каждая страница начинается с YAML-фронтматтера (см. ниже).
- Связи — через `[[wikilinks]]` (минимум 2 исходящие ссылки на страницу).
- При обновлении страницы — обновлять поле `updated`.
- Каждую новую страницу добавлять в `index.md` в нужную секцию.
- Каждое действие дописывать в `log.md`.
- Provenance: на страницах, синтезирующих 3+ источника, в конце абзацев ставить
  `^[raw/articles/source-file.md]`, чтобы проследить источник утверждения.

## Frontmatter
```yaml
---
title: Заголовок страницы
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [из таксономии ниже]
sources: [raw/articles/source-name.md]
confidence: high | medium | low
contested: true
contradictions: [other-page-slug]
---
```

### raw/ Frontmatter
```yaml
---
source_url: https://example.com/article
ingested: YYYY-MM-DD
sha256: <hex digest тела источника после фронтматтера>
---
```

## Tag Taxonomy
Добавлять новые теги СЮДА перед использованием.
- Инфраструктура: vps, docker, supabase, n8n, hermes, model-router, networking, security
- Проекты: project, orchestrator, fullstack-agents, ascofacade, simplifyeu
- Сущности: person, company, lab, model, service, tool
- Техника: architecture, decision, research, comparison, howto, postmortem
- Мета: timeline, controversy, prediction, open-question
