# Log: BMI verification page

## 2026-11-09: review of Asselya's mockup v3 (Vadim: «там в слаці Аселя в каналі маркетинг просить подивитись сторінку бмі»)

- Source: Slack #marketing (C0C0TBSM90E), thread 1792656114.772339, 2026-10-22 08:01 UTC. Asselya: first draft of
  the updated BMI Verification LP, asks for review; the form is a draft, the standard form will be used. Reminders
  2026-10-26 (thread) and 2026-11-09 13:42 UTC (channel, mentions Vadim). No review in the thread until now.
- File `3dlook-bmi-verification-mockup-v3.html` (F0CBA73R1K3) → `asselya-v3-2026-10-22.html`; text extract
  `asselya-v3-2026-10-22.txt` (body ~1,450 words, 7 FAQ).
- Checks: live `/for-bmi-verification/` (title "FitXpress for Weight & BMI verification", ~990 words, schema WebPage +
  BreadcrumbList only); `/fitxpress/` still 301 → `/`, so the rebuild stays at the root URL; mock JS arithmetic
  (78 → 84 kg +7.7%, 80 kg +2.6%, BMI 26.1 / 28.1 / 26.7, lb conversion) correct; detector `--channel page`: no hard
  bans, direct address ~26 per 1,000; Yoast 60 / 154; claims against `proof-points.md`, `tech-spec.md`,
  `compliance.md`, the published online-pharmacy BMI article; logo rules (kit G-I waiver, Vadim 2026-10-21 and
  2026-11-06); live `/pricing/` snapshot 2026-11-05.
- Findings: Burlington Medical (MT client) in a "using FitXpress" logo row, UK Meds absent; RTPV and Clothing Detector
  above the confirmed level; "prompted-action liveness, coming soon" unconfirmed; no weight accuracy figure (approved
  "approximately 3.5% mean absolute error under evaluated conditions" unused); "within 45 seconds" vs canon; no problem
  block, no end-user value block, no price; boundary sentence repeated 4×, "review" 35×.
- `fact-sheet.md` written for the judge. Review in Russian: `review-2026-11-09-asselya-ru.md`. Not sent: waits for
  Vadim's go and his call on the hero audience (online pharmacies + weight-loss telehealth first, other verticals as
  cards linking down).
- Blind judge round 1 (fresh subagent): **39 / 100**. Hard fail: Burlington Medical (MT) under "Selected companies
  using FitXpress", UK Meds absent. Lowest: claims discipline. One fix: capture controls to the confirmed level,
  drop the liveness card and the pose chip, add 3.5% MAE under Predicted weight. `judge-round-1-asselya-v3.json`.
  Review §6 filled.
- 2026-11-09, Vadim: «це більше сторінка де ми описуємо фічі продукта і з неї вже переводимо на лендінги юз кейсів…
  вона більше має навчати та переводити на юз кейси які вже продають» + «також вона слугує можливо для тримання якихось
  ключів. перевір це». Review rewritten around that role: routing table to use-case landings (§1), keywords (§2), the
  "sell" items dropped or softened, judge total read as a vertical-page score.
- Keywords checked: GSC 16 months + Ahrefs US/GB (~1,000 units) → `keywords-2026-11-09.md`. The page holds
  "bmi verification" (pos 9.6 / 90 d 6.4) and, since 2026-08, the brand query "fitxpress" (after `/fitxpress/` went 301
  → `/` in 2026-03 and `/fitxpress/for-telehealth-and-weight-loss/` → telehealth in 2026-07). Ahrefs: "bmi verification"
  US 100 (half LADBS noise), "what is bmi verification" 20, "telehealth bmi verification methods" 20, UK "voy bmi
  verification call" 20.
- Open for Vadim: online pharmacies have no use-case landing (the 10-22 architecture replaced
  `/fitxpress/for-online-pharmacies/` with this page); for now the pharmacy card links to the compliance-guide article.
- 2026-11-09, Vadim on the pharmacy question («а як ти порадиш?» → recommendation: keep this page as the feature
  description, build a separate UK-led online pharmacy landing → «ок»). Review's pharmacy row updated: the card
  links to the compliance guide until `/for-online-pharmacies/` ships.
- 2026-11-09, sent on Vadim's «ок»: Russian reply in Asselya's thread 1792656114.772339 (ts 1794243415.275919,
  mentions Asselya) with `review-2026-11-09-asselya-ru.md` (F0CFQK9UARM) and `keywords-2026-11-09.md` (F0CFQKA2L15).
- Decision recorded in `landing-map.md` (BMI row = feature page; new row for online pharmacies), `site-inventory.md`,
  `page-types.md` and `site-architecture/architecture-2026-10-22.md` (reverses the 10-22 A-4 note).
- 2026-11-11, review item 4 reversed (Vadim: «лівнес теж вже буде до релізу сторінки»; Q3'26 board update lists
  liveness as ready for release in the iOS/Android SDKs). Russian correction posted in Asselya's thread
  1792656114.772339 (ts 1794409611.489999): keep the card; at publication drop «Coming soon» + the «Confirm release
  timing» line if released, otherwise keep «Coming soon»; confirm release and integrations with product first.
  See `brand-assets/product-info/roadmap.md`.
