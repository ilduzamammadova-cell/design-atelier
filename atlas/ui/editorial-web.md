---
id: editorial-web
name: Editorial Web (art-directed long-form)
type: movement
discipline: [ui, graphic]
era: 2008 to present
origin: New York, USA, and worldwide newsrooms and independent publishers
lineage: [swiss-international, alexey-brodovitch, jan-tschichold]
tags:
  mood: [literate, immersive, measured, cinematic]
  topics: [journalism, essays, annual reports, case studies, documentation]
axes: {order: 7, density: 4, ornament: 2, warmth: 6, contrast: 6, geometry: 6, chroma: 3, typevoice: 7, energy: 4, hand: 2, play: 3, era: 6}
---

# Editorial Web (art-directed long-form)

**Essence:** Reading as the interface, magazine-grade typography, a bespoke layout for each story, and media that unfolds as you scroll.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Measure first | Long-form web design starts from comfortable reading: line length, size and leading are set before anything else. | Body 19 to 21 px serif with 1.55 to 1.65 line height, `max-width: 66ch`; paragraphs separated either by space or by indent, never both. Everything else derives from this measure. |
| G2 · Art direction per story | Designers such as Jason Santa Maria and Dustin Curtis gave individual articles their own layout, palette and display type, as magazines do. | Article template exposes per-story tokens (display face, accent colour, hero layout variant) while navigation, body text and footer stay invariant across the site. |
| G3 · Scroll as narrative engine | "Snow Fall" (*The New York Times*, December 2012) wove video, maps and graphics into the reading flow; scrollytelling became a genre (The Pudding, 2017, ). | A sticky media pane (`position: sticky`) beside or behind the text; each paragraph is a "step" that changes the graphic when it crosses 50% of the viewport. Text never scrolls under media without a scrim. |
| G4 · Breakout rhythm | Images and graphics step out of the text column to wide or full-bleed widths, creating rhythm between intimate and expansive. | Grid with named lines: `content` (66ch), `wide` (~1100 px), `full` (100vw). Every figure declares one of the three; alternate widths to pace the story. |
| G5 · Print hierarchy, native to screen | Kickers, headlines, deks, bylines, drop caps and pull quotes give readers entry points. | Component set: kicker (13 px caps, +8% tracking), headline, dek (24 px), byline with date, 3-line drop cap, pull quote at 1.5× body in the display face. |
| G6 · Flow with the web's grain | Responsive design (Ethan Marcotte, 2010) and Frank Chimero's "The Web's Grain" (2015) argued for layouts that flex instead of fixed artboards. | Fluid type with `clamp()`, intrinsic layouts (`minmax`, `fit-content`), no fixed-width canvases; test the story at 320 px first. |

## Visual facts

- **Color:** paper off-white (`#FAF7F2`), ink near-black (`#111`), one accent per story; dark-mode variants for night reading.
- **Type:** newspaper and magazine serifs for body and display, a grotesque or gothic for labels. Free: **Source Serif 4**, **Newsreader**, **Fraunces** (display), **Libre Franklin** (labels).
- **Form:** typographic rules, captions in small sans, full-bleed photographs and video, data graphics.
- **Composition:** one central column with breakouts; generous top whitespace; table of contents or progress indicator for very long pieces.

## Attitude

The editorial web believes journalism and essays deserve the craft once reserved for print magazines, and that the screen adds powers print never had, motion, data, sound, interactivity, without sacrificing the calm of reading. It is reading-first: every flourish must serve comprehension.

## Blends

- **Amplifies:** `swiss-international`, `alexey-brodovitch`, `jan-tschichold`, editorial grids, typographic hierarchy, pacing.
- **Productive tension with:** `brutalist-web`, raw, visible structure carrying impeccable long-form typography reads as confident and independent.
- **Clashes with:** `web-2-gloss`, badges, gloss and sign-up urgency compete with sustained reading.

## Don't copy

- Specific story layouts and assets ("Snow Fall," Bloomberg Businessweek's "What Is Code?" by Paul Ford, 2015, individual Pudding essays), newspaper house typefaces and mastheads.

## Study

- "Snow Fall: The Avalanche at Tunnel Creek," John Branch, *The New York Times* (2012; Pulitzer Prize for Feature Writing 2013).
- Ethan Marcotte, "Responsive Web Design," *A List Apart* (May 2010); Frank Chimero, "The Web's Grain" (2015).
- Jason Santa Maria, *On Web Typography* (A Book Apart, 2014); Matthew Butterick, *Practical Typography* (practicaltypography.com).
- The Pudding (pudding.cool), visual essays and their open methods.
