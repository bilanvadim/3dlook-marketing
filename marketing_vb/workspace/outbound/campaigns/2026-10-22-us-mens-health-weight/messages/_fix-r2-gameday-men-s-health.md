# Fix round 2 — batch gameday-men-s-health — from QC 14/20, 2026-10-23

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


## Coordinator additions
- allen-brooke-834a1119 drops the speed sentence (speed is not the point of his question); timothy-rempher-81347433 keeps it. Then no product-sentence twin is left.
- Layout (item 6 above) applies to every non-referral Gameday M2, all 29, so the compliance line sits before the call line everywhere.
- Presumptive lines from QC section C at Gameday: none named beyond the single lines above; still check rule 6 across the batch.
