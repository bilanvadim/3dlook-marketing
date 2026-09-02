#!/usr/bin/env python3
"""
detect-ai-tells.py — quantitative AI-tell detector for 3DLOOK content.

Adapted from Victor Shulga's `anticopywriting-ai` skill (github.com/victor-shulga/gtm-skills),
which in turn adapts Wikipedia:Signs_of_AI_writing (WikiProject AI Cleanup).

What is different from upstream:
  * 3DLOOK's own bans are wired in as HARD categories: CLAUDE.md section 6 banned words and
    phrasings, `terminology-guardrails.md` (Asselya's word-level rules), and the editorial
    guardrails that matter mechanically (#3 reserved words, #4 bare headline percentages).
  * em dash is a HARD fail on any occurrence, not "overuse" — 3DLOOK bans it outright in all
    contexts (terminology-guardrails.md).
  * `--channel` presets, because the same marker has different weight in a 1,600-word article
    and in a 600-character LinkedIn DM. A DM has no headings to Title Case and no room for a
    participial tail; an article has both.
  * LinkedIn house rules (0 hashtags, max 2 emoji) are checked for `post` and `dm`.
  * Upstream markers that misfire on this corpus are scoped instead of dropped: `navigate`
    only figuratively, `represents` only where a plain verb would do, `objective` only about
    our own output.
  * Synced with the terminology guardrails Doc of 2026-08-13 (2026-08-25): `positioned_as`,
    `presumed_reaction` and `anthropomorphism` are new HARD categories; `plus` as a capability
    connector and `so` introducing a benefit joined `terminology_guardrails`; corrective
    negation and corrective "rather than" are SOFT (`corrective_contrast`) because both are
    licensed when the contrast states a real product, clinical, legal or regulatory boundary
    and no regex can tell a boundary from a slight.
  * `positioned_as` is a REVERSAL, not a new ban: "not positioned as a medical device" was the
    prescribed compliant form until 2026-08-13, so it is still in published articles and in any
    agent prompt that has not been re-synced. Expect hits on the old corpus.

Usage:
    python3 detect-ai-tells.py path/to/draft.md --channel article --pretty
    python3 detect-ai-tells.py path/to/post.md --channel post --profile linkedin-vadim
    cat msg.txt | python3 detect-ai-tells.py --stdin --channel dm

Channels: article (SEO/blog) | post (social) | dm (outbound LinkedIn) | page (landing) | any

Exit code is always 0 — this is a diagnostic, not a gate. The agent reads the JSON and decides.
The `verdict` field says what the numbers mean; `hard_fails` is what must be fixed regardless
of density.

Output JSON:
    language, channel, total_words, total_markers, ai_density_per_1000_words,
    severity, verdict, hard_fails, markers_by_category, style_metrics, top_offenders
"""

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# HARD categories — 3DLOOK-specific bans. Any hit is a fix, at any density.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# CARD — one human-readable line per HARD category, plus the fix.
#
# This exists so `scripts/bans-card.py` can generate the compact rule card that agents read
# instead of reading `ai-tells-sweep.md` (18 KB) and `terminology-guardrails.md` (16 KB) in
# full. The 2026-09-02 pipeline audit found these rules encoded in four places and enforced
# in one: this file. Keeping the human label next to the pattern is what makes the card
# impossible to drift from the enforcement.
#
# Rule for editing: change a pattern, change its CARD row in the same commit. `bans-card.py
# --check` exits 1 when a HARD category has no CARD row, so a new category cannot ship
# unlabelled.
CARD = {
    "banned_words": (
        "Banned vocabulary. Any inflection counts.",
        "Say the specific thing instead. There is no approved synonym, cut the sentence and rewrite it.",
    ),
    "banned_phrasings": (
        "Banned sentence shapes: \"it's not just X, it's Y\", \"in today's fast-paced world\", and friends.",
        "State the claim once, plainly.",
    ),
    "negative_parallelism": (
        "\"Not only ... but also\" and its variants, used for rhythm rather than meaning.",
        "Two sentences, or one that carries the point without the scaffold.",
    ),
    "em_dash": (
        "Em dash and en dash. Banned outright in every channel, not just in rhetorical constructions.",
        "Comma, full stop, or brackets. A hyphen in a numeric range (96-97%) is fine.",
    ),
    "terminology_guardrails": (
        "Words the terminology Doc retires: `objective` about our own output, `the reader`, "
        "`the following sections`, `see below`, `this article`, `by hand`, `let`, `plus` as a "
        "capability connector, `so` introducing a benefit.",
        "standardized / timestamped / structured / repeatable; describe the business reality; "
        "manually; allow; including / such as / along with; reducing... / which can reduce...",
    ),
    "positioned_as": (
        "`positioned as` for product, intended use, scope, replacement or regulatory status. "
        "ONE licensed exception since 2026-09-02: the medical-device sentence.",
        "State the boundary directly. For medical device write exactly: "
        "\"It is not positioned as a medical device.\"",
    ),
    "presumed_reaction": (
        "Telling the audience what it thinks or gets wrong: \"what trips people up\", "
        "\"the mistake buyers make\".",
        "Name the components of the problem directly.",
    ),
    "anthropomorphism": (
        "Behaviour or feeling attributed to a concept: \"two properties do the heavy lifting\".",
        "\"two properties matter\". Plain verbs.",
    ),
    "reserved_words": (
        "`independent`, `third-party`, `validated`, `clinically validated`, `peer-reviewed` "
        "applied to our own evidence. We have none of these.",
        "\"internal validation\", and say what it was measured against.",
    ),
    "bare_percentage": (
        "A bare \">X%\" with no methodology behind it (editorial guardrail #4).",
        "Give the reference method and the conditions, or write \"available under a "
        "non-disclosure agreement\".",
    ),
    "claims_discipline": (
        "Claims about-me.md forbids outright: diagnosis, decisioning, replacing a clinician or "
        "a reference method, guaranteed compliance, automatic fraud detection.",
        "supports / helps standardize / provides structured records / can support review, "
        "where the workflow or protocol allows.",
    ),
}


HARD_EN = {
    # CLAUDE.md section 6 — banned words
    "banned_words": [
        r"\bleverag(e|es|ed|ing)\b",
        r"\butili[sz](e|es|ed|ing|ation)\b",
        r"\bharness(es|ed|ing)?\b",
        r"\brobust(ness)?\b",
        r"\bseamless(ly)?\b",
        r"\bcomprehensive(ly)?\b",
        r"\brevolutioni[sz](e|es|ed|ing)\b",
        r"\brevolutionary\b",
        r"\bcutting[- ]edge\b",
        r"\bstate[- ]of[- ]the[- ]art\b",
        r"\bgame[- ]changer\b",
        r"\bgame[- ]changing\b",
        r"\bdisrupt(s|ed|ing|ive|ion)?\b",
        r"\bdelv(e|es|ed|ing)\b",
        r"\btapestry\b",
        r"\brealm\b",
        r"\bgroundbreaking\b",
        r"\bbest[- ]in[- ]class\b",
        r"\bindustry[- ]leading\b",
        r"\bworld[- ]class\b",
        r"\bunparalleled\b",
        # figurative only — "navigate the regulatory landscape", not "navigate to the settings"
        r"\bnavigat(e|es|ed|ing)\s+(the\s+)?(complex|complexit|challeng|landscape|regulat|uncertain|nuance|shift|evolv|tricky|maze)",
    ],
    # CLAUDE.md section 6 — banned openers / phrasings
    "banned_phrasings": [
        r"\bin today'?s\s+(fast[- ]paced|rapidly[- ]evolving|ever[- ]changing|digital|competitive)\b",
        r"\bunlock(ing)?\s+the\s+(power|potential|value)\b",
        r"\bare\s+you\s+struggling\s+with\b",
        r"\bit'?s\s+no\s+secret\s+that\b",
        r"\bhave\s+you\s+ever\s+wondered\b",
        r"\bin\s+this\s+(article|guide|post),?\s+we(\s+will|'ll)?\b",
        r"\blet'?s\s+div(e|ing)\s+in\b",
        r"\bhere'?s\s+everything\s+you\s+need\s+to\s+know\b",
        # "AI-powered" as a standalone value claim: followed by punctuation or a bare noun stop
        r"\bAI[- ]powered\s*[.,;:!?)]",
    ],
    # CLAUDE.md section 6 — negative parallelism, the single most reliable AI signature
    "negative_parallelism": [
        r"\bit'?s\s+not\s+just\s+.{1,50}?,\s*it'?s\b",
        r"\bnot\s+just\s+.{1,50}?\s*[—–-]\s*it'?s\b",
        r"\bthis\s+isn'?t\s+(just|only)\s+.{1,50}?,\s*(but|it)\b",
        r"\bit'?s\s+not\s+about\s+.{1,50}?,\s*it'?s\s+about\b",
        r"\bnot\s+only\s+.{1,50}?\s+but\s+also\b",
    ],
    # terminology-guardrails.md — em dash banned in ALL contexts, no exceptions
    "em_dash": [
        r"[—–]",
    ],
    # terminology-guardrails.md — Asselya's word-level rules (Part 2)
    "terminology_guardrails": [
        # "objective" about our own output
        r"\bobjective\s+(measurement|data|record|assessment|metric|number|result|output|scan)",
        r"\b(measurement|data|record|assessment|metric|scan)s?\s+(is|are)\s+objective\b",
        r"\bthe\s+(reader|readers|audience)\b",
        r"\bthe\s+following\s+sections?\b",
        r"\b(see|as\s+(shown|described|outlined))\s+below\b",
        r"\bthis\s+(article|guide|paper|piece)\b",
        r"\bour\s+(content|article|guide)\b",
        r"\bby\s+hand\b",
        r"\blets?\s+(you|them|teams?|clinicians?|operators?|users?)\b",
        # "plus" as a capability connector (2.7). Sentence-initial and mid-list forms only:
        # "A plus B" as arithmetic or "a plus for the clinic" are different words.
        r"(?:(?m:^)|[.!?]\s+)\s*Plus\b",
        r",\s+plus\s+\w",
        # "so" introducing a result or business benefit (2.9). Scoped to the benefit shape —
        # "so that" and "so far" are not the banned use, and neither is "so" as an intensifier.
        r",\s+so\s+(?:you|they|it|teams?|clinics?|clinicians?|providers?|patients?|payers?|"
        r"underwriters?|operators?|members?|the\s+\w+)\s+(?:can|could|get|gets|save|saves|"
        r"avoid|avoids|reduce|reduces|see|sees|know|knows|do|does|don'?t|never|no\s+longer)\b",
    ],
    # terminology-guardrails.md 2.10 — "positioned as" for product / intended-use / regulatory
    # statements. REVERSAL: this phrasing was the prescribed compliant form until 2026-08-13,
    # so it is still in older articles and in prompts that have not been re-synced.
    # "positioned as a market leader" (genuine market positioning) is the licensed exception and
    # is deliberately not matched.
    # PARTIAL RE-REVERSAL (2026-09-02, Review 1 on the Wellness hub, Vadim's call): the
    # medical-device boundary sentence "not positioned as a medical device" is the approved
    # wording again and is licensed by the lookahead below. Every other product, intended-use
    # and regulatory use of "positioned as" stays a hard fail.
    "positioned_as": [
        r"\bnot\s+positioned\s+as\s+(?!a\s+medical\s+device\b)",
        r"\b(?:is|are|was|were|be|being|been)\s+positioned\s+as\s+(?:a|an|the)?\s*"
        r"(?:supporting|support|medical|diagnostic|clinical|screening|verification|measurement|"
        r"replacement|alternative|equivalent|substitute|tool|device|solution|platform|layer|"
        r"service|api|sdk)\b",
        r"\bpositioned\s+as\s+equivalent\b",
    ],
    # terminology-guardrails.md 1.5 — no presumed audience reaction
    "presumed_reaction": [
        r"\bwhat\s+trips\s+(?:up\s+)?(?:people|teams|buyers|most|readers|clinics)",
        r"\btrips?\s+up\s+(?:most|many|some)?\s*\w+\s+(?:reviews?|teams?|buyers?|programs?)",
        r"\bthe\s+(?:common|biggest|classic|usual)\s+mistake\b",
        r"\bthe\s+mistake\s+(?:buyers|teams|clinics|most|many|people)\b",
        r"\bwhat\s+most\s+(?:teams|buyers|people|clinics|programs)\s+"
        r"(?:misunderstand|get\s+wrong|miss|overlook|assume)\b",
        r"\bwhere\s+(?:teams|buyers|people|most)\s+(?:get\s+it\s+wrong|go\s+wrong|slip\s+up)\b",
        r"\bmost\s+(?:teams|buyers|people|clinics)\s+(?:assume|think|believe)\b",
        r"\byou\s+might\s+(?:be\s+)?(?:think|thinking|wondering|surprised)\b",
    ],
    # terminology-guardrails.md 1.6 — behaviour attributed to concepts (too casual for the
    # healthcare-enterprise register). Narrow on purpose: only the idioms that actually recur.
    "anthropomorphism": [
        r"\bheavy\s+lifting\b",
        r"\bdoes?\s+the\s+work\s+for\b",
        r"\b(?:data|model|models|algorithm|algorithms|system|systems|platform|feature|features|"
        r"scan|scans|metric|metrics|number|numbers)\s+"
        r"(?:wants?|knows?|thinks?|believes?|understands?|cares?|decides?|feels?|struggles?)\b",
        r"\b(?:workflow|process|pipeline)s?\s+(?:fights?|resists?|wants?)\b",
    ],
    # editorial-guardrails.md #3 — reserved words need a named external party
    "reserved_words": [
        r"\bindependent(ly)?\s+(validat|verif|test|assess|audit)",
        r"\bthird[- ]party\s+(validat|verif|test|assess|audit)",
        r"\bclinically\s+(validated|certified|proven)\b",
        r"\bpeer[- ]reviewed\b",
    ],
    # editorial-guardrails.md #4 — bare headline percentage with no methodology
    "bare_percentage": [
        r"[>≥<≤]\s*\d{1,3}(\.\d+)?\s*%",
        r"\bup\s+to\s+\d{1,3}(\.\d+)?\s*%",
    ],
    # claims discipline — CLAUDE.md section 12 / positioning bans
    "claims_discipline": [
        r"\bdiagnos(e|es|ed|ing|is|tic)\b",
        r"\breplaces?\s+(a\s+)?(clinician|doctor|physician|DXA|DEXA|reference)",
        r"\bguarantees?\s+compliance\b",
        r"\bdetects?\s+fraud\b",
        r"\bmakes?\s+(the\s+)?decisions?\b",
        r"\bmost\s+accurate\b",
        r"\bjust\s+an\s+API\b",
    ],
}

# ---------------------------------------------------------------------------
# SOFT categories — generic AI tells. Judgment, weighted by density.
# ---------------------------------------------------------------------------

SOFT_EN = {
    "inflated_significance": [
        r"\bstands as a testament\b",
        r"\b(marks|marking)\s+a\s+(pivotal|key|defining)\s+(moment|milestone)\b",
        r"\ba\s+(key|crucial|pivotal|major)\s+milestone\b",
        r"\bwatershed\b",
        r"\bparadigm[- ]shift(ing)?\b",
        r"\btransformational\b",
        r"\bindispensable\b",
        r"\bcornerstone\s+of\b",
        r"\bhallmark\s+of\b",
        r"\bushers?\s+in\s+a\s+new\s+era\b",
        r"\ba\s+new\s+era\s+(of|in|for)\b",
        r"\breshap(e|es|ing)\s+the\s+(landscape|industry|future)\b",
        r"\bredefin(e|es|ing)\s+the\s+(boundaries|standard)\b",
        r"\bplays?\s+a\s+(crucial|pivotal|essential|key|vital)\s+role\b",
        r"\bin\s+the\s+broader\s+context\s+of\b",
    ],
    "authority_signaling": [
        r"\bwidely\s+regarded\b",
        r"\bleading\s+experts?\s+agree\b",
        r"\bexperts?\s+(agree|believe|note|say)\b",
        r"\bprominent\s+figures\b",
        r"\bgarnered\s+widespread\b",
        r"\brecognized\s+authority\b",
        r"\bextensively\s+covered\b",
    ],
    "vague_references": [
        r"\baccording\s+to\s+industry\s+reports?\b",
        r"\bobservers?\s+note\b",
        r"\bsome\s+critics?\s+argue\b",
        r"\bvarious\s+sources\s+suggest\b",
        r"\bavailable\s+data\s+indicates?\b",
        r"\bstudies\s+(have\s+)?(show|shown|suggest)\b",
        r"\bresearch\s+suggests?\b",
        r"\bit\s+is\s+widely\s+(known|believed|accepted)\b",
    ],
    "shallow_participles": [
        r",\s*underscoring\b",
        r",\s*highlighting\b",
        r",\s*showcasing\b",
        r",\s*demonstrating\b",
        r",\s*reflecting\b",
        r",\s*embodying\b",
        r",\s*symbolizing\b",
        r",\s*shaping\b",
        r",\s*serving\s+as\s+a\s+reminder\b",
        r",\s*ultimately\s+(driving|enabling|delivering)\b",
    ],
    "promo_language": [
        r"\bboasts?\b",
        r"\bvibrant\b",
        r"\bbustling\b",
        r"\bpicturesque\b",
        r"\bbreathtaking\b",
        r"\bstunning\b",
        r"\brich\s+heritage\b",
        r"\bone[- ]of[- ]a[- ]kind\b",
        r"\bin\s+the\s+heart\s+of\b",
        r"\bleaves?\s+a\s+lasting\s+impression\b",
        r"\bbespoke\b",
        r"\btruly\s+(unique|transformative|remarkable)\b",
    ],
    "challenges_template": [
        r"\bdespite\s+(facing\s+)?(numerous|the\s+typical|these)\s+(challenges|obstacles)\b",
        r"\bcontinues?\s+to\s+thrive\b",
        r"\bchallenges\s+and\s+opportunities\b",
        r"\bin\s+the\s+face\s+of\s+adversity\b",
        r"\bwhile\s+challenges\s+remain\b",
        r"\bthe\s+(future|outlook)\s+(is|looks)\s+(bright|promising)\b",
    ],
    "ai_vocabulary": [
        r"\bdiv(e|es|ing)\s+deep(er)?\b",
        r"\bintricate\b",
        r"\bmultifaceted\b",
        r"\bfoster(s|ed|ing)?\b",
        r"\bunderscor(e|es|ed|ing)\b",
        r"\belucidat(e|es|ed|ing)\b",
        r"\bencompass(es|ed|ing)?\b",
        r"\bthe\s+intersection\s+of\b",
        r"\bpivotal\b",
        r"\bparamount\b",
        r"\bprofound(ly)?\b",
        r"\bholistic(ally)?\b",
        r"\bnuanced\b",
        r"\bresonat(e|es|ed|ing)\b",
        r"\bin\s+line\s+with\b",
        r"\bthe\s+(regulatory|competitive|technology|digital)\s+landscape\b",
    ],
    "connectives": [
        # One pattern, not two: an overlapping "^Moreover" + ". Moreover" pair double-counts
        # the same word and silently inflates density.
        r"(?:(?m:^)|[.!?]\s+)\s*(?:Furthermore|Moreover|Additionally|In\s+addition)\b",
    ],
    "avoiding_is": [
        r"\bserves?\s+as\b",
        r"\bstands?\s+as\b",
        r"\bembodies\b",
        r"\bexemplifies\b",
        r"\bconstitutes\b",
        # "represents" only where a plain "is" would do
        r"\brepresents\s+a(n)?\s+(opportunity|shift|step|milestone|challenge|solution|approach)\b",
    ],
    "false_ranges": [
        r"\bfrom\s+(strategy|startups?|concept|research|design)\s+to\s+(execution|enterprises?|delivery|practice|production)\b",
        r"\beverything\s+from\s+.{1,40}\s+to\s+.{1,40}\b",
    ],
    "filler_phrases": [
        r"\bin\s+order\s+to\b",
        r"\bdue\s+to\s+the\s+fact\s+that\b",
        r"\bat\s+(the\s+)?(present|this)\s+(moment|time)\b",
        r"\bin\s+the\s+event\s+that\b",
        r"\bhas\s+the\s+ability\s+to\b",
        r"\bprior\s+to\b",
        r"\bin\s+terms\s+of\b",
        r"\bwhen\s+it\s+comes\s+to\b",
    ],
    "excessive_hedging": [
        r"\bcould\s+potentially\b",
        r"\bmight\s+possibly\b",
        r"\bit\s+could\s+be\s+(argued|suggested)\b",
        r"\bsome\s+degree\s+of\b",
        r"\bin\s+some\s+cases,?\s+it\s+(may|might|could)\b",
    ],
    "bureaucratese": [
        r"\boperationali[sz](e|es|ed|ing)\b",
        r"\bsynergi[sz](e|es|ed|ing|y)\b",
        r"\bfacilitat(e|es|ed|ing|ion)\b",
        r"\bwith\s+respect\s+to\b",
        r"\bin\s+regard(s)?\s+to\b",
        r"\bpursuant\s+to\b",
        r"\baforementioned\b",
        r"\bgoing\s+forward\b",
    ],
    "prefatory_excess": [
        r"\bit'?s\s+worth\s+noting\b",
        r"\bit\s+is\s+important\s+to\s+(note|emphasi[sz]e|understand|remember)\b",
        r"\bone\s+cannot\s+overlook\b",
        r"\bit\s+should\s+be\s+(noted|mentioned)\b",
        r"\bequally\s+important\s+is\b",
        r"\bit\s+bears\s+(repeating|mentioning)\b",
    ],
    "abstract_world": [
        r"\bin\s+the\s+world\s+of\b",
        r"\bin\s+the\s+realm\s+of\b",
        r"\bin\s+the\s+landscape\s+of\b",
        r"\bin\s+the\s+space\s+of\b",
        r"\bin\s+the\s+arena\s+of\b",
    ],
    "chatbot_artifacts": [
        r"\bI\s+hope\s+this\s+helps\b",
        r"\bI'?d\s+be\s+happy\s+to\b",
        r"\bfeel\s+free\s+to\s+(ask|reach)\b",
        r"\blet\s+me\s+know\s+if\s+you'?d\s+like\b",
        r"\bhere'?s\s+an?\s+overview\b",
        r"(?m)^(Certainly|Absolutely|Of\s+course|Great\s+question)[!,]",
        r"\byou'?re\s+absolutely\s+right\b",
    ],
    "outbound_cliches": [
        r"\bI\s+help\s+companies\s+like\s+yours\b",
        r"\bI\s+(admire|love)\s+your\s+mission\b",
        r"\bexcited\s+about\s+your\s+journey\b",
        r"\bhope\s+this\s+(email|message)\s+finds\s+you\s+well\b",
        r"\bI\s+came\s+across\s+your\s+profile\b",
        r"\bquick\s+question\s+for\s+you\b",
        r"\bcircling\s+back\b",
        r"\bjust\s+following\s+up\b",
        r"\bwanted\s+to\s+(reach\s+out|pick\s+your\s+brain)\b",
    ],
    # terminology-guardrails.md 1.8 / 1.9 — corrective negation and corrective "rather than".
    # SOFT on purpose: both are licensed when the contrast states a real product, clinical, legal
    # or regulatory boundary, and no regex can tell a boundary from a slight. Reported for the
    # editor to judge, one hit at a time.
    "corrective_contrast": [
        r"\brather\s+than\b",
        r"\b(?:is|are|was|were|means|becomes|comes)\s+(?:a|an|the)?\s*[\w-]+(?:\s+[\w-]+){0,3},\s+not\s+(?:a|an|the)?\s*[\w-]+",
        r"\bit'?s\s+(?:about|a)\s+[\w-]+(?:\s+[\w-]+){0,3},\s+not\b",
    ],
    "slogan_ending": [
        r"(?m)^.{0,80}(the\s+future\s+is\s+here|that'?s\s+the\s+real\s+(win|shift)|and\s+that\s+changes\s+everything)\.?\s*$",
        r"\bexciting\s+times\s+(lie\s+)?ahead\b",
        r"\ba\s+step\s+in\s+the\s+right\s+direction\b",
    ],
}

# Ukrainian soft set — used for the rare UK-language artefact (Hermes digests, internal notes).
# 3DLOOK's outward-facing content is English; this is deliberately smaller than the EN set.
SOFT_UK = {
    "inflated_significance": [
        r"\bключов(ий|им|ого|а|ою)\s+етап",
        r"\bзнамену(є|ють)\s+нову\s+еру\b",
        r"\bвідкрива(є|ють)\s+нову\s+сторінку\b",
        r"\bнаріжн(ий|им)\s+камен",
        r"\bграє\s+(ключову|важливу|вирішальну)\s+роль\b",
        r"\bневід'?ємн(ою|ий|а)\s+частин",
    ],
    "ai_vocabulary": [
        r"\bкрім\s+того\b",
        r"\bу\s+контексті\b",
        r"\bнепереборн",
        r"\bбагатогранн",
        r"\bкомплексн(ий|е|а)\s+підхід",
        r"\bсинергі",
    ],
    "avoiding_is": [
        r"\bявля(є|ють)\s+собою\b",
        r"\bвиступа(є|ють)\s+в\s+якості\b",
    ],
    "negative_parallelism": [
        r"\bце\s+не\s+просто\s+.{1,50}?,\s*це\b",
        r"\bне\s+лише\s+.{1,50}?,\s*а\s+й\b",
    ],
    "bureaucratese": [
        r"\bу\s+рамках\b",
        r"\bздійсню(є|ють|вати)\b",
        r"\bз\s+метою\b",
        r"\bдля\s+того\s+щоб\b",
        r"\bналежним\s+чином\b",
    ],
    "prefatory_excess": [
        r"\bварто\s+зазначити,?\s+що\b",
        r"\bслід\s+підкреслити\b",
        r"\bнеобхідно\s+відзначити\b",
    ],
    "vague_references": [
        r"\bексперти\s+(вважають|зазначають)\b",
        r"\bдослідження\s+показують\b",
        r"\bзагальновідомо,?\s+що\b",
    ],
    "abstract_world": [
        r"\bу\s+світі\s+(бізнесу|технологій|маркетингу)\b",
        r"\bу\s+сфері\b",
    ],
}

HARD_UK = {
    "em_dash": [r"[—–]"],
    "negative_parallelism": SOFT_UK["negative_parallelism"],
}

# ---------------------------------------------------------------------------
# CHANNEL PRESETS
# ---------------------------------------------------------------------------
# `mute` = categories that do not apply to this channel's form (a DM has no headings).
# `density_budget` = markers per 1000 words above which the draft needs a real rewrite,
#   not spot fixes. Short forms get a tighter budget: in 60 words there is no room to hide.
# `structure_checks` = which style metrics are meaningful here.

CHANNELS = {
    "article": {
        "label": "SEO / blog article",
        "mute": ["outbound_cliches"],
        "density_budget": 6.0,
        "structure_checks": ["em_dash", "bold", "title_case", "emoji", "uniform_rhythm", "list_ratio"],
        "hashtag_limit": None,
        "emoji_limit": 0,
    },
    "post": {
        "label": "social post",
        "mute": ["outbound_cliches", "filler_phrases"],
        "density_budget": 10.0,
        "structure_checks": ["em_dash", "emoji", "hashtags", "uniform_rhythm"],
        "hashtag_limit": 0,   # LinkedIn house rule: 0 hashtags
        "emoji_limit": 2,     # LinkedIn house rule: max 2 emoji
    },
    "dm": {
        "label": "outbound LinkedIn message",
        "mute": ["title_case", "bold_overuse", "shallow_participles", "challenges_template",
                 "slogan_ending", "bare_percentage"],
        "density_budget": 12.0,
        "structure_checks": ["em_dash", "emoji", "wall_of_text"],
        "hashtag_limit": 0,
        "emoji_limit": 0,
    },
    "page": {
        "label": "landing / vertical page",
        "mute": ["outbound_cliches"],
        "density_budget": 6.0,
        "structure_checks": ["em_dash", "bold", "title_case", "emoji", "uniform_rhythm", "list_ratio"],
        "hashtag_limit": None,
        "emoji_limit": 0,
    },
    "any": {
        "label": "unspecified",
        "mute": [],
        "density_budget": 8.0,
        "structure_checks": ["em_dash", "bold", "title_case", "emoji", "uniform_rhythm"],
        "hashtag_limit": None,
        "emoji_limit": None,
    },
}

EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF⬀-⯿️]"
)


# ---------------------------------------------------------------------------
# DETECTION
# ---------------------------------------------------------------------------

def detect_language(text: str) -> str:
    cyr = len(re.findall(r"[Ѐ-ӿ]", text))
    lat = len(re.findall(r"[A-Za-z]", text))
    return "uk" if cyr > lat else "en"


# A ban is not a ban when the sentence is disclaiming it. "FitXpress is not a diagnostic tool"
# is the REQUIRED framing (guardrail #6), not a claims-discipline failure. Same for "not
# independently validated" and "does not replace a clinician" — those are the compliant forms.
NEGATION_CUES = re.compile(
    r"\b(?:not|never|no|nor|without|neither|cannot|can'?t|isn'?t|aren'?t|don'?t|doesn'?t|"
    r"didn'?t|won'?t|avoid|avoids|refrain\s+from|rather\s+than|instead\s+of|"
    r"as\s+opposed\s+to|no\s+longer)\b",
    re.IGNORECASE,
)


def is_negated(text: str, start: int) -> bool:
    """
    True if a negation cue governs this match. The window spans the whole preceding sentence,
    not a fixed few words, because these disclaimers chain across commas:
    "They do not replace reference methods (...), independently validate endpoints, determine
    eligibility" — one "not" governing three verbs 200 characters apart.
    """
    left = text[max(0, start - 400):start]
    for sep in (". ", ".\n", "! ", "? ", "\n\n"):
        idx = left.rfind(sep)
        if idx != -1:
            left = left[idx + len(sep):]
    return bool(NEGATION_CUES.search(left))


def in_question(text: str, start: int) -> bool:
    """
    True if the match sits on a line that is a question. FAQ headings quote the objection
    verbatim ("Does FitXpress replace DXA?") — asking is not claiming.
    """
    line_start = text.rfind("\n", 0, start) + 1
    line_end = text.find("\n", start)
    line = text[line_start: line_end if line_end != -1 else len(text)]
    return line.rstrip().rstrip("*_ ").endswith("?")


# Categories where a negated hit is the compliant phrasing, so it must not be reported.
NEGATION_AWARE = {"claims_discipline", "reserved_words"}


def find_matches(text: str, patterns: dict, line_offset: int = 0) -> dict:
    """
    Per-category list of (matched_string, line_number, line_excerpt).
    `line_offset` maps line numbers back onto the ORIGINAL file after frontmatter is stripped —
    without it every reported line is short by the frontmatter's height and the agent edits
    the wrong line.
    """
    results = defaultdict(list)
    lines = text.splitlines()
    for category, pattern_list in patterns.items():
        negation_aware = category in NEGATION_AWARE
        for pat in pattern_list:
            for m in re.finditer(pat, text, re.IGNORECASE | re.MULTILINE):
                if negation_aware and (is_negated(text, m.start()) or in_question(text, m.start())):
                    continue
                local_line = text[: m.start()].count("\n") + 1
                excerpt = lines[local_line - 1].strip() if 0 < local_line <= len(lines) else ""
                if len(excerpt) > 140:
                    excerpt = excerpt[:137] + "..."
                results[category].append((m.group(0), local_line + line_offset, excerpt))
    return results


def strip_frontmatter(text: str) -> tuple:
    """
    Frontmatter is metadata, not prose. Counting it skews density and flags our own field names.
    Returns (body, line_offset) so reported line numbers still point at the original file.
    """
    m = re.match(r"\A---\s*\n.*?\n---\s*\n", text, re.DOTALL)
    if not m:
        return text, 0
    return text[m.end():], text[: m.end()].count("\n")


# The banned pattern is the rhetorical ADJECTIVE triad ("fast, reliable, scalable"), not any
# three-item list. "positioning, posture, and equipment" is a real enumeration and rewriting it
# damages good copy — so a triad only counts when the items look like adjectives.
ADJ_SUFFIX = re.compile(
    r"(?:able|ible|ive|ent|ant|ous|ful|less|ic|ical|al|ar|ary|ory|ile|ing|ed|est|y)$"
)
PUNCH_ADJ = {
    "fast", "quick", "cheap", "easy", "simple", "clear", "clean", "safe", "smart", "lean",
    "slow", "hard", "rich", "deep", "broad", "light", "solid", "sharp", "strong", "small",
    "large", "big", "new", "real", "true", "free", "open", "close", "high", "low", "mobile",
    "instant", "modern", "global", "local", "digital", "manual", "precise", "exact",
}
# Words whose -ing/-ed/-al/-y form is almost always a noun in this corpus; without this the
# suffix test alone flags "tracking, wellness, fitness" and "apparel, uniforms, wellness".
NOUN_DESPITE_SUFFIX = re.compile(
    r"(?:ness|ment|tion|sion|ity|ancy|ency|ology|ography|ics|ing)$"
)


def _looks_adjectival(word: str) -> bool:
    w = word.lower()
    # For a hyphenated compound the head is the last element: "data-backed" -> "backed".
    head = w.rsplit("-", 1)[-1]
    if w in PUNCH_ADJ or head in PUNCH_ADJ:
        return True
    if NOUN_DESPITE_SUFFIX.search(head):
        return False
    return bool(ADJ_SUFFIX.search(head))


def count_triads(text: str) -> list:
    """
    Rule-of-three punch triads: three single-word adjectives in series, landing at a clause end.
    Requires (a) all three items adjectival, and (b) the triad to close a clause — that is what
    makes it a rhetorical punch rather than a list of things.
    """
    hits = []
    # Items may be hyphenated compounds — "quick, visual, and data-backed" is the same signature.
    item = r"[A-Za-z]{3,15}(?:-[A-Za-z]{2,15})?"
    pat = re.compile(
        rf"\b({item}),\s+({item}),\s+(?:and\s+|or\s+)?({item})\b"
        r"(?=\s*[.,;:!?)\n]|\s+(?:and|or)\b)"
    )
    for m in pat.finditer(text):
        items = [m.group(1), m.group(2), m.group(3)]
        if sum(_looks_adjectival(w) for w in items) < 3:
            continue
        line_no = text[: m.start()].count("\n") + 1
        hits.append((m.group(0), line_no))
    return hits


def rhythm_metrics(text: str) -> dict:
    """
    Uniform sentence and paragraph length is the clearest structural tell there is.
    Returns coefficient of variation for sentence length; low = monotone.
    """
    body = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    body = re.sub(r"^\s*[-*|#>].*$", "", body, flags=re.MULTILINE)  # drop lists/headings/tables
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", body) if len(s.strip()) > 1]
    lengths = [len(re.findall(r"\b\w+\b", s)) for s in sentences if len(re.findall(r"\b\w+\b", s)) > 2]
    if len(lengths) < 4:
        return {"sentences": len(lengths), "mean_words": 0, "variation": None, "monotone": False}
    mean = sum(lengths) / len(lengths)
    var = sum((x - mean) ** 2 for x in lengths) / len(lengths)
    cv = (var ** 0.5) / mean if mean else 0
    paras = [p for p in re.split(r"\n\s*\n", body) if len(re.findall(r"\b\w+\b", p)) > 15]
    p_lengths = [len(re.split(r"(?<=[.!?])\s+", p)) for p in paras]
    same_para = False
    if len(p_lengths) >= 4:
        same_para = len(set(p_lengths)) <= 2 and max(p_lengths) <= 4
    return {
        "sentences": len(lengths),
        "mean_words": round(mean, 1),
        "variation": round(cv, 2),
        "monotone": cv < 0.35,
        "uniform_paragraphs": same_para,
    }


def style_metrics(text: str, lang: str, channel: dict, line_offset: int = 0) -> dict:
    words = max(len(re.findall(r"\b\w+\b", text)), 1)
    em = len(re.findall(r"[—–]", text))
    bold = len(re.findall(r"\*\*[^*]+\*\*", text))
    # H2+ only: a blog H1 is the article title, and 3DLOOK titles it in Title Case by convention.
    headings = re.findall(r"^#{2,6}\s+(.+)$", text, re.MULTILINE)
    title_case = 0
    for h in headings:
        ws = [w for w in h.split() if len(w) > 3]
        if len(ws) >= 3 and all(w[0].isupper() for w in ws):
            title_case += 1
    emoji = len(EMOJI_RE.findall(text))
    hashtags = len(re.findall(r"(?<!\w)#[A-Za-z][\w-]{1,}", text))
    bullets = len(re.findall(r"^\s*[-*+]\s+", text, re.MULTILINE))
    bold_lead = len(re.findall(r"^\s*[-*+]\s+\*\*[^*]+\*\*\s*[:—-]", text, re.MULTILINE))
    prose_lines = len([l for l in text.splitlines() if len(l.strip()) > 40 and not l.strip().startswith(("-", "*", "#", "|", ">"))])
    paras = [p for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
    wall_of_text = len(paras) == 1 and words > 45

    rh = rhythm_metrics(text)
    triads = count_triads(text)

    return {
        "em_dashes": em,
        "bold_count": bold,
        "bold_per_1000_words": round(bold / words * 1000, 1),
        "title_case_headings": title_case,
        "emoji_count": emoji,
        "hashtag_count": hashtags,
        "bullet_lines": bullets,
        "bold_lead_in_bullets": bold_lead,
        "list_to_prose_ratio": round(bullets / max(prose_lines, 1), 2),
        "wall_of_text": wall_of_text,
        "rhythm": rh,
        "punch_triads": [{"text": t, "line": ln + line_offset} for t, ln in triads[:10]],
        "punch_triad_count": len(triads),
    }


def analyze(text: str, lang: str, channel_name: str, profile: str = None) -> dict:
    text, line_offset = strip_frontmatter(text)
    if lang == "auto":
        lang = detect_language(text)
    ch = CHANNELS.get(channel_name, CHANNELS["any"])

    hard_pats = HARD_UK if lang == "uk" else HARD_EN
    soft_pats = SOFT_UK if lang == "uk" else SOFT_EN

    muted = set(ch["mute"])
    hard_pats = {k: v for k, v in hard_pats.items() if k not in muted}
    soft_pats = {k: v for k, v in soft_pats.items() if k not in muted}

    total_words = len(re.findall(r"\b\w+\b", text))
    hard_hits = find_matches(text, hard_pats, line_offset)
    soft_hits = find_matches(text, soft_pats, line_offset)
    sm = style_metrics(text, lang, ch, line_offset)

    hard_fails = []
    for cat, hits in sorted(hard_hits.items(), key=lambda x: -len(x[1])):
        if not hits:
            continue
        uniq = []
        seen = set()
        for matched, line_no, excerpt in hits:
            key = matched.lower()
            if key in seen:
                continue
            seen.add(key)
            uniq.append({"marker": matched, "line": line_no, "example": excerpt})
        hard_fails.append({"category": cat, "count": len(hits), "hits": uniq[:8]})

    # Punch triads are a hard fail per CLAUDE.md section 6, detected structurally
    if sm["punch_triad_count"]:
        hard_fails.append({
            "category": "punch_triads",
            "count": sm["punch_triad_count"],
            "hits": [{"marker": t["text"], "line": t["line"], "example": ""} for t in sm["punch_triads"][:8]],
        })

    # House-rule violations
    house = []
    if ch["hashtag_limit"] is not None and sm["hashtag_count"] > ch["hashtag_limit"]:
        house.append(f"hashtags: {sm['hashtag_count']} (limit {ch['hashtag_limit']})")
    if ch["emoji_limit"] is not None and sm["emoji_count"] > ch["emoji_limit"]:
        house.append(f"emoji: {sm['emoji_count']} (limit {ch['emoji_limit']})")
    if "wall_of_text" in ch["structure_checks"] and sm["wall_of_text"]:
        house.append("single dense block: split into paragraphs of <=2 sentences")
    if "list_ratio" in ch["structure_checks"] and sm["list_to_prose_ratio"] > 1.0 and sm["bullet_lines"] > 8:
        house.append(f"list-heavy: {sm['bullet_lines']} bullet lines vs {int(sm['bullet_lines']/max(sm['list_to_prose_ratio'],0.01))} prose lines")
    if "bold" in ch["structure_checks"] and sm["bold_lead_in_bullets"] >= 3:
        house.append(f"bold-headed bullet list: {sm['bold_lead_in_bullets']} items")
    if "title_case" in ch["structure_checks"] and sm["title_case_headings"]:
        house.append(f"Title Case headings: {sm['title_case_headings']}")
    if "uniform_rhythm" in ch["structure_checks"] and sm["rhythm"].get("monotone"):
        house.append(f"monotone rhythm: sentence-length variation {sm['rhythm']['variation']} (want >0.35)")
    if "uniform_rhythm" in ch["structure_checks"] and sm["rhythm"].get("uniform_paragraphs"):
        house.append("uniform paragraph length: every block the same size")

    markers_by_category = {}
    for cat, hits in hard_hits.items():
        if hits:
            markers_by_category[cat] = len(hits)
    for cat, hits in soft_hits.items():
        if hits:
            markers_by_category[cat] = markers_by_category.get(cat, 0) + len(hits)
    if sm["punch_triad_count"]:
        markers_by_category["punch_triads"] = sm["punch_triad_count"]

    # em dash is excluded from the density score on purpose. It is a global find-and-replace,
    # not evidence that the prose was generated: 50 of them in one article would dominate the
    # number and hide everything the score is actually for. Reported separately, still a hard fail.
    em_dash_hits = markers_by_category.get("em_dash", 0)
    scored_markers = sum(v for k, v in markers_by_category.items() if k != "em_dash")
    total_markers = scored_markers + em_dash_hits
    density = (scored_markers / max(total_words, 1)) * 1000

    counter = Counter()
    examples = {}
    for cat, hits in list(hard_hits.items()) + list(soft_hits.items()):
        if cat == "em_dash":
            continue  # counted in style_metrics; 50 identical rows crowd out the real markers
        for matched, line_no, excerpt in hits:
            key = matched.lower().strip()
            counter[key] += 1
            examples.setdefault(key, (line_no, excerpt))

    top = []
    for marker, count in counter.most_common(20):
        line_no, excerpt = examples[marker]
        top.append({"marker": marker, "count": count, "first_line": line_no, "example": excerpt})

    budget = ch["density_budget"]
    # Below ~250 words, density is dominated by sampling noise: a single marker in an 84-word
    # post reads as 11.9/1000 and would escalate a one-line fix to "rewrite". Short forms are
    # judged on absolute marker counts instead.
    short_form = total_words < 250
    if short_form:
        if scored_markers <= 1:
            severity = "low"
        elif scored_markers <= 3:
            severity = "medium"
        elif scored_markers <= 6:
            severity = "high"
        else:
            severity = "critical"
    elif density < budget * 0.5:
        severity = "low"
    elif density < budget:
        severity = "medium"
    elif density < budget * 2:
        severity = "high"
    else:
        severity = "critical"

    hard_count = sum(h["count"] for h in hard_fails)
    plural = "" if scored_markers == 1 else "s"
    scale = f"{scored_markers} marker{plural} in {total_words} words" if short_form \
        else f"density {round(density, 1)}/1000 (budget {budget})"

    if hard_count == 0 and not house and severity == "low":
        verdict = "CLEAN — check the positive side (voice, varied rhythm, a stated boundary) and ship."
    elif hard_count == 0 and severity in ("low", "medium"):
        verdict = f"SPOT FIXES — no hard bans hit ({scale}); work the soft markers listed and re-run."
    elif severity in ("low", "medium"):
        verdict = (f"HARD FAILS ({hard_count}) — fix every hard_fails entry and the house-rule "
                   f"violations; the rest of the draft is sound ({scale}).")
    else:
        verdict = (f"REWRITE — {hard_count} hard fails at {scale}. Spot-editing will not save "
                   f"this draft; redraft the affected sections.")

    return {
        "language": lang,
        "channel": channel_name,
        "channel_label": ch["label"],
        "profile": profile,
        "total_words": total_words,
        "total_markers": total_markers,
        "em_dashes_excluded_from_density": em_dash_hits,
        "ai_density_per_1000_words": round(density, 2),
        "density_budget": budget,
        "severity": severity,
        "short_form": short_form,
        "verdict": verdict,
        "hard_fails": hard_fails,
        "house_rule_violations": house,
        "markers_by_category": dict(sorted(markers_by_category.items(), key=lambda x: -x[1])),
        "style_metrics": sm,
        "top_offenders": top,
    }


def main() -> int:
    p = argparse.ArgumentParser(
        description="Detect AI-tells in 3DLOOK content (articles, posts, DMs, pages)."
    )
    p.add_argument("path", nargs="?", help="Path to the text/markdown file.")
    p.add_argument("--stdin", action="store_true", help="Read text from stdin.")
    p.add_argument("--lang", choices=["uk", "en", "auto"], default="auto")
    p.add_argument("--channel", choices=list(CHANNELS.keys()), default="any",
                   help="article | post | dm | page | any")
    p.add_argument("--profile", default=None, help="Social/outbound profile, for the report only.")
    p.add_argument("--pretty", action="store_true")
    p.add_argument("--summary", action="store_true",
                   help="Human-readable digest instead of JSON.")
    a = p.parse_args()

    if a.stdin:
        text = sys.stdin.read()
    elif a.path:
        text = Path(a.path).read_text(encoding="utf-8")
    else:
        p.error("Provide a path or --stdin.")

    r = analyze(text, a.lang, a.channel, a.profile)

    if a.summary:
        print(f"{r['channel_label']} · {r['language']} · {r['total_words']} words")
        scored = r["total_markers"] - r["em_dashes_excluded_from_density"]
        if r["short_form"]:
            print(f"AI markers: {scored} in {r['total_words']} words (short form, counted not scored) -> {r['severity']}")
        else:
            print(f"AI density: {r['ai_density_per_1000_words']}/1000 (budget {r['density_budget']}) -> {r['severity']}")
        if r["em_dashes_excluded_from_density"]:
            print(f"em dashes: {r['em_dashes_excluded_from_density']} (hard fail, excluded from density)")
        print(f"VERDICT: {r['verdict']}")
        if r["hard_fails"]:
            print("\nHARD FAILS:")
            for h in r["hard_fails"]:
                markers = ", ".join(f"{x['marker']!r} (L{x['line']})" for x in h["hits"][:5])
                print(f"  [{h['category']}] x{h['count']}: {markers}")
        if r["house_rule_violations"]:
            print("\nHOUSE RULES:")
            for v in r["house_rule_violations"]:
                print(f"  - {v}")
        if r["top_offenders"]:
            print("\nTOP SOFT MARKERS:")
            for o in r["top_offenders"][:10]:
                print(f"  {o['count']}x {o['marker']!r} (L{o['first_line']})")
        return 0

    print(json.dumps(r, ensure_ascii=False, indent=2 if a.pretty else None))
    return 0


if __name__ == "__main__":
    sys.exit(main())
