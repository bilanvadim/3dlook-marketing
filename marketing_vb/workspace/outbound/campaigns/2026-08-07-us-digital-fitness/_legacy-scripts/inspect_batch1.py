import csv
from collections import Counter

with open('workspace/outbound/campaigns/2026-08-07-us-digital-fitness/people-validated-msg-batch1.csv') as f:
    r = list(csv.DictReader(f))
print(len(r))
print(list(r[0].keys()))
print(Counter(x['icp_verdict'] for x in r))
print(Counter(x['priority'] for x in r))
print(Counter(x['message_angle'] for x in r))
