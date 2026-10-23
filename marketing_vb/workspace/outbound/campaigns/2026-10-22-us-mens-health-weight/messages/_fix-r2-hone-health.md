# Fix round 2 — batch hone-health — from QC 14/20, 2026-10-23

## Rules for this round (the same list goes to every batch)

QC scored the campaign 14/20 (report: workspace/_quality/outbound/2026-10-23-message-sequencer-us-mens-health-weight.md; read only the lines that name your person_ids). Edit only people named in your list below, but every rule here holds for the whole company when you are done. Rules name targets, not sentences: do not copy any wording from this file into copy.

1. **Openers.** No two M1s at one company share their first three words (this replaces round 1's "a hook at most twice"). Adapt the template hook so the first three words differ. A hook verb is followed through: "Thought I'd share" shares something, "Couldn't help but ask" asks, "Quick reaction" reacts. Never address the reader in the third person ("for a chief executive at …").
2. **Product sentence.** No two M1s at one company share a product sentence, by wording or by skeleton (e.g. "[FitXpress] returns 80+ body measurements from two photos", "Two photos in, 80+ out", "FitXpress is a REST API with SDKs"). "80+ body measurements" does not have to be in every M1: rotate the specific (two photos front and side; a guided capture on any phone; 80+ body measurements, waist and hip among them; body composition estimates with BMI and BMR; a 3D model; white-label API and SDKs; the phone as the only hardware, in your own words; the §1.2 repeatability sentence where repeat captures matter; a fixed proof line). If a rewrite turns contorted, pick a different specific instead of rephrasing the same one. No list of three of our own features in one sentence.
3. **Card text is not copy.** Gone from copy: "values are estimates" (any form), "the host app owns the entry point", lane target text ("one capture step HQ adds once and each clinic switches on"), "no device / hardware / nothing to ship" more than once per company, "picks which captures to compare" except for at most 2 people per company whose own question is about comparing captures. Body measurements are never "estimates" (only body composition is).
4. **Message 2 value line** continues the person's own M1 question in new words: one or two sentences about what changes for him or her. A proof line or a rule sentence alone is not a value line. Technical lane: the spec that answers his question. At one company no two value lines share a skeleton ("[Abstract noun] needs X.", "Each capture … timestamped …", "A capture [time phrase] would/could …", "A record that …").
5. **Easy outs.** Only people who are not the buyer get one; founders, co-founders and CEOs get none. At one company no shape is used by more than 3 people ("If/Should HQ …, [ask]"; "[owner]? I'm glad to talk with them"; "a colleague … an intro"; "sits with someone else"), and no two easy outs share verb and structure.
6. **No presumed facts about the reader's company or work** ("X needs Y", "is where teams do Z", "has to be", "lives on", "earns its keep", "is … first", "you know which …", "fills a slot"). Say our side plainly, or ask.
7. **Claims.** Never say or imply that FitXpress keeps a member's history, follows a member over time or across clinics, or that a record travels with him. Fixed proof lines are each their own plain sentence. The integration figure is "a typical basic integration takes 2-4 weeks", never phrased as the reader's plan. No "clinician view". US spelling.
8. **Message 2 layout:** value line, then the compliance line (non-referral), then the call sentence with the calendar link on its own line, then the easy out (if any) on its own line, then Nick. Nothing follows a URL on the same line. Keep the compliance line, calendar link and article links exactly as they are.
9. **Metadata.** Update each changed person's `Proof point:` and hook lines so they match the copy, and correct your `_summary-<batch>.md` (counts, stale flags).
10. Run split-messages until exit 0. Then re-read every changed message in full and check rules 1, 2, 4 and 5 across the whole company yourself, not only for the people you edited.

## Your people (QC fix list, verbatim)

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


## Coordinator additions
- Presumptive lines (QC section C) at Hone: stuartblitz M2, daniel-ward-5976a5204 M1 and M2, rebeccakayhiggins M1 and M2, ashley-camerini-3363717b M1 and M2, hagel M1, nicholas-del-prince-244052ab M1, ayushsoni01 M1, tobin-abraham M1.
- Triple: saad-alam-a146b311 M1.
- seth-franz and alba-mertira are co-founders: no easy out.
