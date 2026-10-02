---
qc_date: 2026-10-02
agent: message-sequencer
artifact: workspace/outbound/campaigns/2026-10-02-us-virta-health/messages/ (primary: amitrshah1, adamwolfberg, danhang; risk set: samiinkinen, caroline-roberts-md-b42848132, jason-lee-798b6b1, lindsayjohnson14, amy-mengyun-zhang, kristen-keating-weeks-055a8b24; _check.json; both summaries; both _batch-*.md read in full for the 50-person cross-check)
track: outbound
artifact_type: messages
total_score: 13/20
status: marginal
coordinator_review: done
---

# QC Report: message-sequencer, 2026-10-02, us-virta-health

**Artifact:** `workspace/outbound/campaigns/2026-10-02-us-virta-health/messages/` (50 people at one company, 2 batches)
**Total: 13/20, marginal.** Each message works on its own. Hooks are real and checked against the profiles. Every person got their own question from the card, the facts agree, and no outcome promise appears anywhere. The campaign's central rule is what fails. card:35 and card:138 say no two people share an opener, a central question, a CTA, a message 2 opener or a product sentence, and card:126 lists the peer groups most likely to forward to each other. Nearly every named peer group has a shared CTA, a shared context line or a shared sentence. Sentence-level fixes to 37 records are enough. Nothing needs to be regenerated.

Scored against `card-messages.md` and the two `_profiles-*.md` files. Per instructions, D is not capped for the missing `product:` in split files.

## Scores

| # | Category | Score | Max |
|---|----------|-------|-----|
| A | Adherence | 3 | 5 |
| B | Factual accuracy | 3 | 5 |
| C | Brand & tone | 2 | 3 |
| D | Format & structure | 2 | 3 |
| E | Output quality | 3 | 4 |

## What was wrong (specific)

### A. Adherence: 3/5
- **The 23 non-referral M1s draw their CTAs from a pool of four stock phrases.** "Open to a quick chat?" ×8 (danhang, kristin-bergethon, adriana-lindsey, castlehazzard, amitrshah1, naomikincler, holly-anderson, jennifer-arensdorf), "Might be worth a quick chat?" ×5 (adamwolfberg, shaila-chhibba, samiinkinen, caroline-roberts, christinevonderach), "Worth a quick chat?" ×3, "Worth a quick chat to explore?" ×2. This breaks card:126 for these named peer pairs: Dan and Amit, Adam and Caroline, Holly and Adriana, Naomi, Castle and Jennifer, and Neha and Karthik.
- **Identical product and context sentences inside named peer groups:**
  - Clinical. kristin-bergethon (_batch-1:122) and jeff-stanley (260) are verbatim the same. adamwolfberg (32) and stephanie-drullinger (168) are near-copies.
  - Finance. rogerkumar (492), alex-choi (566) and andreburkholder (695) are verbatim the same: "We build a two-photo body scan for member apps." manu-diwakar (363) matches dani-lasalvia (473) and patrick-tumpane (640). andrew-chen (676) matches kristenlarson4 (401).
  - Commercial. kristen-keating-weeks (_batch-2:245), lindsayjohnson14 (263) and ryannmdonohue (313) are verbatim the same: "For context, we built a guided two-photo body scan that runs white-label inside an app." laurawalmsley (227) is a near-copy.
  - Engineering/IT. nehashevade (179) and christinevonderach (203) are the same sentence: "Outputs are stored and deletable by scan ID." The scoping lines in nehashevade M2 (187) and kprasad07 M2 (_batch-1:289) are near-copies.
  - CEO, CPO and President. samiinkinen (_batch-2:33) is a near-copy of danhang (_batch-1:9).
- **M2 opener collisions:**
  - "One more try": kristenlarson4 and lindsayjohnson14 (commercial peers).
  - "Circling back": leanabalasco and laurawalmsley (ex-Personify peers), plus radthie and andrew-chen.
  - "Thinking about": holly-anderson and adriana-lindsey (named peers).
  - "Worth 15 min?" is the M2 CTA of both amitrshah1 and colin-daw. amitrshah1 and colin-daw also make the same central argument, a small pilot in one program.
- **M1 hook phrases repeat across batches.** 12 of the 15 batch-2 M1s reuse a batch-1 hook phrase ("Noticed your background", "Saw the news", "This stood out", "Quick thought", "Came across your work", and others). This is partly structural: the prompt forbids reading other batches, and the gate's opener check did not fire. Batch 1 also has internal collisions: kristin and kprasad07, adam and judy-huang, emily and patrick.
- **laurawalmsley M2 (_batch-2:233) asks "who owns the member app roadmap".** That is candi-buell's assigned question (card:99). card:126 requires every referral question to be different.
- **_summary-1:10 is wrong.** It says the four sales people each have "a different former-employer hook". danielle-ritter and jack-rose have no former-employer hook.

### B. Factual accuracy: 3/5
- **The speed wording is not verbatim in 6 records.** card:141 requires it "verbatim, every time". The six:
  - stephanie (_batch-1:176)
  - adriana (199)
  - jeff (266) "each one structured in under 45 seconds from the photos"
  - naomi (_batch-2:67)
  - holly (115)
  - jennifer (163)

  The same drift was flagged in the 2026-09-29 cardiometabolic QC.
- **The 112,100 line breaks its placement rule twice (card:140).**
  - mrondi M2 (_batch-1:84) attaches it to another clause: "Same guided capture every time, with 112,100 scans…". The rule requires its own sentence.
  - samiinkinen M2 (_batch-2:43) has it as a verbless fragment directly after "the care team compares the scans it selects". That reads close to patient scans.
- **caroline-roberts M1 (_batch-2:81) attributes the study to her.** "your work … including the April liver disease study" says she worked on it. The card only pairs her headline with V13 and does not say she was involved.
- **Stretches of Virta facts:**
  - danhang (_batch-1:7): "the app stays the same wherever a member's GLP-1 comes from". V3 says the provider oversight and nutrition care are the same on every route. It says nothing about the app.
  - jason-lee (_batch-2:295): "guarantees in its client contracts". The source is a press launch, not contract terms.
- **The V2 trio (the coordinator's question).** None of the three promises an outcome for FitXpress.
  - amy-mengyun-zhang (_batch-1:619) puts "Virta's cost guarantees" next to "who looks at new data sources". That reads as the scan feeding guarantee measurement, and it is the closest of the three to outcome-guarantee framing.
  - jason-lee adds speculation: "Virta may weigh any new capture carefully".
  - lindsayjohnson14 (_batch-2:261) is only filler, but it uses the date "June 2025". card:141 bans "years" among numbers, and only V19's "since 2014" is cleared.
  - Recommendation: keep V2 as context and do not put it next to data collection or contract exposure.
- **Passes:**
  - Every number comes from the card.
  - No client is named, and the 34,000 line is anonymous.
  - The compliance line is verbatim where required.
  - V6 is absent everywhere. Caroline has the April study and Adam the July one.
  - Caroline's repeatability sentence is verbatim §1.2.
  - V12 is never used.
  - The swap to kristen-keating-weeks correctly leaves out Accolade (not on her profile card), and the agent caught the unverifiable former employers of Naomi, Christine, Ryann and Sami.

### C. Brand & tone: 2/3
- **Tricolons.**
  - amitrshah1 M2 (_batch-2:17): "one program, one care team, scans the team selects".
  - danhang M2 (_batch-1:19): "One SDK inside the Virta app, nothing to ship, under 45 seconds…".
  - rogerkumar (490) lists three studies.
- **candi-buell M2 (_batch-1:350).** "Following your reply, or lack of one" reads as a jab.
- **Presumed reactions.**
  - jack-rose (418): "you probably hear"
  - holly (_batch-2:105): "you know that step well"
  - taraconboy M2 (462): "you would know which engineer to ask"
  - jason-lee (295): "Virta may weigh any new capture carefully"
- **Small slips.**
  - castlehazzard M2 (245) has "structured results" twice in one sentence.
  - sam-berklacich (600) "as the app grows" brushes card:149's growth ban.
- No detector bans and no dashes (confirmed by gate).

### D. Format & structure: 2/3
- **Seven batch-2 M1 paragraphs have 3 sentences.** The prompt allows at most 2: holly, colin, jennifer, kristen-keating-weeks, lindsay, shravya, jason-lee.
- **Three non-referral M1s have no soft CTA** (template step 5): liza-fryberger, jeff-stanley, heypaxton.
- Batch format, summaries, char limits and greetings are fine.

### E. Output quality: 3/4
- Personalization is real. Every message is well above 60% unique on its hook and question, and the hooks were checked against the profiles. Good lines worth keeping:
  - amitrshah1: pilot question
  - naomikincler: retakes
  - shaila-chhibba: rollout
  - jennifer-arensdorf: training material
- The problem is the shared layer: CTA, product line, referral context line and M2 bump. card:35 requires that a forwarded screenshot not read as a mail merge, and these pairs would: Roger and Alex, Kristin and Jeff, Kristen Weeks and Lindsay.
- Non-referral M2s are thin: a spec fragment, the compliance line and a CTA. Given the card's ban on outcome claims, this is acceptable.

## Top 3 issues (priority for improver)

1. **Peer-group collisions (card:35/126/138).** Every non-referral M1 needs its own CTA. Rewrite the referral context lines so no two of the 27 match. Fix the verbatim product sentences (kristin/jeff, neha/christine, roger/alex/andre, kristen-weeks/lindsay/ryann). Give the batch-2 re-run batch 1's openers, CTAs and context lines, because it cannot see them otherwise.
2. **Locked wording.** Make the speed phrase verbatim in 6 records. Give 112,100 its own sentence in mrondi, and move it away from "scans it selects" in samiinkinen.
3. **Claims next to V2 and the studies.** Remove Caroline's study attribution. Remove Jason's "guarantees in its client contracts / may weigh carefully". Decouple Amy's "cost guarantees" from "new data sources". Drop "June 2025" in Lindsay.

System notes (not the agent's fault):
- `split-messages` did not flag one shared CTA, context line or hook phrase across the 50. It needs a cross-batch check for CTA lines and for shared sentences of 8+ words.
- Speed-phrase drift has now recurred in two campaigns. A verbatim check in the gate would close it.

## Coordinator review

(filled in by Claude in chat after the auto-QC run)

## coordinator_review

```
agreement: ✅ agree
top_issue: 50 people at one company split into two blind batches produced shared CTAs, openers and context lines; fixes go batch 1 first, then batch 2 reading batch 1's fixed file, and check-messages now notes repeated closing asks per company and non-verbatim speed wording.
```
