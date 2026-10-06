---
qc_date: 2026-10-06
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-06-uk-weight-management/messages/ (primary: barbara-mcgowan-a36891192, chiaulingchow, dr-george-sanders-0a4429193; _check.json; 7 summaries; all 8 _batch-*.md read in full for the per-company cross-check)
track: outbound
artifact_type: messages
total_score: 11/20
status: failed
coordinator_review: done
---

# QC Report: message-sequencer, 2026-10-06, uk-weight-management

**Artifact:** `workspace/outbound/campaigns/2026-10-06-uk-weight-management/messages/` (223 people, 8 batches)
**Total: 11/20, failed.** This does not mean regenerating all 223. Regenerate the LighterLife referral pairs (both batches) and the Counterweight South Africa pool with a different approach. Reset Health and MoreLife need sentence-level fixes.

**Scoring basis.** Scored against `card-messages.md` and the `_profiles-*.md` files. Gate results (limits, signature, bans, completeness) are taken as fact. D is not capped for the missing `product:` in the split files: `split-messages` writes those files, and the 2026-10-02 QC treated them the same way.

**What holds:**
- Hooks are real, and title-based where the profile is empty.
- No client is named, and no number is invented.
- No outcome promise and no verification framing.
- The NHS, children, pregnancy, owner and Pharmacy2U rules hold.
- The South Africa and Malaysia asks go to the UK head office without local claims.
- No LighterLife message says "your app".

**What fails is the campaign's central rule.** card:35 and card:122 say no two people at one company share an opener, a central question, a closing ask, an M2 opener or a product sentence.
- LighterLife's 64 referral pairs run on one skeleton.
- LighterLife batch 2 got unique questions by asking things unrelated to the scan.
- Counterweight's South Africa pool shares one product sentence.
- Reset Health's executive and clinical peers share CTAs that the gate named and the agent left in place.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 2 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 2 | 4 |

## What was wrong (specific)

### A. Adherence: 2/5
- **Gate-named collisions inside one company were left unfixed.** This breaks prompt checks 2, 9 and 10 and the ⚠ rule ("opener repeated" inside one company is the agent's to fix). card:106 names Reset Health's executive and clinical leaders as the first peer group. The pairs, all in `_batch-reset-health-1`:
  - M1 "Open to 15 minutes?": oliver-mcguinness-6001894a (CEO, :33), thomas-curtis-844271263 (:363), barbara-mcgowan-a36891192 (CMO, :143).
  - M1 "Worth a quick chat?": laura-newson-a0146a20 (:55), racheldreycroft (:253), dr-claudia-ashton-332922237 (:341).
  - M1 "Open to a quick chat?": chiaulingchow (:77), laurensien (:231).
  - M2 "Could we take 15 minutes?": oliver-mcguinness (:41), dr-claudia-ashton (:349).
- **Batch 2 was told to read batch 1 and still copied it.**
  - raquelsanchezwindt M1 (`_batch-reset-health-2`:9) is barbara-mcgowan's product sentence with two words swapped. They are an endocrinologist and her CMO.
  - LighterLife batch 2 repeats exact closing asks three times each (see E).
- **Lane recipes in card:60-64 were missed.**
  - Technical-integration M2 has no FAQ link in garethbartley (:470-474), yousaf-ahmad-00100240 (:494-496) and alasdair-yorke-b19ab390 (:531-533).
  - The clinical lane has no repeatability sentence in barbara-mcgowan, dr-sarah-oldfield-5a8505253, dr-claudia-ashton and thomas-curtis.
  - The product lane has no explicit 15-minute ask in laura-newson, rebecca-ryan-1a42b444 and racheldreycroft.
- **The company is not named in four M1s.** card:122 says "Name the company in every Message 1". deborah-evans-27a2bb1a1, dr-claudia-ashton, andrew-liles and laurensien name neither Reset Health nor Roczen. The gate flagged them and they were left.
- **29 gate-named speed-wording notes were left.** card:136 says "the only speed wording". `_summary-morelife-1` acknowledges 10 of them instead of fixing them.
- **`_summary-reset-health-2.md` does not exist.** Step 5 was skipped for 15 people, and nothing about them was flagged to Vadim.

### B. Factual accuracy: 3/5
- **"100+ clients" is inflated in nine M2s.** It is the all-time 3DLOOK count across both products. Proof-points has 67 active in 2025, internal only. These nine messages present it as current users, and six of them as FitXpress users. Prompt rule 3 says do not inflate.
  - sonel-patel-4439a94b, "100+ clients use FitXpress today" (`_batch-lighterlife-2`:38)
  - mikepallett, "…use FitXpress today" (mixed-1:17)
  - naomibrosnahan (counterweight:38)
  - saira-mashru-31a2b11b0 (mixed-1:423)
  - luana-howes-660ba5204 (mixed-1:463)
  - laurenrockliffe (mixed-1:59)
  - alaa-adwan-b4588b229 (morelife-1:224)
  - laura-newson (reset-health-1:61)
  - rebecca-ryan (reset-health-1:193)
- **davidplans M2 (reset-health-1:171) breaks card:137.** "96-97% accuracy" sits in the same sentence as "body composition values are estimates", which is the case card:137 forbids.
- **112,100 is not in its own sentence (card:135).**
  - dr-george-sanders M2 (morelife-1:17) also truncates the speed wording.
  - justin-slabbert (counterweight:17) and annabellhiggs (:59) use the same clause at the same company.
- **juli-mey (morelife-1:99): "Leading 22 practitioners" is a prospect headcount**, which card:129 and card:136 ban. Her M2 (:109) leads its value line with the accuracy figure, sent to a practitioner manager.
- **New or embellished claims:**
  - matthew-buckley-a895631b4 M2 (:201): "results back the same minute" is a new speed claim.
  - sophie-edwards (:40) and david-wong (reset-health-1:567) extend the anonymised 34,000 line with "each followed the same guided sequence".
  - chiaulingchow M1 (:75): "FitXpress adds a guided two-photo scan to the Roczen app" reads as an existing integration.
  - raquelsanchezwindt M1 (reset-health-2:11) offers "a one-page overview" that is not in the card.
- **The compliance line is used inconsistently.** MoreLife has it in 11 of 11 non-referral M2s. Reset Health has it in 3 of 23, and only one of its 8 clinical leaders gets it (Claudia). The card says "at most one"; prompt rule 7 says it is required for a clinical ICP. The conflict should be settled in the prompt.

### C. Brand & tone: 2/3
- **Writer notes leaked into copy.**
  - edna-moneypenny-00bab516 M1 opens "Short and neutral." (lighterlife-2:581). That is the hook-field note, verbatim.
  - judy-monk-217b4a2a: "Short and plain." (:336)
  - georgina-walsh-33b4b5127 M2: "One line, no pitch." (lighterlife-1:710)
  - louisa-flannery M2: "No pitch here."
- **Dangling modifiers make Katerina the subject:**
  - sean-patrick-mcgowan (reset-health-1:543): "Quick question as Reset Health's commercial associate:"
  - david-wong (:559): "Quick note as Executive Chairman of Reset Health:"
  - imogen-bole (reset-health-2:83): "Had a thought as a senior copywriter at Reset Health:"
- **Tricolons (a judgment ban):** barbara-mcgowan M2 (:149), oliver-mcguinness M2 (:39), jessicaravenscroft M2 (:105), sonel-patel M1 (lighterlife-2:30).
- **Presumed knowledge and flattery.**
  - "you will know / you know" opens more than 12 hooks, for example anne-matterface, carol-graves, charlotte-williams, shweta-sidana and amanda-walton.
  - Other lines: "that is a clear path" (olivia-potter), "is a good aim" (grace-bajo), "a platform worth building on" (justin-slabbert).
- **edna-moneypenny implies a gap at head office.** "needs good help pages" goes against card:123 and card:132.

### D. Format & structure: 2/3
- **Lowercase greetings:** "Hi ann," (ann-mcclean-9894653a), "Hi natalie," (natalie-bellis-3279a928), "Hi nikki," (nikki-cook-938694a1).
- **Body paragraphs with 3 sentences** (the prompt allows at most 2): sarah-kelly M1, tina-horsnell M1, sonel-patel M1, andrew-liles M1, pipyoung M1, laurensien M2, naomibrosnahan M2.
- `_summary-reset-health-2.md` is missing (also counted under A).

### E. Output quality: 2/4
- **The three sampled pairs.**
  - **barbara-mcgowan.** M1 is strong: a real hook and a sharp question. M2 repeats M1 as a tricolon and adds only the speed line. It drops the repeatability sentence, which is the first thing a professor of endocrinology would test. "Results arrive in under 45 seconds from the photos to structured results" says "results" twice.
  - **chiaulingchow.** The hook comes from her bio and the question is good. M2 is one capability line plus "That is the whole operational footprint.", which overclaims: integration, a DPA and support still exist. Nothing in M2 is value for her.
  - **dr-george-sanders.** The best of the three: the evaluation question is good. M2 gives an evaluation lead a volume figure as "one data point for your evaluation work", and volume is not evaluation evidence. Its GDPR paragraph is identical to 10 colleagues'.
- **LighterLife batch 2 got unique questions by asking about things unrelated to the scan.** Examples:
  - billing and payments (siobhan-barron, :302 and :308)
  - budget and cost centre (lyn-obeney, :72 and :78)
  - privacy-notice wording (dianne-bishop, :471)
  - sign-up terms (lee-godwin, :490)
  - online reviews (judy-monk, :338)
  - office managers' tools (elaine-wright, :547)
  - language options (carole-brand, :414)
  - social channels (heather-pearle-van-pelz, :509)
  - employer enquiries (christine-smith, :378)
  - waiting lists (paulinehills, :566)
  - centre-to-online moves (deborah-rice, :623)
  - holiday pauses (amanda-walton, :321)
  - video platform (janette-humphrey, :224)

  None of these reaches the card's targets: the owner of the online programme, the client account or the medication service. To a franchisee, a stranger asking who owns billing, the cost centre or the privacy notice reads as reconnaissance. If it is forwarded, it damages the head-office conversation the campaign exists for.
- **Referral M2s mostly add nothing.** They restate the M1 question and add the speed line; 17 of 35 LighterLife batch 1 M2s carry it.

## Per-company mail-merge risk (coordinator's question)

### LighterLife (68): HIGH. Regenerate the referral pairs.
- **One skeleton for all the referral pairs:** LL fact → FitXpress line → "Who at (LighterLife) head office …?" (58 times across 68 people) → "A name…".
- The LL1 "30 years" fact appears 21 times.
- **Identical central question:**
  - jan-badger-b6304535 (:93-95, M2 :101) and georgina-walsh (:702-704, M2 :710), both therapists, ask "who owns the online programme".
  - natalie-cowie, ann-mcclean M2 and natalie-bellis M2 fall back to the same question.
- **Product line repeated:**
  - "We make FitXpress, a two-photo scan that returns 80+ body measurements" appears in jan-badger, karen-burr-3482a18 (:198) and georgina-walsh.
  - "…with 80+ body measurements as the result" appears 7 times: naomi-banham, paul-anthony-brown, patricia-lyon, pat-ashmore, veronica-barry, marion-holder and steve-smith.
- **Hook phrases repeat inside the company:**
  - "Quick idea for you": tracey-fisken (:238) and ali-robbins (:574). The gate flagged it and it was left.
  - "Quick note": anne-matterface and karen-turmer.
  - "Wanted to reach out": jan-badger and donna-earle-swaby.
  - "Had a thought": julie-johnson and patricia-lyon.
  - "Quick thought": john-moore and sally-harris.
  - "Noticed": 12 times in batch 1.
- **Exact closing asks:**
  - Batch 1:
    - "I would value a name to write to.": anne-matterface (:74) and pat-ashmore (:536)
    - "I am looking for a name to ask.": tabithaprince (:557) and veronica-barry (:641)
    - "A pointer would help.": ann-mcclean (:263) and sally-harris (:725)
  - Batch 2:
    - "A name would help.": nikki-cook (:91), janette-humphrey (:224) and heather-pearle-van-pelz (:509)
    - "A pointer would be welcome.": debbie-kennedy (:110), judyhoskins (:148) and marion-holder (:454)
    - "A name would be welcome.": amanda-walton (:321), nicola-gornall (:397) and steve-smith (:604)
    - "A name or a team is enough.": judy-monk (:340), dianne-bishop (:471) and edna-moneypenny (:585)
- **The head-office trio.** sarah-kelly, tina-horsnell-625341193 and sonel-patel all end M2 with "Grab a slot:". Tina and Sonel share an identical M2 sentence: "Results take under 45 seconds from the photos to structured results." The two business development directors named in card:106, Sarah and Tina, share "Open to 15 minutes(…)?" and the same product angle (at home before the weekly online session, web SDK, 80+ measurements and a 3D model).

### Counterweight (22): HIGH in the South Africa pool (11 people, one office)
- **The same product sentence opens 9 of the 19 referral M1s**, worded "We make / build / built a guided scan…" or "Our guided scan returns 80+ body measurements from two phone photos":
  - bjorn-ronaasen (:106), carlotta-schwertel (:140), tommie-wt-breedt (:208), mayuri-bhagat (:242), kelsey-kolbee (:259), katrina-campbell-wareham (:293), zuheirah-toffar (:310), nuhaa-van-der-ross (:344), taryn-goulding (:361).
- **Openers repeat:**
  - "Noticed your background" 5 times: justin-slabbert, annabellhiggs, olga-wojadzis, mayuri-bhagat, taryn-goulding.
  - "Came across your work as a registered dietitian" is identical in naomibrosnahan (:28) and hannahpaigeguthrie (:274).

### Reset Health (50): MEDIUM-HIGH, concentrated in the most senior people
- The CTA collisions are listed under A.
- "Noticed" opens 17 Reset Health M1s; "Noticed your background" 6 times (rochellecmorris, chiaulingchow, davidplans, thomas-godec, siri-steinmo, amanmohammad).
- "Wanted to reach out" appears 3 times in batch 2: raquelsanchezwindt, shweta-sidana, george-hamlyn-williams.
- **Two executives share a proof line.** rochellecmorris (CPO, :17) and david-wong (Executive Chairman, :567) both get the same 34,000 line.
- **The referral product line repeats about 10 times:** "We build a guided two-photo scan with / returning 80+ body measurements…". It appears in siri-steinmo, sean-patrick-mcgowan, dr-adam-barker, peteryeekk, tristandummer, amanmohammad, kelly-m, tiago-grohmann, catherine-webb and dr-nik-adzrul-ariff.
- The RH1 sentence is verbatim in siri-steinmo, dr-adam-barker and davinaa-chandran-rajeswary.

### MoreLife (58): MEDIUM
- **Batch 1's non-referral M2s all have the same three-part shape:** value line, the identical GDPR paragraph, then the 15-minute link. This holds in 11 of 11: dr-george-sanders, sophie-edwards, grant-westermann, susan-brennan, juli-mey, emily-costelloe, georgia-miller, keisha-c, matthew-buckley, alaa-adwan, amy-broadhurst (lines 19-249).
  - Keep the GDPR line only for grant-westermann, sophie-edwards and one clinical lead.
  - Replace it with person-specific value for the practitioner-facing people.
- **CTA collision:** "Grab 15 min:" in georgia-miller (:159) and matthew-buckley (:205), both service managers.
- **Repeated central questions:**
  - Patient-app owner: anthony-hardley (:262), georgia-apsitis (:279), evan-robertson (:447).
  - Adult programme design: christine-render (:296), chad-haefele (:430), richard-ruff (:651), olivia-potter (:566).
- **Identical product sentence:** anjal-panamparambil-saji (:464) and eltrent-summers (:600).
- **Batch 2 has distinct questions but its own tics:**
  - The opener formula "[role A], then [role B] at MoreLife: you have/know…" appears 8 times: nikola-smith, m-ghezal, victoria-simpson, georgia-froude, nicola-lyons, stephen-young, prestonsarah, sophie-dalpra.
  - The M2 formula "X is the thread/topic." appears 5 times: nicola-lyons, jaishri-patel, natalie-shields, georgia-froude, stephen-young.

## Top 3 issues (priority for improver)

1. **Regenerate the LighterLife referral pairs (64) and the Counterweight South Africa pool (11) with a different approach.**
   - Give the writer a pre-assigned grid: each person gets one card theme, one hook-phrase slot, one product wording and one closer.
   - Allow no question outside the card's theme list for LighterLife units; that ends the billing, cost-centre and privacy-notice asks.
   - Drop the speed line from referral M2s.
2. **Fix the Reset Health and MoreLife collisions in place.**
   - The CTAs the gate named.
   - The copied product sentences: raquelsanchezwindt and barbara-mcgowan; anjal-panamparambil-saji and eltrent-summers.
   - The shared 34,000 line: rochellecmorris and david-wong.
   - The 11-times GDPR paragraph at MoreLife.
   - The repeated MoreLife questions (patient app 3 times, programme design 4 times).
   - The lane gaps: FAQ link for garethbartley, yousaf-ahmad and alasdair-yorke; repeatability for barbara-mcgowan, dr-sarah-oldfield, dr-claudia-ashton and thomas-curtis.
   - Write `_summary-reset-health-2.md`.
3. **Claims.**
   - Change "100+ clients use FitXpress (today)" in 9 M2s to the approved "100+ clients" with no present-tense usage claim.
   - Split davidplans M2 so the 96-97% sentence carries no body composition.
   - Give 112,100 its own sentence in 3 records.
   - Remove "22 practitioners" (juli-mey) and "the same minute" (matthew-buckley).
   - Make the 29 speed phrases verbatim.
   - Remove the writer-note leaks (edna-moneypenny, judy-monk, georgina-walsh) and the three dangling "as [title]" openers.

**System notes (not the agent's fault):**
- `check-messages` flags repeated closing asks only for M1 non-referral lines. It missed the four three-way referral closers in LighterLife batch 2.
- Its opener check misses repeated hook phrases ("Noticed your background" appears 6 times at Reset Health and 5 times at Counterweight).
- Add "short and neutral" and "no pitch" to the writer-note ban list.
- Capitalise first names in `split-messages`.
- The orchestrator should fail a batch that has no `_summary-*.md`.
- Settle the compliance-line rule: prompt rule 7 says "mandatory" and the card says "at most one".

## Coordinator review

(filled in by Claude in chat after the auto-QC run)

## coordinator_review

```
agreement: ✅ agree
top_issue: LighterLife referral copy runs on one skeleton ("Who at head office…" in 56 of 68 files, verified by grep) and batch 2 bought uniqueness with off-topic asks (help pages, billing, cost centre); card wording leaked into copy ("Short and neutral." edna-moneypenny, "No pitch here." louisa-flannery); "100+ clients use FitXpress today" turns the all-time 3DLOOK count into a current FitXpress claim (proof-points.md:108). Fix round sent back to the same message-sequencers: LighterLife referral and the Counterweight SA pool rewritten, Reset Health / MoreLife / mixed edited in place, batch 2 of each split account after batch 1. Compliance line: the card's "at most one" governs this campaign.
```
