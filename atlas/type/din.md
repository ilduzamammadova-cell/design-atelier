---
id: din
name: DIN (DIN 1451 and its digital descendants)
type: typeface
discipline: [graphic, ui]
era: 1931 to present (FF DIN 1995, DIN Next 2009)
origin: Germany, Deutsches Institut für Normung standard sheet DIN 1451
lineage: []
tags:
  mood: [engineered, technical, efficient, impersonal]
  topics: [signage, automotive, dashboards, hardware, sports, data]
axes: {order: 10, density: 6, ornament: 0, warmth: 2, contrast: 5, geometry: 9, chroma: 3, typevoice: 4, energy: 3, hand: 0, play: 1, era: 6}
---

# DIN (1931 standard; FF DIN 1995)

**Essence:** Lettering written as a standard, not drawn as art, strokes on a fixed grid so any engineer could reproduce it on a sign, a plate or a machine.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Letters as a specification | DIN 1451 (published 1931) defined letterforms by construction rules on a grid with a constant stroke, so signs, rail cars and technical drawings matched without a type foundry. | Treat type as spec: every text style is a token with exact size, weight, line-height, tracking and case; no free-form overrides in the component library. Lint for raw `font-size` values. |
| G2 · Condensed width for data | The Engschrift (condensed) and Mittelschrift (medium) widths fit long words and numbers into narrow fields. | Numeric dashboards, instrument clusters and tables: condensed or semi-condensed width, `font-variant-numeric: tabular-nums`, values right-aligned; labels in the normal width at 11 to 12px caps +8% tracking. |
| G3 · Uniform stroke, square-ish rounds | Constant stroke weight and rounds that lean toward straight sides read as machined, which is why DIN signals engineering and automotive precision. | Pair a DIN-style face with hard-edged UI (2 to 4px radii, 1px rules, no soft shadows). For warmth elsewhere, add a humanist text face for paragraphs; never set long reading in DIN at 14px. |
| G4 · Digital refinement of a standard | FF DIN (Albert-Jan Pool, 1995) and DIN Next (Linotype under Akira Kobayashi, 2009) added optical corrections, italics and weights that the original standard never had. | If you adopt a vernacular standard (road, rail, DIN), use a refined digital version with true weights; don't trace the standard sheet, its forms were not drawn for small screen text. |

## Visual facts

- **Classification:** geometric / industrial grotesque (engineering standard lettering).
- **Designer · year · foundry:** DIN 1451 standard (Deutsches Institut für Normung, 1931), developed from earlier Prussian railway and Siemens engineering lettering (Ludwig Goller is usually credited with leading the work).
- **Digital versions & licences:** FF DIN (Albert-Jan Pool, FontFont, 1995; now Monotype); DIN Next (Linotype, 2009; Arabic and slab companions); Bahnschrift (Microsoft, Aaron Bell; DIN 1451 digitisation, the first variable font shipped with Windows 10, 2017; bundled, not redistributable). Commercial except bundles.
- **Proportions:** large x-height, open but squarish counters, horizontal terminals, constant stroke, narrow-to-medium widths.
- **Free / open alternatives (keep the gene):** D-DIN (commissioned by Datto from Monotype; OFL; Normal, Condensed, Expanded; DINish extends language support); Barlow (Jeremy Tribby, OFL, slightly rounded, low-contrast grotesk drawn from California road signs and plates, three widths).

## Attitude

DIN carries the conviction that public communication should be reproducible without artistry, a sign is an instrument. Designers borrow that impersonality to signal precision, measurement and trust in engineering.

## Using it today

- **Signals:** German road signs, car dashboards, sports kits and tech hardware branding; reads "engineered, Germanic, data". Saturated in 2000s to 2010s branding; still strong for numbers.
- **Robotic ↔ humane:** 2/10, constant stroke, squared rounds, grid geometry and no true italic in the standard. FF DIN's softened details and italics move it to 3.
- **UI fitness:** excellent for numerals, dashboards, labels, wayfinding; poor for long body text. Minimum 12px for labels; numbers are its strength. Check Cyrillic/Greek in the chosen version (D-DIN is Latin-focused).
- **Pairs with:** Fira Sans or FF Meta for paragraphs, humanist warmth against engineered numerals; EB Garamond for editorial contrast; JetBrains Mono or IBM Plex Mono for code.

## Blends

- **Amplifies:** `otl-aicher`, `teenage-engineering`, `bloomberg-terminal`, instrument-panel clarity.
- **Productive tension with:** `scandinavian-modern`, engineered letters inside soft materials and warm colour.
- **Clashes with:** `art-nouveau`, standardised strokes cannot carry organic whiplash forms.

## Don't copy

FF DIN, DIN Next and Bahnschrift outlines; specific automotive/sports brand wordmarks set in DIN.

## Study

- DIN Media, DIN 1451 standard record: https://www.dinmedia.de/en/standard/din-1451/75548366
- Microsoft Typography, Bahnschrift: https://learn.microsoft.com/typography/font-list/bahnschrift
- Albert-Jan Pool, talks and writing on the history of DIN lettering.
- D-DIN on Font Squirrel: https://www.fontsquirrel.com/fonts/d-din
