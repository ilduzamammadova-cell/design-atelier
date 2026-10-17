---
id: ios-7-flat
name: iOS 7 Flat
type: system
discipline: [ui]
era: 2013 to 2020
origin: Cupertino, USA
lineage: [metro-design-language, dieter-rams, swiss-international]
tags:
  mood: [airy, bright, deferential, clean]
  topics: [mobile apps, consumer software, health, productivity]
axes: {order: 8, density: 3, ornament: 1, warmth: 4, contrast: 4, geometry: 7, chroma: 6, typevoice: 4, energy: 3, hand: 0, play: 4, era: 8}
---

# iOS 7 Flat

**Essence:** The interface steps back behind the content: hairline glyphs, borderless text buttons, frosted translucent layers and springs, all on bright white.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Deference | Apple's iOS 7 guidance named three themes, deference, clarity, depth. Chrome thinned out so content filled the screen and scrolled beneath translucent bars. | Navigation and tab bars at ~80% white with `backdrop-filter: blur(20px) saturate(180%)`; content scrolls under them edge to edge. No bar backgrounds with texture or gradient. |
| G2 · Text as button | Buttons lost their borders and became tinted words; one tint colour marked everything tappable. | Interactive elements = text in a single tint (`#007AFF`), no outline or fill; reserve filled buttons for one primary action per screen. Tint is never used for non-interactive text. |
| G3 · Outline → fill as state | Tab and toolbar glyphs were thin line drawings that became filled when selected. | Icon pairs: outline (1.5 px stroke) inactive, solid fill active; the same silhouette in both so the state change reads as "lighting up". |
| G4 · Depth by layers, not bevels | Hierarchy came from stacked translucent planes (wallpaper → content → overlays) and a parallax wallpaper tied to device tilt. | Define three z-planes; overlays blur what's beneath; a subtle tilt/pointer parallax (±10 px) on the background plane only. |
| G5 · Thin numerals at scale | Large clock and number displays used very light weights of Helvetica Neue; body text stayed regular. | Light/UltraLight weights only at ≥48 px (clocks, totals, timers); never below 20 px. Body text regular 17 px. |
| G6 · Springs everywhere | UIKit Dynamics brought spring physics to transitions and interactions; motion became interruptible and physical. | All transitions use damped springs (e.g. response 0.4 s, damping 0.8), interruptible mid-flight; no linear easing anywhere in the product. |

## Visual facts

- **Color:** white and light grey (`#F7F7F7`, grouped `#EFEFF4`); system tints blue `#007AFF`, red `#FF3B30`, green `#4CD964`, orange `#FF9500`, yellow `#FFCC00`, purple `#5856D6`, pink `#FF2D55`; icons with vivid two-stop gradients.
- **Type:** Helvetica Neue (Light and UltraLight prominent); San Francisco replaced it from iOS 9 (2015). Free: **Hanken Grotesk** (Light) or **Manrope**.
- **Form:** hairline separators inset from the left, circles and rounded squares, line glyphs, frosted blur.
- **Composition:** large white fields, left-inset lists, big titles (later large-title navigation), content edge to edge.

## Attitude

Announced in June 2013 after Jony Ive took over Human Interface, iOS 7 rejected literal textures in favour of a digital honesty closer to industrial design: the device is a pane of glass, so the UI should be layers of light. Its risk, low-contrast hairlines and ambiguous text buttons, drew sharp usability critiques, which is part of what to learn.

## Blends

- **Amplifies:** `metro-design-language`, `dieter-rams`, `material-design`, reduction, clarity, content first.
- **Productive tension with:** `ios-skeuomorphism`, keep the flat structure but let one true, meaningful material return; the post-flat synthesis of the late 2010s.
- **Clashes with:** `windows-95`, hairlines and translucency beside chunky bevels look like a rendering error.

## Don't copy

- Apple's app icons and wallpapers, the San Francisco typeface (licensed for Apple platforms only), Apple's system glyph set; the iOS icon template as an Apple asset (the concentric-grid *idea* is fine).

## Study

- Apple, *iOS 7 UI Transition Guide* (Apple developer archive), states the three themes.
- WWDC keynote, 10 June 2013 (video) and Apple's iOS 7 press materials.
- Nielsen Norman Group, critiques of flat design and "flat UI elements attract less attention" studies (nngroup.com).
