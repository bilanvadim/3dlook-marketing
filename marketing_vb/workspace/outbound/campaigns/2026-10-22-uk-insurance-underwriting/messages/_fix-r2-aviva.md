# Fix round 2 — aviva (2026-10-26)

Round 1 passed the gate. The coordinator read all 352 messages; this round fixes what the gate does not see. Same rules go to all seven batches. Edit `messages/_batch-aviva.md`, then run split-messages until exit 0.

## Rules for this round

1. **Product sentence shape varies inside a company.** At one company, no 10-word run of the M1 product sentence repeats across three people. Vary which part leads (the record, the threshold set by the company, the 2 photos, the step's place in this person's journey) and include only the parts this person's question needs. Each M1 still says what comes back and who decides (photos and the threshold flag at minimum).
2. **Speed sentence:** at most one person per company carries "under 45 seconds from the photos to structured results", only where speed is that person's point. Others delete it; the pair's number already comes from "2 photos" in M1.
3. **Fixed lines stand alone or go.** "112,100 scans in 2025 across all 3DLOOK customers." and "3DLOOK has worked with 100+ clients." appear only as exact plain sentences, never with a label before them ("For scale,", "For product, the plain facts:") or a claim added after them, and never as the first sentence of M2.
4. **Card rules are not copy** (the current route for applicants who do not scan, the referral-trigger rule text): the listed people get a plain value line instead.
5. Keep everything else: compliance sentences (exactly one per pair, as now), hooks, account facts, the 3.5% wording, the call line. Re-read every changed message in full before split-messages, and check that every pair still has a number the gate recognises.

## Per person


### Manju Devi · manjudevinatarajan · Aviva · referral
- Coordinator read: "FitXpress is a step of 2 photos." is awkward and shared with Victoria Francis: plain product sentence in its own shape.

### Lili Burdass · liliburdass · Aviva · proposition
- Coordinator read: "FitXpress, the step we offer, takes 2 photos" is awkward: plain product sentence.

### Joel Manstoff · joel-manstoff · Aviva · referral
- Coordinator read: "FitXpress is 2 photos, …" is awkward: the product takes photos, it is not photos.

### Sue Hendry · sue-hendry-a8415a17 · Aviva · underwriting
- The 3.5% sentence opens like a colleague's at Aviva («smart scales has approximately…»): keep "approximately 3.5% mean absolute error under evaluated conditions" and "not a scale reading" in one sentence, and frame it differently.

### Victoria Francis · victoria-francis-09949480 · Aviva · proposition
- Coordinator read: "FitXpress is a step of 2 photos." is awkward and shared with Manju Devi: plain product sentence in its own shape.
