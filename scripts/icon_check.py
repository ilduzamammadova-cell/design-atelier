#!/usr/bin/env python3
"""Check a folder of SVG icons for production consistency.

Checks every *.svg in the folder:
  - square viewBox on a standard grid (16, 20, 24, 32, 48) and the same grid across the set
  - one stroke width across the whole set (or none, for fill-only sets)
  - monochrome: colors use currentColor (or none) — no hex colors, gradients, opacity/duotone layers
  - --style outline: fill none + one stroke; --style solid: filled shapes, no strokes, no white knockouts
  - no transform attributes, no embedded raster images, no <style>/<script>, no editor junk ids
  - coordinates stay inside the viewBox (with stroke allowance)
  - file name is kebab-case and describes meaning (warns on names like icon-1, vector, group)

Usage:
  icon_check.py path/to/icons/                    # report
  icon_check.py path/to/icons/ --style outline    # also enforce the outline language
  icon_check.py path/to/icons/ --style solid      # also enforce the solid (glyph) language
  icon_check.py path/to/icons/ --strict   # exit 1 on any warning

No third-party dependencies.
"""

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

GRIDS = {16, 20, 24, 32, 48}
SVG_NS = "{http://www.w3.org/2000/svg}"
BAD_NAMES = re.compile(r"^(icon|vector|group|frame|layer|untitled|path|shape)[-_ ]?\d*$", re.I)
NUM = re.compile(r"-?\d*\.?\d+(?:e-?\d+)?", re.I)


def strip(tag):
    return tag.replace(SVG_NS, "")


def check(path, lang=None):
    issues, info = [], {}
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as e:
        return [f"not valid XML: {e}"], info

    vb = root.get("viewBox")
    if not vb:
        issues.append("no viewBox")
    else:
        x, y, w, h = (float(v) for v in vb.replace(",", " ").split())
        info["grid"] = (w, h)
        if w != h:
            issues.append(f"viewBox not square ({w:g}×{h:g})")
        if w not in GRIDS:
            issues.append(f"viewBox {w:g} not on a standard grid {sorted(GRIDS)}")

    strokes, colors = set(), set()
    max_coord = 0.0
    for el in root.iter():
        tag = strip(el.tag)
        if tag in ("image",):
            issues.append("embedded raster <image>")
        if tag in ("linearGradient", "radialGradient", "pattern", "filter"):
            issues.append(f"<{tag}> — icons are flat and monochrome")
        op = el.get("opacity") or el.get("fill-opacity") or el.get("stroke-opacity")
        if op and float(op) < 1:
            issues.append("opacity < 1 (duotone layer) — icons are single-color")
        if tag in ("style", "script"):
            issues.append(f"<{tag}> element — use attributes only")
        if el.get("transform"):
            issues.append(f"transform on <{tag}> — flatten it")
        eid = el.get("id") or ""
        if re.match(r"^(Vector|Group|Frame|Layer|path|Rectangle)[\s_-]?\d*", eid):
            issues.append(f"editor id '{eid}' left in file")
        sw = el.get("stroke-width")
        if sw:
            strokes.add(sw)
        for attr in ("fill", "stroke"):
            v = (el.get(attr) or "").strip()
            if v and v not in ("none", "currentColor", "inherit"):
                colors.add(v)
        style = el.get("style") or ""
        if "fill:#" in style.replace(" ", "") or "stroke:#" in style.replace(" ", ""):
            colors.add("inline style color")
        for attr in ("d", "points", "x", "y", "cx", "cy", "x1", "x2", "y1", "y2", "width", "height", "r"):
            v = el.get(attr)
            if v and tag != "svg":
                for n in NUM.findall(v):
                    try:
                        max_coord = max(max_coord, abs(float(n)))
                    except ValueError:
                        pass

    whites = {c for c in colors if c.lower() in ("#fff", "#ffffff", "white")}
    if whites and lang == "solid":
        issues.append("white shapes used for details — cut them out of the fill (fill-rule evenodd / subtract)")
    if colors:
        issues.append(f"hard-coded colors {sorted(colors)} — use currentColor (one color only)")
    if lang == "outline":
        root_fill = (root.get("fill") or "").strip()
        if root_fill not in ("none",) and not any((e.get("fill") or "") == "none" for e in root.iter()):
            issues.append("outline style: set fill=\"none\" on the root <svg>")
        if not strokes and not root.get("stroke-width"):
            issues.append("outline style: no stroke-width found")
    if lang == "solid":
        if root.get("stroke") not in (None, "none") or strokes:
            issues.append("solid style: remove strokes — build details as cut-outs in the fill")
    if root.get("stroke-width"):
        strokes.add(root.get("stroke-width"))
    info["strokes"] = strokes
    if "grid" in info and max_coord > info["grid"][0] + 2:
        issues.append(f"coordinates up to {max_coord:g} exceed the {info['grid'][0]:g} grid")

    stem = path.stem
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", stem):
        issues.append(f"file name '{stem}' is not kebab-case")
    if BAD_NAMES.match(stem):
        issues.append(f"file name '{stem}' says nothing about meaning")
    return issues, info


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder", type=Path)
    ap.add_argument("--style", choices=["outline", "solid"], help="enforce one icon language")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    files = sorted(args.folder.glob("*.svg"))
    if not files:
        sys.exit(f"No .svg files in {args.folder}")

    total, grids, strokes = 0, Counter(), Counter()
    for f in files:
        issues, info = check(f, args.style)
        if "grid" in info:
            grids[info["grid"][0]] += 1
        for s in info.get("strokes", ()):
            strokes[s] += 1
        if issues:
            total += len(issues)
            print(f"✗ {f.name}")
            for i in issues:
                print(f"    {i}")
        else:
            print(f"✓ {f.name}")

    print()
    if len(grids) > 1:
        total += 1
        print(f"✗ mixed grids across the set: {dict(grids)}")
    if len(strokes) > 1:
        total += 1
        print(f"✗ mixed stroke widths across the set: {dict(strokes)} — one weight per set (per size)")
    print(f"{len(files)} icons · grid {dict(grids)} · stroke {dict(strokes) or 'none (fill set)'} · {total} issue(s)")
    sys.exit(1 if (args.strict and total) else 0)


if __name__ == "__main__":
    main()
