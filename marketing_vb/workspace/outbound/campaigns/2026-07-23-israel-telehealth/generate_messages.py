#!/usr/bin/env python3
"""Generate LinkedIn Message 1 and Message 2 for each Tier 1 contact (b01+b02).
Version 2: much richer role-specific personalization."""

import csv
import os
import json

BASE_DIR = "/home/vadim_prod/3dlook-marketing/marketing_vb/workspace/outbound/campaigns/2026-07-23-israel-telehealth"
OUT_DIR = os.path.join(BASE_DIR, "messages")
os.makedirs(OUT_DIR, exist_ok=True)

KATYA_CAL = "https://meetings.hubspot.com/kateryna-boichuk"

# =========================================================
# PER-CONTACT MESSAGE DATA (hand-crafted for specificity)
# Each entry: person_id -> {m1_hook, m1_obs, m1_product, m1_cta, m2_value, m2_cta}
# =========================================================

CONTACTS = {}

def add(p_id, first, last, title, company, m1_hook, m1_obs, m1_product, m1_cta, m2_value, m2_cta):
    CONTACTS[p_id] = {
        "first": first, "last": last, "title": title, "company": company,
        "m1_hook": m1_hook, "m1_obs": m1_obs, "m1_product": m1_product,
        "m1_cta": m1_cta, "m2_value": m2_value, "m2_cta": m2_cta,
    }

# --- Product intro variants ---
P_A = "At 3DLOOK, we built FitXpress: a mobile body scanning layer. Two smartphone photos give members 80+ body measurements and composition, verified and HIPAA-compliant, dropping into the patient record."
P_B = "We built FitXpress to solve this: mobile body scanning from two phone photos. Members get consistent body metrics and composition with the audit trail and compliance (HIPAA/GDPR) health systems need."
P_C = "At 3DLOOK, we built FitXpress: mobile body scanning that gives members consistent anthropometrics from two photos. Structured, trackable metrics and body composition, ready for digital health workflows."
P_D = "We built FitXpress for this: a mobile scanning layer that captures consistent body metrics from the phone camera. Two photos, 80+ measurements, body composition, HIPAA-compliant records."
P_E = "FitXpress, our product at 3DLOOK, does exactly this: mobile body scanning from two phone photos. Members get consistent measurements and body composition, HIPAA-compliant, with audit-ready data."

# --- Message 1 CTA variants ---
CTA1_A = "Might be worth a quick chat?"
CTA1_B = "Worth a quick chat to explore?"
CTA1_C = "Open to a quick chat?"

# --- Message 2 CTA variants ---
CTA2_A = "Worth 15 min to walk through it? Grab a slot:"
CTA2_B = "Worth a quick 15 min demo? Grab a slot:"
CTA2_C = "Worth 15 min to see how it works? Grab a slot:"

# =========================================================
# B01 CONTACTS
# =========================================================

# b01-1: Ilan Marcuschamer - Director of Cardiac rehabilitation center - Clalit
add("b01-1", "Ilan", "Marcuschamer", "Director of Cardiac rehabilitation center", "Clalit Health Services",
    "Circling back",
    "curious how cardiac rehab programs at Clalit are handling body-measurement tracking between sessions. Members need consistent anthropometrics over time, especially for weight-related cardiac risk, and remote options are still limited in most rehab workflows.",
    P_A, CTA1_A,
    "Where FitXpress helps cardiac rehab: members can capture consistent body measurements from home between clinic visits. Programs get better longitudinal data on weight and waist trends without asking staff to do extra manual measurements.",
    CTA2_A)

# b01-2: Avigail Orgad - Director of Global Supply Chain - TytoCare
add("b01-2", "Avigail", "Orgad", "Director of Global Supply Chain", "TytoCare",
    "Quick thought",
    "how TytoCare thinks about expanding its remote exam kit with new diagnostic modules. Body composition is one area where the data layer is thin across telehealth, and bundling it alongside existing devices could strengthen the kit's clinical value for weight-management programs.",
    P_B, CTA1_B,
    "Where FitXpress complements TytoCare's hardware: remote exam kits cover vitals, but body measurements are still a blind spot. Adding mobile body scanning as a software module alongside your devices gives clinicians a more complete patient picture without extra hardware.",
    CTA2_B)

# b01-3: Tamir Gotfried - Chief Business & Strategy Officer - TytoCare
add("b01-3", "Tamir", "Gotfried", "Chief Business & Strategy Officer", "TytoCare",
    "Noticed your background",
    "the partnership side of telehealth expansion. Platforms bundling remote diagnostics keep looking for modules that add clinical depth, and body composition is one area where the data layer is still underdeveloped across most telehealth stacks.",
    P_C, CTA1_C,
    "The opportunity we see with telehealth platforms: bundling body scanning alongside remote exam tools creates a more complete virtual visit. Patients get visual progress data between calls, and clinicians get objective metrics without in-person follow-ups. Could strengthen TytoCare's clinical value proposition.",
    CTA2_C)

# b01-4: Yael Shaham - Board Member - Clalit
add("b01-4", "Yael", "Shaham", "Board Member", "Clalit Health Services",
    "Came across your work",
    "how Clalit's leadership is thinking about member engagement in weight and chronic-disease programs. With half of Israel's population under Clalit's care, even modest improvements in remote monitoring could shift population-level health outcomes measurably.",
    P_D, CTA1_A,
    "At Clalit's scale, consistent body data from members at home could strengthen chronic-disease outcome reporting and program ROI data. FitXpress adds that layer: mobile body scanning from two photos, HIPAA-compliant, dropping structured metrics into the patient record.",
    CTA2_A)

# b01-5: Karin Zeevi - Head Of Marketing - Leumit
add("b01-5", "Karin", "Zeevi", "Head Of Marketing", "Leumit Health Services",
    "Saw your activity",
    "how Leumit positions its digital member experience. Israeli HMOs are competing on digital engagement, and objective body-data tools that members can use at home could be a differentiator, especially for weight-management and wellness programs.",
    P_E, CTA1_B,
    "Where FitXpress helps HMO marketing teams: when members can track real body change from their phone, program sign-ups and retention both improve. It's a member-facing tool that also feeds structured data back to clinical teams. Worth seeing how Leumit could position it.",
    CTA2_B)

# b01-6: Ran Balicer - Deputy Director General and Head of the Innovation Division - Clalit
add("b01-6", "Ran", "Balicer", "Deputy Director General and Head of the Innovation Division", "Clalit Health Services",
    "Had a thought",
    "about Clalit's innovation roadmap for remote patient monitoring. Israel leads in digital health adoption, and body-scanning tech that works from any smartphone could fit naturally into Clalit's existing digital member channels for weight and chronic-care programs.",
    P_A, CTA1_C,
    "The pattern across HMO innovation teams: when members can capture body measurements at home via their phone, program completion rates improve and provider trust in remote data goes up. FitXpress adds that layer without changing clinical workflows. Could be a fit for Clalit's innovation pipeline.",
    CTA2_C)

# b01-7: Anat Lichtig - Deputy CEO head of marketing and customer care division - Maccabi
add("b01-7", "Anat", "Lichtig", "Deputy CEO head of marketing and customer care division", "Maccabi Health care Services",
    "Spotted something",
    "about how Maccabi Connect is evolving the member digital experience. Adding body-scanning as a self-service tool within the app could strengthen engagement for weight-management and wellness programs while feeding structured data back to care teams.",
    P_B, CTA1_A,
    "Where FitXpress helps HMO member experience: members in weight programs stay engaged longer when they can see real body change between visits. Adding mobile scanning to Maccabi's digital channels gives members a visual progress tool and care teams objective metrics, without adding staff workload.",
    CTA2_A)

# b01-8: Yifat Godiner - Board Member - Clalit
add("b01-8", "Yifat", "Godiner", "Board Member", "Clalit Health Services",
    "Noticed your background",
    "how Clalit's board evaluates digital health tools that can improve chronic-disease outcomes at scale. Body-measurement consistency across such a large member base is a real challenge, and remote scanning could tighten the data quality for population-level reporting.",
    P_C, CTA1_B,
    "At Clalit's population scale, consistent remote body measurements could improve chronic-disease program reporting and demonstrate ROI to stakeholders. FitXpress gives members a phone-based scanning tool that feeds structured metrics into the care record, HIPAA-compliant and audit-ready.",
    CTA2_B)

# b01-9: Etti Rosenberg - Founder & Director, IOSMC Method - Clalit
add("b01-9", "Etti", "Rosenberg", "Founder & Director, IOSMC Method", "Clalit Health Services",
    "Curious about your take",
    "on how the IOSMC method tracks body-composition changes over the course of treatment. Any structured weight-loss program needs consistent anthropometric data, and getting that remotely between sessions could strengthen both clinical decisions and patient motivation.",
    P_D, CTA1_C,
    "Where FitXpress helps structured weight-loss programs: members can capture consistent body measurements from their phone between visits. Programs get better longitudinal data on body-composition trends, and patients stay motivated seeing real visual progress. Fits naturally into a method like IOSMC.",
    CTA2_C)

# b01-10: Ariel Braverman - Occupational Health - Director of Nursing - Clalit
add("b01-10", "Ariel", "Braverman", "Occupational Health - Director of Nursing", "Clalit Health Services",
    "Quick note",
    "on how occupational health screening handles body-measurement consistency across nurses and sites. Manual measurements introduce variability between staff, and a standardized remote capture tool could reduce that gap for pre-employment and periodic health assessments.",
    P_E, CTA1_A,
    "Where FitXpress helps occupational health: standardizing body-measurement capture across screening sites. Members do a quick phone scan, and the system returns consistent metrics every time, reducing variability between nurses and speeding clearance decisions.",
    CTA2_A)

# b01-11: Michael Kegen - Director of Demand Gen - TytoCare
add("b01-11", "Michael", "Kegen", "Director of Demand Gen", "TytoCare",
    "Caught my eye",
    "how TytoCare's demand gen positions the remote exam kit's clinical value. Adding a body-scanning module to the narrative could open up new buyer conversations in weight management, bariatrics, and chronic care where objective body data is a missing piece.",
    P_A, CTA1_B,
    "Where FitXpress expands the telehealth value story: body scanning adds a new clinical dimension to the remote exam pitch. Health systems evaluating TytoCare for weight-management programs get a more complete package when body-composition data is part of the remote visit.",
    CTA2_B)

# b01-12: Sigal Dadon - Chief Executive Officer - Maccabi
add("b01-12", "Sigal", "Dadon", "Chief Executive Officer", "Maccabi Health care Services",
    "Wanted to reach out",
    "about how Maccabi is approaching body-data capture across its digital member services. As Israel's second-largest HMO with a strong digital-health reputation, adding mobile body scanning to the member app could strengthen chronic-care outcomes and differentiate the member experience.",
    P_B, CTA1_C,
    "At Maccabi's scale, giving members a phone-based body scanning tool could improve chronic-disease program metrics and member retention. FitXpress does this: two photos, consistent body metrics and composition, HIPAA-compliant, feeding structured data into the care record.",
    CTA2_C)

# b01-13: Roni Antman - OCIO Director, Head of IT Projects department - Meuhedet
add("b01-13", "Roni", "Antman", "OCIO Director, Head of IT Projects department", "Meuhedet Health Services - מאוחדת",
    "Quick one",
    "about Meuhedet's IT project pipeline for member-facing digital tools. Body scanning from a smartphone is a lightweight integration that could add clinical depth to existing digital channels without requiring heavy infrastructure changes.",
    P_C, CTA1_A,
    "FitXpress integrates via API/SDK, so it slots into existing HMO digital infrastructure without a heavy lift. Members scan from their phone, and structured body metrics flow into the care record. Could fit into Meuhedet's IT roadmap as a quick-win digital health module.",
    CTA2_A)

# b01-14: Yaron Sheffer - Head of Strategy & business development - Clalit
add("b01-14", "Yaron", "Sheffer", "Head of Strategy & business development", "Clalit Health Services",
    "Got me thinking",
    "about Clalit's strategic priorities for digital health partnerships. Body scanning technology that works from any smartphone could be a low-friction add-on to existing chronic-care programs, strengthening outcome data without heavy operational investment.",
    P_D, CTA1_B,
    "From a strategy perspective: mobile body scanning gives Clalit's chronic-disease programs a standardized data layer that improves outcome reporting and member engagement. FitXpress is already live with health platforms processing tens of thousands of scans per year. Worth exploring for Clalit's pipeline.",
    CTA2_B)

# b01-15: Eyal Reinstein - Director of Genetics - Maccabi
add("b01-15", "Eyal", "Reinstein", "Director of Genetics", "Maccabi Health care Services",
    "Had a thought",
    "about how genomics programs can connect genetic risk profiles with objective body metrics. Consistent anthropometric data alongside genetic markers could strengthen risk stratification and preventive-care recommendations, especially for obesity-related conditions.",
    P_E, CTA1_C,
    "Where FitXpress adds to genomics programs: consistent body measurements from home give clinicians objective phenotype data to correlate with genetic profiles. For obesity-risk counseling and preventive care, having real body-composition trends strengthens the clinical picture.",
    CTA2_C)

# b01-16: Shany Chinsky - Head of Marketing - TytoCare
add("b01-16", "Shany", "Chinsky", "Head of Marketing", "TytoCare",
    "Noticed overlap",
    "between TytoCare's remote exam positioning and the growing demand for body-composition data in telehealth. Health systems evaluating virtual care platforms increasingly want objective body metrics alongside vitals, especially for weight-management and chronic-disease programs.",
    P_A, CTA1_A,
    "Co-marketing angle: TytoCare's remote exam kit plus FitXpress body scanning could be positioned as a complete virtual-assessment package for weight-management and chronic care. Two complementary tools, one integrated member experience. Worth a conversation.",
    CTA2_A)

# b01-17: Yaniv Ovadia - Head of Technologies and Imaging - Maccabi
add("b01-17", "Yaniv", "Ovadia", "Head of Technologies and Imaging", "Maccabi Health care Services",
    "Made me think",
    "about how Maccabi's imaging and technology division evaluates new diagnostic tools. Body scanning from a smartphone is an interesting bridge between consumer mobile tech and clinical-grade measurement, and it fits naturally into a digital imaging pipeline.",
    P_B, CTA1_B,
    "FitXpress produces structured body measurements with 96-97% accuracy against manual benchmarks and under 1 cm repeatability across scans. For Maccabi's imaging and tech team, it's a software-based diagnostic tool that integrates via API and feeds consistent data into existing systems.",
    CTA2_B)

# b01-18: Omer Rosenblum - Head of Medical Education - Maccabi
add("b01-18", "Omer", "Rosenblum", "Head of Medical Education", "Maccabi Health care Services",
    "This stood out",
    "when thinking about medical education and the gap between what doctors learn about body measurement and what actually happens in practice. Manual anthropometrics vary between clinicians, and a standardized digital tool could be valuable for training consistency.",
    P_C, CTA1_C,
    "Where FitXpress helps medical education: it gives clinicians a standardized body-measurement reference tool. Residents and GPs can compare their manual measurements against consistent digital outputs, improving skill calibration. Also useful for teaching remote patient assessment.",
    CTA2_C)

# b01-19: Irit Singer - Board Member - Clalit
add("b01-19", "Irit", "Singer", "Board Member", "Clalit Health Services",
    "Spotted something",
    "in Clalit's chronic-disease strategy that made me think about measurement infrastructure. With Israel's high diabetes and obesity rates, a standardized body-data layer across Clalit's programs could sharpen population-health analytics and program evaluation.",
    P_D, CTA1_A,
    "At Clalit's population scale, standardized body measurements from members at home could improve chronic-disease program metrics and demonstrate clear ROI. FitXpress adds that layer: consistent, HIPAA-compliant body data from a smartphone, feeding structured metrics into the care record.",
    CTA2_A)

# b01-20: Ran Zahor - CTO | Technology Division Manager - Leumit
add("b01-20", "Ran", "Zahor", "CTO | Technology Division Manager", "Leumit Health Services",
    "Quick thought",
    "on Leumit's tech stack and where body-data capture fits. Adding mobile scanning via API could give Leumit's digital services a new data layer for weight and chronic-care programs without a heavy infrastructure project.",
    P_E, CTA1_B,
    "FitXpress integrates via API/SDK, producing structured body metrics from two phone photos. For Leumit's tech division, it's a lightweight integration that adds clinical depth to existing digital channels. Already processing 34K+ scans per year at other health platforms.",
    CTA2_B)

# b01-21: Amir Sheinfeld - Head of Data & AI Delivery & Project Management - Maccabi
add("b01-21", "Amir", "Sheinfeld", "Head of Data & AI Delivery & Project Management", "Maccabi Health care Services",
    "Noticed your background",
    "in data and AI delivery. Body scanning data is a rich structured dataset that could feed into Maccabi's predictive models for chronic-disease management. Consistent anthropometrics from members at home add a new signal layer to existing health data pipelines.",
    P_A, CTA1_C,
    "The data angle: FitXpress produces structured, consistent body-measurement data from smartphone scans. For Maccabi's AI and data teams, this is a new structured-data stream that can feed predictive models for weight-related conditions, with audit-ready provenance and HIPAA compliance.",
    CTA2_C)

# b01-22: Lea Cohen - Chief AI Officer - Meuhedet
add("b01-22", "Lea", "Cohen", "Chief AI Officer", "Meuhedet Health Services - מאוחדת",
    "Saw your activity",
    "in AI leadership at Meuhedet. Body scanning produces structured anthropometric data that could enrich Meuhedet's machine learning models for chronic-disease risk prediction. Consistent remote measurements from members add a signal that self-reported weight doesn't capture.",
    P_B, CTA1_A,
    "From an AI perspective: FitXpress generates structured body-measurement data with 96-97% accuracy, under 1 cm repeatability. For Meuhedet's models, this is a high-quality data stream that can strengthen risk stratification for obesity, diabetes, and metabolic conditions.",
    CTA2_A)

# b01-23: Yaron Savoray - Chief Financial Officer - K Health
add("b01-23", "Yaron", "Savoray", "Chief Financial Officer", "K Health",
    "Curious about your take",
    "on K Health's unit economics for chronic-condition care paths. Adding body-composition tracking to the AI-assisted care flow could improve member retention and outcome metrics, both of which strengthen the financial case for payer and employer partnerships.",
    P_C, CTA1_B,
    "The business case: health platforms adding objective body data to their care flows see better member retention and stronger outcome metrics. FitXpress does this via mobile scanning, and it's already live at platforms processing 34K+ scans per year. Worth looking at the numbers for K Health.",
    CTA2_B)

# b01-24: Michal G. - Head of Addiction Prevention & Treatment | Sharon District - Maccabi
add("b01-24", "Michal", "G.", "Head of Addiction Prevention & Treatment | Sharon District", "Maccabi Health care Services",
    "Quick note",
    "on addiction treatment and the role of physical health monitoring. Substance-use recovery programs often overlook body-composition tracking, but weight and metabolic changes are common during treatment and can signal relapse risk or treatment side effects.",
    P_D, CTA1_C,
    "Where FitXpress helps behavioral health programs: consistent body measurements from home give clinicians an objective window into physical health changes during addiction treatment. Weight shifts and body-composition trends can complement behavioral assessments without adding visit burden.",
    CTA2_C)

# b01-25: Rakefet Jacoby - CIO, VP Information Technology - Leumit
add("b01-25", "Rakefet", "Jacoby", "CIO, VP Information Technology", "Leumit Health Services",
    "Had a thought",
    "about Leumit's IT architecture for member-facing digital tools. Mobile body scanning is an API-first integration that adds clinical data depth without requiring changes to core EMR systems, making it a relatively low-risk addition to the digital roadmap.",
    P_E, CTA1_A,
    "FitXpress integrates via API/SDK and returns structured body metrics from two phone photos. For Leumit's IT team, it's a lightweight addition to the digital stack, HIPAA-compliant, with audit-ready data that fits into existing care-record workflows.",
    CTA2_A)

# b01-26: Tamir Kaplan - Head Of Operations - International Markets - K Health
add("b01-26", "Tamir", "Kaplan", "Head Of Operations - International Markets", "K Health",
    "Made me think",
    "about the operational side of launching body-data features in K Health's international markets. Mobile body scanning works in any geo where members have a smartphone, and it adds a standardized data layer that translates across markets without localization complexity.",
    P_A, CTA1_B,
    "For international rollout: FitXpress works from any smartphone camera, no hardware needed. Members in any market get the same consistent body metrics, and the data feeds into K Health's AI-assisted care flows. Could be a lightweight feature add for new market launches.",
    CTA2_B)

# b01-27: Roy Zucker, MD - Director For LGBTQ health services - Clalit
add("b01-27", "Roy", "Zucker, MD", "Director For LGBTQ health services", "Clalit Health Services",
    "Noticed your background",
    "in LGBTQ health services at Clalit. Body-composition tracking can be especially relevant for transgender patients on hormone therapy, where physical changes are an important clinical marker, and sensitive remote monitoring could reduce the need for frequent in-person measurements.",
    P_B, CTA1_C,
    "Where FitXpress helps specialized health services: members can track body changes privately from home, reducing the need for frequent in-clinic measurements. For patients on hormone therapy or weight-management programs, it adds a sensitive, self-managed data layer that clinicians can review remotely.",
    CTA2_C)

# =========================================================
# B02 CONTACTS
# =========================================================

# b02-1: Gal Yankovitz - Director of B2B Product Marketing - TytoCare
add("b02-1", "Gal", "Yankovitz", "Director of B2B Product Marketing", "TytoCare",
    "Caught my eye",
    "how TytoCare positions its platform to health-system buyers. Body-composition data is becoming a checklist item for weight-management RFPs, and having a body-scanning module in the product narrative could strengthen TytoCare's offering against competing telehealth platforms.",
    P_C, CTA1_A,
    "Product marketing angle: adding body scanning to TytoCare's platform story opens new buyer conversations in weight management and chronic care. It's a software module that complements the hardware kit, and it maps directly to outcomes that health-system buyers care about.",
    CTA2_A)

# b02-2: Kobi Jacobson - CISO, Head of Information Security & BI - TytoCare
add("b02-2", "Kobi", "Jacobson", "CISO, Head of Information Security & BI", "TytoCare",
    "Quick thought",
    "on the security and compliance side of adding body-scanning data to TytoCare's platform. FitXpress is HIPAA-compliant and GDPR-aligned, with encryption in transit and at rest, photo blur on storage, and configurable retention policies. It's designed to slot into regulated health environments.",
    P_D, CTA1_B,
    "From a security perspective: FitXpress processes no personal identifiers, encrypts all data in transit (TLS) and at rest (AWS SSE-S3), auto-blurs stored photos, and supports immediate-delete or 30-day retention policies. Built for the compliance bar health platforms need.",
    CTA2_B)

# b02-3: Naama Warman - Director of Clinical and AI Projects - TytoCare
add("b02-3", "Naama", "Warman", "Director of Clinical and AI Projects", "TytoCare",
    "Noticed your background",
    "in clinical AI projects. Body-scanning data is a structured, high-quality dataset that could feed into TytoCare's clinical AI pipeline. Consistent anthropometric measurements from smartphone scans provide a new data dimension for diagnostic and monitoring algorithms.",
    P_E, CTA1_C,
    "Clinical AI angle: FitXpress produces structured body measurements with 96-97% accuracy and under 1 cm repeatability. For TytoCare's AI projects, this is clean, consistent data that can strengthen clinical algorithms, especially for weight-related and metabolic conditions.",
    CTA2_C)

# b02-4: Ben Gershon - Senior Director, Business Development Team - TytoCare
add("b02-4", "Ben", "Gershon", "Senior Director, Business Development Team", "TytoCare",
    "Came across your work",
    "in business development at TytoCare. Partnerships with health systems increasingly need a broader diagnostic story, and adding body-scanning to the TytoCare bundle could unlock new deal conversations in weight management, bariatrics, and employer wellness.",
    P_A, CTA1_A,
    "BD perspective: body scanning adds a new module to TytoCare's partnership pitch. Health systems evaluating remote exam platforms for chronic care get a more complete package when body-composition data is part of the virtual visit. Could expand the addressable deal scope.",
    CTA2_A)

# b02-5: Avi Attia - VP and Head of Information Systems and Digital Division - Clalit
add("b02-5", "Avi", "Attia", "VP and Head of Information Systems and Digital Division", "Clalit Health Services",
    "Had a thought",
    "about Clalit's digital information systems roadmap. Mobile body scanning is an API-first module that could add clinical depth to Clalit's member-facing digital channels without requiring changes to the core EMR infrastructure.",
    P_B, CTA1_B,
    "For Clalit's digital division: FitXpress integrates via API/SDK into existing member apps and portals. Members scan from their phone, and structured body metrics flow into the care record. Already processing tens of thousands of scans at other health platforms, HIPAA-compliant and audit-ready.",
    CTA2_B)

# b02-6: Shlomi Ambar - CTO and Chief Architect - Maccabi
add("b02-6", "Shlomi", "Ambar", "CTO and Chief Architect", "Maccabi Health care Services",
    "Spotted something",
    "about Maccabi's technology architecture that suggests mobile body scanning could fit naturally. As an API-first module that produces structured JSON outputs, FitXpress is designed to slot into existing health IT stacks without architectural disruption.",
    P_C, CTA1_C,
    "Architecture fit: FitXpress is an API-first service returning structured body metrics (JSON) from two phone photos. Under 45 seconds per scan, 96-97% accuracy, under 1 cm repeatability. Designed for health-system integration with HIPAA compliance and audit-ready data trails.",
    CTA2_C)

# b02-7: Michal Tzuchman - Deputy CEO, Chief Innovation and Research Officer - Maccabi
add("b02-7", "Michal", "Tzuchman", "Deputy CEO, Chief Innovation and Research Officer", "Maccabi Health care Services",
    "Wanted to reach out",
    "about Maccabi's innovation and research priorities. Body scanning technology that works from any smartphone could strengthen Maccabi's research data quality for obesity and metabolic studies while also serving as a member-facing engagement tool.",
    P_D, CTA1_A,
    "Research perspective: FitXpress gives Maccabi's research team consistent, repeatable body-measurement data from members at home. For obesity and metabolic studies, standardized remote anthropometrics reduce site-visit burden and improve longitudinal data quality across cohorts.",
    CTA2_A)

# b02-8: Nir Shahar - Head of Data and Analytics - Clalit
add("b02-8", "Nir", "Shahar", "Head of Data and Analytics", "Clalit Health Services",
    "Quick one",
    "on Clalit's data and analytics pipeline. Body scanning produces structured anthropometric data that could enrich Clalit's population-health analytics. Consistent remote measurements from members add a dimension that self-reported data can't match.",
    P_E, CTA1_B,
    "Data and analytics angle: FitXpress outputs structured body metrics from smartphone scans with 96-97% accuracy. For Clalit's analytics team, this is a clean data stream that can strengthen population-health models for obesity, diabetes, and metabolic conditions.",
    CTA2_B)

# b02-9: Si Yahav - Product Director, Engagement - TytoCare
add("b02-9", "Si", "Yahav", "Product Director, Engagement", "TytoCare",
    "This stood out",
    "when thinking about member engagement in telehealth. The biggest drop-off in virtual weight-management programs happens when patients don't see tangible progress. Adding body scanning to TytoCare's engagement flow gives members visual proof of change between visits.",
    P_A, CTA1_C,
    "Engagement angle: members using body scanning alongside virtual care stay engaged longer because they can see real body change. For TytoCare's product team, adding this visual progress layer to the member experience could reduce drop-off in weight and chronic-care programs.",
    CTA2_C)

# b02-10: Kobi (Jacob) Katz - EVP, CIO, Head of Technology Division - Maccabi
add("b02-10", "Kobi (Jacob)", "Katz", "EVP, CIO, Head of Technology Division", "Maccabi Health care Services",
    "Got me thinking",
    "about Maccabi's enterprise technology strategy and where member-generated health data fits. Body scanning from a smartphone is a lightweight data-collection layer that adds clinical value without heavy infrastructure, aligning with Maccabi's reputation for digital innovation.",
    P_B, CTA1_A,
    "Enterprise tech fit: FitXpress is an API-first module producing structured body metrics. For Maccabi's technology division, it adds a new data dimension to member health records without disrupting existing systems. HIPAA-compliant, with proven scale at 34K+ scans per year.",
    CTA2_A)

# b02-11: tal zazon - Head of GRC - Clalit
add("b02-11", "tal", "zazon", "Head of GRC", "Clalit Health Services",
    "Quick thought",
    "on the governance, risk, and compliance side of adopting mobile body-scanning technology. FitXpress is built with HIPAA compliance, GDPR alignment, encryption at every stage, configurable data retention, and no processing of personal identifiers. It's designed to pass GRC review.",
    P_C, CTA1_B,
    "GRC perspective: FitXpress processes no personal identifiers, encrypts all data in transit (TLS) and at rest (AWS SSE-S3), auto-blurs stored photos, and supports immediate-delete or 30-day retention per client policy. Built for the compliance standards HMOs require.",
    CTA2_B)

# b02-12: Amir Rinder - Head of Engineering and Infrastructure - Meuhedet
add("b02-12", "Amir", "Rinder", "Head of Engineering and Infrastructure", "Meuhedet Health Services - מאוחדת",
    "Noticed your background",
    "in health-system engineering and infrastructure. FitXpress is an API-first service with structured JSON outputs, designed to integrate into existing health IT stacks. It could add body-data capture to Meuhedet's digital infrastructure without architectural disruption.",
    P_D, CTA1_C,
    "Engineering fit: FitXpress returns structured body metrics via API in under 45 seconds per scan. Under 1 cm repeatability, HIPAA-compliant, with SDKs for mobile integration. A lightweight addition to Meuhedet's infrastructure that adds clinical depth to member-facing services.",
    CTA2_C)

# b02-13: Eytan Behiri - System Director of Medical Informatics (CMIO) - Meuhedet
add("b02-13", "Eytan", "Behiri", "System Director of Medical Informatics (CMIO)", "Meuhedet Health Services - מאוחדת",
    "Curious about your take",
    "on how Meuhedet's medical informatics systems handle body-measurement data. Most EMRs capture weight as a single data point, but consistent anthropometrics from remote scans could enrich the clinical record for chronic-disease management.",
    P_E, CTA1_A,
    "Medical informatics angle: FitXpress feeds structured body metrics (80+ measurements plus body composition) into the care record. For Meuhedet's CMIO team, it adds clinical depth to existing informatics workflows without disrupting how clinicians interact with patient data.",
    CTA2_A)

# b02-14: Eyal Saloniki - Senior Director, Loyalty Program - Maccabi
add("b02-14", "Eyal", "Saloniki", "Senior Director, Loyalty Program", "Maccabi Health care Services",
    "Saw your activity",
    "in Maccabi's loyalty program. Wellness rewards tied to objective body-data verification could boost program participation and reduce disputes. Members scanning from their phone get verified progress, and Maccabi gets audit-ready data for reward fulfillment.",
    P_A, CTA1_B,
    "Loyalty program angle: verified body scanning gives Maccabi's rewards program an objective progress-tracking tool. Members earn rewards based on real body-change data, not self-reports, which strengthens program integrity and member trust. Already proven in wellness-rewards use cases.",
    CTA2_B)

# b02-15: Yael Akerman - Director of Product Management - Digital Health - Clalit
add("b02-15", "Yael", "Akerman", "Director of Product Management - Digital Health", "Clalit Health Services",
    "Made me think",
    "about Clalit's digital health product roadmap. Body scanning could be a natural feature addition to Clalit's member app, giving users a self-service tool for tracking body metrics while feeding structured data back to care teams.",
    P_B, CTA1_C,
    "Product management angle: FitXpress is an SDK that integrates into existing member apps. Users scan from their phone, and structured body metrics flow into the care record. It's a member-facing feature that also delivers clinical value, fitting naturally into digital health product roadmaps.",
    CTA2_C)

# b02-16: Avi Husyt - Head of Infrastructure & Cloud Division - Maccabi
add("b02-16", "Avi", "Husyt", "Head of Infrastructure & Cloud Division", "Maccabi Health care Services",
    "Quick note",
    "on the infrastructure side of deploying mobile body scanning at Maccabi's scale. FitXpress runs on AWS with SSE-S3 encryption, TLS in transit, and API-first architecture. It's built to scale in cloud environments without adding on-prem infrastructure burden.",
    P_C, CTA1_A,
    "Infrastructure angle: FitXpress is cloud-native (AWS), API-first, with structured JSON outputs. Under 45 seconds per scan, no on-prem hardware needed. For Maccabi's cloud division, it's a scalable service that adds body-data capture without infrastructure complexity.",
    CTA2_A)

# b02-17: Olivia Rosenfeld - Regional Medical Director - Maccabi
add("b02-17", "Olivia", "Rosenfeld", "Regional Medical Director", "Maccabi Health care Services",
    "This stood out",
    "when considering how regional medical directors evaluate tools that improve clinical consistency across sites. Manual body measurements vary between clinics and staff, and a standardized digital capture tool could tighten the quality of chronic-disease monitoring across Maccabi's regions.",
    P_D, CTA1_B,
    "Clinical consistency angle: FitXpress gives every Maccabi clinic the same body-measurement standard, whether the patient scans at home or in-clinic. 96-97% accuracy against manual benchmarks, under 1 cm repeatability. Reduces variability across regions and staff.",
    CTA2_B)

# b02-18: Bernie Almosni - VP of Engineering - K Health
add("b02-18", "Bernie", "Almosni", "VP of Engineering", "K Health",
    "Noticed your background",
    "in engineering leadership at K Health. FitXpress is an API-first body-scanning module that integrates via SDK into consumer health apps. It returns structured body metrics in under 45 seconds from two phone photos, with HIPAA compliance built in.",
    P_E, CTA1_C,
    "Engineering perspective: FitXpress is an SDK integration that adds body scanning to K Health's app with minimal engineering overhead. Structured JSON outputs, under 45 seconds per scan, HIPAA-compliant. Already live at scale with health platforms processing 34K+ scans per year.",
    CTA2_C)

# b02-19: Yaron D. Barac - Director; Heart and Lung Transplant and Mechanical Circulatory Support Program - Clalit
add("b02-19", "Yaron D.", "Barac", "Director; Heart and Lung Transplant and Mechanical Circulatory Support Program", "Clalit Health Services",
    "Quick thought",
    "on body-composition tracking in transplant programs. Pre- and post-transplant patients need consistent weight and body-composition monitoring, and remote scanning from home could reduce the burden of frequent in-clinic measurements while keeping the care team informed.",
    P_A, CTA1_A,
    "Where FitXpress helps transplant programs: patients can capture consistent body measurements from home between clinic visits. For pre-transplant eligibility and post-transplant recovery monitoring, objective body-composition data adds clinical value without adding visit burden.",
    CTA2_A)

# b02-20: Lilac Mandeles - Board Director - Meuhedet
add("b02-20", "Lilac", "Mandeles", "Board Director: Chair of the Business Development Committee, Member of Insurance and HR Committee", "Meuhedet Health Services - מאוחדת",
    "Wanted to reach out",
    "about Meuhedet's business development and insurance priorities. Body-scanning technology that verifies member health metrics could support both clinical program evaluation and insurance-related use cases where objective data strengthens underwriting or wellness-rewards integrity.",
    P_B, CTA1_B,
    "From a business development and insurance perspective: FitXpress provides verified body metrics that strengthen clinical program reporting and could support insurance-adjacent use cases like wellness verification. HIPAA-compliant, audit-ready data from a smartphone scan.",
    CTA2_B)

# b02-21: Sarit Deshe - CIO - Clalit Mushlam - Clalit
add("b02-21", "Sarit", "Deshe", "CIO - Clalit Mushlam", "Clalit Health Services",
    "Had a thought",
    "about Clalit Mushlam's IT priorities for supplemental health services. Mobile body scanning could add value to Mushlam's member offerings, especially for weight-management and wellness programs where objective progress data strengthens the member experience.",
    P_C, CTA1_C,
    "For Clalit Mushlam's digital services: FitXpress adds body scanning to member-facing apps via SDK integration. Members track real body change from their phone, and structured metrics feed into the care record. A differentiated feature for supplemental health offerings.",
    CTA2_C)

# b02-22: Yossi Zigmon - CMO - Head of Marketing & Digital Division - Meuhedet
add("b02-22", "Yossi", "Zigmon", "CMO - Head of Marketing & Digital Division", "Meuhedet Health Services - מאוחדת",
    "Spotted something",
    "about Meuhedet's digital marketing and member engagement strategy. A member-facing body-scanning tool could be a strong acquisition and retention driver, especially for weight-management and wellness programs where visual progress is a powerful motivator.",
    P_D, CTA1_A,
    "Marketing and digital angle: members who can track real body change from their phone are more likely to enroll and stay in weight-management programs. FitXpress gives Meuhedet a differentiated digital tool that drives engagement and feeds structured data back to clinical teams.",
    CTA2_A)

# b02-23: Dor Gerbi - Head of OD - Meuhedet
add("b02-23", "Dor", "Gerbi", "Head of OD", "Meuhedet Health Services - מאוחדת",
    "Curious about your take",
    "on employee wellness at Meuhedet. HMO staff wellness programs can lead by example, and giving Meuhedet's own employees a body-scanning tool for health tracking could demonstrate the technology's value before a member-wide rollout.",
    P_E, CTA1_B,
    "Internal wellness angle: Meuhedet could pilot FitXpress with its own employees first, demonstrating value before member rollout. Staff get a body-scanning tool for personal health tracking, and Meuhedet collects real usage data to inform a broader deployment decision.",
    CTA2_B)

# b02-24: Dan Levin - Head of Gynecology Fertility and Gestational services - Clalit
add("b02-24", "Dan", "Levin", "Head of Gynecology Fertility and Gestational services Dan -Petach Tikva regional consultant clinic.", "Clalit Health Services",
    "Quick note",
    "on body-composition tracking in women's health and fertility services. Weight and body-composition changes are clinically relevant for fertility treatment and gestational health, and remote scanning from home could give clinicians more frequent data points between visits.",
    P_A, CTA1_C,
    "Where FitXpress helps women's health: patients can track body-composition changes from home during fertility treatment or pregnancy. Clinicians get more frequent data points without additional in-clinic visits, and the data feeds into the patient record for continuity of care.",
    CTA2_C)

# b02-25: Hedva Voliovitch - Board Member - Maccabi
add("b02-25", "Hedva", "Voliovitch", "Board Member", "Maccabi Health care Services",
    "Noticed your background",
    "on Maccabi's board. As Israel's most digitally advanced HMO, adding mobile body scanning to Maccabi's member app could further differentiate the member experience while strengthening chronic-disease program metrics and outcome reporting.",
    P_B, CTA1_A,
    "At Maccabi's digital maturity level, body scanning is a natural next layer: members get a phone-based progress-tracking tool, and Maccabi gets structured, HIPAA-compliant body data for program evaluation. Already live at health platforms processing tens of thousands of scans.",
    CTA2_A)

# b02-26: Guy Rabin - CTO & Head of Digital Transformation - National Pathology Institutes - Clalit
add("b02-26", "Guy", "Rabin", "CTO & Head of Digital Transformation - National Pathology Institutes", "Clalit Health Services",
    "Got me thinking",
    "about digital transformation in pathology and diagnostic services. Body scanning data could complement pathology workflows by adding objective anthropometric context to lab results, especially for metabolic panels and obesity-related diagnostics.",
    P_C, CTA1_B,
    "Digital transformation angle: FitXpress adds body-measurement data to the diagnostic picture. For Clalit's pathology and lab services, having consistent anthropometrics alongside lab results could strengthen clinical interpretation, especially for metabolic and endocrine panels.",
    CTA2_B)

# b02-27: Danny Amir - COO - BetterTogether
add("b02-27", "Danny", "Amir", "COO", "BetterTogether - Losing Weight Together",
    "Caught my eye",
    "how BetterTogether uses social motivation and gamification for weight loss. The engagement loop gets even stronger when members can see and share objective body-composition changes between weigh-ins. Mobile scanning adds a visual proof layer to the group-challenge dynamic.",
    P_D, CTA1_C,
    "Where FitXpress boosts social wellness platforms: members scanning between weigh-ins get objective body-composition data they can share in group challenges. Visual progress proof strengthens the gamification loop and keeps members engaged longer between community check-ins.",
    CTA2_C)


# =========================================================
# GENERATION
# =========================================================

def build_m1(c):
    """Build Message 1."""
    greeting = f"Hi {c['first']},"
    hook = c["m1_hook"]
    obs = c["m1_obs"]
    product = c["m1_product"]
    cta = c["m1_cta"]
    
    msg = f"{greeting}\n\n{hook} - {obs}\n\n{product}\n\n{cta}\nKatya"
    
    # If over 600, trim observation
    if len(msg) > 600:
        # Try shorter product
        msg = f"{greeting}\n\n{hook} - {obs}\n\n{P_E}\n\n{cta}\nKatya"
    if len(msg) > 600:
        # Trim obs to fit
        available = 600 - len(f"{greeting}\n\n{hook} - \n\n{P_E}\n\n{cta}\nKatya")
        obs_short = obs[:available-3].rsplit(" ", 1)[0] + "..."
        msg = f"{greeting}\n\n{hook} - {obs_short}\n\n{P_E}\n\n{cta}\nKatya"
    
    return msg

def build_m2(c):
    """Build Message 2."""
    greeting = f"Hi {c['first']},"
    value = c["m2_value"]
    cta_text = c["m2_cta"]
    
    msg = f"{greeting}\n\n{value}\n\n{cta_text} {KATYA_CAL}\nKatya"
    
    if len(msg) > 550:
        # Try shorter value line
        greeting = f"Hi {c['first']} - quick follow-up."
        msg = f"{greeting}\n\n{value}\n\n{cta_text} {KATYA_CAL}\nKatya"
    if len(msg) > 550:
        # Trim value
        available = 550 - len(f"{greeting}\n\n\n\n{cta_text} {KATYA_CAL}\nKatya")
        value_short = value[:available-3].rsplit(" ", 1)[0] + "..."
        msg = f"{greeting}\n\n{value_short}\n\n{cta_text} {KATYA_CAL}\nKatya"
    
    return msg

def validate(msg):
    """Check for banned content."""
    em_dashes = ["\u2014", "\u2013", "\u2015"]
    for d in em_dashes:
        if d in msg:
            return False, f"Contains em-dash: {repr(d)}"
    
    banned_words = ["leverage", "utilize", "harness", "robust", "seamless", "comprehensive",
                    "cutting-edge", "game-changing", "revolutionary", "delve", "tapestry", "realm"]
    lower = msg.lower()
    for w in banned_words:
        if w in lower:
            return False, f"Banned word: '{w}'"
    
    banned_phrases = ["i admire your mission", "excited about your journey",
                      "it's not just", "not just", "quick, visual, data-backed"]
    for p in banned_phrases:
        if p in lower:
            return False, f"Banned phrase: '{p}'"
    
    return True, ""

def main():
    errors = []
    generated = 0
    
    # Sort by person_id
    sorted_ids = sorted(CONTACTS.keys(), key=lambda x: (x.split("-")[0], int(x.split("-")[1])))
    
    for pid in sorted_ids:
        c = CONTACTS[pid]
        
        msg1 = build_m1(c)
        msg2 = build_m2(c)
        
        # Validate
        ok1, err1 = validate(msg1)
        ok2, err2 = validate(msg2)
        
        m1_len = len(msg1)
        m2_len = len(msg2)
        
        if not ok1:
            errors.append(f"{pid} M1: {err1}")
        if not ok2:
            errors.append(f"{pid} M2: {err2}")
        if m1_len > 600:
            errors.append(f"{pid} M1: {m1_len} chars (max 600)")
        if m2_len > 550:
            errors.append(f"{pid} M2: {m2_len} chars (max 550)")
        
        # Write file
        content = f"# {c['first']} {c['last']} — {c['title']} — {c['company']}\n\n## Message 1 (after connection accepted)\n{msg1}\n\n## Message 2 (+5 days, no reply to Message 1)\n{msg2}\n"
        
        filepath = os.path.join(OUT_DIR, f"{pid}.md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
        generated += 1
        
        status = "OK" if (ok1 and ok2 and m1_len <= 600 and m2_len <= 550) else "WARN"
        print(f"  {status} {pid}: {c['first']} @ {c['company'][:40]} [M1:{m1_len}c M2:{m2_len}c]")
    
    print(f"\n--- SUMMARY ---")
    print(f"Files generated: {generated}")
    print(f"Errors: {len(errors)}")
    for e in errors:
        print(f"  - {e}")

if __name__ == "__main__":
    main()
