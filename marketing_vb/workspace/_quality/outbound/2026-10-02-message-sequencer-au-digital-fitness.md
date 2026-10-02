---
qc_date: 2026-10-02
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-08-14-au-digital-fitness/messages/ (primary: aaron-mcallister-328404170, arleygrey, alison-mclean-06306b20, _check.json; all four _batch-*.md read in full, 123 people / 246 bodies; four _summary-*.md)
track: outbound
artifact_type: messages
total_score: 14/20
status: marginal
coordinator_review: done
---

# QC Report: message-sequencer, 2026-10-02, au-digital-fitness

**Artifact:** `workspace/outbound/campaigns/2026-08-14-au-digital-fitness/messages/` (123 people, 17 companies, 4 batches; AIA Australia is 50 people across aia-australia-1 and aia-australia-2)
**Total: 14/20, marginal.**

Most of the copy is good. The hooks are real and match the profile rows. The partial-overlap accounts are never pitched anything as new. The Kic, AIA and Defeat Diabetes framing limits hold. OQ6 (a) holds in all 246 bodies.

The campaign's own uniqueness rule is what fails (card:108, repeated in the prompt). Of the 12 companies with more than one person, 9 still have shared sentences, closing asks or hook phrases. Only Digital Wellness, Fernwood and Fitstop are clean. That is wider than the coordinator's exact-match list.

Two smaller groups also need fixes:
- Card instruction wording leaked into copy in 5 records.
- Locked wording or placement broke in 3 records.

Every fix is a single sentence. Nothing needs regenerating.

Scored against `card-messages.md` and the four `_profiles-*.md`. The coordinator's gate and scan facts are taken as given. Per instructions, D is not capped for the missing `product:`.

Line refs: aia1 = `_batch-aia-australia-1.md`, aia2 = `_batch-aia-australia-2.md`, mx1 = `_batch-mixed-1.md`, mx2 = `_batch-mixed-2.md`.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence: 3/5

**Coordinator's same-company list.** Confirmed in full:
- Speed wrapper: Vively, Hapana, Sweat, Kic, 12WBT.
- AIA "Results arrive in…", "It returns results in…" and "A pointer would be welcome."
- AIA "We build a scan returning 80+…".

**Further same-company collisions the exact-match scan missed** (card:108: no shared opener, central question, closing ask or product sentence):

Closing asks:
- Hapana: jarronaizen (mx2:423) and milenazanini (491) both close with "Worth a quick chat?".
- Hapana: alansach (445) and gopalagrawal (513) both close with "Open to a quick chat?".
- Xyris: declan-goodsell M1 (885) and shian-russell-jordan M2 (915) both close with "Open to a chat?".
- Everlab: dr-steven-lu M1 (mx1:11) and michael-reid M2 (217) both close with "Open to a quick chat?".

Hook phrase:
- Sonder: nmatthewslondon (mx1:291) and conroymichael (411) both open with "Noticed your background".
- nemo-hu (363) opens with "Noticed your machine learning background", a third at the same company.

Product sentences one word apart, at AIA:
- karenmpurcell (aia1:719) uses "We build a scan that returns 80+ body measurements from two phone photos." The same clause opens george-stavliotis (413). mbroom (53) differs only by "built".
- vaibhav5harma (697) is elke and jordan's sentence with "guided" added.
- trish-curry (741) "two-photo scan returning 80+" matches nicky-serret (675) "two-photo scan with 80+".

Speed wrappers one word apart:
- AIA:
  - trish-curry (749) "The scan runs in" vs luke-ashby (15) "It runs in".
  - sally-barnett (661) and alison-mclean (147) both use "The scan finishes in…".
  - jo-moon (509) "The scan returns results in" vs parker-craig and wanda-britton "It returns results in".
  - matt-goodison (337) "results arrive in" vs theresa and elke.
  - davelevans (379) "Results come in" vs jeremytsimmons (211) "Results come back in".
- Everlab: dr-steven-lu (mx1:17) and matthewtkwong (141) both use "Results arrive in…".

Central question:
- At AIA, arleygrey (aia2:7), katherinemcauliffe (aia2:71) and parker-craig (aia1:159) all ask what gives members "a reason to" open the app, return or check in.
- luke-ashby (aia1:7) and arleygrey both tie that question to "between Health Checks".

**Referral lane without the company fact.** Card:69 requires "the company fact" in the referral lane. Card:122 requires one line in every M1 that could only have been written to that company. Nine referral M1s carry only the company name, so with the name swapped they fit any company:
- mx1: halla-dadouch (227), michaelapigott (475), david-badet (495).
- mx2: ella-wheeler (251), zoe-kirby (291), olivia-houston (379), sally-kubler (399), rajankanwat (555), tessdrobik (663).

The AIA referrals pass because they name AIA Vitality and use the person's background.

**Other adherence points:**
- **a-prof-newman-l-harris was flagged rather than fixed.** The title sits in both greetings (aia1:263, 271), but the person_id carries the given name.
- **Summary self-reports are wrong.**
  - `_summary-aia-australia-1:10` says 112,100 appears "only as own sentence". george-stavliotis and jordanbeasley break that (see B).
  - `_summary-aia-australia-2:11` says the only overlap with batch 1 is the speed tail. That misses the central-question overlap above.
- **Passes:**
  - No compliance line anywhere.
  - No calendar link.
  - Every M1 names the company.
  - Lanes match the profile cards and each lane gets its asset.
  - aia-australia-2 read aia-australia-1 and is the cleanest batch.

### B. Factual accuracy: 4/5

**Rule breaks:**
- **annacrook (mx2:101) uses an unapproved speed claim:** "a 3D model back in seconds". Card:111 allows "the only speed wording, verbatim, every time".
- **112,100 is not its own sentence (card:110) in two records:**
  - george-stavliotis (aia1:423): "…is the only context I would add."
  - jordanbeasley (aia1:551): "…is the scale behind the scan." This ties the 3DLOOK-wide figure to the scan being pitched.

**Misleading or unsupported:**
- **chris-healey (aia1:253): "Delivery takes under 45 seconds…"** M1 says "delivered through an API or SDK", so this reads as integration time.
- **marc-hermann (mx1:57): "foodspring, a brand built around members' daily routines".** This is on neither his row nor the card, and foodspring has no members.
- **dr-michelle-woolhouse (mx2:823) extends the repeatability sentence** with ", which suits a care team comparing scans it selects". Card:111 allows the §1.2 sentence "only as" written. annacrook (109) and shian (913) put a colon prefix before it but keep the content verbatim, which is acceptable.
- **marie-therese-nguyen-da-huong (aia1:391): "When a new data source arrives in AIA Vitality, what do you want to see first?"** This goes to an insurer's GM Data Governance and Business Insights. It frames member body data as flowing into AIA's data estate, which is the closest any AIA line comes to card:117. Judgment call.
- **rochelle-evans:** the proof field (aia2:25) cites the repeatability sentence, but the copy (37) has only the qualitative "Repeat scans stay comparable…". The mismatch is internal and nothing false reaches the prospect.

**Passes:**
- Every number is on the card. The 34,000 line is anonymous (sujan).
- 96-97% carries the correct reference and does not open M2 (benjamin-martin 357).
- No client, competitor, device, drug or health-fund name. Former employers are named only where they are on the person's row.
- AIA stays wellness-only. tracey-crowe, chris-freeman and kimmareeclough get no claims or pricing angle.
- Defeat Diabetes uses person-first language (zoeeaton 41).
- Sweat's photos, 12WBT's My Tracker and Digital Wellness's weigh-in photos are all framed "alongside".
- The Kic quote is used only to agree with it.
- Sourcing: not applicable (outbound).

### C. Brand & tone: 2/3

- **Card instruction wording leaked into copy:**
  - travis-shannon (mx2:533) and victorgarciagonzalez (859): "a generic figure and never a promise" (coordinator).
  - sharifalvis (mx1:181): "a generic figure for a basic integration". This is a third instance, and it says "basic integration" twice in one sentence.
  - sarah-cahill (mx2:737): "Wellness only." (card:66/117).
  - silipa-burgess (aia2:123): "The wellness and engagement framing stays with the program."
- **"so" introducing a benefit** (terminology hard ban): parker-craig (aia1:167) "so the experience stays in the app".
- **Tricolon:** riley-woodcock (mx2:367) "same guided steps, same two photos, every time".
- **Process triple across four companies:** the "capture screen, API call, structured results" pattern repeats in joegolio (63), gopalagrawal (519), tom-grimshaw (651) and kieran-harrison (781).
- **kitty-robinson (mx2:239): the scan becomes "something concrete to share"** in member stories, at a women's club community. Card:116 bans before-and-after framing and treats the 3D model as a view the member chooses to see. Judgment call.
- **Odd lines:**
  - kimmareeclough (aia2:275): "No materials attached to this note."
  - michelle-bennie (aia1:443): "with nothing to sign or review".
  - tim-billington (aia2:253): "A member waits under 45 seconds…".
  - kieran-harrison (mx2:781): "all within under 45 seconds".
  - a-prof-newman-l-harris (aia1:275): "Is there a better person than you for this?"
- **Presumed reactions:**
  - alison-mclean (aia1:139): "you know what turns a health action into a habit".
  - dtodriscoll (aia2:137): "vendor integrations probably cross your desk".
  - lakshmi-koppula (mx2:465): "You know better than most what…".
- No banned words and no dashes (gate and coordinator).

### D. Format & structure: 2/3

- **About 20 mx2 M2s put the soft ask inside the body paragraph.** The prompt wants the CTA on its own line. Examples: ellechai 197, bianca 219, ryan 347, riley 369, jarron 431, lakshmi 477, milena 499, natalie 587, steph 609, laura 631, stephanie-clark 695, jane 717, sarah-cahill 739, tim-veron 805, kat 847, declan 893, shian 915. The other three batches keep it separate.
- **Two M1s have no soft ask after the product line:**
  - dr-michelle-woolhouse (mx2:817, non-referral; the summary flagged it).
  - phillip-klobucki (aia2:311, referral; its question sits in paragraph 1).
- **Fine:** batch format, per-person split, character limits (gate), greetings, signatures and summary shape.

### E. Output quality: 3/4

- **The personalization is real.** Every message is well over 60% unique on its hook and question. Good lines worth keeping:
  - becky-wallis: the scan alongside Activity-section photos.
  - tom-grimshaw: route mapping as the model.
  - jinguo111: language as a design question.
  - stephanie-clark: alongside My Tracker.
  - dtodriscoll: an assessment question for an architect.
  - zoeeaton: the clinical M2.
- **AIA's 24 referral sequences share one skeleton:** a background clause, "who owns the AIA Vitality app", "We build a scan … 80+ … two phone photos", then "a name would help". The repetition comes from cap 50 at one company, but the product line and speed wrapper still have to vary. Forwarded inside AIA, the set reads as a mail merge.
- **Stub sentences dropped in with no tie to the ask:**
  - "112,100 scans in 2025 across all 3DLOOK customers." (tristanknowlesoam aia1:639)
  - "The scan returns 80+ body measurements." (michelle-bennie 445)
  - "Two photos in, structured results out." (vaibhav 705)
- **aaron-mcallister M2 (mx2:759) is thin:** one sentence restating M1, then the CTA, 181 characters. It has no value line (M2 template step 2), though the M1 Body Type Quiz hook is good.
- **The two mixed batches handle the M2 article link inconsistently:**
  - mx1 opens 18 links with the same "A short read:". 7 Sonder people get the same line and the same URL.
  - mx2 drops the asset in 40 of 42 M2s.
  - Both are allowed ("at most one"). The inconsistency points to two writers working without a shared norm.
- **Sample files:**
  - arleygrey: "experience … experiences" in the headline paraphrase (aia2:7). Its central question collides with katherine and parker.
  - alison-mclean: clean, apart from the speed wrapper it shares with sally-barnett.
  - aaron-mcallister: thin M2 (above).

## Top 3 issues (priority for improver)

1. **Same-company uniqueness (card:108), 9 of 12 multi-person companies.** Fix the coordinator's exact matches and the misses above:
   - Closing asks at Hapana, Xyris and Everlab.
   - "Noticed your background" at Sonder.
   - One-word-off product and speed sentences at AIA and Everlab.
   - The AIA "reason to return" question.

   Fixing one side of each pair is enough.
2. **Card instructions in copy (5 records):** travis-shannon, victorgarciagonzalez, sharifalvis, sarah-cahill, silipa-burgess.
3. **Locked wording and rules:**
   - annacrook: speed variant.
   - george-stavliotis, jordanbeasley: 112,100 not its own sentence.
   - a-prof-newman-l-harris: title in the greeting.
   - Nine referral M1s with no company fact.

**System notes (not the agent's fault):**
- **The gate exited 0 with no notes, yet missed four kinds of problem:**
  - Repeated M1 closing asks inside Hapana, Xyris and Everlab. The coordinator note on the 2026-10-02 us-virta-health QC says check-messages now flags these, but it did not fire here. It may check M2 only, or exact matches across M1/M2 only.
  - The "back in seconds" speed variant.
  - 112,100 embedded mid-sentence.
  - Card-phrase leaks ("never a promise", "generic figure", "Wellness only", "framing").

  An n-gram check of copy against the card's rule text would catch the last one.
- **The split per-person files carry the header "Message 2: Value + demo call"**, although vadim has no demo call. This is script text.
- **notify.py was not sent:** this QC run had no Bash tool.

## Coordinator review

(filled in by Claude in chat after the auto-QC run)

## coordinator_review

```
agreement: ✅ agree
top_issue: same-company near-duplicates (closing asks, openers, wrapper sentences) survived because the gate only noted closing asks repeated by 3+ people and only exact "45 sec" drift; fix round sent to all four batches (aia-australia-2 after aia-australia-1), and the gate now flags a repeated closing ask from 2 people at one company and any "seconds" without the verbatim phrase.
```
