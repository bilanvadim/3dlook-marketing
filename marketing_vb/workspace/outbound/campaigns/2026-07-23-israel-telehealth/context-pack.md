context_pack:
  created: 2026-07-23
  product: fitxpress
  track: outbound
  profile: katya
  market: Israel
  objective: "Israel telehealth/health-tech outbound campaign (HMOs, digital therapeutics, RPM, wellness, insurers)"
  target_agent: icp-validator

company_oneliner: "3DLOOK turns two smartphone photos into 80+ body measurements and 3D model in 45 seconds via API/SDK."

product_summary: |
  FitXpress: verified BMI / body composition / measurements for telehealth, insurance, online
  pharmacy, wellness, occupational health. Value props for fit-scoring:
    - Anti-fraud: AI Smart Scales detect self-report/weight mismatch
    - Engagement/retention: 3D goal visualization, side-by-side progress, repeat check-ins
    - Workflow efficiency: remote intake replaces manual/in-person measurement, reduces clinical team load
    - Longitudinal tracking: repeatability (<1cm variance) matters more than one-off accuracy for programs
      built on repeat scans (chronic disease, weight loss, cardiac rehab, RPM)
    - Compliance: HIPAA-compliant, GDPR-aligned, audit-ready records, AWS S3 SSE-S3 encryption,
      no personal identifiers processed, photos deleted immediately or within 30 days

approved_claims (cite only these, use range form when unsure):
  - id: FX-001
    text: "96-97% accuracy vs manual measurements (real-world benchmarks)"
  - id: FX-002
    text: "±3.5% average weight estimation error margin"
  - id: FX-003
    text: "95%+ repeatability; variance <1cm across repeated scans"
  - id: FX-004
    text: "80+ body measurements + body composition (BMI, BMR, fat %, lean mass) from 2 photos in under 45 seconds"
  - id: FX-005
    text: "HIPAA-compliant, GDPR-aligned; TLS in transit, AWS S3 SSE-S3 at rest"
  - id: FX-006
    text: "9+ years training data, 150K+ photos, 30K+ 3D scans, 430K+ measurements"
  - id: FX-007
    text: "Yazen: 34,000 scans (2025), weight-loss management support"
  - id: FX-008
    text: "UK Meds: 7,500 scans (2025), BMI verification for online pharmacy"

banned_claims / no-go positioning:
  - Never lead with "most accurate body scanning" (loses to future Apple/Google native primitives —
    lead with workflow/outcomes/repeatability instead)
  - Never say "AI-powered body scanning" alone without a concrete outcome attached
  - Never claim FDA-cleared / "medical device" / diagnostic claims
  - Never invent comparisons ("Nx more accurate than X") — not in proof-points.md = don't use it
  - No number outside approved_claims above; use range form ("around 95-97%") if uncertain
  - For insurers/HMOs/underwriting-adjacent fits: lead with defensibility/audit-readiness/HIPAA-GDPR,
    not raw accuracy — this audience values compliance over precision claims

icp_context (Israel-relevant FitXpress segments, from icp-detail.md — map each prospect to closest):

  segment_A: "Telehealth & GLP-1 / Weight Loss Programs"
    fits: DarioHealth, Sweetch, K Health, BetterTogether, Datos Health, Laguna Health
    buyer_titles: "Founder/CEO, Chief Medical Officer/Medical Director, Head of Clinical Operations,
      Head of Member Engagement/Retention, Head of Product"
    revenue_threshold: "$2M+ annual revenue, Series A+"
    pain_points:
      - "Members drop off after onboarding without visible progress"
      - "Self-report weight/BMI unreliable, easy to fake"
      - "Small real changes lost in measurement noise without strong repeatability"
      - "Payers/enterprise partners increasingly expect measurable, defensible outcomes"
    hero_message: "Make body progress more visible — before members drop off."
    key_differentiator: "Lead with repeatability, not one-off accuracy — programs depend on repeat scans"
    competitor_context: "Prism Labs (primary), Bodygram (secondary)"

  segment_B: "RPM / Wearables / Remote Monitoring"
    fits: TytoCare, Biobeat, CardiacSense, SHL Telemedicine, Vim, Mon4t
    note: "Not a standalone icp-detail.md segment — treat as technical-integration extension of
      Telehealth/GLP-1 segment (RPM programs). Buyer often CTO/Head of Technology → classify per
      IT-title policy (WEAK + technical-integration, not FAIL, unless clear purchasing authority
      e.g. Chief Business & Strategy Officer)."
    angle: "FitXpress as an additional connected-device data stream (body composition) alongside
      existing vitals/RPM data — complement, not replace"

  segment_C: "Health Plans / HMOs / Employer Wellness (Rewards & Verification)"
    fits: Clalit Health Services, Maccabi Healthcare Services, Leumit Health Services,
      Meuhedet Health Services, Harel Insurance, Migdal Insurance, Phoenix Holdings,
      Wesure/Shomera
    buyer_titles: "CHRO, Head of Wellness/Wellbeing, Chief Medical Officer, VP Population Health,
      Health Plan Operations Director, Compliance & Risk Team, Digital Transformation Leader"
    revenue_threshold: "$5M+ annual revenue, large enterprise, population-scale programs"
    pain_points:
      - "Manual verification workload, unreliable self-reported data"
      - "Fraud/inconsistent submissions undermine program trust and fairness"
      - "Need audit-ready, standardized verification at population scale"
      - "Growing scrutiny on data governance/privacy"
    hero_message: "Verify wellness progress remotely to reduce disputes, boost participation,
      and improve program reporting."

  segment_D: "Insurance Underwriting"
    fits: Harel Insurance, Migdal Insurance, Phoenix Holdings, Wesure/Shomera
    buyer_titles: "Chief Underwriting Officer/VP Underwriting, Chief Medical Officer, Head of
      Risk & Analytics/Chief Risk Officer, Digital Transformation Leader"
    revenue_threshold: "$5M+, large enterprise (5K+ employees)"
    hero_message: "Verify body metrics remotely to issue faster, cut rework, and strengthen auditability."
    critical: "Lead with HIPAA/GDPR + audit logs + workflow integration, NOT accuracy per se"

  segment_E: "Hospitals / Innovation Hubs (pilot-first entry point)"
    fits: Sheba Medical Center / ARC Innovation, Ichilov (Tel Aviv Sourasky), Assuta private clinics,
      Clalit Innovation (Tech.Mate), Maccabi Health Tech accelerator / MDClick
    note: "Not a formal icp-detail.md segment. Closest overlap: Bariatric/Metabolic Clinics (Director
      of Operations, Medical Director, VP Patient Access). These are pilot/innovation-arm entry
      points into large HMOs (Clalit, Maccabi) — expect longer sales cycle, PoC-first, not direct
      enterprise close."
    buyer_titles: "Head of Innovation Division, Director of R&D (innovation center), Medical
      Director, VP Patient Access"

  segment_F: "Occupational Health / Connected & Digital Fitness"
    fits: Holmes Place Israel, Go Active / WeFitness (fitness chains); IDF Medical Corps
      (institutional/public-sector — subject to gov procurement, flag separately)
    buyer_titles (fitness): "Founder/CEO, Chief Product Officer, Head of Growth, VP User
      Engagement, Fitness Program Director"
    revenue_threshold: "$1M+ annual revenue (Digital Fitness)"
    pain_points: "Users lose motivation without visible progress; weak long-term retention;
      manual measurement stations slow and inconsistent"
    hero_message: "Standardize screening intake remotely to increase throughput, reduce
      rescreens, and speed clearance decisions." (occupational) / member-retention framing (fitness)

israel_procurement_note:
  - "Clalit, Maccabi, Leumit, Meuhedet are Israel's 4 statutory HMOs ('kupot holim') — quasi-
    governmental, large member bases (Clalit ~half the population). Expect formal tender/RFP
    procurement, longer sales cycles, multiple stakeholders. Messages should acknowledge this
    procurement context respectfully (per user instruction), not push urgency/hard-sell."
  - "Preferred first-touch entry points for HMOs: Clalit Innovation (Tech.Mate), Maccabi Health
    Tech accelerator / MDClick — flag as preferred contacts when present."
  - "IDF Medical Corps = public-sector/government procurement — WEAK/long-cycle, do not over-index
    outreach effort without Vadim's sign-off."
  - "Private insurers (Harel, Migdal, Phoenix) are commercial entities — standard enterprise B2B
    motion, closer to Insurance Underwriting / Wellness Rewards segments than to HMO tender process."

geo_compliance_flag:
  - "Israel is not explicitly named in CLAUDE.md §4 geo-expansion list or §12 compliance summary
    (which centers on HIPAA/US and GDPR/EU), though it IS an established active outbound + social
    market (katya profile, active since 2026-07-21). Israel has its own Privacy Protection Law
    separate from HIPAA/GDPR. Recommendation: proceed with validation, but surface a one-line note
    for Vadim to confirm Israel health-data compliance status has been checked for outbound sends
    (not just social) — do not block on this."

tone_note (profile katya):
  voice: "BD professional in a fast-moving startup ecosystem. Direct, confident, innovation-friendly. First person."

universal_exclusion_reminders:
  - "No free/freemium consumer apps with no enterprise budget"
  - "Exclude companies with recent acquisition/merger announcements (deal cycle stalls)"
  - "Exclude existing customers — none of the FitXpress named customers (UK Meds, Yazen, Healthyr)
    are in this Israel list, so no overlap expected"
  - "IT/technical titles (CTO, Head of Technologies, OCIO Director) → classify WEAK +
    technical-integration, not auto-FAIL, unless clear purchasing authority"

exclusions:
  profile: katya
  registry: "workspace/outbound/exclusions/katya-registry.json"
  status: "empty — no prior campaigns, no excluded companies/people yet for this profile"
