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
# that the detector still runs after gaining its CARD table, and that `positioned_as` licenses
# no sentence at all: since 2026-09-11 the medical-device boundary is written directly,
# "FitXpress is not a medical device.", and the old form fails like any other.
#
# The negative fixtures are built on the fly from a FROZEN known-good article in
# scripts/fixtures/article-known-good/, so this is safe to run any time and needs no state from a
# previous run.
#
# Why frozen (2026-09-11): the suite used to build everything from the live wellness hub draft in
# workspace/. That draft kept moving through review rounds (2,790 prose words against a plan target
# of 1,750, then the sentence-length gate, then the medical-device ruling), and ten checks failed
# for reasons that had nothing to do with the code under test. A fixture changes only when a test
# needs it to. The article is the editor's final of the occupational-health intake piece plus
# claim markers; its pack is a frozen copy of that article's context pack.
#
# USAGE
#     scripts/test-pipeline-changes.sh
#
# Exit 0 only if every check passes.

set -uo pipefail
cd "$(dirname "$0")/.." || exit 2

A=scripts/fixtures/article-known-good
P=$A/context-pack.yaml
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
 "t1_emdash":     ("FitXpress is not a medical device.", "FitXpress is not a device — and never was."),
 "t2_dexa":       ("Equipment-based testing and physical examination continue on-site.",
                   "Equipment-based testing, a DEXA reading and physical examination continue on-site."),
 "t3_height205":  ("Repeatability testing used a real-world customer dataset with five scans per participant.",
                   "Repeatability testing used a real-world customer dataset of people 150 to 205 cm tall."),
 "t4_predweight": ("80+ body measurements, BMI, and a session timestamp.",
                   "80+ body measurements, BMI, predicted weight and body composition values, and a session timestamp."),
 "t5_unsourced":  ("The steps are similar; their timing and location change.",
                   "The steps are similar, and internal tests show 88% of members complete a 42 cm baseline."),
 "t6_bannedclaim":("FitXpress is not a medical device.", "FitXpress is SOC 2 certified and guarantees compliance."),
 "t7_badclaimid": ("<!-- claim: FX-001 -->", "<!-- claim: FX-999 -->"),
 "t8_m1":         ("under the General Data Protection Regulation (GDPR)", "under GDPR"),
 "t9_nonslash":   ("https://3dlook.ai/content-hub/occupational-health-screening-software/",
                   "https://3dlook.ai/content-hub/occupational-health-screening-software"),
 # An illustration whose ALT TEXT states a figure no approved claim supports. Alt text is
 # published copy, so this must fail exactly as prose would. Added 2026-09-02 while planning
 # the illustrations, when testing this case found two bugs of the opposite kind: the year in
 # `/uploads/2026/09/` was being read as a product figure, and the .webp asset URL was being
 # failed for missing a canonical trailing slash. t11 below guards those.
 "t10_alt_figure": ("## Where FitXpress fits",
                    "## Where FitXpress fits\n\n"
                    "![Progress view showing a 3.2 cm waist reduction over 8 weeks.]"
                    "(https://3dlook.ai/wp-content/uploads/2026/09/banner_1.webp)"),
 # Accuracy discipline, added 2026-09-02 when the live framework article became the canonical
 # source for accuracy wording (brand-assets/product-info/accuracy-formulations.md). Until
 # 2026-09-11 these five sat in a dict named POSITIVE that a second POSITIVE overwrote, so their
 # fixtures were never built and `tn` counted the missing file as a correct failure.
 "t12_wrong_acc":  ("96-97%", "98.5% accuracy"),
 "t13_95_repeat":  ("reported accuracy was approximately 96-97%",
                    "reported repeatability was 95% consistency and accuracy was approximately 96-97%"),
 "t14_mixed_bench":("1.5-2.0 cm",
                    "1.5-2.0 cm, and the ISO 8559 benchmark puts session-to-session repeatability at 0.40 cm"),
 "t15_permeasure": ("reported accuracy was approximately 96-97%",
                    "reported waist error was 2.14 cm and accuracy was approximately 96-97%"),
 "t16_bare_dexa":  ("physical examination continue on-site when they require equipment",
                    "physical examination continue on-site, as a DEXA scan does, when they require equipment"),
}
# These two must PASS: a legitimately illustrated article (asset URL plus figure-free alt text),
# and DEXA licensed when DXA is on the same line (the older spelling carries the search volume and
# one published slug already uses it).
POSITIVE = {
 "t11_asset_ok": ("## Where FitXpress fits",
                  "## Where FitXpress fits\n\n"
                  "![Guided capture screen leading to a structured measurement record.]"
                  "(https://3dlook.ai/wp-content/uploads/2026/09/banner_1.webp)"),
 "t17_dexa_paired":("Equipment-based testing and physical examination continue on-site.",
                    "Equipment-based testing, such as dual-energy X-ray absorptiometry (DXA), also written DEXA, "
                    "and physical examination continue on-site."),
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
t "final.md PASS"            "python3 scripts/article_lint.py $A/final.md --pack $P"
t "draft.md PASS"            "python3 scripts/article_lint.py $A/draft.md --pack $P"
t "plan.md --plan PASS"      "python3 scripts/article_lint.py $A/plan.md --plan"
t "--json is valid json"     "python3 scripts/article_lint.py $A/final.md --pack $P --json | python3 -m json.tool"
t "--report runs"            "python3 scripts/article_lint.py $A/final.md --pack $P --report"
# A fixture that was never built must FAIL here, not count as a correct failure: before
# 2026-09-11 five of these passed on a missing file.
for n in t1_emdash t2_dexa t3_height205 t4_predweight t5_unsourced t6_bannedclaim t7_badclaimid t8_m1 t9_nonslash t10_alt_figure \
         t12_wrong_acc t13_95_repeat t14_mixed_bench t15_permeasure t16_bare_dexa; do
  tn "negative fixture: $n" "test ! -f $FIX/$n/$(basename $A)/final.md || python3 scripts/article_lint.py $FIX/$n/$(basename $A)/final.md --pack $P"
done
t "--no-exit-code suppresses rc" "python3 scripts/article_lint.py $FIX/t3_height205/$(basename $A)/final.md --pack $P --no-exit-code"
t "illustrated article passes (asset url + clean alt)" "python3 scripts/article_lint.py $FIX/t11_asset_ok/$(basename $A)/final.md --pack $P"
t "DEXA licensed when paired with DXA"    "python3 scripts/article_lint.py $FIX/t17_dexa_paired/$(basename $A)/final.md --pack $P"
t "accuracy gate sees the framework link" "python3 scripts/article_lint.py $A/final.md --pack $P 2>&1 | grep -q 'links_to_framework: True'"
t "asset url counted separately from page links" "python3 scripts/article_lint.py $FIX/t11_asset_ok/$(basename $A)/final.md --pack $P 2>&1 | grep -q 'asset_urls: 1'"
# Sentence length, added 2026-09-11 from the editor's final of the occupational-health intake
# article (brand-assets/style-guides/editorial-rewrites.md). Her text must pass and the revision
# she sent back must fail; if the thresholds drift, one of these two breaks first. Both grep for
# the gate's own line, so a crash cannot pass as a correct failure.
O=workspace/seo/articles/2026-09-03-manual-vs-digital-intake-occupational-health
t "sentence gate passes the editorial final" "python3 scripts/article_lint.py $O/editorial-final-2026-09-11.md --no-exit-code | grep -q '^\[ok  \] sentence length'"
t "sentence gate fails the revision she sent back" "python3 scripts/article_lint.py $O/final.md --no-exit-code | grep -q '^\[FAIL\] sentence length'"
# Gate 7 softened 2026-09-11: the H1 and one H2 are enough, the first paragraph is information.
# The editor's final keeps the keyword out of its first paragraph, so it is the test case.
t "keyword gate passes with H1 and one H2 only" "python3 scripts/article_lint.py $O/editorial-final-2026-09-11.md --no-exit-code | grep -q '^\[ok  \] keyword placement'"

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
t "report carries term-group balance"  "python3 scripts/article_lint.py $A/final.md --pack $P --report 2>&1 | grep -q 'term group corporate'"
t "report carries per-section words"   "python3 scripts/article_lint.py $A/final.md --pack $P --report 2>&1 | grep -q 'across 9 H2 sections'"

echo "--- 7. derived agent copies are generated from DEV ---"
t "sync --check clean"        "python3 scripts/sync-agent-copies.py --check"
t "sync --dry-run clean"      "python3 scripts/sync-agent-copies.py --dry-run"
t "old checker agrees"        "python3 scripts/check-agent-copies.py"

echo "--- regressions ---"
# The detector's known-clean article is the frozen fixture.
t  "detector runs after the CARD addition"   "python3 brand-assets/style-guides/scripts/detect-ai-tells.py $A/final.md --channel article --summary"
t  "detector verdict still CLEAN"            "python3 brand-assets/style-guides/scripts/detect-ai-tells.py $A/final.md --channel article --summary | grep -q CLEAN"
t  "direct medical-device sentence passes"   'echo "FitXpress is not a medical device." | python3 brand-assets/style-guides/scripts/detect-ai-tells.py --stdin --channel article | python3 -c "import sys,json; sys.exit(0 if not json.load(sys.stdin)[\"hard_fails\"] else 1)"'
tn "positioned-as medical-device sentence fails" 'echo "It is not positioned as a medical device." | python3 brand-assets/style-guides/scripts/detect-ai-tells.py --stdin --channel article | python3 -c "import sys,json; sys.exit(0 if not json.load(sys.stdin)[\"hard_fails\"] else 1)"'
tn "any other positioned-as still fails"     'echo "It is not positioned as a diagnostic tool." | python3 brand-assets/style-guides/scripts/detect-ai-tells.py --stdin --channel article | python3 -c "import sys,json; sys.exit(0 if not json.load(sys.stdin)[\"hard_fails\"] else 1)"'
# Terminology Doc sync 2026-09-14: the two approved IEEE sentences and the reviewed output wording
# must stay clean, and the banned forms must fail. If a pattern is loosened or tightened, one side breaks.
t  "approved IEEE sentences pass"            'printf "Winner, 2019 Retail Digital Transformation Grand Challenge, run by the 3D Retail Coalition with Kalypso and IEEE.\nParticipant in the IEEE 3D Body Processing working group, which is developing standards for mobile body scanning.\n" | python3 brand-assets/style-guides/scripts/detect-ai-tells.py --stdin --channel article | python3 -c "import sys,json; sys.exit(0 if not json.load(sys.stdin)[\"hard_fails\"] else 1)"'
tn "IEEE-certified fails"                    'echo "3DLOOK is IEEE-certified." | python3 brand-assets/style-guides/scripts/detect-ai-tells.py --stdin --channel article | python3 -c "import sys,json; sys.exit(0 if not json.load(sys.stdin)[\"hard_fails\"] else 1)"'
tn "old IEEE proof-point row fails"          'echo "Member of Mobile Body Scanning Standards." | python3 brand-assets/style-guides/scripts/detect-ai-tells.py --stdin --channel article | python3 -c "import sys,json; sys.exit(0 if not json.load(sys.stdin)[\"hard_fails\"] else 1)"'
t  "reviewed output wording passes"          'echo "Outputs include 80+ body measurements and calculated metrics such as BMI." | python3 brand-assets/style-guides/scripts/detect-ai-tells.py --stdin --channel article | python3 -c "import sys,json; sys.exit(0 if not json.load(sys.stdin)[\"hard_fails\"] else 1)"'
tn "80+ body metrics fails"                  'echo "FitXpress returns 80+ body metrics from two photos." | python3 brand-assets/style-guides/scripts/detect-ai-tells.py --stdin --channel article | python3 -c "import sys,json; sys.exit(0 if not json.load(sys.stdin)[\"hard_fails\"] else 1)"'
tn "BMI as a body measurement fails"         'echo "The scan returns body measurements such as BMI and waist circumference." | python3 brand-assets/style-guides/scripts/detect-ai-tells.py --stdin --channel article | python3 -c "import sys,json; sys.exit(0 if not json.load(sys.stdin)[\"hard_fails\"] else 1)"'
# Trust FAQ sync 2026-09-18: compliance.md was rebuilt from the live FAQ. Its outbound and social lines
# must stay clean in the channels that use them, and the retired statuses must fail.
t  "FAQ HIPAA sentence passes"               'echo "FitXpress can support HIPAA-governed deployments where 3DLOOK acts as a business associate under an executed BAA." | python3 brand-assets/style-guides/scripts/detect-ai-tells.py --stdin --channel article | python3 -c "import sys,json; sys.exit(0 if not json.load(sys.stdin)[\"hard_fails\"] else 1)"'
t  "FAQ SOC 2 sentence passes"               'echo "3DLOOK is working toward obtaining a SOC 2 Attestation Report and has completed an initial readiness assessment aligned with SOC 2 Trust Services Criteria." | python3 brand-assets/style-guides/scripts/detect-ai-tells.py --stdin --channel article | python3 -c "import sys,json; sys.exit(0 if not json.load(sys.stdin)[\"hard_fails\"] else 1)"'
t  "outbound US compliance line passes"      'echo "We support HIPAA-governed deployments under a BAA, encrypt data in transit and at rest, and delete photos after processing or within 30 days." | python3 brand-assets/style-guides/scripts/detect-ai-tells.py --stdin --channel dm | python3 -c "import sys,json; sys.exit(0 if not json.load(sys.stdin)[\"hard_fails\"] else 1)"'
t  "outbound EU compliance line passes"      'echo "In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs." | python3 brand-assets/style-guides/scripts/detect-ai-tells.py --stdin --channel dm | python3 -c "import sys,json; sys.exit(0 if not json.load(sys.stdin)[\"hard_fails\"] else 1)"'
tn "HIPAA compliant fails"                   'echo "FitXpress is HIPAA compliant." | python3 brand-assets/style-guides/scripts/detect-ai-tells.py --stdin --channel article | python3 -c "import sys,json; sys.exit(0 if not json.load(sys.stdin)[\"hard_fails\"] else 1)"'
tn "retired outbound line fails"             'echo "We are HIPAA compliant, encrypt at rest with SSE-S3, and process zero personal identifiers." | python3 brand-assets/style-guides/scripts/detect-ai-tells.py --stdin --channel dm | python3 -c "import sys,json; sys.exit(0 if not json.load(sys.stdin)[\"hard_fails\"] else 1)"'
tn "SOC 2 certified fails"                   'echo "3DLOOK is SOC 2 certified." | python3 brand-assets/style-guides/scripts/detect-ai-tells.py --stdin --channel article | python3 -c "import sys,json; sys.exit(0 if not json.load(sys.stdin)[\"hard_fails\"] else 1)"'
t  "context pack is valid yaml"              "python3 -c \"import yaml; yaml.safe_load(open('$P'))\""
t  "every new script parses without warning" 'for f in scripts/article_lint.py scripts/bans-card.py scripts/sync-agent-copies.py; do python3 -W error::SyntaxWarning -c "import ast; ast.parse(open(\"$f\").read())" || exit 1; done'

echo
echo "######## $pass passed, $fail failed ########"
[ "$fail" = 0 ]
