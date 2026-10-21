# Fix round 1 — mavie-work

QC scored the campaign's messages 10/20. This round regenerates every Message 2 and rewrites the Message 1s named below. Card rules still apply in full; the list below is what broke.

## How to work
1. Update `_grid-mavie-work.md` first: for every person fill the M2 value line again (tied to THIS person's M1 topic: what the scan would change in their own work), the easy-out target (only if the person is not the buyer, see rule 3) and a closer form. No cell shared by two people at the same company.
2. Regenerate EVERY Message 2 in `_batch-mavie-work.md` from the grid, person by person. Rewrite every Message 1 named in "Findings for your batch", and any other M1 whose opener, central question or product sentence matches a colleague's at the same company.
3. Run split-messages until exit 0. Then fix the lane counts in `_summary-mavie-work.md` from the script output (QC found them wrong). Then read every changed message in full once more, and stop with a 5-line report.

## Rules for this round (the same list goes to every batch)
1. **M2 = value, then the call.** One or two sentences of concrete value for this person, then the call offer and the calendar link. No label lead-ins ("For scale:", "So far:", "Offer:", "My offer is short.", "Some scale for context:", "For a founder, scale matters", "For growth work…", "Numbers help a decision like this.", "For a [role], X matters."). No stock closers ("Open to a call?", "Open to a short call?", "Worth a short call?", "Worth 15 minutes?"). **No call length at all** (no minutes, in digits or words).
2. **One closing ask per person, each in its own wording;** no two people at one company share a closing ask or an M2 opener.
3. **Easy out only for people who are not the buyer** (referral, partnership, or someone whose role does not own the topic). CEOs, founders, co-founders, owners, managing directors, general managers and heads of product never get "point me to whoever…" / "if X sits with someone else".
4. **Facts as full sentences of your own, with a verb.** Never a bare figure as a sentence ("112,100 scans in 2025 across all 3DLOOK customers." / "34,000 scans in 2025 at one platform." alone are banned). Keep the fact's own words inside your sentence (34,000 scans in 2025, at one platform; 112,100 scans in 2025, across all 3DLOOK customers). At most one figure per message, only where it supports the person's line; no two people at one company use the same fact sentence. "3DLOOK has worked with 100+ clients" at most once per company. Never add details to the anonymised 34,000-scan platform (no "own app", "web link", "own phone").
5. **Speed phrase only where speed is the point,** as its own sentence in the card's words ("under 45 seconds from the photos to structured results"); never a trailing clause after the 80+ sentence.
6. **No integration-time figure** ("2-4 weeks" or any other). The card's proof-points block offers it, but the campaign rule bans it and the campaign rule wins.
7. **Compliance line:** at most one, in Message 2, BEFORE the calendar link. `product` / `operations` / `technical-integration`: optional; use it only where the M2 is about member data, integration or rollout, and then verbatim the UK / EU line: "In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs." `clinical`: "FitXpress is not a medical device." `referral` / `partnership`: none.
8. **Never copy lane notes, account facts or rule sentences.** These must not appear anywhere: "nothing to ship, stock or install", "standardized, timestamped body record … for the team to review", "a partner capability … has a place in what they offer", "repeats the check every six months", "Once a baseline exists, members book follow-up tests", "frames the check as yearly", "shown only where the programme chooses", "a scan … a member app can ask for".
9. **Cross-company templates are banned too** (other batches had them): the clinical M1 sentence about a standardized, timestamped body record for the team; the founder product M2 "[For X], FitXpress is white-label through API or SDKs… 100+ clients… GDPR… call?"; the technical M1 pair "REST API with API-key authentication. Two photos go in, and 80+ … come back"; the core sentence "a guided two-photo scan returns 80+ body measurements" (write the product line for this person, in your own words); the question "what do members ask between check-ins" and "web, native, or both?".
10. **No triple parallelisms** ("X, Y and Z" lists of three verbs or benefits). **No fragment openers** ("Got me thinking, …", "Made me think, …", "Noticed your background, …", "Quick thought as [title] of [company]", "Couldn't help but ask," without a question). A hook phrase is used at most once in your batch. No career-recap openers ("you went from X to Y") for more than one person per company.
11. **Assets only as the card names them:** Aeon = customer portal (not "Aeon app"); Ahead Health = online health report (not "Ahead app"); Axo Longevity = member platform (not "Axo app"); Mavie: no "Mavie Work app"; name the unit the person works for. CARE is written "care" (the brand on its site and app).
12. **Body measurements are measurements;** only body composition values are estimates. Never offer body composition to AYUN (its on-site analysis is on the card's Never list).
13. **Greeting:** the person's first name as written in the profile, accents kept (e.g. "Hi Jérôme,").
14. Nothing about the sender that is not true: Olena is not a founder and not a Head of Product.

## Findings for your batch (QC, verbatim)

### mavie-work (17)
- `janine-wagenlechner` M1 and `doris-busek-baum-7606b4131` M1: same product sentence at one company ("nothing to ship, stock or install", lane note copied, a triple).
- `janine-wagenlechner`: the M1 hook "Couldn't help but ask," is not followed by a question. The M2 says "Teams run the guided sequence" (members run it, and the wording is lane copy). The M2 has no value line.
- `christophbodenstein` M1 and `johanna-resch-connect` M1: same product sentence at Mavie Next (web link, no app build, 80+).
- `drmeghabhola` M2 and `johanna-resch-connect` M2: same construction at Mavie Next ("If a … needs a body record step").
- `ondrejgandel` M2 and `victoria-sobulska-b5b7a0167` M2: same central argument ("ready part").
- `ondrejgandel` M1 and `vera-brockherde-9a8240126` M1: same product sentence ("a scan … a member app can ask for", lane copy).
- `lukas-mayrl-7093029b` M1 and `vedran-bijelac-00472714a` M1: same central question (what decides a new feature or element joining the Mavie offer).
- Openers at one company: 8 of 17 are "you went from X to Y" career recaps (`lukas-mayrl-7093029b`, `ondrejgandel`, `lea-paradzik`, `drmeghabhola`, `christophbodenstein`, `victoria-sobulska-b5b7a0167`, `johanna-resch-connect`, `doris-busek-baum-7606b4131`).
- `jasmin-cohen2`: the hook (#ThereIsNoBodyB) is stated and dropped, and the M1 has no Mavie Work fact. The M2 opens with "For growth work, scale helps."
- `vedran-bijelac-00472714a` M2: "Numbers help a decision like this." M1: no Mavie fact.
- `victoria-sobulska-b5b7a0167` M1: "partner part" is unclear, plus the triple above. The question ("Which Mavie venture has its members at home most of the time?") has nothing to do with her work.
- `andrea-grandits-42782b101` M2: "whoever owns the Mavie Work app" refers to an app the card does not confirm. She is product P2, so the easy out is not needed.
- `lea-paradzik`: the M2 easy out goes to the owner herself (Head of Product, MavieMe). M1 calls MavieMe "an app"; the card describes home tests and online consultations. The M2 also has the speed phrase as a dangling clause.
- `doris-busek-baum-7606b4131`: writes "Mavie work" in lower case. The M2 has no value line.
- `vera-brockherde-9a8240126` M1: "shown only where the programme chooses" is the 3D-model rule sentence, applied to measurements. The M2 has no value line.
- `nicolas-haffner-a5783460` M1: "80+ body measurements as estimates". Body measurements are not estimates; body composition is.
- `drmeghabhola`: the Covid-facilitator hook is unrelated to her product role. The M2 phrase "without a capture flow of its own" is unclear.

## Campaign-wide QC lines that name your people (only your people apply)

- Assets the card does not confirm: `serge-weydert` "the Aeon app" ×2 (the card says customer portal), `svenjaeschke` and `vinsensius-vega` "the Ahead app" (card: online health report), `tangsergio` "the Axo Longevity app" (card: member platform), `andrea-grandits-42782b101` "the Mavie Work app".
- Triple parallelisms (the M1/M2 template bans them): `pauline-sauvaget` and `alice-conques` ("needs nothing to ship or install, runs the same way on any phone, and returns…", the same sentence at two companies), `joelgrajcer` ("tests, explains and coaches"), `svenjaeschke` ("a baseline, a plan and referrals"), `victoria-sobulska-b5b7a0167` ("takes two photos, returns 80+ … and is white-label"). The lane-note triple "ship, stock or install" adds 6 more.
- The speed phrase is tacked onto the end of the product sentence as a dangling clause, "returns 80+ body measurements, under 45 seconds from the photos to structured results", which reads as if the measurements take under 45 seconds. This happens in 21 messages: `lukas-mayrl-7093029b`, `lea-paradzik` (M2), `serge-weydert`, `ionhaab`, `maximeberthelot`, `jürgen-mehrtens-116303b1`, `alexandre-hollard`, `dennishermann`, `andrew-mccarthy-impact-entrepreneur`, `peterpaul-deleeuw`, `kate%c5%99ina-vrbov%c3%a1-22bb7620a`, `khadija-benmansour-2535b7a8`, `joanna-bensz-205b315`, `magdalena-winnicka-b08972313`, `massimo-pietracaprina-a528951`, `oliks`, `gemmafrenchman`, `hannah-whitcombe-b2b35866`, `peter-roland-737ab34`, `bruno-marco-dufort-224358162`, `eddy-van-b323a9a`.
- The best pairs (`vinzenzweber`, `evakuttichova`, `bdebever`, `julien-montier`, `pauldupuy89`, `cezarneaga`, and the `alexandre-hollard` M1) show what the persona fit should look like.

## Coordinator's scan hits in your batch

  fragment-112100 1 : christophschnedlitz


## Also
- `nicolas-haffner-a5783460`: he works at Mavie Med (UNIQA's private clinics), not Mavie Work; write him at Mavie Med.
