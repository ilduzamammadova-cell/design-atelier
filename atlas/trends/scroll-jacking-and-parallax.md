---
id: scroll-jacking-and-parallax
name: Scroll-Jacking & Parallax
type: trend
discipline: [ui, ux]
era: 2011–2026 (waves — early-2010s parallax, mid-2010s Apple product pages, 2020s GSAP + smooth-scroll libraries)
origin: Global — product launch pages, agency/Awwwards sites, scroll animation libraries
lineage: [flash-era-web, saul-bass]
tags:
  mood: [cinematic, immersive, controlling, showy]
  topics: [product-launches, agencies, storytelling, portfolios, automotive]
axes: {order: 5, density: 3, ornament: 5, warmth: 4, contrast: 6, geometry: 5, chroma: 5, typevoice: 6, energy: 8, hand: 1, play: 5, era: 7}
saturation: 6
---

# Scroll-Jacking & Parallax

**Essence:** The page takes over the scroll wheel — pinning sections, scrubbing video, moving layers at different speeds, smoothing and slowing input — to tell a product story like a film.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Narrative pacing | Sequenced reveals control attention, like a film edit. | Pace with layout, not hijacking: one idea per viewport-height section, native scroll, content fades in once (200ms) when 25% visible and never re-hides. |
| G2 · Depth | Layers moving at different speeds suggest space. | One subtle depth cue per page (hero image translates ≤40px across its scroll range), removed under `prefers-reduced-motion`. |
| G3 · Show a transformation | Scroll-scrubbed sequences can explain how an object works (exploded views). | Give the sequence to the user as a scrubber or step buttons with visible progress (2/5), so the reader controls time and can skip. |

## Why it reads as slop now

Parallax storytelling pages appeared in the early 2010s, inheriting Flash-era intros; Apple's product pages made pinned, scroll-scrubbed reveals famous in the mid-2010s; GSAP ScrollTrigger and smooth-scroll libraries (Locomotive Scroll, Lenis) made it routine in 2020s agency work and Framer/Webflow templates. Nielsen Norman Group's "Scrolljacking 101" (August 2023) found most participants at least mildly disoriented, some thinking the page was broken, and task-focused users feeling their time was wasted — worst when altered scrolling accompanied text. The cheap version: smooth-scroll inertia on every page, a pinned hero where three wheel turns move a headline 20px, horizontally scrolling feature sections, no way to skip.

## Subvert

- **Native scroll, rich object.** Keep the browser's scroll; put the richness in one interactive object (draggable model, before/after slider).
- **Chapters, not tunnels.** Explicit chapter navigation (sticky contents with progress) keeps the cinematic structure and the reader's control.
- **Motion with an end.** Every animation completes within 600ms of its trigger and never depends on scroll velocity.

## Visual facts

- **Color:** often dark, cinematic grading around product shots.
- **Type:** large display type that scales, splits or masks as you scroll.
- **Form:** pinned sections, canvas image sequences, clip-path reveals, layered cut-outs.
- **Composition:** full-viewport scenes, horizontal tracks, stacked sticky cards.

## Attitude

The website as a film the designer directs. It privileges the author's timing over the reader's.

## Blends

- **Amplifies:** `kinetic-type-everywhere`, `spline-3d-hero`, `cursor-followers-and-magnetic-buttons`.
- **Productive tension with:** `saul-bass` — title-sequence economy: one strong idea per beat, short, in service of the story.
- **Clashes with:** `bento-grid`, `centered-hero-three-cards-template` — scan-first layouts lose their point when locked into a timeline.

## Don't copy

Apple's specific product-page sequences (AirPods, iPhone, Mac launches); award-winning agency scroll narratives.

## Study

- Nielsen Norman Group, "Scrolljacking 101" (Sara Paul, Aug 6, 2023) — nngroup.com/articles/scrolljacking-101
- GSAP ScrollTrigger docs (gsap.com) — know the tool in order to restrain it.
- WCAG 2.2, 2.2.2 Pause, Stop, Hide and 2.3.3 Animation from Interactions.
