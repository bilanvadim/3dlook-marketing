# Fix round 1 for batch mixed-3 (coordinator, 2026-11-10)

Edit ONLY the sentences named below, in the per-person files messages/<person_id>.md (or your batch file, then split again). Every other sentence stays as it is.
The card's rules still hold for every edit: compliance line verbatim in M2, calendar link last with the call offer next to it, no «so», «let», «plus», no call length, 3.5% only where the card allows it.
A rewrite must not reuse another stock form: after a phrase is removed, writers tend to converge on the next one. Vary structure, not only words, and check your own batch for the new phrase before you finish.
When done, run `scripts/outbound_pack.py split-messages` (or `check-messages --campaign 2026-11-05-latam-insurance-underwriting`) until it exits 0, then reply with the list of person_ids you changed.

## gmfentanez1402 (Gabriela Martinez Fentanez, Swiss Re Mexico, reinsurance)
- M2: the value line is one speed sentence; give a reinsurance value (a shadow evaluation her team could run with one client, or how a flag sits beside Magnum Go's questions), worded differently from Paulina's and Juliana's.

## antonioferramd (Antonio F, Swiss Re Mexico, medical)
- M1: «It would raise a flag when the gap to the declared weight crosses a threshold set well above its error, as one timestamped record by API.» uses «timestamped record by/through the API or SDK», which 4 of 4 people at Swiss Re already carry (quota 2). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.

## franciscomajos (Francisco Majos, SCOR Mexico, reinsurance)
- M2: delete «For scale, 3DLOOK processed 112,100 scans in 2025 across all 3DLOOK customers.» (the scale line goes only to CEOs and heads of a business; this pair already has its number in M1).
- M2: scale + speed is not a value line for him; give the reinsurance value tied to his M1 question (what a client conversation could start from), worded unlike Yolanda's.

## yolanda-gutierrez-b674b717b (Yolanda Gutierrez, SCOR Mexico, reinsurance)
- M1: «FitXpress adds 2 photos to a life declaration case, with a Smart Scales weight estimate and a flag where the gap to the declared weight crosses the insurer's threshold.» uses «Smart Scales weight estimate and/with a flag», which 4 of 4 people at SCOR already carry (quota 2). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.

## rafael-zimmer-b8268751 (Rafael Zimmer, SCOR Brasil, referral)
- M2: delete «3DLOOK has worked with 100+ clients.» (the scale line goes only to CEOs and heads of a business; this pair already has its number in M1).
- M1: «2 photos in the application give a Smart Scales weight estimate and a flag when the gap crosses a threshold the insurer sets, as one timestamped record through the API.» uses «Smart Scales weight estimate and/with a flag», which 4 of 4 people at SCOR already carry (quota 2). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.
- M1: drop «Separately,»; join the hook to the product line in a plain sentence.
- M2: «What an insurer would receive is one timestamped record per applicant…» is a near-twin of João Caproni's and Juliana Alves's M2; rewrite around his own question.

## julianasobredaalves (Juliana Alves, Swiss Re Brasil, reinsurance)
- M1: «FitXpress adds 2 photos: a Smart Scales weight estimate and a flag when the gap crosses a threshold the insurer sets, as one timestamped record through the API or SDK.» uses «flag when the gap», which 3 of 4 people at Swiss Re already carry (quota 2). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.
- M1: «FitXpress adds 2 photos: a Smart Scales weight estimate and a flag when the gap crosses a threshold the insurer sets, as one timestamped record through the API or SDK.» uses «Smart Scales weight estimate and/with a flag», which 3 of 4 people at Swiss Re already carry (quota 2). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.
- M1: «FitXpress adds 2 photos: a Smart Scales weight estimate and a flag when the gap crosses a threshold the insurer sets, as one timestamped record through the API or SDK.» uses «timestamped record by/through the API or SDK», which 4 of 4 people at Swiss Re already carry (quota 2). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.

## joão-caproni-1ba34189 (João Caproni, Hannover Re Brasil, referral)
- M1: «2 photos in the application give a Smart Scales weight estimate and a flag when the gap crosses a threshold the insurer sets, as one timestamped record through an API or SDK.» uses «timestamped record by/through the API or SDK», which 3 of 3 people at Hannover Re already carry (quota 2). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.
- M2: «one timestamped record per applicant … 100+ clients» is a near-twin of Rafael Zimmer's and Juliana Alves's M2; rewrite his value line around his own question (where a Brazilian life insurer's question lands at Hannover Re).
