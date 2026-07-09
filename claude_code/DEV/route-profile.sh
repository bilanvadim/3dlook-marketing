#!/usr/bin/env bash
# route-profile.sh — deterministic intent → profile classifier.
#
# Prints exactly ONE token on stdout: dev | seo | marketing_vb_sm | security | ambiguous
# Keyword-scored over the task text (RU + EN, case-insensitive, substring match so
# stems like "ранжир" catch "ранжирование"). This is the reliable backbone Hermes
# calls instead of classifying in its head; the orchestrator layer only handles
# explicit overrides and 'ambiguous'.
#
# Decision rule:
#   spec_best = max(seo, marketing, security)
#   - >1 specialized tied at spec_best (>0)        -> ambiguous  (ask)
#   - spec_best == 0                                -> dev if any dev signal, else marketing_vb_sm
#                                                       (marketing-first box: no-signal defaults to the mix, not code)
#   - dev score strictly > spec_best               -> dev        (heavy-dev signal wins a weak specialized one)
#   - otherwise                                     -> the winning specialized profile
#
# Usage:
#   route-profile.sh "<task text>"         -> profile token
#   route-profile.sh --explain "<text>"    -> scores on stderr, token on stdout
# (no `set -e`: arithmetic (( )) that evaluates to 0 returns exit 1 and would
#  abort the classifier mid-way.)
set -uo pipefail

# --menu : print the exact confirmation question Hermes posts to chat.
# --num N: map a numeric reply to a profile.
#   1 Dev · 2 Marketing (VB×SM mix) · 3 Marketing VB (Vadim only) ·
#   4 Marketing SM (Sergiy generic) · 5 SEO · 6 Security.
# On this (marketing-first) repo the keyword scorer returns marketing intent as
# marketing_vb_sm (Vadim's brand-grounded VB×SM mix) — see SYSTEMS.md — so ad-hoc
# and conductor paths land in the brand contour, not generic SM. Use --num 4 (or the
# 6-way menu) to pick generic marketing (SM) / marketing_vb / any other system.
case "${1:-}" in
  --menu)
    printf '%s\n' "Какую систему запустить внутри Claude?" \
      "1. Dev" \
      "2. Marketing (микс VB×SM)" \
      "3. Marketing VB (только система Вадима)" \
      "4. Marketing SM (общая система Сергея)" \
      "5. SEO" \
      "6. Security"
    exit 0 ;;
  --num)
    case "${2:-}" in
      1) echo dev ;; 2) echo marketing_vb_sm ;; 3) echo marketing_vb ;;
      4) echo marketing ;; 5) echo seo ;; 6) echo security ;;
      *) echo "ambiguous"; exit 2 ;;
    esac
    exit 0 ;;
esac

EXPLAIN=0
[[ "${1:-}" == "--explain" ]] && { EXPLAIN=1; shift; }
TEXT="${*:-}"
[[ -n "$TEXT" ]] || { echo "ambiguous"; exit 0; }
t=$(printf '%s' "$TEXT" | tr '[:upper:]' '[:lower:]')

# token lists (| separated, ERE-escaped where needed). Substring semantics.
SEO='seo|сео|serp|ранжир|ранкинг|поисков|органическ|трафик|ключев|keyword|backlink|бэклинк|ссылочн|индексац|индексир|sitemap|robots\.txt|canonical|hreflang|crawl|краул|core web vitals|метатег|meta tag|on-page|сниппет|поисковую выдачу|google search'
MKT='маркетинг|marketing|кампани|campaign|реклам|\bads\b|\bad campaign|paid media|платн(ый|ую) трафик|воронк|funnel|рассылк|email|e-mail|newsletter|соцсет|social|\bsmm\b|контент|content|копирайт|copywrit|сторител|бренд|\bbrand\b|позициони|positioning|\bgtm\b|go-to-market|\bлид(ы|ов|ген)|\blead|\bcrm\b|retention|удержан|нёртер|nurtur|аудитори|креатив|\broas\b|\bcpa\b|пост|\bpost|публикац|publish|стать[яию]|\barticle|блог|\bblog|тред|\bthread|твит|\btweet|linkedin|instagram|\bfacebook|сторис|reels|анонс|announc'
SEC='безопасн|security|уязвим|vulnerab|pentest|пентест|owasp|\brls\b|секрет|secret|эксплойт|exploit|\bcve\b|injection|инъекц|xss|csrf|threat|penetration|харден|hardening'
DEV='\bкод|\bcode|фич[аеуи]|feature|\bбаг|\bbug|багфикс|рефактор|refactor|деплой|deploy|\bapi\b|endpoint|эндпоинт|миграц|migration|база данных|database|\bschema|схем[ауы]|frontend|backend|компонент|component|юнит-тест|unit test|\bunit\b|\btests?\b|\bтесты\b|e2e|\bbuild\b|сборк|typescript|react|next\.js|запусти прилож|почини'

score() { printf '%s' "$t" | grep -oiE "$1" 2>/dev/null | wc -l | tr -d ' '; }
s=$(score "$SEO"); m=$(score "$MKT"); c=$(score "$SEC"); d=$(score "$DEV")

if (( EXPLAIN )); then echo "scores: seo=$s marketing=$m security=$c dev=$d" >&2; fi

# specialized best + tie detection
best=$s; winner=seo
(( m > best )) && { best=$m; winner=marketing_vb_sm; }
(( c > best )) && { best=$c; winner=security; }
ties=0
(( s == best )) && ((ties++)); (( m == best )) && ((ties++)); (( c == best )) && ((ties++))

if (( best == 0 )); then
  # no specialized signal: explicit dev keywords -> dev; otherwise this
  # marketing-first box defaults to Vadim's brand-grounded mix.
  if (( d > 0 )); then echo dev; else echo marketing_vb_sm; fi
elif (( ties > 1 )); then
  echo ambiguous
elif (( d > best )); then
  echo dev
else
  echo "$winner"
fi
