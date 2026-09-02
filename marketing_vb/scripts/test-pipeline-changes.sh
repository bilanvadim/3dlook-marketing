#!/usr/bin/env bash
# test-pipeline-changes.sh — the regression suite for the 2026-09-02 pipeline changes.
#
# WHY THIS FILE EXISTS
# The audit it verifies (docs/seo-pipeline-audit-2026-09-02.md) makes exactly one argument:
# checks worth running are the ones a script runs, because ad-hoc greps are not repeatable.
# Shipping seven changes verified by ad-hoc greps would have contradicted the audit, so the
# verification is here instead.
#
# It covers items 1-7 of the audit's action list, plus the regressions that matter most:
# that the detector still runs after gaining its CARD table, and that the narrowed
# `positioned_as` pattern still licenses exactly one sentence and no more.
#
# The nine negative fixtures are built on the fly, so this is safe to run any time and needs
# no state from a previous run.
#
# USAGE
#     scripts/test-pipeline-changes.sh
#
# Exit 0 only if every check passes.

set -uo pipefail
cd "$(dirname "$0")/.." || exit 2

A=workspace/seo/articles/2026-08-31-ai-body-data-wellness-platforms-hub
P=workspace/seo/_context-packs/2026-08-31-ai-body-data-wellness-platforms-hub.yaml
FIX=$(mktemp -d)
trap 'rm -rf "$FIX"' EXIT

pass=0; fail=0
t()  { printf '%-58s ' "$1"; shift; if eval "$@" >/dev/null 2>&1; then echo "PASS"; pass=$((pass+1)); else echo "FAIL"; fail=$((fail+1)); fi; }
tn() { printf '%-58s ' "$1"; shift; if eval "$@" >/dev/null 2>&1; then echo "FAIL (should have failed)"; fail=$((fail+1)); else echo "PASS (correctly failed)"; pass=$((pass+1)); fi; }

# ---- build the negative fixtures -------------------------------------------------
# Each one injects a single defect into the known-good article and must be caught by the
# gate that owns it. A lint that only ever says PASS is worth nothing.
python3 - "$A/final.md" "$FIX" <<'PY'
import pathlib, shutil, sys
src, out = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
base = src.read_text()
CASES = {
 "t1_emdash":     ("It is not positioned as a medical device.", "It is not a device — and never was."),
 "t2_dexa":       ("Dual-energy X-ray absorptiometry (DXA)", "Dual-energy X-ray absorptiometry (DEXA)"),
 "t3_height205":  ("150 to 220 cm", "150 to 205 cm"),
 "t4_predweight": ("body composition estimates", "predicted weight and body composition values"),
 "t5_unsourced":  ("The mapping holds across most wellness platforms.",
                   "The mapping holds, and internal tests show 88% of members complete a 42 cm baseline."),
 "t6_bannedclaim":("It is not positioned as a medical device.", "FitXpress is SOC 2 certified and guarantees compliance."),
 "t7_badclaimid": ("<!-- claim: FX-001 -->", "<!-- claim: FX-999 -->"),
 "t8_m1":         ("Dual-energy X-ray absorptiometry (DXA)", "DXA"),
 "t9_nonslash":   ("https://3dlook.ai/content-hub/beyond-bmi-business/", "https://3dlook.ai/content-hub/beyond-bmi-business"),
 # An illustration whose ALT TEXT states a figure no approved claim supports. Alt text is
 # published copy, so this must fail exactly as prose would. Added 2026-09-02 while planning
 # the illustrations, when testing this case found two bugs of the opposite kind: the year in
 # `/uploads/2026/09/` was being read as a product figure, and the .webp asset URL was being
 # failed for missing a canonical trailing slash. t11 below guards those.
 "t10_alt_figure": ("## Progress visibility beyond scale weight",
                    "## Progress visibility beyond scale weight\n\n"
                    "![Progress view showing a 3.2 cm waist reduction over 8 weeks.]"
                    "(https://3dlook.ai/wp-content/uploads/2026/09/banner_1.webp)"),
}
# A legitimately illustrated article: asset URL plus figure-free alt text. This one must PASS.
POSITIVE = {
 "t11_asset_ok": ("## Progress visibility beyond scale weight",
                  "## Progress visibility beyond scale weight\n\n"
                  "![Wellness app progress view showing a waist measurement change while "
                  "bodyweight stays flat.]"
                  "(https://3dlook.ai/wp-content/uploads/2026/09/banner_1.webp)"),
}
for name, (old, new) in list(CASES.items()) + list(POSITIVE.items()):
    if old not in base:
        raise SystemExit(f"fixture anchor missing for {name}: {old[:60]!r}\n"
                         "The article changed. Update the anchor, do not delete the test.")
    d = out / name / src.parent.name
    d.mkdir(parents=True, exist_ok=True)
    (d / "final.md").write_text(base.replace(old, new, 1))
    shutil.copy(src.parent / "plan.md", d / "plan.md")
PY
[ $? -eq 0 ] || { echo "could not build fixtures"; exit 2; }

echo "--- 1. seo-writer can run its own linter ---"
t "Bash in all 3 seo-writer copies" '[ $(grep -l "^tools:.*Bash" ../claude_code/DEV/marketing_vb/plugins/mvb-seo/agents/seo-writer.md .claude/plugins/mvb-seo/0.2.0/agents/seo-writer.md .claude/agents/seo/seo-writer.md | wc -l) = 3 ]'
t "writer told to run article_lint.py" 'grep -q "article_lint.py" .claude/agents/seo/seo-writer.md'
t "writer forbidden to fabricate a verdict" 'grep -q "никогда не выдумывай его вывод" .claude/agents/seo/seo-writer.md'

echo "--- 2. external review moves to checkpoint 1 ---"
t "new-article.md documents outline review" 'grep -q "Внешнее рев.ю идёт на аутлайн" .claude/commands/new-article.md'
t "late-review recovery order documented" 'grep -q "Если рев.ю всё-таки пришло на чекпоинт 2" .claude/commands/new-article.md'
t "orchestrator wires lint into the SEO flow" 'grep -q "article_lint.py" .claude/agents/_shared/orchestrator.md'

echo "--- 3. article_lint.py ---"
t "final.md PASS"            "python3 scripts/article_lint.py $A/final.md"
t "draft.md PASS"            "python3 scripts/article_lint.py $A/draft.md"
t "plan.md --plan PASS"      "python3 scripts/article_lint.py $A/plan.md --plan"
t "--json is valid json"     "python3 scripts/article_lint.py $A/final.md --json | python3 -m json.tool"
t "--report runs"            "python3 scripts/article_lint.py $A/final.md --report"
for n in t1_emdash t2_dexa t3_height205 t4_predweight t5_unsourced t6_bannedclaim t7_badclaimid t8_m1 t9_nonslash t10_alt_figure; do
  tn "negative fixture: $n" "python3 scripts/article_lint.py $FIX/$n/$(basename $A)/final.md --pack $P"
done
t "--no-exit-code suppresses rc" "python3 scripts/article_lint.py $FIX/t3_height205/$(basename $A)/final.md --pack $P --no-exit-code"
t "illustrated article passes (asset url + clean alt)" "python3 scripts/article_lint.py $FIX/t11_asset_ok/$(basename $A)/final.md --pack $P"
t "asset url counted separately from page links" "python3 scripts/article_lint.py $FIX/t11_asset_ok/$(basename $A)/final.md --pack $P 2>&1 | grep -q 'asset_urls: 1'"

echo "--- 4. hard-bans card is generated, not hand-written ---"
t "card generates"            "python3 scripts/bans-card.py"
t "card --check clean"        "python3 scripts/bans-card.py --check"
t "card under 6 KB"           '[ $(wc -c <brand-assets/style-guides/hard-bans-card.md) -lt 6000 ]'
t "card marked GENERATED"     'head -1 brand-assets/style-guides/hard-bans-card.md | grep -q GENERATED'
t "writer points at the card" 'grep -q "hard-bans-card.md" .claude/agents/seo/seo-writer.md'
t "editor points at the card" 'grep -q "hard-bans-card.md" .claude/agents/seo/seo-editor.md'

echo "--- 5. plan split by audience ---"
t "planner writes plan-audit.md"       'grep -q "plan-audit.md" .claude/agents/seo/seo-planner.md'
t "planner emits target_words"         'grep -q "target_words" .claude/agents/seo/seo-planner.md'
t "publisher reads the audit file"     'grep -q "plan-audit.md" .claude/agents/seo/seo-publisher.md'
t "writer told NOT to read the audit"  'grep -q "plan-audit.md. не читай" .claude/agents/seo/seo-writer.md'

echo "--- 6. coordinator verification is one call ---"
t "report carries term-group balance"  "python3 scripts/article_lint.py $A/final.md --report 2>&1 | grep -q 'term group corporate'"
t "report carries per-section words"   "python3 scripts/article_lint.py $A/final.md --report 2>&1 | grep -q 'across 11 H2 sections'"

echo "--- 7. derived agent copies are generated from DEV ---"
t "sync --check clean"        "python3 scripts/sync-agent-copies.py --check"
t "sync --dry-run clean"      "python3 scripts/sync-agent-copies.py --dry-run"
t "old checker agrees"        "python3 scripts/check-agent-copies.py"

echo "--- regressions ---"
t  "detector runs after the CARD addition"   "python3 brand-assets/style-guides/scripts/detect-ai-tells.py $A/final.md --channel article --summary"
t  "detector verdict still CLEAN"            "python3 brand-assets/style-guides/scripts/detect-ai-tells.py $A/final.md --channel article --summary | grep -q CLEAN"
t  "medical-device sentence is licensed"     'echo "It is not positioned as a medical device." | python3 brand-assets/style-guides/scripts/detect-ai-tells.py --stdin --channel article | python3 -c "import sys,json; sys.exit(0 if not json.load(sys.stdin)[\"hard_fails\"] else 1)"'
tn "any other positioned-as still fails"     'echo "It is not positioned as a diagnostic tool." | python3 brand-assets/style-guides/scripts/detect-ai-tells.py --stdin --channel article | python3 -c "import sys,json; sys.exit(0 if not json.load(sys.stdin)[\"hard_fails\"] else 1)"'
t  "context pack is valid yaml"              "python3 -c \"import yaml; yaml.safe_load(open('$P'))\""
t  "every new script parses without warning" 'for f in scripts/article_lint.py scripts/bans-card.py scripts/sync-agent-copies.py; do python3 -W error::SyntaxWarning -c "import ast; ast.parse(open(\"$f\").read())" || exit 1; done'

echo
echo "######## $pass passed, $fail failed ########"
[ "$fail" = 0 ]
