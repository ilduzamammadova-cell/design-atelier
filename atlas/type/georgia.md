---
id: georgia
name: Georgia
type: typeface
discipline: [graphic, ui]
era: 1993 to 1996
origin: United States (Matthew Carter for Microsoft)
lineage: []
tags:
  mood: [friendly, readable, steady, unpretentious]
  topics: [news, blogs, reading-apps, education, documentation]
axes: {order: 6, density: 5, ornament: 1, warmth: 6, contrast: 4, geometry: 5, chroma: 1, typevoice: 3, energy: 2, hand: 2, play: 3, era: 4}
---

# Georgia

**Essence:** The first great serif drawn for the screen rather than for paper. It is wide, sturdy and warm, and built from the pixel up so it would stay readable on the coarse displays of the 1990s.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Pixel first, outline second | Carter drew bitmaps at key screen sizes first, then fitted outlines and hints so they reproduced those bitmaps. Microsoft's Bill Hill described it as working back-to-front. | Design critical UI at its real rendering size before scaling: type specimens at 12/14/16px, icons at 16/20/24px, checked on a 1× Windows screen before any 2× mockup. |
| G2 · Large x-height and sturdy hairlines | Big lowercase, generous widths and thin strokes that never get too thin survive low resolution and small sizes. | Screen serif for body at 15 to 17px / 1.5 to 1.6. It keeps its colour in dark mode and on cheap displays, so no weight bump is needed. |
| G3 · Hanging figures by default | Its numerals are old-style text figures that blend into prose. Microsoft's type director asked for this after early versions shipped lining numbers. | Prose numbers are fine. Tables, prices, phone numbers and one-time codes misalign, so render numeric UI in a lining tabular face (the sans, or Georgia Pro with `lnum tnum`). |
| G4 · Bold that jumps a pixel | Because stems were built in whole pixels, the bold is a full step heavier than typical print bolds. | Use bold only for headings. Emphasis in body is italic, never bold. For finer hierarchy use Georgia Pro's intermediate weights or the companion sans. |
| G5 · Zero-download reading | As one of Microsoft's 1996 core fonts for the web, it is preinstalled almost everywhere. | A "lite" reading mode with no web fonts: `font-family: Georgia, Gelasio, serif`. Gelasio's matching metrics prevent layout shift when Georgia is missing. |

## Visual facts

- **Classification:** screen serif in the Scotch Roman tradition (flat-topped serifs on *b, d, h, k, l*), a screen sibling of Carter's print face Miller (Font Bureau, 1997).
- **Origin:** designed by Matthew Carter in 1993 for Microsoft, hinted by Tom Rickner, released 1 November 1996 in Microsoft's core fonts for the web. Georgia Pro (2011) adds weights, small caps and extended character sets; it is free on Windows 10+ and sold elsewhere.
- **Licence:** proprietary Microsoft font, preinstalled on Windows and macOS.
- **Anatomy:** large x-height, wide proportions, moderate contrast, sturdy bracketed serifs, ball terminals, old-style figures; the bold is very heavy.
- **Free / open alternatives:** Gelasio (Eben Sorkin, OFL; metric-compatible with Georgia in regular, bold and both italics; cooler and more formal in look) and Merriweather (Sorkin, OFL; a screen-first serif with a large x-height).

## Attitude

Georgia accepts the medium's limits instead of fighting them. Rather than squeezing print type into pixels, it drew new letters from the pixel grid. That humility made it the reading face of the early web.

## Using it today

- **Signals:** 2000s blogs and news sites (*The New York Times* moved its web text to Georgia in 2007), e-book apps, reading modes. It is saturated, but now feels quietly nostalgic: the honest web serif.
- **Robotic ↔ humane: 6/10.** Ball terminals, open counters, hanging figures and a calligraphic italic are warm. The pixel-born regular construction and heavy bold are utilitarian.
- **UI fitness:** body yes (15 to 18px); labels possible ≥ 13px in regular, but the bold is too heavy for UI states; display plain and clumsy above about 48px. Rendering is excellent on low-DPI screens. Check Greek, Cyrillic and Vietnamese in the version your users have.
- **Pairs with:** Verdana, its sibling from the same Carter-Microsoft project, for UI. Playfair for display (Google suggests Georgia or Gelasio with Playfair). A mono such as IBM Plex Mono for code samples in documentation.

## Blends

- **Amplifies:** `web-1-vernacular`: the honest, system-font early web, readable on anything.
- **Productive tension with:** `swiss-international`: a friendly screen serif on a strict modular grid gives warm documentation with modern structure.
- **Clashes with:** `glassmorphism`: frosted translucency behind a utilitarian web serif feels like two eras colliding.

## Don't copy

Georgia's outlines in a logo without checking Microsoft's licence; *New York Times* web layouts.

## Study

- Bill Hill on how Georgia and Verdana were made (W3C www-font list, 1998): lists.w3.org/Archives/Public/www-font/1998JanMar/0047.html
- Microsoft Typography, Georgia font page (learn.microsoft.com/typography).
- Gelasio specimen and notes: fonts.google.com/specimen/Gelasio
