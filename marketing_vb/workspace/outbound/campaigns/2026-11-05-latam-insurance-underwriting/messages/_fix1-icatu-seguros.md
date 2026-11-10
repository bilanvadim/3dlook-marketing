# Fix round 1 for batch icatu-seguros (coordinator, 2026-11-10)

Edit ONLY the sentences named below, in the per-person files messages/<person_id>.md (or your batch file, then split again). Every other sentence stays as it is.
The card's rules still hold for every edit: compliance line verbatim in M2, calendar link last with the call offer next to it, no «so», «let», «plus», no call length, 3.5% only where the card allows it.
A rewrite must not reuse another stock form: after a phrase is removed, writers tend to converge on the next one. Vary structure, not only words, and check your own batch for the new phrase before you finish.
When done, run `scripts/outbound_pack.py split-messages` (or `check-messages --campaign 2026-11-05-latam-insurance-underwriting`) until it exits 0, then reply with the list of person_ids you changed.

## bernardocarneiro (Bernardo Carneiro, Icatu Seguros, technical-integration)
- M2: delete «3DLOOK has worked with 100+ clients.» (the scale line goes only to CEOs and heads of a business; this pair already has its number in M1).

## eduardo-correa-6a5bb89 (Eduardo Correa, Icatu Seguros, referral)
- M2: delete «3DLOOK has worked with 100+ clients.» (the scale line goes only to CEOs and heads of a business; this pair already has its number in M1). Message 2 is then nearly empty: write one value line that continues this person's own Message 1 question (their lane's Message 2 value in the card), in new words.

## luciana-bastos-83b96a23 (Luciana Bastos, Icatu Seguros, proposition)
- M1: «Saw the news…» is the banned «Saw your post» family. Open with the fact itself, plainly.

## iagoduartesimões (Iago Duarte Simões, Icatu Seguros, referral)
- M1: «The step is 2 photos on the applicant's phone, a weight estimate and a flag above a threshold Icatu sets, as one record through the API.» uses «flag above a threshold», which 13 of 21 people at Icatu Seguros already carry (quota 4). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.

## antonio-carlos-almeida-braga-656229135 (Antonio Carlos Almeida Braga, Icatu Seguros, proposition)
- M1: «Those cases could carry 2 photos with a weight estimate and a flag above a threshold Icatu sets.» uses «flag above a threshold», which 13 of 21 people at Icatu Seguros already carry (quota 4). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.

## sergio-egidio-31321b170 (Sergio Egidio, Icatu Seguros, referral)
- M2: delete «112,100 scans in 2025 across all 3DLOOK customers.» (the scale line goes only to CEOs and heads of a business; this pair already has its number in M1).
- M1: «Our answer is a step of 2 photos with a weight estimate and a flag above a threshold Icatu sets.» uses «flag above a threshold», which 13 of 21 people at Icatu Seguros already carry (quota 4). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.

## marcela-gueiros (Marcela Gueiros, Icatu Seguros, proposition)
- M2: delete «112,100 scans in 2025 across all 3DLOOK customers.» (the scale line goes only to CEOs and heads of a business; this pair already has its number in M1).
- M1: «It adds a Smart Scales weight estimate, BMI from the declared height and a flag above Icatu's threshold, and returns one timestamped record to the portal through the API.» uses «BMI from the declared height», which 8 of 21 people at Icatu Seguros already carry (quota 4). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.

## leonardohijino (Leonardo Hijino, Icatu Seguros, proposition)
- M2: delete «3DLOOK has worked with 100+ clients.» (the scale line goes only to CEOs and heads of a business; this pair already has its number in M1).
- M1: «For cases where nobody measures the applicant, 2 photos taken in the application give a weight estimate and a flag above a threshold Icatu sets, delivered as a timestamped record via API.» uses «flag above a threshold», which 13 of 21 people at Icatu Seguros already carry (quota 4). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.

## l%c3%adgia-abreu-6871b9147 (Ligia Abreu, Icatu Seguros, proposition)
- M1: «FitXpress takes 2 photos in the application and returns BMI from the declared height, a weight estimate and a flag above a threshold Icatu sets.» uses «flag above a threshold», which 13 of 21 people at Icatu Seguros already carry (quota 4). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.
- M1: «FitXpress takes 2 photos in the application and returns BMI from the declared height, a weight estimate and a flag above a threshold Icatu sets.» uses «BMI from the declared height», which 8 of 21 people at Icatu Seguros already carry (quota 4). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.

## jimmymonte (Jimmy Monte, Icatu Seguros, underwriting)
- M1: «A Smart Scales weight estimate comes back with a flag above a threshold Icatu sets, as a timestamped record through the API.» uses «flag above a threshold», which 13 of 21 people at Icatu Seguros already carry (quota 4). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.

## humberto-sardenberg (Humberto Sardenberg, Icatu Seguros, proposition)
- M1: «FitXpress returns a Smart Scales weight estimate, BMI from the declared height and a flag above a threshold Icatu sets, through an API or SDK.» uses «flag above a threshold», which 13 of 21 people at Icatu Seguros already carry (quota 4). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.
- M1: «FitXpress returns a Smart Scales weight estimate, BMI from the declared height and a flag above a threshold Icatu sets, through an API or SDK.» uses «BMI from the declared height», which 8 of 21 people at Icatu Seguros already carry (quota 4). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.

## ingrid-pereira-39a8882b (Ingrid Pereira, Icatu Seguros, proposition)
- M1: «FitXpress is a step brokers could offer inside the life application: 2 photos, a Smart Scales weight estimate, BMI from the declared height, and a flag above a threshold Icatu sets.» uses «flag above a threshold», which 13 of 21 people at Icatu Seguros already carry (quota 4). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.
- M1: «FitXpress is a step brokers could offer inside the life application: 2 photos, a Smart Scales weight estimate, BMI from the declared height, and a flag above a threshold Icatu sets.» uses «BMI from the declared height», which 8 of 21 people at Icatu Seguros already carry (quota 4). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.

## bernardo-dieckmann-8a399678 (Bernardo Dieckmann, Icatu Seguros, underwriting)
- M2: delete «112,100 scans in 2025 across all 3DLOOK customers.» (the scale line goes only to CEOs and heads of a business; this pair already has its number in M1).
- M1: «Our step puts 2 photos into those cases and returns a weight estimate with a flag above a threshold Icatu sets.» uses «flag above a threshold», which 13 of 21 people at Icatu Seguros already carry (quota 4). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.
- M1: «The case file gets a timestamped record through the API.» uses «timestamped record by/through the API or SDK», which 5 of 21 people at Icatu Seguros already carry (quota 4). Rewrite this sentence for this person with a different structure and other words; keep its facts and the rules.
