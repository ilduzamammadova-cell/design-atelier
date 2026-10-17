---
id: glassmorphism
name: Glassmorphism
type: trend
discipline: [ui]
era: 2020 to 2026 (roots 2007, 2013, 2017)
origin: Global, named by Michal Malewicz (Nov 2020), boosted by macOS Big Sur
lineage: [mac-os-x-aqua, fluent-design, ios-7-flat]
tags:
  mood: [airy, sleek, translucent, dreamy]
  topics: [dashboards, fintech, crypto, os-concepts, ai-products]
axes: {order: 6, density: 3, ornament: 5, warmth: 4, contrast: 3, geometry: 6, chroma: 6, typevoice: 3, energy: 4, hand: 1, play: 4, era: 8}
saturation: 8
---

# Glassmorphism

**Essence:** Frosted translucent panels (background blur + white tint + thin light border) floating over colorful blobs, so the interface seems made of sheets of glass.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Show layering | Translucency says a panel sits *above* something, and that the thing below still exists. | Express z-order with one opaque step per layer (base #F5F5F4 → raised #FFFFFF → overlay #FFFFFF + 1px #00000014 border) and fade the underlying layer to 92% opacity in 120ms, no blur needed. |
| G2 · Keep context while focused | A sheet over a map or document keeps the user oriented. | Leave a visible strip of the underlying view (≥24px or ≥10% of the viewport) beside every sheet or modal; dim it, never hide it. |
| G3 · Content tints the chrome | Glass picks up color from what is under it, tying chrome to content. | Sample the dominant color of the current image/artwork and set the toolbar to a solid 6 to 10% tint of it, contrast-checked at 4.5:1. |
| G4 · Light edge = boundary | The bright 1px border reads as a physical edge catching light. | One top-edge highlight (`inset 0 1px 0 rgba(255,255,255,.08)` on dark UI) separates surfaces instead of drop shadows. |

## Why it reads as slop now

Frosted glass is old: Windows Vista's Aero (2007), iOS 7's blur (2013), Microsoft Fluent's Acrylic (2017). Michal Malewicz named "glassmorphism" in November 2020, the month macOS Big Sur shipped translucent sidebars and menus, and Dribbble filled with credit-card and dashboard shots. CSS `backdrop-filter` made it one line of code, so every template adopted it. Apple's Liquid Glass (June 2025) re-energised it and a second wave of imitations followed. The cheap version: white 10 to 20% panels with `blur(20px)` over two purple and pink circles, low-contrast white text, and nothing behind the glass worth seeing, the blur decorates a background that exists only to be blurred.

## Subvert

- **Earn the transparency.** Make a surface translucent only when real, changing content sits behind it (a map, a photo feed, video). If the background is a decorative blob, the panel should be solid.
- **Paper instead of glass.** Opaque, slightly offset sheets with a hard 1px edge and a small tonal shift, a print-studio metaphor (stacked paper, tracing vellum) gives layering with full legibility.
- **Tint, don't blur.** A solid content-derived tint (G3) keeps the "chrome belongs to content" idea and passes contrast every time.

## Visual facts

- **Color:** rgba(255,255,255,0.10 to 0.25) panels; borders rgba(255,255,255,0.3); grounds of saturated blobs (#7C3AED, #EC4899, #06B6D4) or navy #0F172A.
- **Type:** SF Pro, Inter, Poppins; white text, frequently under 4.5:1 contrast.
- **Form:** 16 to 24px radii, `backdrop-filter: blur(12 to 30px)`, soft drop shadows.
- **Composition:** floating cards stacked at slight offsets over a gradient field.

## Attitude

The interface as a weightless, luminous layer between you and content. Its honest core, context should stay visible, is sound; the trend spends it on decoration.

## Blends

- **Amplifies:** `gradient-mesh-and-aurora`, `dark-mode-neon-glow`, glass needs something colorful behind it; together they make the stock "futuristic dashboard".
- **Productive tension with:** `dieter-rams`, `swiss-international`, every layer must justify itself; translucency survives only where it carries information.
- **Clashes with:** `neo-brutalism-web`, hard shadows and opaque fills cancel the floating illusion and read as indecision.

## Don't copy

macOS Big Sur's sidebar and Control Center materials, Windows Fluent Acrylic/Mica recipes, Apple's Liquid Glass rendering, Malewicz's own showcase shots.

## Study

- Michal Malewicz, "Glassmorphism in user interfaces" (UX Collective, Nov 2020), the naming article.
- Webflow blog, "Glassmorphism: examples and best practices", lineage from iOS 7 and Acrylic: webflow.com/blog/glassmorphism
- Microsoft Fluent 2 design system, materials (fluent2.microsoft.design), translucency governed by rules.
- WCAG 2.2 success criteria 1.4.3 and 1.4.11, the contrast tests most glass UIs fail.
