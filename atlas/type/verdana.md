---
id: verdana
name: Verdana
type: typeface
discipline: [graphic, ui]
era: 1996 to present
origin: Redmond, USA / Cambridge, MA, Microsoft (Matthew Carter; hinting by Tom Rickner)
lineage: []
tags:
  mood: [plain, roomy, legible, early-web]
  topics: [web, documentation, forums, enterprise, accessibility]
axes: {order: 7, density: 3, ornament: 0, warmth: 5, contrast: 3, geometry: 6, chroma: 3, typevoice: 2, energy: 2, hand: 0, play: 2, era: 4}
---

# Verdana (1996)

**Essence:** A typeface drawn on the pixel grid first and as outlines second, wide, loosely spaced, unmistakable letters for low-resolution screens.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Pixel-first design | Carter designed bitmaps for each screen size before the outlines, and Tom Rickner hand-hinted every size; the shapes are dictated by what pixels can show. | Design icons and small type on the target grid: draw 16px and 24px icons pixel by pixel, snap strokes to whole pixels, and test text at 1× density before approving any small style. |
| G2 · Wide letters, loose spacing | Generous widths and letter-spacing keep letters from merging when stems are one pixel thick. | For small text on low-density or e-ink screens: +2 to 3% tracking, line-height 1.6, size ≥ 13px; avoid tight tracking for labels under 14px in any face. |
| G3 · Disambiguated characters | Capital I has crossbars, J descends, 1 has a base, confusable characters are made distinct. | For codes, passwords, IDs and coupons, use faces (or `ss`/`cv` alternates) where I, l, 1 and O, 0 differ; enable `zero` (slashed zero) for alphanumeric codes. |
| G4 · Heavy bold by necessity | The bold has two-pixel stems at small sizes, so it is very dark, designed for screens, not for print colour. | Define bold separately per context: in pixel-tight UI use a heavier bold (700+) for emphasis; in print or high-density screens step down to 600 so emphasis doesn't blot. |

## Visual facts

- **Classification:** humanist-leaning sans designed for screen (often called a "screen sans").
- **Designer · year · foundry:** Matthew Carter for Microsoft, released 1996, with hand-hinting by Tom Rickner (then at Monotype); companion to the narrower Tahoma.
- **Digital versions & licences:** Verdana (bundled with Windows and macOS; formerly part of Microsoft's free "core fonts for the web"); Verdana Pro (Font Bureau, 2011, adds light, semibold, black and condensed styles; commercial).
- **Proportions:** very large x-height, wide letters, generous spacing, open apertures, low contrast; true-ish italic.
- **Free / open alternatives (keep the gene):** DejaVu Sans (from Bitstream Vera, free licence, wide, large x-height, distinguishes l/1/I in its mono sibling); Atkinson Hyperlegible Next (Braille Institute, OFL via Google Fonts, the disambiguation gene, taken further).

## Attitude

Verdana is pragmatism at the pixel level: legibility on real screens mattered more than elegance in print. It reminds designers that the medium sets the rules, and that a face drawn for one medium can look clumsy in another (IKEA's 2009 catalogue switch from Futura to Verdana drew heavy criticism).

## Using it today

- **Signals:** late-1990s/2000s web, forums, Microsoft-era documentation, IKEA from 2009; reads "early web, sensible, unfashionable". Saturation: low in new design, feels retro-utilitarian.
- **Robotic ↔ humane:** 5/10, open, wide and friendly at small sizes, but its pixel-grid logic and heavy bold make it blunt rather than graceful.
- **UI fitness:** body and UI labels at small sizes, especially low-density/e-ink; too wide and loose for display (looks clumsy above 24px). Covers Latin, Greek, Cyrillic.
- **Pairs with:** Georgia (Carter's screen serif from the same programme) for headings or reading; a compact grotesque for display; a monospace for code.

## Blends

- **Amplifies:** `georgia`, `web-1-vernacular`, `ambient-and-e-ink-ui`, Carter's screen-serif sibling and low-resolution honesty.
- **Productive tension with:** `editorial-web`, a utilitarian screen face under refined editorial headlines.
- **Clashes with:** `liquid-glass-imitation`, pixel-born plainness against glossy translucency.

## Don't copy

Verdana outlines; redistribution of the Microsoft font files outside their licence.

## Study

- Microsoft Typography, Verdana font family page: https://learn.microsoft.com/typography/font-list/verdana
- Matthew Carter, TED talk "My life in typefaces" (2014).
- ABC News / NPR coverage of IKEA's 2009 Verdana switch ("Verdanagate").
