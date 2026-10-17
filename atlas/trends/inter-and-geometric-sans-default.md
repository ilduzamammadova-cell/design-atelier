---
id: inter-and-geometric-sans-default
name: Inter & Geometric Sans Default
type: trend
discipline: [ui, graphic]
era: 2017 to 2026
origin: Global, Inter by Rasmus Andersson (begun at Figma, released 2017); Google Fonts geometric-sans wave
lineage: [swiss-international]
tags:
  mood: [neutral, clean, safe, anonymous]
  topics: [saas, dashboards, developer-tools, ai-products, everything]
axes: {order: 7, density: 5, ornament: 0, warmth: 3, contrast: 4, geometry: 7, chroma: 3, typevoice: 1, energy: 2, hand: 0, play: 2, era: 6}
saturation: 10
---

# Inter & Geometric Sans Default

**Essence:** Inter, or its cousins Geist, DM Sans, Plus Jakarta Sans, Manrope, Space Grotesk, Poppins, set everywhere (UI, headlines, wordmark) because no one made a typographic decision.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Small-size legibility | Inter's tall x-height and open apertures keep 11 to 14px UI text crisp. | Keep a legibility-first face for dense UI (tables, labels, forms) but pair it with a display face that carries the brand; test at 12px with `tabular-nums` for data. |
| G2 · Neutral carrier | A quiet face lets content and data speak. | Make neutrality a choice: pick a less-default workhorse (IBM Plex Sans, Source Sans 3, Public Sans, Atkinson Hyperlegible, Instrument Sans) and write one line on why. |
| G3 · Wide coverage | Free, variable, many scripts, good hinting. | Put coverage in the type brief (scripts, weights, `opsz`) and choose among faces that pass, coverage is a filter, not a style. |

## Why it reads as slop now

Inter was drawn by Rasmus Andersson for screen UI, released openly in 2017 under the SIL Open Font License, and adopted by GitHub, Mozilla and thousands of products; version 4.0 (2023) added optical sizes. It is genuinely excellent, which is why it became the zero-decision choice of Figma files, Tailwind templates, shadcn/ui demos and AI generators. Anthropic's November 2025 frontend-design article names Inter, Roboto, Arial and system fonts as overused defaults and notes that models then converge on the next default, Space Grotesk. The cheap version: Inter 600 at −2% tracking for the headline, Inter 400 for body, Inter in the wordmark, a page with no typographic voice.

## Subvert

- **Two-face rule.** Keep a neutral face for UI text and give display type real character, a serif, a quirky grotesque, a mono, a revival, chosen from the brand idea.
- **Choose from history.** Take a typeface lineage from an atlas source (a Swiss grotesk for rigor, a humanist sans for warmth, a slab for industrial clarity) and state the reason in the style spec.
- **Customise the default.** If Inter stays, make it yours: character variants (`cv11` single-storey a, `ss01` open digits), tabular numerals, an unusual weight pairing (300 + 800), a modified wordmark.

## Visual facts

- **Color:** n/a (a type default); usually #111 on white or #EDEDED on near-black.
- **Type:** Inter, Inter Display, Geist, DM Sans, Manrope, Plus Jakarta Sans, Space Grotesk, Poppins, Roboto.
- **Form:** tight negative tracking at large sizes, 600 to 700 headline weights, uniform x-heights.
- **Composition:** one family at every level; hierarchy by size and weight only.

## Attitude

Type should be invisible infrastructure. Respectable for a system font; as a brand choice it says "we did not choose".

## Blends

- **Amplifies:** `shadcn-tailwind-default-look`, `purple-blue-gradient-saas`, `centered-hero-three-cards-template`.
- **Productive tension with:** `editorial-serif-revival`, `paula-scher`, a voiced display face over a neutral UI face is the classic fix.
- **Clashes with:** `y2k-chrome-and-acid`, a bland carrier drains a maximalist voice; the mix reads as a template wearing a costume.

## Don't copy

Not an artifact problem (Inter is open source), the risk is sameness. Do not reuse well-known Inter-set wordmarks.

## Study

- Figma blog, "The birth of Inter", figma.com/blog/the-birth-of-inter
- rsms.me/inter, specimen and OpenType features (`cv`, `ss`, `opsz`).
- Anthropic, "Improving frontend design through Skills" (Nov 2025), font convergence in AI output.
- Google Fonts Knowledge (fonts.google.com/knowledge), choosing and pairing type.
