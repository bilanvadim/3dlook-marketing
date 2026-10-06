---
product: fitxpress
type: open-items
vertical: connected-and-digital-fitness
date: 2026-10-02
---

# Open items

## v3 (2026-10-06), after Nika's final iteration

For Vadim:

**Vadim's answers, 2026-10-06:** E → logos of all clients will be on the page (logo row added, design
supplies the set); D → unknown, ask Nika; B → "100+ clients" stays on this page only, insurance unchanged;
G and A → H1 in app language ("…help retain members with in-app body scanning"), focus keyphrase
`body scanning for fitness apps`.

A. **H1.** v3: "FitXpress for fitness apps: retain members with a mobile alternative to the gym body
   scanner" (sales rule 1 + keyword map). Nika's: "Accurate body scanning for fitness apps that makes
   member progress measurable" (no product, no keyword, leads with accuracy). Your call.
B. **"100+ clients since 2016" is back**, in the pilot block (Nika added it; resolves item 5a below for
   this page). The final insurance page still has no client count: align both pages one way.
C. **Nika re-added facts that still have no source** (item 9 below, unanswered since 10-02): 99.5% uptime
   SLA with service credits, "2 days integration at its fastest", iOS 15+ and older Android models,
   React Native kit, SDK size (40 MB / 104 MB), webhooks without retries or signature verification,
   a dedicated customer success manager on every plan (live `/pricing/`: only on Personalized). If she
   has a product source, it goes into `tech-spec.md` first, then onto the page.
D. **Where did "95%+ consistency" and the per-body-part table come from again?** `proof-points.md` marks
   95%+ "INTERNAL ONLY, DO NOT PUBLISH"; the second time on this page suggests a shared source (deck?)
   that still carries it.

E. **No fitness proof on the page.** All three judges docked proof_of_belonging for it. Is any fitness,
   workout or coaching app cleared for a logo, or is there an anonymised fitness figure for
   `proof-points.md`? Without one, the axis stays capped.
F. **Pilot terms.** Judges ask what the pilot costs, how long it runs and how big the cohort is. The page
   says nothing because nothing is defined; a one-line pilot offer would lift conversion.
G. **H1 keyword.** All judges note that `gym body scanner` frames a hardware purchase a fitness-app CPO does
   not make. The keyword map chose it for demand (~220/mo cluster); "body composition app" (50, KD 2) is
   the app-side alternative. Keep the map's choice?

For Asselya / Whitney:

H. Judge round 3 suggested fitness-specific privacy context (app-store health-data disclosures, the FTC
   Health Breach Notification Rule, US state consumer-health-data laws). Not added: no approved wording.
   Worth a line in the trust FAQ first?

Closed by v3: item 7 (App Store / Google Play line cut by the blog test, as Nika did); item 4 stays cut.

---

## v2 (2026-10-02)

## For Vadim

1. **H1 and title on `gym body scanner`.** Followed the keyword map (§2). The H1 is the landing-map anchor "mobile alternative to the gym body scanner", and retention, Vadim's main point to Nika, leads the hero's first sentence. If the H1 must lead with retention instead, the keyword drops to the meta and the first paragraph.
2. **Problem numbers.** Three figures now: Adjust day 1 (24%) and day 30 (7%), verified on the primary page, and the JMIR median of 70% within 100 days. Two come from one source; a second neutral source on fitness churn would be stronger if one exists.
3. **Weight wording.** The final insurance page says "approximately 3.5% mean absolute error under evaluated conditions"; `proof-points.md` says "±3.5% average error, real-world conditions". This page does not use the weight figure, but the two need one wording.
4. **The AEO FAQ "What's the best alternative to hardware 3D body scanners for fitness studios?"** was cut as a repeat. Return it if the AEO prompt matters more than the dedup rule.
5a. **A trust signal near the CTAs.** The judge (round 1) asked for logos or "100+ clients". The kit allows "100+ clients" (slot 3), but the final insurance page removed the client count from its pilot block, so this page follows the final. Add it back on both pages, or keep both without it?
5. **Adjust as a source.** Adjust is a vendor (mobile measurement partner) blog; Asselya's guardrail asks for neutral sources. It is the most cited retention benchmark; keep it or replace it?

## For Asselya

6. HIPAA and GDPR are left bare, as on the final insurance page. Her Doc's list of commonly known abbreviations is still AI, WWW, iOS, BMI, CEO, UK, US, EU (checked 2026-10-02). Add HIPAA and GDPR to the Doc, or expand them.
7. The App Store / Google Play line in the data block is a fitness-specific practical note, not a 3DLOOK claim. Keep it in the data list or move it to an FAQ?

## For product (via Vadim)

8. **Clothing Detector:** the final insurance page says clothing-related information "does not trigger a retake"; `tech-spec.md` says it "can prompt corrective action". Which is current?
9. Facts from Nika's draft with no source in the repo, all cut from the page: iOS SDK size (~40 MB device binary, ~104 MB arm64 slice), models inside the framework, no On-Demand Resources, offline capture in native kits, React Native kit, webhooks without retries or signature verification, ~100 requests per hour with autoscaling, 99.5% uptime with service credits, iOS 15+ minimum, 10 hours a month of implementation support, standing-only capture, two gender options. Several are good answers for a CTO call; if product confirms them, they go to `tech-spec.md` first.

## For the BD owners

10. Nika's ICP card expects "why can't I test it myself?" from CTOs, because Prism Labs publishes a 90-day sandbox. Our answer is "Book a demo" (no public trial, 2026-09-27). Confirm with Nick (US) and Olena (EU) that this objection is real and that the pilot block answers it.
