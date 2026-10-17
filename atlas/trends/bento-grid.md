---
id: bento-grid
name: Bento Grid
type: trend
discipline: [ui, graphic]
era: 2022–2026
origin: Cupertino, USA (Apple keynote and product-page feature grids) → global SaaS
lineage: [metro-design-language, swiss-international]
tags:
  mood: [tidy, modular, confident, product-y]
  topics: [saas, feature-overviews, portfolios, dashboards, keynotes]
axes: {order: 9, density: 7, ornament: 3, warmth: 4, contrast: 5, geometry: 8, chroma: 5, typevoice: 5, energy: 4, hand: 1, play: 4, era: 7}
saturation: 9
---

# Bento Grid

**Essence:** A box of rounded tiles of unequal size — one big hero cell, smaller cells around it — each holding one feature, stat or mini-illustration.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Summary at a glance | Many items compressed into one scannable view; the eye samples cells like a menu. | Use it only where users compare peers (dashboard, spec sheet): every cell answers the same question type with the same internal structure (label 13/16 caps, value 32/36, one-line note). |
| G2 · Size = importance | Cell area encodes priority, so hierarchy is spatial. | Rank items and assign spans by rank: #1 spans 2×2, #2–3 span 2×1, the rest 1×1 on a 4-column grid; never size a cell for visual balance alone. |
| G3 · Modular reflow | Tiles collapse cleanly to one column on mobile. | Define a reading order independent of the desktop mosaic (CSS `order` or source order by rank) so the stacked mobile view reads as a ranked list, not a random pile. |

## Why it reads as slop now

Named after the Japanese lunch box, the tile mosaic has ancestors in Windows Phone / Windows 8 live tiles (2010–2012). Apple's keynote summary slides and product pages around 2022–2023 made the rounded-cell feature overview famous; Dribbble, Framer templates and component libraries (Magic UI ships a bento component) turned it into the default "Features" section. By 2024 it sat in nearly every SaaS template and AI-generated landing page. The cheap version: six to nine cards of arbitrary sizes with 24px radii, each holding a gradient icon, a two-word title and a vague line ("Lightning fast. Built for speed."), with no logic for why any tile is bigger than another.

## Subvert

- **Make it a real table.** If cells are comparable, use an actual comparison table or spec sheet with ruled lines; the honesty reads as confidence.
- **One cell, not nine.** Show one feature full-bleed per screen and let the reader move through them — a sequence instead of a mosaic.
- **Break the box.** Keep variable spans but drop the containers: content sits on the page grid, separated by 1px rules and whitespace, like a newspaper page (lead story, deck, sidebar).

## Visual facts

- **Color:** neutral cells (#F5F5F7 on white, #1C1C1E on black) with one accent cell; gradients inside the mini-illustrations.
- **Type:** SF Pro Display, Inter; big numerals and short headlines.
- **Form:** 16–32px radii, 12–24px gutters, mini screenshots or 3D objects cropped by cell edges.
- **Composition:** asymmetric mosaic on a 3–4 column grid, usually one 2×2 hero cell.

## Attitude

The product as a set of neatly packaged benefits. The order is real, but used as decoration it says "we have many features" rather than "here is what matters".

## Blends

- **Amplifies:** `linear-style-dark-ui`, `dot-grid-and-line-grid-backgrounds` — the standard 2024 dev-tool page.
- **Productive tension with:** `josef-muller-brockmann` — true modular grids where size follows content hierarchy, not tile variety.
- **Clashes with:** `scroll-jacking-and-parallax` — a summary view loses its point if each tile animates in separately.

## Don't copy

Apple's specific keynote summary slides and iPhone/Mac/WWDC product-page grids; the Windows 8 Start screen layout.

## Study

- freeCodeCamp, "Bento grids in web design" — CSS grid mechanics.
- Apple events archive (apple.com/apple-events) — the summary slides that popularised the pattern.
- Josef Müller-Brockmann, *Grid Systems in Graphic Design* (1981) — sizing by hierarchy.
