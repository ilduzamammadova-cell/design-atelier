---
id: brutalist-web
name: Brutalist Web
type: movement
discipline: [ui, graphic]
era: 2014–present (roots in the 1990s web)
origin: Worldwide; named by Pascal Deville, Zürich
lineage: [web-1-vernacular, brutalism, punk-graphics]
tags:
  mood: [raw, defiant, deadpan, fast]
  topics: [portfolios, art schools, publishers, galleries, indie tools]
axes: {order: 4, density: 6, ornament: 1, warmth: 3, contrast: 9, geometry: 8, chroma: 4, typevoice: 8, energy: 6, hand: 3, play: 6, era: 5}
---

# Brutalist Web

**Essence:** The web with its structure left showing — default fonts, visible boxes, underlined links and blunt colour — as a refusal of the smooth template.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Defaults as declaration | System fonts, native form controls and unstyled HTML elements are used deliberately, as concrete is left unclad in Brutalist architecture. | `font-family: Times, serif` or `system-ui` or `monospace`; native `<button>`, `<select>`, `<details>` left unstyled; no CSS reset. The browser's materials are the palette. |
| G2 · Structure made visible | Borders around every block, grid lines on show, raw tables — the scaffolding is the ornament. | 1–2 px solid black borders on all containers; layout grid drawn as visible hairlines; no shadows or rounded corners anywhere. |
| G3 · Blunt colour | Either stark black on white or one unapologetic, fully saturated field (pure blue, magenta, yellow). | One "wrong" full-saturation background per site (e.g. `#0000FF` with white text, or `#FFFF00` with black); everything else monochrome. |
| G4 · Overscale and collision | Huge type cropped by the viewport, elements overlapping, grids broken on purpose. | Display type at 15–25vw allowed to crop; one region where elements overlap using `mix-blend-mode: difference`; body text remains readable and unbroken. |
| G5 · Honest, fast hypertext | David Copeland's brutalist web guidelines: content readable everywhere, links underlined, only links and buttons respond to clicks, decoration only when it helps. | Pages under ~100 KB, no JS required to read, every link underlined, no hover-only affordances, no custom scroll. Speed and clarity are part of the look. |
| G6 · One piece of mischief | A strange cursor, a text trail, a marquee — a single act of play in an otherwise severe page. | Exactly one deliberate oddity per site (custom cursor, scrolling ticker, random layout on reload), kept away from critical paths and disabled under `prefers-reduced-motion`. |

## Visual facts

- **Color:** `#FFF`/`#000`; pure RGB primaries `#0000FF`, `#FF0000`, `#00FF00`; system grey `#C0C0C0`.
- **Type:** Times New Roman, Arial/Helvetica, Courier, system UI fonts; occasionally one giant grotesk. Free: **Tinos**, **Arimo**, **Cousine**, **Space Mono**, **Archivo Black**.
- **Form:** rectangles, rules, raw images without frames, native controls, visible URLs.
- **Composition:** either long single-column text or crowded grid of boxes; asymmetric, sometimes deliberately misaligned.

## Attitude

Pascal Deville's brutalistwebsites.com (2014) collected sites that rejected the polished sameness of templated web design; the name borrowed architecture's raw-concrete honesty. Utility sites (forums, classifieds, link aggregators) had always looked this way by indifference; brutalist designers did it on purpose. Distinguish it from the later `neo-brutalism` trend (thick borders, flat offset shadows, candy colours), which is a softened, commercial descendant.

## Blends

- **Amplifies:** `web-1-vernacular`, `punk-graphics`, `command-line-and-teletext` — defaults, DIY, the medium's own materials.
- **Productive tension with:** `swiss-international` — a rigorous grid made literally visible becomes a confident, editorial brutalism.
- **Clashes with:** `mac-os-x-aqua` — candy gloss on raw structure looks unfinished rather than intentional.

## Don't copy

- Specific sites featured on brutalistwebsites.com, well-known fashion-house brutalist sites, the Yale School of Art wiki-site design (Linked by Air, 2006–07), classifieds brands' logos.

## Study

- brutalistwebsites.com (Pascal Deville, Freundliche Grüsse, 2014–).
- David Bryant Copeland, *Brutalist Web Design* guidelines (brutalist-web.design).
- Yale School of Art website by Linked by Air (a user-editable, wiki-like site, 2006–07).
- Reyner Banham, *The New Brutalism* (1966) — the architectural idea behind the name.
