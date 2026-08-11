#!/usr/bin/env python3
"""Labelled cases for ops/task-heaviness.py. Run it after touching the rules:
    python3 ops/test-task-heaviness.py    # exits non-zero on any wrong verdict

Every HEAVY case here is a task the everyday small model demonstrably fumbles;
every light one is traffic that used to trip the old switcher rule — acks, status
questions, a one-line typo fix, a forwarded client message. Two of these cases are
why the merged version exists at all: "Отрефактори…" scored ZERO under the old
anchored regex, and the billing brief scored 2 of 3 because three heavy intents
were capped at two points.
"""
import importlib.util, sys
import os
spec = importlib.util.spec_from_file_location("th", os.path.join(os.path.dirname(os.path.abspath(__file__)), "task-heaviness.py"))
th = importlib.util.module_from_spec(spec); spec.loader.exec_module(th)

CASES = [
 (True,  "Разберись, почему у нас падает деплой на Vercel после мержа: логов нет, воспроизводится только в прод-окружении. Нужна первопричина, а не заглушка."),
 (True,  "Спроектируй архитектуру биллинга: тарифы, пробный период, вебхуки Stripe, идемпотентность, миграция существующих подписок. Опиши схему БД и точки отказа."),
 (True,  "Проанализируй все 9 профилей соцсетей и сравни, где просел охват за квартал, дай план правок по приоритету"),
 (True,  "Отрефактори модуль оплаты: сейчас логика размазана по 4 файлам, дублируется валидация, тесты падают через раз. Хочу единый сервис и внятные границы."),
 (True,  """Сервис уходит в 100% CPU через час работы, вот трейс:
```
Traceback (most recent call last):
  File "/srv/app/worker.py", line 88, in loop
    await queue.get()
```
Похоже на утечку или гонку. Найди причину."""),
 (True,  "Please investigate why the worker deadlocks under load and compare our queue design with a pull-based one; propose a migration plan."),
 (True,  "Нужен аудит безопасности: проверь авторизацию, RLS-политики, хранение секретов и зависимости во всех сервисах, отчёт с приоритетами."),
 (False, "ок"),
 (False, "спасибо, всё понятно"),
 (False, "Продолжай, пожалуйста, я подожду пока закончится текущая задача и потом посмотрим что вышло"),
 (False, "А почему падает?"),
 (False, "Какая сейчас модель стоит в конфиге и на каком порту работает прокси?"),
 (False, "/heavy"),
 (False, "Поправь опечатку в заголовке на главной странице: написано 'Приемущества', надо 'Преимущества'. Файл src/pages/index.tsx, строка примерно 40."),
 (False, "↪️ Пересланное сообщение от клиента: Здравствуйте! Хотел уточнить, можно ли сделать интеграцию с нашей CRM и сколько это будет стоить примерно?"),
 (False, "Да, давай поехали, всё верно, начинай выполнять как договорились и потом отчитайся мне в этот топик"),
 (False, "Скинь мне ссылку на прод и скажи, задеплоилось ли последнее изменение с кнопкой в футере, я проверю сам глазами"),
 (False, "Всегда пиши мне по-русски, пожалуйста, и не сокращай ответы — мне удобнее читать полностью, когда всё расписано"),
]
ok = bad = 0
print(f'{"ожидание":<9} {"вердикт":<7} {"балл":>4}  причины / текст')
print("─"*112)
for exp, txt in CASES:
    pts, why = th.score(txt); got = pts >= th.THRESHOLD
    good = got == exp; ok, bad = (ok+1, bad) if good else (ok, bad+1)
    print(f'{"HEAVY" if exp else "light":<9} {"heavy" if got else "light":<7} {pts:>4}  {"✓" if good else "✗ ОШИБКА"} {txt[:48]!r}')
    if why: print(f'{"":>23} → {"; ".join(why)}')
print(f"\nитог: {ok}/{len(CASES)} верно, ошибок {bad}")
sys.exit(1 if bad else 0)
