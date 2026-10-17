---
id: palatino
name: Palatino
type: typeface
discipline: [graphic, ui]
era: 1949 to 1950; digital 1999 to 2013
origin: Frankfurt, West Germany (D. Stempel AG)
lineage: [hermann-zapf, aldus-manutius]
tags:
  mood: [calligraphic, open, assured, scholarly]
  topics: [publishing, academia, culture, documentation, hospitality]
axes: {order: 6, density: 5, ornament: 2, warmth: 7, contrast: 4, geometry: 4, chroma: 1, typevoice: 4, energy: 3, hand: 5, play: 2, era: 3}
---

# Palatino

**Essence:** A calligrapher's Renaissance roman for the 20th century. It is broad, open and pen-shaped, made to stay legible on rough paper and at a distance, and it ended up on nearly every computer.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · The broad nib inside the type | Zapf, a calligrapher, let the pen's angle and lift show in the letters. Each form feels written rather than constructed. | Where text should feel authored by a person (founders' letters, handwritten-style notes, certificates, menus): Palatino-class text at 16 to 20px. The UI chrome around it stays neutral so the "hand" is reserved for voice. |
| G2 · Wide, open forms | Open counters and generous proportions keep letters clear in poor printing and at small sizes, at the cost of width. | A robust serif for small screens: 15 to 17px body with a 50 to 65ch measure. Because it sets wide, budget about 10% fewer characters per line than a Times-class face when planning layouts. |
| G3 · A family planned as a system | Around Palatino, Zapf drew Aldus (a lighter book face), Michelangelo and Sistina (titling capitals), and later Palatino Sans and Palatino Arabic. | Build a superfamily of tokens from one design DNA: text serif, titling caps and companion sans with matching x-height and stroke logic. Prefer a family that already has these over mixing unrelated faces. |
| G4 · Provenance over lookalikes | Close clones (e.g. Book Antiqua) circulated widely; URW Palladio became the first legal free version and the base for open derivatives. | Licensing hygiene: use the original or an official open release (TeX Gyre Pagella), never an unlicensed clone. Record source, licence and version on every font asset. |
| G5 · A screen-specific cut | Palatino eText (2013) adapted the design for e-readers and screens. | Where a "screen" or "text" cut exists, map it to sizes ≤ 16px. Keep the print/display cut for larger sizes: one family, two renderings. |

## Visual facts

- **Classification:** humanist old-style (Aldine-influenced, but a new design rather than a revival).
- **Origin:** Hermann Zapf, named after the 16th-century Italian writing master Giambattista Palatino; issued by D. Stempel AG, Frankfurt, from 1949 to 50 and distributed by Linotype.
- **Main digital versions:** Palatino (Linotype; a PostScript core font, preinstalled on macOS). Palatino Linotype (1999, bundled with Windows 2000 onward, extended Greek and Cyrillic). Palatino nova (2005), Palatino Sans (2006), Palatino Arabic, Palatino eText (2013). All commercial; Book Antiqua (Monotype) is a lookalike.
- **Anatomy:** open counters, moderately large x-height for an old-style, calligraphic stroke modulation, moderate contrast, broad proportions, lively italic.
- **Free / open alternatives:** TeX Gyre Pagella (GUST font licence; derived from URW Palladio) and P052 (URW++ base 35, AGPL with an embedding exception).

## Attitude

Zapf believed the calligrapher's knowledge was the best guide for any new technology, from metal to film to digital type. Palatino is tradition reread as a modern tool: humane, sturdy and not nostalgic.

## Using it today

- **Signals:** preinstalled on Macs and Windows, so it shows up in academic theses, LaTeX papers (via Pagella), restaurant menus and self-published books. Saturation is moderate; it reads as learned, slightly 1990s desktop-publishing.
- **Robotic ↔ humane: 8/10.** Pen-angle modulation, open apertures, a written italic and slightly irregular widths. Firm serifs and confident proportions keep it from feeling casual.
- **UI fitness:** body text yes (≥ 16px); labels acceptable ≥ 14px; display good. The wide set needs layout room on mobile. Coverage: Palatino Linotype covers Latin, Greek and Cyrillic; check Vietnamese and other scripts per version.
- **Pairs with:** Optima, by the same designer, for headings and UI, a harmony of pen and flare. A neutral humanist sans (Frutiger, or open Source Sans 3) for dense controls. IBM Plex Mono for code in technical papers.

## Blends

- **Amplifies:** `optima` and `hermann-zapf`: one calligrapher's system across serif and sans.
- **Productive tension with:** `bauhaus`: a pen-made roman inside primary-colour geometric compositions gives human text in a constructed world.
- **Clashes with:** `eurostile`: squircle technology type beside calligraphic modulation pulls in opposite directions.

## Don't copy

Palatino outlines and clones (Book Antiqua and others) in brand marks without licence; Zapf's *Manuale Typographicum* pages.

## Study

- Hermann Zapf, *Manuale Typographicum* (1954; 1968) and *About Alphabets* (1960).
- Linotype / MyFonts, Palatino nova and Palatino eText notes (myfonts.com).
- TeX Gyre Pagella documentation (gust.org.pl/projects/e-foundry/tex-gyre).
