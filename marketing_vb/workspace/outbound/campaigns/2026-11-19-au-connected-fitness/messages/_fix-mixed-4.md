# Fix round 1, batch mixed-4: 2026-11-19-au-connected-fitness (QC 11/20, Vadim chose a fix round, 2026-11-20)

Apply EVERY item below to `messages/_batch-mixed-4.md`, then run `split-messages` until exit 0, then stop. Edit only the named sentences and the inserts; leave every other sentence as it is. Do not rewrite whole messages.

Rules for this round (from the card; the QC list follows them):
- **Message 1 order:** company line, then ONE pain sentence, then the FitXpress fix sentence(s), then the question (Vadim 2026-11-18: Message 1 explains the pain and how the product solves it). A "pain insert" goes right before the first sentence that starts "FitXpress". The insert text may be used verbatim for every listed person (repeats at one company are allowed, Vadim 2026-11-20). If the message already says the same pain in other words, replace that sentence with the insert instead of having two.
- **Respect each company's Account facts Never line** in your insert (e.g. Fernwood: no "weight"; CSB: never describe what the app logs; One Playground: no coach "works from a weight entry").
- **Referral Message 2:** one value line that continues their Message 1 question, then the easy out as ONE plain sentence ("If X sits with head office, a pointer to whoever owns the member app would help."), then the soft ask on its own line. Never two closers ("A short call could cover it, or point me to..." followed by "Might be worth a quick chat?"). Never write as if the person already replied ("Your answer would...", "That tells me...").
- **The soft ask ("Might be worth a quick chat?" and the like) is always its own last paragraph**, never glued to the end of the previous one. Where the QC list says "soft ask on its own line", split it.
- **"3DLOOK has worked with 100+ clients" and "112,100 scans" only for founders, CEOs and managing directors**, and never bolted on as a stand-alone line; where QC says delete, delete.
- **Page URL:** about half of each company's Message 2s carry https://3dlook.ai/fitxpress/for-connected-and-digital-fitness/ on its own line, before the soft ask, with no label in front ("Details:", "Setup page:" are out). Where QC says "add the URL", add it that way.
- After `split-messages` passes, re-read every message you changed, in full.

QC's line-level fixes for this batch (person_id, current → replacement):

**Pain inserts (36 Message 1s).** Each sentence is chosen against that company's Never list:

| Company | People | Sentence to insert |
|---|---|---|
| Barre Body | `siobhanwhitby` | "Strength and posture change between classes is easy to feel and hard to record." |
| Jetts Fitness | `ben-mason-86563b22`, `eddieswinnen`, `samantha-jane-a3012b166` | "Between sessions, a weight entry leaves out waist and lean mass change." |
| Studio Pilates | `john-l-scott-8380a045`, `tanya-winter-b9b52524`, `winterjade` | "Between classes, a weight entry leaves out waist and lean mass change." |
| Sweat | `bettykarikis`, `claireseidler`, `robert-ware-5b867a48` | "A weight figure on its own leaves out waist and lean mass change." |
| Peaches Pilates | `chris-hole`, `teah-foot-3065b5244`, `tori-clapham-902869195` | "Between classes, a weight entry leaves out waist and lean mass change." |
| CONDITN | `daniel-capilli-b27623308`, `jordan-mccreary-5456aba4` | "A weight figure leaves out change at the waist and in lean mass." |
| Revo | `jordan-checker-876b6516b`, `kalen-coughlan-a0a626177`, `kayla-braithwaite-a34753209` | "Between club visits, a weight entry leaves out waist and lean mass change." |
| The Yard | `jessica-buxton-a7722883`, `tiarne-bova-b65456247` | "A weight entry leaves out how waist and hip change as a block runs." |
| GymMaster | `asmithnz`, `kate-rawnsley-shirtcliff-07926923` | "A weight entry leaves out waist and lean mass change." |
| Tammy Fit | `amy-hembrow-b435634a` | "Workout counts show effort, and they leave body change out." (no weight wording) |
| STRONG Pilates | `carl-planicka-14b39b421`, `kat-hegarty-097099b6` | "Between classes, a weight entry leaves out waist and lean mass change." |
| REVL | `jake-hendry-877168224` | "A weight entry misses how waist and hip change across a block." |
| One Playground | `danielbowden411` | "A weight entry leaves out waist and lean mass change." |
| Fluidform | `penelope-hoess-b5410633` | "A weight entry leaves out waist and lean mass change." |
| Clubworx | `emilysmart` | "In a member app, a weight entry leaves out waist and lean mass change." |
| Gym Mate | `bdquinney` | "In a member app, a weight entry leaves out waist and lean mass change." |
| Gravl | `julian-gargicevich` | "Between sessions, body change is hard to see without a measured record." |
| Vision PT | `damian-glynn-vision-personal-training-b0027016` | "At a plan change, a weight entry leaves out waist and hip change." |
| KIC | `emily-robinson-9b7a2011a` | "Between programs, body change is hard to compare without a record taken the same way each time." (no weight wording) |
| Fitstop | `riley-woodcock` | "Between sessions, body change is hard to compare without a record taken the same way each time." |
| UBX | `johncuskelly` | "Between club sessions, a weight entry leaves out waist and lean mass change." |

**Line fixes:**
- `atmerriman` M1: "A coach setting a member's next block works from a weight entry that leaves out waist and hip change." → "A weight entry on its own leaves out waist and hip change."
- `matthewkane` M1: "A weight entry between those check-ins leaves out how waist and hip change." → "Strength and posture change between those check-ins is easy to feel and hard to record."
- `jessica-buxton-a7722883` M1: "The THE YARD GYM app first appeared in April." → "The Yard's app first appeared in April."
- `danielbowden411` M1: "…opened its Zetland superboutique this month…" → "…opened its Zetland superboutique in November…"
- `asmithnz` M1: "GymMaster shipped AI assistant features for club staff this month." → "GymMaster shipped AI assistant features for club staff in November."
- `james-mccreary` M2: "For context, there were 112,100 scans in 2025 across all 3DLOOK customers." → delete.
- `kat-hegarty-097099b6` M2: "There were 112,100 scans in 2025 across all 3DLOOK customers." → delete.
- `claireseidler` M2: "Any answer fits the same setup." → "A body record could sit next to the program's weekly structure, in Sweat's own screens."
- `samantha-jane-a3012b166` M2: "That route matters here, because any new member feature reaches your club through head office." → "A new member feature would reach your club from head office, with nothing to install."
- `john-l-scott-8380a045` M2: "That path decides how any member feature would land in the studios, and the scan would be shown only as Studio Pilates chooses." → "A feature like this would reach the studios through the SP app, shown only as Studio Pilates chooses."
- `tammy-hembrow-3a7739241` M2: "If they belong there, 3D Body Progress tracking and 3D Goal Visualization on the Pro plan give members a side-by-side view of two scans they choose." → "If they belong there, 3D Body Progress tracking on the Pro plan shows a side-by-side view of two scans the program selects." Goal Visualization is dropped because the brand's Never line bars shape wording.
- `penelope-hoess-b5410633` M2: "…give members a side-by-side view of two scans they choose." → "…give members a side-by-side view of two scans the program selects."
- `teah-foot-3065b5244` M1: "Operations and partnerships at Peaches Pilates covers how new capabilities reach members of Peaches Online." → "You head operations and partnerships at Peaches Pilates." Her profile is empty, so the copy stays title-based.
- `tiarne-bova-b65456247` M1: "A scan inside the app would give members a measured body record next to it." → "A scan inside the app would give members a measured body record next to that training."
- **URL:** add it to one REVL Message 2 (cassie-green or jake-hendry) and one One Playground Message 2 (atmerriman or danielbowden411). Both companies have none now.
