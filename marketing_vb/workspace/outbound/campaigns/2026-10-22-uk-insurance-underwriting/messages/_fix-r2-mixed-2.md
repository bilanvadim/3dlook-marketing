# Fix round 2 — mixed-2 (2026-10-26)

Round 1 passed the gate. The coordinator read all 352 messages; this round fixes what the gate does not see. Same rules go to all seven batches. Edit `messages/_batch-mixed-2.md`, then run split-messages until exit 0.

## Rules for this round

1. **Product sentence shape varies inside a company.** At one company, no 10-word run of the M1 product sentence repeats across three people. Vary which part leads (the record, the threshold set by the company, the 2 photos, the step's place in this person's journey) and include only the parts this person's question needs. Each M1 still says what comes back and who decides (photos and the threshold flag at minimum).
2. **Speed sentence:** at most one person per company carries "under 45 seconds from the photos to structured results", only where speed is that person's point. Others delete it; the pair's number already comes from "2 photos" in M1.
3. **Fixed lines stand alone or go.** "112,100 scans in 2025 across all 3DLOOK customers." and "3DLOOK has worked with 100+ clients." appear only as exact plain sentences, never with a label before them ("For scale,", "For product, the plain facts:") or a claim added after them, and never as the first sentence of M2.
4. **Card rules are not copy** (the current route for applicants who do not scan, the referral-trigger rule text): the listed people get a plain value line instead.
5. Keep everything else: compliance sentences (exactly one per pair, as now), hooks, account facts, the 3.5% wording, the call line. Re-read every changed message in full before split-messages, and check that every pair still has a number the gate recognises.

## Per person


### Laura Vaughan · laura-vaughan-b7ba132b2 · Scottish Widows · proposition
- M1 product sentence shares a 10-word run with 3+ colleagues at Scottish Widows («a smart scales weight estimate and bmi from the declared»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.
- Coordinator read: "FitXpress is 2 photos taken in the application, …" is awkward: the product takes photos, it is not photos.

### Eric Walker · eric-walker-4471a7b2 · Scottish Widows · underwriting
- M1 product sentence shares a 10-word run with 3+ colleagues at Scottish Widows («a smart scales weight estimate and bmi from the declared»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Paul Young · paul-young-708558b0 · Scottish Widows · underwriting
- M1 product sentence shares a 10-word run with 3+ colleagues at Scottish Widows («a smart scales weight estimate and bmi from the declared»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Denise Bates · denise-bates-06945338 · Swiss Re UK · reinsurance
- M1 product sentence shares a 10-word run with 2+ colleagues at Swiss Re UK («a smart scales weight estimate and bmi from the declared»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.
- The 3.5% sentence opens like a colleague's at Swiss Re UK («smart scales has approximately…»): keep "approximately 3.5% mean absolute error under evaluated conditions" and "not a scale reading" in one sentence, and frame it differently.

### Dave Evans · dave-evans-bb20a920 · Swiss Re UK · technical-integration
- Coordinator read: "The scan takes 2 photos, deleted after processing or within 30 days, per the insurer's policy." is garbled: write the approved form "Photos are deleted after processing or within 30 days per the insurer's policy, retained photos are blurred and faces are obscured at capture."

### Deborah Smith · drdeborahasmith · Swiss Re UK · medical
- M1 product sentence shares a 10-word run with 2+ colleagues at Swiss Re UK («a smart scales weight estimate and bmi from the declared»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.
- The 3.5% sentence opens like a colleague's at Swiss Re UK («smart scales has approximately…»): keep "approximately 3.5% mean absolute error under evaluated conditions" and "not a scale reading" in one sentence, and frame it differently.

### Natalie Kelly · natalie-kelly-447331a · Swiss Re UK · reinsurance
- The 3.5% sentence opens like a colleague's at Swiss Re UK («smart scales has approximately…»): keep "approximately 3.5% mean absolute error under evaluated conditions" and "not a scale reading" in one sentence, and frame it differently.

### Kylie Irwin · kylie-irwin-385398154 · UnderwriteMe · partnership
- Coordinator read: "FitXpress is 2 photos in the application, …" is awkward: the product takes photos, it is not photos.

### Will Miller · will-miller-78139133 · UnderwriteMe · technical-integration
- Coordinator read: Same garbled photo-deletion sentence as above: use the approved form.

### Rebecca McGeoch · rebecca-mcgeoch-186807134 · Zurich UK · technical-integration
- Coordinator read: Same garbled photo-deletion sentence as above: use the approved form.

### Sabrina Lane · sabrina-lane-406a0b65 · Zurich UK · underwriting
- M1 product sentence shares a 10-word run with 2+ colleagues at Zurich UK («a smart scales weight estimate and bmi from the declared»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.

### Scott Reid · scott-reid-950a3410 · Zurich UK · proposition
- M1 product sentence shares a 10-word run with 2+ colleagues at Zurich UK («a smart scales weight estimate and bmi from the declared»): rebuild it in a different shape (lead with a different part: the record, the threshold, the photos, the step in their journey), and leave out parts their question does not need.
