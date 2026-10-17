---
id: bloomberg-terminal
name: Bloomberg Terminal
type: system
discipline: [ui, ux, product]
era: 1982–present
origin: New York, USA
lineage: [command-line-and-teletext]
tags:
  mood: [dense, urgent, expert, nocturnal]
  topics: [finance, analytics, operations, trading, monitoring, developer tools]
axes: {order: 8, density: 10, ornament: 1, warmth: 2, contrast: 9, geometry: 9, chroma: 5, typevoice: 4, energy: 6, hand: 0, play: 1, era: 5}
---

# Bloomberg Terminal

**Essence:** An expert's instrument — black screens packed with amber data, reached by typed mnemonics and colour-coded keys, unchanged enough that muscle memory becomes a feature.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Dark field, coded colour | Black background with brightly coloured data; colour carries meaning (values, labels, up/down, input fields) rather than decoration. | Background `#000`; values amber (~`#FFA028`); labels white/grey; positive green, negative red; editable fields marked with a distinct fill. Write the colour semantics down and never reuse a colour for a second meaning. |
| G2 · Mnemonics as navigation | Every function is reachable by typing a short code and pressing GO; experts navigate without menus. | Each screen has a short mnemonic (≤5 letters) shown in its header; a global command line with autocomplete; Enter = go. Menus exist for discovery, commands for speed. |
| G3 · Density as respect | Screens show as much as possible at once, in tiled panels, with minimal padding — experts want comparison, not progressive disclosure. | 12–13 px monospaced/tabular numerals, row height ~18 px, four-panel tiled layout; no cards, no empty padding; wrap nothing that can be columnised. |
| G4 · Colour-coded keys | The custom keyboard colours keys by role: yellow market-sector keys, red cancel, green GO. | Carry hardware semantics into the screen: action chips coloured by category (yellow = domain/scope, green = execute, red = cancel/stop) consistently across shortcuts, buttons and docs. |
| G5 · Numbered choices | Menus list numbered items; typing the number selects. | Every list item gets a visible index; typing the index (plus Enter) activates it. Keyboard-first by construction. |
| G6 · Stability over fashion | Core interactions change slowly; users' memorised codes and layouts must keep working. | Never relocate a core command between releases; add, don't reshuffle; redesigns are opt-in with a long overlap. Colour-accessible schemes added as options, not forced swaps. |

## Visual facts

- **Color:** black `#000`, amber/orange data, white labels, green/red deltas, yellow highlights; colour-vision-deficiency schemes offered since a 2021 accessibility effort.
- **Type:** proprietary terminal fonts with tabular figures. Free: **IBM Plex Mono**, **JetBrains Mono**, **Roboto Mono** (all with clear tabular numerals).
- **Form:** text, rules, sparkline-like charts, tiny tables; no imagery.
- **Composition:** multi-panel tiling across several monitors; header line with mnemonic and security; dense tables below.

## Attitude

Bloomberg (founded 1981 as Innovative Market Systems; first terminals to Merrill Lynch in December 1982) built a tool for people whose time is money, then kept it consistent for decades. The design problem is managing complexity, not removing it. An unsolicited 2007 redesign concept (commissioned by a magazine, not Bloomberg) is a famous lesson: experts may prefer an "ugly" tool that never moves.

## Blends

- **Amplifies:** `command-line-and-teletext`, `swiss-international` — grids, tables, typed navigation.
- **Productive tension with:** `editorial-web` — narrative framing over dense data produces data journalism and readable analytics.
- **Clashes with:** `ios-7-flat` — ultralight type, generous whitespace and hairlines dissolve in a density-first screen.

## Don't copy

- The Bloomberg wordmark and logo, the Bloomberg keyboard design, specific function screens and their layouts.

## Study

- Tech at Bloomberg, "Designing the Terminal for Color Accessibility" (techatbloomberg.com, 2021).
- *IEEE Spectrum* history of the Bloomberg Terminal; Michael Bloomberg, *Bloomberg by Bloomberg* (1997).
- Dominique Leca, "The Impossible Bloomberg Makeover," *UX Magazine* (2010) — on the 2007 redesign concepts.
