---
qc_date: 2026-11-19
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-11-19-latam-connected-fitness/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 15/20
status: good
coordinator_review: pending
---

# QC Report — hypothesis-generator — 2026-11-19 (LatAm connected fitness, katya)

Saved by the coordinator from the QC agent's final message (the agent could not write report files).

**Total: 15/20** — good (approve after the fixes below)

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## Answers to the brief's questions

**1. Sub-segment fit / persona = app owner.** Mostly yes. The page argues the gym case itself (comparison column "In-gym body scanner", "FitXpress covers the check-ins between visits", FAQ "Each repeat needs a club visit"); H1, Problem and benchmarks are app-only (hypothesis knows, l.193). Group B (gym-software platforms) is the best structural fit. P1 (CPO, Head de Produto, Head of Digital; Diretor Técnico for the assessment, l.95) is right; the "Whose app" rule (l.212) is the right guard. Breaks: (a) franchise rows — Planet Fitness México and Anytime Fitness México apps belong to the US franchisor (l.42, l.322), yet recommended IN; (b) "our app" not established for Skyfit, Panobianco, Selfit, Gaviões (vendor apps → no product-lane owner); (c) blanket NOT `Marketing`/`Growth`/`CRM` (l.105) can remove the real app owner; ICP §8 lists Head of Growth and Digital Experience Manager; PPL-3 says "do not fill the cap with", not "exclude".

**2. PT/ES capture-screen gap.** Honest in copy (kept out l.207, replies routed to product l.94, OQ 13, fixed capture layer named l.303). Under-weighted as a risk: Risk 6 itself says a chain cannot ship an English-only capture — a go/no-go for Brazil/Mexico member apps — yet it is OQ 13 of 16, not in "Read this first", asked only "before step 5", no plan for "no". OQ 13 calls the roadmap row MT-oriented; roadmap.md l.28 says "MT + FX".

**3. Rules as targets.** Mostly targets (lane "Target:", easy out as target l.216, pilot as list of parts l.202; quotes limited to approved verbatim lines). Ready copy: MSG-4 rule (l.205) "the phone scan covers the check-ins between visits, at home, under the chain's brand, with 80+ measurements and a record in the chain's app"; "The angle" (l.176). "check-ins between (club) visits" appears 11× in the file, 5× in card sections (l.67, 176, 200, 205) — expect repetition at Smart Fit.

## What was wrong

**A (4/5).** TotalPass treated four ways (Reserve l.50, Out l.52, FAIL in Smart Fit row l.270/l.331, banned_terms l.12), no Open question of its own (OQ 9 covers only Wellhub); ICP §8 includes corporate platforms and TotalPass is in-market. Validation bar "fewer than 10: stop" with 24 rows, not argued against the 30-company bar.

**B (3/5).** l.27, l.73, Risk 5: "validation participants from the US and Europe" — that row is **Training data** (proof-points l.73), not the validation study. l.90: replies "say the reference-device work is under way" — roadmap.md l.22 "Lab story needs the CEO's OK"; contradicts l.207. l.44/l.54: Bodytech Colombia counted as evidence in hand though its app is "reported in development". l.324: localization row is MT + FX. l.317: "Your 2026-11-19 direction keeps 'FitXpress is not a medical device.'" — not traceable to inputs.

**C (2/3).** Boundary line default puts "FitXpress is not a medical device." in every pair to LatAm gym readers; the 2026-11-05 LatAm campaign dropped it (basis UK/EU MDR); audience.md §3: no medical language for fitness. The fallback is backwards: keeps the medical clause, drops "It provides structured body data for coaching and program workflows".

**D (3/3).** No issues.

**E (3/4).** Rules contradiction: l.213 "no two people at one company share … a Message 2 value point … an easy-out target" vs l.216 (two easy-out targets) and l.202 (pilot to ~half) — impossible at Smart Fit (30-50). Titles block (l.107-166) lacks CEO, COO, CPO, CTO, Fundador, Cofundador, Sócio, Diretor Executivo. Inclusion allows "or in-app training plan" without an assessment (l.38, l.269) while the pain assumes one; 4 of 9 evidence rows (Sports World, Megatlon, SportClub, Planet Fitness México) show no assessment.

## Top 3 fixes

1. Make capture-screen language a gate before step 2: into "Read this first", ask product before research/people spend, state the "no" action (hold, or group B only with PT/ES flagged); roadmap row = "MT + FX".
2. Rules contradiction and persona gaps: unique wording, shared value points / easy-out targets allowed; add abbreviations + Fundador/Cofundador/Sócio/Diretor Executivo to titles; franchise rows OUT or referral-only by default; narrow the Marketing exclusion; require an assessment or a separate pain branch for training-plan-only chains.
3. Claims slips: training data ≠ validation; drop "reference-device work is under way"; reverse the boundary fallback; confirm the medical-device direction; MSG-4 and angle → targets; one status for TotalPass with its own Open question.

## Coordinator review

- agreement: agree (15/20). B-l.317 is on me: my brief told every agent "'FitXpress is not a medical device' framing stays" — my wording, not Vadim's; for LatAm the 2026-11-05 precedent (clause dropped) wins unless Vadim says otherwise.
- top_issue: PT/ES capture screens are a go/no-go for consumer gym apps — asked of Vadim/product before step 2, not step 5.
