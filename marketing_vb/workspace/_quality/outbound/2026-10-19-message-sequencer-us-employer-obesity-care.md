---
qc_date: 2026-10-19
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-16-us-employer-obesity-care/messages/ (sample: amy-mushlin-884504, alexandra-yurkovic-9162212, akallarakuzhi; plus _check.json and all 14 _summary-*.md; same-company siblings read in _batch-vida-health-1, _batch-omada-health-1, _batch-included-health-1/2/3)
track: outbound
artifact_type: messages
total_score: 13/20
status: marginal
coordinator_review: done
---

# QC Report: message-sequencer, 2026-10-19, us-employer-obesity-care

**Artifact:** `workspace/outbound/campaigns/2026-10-16-us-employer-obesity-care/messages/` (367 people, 734 messages)
**Total: 13/20, marginal**

**Verdict.** The M1s work. Each one is short, names the company, carries a product specific and a number, and ends on a real question. The best two are Alexandra's video-visit question and Ashok's pipeline question. The M2s are the weak half:
- Alexandra's is a list of the card's clinical disclaimers.
- Ashok's is a call agenda with no fact in it.
- Amy's is almost the same text as two other Vida operations people's M2s.

The same-company twin rule ("no two people at one company share … a product sentence, a Message 2 value line, a closer shape") fails in all three sampled companies. Recommendation: no regeneration. Run one sentence-level fix round on the twins listed under A.

**Scoring basis.**
- Scored against card-messages.md and the _profiles files. Limits, signature, bans, detector and completeness are taken from the gate as fact. One "so" benefit got past the gate and is listed under C.
- The split files have no `product:` field. That comes from the script template, so D is not capped (same ruling as QC 2026-10-11/12).
- notify.py was not run, because this QC run had no shell tool.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 2 | 4 |

## What was wrong (specific)

### A. Adherence: 3/5
- **Same-company twins** (card, "Several people at one company"):
  - **Vida, operations lane.** The M1 product sentence in amy-mushlin-884504 ("A Vida member could finish a guided two-photo scan on any phone … waist and 80+ body measurements") is the same sentence as in erin-mynaugh ("At Vida, a member could take a guided two-photo scan from any phone … 80+ body measurements, waist and hip"). It also matches josephmurad ("guided two-photo scan returns waist and 80+ body measurements … no hardware to manage").
  - **Vida, M2.** Amy's M2 line 2 ("The scan returns 80+ body measurements, under 45 seconds …, and one SDK serves every client.") is molliemcgill's M2 line 2 with only the tail swapped ("…, and the app guides each photo."). Amy's line 1 ("timestamped record at each check-in") repeats erin-mynaugh's M2 line 1 ("timestamped result for the check-in").
  - **Included Health, clinical lane.** alexandra-yurkovic-9162212 and jordana-blair-2431a12 share:
    - the hook shape ("An internist at heart …" / "An emergency medicine background …");
    - the product sentence ("Before a video visit/consult, a member could take a (guided) two-photo scan on their phone");
    - the central question (what clinicians want to see or know about the body when the visit starts);
    - the CTA ("I can show a sample result on a call" / "A quick call can show a sample result").
  - **Included Health, "sample result" closer.** The same noun closes the M2 for 5 Included Health clinicians: alexandra, jordana, tony-yuan-md, anishmehtamd, diana-malone-759468235.
  - **Omada, technical lane.** akallarakuzhi's M2 ("A call could cover the field list, IDs and timestamps") has the same value line as terry-miller-b1333a62's ("the useful call is about fields, IDs and timestamps per scan"). marty-lynch's is close ("how scan data is structured and timestamped"). Five Omada technical M2s run "A call could/can cover/set out/go through/map …" and then the link.
- **Card lines copied as copy** (card: "Card lines are targets"; prompt rule 11):
  - alexandra M2 restates the clinical-lane rule sentences ("Body composition values are estimates for the care team. Progress comparisons use two scans the care team picks. The scan never … decides anything about a member.") as the whole value line. tony-yuan-md and anishmehtamd do the same.
  - Amy M1 uses "with the phone as the only hardware", which is the card's wording. The card says "in your own words".
  - Amy's question ("How do check-ins run across employer and plan clients today?") is Vida topic 5 with the function names cut ("run check-ins across employer and plan clients").
- **M2 does not continue the M1 question** (Rules, "Message 1 asks, Message 2 calls"). Alexandra's M1 asks which body-size measure a clinician should see at the start of a video visit. Her M2 switches to scan comparison and body composition.
- **Omada account rule** ("Lead with waist, hip and other measurements and a 3D model next to the weigh-ins") and the M1 gate's "context from the account fact":
  - akallarakuzhi M1 has no Omada fact. "Before Omada" is about the person, and the scan sentence would read the same at any company.
  - marty-lynch, in the same batch, does it right: "Omada's weigh-ins are one input".
- **Soft notes left open in the final _check.json**:
  - "M2 opener repeated": Included Health ×4 open on «3DLOOK has worked with 100+ clients.» and ×4 on «112,100 scans in 2025 …».
  - "closing ask repeated": «worth a call?» ×2.
  - The prompt says to fix opener repeats inside one company. These are cross-batch, so the coordinator may own them.

### B. Factual accuracy: 4/5
- Every number is in the card: two photos, 80+, the speed phrase in full, and the fixed lines. The compliance line is verbatim in all three non-referral M2s.
- The article choice is correct in all three:
  - GLP-1 market for Vida operations;
  - no article for Included Health clinical;
  - the privacy FAQ for Omada technical.
- No client names, no Smart Scales, no eligibility or coverage wording. "Grand Rounds" (Alexandra's former employer, a banned term) and every other banned brand are left out.
- **amy-mushlin-884504 M2: the speed phrase appears where speed is not the point.** Rules: "only where speed is the point". It sits as one item in a three-part list between "80+ body measurements" and "one SDK serves every client", in an M2 about the check-in record and SDK reach.
- **For the coordinator, not scored:** Amy's hook names Anthem. Former employers are allowed, but the card also bans "a prospect's … plan clients", and Vida sells to health plans. Whether Anthem is a Vida plan client is not in the card.

### C. Brand & tone: 2/3
- **akallarakuzhi M2, "so" introducing a benefit** (card word traps). "…, so your pipeline team can judge the load before anyone builds." The gate missed it. The same shape appears in at least 5 other batch entries:
  - _batch-vida-health-2 l.38 ("so your team does not build it");
  - _batch-vida-health-1 l.713 ("so the first check-in has a visual to show");
  - _batch-mdlive l.474;
  - _batch-included-health-2 l.17;
  - _batch-mixed-1 l.169.
- **akallarakuzhi M1 tells him what he knows.** "…before Omada, so vendor data feeds are familiar ground." His bio says analytics and AI at OneTrust, not vendor feeds.
- **alexandra M1 opens on a third-person aphorism** built from her bio ("An internist at heart builds care models around what clinicians can act on."). It assigns her a philosophy her bio does not state.
- **Amy M2 line 2 is a three-part run-on** ("returns 80+ …, under 45 seconds …, and one SDK serves every client"), which reads as the banned triple.

### D. Format & structure: 2/3
- **Per-person files:** structure, paragraphs, signature and limits are correct (script output).
- **Clumsy phrasing that would ship as is:** alexandra M1 "returning waist among 80+ body measurements and BMI calculated" ("BMI calculated" is card shorthand, not English copy).
- **The summaries misreport the soft notes.**
  - Most say the near-duplicates are "mostly the compliance line". The final _check.json also has 37 "sentence opening repeated" notes on product sentences:
    - Included Health ×15 «a guided two photo scan…», ×8 «a scan from two phone…», ×6 «at included health a guided…»;
    - Crossover ×11 «two photos return 80+ body…», ×9 «it returns 80+ body measurements…».
  - The card bans exactly this ("no two people at one company share … a product sentence").
- **_summary-crossover-health-1 contradicts itself:** "clinical 13" and "clinical 12" are on the same line. The summary template still carries a stale "retention N" lane.

### E. Output quality: 2/4
- **What works:** all three M1s are under 350 characters. Each has a specific person hook, a product fact and a question the person can answer. Ashok's ("What does a new measurement type need to clear before it feeds your pipeline?") and Alexandra's are strong.
- **M2s carry little value:**
  - alexandra: disclaimers ("The scan makes no decisions about a member") for a CMO who has not asked about risk.
  - akallarakuzhi: no fact at all. He is engineering, and the card gives engineering people the 2-4 weeks figure in M2, but it is absent. The call is offered twice ("A call could cover …" + "Time that suits you?").
  - amy: repeats 80+ from her own M1.
- **Uniqueness across the company** (the rubric wants 60%+ unique per message) fails for the twins under A. Screenshot one Vida operations M2 next to another and it reads as a mail merge.
- **The hook template runs across companies:** "Your path from X to Y stood out." in amy-mushlin-884504, heather-washington-md and an eMed referral (_batch-emed-1 l.299).

## Top 3 issues (priority for improver)

1. **Same-company twins in the product sentence, M2 value line and closer.**
   - Pairs to fix: Vida operations (amy / erin-mynaugh / molliemcgill / josephmurad); Included Health clinical (alexandra / jordana-blair, plus 5 "sample result" closers); Omada technical (akallarakuzhi / terry-miller / marty-lynch "fields, IDs, timestamps" M2s).
   - The gate counts these only as soft "sentence opening repeated" notes, and the summaries call them compliance-line noise.
2. **Card rule sentences used as M2 value lines.**
   - The clinical-lane disclaimers became the whole M2 for alexandra, tony-yuan-md and anishmehtamd.
   - Amy uses the card's "phone as the only hardware" and a topic line almost word for word.
   - Same failure class as the AU 2026-10-12 QC (card notes became copy).
3. **M2 does not carry the person forward.**
   - Alexandra's M2 drops her M1 question.
   - Ashok's M2 is a call agenda with no fact, missing the 2-4 weeks figure engineering people get.
   - Plus one ungated "so" benefit (akallarakuzhi) and at least 5 more like it across the batches.

## Coordinator review

```
agreement: ✅ agree
top_issue: same-company twins, confirmed beyond the sample: a coordinator scan found 192 twin sentences at 148 of 367 people, plus 20+ ungated "so" result lines and ~40 card-rule restatements ("body composition values are estimates", "the phone as the only hardware", "the care team picks the scans").
```

Fix round 1 (2026-10-19): per-batch lists `messages/_fix1-<batch>-2026-10-19.md` (215 people, 314 items: twins pinned to the later holder, "so" lines, card-rule copy, every QC item above, gate notes on Included Health M2 openers and "Worth a call?"), sent back to the same 14 writers. Anthem dropped from Amy's hook as a precaution (possible plan client).
