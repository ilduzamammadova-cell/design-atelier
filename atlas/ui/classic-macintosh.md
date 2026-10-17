---
id: classic-macintosh
name: Classic Macintosh (System 1, Mac OS 9)
type: system
discipline: [ui, ux]
era: 1984 to 2001
origin: Cupertino, USA
lineage: [xerox-alto-and-star, susan-kare]
tags:
  mood: [friendly, crisp, tidy, characterful]
  topics: [creative tools, documents, education, personal software]
axes: {order: 8, density: 4, ornament: 2, warmth: 6, contrast: 9, geometry: 8, chroma: 1, typevoice: 4, energy: 2, hand: 2, play: 5, era: 6}
---

# Classic Macintosh (System 1, Mac OS 9)

**Essence:** A one-bit desktop of rounded rectangles, striped title bars and a single menu bar, the office metaphor made small, cheerful and consistent enough for anyone.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · One-bit discipline | The 1984 screen was 512×342 pixels of pure black and white at 72 ppi; grey existed only as dither patterns (the 50% checkerboard desktop). | Build a mode that works in `#000`/`#FFF` only. Disabled, inactive and background states use repeating 2×2 or 4×4 dither patterns (CSS `repeating-conic-gradient`), never opacity. |
| G2 · Edge-anchored menu bar | One global menu bar pinned to the top screen edge: the edge stops the pointer, so targets are effectively infinite in height. | Put global commands in a single persistent bar flush to a screen edge; never float primary menus inside windows. Frequent targets live on edges and corners. |
| G3 · Round rects as signature | Jobs pushed Bill Atkinson to make rounded rectangles fast in QuickDraw (Folklore: "Round Rects Are Everywhere!", 1981); buttons, dialogs and even the screen's outer corners were rounded. | Make corner radius a brand token and apply it everywhere, including the viewport: mask the app's outer corners (e.g. 8 px), buttons at full pill or 6 px, dialogs at 6 px. |
| G4 · Texture marks the active window | The active window's title bar is filled with horizontal pinstripes; inactive windows lose the stripes. State is texture, not colour. | Active panel header = six 1 px horizontal lines behind the title (title knocked out on white); inactive = plain. Works for monochrome, accessible themes and print. |
| G5 · Default-button ring & alert pictograms | The default action in a dialog wears a heavy outer ring; alerts carry one of three symbols (stop, caution, note). | Default button gets a 3 px outer ring with 1 px gap, not a fill colour. Exactly three alert severities, each owning one pictogram used nowhere else. |
| G6 · Stacks of cards (HyperCard) | Atkinson's HyperCard (1987) let anyone build stacks of fixed-size cards with buttons, fields and scripts, authoring and using in one tool. | Content as fixed-size cards navigated by arrows; users can place their own buttons and links on a card; a visible toggle between "use" and "edit" modes. |

## Visual facts

- **Color:** `#000`/`#FFF` (1984 to 87); restrained colour icons from System 7 (1991); Mac OS 8's "Platinum" appearance (1997) in soft greys (~`#DDDDDD`) with gentle bevels and a user-chosen highlight colour.
- **Type:** Chicago 12 for menus and titles, Geneva 9/12 for labels, Monaco 9 for code (all bitmap, by Susan Kare); Charcoal replaced Chicago in Mac OS 8. Free: **Pixelify Sans** or **Silkscreen** (bitmap mood); **Chivo** bold for an outline nod to Chicago's chunky humanist forms.
- **Form:** rounded rects, 1 px outlines, drop shadow as a hard 1 px black offset (no blur), scroll bars with grey dither tracks, the close box as an empty square.
- **Composition:** menu bar on top, desktop icons along the right edge, overlapping windows with a strict title-bar / content split; dialogs centred, default button bottom right.

## Attitude

The Mac team believed the computer should be an appliance with a personality, approachable, legible, a little funny, and that consistency was what made it learnable. Apple codified this in published Human Interface Guidelines (book edition 1987) so that third-party software would feel like one family. Borrow the *one rulebook for everyone* stance and the warmth inside rigour.

## Blends

- **Amplifies:** `susan-kare`, `xerox-alto-and-star`, `paul-rand`, economy with wit, systems that still smile.
- **Productive tension with:** `memphis`, contemporaneous (1981 to 87) but opposite in colour; Memphis pattern rendered as 1-bit dithers inside Mac chrome gives a playful but disciplined desktop.
- **Clashes with:** `ios-skeuomorphism`, photographic materials beside 1-bit abstraction look like two eras glued together.

## Don't copy

- The Apple logo, the smiling startup computer, Finder and system icons, Chicago and Geneva bitmap outlines, the startup sound, HyperCard's home-stack artwork. Recreate the logic (dither, ring, stripes), not the pixels.

## Study

- Folklore.org, Andy Hertzfeld's first-hand Macintosh stories; Hertzfeld, *Revolution in the Valley* (2004).
- Apple, *Human Interface Guidelines: The Apple Desktop Interface* (Addison-Wesley, 1987).
- GUIdebook gallery (guidebookgallery.org), screenshots of every System version.
- Infinite Mac (infinitemac.org), classic Mac OS versions running in the browser for hands-on study.
