# Fix list — batch `fitstop` — 2026-10-12

Rules for every person you touch: **"Coordinator decisions 2026-10-12" in `card-messages.md` (rules 1-19)**, plus the technical lane note on data handling. Every batch gets the same rules.

## Main job

Line-fix the people named below.

Then read **every other Message 2** in the file against rules 1-6 (value line, no fit-judging by unit people, easy-out and closer variety per company, no call length, openings). Fix the ones that break a rule and list them in the summary. Leave Message 1s you were not asked to touch exactly as they are.

## From the QC report (only lines that name people in this batch)

- [A. Adherence: 2/5] **Per-brand variation (check 1).** › **Themes:** within quota at Fernwood (max 6/35), Jetts (5/27) and BFT (4/20). At Fitstop the "what has training changed" question runs 7/32: richard-hallam, paul-collins, kevin-kensley, kelly-wade, kendall-winslow, paul-emanuel, chandell-fretwell. That is slightly over the ~6 cap.
  → in this batch: richard-hallam-14a09765, paul-collins-78352720, kevin-kensley-0b048211b, kelly-wade-12ab81192, kendall-winslow-6b81501aa, paul-emanuel-1545a1112, chandell-fretwell-3618bb106
- [A. Adherence: 2/5] **Per-brand variation (check 1).** › **Opener repeats inside one company:** › Fitstop: "Noticed you own a Fitstop." is word for word in bruce-mcconnel and brenna-dillon. "Wanted to reach out about Fitstop X" appears in chris-janke and josephine-tuah. Nine Fitstop M1s open with "Noticed".
  → in this batch: bruce-mcconnel-7909ba32, brenna-dillon-64b6a227a, chris-janke-18586a2aa, josephine-tuah-27a0a0169
- [B. Factual accuracy: 3/5] **Prospect data placed next to ours:** › jaynevaiao: "sit beside the coach's own numbers".
  → in this batch: jaynevaiao
- [B. Factual accuracy: 3/5] **Implied churn or poor measurement:** › jonpepper M1 says reviews "run a little differently from site to site".
  → in this batch: jonpepper
- [C. Brand & tone: 1/3] **"so" introducing a benefit** (card word trap; the gate missed it): shaun-pickering, alissa-o-flaherty, katelyn-farmer, tj-groot, josh-muriwai, sam-merza, paul-brown, jonpepper, josephine-tuah, brooke-price, zaac-schembri.
  → in this batch: jonpepper, josephine-tuah-27a0a0169
- [C. Brand & tone: 1/3] **Presumed reaction as an M2 template** (about 30). Shapes like "Founders usually ask…", "Group trainers tend to like…", "You will know…": › Fitstop: bentoleafoa, paul-emanuel, mark-vaiao, rhianna-buchanan
  → in this batch: bentoleafoa, paul-emanuel-1545a1112, mark-vaiao-04a784a2, rhianna-buchanan-140429bb
- [C. Brand & tone: 1/3] **Dangling "as [role]" openers that make Vadim the owner or director:** danny-pearson, matt-rees, damientampling, dan-bova, jon-davie, michael-nysten, steve-hobart, lauren-nash, emilene-lawrance, luke-skoric.
  → in this batch: lauren-nash-93a465347, emilene-lawrance-5b4926360
- [E. Output quality: 2/4] **Call length (check 3).** 34 M2s name a length: 15 min ×17, ten min ×14, twenty min ×3. The card never asks for one. › The lengths are not consistent within one network: Fitstop has adam-stevens at ten minutes and sam-seaton at twenty.
  → in this batch: adam-stevens-0b788589, sam-seaton-98411b16b

## From the coordinator's scan (rules the gate does not check)

Each line: the rule or the repetition, then the person. For a company-level line (a sentence, opener or closer shared by several people, the speed phrase or the 100+ line over the cap), keep it for at most the cap and give the others their own wording from rule 7. Every pair of messages still cites at least one number.

- COMPANY Fitstop: M2 closer shared by 2: "if member experience sits with someone else at fitstop, i wo"; brenna-dillon-64b6a227a
- COMPANY Fitstop: M2 closer shared by 2: "if member experience sits with someone else at fitstop, i wo"; nebojsa-vujic-613b91116
- COMPANY Fitstop: sentence shared by 2: "a first session is booked in the app, and first-timers arrive early to meet their trainers."; brenna-dillon-64b6a227a
- COMPANY Fitstop: sentence shared by 2: "a first session is booked in the app, and first-timers arrive early to meet their trainers."; josephine-tuah-27a0a0169
- COMPANY Fitstop: sentence shared by 2: "fitxpress turns two phone photos into 80+ body measurements."; jaynevaiao
- COMPANY Fitstop: sentence shared by 2: "fitxpress turns two phone photos into 80+ body measurements."; mark-vaiao-04a784a2
- COMPANY Fitstop: sentence shared by 2: "noticed you own a fitstop."; brenna-dillon-64b6a227a
- COMPANY Fitstop: sentence shared by 2: "noticed you own a fitstop."; bruce-mcconnel-7909ba32
- RULE  100+ attribution: andrew-papadopoulos-1992a341a M2
- RULE  call length: adam-stevens-0b788589 M2
- RULE  call length: sam-seaton-98411b16b M2
- RULE  drift/leave/by eye: jonpepper M1
- RULE  fit-judging: jaynevaiao M2
- RULE  presumed reaction: bentoleafoa M2
- RULE  presumed reaction: paul-emanuel-1545a1112 M2
- RULE  so-benefit: bentoleafoa M1
- RULE  so-benefit: chandell-fretwell-3618bb106 M1
- RULE  so-benefit: jonpepper M1
- RULE  so-benefit: josephine-tuah-27a0a0169 M2

## People to touch (22)

richard-hallam-14a09765, paul-collins-78352720, kevin-kensley-0b048211b, kelly-wade-12ab81192, kendall-winslow-6b81501aa, paul-emanuel-1545a1112, chandell-fretwell-3618bb106, bruce-mcconnel-7909ba32, brenna-dillon-64b6a227a, chris-janke-18586a2aa, josephine-tuah-27a0a0169, jaynevaiao, jonpepper, bentoleafoa, mark-vaiao-04a784a2, rhianna-buchanan-140429bb, lauren-nash-93a465347, emilene-lawrance-5b4926360, adam-stevens-0b788589, sam-seaton-98411b16b, nebojsa-vujic-613b91116, andrew-papadopoulos-1992a341a

## When you are done

Run `python3 scripts/outbound_pack.py split-messages --campaign 2026-10-11-au-sport-fitness --in messages/_batch-fitstop.md` until it exits 0, update `messages/_summary-fitstop.md` (people touched, what changed, anything you could not fix), and stop.
