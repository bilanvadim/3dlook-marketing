#!/usr/bin/env bash
# Regression test for route-profile.sh — task text → expected profile.
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
check "подними нам органический трафик из Google" seo
check "нужен SEO-аудит сайта и работа с ключевыми словами" seo
check "проблемы с индексацией и sitemap, поправь canonical" seo
check "improve our search rankings and fix Core Web Vitals" seo
check "проанализируй ссылочный профиль и бэклинки" seo

# MARKETING
check "запусти рекламную кампанию в Google Ads" marketing_vb_sm
check "сделай контент-план и email-рассылку" marketing_vb_sm
check "нужна маркетинговая стратегия и позиционирование бренда" marketing_vb_sm
check "plan a paid media funnel and social campaign" marketing_vb_sm
check "напиши копирайт для лендинга кампании" marketing_vb_sm
# content/social phrasing (previously misrouted to dev — no marketing keyword)
check "сделай пост про телехелс в поддержку партнёра" marketing_vb_sm
check "напиши статью для блога про body composition" marketing_vb_sm
check "запусти сторис и пост в инстаграм" marketing_vb_sm
# no signal at all on a marketing-first box -> marketing_vb_sm baseline
check "помоги мне с этим" marketing_vb_sm

# SECURITY
check "проверь приложение на уязвимости и OWASP" security
check "сделай security-аудит и проверь RLS политики" security
check "look for vulnerabilities and secret leaks" security
check "нужен пентест и проверка auth" security

# DEV (default / explicit)
check "сделай новую фичу и почини баг в API" dev
check "отрефактори бэкенд и напиши миграцию базы данных" dev
check "build a React component and deploy it" dev
check "просто помоги разобраться с кодом" dev
check "напиши unit-тесты для сервиса" dev

# AMBIGUOUS (balanced specialized signals tie → ask). Note: when one domain's
# keywords dominate by count, the classifier returns that domain (the backbone
# suggests; Hermes handles true multi-intent by splitting + explicit override).
check "SEO и реклама" ambiguous              # seo=1, marketing=1 → tie
check "уязвимости и рассылка" ambiguous       # security=1, marketing=1 → tie
check "keyword research and a newsletter" ambiguous  # seo=1 (keyword), marketing=1 (newsletter)

# number → profile mapping (Hermes parses the user's "2")
checknum() { local got; got="$("$R" --num "$1")"; if [[ "$got" == "$2" ]]; then pass=$((pass+1)); printf '  ok    [--num %s ] %s\n' "$1" "$2"; else fail=$((fail+1)); printf '  FAIL  --num %s expected %s got %s\n' "$1" "$2" "$got"; fi; }
checknum 1 dev
checknum 2 marketing_vb_sm
checknum 3 marketing_vb
checknum 4 marketing
checknum 5 seo
checknum 6 security
checknum 9 ambiguous

# menu text present
if "$R" --menu | grep -q "Какую систему запустить внутри Claude?"; then pass=$((pass+1)); echo "  ok    [--menu    ] question text"; else fail=$((fail+1)); echo "  FAIL  --menu missing question"; fi

echo; echo "$pass passed, $fail failed"
exit $(( fail > 0 ? 1 : 0 ))
