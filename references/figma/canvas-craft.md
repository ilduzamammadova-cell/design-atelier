# Canvas craft

The details a senior designer gets right without being asked: frames, guides, whole pixels, strokes, vectors, text, images, effects, color profile, export, file weight. Apply them to every Figma deliverable, then run the QA list at the end.

API mechanics live in the `figma:figma-use` skill (load it before any `use_figma` call). Numbers for devices, safe areas, targets and breakpoints live in `../dimensions.md`. Auto layout, components, variables, naming and handoff have their own files in this folder: `auto-layout.md`, `components.md`, `variables-and-tokens.md`, `file-structure-and-naming.md`, `handoff.md`.

## 1. Frames and presets

- **Every screen is a top-level frame**, never a group or a section, because prototypes, exports, constraints, scrolling and Dev Mode all key off frames.
- **Start from the Frame tool's presets**, then rename per `file-structure-and-naming.md` (`Payment · Error · 375`). Presets are logical points (1x); never size a frame in physical pixels — a 3x phone screenshot is three times its frame. Sizes: `../dimensions.md`.
- **One width per breakpoint.** Height = the device height for fixed screens; let scrolling pages grow taller, since top-level frames taller than the device scroll in presentation without extra setup.
- **Clip content on**, fill bound to the background variable (not the default white), so the frame previews and exports exactly as the build renders.
- **Draw system chrome in**: status bar, home indicator, on-screen keyboard when an input has focus, as components on top. It keeps safe areas honest and catches content hiding under them.

## 2. Layout guides (formerly "layout grids")

Figma renamed layout grids to **layout guides** in May 2025; they are separate from the grid mode of auto layout (`auto-layout.md`).

- **They still matter with auto layout**: auto layout positions children but shows no column structure. Use column guides to check that content widths and edges land on columns, and for every absolutely positioned or constraint-driven layout.
- **Setup per breakpoint:** Columns, type Stretch, count from `../dimensions.md`, margin = the page-margin token, gutter = the gutter token. Bind them to variables (Plugin API: `setBoundVariableForLayoutGrid` on `count`, `gutterSize`, `offset`, `sectionSize`; the UI documents binding Count) so guides follow the spacing scale.
- **Save one layout guide style per breakpoint** (`grid/mobile`, `grid/tablet`, `grid/desktop`) so every screen at that width uses the same structure.
- **Make the guide real in the layout:** container padding = guide margin, gaps = gutter. Then Figma and CSS grid agree and handoff needs no explanation.
- Add a 4 or 8 px Rows/Uniform guide only to check vertical rhythm or to draw icons. Toggle all guides with Shift+G.

## 3. Constraints (where auto layout doesn't reach)

Use constraints wherever auto layout doesn't position things: absolute children inside auto layout (`auto-layout.md` § 7), decorative layers, illustration internals, icon vectors and any frame without auto layout.

- Options: Left / Right / Left & Right / Center / Scale horizontally; Top / Bottom / Top & Bottom / Center / Scale vertically. Default is Top + Left — usually wrong for anything pinned to the right or bottom.
- Groups can't hold constraints (their children get them), so wrap anything that must resize as a unit in a frame.
- With a Stretch guide, constraints are computed against the nearest column.
- **Test by resizing the parent** to the narrowest and widest breakpoint before calling a screen done.

## 4. Pixel precision

- **Whole pixels for x, y, width, height.** Keep Snap to pixel grid on (Preferences). A half-pixel edge straddles two device pixels and renders as a soft two-pixel smear at 1x — dividers turn grey, icons go fuzzy. Inspect with Pixel preview (1x/2x, View options; Ctrl+P on Mac).
- **Fractions come from**: the Scale tool (K), percentage resizing, centering an odd size in an even one, Center/Scale constraints, rotation (rotation doesn't snap), Fill children splitting an odd width, imported SVG/PDF, and scripts that compute positions. Round in every `use_figma` script.
- **Sizes on the scale**: component heights, padding and radii come from spacing and radius tokens, not from eyeballing.
- **Concentric corners**: inner radius = outer radius − padding, so nested shapes look parallel. Corner smoothing (squircle) only when the build platform renders it — SwiftUI `.continuous` does; plain CSS `border-radius` does not.

| Stroke position | Visual bounds | Use for | Code equivalent |
|---|---|---|---|
| **Inside** (default for shapes and frames) | equal to the layer size | buttons, inputs, cards, any component | `border` with `box-sizing: border-box` |
| **Center** (default for lines; the only option for open paths) | grows by half the weight per side | icon strokes, lines | SVG `stroke` (SVG supports only center strokes) |
| **Outside** | grows by the full weight | focus rings, selection outlines that must not shift layout | `outline` or `box-shadow: 0 0 0 Npx` |

- Center strokes with even weights (2px) stay crisp on whole-pixel paths; odd weights (1px) need the path on a half pixel — the one sanctioned half-pixel position.
- **Per-side stroke weights** for dividers and table rows instead of extra line layers, because they map to `border-bottom` and keep auto layout clean.

## 5. Vectors and icon construction

Grid, keylines, stroke weight and naming come from `../icons.md`. In Figma:

- **Frame per icon** at its size (24×24, clip content, component named per `file-structure-and-naming.md` § 5) with the drawing inside, so exports keep the padding and the viewBox stays constant across the set.
- **Boolean groups (Union, Subtract, Intersect, Exclude) while drawing**, because they stay editable. **Flatten** (Cmd/Ctrl+E) when an icon is final: one vector, one fill or stroke, so color overrides work and SVG output is clean.
- **Outline stroke** (Opt/Alt+Cmd/Ctrl+O) only if the code pipeline expects filled paths. Keep live strokes if code uses `stroke="currentColor"` and a stroke-width token. Choose once per set; never mix.
- **Constraints Scale/Scale on the vector**, so resizing the frame scales the glyph. Stroke weight does not scale with an instance resize, so draw 16/20/24 as separate optical sizes instead of scaling one.
- **Bind the icon's one color** (fill or stroke) to a color variable; no raw hex, no second color unless the style's icon law says duotone.
- Clean vector networks before delivery: no stray points, no hidden helper shapes, no masks left from tracing.

## 6. Text

- **A text style for every step of the type scale**; no unstyled text on a delivered screen. Bind size, line height and letter spacing to variables (`variables-and-tokens.md`).
- **Line height: never Auto in a style.** Auto follows the font's own metrics and silently changes when the font does.
  - **px** for UI styles, in multiples of 4 (16/24, 14/20, 12/16), so text boxes land on the spacing grid. Line-height variables hold absolute numbers (`variables-and-tokens.md` § 7), so variable-bound styles use px.
  - **%** is a multiple of the font size (150% = unitless 1.5 in CSS); use it for fluid or long-form type that isn't variable-bound. Pick one convention per file and tell developers.
- **Letter spacing in %** (a percent of font size: −2% = −0.02em), so it scales with the size. Tighten large display sizes, open up all-caps and tiny labels; tune per face, never one value for all.
- **Paragraph spacing, not empty lines.** An empty line is a fake paragraph carrying a full line height. Lists get list spacing; quotes in editorial layouts get hanging punctuation.
- **Resizing, truncation and vertical trim:** follow `auto-layout.md` § 9. In addition, Max lines works only with Truncate text on and Auto height or Auto width resizing. Test the longest real string and a translation ~30% longer, and annotate the rule for code (`line-clamp`). Use vertical trim only if the build will use `text-box-trim`, or Figma spacing won't match code.
- **OpenType features** (Type settings → Details): tabular figures for prices, tables, timers and anything that updates in place; case-sensitive forms for all-caps; slashed zero for codes and IDs; real fractions; stylistic sets when a law asks. Support varies by font; list each feature for code (`font-variant-numeric`, `font-feature-settings`).
- **Text case in the style** (Uppercase, Small caps) with sentence-case content underneath, so screen readers and code (`text-transform`) get the real text.

## 7. Images

Sourcing, art direction and placeholders: `../imagery.md`. In Figma:

- **Fill** for photos that may crop (cards, heroes); **Fit** for logos and product shots that must never crop; **Crop** to choose the focal area (non-destructive); **Tile** for patterns (size in % of the original).
- **Lock aspect ratios** to the style's 2–3 ratios, so code can use `aspect-ratio` and nothing stretches.
- **Resolution:** source at least 2× the largest display size. Figma scales down any image over 4096 px on its longest side; oversized images cost memory, so downscale before import.
- **Adjustments** (exposure, contrast, temperature…) live only in Figma. Export the adjusted raster for the build, or the original asset in the repo won't match.
- **Placeholders say what's missing**: a tinted field labelled `[photo: courier at the door, 4:5, client to supply]`, listed in the delivery note — never a grey box, never a stand-in presented as real.

## 8. Effects

- **Shadows only as effect styles**, named by role (`elevation/raised`, `elevation/overlay`), 3–4 levels at most, with X, Y, blur, spread and color bound to variables (`variables-and-tokens.md` § 7), so Dark mode can swap shadow color and opacity.
- **Spread renders only** on rectangles, ellipses and frames with a visible fill and clip content on — check before relying on it.
- **Smart Animate does not animate drop or inner shadows** (it falls back to dissolve), so elevation changes crossfade in prototypes.
- **Blur is expensive twice**: stacked blurs and masks are among the heaviest things in a Figma file, and `backdrop-filter` is costly on scroll and on low-end devices. One blurred layer per screen at most (e.g. a fixed nav bar), with a solid fallback.
- **Progressive blur, noise, texture and the Glass effect (beta)** exist. Glass, blur-over-gradient and grain are saturated surface tells (`../anti-slop.md`); use them only when a style law calls for them. Glass reportedly exports to PNG only (verify).

## 9. Color profile

- **Choose the profile deliberately at the start.** New files default to sRGB; the options are sRGB and Display P3 (Unmanaged was retired in August 2023). Change it from the file-name menu → File color profile. **Assign** keeps hex values (appearance shifts); **Convert** keeps appearance (values change). Converting does not touch color styles or variables, and P3 → sRGB clips out-of-gamut colors.
- **Read it first via MCP**: `figma.root.documentColorProfile` (`SRGB`, `DISPLAY_P3`, `LEGACY`) is read-only in the Plugin API, so ask the person to change it in the UI.
- **Default to sRGB** for web and cross-platform work. Use Display P3 only when the build will ship P3 colors (`color(display-p3 …)` with sRGB fallbacks on the web; Display P3 colors on iOS).
- **The mismatch to prevent:** in a P3 file, hex values are P3 coordinates. A developer who pastes that hex into CSS gets an sRGB color, which looks different. Dev Mode output in P3 files has been reported inconsistent (forum, 2025). Say the profile in the handoff note and deliver tokens in the color space the code uses.
- Judge color on a display that supports and is set to the file's profile. Check contrast with the color picker's built-in WCAG 2.2 ratio. It only appears for direct colors, not styles, so check the actual text-on-surface pairs in both modes.

## 10. Export

| Asset | Format | Scale | Settings and reason |
|---|---|---|---|
| UI icon | SVG | 1x | Export the icon frame (keeps padding and viewBox); "Include id attribute" off; one color, so code can map it to `currentColor` |
| Logo, illustration | SVG | 1x | "Outline text" on for wordmarks, so the font isn't required |
| Photo | JPG | 1x + 2x (web), @2x/@3x (iOS) | Figma has no WebP/AVIF export; convert and compress in the build (`../imagery.md` § 6) |
| Raster with transparency | PNG | per platform | Multipliers per platform in `../dimensions.md` § 1; prefer vectors where the platform takes them |
| Print or document | PDF | 1x only | PDF exports only at 1x |

- **Put export settings on the asset layers themselves**, so whoever exports next (developer or designer) gets the intended formats and scales, not a guess.
- **Scale**: `2x` multiplier, `1600w` fixed width, `400h` fixed height. 2x = 144 DPI, 3x = 216 DPI.
- **Naming**: the layer name becomes the file name, lowercase kebab-case by meaning (`icon-close`, `onboarding-step-2`). A `/` in a layer or page name creates folders on export (community-reported), so use it on purpose (`icons/close`). The suffix is appended raw: write `@2x` or `-dark`, not `2x`.
- "Ignore overlapping layers" is on by default (exports only the selection). SVG supports only center strokes, so inside/outside strokes are converted ("Simplify stroke").
- **Export color profile**: Same as file / sRGB / Display P3. Export web assets as sRGB unless the pipeline preserves embedded P3 profiles.

## 11. File performance

- A browser tab has roughly 2 GB of memory for a file (Figma staff, forum — verify the current limit). Watch the memory meter (Manage memory; it can show memory per layer — verify labels).
- **Hidden layers still load.** Delete abandoned alternatives instead of hiding them; in components prefer boolean properties to hidden-layer variants (`components.md`).
- **Downscale images before import**; don't park twenty hidden hero candidates on a screen.
- **Stacked masks, shadows and blurs** cost memory: flatten decorative stacks; simplify imported SVGs with thousands of nodes.
- **Split big files**: move explorations and archived versions to their own file (`file-structure-and-naming.md`).
- **In scripts**: set `figma.skipInvisibleInstanceChildren = true` for read-only audits (much faster traversal), and switch pages once per call (`figma:figma-use`).

### Precision audit (read-only `use_figma`)

```js
figma.skipInvisibleInstanceChildren = true
const page = await figma.getNodeByIdAsync('PAGE_ID'); await figma.setCurrentPageAsync(page)
const frac = v => Math.abs(v - Math.round(v)) > 0.01
const out = []
for (const n of page.findAll(() => true)) {
  if ('width' in n && [n.x, n.y, n.width, n.height].some(frac)) out.push([n.id, n.name, 'fractional'])
  if (n.type === 'TEXT' && n.textStyleId === '') out.push([n.id, n.name, 'no text style'])
}
return out.slice(0, 100)
```

## 12. Shipping as a Figma Site

If the deliverable is a live site built in Figma Sites (launched in open beta at Config 2025; current status — verify): create the breakpoints first (presets Desktop 1280, Tablet 800, Mobile 375, Desktop primary). Use responsive text styles per breakpoint (breakpoint customizations on library styles stay in the file and can't be published). Let responsive components switch variants by breakpoint name. Set HTML tags and alt text on every element. Treat Figma Make output as code: hold it to `../web.md`.

## QA — canvas craft

- [ ] Every screen is a top-level frame at a preset width from `../dimensions.md`, clip on, background bound to a variable.
- [ ] System chrome (status bar, home indicator, keyboard where relevant) drawn; nothing hides under it.
- [ ] Layout guide style applied per breakpoint; margins and gutters match the spacing tokens and the auto layout padding/gaps.
- [ ] Constraint-driven layers survive a resize to the narrowest and widest breakpoint.
- [ ] Precision audit returns nothing: whole-pixel geometry, every text node styled.
- [ ] Stroke positions chosen on purpose: Inside on components, Center on icon paths, Outside for focus rings.
- [ ] Icons: frame per icon, flattened, one bound color, Scale constraints, per-size drawings.
- [ ] Line heights in px or % (no Auto in styles); letter spacing in %; no empty-line spacing.
- [ ] Truncation rules set and tested with the longest string; OpenType features listed for code.
- [ ] Images at ≥ 2× display size, ratios locked, placeholders labelled and listed.
- [ ] Shadows come from effect styles; no more than one blurred layer per screen.
- [ ] File color profile checked and stated in the handoff note; tokens given in the code's color space.
- [ ] Export settings on every asset layer; names kebab-case by meaning; suffixes carry their separator.
- [ ] No abandoned hidden layers; memory meter checked on large files.
