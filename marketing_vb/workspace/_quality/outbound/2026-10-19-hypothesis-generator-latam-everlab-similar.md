---
qc_date: 2026-10-19
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-10-19-latam-everlab-similar/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 15/20
status: good
coordinator_review: done
---

# QC Report — hypothesis-generator — 2026-10-19

**Artifact:** `workspace/outbound/campaigns/2026-10-19-latam-everlab-similar/hypothesis.md`
**Total: 15/20** — good (approve after the top-3 fixes, before step 2 runs)

**Scored against:**
- the coordinator's step-1 brief
- the EU template (`2026-10-19-eu-everlab-similar/hypothesis.md` and its `companies.md`)
- `2026-10-05-latam-health-weightloss/hypothesis.md`, `responses-summary.md` and `import-log.md`
- `icp-detail.md`, `proof-points.md` and `accuracy-formulations.md`
- `global-company-registry.json` and `PROFILE_GEO` in `outbound-pipeline.py`
- the 10-19 EU hypothesis QC
- the agent's own fetched page text, in session transcript `agent-aba8936f078dbd710.jsonl`

**Taken as fact:** limits, signature, bans, detector and completeness.

**Limits:** no web tool, so I checked external claims against what the agent actually fetched, not against the live pages. I had no shell, so notify.py was not run.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 4/5
- **Followed the brief:**
  - Template structure and standing decisions carried over (l.25-31).
  - Language and compliance defaults taken from 10-05 (l.30, l.206, l.219).
  - Mexico question raised as instructed (l.270).
  - No per-person tables, and the research stayed light.
- **Registry claims check out:**
  - 38 `2026-10-05-latam-health-weightloss` keys in `global-company-registry.json`.
  - The `holi` key is `olena`, 2026-07-21.
  - Axo is on the EU `companies.csv`.
  - `PROFILE_GEO["katya"]` still lists Israel and the Gulf, and its `latam` and `south america` needles exist.
- **The template's own outcome is not used.**
  - The EU file it clones records that about 19 leads gave 18 companies, and the list reached 25 only after Vadim released 7 pool companies (EU l.33-38; EU `companies.md` "Pool for Vadim").
  - The LatAm count (l.62) and gate (l.243) do not use that precedent.
  - Step 2 is not told to build a release pool, the mechanism that rescued the EU list.

### B. Factual accuracy — 3/5
- **Internal claims all match:**
  - Everlab decline: AU `responses-summary.md` l.38.
  - Clinique La Prairie decline: EU 10-07 l.22.
  - 128 invites: `import-log.md`.
  - 4 replies, three of them in English: Sensorial asked for studies, Inc Beauty asked how it works, OrienteMe named the Head of Product. The fourth was a Portuguese greeting (10-05 `responses-summary.md`).
  - Validation population: `accuracy-formulations.md` §1.4.
- **External claims that match the captured text:**
  - Fleury Lifecare: R$35M, follow-up cycles in an exclusive app, indicators including body composition and abdominal circumference, R$38B (Saúde Business).
  - Centeni: founded May 2025, 200+ subscribers before launch, two cycles a year, WhatsApp, home collection, digital panel (Exame).
  - SBMCL founded on 8 August (Viva).
- **l.80, Axo misattribution.** Forbes Perú says "cerca de 1.000 membresías activas ... y operan en Europa y Perú". That is a company-wide count, but the sentence ties it to the Peru membership. "With a local lab partner" was not found in the captured source text.
- **l.80, Vitaleo framed selectively.** Forbes Argentina calls it "una plataforma de suplementación personalizada basada en análisis de sangre e IA". The evidence presents it as the preventive-membership model with no qualifier. Only the lead note (l.55) flags the supplement anti-case.
- **l.56 vs l.286, MRI source.** The "private, out-of-pocket trend" framing comes from a different 2024 article that describes a worldwide trend. The cited Canaltech piece is the experts' warning ("moda arriscada").
- **l.62 contradicts the leads.** It says "Argentina ... surfaced no membership model with an app", yet two of the five to-check leads are Vitaleo (a dashboard membership launching in Argentina) and AIONIS (Buenos Aires, digital tools).
- **l.222 and l.39 contradict the bans.** Replies are told to quote §1.9 "each in its own wording", but:
  - The same line bans "clinically validated" and "peer-reviewed", and so do `banned_terms`. Both phrases are inside the §1.9 sentences.
  - Three §1.9 sentences carry "positioned as", which `accuracy-formulations.md` §2.1 and §2.3 say fails the gate.
  - The validation-population clause is §1.4, which the "only" list leaves out.
- **Product numbers are clean.** No client is named.
- **Market figures** (R$35M, 200+, ~1,000, R$38B) are sourced and fenced as context only, with their terms banned in copy. So the proof-points cap is not applied, as in the EU QC.
- **Sourcing:** 7 opened external sources and 5 search-only leads. The search-only leads are labelled honestly (l.286). AIONIS rests on a snippet with no URL kept.

### C. Brand & tone — 2/3
- No em or en dashes. Banned words appear only inside the ban lists (l.11, l.225).
- **Corrective "X, not Y" in carded sections:** l.53 "not verified rows", l.58 "that thesis, not this one", l.230 "Displacement, not this campaign." The file's own l.225 bans this construction.
- **Prospect names in the carded persona (l.89).** "The Clinique La Prairie answer" and "the Sensorial question" go to the sequencer verbatim.
  - Clinique La Prairie was dropped from `banned_terms` (the EU template had it, EU l.12).
  - Sensorial is an active `katya` account and is not banned either.

### D. Format & structure — 3/3
- Frontmatter is complete: `product`, `profile`, `market`, `created`, `status: draft`, `use_case`, `cap_per_group`, `referral_call`, `banned_terms`.
- The path is correct and the `titles` block has one title per line in EN, PT and ES.
- Section names match the template.

### E. Output quality — 3/4
- **Strong:**
  - The thin-market risk is stated plainly, with counts that add up (l.55-62: 1 likely + 5 to check, 2-5 verified).
  - The no-padding stop is explicit (l.243).
  - Localisation is good: the `lang=pt|es` screen, PT and ES titles, hospital, health-plan and lab-group anti-cases, and the Holi name-collision guard.
  - The Sensorial lesson turned into an evidence-question rule, and there is a language-signal metric (l.266).
  - The success metrics are sized to the volume (l.261-263). That fixes the EU QC's top issue.
- **The default path spends a step-2 cycle the file predicts will fail.** l.62 says step 2 will likely stop under 20. Yet that question is OQ6 of 11 (l.275), not a pre-step-2 decision. The agent prompt calls a list that cannot be built "потраченный цикл".
- **Mexico is not offered as a lever.** OQ1 (l.270) excludes Mexico and OQ6 (l.275) lists only "lower the gate" or "widen C". The largest lever available to Vadim is never connected to the thin-market question.
- **Soft padding is left open:**
  - WhatsApp counts as the between-assessment layer (l.49, l.72), and fit-3 rows count toward the gate (l.51, l.276).
  - No test separates a published health-team follow-up channel from WhatsApp booking chat, which nearly every Brazilian clinic has.
  - OQ7 dropped the EU clarification "in B only with clinician or coach follow-up" (EU l.256).
- **The only "likely" account is the riskiest shape.** Fleury Lifecare measures body composition and abdominal circumference on site (l.81), which is the Clinique La Prairie objection setting. It also sits inside a lab group whose labs are an anti-case (l.232). The file handles this (OQ4), but the risk is not counted in the estimate.

## Top 3 issues (priority for improver)

1. **The thin market is not routed to a decision before step 2.**
   - Move the l.62 finding to the top as a pre-step-2 question for Vadim.
   - Add the EU precedent: 18 found, 7 released.
   - Add Mexico (OQ1) as an option in OQ6.
   - Tell step 2 to record a separate release pool with the default or anti-case behind each exclusion.
2. **Two evidence claims overstate their sources (l.80):**
   - Axo's ~1,000 memberships are Europe plus Peru, not Peru.
   - Vitaleo is a supplementation platform in its own source.
   - Also reconcile l.62 with the Argentina and Uruguay leads, and attribute the MRI-trend framing to the article it came from (l.56).
3. **Padding and copy-safety gaps:**
   - Define WhatsApp as qualifying only when it is a published health-team follow-up between cycles (l.49, l.72).
   - Restore the EU fit-3 clarification in OQ7.
   - Put Clinique La Prairie and Sensorial into `banned_terms`, or drop their names from l.89.
   - Fix the §1.9 reply rule: name §1.4 and exclude the "positioned as" sentences per §2.1 and §2.3 (l.222, l.39).

## Coordinator review

agreement: ✅ agree
top_issue: the thin market is not routed to a decision before step 2 (no EU-style release pool, Mexico not offered as a lever). Spot-checked: l.89 still names Clinique La Prairie and Sensorial in the persona section while neither is in banned_terms; l.80 ties Axo's ~1,000 memberships to Peru. Fixes 2-3 and the file part of fix 1 (pool step, Mexico option, EU precedent) go to a fresh hypothesis-generator fix round; the scope decision itself (Mexico, gate, widening C) goes to Vadim.
