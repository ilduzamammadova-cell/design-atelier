---
id: linear-style-dark-ui
name: Linear-Style Dark UI
type: trend
discipline: [ui, ux]
era: 2020–2026
origin: San Francisco, USA (Linear, founded 2019) → dev-tool and AI startups worldwide
lineage: [swiss-international, inter-and-geometric-sans-default]
tags:
  mood: [focused, premium, technical, cool]
  topics: [developer-tools, productivity, project-management, ai-products]
axes: {order: 8, density: 6, ornament: 3, warmth: 2, contrast: 6, geometry: 8, chroma: 2, typevoice: 4, energy: 4, hand: 0, play: 2, era: 8}
saturation: 9
---

# Linear-Style Dark UI

**Essence:** The "built for engineers" look: near-black canvas, hairline borders, small Inter type, headlines fading white-to-gray, a perspective-tilted product screenshot glowing at the bottom of the hero, keyboard shortcuts everywhere.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Luminance ladder | Hierarchy from 4–5 gray steps on dark, not from color. | Surfaces as a ladder: bg #08090A, raised #121314, hover #1A1B1E, border #23252A, text-2 #8A8F98, text-1 #F7F8F8. Color appears only for status and selection. |
| G2 · Speed as aesthetic | Instant transitions and keyboard-first interaction make the product feel fast — the feel *is* the brand. | Every primary action has a shortcut shown in an 11px kbd chip; transitions ≤120ms; a ⌘K command palette indexes all actions. |
| G3 · Product as hero | The marketing page shows the real app, large, rather than illustrations. | Hero visual = a real screen at 1:1 crispness, cropped to its most informative region, with 2–3 annotations instead of a glow. |
| G4 · Calm density | Much information in small, quiet type without crowding. | App body 13/20 at weight 500, 4px spacing base, 32px rows; alignment, not borders, carries structure. |

## Why it reads as slop now

Linear's product and site (from around 2020) turned its users' preference for dark, fast tools into a brand. Anthony Hobday's January 2023 critique already observed sites with no reason to be dark adopting it; designer Daryl Ginn's label "the Linear effect" stuck. By 2024 every dev tool, AI agent and analytics startup had the same hero: fading gradient headline, soft violet glow, tilted app screenshot, logo strip. AI site generators amplified it because it is the median of recent SaaS pages. Linear itself has since dialled color back. The cheap version: a dark page whose "product shot" is a fake dashboard with placeholder charts, gradient text fading to unreadable gray, and no keyboard affordances at all.

## Subvert

- **Light mode with the same discipline.** Keep the luminance ladder and density, inverted to paper (#FBFBFA) and ink — rarer now, rigor intact.
- **Show the speed, don't style it.** Replace the glowing screenshot with a 6-second real interaction loop (keypress → result) and a visible shortcut overlay.
- **Pick a non-tech material.** A dark UI can be warm and specific: espresso ground #1B1410, cream text, one brass accent — the rigor stays, the genre signal goes.

## Visual facts

- **Color:** #08090A–#101012 grounds, grays #8A8F98 / #D0D6E0, one desaturated violet-blue accent (around #5E6AD2) used sparingly; headline gradients white → 40% gray.
- **Type:** Inter / Inter Display, negative tracking on large sizes (−2% to −4%), 13–14px UI text.
- **Form:** 1px borders at ~8% white, 6–12px radii, inner highlights, blurred light streaks.
- **Composition:** centered hero → tilted product image → logo strip → feature rows with screenshots.

## Attitude

Professional software should feel like a precision instrument: quiet, fast, dense, undecorated. The belief is sound; the trend copies the darkness and the glow, not the speed and care.

## Blends

- **Amplifies:** `dark-mode-neon-glow`, `bento-grid`, `dot-grid-and-line-grid-backgrounds`, `shadcn-tailwind-default-look`.
- **Productive tension with:** `wim-crouwel` — systematic, grid-built type for technical audiences pushes the rigor into a distinctive letterform voice instead of default Inter.
- **Clashes with:** `corporate-memphis-illustration` — cartoon warmth undercuts the instrument metaphor.

## Don't copy

Linear's logo, homepage hero, app layout, brand violet and changelog design.

## Study

- Anthony Hobday, "A critique of the Linear website" (Jan 19, 2023) — anthonyhobday.com/blog/20230119.html
- LogRocket, "Linear design" — blog.logrocket.com/ux-design/linear-design
- Rectangle newsletter, "The Linear effect" — rectangle.substack.com/p/the-linear-effect
- Linear Method (linear.app/method) — the product philosophy the look was supposed to express.
