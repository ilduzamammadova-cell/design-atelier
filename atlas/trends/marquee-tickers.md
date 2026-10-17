---
id: marquee-tickers
name: Marquee Tickers
type: trend
discipline: [ui, graphic]
era: 2019 to 2026 (ancestors, news and stock tickers, the 1990s HTML marquee tag)
origin: Global, streetwear and fashion e-commerce, agency portfolios, then SaaS logo strips and AI templates
lineage: [web-1-vernacular, futurism]
tags:
  mood: [busy, energetic, street, looping]
  topics: [fashion, events, agencies, saas-social-proof, ecommerce]
axes: {order: 6, density: 6, ornament: 4, warmth: 4, contrast: 6, geometry: 7, chroma: 5, typevoice: 7, energy: 8, hand: 1, play: 6, era: 5}
saturation: 8
---

# Marquee Tickers

**Essence:** Endless horizontal bands of scrolling text or logos ("FREE SHIPPING ✦ NEW DROP ✦" or "Trusted by …") cutting across the page, often tilted a few degrees.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Liveness | Constant motion says "this is current; things are happening". | Show liveness with real data: "updated 2 min ago", a live count, the latest three changelog entries, static, accurate, linked. |
| G2 · Abundance | A never-ending list implies many customers, products or messages. | State the number plainly ("1,240 studios use X") and show 3 to 5 named examples with context. |
| G3 · Horizontal rhythm | A band breaks vertical scrolling with a different direction and pace. | Break rhythm structurally: a full-bleed rule, a section with a different measure or ground, or one oversized static line of type spanning the grid. |

## Why it reads as slop now

The ticker belongs to stock exchanges, Times Square and TV news; the non-standard HTML `<marquee>` tag made it a 1990s web joke. Streetwear and fashion e-commerce revived it around 2019 to 2021 as a shouting announcement bar, agency sites tilted it, and SaaS templates and component libraries (Magic UI's Marquee, Framer ticker components) turned the "trusted by" logo wall into an infinite scroll. The cheap version: a −3° black band repeating "DESIGN ✦ DEVELOP ✦ DELIVER ✦", plus a grayscale logo carousel that cannot be paused.

## Subvert

- **A ticker that carries data.** If it moves, it should carry information that changes (prices, scores, departures) and pause on hover and focus.
- **Static repetition.** A repeated word set as a still typographic pattern keeps the rhythm without motion, in the spirit of concrete poetry.
- **One line, still.** A single huge line of type bleeding off both edges gives the band effect with zero animation.

## Visual facts

- **Color:** black band with white text or a brand-color band; grayscale logos at 40 to 60% opacity.
- **Type:** uppercase grotesk or extended sans with ✦ or • separators.
- **Form:** CSS keyframe `translateX` loops over duplicated content, edge-fade masks, rotated bands.
- **Composition:** full-bleed between sections, typically between hero and features.

## Attitude

Energy and volume as proof. Motion substitutes for a message.

## Blends

- **Amplifies:** `neo-brutalism-web`, `oversized-grotesk-hero`, `trusted-by-logo-strip`.
- **Productive tension with:** `futurism`, typography of speed with an actual idea of dynamism, not just a loop.
- **Clashes with:** `editorial-serif-revival`, calm reading interrupted by perpetual motion.

## Don't copy

Specific fashion-brand announcement bars; third-party logos you are not licensed to display.

## Study

- WCAG 2.2, 2.2.2 Pause, Stop, Hide, moving content lasting over five seconds needs a pause control.
- MDN, `<marquee>` (deprecated), the history of the element.
- F. T. Marinetti, *Zang Tumb Tuuum* (1914), speed as a typographic idea (see `futurism`).
