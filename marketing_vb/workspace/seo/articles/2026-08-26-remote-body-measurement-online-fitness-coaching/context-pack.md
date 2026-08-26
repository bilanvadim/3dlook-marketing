```yaml
context_pack:
  created: 2026-08-26
  product: fitxpress
  track: seo
  channel: blog
  profile: company
  objective: "New article: Remote Body Measurement for Online Fitness Coaching Programs"
  target_agent: seo-planner
  task_id: 2026-08-26-remote-body-measurement-online-fitness-coaching

  note_prior_attempt: |
    An earlier attempt at this exact title was archived 2026-08-25 to
    workspace/seo/articles/remote-body-measurement-online-fitness-coaching--v1-20260825-archived/
    because the seed phrase has no measured Ahrefs demand. Do NOT treat that archive as an
    approved checkpoint-1 for this run — Ahrefs data below shows the real head term to use.

  company_oneliner: "3DLOOK turns two smartphone photos into 80+ body measurements and a 3D model in under 45 seconds via API/SDK."

  product_summary: |
    FitXpress: verified body composition / measurement layer for telehealth, GLP-1, insurance,
    wellness, and digital/connected fitness. For this article the relevant framing is engagement
    and retention for coaching platforms — NOT clinical or diagnostic.

  approved_claims:
    - id: FX-001
      text: "96-97% accuracy vs manual measurements, real-world benchmarks"
      source: "2025 Accuracy & Repeatability Study"
    - id: FX-002
      text: "Typical absolute error margin 1.5-2.0 cm"
      source: "Same study"
    - id: FX-003
      text: "Scan-to-scan repeatability < 1 cm (95%+ consistency)"
      source: "Same study — write repeatability as '< 1 cm', locked convention (about-me.md)"
    - id: FX-004
      text: "ISO 8559-1:2017 multi-company benchmark: session-to-session repeatability 0.40 cm"
      source: "ISO benchmark, 14 companies / 8 countries / 27 subjects / 1,152 data points — never combine with FX-001/003 (different reference)"
    - id: FX-005
      text: "Two photos, under 45 seconds, 80+ measurements + body composition (BMI, BMR, fat %, lean/fat mass)"
      source: "Product spec"
    - id: FX-006
      text: "Weight estimation ±3.5% average error margin (Smart Scales, software output not a physical scale)"
      source: "FitXpress deck"
    - id: FX-007
      text: "HIPAA-compliant, GDPR-aligned, AWS S3 SSE-S3 encryption, photos deleted immediately or within 30 days"
      source: "Security commitment"
    - id: FX-008
      text: "9+ years of training data, 150K+ photos, 30K+ 3D scans, 430K+ measurements"
      source: "FitXpress deck, Apr 2025 — use only if depth/credibility section needs it, not a lead claim"

  banned_claims:
    - "most accurate body scanning"
    - "guaranteed compliance"
    - "FDA-cleared / FDA-approved / medical device"
    - "diagnoses, detects, or clinically validates any condition"
    - "replaces clinician, DEXA, BIA, or calibrated scale"
    - "automated eligibility / underwriting / employment / clearance decisions"
    - "any number not in approved_claims above"
    - "named-competitor comparisons (Prism Labs / Bodygram / Size Stream) — compare by role/method only"
    - "blurring into GLP-1 clinical workflows or wellness-rewards claims (vertical boundary, this is Fitness cluster)"

  banned_words:
    - leverage
    - utilize
    - harness
    - robust
    - seamless
    - comprehensive
    - delve
    - navigate (metaphorical)
    - tapestry
    - realm
    - unlock / unleash
    - game-changing / revolutionary / cutting-edge / disrupt
    - "It's not just X, it's Y"
    - em dash (—/–) — banned outright, no exceptions (terminology-guardrails.md)

  terminology_guardrails_hard_bans:
    # brand-assets/content-strategy/terminology-guardrails.md (synced 2026-08-25) — writer keeps these in head; seo-editor Pass 4 + Pass 3c detector run the full pass
    - "em dash — always replace with comma, period, or parentheses"
    - "'objective' about our tech/conclusions → use standardized / timestamped / structured / repeatable"
    - "no 'the reader' / 'the audience' / 'see below' / 'the following sections'"
    - "no 'this article' / 'this guide' / 'our content' (except a scope note)"
    - "'by hand' → manually; 'let' → allow"
    - "'plus' as a benefit/feature connector → use including / such as / along with / as well as"
    - "'so' introducing a result/benefit → use reducing… / allowing… / which can reduce…"
    - "'positioned as' about product/intended-use/regulatory status is BANNED — state the boundary directly: 'FitXpress is not a medical device'"
    - "no presumed audience reaction ('what trips people up', 'the mistake buyers make')"
    - "no behaviour/feelings attributed to concepts ('two properties do the heavy lifting' → 'two properties matter')"
    - "corrective negation ('X, not Y') and corrective 'rather than' — lead with the recommended approach; state the limitation as its own sentence"
    - "BMI, CEO, UK, US, EU are commonly known — do NOT expand (2026-08-25 override of old M1 rule); still expand FDA/ICH/GCP-type regulator acronyms on first use"

  tone:
    voice: "expert, data-driven, evidence-led B2B; calm and unhurried; reframe-the-question move; honest about limits in the same breath as capability"
    length: "~1,800-2,800 words typical for P1 supporting article in this hub (compare: hub itself ~4,500 words)"
    format: "Standard 12-part structure (about-me.md / guidelines §12): buyer problem → short answer → why now → workflow/use-case → where FitXpress fits → what improves operationally → what FitXpress does NOT do → comparison/decision framework → buyer/ICP fit → implementation considerations → FAQs (2-5 sentence, GEO/AEO-friendly) → CTA"
    author: "Assel Sekerova (default blog byline per CLAUDE.md §15, unless Vadim specifies otherwise)"
    dont: "no clickbait, no emoji, no generic AI-tell openers, no clinical/diagnostic framing (this is the lighter/less-clinical Fitness vertical)"

  voice_fingerprint:
    - "The reframe move: turn the obvious question into the sharper one (e.g. 'Is a smart scale enough?' → 'Enough for which kind of progress?')"
    - "Declarative and unhurried; 15-30 word sentences, 2-4 sentence paragraphs; concrete over abstract — every claim carries a number, source, or disclosed limit"
    - "Honest about limits in the same breath as capability; buyer framing ('coaches', 'platforms', 'programs'), not 'you'-spam"
    - "No jokes in published copy; sober and dry-but-serious even though this vertical's tone is lighter than clinical verticals"

  claims_discipline:
    - "NEVER: diagnose, make treatment/eligibility/clearance decisions, replace clinician/DEXA/BIA/calibrated scale, guarantee compliance, auto-detect fraud"
    - "Position AS: mobile body-scanning solution / structured body-data capture layer / progress-tracking and scan-to-scan comparison layer"
    - "Not a medical device — state directly, never 'not positioned as' (terminology-guardrails override, 2026-08-25)"

  accuracy_framing:
    - "Never reduce accuracy to one universal number — qualify by decision/reference/protocol/population/tolerance (accuracy framework hub is the canonical source: mobile-body-scanning-accuracy)"
    - "Repeatability written as '< 1 cm'; the two benchmarks (internal vs ISO) are never combined"
    - "For this vertical, repeatability is the differentiator to lead with over one-off accuracy — small real body-recomposition changes get lost in measurement noise without it"

  examples:
    # No FitXpress example exists yet for this exact Digital Coaching cluster (net-new).
    # Per CLAUDE.md §15 hard-req #2, read 1-2 of the three canonical FitXpress reference articles:
    - file: "brand-assets/past-articles/blog/3dlook-turns-two-photos-structured-body-data.md"
      note: "General company/product voice model, structured-data framing"
    - file: "brand-assets/past-articles/blog/wellness-rewards-verification-employers-insurers-using-ai-3d-body-scanning.md"
      note: "Closest tonal analog: engagement/retention/verification framing, softer non-clinical claims"
    - note: "Do NOT model on 2024-era MT/fitness articles in the corpus (top-fitness-tech-companies, connected-fitness-industry, etc.) — they predate the 2026 tone and use now-banned words (leverage/revolutionize/harness)."

  competitors_context: |
    Prism Labs is primary FitXpress competitor, strong in fitness/wellness progress-tracking lead-magnet
    narratives. Bodygram is closer in this specific vertical (mobile body measurement for fitness
    trainers/coaches, longitudinal progress tracking) but weaker on enterprise compliance and has no
    apparel/MTM business. Differentiate on repeatability (< 1 cm), workflow/API integration depth, and
    compliance posture (HIPAA/GDPR) — never name competitors in the article; compare by method/role only.

  icp_context:
    segment: "Connected & Digital Fitness (FitXpress ICP #8 / audience.md segment 3)"
    buyer_persona: "Founder/CEO, Chief Product Officer, Head of Growth / VP User Engagement / Retention (secondary: CTO, Product Manager)"
    pain_points:
      - "Users lose motivation without visible progress; weak long-term retention past onboarding"
      - "Personalization limited to surveys/goals, not real body data"
      - "Crowded market competing mostly on UX; rising CAC demands stronger engagement hooks"
      - "Self-report and manual progress photos feel dated and are easy to fake"
    hero_message: "No exact hero message for this sub-segment in messaging.md — closest available is the shared positioning line 'Verified body data, built for trust.' Use audience.md hook below as the primary angle instead."
    segment_hook: "Visible transformation plus body-data personalization drives engagement, retention, and premium-tier monetization. Tone is lighter and less clinical here than other FitXpress verticals. (audience.md segment 3)"
    do_not_say:
      - "No medical, diagnostic, or clearance language"
      - "Don't blur into GLP-1 clinical workflows or wellness-rewards claims — this is the Fitness vertical boundary, not Wellness or GLP-1"

  content_strategy:
    hub: "Hub 1 — AI in Fitness (live: `ai-in-fitness-industry`, published 2026-07-31, refreshed from Sep 2024 version)"
    hub_url: "https://3dlook.ai/content-hub/ai-in-fitness-industry/"
    cluster: "Digital coaching"
    intent: "MOFU/BOFU"
    action_type: "Create net-new"
    priority: "P1"
    existing_urls: []  # no existing article to refresh; net-new
    cannibalization_guardrail: "Targets coaches/platform workflows, not generic fitness apps. Do not duplicate the hub's broad overview — this piece must be narrower (digital-coaching platform workflows specifically)."
    recommendation: "BOFU destination → /fitxpress/for-connected-and-digital-fitness/. Keep scope to coach/platform operational workflows, not a second broad 'AI in fitness' piece."
    vertical_boundary: "Fitness owns fitness apps, digital coaching, body recomposition, progress visibility, engagement, retention, app features. Do not blur into wellness rewards or GLP-1 clinical workflows (those are separate hubs/clusters — a dedicated 'GLP-1 bridge' cluster article is planned separately for that crossover, this is not it)."
    internal_link_targets:
      up: "AI in Fitness hub — https://3dlook.ai/content-hub/ai-in-fitness-industry/"
      sideways:
        - "Planned (not yet written, do not treat as live): 'Smart Scale vs AI Body Scan' comparison cluster; 'GLP-1 and Fitness Apps' bridge cluster"
        - "Live but different vertical, link only if genuinely relevant to a coaching-platform reader: top-7-remote-body-composition-tools-glp-1-clinics (published 2026-08-21) — GLP-1/telehealth cluster, use sparingly, do not blur vertical boundary"
      down: "https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/ (BOFU product page, per content-plan.md row)"
      trust:
        - "https://3dlook.ai/content-hub/mobile-body-scanning-accuracy/ (accuracy framework — canonical source for any accuracy/repeatability claim)"
        - "Data/Privacy/Security/Regulatory FAQ — NOT YET LIVE (draft only, at workspace/seo/articles/2026-07-14-fitxpress-privacy-security-faq/). Do not link to a live URL for it; if privacy is discussed, keep it a short practical note and flag the missing central FAQ as an Open Item rather than inventing a link."

  published_inventory:
    already_live: false
    published_hub_articles:
      - slug: "ai-in-fitness-industry"
        title: "AI in Fitness: How Structured Body Data Powers Progress Tracking, Personalization, and Digital Coaching"
        published: "2026-07-31"
        role: "hub"
    recently_published_adjacent:
      - slug: "top-7-remote-body-composition-tools-glp-1-clinics"
        published: "2026-08-21"
        hub: "GLP-1 / telehealth cluster — adjacent, not same vertical"
      - slug: "mobile-body-scanning-patient-engagement"
        published: "2026-08-14"
        hub: "Telehealth — patient engagement angle, tonally close (engagement/retention) but different vertical"
    other_live_fitness_cluster_pages_legacy: |
      top-fitness-tech-companies (May 2024), ai-body-scanning-for-fitness (pre-2026), connected-fitness-industry
      (pre-2026), top-trends-and-features-in-fitness-apps (Nov 2023) — legacy 2024-era pages in the same
      hub folder. Do not model tone/claims on these (banned words present); may be candidates for a future
      internal-link/refresh pass but are out of scope for this article.
    refresh_status: "Topic not previously published under any slug. Archived v1 attempt (2026-08-25) does not count as prior publication or as checkpoint-1 approval."

  keywords_raw:
    source: "ahrefs api v3 (keywords-explorer)"
    pulled: "2026-08-26"
    country: "us"
    plan: "Standard 2022, billed monthly"
    seed: "Remote Body Measurement for Online Fitness Coaching Programs"
    seed_has_data: false   # exact seed phrase: NO measured demand at all (not zero — no figure)
    seed_metrics: null
    variants:
      - keyword: "Remote Body Measurement for Online Fitness Coaching Programs"
        no_data: true
      - keyword: "Remote Body Measurement for"
        no_data: true
      - keyword: "online fitness coaching programs"
        volume: 100
        difficulty: null
        cpc: 600
        traffic_potential: null
        intents: {informational: true, commercial: true, transactional: true}
      - keyword: "remote body measurement"
        volume: null
        difficulty: 26
        parent_topic: "mirrorsize"
      - keyword: "fitness coaching programs"
        volume: 60
        difficulty: 57
        traffic_potential: 4700
        parent_topic: "online personal training"
      - keyword: "remote body"
        volume: 0
        difficulty: null
      - keyword: "coaching programs"
        volume: 500
        difficulty: 52
        traffic_potential: 3100
        parent_topic: "icf accredited coaching programs"
        warning: "Higher volume but off-vertical (general/life coaching) — do not chase this as head term, it dilutes the fitness-platform angle"
    idea_seed: "online fitness coaching programs"
    ideas_best:
      - keyword: "online fitness coaching programs"
        volume: 100
        difficulty: null
      - keyword: "best online fitness coaching programs"
        volume: 100
        difficulty: 58
    recommendation_for_planner: |
      seed_has_data = false. Use "online fitness coaching programs" (100/mo, difficulty unmeasured) as the
      working head term instead of the literal seed phrase. Keep "Remote Body Measurement for Online Fitness
      Coaching Programs" as the buyer-facing angle/title framing (matches content-plan.md row), not as the
      primary SEO keyword target. This is thin, BOFU-appropriate demand, not broad top-of-funnel volume —
      legitimate for a P1 BOFU-leaning supporting article, but must be stated explicitly in plan.md and
      Open Items per CLAUDE.md 2026-08-26 entry, so Vadim sees it at checkpoint 1 rather than discovering it
      later in GSC.

  exclusions: null  # not applicable — track=seo, not outbound
```

**Sources read to build this pack:**
- `about-me.md`
- `audience.md`
- `brand-assets/product-info/messaging.md`
- `brand-assets/product-info/proof-points.md`
- `brand-assets/product-info/competitors.md`
- `brand-assets/product-info/icp-detail.md`
- `brand-assets/content-strategy/content-plan.md`
- `brand-assets/content-strategy/content-strategy-guidelines.md`
- `brand-assets/content-strategy/published-articles-inventory.md`
- `workspace/seo/_keywords/2026-08-26-remote-body-measurement-online-fitness-coaching.yaml`

Built by `context-pack-builder` sub-agent (2026-08-26); saved to disk by orchestrator because the builder's session has no Write tool.
