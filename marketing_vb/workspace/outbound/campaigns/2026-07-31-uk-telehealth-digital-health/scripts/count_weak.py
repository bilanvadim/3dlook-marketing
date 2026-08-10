import csv
from collections import Counter

with open('people-validated-batch2.csv') as f:
    r = csv.DictReader(f)
    rows = list(r)

print('total rows', len(rows))
print(Counter(row['icp_verdict'] for row in rows))
weak = [row for row in rows if row['icp_verdict'] == 'WEAK']
print('weak count', len(weak))
print(Counter(row['company_name'] for row in weak))
