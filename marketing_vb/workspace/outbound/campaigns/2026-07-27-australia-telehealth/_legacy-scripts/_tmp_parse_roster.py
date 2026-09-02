import glob, re, collections, csv, os

base = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.join(base, "messages"))

rows = []
for f in sorted(glob.glob("*.md")):
    txt = open(f, encoding="utf-8").read()
    m = re.search(r'to:\s*"(.*?)"\s*\ntitle:\s*"(.*?)"\s*\ncompany:\s*"(.*?)"\s*\nlinkedin:\s*"(.*?)"\s*\nsegment:\s*"(.*?)"', txt)
    if m:
        rows.append((f, m.group(1), m.group(2), m.group(3), m.group(4), m.group(5)))
    else:
        print("NO MATCH", f)

by_company = collections.Counter(r[3] for r in rows)
print("TOTAL:", len(rows))
for c, n in by_company.most_common():
    print(f"{c}: {n}")

with open(os.path.join(base, "_roster_from_messages.csv"), "w", newline="", encoding="utf-8") as out:
    w = csv.writer(out)
    w.writerow(["file", "name", "title", "company", "linkedin", "segment"])
    w.writerows(rows)
