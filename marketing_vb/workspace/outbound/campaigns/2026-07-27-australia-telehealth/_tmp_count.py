import csv
from collections import Counter

path = 'workspace/outbound/campaigns/2026-07-27-australia-telehealth/people-validated-full.csv'
with open(path, newline='', encoding='utf-8') as f:
    r = csv.DictReader(f)
    rows = list(r)

print('total rows', len(rows))
c = Counter(row['decision'].strip() for row in rows)
print(c)
pass_weak = [row for row in rows if row['decision'].strip() in ('PASS', 'WEAK')]
print('PASS+WEAK', len(pass_weak))
print(list(rows[0].keys()))
