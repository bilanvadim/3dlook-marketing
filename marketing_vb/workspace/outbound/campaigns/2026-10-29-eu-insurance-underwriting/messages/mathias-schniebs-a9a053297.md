# Mathias Schniebs — Leiter Services und Schnittstellen — Hannoversche Lebensversicherung AG

## Context used
- Angle: technical-integration
- Hook: leads services and interfaces at Hannoversche, which sells term life and BU direct online
- Proof point: REST API, 2 photos, Smart Scales weight estimate, threshold flag, retention and random identifiers, GDPR line (card)

---

## Connection request (Day 0)
_Без note — отправляем запрос в друзья без сопроводительного текста._

## Message 1 — Opener (сразу после принятия запроса)
Hi Mathias,

Had a thought about your remit for services and interfaces at Hannoversche, which sells term life and BU direct online.

Through the REST API, the application sends 2 photos and receives a Smart Scales weight estimate, with a flag where the gap to the declared weight crosses Hannoversche's threshold.

Which of your existing interfaces would carry the photos and the returned values?

Olena

**Char count:** 404 / 600

## Message 2 — Value + demo call (+5 дней, если нет ответа)
Hi Mathias,

Both the API and the SDKs return one timestamped record to your interfaces. Photos are deleted after processing or within 30 days, per the insurer's policy, and scan records use random identifiers.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

Times for a technical call: https://meetings.hubspot.com/olena-kudriavtseva

Olena

**Char count:** 449 / 550
