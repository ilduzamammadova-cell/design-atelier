---
id: henri-de-toulouse-lautrec
name: Henri de Toulouse-Lautrec
type: artist
discipline: [graphic, art]
era: 1891 to 1901
origin: Paris, France
lineage: [jules-cheret, ukiyo-e]
tags:
  mood: [nocturnal, candid, sardonic, electric]
  topics: [entertainment, music, nightlife, events, media]
axes: {order: 3, density: 4, ornament: 2, warmth: 7, contrast: 8, geometry: 2, chroma: 6, typevoice: 5, energy: 7, hand: 8, play: 7, era: 5}
---

# Henri de Toulouse-Lautrec

**Essence:** Reportage turned into signs: flat silhouettes, bold crops and a few spattered tones that capture a performer's whole presence and the atmosphere of a room.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · The silhouette as symbol | In *La Goulue au Moulin Rouge* (1891) the crowd is a frieze of flat black shapes and the lamps are yellow ovals: shapes become symbols for a place and an event. | Reduce hero imagery to 2 to 3 flat silhouette shapes plus one detailed focal element. Test at 48px: the silhouette must still identify the subject (performer, venue, product). Works for event tickets, playlists, venue pages. |
| G2 · The bold crop | Influenced by Japanese prints, he cut figures with the frame edge, letting an instrument, hat or leg enter from outside the picture. | Crop photos off-canvas deliberately: subject cut by the top or side edge by 15 to 30%, with one strong diagonal element entering from a corner and pointing toward the headline. Use `object-position` presets rather than centred crops. |
| G3 · Foreground cut-out | A dark profile or figure in the immediate foreground (a dancer, a bass neck) sits in front of the scene, creating depth with no perspective drawing. | Three-plane layering: foreground cut-out (PNG/SVG mask) overlapping the headline with `z-index`, a flat middle scene, a solid background colour. Parallax ≤ 8px on scroll if motion is used. |
| G4 · Spatter as tone | He spattered ink from a toothbrush to create tone across flat areas. | A texture token: sparse spatter noise (SVG turbulence or scanned spatter at 3 to 6% opacity) over flat fills only, never over text. It gives warmth to flat illustration without gradients. |
| G5 · Few words, drawn with the picture | His lettering is minimal (often a name and a venue), drawn with the image and placed where the composition leaves room. | Headline ≤ 3 words, positioned in negative space left by the image (not in a separate text band). Name + place + date is the whole message for event surfaces. |

## Visual facts

- **Color:** olive yellow #C9B037, vermilion orange #E0522B, black #1B1B1B, muted green #6E8B5A, red #B8322A on warm paper #E8DFC8; flat and unmodulated.
- **Type:** brush-drawn capitals and casual script. Free stand-ins: Caveat Brush for drawn headlines; a sturdy grotesque for any small print.
- **Form:** fluid contour line, flat silhouettes, spatter (crachis) texture, caricatural exaggeration.
- **Composition:** steep diagonals, high or low viewpoints, cropped figures, empty floor planes, strong foreground repoussoir.

## Attitude

A painter and printmaker who drew nightlife from the inside, Lautrec made only about thirty posters, negotiated in the cabarets where he sketched. He favoured candour over idealization, and his posters were portraits of real performers, sharp and sometimes unflattering. Truth to a moment mattered more to him than prettiness.

## Blends

- **Amplifies:** `plakatstil`: his flat, reduced shapes point toward the object poster.
- **Productive tension with:** `massimo-vignelli`: candid cropped imagery and spatter inside a disciplined typographic grid give lively editorial work with structure.
- **Clashes with:** `alphonse-mucha`: candid caricature against idealized, timeless beauty.

## Don't copy

- *Moulin Rouge, La Goulue* (1891), *Divan Japonais* (1893), *Aristide Bruant* (1892 to 93), *Jane Avril* (1893) and his portraits of named performers.
- His signature monogram.

## Study

- Musée Toulouse-Lautrec, Albi (musee-toulouse-lautrec.com)
- MoMA, Toulouse-Lautrec prints and posters (moma.org/collection)
- Art Institute of Chicago, Lautrec poster holdings (artic.edu)
- Meggs, ch. 11, "The further development of French art nouveau"
