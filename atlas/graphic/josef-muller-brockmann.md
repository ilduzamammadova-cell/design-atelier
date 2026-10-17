---
id: josef-muller-brockmann
name: Josef Müller-Brockmann
type: designer
discipline: [graphic]
era: 1950s to 1980s
origin: Zurich, Switzerland
lineage: [swiss-international, constructivism, new-typography]
tags:
  mood: [rational, musical, austere, precise]
  topics: [culture, music, public-safety, corporate, publishing]
axes: {order: 10, density: 4, ornament: 1, warmth: 2, contrast: 8, geometry: 9, chroma: 4, typevoice: 6, energy: 6, hand: 0, play: 2, era: 7}
---

# Josef Müller-Brockmann (1914 to 1996)

**Essence:** Proportion as music, every element measured in modules so that a poster feels composed the way a score is.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Module-counted format | In *Der Film* (1960) the sheet is cut into 3 × 5 modules; the title takes exactly two, secondary type aligns to the leading edge of the title's first letter. Every distance is a count, not a guess. | Specify layouts in module units: a hero is "3 × 5 modules", title spans 2 modules, metadata starts on the x-coordinate of the title's first glyph stem. Store module size as a token (e.g. `--module: 96px`). |
| G2 · Geometry as rhythm | The Tonhalle concert posters translate musical structure into circles, arcs and bars placed at rhythmic intervals, abstraction that still describes the content. | Data headers and loaders built from shapes whose sizes and gaps map to real values (track lengths, section durations). Use one ratio (3:5 or 1:1.618) for all shape steps. |
| G3 · Documentary photo + one red word | Road-safety and noise-abatement posters pair a neutral black-and-white photograph with a single short headline in red, often running obliquely across it. | Campaign / alert pattern: greyscale photo, 2 to 3 word headline in the only accent red, bold grotesque; no body copy on the image, details below in body size. |
| G4 · The visible grid | In late work the construction lines themselves become the image; the system is shown, not hidden. | Show structure as ornament: 1px column and baseline hairlines at 8 to 12% opacity in hero areas or empty states; they must coincide with the real layout grid. |
| G5 · Baseline-locked scale | His grid method ties type sizes, leading and image heights to one baseline unit, so text and pictures share edges. | Base 4px, line 24px. Image heights = n × 24 − gutter; headings sized so their line-height is a multiple of 24 (48, 72, 96). |
| G6 · Overlap as dissolve | *der* in grey sliding behind *Film* in white mimics a cinematic cross-fade, overlap expresses time. | A secondary word rendered behind the primary heading in 30% grey, offset by one module; page transitions use cross-dissolves rather than slides. |

## Visual facts

- **Color:** black #000000, white, signal red #E2001A, mid grey #8C8C8C; occasional spectral blues/greens in concert posters.
- **Type:** Akzidenz-Grotesk (medium and bold), set flush left → Archivo, Schibsted Grotesk, Hanken Grotesk.
- **Form:** perfect circles, squares, arcs, straight bars; neutral photography shot from dramatic angles.
- **Composition:** modular grid, tilted or rotated sub-grids, strong left alignment, large voids.

## Attitude

He wanted communication free of the designer's moods and of advertising's manipulation, objective, universal, and therefore respectful of the viewer. The grid was a moral instrument: an orderly form that a society could read, trust and reuse.

## Blends

- **Amplifies:** `massimo-vignelli`, `otl-aicher`, module discipline scales naturally into transit, wayfinding and identity systems.
- **Productive tension with:** `saul-bass`, scissor-cut, irregular symbols placed on a counted modular field: warmth carried by a strict structure.
- **Clashes with:** `psychedelic`, vibrating ornament destroys the measured intervals that are the whole point.

## Don't copy

*Der Film* (1960), the *Musica Viva* / Tonhalle series (from 1951), *weniger Lärm* (1960), *Schützt das Kind!* (1953), the L+C identity (1954).

## Study

- *Grid Systems in Graphic Design* (1981); *The Graphic Artist and His Design Problems* (1961); *A History of Visual Communication* (1971).
- Lars Müller, *Josef Müller-Brockmann: Pioneer of Swiss Graphic Design* (1995).
- Museum für Gestaltung Zürich poster collection: https://www.emuseum.ch ; MoMA collection: https://www.moma.org
