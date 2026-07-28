import csv
from collections import Counter

by_company = Counter()
rows = []
with open('people-validated-full.csv') as f:
    r = csv.DictReader(f)
    for row in r:
        if row['decision'] in ('PASS', 'WEAK'):
            by_company[row['company_name']] += 1
            rows.append(row)

print("TOTAL", len(rows))
print("--- by company ---")
for k, v in by_company.most_common():
    print(v, k)

print("--- sample rows ---")
for row in rows[:3]:
    print(row)
