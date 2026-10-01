---
qc_date: 2026-10-01
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-01-us-options-medical-weight-loss/messages/ (jeremyncastle, jessicatarnawa, jdelcecato, joshua-hicks-10ab2014a, nicholasfoy34; _batch-all.md; _check.json; _summary-all.md)
track: outbound
artifact_type: messages
total_score: 15/20
status: good
coordinator_review: done
---

# QC Report: message-sequencer, 2026-10-01, us-options-medical-weight-loss

**Artifact:** `workspace/outbound/campaigns/2026-10-01-us-options-medical-weight-loss/messages/` (5 people, 1 account, 10 messages)
**Total: 15/20, good.** Apply the line fixes below in `_batch-all.md` and re-run `split-messages` before import. Regeneration is not needed. The messages checkpoint is waived, so nobody else will catch these before closely.io.

I scored against `card-messages.md` and `_profiles-all.md` only. The gate results (limits, signature, bans, detector, completeness) are taken as fact. I checked one fact outside the card: Foy's "GLP-1 programs at your clinics" is true per the raw export ("two clinic locations, specializing in GLP-1 programs").

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 4 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence: 4/5
- The per-person notes were all followed. NCO is not expanded. Jory gets no invented function title. Castle's former employers are named and his join date is not. Foy's revenue figures and job-search line are not used. Hicks is written to his title only.
- The lane rules were followed: the compliance line is verbatim in all three non-referral M2s and absent from both referral M2s. The GLP-1 hub is the only 3DLOOK link, and the referral lane has no article.
- **Prompt rule 3 broken: same facts to two people at one company.** Jeremy M1 and Jessica M1 carry the same fact set (two photos, 80+ body measurements, 3D model, body composition estimates, under 45 seconds) in nearly the same sentence. In Jeremy's it is "We built a two-photo scan patients take at home inside your patient app: 80+…". In Jessica's it is "We built a guided two-photo scan patients take at home inside your patient app. It returns 80+…".
- **The profiles file asks for "a different central argument" for each person. The two Clinic Directors get the same one.** Both get the card's referral question almost word for word ("who … looks after the [Options] Health Coach app and the telehealth program?"). They also share one context line verbatim: "a guided two-photo body scan patients take at home inside the app".

### B. Factual accuracy: 4/5
- Every number comes from proof-points. "under 45 seconds from the photos to structured results" is exact. The 34,000 line has no name and no geography. No client is named, there is no pricing and nothing about the FDA. The compliance line is present (healthcare ICP).
- jeremyncastle M2:29, "which keeps results comparable across sites". This claims comparability that no approved line supports, because repeatability may only be stated as the "< 1 cm" sentence. It is also incoherent: the scan is taken at home, not at a site. And "sites" puts the clinic network into the CEO's message in a campaign whose cause is clinic closures.
- jeremyncastle M1:18, jessicatarnawa M1:18 and jdelcecato M1:18 say "a scan patients take at home inside your patient app" and "a guided two-photo scan inside your patient app". Read literally, this says the scan already runs in Options' app. The card's own phrasing causes it, but adding "can" fixes it.
- jdelcecato M2:29 has "3DLOOK customers ran 112,100 scans in 2025." directly after "a feature patients can use…". The juxtaposition invites reading 112,100 as patient scans, but the figure is 3DLOOK-wide and includes apparel. It should be its own line, in the cleared wording.

### C. Brand & tone: 2/3
- nicholasfoy34 M1:18: "No pitch, just the right contact." This is the corrective "no X, just Y" shape that prompt rule 8 bans.
- nicholasfoy34 M2:27: "Following your own schedule is fair, so one short ask." The sentence makes no sense. Sent to a man whose bio says he is exploring other jobs, it can read as a nod to that, which the card bans.
- nicholasfoy34 M1:16: "so you likely know who…" presumes what he knows. This is the same family as `presumed_reaction`.
- jessicatarnawa M1:16 "Quick thought as Director of Medical Operations…" and joshua-hicks M1:16 "Quick one as Clinic Director:" are dangling modifiers: Nick is neither. They also share one skeleton ("Quick ___ as <title>").
- No banned words and no dashes (gate).

### D. Format & structure: 2/3
- **The prompt's "≤ 2 sentences per paragraph" rule is broken in 5 messages:** jeremyncastle M2 (3), jessicatarnawa M2 (3), jdelcecato M2 (4), nicholasfoy34 M1 (3), nicholasfoy34 M2 (3).
- `_summary-all.md:11` says the "no company line" notes fire "because the copy says 'Options', not the full name". That is false for Jessica: her M1 names no company at all. The fix below adds "Options", which makes the line true.
- System note, not capped: no per-person file has `product: fitxpress` frontmatter. The fault is in the `split-messages` template, not the agent (coordinator ruling, 2026-09-29). With the hard cap, D would be 1 and the total 14 (marginal).

### E. Output quality: 3/4
- **The two referral sequences read as a mail merge.** About half of Joshua's M1 appears verbatim in Nicholas's M1, which misses the 60% uniqueness override. These two are peers, the most likely pair to compare notes.
- **Jeremy and Jessica share a product paragraph.** It is about 85% identical, which leaves their M1s about 57% unique.
- **Jeremy and Jory share both CTAs:** "Open to a quick chat?" in M1, and "Worth 15 min? <link>" in M2.
- **Three M2 openers share one skeleton:** "Circling back with the operating view." / "One more thought for the clinical side." / "Picking this up from the program side." Screenshotted side by side, these read as one template with the role noun swapped.
- jdelcecato M1:16, "Caught my eye: your focus on growth and sales strategy". This hook repeats his headline buzzwords back to him. His bio has something concrete: he has worked on prescription medication programs.
- Ceiling, caused by the card: the verbatim compliance line plus the hub and calendar links take up about 47% of each non-referral M2.
- Strong: Jessica's M2 line on the progress reports Options sends referring physicians. Jory's memberships-and-packages question. Castle's named former employers. Every hook checks out against its profile card.

## Line fixes (apply in `_batch-all.md`, then re-run split-messages)

Char counts are hand estimates. The script is authoritative.

**jeremyncastle M1** (→ ~474/600)
- "Noticed your background running operations at The Oncology Institute and OneOncology." → "Noticed your background running multi-site operations at The Oncology Institute and OneOncology."
- "We built a two-photo scan patients take at home inside your patient app:" → "We built a two-photo scan patients can take at home inside your patient app:"

**jeremyncastle M2** (→ ~475/550). Replace the first paragraph with two paragraphs:
- Old: "Circling back with the operating view. One guided sequence means patients scan the same way between visits and on video visits, which keeps results comparable across sites. The telehealth and clinic workflow part of this is useful: https://3dlook.ai/content-hub/glp-1-market/"
- New: "Circling back with the operating view: one guided sequence means every Options patient scans the same way, between clinic visits or on video visits." [blank line] "The section on clinic and telehealth workflows here covers it: https://3dlook.ai/content-hub/glp-1-market/"

**jessicatarnawa M1** (→ ~520/600)
- "Quick thought as Director of Medical Operations with a nurse practitioner background: how would you want providers to review body data at a follow-up?" → "Quick thought, given your nurse practitioner background: as Director of Medical Operations, how would you want Options providers to review body data at a follow-up?"
- "We built a guided two-photo scan patients take at home inside your patient app. It returns 80+ body measurements, a 3D model and body composition estimates in under 45 seconds from the photos to structured results, standardized and timestamped." → "Our guided two-photo scan can run inside your patient app. Patients take it at home, and providers review standardized, timestamped results: 80+ body measurements, a 3D model and body composition estimates." [blank line] "For most evaluated measurements, repeated scans showed typical scan-to-scan differences of less than 1 cm."

**jessicatarnawa M2** (→ ~454/550)
- Old: "One more thought for the clinical side. Providers can compare scans the practice selects, and the structured results can sit alongside the progress reports Options sends referring physicians. Resource: https://3dlook.ai/content-hub/glp-1-market/"
- New: "For follow-ups, providers can compare scans the practice selects, and the structured results can sit alongside the progress reports Options sends referring physicians." [blank line] "Resource: https://3dlook.ai/content-hub/glp-1-market/"

**jdelcecato M1** (→ ~449/600)
- "Caught my eye: your focus on growth and sales strategy. A product question: does a body scan from the phone belong in what Options sells with its memberships and packages?" → "Caught my eye: your growth and sales-strategy work across prescription medication programs. A product question: does a body scan from the phone belong in the memberships and packages Options sells?"
- "It is a guided two-photo scan inside your patient app:" → "It is a guided two-photo scan that can run inside your patient app:"
- "Open to a quick chat?" → "Would a short call on that be useful?"

**jdelcecato M2** (→ ~524/550, the tightest)
- Old: "Picking this up from the program side. A guided at-home scan is a feature patients can use wherever they are, next to body composition analysis and coaching. 3DLOOK customers ran 112,100 scans in 2025. Background: https://3dlook.ai/content-hub/glp-1-market/"
- New: "On the memberships and packages: a guided at-home scan is a program feature patients can use wherever they are, next to the body composition analysis and coaching your programs include." [blank line] "112,100 scans ran in 2025 across all 3DLOOK customers. Background: https://3dlook.ai/content-hub/glp-1-market/"
- "Worth 15 min? https://meetings.hubspot.com/nick-omelchak" → "Grab a slot if it fits: https://meetings.hubspot.com/nick-omelchak"

**joshua-hicks-10ab2014a M1** (→ ~229/600). Joshua's thread becomes the app-roadmap ask. "Thanks," / "Nick" stay.
- Old: "Quick one as Clinic Director: who at Options looks after the Health Coach app and the telehealth program?" [blank line] "We work on a guided two-photo body scan patients take at home inside the app, and I would like to reach the right person."
- New: "A routing question, since you run an Options clinic: who decides what goes into your patient app?" [blank line] "At 3DLOOK we build a guided two-photo body scan that patients can take at home inside an app like yours."

**joshua-hicks-10ab2014a M2:** no change.

**nicholasfoy34 M1** (→ ~263/600). Nicholas's thread becomes the telehealth-program ask.
- Old: "Wanted to reach out: you run operations for GLP-1 programs at your clinics, so you likely know who looks after the Options Health Coach app and the telehealth program." [blank line] "Who would that be? The context is a guided two-photo body scan patients take at home inside the app. No pitch, just the right contact."
- New: "Wanted to reach out: you run operations for GLP-1 programs at your clinics. Who at Options leads the telehealth program and the Health Coach app?" [blank line] "The context: a guided two-photo body scan from 3DLOOK that patients take at home between visits."

**nicholasfoy34 M2** (→ ~137/550)
- Old: "Following your own schedule is fair, so one short ask. Who owns decisions on the patient app at Options? I will take it from there."
- New: "Short nudge in case my note got buried. Who owns decisions on the patient app at Options?" [blank line] "I will take it from there."

After these fixes the five asks differ:
- Castle: one capture for every patient.
- Tarnawa: how providers review at follow-ups.
- Del Cecato: whether it belongs in what Options sells.
- Hicks: who decides the app.
- Foy: who leads the telehealth program.

The M1 CTAs, M2 CTAs and M2 openers are now all different, and every M1 names Options.

## Top 3 issues (priority for improver)

1. **The referral pair is one ask sent twice.** Same question, same context line verbatim, sent to two peer Clinic Directors at once. The card causes part of it: the referral lane prescribes one verbatim question. For single-account campaigns the card should give each referral person a distinct question.
2. **Jeremy M2: "keeps results comparable across sites".** This comparability claim has no approved source, puts "sites" into a CEO message in a closure-driven campaign, and makes no sense for a scan taken at home.
3. **The at-home lane repeats the same fact set and sentence to the CEO and the Director of Medical Operations (prompt rule 3).** It also has a paragraph-length miss in 5 messages and Foy's M2 opener, which can read as a nod to his job search.

System note for the coordinator: the gate's "no company line" check matches only the legal name "Options Medical Weight Loss" and fired on 5/5. Four of those were false positives, because "Options" was named. It should accept the short name, or it will train everyone to ignore it.

## coordinator_review

```
agreement: ✅ agree (the "less than 1 cm" line checked: licensed verbatim, proof-points.md:38 and card-messages.md:64)
top_issue: the two Clinic Directors got the same referral ask; root cause is partly the card, which prescribes one referral question per lane
action: every line fix sent back to message-sequencer and applied in _batch-all.md + split-messages (Vadim waived the checkpoint 2026-10-01); check-messages re-run over the campaign before build-import. Not fixed in this run (pipeline backlog): the gate's company-line check matches only the full legal name; single-account campaigns need a distinct question per person in a shared lane
```
