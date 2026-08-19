#!/usr/bin/env python3
"""
link-sources.py — add source-digest links to span.cite blocks.

For every shelf HTML doc, finds span.cite blocks, extracts paper references,
matches them to source digests in sources/, and inserts a compact sources
line after each cite block with links to the matching digests.

Usage:  python3 scripts/link-sources.py [--dry-run]
Run from the reference/ directory.
"""

import html as html_mod
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # reference/
SOURCES_DIR = BASE_DIR / "sources"


def load_source_keys():
    """Load all source digest short-keys (filenames without .md)."""
    keys = []
    for f in sorted(SOURCES_DIR.glob("*.md")):
        if f.name == "_TEMPLATE.md":
            continue
        keys.append(f.stem)
    return keys


def extract_author_surnames(cite_text):
    """
    Extract all plausible author surnames from a cite block's text.
    Returns a set of lowercase surname strings.
    """
    text = html_mod.unescape(cite_text)
    text = re.sub(r'<[^>]+>', '', text)
    surnames = set()
    # Match: Author & Author, Author & Author & Author
    for m in re.finditer(r'([A-Z][a-zé]+)(?:\s*&\s*([A-Z][a-zé]+))+', text):
        for g in m.groups():
            if g:
                surnames.add(g.lower())
    # Match: Author, Author (in list context)
    for m in re.finditer(r'([A-Z][a-zé]+),\s+([A-Z][a-zé]+)', text):
        surnames.add(m.group(1).lower())
        surnames.add(m.group(2).lower())
    # Match: Author et al.
    for m in re.finditer(r'([A-Z][a-zé]+)\s+et\s+al', text):
        surnames.add(m.group(1).lower())
    # Match: standalone Author (YYYY) — look for Name followed by (Year)
    for m in re.finditer(r'([A-Z][a-zé]+)\s*\((\d{4})\)', text):
        name = m.group(1).lower()
        # Filter out common title words that aren't author names
        skip = {'the', 'a', 'an', 'what', 'how', 'why', 'play', 'work', 'rest',
                'recovery', 'mental', 'food', 'liking', 'wanting', 'leisure',
                'self', 'open', 'new', 'can', 'towards', 'toward', 'taste'}
        if name not in skip:
            surnames.add(name)
    return surnames


def match_surnames_to_keys(surnames, source_keys):
    """Match extracted surnames to source digest keys."""
    matched = set()
    for surname in surnames:
        for key in source_keys:
            if surname in key:
                matched.add(key)
    return matched


def process_doc(html_path, source_keys, dry_run=False):
    """Add source-digest links to a single HTML doc."""
    content = html_path.read_text(encoding='utf-8')
    changed = False
    result = []

    # Split into lines for processing
    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]
        result.append(line)

        # Check if this line opens a span.cite
        if 'class="cite"' in line:
            # Collect the full cite block (may span multiple lines)
            cite_lines = [line]
            j = i + 1
            while j < len(lines) and '</span>' not in lines[j-1]:
                cite_lines[j-i-1+1] if j-i-1+1 < len(cite_lines) else cite_lines.append(lines[j])
                j += 1
            # Actually, let's just collect until we find </span>
            cite_text = line
            k = i + 1
            while k < len(lines) and '</span>' not in lines[k-1]:
                cite_text += ' ' + lines[k]
                k += 1

            # Extract references and match to sources
            refs = extract_paper_refs(cite_text)
            matched_keys = match_refs_to_keys(refs, source_keys)

            if matched_keys:
                # Build the sources line
                source_links = []
                for key in sorted(matched_keys):
                    source_links.append(f'<a href="sources/{key}.md">📄</a>')
                sources_line = '      <span class="source-links">Sources: ' + ' '.join(source_links) + '</span>'

                # Find where the cite </span> is and insert after it
                # We need to find the closing </span> of this cite block
                m = i + 1
                while m < len(lines) and '</span>' not in lines[m]:
                    m += 1
                if m < len(lines):
                    # Insert sources line after the closing </span>
                    # But we already appended lines up to this point in result
                    # We need to insert it after the current line's </span>
                    pass

            i += 1
            continue

        i += 1

    # Simpler approach: use regex to find and replace
    return content, changed


def process_doc_v2(html_path, source_keys, dry_run=False):
    """Add source-digest links using regex replacement."""
    content = html_path.read_text(encoding='utf-8')
    original = content

    # Find all span.cite blocks and their content
    # Pattern: <span class="cite"...> ... </span>
    def add_sources_to_cite(match):
        full_match = match.group(0)
        cite_content = match.group(1)

        # Extract references from the cite content
        refs = extract_paper_refs(cite_content)
        matched_keys = match_refs_to_keys(refs, source_keys)

        if not matched_keys:
            return full_match

        # Build sources links
        source_links = []
        for key in sorted(matched_keys):
            source_links.append(f'<a href="sources/{key}.md">📄</a>')

        # Insert sources line before the closing </span>
        sources_html = '\n        Sources: ' + ' '.join(source_links)
        # Replace the last </span> with sources + </span>
        # But we need to be careful - the cite might span multiple lines
        # Insert before the closing </span>
        last_idx = full_match.rfind('</span>')
        if last_idx >= 0:
            return full_match[:last_idx] + sources_html + '\n      ' + full_match[last_idx:]
        return full_match

    # Match span.cite blocks - they can span multiple lines
    # Use a simpler approach: find each <span class="cite" and collect until </span>
    result_parts = []
    pos = 0
    while True:
        idx = content.find('class="cite"', pos)
        if idx == -1:
            result_parts.append(content[pos:])
            break

        # Find the start of the span tag (go back to find <span)
        tag_start = content.rfind('<span', 0, idx)
        if tag_start == -1:
            result_parts.append(content[pos:idx + 12])
            pos = idx + 12
            continue

        # Find the closing </span> (may have whitespace/newline before >)
        close_match = re.search(r'</span\s*>', content[idx:])
        if not close_match:
            result_parts.append(content[pos:])
            break

        tag_end = idx + close_match.end()
        cite_text = content[tag_start:tag_end]

        # Extract author surnames and match to source digests
        surnames = extract_author_surnames(cite_text)
        matched_keys = match_surnames_to_keys(surnames, source_keys)

        result_parts.append(content[pos:tag_start])

        if matched_keys:
            source_links = []
            for key in sorted(matched_keys):
                source_links.append(f'<a href="sources/{key}.md">📄</a>')
            sources_html = ' Sources: ' + ' '.join(source_links)
            # Insert before closing </span...>
            insert_point = cite_text.rfind('</span')
            result_parts.append(cite_text[:insert_point] + sources_html + cite_text[insert_point:])
        else:
            result_parts.append(cite_text)

        pos = tag_end

    new_content = ''.join(result_parts)
    changed = new_content != original

    if changed and not dry_run:
        html_path.write_text(new_content, encoding='utf-8')

    return changed, len(matched_keys) if changed else 0


def main():
    dry_run = '--dry-run' in sys.argv
    source_keys = load_source_keys()
    print(f"Found {len(source_keys)} source digests")

    docs = sorted(BASE_DIR.glob('*.html'))
    total_links = 0
    changed_docs = 0

    for doc in docs:
        changed, count = process_doc_v2(doc, source_keys, dry_run)
        if changed:
            changed_docs += 1
            total_links += count
            print(f"  {'[DRY] ' if dry_run else ''}Updated {doc.name}: {count} source links")

    print(f"\n{'[DRY RUN] ' if dry_run else ''}Updated {changed_docs} docs with {total_links} source-digest links")


if __name__ == '__main__':
    main()
