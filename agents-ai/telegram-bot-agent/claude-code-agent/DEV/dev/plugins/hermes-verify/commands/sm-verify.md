---
description: Прогнать верификацию по протоколу — независимо перезапустить гейты (ultracite/typecheck/test/build), оценить кодом-ревьюером 0-100, доказать работоспособность runtime-verifier'ом (front+back+db, e2e), и зациклить ретраи до прохождения или эскалации
argument-hint: "[feature-slug] (по умолчанию — текущая фича)"
---
Ты — оркестратор Fullstack agents. Прогони **протокол верификации** для: **$ARGUMENTS** (если пусто — текущая фича в `.claude/scratchpad/`).

Следуй скиллу `verification-protocol`:
1. **Независимо перезапусти гейты** (не верь отчётам исполнителя): `npx ultracite lint` → `tsc --noEmit`/typecheck → `npm test` → `npm run build`. Любой провал → score=0, в ретрай (ревьюера не зовём — экономим).
2. Вызови `code-reviewer` — оценка 0-100 + verdict (approve/request_changes/block), проверка каждого acceptance-критерия с доказательством, против policy-packs нужного слоя.
3. Если approve (≥85, без critical) → вызови `runtime-verifier`: поднять db→back→front, прогнать Playwright e2e + smoke по живому стеку. runtime fail = critical → ретрай.
4. Ретрай-цикл: накопленные критики, baseline-reset рабочего дерева, progress-delta (регрессия или плато <3 → стоп), needs-review (≥70 и рост на потолке попыток → к человеку), иначе block.
5. На block/needs-review — эскалация человеку (в автономе — Telegram через дирижёр) со score, топ-issue и диффом.

Покажи мне итог: финальный score, verdict, статус каждого гейта (вкл. ultracite и runtime), какие acceptance-критерии доказаны (и чем), и что осталось. «Готово» = approve ≥85 + runtime pass + все AC verified.
