---
qc_date: 2026-10-23
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-22-us-mens-health-weight/messages/
track: outbound
artifact_type: messages
total_score: 14/20
status: marginal
coordinator_review: pending
---

# QC Report — message-sequencer — 2026-10-23

**Artifact:** `workspace/outbound/campaigns/2026-10-22-us-mens-health-weight/messages/`. I read all three batch files: gameday-men-s-health (31), hone-health (25) and mixed-1 (Maximus 8, DudeMeds 2, LaSara 1). That is 67 people and 134 messages, read after fix round 1.
**Total: 14/20 — marginal.** One more targeted fix round. Nothing needs regenerating.

Scored against `card-messages.md` and the three `_profiles-*.md` files. I took limits, signature, bans, detector and completeness as fact from the gate. The "no company line ×31" soft note is a known false positive: every Gameday M1 names "Gameday". The template hooks are allowed. Only reuse inside one company counts.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence — 3/5
The card's same-company rule says no two people share an opener, central question, M2 value line, easy-out sentence, closer shape or product sentence. Questions pass: every person has their own. The other five dimensions do not.

- **Openers (first three words), same company.** The fix round allowed up to two uses of each hook. The card rule allows none.
  - Gameday, 7 pairs:
    - allen-brooke-834a1119 and tristyn-coffeen-5642a325b: "Noticed your background"
    - shea-tiana and richard-force-1b4589169: "Came across your work"
    - justinpenny and anna-coble-bsn-rn-9b14a773: "Made me think: you"
    - gina-dressler-2730271b0 and danielleprosinski: "Wanted to reach out"
    - john-hudnall-2b26901a and chadcarman-677a12285: "Quick idea for you"
    - lisa-barr-m-d-90847623 and nicole-marlborough: "Had to say hi"
    - ron-noonan-50a102283 and carlos-elizondo-13898816a: "Thought I'd share this, given your", six identical words
  - Hone, 2 pairs:
    - anthonymalocujr and andynyquist: "This stood out:"
    - ayushsoni01 and carolkhung: "Got me thinking about"
  - The writer did not need to reuse hooks: haleem, timothy, jean, jay, seth and nicholas already open in their own words.
- **Product sentence twins** (details per batch below). About 21 of 31 Gameday M1s fall into 8 clusters of the same "[FitXpress] returns 80+ body measurements from two photos" sentence. Hone has 5 clusters. The card asks for rotation. Instead, "80+ body measurements" is added to every Gameday M1, and the other specifics sit on top of it.
- **Card text as copy after the fix round** (rule 2 of the fix round, plus card rule 11):
  - melanie-doukas-74311661 M2 is three rule sentences and nothing else: "picks which captures to compare", "every decision stays with the clinician" and "Composition values are estimates". The fix round named the last two explicitly.
  - alaric-murg M2: "Body composition values arrive as estimates", which is the replacement rule 2 forbids. Body composition never appears in his M1.
  - saad-alam-a146b311 M2: "The clinician or coach picks which captures to compare", the use-case line word for word.
  - salpilato M2: "the later ones it picks to compare". His question is not about comparing, so rule 2 does not allow it. jonathan-hancock-71216a26 carries the same clause, so both DudeMeds people have it.
  - michael-tabor-5957195 M2: the network lane target almost word for word ("One capture step that HQ adds once and each Gameday clinic switches on … with the phone as the only device").
  - hagel and jasonmclark M2: "the host app owns the entry point", from the Gameday deployment-path note, which is marked "never claimed in copy".
  - The product-lane note "no device to ship" ×4 at Hone: saad-alam-a146b311 M1, stuartblitz M1, ashley-camerini-3363717b M2, nicholas-del-prince-244052ab M2.
- **Hook from the title or company when the profile had specifics** (prompt item 1): sfinnern, nicholas-boerger, stephenciniello, markrpoole, nick-m-632b1177, tylerrdyck, stuartblitz, daniel-ward-5976a5204. The `hook:` metadata for stuartblitz (Seventh Sense) and daniel-ward-5976a5204 (relationship manager) is not in the copy.
- **M2 with no value line that continues the question** (card: "a value line continuing that question"). Non-technical people only, because for the technical lane, specs are the value:
  - spec or proof only: seth-franz, alextreco (repeats M1's "inside your own screens"), andynyquist (repeats M1), yash-kothari-amazon (referral), emily-smith-01435910b
  - disclaimers or proof only: melanie-doukas-74311661, saad-alam-a146b311
- **Easy out given to co-founders:** seth-franz and alba-mertira (Hone co-founders, P1).
- **Questions copied from the card topic line** (low priority). Most of the 67 questions are the card's topic turned into a question, many word for word. They are distinct per person, so this does not hurt sameness. Fix only the stiff ones: judson-threlkeld-4106439, carolkhung, melanie-doukas-74311661, seth-franz.

### B. Factual accuracy — 4/5
- Every number uses the card's wording:
  - 80+, the speed phrase and the exact §1.2 repeatability sentence: gina-dressler, elizabethsimion, andynyquist, nick-m-632b1177.
  - The 34,000 / 112,100 / 100+ lines, all within the "one in five" limit. Hone is exactly at it: 4 / 5 / 5 / speed ×5.
  - 2-4 weeks appears only in technical-integration M2s.
- No client is named, no prices, no GLP-1 as a drug. The compliance line is verbatim in every non-referral M2. Referral M2s carry no compliance line. The technical lane links the privacy FAQ.
- anna-coble-bsn-rn-9b14a773 M2: "A record that travels with the member keeps his history intact wherever he goes." This claims FitXpress tracks a person over time and across clinics. The card's "what the scan does" rule forbids that. **Blocking one-line fix.**
- melanie-doukas-74311661 M1: "80+ body measurements … as estimates". Body measurements are not estimates. Body composition is.
- halmdmba M2: "I can show the clinician view". The card confirms no clinician-facing view: API/SDK plus an optional Admin Panel.
- jasonmclark M2: "Plan on 2-4 weeks" presents the figure as Hone's timeline. The card says "do not present it as this company's timeline".
- daniel-ward-5976a5204 M2: "112,100 scans in 2025 across all 3DLOOK customers, each capture timestamped." The proof line is not its own plain sentence.
- Sourcing: not applicable (outbound).

### C. Brand & tone — 2/3
The hard-ban layer is clean (gate). The judgment rows are not. This sits at the floor of 2, on the same calibration as the 10-21 re-score (2 triples plus 16 presumptive lines scored 2).

- **Presumed facts about the reader's company** (fix rule 6 class), 15 people:
  - Hone:
    - stuartblitz M2: "Operations at scale needs a repeatable step"
    - daniel-ward-5976a5204 M1 and M2: "A client review needs dated records"
    - rebeccakayhiggins M1 and M2: "A small group is the natural place to test it"
    - ashley-camerini-3363717b M1 and M2: "Bets beside the core offer need quick proof"
    - hagel M1: "is a design problem first"
    - nicholas-del-prince-244052ab M1: "you know which … features carry an ad"
    - ayushsoni01 M1: "a between-retest prompt needs a reason to open the portal"
    - tobin-abraham M1: "fills a slot there", which also implies a gap in Hone's offer
  - mixed:
    - nick-m-632b1177 M1: "outcome data has to be clean enough"
    - tylerrdyck M1: "earns its keep when members stay"
    - johnsnedegar M1: "has to travel with them"
    - salpilato M1: "has no front desk … has to be a step he finishes alone"
    - sfinnern M1: "lives on patients returning"
    - jonathan-hancock-71216a26 M1: "carry the relationship"
    - stephenciniello M1: "are where growth teams test changes"
- **Triples** (the M1 template bans them):
  - our own: richard-force-1b4589169 ("two photos, 80+ body measurements and a 3D model") and saad-alam-a146b311 ("guided capture on any phone, white-label inside Hone's own app, with nothing to ship")
  - quoted from bios, lower severity: michael-tabor-5957195, shea-tiana, brandonmaughan, tristyn-coffeen-5642a325b
- **Hook verb with no follow-through:**
  - ron-noonan-50a102283 and carlos-elizondo-13898816a: "Thought I'd share this", but nothing is shared
  - john-marhefka-8527569: "Couldn't help but ask:" is followed by a statement
  - alexander-peterson-896327b8: "Quick reaction:" is followed by a recital of his title
- **Third-person address in a direct message:** gina-dressler-2730271b0 ("to a clinic director at Gameday who is also an NP"), julie-caputo-531a522b7 ("for a chief executive at Gameday"), sommer-rushing-3a4782315.
- **Wording:**
  - jason-ange-32138a6: "organised" (the card says US context, so "organized")
  - alaric-murg M2: "look at at a follow-up"
  - alexander-peterson-896327b8 M2: "If HQ is the right door, I will knock there." (cute)

### D. Format & structure — 2/3
- `_summary-gameday-men-s-health.md` says "clinic-operator 14". The real count is 13 (7+8+13+1+2 = 31), so the summary's lanes add up to 32.
- The Gameday batch metadata is stale after the fix round, and per-person files inherit it:
  - gina-dressler-2730271b0, jean-leisen-bondoc-97699b232 and megann-grant-205521299 list "speed phrase" under `proof:`. None of them carries it.
- `_summary-mixed-1.md` still flags nick-m-632b1177 for missing the §1.2 sentence. The copy now has the exact sentence.
- The Gameday M2 layout differs from the other two batches:
  - In 21 M2s the calendar link sits mid-paragraph, with the easy out on the same line after the URL. The prompt says the CTA goes on its own line. People: jason-ange, justinpenny, ampy-tyler, gina-dressler, jean-leisen-bondoc, megann-grant, ron-noonan, sommer-rushing, shelley-gay, drquimbo, bonesflottmann, judson-threlkeld, alexander-peterson, lisa-barr, carlos-elizondo, richard-force, anna-coble, danielleprosinski, julie-caputo, chadcarman, nicole-marlborough.
  - In all 29 non-referral Gameday M2s, the 147-character compliance line follows the link and buries the call. Hone and mixed put it before the CTA.
- The "no `product:` frontmatter, so D ≤ 1" hard rule is **not applied**. The per-person files come from `split-messages` by design; this is a system gap, as on 10-21.

### E. Output quality — 3/4
- **Strong:**
  - The Gameday local/HQ split is handled well. Clinic people are asked about their own clinic and pointed to HQ. HQ people get network questions.
  - Every question is distinct.
  - The copy is short and plain.
  - Good pairs: john-hudnall-2b26901a, justinpenny, alexander-peterson-896327b8 (the question), timothy-rempher-81347433, stephenciniello, ampy-tyler-37a1b916, jonathan-hancock-71216a26, ken-vetrano-23ba7258.
- **Mail-merge risk at the two big companies** is in the product sentence (Gameday) and the M2 skeleton (Hone). A forwarded screenshot shows it.
- **Referral M2s that point back to M1 after 5 days:**
  - nicole-marlborough: "Wording like that could carry into…"
  - danielleprosinski: "that member step"
- tylerrdyck M2: "finance gets a timestamped record of each capture to read". A VP Finance does not read capture records. The value for him is retention.
- daniel-ward-5976a5204 M1: the hook ("where you hear what partner programs want to see about member progress") restates his question.
- hagel M1: the body and the question repeat "inside Hone's member screens".
- Rubric 60%-unique check: the required compliance line plus a fixed proof line are about 200 of roughly 350 characters in short Hone M2s, so 60% is out of reach by design. I judged uniqueness on the free text (see system notes).

---

## Fix list per batch (person_ids)

### gameday-men-s-health (31)
1. **Opener pairs** (change one of each pair): allen-brooke-834a1119/tristyn-coffeen-5642a325b · shea-tiana/richard-force-1b4589169 · justinpenny/anna-coble-bsn-rn-9b14a773 · gina-dressler-2730271b0/danielleprosinski · john-hudnall-2b26901a/chadcarman-677a12285 · lisa-barr-m-d-90847623/nicole-marlborough · ron-noonan-50a102283/carlos-elizondo-13898816a.
2. **M1 product-sentence clusters** (keep one per cluster, rotate the rest to a specific the neighbours lack):
   - "FitXpress returns 80+ body measurements from two photos": ron-noonan-50a102283, lisa-barr-m-d-90847623, danielleprosinski, brandonmaughan ("It returns 80+ body measurements from two photos.")
   - "timestamped record … 80+ body measurements from two photos": shea-tiana, jason-ange-32138a6, carlos-elizondo-13898816a, chadcarman-677a12285
   - "FitXpress is a guided (two-photo) capture … that returns 80+ body measurements": michael-tabor-5957195, judson-threlkeld-4106439, gina-dressler-2730271b0
   - "FitXpress asks a member for two photos … and returns 80+ body measurements": sommer-rushing-3a4782315, julie-caputo-531a522b7
   - "FitXpress returns waist and other circumferences from two photos": halmdmba, drquimbo
   - "FitXpress turns two photos into a 3D model": ampy-tyler-37a1b916, bonesflottmann
   - "two photos …, 80+ body measurements back": stephen-mercurio-20307b14a, nicole-marlborough
   - The speed sentence twin, allen-brooke-834a1119/timothy-rempher-81347433, was sanctioned by fix round 1. It is left here for the record.
3. **Easy-out shape:** 15 of 25 are "If / Should [HQ condition], [ask]": jason-ange, justinpenny, ampy-tyler, jean-leisen-bondoc, ron-noonan, shelley-gay, bonesflottmann, alexander-peterson, carlos-elizondo, julie-caputo, tristyn-coffeen, shea-tiana, danielleprosinski, mark-larey, drquimbo.
   - Verb and structure twins inside that group:
     - jean-leisen-bondoc/ron-noonan: "I would/will gladly talk/speak"
     - shea-tiana/carlos-elizondo: "introduction there … welcome"
     - justinpenny/julie-caputo: "a contact there is just as good / is welcome"
   - "[X] at HQ may hold …; …": brandonmaughan, richard-force, megann-grant.
4. **M2 value-line shape:**
   - "A capture [time phrase] would/could …": mark-larey-b1951366, megann-grant-205521299, drquimbo, alexander-peterson-896327b8, julie-caputo-531a522b7
   - "A record that …": anna-coble-bsn-rn-9b14a773, chadcarman-677a12285
5. **Single lines:**
   - anna-coble-bsn-rn-9b14a773 M2: the tracking claim (B, blocking)
   - halmdmba M2: "clinician view"
   - michael-tabor-5957195 M2: lane text
   - jason-ange-32138a6: "organised"
   - gina-dressler, julie-caputo, sommer-rushing: third-person openers
   - ron-noonan, carlos-elizondo, alexander-peterson: hook verbs
   - nicole-marlborough, danielleprosinski M2: anaphora back to M1
   - richard-force M1: triple
6. **Layout:** put the CTA on its own line and the compliance line before it, in the 21 M2s listed under D. Fix the summary count (13) and the stale `proof:` lines (gina-dressler, jean-leisen-bondoc, megann-grant).

### hone-health (25)
1. **Opener pairs:** anthonymalocujr/andynyquist · ayushsoni01/carolkhung.
2. **M1 product-sentence clusters:**
   - "Two photos (go) in, 80+ body measurements (come) out/back": matt-buckleman-3322771, stuartblitz, jasonmclark, john-marhefka-8527569, jerreck
   - "FitXpress is a REST API with (web and mobile) SDKs": matt-buckleman-3322771, jasonmclark, jerreck
   - "FitXpress is a guided capture on any phone": saad-alam-a146b311, ken-vetrano-23ba7258
   - "It/FitXpress returns 80+ body measurements from two photos.": saad-alam-a146b311, ashley-camerini-3363717b
   - "FitXpress adds a guided two-photo capture that returns": melanie-doukas-74311661, neika-colbourne
   - "no device/hardware/nothing to ship": saad-alam-a146b311, stuartblitz, ashley-camerini-3363717b, nicholas-del-prince-244052ab
3. **M2 value-line shape:**
   - "[Abstract noun] needs X.": stuartblitz, daniel-ward-5976a5204, rebeccakayhiggins, ashley-camerini-3363717b
   - "Each capture/scan … timestamped": seth-franz, alba-mertira, tobin-abraham, carolkhung, plus daniel-ward-5976a5204 and anthonymalocujr
   - "host app owns the entry point": hagel, jasonmclark
4. **Easy-out shape:**
   - "[owner question]? I can / am glad to / would gladly talk with them": melanie-doukas-74311661, seth-franz, jasonmclark, ken-vetrano-23ba7258, andynyquist, neika-colbourne, rebeccakayhiggins
   - "colleague … intro": anthonymalocujr/carolkhung ("an intro works / would work"), emily-smith-01435910b
   - Co-founders should get no easy out: seth-franz, alba-mertira
5. **M2s that need a value line continuing the question:** melanie-doukas-74311661 (replace all three rule sentences), saad-alam-a146b311 (drop the use-case line), seth-franz, alextreco, andynyquist, yash-kothari-amazon, emily-smith-01435910b.
6. **Single lines:**
   - melanie-doukas-74311661 M1: measurements "as estimates"
   - daniel-ward-5976a5204: 112,100 in its own sentence; the hook restates the question
   - jasonmclark: "Plan on 2-4 weeks"
   - john-marhefka-8527569: hook verb
   - hagel: M1 repetition
   - the presumptive lines under C
   - stiff card-topic questions: melanie-doukas-74311661, seth-franz, carolkhung

### mixed-1 (11)
1. **Maximus tech trio:**
   - markrpoole and daniel-cw-hsu share the M1 argument (a web SDK step in the portal or web app)
   - markrpoole, daniel-cw-hsu and nick-m-632b1177 share the M2 value line (2-4 weeks plus structured, timestamped measurements or "the SDK runs the capture")
   - Give each a value line that continues his own question: effort, the portal step, research data
2. **Maximus easy outs:**
   - "sits with someone else / another team / elsewhere": alaric-murg, daniel-cw-hsu, tylerrdyck
   - "Happy to talk to them / whoever": stephenciniello, daniel-cw-hsu
3. **Maximus opener shape:** "Quick thought/note for Maximus [function]:" in sfinnern and markrpoole.
4. **Rule-sentence residue:**
   - alaric-murg M2: "values arrive as estimates"
   - salpilato M2: the "picks to compare" clause; his question is not about comparing, and jonathan-hancock-71216a26 has the same clause
5. **Hooks from title/company though the profile had specifics:** sfinnern, nicholas-boerger, stephenciniello, markrpoole, nick-m-632b1177, tylerrdyck.
6. **Single lines:**
   - tylerrdyck M2: the finance logic
   - alaric-murg: "at at"
   - presumptive lines: salpilato, jonathan-hancock-71216a26, johnsnedegar, sfinnern, stephenciniello, nick-m-632b1177, tylerrdyck
   - stale nick-m flag in `_summary-mixed-1.md`

## Top 3 issues (priority for improver)

1. **Same-company sameness the gate does not see.**
   - 9 opener pairs (7 Gameday, 2 Hone).
   - Product-sentence clusters covering about 21 of 31 Gameday M1s and 12 Hone M1s. The card says rotate, but "80+ body measurements" is in every Gameday M1.
   - Shared M2 shapes: Gameday "If HQ …" easy out ×15; Hone "[noun] needs X" ×4, "Each capture … timestamped" ×6 and "? … talk with them" ×7; the Maximus tech trio.
2. **Rule sentences and lane text still used as copy after fix round 1.** The worst case is melanie-doukas-74311661: her M2 is three rule sentences. Also alaric-murg ("values arrive as estimates", forbidden by rule 2), saad-alam-a146b311, salpilato, michael-tabor-5957195, hagel and jasonmclark, plus "no device to ship" ×4 at Hone. Seven non-technical M2s have no value line that continues the question.
3. **One claim fix (blocking) and a tone pass.**
   - anna-coble-bsn-rn-9b14a773: "keeps his history intact wherever he goes", which claims person tracking.
   - The tone pass: 15 presumptive lines, mostly Hone and mixed; 2 of our own triples; 3 third-person openers; the Gameday M2 layout with the CTA buried before the compliance line.

## System notes (not scored against the agent)
- The `split-messages` gate checks sentence openings and near-duplicates. Nearly all of its 666 soft notes are the required compliance line. It has no check for the first three words of M1 openers or for M2 easy-out and value-line shapes within one company. All 9 opener pairs passed silently. A first-three-words check per company would catch them.
- The fix-round wording "a hook may appear at most twice" at Gameday conflicts with the card's "no two share an opener (first three words)". The card's M1 template also says "the product intro stays stable", while the campaign rule says rotate the product sentence. The campaign rule should win, and the card should say so.
- The rubric's 60%-unique check cannot hold for short M2s that carry the required 147-character compliance line plus a fixed proof line.
- No `product:` frontmatter in per-person files: the script's template, not the agent (same as 10-21).

## Coordinator review

coordinator_review:
  agreement: agree (14/20 fair; my pre-QC scan caught the label lead-ins, card-rule copy, repeatability and Gameday hook reuse, but my fix-round wording "a hook at most twice" contradicted the card's no-shared-opener rule, and I missed the product-sentence clusters, the M2 value-line shapes and anna-coble's tracking claim)
  top_issue: same-company sameness in M1 product sentences and M2 value-line/easy-out shapes, plus card rules still used as copy (melanie-doukas, alaric-murg); anna-coble tracking claim is blocking
  action: fix round 2 to the same three writer agents with per-batch fix files built from this report (_fix-r2-*.md), then mechanical verification + re-read, no second QC unless the scan shows new patterns
