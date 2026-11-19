---
qc_date: 2026-11-19
agent: hypothesis-generator
artifact: workspace/outbound/campaigns/2026-11-19-au-connected-fitness/hypothesis.md
track: outbound
artifact_type: hypothesis
total_score: 12/20
status: marginal
coordinator_review: done
---

# QC Report — hypothesis-generator — 2026-11-19

**Artifact:** `workspace/outbound/campaigns/2026-11-19-au-connected-fitness/hypothesis.md`
**Total: 12/20** (marginal). It needs a rework, not a full regeneration. The research, the exclusion arithmetic and most of the Rules can be reused. The group design and the card format need to be rebuilt.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 2 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 2 | 4 |

## What was wrong (specific)

### A. Adherence — 3/5
- **Done as briefed:** Message 1 follows company line, method pain, mechanism and payoff, then one question, with no call or link (l.195). Message 2 ends on a soft ask (l.193). No client names (l.209). Retention runs only as a tagged test, with no retention lane (l.162, 246). Only new people are contacted (l.100, 314a). The July funds come back with their history (l.100). Customers stay out (l.96).
- **The brief says "companies may return", and the file defaults the other way.** l.23 says "Under the 3-month rule, re-contact opens on 2027-01-02". No such rule exists: a grep of runners/, docs/, scripts/, agents and exclusions/ finds only the 6-month decline/no_reply windows. Even so, l.99 makes all 56 companies FAIL, and l.280 calls any registry hit "a research error". This contradicts the file's own decision #10 (l.273), the 11-17 rule, and Vadim's 2026-10-11 waiver of 5 brands 9 days after their send. l.314 cites that waiver itself.
- **The October hold is valid, but the date on it is invented.** The hold has a real basis: the campaign was at 96/325 invited on 10-31 (verified in `data-2026-10-31.md`). That is a concurrency reason. "Not before 2027-01-12" (l.25, 317) is not.
- **Group D is the best page fit, and it is gated behind "only if Vadim opens it"** (l.49, 88-90). Group C is the weakest fit, and it is in by default.
- **Only partly one hypothesis.** It has three different pains (A/D, B, C at l.175-177), three pilot variants and three sets of word rules. The prompt asks for one hypothesis.

### B. Factual accuracy — 2/5
- **l.23 "3-month rule":** a process rule stated as existing, with no source anywhere in the repo (see A).
- **l.212 (fund rule, goes verbatim to writers):** "any comparison covers two scans the member chooses". `compliance.md`:57 says Body Progress compares two scans "chosen by the customer", and the approved wording is "the program compares scans it selects". The member does not choose.
- **l.92:** "Centr and F45 (US head office, `nick`)". The 10-02 research (`companies-verified.csv` AUFIT-04) has Centr in Melbourne, with a US PE owner and the note "Confirm the current head office". No new source is given. The US sibling QC found that Centr now belongs to no profile.
- **Numbers cleared for copy are not in `proof-points.md`.** l.205 allows Adjust 24% → 7% and Kidman 70% in Message 1. `proof-points.md` says such numbers need a STOP and a question to Vadim, and no open question asks it. The page log for 2026-10-02 says Adjust 7% was confirmed only through the search index (the page returned 429). The page judges flagged it as "unconfirmed at primary source", and it is global 2022 data whose year is not carried into the rule. The hard cap (B ≤ 2) is applied to copy-cleared numbers only. The sourced market figures in "Why plausible" (AusPlay, Ausleisure, GapMaps) are not penalised.
- **Correct:** page facts (80+, estimates, BMI/BMR as calculated metrics, record/API, white-label, SDKs, Pro-plan 3D tools); voice prompts banned per `roadmap.md` (l.207); repeatability wording (l.208); 100+ and 112,100 wording (l.209); the 17+44−5=56 sum; HYP-2/3 arithmetic (l.242, 290-294); Bupa July history (verified in `responses-classified.csv`).

### C. Brand & tone — 2/3
- **l.175-176:** the A and B pain targets are finished sentences built on "so" introducing a result ("…the photos are not measured, so changes in waist… do not show as numbers"; "…for every repeat, so check-ins… have no measured record"). l.222 narrows the CLAUDE.md ban, which covers "so" introducing a result *or* benefit, to "benefit" only. Writers will copy both sentences.
- Minor: l.60 "measure effort, not body change" uses the corrective X-not-Y in prose that ships in the card's evidence. The l.17 H1 em dash comes from the prompt's own template (not scored).
- Body-image, population and fund-language rules are thorough (l.217-218, 212).

### D. Format & structure — 3/3
- The frontmatter is complete: `product`, `profile`, `market`, `use_case`, `cap_per_group`, `banned_terms`, `learnings`, `message_max_chars`. The file also has the `titles` block, the Account facts placeholder, `## Learnings applied` with every ID, and the template sections in order. No issues against the prompt's template. The gate-format problem is scored under E.

### E. Output quality — 2/4
- **The group design is inverted.** The best page fits are held back: D (own apps; 12WBT "members log measurements") and Centr. C is kept "because the funds are large" (l.28) and as "the only untouched group large enough to carry HYP-3's sizing" (l.318). At 15-25 people per fund (l.318), the 7 funds take about 105-175 of the ~200 invites. The campaign would mostly be a health-fund read of a fitness-app page, including the HYP-6 test.
- **The list padding fails its own screens:**
  - Row 12 Boutique Fitness Studios: "brand apps belong to the US franchisor". It fails screen 1, "An app it owns" (l.41).
  - Row 15 HBF: "Not verified".
  - Rows 10-11: evidence is franchise-for-sale listings.
  - Rows 3-4 (Ovum, Welly): conditional OUT.
  - Row 1 Emily Skye: 0 people.
  - Realistic page-fit count (A+B+D): about 8-13, not 16-20.
- **B's pain contradicts its own rule.** It assumes measurement "on club hardware" (l.176) but forbids saying the club has a scanner, and most reformer studios have none.
- **The gate cannot see the most copyable lines.**
  - Lanes are a table (l.164-171) and questions are a "Question topics" paragraph (l.181).
  - `outbound_pack.py` reads lane notes only as `- **\`lane\`** …` (LANE_NOTE, l.1903) and question targets only as "Question targets:" inside them (l.1931-1947).
  - Result: the card-copy 5-gram check never scans the pain sentences, and the repeated-question coverage check runs on zero targets.
  - All three sibling files use lane notes.
- **Funds make the variety rules impossible.** Only 3 of the 5 question topics apply at C. l.221 requires a different opener, central question, product sentence and closing shape for every person at one company, at 15-25 people per fund.
- **One shared titles block (l.126-158) for all four groups.** At funds, "General Manager", "Product Manager", "Product Owner", "Business Development Manager" and "Head of Health Services" pull insurance-product, broker and provider-network roles. The not-the-buyer list (l.120) excludes those roles.
- Small conflicts:
  - OQ1 bans "plan wording" (l.312), while the fix list allows "on the Pro plan" (l.179, 206).
  - The validation floor is 20 rows (l.279), while l.65 says "Floor: 16".
  - The OQ2 rationale (l.313) acts on MSG-5, which is a [watch] item.
  - OQ8 (l.319) defers NZ, although Les Mills fits the page better than any fund.
- **Strong points:** "Read this first" catches the August → October date premise with evidence. The exclusion arithmetic and history are verified. The pilot is described whole (l.198-204), and the C variant drops the paid-tier measure.

## Coordinator's questions

- **16-20 companies.** The arithmetic is honest, but part of the shortfall is self-made: the invented 3-month rule, D gated, and Centr routed out without a source. The other part is real: October is still inviting. Without C and the padding, the page-fit list is about 8-13.
- **Coherent or stitched?** A, D and B franchisors that own their app share the page argument: the member checks progress inside the brand's app, the coach reviews it, and 3D sits in the paid tier. C is stitched on for count, and the file says so (l.28, 318).
- **Health funds.** Not a fit for this page.
  - The page's stats are about app churn. Its pilot measures free-to-premium. Its coach step is a program block. None of these apply to a fund.
  - The agent had to remove the paid-tier measure and ban "premium". "Matching plan" (l.202) and retention figures (l.205) still read as cover and policyholder retention.
  - That retention frame is what Bupa declined in July (l.86). The same three funds gave 0 interested on ~202 invites.
  - Funds belong to ICP §4, with their own campaign and asset.
- **Targets or samples?** "Rules for steps 3-5" are mostly targets. The easy-out is a pointer (l.197), the pilot is a spec, and verbatim text is used only where it is licensed (l.208-209). The samples sit in "Message angle": the three pain sentences (l.175-177) and five near-finished questions (l.181). The format hides them from the gate.

## Top 3 issues (priority for improver)

1. **Rebuild the group design around the page.**
   - Open D by default, under the 11-17 rule and "companies may return".
   - Delete the "3-month rule". Keep only the October concurrency hold, re-opened when its invites finish and its replies are classified.
   - Take C out into its own §4 campaign.
   - Settle Centr's head office with `nick`.
   - Drop BFS (fails screen 1) and HBF (unverified).
   - State the honest page-fit count and let Vadim choose between a small list, NZ (Les Mills) and January.
2. **Rewrite lanes as gate-readable lane notes** (`- **\`product\`** … Question targets: …; …`). Move the per-group pains into them as fragments, without "so" + result. Restore the CLAUDE.md "so" ban (result or benefit) at l.222.
3. **Fix the copy facts.**
   - "The program compares scans it selects" (`compliance.md`:57).
   - If C survives anywhere: no "plan" in the fund pilot, no retention figures at C, a fund-specific titles block, and a per-fund limit.
   - Add Adjust (2022 data) and Kidman to `proof-points.md`, or ask Vadim, before they go into Message 1.
   - Align OQ1 with the "on the Pro plan" fact.

## Coordinator review

(filled in by Claude in chat after the automatic QC run)
