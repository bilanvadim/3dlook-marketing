---
qc_date: 2026-10-21
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-19-latam-everlab-similar/messages/ (sample: agustin-de-la-llave, marina-aranha-andrade-302666213, pascal-latorre-vidales; full read of _batch-fleury-lifecare.md and _batch-mixed-1.md after fix round 1)
track: outbound
artifact_type: messages
total_score: 13/20
status: marginal
coordinator_review:
  agreement: "✅ agree"
  top_issue: "One skeleton per company (Fleury 20, Timeless/Humanolab/Care Club 3 each): the five-word gate and my scan only see openings, not shared arguments; round 2 runs on a per-person grid built first."
---

# QC Report: message-sequencer, 2026-10-21, latam-everlab-similar

**Artifact:** `workspace/outbound/campaigns/2026-10-19-latam-everlab-similar/messages/` (48 people, 96 messages, 2 batches)
**Total: 13/20, marginal**

**Verdict.** Fix round 1 worked as asked:
- every Message 1 now stands on an account fact;
- no account's "Never:" list is broken outright;
- all numbers, the speed phrase and the repeatability sentence use card wording;
- pool B follows Vadim's decision (3), point 3.

Three things block the batch as it stands:
- **Fleury reads as a mail merge across the company**, and so do three smaller accounts. The gate compares the first five words. These repeats are semantic, so it lets them through.
- **Card rules and lane notes went into the copy.**
- **Three copy bugs and several hollow M2s.**

Recommendation: no regeneration. Run a round 2 on patterns, not named sentences: Fleury first, then the rule-copy class campaign-wide.

**Scoring basis.**
- Scored against `card-messages.md` (re-cut, with Account facts) and the two `_profiles-*.md` files. Limits, signature, bans, detector and completeness are taken from the gate as fact (`_check.json`: hard 0).
- D is not capped for the missing `product:` field. That comes from the script template (standing ruling since 2026-09-29).
- No deduction for the missing compliance line: the campaign rule says "none in any sequence". It overrides the rubric's healthcare override.
- notify.py was not run, because this QC run had no shell tool.

## Pool B check (Vadim's decisions 2026-10-21 (3), point 3)

| Requirement | jeane-tsutsui | edgardarnas | alessandroferreira |
|---|---|---|---|
| Lane `product` | yes | yes | yes |
| M1 goes straight to the specifics (what the scan returns + why it matters for Lifecare members between assessments) | partly: l.7 gives the returns and a "when" ("After it…"), not a why | yes, l.47 ("between assessments and without a clinic trip") | yes, l.87 (brand lived after the first visit) |
| M1 ends with interest + "if not, whom" | yes, l.9 | yes, l.49 | yes, l.89 |
| Area tied to the person's own remit, worded fresh | generic: "member follow-up" for a group CEO | good: "Lifecare offer design" (strategy, commercial excellence) | acceptable: "member experience". His remit is commercial and marketing, so "brand" or "go-to-market" would fit tighter |
| M2 = call + calendar link | yes | yes | yes |

**Pool B result: pass, with three defects.**
- All three M2s ask the "who" question a second time: Jeane l.17, Edgard l.57, Alessandro l.97. The card says "Never the same ask twice".
- Edgard M2 l.57 "Whoever owns the member offer can join **in my place**" means the owner replaces Kateryna on the call. Compare Cinthia l.431 "in your place".
- Jeane M2 l.15 repeats "80+ body measurements" from her M1.
- Alessandro's M1 target ("member experience") and M2 target ("member app") differ.

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
- **Card rules written as copy** (prompt item 11; the 2026-10-07 failure class):
  - The 3D-model rule, paraphrased in 5 letters:
    - Germán l.9 "shown only if AIONIS chooses";
    - Lucas l.101;
    - Pedro Heckmann l.170;
    - Alfredo l.329;
    - Pedro Junqueira l.444.
  - "Care team chooses which scans to compare" in 6 letters: Marina l.408, Santiago l.226, Cinthia l.421, Aline AM l.75, Carla l.315, Rendrik l.215. Similar: Fernanda l.195, Fabio l.395 ("team chooses/decides what members see").
  - The operations lane note ("nothing to ship, stock or install; the same guided sequence on any phone") lifted almost word for word: Agustin M2 l.40, Renan M2 l.86, Gustavo M2 l.235, Marcos M1 l.247.
- **Account facts copied almost word for word.** The card says "fresh words… never copied word for word":
  - Oleg l.534 "book video consults with doctors who read their history first";
  - Santiago l.214 "The ERA app carries the protocol between consultations";
  - Franco l.557 "a yearly study, a protocol and a doctor-led review".
- **Fix-round rule R4 (no label lead-ins) still broken:**
  - "On repeatability:" Marina l.406, Yosafat l.360;
  - "One data point on volume:" Aline AM l.75;
  - "For the operations view:" Marcos l.255.
- **The card's same-company rule is broken in meaning.** It says no two people at one company share an opener, a central question, a closing ask or a product sentence. Examples are under E.
- **Both summaries are stale after the fix round, not just mixed-1.**
  - _summary-fleury-lifecare still says "No companies.md fact about Lifecare was in the card".
  - Its sample note says Marco carries the repeatability sentence. His M2 now has 100+ (l.135).

### B. Factual accuracy: 4/5
- All numbers are card numbers in card wording:
  - 80+;
  - the speed phrase, with the scan as the subject;
  - 100+ as "3DLOOK has worked with 100+ clients";
  - 112,100 in its own sentence;
  - 34,000 "at one platform";
  - repeatability verbatim (Daniella, Lucas, Santiago, Marina, Yosafat).
- No client or competitor is named, and no country is named for Humanolab. "Pilot" (Rendrik l.207/217, Daniella l.369) sits near trial wording; it is not counted here.
- **Rodrigo M2 l.275:** "The app uploads the photos, deletes them after processing…". This credits the Lifecare app with deletion that 3DLOOK processing does.
- **Marco M1 l.127:** "Between Fleury Lifecare cycles, a remote consult starts…". The Lifecare account fact has no remote consults.
- **Pascal M1 l.304:** "What they do afterwards is mostly self-run." The fact does not say this, and it implies a gap. The card says "never imply what the company lacks". It also ignores the six-month re-check that the fact does list.
- **Oleg (Previva), l.534/536/544:** both messages route the scan to "the doctor" ("join what the doctor sees", "for the doctor to review", "give the doctor… before a video consult"). Previva's "Never:" list bans clinician-led framing.
- **Germán M2 l.17:** "could sit alongside each Longevity Map re-evaluation" puts the scan next to the on-site re-evaluation. The card positions it between assessments.
- **Edgard M2 l.55:** "The platform handled 112,100 scans…". "The platform" has no referent and reads close to the one-platform framing.

### C. Brand & tone: 2/3
- **Presumed-reaction M2 openers** (hard-bans card, judgment row). Seven M2s open by telling the reader what their role thinks:
  - Leticia l.155 "The build question for a product manager is…";
  - Aline Vanni l.175 "Product teams like a feature…";
  - Fernanda l.195 "Platform owners ask where…";
  - Carla l.315 "Developers like a record with a clear shape";
  - Marco l.135 "Telemedicine teams ask first…";
  - Daniella l.375 "Stability of a home capture matters to R&D";
  - Ignacio l.590 "Build or add is a fair question for a CPO".
- **Triple lists:**
  - Fabio M2 l.395 "clear prompts, front and side photo, one short flow";
  - Pascal l.304 "a consultation, a plan and a year in the app".
- **Unclear English for second-language readers** (the card asks for plain words):
  - Edgar Gil l.27 "could give those cycles a step";
  - Aline Vanni l.167 "Fleury Lifecare carries the follow-up cycles";
  - Oleg l.536 "body composition estimates, as estimates for the doctor".

### D. Format & structure: 2/3
- Batch format is correct and gate exit is 0.
- **Summary lane counts are wrong:**
  - Fleury says "product 12", which sums to 21 people. The batch has product 11.
  - mixed-1 says product 15 and operations 5. The batch has 16 and 4.
- **Stale per-person metadata:** galileu's proof line (l.369) says "100+ clients", but his M2 (l.383) uses 112,100.
- **Script note for the coordinator, not scored:**
  - the combined `_check.json` shows `soft: []`;
  - `_check-mixed-1.json` still lists two campaign-wide M2-opener repeats: "3DLOOK has worked with 100+ clients." ×5 and "In 2025, 112,100 scans ran…" ×4. Both are still in the batch.

### E. Output quality: 2/4
- **Fleury (20 people, one company), checked across the whole company:**
  - 13 of 20 M1s open with "Fleury Lifecare [verb]…".
  - About 10 hooks are the same fact, "follow-up cycles in its own app": Edgard, Joao, Leticia, Aline Vanni, Fernanda, Gustavo, Rodrigo, Carla, Daniella, Fabio.
  - **Joao ↔ Rodrigo** (IT exec and his likely head of engineering) share:
    - the M1 API sentence (l.107 / l.267);
    - the M2 deletion content (l.115 / l.275);
    - the easy out "a different engineer owns the app" (l.117 / l.277). Calling an Executive IT Director "engineer" also misreads his seniority.
  - **Edgar Gil ↔ Aline AM** (same unit, Novos Elos) ask the same question: l.29 "Where in your unit … step between visits?" / l.69 "Where in Novos Elos does a home step between visits come up?".
  - **The operations quartet** shares one argument and one question:
    - argument: "nothing shipped or installed" (Gustavo l.227), "nothing to install or stock" (Marcos l.247), "nothing for your teams to install" (João Paulo l.295);
    - question: "member step / operations" (l.229, l.249, l.289).
  - **Leticia l.147 ↔ Fabio l.387:** "Fleury Lifecare members already have their own app…" / "Fleury Lifecare members already live in an app…".
  - **Jeane l.15 ↔ Marcos l.255:** the same M2 product sentence, "returns 80+ body measurements, under 45 seconds…".
  - **All 20 M2 easy outs use one shape,** "If [X] owns/leads [Y], I will [switch/talk/reach out]". Joao and Leticia both end "switch to them".
- **Same-company repeats in mixed-1:**
  - Timeless: all three open on the app messaging with the clinical team (Franco l.557, Ignacio l.580, Ana l.601).
  - Humanolab: all three open on plan + year of app access (Cristina l.260, Andres l.283, Pascal l.304).
  - Care Club operations: Renan l.76, Lucas l.99 and Murilo l.124 all argue "no equipment / nothing of the unit". Lucas l.103 and Murilo l.126 ask the same staff-burden question.
  - Med-Rio: Galileu ↔ Arlei share the web-link product sentence (l.375 / l.467) and the post-return-consult hook.
  - AIONIS: both founders ask about patients between re-evaluations (l.11 / l.34).
- **Hollow or broken M2s:**
  - Agustin l.40: the operations lane note only, nothing for AIONIS.
  - Junqueira l.452: a disclaimer only.
  - Pedro Pinto l.335: one abstract sentence.
  - Aline Vanni l.175.
  - Marco l.135 answers "how a home capture holds up" with a client count.
- **Sample of three:**
  - **Marina:** the best of the three. The lifestyle-medicine hook comes from her headline, with the account fact and the verbatim repeatability. It loses on "On repeatability:", and "chooses which scans to compare" twins Cinthia's M1 at the same company.
  - **Agustin:** a solid M1 with the correct speed phrase. The logic slips: "patients already give the centre their time. A home step should ask nothing more of the staff". His M2 is the operations lane note given to a product-lane person.
  - **Pascal:** the question fits a COO. Weak points:
    - "mostly self-run" (see B);
    - his opener's content is the same as Andres's and Cristina's;
    - "It" in M2 l.314 is ambiguous;
    - the easy out "Should a colleague run member operations" misfits the co-founder who runs operations.

## Top 3 issues (priority for improver)

1. **Same-company sameness that the five-word gate cannot see. Fleury is the worst case.**
   - Fleury: about 10 hooks on "follow-up cycles in its own app"; the Joao↔Rodrigo and Edgar Gil↔Aline AM twins; one shared argument and question across the operations quartet; 20 easy outs in one shape.
   - Mixed-1: the Timeless ×3, Humanolab ×3, Care Club ×3, Galileu↔Arlei and AIONIS repeats.

   Round 2 should give each Fleury person a role-specific argument and vary the easy-out shape. It should also check semantic twins per company, not first words.
2. **Card rules, lane notes and account facts written as copy:**
   - the 3D-model rule ×5;
   - "chooses which scans to compare" ×6 (Marina↔Cinthia at Med-Rio);
   - the operations lane note ×4;
   - near-verbatim facts (Oleg, Santiago, Franco);
   - R4 label lead-ins that survived round 1 (×4).
3. **Copy bugs and hollow M2s:**
   - Edgard "join in my place";
   - Aline Vanni "Fleury Lifecare carries the follow-up cycles";
   - Rodrigo "The app … deletes them";
   - Marco's non-sequitur;
   - hollow M2s at Agustin, Junqueira, Pedro Pinto and Aline Vanni;
   - 7 presumed-reaction M2 openers;
   - pool B M2s asking "who" a second time;
   - Previva clinician-led framing.

## Coordinator review

agreement: ✅ agree
top_issue: Same argument, question and easy-out shape across people at one company; my round-1 scan checked only five-word openings, so it passed what QC caught. Round 2: per-company grid first (M1 lead, question, M2 value, easy-out target and shape, one wording each), card rules and lane notes out of copy, pool B M2 without a second "who".
