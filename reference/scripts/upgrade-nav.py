#!/usr/bin/env python3
"""
Upgrade nav blocks across the shelf.

Improvements:
1. Group EN navs into Close (1-hop) / Also (distant) tiers
2. Add next/prev reading-order links
3. Add evidence-base link to source-heavy docs
4. Add lang-switch to AR navs (AR→EN back link)
5. Cluster glossary nav into topic groups
"""

import re, os, sys
from pathlib import Path

REF = Path(__file__).resolve().parent.parent

# ── Reading order (index.html order) ──
ORDER = [
    "blooms-six-levels-of-thinking",
    "learning-myths",
    "learning-system",
    "orders-of-learning",
    "self-management",
    "memory-techniques",
    "study-advice",
    "rest-and-recovery",
    "productivity-systems",
    "reverse-goal-setting",
    "skill-acquisition",
    "play-as-recovery",
    "motivation-and-self-determination",
    "metacognition-and-calibration",
    "ai-and-learning",
    "note-taking",
    "wanting-vs-liking",
    "planning-and-execution",
    "focus-and-attention",
    "evidence-base",
]

# ── Display names ──
NAMES = {
    "blooms-six-levels-of-thinking": "Bloom's Six Levels",
    "learning-myths": "Learning Myths",
    "learning-system": "The Learning System",
    "orders-of-learning": "Orders of Learning",
    "self-management": "Self-Management",
    "memory-techniques": "Memory Handling",
    "study-advice": "Study Advice",
    "rest-and-recovery": "Rest &amp; Recovery",
    "productivity-systems": "Productivity Systems",
    "reverse-goal-setting": "Reverse Goal Setting",
    "skill-acquisition": "Skill Acquisition",
    "play-as-recovery": "Play as Recovery",
    "motivation-and-self-determination": "Motivation &amp; Self-Determination",
    "metacognition-and-calibration": "Metacognition &amp; Calibration",
    "ai-and-learning": "AI &amp; Learning",
    "note-taking": "Note-taking",
    "wanting-vs-liking": "Wanting vs Liking",
    "planning-and-execution": "Planning &amp; Execution",
    "focus-and-attention": "Focus &amp; Attention",
    "evidence-base": "Evidence Base",
    "learning-to-learn-glossary": "Glossary",
}

# ── Neighbor map: Close = 1-hop, Also = related but distant ──
# Each entry: (close_list, also_list)
NEIGHBORS = {
    "blooms-six-levels-of-thinking": (
        ["learning-system", "orders-of-learning", "learning-myths"],
        ["metacognition-and-calibration", "ai-and-learning", "self-management"],
    ),
    "learning-myths": (
        ["blooms-six-levels-of-thinking", "learning-system", "metacognition-and-calibration"],
        ["study-advice", "ai-and-learning", "memory-techniques", "self-management"],
    ),
    "learning-system": (
        ["orders-of-learning", "memory-techniques", "note-taking", "metacognition-and-calibration"],
        ["study-advice", "ai-and-learning", "blooms-six-levels-of-thinking"],
    ),
    "orders-of-learning": (
        ["learning-system", "blooms-six-levels-of-thinking", "note-taking"],
        ["memory-techniques", "metacognition-and-calibration", "study-advice"],
    ),
    "self-management": (
        ["productivity-systems", "planning-and-execution", "focus-and-attention"],
        ["rest-and-recovery", "motivation-and-self-determination", "reverse-goal-setting"],
    ),
    "memory-techniques": (
        ["learning-system", "note-taking", "study-advice"],
        ["metacognition-and-calibration", "orders-of-learning", "blooms-six-levels-of-thinking"],
    ),
    "study-advice": (
        ["learning-system", "memory-techniques", "note-taking", "metacognition-and-calibration"],
        ["ai-and-learning", "orders-of-learning", "blooms-six-levels-of-thinking", "self-management"],
    ),
    "rest-and-recovery": (
        ["play-as-recovery", "self-management", "productivity-systems"],
        ["learning-system", "memory-techniques", "wanting-vs-liking"],
    ),
    "productivity-systems": (
        ["self-management", "planning-and-execution", "focus-and-attention"],
        ["reverse-goal-setting", "motivation-and-self-determination", "rest-and-recovery", "wanting-vs-liking", "learning-system"],
    ),
    "reverse-goal-setting": (
        ["motivation-and-self-determination", "planning-and-execution"],
        ["productivity-systems", "self-management", "wanting-vs-liking"],
    ),
    "skill-acquisition": (
        ["learning-system", "self-management", "metacognition-and-calibration"],
        ["study-advice", "motivation-and-self-determination"],
    ),
    "play-as-recovery": (
        ["rest-and-recovery", "wanting-vs-liking"],
        ["motivation-and-self-determination", "productivity-systems", "self-management", "study-advice", "memory-techniques", "ai-and-learning"],
    ),
    "motivation-and-self-determination": (
        ["wanting-vs-liking", "reverse-goal-setting", "self-management"],
        ["play-as-recovery", "rest-and-recovery", "productivity-systems", "skill-acquisition"],
    ),
    "metacognition-and-calibration": (
        ["study-advice", "learning-system", "learning-myths"],
        ["ai-and-learning", "motivation-and-self-determination", "wanting-vs-liking", "orders-of-learning"],
    ),
    "ai-and-learning": (
        ["study-advice", "learning-system", "metacognition-and-calibration"],
        ["wanting-vs-liking", "blooms-six-levels-of-thinking", "learning-myths", "play-as-recovery"],
    ),
    "note-taking": (
        ["learning-system", "memory-techniques", "orders-of-learning"],
        ["study-advice", "metacognition-and-calibration"],
    ),
    "wanting-vs-liking": (
        ["play-as-recovery", "motivation-and-self-determination"],
        ["ai-and-learning", "rest-and-recovery", "productivity-systems", "self-management", "metacognition-and-calibration"],
    ),
    "planning-and-execution": (
        ["focus-and-attention", "productivity-systems", "self-management"],
        ["reverse-goal-setting", "motivation-and-self-determination", "rest-and-recovery"],
    ),
    "focus-and-attention": (
        ["planning-and-execution", "productivity-systems"],
        ["self-management", "wanting-vs-liking", "rest-and-recovery", "play-as-recovery", "learning-myths", "metacognition-and-calibration"],
    ),
    "evidence-base": (
        ["learning-to-learn-glossary"],
        ["study-advice", "metacognition-and-calibration", "rest-and-recovery", "play-as-recovery", "wanting-vs-liking", "learning-system"],
    ),
}

# ── Docs that cite sources heavily (get evidence-base link) ──
SOURCE_HEAVY = {
    "play-as-recovery", "rest-and-recovery", "wanting-vs-liking",
    "motivation-and-self-determination", "study-advice", "metacognition-and-calibration",
    "learning-system", "memory-techniques", "ai-and-learning", "learning-myths",
    "blooms-six-levels-of-thinking", "skill-acquisition", "productivity-systems",
    "self-management", "note-taking", "orders-of-learning", "planning-and-execution",
    "focus-and-attention", "reverse-goal-setting",
}

# ── Glossary clusters ──
GLOSSARY_CLUSTERS = {
    "Learning & Memory": [
        "learning-system", "orders-of-learning", "memory-techniques",
        "note-taking", "study-advice", "blooms-six-levels-of-thinking",
    ],
    "Execution & Focus": [
        "self-management", "productivity-systems", "planning-and-execution",
        "focus-and-attention", "skill-acquisition",
    ],
    "Recovery & Motivation": [
        "rest-and-recovery", "play-as-recovery", "wanting-vs-liking",
        "motivation-and-self-determination", "reverse-goal-setting",
    ],
    "Meta & Tools": [
        "metacognition-and-calibration", "ai-and-learning", "learning-myths",
        "evidence-base",
    ],
}


def extract_nav_links(html, is_ar=False):
    """Extract all <a> links from a nav block."""
    # Find nav block
    m = re.search(r'<nav class="ref-nav">(.*?)</nav>', html, re.DOTALL)
    if not m:
        return []
    nav_html = m.group(1)
    links = []
    for a in re.finditer(r'<a href="([^"]*)"[^>]*>(.*?)</a>', nav_html, re.DOTALL):
        href, text = a.group(1), a.group(2).strip()
        # Extract doc stem from href
        stem = None
        if href.endswith('.html'):
            stem = href.replace('.html', '')
            if stem.startswith('../'):
                stem = stem[3:]
            if stem.startswith('ar/'):
                stem = stem[3:]
        links.append((href, text, stem))
    return links


def get_nav_pattern(html):
    """Detect the nav HTML pattern used in this file."""
    m = re.search(r'(<nav class="ref-nav">)(.*?)(</nav>)', html, re.DOTALL)
    if not m:
        return None, None, None
    return m.group(1), m.group(2), m.group(3)


def build_en_nav(stem, existing_links):
    """Build a grouped nav for an EN doc."""
    close_stems, also_stems = NEIGHBORS.get(stem, ([], []))
    should_have_evidence = stem in SOURCE_HEAVY and stem != "evidence-base"

    # Build close links
    close_parts = []
    for s in close_stems:
        name = NAMES.get(s, s)
        close_parts.append(f'<a href="{s}.html">{name}</a>')

    # Build also links
    also_parts = []
    for s in also_stems:
        name = NAMES.get(s, s)
        also_parts.append(f'<a href="{s}.html">{name}</a>')

    # Next/prev
    idx = ORDER.index(stem) if stem in ORDER else -1
    nav_parts = []
    if idx > 0:
        prev_stem = ORDER[idx - 1]
        nav_parts.append(f'<a href="{prev_stem}.html">← {NAMES[prev_stem]}</a>')
    if idx < len(ORDER) - 1:
        next_stem = ORDER[idx + 1]
        nav_parts.append(f'<a href="{next_stem}.html">{NAMES[next_stem]} →</a>')

    # Glossary + evidence-base
    nav_parts.append(f'<a href="learning-to-learn-glossary.html">Glossary</a>')
    if should_have_evidence:
        nav_parts.append(f'<a href="evidence-base.html">Evidence Base</a>')

    # Assemble
    lines = []
    lines.append('<nav class="ref-nav">')
    if close_parts:
        lines.append(f'  <strong>Close</strong> &nbsp;·&nbsp; {" &nbsp;·&nbsp; ".join(close_parts)}')
    if also_parts:
        lines.append(f'  <strong>Also</strong> &nbsp;·&nbsp; {" &nbsp;·&nbsp; ".join(also_parts)}')
    if nav_parts:
        lines.append(f'  {" &nbsp;·&nbsp; ".join(nav_parts)}')
    lines.append('</nav>')
    return '\n'.join(lines)


def build_ar_nav(stem, ar_stems_with_twins):
    """Build a nav for an AR twin with lang-switch."""
    close_stems, also_stems = NEIGHBORS.get(stem, ([], []))

    # Arabic display names
    AR_NAMES = {
        "blooms-six-levels-of-thinking": "مستويات بلوم الستة",
        "learning-myths": "أساطير التعلم",
        "learning-system": "نظام التعلم",
        "orders-of-learning": "مراتب التعلم",
        "self-management": "إدارة الذات",
        "memory-techniques": "الذاكرة",
        "study-advice": "نصائح الدراسة",
        "rest-and-recovery": "الراحة والتعافي",
        "productivity-systems": "أنظمة الإنتاجية",
        "reverse-goal-setting": "تحديد الأهداف العكسي",
        "skill-acquisition": "اكتساب المهارات",
        "play-as-recovery": "اللعب بوصفه تعافيًا",
        "motivation-and-self-determination": "التحفيز وتقرير الذات",
        "metacognition-and-calibration": "ما وراء المعرفة والمعايرة",
        "ai-and-learning": "الذكاء الاصطناعي والتعلم",
        "note-taking": "تدوين الملاحظات",
        "wanting-vs-liking": "الرغبة مقابل الاستمتاع",
        "planning-and-execution": "التخطيط والتنفيذ",
        "focus-and-attention": "التركيز والانتباه",
    }

    close_parts = []
    for s in close_stems:
        name = AR_NAMES.get(s, s)
        # Use ./ for AR twins, ../ for EN-only
        prefix = "./" if s in ar_stems_with_twins else "../"
        close_parts.append(f'<a href="{prefix}{s}.html">← {name}</a>')

    also_parts = []
    for s in also_stems:
        name = AR_NAMES.get(s, s)
        prefix = "./" if s in ar_stems_with_twins else "../"
        also_parts.append(f'<a href="{prefix}{s}.html">← {name}</a>')

    # Lang-switch back to EN
    lang_switch = f'<a href="../{stem}.html">📖 English</a>'

    lines = []
    lines.append('<nav class="ref-nav">')
    if close_parts:
        lines.append(f'  <strong>ذوي الصلة</strong> &nbsp;·&nbsp; {" &nbsp;·&nbsp; ".join(close_parts)}')
    if also_parts:
        lines.append(f'  <strong>أيضًا</strong> &nbsp;·&nbsp; {" &nbsp;·&nbsp; ".join(also_parts)}')
    lines.append(f'  {lang_switch}')
    lines.append('</nav>')
    return '\n'.join(lines)


def build_glossary_nav():
    """Build a clustered glossary nav."""
    lines = ['<nav class="ref-nav">']
    for cluster, stems in GLOSSARY_CLUSTERS.items():
        links = []
        for s in stems:
            name = NAMES.get(s, s)
            links.append(f'<a href="{s}.html">{name}</a>')
        lines.append(f'  <strong>{cluster}</strong> &nbsp;·&nbsp; {" &nbsp;·&nbsp; ".join(links)}')
    lines.append('</nav>')
    return '\n'.join(lines)


def upgrade_en_doc(filepath):
    """Upgrade a single EN doc's nav."""
    html = filepath.read_text(encoding='utf-8')
    if '<nav class="ref-nav">' not in html:
        return False

    stem = filepath.stem
    if stem not in NEIGHBORS:
        return False

    # Extract old nav
    m = re.search(r'(<nav class="ref-nav">)(.*?)(</nav>)', html, re.DOTALL)
    if not m:
        return False

    old_nav = m.group(0)
    new_nav = build_en_nav(stem, extract_nav_links(html))

    html = html.replace(old_nav, new_nav, 1)
    filepath.write_text(html, encoding='utf-8')
    return True


def upgrade_ar_doc(filepath, ar_stems_with_twins):
    """Upgrade a single AR doc's nav."""
    html = filepath.read_text(encoding='utf-8')
    if '<nav class="ref-nav">' not in html:
        return False

    stem = filepath.stem
    if stem not in NEIGHBORS:
        return False

    m = re.search(r'(<nav class="ref-nav">)(.*?)(</nav>)', html, re.DOTALL)
    if not m:
        return False

    old_nav = m.group(0)
    new_nav = build_ar_nav(stem, ar_stems_with_twins)

    html = html.replace(old_nav, new_nav, 1)
    filepath.write_text(html, encoding='utf-8')
    return True


def main():
    # Find AR twins
    ar_dir = REF / "ar"
    ar_stems = set()
    if ar_dir.exists():
        for f in ar_dir.glob("*.html"):
            ar_stems.add(f.stem)

    # Upgrade EN docs
    en_count = 0
    for stem in ORDER:
        fp = REF / f"{stem}.html"
        if fp.exists() and upgrade_en_doc(fp):
            en_count += 1
            print(f"  ✅ EN: {stem}")

    # Upgrade glossary
    glossary = REF / "learning-to-learn-glossary.html"
    if glossary.exists():
        html = glossary.read_text(encoding='utf-8')
        m = re.search(r'(<nav class="ref-nav">)(.*?)(</nav>)', html, re.DOTALL)
        if m:
            old_nav = m.group(0)
            new_nav = build_glossary_nav()
            html = html.replace(old_nav, new_nav, 1)
            glossary.write_text(html, encoding='utf-8')
            print(f"  ✅ EN: glossary (clustered)")
            en_count += 1

    # Upgrade AR docs
    ar_count = 0
    if ar_dir.exists():
        for f in sorted(ar_dir.glob("*.html")):
            if f.stem in NEIGHBORS and upgrade_ar_doc(f, ar_stems):
                ar_count += 1
                print(f"  ✅ AR: {f.stem}")

    # Upgrade index nav
    index = REF / "index.html"
    if index.exists():
        html = index.read_text(encoding='utf-8')
        m = re.search(r'(<nav class="ref-nav">)(.*?)(</nav>)', html, re.DOTALL)
        if m:
            old_nav = m.group(0)
            new_nav = '<nav class="ref-nav">\n<strong>Start here</strong> &nbsp;·&nbsp; <a href="learning-system.html">The Learning System</a> &nbsp;·&nbsp; <a href="learning-to-learn-glossary.html">Glossary</a> &nbsp;·&nbsp; <a href="evidence-base.html">Evidence Base</a>\n</nav>'
            html = html.replace(old_nav, new_nav, 1)
            index.write_text(html, encoding='utf-8')
            print(f"  ✅ EN: index (added evidence-base)")

    print(f"\nDone: {en_count} EN docs + {ar_count} AR twins upgraded")


if __name__ == "__main__":
    main()
