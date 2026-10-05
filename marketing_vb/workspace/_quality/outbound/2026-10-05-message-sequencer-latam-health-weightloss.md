---
qc_date: 2026-10-05
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-05-latam-health-weightloss/messages/ (bruno-haidar-a33968106.md, alessisoncini.md, alexandre-pimentelhc.md, _check.json, _batch-mixed-{1,2,3,4}.md)
track: outbound
artifact_type: messages
total_score: 14/20
status: marginal
coordinator_review: done
---

# QC Report — message-sequencer — 2026-10-05

**Artifact:** `workspace/outbound/campaigns/2026-10-05-latam-health-weightloss/messages/`: 3 per-person files, `_check.json` and 4 batch files (128 people, 256 bodies)
**Total: 14/20**, marginal. The rework is targeted: 45 people, nearly all one-sentence edits. A full regeneration is not needed.

What I read: `card-messages.md`, the 4 batch files, the 3 per-person files and `_check.json`. I did not open `_profiles-mixed-*.md` or any other per-person file, to keep token cost down, so hooks were checked against the card's per-person table only. I took the coordinator's facts as given: gate exit 0, greetings and signatures correct, no compliance, banned, client, LGPD or pen wording, and 0 identical sentences within any company.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 4 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 3 | 3 |
| E | Output quality | 2 | 4 |

## What was wrong (specific)

### A. Adherence — 3/5
- **The accuracy line opens a Message 2.** The card says it never does ("It never opens Message 2"). In lucas-mateus-silva-de-souza M2 the first sentence is "The body measurements carry 96-97% accuracy against expert manual measurement."
- **Writer notes were pasted into copy.**
  - adriana-bottoni M1: "Any interest would run through SPDM's own procurement process". The SPDM writer note reads "Public institution: any interest goes through its own procurement."
  - The aesthetic-segment writer note "The 3D model is a view the clinic chooses to show." appears word for word in marisaperaro M1, paula-tecchio M2 and monique-diana-martins M2.
- **Two Message 1s have no product specific.** martingolini M1 and williamfalinski M1 give only API, authentication and deletion facts: no two photos, no 80+, no speed. The card defines the product specific as what the scan returns, from how many photos and how fast. The gate passed both.
- **Uniqueness inside the named peer groups is met only to the letter.** Details are under E.
- **One product-lane pair is incomplete.** bruno-haidar never mentions white-label, API or SDK, "nothing to ship", body composition or the 3D model, all of which the lane lists. For comparison, luis-gonzalez and victor-marcondes cover the lane fully.
- **What held:**
  - No compliance line anywhere, and Vidalink is clean.
  - Partnership asks accept a no and never claim the prospect needs body scanning. ligia leaves out "post-check-up", so the corporate-health boundary never applies.
  - The asset table was followed. The FAQ appears only in technical Message 2s, and no article goes to partnership, referral, telehealth or aesthetic accounts.
  - 112,100 always stands as its own sentence.

### B. Factual accuracy — 4/5
- Every number comes from `proof-points.md` or is cleared by the card: 80+, the speed phrase, 2-4 weeks (technical lane only), 30 days, 34,000 anonymised, 112,100, the <1 cm sentence and the 96-97% sentence. No client is named. The company facts match the fact table.
- lucas-mateus M1 says "your Santander Brasil analyst years before data engineering". His row says Senior Data Analyst, so the data-engineering role is invented.
- lucas-schneider M1 says L2D "depends on every step repeating the same way". That is an inference stated as fact, and LD1 does not support it.
- The external-sourcing rule does not apply to outbound.

### C. Brand & tone — 2/3
- **"so" introducing a benefit** (a card word trap), 4 times:
  - filipe-firmino M2: "so CX has little to configure"
  - thiara-almeida M2: "so the scans a nurse selects can be compared"
  - simone-fatima M2: "so unit teams see the same steps each time"
  - marisaperaro M2: "so evaluators compare the scans they select"
- **Two openers read as if the prospect's title were Kateryna's.**
  - janiel M1: "Wanted to reach out as L2D Saúde Digital's group executive director."
  - flaviosvaiter M1: "Wanted to reach out, as Telecárdio's finance director."
- **The copy reads like a mail merge.**
  - "Noticed…" opens 44 of the 128 Message 1s, including 9 of the 16 at Vidalink.
  - In mixed-3, 8 Message 1s add a second ask ("Open to a quick chat?", "Worth a quick look?") after the person's own question.

### D. Format & structure — 3/3
- No issues. Missing `product:` frontmatter is not counted, per the brief. The only blemish is cosmetic: mixed-3 records have no blank line before `@@@`.

### E. Output quality — 2/4
- **One product sentence does most of the work in mixed-3.** "FitXpress is a guided two-photo scan that returns 80+ body measurements", with a different tail each time, is the product line for 26 of 33 people. It covers every multi-person company in the batch: Siluets 4 of 4, Pró-Corpo 3, Salvia 3, TELUS 3, Grupo Wellness Latina 3, plus Atrys, Wellbe, Sensorial and Llamando.
  - It hits the named Dalul pair too: flaminio "…returns 80+ body measurements." and adrielle-dalul "…returns 80+ body measurements, inside a booking or client flow."
  - This passes the identical-sentence scan but defeats its purpose.
- **Named peer groups share near-identical lines:**
  - **Telecárdio co-CEOs.** Openers: roberto "Quick thought for the co-founder of Telecárdio…" and marceloespiga "Quick note for a Co-CEO of Telecárdio…". Product lines: "We have a separate capability: a guided two-photo scan returning 80+…" and "Our capability is separate: a guided two-photo scan returns 80+…".
  - **Reliv and Céntriqo** (one group because of shared history). martin-samaniego and paola-almeida share the opener "Noticed your background as a physician…", the identical sentence "The doctor decides how to use the values." and the same closing ask, "Worth 15 minutes?". natalia has "The doctor decides what to do with the values." The coordinator's scan ran per company, so it never compared these two companies.
  - **OrienteMe co-founders.** fernanda-maluf "A guided two-photo scan returns 80+ body measurements and a 3D model in under 45 seconds…" and alessisoncini "A guided two-photo capture returns 80+ body measurements in under 45 seconds…".
  - **Liti nutritionists.** ana-paula "We built a guided two-photo scan that members capture at home." and gabriela-teixeira "We built a guided two-photo scan that returns 80+ body measurements from a member's phone." Their Message 2 openers make the same easier-to-forward point.
  - **GESmed.** Closing asks: lucasllau "Happy to show the flow in 15 min" and thiara "Happy to walk through the flow".
  - **Magrass.**
    - rodrigo-baroni "We built a two-photo body scan that clients can take from home" and sandra-panza "We built a guided two-photo scan … that clients take at home".
    - marina and janaina both use the "FitXpress is a two-photo scan clients take…" sentence shape.
  - **Same opener, same company:** Grupo 5S (edivana and paulo-almança), holaDr (paola-giraldo and anamariarpo), Zínea (anderson and graziela), and Vidalink commercial (abi and aline, both "Noticed your [X] background … before [role] at Vidalink").
- **The speed phrase was pasted into sentences where it does not fit.**
  - eliane: "within under 45 seconds from the photos to structured results"
  - filipe and gabrielagalvis: "structured results … under 45 seconds from the photos to structured results"
  - "results in under 45 seconds from the photos to structured results" appears in rodrigo-baroni M1 and in the Message 2s of abilenynogueira, alinesantos-negociacao, ana-paula-moraes, mauriciodl and paty-marques.
- **Partnership lane.**
  - emerson-goulart M2, "nothing to lend or collect", sets the scan against RWE's equipment-on-loan model. The card says never compare with the prospect's own product.
  - alexandre-pimentelhc M2, "inside the partner's own app", leaves unclear whose app is meant. This is minor.
- **Strengths.** Hooks come from the rows, and every Message 1 carries the person's own question. The technical lane is concrete and consistent: alessisoncini covers every lane item. Partnership copy accepts a no and claims no need.

## Top 3 issues (priority for improver)

1. **Uniqueness inside companies and peer groups is met only to the letter.** One product-sentence stem runs across mixed-3, and the named compare-notes groups share near-identical openers, sentences and asks: Telecárdio co-CEOs, Reliv and Céntriqo, OrienteMe co-founders, Liti nutritionists, the Siluets Dalul pair and Magrass. Proposed check: compare shared first words of sentences and openers, not only whole sentences, and run it across each cross-company peer group as well as within each company.
2. **The gate let through four kinds of rule break:**
   - the accuracy line opening a Message 2 (lucas-mateus);
   - writer notes pasted into copy (the adriana-bottoni procurement line, and the 3D-model line 3 times);
   - Message 1s with no product specific (martingolini, williamfalinski);
   - "so" introducing a benefit, 4 times.
3. **Broken sentences**, mostly from fitting the verbatim speed phrase:
   - "within under 45 seconds";
   - "structured results … structured results";
   - "results in … structured results", 6 times;
   - two openers that read as if the prospect's title were the sender's ("Wanted to reach out as [prospect's title]").

## Fix list (person_ids)

- **mixed-1:** eliane-simeão-96a330, filipe-firmino-0787835b, lucas-mateus-silva-de-souza-a76114288, rodrigo-baroni-18455216b, janainapossebon, abilenynogueira, alinesantos-negociacao
- **mixed-2:** marceloespiga, alessisoncini, ana-paula-moraes-177a81112, janiel-josé-zioti-9560602a6, flaviosvaiter, gabrielagalvis, mauriciodl, castilho-jus, emerson-goulart-781585367, bruno-haidar-a33968106 (lane gap, minor)
- **mixed-3:**
  - Rule breaks: martingolini, williamfalinski, thiara-almeida, simone-fatima-amaral-martins-a06122111, marisaperaro
  - Product-sentence rewrites (one person per company keeps the stem): adrielle-dalul-aa955b201, lívia-sales-bb25a920, jackeline-lopes-08b81b167, andreza-zatorre-pereira-4a642b8, barbaracarvalhor, renisemarmentini, sonia-maria-figueiredo-82968a14, carlosprestessilva, ángeles-dubini-50011417, jimena-maldonado-de-chazal-096340268, matheus-rodrigues-7925631a3, sidneisalmaso, victor-cavallari-434a81ab, viviana-salazar-8a4b984b
- **mixed-4:** martin-samaniego-reliv, natalia-dezerega-molina, adriana-bottoni-0a606131, paty-marques-710b1b25b, paulo-almança-4bb7026a, anamariarpo, grazielaheusserazeredo, paula-tecchio-1a66111b7, monique-diana-martins-8b9577165

## Coordinator review

(заполняется Claude в чате после автозапуска QC)

## coordinator_review

```
agreement: ✅ agree
top_issue: near-duplicate lines between colleagues passed an exact-match scan; fixes go to all four batches with a difflib ≥ 0.75 self-check, and check-messages now notes near-duplicate sentences within a company and an M2 that opens with the accuracy figure.
```
