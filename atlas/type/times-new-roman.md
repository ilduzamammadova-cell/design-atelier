---
id: times-new-roman
name: Times New Roman
type: typeface
discipline: [graphic, ui]
era: 1931–1932
origin: London, England
lineage: [garamond]
tags:
  mood: [efficient, neutral, institutional, compact]
  topics: [news, academia, law, government, documents]
axes: {order: 7, density: 8, ornament: 1, warmth: 4, contrast: 6, geometry: 6, chroma: 1, typevoice: 2, energy: 3, hand: 1, play: 1, era: 3}
---

# Times New Roman

**Essence:** A newspaper's economy turned into the world's default document. It is compact, crisp and so familiar that it reads as "no choice was made", which is both its weakness and its power.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Economy of the column | Built for *The Times*: a high x-height with relatively condensed letters and short descenders, so more words fit a narrow column and leading can stay tight. | Dense reading layouts (news lists, citations, footnotes, transcripts): 15–16px / 1.35 in 35–45ch columns. Choose it, or a descendant, when characters per line is the hard constraint. |
| G2 · Sharpened contrast | Morison and Lardent started from Monotype's Plantin but raised the contrast and sharpened the serifs for a crisper page. | Crisp on 2× screens. On 1× and Windows keep text ≥ 16px or swap to a screen-hinted metric twin (Tinos). Never below 13px, where the hairlines dissolve. |
| G3 · The invisible default | Shipped with every Windows since 3.1 and long the word-processor default, it signals "unstyled document". | Use deliberately or not at all. As a deadpan signal (official record, raw document preview, anti-design brand), set it on purpose with tight margins. Otherwise define full font stacks so browsers never fall back to Times by accident. |
| G4 · Metric twins as infrastructure | Liberation Serif, Tinos and Nimbus Roman share its character widths, so documents reflow identically across systems. | For editors, PDF generation and document products, choose a body face with an open metric twin and declare it: `font-family: "Times New Roman", Tinos, "Liberation Serif", serif`. Page breaks then match on every OS. |
| G5 · Type cut to a publication's brief | Morison criticised *The Times*'s old type, and the new face was drawn to fix measured problems of space and clarity. | Write a type brief from real constraints before choosing (column width, chars per line, smallest size, rendering targets, scripts). Evaluate candidates against it, not against a mood board. |

## Visual facts

- **Classification:** transitional / "modernized old-style" newspaper serif.
- **Origin:** Stanley Morison (Monotype's typographic adviser) with Victor Lardent of *The Times* advertising department, based on Monotype Plantin. Released 1931 and first used by *The Times* on 3 October 1932. The paper itself left it in 1972.
- **Main digital versions:** Monotype Times New Roman (bundled with Windows; the current version adds small caps and text figures). Linotype Times / Times Roman (a PostScript core font, preinstalled on macOS). Both commercial and pre-licensed with the OS.
- **Anatomy:** high x-height, short descenders, condensed for its x-height, sharp bracketed serifs, fairly high contrast, steep compact italic.
- **Free / open alternatives:** Liberation Serif (Red Hat; OFL from version 2.0; metric-compatible), Tinos (Google's Croscore fonts, Apache 2.0; metric-compatible), TeX Gyre Termes (GUST font licence), Nimbus Roman (URW++ base 35, AGPL with an embedding exception).

## Attitude

Morison wanted a type that served the newspaper's economics and its readers without calling attention to itself. Its afterlife as the computer default proves the point too well: neutrality can become invisibility, and invisibility can become a statement.

## Using it today

- **Signals:** Word documents, school and academic papers (suggested by APA style), legal filings, governments. The US State Department used it from 2004 to 2023, switched to Calibri, and returned to it in 2025. The Australian Government wordmark is set in Times New Roman Bold. It is totally saturated and therefore nearly invisible, reading as "official" or "unstyled".
- **Robotic ↔ humane: 4/10.** Compact regular rhythm, sharp serifs, stiff vertical texture. The italic and bracketed serifs keep some old-style warmth.
- **UI fitness:** body text in documents ≥ 16px; poor for UI labels (thin strokes at 12–13px on 1×); generic and brittle as display. Coverage is a strength: the Windows version covers Latin, Greek, Cyrillic, Hebrew, Arabic and Vietnamese.
- **Pairs with:** a grotesque sans for headings, the classic newspaper and document pairing (Helvetica, Arial, or open Archivo). Courier Prime for drafts and annotations, a typewriter-to-print lineage. A mono (IBM Plex Mono) for code in technical papers.

## Blends

- **Amplifies:** `editorial-web`: dense, citation-heavy reading pages are its home turf.
- **Productive tension with:** `brutalist-web`: the default serif on raw HTML, used knowingly, is an anti-design signature, honest and deadpan.
- **Clashes with:** `psychedelic`: vibrating colour and melting forms against the most bureaucratic face reads as accident, not intent.

## Don't copy

*The Times* masthead and page layouts; Monotype and Linotype outlines outside their bundled licences; the Australian Government wordmark.

## Study

- *Printing The Times* (The Times, 1932): the paper's own record of the 1932 change.
- Microsoft Typography, Times New Roman font page (learn.microsoft.com/typography).
- Fonts In Use, Times New Roman: fontsinuse.com (search "Times New Roman").
- Liberation fonts project (github.com/liberationfonts).
