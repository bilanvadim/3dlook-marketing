# Message Sequences — Summary

**Campaign:** 2026-07-31-uk-telehealth-digital-health
**Sender profile:** katerina (Katerina Galich, CEO) — UK market
**Product:** fitxpress

## Volume

- Total people: **92** (60 PASS + 32 WEAK; 95 FAIL contacts skipped)
  - P1: 16 | P2: 18 | P3: 26 | WEAK: 32
- Total messages: **184** (92 connection requests, no note + 92 Message 1 + 92 Message 2)

## Character counts

| Segment | Msg 1 avg (/600) | Msg 2 avg (/550) |
|---|---|---|
| P1 (16) | 551 | 455 |
| P2 (18) | 529 | 397 |
| P3 (26) | 463 | 330 |
| WEAK (32) | 366 | 286 |
| **All 92 (weighted)** | **458** | **349** |

No message exceeds its limit (Msg 1 max observed: 583/600 — Robert Nutley; Msg 2 max observed: 520/550 — Julie Pons). PASS-tier messages run longer (more clinical/business context per the 15-minute CTA framing); WEAK-tier messages are intentionally shorter and softer (10-minute CTA, exploratory tone).

## Angle distribution (92 contacts)

| Angle | Count |
|---|---|
| member-engagement | 40 |
| clinical-operations | 16 |
| technical-integration | 14 |
| digital-transformation | 14 |
| compliance | 3 |
| preventive-health | 3 |
| weight-management | 2 |
| **Total** | **92** |

## Quality checks

- **Banned-word scan** (leverage, utilize, harness, robust, seamless, comprehensive, delve, navigate, tapestry, realm, game-changer, revolutionary, disrupt): **0 hits** across all 92 message files.
- **Long dash scan** (— / –): dashes appear only in file-header boilerplate (`# Name — Title — Company`, section headers, Russian instructional lines) — **0 hits inside actual message text**.
- **"It's not just X, it's Y" construction:** 0 hits.
- **Forbidden openers** ("I hope this finds you well", "I came across your profile", "I help companies like yours", "I noticed you work at"): 0 hits.
- **NDA / client-naming check:** no named clients (UK Meds, Yazen, Healthyr, Safariland, etc.) appear anywhere; all social proof uses generic framing ("a regulated UK pharmacy programme").
- **GDPR/compliance mention in Message 2:** present in all 92 (100%).
- **Calendar link in Message 2:** `https://meetings.hubspot.com/katerina-galich` present in all 92.
- **CTA discipline:** 15-minute CTA used for all 60 PASS contacts; 10-minute CTA used for all 32 WEAK contacts.

## Personalization notes

Heaviest company overlaps and how they were differentiated by function:
- **Zoe** (17 contacts across P1–WEAK): angle varies by function — CPO/CEO get weight-management/roadmap framing, VP Engineering ×2 get distinct technical angles (architecture/latency vs. SDK/data schema), Finance/Legal/PR/Content/Design/Motion/IT each get a function-specific hook.
- **Vira Health** (11 contacts): clinical roles (Medical Director ×2, Clinical Director, Global Clinical Programs) each anchored to a different clinical sub-problem (HRT titration, multi-market consistency, women's-health care strategy); commercial/partnership roles (CCO, EMEA Partnerships, Europe Partnerships, Product Marketing, Product Management) each given a distinct commercial angle; Legal/Design/CTO/Chief of Staff each function-specific.
- **Peppy** (9 contacts): clinical-operations roles split across lifestyle healthcare, clinical services, clinical ops (exact-title match), nursing governance; commercial roles split across CEO vision, CPO product, growth, sales/partnerships, client success.
- **Physitrack** (6), **Thriva** (5), **Hertility** (5), **Sweatcoin** (3), **The Body Coach** (4), **Newson Health** (4), **Tonic Weight Loss Surgery** (2) similarly varied by title function.

## 5 random samples for review

### 1. Julie Pons — CPO — Zoe (P1, weight-management)
> Hi Julie, ZOE's evidence-first approach to nutrition stands out in a crowded market. Weight-management programmes live or die on one thing: can members trust the numbers tracking their progress. We built a mobile scanning layer, two smartphone photos, under 45 seconds, 80+ measurements plus body composition (body fat, lean mass, and BMR), 96-97% accuracy against manual measurement. Feeds straight into a member's progress view. Worth 15 minutes to see if it fits your roadmap?

### 2. Dr Frances Yarlett — Medical Director — Vira Health (P1, clinical-operations)
> Hi Frances, as a practising GP moving into Medical Director work, you'll know how thin the objective data usually is in menopause consultations beyond what patients self-report. Weight and body composition change are two of the more measurable markers, and neither is captured consistently between appointments today. We built a mobile scanning layer, two smartphone photos, under 45 seconds, returning 80+ measurements and body composition at 96-97% accuracy against manual measurement. Worth 15 minutes to see if it's useful for Vira Health's clinical model?

### 3. Henrik Molin — CEO & Co-founder — Physitrack (P3, member-engagement)
> Hi Henrik, Physitrack's positioning around measurable rehab outcomes rather than just remote convenience is a stronger long-term bet than most telehealth platforms are making. Objective body measurement is one of the pieces still missing from most remote rehab pathways. We built a mobile scanning layer, two smartphone photos, under 45 seconds, returning 80+ measurements and body composition at 96-97% accuracy against manual measurement. Worth 15 minutes to see if it fits the platform's direction?

### 4. Kostantinos Frantzis — Director of Product Design | Head of Design — Zoe (WEAK, member-engagement)
> Hi Kostantinos, no rush given the parental leave, flagging this for whenever it's useful. Our mobile scanning layer produces a 3D progress model from two smartphone photos, under 45 seconds, which could be a genuinely useful visual asset for how ZOE shows member progress. 96-97% accuracy against manual measurement. Worth 10 minutes whenever convenient?

### 5. Michael R. — Head of Information Security — Peppy (P3, compliance)
> Hi Michael, information security for a workplace health platform usually means any new data capture gets scrutinized before it's allowed anywhere near patient data. Body scanning through smartphone photos raises the obvious question first: what happens to the images. Ours processes two photos in under 45 seconds and deletes them after processing, GDPR-aligned and HIPAA-aware, returning only structured measurements. Worth 15 minutes to walk through the security architecture?

## Files

- Per-contact sequences: `messages/{person_id}.md` (92 files)
- Import file: `closelyhq-import.csv` (92 rows, verified against 92 filenames)

## Next step

Ready for Vadim's Telegram approval, then `closelyhq-importer` step (step 6) to finalize the import file for manual upload to closelyhq.com. Vadim imports and starts the campaign manually — no auto-launch from this agent.
