# Target Companies — 2026-10-22-uk-insurance-underwriting

Profile `katerina`, market UK. Scope hash stamped `dfde15582b423f32` (hypothesis-gate 2026-10-22, status approved).

## Summary
- Total: 24 companies IN (target 25, floor 22 passed). Group A insurers 14, group B reinsurers 7, group C platforms 3.
- 28 named candidates: 24 IN, 4 dropped (OneFamily, Scottish Friendly, Wesleyan, MetLife UK). No company added to reach a number.
- Hypothesis fit: high for the 7 adviser-market insurers (Aviva, Royal London, Zurich, VitalityLife, Scottish Widows, plus L&G and LV= with caveats) and Pacific Life Re; medium for the four small income-protection mutuals, National Friendly and SCOR UK. Overall: high-medium.
- Rows held for Vadim on displacement (remote body, face or BMI-from-image evidence found in public sources): Legal & General, Hannover Re UK Life Branch, Gen Re UK. Soft flags: Zurich UK, Shepherds Friendly. Details below. None dropped silently.
- Registry check: all 28 candidate slugs checked against `global-company-registry.json` by hand; no hits (only `phoenix-health` resembles a candidate name and no Phoenix row is in the list). Run `outbound-registry.py check --profile katerina` after extract as the hypothesis asks.
- Search health: `search-health.py` exit 0 at the start; no run of three empty queries occurred. `WebFetch` is blocked by the stack for most trade sites; dates were confirmed with plain HTTP fetches where the site allowed (COVER, Mortgage Solutions, Reinsurance News, Insurance Business, The Intermediary). Health & Protection and IFA Magazine block this VPS, so facts that rest only on them carry "snippet only".

## Company list

| # | Company | HQ | Employees | Revenue | Why fit | Source |
|---|---------|-----|-----------|---------|---------|--------|
| 1 | Aviva | London | 10,001+ (LinkedIn, group) | Not confirmed for UK protection | Changed non-medical limits and moved over 80% of medical exams to nurse screening in June 2026. | https://www.covermagazine.co.uk/news/4531397/aviva-updates-medical-underwriting-limits |
| 2 | Legal & General | London | 10,001+ (group) | Not confirmed | Reworked life and CI application questions January 2026 to cut manual referrals. HOLD (selfie-BMI precedent). | https://www.mortgagesolutions.co.uk/mortgage-news/2026/01/08/lg-retail-protection-improves-underwriting-process/ |
| 3 | Royal London | London | 1,001-5,000 | Protection sales GBP483m PVNBP H1 2026 | Refreshed IP occupation classes 2026; HNW protection growing. | https://www.covermagazine.co.uk/news/4533966/royal-london-records-rise-sales-amid-ip-changes |
| 4 | Liverpool Victoria (LV=) | Bournemouth | Not confirmed | Protection sales GBP430m 2025 | Offers partially underwritten quotes with height and weight on Iress. | https://www.covermagazine.co.uk/news/4527627/lv-pays-151m-2025 |
| 5 | Zurich UK | Farnborough (confirm) | 10,001+ (global page) | Not confirmed | Live on iPipeline Advanced Underwriting and Iress; new Zurich Life chief underwriter Sept 2026. | https://www.mortgagesolutions.co.uk/news/2026/01/20/ipipeline-adds-scottish-widows-to-protection-platform/ |
| 6 | VitalityLife | London | 1,001-5,000 (Vitality UK) | Not confirmed | BMI is about 75% of its loadings; BMI-reduction benefit launched 15 Oct 2026. | https://www.vitality.co.uk/media/vitalitylife-announces-dub-to-recognise-impact-of-sustained-health-improvement/ |
| 7 | Scottish Widows | Edinburgh | 5,001-10,000 | Not confirmed | Joined iPipeline Advanced Underwriting Jan 2026; rules refined on UnderwriteMe platform. | https://www.mortgagesolutions.co.uk/mortgage-news/2026/01/20/ipipeline-adds-scottish-widows-to-protection-platform/ |
| 8 | Guardian Financial Services | London | 201-500 (confirm) | Not confirmed | Underwriting time under a day in H1 2026 through rule changes; next target cholesterol. | https://www.mortgagesolutions.co.uk/mortgage-news/2026/08/27/guardian-speeds-up-decisions-with-refined-underwriting/ |
| 9 | The Exeter | Exeter | Not confirmed | Gross premium income GBP135m 2025 | Live on iPipeline Advanced Underwriting and Iress; first insurer on UnderwriteMe's engine (2014). | https://www.mortgagesolutions.co.uk/mortgage-news/2026/06/26/the-exeter-reports-rise-in-income-protection-and-life-insurance-premiums-for-2025/ |
| 10 | Cirencester Friendly Society | Cirencester | 51-200 | About GBP21m premium income (undated, confirm) | IP specialist; minimum benefit guarantee May 2026. IP only. | https://www.icmif.org/news_story/cirencester-friendly-introduces-minimum-benefit-guarantee-as-income-protection-claims-data-highlights-changing-health-and-work-trends/ |
| 11 | Holloway Friendly | Gloucester | 11-50 (pre-merger) | Not confirmed; size to confirm | IP mutual with instant point-of-sale decisions; just merged with Wiltshire Friendly (flag). | https://www.covermagazine.co.uk/news/4528461/holloway-friendly-merge-wiltshire-friendly |
| 12 | British Friendly | Bedford | 51-200 | Not confirmed; size to confirm | IP cap raised to GBP10,000, non-medical limits reviewed, May 2026. | https://www.britishfriendly.com/ |
| 13 | Shepherds Friendly | Cheadle | 51-200 | Not confirmed; size to confirm | Underwritten IP; moved to Alula underwriting platform Sept 2025. | https://www.shepherdsfriendly.co.uk/ |
| 14 | National Friendly | Bristol | 51-200 | Not confirmed; size to confirm | Underwritten short-term IP with BMI questions on Iress. Marginal. | https://nationalfriendly.co.uk/ |
| 15 | Swiss Re UK | London | Not published | n/a (branch) | Magnum and Life Guide under UK insurers' rules; new UK L&H head from 1 Nov 2026. | https://www.insurancebusinessmag.com/uk/news/breaking-news/swiss-re-names-damien-bartlett-and-karen-tan-to-lead-landh-re-units-585629.aspx |
| 16 | Munich Re UK Life Branch | London | Not published | n/a (branch) | UK protection is one of three pillars; hiring a UK protection underwriting and claims strategy lead 2026. | https://careers.munichre.com/en/job/london/underwriting-and-claims-strategy-manager/3342/37511568000 |
| 17 | Hannover Re UK Life Branch | London | About 65 | n/a (branch) | Reinsures 2M+ UK protection lives. HOLD (face-scan study). | https://www.hannover-re.com/119661/hannover-re-uk-life-branch-london |
| 18 | Gen Re UK | London | Not published | n/a (branch) | Publishes UK Protection Pulse; Q1 2026 data Aug 2026. HOLD (selfie BMI app). | https://www.covermagazine.co.uk/news/4534036/protection-ape-board-gen |
| 19 | RGA UK | London | Not published | n/a (branch) | UK protection client team under a head of protection UK and Ireland. | https://www.rgare.com/global-presence/emea/united-kingdom/protection-client-management-team---united-kingdom |
| 20 | SCOR UK | London | Not published | n/a (branch) | UK L&H protection reinsurer; group Q1 2026 L&H margin driven by protection. | https://www.reinsurancene.ws/scor-posts-e225m-q126-profit-as-strong-renewals-lift-pc-revenue/ |
| 21 | Pacific Life Re | London | Not published | n/a (subsidiary) | Owns UnderwriteMe's engine; new Head of Underwriting and Claims, Protection, Europe May 2026. | https://www.reinsurancene.ws/pacific-life-re-hires-febby-mulewa-as-head-of-underwriting-and-claims-protection-europe/ |
| 22 | UnderwriteMe | London | 51-200 | Not confirmed | Decision Platform and Protection Platform; AI post-issue audit engine March 2026. | https://theintermediary.co.uk/2026/03/underwriteme-launches-ai-engine-for-post-issue-audit-misrepresentation-detection/ |
| 23 | Iress UK | Cheltenham | Not confirmed | n/a (UK arm) | The Exchange carries height, weight and waist questions for partially underwritten quotes. | https://www.iress.com/about/media-centre/2025/10/iress-expands-ex-smoker-pricing-to-multi-benefit-service-with-backing-from-nine-major-insurers/ |
| 24 | iPipeline UK | Cheltenham | 501-1,000 (global) | n/a (UK arm) | Advanced Underwriting captures top 20 disclosures pre-application; four insurers live. | https://www.mortgagesolutions.co.uk/news/2026/01/20/ipipeline-adds-scottish-widows-to-protection-platform/ |

Employee figures are LinkedIn size bands from search snippets, not counts. Revenue is shown only where a trade source gave a number; "Not confirmed" means none found. Small mutuals need a size check against the USD5M+ threshold (Holloway, British Friendly, Shepherds, National Friendly, Cirencester).

## Account facts (all 24 IN rows, for the messages card)

Facts are 1-3 per company, from the last 18 months where found. "None found" is stated where search did not return one; do not invent. Never-as-fact items from the hypothesis (claims-paid rates, ratings, market share, exits, deals, reinsurers, vendors) are excluded from the "usable" lines; deal and merger items are listed only as flags.

**Group A**
- Aviva: (1) 2026-06-18 non-medical underwriting limits changed, over 80% of medical exams moving from doctor to nurse-led screening, up to 50% faster. https://www.covermagazine.co.uk/news/4531397/aviva-updates-medical-underwriting-limits (2) Oct 2025 supports Iress ex-smoker pricing on the multi-benefit service. https://www.iress.com/about/media-centre/2025/10/iress-expands-ex-smoker-pricing-to-multi-benefit-service-with-backing-from-nine-major-insurers/
- Legal & General: (1) 2026-01-08 retail protection simplified life and CI application questions, split broad questions, "full blood" family history, to cut errors and manual referrals. https://www.mortgagesolutions.co.uk/mortgage-news/2026/01/08/lg-retail-protection-improves-underwriting-process/ and https://group.legalandgeneral.com/en/newsroom/press-releases/l-g-s-retail-protection-business-announces-underwriting-improvements-to-drive-better-customer-outcomes (2) 2026-02 simplified life and CI policy documents. https://group.legalandgeneral.com/newsroom/press-releases/2026/2/l-g-s-retail-protection-business-simplifies-life-and-critical-illness-policy-documents-to-support-advisers-and-drive-better-customer-outcomes/
- Royal London: (1) 2026 (reported 2026-08-05) income protection occupation classes refreshed: 545 occupations opened, lower prices for 162 more. https://www.covermagazine.co.uk/news/4533966/royal-london-records-rise-sales-amid-ip-changes (2) Oct 2025 supports Iress ex-smoker pricing (same Iress link as above).
- Liverpool Victoria (LV=): (1) No dated 2026 LV= underwriting change found. Closest: listed among providers offering partially underwritten quotes with height and weight on Iress, reported 2024-11-19 (older than 18 months). https://www.mortgagesolutions.co.uk/news/2024/11/19/national-friendly-supports-bmi-on-iress-the-exchange/ (2) 2026-03-27 LV= reported record protection share and GBP430m protection sales (financial, not for copy). https://www.covermagazine.co.uk/news/4527627/lv-pays-151m-2025
- Zurich UK: (1) 2026-07-15 Sabrina Lane named chief underwriter Zurich Life from 3 September 2026 (snippet only). https://healthcareandprotection.com/lane-appointed-zurich-life-chief-underwriter-as-bray-retires-exclusive/ (2) Live on iPipeline Advanced Underwriting (rolled out to all advisers Sept 2025). https://www.mortgagesolutions.co.uk/news/2026/01/20/ipipeline-adds-scottish-widows-to-protection-platform/
- VitalityLife: (1) 2026-10-15 Dynamic Underwriting Benefit: members with a BMI loading can lower it by reducing BMI; BMI is about 75% of loadings (company data), progress checked at the annual Vitality Healthcheck (search snippet; page returns 403 to this VPS, re-check by hand). https://www.vitality.co.uk/media/vitalitylife-announces-dub-to-recognise-impact-of-sustained-health-improvement/ (2) 2026-04 AI summaries of GP reports for life and CI underwriting (snippet only). https://healthcareandprotection.com/vitality-introduces-ai-summaries-of-gp-reports-for-life-and-ci-underwriting/ (3) Evidence Analyser and pre-sales likely-decision tool (undated, trade summary). https://covermagazine.co.uk/news/4021685/vitalitylife-introduces-immediate-access-underwriting-decisions
- Scottish Widows: (1) 2026-01-20 life, CI and IP added to iPipeline Advanced Underwriting. https://www.mortgagesolutions.co.uk/mortgage-news/2026/01/20/ipipeline-adds-scottish-widows-to-protection-platform/ (2) 2026-09-04 (sponsored piece, snippet only) continues to refine underwriting rules on the UnderwriteMe Protection Platform and its extranet. https://healthcareandprotection.com/new-business-protection-risk-report-reveals-the-hidden-consequences-of-success/
- Guardian Financial Services: (1) 2026-08-27 average protection underwriting time under a day in H1 2026 (from three days in 2025), instant-decision rate up about 5%, mental health disclosure rules updated, cholesterol next. https://www.mortgagesolutions.co.uk/mortgage-news/2026/08/27/guardian-speeds-up-decisions-with-refined-underwriting/ (2) Underwriting headcount up 35% after late-2025 hiring (same article).
- The Exeter: (1) Live on iPipeline Advanced Underwriting (2025-09 rollout; Jan 2026 article). https://www.mortgagesolutions.co.uk/mortgage-news/2026/01/20/ipipeline-adds-scottish-widows-to-protection-platform/ (2) May 2025 Real Life life product and Income First IP on Iress The Exchange. https://www.iress.com/media/documents/2504_Iress_Exeter_term_press_release_FINAL_APPROVED_FOR_RELEASE.docx.pdf No dated 2026 rule change found.
- Cirencester Friendly Society: (1) 2026-05-12 minimum benefit guarantee up to GBP1,500 a month on Income Assured and My Earnings, for irregular incomes. https://www.icmif.org/news_story/cirencester-friendly-introduces-minimum-benefit-guarantee-as-income-protection-claims-data-highlights-changing-health-and-work-trends/ and https://insurance-edge.net/2026/05/14/cirencester-friendly-launches-1500pcm-minimum-on-income-protection-product/
- Holloway Friendly: (1) No dated 2026 underwriting or proposition fact found beyond the merger (flag, never for copy): announced 2026-04-17, completed 2026-10-01. https://www.covermagazine.co.uk/news/4528461/holloway-friendly-merge-wiltshire-friendly (2) Instant point-of-sale underwriting decision with 24-hour turnaround where underwriting is needed (undated). https://covermagazine.co.uk/news/3028904/holloway-friendly-introduces-immediate-underwriting-decision (3) Joined UnderwriteMe Protection Platform 2024-06-06 (older than 18 months). https://underwriteme.co.uk/?p=9758
- British Friendly: (1) 2026-05-06/07 Protect benefit cap raised from GBP4,750 to GBP10,000, 104-week deferred period added, non-medical limits reviewed (biggest gains for younger applicants), My HealthHero app. https://insurance-edge.net/2026/05/07/british-friendly-adds-features-to-its-protect-product/ and https://healthcareandprotection.com/british-friendly-ups-ip-benefit-limits-and-adds-two-year-deferred-period/
- Shepherds Friendly: (1) 2025-09-09 partnership with Alula Technologies for a low-code underwriting platform, AI decisioning and document analysis planned. https://ifamagazine.com/shepherds-friendly-partners-with-alula-technologies-to-future-proof-underwriting/ (2) 2026-04 Income Protection Key Features: interactive underwriting, day-one cover. https://storage.shepherdsfriendly.co.uk/pdf-media/Income-Protection-Key-Features_2026.04.pdf
- National Friendly: (1) 2025-05 hazardous pursuits underwriting updated for IP and accident-only. https://nationalfriendly.co.uk/member/news-insights/press-releases/this-means-improved-clarity-for-the-product-national-friendly-updates-hazardous-pursuits-underwriting/ (2) 2024-11-19 height and weight (BMI) feature on Iress for IP quotes (older than 18 months). https://www.mortgagesolutions.co.uk/news/2024/11/19/national-friendly-supports-bmi-on-iress-the-exchange/ (3) Adviser IP underwriting guide dated March 2024, rules engine decides or refers. https://nationalfriendly.co.uk/media/a25dho3l/ip-underwriting-guide.pdf

**Group B**
- Swiss Re UK: (1) 2026-08-11 Damien Bartlett named head of Life & Health UK and Ireland and MEA from 1 November 2026; Karen Tan chief underwriting officer L&H Re from 1 October. https://www.insurancebusinessmag.com/uk/news/breaking-news/swiss-re-names-damien-bartlett-and-karen-tan-to-lead-landh-re-units-585629.aspx (2) Undated UK and Ireland L&H Underwriting Portfolio Lead role: UK underwriting philosophy, Life Guide manual. https://www.swissre.com/careers/job/L-and-H-Underwriting-Portfolio-Lead-80-100-/1428018433
- Munich Re UK Life Branch: (1) 2026 posting (closing 14 May 2026) for Underwriting & Claims Strategy Manager, UK Protection. https://careers.munichre.com/en/job/london/underwriting-and-claims-strategy-manager/3342/37511568000 (2) 2026 Senior Transformation Underwriter role maintaining the UK underwriting philosophy. https://careers.munichre.com/en/job/london/senior-transformation-underwriter/3342/31297145088 (3) Jobs, not announcements; no 2026 press item found.
- Hannover Re UK Life Branch: (1) UK branch reinsures over 2 million UK lives, mortality and CI, about 65 staff; Chief Underwriter and Head of Protection named on its site. https://www.hannover-re.com/119661/hannover-re-uk-life-branch-london (2) 2024-09 article on the Alula rPPG face-scan study (see displacement). https://life-and-health-uk.hannover-re.com/changing-the-face-of-preventative-healthcare-part-2/ No 2026 UK item found.
- Gen Re UK: (1) 2026-08-06 Protection Pulse Q1 2026: total APE GBP219m, underwritten whole of life APE up 45%. https://www.covermagazine.co.uk/news/4534036/protection-ape-board-gen (market data, usable as context only)
- RGA UK: (1) Head of Protection UK and Ireland (joined 2024) leads business development, pricing, claims and underwriting. https://www.rgare.com/our-company/people/detail/anna-graham No dated UK-specific 2026 fact found; group-level Q2 2026 call said underwriting is becoming a primary value driver (not UK). https://earningswhispers.com/transcript/RGA/Q22026
- SCOR UK: (1) 2024-07 hired a former AIG chief underwriter to lead L&H underwriting for UK and Ireland (older than 18 months). https://www.intelligentinsurer.com/top-aig-underwriter-departs-to-join-scor-in-key-uk-role (2) Q1 2026 group L&H new business CSM EUR115m driven by protection and longevity (group). https://www.reinsurancene.ws/scor-posts-e225m-q126-profit-as-strong-renewals-lift-pc-revenue/ No UK-specific 2026 fact found.
- Pacific Life Re: (1) 2026-05-15 Febby Mulewa appointed Head of Underwriting and Claims, Protection, Europe (from Swiss Re). https://www.reinsurancene.ws/pacific-life-re-hires-febby-mulewa-as-head-of-underwriting-and-claims-protection-europe/ (2) 2025-06 Sarah Cheng succeeds Andrew Murphy as MD Europe and North America protection (snippet only). https://healthcareandprotection.com/cheng-succeeds-murphy-as-pacific-life-re-europe-and-north-america-protection-md/

**Group C**
- UnderwriteMe: (1) 2026-03-18 AI Engine for Post-Issue Audits launched for UK life insurers on the Decision Platform. https://theintermediary.co.uk/2026/03/underwriteme-launches-ai-engine-for-post-issue-audit-misrepresentation-detection/ (2) Two products confirmed in the hypothesis (Decision Platform for insurers, Protection Platform for advisers). https://www.underwriteme.co.uk/about-us
- Iress UK: (1) Oct 2025 ex-smoker pricing extended to multi-benefit service, nine insurers (Aviva, HSBC, L&G, Royal London, Vitality, Zurich, National Friendly, Walsham Brothers, Scottish Widows). https://www.iress.com/about/media-centre/2025/10/iress-expands-ex-smoker-pricing-to-multi-benefit-service-with-backing-from-nine-major-insurers/ (2) Height, weight and waist questions on The Exchange return partially underwritten quotes; BMI drives most underwriting-related price increases (undated, about 2022-2024). https://covermagazine.co.uk/news/3000211/iress-reforms-underwriting-capability-bmi
- iPipeline UK: (1) 2026-01-20 Scottish Widows is the fourth provider on Advanced Underwriting after The Exeter, Vitality and Zurich. https://www.mortgagesolutions.co.uk/news/2026/01/20/ipipeline-adds-scottish-widows-to-protection-platform/ (2) 2025-09-01 rolled out to all advisers through SolutionBuilder. https://www.mortgagesolutions.co.uk/mortgage-news/2025/09/01/ipipeline-rolls-out-advanced-underwriting-feature-to-all-advisers/

## Displacement search results (held for Vadim, not dropped)

Searches run: UK selfie or photo BMI underwriting; reinsurer remote BMI from image or video; 3D body scan smartphone UK protection; Vitality BMI remote measurement; photo, selfie or video build verification at named UK insurers; Hannover Re UK pilot. No UK protection insurer was found running a remote body scan, face or video BMI estimate, selfie quote or image-based build tool in its application. Search coverage of insurer application journeys is thin, so "none found" is not "none exists".

HOLD-FOR-VADIM:
1. Legal & General. Legal & General America launched SelfieQuote (Lapetus face photo, estimates age, gender and BMI, term quote) as a 2017 beta. A US executive said the UK team was "preparing to launch it in the UK" with the same vendor. No UK launch was found. Sources: https://insurancebusinessmag.com/us/news/technology/lga-launches-fun-and-simple-selfiequote-tool-90113.aspx and https://dig-in.com/news/legal-general-plans-big-push-for-biometric-quoting-tool (undated in search). The 2026 L&G underwriting fact is separate and current.
2. Hannover Re UK Life Branch. UK branch ran a pilot with Alula (VivaScore, rPPG face scan): 12 weeks, 30 staff, then a larger study of over 1,000 insured customers comparing face scans with blood pressure, cholesterol and glucose (article September 2024; results not published in what we found). It does not claim a BMI estimate. Group Hannover Re ran a 26-week Nuralogix Anura video-selfie study with 1,650 applicants and staff in South Africa, which includes BMI. Sources: https://life-and-health-uk.hannover-re.com/202406-changing-the-face-of-preventative-healthcare/ , https://life-and-health-uk.hannover-re.com/changing-the-face-of-preventative-healthcare-part-2/ , https://www.hannover-re.com/en/life-and-health/inspire/underwriting-case-studies/ai-video-technology-for-health-and-risk-insights/
3. Gen Re UK. Gen Re developed a facial-analytics app on Lapetus technology estimating age, gender and BMI from a selfie (2019, prototype, US and Asia testing). No UK deployment found. Sources: https://www.reinsurancene.ws/gen-re-develops-facial-analytics-app-for-insurance-buyers/ and https://www.dig-in.com/news/gen-re-pilots-selfie-based-life-insurance-underwriting

Soft flags:
- Zurich UK: launched FaceQuote selfie app in 2017 to estimate cover needed, not build; no current use found.
- Shepherds Friendly: Alula underwriting platform since 2025-09; Alula also sells an rPPG face-scan app, but no rPPG use at Shepherds was reported.
- VitalityLife: BMI progress is verified through the annual Vitality Healthcheck (in person), not a remote scan.

## Detailed notes (top 10)

Ranked by fit and by how much a build-evidence step changes the point-of-sale decision.

### 1. VitalityLife
- Website: https://www.vitality.co.uk (403 to this VPS; expect `blocked:*` in web-verify)
- LinkedIn: https://uk.linkedin.com/company/vitalityuk (shared with Vitality health; restrict titles to life and protection)
- Recent news / triggers: 2026-10-15 launch of a benefit that lowers a BMI loading when a member reduces BMI.
- Tech stack hints: iPipeline Advanced Underwriting live; Evidence Analyser; AI summaries of GP reports (April 2026).
- Why fit: BMI makes up about 75% of loadings on its plans by its own data, and it has just built a product around changing BMI. Build evidence is the center of its proposition, so a second source of build at application is a direct question for its underwriting and proposition teams.

### 2. Aviva
- Website: https://www.aviva.co.uk
- LinkedIn: https://uk.linkedin.com/company/aviva-plc (group page; Sales Nav needs UK filter)
- Recent news / triggers: 2026-06-18 non-medical limits changed, over 80% of medical exams to nurse screening.
- Tech stack hints: Iress partially underwritten quotes (first provider to use height, weight, waist); Iress ex-smoker pricing.
- Why fit: Largest UK writer, actively changing which cases get evidence. Fewer doctor exams means more cases where build is declared and not measured. The AIG Life deal is not mentioned in any copy.

### 3. Royal London
- Website: https://www.royallondon.com
- LinkedIn: https://uk.linkedin.com/company/royallondon
- Recent news / triggers: 2026 IP occupation refresh; H1 2026 results 2026-08-05.
- Tech stack hints: Iress ex-smoker pricing supporter.
- Why fit: Protection growth led by income protection and HNW cases, both of which rate build. A mutual with a long record of non-medical limit changes.

### 4. Scottish Widows
- Website: https://www.scottishwidows.co.uk
- LinkedIn: https://uk.linkedin.com/company/scottish-widows
- Recent news / triggers: iPipeline Advanced Underwriting go-live January 2026; wrap access June 2026 (headline only).
- Tech stack hints: UnderwriteMe Protection Platform, iPipeline, Iress.
- Why fit: Its share has risen on adviser volume, and it sits on all three group C platforms, so the declaration step is already digital and rule-driven.

### 5. Zurich UK
- Website: https://www.zurich.co.uk
- LinkedIn: https://www.linkedin.com/company/zurich-insurance-company-ltd (global) and https://uk.linkedin.com/showcase/zurichuk/
- Recent news / triggers: new Zurich Life chief underwriter from 3 September 2026.
- Tech stack hints: iPipeline Advanced Underwriting, Iress.
- Why fit: Mid-size adviser-market protection insurer on two platforms, with a leadership change in underwriting that opens the philosophy question.

### 6. Pacific Life Re
- Website: https://www.pacificlifere.com
- LinkedIn: https://www.linkedin.com/company/pacific-life-re
- Recent news / triggers: Head of Underwriting and Claims, Protection, Europe hired 2026-05-15.
- Tech stack hints: owns UnderwriteMe's engine; the Exeter's rules engine launched 2014 on it.
- Why fit: Reinsurer that co-owns the build decision for several UK insurers through the UnderwriteMe engine, and new underwriting leadership for Europe protection.

### 7. Legal & General
- Website: https://www.legalandgeneral.com
- LinkedIn: https://www.linkedin.com/company/legal-&-general
- Recent news / triggers: 2026-01-08 application question changes.
- Tech stack hints: Iress ex-smoker pricing supporter.
- Why fit: Largest adviser-channel term writer; question redesign aimed at fewer manual referrals. HOLD: see SelfieQuote precedent; Vadim decides whether to proceed before step 3.

### 8. Guardian Financial Services
- Website: https://guardianfs.co.uk
- LinkedIn: https://uk.linkedin.com/company/guardian-financial-services
- Recent news / triggers: underwriting under a day in H1 2026, more underwriters hired.
- Tech stack hints: Iress partially underwritten quotes; Protection Builder.
- Why fit: Newer insurer competing on speed, tuning rules disclosure by disclosure; a build step that adds no friction fits its approach. LinkedIn page needs people checks (similar names).

### 9. Swiss Re UK
- Website: https://www.swissre.com (403 to this VPS)
- LinkedIn: https://www.linkedin.com/company/swiss-re (global)
- Recent news / triggers: new UK and Ireland L&H head from 1 November 2026.
- Tech stack hints: Magnum Pure, Life Guide manual, Life Guide Scout pilot.
- Why fit: Its engine and manual set the build rules inside several UK insurers, and a new market-unit head from 1 November makes a client-evaluation conversation timely.

### 10. The Exeter
- Website: https://www.the-exeter.com
- LinkedIn: https://www.linkedin.com/company/exeter-family-friendly
- Recent news / triggers: iPipeline Advanced Underwriting live; life new business up in 2025.
- Tech stack hints: UnderwriteMe engine since 2014, Iress, iPipeline.
- Why fit: A mid-size mutual live on every platform in group C, with a rules engine built on Pacific Life Re's engine. Small enough for one team to run a shadow evaluation.

## Excluded candidates and why
- Chesnara Life, Phoenix, ReAssure: closed books or consolidators (anti-case; Chesnara OUT by Vadim decision 6).
- OneFamily (Beagle Street underwriter): application has no medical or financial underwriting, OneFamily's site says no exams (2023 report, current position to confirm); merger with Scottish Friendly agreed 2026-02-04, effective early 2027. Fails "open to new underwritten business" and is in transition.
- Scottish Friendly: merger with OneFamily pending (above); protection mostly sold through partners such as Guardian and a shift to own-brand; protection sales fell 8% in 2025. Not confirmed as underwriting its own individual protection.
- Wesleyan: sells income protection to medical, dental and legal professionals, but public pages did not show which entity underwrites it and wesleyan.co.uk blocks this VPS (Azure WAF). Not confirmed open to new underwritten business as insurer; if Vadim wants it, a manual check of the key features document is needed.
- MetLife UK: individual protection (EverydayProtect) asks no health questions; build not used. Fails the criterion.
- Canada Life UK (2022), Aegon UK (2023), AIG Life (to Aviva): exited individual protection (anti-case).
- Irish arms (Irish Life, New Ireland, Canada Life International): not this profile's market.
- Group risk, PMI, brokers, comparison sites, nurse-screening and GP-report suppliers: out of scope per Anti-cases; not widened.
- Registry exclusions: none. `phoenix-health` (covered by katerina, 2026-09-27) is not a candidate.

## Coverage gaps / risks
- 24 IN against a target of 25. The gap is the four drops above; each fails a stated criterion. No padding.
- Fewer than 25 also means that any Vadim exclusion on HOLD rows (L&G, Hannover Re UK, Gen Re UK) takes the list to 21, below the floor of 22. Decide on those three before step 3. Excluding National Friendly or Holloway as well would deepen that.
- Four rows are small income-protection mutuals (Cirencester, Holloway, British Friendly, Shepherds) plus National Friendly: IP only or IP-led, thin revenue evidence against USD5M+, and likely few senior underwriting titles in Sales Navigator. They carry fit 2-3.
- Holloway Friendly merged with Wiltshire Friendly on 2026-10-01 (universal exclusion for recent acquisitions and transitions; Holloway is the surviving entity). Included with a flag; Vadim to confirm.
- Six rows use a global LinkedIn page (Swiss Re, Munich Re, Hannover Re, Gen Re, RGA, SCOR, Pacific Life Re's Bermuda-listed page, also Aviva, L&G, Zurich, iPipeline): Sales Navigator needs the United Kingdom geography filter, per the coordinator. Iress's company page was not found by search; the slug in the CSV is expected, not confirmed.
- Group B and C have no verified UK-specific 2026 news for RGA UK, SCOR UK, Munich Re UK (jobs only) and Hannover Re UK. Facts there are thin; the messages card should lean on group lanes.
- web-verify will mark lv.com, vitality.co.uk and swissre.com as blocked (403 from this VPS; curl tested 2026-10-22). Not dead.
- Company size: LinkedIn bands only; no employee counts were invented.
- Trade-press dates: some facts rest on Health & Protection or IFA Magazine snippets because those sites block this VPS. They are marked "snippet only"; confirm before the Account facts block is written.
- LV= key: the two-letter slug `lv` should not join unrelated rows. The row is `Liverpool Victoria (LV=)`.
