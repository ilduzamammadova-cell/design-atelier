---
id: atomic-design
name: Atomic Design
type: system
discipline: [ui, ux]
era: 2013–present
origin: Pittsburgh, Pennsylvania, USA
lineage: [christopher-alexander]
tags:
  mood: [systematic, modular, consistent, scalable]
  topics: [design systems, web apps, multi-brand products, enterprise, component libraries]
axes: {order: 9, density: 5, ornament: 1, warmth: 4, contrast: 5, geometry: 7, chroma: 4, typevoice: 3, energy: 3, hand: 1, play: 2, era: 6}
---

# Atomic Design

**Essence:** Interfaces are built from a small set of parts composed upward — atoms, molecules, organisms, templates, pages — so design a system of components, not a pile of pages.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Five levels of composition | Brad Frost's chemistry metaphor: atoms (label, input, button) → molecules (search field) → organisms (header) → templates (page structure) → pages (real content) | Library folders mirror the five levels; a component may only import from levels below it; a new organism must be assembled from existing molecules before any new atom is allowed |
| G2 · Systems, not pages | One-off page styling is what makes products drift and rot | Lint rule: no raw hex, px or font values in feature code — only tokens and components; every exception logged as a candidate for the system |
| G3 · Molecules do one job | Small composites with a single responsibility stay reusable and testable | A component API has ≤ 5 variants and ≤ 8 props; if it needs more, split it; names describe purpose ("SearchField"), not appearance ("GreyBox") |
| G4 · Templates show structure, pages stress it | Templates hold the content skeleton; pages fill it with real, extreme content | Every template reviewed with real data at the edges: empty state, one item, 10,000 items, a 60-character name, a right-to-left name, a missing image |
| G5 · The library is alive | The pattern library is the code itself (Frost and Dave Olsen's Pattern Lab), not a PDF that drifts | Each component documented with a live, interactive example of every state (default, hover, focus, disabled, loading, error) generated from production code |
| G6 · Move between scales constantly | The process is non-linear: zoom out to pages, in to atoms, and back | Design reviews alternate: one whole page, then the atoms it revealed as inconsistent; any change to an atom shows its blast radius across pages before merging |

## Visual facts

- **Color:** whatever the brand demands, but expressed as tokens (primitive → semantic → component); consistency is the visible signature.
- **Type:** a single type scale (e.g. 12/14/16/20/24/32/40) consumed only through tokens.
- **Form:** repeated components with identical radii, spacing and states across the product.
- **Composition:** layouts assembled from organisms on a shared grid; no bespoke page compositions.

## Attitude

Frost wrote the methodology as a 2013 blog post, released Pattern Lab with Dave Olsen, and published *Atomic Design* as a book (free to read online). The belief: a design system is a product that serves other products, and the boundaries between designers and developers dissolve when both work in the same components. The chemistry metaphor is a thinking tool, not dogma.

## Blends

- **Amplifies:** `swiss-international`, `gestalt-principles`, `josef-muller-brockmann` — systematic, grid-based consistency.
- **Productive tension with:** `push-pin-studios` — systematic components carrying hand-drawn, illustrative character produce expressive products that still scale.
- **Clashes with:** `art-nouveau` — bespoke, flowing ornament resists modular decomposition; it ends up as image fills on rigid boxes.

## Don't copy

Frost's atomic diagrams and book illustrations and the Pattern Lab branding. Build your own levels and naming.

## Study

- Brad Frost, *Atomic Design* (book, free online): https://atomicdesign.bradfrost.com
- Brad Frost, "Atomic Design" blog post (2013): https://bradfrost.com/blog/post/atomic-web-design/
- Pattern Lab: https://patternlab.io
- Alla Kholmatova, *Design Systems* (Smashing Magazine, 2017)
- Christopher Alexander, *A Pattern Language* (1977) — the ancestor of pattern thinking
