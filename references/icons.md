# Icons

Icons are where most interfaces quietly become generic: the same default outline set, at the same size, in every product. In a personal style the icon set must *belong* — its stroke, corners and terminals should look drawn by the same hand as the type.

## House rule: monochrome and simple

Icons are **one color, simple, and black by default** (`currentColor`, so they take the ink token and follow light/dark mode). No multicolor, no gradients, no duotone, no shadows, no opacity layers — unless the person explicitly asks for them. A personal style shows in an icon's construction (corners, terminals, stroke, proportion), never in added color.

Two icon languages, pick one per set (per product, usually one; a solid variant of the outline set is allowed for selected/active states):

| | **Outline (line)** | **Solid (glyph)** |
|---|---|---|
| Looks like | Drawn with one even pen: e.g. a school-supplies set of books, pencils, flasks, globes | Filled silhouettes: e.g. a naval set of ships, anchors, lifebuoys |
| Grid | 24×24, 2px padding (live area 20) | 24×24, 2px padding |
| Construction | One stroke weight for every line, inner details included (1.5–2 at 24); caps and joins round or square — one choice for the whole set; small dots as filled circles allowed | Solid fill, no strokes; inner details are **cut-outs** (holes in the shape, `fill-rule="evenodd"` or path subtraction) — never white shapes on top, so the icon works on any background |
| Detail | Only what identifies the object; 3–6 inner lines at most | Strong, recognisable silhouette first; details as 1.5–2px knockout gaps; no part thinner than 1.5px |
| Reads best | UI navigation, toolbars, dense product UI, airy styles | Small sizes, maps, signage, bold styles, active/selected states |

Organise sets the way a professional library does: themed category groups of up to 20 icons (5 per row), named `<theme>-icons-<NN>-<category>` — e.g. `edu-icons-01-supplies`, `edu-icons-02-science`, `naval-icons-05-rigging`, `naval-icons-06-safety`. Each icon is named by meaning (`microscope`, `life-buoy`, `anchor`), never by appearance or number.

## Decide: library, adapted library, or custom

| Situation | Choice |
|---|---|
| Product UI with many icons, small team, tight time | **Library**, chosen to match the style's type and geometry (table below) |
| Style has a strong shape law (cut corners, pixel grid, ink edge, seams) | **Adapted library** — keep a library's metaphors, redraw or post-process to the law |
| Brand-led piece, marketing site, small icon count (< 30), or a style whose Voice gene is about form | **Custom set** drawn from the style's laws |

The default answer in the generic-AI look is Lucide at 24px, 2px stroke, everywhere. Choosing it is fine *when it is chosen*: say why it fits this style's type.

## Matching an icon set to the style

Match these properties to the typeface first, then to the style laws:

| Property | Read it from | Rule of thumb |
|---|---|---|
| **Stroke weight** | Text face stem weight at icon size | Icon stroke ≈ the text's vertical stem at the size the icon sits next to. Light text + heavy icons looks pasted on. |
| **Corners & terminals** | Type terminals, radius tokens | Rounded terminals with round-terminal type (e.g. humanist/rounded sans); square/butt caps with grotesks and slab serifs. |
| **Geometry** | `geometry` axis | ≥ 7: strict circles/squares, 45°/90° only. ≤ 3: hand-drawn or calligraphic curves. |
| **Fill** | `contrast`, `density` | Airy, quiet styles: outline. Bold, high-contrast or small-size use: solid. Outline for idle + solid for active is the one allowed mix. |
| **Detail** | `ornament`, size | Fewer strokes at small sizes. Ornamental styles can carry detail at 32px+, never at 16px. |
| **Optical size** | where icons appear | Draw or pick per size (16 / 20 / 24); don't just scale one 24px drawing down. |

## Library field guide

Verify licences on the project's terms before shipping; they change.

| Library | Character | Fits styles that are… |
|---|---|---|
| **Lucide** (Feather lineage) | 24px grid, uniform stroke, rounded caps, very neutral | neutral-humanist; the safe default — and therefore the generic one |
| **Phosphor** | Six weights (thin → bold, fill, duotone) from one family | styles needing weight variation; thin weight suits light, airy, editorial styles |
| **Tabler** | Large set, 24px, 2px stroke, outline + filled | dense product UI with many concepts |
| **Heroicons** | Outline, solid, mini, micro sizes; Tailwind-adjacent | utilitarian product UI; strongly associated with the default Tailwind look |
| **Iconoir** | Thin, clean 1.5px stroke | light, calm, Swiss-leaning styles |
| **Material Symbols** | Variable font: fill, weight, grade, optical size | systematic styles that want icon weight to track text weight exactly |
| **Fluent UI System Icons** | Soft geometry, regular + filled | calm, friendly productivity UI |
| **IBM Carbon icons** | Rational, squared, engineered | technical, data-dense, institutional styles |
| **Radix Icons** | 15×15, crisp, minimal | compact tool UI, small sizes |
| **Pixelarticons** and other pixel sets | Hard pixel grid | retro-computing, game, terminal-gene styles |
| **SF Symbols** | Apple platforms only, weight-matched to SF | native Apple apps only — not for web |

## Drawing a custom set from the style

1. **Grid:** choose the base (16/20/24) from the type size the icons sit beside. Define keylines (circle, square, portrait and landscape rectangles) on that grid.
2. **Stroke:** equal to the text stem at that size; round or square caps per the type's terminals.
3. **Laws apply — to shape only:** if the style says "joints are visible", icon strokes meet with a visible notch; if "cut corners", every corner is a 45° cut of the same size. Keep it subtle: an icon must stay simple and instantly readable. Laws never add color, texture or gradients to icons.
4. **Metaphors:** one idea per icon, borrowed from the style's world when possible (a ledger style can use a tick in a box from bookkeeping rather than a generic check-circle).
5. **Core set first:** navigation (home, search, menu, back, close), actions (add, edit, delete, share, download), states (success, warning, error, info, loading). Expand only as the product needs.
6. **Deliver** as SVG with `currentColor`, consistent viewBox, no transforms; and as a Figma component set with size variants.

### Producing the set

Draw icons as real SVG, not described in prose:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
     stroke="currentColor" stroke-width="1.5" stroke-linecap="square" stroke-linejoin="miter">
  <circle cx="11" cy="11" r="6"/>
  <path d="M15.5 15.5 20 20"/>
</svg>
```

- One file per icon, named by meaning in kebab-case (`search.svg`, `arrow-left.svg`, `shift-night.svg`) — never `icon-1` or `vector`.
- Keep 2px of padding inside the viewBox (live area 20 on a 24 grid); align strokes so they land on whole or half pixels at 1×.
- Put shared attributes (fill, stroke, width, caps, joins) on the root `<svg>` so the whole set changes together.
- Run the checker with the set's language and fix every issue before delivery:
  ```bash
  python3 <skill-dir>/scripts/icon_check.py path/to/icons/ --style outline   # or --style solid
  ```
- Render the set at 16, 20 and 24px on both light and dark surfaces and look at it as a group: equal visual weight, equal optical size (circles slightly larger than squares), same corner logic.
- In Figma, build each icon as a component (`icon/search`), with the stroke bound to a color variable, in a size-variant set; export as SVG from the components.

## Rules that hold in every style

- Icons that act need a text label or an accessible name; icon-only buttons need `aria-label` and a tooltip.
- Never use emoji as interface icons.
- One set per product. Mixing two libraries is visible even to non-designers.
- Hit area ≥ 24×24 CSS px (WCAG 2.2 target size minimum), 44×44 recommended for touch, regardless of glyph size.
- The ✨ "AI sparkle" is a saturated trend; if the product has AI features, find a metaphor from the style instead.
