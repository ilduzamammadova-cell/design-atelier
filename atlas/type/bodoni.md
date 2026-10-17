---
id: bodoni
name: Bodoni
type: typeface
discipline: [graphic, ui]
era: 1790s; revivals 1926–2020s
origin: Parma, Italy
lineage: [giambattista-bodoni, baskerville]
tags:
  mood: [dazzling, aristocratic, severe, glamorous]
  topics: [fashion, beauty, luxury, opera, editorial]
axes: {order: 8, density: 2, ornament: 1, warmth: 2, contrast: 10, geometry: 8, chroma: 1, typevoice: 8, energy: 4, hand: 1, play: 2, era: 4}
---

# Bodoni

**Essence:** Maximum contrast as a voice. Heavy verticals, hairline horizontals and flat unbracketed serifs make the line glitter. It is magnificent large and fragile small.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Vertical stress, hairline serifs | Thick strokes stand upright, the thin ones shrink to hairlines, and serifs meet stems at a sharp right angle with no bracket. | Display-only token. With Bodoni Moda use `font-optical-sizing: auto`, or pin `opsz` to the rendered size. The high-contrast cut appears only where its hairline renders ≥ 1 device pixel: about 32px+ on 1×, 24px+ on 2×. |
| G2 · Optical sizes, rebuilt from punches | ITC Bodoni (1994) went back to the Parma punches and produced three designs: Six for small text, Seventytwo for large, and Twelve interpolated between. Bodoni himself varied each size. | Map tokens to optical sizes, not just pixel sizes: caption → `opsz` 6–11, body → 11–14, display → 72–96. One family, three voices, and the small one gets sturdier hairlines and looser spacing. |
| G3 · Ball terminals as the only curve | Drops on *a, c, f, r, y* are the softest moment in a severe system. | Echo the ball terminal as the system's only rounded element (solid round bullets, radio dots, slider knobs) while every other corner stays at 0px radius. |
| G4 · Picket-fence rhythm | Narrow-ish letters with strong verticals create a dazzling stripe. It is thrilling in a headline and tiring in a paragraph. | Headlines track 0 to −1%. All-caps navigation in Bodoni opens to +8–12% so the stripes breathe. No Bodoni paragraph runs longer than three lines; text goes to the companion face. |
| G5 · Big theatrical numerals | High-contrast lining figures turn dates, prices and edition numbers into ornaments. | "Big number" hero (year, issue no., price) at ≥ 80px in Bodoni with a 12–14px sans caption under it. Tabular data never uses Bodoni figures. |

## Visual facts

- **Classification:** Didone (Modern) serif.
- **Origin:** Giambattista Bodoni, Parma, refined through the 1790s; shown in the *Manuale tipografico* (1788; expanded edition 1818).
- **Main digital versions:** Bauer Bodoni (Heinrich Jost with punchcutter Louis Hoell, 1926–27; often called the most faithful revival; commercial via Linotype/Monotype). ITC Bodoni (1994; team led by Sumner Stone with Holly Goldsmith, Janice Prescott Fishman and Jim Parkinson; commercial). Its Seventytwo cut ships with macOS as Bodoni 72. ATF Bodoni (Morris Fuller Benton) was the American standard Bauer competed with.
- **Anatomy:** small x-height, long extenders, extreme stroke contrast, flat hairline serifs, ball terminals, fairly narrow proportions, terminals that curl inward (tight apertures).
- **Free / open alternatives:** Bodoni Moda (Owen Earl / indestructible type, OFL; variable weight and optical-size axes, the gene intact) and Libre Bodoni (Impallari Type, OFL).

## Attitude

Bodoni designed for the magnificent occasion, not the everyday reader. The face is a machine for producing ceremony. Its value in a product is scarcity: one Bodoni moment per screen is luxury, while ten is noise.

## Using it today

- **Signals:** fashion and beauty, opera and theatre programmes, luxury retail. Massimo Vignelli kept Bodoni in his six basic typefaces. It is heavily saturated in fashion, and Didone headlines are a staple of the editorial serif revival.
- **Robotic ↔ humane: 2/10.** Rigid vertical axis, unbracketed hairline serifs, machined repetition of identical stems and closed apertures. Only the ball terminals hint at a hand.
- **UI fitness:** display only. Never form labels, buttons or body. Minimum ≈ 32px on 1× screens unless you use an optical small cut. Dark mode thins hairlines further, so raise `opsz` or weight. Check Cyrillic and Greek support in whichever Bodoni you choose; free revivals mostly focus on Latin.
- **Pairs with:** a geometric sans (Futura, or the open Jost by the same designer as Bodoni Moda), the classic fashion pairing of contrast and monoline. A neutral grotesk for UI (Helvetica, open Hanken Grotesk). A small-cap sans for captions.

## Blends

- **Amplifies:** `didot`: the twin Didone; together they define the fashion register.
- **Productive tension with:** `punk-graphics`: hairline aristocracy on photocopy grit and torn paper gives the fashion-zine look, glamour against dirt.
- **Clashes with:** `caslon`: gentle old-style irregularity beside machined contrast makes both look wrong.

## Don't copy

Pages of the *Manuale tipografico*; Bauer, ITC and Berthold Bodoni outlines without licence; fashion mastheads drawn in Didone lettering.

## Study

- Museo Bodoniano, Parma: revivals compared, e.g. museobodoniano.com/tipi/bauer-bodoni-en/ and /tipi/itc-bodoni-en/
- *U&lc* vol. 21 no. 2 (Fall 1994), the ITC Bodoni launch: fontsinuse.com/uses/69729
- Fonts In Use, Bauer Bodoni: fontsinuse.com/typefaces/225/bauer-bodoni
- Bodoni Moda source: github.com/indestructible-type/Bodoni
