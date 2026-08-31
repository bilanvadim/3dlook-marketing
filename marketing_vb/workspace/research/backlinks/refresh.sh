#!/usr/bin/env bash
# Re-pull the Backlink Analysis Report from Google Sheets and regenerate the CSVs.
set -euo pipefail
ID=171n8SVk_MdlKa-1XChbf57LvRuCYtAKWSperfUTdQRg
DIR="$(cd "$(dirname "$0")" && pwd)"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
curl -sSLf -o "$TMP/bl.xlsx" "https://docs.google.com/spreadsheets/d/$ID/export?format=xlsx"
python3 "$DIR/xlsx2csv.py" "$TMP/bl.xlsx" "$DIR"
echo "Refreshed: $DIR"
