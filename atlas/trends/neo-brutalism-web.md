---
id: neo-brutalism-web
name: Neo-Brutalism (Web)
type: trend
discipline: [ui, graphic]
era: 2020–2026 (peak 2022–2024)
origin: Global — indie and creator tools; Gumroad's 2021 redesign the most-cited example
lineage: [brutalist-web, brutalism, memphis, punk-graphics]
tags:
  mood: [loud, blunt, playful, raw]
  topics: [creator-tools, indie-saas, portfolios, newsletters, education]
axes: {order: 7, density: 6, ornament: 3, warmth: 6, contrast: 9, geometry: 9, chroma: 8, typevoice: 7, energy: 6, hand: 3, play: 8, era: 5}
saturation: 6
---

# Neo-Brutalism (Web)

**Essence:** Thick black outlines, hard offset shadows with zero blur, flat candy fills and chunky type — a deliberately "under-designed" sticker-book look that became its own polished template.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Visible structure | Borders show every container; nothing pretends to float. The page explains its own construction. | Draw structure with rules rather than boxes: 1–2px full-width rules between sections, column dividers in dense content; no container gets both a border and a fill. |
| G2 · Unmistakable affordance | A hard shadow under a button screams "press me", and it moves when pressed. | Primary button only: solid fill, 2px border, `4px 4px 0` shadow that collapses to `0 0 0` with `translate(4px,4px)` on press. Everything else stays flat so the effect stays meaningful. |
| G3 · Personality on a budget | Flat high-contrast color and type create a voice without illustration or photography. | Voice from one typographic decision (a quirky display face at 64px+) and one off-palette color; the rest stays system-neutral. |

## Why it reads as slop now

The name borrows from Brutalist architecture via the late-2010s "brutalist websites" (raw HTML, browser defaults). The 2020s version kept the bluntness but added color and polish: Gumroad's 2021 redesign under Sahil Lavingia (pink, black outlines, hard shadows) became the reference, then Figma community kits, Tailwind plugins and neobrutalism component libraries made it a theme you switch on. By 2024 it was the default "we're not corporate" look for indie SaaS and newsletters, and AI prompt galleries list it as a preset. The cheap version: every card with a 3px black border and `6px 6px 0 #000`, yellow and pink fills, an emoji in each heading — rebellion as a CSS class.

## Subvert

- **Raw for real.** Return to the actual brutalist-web impulse: system fonts, default link blue, honest HTML structure, speed as aesthetic (see `brutalist-web`).
- **Hard edge, quiet palette.** Keep the offset-shadow logic in one tone (ink #1A1A1A on paper #F2EFE6) — print-like instead of cartoon.
- **Structure from type.** Replace borders with a strong typographic grid — huge numerals, hanging heads, rules — so bluntness comes from hierarchy.

## Visual facts

- **Color:** black #000 outlines; fills like yellow #FFDC58, pink #FF90E8, aqua #A6FAFF, lavender #B8A9FF; off-white grounds #FFFDF5.
- **Type:** chunky grotesques (Archivo Black, Space Grotesk, Lexend Mega), mono for details.
- **Form:** 2–4px borders, zero-blur offset shadows (4–8px), small or zero radii, sticker badges.
- **Composition:** blocky cards in a visible grid, slight rotations on stickers, high contrast throughout.

## Attitude

Anti-polish: show the bones, be loud, be human, refuse SaaS gloss. Once anti-polish is a template, it becomes another polish.

## Blends

- **Amplifies:** `emoji-as-icons`, `marquee-tickers`, `oversized-grotesk-hero`.
- **Productive tension with:** `swiss-international` — rigorous grid plus brutal contrast yields a serious, structural version.
- **Clashes with:** `glassmorphism`, `gradient-mesh-and-aurora` — soft optics against hard ink.

## Don't copy

Gumroad's site and brand system (pink-and-black palette, logo, illustrations); neobrutalism component kits shipped unmodified.

## Study

- SVGator blog, "What is neubrutalism" and "Neubrutalism in web design: embracing the ugly".
- UX Collective, "Neubrutalism is taking over the web" (2022).
- Brutalist Websites archive (brutalistwebsites.com) — the rawer predecessor.
