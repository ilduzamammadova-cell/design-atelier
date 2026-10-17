---
id: metro-design-language
name: Metro Design Language (Zune, Windows Phone, Windows 8)
type: system
discipline: [ui, graphic]
era: 2009–2015
origin: Redmond, USA
lineage: [swiss-international, bauhaus, otl-aicher]
tags:
  mood: [typographic, brisk, flat, confident]
  topics: [mobile, media, dashboards, transit, news]
axes: {order: 9, density: 4, ornament: 0, warmth: 4, contrast: 8, geometry: 10, chroma: 6, typevoice: 9, energy: 6, hand: 0, play: 4, era: 8}
---

# Metro Design Language (Zune, Windows Phone, Windows 8)

**Essence:** Navigation made of oversized type rather than icons, flat colour tiles that change with live data, and motion choreographed like turning pages of a signage system.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Type is the chrome | Section headers were huge, light-weight words; the next section's title bled off the right edge to show there was more. | Hub headers at 56–72 px Light; neighbouring section title partially visible at the right edge as the affordance. No icons in primary navigation — words only. |
| G2 · Content before chrome | No bevels, gradients, borders or glossy bars; hierarchy came from size, weight and space alone. | Ban borders, shadows and gradients in the component library. Express hierarchy only through a type ramp (e.g. 72/42/24/15) and spacing on a 4 px grid. |
| G3 · Live tiles | Home was a grid of flat colour squares and rectangles that displayed live content and periodically flipped to show more. | Dashboard of flat tiles in 1×1, 2×1, 2×2 units; each shows a live value; tiles flip (3D, 400 ms) on staggered timers of 6–10 s so the grid feels alive, never in sync. |
| G4 · Panorama and pivot | Hubs were horizontal canvases wider than the screen; titles and backgrounds moved at slower speeds than content (parallax). Pivots were tab strips made of words. | Horizontal hub where the title scrolls at ⅓ the speed of content; tabs as a row of large words with the active one bright and others at 40% opacity. |
| G5 · Signage DNA | Inspired by airport and transit wayfinding: simple white pictograms in circles, strong left alignment, one accent colour. | Icons are white glyphs in thin circles; everything flush left, ragged right; one user-chosen accent colour applied consistently across the whole UI. |
| G6 · Turnstile choreography | Page transitions swung items in like a turnstile; lists entered with staggered delays. | Page-in: items rotate from `rotateY(-80deg)` around their left edge with 30 ms stagger; page-out reverses. Motion is typographic, not decorative. |

## Visual facts

- **Color:** black or white backgrounds with one accent from a set of saturated hues, e.g. blue `#1BA1E2`, magenta `#FF0097`, lime `#8CBF26`, orange `#F09609`, red `#E51400`, teal `#00ABA9`, purple `#A200FF`.
- **Type:** Segoe WP (made for Windows Phone 7) and Segoe UI in Light and Semilight. Free: **Selawik** (Microsoft's open-source Segoe UI fallback) or **Open Sans**.
- **Form:** rectangles, squares, thin circles, no radius; photography full-bleed in hubs.
- **Composition:** left-aligned columns, generous margins, content cropped deliberately at the right edge.

## Attitude

Metro (the name was dropped in 2012 over a trademark issue) argued that digital interfaces should be "authentically digital" — honest to the screen rather than imitating leather — and borrowed clarity from transit signage and Swiss typography. It ran from Zune HD (2009) through Windows Phone 7 (2010) to Windows 8 (2012). Designers such as Albert Shum and Mike Kruzeniski articulated it publicly. Its legacy is the idea that typography itself can be the interface.

## Blends

- **Amplifies:** `swiss-international`, `wim-crouwel`, `otl-aicher` — grid, signage, systematic colour.
- **Productive tension with:** `memphis` — Metro's flat tiles and type with Memphis pattern and colour inside the tiles: strict layout, exuberant content.
- **Clashes with:** `web-2-gloss` — gloss and reflections on type-led flat chrome cancel the clarity Metro depends on.

## Don't copy

- Windows and Windows Phone logos, Zune branding, the exact Start-screen tile arrangement, Segoe letterforms, Microsoft's icon set.

## Study

- Mike Kruzeniski, "From Transportation to Pixels" (2011 essay on Metro's origins).
- MIX10 session "Windows Phone UI and Design Language" (Albert Shum and colleagues, 2010).
- *Windows Phone 7 UI Design and Interaction Guide* (Microsoft, 2010).
