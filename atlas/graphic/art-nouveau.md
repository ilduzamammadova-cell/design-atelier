---
id: art-nouveau
name: Art Nouveau (Jugendstil, Modernismo, Stile Liberty, Nieuwe Kunst)
type: movement
discipline: [graphic, architecture, product, craft]
era: c. 1890–1910
origin: Paris, Brussels, Munich, Glasgow, Vienna, Barcelona, Nancy
lineage: [arts-and-crafts, chromolithography]
tags:
  mood: [sensuous, flowing, organic, theatrical]
  topics: [beauty, fashion, food & drink, culture, hospitality]
axes: {order: 3, density: 7, ornament: 10, warmth: 8, contrast: 5, geometry: 0, chroma: 6, typevoice: 7, energy: 6, hand: 6, play: 5, era: 5}
---

# Art Nouveau

**Essence:** A living line freed from history: whiplash curves of stems, hair and flame carry the whole composition, and ornament and structure become the same thing.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · One signature curve | The movement's identifying mark is an organic line that can whip or glide, sprouting from corners and organizing whole surfaces. | Define one brand curve as an SVG path token (e.g. an S-curve with a 1:3 rise) and reuse it everywhere: section divider, image mask edge, scroll-progress path, motion path for transitions. One curve, many jobs; no ad hoc curves elsewhere. |
| G2 · Ornament is the structure | Victor Horta's interiors grew their ironwork, railings and ceilings from one tendril vocabulary, so decoration and function fused. | Make functional parts the decorative ones: scroll indicators, dividers, progress bars and card corners carry the ornament (curved progress line, tendril-tipped slider). No separate decoration layer. |
| G3 · The organic frame | Posters and covers enclose text in shaped panels such as arched tops, tendril borders or hair that becomes a frame. | Text containers with one shaped edge: `border-radius: 48% 48% 8px 8px / 24% 24% 8px 8px` arched tops, or `clip-path` with the brand curve. Use on hero, cover and invitation surfaces only; keep data UI rectangular. |
| G4 · Flat colour with a living contour | Influenced by Japanese prints, Nouveau graphics favour flat colour areas bounded by a fluid contour of varying weight. | Illustration spec: flat fills (no gradients), a contour line that tapers between 1 and 3px (variable stroke via a pressure-sensitive brush or SVG outlines), 3–5 colours per image. |
| G5 · Total work of art | Designers shaped buildings, furniture, posters, jewellery, type and cutlery as one environment (the *Gesamtkunstwerk*). | Brand touches reach every surface (404, transactional email, invoice PDF, loading state, packaging) through shared tokens and one motif kit, audited quarterly. |
| G6 · Pattern books as distribution | Verneuil, Mucha and Auriol's *Combinaisons ornementales* (c. 1900) and many Dutch manuals taught the style through construction plates. | Ship the motif kit with a "how to construct" page: lattice, curve token, permitted combinations, step-by-step builds, so others extend the style correctly instead of copying screenshots. |

## Visual facts

- **Color:** sage #9CAF88, mauve #B48EAD, ochre #C8963E, peacock teal #1F6F78, cream #F3E7C9, with gold highlights #B8963E.
- **Type:** drawn lettering with soft, swelling strokes; Eckmannschrift (1900) and Grasset's types. Free stand-ins: Federant and Smythe (Google Fonts) for display; set body in a calm serif such as Sorts Mill Goudy.
- **Form:** whiplash curves, lilies, irises, peacocks, flowing hair, insects, flames; asymmetric organic growth.
- **Composition:** asymmetrical yet enclosed; figure and lettering intertwined; borders that sprout and frame.

## Attitude

Art Nouveau rejected the Victorian habit of copying past styles and sought a new art for modern life, taking its forms from nature and from Japanese design. It aimed to bring art into everyday objects and mass communication, and it was the hinge between historicism and modernism: ornament derived from invented, abstracting line rather than borrowed motifs.

## Blends

- **Amplifies:** `alphonse-mucha`, `henry-van-de-velde`: its most complete graphic statements.
- **Productive tension with:** `swiss-international`: one Nouveau curve as the only organic element in a strict grid gives a single living gesture against order (see G1).
- **Clashes with:** `de-stijl`: orthogonal purity and whiplash line negate each other.

## Don't copy

- Mucha's, Grasset's and Horta's specific works; Guimard's Paris Métro entrance lettering and cast-iron forms.
- Commercial digitizations of Nouveau display faces (Arnold Böcklin, Eckmann revivals). Use open fonts or draw your own.

## Study

- Musée d'Orsay, decorative arts collection (musee-orsay.fr); Musée de l'École de Nancy
- Horta Museum, Brussels (hortamuseum.be)
- V&A, *Art Nouveau 1890–1914*, exhibition catalogue, ed. Paul Greenhalgh (2000)
- Meggs, ch. 11, "Art Nouveau"
