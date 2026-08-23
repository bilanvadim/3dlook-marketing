# Log — awards & rankings submission tracker

**Track:** pr (new — no existing track fit "which rankings/awards to submit to and when," so this
sits alongside seo/social/outbound/pages/health/research/trust-article/_quality rather than being
force-fit into one of them. Flagged for Vadim as a naming decision, not a unilateral one — see
open-questions.md #8 for the related `product:` frontmatter question.)

**Task:** 2026-08-23-awards-and-rankings

## What was done

1. Delegated live web research (general-purpose agent, WebSearch) to check current 2026/2027
   submission windows and eligibility rules for ~24 ranking/award programs (Inc 5000, Deloitte Fast
   500/Fast 50 variants, FT rankings, Stevie Awards programs, MedTech Breakthrough, Digital Health
   Awards, Globee, BIG Innovation Awards, SaaS/Cloud Awards, Fast Company, CES Innovation Awards,
   Fierce Healthcare, HealthTech Impact, VivaTech Female Founder, InsurTech100, Gartner/CB Insights
   analyst recognition, MM+M 40 Under 40), checked against 3DLOOK's real 2025 numbers (ARR $1.084M,
   67 active customers, founded 2016).
2. Wrote `priority-list.md`: hard-no list (revenue/geography floors we don't clear), a ranked
   shortlist of 6 programs worth acting on this cycle, a "worth tracking, not drafting yet" list, and
   immediate next steps for Vadim.
3. Drafted submission copy for the 4 highest-priority, deadline-confirmed programs:
   - `drafts/01-stevie-women-in-business-essay.md` (deadline Sept 3, 2026 — most urgent)
   - `drafts/02-fast-company-most-innovative-application.md` (deadline Oct 2, 2026)
   - `drafts/03-big-innovation-awards-nomination.md` (deadline Nov 27, 2026)
   - `drafts/04-fierce-healthcare-innovation-awards-submission.md` (deadline unconfirmed, entries open)
   Plus two non-drafts flagging why: `drafts/05-digital-health-awards-notes.md` (deadline not
   published yet) and `drafts/06-medtech-breakthrough-watch-note.md` (2027 window not open yet).
4. Ran `brand-checker` against drafts 01 and 02. Both came back FAIL on first pass: em dashes
   throughout (hard-banned per CLAUDE.md §6 / ai-tells-sweep.md), corrective-negation constructions
   ("isn't X, it's Y" / "not X, but Y"), essay 01 ran ~14 words over its 525-word cap, BMI/HIPAA/GDPR
   not expanded at first use, and one unsourced claim (Gartner/CB Insights/RTIH finalist status,
   present in `overview.md` but not `proof-points.md`) plus a tenure-implying line about Katerina
   that isn't documented anywhere. All fixed: dashes removed from submittable copy, negation
   rewritten to positive scoping per M2, essay trimmed to 522/525 words (bio 117/125), abbreviations
   expanded, unsourced claim and unverifiable tenure line dropped rather than kept and hedged.
5. Applied the same em-dash and phrasing fixes to drafts 03 and 04 by inspection (not yet re-run
   through `brand-checker` — flagged inline in each file as a to-do before Vadim treats them as
   final).
6. Wrote `open-questions.md` — 8 items that need Vadim's answer before anything in this folder is
   submitted (revenue-disclosure comfort, Katerina's founder status, entry fee budget/approval,
   category selection, legal entity/HQ facts for the "hard no" list, whose name is the company
   spokesperson, missing supporting assets, and the `product:` frontmatter enum gap).

## What was explicitly NOT done

- Nothing was submitted anywhere. Per CLAUDE.md §10.2, this bot has no publishing keys and no
  submission-portal access even if it did — everything here is an artifact for Vadim to review, edit,
  and file himself.
- No numbers were invented. Every figure in every draft traces to `brand-assets/product-info/
  proof-points.md` or `overview.md`; anything not in those files (Katerina's founder status, exact
  entry fees, exact deadlines for 3 programs) is flagged as an open question instead of guessed.
- Drafts 03 and 04 have not been through a full `brand-checker` pass yet — flagged as a next step,
  not silently skipped.

## Coordinator review

agreement: ✅ agree — both `brand-checker` FAILs were correct and specific; fixes applied match the
findings exactly (dashes, negation, word count, abbreviation expansion, unsourced claim removal).
top_issue: the same em-dash habit that brand-checker exists to catch showed up in my own first-pass
drafts across all 6 files, including the internal notes — worth remembering next time this artifact
type comes up: write the submittable copy dash-free from the first draft, not as a cleanup pass.
