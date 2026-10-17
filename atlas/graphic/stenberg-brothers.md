---
id: stenberg-brothers
name: Stenberg Brothers (Vladimir and Georgii Stenberg)
type: designer
discipline: [graphic]
era: 1923 to 1933
origin: Moscow, USSR
lineage: [constructivism, photomontage]
tags:
  mood: [cinematic, dizzying, dramatic, populist]
  topics: [film, streaming, entertainment, theatre, events]
axes: {order: 3, density: 6, ornament: 1, warmth: 5, contrast: 9, geometry: 6, chroma: 7, typevoice: 7, energy: 10, hand: 4, play: 6, era: 8}
---

# Stenberg Brothers (Vladimir 1899 to 1982, Georgii 1900 to 1933)

**Essence:** Film posters that move, enlarged film frames, spiralling type and vertiginous perspective that make a still sheet feel like a cut.

Working as one signature ("2 Stenberg 2"), they designed theatre sets and a large body of Soviet film posters, for Soviet and imported films alike, until Georgii's death in 1933. MoMA gave them a retrospective in 1997.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Drawn montage via projection | Photos reproduced badly, so they projected film frames with a device of their own, enlarging, distorting and rotating them, then traced and printed them as flat lithographic colour | Image pipeline: stills posterised to 2 to 4 tones (threshold/trace), recoloured with brand tokens; vector-like images can then be scaled, rotated and skewed freely without photo artefacts |
| G2 · Spiral and ring type | Titles and credits set in rings and spirals that pull the eye inward (*Man with a Movie Camera*, 1929) | Circular text on an SVG `textPath` around a focal image for event or feature promotion; rotate ≤ 6°/s and stop under `prefers-reduced-motion` |
| G3 · Vertigo perspective | Figures fall through space; buildings and rails tilt at extreme angles | Hero with forced perspective: a skewed grid plane (`perspective: 800px`, `rotateX(55deg)`) behind flat content; content itself never skewed |
| G4 · Giant face, tiny figure | A tightly cropped close-up beside small full-length figures produces scale shock | Media-tile rule: face or eyes fill ≥ 50% of the tile, plus one small full-body cut-out for scale |
| G5 · Realism against flat colour | Near-photographic figures float on saturated flat fields with one geometric shape | Photo cut-outs on flat brand-colour backgrounds (no environment), one circle or bar per tile as the only graphic device |

## Visual facts

- **Color:** saturated yellow, orange, magenta-pink, blue and black, approx. `#F2C200`, `#E8541E`, `#D6336C`, `#2A4D9B`, `#111111`.
- **Type:** hand-lettered condensed sans, set in arcs, in perspective or stepped. Free: Oswald, Big Shoulders Display, Bebas Neue.
- **Form:** traced photographic figures, rings, rails, fragments of bodies.
- **Composition:** radial or diagonal, centrifugal; type orbits the image.

## Attitude

Cinema was the mass art of the revolution, and the poster had to carry montage's shock onto the street. They treated the poster as a frame of film, motion, cut and close-up, rather than as a painting.

## Blends

- **Amplifies:** `saul-bass`, `alexander-rodchenko`, reduction and kinetic type for film.
- **Productive tension with:** `josef-muller-brockmann`, a calm modular grid streaming interface where each title's key art alone is allowed Stenberg-style motion.
- **Clashes with:** `arts-and-crafts`, handmade gentleness drains the velocity that is the whole point.

## Don't copy

Posters for *Man with a Movie Camera* (1929), *The General* (1929), *Battleship Potemkin* (1929 version), *Berlin: Symphony of a Great City* and *The Eleventh Year*.

## Study

- MoMA, *Stenberg Brothers: Constructing a Revolution in Soviet Design* (1997, Christopher Mount).
- Cooper Hewitt collection (collection.cooperhewitt.org); Merrill C. Berman Collection (mcbcollection.com).
- Meggs' History of Graphic Design, ch. 15.
