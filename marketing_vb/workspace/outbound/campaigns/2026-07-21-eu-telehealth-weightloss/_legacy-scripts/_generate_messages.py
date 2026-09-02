#!/usr/bin/env python3
"""
Message-sequencer generator for campaign 2026-07-21-eu-telehealth-weightloss.
Profile: olena (Olena Kudryavtseva, BD Europe). Product: FitXpress.

NOTE ON SPEC: The brief that triggered this run asked for a legacy 4-step
sequence (note+3 follow-ups). That sequence was deprecated today (2026-07-21)
per CLAUDE.md changelog in favor of a 2-message, note-less sequence
(message-sequencer.md, outbound-message1-template.md, outbound-message2-template.md).
Since the current CLAUDE.md instructions override default behavior and no
explicit override to the legacy format was confirmed, this generator follows
the CURRENT 2-message architecture:
  - Connection request: sent WITHOUT a note (connection_note left blank)
  - Message 1: sent immediately on accept, <=600 chars
  - Message 2: sent +5 days if no reply, <=550 chars, ends in calendar CTA
    (Olena's link) for PASS, soft chat ask for WEAK-lower-touch treatment
    kept consistent with template (calendar CTA for all, "10 min" vs "15 min"
    wording carries the PASS/WEAK distinction requested in the brief).
GDPR mention: folded into Message 2 (compliance line) since compliance.md
instructs including it in "step 2 or 3" of the sequence, and Message 2 is
the analogous slot in the current 2-message architecture.
"""
import csv
import hashlib
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
VALIDATED = os.path.join(BASE, "people-validated.csv")
RAW = os.path.join(BASE, "people-raw.csv")
MSG_DIR = os.path.join(BASE, "messages")
os.makedirs(MSG_DIR, exist_ok=True)

BANNED_WORDS = [
    "leverage", "utilize", "harness", "robust", "seamless", "comprehensive",
    "delve", "navigate", "tapestry", "realm", "game-changer", "revolutionary",
    "disrupt",
]

OLENA_CALENDAR = "https://meetings.hubspot.com/olena-kudriavtseva"

# ---------- Load & join data ----------

def load_raw():
    raw = {}
    with open(RAW, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            raw[row["person_id"]] = row
    return raw


def load_validated():
    with open(VALIDATED, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


raw_by_id = load_raw()
validated = load_validated()

TARGET_CLASS = {"PASS_P1", "PASS_P2", "PASS_P3", "WEAK"}
contacts = [r for r in validated if r["classification"] in TARGET_CLASS]

# ---------- Variant pools ----------

HOOKS = [
    "Circling back after connecting",
    "Saw your work at {company}",
    "Quick thought on {company}'s weight-management side",
    "Noticed your background in {field}",
    "Came across {company}'s program",
    "Got me thinking about your patient journey",
    "Curious about your take on remote progress tracking",
    "Quick note on something in your space",
    "Spotted something relevant to {company}",
    "Thought I'd share something specific to your program",
    "Quick one on GLP-1 program retention",
    "Had a thought after reading about {company}",
    "Quick idea for your team",
    "This caught my eye about {company}",
    "Wanted to reach out on something concrete",
]

OBSERVATIONS = {
    "weight-management": [
        "Programs like {company}'s live or die on whether patients can see real progress between visits, and self-reported weight rarely tells the full story.",
        "With GLP-1 demand rising across Europe, verifying body composition (not just weight) is becoming the differentiator for programs like yours.",
        "Weight-loss programs that show visible body change tend to keep patients engaged past the first few months, which is the hardest stretch to hold onto.",
    ],
    "member-engagement": [
        "Member engagement in digital weight programs usually drops once the initial motivation fades, unless there's something concrete to show for the effort.",
        "The apps that keep members longest are the ones giving them something to see, not just a number on a scale.",
    ],
    "virtual-care": [
        "Virtual care platforms adding weight management often hit the same wall: no objective way to show a patient's progress between calls.",
        "As virtual-care platforms expand into weight and metabolic health, the gap is usually the lack of an objective progress signal between consultations.",
    ],
    "digital-transformation": [
        "Digital transformation programs in healthcare increasingly need measurable, auditable patient data, not just more app features.",
        "Large providers moving services digital usually need a data layer that's both patient-friendly and defensible for governance.",
    ],
    "compliance": [
        "With the EU Health Data Space and Germany's DiGA framework tightening, verified and auditable patient data is becoming less optional.",
        "Regulatory scrutiny on digital health data is increasing across the EU, which puts a premium on verifiable, audit-ready records.",
    ],
    "clinical-operations": [
        "Clinical operations teams running weight or metabolic programs often lack a fast, objective way to check patient progress between appointments.",
        "Operational teams supporting weight-management pathways usually need a lighter way to capture consistent measurements at each check-in.",
    ],
    "default": [
        "Teams running digital health or weight-management programs often struggle to verify patient progress objectively between visits.",
        "Programs supporting patient weight or metabolic goals usually rely on self-reported numbers, which is a known gap.",
    ],
}

PRODUCT_INTRO = {
    "clinical": (
        "We've built a mobile body scanning layer at 3DLOOK: two phone photos produce structured body measurements and composition data that drop "
        "straight into the patient record."
    ),
    "member": (
        "We've built a mobile body scanning layer at 3DLOOK: two phone photos produce structured body measurements and composition data that drop "
        "straight into the member profile."
    ),
}

SOFT_CTA_M1 = [
    "Might be worth a quick chat?",
    "Worth a quick chat to explore?",
    "Open to a quick chat?",
    "Could be worth 10 minutes to compare notes?",
]

VALUE_LINES_M2 = {
    "weight-management": "Where this tends to help programs like {company}'s: members stay in the program longer once they can see real body change, not only a weight trend line. Yazen uses this in their weight-loss app today, with 34,000 scans run in 2025.",
    "member-engagement": "Where this tends to help: engagement holds up longer when members get a visible, structured progress signal, not just a number. Yazen runs this in production, 34,000 scans in 2025, as part of member progress tracking.",
    "virtual-care": "Where this tends to help virtual-care teams: patients get an objective progress check between consultations, without an extra visit. Yazen has this live for weight-loss support, 34,000 scans in 2025.",
    "digital-transformation": "Where this tends to help a digital program like {company}'s: it adds a structured, trackable data point without new hardware or extra visits. Yazen runs this in production for weight-loss support, 34,000 scans in 2025.",
    "compliance": "Where this tends to help compliance-minded programs: the data is structured and traceable, which supports the audit trail regulators are asking for. Yazen runs this in production, 34,000 scans in 2025.",
    "clinical-operations": "Where this tends to help operations teams: a 45-second scan at check-in replaces manual measurement without adding staff time. Yazen uses it for weight-loss progress tracking, 34,000 scans in 2025.",
    "default": "Where this tends to help programs like {company}'s: members and care teams get an objective, trackable progress signal instead of a self-reported number. Yazen runs this in production, 34,000 scans in 2025.",
}

GDPR_LINE = "Data handling is GDPR-aligned: photos are deleted immediately or within 30 days, and no personal identifiers are stored."


def angle_key(raw_angle: str) -> str:
    a = (raw_angle or "").strip().lower()
    if not a:
        return "default"
    for key in ["weight-management", "member-engagement", "virtual-care",
                "digital-transformation", "compliance", "clinical-operations"]:
        if key in a:
            return key
    return "default"


def is_clinical_title(title: str) -> bool:
    t = (title or "").lower()
    return any(k in t for k in [
        "medical", "physician", "dr.", "chief medical", "clinical", "surgeon",
        "dietitian", "doctor",
    ])


def pick(pool, seed, salt=""):
    h = int(hashlib.sha256((seed + salt).encode()).hexdigest(), 16)
    return pool[h % len(pool)]


def fit_len(s: str, limit: int) -> str:
    """Trim on a word boundary if over limit, keep it graceful."""
    if len(s) <= limit:
        return s
    cut = s[:limit]
    cut = cut.rsplit(" ", 1)[0]
    return cut.rstrip(",.;: ") + "."


def check_banned(text: str):
    hits = []
    low = text.lower()
    for w in BANNED_WORDS:
        if w in low:
            hits.append(w)
    if "it's not just" in low:
        hits.append("not-just-construction")
    if re.search(r"[—–]", text):
        hits.append("long-dash")
    return hits


def clean_company_field(name: str) -> str:
    return name.strip().strip('"')


def build_message1(first_name, company, angle, seed):
    hook_t = pick(HOOKS, seed, "hook")
    hook = hook_t.format(company=company, field="digital health")
    obs_t = pick(OBSERVATIONS.get(angle, OBSERVATIONS["default"]), seed, "obs")
    obs = obs_t.format(company=company, field="digital health")
    intro_key = "clinical" if angle in ("clinical-operations", "compliance") else "member"
    intro = PRODUCT_INTRO[intro_key]
    cta = pick(SOFT_CTA_M1, seed, "cta1")
    msg = f"Hi {first_name},\n{hook}. {obs}\n{intro} {cta}\nOlena"
    msg = fit_len(msg, 600)
    return msg


def build_message2(first_name, company, angle, classification, seed):
    value_t = VALUE_LINES_M2.get(angle, VALUE_LINES_M2["default"])
    value = value_t.format(company=company)
    minutes = "10" if classification == "WEAK" else "15"
    cta = f"Worth {minutes} min to walk through it? Grab a slot: {OLENA_CALENDAR}"
    msg = f"Hi {first_name},\n{value} {GDPR_LINE}\n{cta}\nOlena"
    if len(msg) > 550:
        # drop GDPR line first if too long, keep value + CTA
        msg = f"Hi {first_name},\n{value}\n{cta}\nOlena"
    msg = fit_len(msg, 550)
    return msg


# ---------- Generate ----------

by_company_seq = {}
records = []
warnings = []

for row in contacts:
    pid = row["person_id"]
    raw = raw_by_id.get(pid, {})
    first = row["first_name"].strip()
    last = row["last_name"].strip()
    company = clean_company_field(row["company_name"])
    title = row["title"].strip()
    country = row["location_country"].strip()
    city = raw.get("location_city", "").strip()
    location = f"{city}, {country}" if city else country
    linkedin_url = raw.get("person_linkedin_url", "").strip()
    classification = row["classification"]
    angle = angle_key(row.get("message_angle", ""))

    seq = by_company_seq.get(company, 0)
    by_company_seq[company] = seq + 1
    seed = f"{pid}|{company}|{seq}"

    m1 = build_message1(first, company, angle, seed)
    m2 = build_message2(first, company, angle, classification, seed)

    hits1 = check_banned(m1)
    hits2 = check_banned(m2)
    if hits1 or hits2:
        warnings.append(f"{pid} ({first} {last}, {company}): banned pattern hit -> m1={hits1} m2={hits2}")

    if len(m1) > 600:
        warnings.append(f"{pid}: message_1 over 600 chars ({len(m1)})")
    if len(m2) > 550:
        warnings.append(f"{pid}: message_2 over 550 chars ({len(m2)})")

    rec = {
        "person_id": pid,
        "first_name": first,
        "last_name": last,
        "full_name": row["full_name"],
        "title": title,
        "company": company,
        "location_country": country,
        "location": location,
        "linkedin_url": linkedin_url,
        "classification": classification,
        "angle": angle,
        "message_1": m1,
        "message_2": m2,
        "len1": len(m1),
        "len2": len(m2),
    }
    records.append(rec)

    fm = (
        "---\n"
        "product: fitxpress\n"
        "campaign: 2026-07-21-eu-telehealth-weightloss\n"
        "profile: olena\n"
        f"person_id: {pid}\n"
        f"full_name: {row['full_name']}\n"
        f"title: {title}\n"
        f"company: {company}\n"
        f"location: {location}\n"
        f"classification: {classification}\n"
        f"angle: {angle}\n"
        "sequence: connection_request(no note) -> message_1(day 0, on accept) -> message_2(day +5, if no reply)\n"
        "---\n\n"
    )
    body = (
        f"# {row['full_name']} — {title} — {company}\n\n"
        "## Connection request\n(sent WITHOUT a note, per current outbound spec)\n\n"
        f"## Message 1 (day 0, on accept) — {len(m1)}/600 chars\n```\n{m1}\n```\n\n"
        f"## Message 2 (day +5, if no reply) — {len(m2)}/550 chars\n```\n{m2}\n```\n"
    )
    with open(os.path.join(MSG_DIR, f"{pid}.md"), "w", encoding="utf-8") as out:
        out.write(fm + body)

print(f"TOTAL_CONTACTS={len(records)}")
print(f"WARNINGS={len(warnings)}")
for w in warnings[:50]:
    print("WARN:", w)

# ---------- CSV export ----------
csv_path = os.path.join(BASE, "closelyhq-import.csv")
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "first_name", "last_name", "company", "title", "linkedin_url",
        "location", "connection_note", "message_1", "message_2",
    ])
    for r in records:
        writer.writerow([
            r["first_name"], r["last_name"], r["company"], r["title"],
            r["linkedin_url"], r["location"], "", r["message_1"], r["message_2"],
        ])
print(f"CSV_WRITTEN={csv_path}")

# ---------- Summary ----------
from collections import Counter, defaultdict

by_company = defaultdict(list)
for r in records:
    by_company[r["company"]].append(r)

class_counts = Counter(r["classification"] for r in records)
angle_counts = Counter(r["angle"] for r in records)

summary_lines = []
summary_lines.append("---")
summary_lines.append("product: fitxpress")
summary_lines.append("campaign: 2026-07-21-eu-telehealth-weightloss")
summary_lines.append("profile: olena")
summary_lines.append(f"total_contacts_messaged: {len(records)}")
summary_lines.append("---\n")
summary_lines.append("# Message Sequencing Summary — 2026-07-21-eu-telehealth-weightloss\n")
summary_lines.append(
    "**Spec note:** generated on the CURRENT 2-message, note-less sequence "
    "(message-sequencer.md / outbound-message1-template.md / outbound-message2-template.md), "
    "not the legacy 4-step sequence, because the legacy format was deprecated today per CLAUDE.md "
    "and no explicit override was confirmed. GDPR/compliance line folded into Message 2. "
    "PASS/WEAK distinction preserved as 15-min vs 10-min CTA wording in Message 2.\n"
)
summary_lines.append(f"## Totals\n- Total contacts messaged: **{len(records)}**")
for k in ["PASS_P1", "PASS_P2", "PASS_P3", "WEAK"]:
    summary_lines.append(f"- {k}: {class_counts.get(k, 0)}")
summary_lines.append("\n## Angle distribution")
for k, v in angle_counts.most_common():
    summary_lines.append(f"- {k}: {v}")

summary_lines.append("\n## Breakdown by company")
summary_lines.append("| Company | Contacts | PASS | WEAK |")
summary_lines.append("|---|---|---|---|")
for company, recs in sorted(by_company.items(), key=lambda kv: -len(kv[1])):
    p = sum(1 for r in recs if r["classification"].startswith("PASS"))
    w = sum(1 for r in recs if r["classification"] == "WEAK")
    summary_lines.append(f"| {company} | {len(recs)} | {p} | {w} |")

summary_lines.append(f"\n## Character limit compliance\n- Message 1 max observed: {max(r['len1'] for r in records)} / 600")
summary_lines.append(f"- Message 2 max observed: {max(r['len2'] for r in records)} / 550")
summary_lines.append(f"- Warnings: {len(warnings)}")
if warnings:
    summary_lines.append("\n### Warnings detail")
    for w in warnings:
        summary_lines.append(f"- {w}")

summary_lines.append("\n## Sample (first 3 records)")
for r in records[:3]:
    summary_lines.append(f"\n### {r['full_name']} — {r['company']} ({r['classification']}, angle={r['angle']})")
    summary_lines.append(f"**Message 1** ({r['len1']} chars):\n```\n{r['message_1']}\n```")
    summary_lines.append(f"**Message 2** ({r['len2']} chars):\n```\n{r['message_2']}\n```")

with open(os.path.join(MSG_DIR, "_summary.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(summary_lines) + "\n")

print("SUMMARY_WRITTEN=" + os.path.join(MSG_DIR, "_summary.md"))
print("BY_COMPANY_COUNT=" + str(len(by_company)))
