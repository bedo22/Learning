#!/usr/bin/env bash
# One-command shelf health check: twin gates + digest coverage + link liveness.
# Usage: bash reference/scripts/check.sh   (or ./check.sh)  — run from anywhere.
set -u
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"   # repo root
REF="$ROOT/reference"
fail=0

echo "=== 1/3 Twin gates (EN vs AR) ==="
cd "$REF"
for p in *.html; do
  [ "$p" = "index.html" ] && continue
  stem="${p%.html}"
  [ -f "ar/$p" ] || { echo "SKIP $stem (no AR twin)"; continue; }
  out=$(cd "$ROOT" && python3 reference/scripts/verify-twins.py "$stem" 2>&1 | tail -1)
  case "$out" in
    ALL\ GATES\ PASSED*) echo "PASS $stem" ;;
    *) echo "FAIL $stem"; echo "$out"; fail=1 ;;
  esac
done

echo; echo "=== 2/3 Digest coverage ==="
python3 scripts/digest-coverage.py > /tmp/cov.$$ 2>&1 || fail=1
tail -4 /tmp/cov.$$
rm -f /tmp/cov.$$

echo; echo "=== 3/3 Link liveness ==="
out=$(python3 scripts/verify-links.py 2>&1)
echo "$out" | grep -E "links \(" 
# transient rate-limits (429/503) on flaky hosts are warnings, not failures
if echo "$out" | grep -qE "\[FAIL\]"; then
  echo "$out" | grep "\[FAIL\]"
  if echo "$out" | grep -vE "biorxiv|http 429|http 503" | grep -qE "\[FAIL\]"; then fail=1
  else echo "(only transient rate-limited hosts failing — warning)"; fi
fi

echo; [ $fail -eq 0 ] && echo "ALL CHECKS PASSED ✅" || echo "CHECKS FAILED ❌"
exit $fail
