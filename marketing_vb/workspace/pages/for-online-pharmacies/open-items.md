---
product: fitxpress
type: open-items
vertical: online-pharmacies
page: page.md / page.html (2026-11-23). GATE NOT TAKEN: 75/85 after three blind rounds (73, 71, 75); post-round-3
  correctness fixes unscored. Publishing requires Vadim's explicit decision.
---

# Open items: FitXpress for online pharmacies

Every bent guardrail and every claim that needs a decision or a confirmation (editorial principle #11). Ordered:
blocking first, then product, then register, then risks and findings.

## A. Blocking before publish (Vadim)

1. **Weight-accuracy figure: two canon files disagree.** The page states "Smart Scales estimates weight with
   approximately 3.5% mean absolute error under evaluated conditions" (accuracy H2, figure tile, method sentence).
   For it: `proof-points.md` (page wording approved 2026-10-02), the live `/for-insurance-underwriting/`, Asel's BMI
   page v7 (asked for in our 11-09 review), Kit slot 9 ("where weight matters to the vertical"). Against it:
   `roadmap.md` (2026-11-11), "Weight-prediction accuracy baseline, Q4 2026 (R&D): No weight-accuracy numbers until R&D
   publishes the baseline". `accuracy-formulations.md` has no weight formulation at all, so the brief's rule ("only the
   verbatim formulation in accuracy-formulations.md") cannot be met literally. Not averaged, not silently picked
   (guardrail #2): the page uses the approved page wording and waits for your call.
   **If the figure goes:** delete the figure tile and the sentence "This figure comes from internal validation. Peer
   review … (NDA).", and make the intro: "Smart Scales returns a software estimate of weight, and the pharmacy sets its
   mismatch threshold with the estimate's error in mind. FitXpress is not equivalent to a calibrated scale when the
   pharmacy's protocol requires one." The descriptor conflict ("evaluated" on pages vs "real-world" in the deck) is
   already open in `proof-points.md`.
2. **H1** changed in round 2 (coordinator ruling) from option B "…: a second weight source before weight-loss
   prescribing" to "FitXpress for online pharmacies: a live weight check before weight-loss prescribing". Same meaning,
   now carries "weight check" and names the outcome the judge said was missing. Your confirmation at the final
   checkpoint.
3. **Primary phrase, title, anchors.** Primary `weight checks for online pharmacies`; title `Order-Flow Weight Checks
   for Online Pharmacies | FitXpress` (58); the G-A draft title with "BMI Verification" at its head was dropped for
   requirement 1. Anchors proposed for the `landing-map.md` row: weight checks for online pharmacies · FitXpress for
   online pharmacies · weight check before weight-loss prescribing.

## B. Product confirmations

4. **Live capture in every SDK flavour.** Hero ("photos taken live at checkout"), strip ("taken live on the patient's
   own phone"), step 2 ("takes both photos live"), the comparison row "Where the evidence comes from", the problem-block
   scope sentence ("a weight estimate from photos taken live in the order flow"), H1 ("a live weight check"), meta
   description. Source: the published
   compliance guide ("FitXpress controls capture via its SDK, without a camera roll picker"). Confirm it holds for the
   web SDK as well as iOS and Android, and that an API-only integration is excluded by the "recommended setup" line.
5. **Who sets the mismatch threshold.** Page: "A threshold set by the pharmacy determines whether the record carries a
   flag." `tech-spec.md` says FitXpress returns a mismatch flag when self-reported weight is provided, and does not say
   whether the threshold is configured per customer in FitXpress or applied in the pharmacy's system. The live
   insurance page uses the same "carrier-defined threshold" pattern. If the threshold lives only in the pharmacy's
   system, the tile becomes: "The pharmacy's system compares the estimate with the declared weight and flags orders
   above its own threshold."
6. **Re-order check.** G-I fact 4 asked for product's OK before re-orders go on the page. The page frames it as the
   pharmacy running the same scan at a re-order (scan entry point "trigger from any flow", `tech-spec.md`), with no
   comparison to earlier scans. Confirm, and confirm each re-order scan is one API request.
7. **Admin Panel.** Tile: "supports monitoring and export, showing compliance staff failed-scan messages and
   photo-deletion dates for past scans" (`roadmap.md`: Live; `tech-spec.md`: canonical "monitoring and exporting
   results"). Confirm the panel is available on Starter.
6a. **Scan during an online consultation (Vadim, 2026-11-23).** Step 1, the comparison closing line and a new FAQ say
    the pharmacy can place the scan "during or straight after" an online or video consultation (`tech-spec.md`: scan
    entry point, trigger from any flow). Product to confirm whether the SDK capture flow runs on the same phone while
    the patient is on a video call (the call app holds the camera), or needs a second device or a step straight after
    the call. No call integration, video analysis or claim that the scan counts as video verification is made.
7a. **How much the weight estimate depends on entered height (round 3).** The page now says Smart Scales estimates
    weight "from the two live photos and the height the patient enters" (`compliance.md` §3 lists height as a submitted
    input). Product to say how sensitive the estimate is to a wrong entered height. If it is strongly dependent, the
    "second weight source" wording (record H2) and the mismatch-flag logic need a sentence on what a false height does
    to the flag.
8. **Liveness left out.** Anti-fraud live human validation is "coming soon" outside the BMI page (`roadmap.md`). When
   product confirms release, one line can go into step 2 or a FAQ; until then nothing on this page implies a liveness
   check. Clothing Detector also left out (Q4 2026).

## C. Register and Kit deviations (Asel)

9. **Block order follows the live fitness page**, not the Kit table: "How it works" comes before the scan record
   (Vadim's requirement 2). The blind judge's one_fix (move the record up, make it a table) was declined by the
   coordinator for that reason; the gap was closed with buttons and per-tile benefits instead. The comparison and
   accuracy blocks still run about 3,460 px at 1280×800 without a button, as on the fitness template.
10. **Accuracy block carries one figure**, not the Kit's three: the 96-97% and < 1 cm body-measurement figures do not
    answer a weight question and would pull the page toward measurement selling.
11. **Comparison has two options**, the alternative named generically ("manually reviewed evidence"), because the BMI
    page owns the methods comparison (self-report, video consultation, calibrated scale).
12. **FDA dropped** from the trust-FAQ sentence (UK page, per the brief); medical-device status and SOC 2 kept.
13. **Links:** the value block's in-depth link goes to the BMI feature page; the compliance-guide link sits under the
    regulatory paragraph (requirement 1). One shared source line serves both GPhC figures. Round 2: the API
    documentation link sits in the recommended-setup line (the integration FAQ was replaced), `/technology/` was
    dropped for length, and a "Related pages" line after the FAQ repeats the two sibling links.
14. **Acronyms:** GPhC expanded by hand (the detector regex cannot see it). Round 2 expands "UK General Data
    Protection Regulation (UK GDPR)" and "glucagon-like peptide-1 (GLP-1)"; GDPR in the canonical role sentence stays
    bare, as on the insurance final; BMI stays bare (CLAUDE.md list). "scan identifier" used for "scan ID" (the detector reads "ID" as an
    unexpanded acronym; the fitness page wrote "scan ID").
15. **"customer"** appears only in the canonical legal sentences (GDPR role, photo policy, model training).
16. **Breadcrumb** has two levels until `/fitxpress/` is live (Kit slot 1).
16-r3. **Closed (coordinator, 2026-11-23; kept through the post-round-3 pass):** the physical-disabilities limitation sentence, cut for length in round 3,
    is restored verbatim in the accuracy block with "Those patients follow the pharmacy's alternative route."
    Visible copy after the post-round-3 pass, the reorder and the consultation option: 1,596 words.
16d. **Keyphrase placement (post-round-3).** The lede was rewritten to stop reading keyword-stuffed, so the exact
    focus keyphrase "weight checks for online pharmacies" now sits only in the SEO title and meta description. Yoast
    will flag "keyphrase in introduction". With zero measured demand, accepted; Vadim may prefer a different keyphrase
    (the round-3 judge called it unnatural).
16e. **Comparison row removed (post-round-3):** "What the patient does" repeated "Where the evidence comes from" after
    the round-3 rewrite; five operational rows remain.
16f. **Block order changed after round 3 (Vadim, 2026-11-23):** the scan record now precedes How it works (value
    before mechanics; round 1's one_fix). The live fitness page keeps the opposite order; the same change could be
    proposed there. Not re-scored.
16a. **Spelling.** The page keeps US house spelling (anonymized, authorization), as on the fitness page, for site-wide
    consistency. The judge marked it down on a UK-targeted page. Question for Asel: keep US spelling site-wide, or
    use UK spelling on UK-led landings?
16b. **Method wording.** "The figure comes from an internal study" replaces the insurance landing's "internal
    validation" (reserved word without an external party). The two live pages would then describe the same 3.5% figure
    differently; one wording for both is Asel's call.
16c. **Roles.** Pilot criteria are "agreed with the superintendent pharmacist and compliance lead"; (until 2026-11-23
    FAQ 1 also said the
    superintendent pharmacist decides whether the complete process meets GPhC guidance.) Katerina (UK BD owner) to
    confirm these are the right sign-off roles for UK online pharmacies.

## D. Regulatory framing (Whitney)

17. GPhC wording in the problem block (post-round-3): the prescriber verifies "the person's weight, height and/or body
    mass index" using "a different way to verify the information provided to them by the person" (both verbatim from
    the February 2025 guidance), then the cost sentence and the scope sentence ("FitXpress adds one input to that
    check … Whether that estimate, alone or with other checks, meets the pharmacy's process is the pharmacy's
    decision.").
17a. **Regulator quotation vs the reserved-word gate (Asel).** The guidance's own word is "independently";
    `detect-ai-tells.py` hard-fails "independently verif" even inside a quotation, so the page uses the guidance's
    definition of the word instead. Decide whether a verbatim regulator quotation is exempt.
18. FAQ 1 was removed on 2026-11-23 (the problem block's scope sentence answers it, and the online-consultation FAQ
    took its place); the remaining boundary FAQs are the height question and the consultation question ("The
    prescriber still decides, and the pharmacy judges whether the combined check meets its process.") and FAQ 2 (height is supplied by the patient; any further height check sits outside
    FitXpress). Height verification is 2027; nothing implies it is verified.
18a. **The guidance's own examples.** The February 2025 GPhC guidance (read 2026-11-23) says independent verification
    "could be through a video consultation, in person, from the person's clinical records or by contacting another
    healthcare provider such as the person's GP". A photo-based weight estimate is not among the examples (the list is
    not exhaustive). The page never says FitXpress counts as independent verification; the scope sentence leaves that judgement to
    the pharmacy, and the comparison names video consultations and clinical records as the manual route. Whitney to confirm this framing; sales should
    expect the question.

18b. **No MHRA or CQC context (round-2 judge).** Neither regulator is in the canon sources for this page; the page
    names only the GPhC, whose guidance and review were read in full. Whitney and Asel to decide whether a line on the
    MHRA (medicines advertising, the joint enforcement notice the GPhC review cites) or the CQC (independent online
    doctor services in England) belongs on a UK pharmacy landing.

## E. Risks and findings for Vadim and Katerina

19. **Clothing objection.** The GPhC review lists public concerns about "requests for photographs of individuals in
    'tight-fitting clothes' or underwear to evidence body weight", practices "not being aligned with regulatory
    expectations". FitXpress capture guidance recommends form-fitting or regular-fit clothing (`tech-spec.md`). The page
    says nothing about clothing; sales should be ready for the question, and the patient-facing instruction wording for
    UK pharmacies may need a check with product and Whitney.
20. **Verified GPhC facts not used** (the brief limits the page to G-I items 1-5). From the February 2025 guidance:
    "Verifying information helps to confirm that any continued supply is clinically suitable" (fits re-orders) and
    "Verifying information through a phone call would not be appropriate when supplying medication for weight loss".
    From the April 2026 review: "Every supply request should be
    individually reviewed for clinical suitability" (fits the re-order card); 49% of concerns related to online
    pharmacies; inspectors list "lack of independent verification or information to determine BMI" among common issues.
    All in the April 2026 review PDF (pages 2-10). Add them to G-I if you want them on the page.
21. **Template anchor mismatch (resolved on this page in round 3: the form section is `#demo`, `#form` is an alias,
    every button points to `#demo`).** The live fitness landing has no `#demo`: its form sits in the footer at `#form`.
    `landing-map.md` rule 4 and Kit slot 15 send article buttons to `{landing}#demo`, so those clicks land at the top of
    the fitness page. This page carries both (`#form` plus a `#demo` alias). Suggest a theme-level `#demo` alias, or
    flip the landing-map "Demo button now" column to `#form` for the template pages.
22. **Template contrast.** The fitness prototype's 12 px captions (`.fx-cf-illus`, `.fx-cf-mock`, `#808080` on white)
    measure 3.95:1, under the 4.5:1 floor; fixed on this page (`#666`, 5.74:1). Worth a check on the live fitness page.
23. **Timing wording drift on the live fitness page:** "results in under 45 seconds after capture" against the one
    public definition "under 45 seconds from the photos to structured results". This page uses the canonical form.
24. **Pricing note in `site-inventory.md` is stale:** it says "Starter $1,000/mo (up to 500 scans)"; the live
    `/pricing/` now reads "500 API requests included per month. Additional requests: $2.00 each." This page uses the live
    wording without the overage rate.
24a. **USD prices on a UK page (round-2 judge).** The live `/pricing/` lists FitXpress in USD only. The page repeats
    the live figures. A GBP line needs a pricing decision first (Vadim).
25. **EU later.** `areaServed` is United Kingdom only, and the problem block is GPhC-specific. An EU version swaps that
    block and the meta; the DPA and SCC lines already cover EU transfers.

## F. Handoff items to carry into TODO.md (Phase 6)

26. 301 `/for-online-pharmacies/` → `/fitxpress/for-online-pharmacies/` when `/fitxpress/` ships; GTM `fx_vertical`
    lookup row for the path; `landing-map.md` row flipped to live with "Link now" and the demo anchor; the BMI page's
    pharmacy card linked down here; the compliance guide's down link (today `/for-bmi-verification/`) relinked here.
27. Run validator.schema.org on the final graph; measure performance; tab through the page; verify `generate_lead`
    and `demo_click` firing after publish.
