# Fix round 2 — legal-general (2026-10-26)

Round 1 passed the gate. The coordinator read all 352 messages; this round fixes what the gate does not see. Same rules go to all seven batches. Edit `messages/_batch-legal-general.md`, then run split-messages until exit 0.

## Rules for this round

1. **Product sentence shape varies inside a company.** At one company, no 10-word run of the M1 product sentence repeats across three people. Vary which part leads (the record, the threshold set by the company, the 2 photos, the step's place in this person's journey) and include only the parts this person's question needs. Each M1 still says what comes back and who decides (photos and the threshold flag at minimum).
2. **Speed sentence:** at most one person per company carries "under 45 seconds from the photos to structured results", only where speed is that person's point. Others delete it; the pair's number already comes from "2 photos" in M1.
3. **Fixed lines stand alone or go.** "112,100 scans in 2025 across all 3DLOOK customers." and "3DLOOK has worked with 100+ clients." appear only as exact plain sentences, never with a label before them ("For scale,", "For product, the plain facts:") or a claim added after them, and never as the first sentence of M2.
4. **Card rules are not copy** (the current route for applicants who do not scan, the referral-trigger rule text): the listed people get a plain value line instead.
5. Keep everything else: compliance sentences (exactly one per pair, as now), hooks, account facts, the 3.5% wording, the call line. Re-read every changed message in full before split-messages, and check that every pair still has a number the gate recognises.

## Per person


### Michael Spiteri · spiterimichael · Legal & General · technical-integration
- M1 product sentence shares a 10-word run with 5+ colleagues at Legal & General («scales weight estimate and a flag when the gap to»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Tariq Surty · tariq-surty-8911101 · Legal & General · technical-integration
- M1 product sentence shares a 10-word run with 5+ colleagues at Legal & General («from the declared height and a flag when the gap»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Jenny Reeve · jennyreeve · Legal & General · referral
- M1 product sentence shares a 10-word run with 5+ colleagues at Legal & General («in the application a smart scales weight estimate and a»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Gary M. · gary-m-3b7b913b · Legal & General · referral
- M1 product sentence shares a 10-word run with 5+ colleagues at Legal & General («scales weight estimate with a flag when the gap to»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Steve Davis · sdavis2 · Legal & General · referral
- M1 product sentence shares a 10-word run with 5+ colleagues at Legal & General («height and a flag at a threshold the insurer sets»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Cris Saunders · crissaunders · Legal & General · referral
- M1 product sentence shares a 10-word run with 5+ colleagues at Legal & General («a flag when the gap to declared weight crosses a»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Nicki Plews · nicki-plews-b037aa2b · Legal & General · proposition
- M1 product sentence shares a 10-word run with 5+ colleagues at Legal & General («scales weight estimate and a flag when the gap to»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Sara Denyer · sara-denyer-b81a2a92 · Legal & General · underwriting
- M1 product sentence shares a 10-word run with 5+ colleagues at Legal & General («height and a flag at a threshold the insurer sets»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Jenni Phillips · jenni-phillips-98892a24 · Legal & General · underwriting
- M1 product sentence shares a 10-word run with 5+ colleagues at Legal & General («a flag when the gap to declared weight crosses a»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### John Redmond · john-redmond-884597a · Legal & General · underwriting
- M1 product sentence shares a 10-word run with 5+ colleagues at Legal & General («a flag when the gap to declared weight crosses a»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### David Banks · david-banks-9b750391 · Legal & General · underwriting
- M1 product sentence shares a 10-word run with 5+ colleagues at Legal & General («a flag when the gap to declared weight crosses a»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Brian Kemp · brian-kemp-0467b898 · Legal & General · underwriting
- M1 product sentence shares a 10-word run with 5+ colleagues at Legal & General («a flag when the gap to declared weight crosses a»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Tarun Gupta · drtarungupta · Legal & General · medical
- M1 product sentence shares a 10-word run with 5+ colleagues at Legal & General («from the declared height and a flag when the gap»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Nicky McRae · nicky-mcrae-a4a3b5206 · Legal & General · underwriting
- M1 product sentence shares a 10-word run with 5+ colleagues at Legal & General («from the declared height and a flag when the gap»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Pippa Barber · pippa-barber-nee-keefe-487b64b6 · Legal & General · proposition
- M1 product sentence shares a 10-word run with 5+ colleagues at Legal & General («the application a smart scales weight estimate and a flag»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.
- Coordinator read: "The scan takes under 45 seconds from the photos to structured results." rewrites the fixed speed line: use it exactly as its own plain sentence, e.g. built on "under 45 seconds from the photos to structured results", or drop it.

### Hai Luc · hai-luc-67306367 · Legal & General · proposition
- M1 product sentence shares a 10-word run with 5+ colleagues at Legal & General («height and a flag at a threshold the insurer sets»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.
- Coordinator read: M2 "compared with later outcomes" points at claims: drop the later-outcomes idea.
