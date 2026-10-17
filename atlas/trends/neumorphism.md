---
id: neumorphism
name: Neumorphism (Soft UI)
type: trend
discipline: [ui]
era: 2019–2021 peak; residual to 2026
origin: Global — Dribbble banking concept by Alexander (Oleksandr) Plyuto, late 2019
lineage: [ios-skeuomorphism, ios-7-flat, dieter-rams]
tags:
  mood: [soft, calm, tactile, monochrome]
  topics: [smart-home, fintech, music-players, wellness]
axes: {order: 7, density: 2, ornament: 3, warmth: 4, contrast: 1, geometry: 5, chroma: 1, typevoice: 2, energy: 1, hand: 1, play: 3, era: 6}
saturation: 3
---

# Neumorphism (Soft UI)

**Essence:** Controls extruded from, or pressed into, a single matte surface by paired light and dark shadows, as if the whole interface were moulded from one piece of soft plastic.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Physical affordance | Raised = pressable, sunken = pressed/active: a tactile signal flat UI lost. | Keep the state logic, raise the contrast: an unpressed toggle has a 1px #00000026 border and `0 2px 0` shadow; pressed drops the shadow and darkens fill 8%. State must also change label or icon, never shadow alone. |
| G2 · One-material calm | Everything is the same substance, so the UI feels quiet and unified. | Limit surfaces to one base color plus one raised tone; separate groups with spacing (24/32px), not with new colors or boxes. |
| G3 · Light from one direction | A consistent top-left light makes the scene coherent. | Fix one light direction for the whole system and bake it into every elevation token (`--elev-1: 0 1px 2px`, `--elev-2: 0 4px 8px`); never mix offsets. |

## Why it reads as slop now

A late-2019 Dribbble banking concept by Alexander Plyuto revived soft extruded shadows. The label "neumorphism" (new + skeuomorphism) is variously credited — to commenters on Michal Malewicz's article about the style, or to designer Jason Kelley — and generators and UI kits followed within weeks. It peaked in 2020 and collapsed quickly, mainly because it fails accessibility: element and background share one color, boundaries depend on faint shadows that low-vision users and bright screens erase, and button states are nearly invisible. Today it survives mostly in AI style prompts and smart-home concepts. The cheap version: a #E0E5EC screen where every card has `9px 9px 16px #a3b1c6, -9px -9px 16px #ffffff`, with gray-on-gray labels.

## Subvert

- **Tactile through material, not shadow.** A real surface difference (matte ground, a button with a 3% highlight band) plus a crisp border — touchable and legible.
- **Hardware honesty.** Borrow from physical product controls (Braun radios, appliance dials): labels printed beside controls, one accent color for the single most important switch.
- **Press only on interaction.** Surfaces stay flat at rest; the soft-press effect appears only as 100ms feedback.

## Visual facts

- **Color:** monochrome base #E0E5EC (light) or #2B2E33 (dark); shadows one tone darker and one lighter; occasional single accent.
- **Type:** Poppins, Montserrat, Nunito in mid-gray.
- **Form:** large radii (16–32px), dual outer shadows for raised, inset shadows for pressed, circular dials.
- **Composition:** sparse grids of oversized controls, lots of empty matte surface.

## Attitude

A correction to flat design's lost affordance, reaching back to physical objects — pursued as a surface treatment rather than as clarity of state.

## Blends

- **Amplifies:** `3d-clay-and-blob-renders` — same soft-plastic world; clay's inflated elements were partly a fix for neumorphism's contrast failure.
- **Productive tension with:** `swiss-international` — strict type and grid give soft surfaces the hierarchy they lack.
- **Clashes with:** `dark-mode-neon-glow` — glow destroys the single-light-source illusion.

## Don't copy

Plyuto's banking-app shot and the endlessly cloned neumorphic calculator, smart-home and music-player concepts of 2019–2020.

## Study

- Wikipedia, "Neumorphism" — origins and the accessibility critique.
- Webflow blog, "Neumorphism: its rise and fall in UI design".
- Dieter Rams' Braun products (Vitra Design Museum, Die Neue Sammlung) — physical affordance done right.
