---
id: didot
name: Didot
type: typeface
discipline: [graphic, ui]
era: 1784 to 1811; revivals 1991 to 2023
origin: Paris, France
lineage: [firmin-didot, baskerville]
tags:
  mood: [glamorous, cool, precise, haughty]
  topics: [fashion, beauty, luxury, magazines, culture]
axes: {order: 8, density: 2, ornament: 1, warmth: 2, contrast: 10, geometry: 8, chroma: 1, typevoice: 8, energy: 3, hand: 0, play: 1, era: 4}
---

# Didot

**Essence:** Neoclassical razor type. It is so thin in the hairlines and so upright in the stems that it only truly lives at large sizes, which is why it became the voice of fashion covers.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Dazzle management | Thick verticals beside near-invisible hairlines make text shimmer ("dazzle") and pull the eye away from the thin strokes that tell letters apart. | Wherever Didot runs to more than one line: tracking +2 to 4%, line-height ≥ 1.3, never justified, ≤ 6 words per headline. Body and anything ≥ 2 sentences go to the companion face. |
| G2 · Scale contrast is the layout | Magazine covers set a huge Didot masthead against small text and photography. The gap between sizes carries the drama. | Three sizes only per screen: e.g. 96 / 18 / 12px. Display steps jump by ≥ 1.5×; no intermediate sizes allowed. The masthead or hero word takes ≥ 60% of viewport width. |
| G3 · Larger means lighter | HTF Didot was drawn as a set of optical sizes: the bigger the setting, the finer the hairline can be. | A rule in the type tokens: as display size rises, choose the finer optical cut (or higher `opsz`), never the reverse. At 2× density, hairlines may go to 0.5 CSS px; at 1× they must stay ≥ 1px. |
| G4 · Monumental capitals | Didone capitals letterspaced become an engraved title line. | Caps in Didot only at ≥ 24px with +10 to 15% tracking. Small all-caps labels (nav, eyebrows) switch to a sans; Didot hairlines vanish at 11 to 13px. |
| G5 · A multilingual Didone | Didot-style faces became central to Greek printing, and that tradition continues in GFS Didot and Theano Didot. | For multilingual luxury brands, pick a Didone with real Greek and Cyrillic, and check that each script's hairlines and x-height match the Latin before launch. |

## Visual facts

- **Classification:** Didone (Modern) serif.
- **Origin:** Firmin Didot cut the defining types in Paris between 1784 and 1811; his brother Pierre printed with them (e.g. Voltaire's *La Henriade*, 1818).
- **Main digital versions:** Linotype Didot (Adrian Frutiger, 1991; ships with macOS; display-leaning). HTF Didot (Jonathan Hoefler, drawn 1991 for the *Harper's Bazaar* redesign, first printed September 1992; optical sizes; in MoMA's collection). Both commercial.
- **Anatomy:** strict vertical stress, extreme contrast, flat unbracketed hairline serifs, ball terminals, moderate x-height, narrow apertures.
- **Free / open alternatives:** Playfair (Claus Eggers Sørensen, OFL; the 2023 variable version adds an optical-size axis down to text). Bodoni Moda (OFL). GFS Didot (Greek Font Society, OFL) is a true Didot for Greek; its Latin follows Palatino, so use it for Greek and not as a Latin Didone. Theano Didot (Alexey Kryukov, free) covers Greek and Cyrillic.

## Attitude

The Didots joined fine printing with industrial method. Their type is cool, measured and sure of its rank. In a product it signals curation and taste, and it fails the moment the content is ordinary.

## Using it today

- **Signals:** fashion covers. *Vogue* took up Didot in the 1950s, *Harper's Bazaar* uses HTF Didot, CBS used a custom Didot for years, and Zara redrew a tight Didone logo in 2019. It is extremely saturated in beauty and luxury, and "Didone on cream" is a default premium preset for AI generators.
- **Robotic ↔ humane: 1/10.** Pure vertical axis, hairline unbracketed serifs, mechanical regularity, closed apertures; nothing of the pen survives.
- **UI fitness:** display only, ≥ 36px on 1× and ≥ 24px on 2× with a display cut. No labels, buttons or body. Rendering: hairlines disappear on low-DPI Windows and in light-on-dark text, so raise weight. Coverage: confirm Cyrillic and Greek per version.
- **Pairs with:** a geometric sans (Futura, or open Jost) for the fashion classic. A neutral grotesk for UI (Helvetica, or open Hanken Grotesk). Georgia or Gelasio for running text, a pairing Google suggests for Playfair.

## Blends

- **Amplifies:** `alexey-brodovitch`: his *Harper's Bazaar* spreads show how scale contrast and white space carry a Didone masthead.
- **Productive tension with:** `bloomberg-terminal`: one Didot headline above dense mono data gives luxury finance, where taste meets information.
- **Clashes with:** `cooper-black`: soft fat serifs beside hairlines make each look like a parody of the other.

## Don't copy

The *Vogue*, *Harper's Bazaar* and Zara mastheads; HTF Didot and Linotype Didot outlines without licence; specific fashion cover compositions.

## Study

- MoMA, HTF Didot: moma.org/collection/works/139304
- Hoefler&Co. on HTF Didot's optical sizes (typography.com)
- Greek Font Society: greekfontsociety-gfs.gr (GFS Didot history)
- Gallica (gallica.bnf.fr): Didot editions in full
