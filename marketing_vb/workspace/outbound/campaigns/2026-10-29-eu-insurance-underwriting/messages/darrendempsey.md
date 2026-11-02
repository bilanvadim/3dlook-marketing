# Darren Dempsey — Chief Technology Officer — Munich Re Automation Solutions Ltd

## Context used
- Angle: technical-integration
- Hook: software architecture; CTO of the platform that applies an insurer's rules
- Proof point: REST API, 2 photos, Smart Scales weight estimate, threshold flag, retention, GDPR line (card)

---

## Connection request (Day 0)
_Без note — отправляем запрос в друзья без сопроводительного текста._

## Message 1 — Opener (сразу после принятия запроса)
Hi Darren,

Came across your work in software architecture at Munich Re Automation Solutions. ALLFINANZ applies an insurer's rules on one SaaS platform.

Smart Scales turns 2 photos into a weight estimate, and the timestamped record carries a flag when the gap to the declared weight crosses the insurer's threshold.

Where in ALLFINANZ would the estimate and the flag be read: at the journey step or inside the rules?

Olena

**Char count:** 425 / 600

## Message 2 — Value + demo call (+5 дней, если нет ответа)
Hi Darren,

A REST API request from the journey returns the record as structured fields that rules can use. Photos are deleted after processing or within 30 days, per the insurer's policy.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

I can walk through the REST API on a call: https://meetings.hubspot.com/olena-kudriavtseva

Olena

**Char count:** 442 / 550
