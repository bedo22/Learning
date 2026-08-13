#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Section-level splice/rebuild tool for reference-shelf twins.

Rebuild a doc from a manifest: keep source sections by ordinal (optionally
retitled / demoted h2→h3), insert standalone section files, drop sections
ONLY when explicitly listed. Output is byte-exact by construction:

    output = page_head + concatenated sections + page_tail

Head/tail (doctype…first <h2> / last </h2>…EOF) are never touched, so the
v20 failure class — a hand-splice silently dropping the pre-h2 header
prefix — is impossible here. Pre blocks are masked before every h2 scan:
phantom <h2>s inside code samples never split a section (v16 lesson).

Manifest (maps/<doc>.json style, or /tmp for rebuilds):
  {
    "sections": [
      {"ordinal": 0},                         # keep source h2 #0 verbatim
      {"ordinal": 7, "retitle": "…"},         # keep body, swap h2 text
      {"ordinal": 6, "demote": true},         # h2→h3, text kept (AR-only
                                              #   content, e.g. v20 serverless)
      {"ordinal": 3, "retitle": "…", "demote": true},
      {"file": "/tmp/ar-c2h-3b.html"}         # standalone section, exactly
    ],                                        #   one <h2>…</h2> inside
    "drop": [17, 18]                          # ordinals intentionally omitted
  }

Checks (fail loudly, exit 1): every ordinal unique and in range; every
source section kept or explicitly dropped; every file exists and holds
exactly one h2; no <h2> in head or tail (post-mask); optional
--expect N against the final visible h2 count.

Usage: python3 splice-sections.py <src.html> <out.html> <manifest.json> [--expect N]
Run on a WORK COPY, then: twin-pipeline.py (copy) → verify-twins.py → install.
Splice is assembly, not hygiene — the pipeline remains the hygiene pass.
Do not hand-roll this in a session — extend THIS file.
"""
import re, sys, json

SRC, OUT, MANIF = sys.argv[1], sys.argv[2], sys.argv[3]
EXPECT = int(sys.argv[sys.argv.index('--expect') + 1]) if '--expect' in sys.argv else None
assert SRC != OUT, 'in-place splice is forbidden — write to a work copy'

PRE = re.compile(r'<pre[^>]*>.*?</pre\s*>', re.S)
H2O = re.compile(r'<h2\b')
H2C = re.compile(r'</h2\s*>')
H2P = re.compile(r'<h2\b([^>]*)>(.*?)(</h2\s*>)', re.S)

store = []  # pre-mask payloads, restored by marker index

def mask_pres(t):
    def rep(m):
        store.append(m.group(0))
        return '§PHS§%d§EHS§' % (len(store) - 1)
    return PRE.sub(rep, t)

def restore(t):
    return re.sub(r'§PHS§(\d+)§EHS§', lambda m: store[int(m.group(1))], t)

def count_h2(t):
    return len(H2O.findall(mask_pres(t)))

def keep(part, op):
    if op.get('retitle'):
        part = H2P.sub(lambda m: '<h2%s>%s%s' % (m.group(1), op['retitle'], m.group(3)),
                       part, count=1)   # rebuild the full open tag — group(1) is
                                         # only the attrs; the bare-tag form is
                                         # <h2>, not <h2> without brackets (v-sk5
                                         # retitle bug: retitled h2s vanished)
    if op.get('demote'):
        part = H2P.sub(lambda m: '<h3%s>%s</h3>' % (m.group(1), m.group(2)), part, count=1)
    return part

# ---- partition source: head / sections / tail (pres masked first) ----
src = open(SRC, encoding='utf-8').read()
masked = mask_pres(src)
first = H2O.search(masked)
closers = list(H2C.finditer(masked))
assert first, 'source has no <h2>'
assert closers, 'source has unbalanced <h2> (no closer)'
head = masked[:first.start()]
mid = masked[first.start():closers[-1].end()]
tail = masked[closers[-1].end():]
assert '<h2' not in head, 'stray <h2> before first section'
assert '<h2' not in tail, 'stray <h2> after last section (template/footer?)'
sections = re.split(r'(?=<h2\b)', mid)
if not sections[0]: sections = sections[1:]   # zero-width split at start yields ''
assert sections[0].startswith('<h2'), 'mid does not start with an h2'

cfg = json.load(open(MANIF, encoding='utf-8'))
ops = cfg['sections']
drop = set(cfg.get('drop', []))

# ---- validate manifest ----
ords = [o['ordinal'] for o in ops if 'ordinal' in o]
assert len(ords) == len(set(ords)), 'duplicate ordinals: %s' % [
    x for x in set(ords) if ords.count(x) > 1][:5]
assert all(0 <= o < len(sections) for o in ords), 'ordinal out of range'
assert ords and not set(ords) & drop, 'ordinal both kept and dropped: %s' % sorted(set(ords) & drop)
assert all(isinstance(d, int) and 0 <= d < len(sections) for d in drop), \
    'drop out of range: %s' % drop
missing = set(range(len(sections))) - set(ords)
assert missing == drop, \
    'sections omitted without explicit drop: %s (add them or list in "drop")' % sorted(missing)
for o in ops:
    assert 'ordinal' in o or 'file' in o, 'op has neither ordinal nor file: %r' % o

# ---- assemble ----
out_parts, n_ret, n_dem, n_ins = [], 0, 0, 0
for o in ops:
    if 'ordinal' in o:
        part = sections[o['ordinal']]
        n_ret += 1 if o.get('retitle') else 0
        n_dem += 1 if o.get('demote') else 0
        out_parts.append(keep(part, o))
    else:
        body = open(o['file'], encoding='utf-8').read()
        assert count_h2(body) == 1, 'insert file has %d h2s (want 1): %s' % (
            count_h2(body), o['file'])
        out_parts.append(body)
        n_ins += 1

out = restore(head + ''.join(out_parts) + tail)   # restore once over the whole
                                                      # concat — kept parts carry
                                                      # pre-mask markers (v-sk5)
n_h2 = count_h2(out)
if EXPECT is not None:
    assert n_h2 == EXPECT, 'final visible h2 count %d != --expect %d' % (n_h2, EXPECT)
open(OUT, 'w', encoding='utf-8').write(out)
print('SPLICE REPORT: kept %d (retitled %d, demoted %d), inserted %d, dropped %d, '
      'visible h2s %d%s%s' % (len(out_parts) - n_ins, n_ret, n_dem, n_ins,
                              len(sections) - len(ords), n_h2,
                              ' / expect %d' % EXPECT if EXPECT else '',
                              ''))
print('written OK:', OUT)