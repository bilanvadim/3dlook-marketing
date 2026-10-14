---
product: fitxpress | mobile_tailor
status: paused (Vadim, 2026-10-14). Decisions pending, see the end of this file
---

# Site chatbot on 3dlook.ai: audit and proposal (2026-10-14)

The full write-up for the team is the Google Doc "3dlook.ai Website Chatbot: Audit and Proposed Setup", `1J78XjJS3DlYKlwgVl-JLK0OClZLJC5BIx-r4TJPEyD4`, in Vadim's Drive. It is not shared yet.

HubSpot numbers and internal routing findings stay local in `data/`, which is excluded from git (public repo). The Wrist Measurement page is out of scope here. Its owner decides about it separately.

## What runs today

- **Tool.** HubSpot Chatflows, portal 6014382, chatflow "Main ChatBot v 3.0". The site has no other chat vendor.
- **Bot.** A scripted bot with no AI and no handoff to a person. It is named "Jason" and uses a stock photo as avatar.
- **Where it shows.** Every page except `/mobile-tailor/*`, where HubSpot hides it.
- **When it opens.** On desktop the welcome message pops open after 15 seconds. On mobile there is only the launcher.
- **Script.** "How we can help you?" with two buttons. Typing is disabled.
  - "Learn more" asks for first name, last name, company website (URL only) and business email. It then says "our team will contact you shortly" and mentions case studies.
  - "7-day trial" replies "Please sign up for a trial here." and links to `/pricing?utm_source=website&utm_medium=chatbox&utm_campaign=chatbox-flow`.

## Problems

1. **The website step is a dead end.** Any answer that is not a URL gets "I'm sorry, I didn't get that. Try again?", with no limit. Visitors without a site cannot finish.
2. **Visitors cannot ask a question.** Free text is off at the start. Questions typed later land in the name or website fields.
3. **The email comes last.** Most visitors leave before they give it.
4. **The trial button is on the wrong pages.** FitXpress has no trial before a contract (`brand-assets/product-info/pricing.md`, 2026-10-14). Mobile Tailor does have a 7-day self-serve trial, but the bot is hidden on `/mobile-tailor/*`.
5. **A bot with a person's name and photo.**

## Proposal: one chatflow per page group

| Chatflow | Pages | Lead owner |
|---|---|---|
| General / FitXpress | all except `/mobile-tailor/*` and `/wrist-measurement/*` | to decide |
| Mobile Tailor | `/mobile-tailor/*` | to decide |
| Wrist Measurement | `/wrist-measurement/*` | handled separately |

**General / FitXpress**
- **Identity and welcome.** "3DLOOK Assistant" with no personal photo. Welcome: "Hi! What brings you to 3DLOOK today?"
- **"Book a demo".** Business email → company name (plain text) → "What are you working on?" → the owner's meetings link. If the answer is "Apparel or uniforms", hand off to the Mobile Tailor branch. If it is "Wrist sizing", send no meetings link and route to the wrist owner.
- **"How do I get started?"** "FitXpress starts with a demo call. After it, you get demo access to try the scan flow yourself. Once a contract is signed, the first month is free for integration and testing." No numbers: no scan counts, durations or prices. Point apparel visitors to the Mobile Tailor plans and the 7-day trial.
- **"I have a question".** Free text → business email → owner.
- **"Something else".** Jobs, partnerships and press get the careers link or an email address. No sales record is created.

**Mobile Tailor** (first confirm that the MT team wants a chat)
- **Welcome:** "Measuring customers for custom apparel or uniforms?"
- **"Start a 7-day trial":** a link to the MT plans, with `utm_medium=chatbox`. Always say "7-day trial", never "free trial".
- **"Talk to sales":** for uniform programs, made-to-measure at scale and integrations.
- **"I have a question".**

**Rules for every bot message:**
- the CLAUDE.md language rules apply;
- no "free trial" for FitXpress;
- no "HIPAA compliant";
- no accuracy figures;
- no customer names.

**How to build it:**
1. Clone the live chatflow.
2. Target the clone at a test query parameter.
3. Walk every branch.
4. Switch the URL targeting over.
5. Turn off "v 3.0".

Each page must match exactly one chatflow, so set explicit URL exclusions. Chatflows have no API: changes are made by hand in HubSpot (Automation → Chatflows), and our HubSpot access is read-only.

## Decisions pending

1. Owner and meetings link for General/FitXpress leads.
2. Does Mobile Tailor want the chat on its pages, and who owns those leads?
3. Bot name and avatar.
4. Where chat leads go: a sales record instead of a support ticket. What happens to the open chat tickets?
5. Should we test HubSpot's AI Customer Agent later? It would need approved sources (product pages, the trust FAQ), a ban list and a handoff to a person.
