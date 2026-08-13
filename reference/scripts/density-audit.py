#!/usr/bin/env python3
"""Density audit — per-h2 AR/EN char ratios validating recorded ratio exceptions.

Canonical measure (same as verify-twins.py): pre-stripped, tag-stripped text.
A section whose ratio drops far below the doc mean (< 0.45 or > 1.6) is a
prose-abbreviation candidate — eyeball ONLY those sections, never the whole doc.
Numbers, code spans, and Latin tokens legitimately compress AR prose; the flag
threshold is deliberately loose (0.45) — the doc-level band is 0.75-0.97.

Usage: density-audit.py <en.html> <ar.html>
"""
import re, sys

def sections(path):
    t = open(path, encoding='utf-8').read()
    heads = list(re.finditer(r'<h2\b', t))
    out = []
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(t)
        body = re.sub(r'<pre.*?</pre>', '', t[m.start():end], flags=re.S)
        text = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', body)).strip()
        title = re.sub(r'<[^>]+>', '', body[:200]).strip()[:44]
        out.append((title, len(text)))
    return out

if len(sys.argv) != 3:
    print('usage: density-audit.py <en.html> <ar.html>'); sys.exit(1)

en, ar = sections(sys.argv[1]), sections(sys.argv[2])
print('per-h2 AR/EN char ratios (canonical: pre-stripped, tag-stripped)')
print('%-6s %7s %7s  %s' % ('ratio', 'AR', 'EN', 'section'))
outliers = []
for (et, en_n), (at, ar_n) in zip(en, ar):
    r = ar_n / en_n if en_n else 0.0
    flag = ''
    if r < 0.45:
        flag = '   <<< ABBREVIATION CANDIDATE'
        outliers.append(at)
    elif r > 1.6:
        flag = '   <<< EXPANSION CANDIDATE'
    print('%-6.2f %7d %7d  %s%s' % (r, ar_n, en_n, at, flag))
print()
print('sections: %d | outliers: %d' % (len(en), len(outliers)))
if outliers:
    print('eyeball ONLY: %s' % '; '.join(outliers))