#!/usr/bin/env python3
"""Match a Style DNA vector against the design-atelier atlas.

Reads the YAML front matter of every card in atlas/**/<id>.md, then ranks
cards by how they relate to a target vector:

  kin       — closest sensibilities (reinforce the person's taste)
  tension   — agree on most axes, diverge sharply on 2-3 (where novelty lives)
  far       — distant on most axes (use only as a single deliberate gene)

Usage:
  atlas_match.py --vector "order=8,density=3,ornament=2,warmth=6,contrast=7,geometry=8,chroma=3,typevoice=6,energy=4,hand=3,play=4,era=6"
  atlas_match.py --profile ~/.design-atelier/profiles/ilduza/dna.md
  atlas_match.py --vector ... --section graphic,art --topic music --top 8
  atlas_match.py --index            # print a compact index of the whole atlas
  atlas_match.py --check            # validate cards: axes, ids, dangling refs
  atlas_match.py --vector ... --vary --seed 7     # sample from a wider pool instead of the same top cards
  atlas_match.py --record josef-albers,carlo-scarpa   # log sources used in a blend (down-ranked next time)
  atlas_match.py --genes saul-bass,luis-barragan      # print only essence + genes + don't-copy (saves reading whole cards)

Sources recorded in ~/.design-atelier/recent-sources.json (last 40) are pushed
to the end of every list, so the same masters don't become a house default.

No third-party dependencies.
"""

import argparse
import datetime
import json
import math
import random
import re
import sys
from pathlib import Path

AXES = ["order", "density", "ornament", "warmth", "contrast", "geometry",
        "chroma", "typevoice", "energy", "hand", "play", "era"]

ROOT = Path(__file__).resolve().parent.parent
RECENT = Path.home() / ".design-atelier" / "recent-sources.json"
ATLAS = ROOT / "atlas"


def parse_front_matter(text):
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return None
    fm = {}
    block = m.group(1)
    for key in ("id", "name", "type", "era", "origin"):
        km = re.search(rf"^{key}:\s*(.+?)\s*(#.*)?$", block, re.M)
        if km:
            fm[key] = km.group(1).strip().strip('"\'')
    for key in ("discipline", "lineage", "mood", "topics"):
        km = re.search(rf"^\s*{key}:\s*\[(.*?)\]", block, re.M)
        fm[key] = [s.strip().strip('"\'') for s in km.group(1).split(",") if s.strip()] if km else []
    am = re.search(r"^axes:\s*\{(.*?)\}", block, re.M)
    if am:
        pairs = dict(
            (k.strip(), v.strip()) for k, v in
            (p.split(":", 1) for p in am.group(1).split(",") if ":" in p)
        )
        try:
            fm["axes"] = [float(pairs[a]) for a in AXES]
        except (KeyError, ValueError):
            fm["axes_error"] = "missing or non-numeric axis"
    sm = re.search(r"^saturation:\s*(\d+)", block, re.M)
    if sm:
        fm["saturation"] = int(sm.group(1))
    return fm


def load_atlas():
    cards = []
    for path in sorted(ATLAS.rglob("*.md")):
        if path.name.startswith("_") or "_sources" in path.parts:
            continue
        fm = parse_front_matter(path.read_text(encoding="utf-8"))
        if fm is None:
            continue
        fm["section"] = path.parent.name
        fm["path"] = str(path.relative_to(ROOT))
        cards.append(fm)
    return cards


def parse_vector(s):
    vals = dict(p.split("=") for p in s.replace(" ", "").split(","))
    return [float(vals[a]) for a in AXES]


def vector_from_profile(path):
    text = Path(path).expanduser().read_text(encoding="utf-8")
    fm = parse_front_matter(text) or {}
    if "axes" not in fm:
        sys.exit(f"No axes: {{...}} map in front matter of {path}")
    return fm["axes"]


def dist(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def tension_score(a, b):
    """High when most axes agree but 2-3 diverge strongly.

    Cards that also disagree on the remaining axes (any of them by 4+) are
    pushed to the bottom: that is distance, not tension.
    """
    diffs = sorted((abs(x - y) for x, y in zip(a, b)), reverse=True)
    sharp = sum(diffs[:3])
    rest = diffs[3:]
    score = sharp - 2.0 * sum(rest)
    if rest and rest[0] >= 4:
        score -= 100
    return score


def fmt_axes(v):
    return " ".join(f"{a[:3]}{int(x)}" for a, x in zip(AXES, v))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--vector")
    ap.add_argument("--profile")
    ap.add_argument("--section", help="comma list: graphic,product,ui,ux,art,architecture,cultures,trends,type")
    ap.add_argument("--topic", help="substring matched against topics/mood tags")
    ap.add_argument("--top", type=int, default=6)
    ap.add_argument("--include-trends", action="store_true", help="trends are excluded from matching by default")
    ap.add_argument("--include-cultures", action="store_true", help="cultures only when the user asked for cultural mixing")
    ap.add_argument("--vary", action="store_true", help="sample each list from a 3x wider pool")
    ap.add_argument("--seed", type=int, help="random seed for --vary (omit for a fresh draw)")
    ap.add_argument("--recent", type=Path, default=RECENT, help="recently used sources file")
    ap.add_argument("--record", help="comma list of ids used in a finished blend; appends to --recent and exits")
    ap.add_argument("--genes", help="comma list of ids: print essence, genes table and don't-copy only")
    ap.add_argument("--index", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    if args.record:
        data = []
        if args.recent.exists():
            try:
                data = json.loads(args.recent.read_text())
            except json.JSONDecodeError:
                data = []
        today = datetime.date.today().isoformat()
        data += [{"id": i.strip(), "date": today} for i in args.record.split(",") if i.strip()]
        args.recent.parent.mkdir(parents=True, exist_ok=True)
        args.recent.write_text(json.dumps(data[-40:], indent=1))
        print(f"recorded {args.record} → {args.recent}")
        return

    cards = load_atlas()

    if args.genes:
        by_id = {c.get("id"): c for c in cards}
        for cid in [i.strip() for i in args.genes.split(",") if i.strip()]:
            c = by_id.get(cid)
            if not c:
                print(f"## {cid}: not found\n"); continue
            text = (ROOT / c["path"]).read_text(encoding="utf-8")
            body = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)
            ess = re.search(r"^\*\*Essence:\*\*.*$", body, re.M)
            genes = re.search(r"^## Genes\n(.*?)(?=^## )", body, re.S | re.M)
            dont = re.search(r"^## Don't copy\n(.*?)(?=^## |\Z)", body, re.S | re.M)
            print(f"## {c.get('name', cid)} ({cid}, {c['section']}, {c.get('era', '')})")
            if ess: print(ess.group(0))
            if genes: print(genes.group(1).strip())
            if dont: print("Don't copy: " + " ".join(dont.group(1).split()))
            print()
        return

    if args.check:
        ids = {c.get("id") for c in cards}
        problems = 0
        seen = {}
        for c in cards:
            cid = c.get("id")
            if not cid:
                print(f"NO ID      {c['path']}"); problems += 1; continue
            if Path(c["path"]).stem != cid:
                print(f"ID≠FILE    {c['path']} (id: {cid})"); problems += 1
            if cid in seen:
                print(f"DUPLICATE  {cid}: {seen[cid]} & {c['path']}"); problems += 1
            seen[cid] = c["path"]
            if "axes" not in c:
                print(f"AXES       {c['path']} {c.get('axes_error', 'missing')}"); problems += 1
            elif any(not 0 <= x <= 10 for x in c["axes"]):
                print(f"RANGE      {c['path']}"); problems += 1
            for ref in c.get("lineage", []):
                if ref and ref not in ids:
                    print(f"DANGLING   {cid} lineage → {ref}")
        print(f"\n{len(cards)} cards, {problems} hard problems")
        sys.exit(1 if problems else 0)

    if args.index:
        by = {}
        for c in cards:
            by.setdefault(c["section"], []).append(c)
        for sec in sorted(by):
            print(f"\n## {sec} ({len(by[sec])})")
            for c in by[sec]:
                sat = f" sat{c['saturation']}" if "saturation" in c else ""
                ax = fmt_axes(c["axes"]) if "axes" in c else "—"
                print(f"- {c['id']} · {c.get('name','')} · {c.get('era','')} · {', '.join(c.get('mood', []))}{sat} · [{ax}]")
        return

    if args.profile:
        target = vector_from_profile(args.profile)
    elif args.vector:
        target = parse_vector(args.vector)
    else:
        ap.error("give --vector, --profile, --index or --check")

    pool = [c for c in cards if "axes" in c]
    if args.section:
        secs = set(args.section.split(","))
        pool = [c for c in pool if c["section"] in secs]
    else:
        if not args.include_trends:
            pool = [c for c in pool if c["section"] != "trends"]
        if not args.include_cultures:
            pool = [c for c in pool if c["section"] != "cultures"]
        # typefaces are matched separately (--section type) so they don't crowd out masters
        pool = [c for c in pool if c["section"] != "type"]
    if args.topic:
        t = args.topic.lower()
        pool = [c for c in pool if any(t in x.lower() for x in c.get("topics", []) + c.get("mood", []))] or pool

    recent = set()
    if args.recent.exists():
        try:
            recent = {r["id"] for r in json.loads(args.recent.read_text())}
        except (json.JSONDecodeError, KeyError, TypeError):
            recent = set()
    rng = random.Random(args.seed)

    def pick(ranked, n):
        """Fresh sources first; recently used ones sink. --vary samples from a wider pool."""
        fresh = [c for c in ranked if c["id"] not in recent]
        used = [c for c in ranked if c["id"] in recent]
        ordered = fresh + used
        if args.vary:
            pool_n = ordered[: n * 3]
            return rng.sample(pool_n, min(n, len(pool_n)))
        return ordered[:n]

    def row(c, extra):
        mark = "  (recently used)" if c["id"] in recent else ""
        return f"  {c['id']:<34} {c['section']:<13} {extra}  [{fmt_axes(c['axes'])}]{mark}"

    print(f"target: [{fmt_axes(target)}]" + (f"  · {len(recent)} recently used sources down-ranked" if recent else "") + "\n")
    print("KIN — reinforce the taste")
    for c in pick(sorted(pool, key=lambda c: dist(target, c["axes"])), args.top):
        print(row(c, f"d={dist(target, c['axes']):4.1f}"))
    print("\nTENSION — agree mostly, diverge on 2-3 axes (novelty source)")
    for c in pick(sorted(pool, key=lambda c: -tension_score(target, c["axes"])), args.top):
        diffs = sorted(((abs(x - y), a) for a, x, y in zip(AXES, target, c["axes"])), reverse=True)[:3]
        print(row(c, "Δ " + ",".join(f"{a}{'+' if c['axes'][AXES.index(a)] > target[AXES.index(a)] else '-'}" for _, a in diffs)))
    print("\nFAR — single deliberate gene only")
    for c in pick(sorted(pool, key=lambda c: -dist(target, c["axes"])), max(3, args.top // 2)):
        print(row(c, f"d={dist(target, c['axes']):4.1f}"))

    trends = [c for c in cards if c["section"] == "trends" and "axes" in c]
    near = [c for c in trends if dist(target, c["axes"]) < 6]
    if near:
        print("\nWARNING — target sits near saturated trends:")
        for c in sorted(near, key=lambda c: dist(target, c["axes"])):
            print(row(c, f"d={dist(target, c['axes']):4.1f} sat{c.get('saturation', '?')}"))


if __name__ == "__main__":
    main()
