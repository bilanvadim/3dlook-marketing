---
product: fitxpress
type: open-items
vertical: all
date: 2026-09-27
---

# Open items: /fitxpress/

Every bent guardrail and every canon conflict found while building, per editorial principle #11. Nothing
here was decided silently. Owner in brackets.

## A. Decisions made on the page that someone should confirm

1. **Price named on the page** [Vadim, Asselya]. `about-me.md` says "Pricing. Never state or imply
   prices." The page-builder skill requires a price signal naming the entry tier. The page follows the
   skill (Starter, $1,000 per month for up to 500 scans, from live `/pricing/`). `about-me.md` is written
   for articles; confirm the page exception.
2. **No trial anywhere on the page** [Vadim]. Done per the 2026-09-27 decision (API/SDK access after a
   demo call or NDA). The sentence "API and SDK access is set up after a demo call or under a
   non-disclosure agreement" is new public wording; confirm it.
3. **Healthyr logo** [Vadim]. Healthyr exists only as one row in `proof-points.md` (L89, "Patient profile
   complement"). There is no `case-studies/healthyr.md`, and the current site asset is labelled "Reddit"
   (SEO plan §1.4). Confirm Healthyr is a current customer and that its logo may appear.
4. **No anonymised figure on the page** [Vadim]. The SEO plan allows anonymised figures from
   `proof-points.md`. None fits: 112,100 scans (2025) and 100+ customers are company-wide and include
   Mobile Tailor; any FitXpress-only total would be close to Yazen's 34,000 and could identify it. If a
   FitXpress-only aggregate (for example, total FitXpress scans in 2025) is wanted, it needs a new
   `proof-points.md` row and clearance.
5. **SDK recommendation stated as opinion** [Asselya]. "In our experience, capture quality is the largest
   single factor in measurement quality that a program controls." Source is `tech-spec.md` L28 ("single
   biggest factor in measurement accuracy"), an internal claim with no figure. Kept as an explicitly
   hedged opinion; cut if guardrail #1 is read strictly.
6. **Predicted weight shown as "Smart Scales, in beta"** [Vadim]. `tech-spec.md` and `how-it-works.md`
   still call Smart Scales beta; live `/pricing/` lists "Predicted weight" with no beta label. Confirm the
   status before publishing.
7. **Accuracy FAQ sentence edited** [Asselya]. `accuracy-formulations.md` §5 FAQ form reads "…compare
   FitXpress with expert tape measurements, which serve as the reference." The detector flags "serve as";
   the page says "3DLOOK's published figures use expert tape measurements as the reference." Same claim.
8. **"Internal" restored** on the validation study ("A separate internal validation…"), per the §5 note,
   because the page sits next to the trust block and could be read as implying outside validation.
9. **FDA sentence shortened** [Whitney]. The trust block carries the first half of the FAQ's FDA sentence
   and links the FAQ for the rest ("3DLOOK makes no representation as to whether FDA clearance… is
   required…"). The FAQ answer on the page has the same shortening. Regulatory framing goes to Whitney.
10. **Decision boundary paraphrased** [Asselya]. The standard intended-use sentence ("FitXpress does not
    diagnose conditions…") trips the detector's `claims_discipline` literal "diagnose". The page uses
    `compliance.md` §7's own scope instead: "Clinical, underwriting and eligibility decisions stay with the
    program's clinicians, underwriters or other designated decision-makers." The detector and the
    guardrail's model sentence disagree; worth fixing one of them.
11. **Employer wellness link target** [Asselya]. Linked to the Wellness Rewards Verification article (the
    employer/insurer sub-hub per `content-plan.md` L195). Hub 5, `ai-body-data-wellness-platforms`, is the
    broader platform hub and was not indexed on 2026-09-21. Confirm the choice.
12. **"We / our" used twice**, both as claims of ownership ("We recommend", "In our experience").
13. **FAQ question "Is FitXpress HIPAA compliant?"** repeats the phrase buyers search for, then corrects it
    ("HIPAA is a regulatory framework, not a certification."). Same question shape as `compliance.md` §10;
    the detector passes it. If the judge or Asselya reads the question itself as the banned claim, rephrase to
    "Does FitXpress support HIPAA-governed deployments?".
14. **Medical-device wording: short form only (judge round 1)** [Whitney, Asselya]. `compliance.md` L16
    carries the long sentence "An independent regulatory assessment concluded that FitXpress does not meet
    the definition of a medical device under the UK MDR or EU MDR." The blind judge failed it under
    guardrail #3: "independent" with no named party and no citable output on the page. The page now uses
    "FitXpress is not a medical device." with the FDA sentence, and sends the reader to the trust FAQ for the
    assessment and the UK/EU detail. If the assessor can be named with a citable output, the long sentence
    can come back. Note the conflict: canon approves the sentence, guardrail #3 forbids it on a page that
    does not name the party.
15. **Results block** [Vadim]. Canon has no public payload field names (`tech-spec.md` L122: endpoint paths
    and code confidential), so the block describes the payload in words and shows no JSON. "Standard 3D file
    format" is as specific as `tech-spec.md` L116 allows; name the format (OBJ, GLB…) only if product confirms.
    Destinations per program are phrased as where programs send results, from use-case files and
    `tech-spec.md` patterns, not as built integrations.
16. **Industries grid pains** are taken from the use-case files' "The pain we remove" and `audience.md`,
    lightly shortened. "Patients misreport BMI to qualify" is `audience.md`'s wording and describes some
    patients; confirm the tone with Asselya.
17. **Opinion added**: "a scan should document the body data behind a decision… The decision itself belongs
    to the program's own reviewers." Stated once, in the industries section.
18. **Single biggest lever for the proof axis: a FitXpress deployment figure** [Vadim]. Two blind-judge
    rounds scored proof lowest (12/20, 11/20). The page can only show logos and non-client canon (training
    data, accuracy framework, trust FAQ). No `proof-points.md` row gives an anonymised FitXpress figure that
    cannot identify a logo'd client: 34,000 (Yazen) and 7,500 (UK Meds) are client-specific, and 112,100 /
    100+ are company-wide including Mobile Tailor. Options: (a) a new approved row such as total FitXpress
    scans in 2025 or number of FitXpress programs live, checked that it does not point at Yazen; (b) one
    approved anonymised quote; (c) a G2 rating once it is in `proof-points.md`.
19. **Round-3 number sweep** [Asselya]. Removed "first 90 days" from the fitness card (source was
    `fx-digital-fitness.md` only; not an allowed number source) and "five scans per participant" from the
    repeatability sentence (in `accuracy-formulations.md` §5 but not in `proof-points.md`). The sentence now
    reads "with repeated scans of each participant". If "five" is wanted back, add it to `proof-points.md`.
20. **Medical line in the body is now the short form only** ("FitXpress is not a medical device." + trust FAQ
    link). The FDA sentence appears once, in the FAQ answer to a question that asks about the FDA, in full
    canon wording from `compliance.md` L17. Supersedes the shortened-FDA note in A9.
21. **Decision-boundary idea kept once** (trust section). The round-2 opinion line on decisions was cut as
    repetition; the page keeps one opinion ("A single accuracy percentage tells a procurement team very
    little") and one boundary sentence.

## B. Canon contradictions found (not resolved here)

1. **Trial: three definitions, and the live site still promises one.**
   - Live `/pricing/` meta description: "Sign up for a 7-day trial or request a demo"; Mobile Tailor tiers
     carry "Sign up for a trial" / "Start a Trial"; a block near the end of `/pricing/` also reads "Sign up for a 7-day trial".
   - `pricing.md` and `proof-points.md` L151: 1 month, 200 free requests. `faq.md`: "Is there a free
     trial? Yes, 1 month, 200 free requests, full SDK access". `CLAUDE.md` §2 repeats it.
   - Vadim 2026-09-27: no public trial promise anywhere, access after NDA or demo.
   The FitXpress tab on `/pricing/` already uses "Book a demo", so the conflict is the meta description,
   that block and the repo files. [Vadim]
2. **Timing: one canon, five other versions.** Canon (`proof-points.md` L50, Vadim 2026-09-23): "under
   45 seconds from the photos to structured results". Elsewhere: `about-me.md` "(< 30 s), full pipeline
   < 45 s"; `audience.md` "under a minute"; `overview.md`, `CLAUDE.md` §1 and `faq.md` "in 45 seconds"
   (no "under"); `messaging.md` tagline "45 seconds"; live telehealth benchmark hero "in under a minute";
   live `/pricing/` FAQ "under a minute, with processing typically under 40 seconds". [Vadim to sync
   repo files; CMS edits for the live pages]
3. **`faq.md` is out of date against `tech-spec.md` and `compliance.md`.** "React, iOS, and Android SDKs"
   (public wording is "web and mobile SDKs, including supported iOS and Android integrations");
   "SDK integration is days, not months" and "99.5% uptime" have no `proof-points.md` row; "Does it work
   with all body types? Yes" contradicts the population limitation (`proof-points.md` L74). None of these
   was used on the page. [Vadim]
4. **`about-me.md` "Canonical figures" privacy line** still reads "GDPR-aligned (EU), SOC 2 where
   applicable … no names or personal identifiers processed", which `compliance.md` (2026-09-18) retires.
   [Vadim]
5. **`pricing.md` vs live `/pricing/`.** `pricing.md` has six per-request tiers ($1,000 / 500 requests up
   to $10,000 / 20,000); the live FitXpress tab publishes Starter $1,000 / up to 500 scans, Pro $1,500 /
   up to 1,000 scans, Personalized custom. Units differ (requests vs scans). The page uses the live
   figures only. [Vadim, re-sync `pricing.md`]
6. **Live `/pricing/` FitXpress FAQ breaks current canon**: "approximately 96-97% accuracy … across all
   body metrics and 95%+ repeatability" (95%+ is internal-only per `proof-points.md` L37), "FitXpress
   maintains HIPAA compliance and adheres to GDPR principles", "we don't have access to PII", "images are
   … deleted immediately after processing" (retention is immediate or up to 30 days), "80+ precise body
   measurements … including Fat %, BMI, BMR" (§2.13). [CMS edit, whoever owns WordPress]
7. **Live homepage** carries "HIPAA Compliant", "never link photos to personal identifiers", "over 95%
   consistency in repeatability", "89% accuracy" for BMI (not in `proof-points.md`), "Leverage",
   "Seamlessly", "cutting edge", and two third-party statistics (58%, 40%) with vague attributions. Out of
   this skill's scope, but the homepage FitXpress block that links here should not repeat any of it. [Vadim]
8. **Footer "HIPAA Compliant" badge** will render on `/fitxpress/` (the theme footer). `DESIGN.md` §8 keeps
   it as a site element by Vadim's 2026-09-18 decision, while the same phrase is banned in copy and the
   trust table on this page says the opposite. A diligence reader will see both on one screen. [Vadim]
9. **Telehealth benchmark page** (the skill's model) itself uses "under a minute", "80+ ISO-compatible
   measurements", "HIPAA-aware", "GDPR-aligned" and "Body Mass Index (BMI)" in its schema. Its structure
   was followed; its wording was not.
10. **"across body metrics"** in the canonical accuracy sentence (`accuracy-formulations.md` §1.1) vs
    §2.13. The page uses the §5 short form ("Across the evaluated body measurements"), which avoids it.
    Already an open item in `terminology-guardrails.md` §2.13.

## C. Needs Whitney (regulatory framing)

- Trust block wording as a whole, especially the shortened FDA sentence (A9) and the decision-boundary
  paraphrase (A10).
- "Eligibility documentation" as a typical use of calculated metrics in the outputs table.
