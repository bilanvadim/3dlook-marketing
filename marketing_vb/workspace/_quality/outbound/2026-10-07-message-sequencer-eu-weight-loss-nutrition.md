---
qc_date: 2026-10-07
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-07-eu-weight-loss-nutrition/messages/ (samples andresantos-nutrium.md, arnaud-marche-923259123.md, massimo-caprino-8bab5.md; _check.json; 7 _summary-*.md; _batch-rnpc/-dietplus/-bodyhit.md read in full against their _profiles; _batch-mixed-2/-3.md read in full; _batch-mixed-1.md lines 1-320; _batch-mixed-4.md grepped)
track: outbound
artifact_type: messages
total_score: 10/20
status: failed
coordinator_review: pending
---

# QC Report: message-sequencer, 2026-10-07, eu-weight-loss-nutrition

**Artifact:** `workspace/outbound/campaigns/2026-10-07-eu-weight-loss-nutrition/messages/` (209 people, 7 batches)
**Total: 10/20, failed.**

**Verdict.** The mechanics are clean. The gate shows 0 hard findings. Every M1 I read ends on a question, with no call ask and no link. Every M2 has the calendar link, and every referral M2 has an easy out.

The campaign's main risk did happen. RNPC (30 people), Dietplus (27) and BODYHIT (22) each collapsed into one skeleton:
- **M1:** one context line, then "A (guided) scan [from a link the centre sends] returns 80+ body measurements [in under 45 seconds]", then a question built on one of three or four stems.
- **M2:** "[call offer] 15 minutes: link", then "If … head office, point me to whoever looks after client follow-up / member experience (there)".

Three more problems sit on top of that:
- one hook built on a recipient's own obesity history (philippe-l-2914a1130);
- one prospect figure that is not in proof-points.md;
- "100+ clients use FitXpress (today)" in 14 messages.

**Recommendation.**
1. Fix philippe-l-2914a1130 first.
2. Regenerate RN, DP and BH from a per-person variation grid. The grid should assign each person a product fact, a question theme and a closer form *before* writing.
3. Line-fix the mixed batches using the list below.

**Scoring basis.** As in the r3 UK report: scored against `card-messages.md` and `_profiles-*.md`. Limits, signature, bans, detector and completeness are taken from the gate as fact. The missing `product:` in the split files is a script format and is not capped.

Batch abbreviations used below: RN = `_batch-rnpc.md`, DP = `_batch-dietplus.md`, BH = `_batch-bodyhit.md`, MX1-MX4 = `_batch-mixed-1..4.md`. Numbers are line numbers in the batch file.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 2 | 5 |
| C | Brand & tone | 1 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 2 | 4 |

## Contract check ("Message 1 asks, Message 2 calls")

- **M1 ends on a question, with no call ask and no link:** holds in every batch I read in full (RN, DP, BH, MX2, MX3) and in MX1 lines 1-320.
- **M2 has the calendar link:** 209/209, per the gate.
- **Easy out for non-buyers:** RN 27/27 referral, DP 23/23, BH 21/21.
  - Missing for damien-cacaret (RN:53-55). He is in the product lane, but his profile says it is not known whether he sits at head office or at a centre.
- **Link hygiene.** In 8 M2s the calendar URL runs straight into a full stop or the next sentence, and LinkedIn may fold the full stop into the link:
  - shadi-marie-le-maout-13488758 MX2:243
  - silviaojedavalenzuela MX2:393
  - hanna-blisnjuk-4b7748160 MX2:410
  - mattijs-keess-903b7469 MX2:598
  - bas-harmsen MX2:615
  - fabrice-g MX2:632
  - mischacohn MX1:269
  - kevin-johnston-0708537 MX1:291

## Per-company skeleton (franchise pools)

### RNPC: 30 people, 27 referral. Mail-merge risk: HIGH

- **Openers:** varied. The exception is the "you (will) know …" presumption in nicolas-charpentier :121, louisdenazelle :140, thomas-hervé :482 and cécile-troisgros :501.
- **Product sentence:**
  - "A guided scan" opens about 22 of 30 product sentences.
  - "from a link / web page the centre sends" appears in 24 of 30.
  - All 30 cite the same fact pair (two photos, 80+ body measurements). That fails prompt item 3: different facts for different people at one company.
  - Twins:
    - nicolas-charpentier-87901546 :121 / cynthia-grosbois-4a6017135 :368, "A guided scan, two photos from a link the centre sends, returns 80+ body measurements".
    - karine-le-meaux-53858983 :235 / fannysoleil :330, the same sentence with "web page".
    - paul-de-castries-2a823146 :159 / sandra-fontalba-5a22a5136 :406 / laurent-dagieu-627022249 :444, "A guided scan from a link the centre sends returns 80+ … from two photos".
    - nadège-pilat-b97256110 :292 / cécile-troisgros-8a8b16263 :501 / beatrice-mailly-358a82273 :539, "A guided scan from a link the centre sends adds / can fill …".
    - thierry-bernabe :463 / ivan-dombes-0b8031399 :558, "A guided scan, sent as a link …, needs/takes two photos and returns 80+ … in under 45 seconds".
    - patrick-gaytte-8b009b122 :7 / rémy-legrand-20507386 :28, "The client takes/opens it from a [web page/link] the centre sends."
- **Central question twins:**
  - nathalie-moreau-a029a231 :85 / nadège-pilat :294: what the dietitian has in hand before the client comes in.
  - philippe-monlauzeur-71bb9645 :104 / delphine-thierry-7041a4a5 :313: follow-up after the programme has ended.
  - karine-le-meaux :237 / thierry-bernabe :465: introducing something new to a client.
  - laurent-dereudre-58961710a :275 / thomas-hervé-7b6003213 :484: training on a new tool.
- **M2 openers:**
  - "15 minutes" appears in 30/30.
  - "I can show the [capture / scan] (to you) in 15 minutes" appears in nathalie-moreau :91, valérie-guigou-0a831b57 :186, beatrice-mailly :547 and gwénaëlle-queguiner-08996a136 :395.
- **M2 proof sentence:** "112,100 scans ran in 2025 across all 3DLOOK customers" appears word for word ×6: patrick :15, nathalie-moreau :91, paul :167, karine :243, fannysoleil :338 and laurent-dagieu :452.
- **Closers:**
  - 21 of 27 are "If [this/it] [sits/belongs/is] … head office, …".
  - Exact stem "If this belongs with head office": nicolas :131 / gwénaëlle :397.
  - "a pointer is welcome": valérie :188 / ivan :568.
  - "whoever looks after client follow-up" ×9: corinne-brunet-a330b965 :74, philippe-monlauzeur :112, nicolas :131, louisdenazelle :150, corinne-malitte-46b601122 :207, cynthia :378, sandra :416, thierry :473 and cécile :511.

### Dietplus: 27 people, 23 referral. Mail-merge risk: HIGH

- **Context line:** the DP1 fact is restated almost verbatim in about 18 of 27 M1s.
  - amandine-poirier-423b16350 :455 matches natacha-alonso-valckx-35888b100 :7, and both match the card's DP1.
  - The same restatement appears in isabel-barreto-… :209, benjaminhoresnyi :101 and valéry-leprevots-04a9ab35b :495.
  - damien-haessler-099693121 :145 / nathalie-peron-6878ab92 :229 are twins on "[A] coach at Dietplus [town] sees clients every week, after (the) free first assessment" (the gate flags this pair too).
- **Product sentence twins:**
  - fabien-rolland-434a37148 :333 / amandine-poirier :455 are identical except for "phone".
  - isabel :209 / jeanne-guigui-963698150 :353 / valéry :495 / dietplus-la-roche-sur-foron-094426267 :415, "A scan from two photos … 80+ … from a link the centre sends".
  - cristine-baumert-040781353 :475 / daphne-cierniak-100558425 :535 / nathalie-peron :229, "Two (phone) photos (from the client's phone) give … in under 45 seconds".
  - benjaminhoresnyi :103 / natacha :9, "A client can take two photos from a link the centre sends".
  - damien-haessler :145 / hélène-bellod-642366172 :311, "We built a scan that fits that rhythm / that welcome".
- **Question twins:**
  - samya-mikou-8833a2140 :293 / gaelle-aveline-330b867b :171: going over the previous week.
  - sophie-canoen-loucheur-982357314 :397 / johanna-yung-19b890330 :517: what to go through at each session.
  - natacha :11 / magali-le-gendre-8296b2120 :127 / daphne :537: what clients do between weekly visits.
  - cristine :477 / nathalie-dourdoigne-15b574173 :557: a client who skips a week or comes back after a gap. This pair also carries adherence framing.
- **Closers:**
  - The "client follow-up" pointer closes 21 of 23 referral M2s.
  - The exact clause "point me to whoever looks after client follow-up there" appears ×6: damien-haessler :157, isabel :219, hélène :321, fabien :343, la-roche :425 and daphne :545. sophie-canoen :405 is the same clause without "there".
  - "tell me who looks after client follow-up there": magali :135 / valéry :505.
  - This is the card's example sentence (card:78), copied.
- **M2 openers:** "15 minutes" appears in 27/27.

### BODYHIT: 22 people, 21 referral. Mail-merge risk: HIGH

- **Openers:**
  - "Noticed …" ×5: chloetraina :28, killian-chotard-758672167 :133, corentin-bernard-47b65723b :259, angelo-phirate-86767131b :364 and hassatou-diallo-92b459170 :406.
  - chloetraina / angelo-phirate both open "Noticed your background in …" (exact).
  - "[Quick note / Quick idea / Short note / A short one] for the [main] manager of a BODYHIT [studio/club]": raphaëla-capelle-88a711196 :70, françois-xavier-quéré-82a0a517b :175, lila-sodano-139852256 :196 and juline-boulanger-368487141 :448.
- **Product sentence twins (16 of 22 people):**
  - stéphanie-teixeira-44975716b :154 / jan-alan-96385423a :280 / anna-dhervillers-491a8628b :343 share the exact clause "A scan from two photos gives 80+ body measurements in under 45 seconds".
  - chloetraina :28 / virginie-bourgerie-978a4720b :301, "FitXpress lets a club offer … 80+ … and a 3D model".
  - corentin :259 / antoine-cormier-266bb1433 :385, "FitXpress gives a club a scan from two photos … and a 3D model".
  - patricia-gouedard-411015132 :91 / audrey-boussin-473997223 :217, "FitXpress gives/adds a … two-photo scan with 80+ … and a 3D model".
  - raphaëla :70 / killian :133 / ines-h-344686185 :427, "FitXpress is a scan a member takes …".
  - lila :196 / juline :448, "… in under 45 seconds, under the club's own brand".
- **Questions:** 13 of 21 are about member progress, built on three stems:
  - chloetraina :30 / raphaëla :72 / quentin-fabre-08164b27b :324: what members see of their progress.
  - julie-lacoste-5aa27584 :51 / patricia :93 / audrey :219 / antoine :387: going or talking through progress with a member.
  - killian :135 / corentin :261 / juline :450: what you show or tell a member, or what members ask.
  - **jan-alan and antoine-cormier run the same club** (Guérande / La Baule / Pornichet), so they will compare.
- **M2:**
  - "112,100 scans were run in 2025 across all 3DLOOK customers" ×4: julie :57, killian :141, quentin :330 and ines :435.
  - "3DLOOK has 100+ clients" ×3: françois-xavier :183, virginie :309 and angelo :372.
  - "Calendar:" ×3 and "Grab a slot:" ×2.
- **Closers:**
  - chloetraina :40 / ines :439 are near-exact: "If this sits with head office, point me to whoever looks after member experience".
  - julie :61 / antoine :397: "new member services … head office".
  - lila :208 / juline :460: "member services".

## Sensitive hooks

- **philippe-l-2914a1130, DP:31: "Your own story behind Dietplus stayed with me."**
  - His profile bio (`_profiles-dietplus.md`:21) reads: "Ancien obèse, Je sais ce que c'est de perdre confiance en soi, de ne plus oser s'habiller ou ne plus vouloir être pris en photos…" ("Formerly obese, I know what it is to lose self-confidence, to no longer dare to dress or want to be photographed…").
  - The hook points straight at his weight history. The next paragraph then pitches a **two-photo** body scan.
  - The summary flagged it ("sensitive hook") but the message was not changed. **Fix first.**
- I grepped all 7 profile files for weight, obesity and health-history terms. No other personal-health bio was used.
- Lower risk:
  - sophie-canoen DP:393 turns a mental-health first-aid credential into flattery.
  - hassatou-diallo BH:406 hooks on her esthéticienne training, and the card bans beauty claims for BODYHIT.

## What was wrong (specific)

### A. Adherence: 3/5

- **Card:144 uniqueness rule** ("No two people at one company share an opener, a central question, a closing ask, a Message 2 opener or a product sentence") fails in RN, DP and BH (above). So does prompt item 3: different facts for different people at one company.
- **Speed wording (card:154, "one public definition").**
  - About 112 messages use an "in under 45 seconds" variant (gate soft).
  - `_summary-mixed-1`:12 asks Vadim whether to apply a rule the card already states.
  - magali-le-gendre DP:125 says "within 45 seconds".
- **Clinical lane (card:74) requires the repeatability sentence.** jean-jacques-houben-2a40b160 (DP:79-91) has none.
- **Writer notes copied into copy (card:35):**
  - jacques-ley-8a5818148 DP:55 reuses the card:39 writer note, "a capability head office can switch on for every centre at once".
  - sophie-canoen DP:403, "a short and neutral walk-through", comes from card:78 "short and neutral".
- **"Never pitch a unit to adopt anything" (card:149).** These lines make the unit the operator or owner:
  - damien-haessler DP:145, "from a link you send"
  - sophie-canoen DP:395 (same)
  - nathalie-dourdoigne DP:555, "from your link"
  - julie-lacoste BH:49, "A club can add a scan"
  - antoine-cormier BH:393, "carries the club's own look"
  - lila BH:196 and juline BH:448, "under the club's own brand"
  - damien-rollin BH:246, "a club's own app"
- **Colleagues and group owners (card:144, :150):**
  - "colleague" at head office: nadège-pilat RN:302, katerina-abaeva-298212190 DP:383, johanna-yung DP:525.
  - angelique-rodrigues-b07a852a5 DP:445 asks her to "introduce me", which implies head office will hear about the message.
  - cécile-troisgros RN:511, "your time at the group", points at the group owner.
- **"Name the company in every Message 1" (card:144):** antoine-cormier BH:385, hassatou-diallo BH:406 and ellie-heath-6704b422 MX3:325. All three are gate soft notes that were left unfixed.

### B. Factual accuracy: 2/5

- **Cap applied.** quentin-fabre BH:322, "someone who trains 20 minutes at a time", is a prospect figure. Card:154 bans prospect figures, and the number is not in proof-points.md.
- **"100+ clients use FitXpress (today) / already use it / the scan" ×14.**
  - In proof-points.md, 100+ is the all-time 3DLOOK total from the company deck, across both products. The present-tense claim about FitXpress use has no source; internally, the 2025 active count is 67.
  - Affected messages:
    - nicolas-charpentier RN:129
    - nadège-pilat RN:300
    - thomas-hervé RN:490
    - beatrice-mailly RN:547
    - valeriadinatale MX2:167
    - jc-heyneke MX2:279
    - pbraam MX2:427
    - giuliamarinelli MX2:560
    - josecarlosalves MX3:657
    - mischacohn MX1:267
    - todd-peavey-5a00703 MX1:311
    - jean-maurice-pohl-ab2806bb MX1:447
    - sanja-kuche-80203822b MX1:513
    - ilija-bozic-b7165532a MX1:605
  - ericleddin MX1:113 ("work with 3DLOOK") and susanne-burger MX1:159 phrase it acceptably.
- **Invented RNPC facts.** The card gives only RN1 and RN2:
  - ivan-dombes RN:558, "with a doctor's recommendation or on their own", **contradicts RN2**.
  - beatrice-mailly RN:539, "the next step is booked"
  - laurent-dagieu RN:444, "a city centre where clients come in by appointment"
  - gwénaëlle RN:387, "often have questions about what comes next"
  - paul-de-castries RN:159, "you see clients … only through the follow-up"
- **Embellished proof and product claims:**
  - damien-cacaret RN:53 adds "all captured by the client on a phone" to the 34,000 line.
  - simon-hamer9 MX2:260 adds "which shows how often a scan gets used inside an app".
  - corinne-malitte RN:205, "I can show the setup", implies showing the anonymised client's setup.
  - nathalie-moreau RN:91, "so the sequence is well used"
  - thomas-hervé RN:490, "the training on our side is short"
  - angelo-phirate BH:372, "so partners can see how others use it"
  - louisdenazelle RN:140, "The scan we built for RNPC-type programmes"
  - jan-alan BH:280 invents seaside seasonality.
  - killian BH:133, "a 3D model of the result", implies an outcome.
- **What holds:**
  - No client names, no pricing and no medication.
  - No "app" in RNPC, Dietplus, Naturhouse or Ysonut copy.
  - The GDPR sentence and "FitXpress is not a medical device." are verbatim.
  - The repeatability wording matches §1.2.
  - 96-97% never appears in a sentence with body composition.

### C. Brand & tone: 1/3

- **philippe-l DP:31**, above. This is the notable lapse.
- **Presumed reaction ("you (will) know …", "you will weigh …") ×26 across the batches**, for example:
  - andresantos-nutrium MX3:529 and arnaud-marche-923259123 MX2:45
  - olga-donica-19753744 MX2:102, salvatoretipaldi MX2:476, paulo-cudjo-26b060157 MX2:514, celiazouggagh MX2:216, vincentvreugdenhil MX2:328
  - fumi-f-29a048153 MX3:193, hannahpearman MX3:345, tomlionelfuller MX3:303, asergioacosta MX3:573
  - saemundur-oddsson-md-148867115 MX1:31
  - katia-gabarroca-759509139 DP:269, fabien DP:331, jacques-ley DP:55
  - stéphanie BH:154, damien-rollin BH:238, hassatou BH:406, antoine BH:385
  - the four RNPC cases listed above
- **"so" introducing a benefit (card:157)** ×4:
  - nathalie-moreau RN:91
  - victor-keunen MX2:317
  - audrey-boussin BH:225
  - angelo-phirate BH:372
- **Flattery and clichés:**
  - valérie-guigou RN:178, "says it all"
  - angelique DP:435, "prepare you well"
  - sophie-canoen DP:393, "show how carefully you follow clients"
  - hélène DP:311, "Welcoming people is a skill"
  - katerina-abaeva DP:373: the tea-shop hook reads as condescending.
- **Tricolon:** magali DP:125.
- **"let" as a capability verb** (terminology guardrail; the detector missed it):
  - chloetraina BH:28 and virginie BH:301, "lets a club offer"
  - fr%c3%a9d%c3%a9ric-julien-190b9932 MX3:367, "could let a client record"
- **Hard to parse for second-language readers:**
  - massimo-caprino-8bab5 MX2:7, "many teams read the same guest"
  - natacha DP:17, "taken at home and in front of the coach"
  - sylvie-plichta-77069a164 BH:114: the question has no clear purpose.
  - manuela-abreu1 MX3:593, "a dietitian could compare two scans it selects"

### D. Format & structure: 2/3

- quentin-fabre BH:320/:328 greets "Hi quentin," in lowercase. Every other lowercase first name was capitalised.
- The calendar URL is glued to a full stop or the next sentence in 8 M2s (see the contract check).
- **The speed phrase is pasted into sentences that already say "results":**
  - andresantos MX3:531, "results come in under 45 seconds from the photos to structured results"
  - elisa-stoosz MX4:39, "structured results … to structured results"
  - romana-krčmářová-157704b7 MX4:337 adds a product fact after the pointer.
- **Summaries:**
  - `_summary-mixed-3`:4 gives angle counts that add up to 34 for 33 people (referral is 13).
  - No summary reports the product-sentence, question or closer twins. They mention only the gate's near-duplicate notes.
- The missing `product:` in the split files is not capped (script format).

### E. Output quality: 2/4

- **Good:**
  - The hooks I checked against the profiles are real: andresantos (software engineer), arnaud-marche (three countries), massimo-caprino (four pillars), rémy-legrand, damien-cacaret (Autonomia), corinne-brunet, louisdenazelle, benjaminhoresnyi (Urgo), damien-rollin, simon-hamer9, jmhellendoorn and fntneves.
  - massimo-caprino and fntneves are reference-grade.
  - RNPC copy is sober, mentions no app and uses RN1/RN2 well in rémy-legrand and delphine-thierry.
- **The franchise skeleton (above).** In all three networks, a screenshot forwarded between two owners will read as one template.
- **M2 = call plus legal boilerplate.**
  - The GDPR sentence is in 11 of 13 Clinique La Prairie M2s, 7 of 9 FitForMe, 8 of 8 Nutrium and 9 of 9 Liva.
  - Some M2s carry no value line at all: andresantos MX3:539-541, arnaud-marche MX2:53, erick-ribeiro-919337183 MX2:186 and rebecca-chia-lung-chang-v-23bb2b394 MX2:205.
  - At Clinique La Prairie this clashes with card:43, "luxury, discreet tone". The line is allowed ("at most one") but not required.
- **Two compliance sentences in one M2** (the GDPR line plus the medical-device line): massimo MX2:15, jean-jacques DP:91, fumi MX3:205, manuela MX3:603, ellie MX3:335 and saemundur MX1:41/:45. Card:152 says "at most one"; see the system notes.
- **Twins outside the franchise pools:**
  - Virtuagym: pbraam MX2:421 / mattijs-keess :592 share "Does a capability like that have (any) place …".
  - Sidekick partnership: mischacohn MX1:257, kevin-johnston :279 and todd-peavey :301 share the SK1 sentence and the "partner capability like that" question.
- **Adherence, retention or trial framing aimed at units:**
  - ines BH:429, "keep members coming back"
  - ines BH:435, "simple to try out" (card:159 bans trial terms)
  - cristine DP:477
  - nathalie-dourdoigne DP:557

## Line-level fixes per person_id

### RN (`_batch-rnpc.md`)

- **patrick-gaytte-8b009b122:** :7 the link clause twins rémy. Use the verbatim speed phrase.
- **rémy-legrand-20507386:** :28 the link clause twins patrick.
- **damien-cacaret:**
  - :53 drop "all captured by the client on a phone".
  - Add an easy out (his seat is unknown).
- **corinne-brunet-a330b965:**
  - :74 replace the card example closer with her own.
  - :72 use the verbatim speed phrase.
- **nathalie-moreau-a029a231:**
  - :91 drop "so the sequence is well used".
  - :85 the question twins nadège.
  - :91 the M2 opener twins beatrice.
- **philippe-monlauzeur-71bb9645:** :104 the question twins delphine.
- **nicolas-charpentier-87901546:**
  - :129 use the card's "100+ clients" (3DLOOK), not "use FitXpress today".
  - :121 the product sentence twins cynthia, and "you will know" is a presumption.
  - :131 the closer stem twins gwénaëlle.
- **louisdenazelle:** :140 drop "we built for RNPC-type programmes" and the "you know" presumption.
- **paul-de-castries-2a823146:**
  - :159 drop the invented "only through the follow-up".
  - :159 the product sentence twins sandra and laurent-dagieu.
  - :167 the 112,100 sentence is one of six copies.
- **valérie-guigou-0a831b57:**
  - :178 drop "says it all".
  - :186 use the verbatim speed phrase.
  - :188 the closer twins ivan.
- **corinne-malitte-46b601122:** :205 drop the "show the setup" implication.
- **karine-le-meaux-53858983:**
  - :235 the product sentence twins fannysoleil.
  - :237 the question twins thierry.
  - :243 the 112,100 sentence is a copy.
- **laurent-dereudre-58961710a:**
  - :273 drop the generalisation "a new tool only works if…".
  - :275 the question twins thomas.
- **nadège-pilat-b97256110:**
  - :300 fix the 100+ wording.
  - :302 drop "colleague".
  - :294 the question twins nathalie-moreau.
  - :292 the product sentence twins cécile and beatrice.
- **delphine-thierry-7041a4a5:** :313 the question twins philippe-monlauzeur.
- **fannysoleil:**
  - :330 the product sentence twins karine.
  - :338 the 112,100 sentence is a copy.
- **cynthia-grosbois-4a6017135:**
  - :368 the product sentence twins nicolas.
  - "you choose which scans to compare" makes the unit the user.
- **gwénaëlle-queguiner-08996a136:**
  - :387 drop the invented client behaviour.
  - :397 the closer stem twins nicolas.
- **sandra-fontalba-5a22a5136:** :406 the product sentence twins paul and laurent-dagieu.
- **laurent-dagieu-627022249:**
  - :444 drop the invented "by appointment".
  - :444 the product sentence is a twin.
  - :452 the 112,100 sentence is a copy.
- **thierry-bernabe:**
  - :463 the opener has no content.
  - :463 the product sentence twins ivan.
  - :465 the question twins karine.
- **thomas-hervé-7b6003213:**
  - :490 fix the 100+ wording and drop "training on our side is short".
  - :484 the question twins laurent-dereudre.
  - :482 "you know" is a presumption.
- **cécile-troisgros-8a8b16263:**
  - :511 drop "your time at the group".
  - :501 the product sentence is a twin.
- **beatrice-mailly-358a82273:**
  - :539 drop the invented "next step is booked".
  - :547 fix the 100+ wording.
  - :547 the M2 opener twins nathalie-moreau.
- **ivan-dombes-0b8031399:**
  - :558 drop "or on their own" (it contradicts RN2).
  - :558 the product sentence twins thierry.
  - :568 the closer twins valérie.

### DP (`_batch-dietplus.md`)

- **philippe-l-2914a1130:** :31 replace the hook with a role-based one (President of the franchisor). Nothing from the bio. **First.**
- **natacha-alonso-valckx-35888b100:**
  - :7 the DP1 restatement twins amandine.
  - :17 "at home and in front of the coach" is muddled.
- **jacques-ley-8a5818148:** :55 remove the writer-note line and the "you know" presumption.
- **jean-jacques-houben-2a40b160:**
  - Add the clinical repeatability sentence.
  - :91 has two compliance sentences.
- **benjaminhoresnyi:**
  - :103 the product sentence twins natacha.
  - :113 the closer is in the family.
- **magali-le-gendre-8296b2120:**
  - :125 "within 45 seconds", the tricolon and "her phone".
  - :127 the question twins natacha and daphne.
  - :135 the closer twins valéry.
- **damien-haessler-099693121:**
  - :145 drop "from a link you send".
  - :145 the context line twins nathalie-peron.
  - :145 "We built a scan that fits" twins hélène.
  - :157 the closer is the exact clause.
- **gaelle-aveline-330b867b:** :171 the question twins samya; "she arrives".
- **anne-rita-urzetta-terver-b32691b8:** :197 use the verbatim speed phrase.
- **isabel-barreto-ma-b-isabel-b2-ab1756101:**
  - :209 the DP1 restatement and the product sentence are twins.
  - :219 the closer is the exact clause.
- **nathalie-peron-6878ab92:** :229 the context and product sentences twin damien-haessler and cristine.
- **katia-gabarroca-759509139:** :269 "you know" is a presumption.
- **samya-mikou-8833a2140:** :293 the question twins gaelle.
- **hélène-bellod-642366172:**
  - :311 flattery, and the "We built" sentence twins damien-haessler.
  - :321 the closer is the exact clause.
- **fabien-rolland-434a37148:**
  - :333 the product sentence is identical to amandine's.
  - :331 the presumption.
  - :343 the closer is the exact clause.
- **jeanne-guigui-963698150:** :353 the product sentence is a twin.
- **katerina-abaeva-298212190:**
  - :373 the tea-shop hook.
  - :383 "colleague".
- **sophie-canoen-loucheur-982357314:**
  - :403 drop "short and neutral".
  - :393 flattery.
  - :395 "from a link you send".
  - :397 the question twins johanna.
- **dietplus-la-roche-sur-foron-094426267:**
  - :415 the product sentence is a twin.
  - :425 the closer is the exact clause.
- **angelique-rodrigues-b07a852a5:**
  - :435 flattery.
  - :445 drop "introduce me" and "colleague".
- **amandine-poirier-423b16350:** :455 the DP1 restatement is verbatim, and the product sentence is identical to fabien's.
- **cristine-baumert-040781353:**
  - :475 the product sentence twins daphne.
  - :477 the adherence question twins nathalie-dourdoigne.
- **valéry-leprevots-04a9ab35b:**
  - :495 the product sentence is a twin.
  - :505 the closer twins magali.
- **johanna-yung-19b890330:**
  - :525 "head office colleague".
  - :517 the question twins sophie.
- **daphne-cierniak-100558425:**
  - :535 the product sentence twins cristine.
  - :537 the question twins natacha and magali.
  - :545 the closer is the exact clause.
- **nathalie-dourdoigne-15b574173:**
  - :555 "from your link".
  - :557 the adherence question twins cristine.

### BH (`_batch-bodyhit.md`)

- **fredericferet:**
  - :7 use the verbatim speed phrase.
  - :15 says "3DLOOK ran 112,100 scans"; the card's subject is the customers.
- **chloetraina:**
  - :28 the opener twins angelo, the product sentence twins virginie, and "lets".
  - :30 the question twins raphaëla and quentin.
  - :40 the closer twins ines.
- **julie-lacoste-5aa27584:**
  - :49 "A club can add" is a unit pitch.
  - :51 the question twins patricia, audrey and antoine.
  - :61 the closer twins antoine.
  - :57 the 112,100 sentence is a copy.
- **raphaëla-capelle-88a711196:**
  - :70 the opener stem and product sentence are twins.
  - :72 the question twins chloetraina.
- **patricia-gouedard-411015132:**
  - :91 the product sentence twins audrey.
  - :93 the question is a twin.
  - :99 "works with 100+ clients" is present tense.
- **sylvie-plichta-77069a164:**
  - :114 the question has no clear purpose.
  - :120 use the verbatim speed phrase.
- **killian-chotard-758672167:**
  - :133 "a 3D model of the result", and the product sentence is a twin.
  - :141 the 112,100 sentence is a copy.
- **stéphanie-teixeira-44975716b:** :154 the product clause equals jan and anna, plus "you know".
- **françois-xavier-quéré-82a0a517b:**
  - :175 the opener stem is a twin.
  - :183 "3DLOOK has 100+ clients" is one of three copies.
- **lila-sodano-139852256:**
  - :196 the opener stem is a twin, and "under the club's own brand" is a unit pitch.
  - :208 the closer twins juline.
- **audrey-boussin-473997223:**
  - :225 the "so" benefit and the overclaim.
  - :217 the product sentence twins patricia.
- **damien-rollin:**
  - :238 the presumption.
  - :246 "a club's own app".
- **corentin-bernard-47b65723b:**
  - :259 the product sentence twins antoine.
  - :261 the question twins killian and juline.
- **jan-alan-96385423a:**
  - :280 drop the invented seasonality; the product clause equals stéphanie and anna.
  - He runs the same club as antoine.
- **virginie-bourgerie-978a4720b:** :301 the product sentence twins chloetraina, and "lets". The identity check is still pending.
- **quentin-fabre-08164b27b:**
  - :320/:328 capitalise the name.
  - :322 drop "20 minutes".
  - :324 the question is a twin.
  - :330 the 112,100 sentence is a copy.
- **anna-dhervillers-491a8628b:** :343 the product clause equals stéphanie and jan.
- **angelo-phirate-86767131b:**
  - :364 the opener twins chloetraina.
  - :372 drop "so partners can see how others use it".
- **antoine-cormier-266bb1433:**
  - :385 name BODYHIT; the product sentence twins corentin.
  - :393 "the club's own look" is a unit pitch.
  - :387 the question is a twin.
  - :397 the closer twins julie.
- **hassatou-diallo-92b459170:** :406 name BODYHIT. The esthéticienne hook, "Noticed" and "You know" all repeat patterns.
- **ines-h-344686185:**
  - :429 the retention question.
  - :435 "simple to try out", and the 112,100 sentence is a copy.
  - :439 the closer twins chloetraina.
- **juline-boulanger-368487141:**
  - :448 the opener stem is a twin, and "under the club's own brand" is a unit pitch.
  - :460 the closer twins lila.

### Mixed batches

- **andresantos-nutrium (MX3):**
  - :531 the doubled "results".
  - :529 the presumption.
  - :539-541 the M2 needs a value line; the GDPR line should not be the last thing before the signature.
- **arnaud-marche-923259123 (MX2):**
  - :45 use the verbatim speed phrase and drop the presumption.
  - :53 the M2 is only the GDPR line and the call.
- **massimo-caprino-8bab5 (MX2):**
  - :7 "read the same guest", and use the verbatim speed phrase.
  - :15 two compliance sentences.
- **manuela-abreu1 (MX3):** :593 "it selects" refers to a person.
- **100+ wording:** valeriadinatale, jc-heyneke, pbraam, giuliamarinelli, josecarlosalves, mischacohn, todd-peavey-5a00703, jean-maurice-pohl-ab2806bb, sanja-kuche-80203822b, ilija-bozic-b7165532a (lines under B).
- **victor-keunen (MX2):** :317 the "so" benefit.
- **simon-hamer9 (MX2):** :260 drop the "inside an app" inference.
- **pbraam / mattijs-keess-903b7469:** split the shared question.
- **mischacohn / kevin-johnston-0708537 / todd-peavey-5a00703:** split the SK1 sentence and the question.
- **ellie-heath-6704b422 (MX3):** :325 name Liva.
- **fr%c3%a9d%c3%a9ric-julien-190b9932 (MX3):** :367 "let".
- **elisa-stoosz (MX4):** :39 the doubled "structured results".
- **romana-krčmářová-157704b7 (MX4):** :337 move the product fact out of the closer.
- **Link hygiene:** the 8 people listed in the contract check.

## Top 3 issues (priority for improver)

1. **philippe-l-2914a1130 DP:31.** The hook stands on the recipient's own obesity history and photo avoidance, then pitches a two-photo scan. Replace it with a role hook before anything is imported.
2. **The franchise pools collapsed into one skeleton** (RN 30, DP 27, BH 22). Twins appear in the product sentence, the question stem, the closer (the card's example sentence copied about 30 times) and the M2 proof sentence (112,100 ×10). Regenerate these three batches from a per-person grid set before writing, with a distinct fact, question theme and closer form for each person.
3. **Claims.**
   - "100+ clients use FitXpress (today)" ×14.
   - The prospect figure "20 minutes" (quentin-fabre).
   - The RN2 contradiction (ivan-dombes) and four invented RNPC process facts.
   - The writer-note leaks (jacques-ley, sophie-canoen).
   - The clinical lane without the repeatability sentence (jean-jacques-houben).
   - The verbatim speed phrase in about 112 messages.

**System notes (not the agent's fault):**
- The near-duplicate check works at sentence level. A per-company check would have caught all three franchise skeletons. It should compare:
  - the first 6 words of the M1 product sentence;
  - the first 6 words of the M1 question;
  - the last sentence of M2.
- Card:78 gives the pointer as a full sentence, and about 30 people copied it. The card should name the pointer target, not supply a sentence.
- The card says the speed phrase has "one public definition", but the gate treats a variant as soft. It should be hard.
- "At most one compliance line" (card:152) and the clinical MD sentence: settle whether the MD sentence counts as the one line.
- notify.py was not run from this session (no shell tool). Text for the coordinator to send: `QC: message-sequencer → 10/20 (failed) ❌ regenerate RN/DP/BH | Top issue: philippe-l hook on own obesity history + franchise pools collapsed into one skeleton | File: workspace/_quality/outbound/2026-10-07-message-sequencer-eu-weight-loss-nutrition.md`

## Coordinator review

```yaml
coordinator_review:
  agreement: agree
  top_issue: "Franchise referral pools (RNPC 30, Dietplus 27, BODYHIT 22) collapsed into one skeleton per company despite an explicit anti-skeleton line in the batch prompt; '100+ clients use FitXpress (today)' in ~14 messages because the card gives only the bare '100+ clients' with no all-time/3DLOOK-wide wording."
  notes:
    - "Coordinator per-company grep (first 5-6 words of M1 opener, M1 question, M2 first/last paragraph) caught only the M2 compliance closer and a few pairs; QC's sentence-stem reading found the template at the product-sentence and easy-out level. The grep window was too coarse; QC was right."
    - "Philippe L. hook (own obesity story -> two-photo scan) was flagged by the batch writer and left in; agreed it must go."
    - "Decision taken by default for the fix round: at most one compliance sentence per M2; clinical keeps only 'FitXpress is not a medical device.', product/operations/technical-integration only the GDPR line."
    - "Fix round 1 (2026-10-07): RN/DP/BH rewritten by their writers, mixed batches line-fixed; each writer read this report. Re-QC follows."
  card_gaps_for_improver:
    - "card-messages 'Facts you may cite': '100+ clients' should read '3DLOOK has worked with 100+ clients' (all-time, both products)."
    - "check-messages: near-duplicate check is whole-sentence; add a per-company first-five-words check on M1 product sentence, M1 question and M2 last sentence; consider making the non-verbatim speed phrase a hard fail."
```
