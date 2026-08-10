#!/usr/bin/env bash
# Regression test for route-profile.sh — task text → expected profile.
# Expectations carry the -sm suffix since the 2026-07-11 profile rename
# (full_stack_sm→dev-sm etc.). They did not, so 23 of 28 cases failed and the
# suite could no longer catch a real regression in the classifier.
# Run: ./test-route.sh   (exit 0 = all pass)
set -uo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
R="$DIR/route-profile.sh"
pass=0; fail=0

check() { # "<text>" <expected>
  local got; got="$("$R" "$1")"
  if [[ "$got" == "$2" ]]; then pass=$((pass+1)); printf '  ok    [%-9s] %s\n' "$2" "$1"
  else fail=$((fail+1)); printf '  FAIL  expected %s, got %s: %s\n' "$2" "$got" "$1"; fi
}

# SEO
check "подними нам органический трафик из Google" seo-sm
check "нужен SEO-аудит сайта и работа с ключевыми словами" seo-sm
check "проблемы с индексацией и sitemap, поправь canonical" seo-sm
check "improve our search rankings and fix Core Web Vitals" seo-sm
check "проанализируй ссылочный профиль и бэклинки" seo-sm

# MARKETING
check "запусти рекламную кампанию в Google Ads" marketing-sm
check "сделай контент-план и email-рассылку" marketing-sm
check "нужна маркетинговая стратегия и позиционирование бренда" marketing-sm
check "plan a paid media funnel and social campaign" marketing-sm
check "напиши копирайт для лендинга кампании" marketing-sm

# SECURITY
check "проверь приложение на уязвимости и OWASP" security-sm
check "сделай security-аудит и проверь RLS политики" security-sm
check "look for vulnerabilities and secret leaks" security-sm
check "нужен пентест и проверка auth" security-sm

# DEV (default / explicit)
check "сделай новую фичу и почини баг в API" dev-sm
check "отрефактори бэкенд и напиши миграцию базы данных" dev-sm
check "build a React component and deploy it" dev-sm
check "просто помоги разобраться с кодом" dev-sm
check "напиши unit-тесты для сервиса" dev-sm

# AMBIGUOUS (balanced specialized signals tie → ask). Note: when one domain's
# keywords dominate by count, the classifier returns that domain (the backbone
# suggests; Hermes handles true multi-intent by splitting + explicit override).
check "SEO и реклама" ambiguous              # seo=1, marketing=1 → tie
check "уязвимости и рассылка" ambiguous       # security=1, marketing=1 → tie
check "keyword research and a newsletter" ambiguous  # seo=1 (keyword), marketing=1 (newsletter)

# number → profile mapping (Hermes parses the user's "2")
checknum() { local got; got="$("$R" --num "$1")"; if [[ "$got" == "$2" ]]; then pass=$((pass+1)); printf '  ok    [--num %s ] %s\n' "$1" "$2"; else fail=$((fail+1)); printf '  FAIL  --num %s expected %s got %s\n' "$1" "$2" "$got"; fi; }
checknum 1 dev-sm
checknum 2 marketing-sm
checknum 3 seo-sm
checknum 4 security-sm
checknum 9 ambiguous

# menu text present
if "$R" --menu | grep -q "Какую систему запустить внутри Claude?"; then pass=$((pass+1)); echo "  ok    [--menu    ] question text"; else fail=$((fail+1)); echo "  FAIL  --menu missing question"; fi

echo; echo "$pass passed, $fail failed"
exit $(( fail > 0 ? 1 : 0 ))
