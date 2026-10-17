---
id: caslon
name: Caslon
type: typeface
discipline: [graphic, ui]
era: 1720s to 1760s; revivals 1990 to 2014
origin: London, England
lineage: [william-caslon, garamond]
tags:
  mood: [sturdy, plainspoken, warm, trustworthy]
  topics: [civic, publishing, news, heritage-brands, education]
axes: {order: 5, density: 6, ornament: 2, warmth: 7, contrast: 5, geometry: 3, chroma: 1, typevoice: 4, energy: 3, hand: 5, play: 2, era: 1}
---

# Caslon

**Essence:** The workmanlike English old-style. Its rhythm is a little uneven, its italic lively, and it reads as dependable, public and plainly spoken.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Uneven, comfortable texture | Caslon's letters vary slightly in width and set, so a paragraph has a hand-made shimmer and no mechanical regularity. | Use it as the long-reading voice in civic, publishing or member products: Libre Caslon Text at 17 to 19px / 1.5. Keep geometric precision for the chrome so the content surface alone feels human. |
| G2 · Every size drawn differently | Caslon cut each size separately: small sizes sturdier and wider, large sizes finer. Founder's Caslon and Big Caslon digitize that difference. | Two tokens, never one: `serif-text` (Libre Caslon Text, Adobe Caslon) ≤ 24px and `serif-display` (Libre Caslon Display, Big Caslon) ≥ 32px. Enlarging a text cut to hero size looks blunt and loose. |
| G3 · Lively italic with swash capitals | The italic has varied slopes and swash capitals, so it reads as a voice rather than a slanted copy of the roman. | One italic word per headline at most. Swash capitals (`font-feature-settings: "swsh"`) only as display initials ≥ 48px, never in running text or UI. |
| G4 · The public record | Most of the type in the first printing of the Declaration of Independence (Dunlap broadside, 1776) is thought to have come from Caslon's foundry. It became the voice of colonial and civic print. | Statements of record (charters, founders' letters, terms summaries, public notices) are set in a Caslon text cut. Interaction (buttons, forms, nav) stays in a plain sans, so "record" and "action" never mix. |

## Visual facts

- **Classification:** English old-style (Garalde) serif with Dutch baroque influence.
- **Origin:** William Caslon I, London; romans cut from the 1720s, broadside specimen 1734; the foundry continued under his heirs.
- **Main digital versions:** Adobe Caslon (Carol Twombly, 1990, from Caslon's own specimens; commercial). Big Caslon (Matthew Carter, 1994, display, drawn from the large sizes; ships with macOS). ITC Founder's Caslon (Justin Howes; separate digitizations of 12, 30 and 42 pt and poster sizes; commercial).
- **Anatomy:** moderate x-height, short descenders, bracketed serifs, near-vertical stress, wide capitals, moderate contrast; the italic is steep and irregular.
- **Free / open alternatives:** Libre Caslon Text and Libre Caslon Display (Pablo Impallari and Rodrigo Fuenzalida, 2012 to 14, OFL). The text cut is tuned for 16px web body and keeps the uneven texture. Both are on Google Fonts.

## Attitude

Caslon was never trying to be new. It served printers and readers so reliably that it became the default of a century. The lesson: modest, robust and readable beats remarkable, and a type can earn trust by refusing to show off.

## Using it today

- **Signals:** 18th-century English books, American founding documents, heritage institutions. Printers had an old rule of reaching for Caslon when unsure. It is under-used on screen compared with Garamond, so it still feels fresh in product UI.
- **Robotic ↔ humane: 8/10.** Irregular widths, bracketed serifs, ball terminals on *a* and *c*, and a jaunty italic. Firmer and more upright than Garamond, so slightly less soft.
- **UI fitness:** body text yes (Libre Caslon Text ≥ 17px); display yes with a display cut; labels no, because the hairlines and short x-height blur at 12 to 14px. Rendering: test Adobe Caslon on 1× Windows, where the hairlines break up. Coverage: mostly Latin; check Cyrillic and Greek before committing.
- **Pairs with:** Public Sans (open, from the US Web Design System) or Libre Franklin for interface, a civic American pairing. Big Caslon or Libre Caslon Display for headlines. IBM Plex Mono for data and references.

## Blends

- **Amplifies:** `william-caslon` and `arts-and-crafts`: the private-press revival leaned on old-style warmth.
- **Productive tension with:** `brutalist-web`: raw, unstyled HTML structure with a Caslon reading face gives honest form with a human voice.
- **Clashes with:** `bodoni`: machined contrast beside gentle irregularity makes both look wrong.

## Don't copy

Facsimiles of the Dunlap broadside or the 1734 specimen sheet as page templates; Big Caslon and Adobe Caslon outlines without a licence.

## Study

- Caslon specimen sheet, 1734 (St Bride Library, London).
- Fonts In Use, "The Dunlap Broadside": fontsinuse.com/uses/1666/the-dunlap-broadside
- Libre Caslon Text: fontsinuse.com/typefaces/230964/libre-caslon-text
- Johnson Ball, *William Caslon 1693 to 1766* (1973).
