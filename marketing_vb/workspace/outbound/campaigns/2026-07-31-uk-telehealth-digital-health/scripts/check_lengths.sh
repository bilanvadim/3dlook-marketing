#!/bin/bash
cd "$(dirname "$0")/../messages-batch2-weak" || exit 1
violations=0
for f in *.md; do
  m1=$(sed -n '/^## Message 1/,/^## Message 2/p' "$f" | sed '1d;$d' | sed '/^$/d')
  m2=$(sed -n '/^## Message 2/,$p' "$f" | sed '1d' | sed '/^$/d')
  l1=$(printf '%s' "$m1" | wc -c)
  l2=$(printf '%s' "$m2" | wc -c)
  if [ "$l1" -gt 550 ] || [ "$l2" -gt 500 ]; then
    echo "VIOLATION: $f M1=$l1 M2=$l2"
    violations=$((violations+1))
  fi
done
echo "Checked $(ls *.md | wc -l) files. Violations: $violations"
