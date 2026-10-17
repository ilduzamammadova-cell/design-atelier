---
id: charter
name: Charter
type: typeface
discipline: [graphic, ui]
era: 1987; open release 1992
origin: Cambridge, Massachusetts, USA (Bitstream)
lineage: []
tags:
  mood: [sturdy, plain, practical, honest]
  topics: [documentation, legal, publishing, reading-apps, government]
axes: {order: 7, density: 6, ornament: 0, warmth: 5, contrast: 3, geometry: 6, chroma: 1, typevoice: 2, energy: 2, hand: 1, play: 2, era: 5}
---

# Charter

**Essence:** A serif engineered for bad output. It is compact, low in contrast and built from simple outlines so it would print cleanly on 1980s laser printers and fax machines, which is why it still reads well on any screen.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Designed for the worst device | Carter drew it in 1987 for low-resolution output (300 dpi laser printers, fax), with simplified outlines that rasterize cleanly. | Choose body type by worst-case rendering: test at 15 to 17px on a 1× Windows screen, an e-ink reader and a phone at low brightness. Ship the face that survives all three, not the one that wins on a retina mockup. |
| G2 · Low contrast, square-ish serifs | Strong hairlines and flat, slightly slab-like serifs don't shimmer or break up. | Use it as the dark-mode-safe serif: regular weight on dark grounds without the usual weight bump; it suits light-on-dark long reads in documentation and reading apps. |
| G3 · Compact with a large x-height | It fits many words per line while staying legible, an economical text face. | Dense documents (legal, specs, help centres): 16px at a 34 to 38em max width; it holds up in two-column layouts and narrow mobile measures without hyphenation. |
| G4 · Open licence as distribution | Bitstream donated Charter to the X Consortium in 1992 under permissive terms. Free derivatives (XCharter, Charis SIL) followed, and Apple ships it with macOS. | For multi-platform products, prefer open or freely redistributable faces so web, native apps, generated PDFs and offline exports use one face without licence friction. |

## Visual facts

- **Classification:** transitional serif with slab-like serifs (often grouped with slabs).
- **Origin:** Matthew Carter for Bitstream, 1987.
- **Main digital versions:** Bitstream Charter (freely redistributable since the 1992 donation). Charter BT and ITC Charter (commercial). Charter Pro (2004; old-style figures, small caps; commercial). Ships with macOS. *Medium* adopted it as its body face in its 2015 redesign.
- **Anatomy:** large x-height, compact width, low contrast, flat bracketless-looking serifs, open apertures, simplified curves.
- **Free / open alternatives:** Bitstream Charter itself (permissive licence). XCharter (Michael Sharpe, 2013; adds small caps and old-style figures; TeX). Charis SIL (SIL International, OFL; extended Latin and Cyrillic for linguistic and multilingual text).

## Attitude

Carter's view was that type must work in the conditions it will actually meet, not in ideal ones. Charter has no nostalgia and no showmanship: it is a well-made tool, and its generosity (the open licence) made it infrastructure.

## Using it today

- **Signals:** *Medium*'s reading experience (from 2015, paired first with Kievit, later with Marat Sans), LaTeX documents, Matthew Butterick's *Practical Typography*, which recommends it as a free text face. Saturation is low to moderate; it reads as sensible, editorial and unbranded.
- **Robotic ↔ humane: 5/10.** Simplified, almost polygonal curves and low contrast are rational. Open apertures, a warm italic and comfortable spacing keep it friendly.
- **UI fitness:** body text excellent (≥ 15px); labels workable ≥ 13px; display sturdy but bland. Renders well everywhere. Coverage: Bitstream Charter is basic Latin; use Charis SIL for extended Latin and Cyrillic.
- **Pairs with:** a humanist sans for UI (Medium paired it with Kievit; open Source Sans 3). IBM Plex Mono for code in docs. A high-contrast display serif for rare editorial headlines (Playfair, or open Bodoni Moda).

## Blends

- **Amplifies:** `editorial-web`: sustained on-screen reading with modest, robust type.
- **Productive tension with:** `y2k-chrome-and-acid`: a sober text face under exuberant graphics keeps the content credible while the surface plays.
- **Clashes with:** `art-nouveau`: engineered simplicity beside lavish organic ornament feels unfinished.

## Don't copy

The *Medium* reading layout as a template; Charter Pro outlines without licence; renaming modified Bitstream Charter files without honouring the original notice.

## Study

- Matthew Butterick, *Practical Typography*, "Charter" (practicaltypography.com/charter.html).
- Medium Design, "Cast of characters" (medium.design): why Medium chose Charter.
- Charis SIL (software.sil.org/charis) and XCharter on CTAN (ctan.org).
