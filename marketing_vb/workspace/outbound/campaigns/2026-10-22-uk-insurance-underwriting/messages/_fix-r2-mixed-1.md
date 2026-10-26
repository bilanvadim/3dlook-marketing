# Fix round 2 — mixed-1 (2026-10-26)

Round 1 passed the gate. The coordinator read all 352 messages; this round fixes what the gate does not see. Same rules go to all seven batches. Edit `messages/_batch-mixed-1.md`, then run split-messages until exit 0.

## Rules for this round

1. **Product sentence shape varies inside a company.** At one company, no 10-word run of the M1 product sentence repeats across three people. Vary which part leads (the record, the threshold set by the company, the 2 photos, the step's place in this person's journey) and include only the parts this person's question needs. Each M1 still says what comes back and who decides (photos and the threshold flag at minimum).
2. **Speed sentence:** at most one person per company carries "under 45 seconds from the photos to structured results", only where speed is that person's point. Others delete it; the pair's number already comes from "2 photos" in M1.
3. **Fixed lines stand alone or go.** "112,100 scans in 2025 across all 3DLOOK customers." and "3DLOOK has worked with 100+ clients." appear only as exact plain sentences, never with a label before them ("For scale,", "For product, the plain facts:") or a claim added after them, and never as the first sentence of M2.
4. **Card rules are not copy** (the current route for applicants who do not scan, the referral-trigger rule text): the listed people get a plain value line instead.
5. Keep everything else: compliance sentences (exactly one per pair, as now), hooks, account facts, the 3.5% wording, the call line. Re-read every changed message in full before split-messages, and check that every pair still has a number the gate recognises.

## Per person


### Nicky Roux · nicky-le-roux-7b8b758 · VitalityLife · underwriting
- Speed sentence «The scan returns 80+ body measurements, under 45 seconds from the photos to structured results.»: delete it (speed is not this person's point; the pair keeps its number from "2 photos" in M1).

### Louise Cowan · louise-cowan-692b9b123 · VitalityLife · proposition
- M1 product sentence shares a 10-word run with 2+ colleagues at VitalityLife («a gap between declared and estimated weight only above a»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Gareth Alan-Williams · gareth-alan-williams-7709b658 · VitalityLife · proposition
- M2 opens on "3DLOOK has worked with 100+ clients.": open on the value line; move or drop the line.

### Becca Cooke · beccacooke · VitalityLife · proposition
- Label or add-on around a fixed line «For product, the plain facts: 112,100 scans in 2025 across all 3DLOOK customers.»: delete the sentence (or keep "112,100 scans in 2025 across all 3DLOOK customers." exactly, alone, only if it serves this person).

### Kathryn Conniff · kathrynconniff · VitalityLife · underwriting
- Speed sentence «The scan returns a weight estimate, under 45 seconds from the photos to structured results.»: delete it (speed is not this person's point; the pair keeps its number from "2 photos" in M1).

### Fareeha Brownless · fareeha-brownless-nee-hasani-84b7b413 · VitalityLife · proposition
- Coordinator read: The pair now argues the card rule (applicants who skip carry on as today) in M1, the question and M2. Rewrite the pair for a Head of Product (Life): a question about her life application journey, and an M2 value line that answers it. The current-route idea may appear at most as half a sentence, not as the question.

### Rachel Loudain · rachel-l-2387142a · VitalityLife · proposition
- M1 product sentence shares a 10-word run with 2+ colleagues at VitalityLife («a gap between declared and estimated weight only above a»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.
- Speed sentence «It returns a weight estimate, under 45 seconds from the photos to structured results.»: delete it (speed is not this person's point; the pair keeps its number from "2 photos" in M1).

### James Ayland · james-ayland-6181bab5 · VitalityLife · underwriting
- Label or add-on around a fixed line «For scale, 112,100 scans in 2025 across all 3DLOOK customers.»: delete the sentence (or keep "112,100 scans in 2025 across all 3DLOOK customers." exactly, alone, only if it serves this person).

### Sandi Sohal · sandi-sohal-2853aa13 · Pacific Life Re · reinsurance
- Coordinator read: "which is why I am writing from 3DLOOK to Pacific Life Re about build" is clunky: shorter plain opener.

### Réka Halász · réka-halász-9a72b585 · Pacific Life Re · reinsurance
- M2 opens on "3DLOOK has worked with 100+ clients.": open on the value line; move or drop the line.

### Mala Thurston · mala-thurston-22a0b499 · Pacific Life Re · reinsurance
- M2 opens like 4 colleagues at Pacific Life Re («a shadow evaluation…»): open differently.

### Martin Boniface-Jones · martin-boniface-jones-371173112 · Pacific Life Re · reinsurance
- Label or add-on around a fixed line «For scale, 112,100 scans in 2025 across all 3DLOOK customers.»: delete the sentence (or keep "112,100 scans in 2025 across all 3DLOOK customers." exactly, alone, only if it serves this person).

### Killian Farrelly · killian-farrelly-96422a60 · Pacific Life Re · reinsurance
- M2 opens like 4 colleagues at Pacific Life Re («a shadow evaluation…»): open differently.

### David Waters · david-waters-05719b114 · Pacific Life Re · reinsurance
- Speed sentence «It returns 80+ body measurements, under 45 seconds from the photos to structured results.»: delete it (speed is not this person's point; the pair keeps its number from "2 photos" in M1).

### Nikolai Harrowing · nikolai-harrowing-5246b353 · Pacific Life Re · reinsurance
- M1 product sentence shares a 10-word run with 2+ colleagues at Pacific Life Re («a gap between declared and estimated weight only above the»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.
- Coordinator read: M2 opens on the boundary sentence and has no value line ("It returns 80+ … record"): write a value line that continues his question, then the boundary sentence before the call line.

### Justin Farrow · justin-farrow-226782108 · Pacific Life Re · reinsurance
- M1 product sentence shares a 10-word run with 2+ colleagues at Pacific Life Re («a gap between declared and estimated weight only above the»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.
- Speed sentence «The scan returns a record, under 45 seconds from the photos to structured results.»: delete it (speed is not this person's point; the pair keeps its number from "2 photos" in M1).
- M2 opens like 4 colleagues at Pacific Life Re («a shadow evaluation…»): open differently.

### James Sims · james-sims-846a9251 · Pacific Life Re · reinsurance
- Speed sentence «The scan returns a weight estimate, under 45 seconds from the photos to structured results.»: delete it (speed is not this person's point; the pair keeps its number from "2 photos" in M1).
- M2 opens like 4 colleagues at Pacific Life Re («a shadow evaluation…»): open differently.
