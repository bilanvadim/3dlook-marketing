# Messaging — 2026-09-27-uk-bariatric-prequal

- Product: fitxpress · Profile: katerina (UK) · Market: UK
- Total people: 74 (all `decision = PASS` rows in `people-validated.csv`; RESERVE/FAIL untouched)
- Total messages generated: 74 × 2 = 148
- Avg char count message 1: 428 / 600
- Avg char count message 2: 515 / 550
- Sender: Katerina Galich. Signature on every message is `Katerina` only (no title, no company).
- Compliance line (UK/EU, verbatim from `compliance.md` §9): included once per person, in Message 2, on all 74 (this ICP is healthcare-regulated, so the mention is mandatory for the whole list): "In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs."
- Article link (`https://3dlook.ai/content-hub/bariatric-pre-qualification-mobile-3d-body-scanning/`) is in Message 2 only, framed as "we wrote up the intake workflow and its limits" (3 rotating phrasings), per hypothesis. Never in the connection note (there is none) or Message 1.
- Calendar link on every Message 2: `https://meetings.hubspot.com/katerina-galich` (Katerina's own link, per `outbound-message2-template.md`).
- Proof points used: none beyond the mechanism itself (no client names, no scan-count figure). The hypothesis's only approved anonymised line ("34,000 scans... at one weight-management customer") was not needed to make the case and was left out rather than forced in; the banned "7,500 UK scans" line was not used anywhere. No pricing anywhere.
- No client names (UK Meds, Yazen, Safariland, Burlington Medical) anywhere in the batch (checked by grep).
- US pre-auth / CMS-0057-F language: not used. UK framing only (NICE-gated eligibility, GDPR/DPA, "insurer pre-authorisation pack" only for the one Vitality/Streamline PMI-angle contact).
- Banned words (leverage, utilize, harness, robust, seamless, comprehensive, delve, navigate, tapestry, realm), long dashes, triple parallelisms, and "it's not just X, it's Y" / casual "not just" constructions: zero hits after two fix passes (one round caught 7 "utilisation" hits, flagged by `detect-ai-tells.py`'s banned-words category, and a second round caught 5 casual "not just" constructions on manual review; both fixed and re-verified clean).
- `detect-ai-tells.py --channel dm` run on all 148 message bodies (M1 and M2 extracted separately, not the surrounding file scaffolding): **0 hard fails, 0 soft flags** on the final pass.
- Greeting names were cleaned for 8 people whose `first_name` field carried an honorific or a compound name from LinkedIn parsing (e.g. "Professor Lisa" → "Hi Lisa,", "Dr Melanie" → "Hi Melanie,", "Debashis." → "Hi Debashis,"), so the salutation reads as something a person would actually type. Full names in the H1 header stay as recorded.

## Distribution by angle (from `recommended_message_angle` in the CSV)

| Angle | N |
|---|---|
| consult-slots | 46 |
| glp1-bmi-history | 18 |
| one-record-two-jobs | 4 |
| pmi-preauth-pack | 1 |
| (blank, campaign-level override persona) | 5 |

The 5 blank rows are the finance and dietitian roles Vadim's 2026-09-28 checkpoint added to this campaign (normally excluded by the hypothesis's persona rules). They got a custom angle built for their function, not one of the four named hooks:

| Custom angle | N | Who |
|---|---|---|
| finance | 2 | Leigh Joseph (Finance Manager, Streamline), Victoria Jones (Director of Finance, Phoenix) |
| dietitian | 3 | Nicole Alabaster, Heidi te Braake, Ayaan N. (all Streamline) |

Two more people kept their CSV angle (`consult-slots`) but were pitched through a technical/integration framing rather than the clinical-outcome one, because they are P3 digital evaluators (2026-07-22 IT policy: do not lead with them, evaluator lens only): Melanie Tan (Director of Medical Informatics, Cleveland Clinic London) and Andrew Mikhail (CCIO, Practice Plus Group). Their product-intro paragraph uses the SDK/integration wording instead of the standard consult-slots one; noted in each file's "Context used" block.

## Special-handling notes (per hypothesis / validation checkpoint)

- **Qutayba Almerie** — company column says Circle Health Group, but written to in his Phoenix Health capacity (Programme Director of the RCS-accredited bariatric fellowship there), per the reason field and the hypothesis's explicit instruction.
- **Greg Jones and Marianne Sampson** — written as founding partners of **Optimise Weight Loss Surgery**, not as Spire/Circle employees. Neither message mentions Spire or Circle.
- **Danny Brown and Emma Thomas (Phoenix Health)** — both messages say "private self-pay" explicitly; no NHS framing, per the anti-case rule for Phoenix.
- **Sandip Hindocha (Tonic)** — framed around his real role there (post-bariatric body contouring), not the CMO title he holds at The Private Clinic.
- **Rishi Singhal (Healthier Weight)** — new contact, not one of the four people excluded from the 07-31 campaign; company re-entry per Vadim's decision 5.
- **Debashis Ghosh (The London Clinic)** — his division is Breast/Plastics/Urology/Gynae/Derm/Ophthalmology, not GI. Message says so plainly and asks him to route to the right division head rather than assuming fit.

## Random sample for Vadim review (5 people)

1. **Ayaan N.** — Specialist Bariatric Surgery Dietitian, Streamline Surgical (custom dietitian angle) — `ayaan-n-83b339244.md`
2. **Sam Lock** — National Director, Circle Health Group (consult-slots, group ops) — `samlock.md`
3. **Kate Convery** — Surgery Support Manager, The Hospital Group (consult-slots, pathway) — `kate-convery-0b536872.md`
4. **Grace P.** — Director Of Development, HCA Healthcare UK (consult-slots, ex GI-service-manager background) — `grace-p-8b969a54.md`
5. **Kogie Naidoo** — Executive Director, Circle Bath Clinic (consult-slots, site ops) — `kogie-naidoo-614b703b.md`

All file paths under `workspace/outbound/campaigns/2026-09-27-uk-bariatric-prequal/messages/`.

## Not run

`closelyhq-importer` was not run. This is the message-sequencer checkpoint; Vadim reviews before import.

## Vadim approval (2026-09-28)

Approved as is: no proof number added, GDPR line stays in Message 2.
