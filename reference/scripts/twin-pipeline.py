#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Twin hygiene pipeline — the ONE mechanical implementation for reference-shelf twins.

Global conventions (do not re-derive; extend here when a new shape appears):
  - h2/h3 numerals stripped per R_EN / R_AR (Arabic-Indic, ASCII, Latin suffixes).
  - AR suffix letters أ/ب/ج/د/هـ/و map to a/b/c/d/e/f for §-token canonicals.
  - §-tokens are matched WITHOUT a rest capture (a rest capture swallowed whole
    text runs in v17) and must be followed by a boundary char (B) or end.
  - Pre blocks are masked with numbered markers before every h2/§ scan and
    RESTORED afterwards (a mask that dropped content deleted 7 pres in v16).
  - Existing <a>…</a> and <pre>…</pre> are base64-protected before remap so
    §-tokens inside already-linked text are never re-wrapped (html-and-css §5b
    fold, v17).
  - Folds merge §-tokens into existing anchors / make bare cross-doc refs real;
    they are the ONLY hand-edited hygiene artifact and live in the doc's map.
  - `</pre\s*>` tolerance: multi-line closers (`</pre\n >`) are v10-era residue
    (normalize in the doc, hdft v17).
Usage:
  python3 twin-pipeline.py <en.html> <ar.html> <N-visible-h2> [--map maps/<doc>.json] [--strict-folds]
Run from the reference/ dir. End with: python3 verify-twins.py <doc>.
Do not re-implement these steps in a session — extend THIS file.
--strict-folds: any fold matching neither twin is a 0-match → FAIL (exit 1)
  instead of WARN. Use on FRESH installs where every fold must land today;
  omit on re-runs, where already-applied folds legitimately match nothing
  (v21: a phantom trailing space in an AR fold old-string quietly linked
  "حل المشكلات §١٠" to the LOCAL summary id instead of the cross-doc
  Problem-Solving target — strict mode makes that class fail instantly).
"""
import re, os, sys, json, base64 as _b64

EN, AR = sys.argv[1], sys.argv[2]
NH = int(sys.argv[3])
MAPF = sys.argv[sys.argv.index('--map')+1] if '--map' in sys.argv else None

WANT = {}   # canonical number -> local section id
FOLDS = []  # [old, new] exact strings, applied per twin where present
STRICT_FOLDS = '--strict-folds' in sys.argv
if MAPF:
    cfg = json.load(open(MAPF, encoding='utf-8'))
    WANT = cfg.get('WANT', {}); FOLDS = cfg.get('FOLDS', [])
    print('map:', MAPF, '|', len(WANT), 'WANT entries,', len(FOLDS), 'folds')

# ---- global conventions ----
ARF  = {'٠':'0','١':'1','٢':'2','٣':'3','٤':'4','٥':'5','٦':'6','٧':'7','٨':'8','٩':'9'}
ARF2 = {'أ':'a','ب':'b','ج':'c','د':'d','ه':'e','هـ':'e','و':'f'}
R_EN = re.compile(r'^\s*\d+[a-z]?\.\s*')
R_AR = re.compile(r'^\s*(?:[٠-٩]|[0-9])+[أ-يـa-z]*\.\s*')
B = r"(?=[\s<,،).;:؛&§–—‑'\"’‘-]|$)"   # token boundary class: digits followed by non-token char (straight+typographic quotes v-sk7; hyphen last = literal)


def vis(t, tag):
    body = re.sub(r'<pre[^>]*>.*?</pre\s*>', '', t, flags=re.S)
    return re.findall(r'<h%d\b([^>]*)>(.*?)</h%d\s*>' % (tag, tag), body, re.S)

def strip(t, tag, R):
    n = [0]
    def sub(m):
        attr, inner = m.group(1), m.group(2)
        new = R.sub('', inner, count=1)
        if new != inner: n[0] += 1
        return '<h%d%s>%s</h%d>' % (tag, attr, new, tag)
    return re.sub(r'<h%d\b([^>]*)>(.*?)</h%d\s*>' % (tag, tag), sub, t, flags=re.S), n[0]

def b64(s): return _b64.b64encode(s.encode()).decode()
def protect(t):
    t = re.sub(r'<pre[^>]*>.*?</pre\s*>', lambda m: '§PR§' + b64(m.group(0)) + '§RP§', t, flags=re.S)
    t = re.sub(r'<a\b[^>]*>.*?</a>', lambda m: '§AN§' + b64(m.group(0)) + '§NA§', t, flags=re.S)
    return t
def unprotect(t):
    t = re.sub(r'§AN§([A-Za-z0-9+/=]+)§NA§', lambda m: _b64.b64decode(m.group(1)).decode(), t)
    t = re.sub(r'§PR§([A-Za-z0-9+/=]+)§RP§', lambda m: _b64.b64decode(m.group(1)).decode(), t)
    return t

def idpass(t, ids):
    n = [0]; pres = []
    def sub(m):
        n[0] += 1
        attr, inner = m.group(1), m.group(2)
        attr = re.sub(r'\bid="[^"]*"\s*', '', attr).strip()   # never double-wrap ids (v16)
        return '<h2 %s>%s</h2>' % (ids[n[0]-1].strip() + (' '+attr if attr else ''), inner)
    t2 = re.sub(r'<pre[^>]*>.*?</pre\s*>', lambda m: '§PRE§%d§' % (pres.append(m.group(0)) or len(pres)-1), t, flags=re.S)
    t2 = re.sub(r'<h2\b([^>]*)>(.*?)</h2\s*>', sub, t2, flags=re.S)
    for k, blk in enumerate(pres):   # restore masks — never drop pre content (v16)
        t2 = t2.replace('§PRE§%d§' % k, blk)
    return t2, n[0]

def remap(t, pref=''):
    n = [0]
    def sub(m):
        n[0] += 1
        h = WANT.get(m.group(1))
        assert h, 'unmapped §'+m.group(1)
        return '<a href="%s#%s">§%s</a>' % (pref, h, m.group(1))
    return re.sub(r'§(\d+(?:\.\d+)?[a-z]?)' + B, sub, t), n[0]

def remap_ar(t):
    n = [0]
    def sub(m):
        n[0] += 1
        num = m.group(1)
        digits = re.match(r'[٠-٩]+', num).group(0)
        suffix = num[len(digits):]
        canon = ''.join(ARF.get(ch, ch) for ch in digits) + ARF2.get(suffix, suffix)
        h = WANT.get(canon)
        assert h, 'AR unmapped §'+num
        return '<a href="#%s">§%s</a>' % (h, num)
    return re.sub(r'§([٠-٩]+[أ-يـa-z]*)' + B, sub, t), n[0]

# ---- run ----
en = open(EN, encoding='utf-8').read()
ar = open(AR, encoding='utf-8').read()
def norm_pre(t):          # v10-era multi-line closers: `</pre\n >` → `</pre`
    return re.sub(r'</pre\s*>', '</pre>', t)
en, ar = norm_pre(en), norm_pre(ar)
n_strip = 0
for tag in (2, 3):
    en, k = strip(en, tag, R_EN); n_strip += k
    ar, k = strip(ar, tag, R_AR); n_strip += k

en_ids = [a for a, _ in vis(en, 2)]
assert len(en_ids) == NH, (len(en_ids), NH)
ar, n_ids = idpass(ar, en_ids); assert n_ids == NH, n_ids
got = [a for a, _ in vis(ar, 2)]
assert len(set(got)) == NH and got == en_ids, 'AR ids != EN ids'

n_fold = 0
for old, new in FOLDS:
    i_en, i_ar = en.count(old), ar.count(old)
    if i_en + i_ar == 0:
        msg = 'fold matches neither twin: %r' % old[:70]
        if STRICT_FOLDS:
            print('FAIL ' + msg); sys.exit(1)
        print('WARN ' + msg + ' (already applied? typo?)')
    if i_en: en = en.replace(old, new); n_fold += i_en
    if i_ar: ar = ar.replace(old, new); n_fold += i_ar

en, n_remap = remap(protect(en)); en = unprotect(en)
ar, n_remap_ar = remap_ar(protect(ar)); ar = unprotect(ar)

open(EN, 'w', encoding='utf-8').write(en)
open(AR, 'w', encoding='utf-8').write(ar)
print('CHANGE REPORT: stripped %d heading numerals, ids written %d, '
      'folds applied %d, §-tokens remapped EN %d / AR %d' %
      (n_strip, n_ids, n_fold, n_remap, n_remap_ar))
print('written OK:', EN, AR)