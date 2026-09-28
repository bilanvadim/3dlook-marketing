# Messaging — 2026-09-14-eu-erakulis-similar — group BetterMe

Written by one of four parallel step-5 agents. Scope: only `people-approved.csv` rows with
`group == "BetterMe"` (30 people). The other three groups (Gymondo, Welltech, Yazio/Kilo/rest)
are written by other agents into the same `messages/` directory and are not touched here.

- **People in this batch:** 30 (29 wave 1, 1 wave 2 referral: Tanya Goncharenko, sent after
  wave 1 at BetterMe per hypothesis addendum).
- **Total messages generated:** 30 x 2 = 60.
- **Char count — Message 1:** min 352, avg 427.9, max 508 (limit 600).
- **Char count — Message 2:** min 187, avg 276.0, max 362 (limit 550).
- **Distribution by angle (from `recommended_message_angle`):** product 19, retention 8,
  technical-integration 2 (Nastya Kobzeva — Senior AI Engineer, cold `technical-integration`
  per pool K; Vitalii Malakhovskyi — CTO, cold `technical-integration` per pool D, Vadim
  2026-09-28), referral 1 (Tanya Goncharenko, Head of Finance, wave 2).
- **Priority split:** P1 x1 (Bogdan Rogovchenko), P2 x23, P3 x6.
- **Pool split:** A x18, L x4, v1 x3, B x2 (Retention Manager), K x1, E x1, D x1.

## What each message carries

- **Product specifics (proof-points.md), Message 1 gate:** every Message 1 cites at least one
  of "two photos", "80+ measurements", "body composition (fat %, lean mass, BMI)", "under 45
  seconds" — the same set the 30-person batch rotates across 7 product-intro phrasings so no
  two adjacent contacts read the identical sentence. No accuracy-percentage claim was needed
  for this batch (BetterMe pitch leans on measurement/speed specs and the SDK/API integration
  line, not the accuracy benchmark), so `accuracy-formulations.md` wording wasn't invoked.
- **Company-specific hook, one line "written only to BetterMe":** every message ties to either
  (a) the BetterMe Smart Scale (shallow body-composition hardware, the natural extension case),
  (b) the person's own LinkedIn headline/bio/experience (ex-Samsung Healthcare, ex-Welltech,
  ex-Nielsen, 2Smart Cloud/IoT, banking product background, biotech/genetics, etc., pulled from
  `sales-nav-raw/2026-09-28-sales-nav-olena.csv` joined on LinkedIn URL), or (c) the retention /
  churn framing from the hypothesis (front-loaded churn, visible progress before the scale
  moves). Fifteen of the 19 "product"-angle people have the identical `reason` field in
  `people-approved.csv` ("PM/PO at a multi-app group"), so all differentiation for that group
  came from individual headline/bio/experience, not from the CSV reason text.
- **Compliance:** one person only, Olena Parkhomenko (Technical Project Manager who runs GDPR
  compliance and physical-product delivery per her bio) — GDPR sentence used **verbatim** from
  `compliance.md` §2/§9 UK/EU variant: "In most enterprise deployments, the customer acts as the
  data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes
  SCCs." No other file carries a compliance line; BetterMe is consumer wellness, not one of the
  verticals where CLAUDE.md §12 makes the line mandatory.
- **Technical-integration:** Nastya Kobzeva (Senior AI Engineer) and Vitalii Malakhovskyi (CTO)
  get the build-vs-buy framing: pre-trained model via SDK/REST API, "typically 2-4 weeks" for a
  basic integration (`icp-detail.md:597`, explicitly cleared for this campaign by the hypothesis'
  reason #3), no computer-vision team to hire. Vitalii is the cold CTO first touch approved by
  Vadim 2026-09-28 (pool D), measured separately per the hypothesis.
- **Referral (Tanya Goncharenko, wave 2):** short, no product pitch dump, asks who owns the app
  roadmap / body-progress decision, notes in Message 1 that a few BetterMe product people were
  already contacted. Message 2 is a bare follow-up ask with no calendar link and no CTA offer,
  consistent with "no pitch" for a referral-only contact.
- **No client names:** grepped for Erakulis, Yazen, UK Meds, Healthyr, Zing Coach, CR7/Ronaldo
  across all 30 files — zero hits.
- **No pricing:** grepped for `$`, `€`, `£`, "pricing", "free trial" — zero hits.
- **No anonymous scan-volume proof (34,000 / 112,100) used in this batch.** The batch leans on
  product-spec proof (measurement count, speed, SDK/API) and the person's own background instead;
  none of the 30 messages needed the scan-count figures to make the point, so they weren't forced
  in. Flagging this so Vadim can decide if that is a gap versus the other three parallel batches.
- **GLP-1 / BetterMe's clinician-prescribed GLP-1 add-on:** not mentioned anywhere. Flavour 4 is
  out of scope for this campaign (Vadim 2026-09-14); the add-on is a scoring signal only, not an
  outbound hook.

## Hard-rule sweep (mechanical, run on this batch's 30 files)

| Check | Result |
|---|---|
| Client names (Erakulis/Yazen/UK Meds/Healthyr/Zing Coach/CR7) | 0 hits |
| Pricing (`$`/`€`/`£`/"pricing"/"free trial") | 0 hits |
| Em/en dash in message bodies | 0 (dashes found only in the required Russian template
  boilerplate — file headers and the two `## Message N` section labels — never inside a
  message body) |
| Char limits (600 / 550) | all 30 within limits (see min/avg/max above) |
| Corrective negation ("X, not Y" / "rather than" / "not just X") | swept and rewritten in 13
  files after a first draft; second pass grep is clean |
| `plus` as a benefit/feature connector | swept and rewritten (6 hits fixed: "measurements plus
  body composition" x4, "Samsung Healthcare plus scaling", "scale-plus-app"); remaining `plus`
  hits are non-connector uses ("200+ SKUs" adjacent text, "Product Office and an e-commerce...")
  or gone entirely |
| `so` / `let` / generic `organization` as connectors | 0 hits |
| Banned words (leverage/utilize/harness/robust/seamless/comprehensive/delve/navigate/
  tapestry/realm) | 0 hits |
| Outbound clichés ("hope this finds you well", "I came across your profile", "I admire your
  mission", "excited about your journey", "quick question for you", "I help companies like
  yours", "just following up", "circling back", "wanted to pick your brain") | 0 hits |
| `detect-ai-tells.py --channel dm` on message bodies only (extracted to a temp file, not the
  `.md` files with their header em dashes) | batch file: CLEAN, density 0.28/1000 (budget
  12.0); one soft marker, "wanted to reach out" (Nadiia Rudiuk hook), which is an
  approved hook phrase straight from `outbound-message1-template.md`'s own list, not a
  fabricated cliché |
| `detect-ai-tells.py` per person (30 individual files, bodies only) | 30/30 CLEAN |

## Random sample for Vadim review (5 people)

- `messages/bogdan-rogovchenko.md` — P1, product angle, Smart Scale/hardware hook (Release
  Train owner).
- `messages/elenaparkhomenko.md` — compliance angle, GDPR verbatim line, pool L.
- `messages/nastya-kobzeva.md` — technical-integration, Senior AI Engineer, build-vs-buy framing.
- `messages/purpleshirted.md` — technical-integration, CTO cold first touch, pool D.
- `messages/tanya-goncharenko-a32624102.md` — referral, wave 2, no calendar link, sent after
  wave 1.

## Not done / flagged for Vadim

- No pilot check that the other three parallel agents (Gymondo / Welltech / Yazio-Kilo-rest)
  used different hooks for people who may have moved between these companies (e.g. anyone who
  went BetterMe -> Welltech or the reverse) — out of scope for this batch, flagged so the
  coordinator can dedupe phrasing across all four batches before import.
- Did not use either of the two anonymous scan-volume proofs (34,000 scans / 112,100 scans)
  anywhere in this batch (see above) — a deliberate choice given the batch already carries a
  product-spec proof in every Message 1, not an oversight, but worth a decision if the other
  batches lean on the scan-volume proofs and Vadim wants BetterMe to match.
- Importer not run, per instructions.
