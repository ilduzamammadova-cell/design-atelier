---
id: courier
name: Courier
type: typeface
discipline: [graphic, ui]
era: 1955 to 1956; digital 1990s to 2013
origin: United States (IBM)
lineage: []
tags:
  mood: [mechanical, documentary, raw, deadpan]
  topics: [film, journalism, legal, code, archives]
axes: {order: 8, density: 6, ornament: 0, warmth: 4, contrast: 1, geometry: 7, chroma: 1, typevoice: 5, energy: 2, hand: 3, play: 3, era: 3}
---

# Courier

**Essence:** The typewriter's letter. Every character takes the same width and every stroke the same weight, so text becomes a grid of evidence: drafts, dossiers, scripts.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · One width for every character | Monospacing makes columns align and page length predictable. Screenplays are kept in 12pt Courier partly so page count can stand in for screen time. | Character-grid layouts (logs, terminals, receipts, diff views, code): size containers in `ch` units, align columns by character count, and keep tables free of proportional figures. |
| G2 · Typewriter means draft | Courier carries the look of an unfinished, unofficial or raw document: the manuscript before typesetting. | Use type to show state: drafts, AI first passes, redline proposals and raw transcripts render in a slab mono; accepted or published text switches to the proportional face. |
| G3 · Slabs fill the cell | In a fixed-width cell, narrow letters (*i, l, j*) get long slab serifs so their visual weight matches the wide ones. | When building fixed-width controls (segmented buttons, tabs, keypad keys), give narrow content extra visual mass (padding, icons, rules) so every cell carries equal weight; never centre a tiny glyph in an empty cell. |
| G4 · Thin digital ghosts | Courier New was digitized from an IBM Selectric type element without the weight added by ink spread, so it looks spindly on screen and paper. | Specify mono weight for the medium: Courier Prime (heavier, crisper) or a mono at 450 to 500 weight. Never Courier New below 15px on 1× screens. |

## Visual facts

- **Classification:** monospaced slab serif (typewriter).
- **Origin:** Howard "Bud" Kettler for IBM, published 1955 or 1956. IBM never trademarked the name, so the name and design concept are in the public domain. Claims that Adrian Frutiger redrew it for the Selectric are disputed.
- **Main digital versions:** Courier New (Monotype; shipped with Windows 3.1 and since; thin). Courier 10 Pitch (Bitstream; heavier, closer to typed output; donated to the X Consortium). Linotype/Adobe Courier as a PostScript core font. Licences vary: OS-bundled or free.
- **Anatomy:** monoline strokes, round ball-like terminals, slab serifs extended on narrow letters, open forms, low x-height for a mono.
- **Free / open alternatives:** Courier Prime (Alan Dague-Greene, commissioned by John August / Quote-Unquote Apps, January 2013, OFL; metric-compatible with Courier, true italics). Nimbus Mono (URW++ base 35). Liberation Mono (metric-compatible with Courier New, but sans in style).

## Attitude

Kettler wanted an ordinary messenger with dignity. Courier's power is that it refuses to be designed-looking: it records rather than persuades. Use it to make content feel raw and accountable.

## Using it today

- **Signals:** screenplays (12pt Courier is the industry standard), typewritten documents, government files (the US State Department used 12pt Courier New until 2004), early terminals and code. Its use for "classified dossier" is a cliché in UI and film titles.
- **Robotic ↔ humane: 4/10.** Monoline strokes and fixed width are mechanical. The soft round terminals and the memory of a struck key and inked ribbon add nostalgia and some warmth.
- **UI fitness:** code, data and short labels (≥ 13px Courier Prime); long body is tiring because of uneven word spacing and fixed widths; display only as a deliberate document signal. Coverage: Courier New is broad (Latin, Greek, Cyrillic, Hebrew, Arabic in Windows versions); check Courier Prime beyond Latin.
- **Pairs with:** a grotesque sans for the interface (Helvetica, or open Archivo). A text serif for "published" states (Times New Roman or Charter) to make the draft-to-final switch visible. IBM Plex Mono when code needs a modern mono beside the typewriter voice.

## Blends

- **Amplifies:** `command-line-and-teletext`: fixed-width character grids as the whole visual language.
- **Productive tension with:** `editorial-web`: typewriter drafts beside finished editorial type turn process into content (versions, edits, annotations).
- **Clashes with:** `art-nouveau`: monospaced bureaucracy cannot meet whiplash ornament halfway.

## Don't copy

IBM typewriter type-element artwork; specific film title sequences; government document templates and classification stamps.

## Study

- Courier Prime: quoteunquoteapps.com/courierprime
- Paul Shaw on Courier's attribution history (his writing on IBM typefaces).
- Microsoft Typography, Courier New font page (learn.microsoft.com/typography).
