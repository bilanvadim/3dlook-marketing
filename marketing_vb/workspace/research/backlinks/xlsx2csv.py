import zipfile, csv, re, os, sys
from xml.etree import ElementTree as ET

NS = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
RNS = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
src, out = sys.argv[1], sys.argv[2]
z = zipfile.ZipFile(src)

# shared strings
shared = []
if 'xl/sharedStrings.xml' in z.namelist():
    for si in ET.fromstring(z.read('xl/sharedStrings.xml')):
        shared.append(''.join(t.text or '' for t in si.iter(NS+'t')))

rels = {}
for rel in ET.fromstring(z.read('xl/_rels/workbook.xml.rels')):
    rels[rel.get('Id')] = 'xl/' + rel.get('Target').lstrip('/').replace('xl/','',1)

wb = ET.fromstring(z.read('xl/workbook.xml'))
sheets = [(s.get('name'), rels[s.get(RNS+'id')]) for s in wb.iter(NS+'sheet')]

def colnum(ref):
    c = re.match(r'([A-Z]+)', ref).group(1)
    n = 0
    for ch in c:
        n = n*26 + (ord(ch)-64)
    return n-1

os.makedirs(out, exist_ok=True)
for name, path in sheets:
    slug = re.sub(r'[^a-z0-9]+','-', name.lower()).strip('-')
    dest = os.path.join(out, slug + '.csv')
    rows_written = 0
    with open(dest, 'w', newline='', encoding='utf-8') as fh:
        w = csv.writer(fh)
        for _, row in ET.iterparse(z.open(path), events=('end',)):
            if row.tag != NS+'row':
                continue
            cells = {}
            for c in row.iter(NS+'c'):
                ref = c.get('r') or ''
                idx = colnum(ref) if ref else len(cells)
                t = c.get('t')
                v = c.find(NS+'v')
                if t == 's' and v is not None:
                    val = shared[int(v.text)]
                elif t == 'inlineStr':
                    is_ = c.find(NS+'is')
                    val = ''.join(x.text or '' for x in is_.iter(NS+'t')) if is_ is not None else ''
                else:
                    val = v.text if v is not None else ''
                cells[idx] = val or ''
            if cells:
                mx = max(cells)
                w.writerow([cells.get(i,'') for i in range(mx+1)])
                rows_written += 1
            row.clear()
    print(f'{name} -> {dest} ({rows_written} rows)')
