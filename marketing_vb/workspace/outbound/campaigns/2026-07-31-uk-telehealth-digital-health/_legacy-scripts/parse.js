const fs = require('fs');
const text = fs.readFileSync('people-validated-batch2.csv', 'utf8');

function parseCSV(str) {
  const rows = [];
  let row = [];
  let field = '';
  let inQuotes = false;
  for (let i = 0; i < str.length; i++) {
    const c = str[i];
    if (inQuotes) {
      if (c === '"') {
        if (str[i + 1] === '"') { field += '"'; i++; }
        else { inQuotes = false; }
      } else field += c;
    } else {
      if (c === '"') inQuotes = true;
      else if (c === ',') { row.push(field); field = ''; }
      else if (c === '\n') { row.push(field); field = ''; rows.push(row); row = []; }
      else if (c === '\r') { /* skip */ }
      else field += c;
    }
  }
  if (field.length || row.length) { row.push(field); rows.push(row); }
  return rows;
}

const rows = parseCSV(text);
const header = rows[0];
console.log('header', JSON.stringify(header));
console.log('total data rows', rows.length - 1);
const idx = header.indexOf('icp_verdict');
const compIdx = header.indexOf('company_name');
const counts = {};
let weakCount = 0;
const weakByCompany = {};
for (let i = 1; i < rows.length; i++) {
  const r = rows[i];
  if (!r || r.length < header.length) continue;
  const v = r[idx];
  counts[v] = (counts[v] || 0) + 1;
  if (v === 'WEAK') {
    weakCount++;
    const c = r[compIdx];
    weakByCompany[c] = (weakByCompany[c] || 0) + 1;
  }
}
console.log(counts);
console.log('weak', weakCount, weakByCompany);
