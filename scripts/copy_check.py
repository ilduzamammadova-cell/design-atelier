#!/usr/bin/env python3
"""Check user-facing copy for dashes and AI-slop phrasing.

Scans .html, .md and .txt files. For HTML it checks visible text plus the
alt, title, aria-label, placeholder and meta content attributes, and skips
<style>, <script> and <svg> blocks.

Reports, with line numbers:
  DASH   em dash (—), en dash (–), spaced hyphen ( - ), double hyphen (--)
  RANGE  number range written with a hyphen (2-3): write it in words
  SLOP   AI-vocabulary and template phrases (English and Azerbaijani)

Usage:
  copy_check.py page.html [more files...]
  copy_check.py site/ --strict      # exit 1 if any DASH or SLOP hit

No third-party dependencies.
"""

import argparse
import re
import sys
from pathlib import Path

DASHES = [("—", "em dash"), ("–", "en dash"), (" -- ", "double hyphen"), (" - ", "spaced hyphen")]
RANGE = re.compile(r"\b\d+\s?-\s?\d+\b")

SLOP_EN = [
    "unlock", "seamless", "elevate", "effortless", "supercharge", "revolutioniz", "game-changer",
    "cutting-edge", "next-level", "world-class", "all-in-one", "curated", "delve", "tapestry",
    "testament", "vibrant", "pivotal", "crucial", "embark", "immerse", "realm", "transformative",
    "unparalleled", "meticulous", "empower", "synergy", "holistic", "boasts", "serves as",
    "not just", "more than just", "whether you're", "in today's",
]
SLOP_AZ = [
    "inqilabi", "misilsiz", "unikal təcrübə", "möhtəşəm", "heyrətamiz", "sehrli", "unudulmaz",
    "qərq olun", "yeni səviyyəyə", "hər zövqə uyğun", "zövqünüzü oxşa", "mükəmməl seçim",
    "səyahətə çıxın", "əsl sənət əsəri", "ən yüksək keyfiyyət", "təkcə", "nəinki",
]
SLOP = [(w, re.compile(r"(?<!\w)" + re.escape(w), re.I)) for w in SLOP_EN + SLOP_AZ]

ATTRS = re.compile(r'\b(?:alt|title|aria-label|placeholder|content)="([^"]*)"', re.I)


def visible_lines(path):
    text = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix.lower() not in (".html", ".htm"):
        # skip fenced code blocks in markdown
        out, fence = [], False
        for line in text.splitlines():
            if line.strip().startswith("```"):
                fence = not fence
                out.append("")
                continue
            out.append("" if fence else line)
        return out
    # blank out non-visible blocks but keep line count
    def blank(m):
        return "\n" * m.group(0).count("\n")
    text = re.sub(r"<(style|script|svg)\b.*?</\1>", blank, text, flags=re.S | re.I)
    lines = []
    for line in text.splitlines():
        attrs = " ".join(ATTRS.findall(line))
        body = re.sub(r"<[^>]+>", " ", line)
        lines.append((body + " " + attrs).replace("&nbsp;", " "))
    return lines


def check(path):
    hits = []
    for n, line in enumerate(visible_lines(path), 1):
        for ch, name in DASHES:
            if ch in line:
                hits.append((n, "DASH", name, line.strip()))
        for m in RANGE.finditer(line):
            hits.append((n, "RANGE", m.group(0), line.strip()))
        for word, rx in SLOP:
            if rx.search(line):
                hits.append((n, "SLOP", word, line.strip()))
    return hits


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+", type=Path)
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    files = []
    for p in args.paths:
        if p.is_dir():
            files += [f for f in sorted(p.rglob("*")) if f.suffix.lower() in (".html", ".htm", ".md", ".txt")]
        else:
            files.append(p)

    hard = 0
    for f in files:
        hits = check(f)
        if not hits:
            print(f"✓ {f}")
            continue
        print(f"✗ {f}")
        for n, kind, what, line in hits:
            print(f"    {n:>4}  {kind:<5} {what:<16} {line[:90]}")
            if kind in ("DASH", "SLOP"):
                hard += 1
    sys.exit(1 if (args.strict and hard) else 0)


if __name__ == "__main__":
    main()
