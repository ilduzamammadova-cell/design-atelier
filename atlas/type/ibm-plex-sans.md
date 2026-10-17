---
id: ibm-plex-sans
name: IBM Plex Sans
type: typeface
discipline: [graphic, ui]
era: 2017 to present
origin: USA / Netherlands, IBM with the Dutch foundry Bold Monday (Mike Abbink, Paul van der Laan, Pieter van Rosmalen)
lineage: [franklin-gothic, corporate-identity]
tags:
  mood: [engineered, candid, contemporary, distinctive]
  topics: [enterprise, developer-tools, data, design-systems, multilingual]
axes: {order: 8, density: 5, ornament: 0, warmth: 5, contrast: 4, geometry: 7, chroma: 4, typevoice: 4, energy: 3, hand: 1, play: 3, era: 7}
---

# IBM Plex Sans (2017)

**Essence:** A corporate grotesque with engineered edges and a candid personality, and, unusually for a corporation, given away as open source so the brand voice can travel everywhere.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Corporate face as open source | IBM replaced Helvetica (used for over fifty years) with its own family and released it under the SIL OFL, ending licence fees and letting partners and developers use the brand voice freely. | If you are building a design system that third parties must implement, pick or commission an OFL face; publish it in the system repo with tokens so every product renders the same voice. |
| G2 · Grotesque with mechanical cuts | Plex Sans takes American-gothic structure (Franklin Gothic) and adds engineered details: angled terminals, squared transitions, a baseline stroke on the 1. | Use one engineered detail family-wide: if the type has squared-off curves, give UI shapes small radii (2 to 4px) and icons squared joins; consistency between type and shape makes the brand. |
| G3 · Superfamily with defined roles | Sans, Sans Condensed, Serif, Mono, plus separate Arabic, Devanagari, Hebrew, Thai, Japanese and Korean families share proportions. | Assign roles: Sans for UI, Condensed for tables and narrow cards, Mono for code and IDs, Serif for long reading. Set fallback stacks per locale (e.g. `"IBM Plex Sans", "IBM Plex Sans Arabic"`) to keep weights aligned. |
| G4 · Personality in the italic and figures | The italic (with Selectric-inspired shapes in Plex Mono) and distinctive numerals carry character that the upright keeps restrained. | Put personality in emphasis and numbers: italics for quotes and metadata, `tnum` lining figures in tables, `zero` in code; keep upright UI text plain. |

## Visual facts

- **Classification:** grotesque (neo-grotesque with engineered/humanist details).
- **Designer · year · foundry:** Mike Abbink (IBM) with Paul van der Laan and Pieter van Rosmalen (Bold Monday), introduced 2017.
- **Digital versions & licences:** IBM Plex Sans, Sans Condensed, Sans Variable (2019), Serif, Mono, and script families (Arabic, Devanagari, Hebrew, Thai, JP, KR). SIL OFL; name reserved and trademarked.
- **Proportions:** large x-height, medium-open apertures, low contrast, angled terminals, double-storey g, squarish curve transitions; true italic.
- **Free / open alternatives (keep the gene):** it is itself OFL. Related open faces: Public Sans (American-gothic root, plainer); Source Sans 3 (softer, more humanist).

## Attitude

Plex treats the corporate typeface as a shared tool rather than a guarded asset, a statement that an engineering company's voice should be precise, a little blunt, and available to everyone who builds with it.

## Using it today

- **Signals:** IBM and Carbon Design System, developer tools, data products, conference sites; reads "engineering, enterprise, considered". Saturation: moderate, popular with designers, not yet a template default.
- **Robotic ↔ humane:** 5/10, mechanical cuts and grotesque structure are cool; a true italic, double-storey g and frank, slightly quirky details add a human edge.
- **UI fitness:** body text, UI labels, dense data (Condensed), code (Mono); display works with −1% tracking at 40px+. Unusually wide script coverage across companion families.
- **Pairs with:** IBM Plex Serif or a sturdy transitional serif for long reading; Plex Mono for code; an expressive display face only for marketing headlines.

## Blends

- **Amplifies:** `corporate-identity`, `bloomberg-terminal`, rigorous information products.
- **Productive tension with:** `teenage-engineering`, corporate engineering voice in a playful hardware context.
- **Clashes with:** `art-nouveau`, engineered cuts against organic ornament.

## Don't copy

IBM's logo and brand assets; the "IBM Plex" name for modified versions (reserved).

## Study

- IBM Plex site and repository: https://www.ibm.com/plex/ and https://github.com/IBM/plex
- Bold Monday, IBM custom type case study: https://boldmonday.com/custom/ibm/
- IBM Carbon Design System, typography guidance.
