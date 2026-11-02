# Brendan Lambe — Head of Architecture and Cloud — Irish Life

## Context used
- Angle: technical-integration
- Hook: Head of Architecture and Cloud at Irish Life, where a record lands
- Proof point: REST API, SDKs, 2 photos, Smart Scales weight estimate, threshold flag, timestamped record

---

## Connection request (Day 0)
_Без note — отправляем запрос в друзья без сопроводительного текста._

## Message 1 — Opener (сразу после принятия запроса)
Hi Brendan,

Quick idea for you as Head of Architecture and Cloud at Irish Life. A new evidence step is judged on how its data reaches underwriting.

FitXpress offers a REST API and SDKs: 2 photos in the application return one structured, timestamped record per applicant, with a Smart Scales weight estimate and a flag set by the insurer's threshold.

In your architecture, where would such a record enter the underwriting system?

Olena

**Char count:** 438 / 600

## Message 2 — Value + demo call (+5 дней, если нет ответа)
Hi Brendan,

One record per applicant comes back through the API, on a random identifier. SDKs cover web and mobile.

In most enterprise deployments, the customer acts as the data controller and 3DLOOK acts as the data processor under GDPR, with a DPA that includes SCCs.

The owner of the underwriting system interface is welcome too. A call: https://meetings.hubspot.com/olena-kudriavtseva

Olena

**Char count:** 398 / 550
