---
product: fitxpress
profile: vadim
market: Australia
created: 2026-10-11
status: draft
use_case: fx-digital-fitness
cap_per_group: 50
referral_call: yes
banned_terms: [Erakulis, Zing Coach, Verv, Yazen, UK Meds, Healthyr, Safariland, Burlington, Jim's Formal Wear, Generation Tux, Tailoor, Redthread, Prism, Bodygram, Size Stream, Evolt, Advanced Health Intelligence, MyFiziq, mPort, InBody, Tanita, Withings, Styku, Fit3D, Seca, Bodymapp, ShapeScale, Technogym, HYPOXI, Xponential, Lift Brands, Quadrant, Franchise Equity Partners, Brait, Wesfarmers, Purpose Brands, AIA Vitality, Medibank, Bupa, HCF, Ozempic, Wegovy, Mounjaro, Saxenda, semaglutide, tirzepatide, HIPAA, GDPR, SOC 2, FDA, TGA, Privacy Act, Privacy Principles, compliant, certified, certification, accredited, clinically validated, clinically proven, verify, verified, verification, eligibility, eligible, fraud, mismatch, self-reported, guesswork, unreliable, inaccurate, error-prone, tape measure, beyond the scale, beyond weight, scale weight, weight alone, weight only, just weight, non-scale, DEXA, DXA, BIA, bioimpedance, visceral, obese, bikini, before and after, before-and-after, burn fat, fat loss, summer body, shred, pregnancy, pregnant, postnatal, NDIS, disability, guarantee, guaranteed, refund, money-back, ROI, royalties, franchise fee, funding, investors, investor, valuation, acquisition, acquired, IPO, buyout, generic figure, never a promise, not a promise, context only, writer note, Circling back, Following up, Saw your post, reconnecting, as promised, BIOSCAN, PXI, Myzone, menopause, perimenopause, money back]
---

# Outbound Hypothesis: 2026-10-11, Australian gym, studio and fitness networks (fixed list, Vadim)

- **Campaign:** `2026-10-11-au-sport-fitness`
- **Owner and sender:** Vadim Bilan, profile `vadim`, market Australia. Every message ends with `Vadim` alone on the last line. **No calendar account:** Message 2 is a short call offer with a soft ask and no link (`outbound-message2-template.md`).
- **Company list: fixed, not researched.** Vadim's closely.io enrichment of a Sales Navigator keyword search ("Au sport", filter in `export-summary.md`), `sales-nav-raw/export-1.csv`: 386 people, 204 groups, every person located in Australia, read with stdlib `csv`. No company-researcher step: step 2 is `companies.csv` (40 rows: 39 IN accounts and Mosh, whose one new person is on HOLD), written from the verdict table and fixed in the QC fix round of 2026-10-11. Person-level notes, earlier contacts and identity checks: `hooks-by-company.md`.
- **ICP:** `icp-detail.md` §8 (Connected & Digital Fitness) is the core: gym, studio and PT networks with their own member apps, fitness apps and B2B fitness software. §4 (Employer wellness) covers Fitness Passport, Ford Health and SiSU Health; §1 (weight loss) covers Mosh (HOLD only).
- **Use-case file:** `use_case: fx-digital-fitness` (the IN majority is clubs, studios and apps: 264 of 283 people). Its "90 days" line, its KPI list and its "Higher LTV via retention" line are not usable as numbers or promises in copy (Rules).
- **Registry, checked 2026-10-11** (`outbound-registry.py check --profile vadim` on the export, written to a scratch file): **8 export people were already messaged from `vadim`** (person-level, FAIL): Belinda Amis Wheaton (Fernwood CEO), Olivia Houston (Fitstop Bundall), Chris Torcasio and Adam Koch (Sweat), all on 2026-08-14; Glenn O'Sullivan, Suren Wickramasinghe, Joanna Wang and Andy Pavalache (Mosh), on 2026-07-27. `export-summary.md` says none of the 386 is personally in a registry: the URLs differ only in their host (`linkedin.com` against `www.linkedin.com`), and `check` normalises them. 46 more rows carry "company already worked from vadim" (Fernwood, Fitstop, Sweat, Mosh, KIC, Hapana): cleared by Vadim's decision of 2026-10-11 for this campaign only. No IN account is a 3DLOOK customer or covered by another profile; Lift Brands and Snap Fitness, added in the fix round, are in no registry (checked 2026-10-11).

> **Read this first.**
> 1. **283 people IN, 3 on HOLD, 100 OUT, 386 in all. 39 accounts IN; `companies.csv` has 40 rows (the 39 and Mosh, HOLD only).** OUT: product-only nutrition, supplement and wellness-product brands 36; in-store supplement retail 13 (Australian Sports Nutrition 7, Mr Vitamins 3, Go Vita 3; offered as a pool in Open question 5); unrelated businesses and name-alikes 8; equipment sale or servicing 7; NovoFit beyond its cap of two 3; single sites without a company page 6; competitor (Evolt) 4; general digital agency (equ) 3; hospital 2; associations 2; already messaged from `vadim` 8; duplicate profiles 6; a name collision 1 (SWEAT); a franchise role behind a three-letter employer cell 1 (BHP). 36+13+8+7+3+6+4+3+2+2+8+6+1+1 = 100.
> 2. **HOLD, not sent by default (3, Open question 3):** Eamon H. (Mosh, until Katerina, who owns the live Mosh thread, says yes), Nikita Fernandes (SiSU Health, Head of Compliance) and Rhys Holleran (Viva Leisure, Chair).
> 3. **Twelve OUT rows join an IN account by name** in `extract-people` and must be failed by name at validation; the three HOLD people join too and are held by name (both lists under the verdict table). The other 88 OUT rows join nothing (checked with the pipeline's own `company_keys` and `shortlist_keys` on 2026-10-11 against the fixed `companies.csv`: 298 export rows join, no key collides between two accounts, all 40 rows route to `vadim`).
> 4. **Registry-waived brands (Vadim, 2026-10-11): 77 people IN.** Fernwood 38, Fitstop 33, Sweat 3, KIC 2, Hapana 1; Mosh 0 IN and 1 HOLD. Person-level exclusion stays: the 8 people above are OUT.
> 5. **Franchise networks dominate.** Fernwood 38, Fitstop 33, Jetts 30, BFT 23, UBX 18, Viva Leisure with Plus Fitness 14, KX Pilates 13, REVL 12: 201 of 283 people are `referral`, mostly unit owners, under standing decision 9 and gated like every other lane (`referral_call: yes`). The nine brands with 9 or more referral people each get their own question topics, and every person gets an anchor in `hooks-by-company.md`.
> 6. **41 people are IN through an alias cell** naming their own other employer (EU precedent: `Indépendant`, `Dsign.`, `Bindinc.`): the 39 alias rows of the verdict table (the first version's summary counted 37) and Mark Grey and Lauren Anliev at Anytime, added in the fix round. Each gets a current-role or identity check (Open question 7).
> 7. **Ownership flags, kept IN on `vadim` by default (Open question 2):** BFT, Planet Fitness Australia, Virgin Active Australia, STRONG Pilates, and Snap Fitness Australia (Lift Brands APAC, whose CEO is based in Australia: moved from OUT in the fix round).
> 8. **In-club scanner overlap (Open question 9):** a competitor's in-club body-composition scanner is offered at Jetts, Genesis, BFT (challenges), Vision Personal Training (studios) and Goodlife (Fitness and Lifestyle Group). Partial overlap: IN by default, and copy never mentions the scanner.
> 9. **Lanes:** `referral` 201, `product` 40, `operations` 14, `technical-integration` 10, `member-experience` 9, `partnerships` 9. Tiers: P1 56, P2 16, P3 10, P4 201. `cap_per_group: 50`; the largest group is Fernwood at 38.
> 10. **What changed in the QC fix round:** see "QC fix round 2026-10-11 (QC 14/20)" near the end.

---

## Vertical

Australian gym, studio and personal-training networks (franchisors and their units), fitness apps, workplace fitness and corporate health programmes, and the software and facility partners that serve gyms.

## Sub-segment

The 39 IN accounts by segment, and Mosh (HOLD only):

- **A. Club and studio networks (franchisor or head office is the buyer):** Fernwood Fitness, Fitstop, Jetts Fitness, BFT, UBX (with the former 12RND clubs), Viva Leisure (Club Lime and Plus Fitness), KX Pilates, REVL Training, Genesis Health + Fitness (Belgravia Health & Fitness), World Gym Australia, The Yard Gym, Fitness and Lifestyle Group, One Playground, Revo Fitness, Anytime Fitness Australia, Planet Fitness Australia, Virgin Active Australia, STRONG Pilates, Fitness Cartel, TotalFusion, FS8, VAURA Pilates, EMF Performance & Fitness Centres, Love Athletica, Snap Fitness Australia (Lift Brands APAC, added in the fix round).
- **B. Personal-training networks (trainer follows a client session to session):** Vision Personal Training, Fitness Enhancement, Fitness Inside Out.
- **C. Fitness apps (consumer):** Sweat, KIC, Move With Us (account name CSB).
- **D. Workplace fitness and health programmes:** Fitness Passport, Ford Health, SiSU Health; and Mosh (digital health, weight loss; its one new person is on HOLD).
- **E. Software, programme and facility partners (partnership ask):** Hapana, Recovr, Les Mills Asia Pacific, NovoFit (capped at its CEO and founding director), Your Reformer. Australian Sports Nutrition left in the fix round: in-store supplement retail is OUT under one rule (Open question 5).

**Size:** no headcount floor (standing decision 1). Revenue is not disclosed by most accounts and is not a FAIL reason on this list.

## Company types in scope: verdict table (one row per export group)

Groups follow `export-summary.md` (company LinkedIn page, or the cell as typed when there is no page). Matching in `extract-people` is on name keys, so collisions are failed by name. **Aliases** are written in `companies.csv` (`Canonical (alias / alias)`); `Plus Fitness 24/7 …` is aliased with `-` for `/` (both forms normalise to one key). Fix round: `Lift Brands` is the alias of the new account Snap Fitness Australia; `Collective Health and Wellness` and `ZENKIN` are aliases of Anytime Fitness Australia, with an identity check; NovoFit lost its alias `The Fitness Generation`; Australian Sports Nutrition is no longer a row. Three-letter cells cannot be aliases (the parser drops them): `UBX` and `BFT` are therefore canonical names, Move With Us sits under the canonical `CSB`, and Rick Coetzee (`BHP`) is OUT. Not aliased on purpose: `Fernwood Fitness Woonona`, `Fitstop Bundall` and `Worldgym australia` (each holds only an OUT duplicate or an already-messaged person), `Moreton bay distributors` (Chris Janke's other profile), `The Fitness Generation` (distributor cap).

| # | Export group (cells) | IN | HOLD | OUT | Account | Lanes | Reason or note |
|---|---|---|---|---|---|---|---|
| 1 | `Fernwood Fitness`, `Fernwood National Office`, `Fernwood Women's Health Club Ballarat`, `Fernwood Women's ... | 23 | 0 | 1 | Fernwood Fitness | referral 22, member-experience 1 | Belinda Amis Wheaton: already messaged from vadim, 2026-08-14-au-digital-fitness; identity check (Binish Mobeen, Fernwood Tuggeranong, Kristy Johnson) |
| 2 | `Fitstop`, `Fitstop South Melbourne` | 17 | 0 | 0 | Fitstop | referral 16, member-experience 1 | identity check (Aurora Gilbert, Shami Sivan, Jesse Malseed, Jamie Biondi, Kelly Wade, Josephine Tuah) |
| 3 | `BFT`, `BFT International`, `Body Fit Training` | 15 | 0 | 0 | BFT | referral 12, product 2, operations 1 | identity check (St Leonards Body Fit Training) |
| 4 | `Jetts Australia` | 12 | 0 | 0 | Jetts Fitness | referral 9, operations 1, product 1, member-experience 1 | identity check (Viran Kumar, Chris Pepper, Jetts Gym Mount Hutton) |
| 5 | `UBX`, `UBX Training` | 10 | 0 | 0 | UBX | referral 6, product 2, operations 1, technical-integration 1 | |
| 6 | `KX Pilates`, `KX Pilates Miami` | 9 | 0 | 0 | KX Pilates | referral 8, product 1 | |
| 7 | `REVL Training` | 8 | 0 | 0 | REVL Training | referral 5, product 3 | |
| 8 | `Vision Personal Training Franchises Australia & New Zealand` | 8 | 0 | 0 | Vision Personal Training | referral 8 | |
| 9 | `Fitness Passport`, `Fitness Passport Pty Ltd` | 7 | 0 | 0 | Fitness Passport | partnerships 3, technical-integration 2, product 2 | |
| 10 | `THE YARD GYM` | 6 | 0 | 0 | The Yard Gym | referral 3, product 2, member-experience 1 | |
| 11 | `BON CHARGE` | 0 | 0 | 6 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 12 | `Viva Leisure` | 4 | 1 | 0 | Viva Leisure | referral 1, operations 1, member-experience 1, technical-integration 1 | HOLD: Rhys Holleran (Chair), high-risk low-yield referral (QC fix round) |
| 13 | `One Playground` | 5 | 0 | 0 | One Playground | product 2, technical-integration 1, operations 1, member-experience 1 | |
| 14 | `Mosh` | 0 | 1 | 4 | Mosh (HOLD only) | - | Eamon H.: HOLD until Katerina, who owns the live Mosh thread, says yes (QC fix round); Glenn O'Sullivan: already messaged from vadim, 2026-07-27-australia-telehealth; Suren Wickramasinghe: already messaged from vadim, 2026-07-27-australia-telehealth; Joanna Wang: already messaged from vadim, 2026-07-27-australia-telehealth; Andy Pavalache: already messaged from vadim, 2026-07-27-australia-telehealth |
| 15 | `Swisse Wellness`, `Swisse Wellness (part of H&H Group)` | 0 | 0 | 5 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 16 | `Sweat` | 3 | 0 | 2 | Sweat | technical-integration 2, product 1 | Chris Torcasio: already messaged from vadim, 2026-08-14-au-digital-fitness; Adam Koch, MAICD: already messaged from vadim, 2026-08-14-au-digital-fitness |
| 17 | `Fitness and Lifestyle Group` | 5 | 0 | 0 | Fitness and Lifestyle Group | technical-integration 2, product 2, member-experience 1 | |
| 18 | `12RND Fitness`, `12RND Fitness Birkdale`, `12RND Fitness Caloundra`, `12RND Fitness Nambour` | 5 | 0 | 0 | UBX | referral 5 | |
| 19 | `Evolt Health`, `Evolt IOH`, `Evolt IoH` | 0 | 0 | 4 | - | | Competitor (Evolt 360 scanner and app) |
| 20 | `NovoFit` | 2 | 0 | 2 | NovoFit | partnerships 2 | Distributor cap (coordinator, QC fix round): CEO Barry McDonald and founding director Adam Lewit IN; Daniel Waide (COO) and Corey Eames-Mayer (Group COO) fail by name |
| 21 | `Australian Sports Nutrition` | 0 | 0 | 4 | - | | In-store supplement retail: OUT under one rule with Australian Sports Nutrition, Mr Vitamins and Go Vita (pool offered in Open question 5) |
| 22 | `Plus Fitness`, `Plus Fitness - Australian Fitness Management` | 4 | 0 | 0 | Viva Leisure | referral 4 | identity check (GH undefined, PF Syd Olympic Park) |
| 23 | `World Gym Australia` | 3 | 0 | 0 | World Gym Australia | product 2, referral 1 | |
| 24 | `Equilibrium`, `equ` | 0 | 0 | 3 | - | | General digital agency, no health or fitness client found (Open question 6) |
| 25 | `Go Vita Distributors Ltd - Australia's Largest Wholesale & Retail Health Store Group`, `Go Vita Group Ltd ... | 0 | 0 | 3 | - | | In-store supplement retail: OUT under one rule with Australian Sports Nutrition, Mr Vitamins and Go Vita (pool offered in Open question 5) |
| 26 | `Your Reformer` | 3 | 0 | 0 | Your Reformer | product 2, operations 1 | |
| 27 | `SiSU Health`, `SiSU Health Group` | 2 | 1 | 0 | SiSU Health | product 1, partnerships 1 | HOLD: Nikita Fernandes (Head of Compliance, quality and regulatory), high-risk low-yield referral (QC fix round) |
| 28 | `Genesis Fitness Clubs` | 3 | 0 | 0 | Genesis Health + Fitness | referral 3 | identity check (Gym Genesis) |
| 29 | `Nutrition Systems` | 0 | 0 | 3 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 30 | `TotalFusion Australia` | 3 | 0 | 0 | TotalFusion | referral 1, operations 1, member-experience 1 | |
| 31 | `VERVE Fitness` | 0 | 0 | 2 | - | | Equipment sale or servicing, no member software here |
| 32 | `KIC` | 2 | 0 | 0 | KIC | technical-integration 1, operations 1 | |
| 33 | `Fitness Cartel Australia`, `Fitness Cartel Australia & New Zealand` | 2 | 0 | 0 | Fitness Cartel | product 1, operations 1 | |
| 34 | `Wellnex Life` | 0 | 0 | 2 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 35 | `Planet Fitness Australia` | 2 | 0 | 0 | Planet Fitness Australia | operations 1, referral 1 | |
| 36 | `Heritage Brands` | 0 | 0 | 2 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 37 | `Essence Group Sydney` | 0 | 0 | 2 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 38 | `sportsmed` | 0 | 0 | 2 | - | | Private orthopaedic hospital (the filter excluded hospitals) |
| 39 | `Mr Vitamins` | 0 | 0 | 2 | - | | In-store supplement retail: OUT under one rule with Australian Sports Nutrition, Mr Vitamins and Go Vita (pool offered in Open question 5) |
| 40 | `VAURA Pilates` | 2 | 0 | 0 | VAURA Pilates | referral 1, operations 1 | |
| 41 | `Gym Services Australia` | 0 | 0 | 2 | - | | Equipment sale or servicing, no member software here |
| 42 | `VIDA GLOW` | 0 | 0 | 2 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 43 | `Advanced Intelligence Pty Ltd` | 0 | 0 | 2 | - | | Unrelated business or name-alike |
| 44 | `FS8` | 2 | 0 | 0 | FS8 | operations 1, product 1 | |
| 45 | `REVL Training Greenslopes` | 1 | 0 | 1 | REVL Training | referral 1 | Bec Kirkup: duplicate profile of Bec Kirkup (bec-kirkup-446844415 stays IN) |
| 46 | `EMF Fitness Centre` | 1 | 0 | 0 | EMF Performance & Fitness Centres | product 1 | |
| 47 | `Fernwood Fitness Yarraville` | 1 | 0 | 0 | Fernwood Fitness | referral 1 | |
| 48 | `Jetts 24 Hour Fitness` | 1 | 0 | 0 | Jetts Fitness | referral 1 | |
| 49 | `UBX Buderim` | 1 | 0 | 0 | UBX | referral 1 | |
| 50 | `DJKK Holdings` | 1 | 0 | 0 | Jetts Fitness | referral 1 | alias for Damien Ng: Director at Jetts Australia on his row |
| 51 | `Myotherapy Association Australia` | 1 | 0 | 0 | BFT | referral 1 | alias for Scott Bumpstead: Owner - BFT Hindmarsh on his row |
| 52 | `Elix'r Health Club` | 0 | 0 | 1 | - | | Single site or freelancer, no company page |
| 53 | `Fitness plus` | 0 | 0 | 1 | - | | Single site or freelancer, no company page |
| 54 | `Joint Accreditation System of Australia and New Zealand (JASANZ)` | 0 | 0 | 1 | - | | Association or non-profit, no buyer |
| 55 | `SQNNSW Innovation Hub` | 1 | 0 | 0 | Fitstop | referral 1 | alias for Bruce McConnel: Business Owner at Fitstop on his row |
| 56 | `Lotic App` | 1 | 0 | 0 | FS8 | referral 1 | alias for Nina Woodhouse: Franchise Owner FS8 (headline) |
| 57 | `Vita Life Sciences` | 0 | 0 | 1 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 58 | `Apex Vitality` | 1 | 0 | 0 | BFT | referral 1 | alias for Philip Grasso: Business Owner at BFT on his row |
| 59 | `BeWell Brands` | 1 | 0 | 0 | Jetts Fitness | product 1 | |
| 60 | `Sierra` | 1 | 0 | 0 | Fitness Passport | referral 1 | alias for Damien Tampling: Board of Directors at Fitness Passport on his row |
| 61 | `Fernwood Woonona` | 1 | 0 | 0 | Fernwood Fitness | referral 1 | |
| 62 | `Jetts Hamilton` | 1 | 0 | 0 | Jetts Fitness | referral 1 | |
| 63 | `Ninja Parc` | 1 | 0 | 0 | Genesis Health + Fitness | operations 1 | alias for John Pirlo: Managing Director - Genesis Fitness Clubs NSW (headline); Ninja Parc is in the Belgravia portfolio |
| 64 | `Mutual Wide Corporation` | 0 | 0 | 1 | - | | Unrelated business or name-alike |
| 65 | `Belgravia Health & Fitness` | 1 | 0 | 0 | Genesis Health + Fitness | product 1 | |
| 66 | `Australian Sports Nutrition` | 0 | 0 | 1 | - | | In-store supplement retail: OUT under one rule with Australian Sports Nutrition, Mr Vitamins and Go Vita (pool offered in Open question 5) |
| 67 | `Ford Health` | 1 | 0 | 0 | Ford Health | product 1 | |
| 68 | `ZIISH (formerly SWIISH)` | 0 | 0 | 1 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 69 | `Vodafone Business Centre Sydney North Shore` | 0 | 0 | 1 | - | | Unrelated business or name-alike |
| 70 | `JC Consulting` | 1 | 0 | 0 | BFT | referral 1 | alias for Jason Clark: Owner - BFT Ponsonby (Auckland) on his row; ex Franchise Sales Director, BFT International |
| 71 | `WelleCo` | 0 | 0 | 1 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 72 | `Health Plus Fitness` | 0 | 0 | 1 | - | | Single site or freelancer, no company page |
| 73 | `Fitness Enhancement & Fit Your Ability Personal Training` | 1 | 0 | 0 | Fitness Enhancement | referral 1 | |
| 74 | `Maintain Technology` | 1 | 0 | 0 | Fitstop | referral 1 | alias for Jonathan Pepper: Fitstop Franchise Director (multi location) on his row |
| 75 | `Life Fitness Australia` | 0 | 0 | 1 | - | | Equipment sale or servicing, no member software here |
| 76 | `Love Athletica` | 1 | 0 | 0 | Love Athletica | product 1 | |
| 77 | `Family Fitness & Playground Equipment` | 0 | 0 | 1 | - | | Equipment sale or servicing, no member software here |
| 78 | `Rhise Performance Nutrition` | 1 | 0 | 0 | REVL Training | referral 1 | alias for Ben Seymour: Franchise Owner at REVL Training on his row |
| 79 | `Lift Brands` | 1 | 0 | 0 | Snap Fitness Australia | product 1 | Chris Caldwell, CEO APAC, based in Australia: IN under the Australian-head-office default (coordinator, QC fix round; Open question 2); never name Lift Brands or Fitstop |
| 80 | `Nutrition Systems` | 0 | 0 | 1 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 81 | `Fernwood Fitness Woonona` | 0 | 0 | 1 | - | | Janet binns: duplicate profile of Janet Binns (janet-binns-97015636 stays IN) |
| 82 | `Fit Your Ability` | 1 | 0 | 0 | Fitness Enhancement | product 1 | |
| 83 | `Fernwood Fitness -Bulleen` | 1 | 0 | 0 | Fernwood Fitness | referral 1 | |
| 84 | `Verve Fitness` | 0 | 0 | 1 | - | | Single site or freelancer, no company page |
| 85 | `Bodyscience Fitness Pty Ltd` | 0 | 0 | 1 | - | | Single site or freelancer, no company page |
| 86 | `Australian Flying Disc Association (AFDA)` | 0 | 0 | 1 | - | | Association or non-profit, no buyer |
| 87 | `Champions Gym` | 0 | 0 | 1 | - | | Single site or freelancer, no company page |
| 88 | `City of Greater Geelong` | 1 | 0 | 0 | Jetts Fitness | referral 1 | alias for Peter Tremain: Franchise Owner at Jetts Australia (headline) |
| 89 | `Fernwood Fitness Carindale` | 1 | 0 | 0 | Fernwood Fitness | referral 1 | |
| 90 | `Genesis Fitness Club Berwick` | 1 | 0 | 0 | Genesis Health + Fitness | referral 1 | |
| 91 | `Fernwood Fitness` | 1 | 0 | 0 | Fernwood Fitness | referral 1 | |
| 92 | `Jetts Fitness Aveley` | 1 | 0 | 0 | Jetts Fitness | referral 1 | identity check (Mel George) |
| 93 | `SWEAT` | 0 | 0 | 1 | - | | Jack Revens: 'Owner, SWEAT': not the Sweat app (sole owner Kayla Itsines since March 2026); name collision |
| 94 | `Advanced Business Technologies - ABT Group` | 1 | 0 | 0 | Fernwood Fitness | referral 1 | alias for Mark M.: Business Owner at Fernwood Fitness on his row |
| 95 | `Fernwood Bendigo` | 1 | 0 | 0 | Fernwood Fitness | referral 1 | |
| 96 | `The Fitness Generation` | 0 | 0 | 1 | - | | Tim Horskins: distributor cap (NovoFit: CEO and founding director only); alias removed, the cell joins nothing |
| 97 | `Bulk Nutrients` | 0 | 0 | 1 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 98 | `Les Mills Asia Pacific` | 1 | 0 | 0 | Les Mills Asia Pacific | partnerships 1 | |
| 99 | `The Yard Gym Deer Park` | 1 | 0 | 0 | The Yard Gym | referral 1 | |
| 100 | `World Gym Australia` | 1 | 0 | 0 | World Gym Australia | referral 1 | |
| 101 | `BXB Technologies Pty Ltd` | 1 | 0 | 0 | KX Pilates | referral 1 | alias for Bruno Gallucci: Franchise Owner at KX Pilates on his row |
| 102 | `Fitstop St Leonards` | 1 | 0 | 0 | Fitstop | referral 1 | identity check (Susie Jackson) |
| 103 | `Fitness Inside Out Pty Ltd` | 1 | 0 | 0 | Fitness Inside Out | product 1 | |
| 104 | `Fitness & Lifestyle Group` | 1 | 0 | 0 | Fitness and Lifestyle Group | partnerships 1 | |
| 105 | `Nutrition Plus Ltd.` | 0 | 0 | 1 | - | | Louise Ormerod: duplicate profile of Louise Ormerod at Juice Plus (row 114, OUT). Nutrition Plus Ltd itself is a children's charity; v1's nutrition-brand label is corrected |
| 106 | `Fitness Enhancement Personal Training Essendon` | 1 | 0 | 0 | Fitness Enhancement | referral 1 | |
| 107 | `Plumbers Co-op` | 0 | 0 | 1 | - | | Unrelated business or name-alike |
| 108 | `Plus Fitness 24/7 Goulburn` | 1 | 0 | 0 | Viva Leisure | referral 1 | |
| 109 | `Plus Fitness 24/7 Rockdale` | 1 | 0 | 0 | Viva Leisure | referral 1 | |
| 110 | `Australian Sports/Nutrition Industries Pty Ltd` | 0 | 0 | 1 | - | | In-store supplement retail: OUT under one rule with Australian Sports Nutrition, Mr Vitamins and Go Vita (pool offered in Open question 5) |
| 111 | `AEC Group Pty Ltd` | 0 | 0 | 1 | - | | Unrelated business or name-alike |
| 112 | `Johnson Health Tech Australia` | 0 | 0 | 1 | - | | Equipment sale or servicing, no member software here |
| 113 | `Genesis Fitness` | 1 | 0 | 0 | Genesis Health + Fitness | referral 1 | |
| 114 | `The Juice Plus Company Australia Pty Ltd` | 0 | 0 | 1 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 115 | `LoanBird` | 1 | 0 | 0 | Fitstop | referral 1 | alias for Jayne V.: Fitstop Business Owner (headline) |
| 116 | `Sangaweech` | 1 | 0 | 0 | Fitstop | referral 1 | alias for Nebojsa Vujic: Fitstop Franchise Owner (headline) |
| 117 | `Revo Fitness` | 1 | 0 | 0 | Revo Fitness | product 1 | |
| 118 | `Baildon Group` | 1 | 0 | 0 | Jetts Fitness | referral 1 | alias for Andrew Baildon OLY: Baildon Group runs Jetts Pacific Pines, Coomera and Pimpama (company About) |
| 119 | `Genesis Fitness Clubs` | 1 | 0 | 0 | Genesis Health + Fitness | referral 1 | identity check (L B) |
| 120 | `Fitstop Caloundra` | 1 | 0 | 0 | Fitstop | referral 1 | |
| 121 | `World Gym Palmerston` | 1 | 0 | 0 | World Gym Australia | referral 1 | |
| 122 | `Australian Sports Nutrition Darlinghurst` | 0 | 0 | 1 | - | | In-store supplement retail: OUT under one rule with Australian Sports Nutrition, Mr Vitamins and Go Vita (pool offered in Open question 5) |
| 123 | `Fitness Enhancement Personal Training castle hill` | 1 | 0 | 0 | Fitness Enhancement | referral 1 | |
| 124 | `Bare & Wilde` | 1 | 0 | 0 | KX Pilates | referral 1 | alias for Kylie Falconer: Franchise Owner at KX Pilates on her row |
| 125 | `Self-employed` | 0 | 0 | 1 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 126 | `Moreton bay distributors` | 0 | 0 | 1 | - | | Chris Janke: duplicate of Chris Janke (Fitstop Cleveland stays IN); this row works at Moreton Bay Distributors |
| 127 | `UBX South Yarra` | 1 | 0 | 0 | UBX | referral 1 | |
| 128 | `CBRE Asia Pacific` | 1 | 0 | 0 | Jetts Fitness | referral 1 | alias for Brendan Robins: Business Owner at Jetts Australia on his row |
| 129 | `Fernwood Shellharbour` | 1 | 0 | 0 | Fernwood Fitness | referral 1 | |
| 130 | `Sports Advisory Partners Australia` | 1 | 0 | 0 | Anytime Fitness Australia | referral 1 | alias for Jordan Smith: Non Executive Director at Collective Wellness Group and Anytime Fitness on his row |
| 131 | `Jetts Rosemeadow` | 1 | 0 | 0 | Jetts Fitness | referral 1 | |
| 132 | `BHP` | 0 | 0 | 1 | - | | Rick Coetzee: current employer BHP; Fitstop role second on his row; a 3-letter cell cannot be aliased |
| 133 | `Fitstop Bundall` | 0 | 0 | 1 | - | | Olivia Houston: already messaged from vadim, 2026-08-14-au-digital-fitness |
| 134 | `BFT Hindmarsh` | 1 | 0 | 0 | BFT | referral 1 | |
| 135 | `Gorilla X Labs` | 1 | 0 | 0 | Viva Leisure | product 1 | alias for Harry Konstantinou: CEO & Managing Director of Viva Leisure (headline) |
| 136 | `Pitch Black Group` | 1 | 0 | 0 | Fitstop | referral 1 | alias for Adam Stevens: Business Owner at Fitstop on his row |
| 137 | `Jetts Ashmore & Helensvale` | 1 | 0 | 0 | Jetts Fitness | referral 1 | |
| 138 | `ZENKIN` | 1 | 0 | 0 | Anytime Fitness Australia | product 1 | alias for Lauren Anliev (Rovers): 'Director at ZENKIN and Collective Wellness CO'; identity check against Collective Wellness Group, Anytime's owner (QC fix round) |
| 139 | `Fernwood Fitness Newstead` | 1 | 0 | 0 | Fernwood Fitness | referral 1 | |
| 140 | `Flair Action Sports & Promotions` | 1 | 0 | 0 | Fitstop | referral 1 | alias for Rhianna Buchanan: Company Owner at Fitstop Lutwyche on her row |
| 141 | `Jetts Fitness` | 1 | 0 | 0 | Jetts Fitness | referral 1 | |
| 142 | `Horizon Property Alliance` | 1 | 0 | 0 | Jetts Fitness | referral 1 | alias for Mike Knights: Business Owner at Jetts Fitness Australia on his row |
| 143 | `Jetts Wanneroo` | 1 | 0 | 0 | Jetts Fitness | referral 1 | |
| 144 | `KX Pilates` | 1 | 0 | 0 | KX Pilates | referral 1 | identity check (KX Pilates Glen Waverley) |
| 145 | `Better Rehab` | 1 | 0 | 0 | Fitstop | referral 1 | alias for Chandell Fretwell: Director and Franchisee at Fitstop on her row |
| 146 | `Fernwood Fitness Camberwell` | 1 | 0 | 0 | Fernwood Fitness | referral 1 | |
| 147 | `Plus Fitness Rockdale` | 0 | 0 | 1 | - | | Thomas Hepburn: duplicate profile of Thomas Hepburn (thomas-hepburn-09084559 stays IN) |
| 148 | `Mr Vitamins` | 0 | 0 | 1 | - | | In-store supplement retail: OUT under one rule with Australian Sports Nutrition, Mr Vitamins and Go Vita (pool offered in Open question 5) |
| 149 | `Best In Travel Group` | 1 | 0 | 0 | Genesis Health + Fitness | referral 1 | alias for Tom Bayford: Director at Genesis Fitness Clubs on his row |
| 150 | `Purgreens AU` | 1 | 0 | 0 | Planet Fitness Australia | product 1 | alias for Danielle Monroy: Managing Director Planet Fitness Australia (headline) |
| 151 | `Jetts Fitness Lynbrook` | 1 | 0 | 0 | Jetts Fitness | referral 1 | |
| 152 | `Plus Fitness 24/7 Kirrawee` | 1 | 0 | 0 | Viva Leisure | referral 1 | |
| 153 | `Fernwood Fitness Miranda & Kirrawee` | 1 | 0 | 0 | Fernwood Fitness | referral 1 | |
| 154 | `Fitstop Engadine` | 1 | 0 | 0 | Fitstop | referral 1 | |
| 155 | `Worldgym australia` | 0 | 0 | 1 | - | | Jonathan Davie: duplicate profile of Jon Davie (jon-davie-70660122 stays IN) |
| 156 | `Jetts Fitness St Leonards` | 1 | 0 | 0 | Jetts Fitness | referral 1 | identity check (Jetts St Leonards) |
| 157 | `Hapana` | 1 | 0 | 0 | Hapana | referral 1 | |
| 158 | `Vitable` | 0 | 0 | 1 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 159 | `YOUNG AGAIN BIOCEUTICALS` | 0 | 0 | 1 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 160 | `Coles` | 1 | 0 | 0 | BFT | referral 1 | alias for Kristy Ellis: Business Owner at BFT on her row |
| 161 | `株式会社アールティソリューションズ` | 0 | 0 | 1 | - | | Unrelated business or name-alike |
| 162 | `Genesis Fitness Club Charlestown` | 1 | 0 | 0 | Genesis Health + Fitness | referral 1 | |
| 163 | `Fitstop Slacks Creek` | 1 | 0 | 0 | Fitstop | referral 1 | |
| 164 | `fitstop morningside` | 1 | 0 | 0 | Fitstop | referral 1 | |
| 165 | `Anytime Fitness Australia` | 1 | 0 | 0 | Anytime Fitness Australia | product 1 | |
| 166 | `BFT concord` | 1 | 0 | 0 | BFT | referral 1 | |
| 167 | `Macro Mike` | 0 | 0 | 1 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 168 | `The Yard Gym North Lakes` | 1 | 0 | 0 | The Yard Gym | referral 1 | |
| 169 | `ECO-SITE` | 1 | 0 | 0 | UBX | referral 1 | alias for Levi Greenwood: Director at UBX Australia on his row |
| 170 | `STRONG Pilates` | 1 | 0 | 0 | STRONG Pilates | referral 1 | |
| 171 | `recovr` | 1 | 0 | 0 | Recovr | partnerships 1 | |
| 172 | `Dawghouse` | 1 | 0 | 0 | BFT | referral 1 | alias for Anthony Hoang: Owner and Studio Manager at BFT on his row |
| 173 | `Body Science International Pty Ltd` | 0 | 0 | 1 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 174 | `VPA Australia` | 0 | 0 | 1 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 175 | `Fitness Ventures` | 1 | 0 | 0 | World Gym Australia | referral 1 | alias for Mitch Hannam: Director at World Gym Maitland on his row |
| 176 | `Collective Health and Wellness` | 1 | 0 | 0 | Anytime Fitness Australia | product 1 | alias for Mark Grey: CEO at 'Collective Health and Wellness'; identity check against Collective Wellness Group, Anytime's owner (QC fix round) |
| 177 | `Jetts Oakleigh` | 1 | 0 | 0 | Jetts Fitness | referral 1 | identity check (Jetts Oakleigh) |
| 178 | `Bulk Nutrients` | 0 | 0 | 1 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 179 | `Glenn Twiddle - Real Estate Training` | 0 | 0 | 1 | - | | Unrelated business or name-alike |
| 180 | `Revo Foundation` | 1 | 0 | 0 | Revo Fitness | operations 1 | |
| 181 | `Fitness Enhancement Personal Training Bondi` | 1 | 0 | 0 | Fitness Enhancement | referral 1 | |
| 182 | `Carafix Caravan Repairs` | 1 | 0 | 0 | Jetts Fitness | referral 1 | alias for Catherine Hanly: Business Owner at Jetts Australia (headline) |
| 183 | `Fernwood Fitness Ballarat` | 1 | 0 | 0 | Fernwood Fitness | referral 1 | identity check (Fernwood Fitness Ballarat) |
| 184 | `Fitstop` | 1 | 0 | 0 | Fitstop | referral 1 | |
| 185 | `Fitstop Burleigh` | 1 | 0 | 0 | Fitstop | referral 1 | |
| 186 | `Ritz Realty` | 1 | 0 | 0 | Fernwood Fitness | referral 1 | alias for Moby Malik: Franchise Owner at Fernwood Fitness on his row |
| 187 | `BFT North Lakes` | 1 | 0 | 0 | BFT | referral 1 | |
| 188 | `Charity Bounce` | 1 | 0 | 0 | Viva Leisure | referral 1 | alias for Kane Schrader: Plus Fitness Narrabeen Franchisee (headline) |
| 189 | `Plus Fitness rockdale` | 1 | 0 | 0 | Viva Leisure | referral 1 | |
| 190 | `Fitstop Newstead` | 1 | 0 | 0 | Fitstop | referral 1 | |
| 191 | `FS8 Liverpool` | 1 | 0 | 0 | FS8 | referral 1 | |
| 192 | `ANC Enterprises` | 0 | 0 | 1 | - | | Product-only nutrition, supplement or wellness-product business: no programme that follows a person |
| 193 | `EMF Performance & Fitness Centres` | 1 | 0 | 0 | EMF Performance & Fitness Centres | referral 1 | |
| 194 | `Virgin Active Australia` | 1 | 0 | 0 | Virgin Active Australia | member-experience 1 | |
| 195 | `REVL Training Mile End` | 1 | 0 | 0 | REVL Training | referral 1 | |
| 196 | `CSB` | 1 | 0 | 0 | CSB | product 1 | alias for Rachel Dillon: Founder at Move With Us on her row |
| 197 | `Fitness Enhancement Personal Training` | 1 | 0 | 0 | Fitness Enhancement | referral 1 | |
| 198 | `Soul Supps` | 1 | 0 | 0 | KX Pilates | referral 1 | alias for Luisa Helps: Multi Studio Owner KX Pilates M-City Monash & Semaphore (headline) |
| 199 | `Fitstop Cleveland` | 1 | 0 | 0 | Fitstop | referral 1 | |
| 200 | `REVL Training Brighton` | 1 | 0 | 0 | REVL Training | referral 1 | |
| 201 | `GroupFitQuick` | 1 | 0 | 0 | Fernwood Fitness | referral 1 | alias for Melissa Jones: Franchise Owner Penrith & Parramatta at Fernwood Fitness on her row |
| 202 | `Innovation Victoria` | 1 | 0 | 0 | Fernwood Fitness | referral 1 | alias for Susan Oliver AM: Non Executive Director at Fernwood Fitness on her row |
| 203 | `HK Health & Performance` | 1 | 0 | 0 | Vision Personal Training | referral 1 | alias for Haydn Kiel: Director at Vision Personal Training on his row |
| 204 | `Prosperiti Disability Services` | 1 | 0 | 0 | Jetts Fitness | referral 1 | alias for Sam Bhandari: Director & Owner at Jetts Australia, Owner Jetts Canning (headline) |
| | **Total (386)** | **283** | **3** | **100** | 39 accounts IN; Mosh is HOLD only | | |

**Fail by name at validation (12 rows that join an IN account in `extract-people`):** Belinda Amis Wheaton (Fernwood), Chris Torcasio and Adam Koch, MAICD (Sweat), Glenn O'Sullivan, Suren Wickramasinghe, Joanna Wang and Andy Pavalache (Mosh): already messaged from `vadim`, and `check` fails them on its own; Jack Revens (cell `SWEAT`, "Owner, SWEAT": not the Sweat app, a name collision); Bec Kirkup `/in/bec-kirkup-378641362` and Thomas Hepburn `/in/thomas-hepburn-50949997` (duplicate profiles; the other profile of each stays IN); Daniel Waide `/in/daniel-waide-7ab7051b` and Corey Eames-Mayer `/in/corey-eames-mayer-390511117` (NovoFit, distributor cap).

**Hold by name at validation (3 rows that join an IN account; the decision is HOLD, which a yes can later promote):** Eamon H. `/in/eamon-h-a7363413a` (Mosh): a CPO and Medical Director thread with a CEO call is live, and one referral of upside does not justify an uncoordinated touch. Held until Katerina, who owns the thread, says yes. Nikita Fernandes `/in/nikitafernandes13` (SiSU Health, Head of Compliance, quality and regulatory): she owns compliance for health stations that are a medical device, and a cold referral ask to her is high-risk and low-yield. Rhys Holleran `/in/rhys-holleran-9296ab3b` (Viva Leisure, Chair of an ASX-listed company): a referral ask to the board Chair is high-risk and low-yield.

**Identity and current-role checks (stay IN unless the check fails):** company-named profiles (Fernwood Tuggeranong, Fernwood Fitness Ballarat, St Leonards Body Fit Training, Jetts Gym Mount Hutton, Jetts St Leonards, Jetts Oakleigh, KX Pilates Glen Waverley, PF Syd Olympic Park, Gym Genesis): send only if each reads as one person running the unit; no usable name (GH undefined at Plus Fitness, L B at Genesis); franchise owners whose headline names another employer (12, flagged in `hooks-by-company.md`); the 41 alias people, including Mark Grey and Lauren Anliev at Anytime, who are sent only if their profile shows Collective Wellness Group (Anytime's owner); Mel Burn and Melissa Burn at Fernwood (possibly one person with two profiles: send to one only); Sweat's two CEO titles (Damien Mavroudis, and Adam Koch who is OUT): send to Damien only if his profile shows Sweat as current. A job-change check runs on all 283.

## Use case (1 sentence)

Australian gym, studio and personal-training networks, fitness apps and workplace programmes can offer members a guided two-photo scan in their own app or a web page, returning 80+ body measurements and body composition estimates.

## Why this is plausible (evidence)

1. **Australian clubs already treat a body-composition check as a member service, tied to a device in the club.** Goodlife (Fitness and Lifestyle Group) gives members in-club body-composition scans on a scanner ([goodlife.com.au](https://www.goodlife.com.au/evolt360/)); Hapana lists body-scan partners among its gym integrations ([Hapana](https://www.hapana.com/integrations/body-scans-wearables)); SiSU Health runs free health stations that measure weight, BMI and body fat % ([SiSU Health and Wesfarmers Health](https://www.sisuhealthgroup.com/press/wesfarmers-health-partnership)). The habit exists; a phone capture takes it to the member's home and to clubs with no device. Context only, never copy: no device, scanner or maker is named or compared.
2. **The networks on this list run their own member apps, and several are new.** App Store Australia, first-release dates from the iTunes lookup `releaseDate` (not the last-update date), checked 2026-10-11: UBX Member App September 2026, FWD by Fernwood June 2026, Planet Fitness Australia by Bravo Fit June 2026, The Yard Gym April 2026, REVL Training March 2026, One Playground February 2026, Virgin Active Australia July 2025, Fitstop Fitness December 2024, Jetts Fitness Australia September 2024. Viva Leisure's Club Lime and Plus Fitness Member apps and Vision Personal Training's MyVision are older. A white-label SDK goes into an app the brand already owns. Where the brand has no app of its own (Fitness Enhancement, Fitness Inside Out, EMF), the web SDK runs the capture in a page; where the app belongs to an overseas franchisor or owner (Anytime, BFT, Snap Fitness), copy talks about members and clubs. Context only: a release month is copy only where "Company facts" clears it (UBX).
3. **Large, growing networks with one head office per brand.** Anytime Fitness Australia: 630 clubs and 780,000 members, with a target of 800 clubs by 2030 ([Australasian Leisure Management, 2026](https://www.ausleisure.com.au/news/anytime-fitness-australia-marks-18-year-milestone-and-sets-target-of-800-clubs-and-one-million-members-by-2030)); Fitness Passport: 550,000+ members, 950+ employer programmes and 2,300+ facilities ([ALM, August 2026](https://www.ausleisure.com.au/news/fitness-passport-chief-executive-advises-of-40-engagement-of-employer-partners-workforce-in-gym-programs)); Bravo Fit: 32 Planet Fitness clubs with rights to about 100 more ([franchising.com, July 2026](https://www.franchising.com/news/20260722_franchise_equity_partners_acquires_bravo_fit_planet_fitness_australian_fran.html)). Context only: no prospect figure goes into copy.

**What FitXpress brings, with its limits.** From `proof-points.md`: two photos (front and side); under 45 seconds from the photos to structured results; 80+ body measurements; body composition estimates (body fat %, lean mass, fat mass) with BMI and BMR calculated; a 3D model; typical scan-to-scan differences under 1 cm for most evaluated measurements; white-label API and web and mobile SDKs, nothing to ship. Honest limits: body composition values are estimates; no visceral fat output; validation population 16-78 years, 150-220 cm, 38-210 kg, from the US and Europe ("Performance outside this scope has not been characterized"); performance for people with physical disabilities is not established (`accuracy-formulations.md` §5); no Australian reference and no nameable fitness reference. The nearest proof: one weight-management platform ran 34,000 scans in 2025, and 112,100 scans in 2025 across all 3DLOOK customers.

## What earlier campaigns teach this one

- **`2026-07-27-australia-telehealth` (`vadim`):** 38 of 220 invites accepted (17.3%), then replies from 5 of 38 accepted (13.2%); the interested replies came from a product owner and a medical director at one digital-health platform (Mosh), none from the health funds. Acceptance is the loss on this profile; invites go without a note.
- **`2026-08-14-au-digital-fitness` (`vadim`, 123 people in the import file on 2026-10-02):** one reply so far, interested (an insurer's partnerships manager, call the week of 20 October; `responses-summary.md`, 2026-10-08). Its head-office contacts at Fernwood, Fitstop, Sweat, KIC and Hapana are the people this list must not repeat (Rules; `hooks-by-company.md`).
- **`2026-10-07-eu-weight-loss-nutrition` (`olena`, fixed list, referral-heavy):** the shape this hypothesis copies. Its card samples were pasted into copy (an easy-out sample in about 30 messages, a 3D-model display sentence in 24), so card lines here are targets, never sentences.
- **45% of the July AU first messages invented a prior contact** ("Circling back", "Saw your post"): banned, and doubly so at the six brands Vadim messaged before.

## Target buyer persona

**Who buys:** the head office that owns the member app and the member journey at a network (CEO or founder, product, digital, member experience, fitness or programmes), the product owner at an app, the programme owner at a workplace programme, and the partnership owner at a software, programme or facility partner. Unit owners, club managers, board members and staff below lead level are referral paths to head office. Tiers only order the list; one import file.

**Lane by title (the validator assigns exactly one per person):**

| Function at an IN account | Lane | Tier |
|---|---|---|
| Founder, co-founder, CEO, managing director, executive director at head office; head of product, digital product or digital delivery; product owner; owner of a single-brand studio business (Love Athletica, Fitness Inside Out, EMF) | `product` | P1 (directors at head office whose unit is unclear: P2) |
| COO, head of operations, head of franchise performance, head of company clubs, regional managing director at head office, director of operations | `operations` | P1 |
| Director or head of fitness, group fitness, programmes, athletics, creative, customer insights, member experience | `member-experience` | P1 (unclear head-office role: P2) |
| Partnerships, network partnerships, ecosystem, strategic partnerships; every person at NovoFit, Recovr and Les Mills Asia Pacific | `partnerships` | P2 |
| CTO, CIO, head of technology, engineering, data, IT, AI and technology lead | `technical-integration` | P3 |
| Franchise, club and studio owners and their managers; board members and non-executive directors; staff below lead level; people whose franchise role sits behind another employer's cell | `referral` | P4 |

**Not the buyer (FAIL for the cold send):** only the 100 OUT rows of the verdict table. The 3 HOLD rows wait for a decision. Every function at an IN account has a lane.

**KPIs they care about:** member retention and visit frequency; what members see of their progress; programme and challenge completion; the member app's rating and use; for PT networks, client progress across a training block; for workplace programmes, participation; for partners, a capability their own clients can offer.

**Likely objections and the honest answer:**
- "We already have a scanner in clubs / a weight log / progress photos" (Goodlife at Fitness and Lifestyle Group, Jetts, Genesis, BFT challenges and Vision Personal Training studios with a competitor's in-club scanner, Fernwood's studios, Hapana's partners, SiSU's stations, Fitstop's nutrition app, Sweat's progress photos). True; nothing replaces it. The phone capture covers home and clubs with no device, with on-screen guidance at every scan, and sits next to what they already run. Never suggest their data is wrong.
- "Accuracy?" "96-97% accuracy against expert manual measurement" describes body measurements, never body composition; or the full `accuracy-formulations.md` §1.1 sentence; repeatability as the §1.2 sentence; validation scope as above.
- "Data, privacy, where is it hosted?" Replies only: `compliance.md` §10 answers (AWS, primarily US-West-2; photos deleted after processing or within 30 days; outputs stored until deleted by scan ID) and the FAQ link; documents through legal@3dlook.me. Nothing about Australian law, either way.
- "I only run one club." Then the call is about who at head office owns the member experience. "Our members are not app people." The web SDK runs in a page. "Price?" A call question, never in copy.

### Target buyer persona: Sales Navigator pull for step 3

**Pull by title filter inside the approved company list, never by company alone.** The export is the list: this block drives only an Apollo top-up if Vadim asks for one (Open question 4), on IN accounts only, with the lane-by-title table above. Broad on purpose: the validator assigns lanes and fails what does not fit.

```titles
Chief Executive Officer
CEO
Founder
Co-Founder
Managing Director
General Manager
Chief Operating Officer
Head of Operations
Head of Franchise Performance
Franchise Operations Manager
Head of Company Clubs
Chief Product Officer
Head of Product
Product Manager
Product Owner
Chief Digital Officer
Head of Digital
Head of Digital Product
Head of Member Experience
Head of Customer Experience
Member Experience Manager
Head of Fitness
National Fitness Manager
Head of Group Fitness
Head of Training
Head of Programming
Head of Coaching
Head of Retention
Head of Growth
Chief Marketing Officer
Head of Marketing
Head of CRM
Chief Technology Officer
Chief Information Officer
Head of Technology
Head of Engineering
Head of Data
Head of Partnerships
Partnerships Manager
Head of Business Development
Head of Wellbeing
Program Director
```

**`cap_per_group: 50`** (standing decision 2). Fernwood 38, Fitstop 33, Jetts 30, BFT 23: a top-up may take a network to 50, head-office people first.

## Message angle: segments, lanes, company facts and the content asset

Every person gets exactly one lane, spelled as below. People at one network talk to each other: Rules, "Several people at one company"; facts agree across all of them. Numbers in copy come only from `proof-points.md`. **Writer notes are instructions to the writer and are never copied into a message.**

### Segment angles (writer notes)

- **A. Club and studio networks.** A scan the member can take on a phone at home or in the club, inside the brand's own member app (or a page the club sends where the app is not the brand's own), which the member and their trainer can look back on later. For head office: a capability added once to the app or page through the API or SDKs, with nothing to ship or install in clubs. For a unit owner: a question about their own club and members from the brand's topic bank, never a pitch to adopt anything. Where a club already offers an in-club scanner (Open question 9), the phone capture is for home and for weeks away from the club, and copy never mentions the scanner.
- **B. Personal-training networks.** A standardized set of measurements a trainer can request from a client by link, taken at home, outdoors or in the studio, and set against that client's earlier scans over a training block. Vision Personal Training has its MyVision app (never describe what it records). Fitness Enhancement and Fitness Inside Out have no verified app: never write "your app" to them.
- **C. Fitness apps.** The capture inside the app through the SDK, white-label, offered at the points the member picks. KIC and Move With Us: strength, movement and the member's choice; never weight, shape or appearance.
- **D. Workplace programmes and health.** An optional body check members can take at home in the programme's app, with the programme deciding what is shown and to whom; never data to employers, never eligibility. SiSU Health: alongside its stations, never compared. Mosh: HOLD, nobody sent by default.
- **E. Partners.** A capability the partner can offer its own club clients inside their apps: one SDK, the partner decides where it appears. NovoFit (CEO and founding director only) and Les Mills Asia Pacific: a partnership question only, never an app pitch. Your Reformer: its product and operations people hear about the At Home app.

### Apps verified (App Store Australia, 2026-10-11; mention an app only where listed here)

**The brand's own app (it may be mentioned; never describe what it records):** Fernwood (Fernwood Fitness app and FWD by Fernwood, both out of copy this round: the August thread used them) · Fitstop (Fitstop Fitness) · Jetts (Jetts Fitness Australia) · UBX (UBX Member App) · Viva Leisure (Club Lime; Plus Fitness Member) · KX Pilates · REVL (REVL Training) · Vision Personal Training (MyVision) · The Yard Gym · One Playground (One Playground; One Coach) · Fitness and Lifestyle Group (Fitness First Australia and Goodlife apps) · Genesis (Genesis Connect) · Revo Fitness · Planet Fitness Australia (Bravo Fit's own app) · Virgin Active Australia · STRONG Pilates · Fitness Cartel · TotalFusion · FS8 · VAURA · Love Athletica · Fitness Passport · SiSU Health · Sweat · KIC (KIC Wellness; KICStudio) · Move With Us · Your Reformer (At Home) · Mosh.

**App published by an overseas franchisor or owner (talk about members and clubs; never "your app", never name the app):** Anytime Fitness Australia (AF App, Anytime Fitness, LLC), BFT (BFT Performance and BFT Booking, both Xponential entities), Snap Fitness Australia (Snap Fitness app, Lift Brands, Inc.).

**No app verified (a page the club or trainer sends; never "your app"):** Fitness Enhancement, Fitness Inside Out, EMF, Ford Health, World Gym Australia (last app update 2020), Les Mills Asia Pacific, NovoFit.

### Lanes

- **`product`** (founders, CEOs, MDs, product and digital heads). What the member app, or a page the brand sends, can ask a member for: a guided two-photo scan that returns 80+ body measurements, body composition estimates and a 3D model, white-label through API or web and mobile SDKs, nothing to ship. The question: at which point in a member's year a scan would fit for their members (joining, a goal review, a challenge, a stretch away from the club).
- **`operations`** (COOs, franchise performance, company clubs, operations directors). Nothing to ship, stock or install in clubs; the capture runs on any phone with on-screen guidance; the speed wording from the Rules. The question: how clubs run member check-ins or goal reviews today. Never say or imply clubs measure badly.
- **`member-experience`** (fitness, group fitness, programmes, athletics, creative, insights, member experience). An optional scan a member can repeat at home or across a programme, set against an earlier scan the member picks, and shown only where the brand chooses. The question: how members see what their training is changing today. Never promise retention or results.
- **`partnerships`** (partnership, ecosystem and BD owners; NovoFit, Recovr, Les Mills Asia Pacific). Message 1: what the scan returns, the company fact, and whether a partner capability has a place in what they offer clubs or employers. Never name or compare with existing partners.
- **`technical-integration`** (CTO, CIO, technology, engineering, data). REST API with API-key authentication, web and mobile SDKs, white-label; photos deleted after processing or within 30 days; outputs stored and deletable by scan ID; technical tone. No integration-time figure in Message 1.
- **`referral`** (unit owners, managers, board members, staff). Standing decision 10: never a bare "who owns X?". Message 1: one line on what the scan returns and why it matters for this brand's members (from its fact; an app line only where the Rules allow one), then one question about the person's own club, studio or work, built from the brand's topic bank and the person's anchor in `hooks-by-company.md`. Message 2: a short call offer with a soft ask, and an easy out that is a different ask: a pointer to the person at head office who owns the member app or member experience, worded fresh for each person (name the target, never reuse a sentence). Unit owners: the Rules' franchise limits; never suggest head office knows about the message.

### Earlier threads at the six registry-waived brands (writer notes)

Vadim messaged head-office people at these brands on 2026-08-14 (Mosh: 2026-07-27). The new people get angles those people did not get (`hooks-by-company.md` lists who and in which role):
- **Fernwood:** the CEO and five marketing, CRM and content people got the member-app and FWD angle. Here: club owners on topics from the Fernwood bank, with no app and no FWD, and the Director of Fitness on FIIT30 and training programmes.
- **Fitstop:** growth, GM, brand and head-coach people. Here: studio owners on topics from the Fitstop bank; the Athletic Director on programming, testing and Global Games.
- **Sweat:** CEO, product and marketing. Here: the CEO title (current-role check) on the strength programmes, and technical people on how a capture sits in the app.
- **KIC:** marketing, co-founders, product. Here: technology and platform; strategy and operations.
- **Hapana:** CEO, COO, CTO, product, marketing. Here: one technical platform specialist, referral only.
- **Mosh:** a live sales conversation with the CPO and the Medical Director. Eamon H. (creative) is on HOLD until Katerina, who owns the thread, says yes (Open question 3).

### Company facts the copy may use

Dates may be used as months or years; no other prospect figure (members, clubs, studios, prices, funding, class lengths, block lengths). Never name an owner, investor, parent, partner or another prospect. Facts added in the QC fix round come from each brand's own site, read on 2026-10-11 (Sources). Across one brand's people, facts rotate: no fact opens more than about a fifth of that brand's first messages.

| Company | ID | Fact the copy may use | Writer notes |
|---|---|---|---|
| Fernwood Fitness | FW2 | Fernwood is a women's health club network that began in Bendigo and is run by franchise owners across Australia. | Unit owners: their own club only. v1's FW1 (FWD by Fernwood) is out of copy for everyone, the Director of Fitness included: the August head-office thread used it, and it names Fernwood's own progress tooling |
| Fernwood Fitness | FW3 | FIIT30 is Fernwood's coach-led small-group training program for women, with four class types: Full Body Athletic, Total Body Strength, Lower Body Power and Upper Body Power. | FIIT30's own page says some members already use body scans: never pitch scanning, measurement, progress or 3D as new. No class length |
| Fernwood Fitness | FW4 | New Fernwood members book a first session with a Fernwood trainer, one-on-one or as a group introduction, to build a plan that suits them. | |
| Fernwood Fitness | FW5 | Fernwood describes personal training as one of its most popular services, closely followed by FIIT30. | Never mention studio treatments |
| Fitstop | FS1 | Fitstop trains members across four styles, Lift, Perform, Condition and Sweat, and members book through the Fitstop Fitness app. | Never mention its nutrition app's weight tracking, its software vendor or its investors |
| Fitstop | FS2 | Fitstop runs Global Games, a teams-of-two competition across Lift, Condition, Perform and Sweat stations, with a Brisbane event in October 2026. | Month only; never claim who took part or how they placed |
| Fitstop | FS3 | Fitstop names progression as one of its pillars and builds each week as a rotation of its four session styles. | Never imply progression goes unmeasured |
| Fitstop | FS4 | A first Fitstop session is free and booked in the app, and first-timers arrive early to meet their trainers. | |
| BFT | BF1 | BFT uses science and technology to give each member a training experience relevant to their own body and fitness level. | Never name the owner. Never "your app" or an app name: both BFT apps are published by the US owner. Never mention challenges, in-studio scans, BFT³ or PXI |
| BFT | BF2 | BFT programs progress in multi-week blocks, with each class built into the next. | No block length |
| BFT | BF3 | BFT runs PODIUM, a teams-of-two strength and conditioning competition whose first series opened for registration in June 2026. | Month only |
| BFT | BF4 | BFT's trial lets a new member try several classes to see how the progressive programming works. | |
| Jetts Fitness | JT1 | Jetts has run 24-hour gyms since 2007, born and bred in Australia, and members use the Jetts Fitness Australia app. | "since 2007" is a date, allowed; never mention the buyout or the former parent |
| Jetts Fitness | JT2 | BeWell Brands brings Jetts together with recovery and wellness brands in one platform. | Head-office copy only |
| Jetts Fitness | JT3 | Jetts memberships come with 24/7 access and no lock-in contracts. | Never imply members leave; no retention promise |
| Jetts Fitness | JT4 | Jetts clubs offer personal trainers and exercise physiologists alongside open zones for functional, HIIT and strength training. | Never clinical framing (rehab, conditions). Never mention in-club scanners (Open question 9) |
| UBX | UB1 | UBX mixes boxing and strength training in a flexible format, and the clubs that began as 12RND now train under the UBX name. | Unit owners from 12RND: never suggest the rebrand was an issue |
| UBX | UB2 | UBX launched a new UBX Member App in September 2026. | Proven by the App Store first-release date (iTunes `releaseDate` 2026-09-11). Never mention the older third-party portal app |
| UBX | UB3 | UBX has no class timetables: members arrive when they like and work through boxing and strength rounds with coaches on the floor. | No round counts or durations |
| UBX | UB4 | New UBX members are met by a coach and get a boxing walk-through before their first workout. | |
| Viva Leisure | VV1 | Viva Leisure runs Club Lime and is the master franchisor of Plus Fitness, and both have their own member apps. | Plus Fitness unit owners: talk about Plus Fitness, not Viva |
| Viva Leisure | VV2 | Viva Leisure designs, develops and manages its own integrated technology ecosystem for its brands, including NFC wallet entry. | Head office only |
| Viva Leisure | VV3 | Plus Fitness runs local 24/7 gyms across Australia, which the brand describes as newly recharged. | Plus Fitness unit owners; never a refresh or rebrand as a problem; no club counts |
| Viva Leisure | VV4 | Club Lime extended its Canberra Raiders partnership through to 2028, announced in August 2026. | Head office only; never results, dividends or investors. Never mention World Gym Australia (Open question 10) |
| KX Pilates | KX1 | KX Pilates runs high-intensity reformer classes that combine Pilates with cardio and endurance, through franchised studios and the KX Pilates app. | No class length |
| KX Pilates | KX2 | KX Pilates classes run from Basics through Signature and Strength to Advanced, with Active Recovery for reset days. | Never the Pre & Post Natal class: pregnancy is out of scope |
| KX Pilates | KX3 | KX Pilates pairs dynamic reformer Pilates with the Kaizen idea of continuous improvement. | |
| REVL Training | RV1 | REVL Training combines several training methods into one approach, and members book through its own REVL Training app. | No launch month: v1's "September 2026" was an update date (first release March 2026, and an older REVL-named app of unknown relation exists) |
| REVL Training | RV2 | REVL periodises its programming into multi-week training blocks with prescribed intensity and progressive overload. | No block length |
| REVL Training | RV3 | REVL runs three goal-based programs: Perform for strength, Move Total for total-body strength and conditioning, and Sweat for conditioning. | |
| REVL Training | RV4 | REVL's Race The Globe, a teams-of-four hybrid race open to members, coaches and the public, comes to Brisbane in October 2026. | Month only; after the event, past tense. Never mention Recovr |
| Vision Personal Training | VP1 | Vision Personal Training is a network of personal-training studios across Sydney, Wollongong, the Gold Coast, Melbourne and New Zealand. | Never the in-studio scan (Open question 9); never pitch body composition as new; never the results guarantee or money-back offer |
| Vision Personal Training | VP2 | Vision builds each client's program on four pillars, emotions, education, eating and exercise, in that order. | |
| Vision Personal Training | VP3 | Vision trainers run coaching and goal-setting sessions with each client, in the studio, outdoors or online, and clients use the MyVision app. | Never describe what MyVision records |
| Vision Personal Training | VP4 | strongHER is Vision's personalised strength program for women, with one-on-one training and structured nutrition. | Strength only: never life stage, symptoms, bone density, weight or a health claim |
| The Yard Gym | YG1 | The Yard Gym exists to change lifestyles and has its own app. | No launch month: v1's "September 2026" was an update date |
| One Playground | OP1 | Fitness Playground became One Playground to go beyond fitness and aesthetics into health and wellness under one roof, with the One Playground and One Coach apps. | |
| Fitness and Lifestyle Group | FL1 | Fitness and Lifestyle Group runs Fitness First, Goodlife and Barry's, with member apps for its brands. | Never mention in-club scanners, the owner or a sale |
| World Gym Australia | WG1 | World Gym Australia describes itself as an intelligent approach to fitness for ambitious, motivated members. | No app mention. Never mention Viva Leisure or its brands (Open question 10) |
| Genesis Health + Fitness | GN1 | Genesis Health + Fitness began in Ringwood in 1997 and sits in Belgravia Health & Fitness with Coaching Zone and Ninja Parc; members use Genesis Connect. | Never mention in-club scanners (Open question 9) |
| Revo Fitness | RF1 | Revo Fitness sets out to make fitness accessible to every person at an affordable price, with its own app and the Revo Foundation. | |
| Anytime Fitness Australia | AF1 | Collective Wellness Group runs Anytime Fitness across Australia as a 24/7 club network. | Never "your app"; never mention the global franchisor. Mark Grey and Lauren Anliev only after their identity checks pass |
| Snap Fitness Australia | SN1 | Snap Fitness runs 24/7 gyms across Australia under its "For the Feeling" positioning, which treats every kind of fitness as valid. | Chris Caldwell only. Never "your app"; never Lift Brands or Fitstop |
| Planet Fitness Australia | PF1 | Planet Fitness Australia runs a Judgement Free Zone for members and has its own Australian member app. | No launch month: v1's "September 2026" was an update date (first release June 2026). Never mention the 2026 deal, investors or the US franchisor's older app |
| Virgin Active Australia | VA1 | Virgin Active Australia has its own Australian member app. | No launch month: v1's "September 2026" was an update date (first release July 2025). Never mention the global owner |
| STRONG Pilates | SP1 | STRONG Pilates combines reformer Pilates with rowing or riding in one full-body class, with the STRONG Pilates app. | Unit owner only |
| Fitness Cartel | FC1 | Fitness Cartel is Australian-owned and runs 24/7 full-service health clubs alongside apparel, supplements and a wellness spa, with its own app. | No club targets |
| TotalFusion | TF1 | TotalFusion runs multi-sensory health and wellness destinations and has its own app. | |
| FS8 | F81 | FS8 remixes Pilates, Tone and Yoga into a low-impact, high-energy workout, with the FS8 app. | Never mention VAURA |
| VAURA Pilates | VR1 | VAURA fuses reformer Pilates with athletic training, with the VAURA app. | Never mention FS8 |
| EMF Performance & Fitness Centres | EM1 | EMF runs fitness and performance training centres across Brisbane, the Gold Coast and Newcastle. | No app |
| Love Athletica | LA1 | Love Athletica is a reformer Pilates studio with cardio, strength and restorative flow, and members book through its app. | |
| Fitness Enhancement | FE1 | Fitness Enhancement runs private personal-training studios and mobile trainers for busy people who would rather avoid the gym scene. | Never Fit Your Ability or its clients as a scan context; no app |
| Fitness Inside Out | FI1 | Fitness Inside Out sends personal trainers to clients' homes, outdoors and online across five cities. | No app |
| Sweat | SW1 | Sweat is a women's fitness app and community that began as Sweat with Kayla, with gym-based strength programs such as Strength with Kayla. | Progress photos exist: never pitch photos or visual progress as new |
| KIC | KC1 | KIC frames wellness as a feeling, and its programs cover movement, strength and mindset. | No weight, shape or appearance; never quote its tagline (corrective negation) |
| CSB (Move With Us) | MW1 | Move With Us is a women's training and nutrition app with on-demand Pilates, strength and running sessions. | Address it as Move With Us; never pitch apparel; no bikini or aesthetic framing |
| Fitness Passport | FP1 | Fitness Passport is a workplace health and wellbeing program that gives employees and their families gym and pool access across Australia and New Zealand, with an app for check-in. | Wellness only; never data to employers, never eligibility |
| Ford Health | FH1 | Ford Health provides corporate health services to employees in metropolitan, regional and remote areas. | No app |
| SiSU Health | SS1 | SiSU Health runs free self-serve health checks with results in the SiSU Health app. | Never pitch BMI or body fat as new; never compare with its stations; never mention its owner |
| Mosh | MO1 | Mosh offers personalised healthcare across weight loss and other areas through the Mosh app. | HOLD: used only if Katerina clears Eamon H.; never mention the earlier conversation |
| Hapana | HP1 | Hapana is the operating platform gyms, studios and franchises run their business on, with branded member apps. | Never name its customers or its integration partners |
| Recovr | RC1 | Recovr flags gym members at risk of cancelling weeks earlier and guides the team on what to do. | Never name its customers or integrations; no figures; never mention its founder's REVL studio |
| Les Mills Asia Pacific | LM1 | Les Mills Asia Pacific gives facilities instructor training, marketing support and a group fitness management system. | Partnership only; no app |
| NovoFit | NF1 | NovoFit delivers fitness facilities to health clubs and other operators, built from two long-standing Australian equipment suppliers. | Partnership only; CEO and founding director only |
| Your Reformer | YR1 | Your Reformer makes reformers for homes and studios, with Pilates education and the Your Reformer At Home app. | |

### Question topics by brand (writer notes)

Each person gets one question nobody else at the company gets, built from their title, unit and anchor (`hooks-by-company.md`) and about their own work. In Message 1 it is never a "who" question; the pointer to head office is only Message 2's easy out. The topics below are targets: what the question is about and whose job it is. They are never sentences to copy. Each is a point a phone body scan genuinely plugs into: a member's starting point, a review, a training block or event, or time away from the club.

**A theme may repeat within a brand, at most about a fifth of that brand's referral people; wording, hook, structure and closer may not repeat.**

**Fernwood Fitness** (37 referral; a theme at most about 7 times). Never the member app, FWD, studio treatments, weight, shape or appearance.
- A new member's first-session plan (FW4): what the club's trainers set with her at the one-on-one or group introduction; the owner runs onboarding.
- FIIT30 small groups (FW3): how coaches let a member see she is getting stronger across the four class types; the owner runs the coaching team.
- The club's FIIT30 challenge: how the club marks where a member started and where she finished, on strength and confidence only; the owner runs the club's own challenge extras.
- Personal training reviews (FW5): what a Fernwood PT has in hand when a member's program is reviewed; the owner hosts the PTs.
- Members who mix Reformer Pilates, FIIT30 and the gym floor: where one member's goals and check-ins sit when she uses several services; the owner sets the club's service mix.
- Members coming back after a break: how the club restarts a returning member's plan; the owner's trainers and front desk.
- Owners of two or more clubs (anchor names them): whether goal reviews run the same way at each club; the owner sets both clubs' routines.
- Board members (Angela Williams, Susan Oliver AM): how a network of owner-run clubs weighs a new member service; never a pitch.

**Fitstop** (32 referral; about 6). Never the nutrition app, weight, the software vendor or investors.
- The four-style week (FS1, FS3): how the studio shows a member what a stretch of Lift, Perform, Condition and Sweat has changed; the owner runs the coaching floor.
- Global Games (FS2): how the studio readied members to compete in pairs, and what they took from it; the owner's members represent the studio.
- The free first session and first weeks (FS4): what coaches note about a newcomer's starting point; the owner sets onboarding.
- Goal reviews or check-ins: how often they run at the studio and what the coach brings to them; the owner sets the routine.
- Everyday members next to high performers (the event's ALL STAR and PRO divisions): how coaches keep both groups' progress in view; the owner's coaches.
- Members who train away from the studio for a while (travel, shift work, busy weeks): how the studio stays in touch with what they do; the owner. Never a retention promise.
- Multi-location owners (anchor): whether studios run check-ins the same way; the owner sets it.

**Jetts Fitness** (26 referral; about 5). Never in-club scanners.
- 24/7 access (JT3): members who mostly train when no staff are on, and how the club keeps up with what they are working toward; the owner staffs the club.
- No lock-in contracts (JT3): what the club shows members about their own training; a question about the club's practice, never a retention promise.
- A new member's trial weeks: what the club learns about their starting point during them; the owner runs the trial.
- PT and exercise physiology sessions (JT4): what the trainer has in hand at a client's program review; the owner hosts the trainers. Never clinical framing.
- Members on their own program in the functional, HIIT and strength zones (JT4): how they see change over months with no trainer; the owner's floor team.
- Owners of several clubs (anchor): whether member check-ins run the same way at each.

**BFT** (20 referral; about 4). Never challenges, in-studio scans, BFT³, PXI, the owner, or "your app".
- The end of a program block (BF2): how the studio shows members what the block changed; the owner's coaches run the blocks.
- PODIUM (BF3): how the studio readied its teams and what members took from competing; the owner.
- The trial (BF4): what coaches learn about a new member across the first classes; the owner runs the trial.
- Personal attention in a group class: how coaches give each member feedback on progress in a busy session; the owner's coaching team.
- Members who miss weeks (travel, shifts, family): how the studio sees what they did while away; the owner.
- Owners of several studios (anchor: Valentin U., Stef Mathieson): whether member reviews run the same way across studios.

**UBX** (14 referral; about 3). Never round counts, durations or the change from 12RND as a problem.
- No timetables (UB3): how coaches keep up with a member whose visits never land in a fixed class; the owner runs the floor.
- The new-member walk-through (UB4): what the coach notes about a newcomer's starting point; the owner.
- Boxing rounds and strength rounds: how members see what the strength side of the workout is doing for them; the owner's coaches.
- The new member app (UB2): what the club hopes its members will use it for; the owner. Never describe what the app records.
- Clubs that trained as 12RND (anchor marked ex-12RND): what members ask the club for now that it trains as UBX.
- Multi-site operators (anchor): how member check-ins run across sites.

**KX Pilates** (12 referral; about 2-3). Never pregnancy or the Pre & Post Natal class; no class length.
- Moving up the class ladder (KX2): how the studio decides a member is ready to move from Basics or Signature to Strength or Advanced; the owner's trainers.
- The Strength class (KX2): what members see of their strength work over months; the owner.
- Kaizen (KX3): how the studio shows a member small improvements over time; the owner.
- Studio challenges (KX ran its KX3 Challenge in February 2025): how the studio marks the start and the end of a challenge; the owner.
- The intro offer: what trainers learn about a new member in the first classes; the owner.
- Owners of several studios (anchor: Justine Rosham, Luisa Helps, James Trenerry): whether member reviews run the same way across studios.

**Viva Leisure and Plus Fitness** (10 referral; about 2). Owners of Plus Fitness clubs hear about Plus Fitness only and never about Viva or World Gym Australia.
- Members who train in the hours with no staff on (VV3): how the club keeps up with their goals; the owner.
- Onboarding at a 24/7 club: what the club captures about a new member's starting point; the owner.
- PTs working in the club: what a PT has in hand at a client's review; the owner hosts the PTs.
- The refreshed club (VV3): what members have asked for since; never the refresh as a problem.
- Owners of several clubs (anchor: Adrian Haywood, LEIGH J.): whether check-ins run the same way at each club.
- Head-office projects (Shane Johnson, fit-outs): how a new member-facing feature reaches clubs during a fit-out or refit.

**REVL Training** (9 referral; about 2). Never Recovr.
- The end of a periodised block (RV2): how the studio shows members what the block changed; the owner.
- Perform (RV3): how members see their strength progress across cycles; the owner's coaches.
- Members who mix Perform, Move Total and Sweat (RV3): where one member's overall picture sits.
- Race The Globe (RV4): how the studio readied its teams of four.
- First timers: what coaches note about a newcomer's starting point.
- Owners of several studios (anchor: Wayne Markus): whether reviews run the same way across studios.

**Vision Personal Training** (9 referral; about 2). Never the in-studio scan, body composition as new, the guarantee or the money-back offer.
- Clients training online, outdoors or at home (VP3): how the trainer sees a client's progress when they rarely meet in the studio; the studio owner.
- Goal-setting sessions (VP3): what the trainer has in hand when goals are set and reviewed.
- The four pillars (VP2): where progress in the exercise pillar shows up for the client.
- strongHER (VP4): how trainers show women in the program their strength progress; strength only.
- A new client's first weeks: how the trainer marks the starting point.
- Directors of several studios (anchor: Daniel Collins): whether reviews run the same way across studios.

**Every other company** (Genesis 8 referral, The Yard Gym 5, Fitness Enhancement 5, World Gym Australia 4, single referral people elsewhere). Genesis: never in-club scanners. World Gym Australia: never Viva.
- Club, studio and franchise owners: how the club marks a new member's starting point; how goal reviews or check-ins run; what members ask the team about their progress; how new member-app features reach the club.
- PT studio owners and trainers: how a client's progress is recorded over a training block; what the trainer has in hand at a review.
- Board members and non-executive directors: how the network decides on new member-facing technology.

### Content asset in Message 2 (at most one article link; no calendar link on this profile)

| Who | Link | Writer notes |
|---|---|---|
| `product`, `operations`, `member-experience` at segments A, B, C | https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/ | Do not quote figures from the page |
| `product` at segment D, every `partnerships` person | https://3dlook.ai/content-hub/ai-body-data-wellness-platforms/ | Do not quote figures from the page |
| `product`, `operations` at segment E (Your Reformer: an at-home app) | https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/ | Do not quote figures from the page |
| `technical-integration` | https://3dlook.ai/content-hub/fitxpress-data-privacy-security-regulatory-faq/ | Never restate it |
| `referral` | no article | |

All three links returned HTTP 200 on 2026-10-11.

## Outreach language

English, every message. Short sentences, plain words, Australian context without slang.

## Rules for steps 3-5

- **Sender and format:** Vadim, English, `Vadim` alone on the last line, first name only. Connection request with no note. Message 1 ≤ 600 characters; Message 2 ≤ 550. Message 1 carries no link. Message 2: a short call offer closed with a soft ask (no calendar link exists for `vadim`), at most one article link (asset table). Everyone goes in one import file; tiers only order the list.
- **Lanes are exactly** `product`, `operations`, `member-experience`, `partnerships`, `technical-integration`, `referral`.
- **Message 1 asks, Message 2 calls** (standing decision 10), every lane, referral included. Message 1: context first (what the scan returns and why it matters for this company's members, from its fact), then one question; no call ask and no link. Message 2: the call offer as a soft ask; people who are not the buyer get an easy out that points to whoever owns the member app or member experience at head office. Never the same ask twice.
- **Registry-waived brands (Fernwood, Fitstop, Sweat, KIC, Hapana, Mosh).** Vadim has messaged other people there. Copy must not read as a first-ever introduction of 3DLOOK to the company, and makes no claim either way about the earlier thread: no "introducing 3DLOOK", no "we have not spoken", no "as discussed", no "following up", no mention of colleagues. Each new person gets an angle from "Earlier threads" that differs from the roles messaged before.
- **Several people at one company.** Never mention colleagues, other people's clubs or units, owners or consultants; never claim to have spoken with anyone there; never claim an interaction that did not happen ("Circling back", "Saw your post", "Following up" are banned). Name the company in every Message 1. No two people at one company share an opener, a central question, a closing ask, a Message 2 opener or a product sentence. People who share a club (flagged in `hooks-by-company.md`) get different topics and never a mention of each other.
- **Franchise networks.** Head office is the buyer; units are referral paths. Never pitch a unit to adopt anything; never mention franchise terms, fees, territories, network-wide club or member counts, rebrands as a problem, or head-office plans; never suggest head office knows about the message. **Carve-out:** naming the person's own club or clubs, as their row gives them (`hooks-by-company.md`), is allowed; a count of the network's clubs is not.
- **Apps.** Mention a member app only where "Apps verified" lists the brand's own app. Anytime Fitness Australia, BFT and Snap Fitness Australia use apps published by an overseas franchisor or owner: never "your app", never an app name. Elsewhere the capture is a page the club or trainer sends. Never describe what an app records.
- **Message 1 makes an observation from the company fact or the person's role,** never about something the company lacks.
- **Never put a prospect's own data or devices next to ours.** No message names a club's scanner, weigh-ins, progress photos, health stations or member data and then says what the scan returns. Never compare with in-club devices. Partial overlap (Open question 9): Jetts, Genesis, BFT, Vision Personal Training and Goodlife offer a competitor's in-club body-composition scanner, and Fernwood's FIIT30 page says some members use body scans. Never mention a scanner, a scan program or a challenge that includes scans, and never present the phone capture as a replacement.
- **Body image and tone.** Many accounts serve women (Fernwood, Sweat, KIC, Move With Us, KX Pilates, STRONG Pilates, FS8, VAURA, Love Athletica). No weight-loss, shape, toning or appearance promises, no before-and-after, no aesthetic words about bodies. Writer note, not copy: the 3D model is shown only where the brand chooses, so never lead with it as the value.
- **People the scan is not for.** Never offer it for people with physical disabilities (Fit Your Ability's NDIS clients; performance not established), under 16, or in pregnancy (KX Pilates' Pre & Post Natal class included). No life-stage or symptom framing (Vision's strongHER).
- **Workplace programmes (Fitness Passport, Ford Health, SiSU Health).** Wellness and participation only; never eligibility, verification, premiums or data reaching an employer.
- **What the scan does not do.** It does not diagnose, decide eligibility or interpret results. Any comparison covers only scans the member selects. Copy never says or implies that the scan, the club or 3DLOOK tracks a member over time. No visceral fat output.
- **No outcome promises.** Never promise or imply better retention, engagement, results, weight loss or ROI. Describe what the scan returns, where it runs and how much it is used.
- **Compliance line: none in Australian cold copy** (standing decision 12). No HIPAA, GDPR, SOC 2, Privacy Act, TGA, FDA or medical-device wording in any sequence; privacy questions in replies go to `compliance.md` §10 and the FAQ link.
- **No 3DLOOK client is named.** Anonymised proof allowed, in this locked wording (fixed proof lines that may be used as written): "one weight-management platform ran 34,000 scans in 2025" (no client name, no geography); "112,100 scans in 2025 across all 3DLOOK customers" (3DLOOK-wide scale, its own sentence, never read as fitness or club scans); "3DLOOK has worked with 100+ clients" (all-time, both products; never "100+ clients use FitXpress" or "today").
- **Numbers and accuracy, only from `proof-points.md` and in its wording:** two photos (front and side); "under 45 seconds from the photos to structured results" (the only speed wording, inside a sentence whose subject is the scan or its output); 80+ body measurements; body composition estimates (body fat %, lean mass, fat mass) with BMI and BMR calculated; "96-97% accuracy against expert manual measurement" (body measurements only, never in a sentence with body composition, never opening Message 2); the §1.2 repeatability sentence; the 34,000, 112,100 and 100+ lines. No prospect figure, no integration-time figure in Message 1.
- **Owners, deals, former employers.** Never mention funding, investors, valuation, acquisitions, buyouts, group owners, sale processes, revenue, prices, headcount or club counts. A former employer may be named unless it is another account in this campaign, a competitor or a banned term; `hooks-by-company.md` flags the cases.
- **Cell employers.** Never name the person's cell employer when it is not the IN brand: the alias rows (Coles, CBRE Asia Pacific, Prosperiti Disability Services, City of Greater Geelong, Ritz Realty, LoanBird and the rest in `hooks-by-company.md`). Address the person only through their role at the IN brand. Another current job in a headline follows the same rule.
- **Word traps.** Never "objective" about our data (standardized, timestamped, structured, repeatable); never "comprehensive", "seamless", "leverage", "game-changer"; no em or en dash; no "plus" as a connector; no "so" introducing a benefit; no corrective "X, not Y".
- **Writer notes and card instructions are not copy.** "generic figure", "never a promise", "not a promise", "context only" and "writer note" are banned terms, so a leak fails the gate. Card lines are targets: write your own sentence every time.
- **No pricing and no trial terms** of ours anywhere. A price or trial question goes to the call. A prospect's own trial or first session may be a topic, never with the words "free trial", which the gate fails as a price.
- **Message 1 gate.** Every message 1 carries at least one product specific from `proof-points.md` and one line that could only have been written to that company; each pair of messages cites at least one number. The `referral` lane is not exempt here (`referral_call: yes`).

## Anti-cases (where it does NOT work)

- **Out, by name:** the 100 OUT rows of the verdict table, and the 12 of them that join an IN account (fail by name). The 3 HOLD rows are held by name for a decision. Match on the company LinkedIn page and the person's own row, never on the name alone.
- **Structural anti-cases:**
  - **Competitors and their app partners:** Evolt (Evolt 360 scanner and app) and any company whose own product is body scanning or body measurement from images.
  - **Product-only nutrition, supplement and wellness-product brands** (BON CHARGE, Swisse, Bulk Nutrients, VPA, Macro Mike, Vida Glow, WelleCo, ZIISH, Vitable, Juice Plus and others): no programme that follows a person.
  - **In-store supplement retail** (Australian Sports Nutrition, Mr Vitamins, Go Vita; one rule since the fix round): in-store advice is not a programme that follows a person, and the scan cannot honestly be tied to supplements or results. OUT; the 13 people are offered to Vadim as a pool (Open question 5).
  - **Equipment sellers and servicers without a member software surface** (VERVE Fitness, Life Fitness Australia, Johnson Health Tech Australia, Gym Services Australia, Family Fitness & Playground Equipment): not competitors, no buyer for a member capability. Life Fitness Australia and Johnson Health Tech Australia are local sales and service arms of overseas manufacturers whose connected-equipment software is built abroad. **NovoFit is the one distributor kept,** capped at its CEO and founding director, as a partnership ask: it is Australian-owned, decides partnerships in Australia and fits out clubs for many operators.
  - **Hospitals and clinical providers** (sportsmed): the filter excluded them and the conversation would be clinical.
  - **Single sites and freelancers without a company page:** a unit with no app and no head office behind it.
  - **Franchise units on their own:** a unit cannot add an SDK to the franchisor's app; units are referral paths only.
  - **Head office or operating parent in the US with no Australian head office:** belongs to `nick`. None left on this list: Lift Brands APAC is run from Australia and moved IN in the fix round. Financial owners and global brand owners abroad are flagged, not routed (Open question 2).
  - **People the scan is not validated for:** people with physical disabilities, under 16, in pregnancy, outside 38-210 kg.
- **Displacement:** an account that runs a phone-camera body scan or has signed a phone-scanning vendor is held for Vadim. None found at an IN account on 2026-10-11. **Partial overlap is not displacement:** a competitor's in-club body-composition scanner at Jetts (preferred supplier since November 2023), Genesis (rollout from 2022), BFT (challenge scans), Vision Personal Training (studio scans) and Goodlife (Fitness and Lifestyle Group); Fernwood's FIIT30 page saying some members use body scans; Hapana's scan partners; SiSU's stations; Fitstop's nutrition-app weight log; Sweat's progress photos. All stay IN, and copy never sets them next to the scan (Open question 9).
- **Stop conditions before send:** an IN account announces a sale to an offshore owner (Fitness and Lifestyle Group is in a sale process), a closure or a body-scanning partner (pause, Vadim decides); a profile shows the person has left (drop).

## Data handling (replies only)

Australian prospects handle member data under their own obligations; FitXpress copy never claims compliance with Australian law. In replies, use only `compliance.md` wording: TLS in transit and SSE-S3 at rest; AWS, primarily US-West-2 and partially US-East-1; photos deleted after processing or within 30 days, per the customer's policy; retained photos blurred, faces obscured at capture; measurements, body composition and 3D models stored until deleted by scan ID; scan records on random IDs; production data not used to train models; documents through legal@3dlook.me. Never "processed, not stored", "no personal data" or "no personal identifiers". Offshore hosting questions go to legal@3dlook.me.

## Vadim's standing decisions (built in, not open questions)

1. **No headcount floor** (2026-09-29).
2. **`cap_per_group: 50`, no waves** (2026-09-29): one closely.io import file.
3. **A lane for every function** (2026-09-29).
4. **FAIL only for the wrong company, people who left, identity collisions, duplicates and people already messaged;** company-named profiles get an identity check (2026-09-29, 2026-10-07).
5. **Former employers may be named** (2026-09-29), within the Rules' limit.
6. **Live 3DLOOK pages may be linked as they are** (2026-09-29).
7. **No 3DLOOK client is named;** 34,000 scans without client or geography; 112,100 as 3DLOOK-wide scale; "3DLOOK has worked with 100+ clients", all-time (2026-09-29, 2026-09-30, wording 2026-10-07).
8. **A list Vadim brings has no company-researcher step** (2026-10-07).
9. **Franchise networks:** the franchisor is the buyer; units are referral paths under its canonical name (2026-10-07).
10. **Message 1 asks, Message 2 calls, in every campaign and every lane, referral included** (2026-10-07, «для всех»).
11. **`vadim` has no calendar account:** Message 2 ends with a soft ask, no link (`outbound-message2-template.md`).
12. **No compliance line in Australian cold copy** (2026-10-02, the default taken in `2026-08-14-au-digital-fitness` on Open question 6, never reversed).
13. **Card samples are not copy** (2026-10-07): card lines are targets.
14. **Messaged people stay excluded; re-entry is through new people only** (2026-09-28).

## Vadim's decisions 2026-10-11 (scope)

1. **Maximum use of the list:** «максимально використовуй контакти в списку». Every non-junk person at an IN account goes in, any function or seniority; OUT only for companies outside the ICP, competitors, junk rows (name collisions, unrelated businesses, single sites), duplicates, a US HQ, and people already messaged.
2. **The six registry-held brands are IN:** Fernwood Fitness, Fitstop, Sweat, Mosh, KIC and Hapana. The company-level registry exclusion (`2026-08-14-au-digital-fitness`, imported 2026-10-02; `2026-07-27-australia-telehealth` for Mosh) is **waived for this campaign only**. Person-level exclusion stays: nobody already messaged gets a second message (8 people in this export, all OUT). Coordinator's counts by cell: Fernwood 36, Fitstop 27, Sweat 6, Mosh 5, KIC 2, Hapana 1; after person-level exclusion, the name collision, duplicates and alias joins: Fernwood 38, Fitstop 33, Sweat 3, KIC 2, Mosh 1, Hapana 1 (78).
3. **Copy at those brands must not read as a first-ever introduction of 3DLOOK** and makes no claim either way about the earlier thread; new angles differ from the roles messaged before (Rules; `hooks-by-company.md`).
4. **Sender `vadim`, market Australia, product FitXpress.**

## Validation criteria (Step 2 will check)

No company research: step 2 is `companies.csv`; step 4 validates people against the persona.

- **Companies.** 40 rows (39 IN accounts and Mosh, HOLD only), aliases as above, `hq_country` Australia on every row, `icp_fit` high (19) or medium (21), source and the 2026-10-11 checks in `source_url` and `notes`, `registry_waived` on the six brands. `record` registers the companies of the people actually imported, never an OUT company, and Mosh only if Katerina clears Eamon H.
- **Registry.** `check --profile vadim` should flag the 8 already-messaged people (FAIL) and "company already worked from vadim" on people at the six waived brands (cleared by decision 2 above), and nothing else.
- **Displacement re-check** before import.
- **People.** 283 PASS before identity checks: P1 56, P2 16, P3 10, P4 201; lanes as in "Read this first". FAIL: the 12 fail-by-name rows. HOLD: the 3 hold-by-name rows. Identity holds as listed under the verdict table.
- **Message gate.** The Rules' Message 1 gate and "Message 1 asks, Message 2 calls", every lane; zero client names, pricing, `banned_terms`, compliance wording, prospect data or devices next to ours, outcome promises, app mentions at no-app accounts or at Anytime, BFT and Snap Fitness, cell-employer names, network-wide counts, first-introduction wording at the six waived brands. Referral messages at the nine large brands use that brand's topic bank within its quota. A failure, not a note: `2026-07-21` wrote 307 first messages with no product specific and drew 1 reply on 67 sends.

## Success metrics for this campaign

Closely event counters, as in `metrics-final.json`; read per segment.

| Metric | Target | Floor | Basis |
|---|---|---|---|
| Invites sent | 270 | 240 | 283 before identity checks |
| Connection acceptance | 20% | 15% | `vadim` July 17.3% |
| Replies per accepted person | 10% | 5% | July 13.2%; referral-heavy list |
| Positive replies from P1-P3 | 3 | 1 | 82 P1-P3 |
| Referral replies naming an owner or taking the call | 6 | 2 | 201 referral |
| Accounts with a reply | 8 of 39 | 4 | |
| Discovery calls | 3, different accounts | 1 in 8 weeks | |

**Falsified if** three or more P1 or P2 replies say members would not take a body scan on their phone, or that their in-club checks already cover it. **Inconclusive** if fewer than 30 people accept.

## Risks

1. **Referral weight:** 201 of 283 are referral, mostly franchise owners; buyer reach depends on unit owners pointing upward.
2. **Second touch at six brands:** the waived brands heard from Vadim in August; a new person there can read as pressure. Mosh has a live thread, so its one new person is on HOLD.
3. **Body image:** women's clubs and apps may hear a body pitch as aesthetic pressure.
4. **Ownership drift:** Fitness and Lifestyle Group is in a sale process; BFT, Planet Fitness Australia, Virgin Active Australia and Snap Fitness Australia have owners or parents abroad.
5. **Acceptance on `vadim`:** 17.3% in July.
6. **No nameable reference** in Australian fitness.
7. **In-club scanners:** five IN accounts offer a competitor's in-club body-composition scanner (Open question 9); owners there may see the phone scan as a duplicate.

## Open questions for Vadim

1. **Eight export people were already messaged from `vadim`** (Belinda Amis Wheaton, Olivia Houston, Chris Torcasio, Adam Koch, and four at Mosh), although `export-summary.md` says none was. They are OUT under your person-level rule. Nothing to decide unless you want them in.
2. **Ownership flags.** BFT (IP and US brand owned by Xponential Fitness, NYSE, since 2021; BFT stays master franchisor here), Planet Fitness Australia (Franchise Equity Partners, a US investor, since July 2026; management in Sydney), Virgin Active Australia (group HQ London, controlling owner Brait, South Africa), STRONG Pilates (one source places a US HQ in Los Angeles; LinkedIn and the app publisher are Australian), and, new in the fix round, Lift Brands APAC (Snap Fitness Australia): CEO APAC Chris Caldwell is based in Australia while Lift Brands' HQ is in Chanhassen, US; he is also a Fitstop non-executive director (Fitstop's head office was messaged on 2026-08-14), and copy to him covers Snap Fitness only. Default: all five IN on `vadim` (an Australian head office runs the Australian business). Move any to `nick` or `katerina`?
3. **HOLD pool (3 people, not sent by default).** Eamon H. (Mosh, Associate Creative Director): the CPO and the Medical Director replied interested in August and a call with Katerina was booked; he waits until Katerina, who owns the Mosh thread, says yes. Nikita Fernandes (SiSU Health, Head of Compliance, quality and regulatory) and Rhys Holleran (Viva Leisure, Chair): high-risk, low-yield referral touches. Send any of them?
4. **Head-office gaps.** No head-office buyer in the export at Vision Personal Training (9, all studio owners), STRONG Pilates (1) and Anytime Fitness Australia (the co-founder only, if both identity checks fail); only one at Fernwood (Director of Fitness) and Fitstop (Athletic Director), whose head offices were messaged in August. Default: no Apollo top-up (you asked to use the list). Top up Vision PT, STRONG and Anytime from the ```titles block?
5. **Weak fits and optional pools.** Kept at medium for maximum use: NovoFit (partnership only, capped at CEO Barry McDonald and founding director Adam Lewit), Your Reformer, Les Mills Asia Pacific, World Gym Australia (no current app), Ford Health. OUT under the distributor rule: NovoFit's Daniel Waide (COO, the strongest technology background: ex APAC GM of a digital-fitness content company) and Corey Eames-Mayer (Group COO), Tim Horskins (CEO, The Fitness Generation), Steven Molinaro (COO, Life Fitness Australia) and Gerard Healy (MD, Johnson Health Tech Australia). **Optional add-on pool, in-store supplement retail (13 people, OUT by default):** Australian Sports Nutrition 7 (Aydan Ballard, Head of Digital Operations; Simon Rees, Company Owner; Matt Rees, Director; franchise owners David Wilkie, Brett Read, Peter Reed and Danny Pearson), Mr Vitamins 3 (Garry Mortlock, CEO; Amy Imprasertsuk, Head of Retail; one owner row with an unusable name) and Go Vita 3 (Ann Cattelan, CEO; Jodie Smith, board; Nina Al-Bahrani, proprietor). Bring the pool in, as one partnership ask? The 36 people at product-only nutrition brands stay OUT (Swisse, BON CHARGE, Nutrition Systems and others, the EU 2026-10-07 rule).
6. **equ (3, Perth digital agency).** The export calls it Equilibrium; its site shows no health, fitness or wellness client. Default: OUT. Take it as a partnership ask (an agency that builds client apps)?
7. **41 alias people** (a franchise or board role on their own row, another employer in the cell: CBRE, Coles, a council, a realty firm): the 39 alias rows of the verdict table, which the first version counted as 37, and Mark Grey ("Collective Health and Wellness", CEO) and Lauren Anliev ("Director at ZENKIN and Collective Wellness CO"), name-alike OUTs in v1, now IN at Anytime pending an identity check against Collective Wellness Group. Both checks may fail: CWG's CEO was reported as Nicole Noye, and Lauren Anliev's row reads as a massage-education business. Default: IN with a current-role or identity check, send if it passes. Rick Coetzee (BHP, Fitstop owner) cannot be joined and stays OUT.
8. **Identity holds** (company-named profiles, no-name rows, Mel Burn and Melissa Burn at Fernwood as a possible single person, Sweat's two CEO titles). Default: current-role check, send if it passes, one profile per person.
9. **In-club scanner overlap.** A competitor's in-club body-composition scanner (Evolt 360) is offered at Jetts (preferred supplier since November 2023; 30 people), Genesis (rollout from 2022; 10), BFT (challenge scans; 23), Vision Personal Training (a branded studio scan; 9) and Goodlife at Fitness and Lifestyle Group (6). Fernwood's FIIT30 page says some members use body scans (38). Default: partial overlap, IN, with the phone capture for home and clubs with no device and the scanner never mentioned. Hold any of them?
10. **World Gym Australia and Viva Leisure.** Viva took a strategic investment in World Gym Australia and bought three World Gym locations (ASX announcement, 10 December 2024), lists it in its portfolio, and Harry Konstantinou sits on World Gym Australia's board. Default: two accounts (World Gym 6, Viva 14) with a never-mention rule both ways. Treat them as one group instead?

## QC fix round 2026-10-11 (QC 14/20)

QC report `workspace/_quality/outbound/2026-10-11-hypothesis-generator-au-sport-fitness.md` (14/20, marginal). The coordinator accepted every issue; the moves below are the coordinator's decisions, pending Vadim. The first version is saved as `hypothesis-v1-2026-10-11.md`. Status stays `draft`.

1. **Referral lane.** "Question themes" (4 generic themes) became "Question topics by brand": 6-8 topics each for Fernwood, Fitstop, Jetts, BFT, UBX, KX Pilates, Viva Leisure with Plus Fitness, REVL and Vision Personal Training, each tied to the brand's own model and the owner's role, written as targets. A theme may repeat at most about a fifth of a brand's referral people. New copy facts from each brand's own site, read 2026-10-11: FW3-FW5, FS2-FS4, BF2-BF4, JT3-JT4, UB3-UB4, VV2-VV4, KX2-KX3, RV2-RV4, VP2-VP4, SN1.
2. **`hooks-by-company.md`** now gives every IN and HOLD person a lane, tier and one anchor from the export (own clubs, multi-site ownership, background), with flags (alias, identity check, shared club, former employers that are accounts here).
3. **Own clubs carve-out.** The franchise rule now bans network-wide counts only; naming the person's own club or clubs is allowed.
4. **App dates, checked with the iTunes lookup `releaseDate` on 2026-10-11.** UBX Member App: first release 2026-09-11, so UB2 keeps "September 2026". Withdrawn because the date was a last update: REVL Training (first release 2026-03-30), The Yard Gym (2026-04-30), Planet Fitness Australia by Bravo Fit (2026-06-10), Virgin Active Australia (2025-07-13). RV1, YG1, PF1 and VA1 now only say the brand has its own app. The evidence line uses release dates. BFT's two apps are published by Xponential entities, and BFT now follows the same rule as Anytime: never "your app".
5. **Fernwood.** FW1 (FWD) is out of copy for everyone, the Director of Fitness included. It repeated the August angle and named Fernwood's own progress tooling. Fernwood gets FW3-FW5 and its own topic bank. FIIT30's page says some members use body scans, so that is a partial overlap.
6. **Coined phrases** ("between sessions", "progress moment", "same guided sequence", "body-progress record") are replaced with plain descriptions, worded differently each time. The rule on what the scan does not do is now a constraint with no quoted phrase. "Switched on for every club at once" had no source in `proof-points.md` and is cut.
7. **IN/OUT consistency (coordinator, pending Vadim).**
   - **In-store supplement retail:** one rule, OUT. Australian Sports Nutrition (7) joins Mr Vitamins (3) and Go Vita (3); the 13 are a pool in Open question 5.
   - **Distributors:** NovoFit stays IN, capped at CEO Barry McDonald and founding director Adam Lewit. Daniel Waide and Corey Eames-Mayer fail by name. The Fitness Generation alias was removed, so Tim Horskins is OUT. Life Fitness Australia and Johnson Health Tech Australia stay OUT: they are local sales arms of overseas manufacturers.
   - **Lift Brands APAC:** CEO Chris Caldwell is IN as the new account Snap Fitness Australia, under the Australian head-office default (Open question 2).
   - **Identity checks at Anytime:** Mark Grey ("Collective Health and Wellness") and Lauren Anliev ("ZENKIN") are aliases of Anytime with an identity check, no longer OUT by name.
   - **Mosh:** Eamon H. is on HOLD.
8. **Smaller fixes.**
   - The Use case is 34 words with no "so" result.
   - Nutrition Plus Ltd is relabelled as Louise Ormerod's duplicate profile.
   - The STRONG "120+ studios in 15 countries" figure had no source and is cut.
   - Segment E Your Reformer gets a Message 2 asset row.
   - A new Rule bans naming a person's cell employer when it is not the IN brand.
   - The SiSU Head of Compliance and the Viva Chair moved to HOLD.
9. **Found while fixing.**
   - Vision Personal Training has its own app (MyVision) and is no longer a no-app account.
   - Vision PT, BFT challenges, Jetts and Genesis offer a competitor's in-club scanner (Open question 9).
   - Viva Leisure holds a strategic investment in World Gym Australia (Open question 10).
   - Mel Burn and Melissa Burn at Fernwood may be one person.
   - Banned terms added: BIOSCAN, PXI, Myzone, menopause, perimenopause, money back.
10. **Totals after the round:** 283 IN, 3 HOLD, 100 OUT. 39 accounts IN, and 40 rows in `companies.csv`. Lanes: referral 201, product 40, operations 14, technical-integration 10, member-experience 9, partnerships 9. Tiers: P1 56, P2 16, P3 10, P4 201. The joins were re-run against the fixed `companies.csv`: 298 rows join, with no key collision.

## Sources

- Export `sales-nav-raw/export-1.csv` (stdlib `csv`) and `export-summary.md`; joins checked with `scripts/outbound-pipeline.py` (`company_keys`, `shortlist_keys`, `geo_profile`); registry `outbound-registry.py check --profile vadim` on the export (scratch output), `vadim-registry.json`, and the import files of `2026-08-14-au-digital-fitness` and `2026-07-27-australia-telehealth`.
- Ownership and status (searched 2026-10-11): [BFT and Xponential](https://www.businessnewsaustralia.com/articles/body-fit-training-to-pump-up-us-presence-through--60m-ip-sale-to-xponential-fitness.html) · [12RND to UBX](https://franchiseexecutives.com.au/12rnd-ubx-international-expansion/) · [Anytime Fitness Australia and Collective Wellness Group](https://www.ausleisure.com.au/news/anytime-fitness-australia-marks-18-year-milestone-and-sets-target-of-800-clubs-and-one-million-members-by-2030) · [Fitness and Lifestyle Group, owner and sale reports](https://www.ausleisure.com.au/news/reports-indicate-likely-fitness-and-lifestyle-group-sale) · [Bravo Fit acquired by Franchise Equity Partners](https://www.franchising.com/news/20260722_franchise_equity_partners_acquires_bravo_fit_planet_fitness_australian_fran.html) · [Virgin Active parent](https://www.cbinsights.com/company/virgin-active) · [Jetts buyout and BeWell Brands](https://franchiseexecutives.com.au/jetts-fitness-unveils-bewell-brands-adds-wellness-in-o-studio-deal/) · [Viva Leisure completes Plus Fitness](https://www.vivaleisure.com.au/news/news/viva-completes-acquisition-of-plus-fitness/) · [STRONG Pilates US expansion](https://athletechnews.com/strong-pilates-us-expansion-nyc-boston-los-angeles/) · [KX Pilates](https://franchiseexecutives.com.au/kx-pilates-unveils-new-training-program-as-it-ramps-up-expansion/) · [SiSU Health and Wesfarmers Health](https://www.sisuhealthgroup.com/press/wesfarmers-health-partnership) · [Recovr](https://athletechnews.com/recovr-raises-1-million-to-scale-ai-powered-retention-software-enter-us-market/) · [Fitness Passport, ALM August 2026](https://www.ausleisure.com.au/news/fitness-passport-chief-executive-advises-of-40-engagement-of-employer-partners-workforce-in-gym-programs) · [Move With Us, App Store](https://apps.apple.com/app/id1523442465) · [Goodlife in-club scans](https://www.goodlife.com.au/evolt360/) (context only).
- App Store Australia (iTunes search API, 2026-10-11): listing, publisher and last update per account in `companies.csv` notes. Fix round: first-release dates from `https://itunes.apple.com/lookup?id=<id>&country=au` (`releaseDate`) for every app named in copy or evidence, 2026-10-11.
- Brand sites read on 2026-10-11 for the fix-round facts: [Fernwood FIIT30](https://www.fernwoodfitness.com.au/why-fernwood/services/fiit30), [Fernwood first timers](https://www.fernwoodfitness.com.au/first-timers), [Fernwood personal training](https://www.fernwoodfitness.com.au/why-fernwood/services/personal-training) · [Fitstop: what is Fitstop](https://fitstop.com/au/what-is-fitstop/), [Global Games](https://fitstop.com/global-games/), [first timers](https://fitstop.com/au/first-timers/) · [BFT](https://www.bodyfittraining.au/), [PODIUM](https://www.bodyfittraining.au/bft_podium), [first timers](https://www.bodyfittraining.au/first-timers), [challenges](https://www.bodyfittraining.au/challenges) and [BFT³](https://www.bodyfittraining.au/bft3) (writer notes only) · [Jetts](https://www.jetts.com.au/), [ways to train](https://www.jetts.com.au/ways-to-train), [personal training](https://www.jetts.com.au/personal-training) · [UBX: what is UBX](https://ubxtraining.com/what) · [KX classes](https://kxpilates.com/au/classes), [KX own a studio](https://kxpilates.com/au/own-a-studio), [KX Life](https://kxpilates.com/au/kx-life) · [Viva Leisure](https://vivaleisure.group/), [Plus Fitness](https://www.plusfitness.com.au/) · [REVL programs](https://revltraining.com/programs/), [Race The Globe](https://revltraining.com/race-the-globe/) · [Vision PT](https://www.visionpersonaltraining.com/), [personal training](https://www.visionpersonaltraining.com/our-offering/personal-training), [strongHER](https://www.visionpersonaltraining.com/strongher) · [Snap Fitness Australia](https://www.snapfitness.com/au).
- Fix-round web checks (2026-10-11): [Evolt 360 and Jetts Australia, Active Management](https://activemgmt.com.au/evolt-360-expands-global-reach-signing-key-contracts-with-goodlife-fitness-canada-matrix-fitness-and-jetts-australia/) · [Evolt at Genesis](https://www.genesisfitness.com.au/blog/evolt-body-scanner-now-genesis) · [Lift Brands APAC CEO, Business Franchise Australia](https://businessfranchiseaustralia.com.au/news/lift-brands-evolves-leadership-team-accelerate-rapid-growth) · [Snap Fitness 350th APAC club](https://franchiseexecutives.com.au/snap-fitness-opens-doors-to-350th-aussie-club) · [Collective Wellness Group CEO change](https://franchiseexecutives.com.au/ceo-arthur-mccoll-to-exit-collective-wellness-group/) (identity check context only). Registries searched for Lift Brands, Snap Fitness, Anytime, Collective Wellness, NovoFit and the supplement retailers: no hits.
- Sites (HTTP status, 2026-10-11): 200 for every IN account's site except genesisfitness.com.au (403), fitnessinsideout.com (406, bot filter) and www.fordhealth.com.au (500; fordhealth.com.au 200); equ.com.au read for clients (none in health or fitness).
- Internal: `2026-08-14-au-digital-fitness/hypothesis.md` and `responses-summary.md`; `2026-07-27-australia-telehealth/responses-summary.md`; `2026-10-07-eu-weight-loss-nutrition/hypothesis.md`; `icp-detail.md` §1, §4, §8; `use-cases/fx-digital-fitness.md`; `proof-points.md`; `accuracy-formulations.md`; `compliance.md`; `competitors.md`; `outbound-message2-template.md`; `scripts/outbound_pack.py`, `scripts/outbound-pipeline.py`, `scripts/outbound-registry.py`.
