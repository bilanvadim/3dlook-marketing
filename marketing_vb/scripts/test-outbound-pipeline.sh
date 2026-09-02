#!/usr/bin/env bash
# test-outbound-pipeline.sh — regression suite for the 2026-09-02 outbound hardening.
#
# WHY THIS FILE EXISTS
# Same argument as test-pipeline-changes.sh: a check worth running is one a script runs.
# The outbound changes are gates, and a gate whose exit code nobody re-verifies is a gate
# that will quietly start passing everything.
#
# WHAT IT COVERS
#   search-health.py     blind backend, unreachable backend, healthy backend
#   web-verify.py        verified-live vs blocked classification
#   outbound-pipeline.py hypothesis-gate (approved / draft / scope-drift / prose-edit)
#                        validate-companies (aligned vs drifted)
#                        extract-people (dry-run, clobber guard)
#                        check-import (identity, legacy schema, copy caps, em dash)
#                        check-responses (missing / good / wrong-ids / wrong-schema)
#                        fix-validated
#   existing tooling     agent copies, linkedin briefs, registry status still work
#
# TWO THINGS ARE DELIBERATELY STUBBED, NOT LIVE
#   1. The healthy search backend. The real SearXNG flips into blindness roughly hourly —
#      it went blind 03:50, recovered 17:04, was suspended again by 19:00 on 2026-09-02
#      under a dozen probes. Asserting "the backend is up" makes the suite fail for a
#      reason that is not a regression, so the healthy path runs against a local stub.
#   2. Campaign fixtures. Temp campaigns are created and removed, so no live campaign's
#      files are touched. A test run on 2026-09-02 overwrote a shipped campaign's
#      people-raw.csv; never again from here.
#
# USAGE
#     scripts/test-outbound-pipeline.sh
#
# Exit 0 only if every check passes.

set -uo pipefail
cd "$(dirname "$0")/.." || exit 2

S=scripts
CAMP=workspace/outbound/campaigns
UK=$CAMP/2026-09-01-uk-erakulis-similar
AU=$CAMP/2026-07-16-au-telehealth
US=$CAMP/2026-08-07-us-digital-fitness
TMP_CAMPAIGNS=()

pass=0; fail=0

cleanup() {
  for c in "${TMP_CAMPAIGNS[@]:-}"; do
    [ -n "$c" ] && [ -d "$CAMP/$c" ] && python3 -c "
import shutil, sys; shutil.rmtree('$CAMP/$c', ignore_errors=True)"
  done
  [ -n "${STUB_PID:-}" ] && kill "$STUB_PID" 2>/dev/null
  return 0
}
trap cleanup EXIT

check() {  # check <description> <expected-exit> <command...>
  local desc="$1" want="$2"; shift 2
  "$@" >/dev/null 2>&1
  local got=$?
  if [ "$got" = "$want" ]; then
    printf '  ✓ %s\n' "$desc"; pass=$((pass+1))
  else
    printf '  ✗ %s — exit %s, expected %s\n' "$desc" "$got" "$want"; fail=$((fail+1))
  fi
}

grep_check() {  # grep_check <description> <pattern> <command...>
  # Output is captured BEFORE grepping, on purpose. Piping straight into grep under
  # `set -o pipefail` returns the LEFT command's status, and half the commands here
  # legitimately exit 1 (that is what they are being tested for) — so a matched pattern
  # still reported a failure. Two checks failed that way on the first run.
  local desc="$1" pat="$2"; shift 2
  local out
  out=$("$@" 2>&1)
  if printf '%s' "$out" | grep -qE "$pat"; then
    printf '  ✓ %s\n' "$desc"; pass=$((pass+1))
  else
    printf '  ✗ %s — output did not match /%s/\n' "$desc" "$pat"; fail=$((fail+1))
  fi
}

echo "== search-health =="
check "unreachable backend -> 1" 1 python3 $S/search-health.py --url http://127.0.0.1:9999
check "unreachable + --wait gives up -> 1" 1 python3 $S/search-health.py --url http://127.0.0.1:9999 --wait 1

# healthy path against a stub, for the reason in the header
python3 - <<'PY' &
import json, sys
from http.server import BaseHTTPRequestHandler, HTTPServer
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"query": "x",
                           "results": [{"url": "https://e.com", "title": "t"}] * 7,
                           "unresponsive_engines": []}).encode()
        self.send_response(200); self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body))); self.end_headers()
        self.wfile.write(body)
    def log_message(self, *a): pass
try:
    HTTPServer(("127.0.0.1", 8897), H).serve_forever()
except OSError:
    sys.exit(0)
PY
STUB_PID=$!
python3 - <<'PY'
import time, urllib.request
for _ in range(50):
    try:
        urllib.request.urlopen("http://127.0.0.1:8897/search?q=x&format=json", timeout=1).read()
        break
    except Exception:
        time.sleep(0.1)
PY
check "healthy backend (stub) -> 0" 0 python3 $S/search-health.py --url http://127.0.0.1:8897
grep_check "names suspended engines" "Suspended|BLIND|healthy" python3 $S/search-health.py --url http://127.0.0.1:8897

echo "== web-verify =="
check "reachable site -> 0" 0 python3 $S/web-verify.py verify --url https://www.numan.com/
grep_check "extracts a legal registration" "evidence_registered_office +Registered office" \
  python3 $S/web-verify.py verify --url https://www.numan.com/
grep_check "no 'Wales' from the England-and-Wales footer" "evidence_geo +England; London$" \
  python3 $S/web-verify.py verify --url https://www.numan.com/

echo "== hypothesis-gate =="
T=_test-gate; TMP_CAMPAIGNS+=("$T"); mkdir -p "$CAMP/$T"
cp "$UK/hypothesis.md" "$CAMP/$T/hypothesis.md"
check "approved, unstamped -> 0" 0 python3 $S/outbound-pipeline.py hypothesis-gate --campaign $T
check "stamp -> 0" 0 python3 $S/outbound-pipeline.py hypothesis-gate --campaign $T --stamp
check "unchanged after stamp -> 0" 0 python3 $S/outbound-pipeline.py hypothesis-gate --campaign $T
python3 -c "
import pathlib; p = pathlib.Path('$CAMP/$T/hypothesis.md')
p.write_text(p.read_text().replace('## Why plausible', '## Why plausible\n\n(typo fix.)'))"
check "prose edit does NOT invalidate -> 0" 0 python3 $S/outbound-pipeline.py hypothesis-gate --campaign $T
python3 -c "
import pathlib; p = pathlib.Path('$CAMP/$T/hypothesis.md')
p.write_text(p.read_text().replace('## Sub-segment\n', '## Sub-segment\n\nPlus fitness and nutrition apps, any HQ.\n'))"
check "sub-segment change DOES invalidate -> 1" 1 python3 $S/outbound-pipeline.py hypothesis-gate --campaign $T
python3 -c "
import pathlib; p = pathlib.Path('$CAMP/$T/hypothesis.md')
p.write_text(p.read_text().replace('- **Status:** approved', '- **Status:** draft'))"
check "unapproved status -> 1" 1 python3 $S/outbound-pipeline.py hypothesis-gate --campaign $T

echo "== validate-companies =="
check "hypothesis-aligned + verified -> 0" 0 \
  python3 $S/outbound-pipeline.py validate-companies --campaign 2026-09-01-uk-erakulis-similar \
    --in companies-glp1-telehealth-verified.csv
check "drifted list -> 1" 1 \
  python3 $S/outbound-pipeline.py validate-companies --campaign 2026-09-01-uk-erakulis-similar \
    --in _quarantine-2026-09-02/companies-verified.csv
grep_check "routes non-UK rows to their owner" "nick +8" \
  python3 $S/outbound-pipeline.py validate-companies --campaign 2026-09-01-uk-erakulis-similar \
    --in _quarantine-2026-09-02/companies-verified.csv
grep_check "names a missing fit column" "NO FIT COLUMN" \
  python3 $S/outbound-pipeline.py validate-companies --campaign 2026-09-01-uk-erakulis-similar \
    --in companies-glp1-telehealth-verified.csv

echo "== extract-people =="
check "dry-run writes nothing -> 0" 0 \
  python3 $S/outbound-pipeline.py extract-people --campaign 2026-08-07-us-digital-fitness --dry-run
check "refuses to clobber a shipped list -> 1" 1 \
  python3 $S/outbound-pipeline.py extract-people --campaign 2026-08-07-us-digital-fitness
grep_check "slug+alias join keeps >500 of 643" "people kept +5[0-9][0-9]" \
  python3 $S/outbound-pipeline.py extract-people --campaign 2026-08-07-us-digital-fitness --dry-run
grep_check "prints the unmatched companies" "people dropped: their company is not in the shortlist" \
  python3 $S/outbound-pipeline.py extract-people --campaign 2026-08-07-us-digital-fitness --dry-run

echo "== check-import =="
check "AU: blank identity + legacy 4-step -> 1" 1 \
  python3 $S/outbound-pipeline.py check-import --campaign 2026-07-16-au-telehealth
grep_check "AU: reports 253/253 blank" "first_name. is blank in 253/253" \
  python3 $S/outbound-pipeline.py check-import --campaign 2026-07-16-au-telehealth
check "US batch1 (124 sent) -> 0" 0 \
  python3 $S/outbound-pipeline.py check-import --file $US/closelyhq-import-batch1.csv
check "EU (307 sent) -> 0" 0 \
  python3 $S/outbound-pipeline.py check-import --file $CAMP/2026-07-21-eu-telehealth-weightloss/closelyhq-import.csv
check "Israel: 25/215 missing URL -> 1" 1 \
  python3 $S/outbound-pipeline.py check-import --file $CAMP/2026-07-23-israel-telehealth/closelyhq-import.csv
check "UK: one row over the 600-char cap -> 1" 1 \
  python3 $S/outbound-pipeline.py check-import --file $CAMP/2026-07-31-uk-telehealth-digital-health/closelyhq-import.csv
grep_check "header drift is a warning, not a failure" "header drift vs the documented schema" \
  python3 $S/outbound-pipeline.py check-import --file $US/closelyhq-import-batch1.csv

echo "== check-responses =="
# An empty temp campaign, not a live one: this check used to point at
# 2026-08-07-us-digital-fitness, and broke the moment that campaign legitimately got its
# responses-raw.csv. A test must not assert the absence of real work.
E=_test-noresp; TMP_CAMPAIGNS+=("$E"); mkdir -p "$CAMP/$E"
check "absent file -> 2" 2 python3 $S/outbound-pipeline.py check-responses --campaign $E
R=_test-resp; TMP_CAMPAIGNS+=("$R"); mkdir -p "$CAMP/$R"
cp "$AU/people-raw.csv" "$AU/people-validated.csv" "$CAMP/$R/"
python3 - <<PY
import csv, pathlib
t = pathlib.Path("$CAMP/$R")
ids = [r["person_id"] for r in csv.DictReader((t/"people-validated.csv").open(newline="", encoding="utf-8-sig"))][:10]
cols = ["person_id", "response_date", "response_text", "which_message_replied_to"]
def w(rows):
    with (t/"responses-raw.csv").open("w", newline="", encoding="utf-8") as f:
        c = csv.DictWriter(f, fieldnames=cols); c.writeheader(); c.writerows(rows)
w([{"person_id": i, "response_date": "2026-08-20", "response_text": "tell me more",
    "which_message_replied_to": "1"} for i in ids])
PY
check "valid export -> 0" 0 python3 $S/outbound-pipeline.py check-responses --campaign $R
python3 - <<PY
import csv, pathlib
t = pathlib.Path("$CAMP/$R")
cols = ["person_id", "response_date", "response_text", "which_message_replied_to"]
with (t/"responses-raw.csv").open("w", newline="", encoding="utf-8") as f:
    c = csv.DictWriter(f, fieldnames=cols); c.writeheader()
    c.writerows([{"person_id": f"deadbeef{n:04d}", "response_date": "2026-08-20",
                  "response_text": "no", "which_message_replied_to": "1"} for n in range(8)])
PY
check "another campaign's ids -> 1" 1 python3 $S/outbound-pipeline.py check-responses --campaign $R
python3 - <<PY
import csv, pathlib
t = pathlib.Path("$CAMP/$R")
with (t/"responses-raw.csv").open("w", newline="", encoding="utf-8") as f:
    c = csv.DictWriter(f, fieldnames=["Name", "Message", "Date"]); c.writeheader()
    c.writerow({"Name": "A B", "Message": "hi", "Date": "2026-08-20"})
PY
check "raw export with no join column -> 1" 1 python3 $S/outbound-pipeline.py check-responses --campaign $R

echo "== check-classified =="
check "well-formed step-8 output -> 0" 0 \
  python3 $S/outbound-pipeline.py check-classified --campaign 2026-08-07-us-digital-fitness
# the exact defect from the first live run: an unquoted comma shifts every later column
CL=_test-classified; TMP_CAMPAIGNS+=("$CL"); mkdir -p "$CAMP/$CL"
printf 'person_id,full_name,company,response_date,category,confidence,summary\n' > "$CAMP/$CL/responses-classified.csv"
printf 'p1,Assi C,Clalit Health Services (Innovation Center, South District),2026-05-16,question,low,asked what it is\n' >> "$CAMP/$CL/responses-classified.csv"
check "unquoted comma / column shift -> 1" 1 \
  python3 $S/outbound-pipeline.py check-classified --campaign $CL
grep_check "names the extra field as the cause" "one extra field" \
  python3 $S/outbound-pipeline.py check-classified --campaign $CL
printf 'person_id,full_name,company,response_date,category,confidence,summary\n' > "$CAMP/$CL/responses-classified.csv"
printf 'p1,Assi C,Clalit,2026-05-16,2026-05-16T11:41:01,low,x\n' >> "$CAMP/$CL/responses-classified.csv"
check "a timestamp in the category column -> 1" 1 \
  python3 $S/outbound-pipeline.py check-classified --campaign $CL

echo "== fix-validated =="
check "AU re-join -> 0" 0 python3 $S/outbound-pipeline.py fix-validated --campaign 2026-07-16-au-telehealth --overwrite
grep_check "restores all 439" "identity restored +439/439" \
  python3 $S/outbound-pipeline.py fix-validated --campaign 2026-07-16-au-telehealth --overwrite

echo "== remind =="
check "digest prints -> 0" 0 python3 $S/outbound-pipeline.py remind
grep_check "groups campaigns by the ASK" "export replies from closely.io into responses-raw.csv +\[[0-9]+\]" \
  python3 $S/outbound-pipeline.py remind

echo "== closely-pull (against a stub of their private API) =="
# No credentials are needed or used here. The stub answers the shapes read out of their
# web bundle, and forces the two failure modes that matter: one 401 (must refresh) and one
# 429 (must back off). CLOSELY_BASE_URL points the client at it; HOME is faked so the real
# ~/.hermes/.env and token cache are never touched.
STUB_HOME=$(mktemp -d)
mkdir -p "$STUB_HOME/.hermes"
printf 'CLOSELY_EMAIL=test@example.com\nCLOSELY_PASSWORD=stub\n' > "$STUB_HOME/.hermes/.env"
chmod 600 "$STUB_HOME/.hermes/.env"
# The stub gets its OWN directory, not bare /tmp. A python script's own directory goes on
# sys.path[0], and this box has /tmp/bisect.py sitting there (sergiy_prod's, 2026-08-29),
# which SHADOWS the stdlib bisect module — so a stub run from /tmp dies inside `import
# random` with a PermissionError from someone else's debug script. Cost 8 failing checks
# on the first run.
STUB_DIR=$(mktemp -d)
STUB_PY="$STUB_DIR/closely_stub.py"
cat > "$STUB_PY" <<'STUBEOF'
import json, re, threading, urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
S = {"401": False, "429": False}
GOOD, STALE = "good-token", "stale-token"
CAMP = [{"id": 77, "name": "AU telehealth", "status": "active"}]
CONV = [
    {"conversation_id": "c-101", "last_message": "send pricing please",
     "last_message_date": "2026-08-22T14:03:00+03:00", "account_id": 1,
     "account_display_name": "bilanvadim@gmail.com", "archived": False, "unread_count": 1,
     "contact": {"contact_id": 101, "lid": "dani-rutman", "display_name": "Dani Rutman",
                 "job_title": "Head of Health", "email": None, "campaigns": CAMP}},
    {"conversation_id": "c-102", "last_message": "…", "account_id": 1,
     "account_display_name": "bilanvadim@gmail.com", "archived": False, "unread_count": 0,
     "contact": {"contact_id": 102, "lid": "sam-okoro", "display_name": "Sam Okoro",
                 "job_title": "VP Product", "email": None, "campaigns": CAMP}},
    # belongs to NO campaign: a stranger cold-pitching us. 216 of the real 270 look like
    # this, and none of them may reach responses-raw.csv.
    {"conversation_id": "c-103", "last_message": "let me write about you",
     "account_id": 1, "account_display_name": "katerina@3dlook.me", "unread_count": 2,
     "contact": {"contact_id": 103, "lid": "cold-pitcher", "display_name": "Koby Pitch",
                 "job_title": "Founder", "email": None, "campaigns": []}},
]
# drill rows: contact_id, names, lid as a FULL url (unlike the inbox's bare slug)
DRILL = {
    "77": [
        {"contact_id": 101, "first_name": "Dani", "last_name": "Rutman",
         "lid": "https://www.linkedin.com/in/dani-rutman/", "status": "finishedWithReply"},
        {"contact_id": 102, "first_name": "Sam", "last_name": "Okoro",
         "lid": "https://www.linkedin.com/in/sam-okoro/", "status": "finishedWithReply"},
    ],
    "88": [
        {"contact_id": 104, "first_name": "Batch2", "last_name": "Person",
         "lid": "https://www.linkedin.com/in/batch2-person/", "status": "finishedWithReply"},
    ],
}
MSG = {
    "c-101": [{"message_id": "m1", "message": "our opener", "sent_at": "2026-08-18T09:12:00+03:00", "is_incoming": False},
              {"message_id": "m2", "message": "our follow-up", "sent_at": "2026-08-21T09:12:00+03:00", "is_incoming": False},
              {"message_id": "m3", "message": "send pricing please", "sent_at": "2026-08-22T14:03:00+03:00", "is_incoming": True}],
    "c-102": [{"message_id": "m4", "message": "no direction field at all", "sent_at": "2026-08-23T10:00:00+03:00"}],
    "c-103": [{"message_id": "m5", "message": "cold pitch", "sent_at": "2026-08-24T10:00:00+03:00", "is_incoming": True}],
    # the pull addresses conversations by contact_id now
    "101": [{"message_id": "m1", "message": "our opener", "sent_at": "2026-08-18T09:12:00+03:00", "is_incoming": False},
            {"message_id": "m2", "message": "our follow-up", "sent_at": "2026-08-21T09:12:00+03:00", "is_incoming": False},
            {"message_id": "m3", "message": "send pricing please", "sent_at": "2026-08-22T14:03:00+03:00", "is_incoming": True}],
    "102": [{"message_id": "m4", "message": "no direction field at all", "sent_at": "2026-08-23T10:00:00+03:00"}],
    "104": [{"message_id": "m6", "message": "batch two reply", "sent_at": "2026-08-25T10:00:00+03:00", "is_incoming": True}],
}
class H(BaseHTTPRequestHandler):
    def _s(self, c, p):
        b = json.dumps(p).encode(); self.send_response(c)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_POST(self):
        n = int(self.headers.get("Content-Length") or 0)
        body = json.loads(self.rfile.read(n) or b"{}")
        m = re.match(r"^/v1/drill/campaigns/(\d+)/contacts$", self.path)
        if m:
            # the authoritative reply record the pull now reads (data.rows, camelCase
            # status). 103 is a second campaign so the multi-id path is covered.
            if self.headers.get("Authorization") != "Bearer " + GOOD:
                S["401"] = True; return self._s(401, {"error": "Unauthorized"})
            if body.get("statuses") != ["finishedWithReply"]:
                return self._s(400, {"error": "invalidStatus"})
            rows = DRILL.get(m.group(1), [])
            return self._s(200, {"success": True, "error": None,
                                 "data": {"total_count": len(rows), "rows": rows}})
        if self.path == "/v1/login/check":
            return self._s(200, {"token": STALE, "refresh_token": "rt"}) if body.get("email") \
                else self._s(400, {"error": "no creds"})
        if self.path == "/v1/login/refresh":
            return self._s(200, {"token": GOOD, "refresh_token": "rt"}) if body.get("refresh_token") == "rt" \
                else self._s(401, {"error": "bad rt"})
        return self._s(404, {})
    def do_GET(self):
        u = urllib.parse.urlparse(self.path); q = urllib.parse.parse_qs(u.query)
        if self.headers.get("Authorization") != "Bearer " + GOOD:
            S["401"] = True; return self._s(401, {"error": "Unauthorized"})
        if u.path == "/v1/inbox/" and not S["429"]:
            S["429"] = True; return self._s(429, {"error": "Too Many Requests"})
        if u.path == "/v1/inbox/":
            if q.get("with_incoming") != ["1"]:
                return self._s(400, {"error": "with_incoming filter missing"})
            o = int(q.get("offset", ["0"])[0]); l = int(q.get("limit", ["15"])[0])
            sel = CONV
            if q.get("campaign_id"):
                want = q["campaign_id"][0]
                sel = [c for c in CONV
                       if any(str(x["id"]) == want for x in c["contact"]["campaigns"])]
            return self._s(200, {"success": True, "error": None,
                                 "data": {"conversations": sel[o:o + l],
                                          "total_count": len(sel)}})
        m = re.match(r"^/v1/inbox/([\w-]+)/messages$", u.path)
        if m:
            return self._s(200, {"success": True, "error": None,
                                 "data": {"conversation_id": m.group(1),
                                          "messages": MSG.get(m.group(1), []),
                                          "total_count": len(MSG.get(m.group(1), []))}})
        if u.path == "/v1/campaigns/":
            return self._s(200, {"success": True, "error": None, "data": {
                "campaigns": [{"campaign_id": 77, "name": "AU telehealth", "status": "active"}],
                "total_count": 1}})
        return self._s(404, {})
    def log_message(self, *a): pass
HTTPServer(("127.0.0.1", 8896), H).serve_forever()
STUBEOF
python3 "$STUB_PY" & STUB2_PID=$!
python3 - <<'WAITEOF'
import time, urllib.request
for _ in range(60):
    try:
        urllib.request.urlopen("http://127.0.0.1:8896/v1/campaigns/", timeout=1)
        break
    except Exception as e:
        if "401" in str(e) or "Unauthorized" in str(e): break
        time.sleep(0.1)
WAITEOF

C=_test-closely; TMP_CAMPAIGNS+=("$C"); mkdir -p "$CAMP/$C"
python3 - <<PYEOF
import csv, pathlib
p = pathlib.Path("$CAMP/$C/people-raw.csv")
with p.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["person_id", "full_name", "person_linkedin_url"])
    w.writeheader()
    w.writerow({"person_id": "abc123def456", "full_name": "Dani Rutman",
                "person_linkedin_url": "https://www.linkedin.com/in/dani-rutman/"})
PYEOF

export CLOSELY_BASE_URL=http://127.0.0.1:8896
CL="env HOME=$STUB_HOME CLOSELY_BASE_URL=http://127.0.0.1:8896 python3 $S/closely-pull.py"

check "no credentials -> explains and exits 1" 1 \
  env HOME=$(mktemp -d) CLOSELY_BASE_URL=http://127.0.0.1:8896 python3 $S/closely-pull.py probe
check "probe (login -> 401 refresh -> 429 backoff) -> 0" 0 $CL probe
check "campaigns lists ids -> 0" 0 $CL campaigns
check "pull without a campaign id -> 2" 2 $CL pull --campaign $C --dry-run
check "pull --dry-run -> 0" 0 $CL pull --campaign $C --closely-campaign-id 77 --dry-run
grep_check "reads the drill, not the inbox listing" "authoritative reply record" \
  $CL pull --campaign $C --closely-campaign-id 77 --dry-run
grep_check "counts the step the reply answers" "replies extracted +1" \
  $CL pull --campaign $C --closely-campaign-id 77 --dry-run
grep_check "SKIPS a message of unknown direction" "did not say whether they are inbound" \
  $CL pull --campaign $C --closely-campaign-id 77 --dry-run
grep_check "drops a replier absent from our people files" "dropped 1 reply" \
  $CL pull --campaign $C --closely-campaign-id 77,88 --dry-run
grep_check "aggregates two campaigns onto one folder" "campaign\(s\) 77, 88" \
  $CL pull --campaign $C --closely-campaign-id 77,88 --dry-run
check "pull writes responses-raw.csv -> 0" 0 $CL pull --campaign $C --closely-campaign-id 77
check "refuses to overwrite -> 1" 1 $CL pull --campaign $C --closely-campaign-id 77
check "map-campaigns runs -> 0" 0 $CL map-campaigns
check "the pulled file passes check-responses -> 0" 0 \
  python3 $S/outbound-pipeline.py check-responses --campaign $C
grep_check "joins person_id from the local people file" "1 matched" \
  python3 $S/outbound-pipeline.py check-responses --campaign $C
kill $STUB2_PID 2>/dev/null
rm -rf "$STUB_DIR" "$STUB_HOME"
unset CLOSELY_BASE_URL

echo "== campaign->folder discriminators (pure functions, no API) =="
# Three separate bugs shipped in this logic on 2026-09-02, each one filing a campaign's
# replies under the WRONG folder — the worst failure this pipeline has, because the
# artifacts look right and step 9 then reasons about someone else's campaign.
DISC=$(mktemp -d)
cat > "$DISC/t.py" <<'PYEOF'
import importlib.util, sys
spec = importlib.util.spec_from_file_location(
    "cp", "/home/vadim_prod/3dlook-marketing/marketing_vb/scripts/closely-pull.py")
cp = importlib.util.module_from_spec(spec); spec.loader.exec_module(cp)

FAKE = {
    "au-jul27": [["person_id","first_name","last_name","title","company","linkedin_url",
                  "segment","angle","priority","message_m1","message_m2"]],
    "au-jul16": [["first_name","last_name","company","title","linkedin_url","location",
                  "message_step1","message_step2","message_step3","message_step4"]],
    "israel":   [["first_name","last_name","company","title","message_1","message_2",
                  "campaign_tag","linkedin_url"]],
    "uk":       [["contact_id","first_name","last_name","email_guess","company_name",
                  "job_title","message_m1","message_m2","tag","linkedin_url"]],
    "us":       [["contact_id","first_name","last_name","email_guess","company_name",
                  "job_title","message_m1","message_m2","tag","linkedin_url"]],
}
def src(cols):
    return cp._source_folder(
        {"contact_source": [{"data": {"table": {c: [] for c in cols}}}]}, FAKE)

fails = []
def check(desc, got, want):
    if got != want:
        fails.append(f"{desc}: got {got!r} want {want!r}")

# bug 1 context: a distinctive header must win over contact overlap
check("distinctive header resolves", src(FAKE["au-jul27"][0]), "au-jul27")
check("4-step header resolves", src(FAKE["au-jul16"][0]), "au-jul16")
# bug 2: a SHORT header must not swallow a longer table
check("short header does not capture a longer table",
      src(FAKE["uk"][0]) in ("uk", "us", ""), True)
# bug 3: byte-identical headers must DEFER rather than pick one
check("identical headers defer", src(FAKE["us"][0]), "")
check("unknown header makes no claim", src(["alpha","beta","gamma"]), "")
check("empty contact_source makes no claim",
      cp._source_folder({"contact_source": []}, FAKE), "")
# the date guard's helper
check("shift_days over a month boundary", cp._shift_days("2026-07-05", -10), "2026-06-25")

for f in fails:
    print("   " + f)
sys.exit(1 if fails else 0)
PYEOF
check "mapping discriminators (7 cases)" 0 python3 "$DISC/t.py"
rm -rf "$DISC"

echo "== existing tooling still green =="
check "outbound-registry status" 0 python3 $S/outbound-registry.py status
check "agent copies identical" 0 python3 $S/check-agent-copies.py
check "agent copies match DEV" 0 python3 $S/sync-agent-copies.py --check
check "linkedin briefs match master" 0 python3 $S/split-linkedin-prompts.py --check

echo
echo "-------------------------------------------"
printf '%s passed, %s failed\n' "$pass" "$fail"
[ "$fail" = 0 ] || exit 1
