---
id: mac-os-x-aqua
name: Mac OS X Aqua
type: system
discipline: [ui]
era: 2000–2012
origin: Cupertino, USA
lineage: [nextstep, classic-macintosh]
tags:
  mood: [luscious, liquid, optimistic, polished]
  topics: [consumer software, media apps, creative tools, launch pages]
axes: {order: 7, density: 4, ornament: 6, warmth: 6, contrast: 6, geometry: 6, chroma: 5, typevoice: 3, energy: 4, hand: 0, play: 6, era: 9}
---

# Mac OS X Aqua

**Essence:** Interface as candy and water — translucent gel buttons, pinstriped surfaces and fluid motion that made software feel desirable, like the translucent iMac it was born beside.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Gel controls | Buttons and scroll thumbs looked like translucent, wet candy: saturated blue body, a bright specular highlight across the top half, a soft glow pooling at the bottom. | Primary button: vertical gradient `#A8D8FF → #2C7EE8`, top-half highlight `rgba(255,255,255,.7 → .1)` clipped to a pill, 1 px darker rim, faint inner glow at the base. Secondary buttons in clear/white gel with the same highlight. |
| G2 · The breathing default | The default button in a dialog pulsed slowly, telling you which action Return would take. | Default action pulses brightness ±8% on a 2 s ease-in-out loop while it is the Return target; the pulse stops when focus moves. Respect `prefers-reduced-motion` with a static ring. |
| G3 · Motion that remembers where things go | The Genie effect poured windows into the Dock; Dock icons magnified under the pointer. Motion explained spatial relationships. | Minimise/close animations travel toward the element's home (shrink into its launcher or tab); launcher items magnify with a Gaussian falloff across neighbours on hover. |
| G4 · Pinstripes and translucency | Window backgrounds carried faint horizontal pinstripes; menus were slightly see-through. | Panel background: 2 px repeating horizontal stripes at 3–4% contrast. Menus at ~92% opacity with a soft shadow, so context stays faintly visible. |
| G5 · Depth equals focus | Windows cast large, soft shadows; the active window cast the deepest one. | Active window shadow `0 20px 40px rgba(0,0,0,.45)`; inactive `0 8px 16px rgba(0,0,0,.2)`. Never use shadow decoratively — it always signals focus. |
| G6 · Traffic lights and photographic icons | Close/minimise/zoom became red, yellow and green gel dots whose symbols appeared on hover; icons grew to 128 px and were rendered like product photography. | Window controls as three coloured circles, glyphs revealed only on hover. App icons large (128+), lit, with perspective and reflections — each one a small object. |

## Visual facts

- **Color:** "Aqua" blue (~`#3D8BFF` family) and the alternative Graphite appearance (blue-greys ~`#8E9AA6`); white and pale grey pinstripes; red/amber/green window dots. Brushed metal (introduced in the QuickTime 4 Player, 1999) as a second skin for media apps.
- **Type:** Lucida Grande 13 pt as system font (Mac OS X 10.0 through 10.9). Free: **Fira Sans** or **Source Sans 3** for its humanist openness.
- **Form:** pills and capsules, glossy rounded tabs, soft shadows, transparency, reflective surfaces.
- **Composition:** generous padding around controls, sheets that slide out of title bars (dialogs attached to their window), toolbars of large labelled icons.

## Attitude

Unveiled at Macworld in January 2000 (Mac OS X 10.0 shipped March 2001), Aqua carried Apple's late-1990s product language — translucent, coloured, friendly — into software. Steve Jobs joked that the buttons looked good enough that "you'll want to lick them." Cordell Ratzlaff led the Human Interface group; Bas Ording shaped the animations and the Dock. The belief: delight is not decoration but a reason to choose a computer.

## Blends

- **Amplifies:** `streamline-moderne`, `web-2-gloss`, `ios-skeuomorphism` — glossy optimism and material richness.
- **Productive tension with:** `swiss-international` — gel materials on a rigorous typographic grid: lush surface, strict structure.
- **Clashes with:** `brutalist-web` — raw defaults beside candy gloss reads as unfinished, not ironic.

## Don't copy

- Aqua's exact button and scroll-bar artwork, the default Aqua wallpapers, the Finder face icon, Apple's application icons, the Apple logo.

## Study

- Macworld San Francisco keynote, 5 January 2000 (video) — Aqua's first demonstration.
- Apple, *Aqua Human Interface Guidelines* (2001 onward; via Apple developer archive / Wayback).
- GUIdebook gallery — Mac OS X 10.0–10.4 screenshots; 512pixels.net (Stephen Hackett) on brushed metal and Aqua history.
