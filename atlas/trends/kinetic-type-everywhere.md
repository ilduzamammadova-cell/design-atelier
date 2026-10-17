---
id: kinetic-type-everywhere
name: Kinetic Type Everywhere
type: trend
discipline: [ui, graphic]
era: 2018–2026
origin: Global — motion-design reels, agency sites, social-video typography, variable fonts and GSAP SplitText
lineage: [saul-bass, futurism, flash-era-web]
tags:
  mood: [energetic, theatrical, loud, restless]
  topics: [agencies, music, events, brand-launches, social-content]
axes: {order: 4, density: 4, ornament: 4, warmth: 4, contrast: 8, geometry: 6, chroma: 5, typevoice: 10, energy: 9, hand: 1, play: 6, era: 7}
saturation: 7
---

# Kinetic Type Everywhere

**Essence:** Headlines that split into letters and fly in, words rotating through a list ("for designers / founders / teams"), weights stretching on variable axes, text scrambling like a terminal — type that never sits still.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Time-based hierarchy | Motion orders reading: what moves first is read first. | Animate at most one text element per screen, once, ≤600ms ease-out; everything else is visible from first paint (no text hidden until animated — it hurts LCP and screen readers). |
| G2 · Type as performer | Letterforms express voice through weight, width and rhythm. | Use variable axes only on interaction and with meaning: weight rises on hover/selection (400 → 600 over 150ms) to show state. |
| G3 · Message variety | Rotating words address several audiences at once. | Replace rotators with a static audience selector (tabs "For designers / For developers") that changes the content beneath. |

## Why it reads as slop now

Saul Bass's title sequences and Futurist typography long ago showed type in motion. Variable fonts (OpenType 1.8, 2016), GSAP SplitText, Lottie and After Effects templates made it routine; social video normalised it; agency sites adopted split-letter entrances; Framer and Webflow presets now apply them with one toggle. The cheap version: every heading staggers in letter by letter on scroll, a typewriter hero cycles three nouns, text scrambles like a hacker film — and all of it is invisible until the animation fires, so the page is blank for a second.

## Subvert

- **Motion in one place.** Make a single typographic moment the signature (logo animation, page-transition title) and keep all reading text still.
- **Energy through composition.** Diagonals, scale jumps and crops (`constructivism`, `wolfgang-weingart`'s layered type) express dynamism without animation.
- **Motion that encodes data.** Numbers count up once to real values; type size responds to a real variable (volume, temperature, progress).

## Visual facts

- **Color:** high contrast — black/white with one accent.
- **Type:** variable grotesks and display faces (Roboto Flex, Anybody, Bricolage Grotesque, commercial neo-grotesks); mono for scramble effects.
- **Form:** per-letter transforms, line masks, loops, weight/width morphs.
- **Composition:** headline-dominant screens, usually oversized.

## Attitude

Type as performance — the page must entertain. It forgets that most text is there to be read.

## Blends

- **Amplifies:** `oversized-grotesk-hero`, `marquee-tickers`, `scroll-jacking-and-parallax`.
- **Productive tension with:** `swiss-international` — a strict static layout with one precisely timed animated element feels more modern than constant motion.
- **Clashes with:** `editorial-serif-revival` — long reading wants still text.

## Don't copy

Saul Bass's title sequences (*Vertigo*, *North by Northwest*, *Psycho*); identifiable agency reels; commercial animated-font products redistributed.

## Study

- Art of the Title (artofthetitle.com) — Saul Bass and successors: motion in service of one idea.
- GSAP SplitText docs (gsap.com) — including its accessibility notes.
- WCAG 2.2, 2.3.3 Animation from Interactions; MDN on `prefers-reduced-motion`.
