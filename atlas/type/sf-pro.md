---
id: sf-pro
name: SF Pro (San Francisco)
type: typeface
discipline: [graphic, ui]
era: 2015 to present
origin: Cupertino, USA, Apple
lineage: [ios-7-flat, helvetica]
tags:
  mood: [precise, neutral, refined, platform]
  topics: [ios, macos, wearables, consumer-apps, system-ui]
axes: {order: 9, density: 5, ornament: 0, warmth: 4, contrast: 4, geometry: 7, chroma: 4, typevoice: 1, energy: 2, hand: 0, play: 2, era: 7}
---

# SF Pro (San Francisco, 2015)

**Essence:** A system typeface engineered as a size-aware instrument, the shapes and spacing change automatically with point size, so the reader never notices the type working.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Automatic optical sizes | SF Pro switches from Text (below 20pt: looser spacing, sturdier strokes, larger counters) to Display (20pt and up: tighter, finer) automatically. | Use a face with an `opsz` axis and `font-optical-sizing: auto`; if you only have static fonts, keep two families (Text ≤ 19px, Display ≥ 20px) and switch at the same threshold. |
| G2 · Size-specific tracking | Apple publishes a tracking table: small text is spaced open, large text tight. Tracking is a function of size, not a style choice. | Encode tracking per size in tokens: 11px +0.6%, 13px +0.2%, 17px −0.4%, 28px −0.8%, 34px+ −1% (tune per face). Never one global letter-spacing. |
| G3 · Born on the smallest screen | San Francisco debuted on the Apple Watch; its SF Compact cut flattens round sides to add space between letters at tiny sizes. | Design the smallest context first: set labels at your minimum (11 to 12px) on the smallest device, fix legibility there, then scale up. Flatter rounds and more open spacing at small sizes. |
| G4 · One family, many widths and roles | Weights × widths (Condensed, Compressed, Expanded), SF Rounded, SF Mono and the New York serif give one coherent system with defined roles. | Build a small, role-locked family: Text for UI, Display for titles, a rounded variant only for playful/wellness contexts, mono for code and numbers (`tnum`). Document which role may use which width. |

## Visual facts

- **Classification:** neo-grotesque system UI face.
- **Designer · year · foundry:** Apple's in-house type team; introduced with the Apple Watch (2014 to 15), system font on iOS 9 and OS X El Capitan (2015), replacing Helvetica Neue.
- **Digital versions & licences:** SF Pro, SF Compact, SF Mono, SF Rounded, SF Arabic and other script companions; New York serif (2019). Licensed for designing and developing apps for Apple platforms only, not for general brand or web use; on the web reach it via `system-ui` / `-apple-system`.
- **Proportions:** large x-height, medium apertures, straight-sided rounds (a rounded-rectangle feel), low contrast; Text and Display optical sizes; variable weight/width/optical size.
- **Free / open alternatives (keep the gene):** Roboto Flex (OFL, optical size, width and grade axes); Google Sans Flex (OFL since Nov 2025, optical size axis). Or simply use `font-family: system-ui` to let each platform supply its tuned face.

## Attitude

Apple treats the system font as part of the hardware experience: legibility, density and polish are engineered, measured and owned. The belief is that type should be invisible because it is perfectly adapted.

## Using it today

- **Signals:** every iPhone, Mac and Watch since 2015; reads "Apple-native, premium-neutral". Saturation: total on Apple platforms; outside them, using it reads as copying Apple.
- **Robotic ↔ humane:** 4/10, engineered, square-ish rounds and uniform strokes; humane only in its care for size and spacing. Italics are mostly obliques; SF Rounded adds softness.
- **UI fitness:** the reference for UI text on Apple platforms from 11pt labels to large titles; follow Dynamic Type sizes. Covers Latin, Greek, Cyrillic plus companion script families.
- **Pairs with:** New York (its serif sibling) for reading; SF Mono for code and numbers; a single brand display face for marketing only, never inside native UI chrome.

## Blends

- **Amplifies:** `ios-7-flat`, `jonathan-ive`, `dieter-rams`, reduction and engineered polish.
- **Productive tension with:** `editorial-web`, a system sans for chrome under expressive editorial headings.
- **Clashes with:** `classic-macintosh`, pixel-bitmap charm vs optical-size perfection; mixing looks unresolved.

## Don't copy

SF font files outside Apple's licence; never embed SF in websites, Android apps or brand assets.

## Study

- Apple Developer, Fonts: https://developer.apple.com/fonts/
- Apple Human Interface Guidelines, Typography (tracking tables, Dynamic Type): https://developer.apple.com/design/human-interface-guidelines/typography
- WWDC 2015 session "Introducing the New System Fonts"; WWDC 2020 "The details of UI typography".
