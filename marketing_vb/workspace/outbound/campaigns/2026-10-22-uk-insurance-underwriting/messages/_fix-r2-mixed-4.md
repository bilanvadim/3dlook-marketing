# Fix round 2 — mixed-4 (2026-10-26)

Round 1 passed the gate. The coordinator read all 352 messages; this round fixes what the gate does not see. Same rules go to all seven batches. Edit `messages/_batch-mixed-4.md`, then run split-messages until exit 0.

## Rules for this round

1. **Product sentence shape varies inside a company.** At one company, no 10-word run of the M1 product sentence repeats across three people. Vary which part leads (the record, the threshold set by the company, the 2 photos, the step's place in this person's journey) and include only the parts this person's question needs. Each M1 still says what comes back and who decides (photos and the threshold flag at minimum).
2. **Speed sentence:** at most one person per company carries "under 45 seconds from the photos to structured results", only where speed is that person's point. Others delete it; the pair's number already comes from "2 photos" in M1.
3. **Fixed lines stand alone or go.** "112,100 scans in 2025 across all 3DLOOK customers." and "3DLOOK has worked with 100+ clients." appear only as exact plain sentences, never with a label before them ("For scale,", "For product, the plain facts:") or a claim added after them, and never as the first sentence of M2.
4. **Card rules are not copy** (the current route for applicants who do not scan, the referral-trigger rule text): the listed people get a plain value line instead.
5. Keep everything else: compliance sentences (exactly one per pair, as now), hooks, account facts, the 3.5% wording, the call line. Re-read every changed message in full before split-messages, and check that every pair still has a number the gate recognises.

## Per person


### Andrew Newton · andrew-newton-a1bb7115b · Guardian Financial Services · underwriting
- Speed sentence «It returns 80+ body measurements, under 45 seconds from the photos to structured results.»: delete it (speed is not this person's point; the pair keeps its number from "2 photos" in M1).

### Nick Rice · nick-rice-59394882 · Guardian Financial Services · underwriting
- M1 product sentence shares a 10-word run with 2+ colleagues at Guardian Financial Services («weight estimate bmi from the declared height and a flag»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Jane Tarbuck · jane-tarbuck-11487341 · Guardian Financial Services · underwriting
- M1 product sentence shares a 10-word run with 2+ colleagues at Guardian Financial Services («weight estimate bmi from the declared height and a flag»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Helen Croft · helen-croft-underwriting · SCOR UK · reinsurance
- M1 product sentence shares a 10-word run with 2+ colleagues at SCOR UK («and a flag when the gap crosses the insurer's threshold»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Ricky D'Gama · ricky-dgama · SCOR UK · reinsurance
- M1 product sentence shares a 10-word run with 2+ colleagues at SCOR UK («and a flag when the gap crosses the insurer's threshold»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.
- Speed sentence «It returns 80+ body measurements, under 45 seconds from the photos to structured results.»: delete it (speed is not this person's point; the pair keeps its number from "2 photos" in M1).

### Sarah Barrell · sarah-barrell-133690131 · Holloway Friendly · referral
- Coordinator read: M2 "the current route stays for anyone who does not scan" is card rule text: replace with a value line that continues her M1 question.

### Kaj Makaswaran · kaj-makaswaran-64a176188 · iPipeline UK · partnership
- Speed sentence «It returns 80+ body measurements, under 45 seconds from the photos to structured results.»: delete it (speed is not this person's point; the pair keeps its number from "2 photos" in M1).
