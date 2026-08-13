#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verify-twins.py — the shelf's deterministic gate battery.

Standalone: runnable on ANY twin pair at ANY time (before every commit, per
AGENTS.md). Run from the reference/ dir:
    python3 verify-twins.py <doc-stem>            (reference/<stem>.html + ar/<stem>.html)
or explicit:  python3 verify-twins.py <en.html> <ar.html> [<doc-stem-for-ratio>]

Output: PASS per check, or FAIL with a specific message. Flag (not fail):
ratio outside band — per-doc exceptions are recorded judgments, not silent skips.
Exit 0 only when every non-flagged check passes.
"""
import re, sys, os

RATIO_BAND = (0.75, 0.97)          # calibrated on cs-and-se 0.75 / react 0.84 / glossary 0.97 (v12)
RATIO_EXCEPTIONS = {                # canonical-measure density judgments (FLAG, not FAIL)
    'version-control-ci-cd-deployment': 0.61,   # FILLED v40 (4 sections rebuilt 1:1); audit 0 outliers;
                                                # residual = uniform style-terseness, audit pending
    'how-developers-think-frontend':    1.17,   # verbose twin style; audited 2026-08-11 — 0 outliers
    'cs-and-software-engineering':      0.98,   # AR grew with v10 factual fixes; audited 2026-08-11 — 0 outliers
    'glossary':                         0.99,   # term-list density; audited 2026-08-11 — 0 outliers
    'problem-solving':                  0.70,   # just under band; audited 2026-08-11 — 0 outliers
    'nextjs-deep-dive':                 0.72,   # v38: code-token-dense EN (JSX/code spans inflate EN length);
                                                # audited 2026-08-11 — 0 outliers
    'income-stream-landscape':        1.01,   # v53: workbook table-expansion class; audited
                                                # 2026-08-12 — 0 outliers, uniform 0.98-1.16
    'class-to-hooks-paradigm-shift':    1.34,   # v22 rebuild: AR §1 preserves legacy 0.x
                                                # depth (65K old-EN foundations as h3s vs
                                                # EN 8.5K) — audited 2026-08-11: 4 expansion
                                                # sections = documented legacy-depth preservation
}

if len(sys.argv) == 2:
    stem = sys.argv[1]
    EN, AR = 'reference/%s.html' % stem, 'reference/ar/%s.html' % stem
    anchor = stem
elif len(sys.argv) >= 3:
    EN, AR = sys.argv[1], sys.argv[2]
    anchor = sys.argv[3] if len(sys.argv) > 3 else os.path.basename(EN).replace('.html', '')
else:
    sys.exit('usage: verify-twins.py <doc-stem> | <en.html> <ar.html> [stem]')

fails, flags = [], []

def chk(name, ok, detail=''):
    if ok is None:
        flags.append((name, detail)); print('  flag ' + name + ((' — ' + str(detail)) if detail else ''))
    elif ok:
        print('PASS  ' + name + ((' — ' + detail) if detail else ''))
    else:
        fails.append((name, detail)); print('FAIL  ' + name + ((' — ' + str(detail)) if detail else ''))

en = open(EN, encoding='utf-8').read()
ar = open(AR, encoding='utf-8').read()

def body(t): return re.sub(r'<pre[^>]*>.*?</pre\s*>', '', t, flags=re.S)
def ids_of(t): return [a for a, _ in re.findall(r'<h2\b([^>]*)>(.*?)</h2\s*>', body(t), re.S)]

# 1. balance
chk('h2 balance', en.count('<h2') == en.count('</h2') and ar.count('<h2') == ar.count('</h2'),
    'EN %d/%d AR %d/%d' % (en.count('<h2'), en.count('</h2'), ar.count('<h2'), ar.count('</h2')))
chk('h3 balance', en.count('<h3') == en.count('</h3') and ar.count('<h3') == ar.count('</h3'))
chk('pre balance', len(re.findall(r'<pre[^>]*>', en)) == len(re.findall(r'</pre\s*>', en))
    and len(re.findall(r'<pre[^>]*>', ar)) == len(re.findall(r'</pre\s*>', ar)))

# 2. h2 parity + ids
ei, ai = ids_of(en), ids_of(ar)
chk('visible h2 parity', len(ei) == len(ai), 'EN %d AR %d' % (len(ei), len(ai)))
chk('ids identical twins', ei == ai, 'EN %d AR %d' % (len(ei), len(ai)))
chk('ids unique', len(set(ei)) == len(ei) and len(set(ai)) == len(ai))

# 3. numeral-free headings (legacy residue guard)
R_EN = re.compile(r'^\s*\d+[a-z]?\.\s*')
R_AR = re.compile(r'^\s*(?:[٠-٩]|[0-9])+[أ-يـa-z]*\.\s*')
def residue(t, R, tag):
    body2 = body(t)
    return sum(1 for a, n in re.findall(r'<h%d\b([^>]*)>(.*?)</h%d\s*>' % (tag, tag), body2, re.S) if R.search(n))
r = residue(en, R_EN, 2) + residue(en, R_EN, 3) + residue(ar, R_AR, 2) + residue(ar, R_AR, 3)
chk('numeral-free headings', r == 0, '%d residue' % r)

# 4. §-tokens: zero outside links (visible text, pre excluded)
def stray(t):
    s = re.sub(r'<a[^>]*>.*?</a>', '', body(t), flags=re.S)
    return sorted(set(re.findall(r'§[\d٠-٩]', s)))
se, sa = stray(en), stray(ar)
chk('zero stray §', not se and not sa, 'EN %s AR %s' % (se, sa))

# 5. anchors
def bad_internal(t):
    return [m.group(1) for m in re.finditer(r'href="#([^"]+)"', t)
            if not re.search(r'id="%s"' % re.escape(m.group(1)), t)]
be, ba = bad_internal(en), bad_internal(ar)
chk('internal anchors resolve', not be and not ba, 'EN %s AR %s' % (be, ba))

def cross_refs(t, prefix):
    out = []
    for m in re.finditer(r'href="(\.\.?/[^"#]+\.html#(sec-[^"]+))"', t):
        fn, an = m.group(1).split('#', 1)
        if fn.startswith('../'):     # AR doc → sibling at reference/ root (EN-only) or ar/
            absf = ('reference/' + fn.replace('../', ''))
        else:                        # './x.html' — same dir as the file being scanned
            absf = 'reference/' + prefix + '/' + fn.lstrip('./')
        ok = os.path.exists(absf) and an in open(absf, encoding='utf-8').read()
        out.append((m.group(1), ok))
    return out
cr = cross_refs(en, '') + cross_refs(ar, 'ar')
chk('cross-doc anchors resolve', all(ok for _, ok in cr), [r for r, ok in cr if not ok][:4])

# 5b. raw sample headings forbidden — `<code><h[1-6]` must be escaped (`&lt;h2&gt;`):
#     raw forms enter the a11y tree as real headings, break pre-stripped counts,
#     and hosted the v10 content-swallowing corruption (v16/v19 repairs).
rsh = sorted(set(re.findall(r'<code><h[1-6][^>]*>', en) + re.findall(r'<code><h[1-6][^>]*>', ar)))
chk('no raw sample headings', not rsh, 'EN+AR %s' % rsh)

# 6. lang-switch lines
chk('lang-switch EN→AR', './ar/%s.html' % anchor in en and 'العربية' in en)
chk('lang-switch AR→EN', '../%s.html' % anchor in ar and 'English' in ar)

# 7. ratio
def text_len(t):
    return len(re.sub(r'<[^>]+>', '', body(t)))
ratio = text_len(ar) / text_len(en)
lo, hi = RATIO_BAND
if lo <= ratio <= hi:
    chk('ratio in band', True, '%.2f' % ratio)
elif anchor in RATIO_EXCEPTIONS:
    chk('ratio out of band', None, '%.2f (recorded exception; density audit pending)' % ratio)
else:
    chk('ratio in band', False, '%.2f ∉ [%.2f, %.2f]' % (ratio, lo, hi))

print()
if flags: print('FLAGS (%d):' % len(flags)); [print('  -', n, '—', str(d)[:110]) for n, d in flags]
if fails:
    print('FAILED (%d):' % len(fails)); [print('  -', n, '—', str(d)[:110]) for n, d in fails]
    sys.exit(1)
print('ALL GATES PASSED —', EN, '+', AR)