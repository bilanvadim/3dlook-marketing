# Fix round 2 — royal-london (2026-10-26)

Round 1 passed the gate. The coordinator read all 352 messages; this round fixes what the gate does not see. Same rules go to all seven batches. Edit `messages/_batch-royal-london.md`, then run split-messages until exit 0.

## Rules for this round

1. **Product sentence shape varies inside a company.** At one company, no 10-word run of the M1 product sentence repeats across three people. Vary which part leads (the record, the threshold set by the company, the 2 photos, the step's place in this person's journey) and include only the parts this person's question needs. Each M1 still says what comes back and who decides (photos and the threshold flag at minimum).
2. **Speed sentence:** at most one person per company carries "under 45 seconds from the photos to structured results", only where speed is that person's point. Others delete it; the pair's number already comes from "2 photos" in M1.
3. **Fixed lines stand alone or go.** "112,100 scans in 2025 across all 3DLOOK customers." and "3DLOOK has worked with 100+ clients." appear only as exact plain sentences, never with a label before them ("For scale,", "For product, the plain facts:") or a claim added after them, and never as the first sentence of M2.
4. **Card rules are not copy** (the current route for applicants who do not scan, the referral-trigger rule text): the listed people get a plain value line instead.
5. Keep everything else: compliance sentences (exactly one per pair, as now), hooks, account facts, the 3.5% wording, the call line. Re-read every changed message in full before split-messages, and check that every pair still has a number the gate recognises.

## Per person


### Amy Higgs · amy-higgs-a1960563 · Royal London · referral
- Speed sentence «FitXpress returns 80+ body measurements, under 45 seconds from the photos to structured results.»: delete it (speed is not this person's point; the pair keeps its number from "2 photos" in M1).

### Myrto (Myrsini) A. · malexandratou · Royal London · referral
- M1 product sentence shares a 10-word run with 5+ colleagues at Royal London («flags a gap between declared and estimated weight above a»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.
- Label or add-on around a fixed line «For scale, 112,100 scans in 2025 across all 3DLOOK customers.»: delete the sentence (or keep "112,100 scans in 2025 across all 3DLOOK customers." exactly, alone, only if it serves this person).

### Fi Wynn · fi-wynn-72936a4 · Royal London · proposition
- Speed sentence «FitXpress returns 80+ body measurements, under 45 seconds from the photos to structured results.»: delete it (speed is not this person's point; the pair keeps its number from "2 photos" in M1).

### James Sandell · james-sandell-4686b59 · Royal London · technical-integration
- M1 product sentence shares a 10-word run with 5+ colleagues at Royal London («flags a gap between declared and estimated weight above a»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Dominic Pagan · dominic-pagan-4077583 · Royal London · underwriting
- The 3.5% sentence opens like a colleague's at Royal London («smart scales has approximately…»): keep "approximately 3.5% mean absolute error under evaluated conditions" and "not a scale reading" in one sentence, and frame it differently.

### Robert Arbuckle · robert-arbuckle-b4aa3669 · Royal London · underwriting
- M1 product sentence shares a 10-word run with 5+ colleagues at Royal London («flags a gap between declared and estimated weight above a»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### William Stratton · william-stratton-8ab764104 · Royal London · underwriting
- M1 product sentence shares a 10-word run with 5+ colleagues at Royal London («flags a gap between declared and estimated weight above a»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Damian Mapplebeck · damian-mapplebeck-99103818 · Royal London · underwriting
- Label or add-on around a fixed line «The scale behind the service: 112,100 scans in 2025 across all 3DLOOK customers.»: delete the sentence (or keep "112,100 scans in 2025 across all 3DLOOK customers." exactly, alone, only if it serves this person).

### Seb Bowden · sebbowden · Royal London · underwriting
- M1 product sentence shares a 10-word run with 5+ colleagues at Royal London («flags a gap between declared and estimated weight above a»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Robin Goodwin · robin-goodwin-039aa5271 · Royal London · underwriting
- The 3.5% sentence opens like a colleague's at Royal London («smart scales has approximately…»): keep "approximately 3.5% mean absolute error under evaluated conditions" and "not a scale reading" in one sentence, and frame it differently.
