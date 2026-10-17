---
id: pierre-simon-fournier
name: Pierre-Simon Fournier le Jeune
type: designer
discipline: [graphic]
era: 1736–1768
origin: Paris, France
lineage: [claude-garamond]
tags:
  mood: [graceful, systematic, decorative, inventive]
  topics: [systems, tooling, publishing, luxury, culture]
axes: {order: 8, density: 7, ornament: 8, warmth: 6, contrast: 4, geometry: 6, chroma: 2, typevoice: 6, energy: 4, hand: 3, play: 5, era: 2}
---

# Pierre-Simon Fournier le Jeune

**Essence:** A rococo typefounder who gave printers a whole design system: a standard unit of measure, families of compatible faces, and tiny ornaments that snapped together into endless borders.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · One base unit for everything | In 1737 he published a table of proportions that tied every type size to a fixed scale of lines and points, replacing chaotic, foundry-specific sizes. His 1764 *Manuel* moved to a pure point. | Define a single base unit (4px) and derive every size, space and radius from it: type 12/14/16/20/24/32/40/48, spacing 4/8/12/16/24/32/48/64. Name tokens by number, never by vibe ("space-16", not "medium"). |
| G2 · The type family | His specimen offered romans and italics in varied weights and widths designed to mix, an early version of the idea that faces should come as compatible families. | Pick one superfamily that covers every need (text, display, condensed, mono) instead of pairing unrelated fonts. Each role maps to a family member, so contrast comes from weight and width, not from clashing designs. |
| G3 · Fleurons as a construction kit | He cut small ornament sorts that could be used singly or multiplied and rotated into borders, rules and frames of any size, without hand-engraving. | A 3–5 glyph ornament kit (corner, link, terminal, dot) delivered as an SVG sprite or icon font. Dividers, frames and empty states are composed from it with `border-image` or repeated backgrounds. New ornaments are assembled, never drawn ad hoc. |
| G4 · Everything snaps to the same measure | Roman, italic, script, decorative types, rules up to about 35cm long, and ornaments all fit the same measurement, so they locked together visually and physically. | Icons, illustration frames, rules and type all align to the 4px grid and the same baseline. A visual-regression check flags any element whose box isn't a multiple of the base unit. |
| G5 · The specimen is the manifesto | His *Modèles des caractères* (1742) showed 4,600 characters he had cut himself, and the specimen pages were showpieces of rococo design. | Publish a living specimen page for the design system: every type role, ornament and colour at real size, composed into beautiful pages (not just tables), so the system sells itself to the people using it. |

## Visual facts

- **Color:** black with occasional red on cream laid paper #F2EBDA; the colour of the page comes from ornament density.
- **Type:** transitional roman following the Romain du Roi; condensed and decorative variants; script. Free stand-ins: Old Standard TT, Libre Baskerville.
- **Form:** S- and C-curve rococo fleurons, garlands, shells and vines built from small modular units; fine rules in single, double and triple lines.
- **Composition:** symmetrical title pages framed by assembled borders; generous use of ornament, always on the vertical and horizontal axes the metal demanded.

## Attitude

Fournier saw the printing house as a place that needed standards, not only beauty. He cut, cast, measured and documented, and his gift to printers was a coherent kit in which every part fitted every other. Elegance came from the system working.

## Blends

- **Amplifies:** `firmin-didot`: the Didots refined his point into the system still used in Europe.
- **Productive tension with:** `swiss-international`: modular ornament kits run on a rational base unit can produce decorated surfaces that still pass a grid audit.
- **Clashes with:** `art-nouveau`: hand-drawn whiplash curves resist being broken into repeatable sorts.

## Don't copy

- Specific Fournier fleuron designs and his specimen-book compositions.
- His title pages for *Manuel typographique* (1764–68).

## Study

- *Modèles des caractères de l'imprimerie* (1742), *Manuel typographique* (1764, 1768): Gallica, BnF (gallica.bnf.fr)
- Harry Carter, ed., *Fournier on Typefounding* (1930, reprint 1973)
- Meggs, ch. 8, "Graphic design of the rococo era"
