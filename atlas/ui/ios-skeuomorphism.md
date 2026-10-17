---
id: ios-skeuomorphism
name: iOS Skeuomorphism (iPhone OS 1 – iOS 6)
type: system
discipline: [ui, product]
era: 2007–2013
origin: Cupertino, USA
lineage: [mac-os-x-aqua, classic-macintosh]
tags:
  mood: [tactile, crafted, reassuring, nostalgic]
  topics: [mobile apps, notes, music, games, reading, finance]
axes: {order: 7, density: 4, ornament: 7, warmth: 8, contrast: 5, geometry: 5, chroma: 5, typevoice: 3, energy: 3, hand: 4, play: 6, era: 2}
---

# iOS Skeuomorphism (iPhone OS 1 – iOS 6)

**Essence:** A radically new touch device that borrowed trust from old objects — felt, leather, linen, paper and wood — and made glass feel like something you could hold.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Material as meaning | Each app wore a material that announced its domain: green felt for Game Center, stitched leather for Find My Friends and calendar apps, wooden shelves for Newsstand, yellow legal paper for Notes. | Pick one material per product that encodes its domain (ledger paper for accounting, canvas for a design app) and render it as a subtle surface texture at 3–6% contrast. One material per screen, never stacked. |
| G2 · Controls that mimic the gesture | The date picker was a curved drum spun with a flick; switches slid; the Podcasts app showed a reel-to-reel deck. | Choose controls whose physical analogue matches the motion: rotary drum pickers with 3D curvature, inertial scroll and row snap; sliders with a grippable thumb; dials for continuous values. |
| G3 · Letterpress labels | Text on textured bars and panels was "engraved" with a one-pixel highlight or shadow. | On light surfaces: `text-shadow: 0 1px 0 rgba(255,255,255,.6)`; on dark: `0 -1px 0 rgba(0,0,0,.5)`. Makes type feel stamped into the material. |
| G4 · Glossy squircle icon | Home-screen icons shared one rounded-square mask with an automatic glossy highlight arc across the top. | Icon template: shared corner mask, consistent top highlight arc and 1 px inner stroke, photoreal or illustrated subject; consistency of the frame lets subjects vary wildly. |
| G5 · Physical transitions and elastic edges | Pages curled, drawers slid, lists bounced back when pulled past their end, and momentum decayed naturally. | Transitions enact the metaphor (page turn for reading, slide-out drawer for menus). Overscroll offers elastic resistance (~0.55× drag) and springs back; flick scroll keeps momentum. |
| G6 · Stitches and edges as craft cues | Stitching, torn paper stubs and bevelled leather edges signalled care and handmade quality. | Use a single crafted edge detail (dashed "stitch" border 1 px inset, torn-edge mask) on one hero surface to signal craft; never on every component. |

## Visual facts

- **Color:** navigation-bar blue-grey gradient (~`#B0BCCD → #6D84A2`), pinstriped light blue-grey grouped tables (~`#C5CCD4`), dark linen (~`#3A3D43`) for system layers, felt green, saddle browns, legal-pad yellow.
- **Type:** Helvetica (Neue) for system text; Marker Felt in Notes. Free: **Arimo** or URW **Nimbus Sans**; for handwritten notes **Patrick Hand**.
- **Form:** glossy bars, rounded grouped table cells, inner shadows, embossed text, photoreal textures, stitches.
- **Composition:** top bar + content + bottom tab bar of five; grouped table views; full-screen app metaphors.

## Attitude

When the iPhone launched (announced January 2007, 320×480 at 163 ppi), touch screens were unfamiliar. Visual metaphors from real objects told people what to touch and how. Under Scott Forstall the approach became increasingly literal, which provoked the 2013 reversal led by Jony Ive (`ios-7-flat`). Take the underlying idea — materials that *mean* something — not the faux leather.

## Blends

- **Amplifies:** `arts-and-crafts`, `mac-os-x-aqua`, `streamline-moderne` — craft, material love, glossy optimism.
- **Productive tension with:** `bauhaus` — "truth to materials" pressed against fake materials can yield honest digital materials: textures that describe real data or real wear.
- **Clashes with:** `metro-design-language` — Metro was explicitly founded against this; mixing produces neither craft nor clarity.

## Don't copy

- Apple's specific app artwork: Game Center felt, Find My Friends leather, Notes paper, Newsstand shelves, iBooks woodgrain, the system linen texture and Apple icons. Paint your own materials from your own domain.

## Study

- Apple iPhone Human Interface Guidelines, 2008–2012 editions (Wayback Machine / Apple developer archive).
- iPhone introduction keynote, Macworld 9 January 2007 (video).
- General Magic's Magic Cap (1994) — a room-and-desk metaphor that anticipated this approach; *General Magic* documentary (2018).
- Nielsen Norman Group articles on skeuomorphism and flat design (nngroup.com).
