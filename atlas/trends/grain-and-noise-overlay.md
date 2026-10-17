---
id: grain-and-noise-overlay
name: Grain & Noise Overlay
type: trend
discipline: [ui, graphic]
era: 2020–2026
origin: Global — "grainy gradients" CSS/SVG technique, analog-photo nostalgia, AI-brand illustration
lineage: [gradient-mesh-and-aurora]
tags:
  mood: [analog, soft, warm, moody]
  topics: [ai-products, music, wellness, portfolios, editorial]
axes: {order: 5, density: 4, ornament: 4, warmth: 7, contrast: 3, geometry: 3, chroma: 5, typevoice: 4, energy: 3, hand: 6, play: 4, era: 4}
saturation: 7
---

# Grain & Noise Overlay

**Essence:** A fine noise texture laid over gradients, backgrounds and images so digital color feels like film, paper or risograph.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Dithering fixes banding | Noise breaks up the visible steps in smooth gradients on 8-bit displays — a real technical benefit. | Where a gradient is truly needed, add 2–4% monochrome noise to that element only; never to the whole page or to text containers. |
| G2 · Tactility | Texture says "physical, made" in a flat digital world. | Use one real material scan once (paper fibre in a hero, a fabric swatch in a product shot) instead of a uniform digital overlay. |
| G3 · Analog memory | Film grain evokes photography and time. | Put grain where it belongs — in real analog or properly graded photography — and keep UI surfaces clean so the photo's grain means something. |

## Why it reads as slop now

Grainy gradients spread around 2020–2022 as a counter to sterile flat color, helped by CSS-Tricks' "Grainy Gradients" SVG `feTurbulence` technique and Figma noise plugins. Aurora gradients plus grain became the house style of AI-company illustration and indie portfolios; noise generators, Tailwind plugins and image prompts followed. The cheap version: a full-page fixed noise PNG at 8–15% opacity over a purple aurora, visible as dirty static on every surface including text, and costing scroll performance (SVG turbulence is CPU-rendered).

## Subvert

- **Texture from a real process.** Risograph overprint (two spot inks, visible misregistration), halftone, screenprint, letterpress bite — each with its own rules.
- **Grain where light is.** Apply noise only to photographic or illustrated content, never to chrome, controls or text.
- **Clean as contrast.** In a grainy era, perfectly flat, crisp color fields with precise edges read fresher.

## Visual facts

- **Color:** over aurora/mesh gradients or beige/cream grounds; monochrome noise.
- **Type:** often paired with editorial serifs or soft sans.
- **Form:** SVG `feTurbulence` (baseFrequency 0.6–0.9), tiled noise PNGs, `mix-blend-mode: overlay` or `soft-light`, 3–15% opacity.
- **Composition:** full-bleed overlays; grain inside blurred shapes.

## Attitude

A wish for the analog and imperfect inside screens. The honest version is about material; the trend version is a filter.

## Blends

- **Amplifies:** `gradient-mesh-and-aurora`, `editorial-serif-revival`.
- **Productive tension with:** `swiss-international`, `dieter-rams` — a strict flat system with one deliberate material moment.
- **Clashes with:** `linear-style-dark-ui` — hairlines and luminance ladders turn muddy under noise.

## Don't copy

Specific AI-company gradient illustrations; commercial film-emulation presets redistributed as assets.

## Study

- CSS-Tricks, "Grainy Gradients" — the SVG noise technique and its trade-offs.
- Risograph studio guides (e.g. Risotto Studio, Glasgow) — texture with process rules.
- WCAG 2.2, 1.4.3 Contrast (Minimum) — test text over textured backgrounds.
