---
id: garamond
name: Garamond
type: typeface
discipline: [graphic, ui]
era: 1540s; revivals 1917 to 2011
origin: Paris, France
lineage: [claude-garamond, aldus-manutius]
tags:
  mood: [literary, graceful, quiet, classical]
  topics: [publishing, reading-apps, culture, education, luxury]
axes: {order: 6, density: 5, ornament: 2, warmth: 7, contrast: 4, geometry: 3, chroma: 1, typevoice: 3, energy: 2, hand: 4, play: 2, era: 1}
---

# Garamond

**Essence:** The Renaissance book voice. Slanted stress, a small x-height and long ascenders make a page read as literature before a single word has been taken in.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Pen-angle stress | The thickest part of each curve sits on a diagonal, as if drawn with a broad nib. That gives the line a written pulse that geometric faces lack. | Reserve it for reading surfaces where a human voice matters (essays, letters, long help articles). Body 18 to 20px web / 17pt app, line-height 1.5 to 1.6, measure 60 to 70ch. Never for dense chrome. |
| G2 · Small x-height, long extenders | The lowercase is short and the ascenders tall, so lines look airy and the paragraph has a strong vertical rhythm. | Set Garamond one step larger than its sans partner so x-heights match (sans 16px ↔ Garamond 18 to 19px). Use `font-size-adjust` on the stack so fallbacks keep the same apparent size. |
| G3 · Two voices: roman and cursive | Garamond's romans were later married to Robert Granjon's italics: a narrower, faster cursive that works as a second speaker. | Make italic a semantic channel: titles of works, quoted speech, a second narrator (e.g. the assistant's aside versus the user's text). Always load the true italic file; synthetic obliques are banned. |
| G4 · Delicate details need a display cut | The small eye of the *e* and fine serifs sparkle when large and clog when small. | Two tokens: `serif-text` (EB Garamond, Garamond Premier text) ≤ 24px; `serif-display` (Cormorant Garamond, Premier Display) ≥ 40px with −1% tracking. Never scale the text cut up to hero size. |
| G5 · Numerals as lowercase | Renaissance type had no lining figures. Numbers rise and fall like letters and disappear into prose. | Prose uses `font-variant-numeric: oldstyle-nums proportional-nums`. Tables, prices and codes switch to `lining-nums tabular-nums`, or to the sans. |

## Visual facts

- **Classification:** French Renaissance old-style (Garalde) serif.
- **Origin:** punches by Claude Garamond (Garamont), Paris, active c. 1540 to 1561, following Aldus Manutius's roman of c. 1495. Many 20th-century "Garamonds" actually copy Jean Jannon's types (specimen 1621): ATF Garamond (c. 1917) and Monotype Garamond (1922 to 23, bundled with Microsoft Office). Stempel Garamond (1920s) and Sabon (Jan Tschichold, 1967) follow genuine Garamond material.
- **Main digital versions:** Adobe Garamond (Robert Slimbach, 1989) and Garamond Premier (2005, four optical sizes, Greek and Cyrillic), both commercial from Adobe. ITC Garamond (Tony Stan, 1970s) is commercial and has a much larger x-height. It was the basis of Apple Garamond.
- **Anatomy:** low x-height, long extenders, wide open apertures, cupped bracketed serifs, moderate contrast; the italic is narrow and steep.
- **Free / open alternatives:** EB Garamond (Georg Duffner, 2011, OFL; drawn from the 1592 Egenolff-Berner specimen) for text. Cormorant Garamond (Christian Thalmann, OFL) for display only, since its fine details break up below about 20px.

## Attitude

Garamond wants to disappear into reading. Its beauty is the evenness of a whole paragraph, not any single letter. Using it borrows the authority of the book, so it only rings true when real writing stands behind it.

## Using it today

- **Signals:** books, literary publishing, universities. Apple's condensed Apple Garamond ran from 1984 into the early 2000s, and the Harry Potter hardcovers were set in Adobe Garamond. It is saturated in book publishing, and EB and Cormorant Garamond now show up constantly in "elegant" web templates for weddings and wellness.
- **Robotic ↔ humane: 8/10.** The diagonal stress, open apertures, cupped serifs, slightly varied widths and handwritten italic all read as human. It loses points for its courtly formality.
- **UI fitness:** good for body text (≥ 18px) and display if you use a display cut. Poor for UI labels: at 12 to 14px the small x-height turns muddy, especially on 1× Windows screens. Check Greek and Cyrillic per revival; Premier has both, many free cuts are uneven.
- **Pairs with:** a humanist sans for interface (Source Sans 3, Frutiger), since both come from calligraphy. A geometric sans (Futura, or the open Jost) for modernist contrast; Vignelli kept both in his short list. A mono (IBM Plex Mono) for data.

## Blends

- **Amplifies:** `aldus-manutius`: the italic-as-second-voice gene comes straight from the Aldine book.
- **Productive tension with:** `swiss-international`: Renaissance text in an asymmetric modular grid gives literary warmth with modern structure.
- **Clashes with:** `neo-brutalism-web`: thick black borders and hard shadows make Garamond's finesse look like a costume.

## Don't copy

The Apple Garamond wordmark style; the commercial outlines of Adobe Garamond, Garamond Premier and ITC Garamond without a licence; Harry Potter book typography as a template.

## Study

- Beatrice Warde (as "Paul Beaujon"), "The 'Garamond' Types", *The Fleuron* 5 (1926): the article that untangled Jannon from Garamond.
- Museum Plantin-Moretus, Antwerp: surviving 16th-century punches and matrices.
- Adobe's Garamond Premier specimen; EB Garamond repository (github.com/georgd/EB-Garamond).
- Fonts In Use: fontsinuse.com, search "Garamond" for revivals compared in real work.
