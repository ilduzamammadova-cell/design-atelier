---
id: command-line-and-teletext
name: Text-Mode Interfaces (Command Line, ANSI Art, Teletext)
type: movement
discipline: [ui, graphic]
era: 1970s–1990s (living subculture)
origin: London, UK (Teletext) / USA (terminals, BBS)
lineage: []
tags:
  mood: [blunt, nocturnal, systematic, nostalgic]
  topics: [developer tools, news, dashboards, music, terminals]
axes: {order: 9, density: 7, ornament: 3, warmth: 3, contrast: 9, geometry: 9, chroma: 6, typevoice: 8, energy: 3, hand: 2, play: 5, era: 4}
---

# Text-Mode Interfaces (Command Line, ANSI Art, Teletext)

**Essence:** A screen that is a grid of identical character cells, where layout, illustration and navigation are all built from letters, block glyphs and a handful of hard colours.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Character-cell grid | Every element lives on a fixed monospace cell (80×25 on a PC console, 40×24 on a Teletext page). Nothing sits between cells, so alignment is automatic and absolute. | Define one cell = `1ch × 1lh` of a mono face (e.g. 9×18 px). Panel widths, paddings, gutters and icon boxes are whole cells only; declare containers in `ch` (`max-width: 80ch`). No half-cell nudges, ever. |
| G2 · Line-drawing chrome | Windows and panels are framed with box-drawing characters (single and double rules) rather than shadows; weight of the line carries state. | Cards get a 1px rule; the focused or active panel switches to a double rule (`border: 3px double`). No drop shadows, no blur, no radius. Section titles sit *inside* the top border, interrupting it. |
| G3 · Eight hard colours | Teletext offered black plus seven fully saturated primaries and secondaries; in text mode a colour change could even cost a whole cell. | Restrict the palette to `#000 #F00 #0F0 #FF0 #00F #F0F #0FF #FFF` (or the 16 CGA tones). Each colour switch inside a line is preceded by one cell of space — make that a spacing token, so colour becomes rhythmic. |
| G4 · Numbers as addresses | Teletext pages were reached by typing three digits (100 = index) and four coloured "Fastext" keys jumped to linked pages. | Give every view a short visible address (`P302`, `/wx`) shown in a header strip, typeable in a command palette. Add a footer of exactly four colour-coded shortcut chips mapped to keys 1–4. |
| G5 · Inverse video | Selection is shown by swapping foreground and background, not by tint or glow. | Selected row = inverted colours, full row width. Cursor = full block blinking at ~530 ms. Focus never uses opacity. |
| G6 · Mosaic illustration | Teletext and ANSI artists drew with block characters: each cell split into a coarse 2×3 sub-grid (Teletext) or half-blocks and shade glyphs (░▒▓) on PCs. | Illustrations and charts are drawn on a coarse sub-cell grid (2×3 per cell); bar charts from block glyphs; empty states as small mosaic pictures, not vector art. |

## Visual facts

- **Color:** phosphor green `#33FF33` or amber `#FFB000` on `#0A0A0A`; PC console blue `#0000AA` with cyan `#00AAAA` (file-manager style); Teletext's eight colours at full strength on black.
- **Type:** fixed bitmap faces — IBM VGA 8×16, DEC terminal fonts, the Mullard SAA5050 Teletext character generator. Free: **VT323**, **IBM Plex Mono**, **Space Mono** (Google Fonts); **Bedstead** (free SAA5050-style Teletext face).
- **Form:** square cells, stair-stepped diagonals, block shading, scanline softness on real CRTs; no curves except those built from glyph combinations.
- **Composition:** header row (page number, title, clock), dense body in columns, footer row of key hints. Everything left-aligned to the cell grid.

## Attitude

The screen shows exactly what the machine holds — no simulated paper, no hidden layers. Constraint (cells, eight colours, 1 KB pages) was not apologised for; whole communities (BBS art groups, Teletext artists) turned it into an aesthetic. Borrow it to make software feel honest, fast and keyboard-native.

## Blends

- **Amplifies:** `bloomberg-terminal`, `demoscene-and-tracker-ui`, `brutalist-web`, `wim-crouwel` — all treat the raster or grid as the design, not a limitation to hide.
- **Productive tension with:** `fluent-design` — translucent acrylic and soft depth layered over a strict monospace grid gives the modern "beautiful terminal" (blurred, tinted panes over hard cells).
- **Clashes with:** `ios-skeuomorphism` — photographic leather and stitching around character cells reads as costume, not system.

## Don't copy

- Specific ANSI artworks and NFO logos by named art groups (ACiD, iCE and others) — they are signed works.
- Recovered BBC Ceefax pages, the Ceefax wordmark, and any broadcaster's Teletext page designs.
- The exact panel layout and colour scheme of a specific commercial file manager; make your own panel logic.

## Study

- Ceefax (BBC, 1974–2012) and Jason Robertson's recoveries of broadcast Teletext pages from home VHS tapes; teletextart.co.uk (Dan Farrimond's Teletext art hub, linked to the International Teletext Art Festival).
- 16colo.rs — searchable archive of ANSI/ASCII art packs; textfiles.com and *BBS: The Documentary* (Jason Scott, 2005).
- DEC VT100 (1978) and IBM PC code page 437 — the box-drawing/block glyph set behind decades of text UIs.
- Bedstead font project (bjh21.me.uk/bedstead) for faithful Teletext glyph geometry.
