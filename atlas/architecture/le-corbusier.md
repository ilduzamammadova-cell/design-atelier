---
id: le-corbusier
name: Le Corbusier (Charles-Édouard Jeanneret)
type: designer
discipline: [architecture, product, graphic]
era: 1920s–1960s
origin: Paris, France (born La Chaux-de-Fonds, Switzerland)
lineage: [peter-behrens]
tags:
  mood: [rational, sculptural, heroic, sunlit]
  topics: [housing, civic, tools, editorial, systems]
axes: {order: 8, density: 4, ornament: 2, warmth: 4, contrast: 7, geometry: 7, chroma: 5, typevoice: 4, energy: 5, hand: 3, play: 3, era: 8}
---

# Le Corbusier

**Essence:** A proportion system measured from the human body, a structure that frees walls from carrying loads, and color used to shape space instead of to decorate it.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Two-series human scale | The Modulor (1948, revised 1955) builds a measuring scale from a 183 cm figure: a "red" series anchored on navel height (113 cm) and a "blue" series on raised-hand height (226 cm). Each steps by the golden ratio, and every blue value is exactly double a red one. Sizes come from bodies, not from round numbers. | Spacing tokens from two interleaved Fibonacci-like ladders: red `4·6·10·16·26·42·68·110`, blue `8·12·20·32·52·84·136·220`. Red for padding, gaps and icon sizes; blue for section rhythm, container widths, image heights. A lint rule rejects any spacing value outside the two ladders. |
| G2 · Free plan, free façade | The Five Points (1926–27): pilotis lift the house and a concrete frame carries the loads, so partitions can curve freely and the façade becomes its own layer. | Keep the structural grid (columns, gutters) fixed and invisible, and let inner partitions (cards, dividers, curved panels) take any shape because they carry nothing. The page skin (header, background, chrome) is a separate layer you can restyle without touching layout. |
| G3 · Ribbon window | The long horizontal window (fenêtre en longueur) gives even light and one continuous panoramic view instead of punched holes. | One full-width horizontal band, about 1/5 of the viewport tall, is the only place where imagery or live content appears: a media strip, a timeline, a ticker. Above and below it the surfaces stay solid and calm. |
| G4 · Color keyboards | His Polychromie architecturale (43 hues for the Salubra wallpaper firm in 1931, 20 more in 1959) arranged paint on "keyboards" with a slider that isolates 3–5 colors that work together. Each hue had a spatial job: blues push a wall back, reds bring it forward, ochres warm it. | Define the palette as chords of 3–5 tones chosen together, never single swatches. Every token carries a spatial role: `advance` (accent, primary action), `recede` (backgrounds, secondary panels), `neutral` (lime white, stone). Product areas switch chords; colors are never mixed across chords. |
| G5 · Promenade architecturale | Villa Savoye is experienced as a walk: a ramp reveals framed views one after another, from entrance to roof garden. | Long pages built as a guided route: each scroll step reveals exactly one new framed "view", tied together by a continuous ramp element (a connecting rule or progress line). The route ends in a quiet "roof garden" section, not a crowded footer. |
| G6 · Regulating lines | He drew tracés régulateurs, diagonals and ratio rectangles over façades, to check that every opening related to the whole. | Check layouts with an overlay of diagonals and 1:1.618 rectangles: the corners of the hero image, headline block and main action must sit on a shared diagonal. Ship a dev toggle that draws these lines on any screen. |

## Visual facts

- **Color:** lime white (≈ #F2EFE6), ultramarine (≈ #2B4C9B), burnt sienna (≈ #8B3A27), ochre yellow (≈ #D9A23B), pale green (≈ #9AAE8C), warm light grey (≈ #D6D4CE). Approximate. The licensed Les Couleurs Le Corbusier swatches are the real reference.
- **Type:** stencil capitals on drawings, books and buildings; plain grotesques in his publications → free: "Big Shoulders Stencil" or "Stardos Stencil" for signage moments, "Work Sans" or "Archivo" for text.
- **Form:** white prisms on thin pillars in the 1920s; after the war, raw béton brut, sculpted roofs, deep brise-soleil grids.
- **Composition:** horizontal bands, double-height rooms, roof terraces; plans and façades checked against golden-section rectangles.

## Attitude

He saw architecture as equipment for modern life: something that could be standardised and mass-produced, measured against the human body. He believed a well-designed standard frees people rather than confining them. His late work (Ronchamp, Chandigarh) bends the same system into sculpture and raw material, which shows the rules were a base to depart from, not a cage.

## Blends

- **Amplifies:** `swiss-international`, `josef-muller-brockmann` — both turn proportion into a grid; the Modulor gives a Swiss grid a body-based rhythm instead of an arbitrary module.
- **Productive tension with:** `luis-barragan` — an open plan and ribbon windows set against Barragán's enclosed, windowless color walls; the mix gives an open structure with a few closed, saturated "rooms".
- **Clashes with:** `memphis` — Memphis treats proportion as a joke; next to Modulor ratios, both end up looking arbitrary.

## Don't copy

The Modulor figure drawing (rights held by the Fondation Le Corbusier); the roof silhouette and pierced south wall of Ronchamp; the LC chaise longue and other furniture designed with Charlotte Perriand and Pierre Jeanneret; the Les Couleurs Le Corbusier swatch names and codes as a branded palette.

## Study

- Villa Savoye, Poissy (1928–31); Unité d'habitation, Marseille (1947–52); Notre-Dame du Haut, Ronchamp (1950–55); Sainte-Marie de La Tourette (1953–60); Capitol Complex, Chandigarh (from 1951).
- Books: *Vers une architecture* (1923); *Le Modulor* (1948) and *Modulor 2* (1955); Arthur Rüegg, *Le Corbusier: Polychromie architecturale* (Birkhäuser, 1997; 3rd ed. 2016).
- Fondation Le Corbusier: https://www.fondationlecorbusier.fr
- UNESCO World Heritage: *The Architectural Work of Le Corbusier* (17 sites, inscribed 2016).
