---
product: fitxpress
profile: katerina
campaign: 2026-10-22-uk-insurance-underwriting
created: 2026-10-23
stage: validate
status: awaiting_review
---

# ICP Validation Summary — 2026-10-22-uk-insurance-underwriting

Validated in five `icp-validator` batches: Aviva 449 · Legal & General 298 · other Sales Nav companies 259 · Apollo gap top-up 135 (the 11 companies Sales Nav left empty) · Apollo title top-up 142 (the 12 Sales Nav companies, by hypothesis titles). The coordinator merged the decision files into `decisions.md` and ran `apply-decisions` and `skipped`. Batch sections below are the validators' own tables (the title top-up section is built from its decisions file: that validator's session ended before its report).

## Stats

1,283 people (Sales Navigator 1,006 + Apollo 277, 23 of 23 companies; Vadim approved 135 + 144 Apollo credits) · **PASS 148** (P1 32 · P2 64 · P3 52) · **WEAK 130** · FAIL 1005 · excluded by registry 0 · cap 50 per group, largest group 20 PASS.

PASS by angle: underwriting 46 · reinsurance 35 · proposition 23 · referral 18 · technical-integration 15 · partnership 8 · medical 3

| Group | PASS | WEAK | FAIL |
|---|---|---|---|
| Aviva | 20 | 24 | 453 |
| Royal London | 15 | 15 | 109 |
| Legal & General | 14 | 24 | 287 |
| Pacific Life Re | 11 | 10 | 25 |
| Swiss Re UK | 10 | 1 | 4 |
| Zurich UK | 8 | 15 | 23 |
| VitalityLife | 8 | 14 | 8 |
| Scottish Widows | 8 | 3 | 13 |
| UnderwriteMe | 7 | 7 | 0 |
| Munich Re UK Life Branch | 6 | 3 | 4 |
| RGA UK | 6 | 0 | 1 |
| LV= | 5 | 4 | 44 |
| SCOR UK | 5 | 1 | 3 |
| Guardian Financial Services | 5 | 0 | 0 |
| The Exeter | 4 | 1 | 10 |
| Shepherds Friendly | 4 | 2 | 7 |
| Cirencester Friendly Society | 4 | 0 | 4 |
| iPipeline UK | 3 | 0 | 0 |
| Hannover Re UK Life Branch | 2 | 2 | 0 |
| Holloway Friendly | 1 | 1 | 6 |
| British Friendly | 1 | 2 | 3 |
| Gen Re UK | 1 | 0 | 1 |
| Iress UK | 0 | 1 | 0 |

## Main finding: the Sales Navigator export was pulled by company, not by title

All three Sales Nav validators found it independently: the export is every senior person at each company (speechwriting, events, catering, PAs), and the underwriting owners the persona is built on were missing at all 12 companies. Of 1,006 Sales Nav people 45 PASS. The two Apollo pulls by the hypothesis titles gave 54 of 135 and 49 of 142, and brought in the underwriting and medical lanes: Royal London Chief Underwriter, L&G Underwriting & Claims Director and CMO, Aviva Head of Underwriting Strategy & Governance, heads of underwriting at British Friendly and Shepherds Friendly, the reinsurers' CUOs and CMOs.

## Data issues

- `compact` bug: `earlier_roles` split Experience on `, `, so a comma inside the current title leaked as a fake earlier role. **Fixed 2026-10-23, commit 40002e5** (`split_roles`, also used by `empty-profile` and the messages profiles card). The title top-up batch was compacted after the fix; earlier batches decided on the full title, so their decisions stand.
- Same person under two LinkedIn slugs: Fiona Wynn (Apollo) = Fi Wynn (Sales Nav), suffix `72936a4`; the Apollo row is FAIL as a duplicate. `extract-people` dedupes on the full URL only.
- Duplicates inside the export: Fiona Beale, Neil Southam (Aviva); Lee Taylor, Christina Nicolaou, Paul Lewis (L&G); Robin Crouch, Gavin Drescher, Lorraine Donald. Extra copies FAIL.
- Identity collisions: Valerie Edward ("LV Limited" joins the `lv` key), 丹丹 欧阳 (Chinese fintech), Nichola H (artist, Apollo), Alwyn Roberts (Wynn Resorts, Apollo). All FAIL. Apollo rows carry no `other-company-page` flag.
- Mixed company pages: LV= includes LV= GI (Allianz); Aviva includes Direct Line; VitalityLife includes VitalityHealth; Munich Re includes Great Lakes (P&C); Gen Re includes Faraday (P&C).
- Royal London × LV=: a validator recalled a 2025 deal. Two web searches found only 2021-22 (Bain vote failed, Royal London talks ended); no completed deal, so the acquisition rule does not apply.
- UnderwriteMe ↔ Pacific Life Re are linked (Andrew Doran ex PLRe Global Chief Underwriter): keep the partnership and reinsurance messages consistent.
- CMO titles to eyeball: Deborah Smith (Swiss Re, P1) thin history; Harpreet Sarna (Vitality, WEAK) no medical history.

## Batch: Apollo title top-up for the Sales Nav companies (142)

**Counts:** PASS 49 (P1 10 · P2 30 · P3 9) · WEAK 30 · FAIL 63 (Fiona Wynn = Fi Wynn from Sales Nav, renamed slug → FAIL as duplicate) · registry 0.

#### Proposed to SEND (title top-up)
| Group | Person | Title | P | Angle |
|---|---|---|---|---|
| Aviva | James Whitty | Head of Underwriting Strategy & Governance | 1 | underwriting |
| Aviva | Nick Austin | Protection Commercial Director | 1 | proposition |
| Aviva | Michelle Cross | Underwriting Philosophy Manager | 2 | underwriting |
| Aviva | Tom Parkinson | Underwriting Rules Developer | 2 | underwriting |
| Aviva | Daryl Warren | Head of Individual Protection Pricing | 2 | proposition |
| Aviva | Sally James | Senior Development Underwriter | 2 | underwriting |
| Aviva | Paul Welsh | Group Head of Innovation | 3 | referral |
| Aviva | Harriet Granville-Jones | Partnerships Manager - Group Innovation | 3 | referral |
| British Friendly | Alex Yates | Head of Underwriting | 1 | underwriting |
| Cirencester Friendly Society | Steve Betteridge | Senior Development Underwriter | 2 | underwriting |
| Cirencester Friendly Society | Samuel Njoroge | Underwriting Analytics & Development Manager | 2 | underwriting |
| Cirencester Friendly Society | Sue Kissane | Underwriting Manager | 3 | underwriting |
| Holloway Friendly | Jamie Welch | Underwriting and Claims Technical Manager | 3 | underwriting |
| LV= | Lucy Luscombe | Head of Protection Pricing at LV= | 2 | proposition |
| LV= | Gareth Hurst | Development Underwriter | 2 | underwriting |
| LV= | Rachel Haig | Development Underwriter | 2 | underwriting |
| Legal & General | David Banks | Underwriting & Claims Director | 1 | underwriting |
| Legal & General | Tarun Gupta | Chief Medical Officer | 1 | medical |
| Legal & General | Pippa Barber | Commercial Director, Retail Protection | 1 | proposition |
| Legal & General | Sara Denyer | Underwriting Rules User Business Analyst | 2 | underwriting |
| Legal & General | John Redmond | Claims & Underwriting Development Team Manager | 2 | underwriting |
| Legal & General | Hai Luc | Head of Actuarial Research, Retail Protection | 2 | proposition |
| Legal & General | Andrew Greatbanks | Customer Underwriting Service Delivery Manager | 3 | underwriting |
| Pacific Life Re | David Waters | Underwriting Director | 1 | reinsurance |
| Pacific Life Re | Febby Mulewa | Head of Underwriting and Claims, Protection, Europe | 1 | reinsurance |
| Pacific Life Re | Killian Farrelly | Director, Protection Pricing | 2 | reinsurance |
| Pacific Life Re | Nikolai Harrowing | Development Underwriter | 2 | reinsurance |
| Pacific Life Re | Caroline Smith | Underwriting and Claims Developer | 2 | reinsurance |
| Pacific Life Re | Justin Farrow | Manager, Underwriting | 3 | reinsurance |
| Royal London | Craig Paterson | Chief Underwriter | 1 | underwriting |
| Royal London | Ceri Davies | Underwriting Rules and Philosophy Developer | 2 | underwriting |
| Royal London | Dominic Pagan | Underwriting Philosophy Manager | 2 | underwriting |
| Royal London | William Stratton | Underwriting Rules Developer | 2 | underwriting |
| Royal London | Damian Mapplebeck | Underwriting Rules Developer | 2 | underwriting |

| Royal London | Caitlin Stronach | Head of Protection Commercials and Business Quality | 2 | proposition |
| Royal London | Robin Goodwin | Underwriting Analytics Manager | 2 | underwriting |
| Royal London | James Blaney | Underwriting & Claims Quality Assurance Manager | 3 | underwriting |
| Scottish Widows | Simon Vooght | Protection Proposition Manager | 2 | proposition |
| Scottish Widows | Daniel Musty | Underwriting Development Manager | 2 | underwriting |
| Scottish Widows | Eric Walker | Development Underwriting Manager | 2 | underwriting |
| Scottish Widows | Kerrie Cross | Protection Underwriting Development Manager | 2 | underwriting |
| Scottish Widows | David Russell | Senior Manager Claims & Underwriting Strategy | 2 | underwriting |
| Scottish Widows | Scott Innes | Senior Technical Underwriting Manager | 3 | underwriting |
| Shepherds Friendly | Michael Jackson | Head of Underwriting | 1 | underwriting |
| The Exeter | David Piggin | Underwriting Rules Developer | 2 | underwriting |
| The Exeter | Ed Lyon | Head of Underwriting Operations | 2 | underwriting |
| UnderwriteMe | Helen Sutherland-Thomas | Lead Development Underwriter | 2 | partnership |
| UnderwriteMe | James Hetherington | Manager, Development Underwriting | 2 | partnership |
| UnderwriteMe | Will Miller | VP, Head of Legal and Risk and DPO | 3 | technical-integration |

#### WEAK (title top-up)
| Person | Title | Group | Why borderline |
|---|---|---|---|
| Stuart McKellar | Data Protection Officer | Aviva | DPO title at multi-line Aviva with a paralegal background: likely a member of the data protection team, not the protection DPO, and the line is not shown. |
| Robert Morrison | Chief Underwriting Officer | Aviva | Chief Underwriting Officer title would be P1 if protection, but the profile is empty, the line is not shown, and the other Aviva CUO titles in this batch are GI (Michael Korner, Jason Chambers' former SME role). |
| Dan Tinson | Head of Protection Reinsurance | Aviva | Head of Protection Reinsurance owns the treaties whose reinsurers sign off evidence changes, but reinsurance management is not a tier in the card. |
| Suzanne Lawson | Partnerships Manager - Group Innovation | Aviva | Second Partnerships Manager in Group Innovation, next to Harriet Granville-Jones and Paul Welsh (both PASS), with a corporate affairs and UK Life business management background: add only if Vadim wants depth in that team. |
| Adrian Nye | Health & Protection Procurement and Outsourcing Director | Aviva | Health and Protection procurement and outsourcing director who would hold the evidence-supplier contracts, but procurement is outside the card's functions and his headline places him at Aviva Health (PMI). |
| Debbie Elms | Head of Underwriting & Claims | British Friendly | Head of Underwriting and Claims, but Alex Yates also holds Head of Underwriting at British Friendly and her career is claims-led, so one title is probably stale. |
| Scott Greenhill | Head of Underwriting | LV= | Head of Underwriting would be P1, but the profile is empty and the LV= name also covers the GI business now owned by Allianz, so the line is not shown. |
| Adam Davison | Head of Distribution Quality - Protection | LV= | Head of Distribution Quality for Protection owns the quality of adviser-submitted business, which touches disclosure, but the role is adviser-facing and outside the card's tiers. |
| Matthew Wilton | Underwriting Development | Legal & General | London underwriting development role with a life-assurance contract background, but L&G's London underwriting development head (Paul Murchan) runs Retail Retirement, so this may be annuities. |
| Richard Whaley | Development Underwriter | Legal & General | Cardiff development underwriter, likely in John Redmond's development team (PASS), with an enhanced-annuity past: the line is not certain and the team is already covered. |
| Jenni Phillips | Development Underwriter | Legal & General | Cardiff development underwriter, likely in John Redmond's development team (PASS): add only if Vadim wants a second voice from that team. |
| Ann Nuttall | Underwriting Development Specialist | Legal & General | Underwriting Development Specialist with an empty profile at multi-line L&G: P2 if protection, but neither the line nor the person can be confirmed. |
| Malcolm Cooper | Director, Pricing and Underwriting | Legal & General | Director, Pricing and Underwriting would be P1, but his headline reads "Old, happy - not looking for work" and the same title is also listed as a past role, so he may have retired. |
| Donna Cowell | Head of Reinsurance, Protection | Legal & General | Head of Reinsurance for Protection and former Head of Pricing at Swiss Re iptiQ EMEA: close to pricing and to the reinsurers who approve evidence changes, but reinsurance management is not a tier in the card. |
| Justin Choi | Group Head, Digital Channels & Innovation | Legal & General | Group Head of Digital Channels and Innovation fits the card's group-wide innovation lead (P3 referral), but his profile reads as brand, content and channels. |
| Alan Dott | Director of Underwriting | Pacific Life Re | Director of Underwriting would be P1, but the profile is empty and Pacific Life Re already has two underwriting leads PASS in this batch. |
| Warren Copp | Chief Underwriter | Pacific Life Re | Chief Underwriter would be P1, but the profile is empty, so the person and the current role cannot be confirmed. |
| Paul Reddick | Head of Medical Underwriting & Claims | Pacific Life Re | Head of Medical Underwriting and Claims would be P1 or P2, but the profile is empty and cannot be confirmed. |
| Daragh Brady | Head of Risk, Global Protection & Capital Solutions | Pacific Life Re | Head of Risk for Global Protection and Capital Solutions: the card gives everyone at a reinsurer the reinsurance lane, but it names the CRO line as not the buyer. |
| James Sims | Underwriting Developer | Pacific Life Re | Underwriting Developer, the third developer at Pacific Life Re in this batch: add only for depth. |
| Robert Arbuckle | Underwriting Rules Developer | Royal London | Underwriting Rules Developer (ex-Bright Grey, Scottish Provident), a fifth rules or philosophy person at Royal London in this batch: add only if Vadim wants depth in one team. |
| Daniel Smith | Underwriting Philosophy Developer | Royal London | Underwriting Philosophy Developer, but his headline still says Development Underwriter at Aviva, so the current employer needs a check, and Royal London's rules team is already covered. |
| Jane Lyle | Development Underwriter | Royal London | Development Underwriter (ex-Scottish Widows, L&G) in a Royal London rules and development team already covered by four PASS: add only for depth. |
| Robert Morrison | Head of Underwriting and Claims | Royal London | Head of Underwriting and Claims would be P1, but the profile is empty and the same name has an empty Aviva CUO record in this batch, so identity needs a check. |
| Seb Bowden | Rules & Development Underwriter | Royal London | Rules and Development Underwriter, ex-L&G development underwriter and medical underwriting trainer, in a Royal London rules team already covered by four PASS: add only for depth. |
| Paul Young | Development Underwriter | Scottish Widows | Development Underwriter in a Scottish Widows development team already covered by three PASS managers: add only for depth. |
| Tom Green | Development Underwriter | Scottish Widows | Development Underwriter and former medical underwriting manager in a Scottish Widows development team already covered by three PASS managers: add only for depth. |
| Frances Heggie | Senior Underwriting Strategy Manager | Scottish Widows | Senior Underwriting Strategy Manager would be P2, but the profile is empty and David Russell (PASS) already covers underwriting strategy. |
| Val Brookes | Claims and Underwriting Manager | Shepherds Friendly | Claims and Underwriting Manager with an empty profile and a claims-first title, at a society whose head of underwriting is already PASS. |
| Pete Martin | Lead Development Underwriter (NA and UK&I) | UnderwriteMe | Lead Development Underwriter for North America and UK&I, the third development underwriting lead at UnderwriteMe in this batch: add only for depth. |

#### FAIL (title top-up), by the validator's reason

retired per headline 3 · gi business development underwriter 2 · underwriting ops team manager 2 · gi underwriting innovation, ex-nig commercial 1 · gi property technical underwriting 1 · gi head of underwriting, ex-azur 1 · intranet digital workplace, no line 1 · gi commercial development underwriter 1 · gi development underwriter, perth 1 · gi development underwriter, ex-mga 1 · gi sme underwriting transformation 1 · associate-level digital transformation 1 · gi underwriting effectiveness, ex-norwich union insurance 1 · gi construction trading underwriter 1 · gi head of product 1 · cio operational risk director 1 · innovation manager, no line shown 1 · gi technical underwriting team 1 · gi international commercial underwriting 1 · gi accident and health 1 · actuarial innovation manager, no line 1 · pricing technician, below head 1 · gi technical underwriting, ex-exposure management 1 · risk business partnering (cro line) 1 · gi underwriting effectiveness, empty profile 1 · gi underwriting governance 1 · gi underwriting analytics, perth 1 · protection distribution, adviser-facing 1 · protection governance and assurance 1 · protection distribution director 1 · automation manager, no line, empty 1 · gi underwriting quality, empty profile 1 · gi partnership operations secondment 1 · gi retail cuo, motor background 1 · gi chief underwriting office quality 1 · retail retirement underwriting development 1 · data engineer below cto 1 · m365 it specialist 1 · customer underwriting team manager 1 · product governance, pensions background 1 · product and commercial risk 1 · data science manager, not cto 1 · ops team manager, empty profile 1 · adviser-facing distribution manager 1 · team manager, empty profile 1 · medical underwriting team manager 1 · pricing actuary below head, empty 1 · automation manager, no line shown 1 · customer service director, pensions-led 1 · equity release, out of line 1 · gi pet and travel 1 · protection marketing head 1 · protection sales director 1 · individual initial underwriter 1 · on a career break 1 · underwriting team manager 1 · left holloway per headline 1 · claims-led team manager 1

## Batch: Apollo gap top-up (135)

**Counts:** PASS 54 (P1 13 · P2 24 · P3 17) · WEAK 37 · FAIL 44 · registry 0.

| Group | n | P1 | P2 | P3 | WEAK | FAIL |
|---|---|---|---|---|---|---|
| Zurich UK | 46 | 1 | 3 | 4 | 15 | 23 |
| VitalityLife | 30 | 0 | 5 | 3 | 14 | 8 |
| Swiss Re UK | 15 | 3 | 5 | 2 | 1 | 4 |
| Munich Re UK Life Branch | 13 | 3 | 2 | 1 | 3 | 4 |
| SCOR UK | 9 | 1 | 3 | 1 | 1 | 3 |
| RGA UK | 7 | 2 | 3 | 1 | 0 | 1 |
| Guardian Financial Services | 5 | 1 | 3 | 1 | 0 | 0 |
| Hannover Re UK Life Branch | 4 | 1 | 0 | 1 | 2 | 0 |
| iPipeline UK | 3 | 0 | 0 | 3 | 0 | 0 |
| Gen Re UK | 2 | 1 | 0 | 0 | 0 | 1 |
| Iress UK | 1 | 0 | 0 | 0 | 1 | 0 |

**P1 sample:** Sabrina Lane (Zurich Chief Underwriter), Nick Rice (Guardian Head of UW & Claims), Natalie Kelly / Claire Nolan / Deborah Smith CMO (Swiss Re), Madhu Sridharan CUO / Matt Bone / Adrian Stevenson (Munich Re), Tim Smith (Hannover Re), Lynn Baillie (Gen Re CUO), Mike Evans / Anna Graham (RGA), Helen Croft (SCOR).

**Validator's questions:** (1) 6 Vitality heads of product, line not shown: all P3 or none? (2) 2 Vitality Directors of Pricing and Underwriting (Marszalek, Yarham): both P1? (3) Zurich Underwriting Managers with empty profiles (Penny, Paxford): drop?

**Data:** identity collisions missed by flags (Apollo rows have no other-company-page): Nichola H (artist), Alwyn Roberts (Wynn Resorts) → FAIL. VitalityLife page mixes VitalityHealth. Munich Re includes Great Lakes (P&C), Gen Re includes Faraday (P&C). Zurich: both CUOs are GI; protection lead titled Chief Underwriter. CMO checks: Deborah Smith (Swiss Re, P1) thin history; Harpreet Sarna (Vitality, WEAK) no medical history.

Pools: GI/P&C leaders 8 (none) · reinsurer L&H seniors outside UW 5 (referral, needs claims=yes) · Vitality product marketing 2 · Vitality adviser-facing 2 · Vitality claims/health 3 · Zurich retirement 1 · GI ICs 15 · left/collisions 4 · junior 4.

## Batch: Royal London, LV=, Pacific Life Re, Scottish Widows, The Exeter, mutuals, UnderwriteMe (259)

**Counts:** PASS 26 (P1 7 · P2 7 · P3 12) · WEAK 27 · FAIL 206 · registry 0. No group near the cap.

| Group | n | P1 | P2 | P3 | PASS | WEAK | FAIL |
|---|---|---|---|---|---|---|---|
| Royal London | 121 | 1 | 1 | 5 | 7 | 10 | 104 |
| LV= | 44 | 0 | 1 | 1 | 2 | 2 | 40 |
| Pacific Life Re | 35 | 1 | 3 | 1 | 5 | 5 | 25 |
| Scottish Widows | 14 | 2 | 0 | 0 | 2 | 0 | 12 |
| The Exeter | 11 | 1 | 1 | 0 | 2 | 1 | 8 |
| Shepherds Friendly | 11 | 0 | 1 | 2 | 3 | 1 | 7 |
| UnderwriteMe | 10 | 2 | 0 | 2 | 4 | 6 | 0 |
| Cirencester | 5 | 0 | 0 | 1 | 1 | 0 | 4 |
| Holloway | 4 | 0 | 0 | 0 | 0 | 1 | 3 |
| British Friendly | 4 | 0 | 0 | 0 | 0 | 1 | 3 |

**Data note:** no underwriting title anywhere in the slice (not even Royal London's chief underwriter, whom the persona cites): the underwriting and medical lanes are empty. LV= rows include LV= GI staff (Allianz since 2019) → FAIL. Duplicates: robin-crouch, gavin-drescher, lorraine-donald. Retired: jon-glen, graham-nichol. valerie-edward = identity collision, FAIL. UnderwriteMe ↔ Pacific Life Re linked (Andrew Doran ex PLRe Global Chief Underwriter). To check: Royal London's 2025 deal for LV= (recent-acquisition rule?).

#### Proposed to SEND (rest)
| Group | Person | Title | P | Angle |
|---|---|---|---|---|
| Royal London | Carrie Johnson | Customer Lifestage Director - Protection and Build & Grow (Protection P&L) | 1 | proposition |
| Royal London | Fi Wynn | Head of Protection Propositions | 2 | proposition |
| Royal London | James Sandell | UK CIO / CTO | 3 | technical-integration |
| Royal London | Lee Ellis | Group Chief Digital Officer | 3 | referral |
| Royal London | Amy Higgs | Head of Strategic Transformation | 3 | referral |
| Royal London | Joshua Goodwin | Head of Transformation and Innovation | 3 | referral |
| Royal London | Myrto (Myrsini) A. | Head of Strategy & Innovation | 3 | referral |
| LV= | Gary Beyer | Protection Proposition Director | 2 | proposition |
| LV= | Karl Pickering | CTO | 3 | technical-integration |
| Pacific Life Re | Mala Thurston | Head of Protection, Europe | 1 | reinsurance |
| Pacific Life Re | Sandi Sohal | AVP, Basis Development, R&D | 2 | reinsurance |
| Pacific Life Re | Réka Halász | AVP, Basis Development, R&D | 2 | reinsurance |
| Pacific Life Re | Martin Boniface-Jones | AVP, R&D | 2 | reinsurance |
| Pacific Life Re | Caroline Burton | DPO - AVP | 3 | technical-integration |
| Scottish Widows | Kate Lyons | Protection Director | 1 | proposition |
| Scottish Widows | Laura Vaughan | Head of Protection (thin profile) | 1 | proposition |
| The Exeter | Toby Bainbridge | Head of Insurance Solutions (ex Director of Protection, LV=) | 1 | proposition |
| The Exeter | Jack Southcott | Head of Proposition (Protection) | 2 | proposition |
| Shepherds Friendly | Steve Smith | Head of Product (ex Head of Underwriting, CPD) | 2 | proposition |
| Shepherds Friendly | Michael Williams | Chief Change Officer | 3 | referral |
| Shepherds Friendly | Elizabeth Cook | Head of Business Innovations | 3 | referral |
| UnderwriteMe | Andrew Doran | CEO | 1 | partnership |
| UnderwriteMe | Kylie Irwin | CPO | 1 | partnership |
| UnderwriteMe | Sai Tejo Kiran | Director of Product Management | 3 | partnership |
| UnderwriteMe | Riccardo Rossi | Product Manager Director | 3 | partnership |
| Cirencester | John Underwood | Director of Technology | 3 | technical-integration |

#### WEAK (rest)
| Person | Title | Group | Why borderline |
|---|---|---|---|
| Jonathan Letham | Head of Proposition | Royal London | No line; earlier roles wealth |
| Daniel T. | Head of Proposition | Royal London | No line named |
| Sophie Hadfield | Head of Proposition | Royal London | No line; Deloitte audit background |
| Maureen Duckworth | Head of Product Management | Royal London | Multi-line, no profile |
| Sarah Farquharson | Head of Transformation and Performance | Royal London | Ops-efficiency background |
| Finlay Boyd | Head of Commercial Insight / Planning / E2E Transformation | Royal London | Reads as commercial planning |
| Ritwik Samsi | Group Corporate Development Director | Royal London | Owns no evidence; insurtech boards |
| Vicki Wharton | Group Customer Operations Director | Royal London | New-business processing may report to her |
| Kevin Milne | Case Management Consultant, New Business - Protection | Royal London | IC in protection new business; referral |
| Jones (Birmingham) | Head of Customer Experience (New Business) | Royal London | No first name |
| Martyn Luke | Head of Protection Change | LV= | Delivers, does not decide |
| Jonathan Manning | Head of Change (S&R) | LV= | Headline adds Protection; delivers |
| Charles King | Head of Digital Process | Pacific Life Re | Scope unclear |
| Richard Purcell | Client Solutions Director | Pacific Life Re | Underwriting solutions or capital/longevity? |
| Matthew Barclay | Director, Client Solutions | Pacific Life Re | Same question |
| Oliver Gingell | VP, Head of Client Solutions UK | Pacific Life Re | Same; longevity background |
| Ben Acheson-Gray | AVP, Technical Services, Europe & NA | Pacific Life Re | May be client underwriting support |
| Ali Law | CIO | The Exeter | Card excludes CIOs, but top technologist, no CTO |
| Darren Wing | Head of IT and Change | Holloway | Top technologist at a small IP mutual |
| Nic Herbert | Head of Technology & Change | British Friendly | Top technologist at a small IP mutual |
| Daniel Simpson | Chief Commercial Officer | Shepherds Friendly | Product/proposition/pricing background |
| Simon Coutts, Will Hutchinson, Sergey Kobzar, Alan Pich | Directors of Engineering | UnderwriteMe | Four, no CTO in the pull; pick one |
| Kristian Samuel-Camps | Director of Product Operations | UnderwriteMe | Runs product ops |
| Paul Mburu | Head of Strategy | UnderwriteMe | May own partnerships |

#### Pools left out (rest, seniors first)
| Pool | People | Who | Angle | What would have to change |
|---|---|---|---|---|
| A1. Executives at single-line protection mutuals | 7 | Ben Pears (CEO Holloway), Ann-Marie O'Dea (CEO Shepherds Group), Jonathan Sandell (CEO Shepherds Friendly), Suzy Esson (COO The Exeter), Ben Howe (COO Cirencester) … | referral | add CEO/COO at a single-line protection mutual as P3 referral — **recommended**: no underwriting owner returned there |
| A2. Executives at multi-line groups | 7 | Barry O'Dwyer, Peter Josse, Jo Kite, Bernie Hickman (RL); Anita Fernqvist, Richard Rowney (LV=) | referral | card says group CEO is not the buyer — not recommended |
| C. CIOs and heads of architecture | 11 | Ian Andrews (LV=); Lisa Bullock, Stuart R., Michael Hunter, Charul Scott (RL) … | technical-integration | lift the CIO rule or give architecture a tier |
| B. Protection distribution heads | 4 | Jon Fuller (RL), Catherine Trimble (SW), Jamie Page (Exeter), Alan Waddington (Cirencester) | proposition | exempt protection-named distribution heads |
| D. Data and AI | 20 | Chris Miller (Group Chief Data & AI Officer, RL), Lee Wilson (RL), Ian McNamara (PLRe), Annabel Banks (LV=), Russell Johnston (RL) … | technical-integration | group data/AI chiefs as P3 — Miller and Wilson only |
| E. Strategy / corporate development | 7 | Etienne B. (RL), Chris Walker (LV=), Hannah Rothery (PLRe), Minoka Radhakrishnan, Julie Clapperton (RL) … | referral | strategy heads as referral |
| F. Pacific Life Re ops / client services / actuarial | 7 | Myles Rix (SVP Global Head of Ops), Travis Short, Savita Rai, Akta Savla, Mark Howlett … | reinsurance | read "reinsurance lane = everyone at group B" literally |
| H. Operations and customer | 13 | Ian Wheat (RL), Claire Hird (Exeter), Lorraine Donald (BF), Valerie Rogerson, Gail Manchester … | referral | new-business ops owners, small mutuals only |
| G. Change / PMO / delivery | 17 | Hilary Jones, Caroline Edgar, Wayne Morris (RL); Kevin Buckland (LV=); Simon Trowbridge (Exeter) … | referral | not recommended |
| I. Claims | 2 | Ian Rowe (PLRe), Maxine Jannetta (BF) | none | open question 4 keeps claims out |

Not offered (111): out of line 26, general distribution/BD 17, IT below CIO/CTO 23, support 35, legacy/unclear 4, duplicates/retired/collision 6.

## Batch: Aviva (449)

**Counts:** PASS 12 (P1 2 · P2 2 · P3 8) · WEAK 19 · FAIL 418 · registry 0 · cap 50 not reached.
FAIL by reason (validator's tally): GI 104 · group support 95 · tech/data/AI 82 · transformation/change 40 · governance/audit/regulatory 29 · wealth/pensions 27 · empty/junk/left/duplicate 24 · claims 9 · Aviva Health 8.

**Data note:** company-wide pull, not by title (card: "never by company alone"). Of the P1 roles only Sue Hendry and Victoria Francis are present; no CUO, Chief Underwriter, CMO, development/philosophy underwriter, MD Protection, Head of New Business. Duplicates: Fiona Beale ×2, Neil Southam ×2. Junk/collisions: 丹丹-欧阳 (Chinese fintech), ma-ma (Landlord), darran-r (investigator), two retired, rob-fisher (other-company-page). Direct Line staff now under Aviva (GI, FAIL).

#### Proposed to SEND (Aviva)
| Group | Person | Title | P | Angle |
|---|---|---|---|---|
| Aviva | Sue Hendry | Head of Protection UW/Claims and Customer Services | 1 | underwriting |
| Aviva | Victoria Francis | Protection Propositions Director | 1 | proposition |
| Aviva | Lili Burdass | Head of Transformation, Protection | 2 | proposition |
| Aviva | Rachel Hannon | Chief Transformation Officer, UK Life (IWR) | 2 | proposition |
| Aviva | Jon O'Neal | Head of IT, Aviva Protection UK | 3 | technical-integration |
| Aviva | Steve Lister | Head of Architecture, Insurance, Wealth & Retirement | 3 | technical-integration |
| Aviva | Arslan Hannani | Chief Innovation Officer (group) | 3 | referral |
| Aviva | Marina Belezina | Group Director Strategy & Innovation | 3 | referral |
| Aviva | Hannah Spiro | Head of Innovation Engagement | 3 | referral |
| Aviva | Joel Manstoff | Group Head of Transformation | 3 | referral |
| Aviva | Aman Hayer | Group Transformation Director | 3 | referral |
| Aviva | Manju Devi | Head of Digital Portfolio, Group Strategy & Transformation | 3 | referral |

#### WEAK (Aviva)
| Person | Title | Group | Why borderline (angle) |
|---|---|---|---|
| Martin Felice | Head of Underwriting Governance | Aviva | Empty profile; GI or protection unknown (underwriting) |
| Gary Williams | Director of Product and Underwriting | Aviva | Buyer title, line not shown; GMAC motor background (underwriting) |
| Katriona Cunningham | Head of Underwriting Counter Fraud | Aviva | Owns application misrepresentation, but persona excludes fin-crime; Perth suggests GI (underwriting) |
| Dan Turner | Head of Change | Aviva | Ex Head of Change at AIG Life (now Aviva protection) (proposition) |
| Clare Mallion | Head of Transformation (headline: Head of Pricing) | Aviva | Protection pricing would be P2; line not shown (proposition) |
| Brian Spinks | Head of New Business Development, Propositions & Insights | Aviva | Reads as BD; line not shown (proposition) |
| Ashley Murray | Head of Retail Propositions & Change | Aviva | Retail includes direct protection and savings (proposition) |
| Louise M. | Head of Propositions | Aviva | Line not shown (proposition) |
| Mike Jackson | Head of Product | Aviva | Bare title, no detail (proposition) |
| Maria C. | Head of Digital Product | Aviva | Prior role commercial GI (proposition) |
| Jen Hobbs | Head of Digital Product (Interim) | Aviva | Line not shown (proposition) |
| Michael Sasaki | IT Director IWR | Aviva | Ex CIO AIG Life; card says CIO-level does not own evidence (technical-integration) |
| Juan Gómez-Reino Garrido | CIO IWR and Group Deputy CIO | Aviva | Same CIO rule (technical-integration) |
| Ashley Bevan | Head of Life and Group Data Platform | Aviva | Life-scoped data platform (technical-integration) |
| David Montgomery | COO, Insurance, Wealth & Retirement | Aviva | Runs protection ops among others; no COO lane (referral) |
| Amanda Weston | Head of Partnerships | Aviva | Ex AIG Life partnerships; distribution (referral) |
| Matt Rushbrooke | Customer Expert, Protection Operations | Aviva | Individual contributor in protection (referral) |
| James Appleton | Head of Innovation Delivery | Aviva | Probably group innovation (referral) |
| Ashley Stevens | Global Head of Transformation | Aviva | "Global" at Aviva often = GCS (GI) (referral) |

#### Pools left out (Aviva, seniors first)
| Pool | People | Who | Angle | What would have to change |
|---|---|---|---|---|
| Group executives and group technology | 9 | Amanda Blanc (Group CEO), Craig Fazzini-Jones (Group COO), John Cummings (Group CIO), Ajit Dhaliwal, Paul Shaw (Group CISO), Chris Cochrane, Martin Lamb, Andy Piper, Anna King | referral · technical-integration | allow group C-suite referral and group CIO/CISO |
| Life and protection support functions | 8 | Steve Bridger (Chief Claims Officer, ex-MD Group Protection), Richard English, Jackie Kerwood, Karen Howard, Tegan Gill, Eva Werry, Chris Wood, Michelle Mapplebeck | referral | open question 4 (claims) = yes; IWR-wide support as referral |
| AI and data leadership | 11 | Angela Luget (Chief AI Officer), Chris Thompson, Alberto Romero, Tom Spencer, David Young … | referral | add an AI/data referral lane |
| Group strategy / corporate development | 9 | Megumi Takenoshita, James Oram, Alistair Hargreaves (ex L&G digital proposition), Nathan Tomlinson, Charlotte Davey … | referral | treat group strategy as group-wide P3 |
| Transformation heads, scope not shown | 16 | Rachel Robinson, Paula Whitwell, Samantha Lacey, Radhika Kale, Jon Day … | referral | unscoped transformation = group-wide P3 |
| Architecture, scope not shown | 6 | Joshua Cruickshank, Luke Temple, Atanu B., Martin Copley, David McIntyre … | technical-integration | accept architecture heads without protection scope |
| Cross-line digital and customer | 5 | Kiran Bharucha, Alex Allen (MyAviva), Delia Todman, Jason Knowles, Chris Johnston | proposition | cross-line digital as P3 |
| Aviva Health (PMI) | 8 | Matthew McGill, Lisa Bartlett, Rob McKillop, Lucy Dearing, Charles McElroy … | none (anti-case) | a separate health campaign |

Not proposed: GI 104, wealth/pensions 27, distribution ~12, governance/HR/finance/comms, IT delivery, junk 24.

## Batch: Legal & General (298)

**Counts:** PASS 7 (P1 0, P2 1, P3 6) · WEAK 17 · FAIL 274 · registry 0. Under the cap (50).

**Data note:** the L&G export is a company-wide seniority pull, not a title pull: zero underwriting / Chief Underwriter / CMO titles, no Head of Protection. Only real protection buyer: Nicki Plews. Duplicates: Lee Taylor ×2, Christina Nicolaou ×2 (empty copies FAIL), Paul Lewis ×2 (both FAIL). Three "IT & Transformation Director" profiles (Siingh, Rautaray, Sundarraj) look like TCS account staff. Ruth Burgess has likely left. Group Protection (Yash Gupta, Chloe Carter, Jimmy Turrell) FAIL as group risk.

#### Proposed to SEND (L&G)
| Group | Person | Title | P | Angle |
|---|---|---|---|---|
| L&G | Nicki Plews | Head of Product and Proposition (ex Head of Protection Strategy and Proposition, ex Munich Re) | 2 | proposition |
| L&G | Tariq Surty | Chief Technology Officer ("CTO - Retail") | 3 | technical-integration |
| L&G | Michael Spiteri | Group CTO | 3 | technical-integration |
| L&G | Jenny Reeve | Group Head of Transformation | 3 | referral |
| L&G | Steve Davis | Group Director of Transformation | 3 | referral |
| L&G | Gary M. | Transformation Director - Retail | 3 | referral |
| L&G | Cris Saunders | Head of Groupwide Digital Products | 3 | referral |

#### WEAK (L&G)
| Person | Title | Group | Why borderline |
|---|---|---|---|
| Laura Mason | CEO, Retail | L&G | Runs the division that holds protection; CEO-to-CEO referral fits, but the card has no insurer-CEO tier |
| Wayne Lancaster | Head of Clinical Operations | L&G | Could be the medical-evidence team behind underwriting or Group Protection rehab |
| Judit F. | Head of IT & InfoSec (LGRS), "L&G Retail" | L&G | Lane names InfoSec owners for new business, no tier names the title |
| Claire Toller | CTO, OneTech Services | L&G | Shared tech unit; protection scope not shown |
| Lee Taylor | CTO | L&G | Division not shown; Retail CTO already PASS |
| Cheryl Hinton | CTO Innovation | L&G | Board seats point to Workplace Savings |
| Emese Simoradik | Product Director | L&G | Life actuary (ex Prudential Financial); line not shown |
| Dave Butcher | Product Director | L&G | Line not shown; ex Aon |
| Aran Chamberlain-Clark | Product Director | L&G | Line not shown; pensions-consulting background |
| Steven Morrison | Head Of Product Management | L&G | No line, no history |
| Andy Bergin | Head of Product and Delivery | L&G | No line, no history |
| Dan Borrill | Head of Proposition and Implementation | L&G | Line not shown; advice/wealth background |
| Rachel Cude | Head of Product Proposition Development & Oversight | L&G | Last proposition role was workplace savings |
| Natalie Bentley | Head of Pricing Execution | L&G | Protection pricing = P2, but common PRT team name |
| Matt Kirwin | Digital Product Director & Head of App | L&G | App spans lines |
| Fraser Brough | Head of Onboarding Administration | L&G | Earlier role group risk: likely scheme onboarding |
| OPG One Piccadilly Gardens | Owner | L&G | Company-named profile (standing decision 4); recommend drop |

#### Pools left out (L&G, seniors first)
| Pool | People | Who | Angle | What would have to change |
|---|---|---|---|---|
| A. Executives / strategy above the buyer | 6 | António Simões (Group CEO), Gareth Mee, Kate Avery (empty), Sarah Spooner (CCO), Martin Todd (Head of Strategy, Retail), James McMillan (Group Strategy) | referral | allow insurer CEOs/strategy as referral; one at most |
| B. Protection distribution / partnerships | 6 | Adrian Riddleston, Sam T. (BD, Insurance), Brett Dexter, Natalie H., Nick Birdseye, Paul Maxwell | referral | lift the adviser-distribution ban for protection partnership heads; only Riddleston and Sam T. show protection |
| C. Transformation, scope not shown | 10 | Kate Smalley, Rich Dixon, Simon Sheldon, Nina Taylor, Paul Rogers, Liz Greenwood, Russell Evans + 3 TCS-looking profiles | referral | treat unscoped transformation heads as group-wide P3 |
| D. Data and analytics | 5 | James Jarman (CDAO, Retail), Henry Carman, Mark Bird, David Stewart, Michaela Finlayson | technical-integration | add Retail data leads |
| E. Architecture, other CTO, DPO | 6 | Christina N. (CTO Group Functions), Sonya Cerutti (Head of Data Protection), Dan Kaiserman, James Bull, Neil Workman, Nik Hart | technical-integration | give architecture heads P3 |
| F. Conduct / customer outcomes | 3 | Joanne Gregory, Kerrie Mitchener-Nissen, Thomas Lucas | referral | pull Consumer Duty owners (card excludes compliance) |
| G. Protection claims | 1 | Arnaud Carette (Head of Retail Protection Claims Operations) | referral | reverse open question 4 (claims) |

## Skipped pools (script)

`skipped-detail.md`: 1135 not sent. Pools with a proposed angle are in each batch section above; add by name with `outbound_pack.py promote --names "…" --angle … --pool …`.
