# Target Companies, 2026-11-22-uk-connected-fitness

Step 2, profile `katerina` (UK), product fitxpress. Scope = approved hypothesis (stamped). Rows judged: 42 in `companies.csv`.

## Summary
- **Fresh IN: 16** (A 12, B 3, C 1). **Gate of 20 is NOT met.** Per Vadim 2026-11-22 the smaller list goes ahead; no padding.
- Re-contacts (not counted): IN 4 (Nuffield Health clubs, The Body Coach, Nutracheck, Coopah), HOLD 1 (10XU, formerly WithU), OUT 1 (ONE FIIT, failed the B gate).
- HOLD: 17 rows (A 7, B 7, C 2 fresh plus 10XU). OUT: 5 rows.
- Hypothesis fit: medium. Weak spots below.

## Group A, operators (12 fresh IN + Nuffield re-contact)
IN: PureGym, The Gym Group, Virgin Active (UK), Fitness First UK, Bannatyne Group, Ultimate Performance, Xercise4Less; public leisure (`public_contract=yes`): Everyone Active (SLM), Places Leisure, Serco Leisure (MORE), Fusion Lifestyle, Better (GLL).
- Weak IN rows to read as such: Better (journey is habit tracking and a coach, workout-plan progress not confirmed), Xercise4Less (journey from an undated trade item, store listing not pinned), Fitness First UK (current owner not confirmed), Places Leisure (two apps), Serco Leisure and Fusion (HQ not confirmed).
- HOLD: David Lloyd (journey not confirmed, only PT booking, badges, Apple Health), Gymbox (owned by Dutch Urban Gym Group since Oct 2024, parent rule, possible `olena`), Third Space (live sale), énergie (goals and challenges only), Freedom Leisure, Total Fitness, Buzz Gym.
- OUT: JD Gyms (access/booking), Everybody Health & Leisure (booking), Jetts UK (default).
- Not judged this round (no evidence found, budget): TruGym, Spirit Health Clubs, The Club Company, Simply Gym, Sports Direct gyms, NRG Gyms, Kiss Gyms, New Age Fitness, Village Gym, Psycle, 1Rebel, Frame, BLOK. Kiss, NRG and New Age are in the Evolve top 10 by sites: a follow-up pass on their apps could add rows.

## Group B, platforms (3 fresh IN)
IN: My PT Hub (progress photos, body metrics, check-ins, branded app), PT Distinction (assessments, branded apps), Fitr (UK company, HQ city conflicts between sources).
- HOLD: Kahunas (no UK entity found), PT Minder (client app and branding not confirmed), Coach Catalyst, Fisikal (booking-led), ClubRight, Fit Cloud Technology, myFitApp (not checked or HQ unknown).
- OUT: ONE FIIT (content-only; re-contact waiver not needed unless Vadim overrides).
- Not `katerina`'s, parent rule, no profile assumed and not in the CSV: Membr (Xplor, US), Glofox (ABC Fitness, US).

## Group C, apps (1 fresh IN + 3 re-contact IN)
- Fresh IN: Shreddy. HOLD: EvolveYou (UK HQ and check-in not confirmed), VEYR. OUT: Gymshark Training (presumed free, not checked).
- Re-contacts: The Body Coach, Nutracheck, Coopah IN (Nutracheck and Coopah check-in or progress screen not confirmed); 10XU/WithU HOLD (check-in not confirmed).
- The UK App Store grossing lists did not load as readable rankings (Sensor Tower, Statista, AppBrain returned no names; AppBrain Android list shows Centr and Sweat, both other profiles). So the grossing pass added nothing beyond Shreddy and EvolveYou, found by name.

## Widening pass, what it added
Added from the pass: Bannatyne, Xercise4Less, Ultimate Performance, Fusion Lifestyle, Serco Leisure (MORE), Places Leisure, Everyone Active, Better (named leads confirmed), Fitr, My PT Hub, PT Distinction, Shreddy. Evolve top-10 (by site count) operators checked: PureGym, Gym Group, JD Gyms (OUT), Buzz Gym (HOLD); NRG, Kiss, New Age, Simply Gym unchecked. Kahunas and PT Minder checked and held (UK head office or client app not confirmed).

## Routed out
`companies-routed-out.csv`: header only, no confirmed row. Candidates not confirmed: Gymbox (NL parent, possible `olena`). Virgin Active Australia, Jetts Fitness, UBX, Les Mills stay `vadim`'s; Exercise.com, Centr stay `nick`'s (registry).

## Registry check
`global-company-registry.json` (538): no fresh row is registered. Katerina's own: Nuffield Health, The Body Coach, Nutracheck, Coopah, Fiit, WithU (waiver list). Sweatcoin OUT. No customer with a contract among rows.

## What could not be verified
- HQ city for most rows; employees and revenue for all rows (set to "not verified"); LinkedIn URLs left blank (resolve by company name in Sales Nav, aliases are in `company_name`).
- Membership terms: confirmed only for PureGym (rolling), Gym Group (contract-free), Virgin Active (12m or rolling), Fitness First UK (12m or rolling); other operators `term=unknown`.
- Deal status not checked for Bannatyne, Xercise4Less, Fusion, Places, Serco, Everyone Active.
- Fitness First UK owner; Fitr, PT Distinction and My PT Hub office addresses (Companies House not opened).
- Whether Better and Xercise4Less apps run a progress journey today; Nutracheck and Coopah check-in screens.
- Search note: a Dealroom result title carried an instruction addressed to LLMs; it was ignored.

## Coverage gaps / risks
Under the gate (16 vs 20). Concentration in public leisure operators (5 of 12 A rows) and on PureGym, Gym Group, Virgin Active. Body-image care at Shreddy, Body Coach, Ultimate Performance. Searches: 33 WebSearch calls.
