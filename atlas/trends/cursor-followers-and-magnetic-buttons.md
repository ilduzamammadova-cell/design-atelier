---
id: cursor-followers-and-magnetic-buttons
name: Cursor Followers & Magnetic Buttons
type: trend
discipline: [ui, ux]
era: 2017–2026
origin: Global — creative-agency portfolios on the Awwwards circuit, GSAP demos, Framer/Webflow components
lineage: [flash-era-web, scroll-jacking-and-parallax]
tags:
  mood: [playful, showy, tactile, restless]
  topics: [agencies, portfolios, fashion, creative-studios, launches]
axes: {order: 4, density: 3, ornament: 5, warmth: 5, contrast: 6, geometry: 5, chroma: 4, typevoice: 5, energy: 8, hand: 1, play: 8, era: 7}
saturation: 6
---

# Cursor Followers & Magnetic Buttons

**Essence:** A custom circle or blob trailing the pointer (often `mix-blend-mode: difference`), buttons that lean toward the cursor, images revealed under the pointer — interaction as personality.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Responsive presence | The page feels alive and aware of the visitor. | Respond to intent, not every movement: hover/focus states on actionable things within 50ms with a clear change (underline thickens, fill shifts 8%). |
| G2 · Easier targeting | Magnetism enlarges the effective hit area — a Fitts's-law idea (`fitts-and-hicks-laws`). | Enlarge the real hit area: ≥44×44px targets, padding-inflated links, generous spacing between adjacent actions. No animated pull needed. |
| G3 · Contextual preview | A cursor label ("View", "Drag") explains what clicking will do. | Put that information in the element: visible "View case →" text, drag handles, tooltips on focus as well as hover. |

## Why it reads as slop now

Late-2010s agency portfolios used custom cursors and magnetic hovers to show off motion craft; GSAP tutorials, CodePens and Framer/Webflow marketplace components turned them into copy-paste effects, and animated component kits list magnetic buttons among their stock items. Inclusive-design writers such as Eric Bailey argue custom cursors fall apart under scrutiny: they lag, replace the system pointer, ignore touch and keyboard, and fail low-vision users. The cheap version: a 40px blend-mode circle lagging behind the mouse, buttons wobbling toward the pointer, "Drag" labels — on a site whose content is four project thumbnails.

## Subvert

- **System cursor, crafted states.** Keep the native pointer; invest in hover, focus and pressed states that are distinct, fast and consistent.
- **One signature interaction.** A single product-relevant interaction (draggable timeline, scrubbable before/after) made excellent.
- **Keyboard parity.** Anything a hover reveals is reachable and visible on focus; design focus rings as part of the style.

## Visual facts

- **Color:** inverted blend-mode circles, accent blobs.
- **Type:** often paired with oversized grotesks and split-text animation.
- **Form:** 8–60px circles, trailing interpolation 0.1–0.2, magnetic radius 80–120px, image trails.
- **Composition:** sparse layouts that leave room for pointer effects.

## Attitude

The site as an instrument the visitor plays. Charming once; tiring when every studio plays the same tune.

## Blends

- **Amplifies:** `oversized-grotesk-hero`, `kinetic-type-everywhere`, `marquee-tickers`.
- **Productive tension with:** `dieter-rams` — controls that communicate precisely, without needless movement.
- **Clashes with:** `shadcn-tailwind-default-look` — gimmick motion on generic components exposes both.

## Don't copy

Specific agency-portfolio interactions; paid Framer/Webflow cursor components used unchanged.

## Study

- Eric W. Bailey on custom cursors and inclusive design (ericwbailey.website).
- WCAG 2.2, 2.5.8 Target Size (Minimum) and 2.4.7 Focus Visible.
- Nielsen Norman Group, "Fitts's Law and its applications in UX" (nngroup.com).
