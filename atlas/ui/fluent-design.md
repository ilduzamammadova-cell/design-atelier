---
id: fluent-design
name: Fluent Design System
type: system
discipline: [ui]
era: 2017 to present
origin: Redmond, USA
lineage: [metro-design-language, mac-os-x-aqua]
tags:
  mood: [soft, luminous, calm, layered]
  topics: [desktop productivity, enterprise apps, cross-device software]
axes: {order: 8, density: 5, ornament: 3, warmth: 5, contrast: 4, geometry: 6, chroma: 3, typevoice: 3, energy: 3, hand: 0, play: 4, era: 8}
---

# Fluent Design System

**Essence:** Metro's flat clarity given light, depth and material again, frosted acrylic, wallpaper-tinted Mica and highlights that follow the pointer, tuned for many devices and inputs.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Light follows the pointer | "Reveal" highlight lit up borders and backgrounds near the cursor, showing what is interactive without permanent chrome (later retired in WinUI). | Lists and grids get a radial border highlight centred on the pointer (radius ~80 px, 8 to 12% white), fading over 200 ms. Interactivity revealed by light rather than outlines. |
| G2 · Acrylic: blur with grain | Transient surfaces were frosted, blurred background, colour tint and a fine noise texture so the blur felt like a material, not a smear. | Flyouts and menus: `backdrop-filter: blur(30px)`, 60 to 70% tint, plus a 2 to 3% monochrome noise overlay. Use only on transient, light-dismiss surfaces. |
| G3 · Mica: personal but quiet | Windows 11's Mica tints an app's base layer with a heavily blurred sample of the desktop wallpaper, computed once, cheap, subtle. | App background tinted by a blurred, very low-opacity (~5 to 8%) sample of the user's wallpaper or brand image, computed once at launch; content layers stay opaque above it. |
| G4 · Layering with soft geometry | Depth is expressed with a base layer, content layers and shadows; Windows 11 settled on 8 px radius for windows/surfaces and 4 px for controls. | Radius tokens: 4 (controls), 8 (cards, windows); two shadow levels only; layer colours differ by 2 to 4% lightness rather than borders. |
| G5 · Connected motion and scale | Elements travel between views (connected animation), and the system was designed to scale from phones to large screens and mixed reality. | Shared elements animate continuously between pages; components defined with density modes (compact/standard) and input modes (mouse/touch/pen) from the start. |
| G6 · Soft dimensional emoji and icons | Fluent introduced 3D-style emoji (announced 2021, open-sourced 2022) and a rounded, friendly system icon set. | One illustrative layer of soft, matte "clay" objects for empty states and onboarding; UI icons stay as rounded line glyphs at 20/24 px. Never mix the two in one control. |

## Visual facts

- **Color:** neutral greys with slight warmth/coolness from Mica; Windows accent blue (~`#0078D4`); light and dark themes treated as equals.
- **Type:** Segoe UI Variable (Windows 11) with optical sizes; Segoe UI before. Free: **Selawik** (open-source Segoe fallback), **Noto Sans**, **Open Sans**.
- **Form:** rounded rectangles, frosted surfaces, subtle shadows, thin strokes on controls, soft 3D emoji.
- **Composition:** navigation view (left rail) + content; command bars; layered panes with breathing room.

## Attitude

Announced at Microsoft Build in May 2017 with five building blocks, light, depth, motion, material, scale, Fluent tried to make software feel physical again without returning to fake leather. Fluent 2 (2023) consolidated it into a cross-platform system. The useful belief: materials should be *functional* (signalling transience, focus, personalisation), not decorative.

## Blends

- **Amplifies:** `metro-design-language`, `material-design`, `mac-os-x-aqua`, systematic, layered, polished.
- **Productive tension with:** `command-line-and-teletext`, frosted, tinted panes over a hard monospace cell grid: the modern beautiful terminal.
- **Clashes with:** `ios-skeuomorphism`, frosted glass plus leather gives two contradictory material logics. (For the 2020s glass trend itself, see `glassmorphism`.)

## Don't copy

- Windows logos and the Bloom wallpaper, Microsoft product icons, the Fluent emoji set presented as your own illustration style.

## Study

- fluent2.microsoft.design, Fluent 2 documentation, tokens and components.
- Microsoft Learn: "Mica material" and "Acrylic material" pages (learn.microsoft.com/windows/apps/design).
- Microsoft Build 2017 keynote (Fluent introduction); microsoft/fluentui-emoji repository on GitHub.
