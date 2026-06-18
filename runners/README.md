# Runners

Runner-ы — это **координаторы пайплайнов**. Они либо bash-скрипты (для линейных пайплайнов), либо отдельные субагенты (когда нужно ветвление, чтение feedback, автодетект состояния).

## Что есть

| Файл | Тип | Покрывает | Когда вызывается |
|------|-----|-----------|------------------|
| `weekly-posts.sh` | bash | Линейный: post-drafter × N профилей | Cron / руками еженедельно |
| `outbound-runner.md` | subagent | Branching: 8 шагов с чекпоинтами | Через `/outbound [stage]` |
| `seo-runner.md` | subagent | Branching: 8 шагов + N section-writes | Через `/new-article [stage]` |

## Почему два разных подхода

**Bash для weekly-posts:** там один и тот же агент крутится в цикле по списку профилей. Никаких решений «что делать дальше». Cron-friendly.

**Subagent для outbound и SEO:** нужно читать `feedback.md`, понимать, что Вадим запросил Edit, переключаться между путями. Это решения на уровне LLM.

## Cron (опционально)

`crontab -e`:

```cron
# Запуск пайплайна постов каждый понедельник в 10:00
0 10 * * 1 /home/vadim/marketing-claude-code/runners/weekly-posts.sh >> /var/log/marketing/weekly.log 2>&1

# Каждый день в 9:00 проверять новые ответы в outbound (если есть свежий responses-raw.csv)
0 9 * * * cd /home/vadim/marketing-claude-code && claude -p "/outbound responses" --dangerously-skip-permissions
```

## Логи

Все runner-ы должны писать в `/var/log/marketing/`:

```bash
mkdir -p /var/log/marketing
chown vadim:vadim /var/log/marketing
```

## Запуск через Claude Code headless

Любой runner-subagent вызывается через:

```bash
cd /home/vadim/marketing-claude-code
claude -p "/outbound validate 2026-04-28-insurance" \
  --output-format json \
  --max-turns 30 \
  --dangerously-skip-permissions
```

Это и есть способ автоматизации без человека-в-чате. Но **чекпоинты Вадима** всегда остаются — runner шлёт уведомления и останавливается.
