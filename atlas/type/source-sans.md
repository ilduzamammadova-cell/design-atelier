---
id: source-sans
name: Source Sans (Source Sans 3)
type: typeface
discipline: [graphic, ui]
era: 2012–present
origin: San Jose, USA — Adobe (Paul D. Hunt)
lineage: [franklin-gothic]
tags:
  mood: [clear, unfussy, open, scholarly]
  topics: [user-interfaces, documentation, government, open-source, publishing]
axes: {order: 8, density: 5, ornament: 0, warmth: 6, contrast: 3, geometry: 5, chroma: 3, typevoice: 2, energy: 2, hand: 1, play: 2, era: 6}
---

# Source Sans (2012)

**Essence:** Adobe's first open-source family — American gothic clarity with humanist openness, drawn for interfaces and long reading alike.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Gothic clarity, humanist openness | Paul Hunt simplified forms in the spirit of Benton's American gothics (News Gothic, Franklin Gothic) but kept open apertures and a gentle humanist rhythm. | For interfaces that are mostly reading (docs, settings, forms) pick a slightly narrow, open sans: body 16/24, labels 13/18 at 600; the narrower width fits more words per line without crowding. |
| G2 · Fix confusables from feedback | Early users asked for a distinct l; Hunt reshaped it with a tail so it differs from capital I. | Run a "confusables audit" on any adopted face: Il1, O0, rn/m, cl/d at 12–14px. If it fails, use OpenType alternates or switch faces for codes and inputs. |
| G3 · Open source as design system | Released under the SIL OFL with sources on GitHub; extended into Source Serif and Source Code — a coordinated, open superfamily. | Choose a superfamily with matched sans/serif/mono members for a design system: shared x-height and weight range, so `ui-text`, `reading-text` and `code` tokens align on one baseline grid. |
| G4 · Modest x-height, calm colour | It sets visually smaller than Open Sans-class faces at the same size, giving a calmer, more bookish page. | Size it up one step: if your scale was tuned on a large-x-height face, add +1px to body and labels (16 → 17, 12 → 13) and recheck line lengths. |

## Visual facts

- **Classification:** humanist-gothic sans (grotesque structure, humanist apertures).
- **Designer · year · foundry:** Paul D. Hunt, Adobe; announced 2 August 2012 as Adobe's first open-source type family.
- **Digital versions & licences:** Source Sans Pro (2012) renamed Source Sans 3 in 2021 (more Greek and Cyrillic, variable fonts); SIL OFL. Companions: Source Serif 4, Source Code Pro, Source Han Sans (CJK).
- **Proportions:** modest x-height, slightly narrow, open apertures, low contrast, tailed l; true italic with cursive touches.
- **Free / open alternatives (keep the gene):** Public Sans and Libre Franklin (OFL — same American-gothic root); Fira Sans (OFL — more humanist, wider).

## Attitude

Source Sans reflects a belief that a type company should contribute a well-crafted commons — fonts that anyone can study, improve and ship. Clarity, openness and maintenance are the design.

## Using it today

- **Signals:** open-source projects, government and academic sites, documentation, Adobe's own UIs; reads "competent, open, unbranded". Saturation: moderate — common but not tired.
- **Robotic ↔ humane:** 7/10 — open apertures, gentle rhythm and a true italic make it feel humane; gothic simplification keeps it sober.
- **UI fitness:** body text, UI labels, data tables (enable `tnum`); display acceptable in heavier weights. Latin, Greek, Cyrillic, Vietnamese; Source Han Sans for CJK.
- **Pairs with:** Source Serif 4 for long reading (matched metrics); Source Code Pro for code; a geometric or high-contrast display face for marketing headlines.

## Blends

- **Amplifies:** `inclusive-design`, `edward-tufte` — clear, evidence-first presentation.
- **Productive tension with:** `paula-scher` — expressive display scale above disciplined body text.
- **Clashes with:** `y2k-chrome-and-acid` — sober gothic cannot carry that maximalism.

## Don't copy

Not an artifact problem (OFL); keep the Reserved Font Name rules if you modify it.

## Study

- Adobe Typekit blog, "Source Sans Pro: Adobe's first open source type family" (2012): https://blog.typekit.com/2012/08/02/source-sans-pro
- GitHub, adobe-fonts/source-sans (release notes, design changes).
- Adobe Fonts, Source Sans 3 specimen.
