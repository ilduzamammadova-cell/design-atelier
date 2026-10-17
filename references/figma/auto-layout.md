# Auto layout

Load when building or reviewing any frame, component or screen in Figma. This file is the professional *what and why*. The Plugin API *how* (`figma.createAutoLayout()`, `layoutSizing*` value rules, `resize()` ordering, text auto-resize) lives in the `figma:figma-use` skill, `references/gotchas.md` and `references/plugin-api-patterns.md`. Do not restate it; follow it.

Related: [components.md](components.md) · [variables-and-tokens.md](variables-and-tokens.md) · [canvas-craft.md](canvas-craft.md) · [file-structure-and-naming.md](file-structure-and-naming.md).

Checked against help.figma.com, Figma forum product updates and the Plugin API typings (October 2026). "(verify)" marks anything not confirmed in a primary source.

## 1. Mental model: every frame is a CSS container

A frame that holds related children is a flex or grid container. Decide the CSS first, then set the Figma control that produces it, the developer will read it back as CSS in Dev Mode.

| Figma control | CSS it means | Note |
|---|---|---|
| Flow: Horizontal / Vertical | `display:flex; flex-direction: row / column` | One axis |
| Flow: Grid | `display:grid`, tracks in `fr` / px / fit-content | Two axes; out of beta, all plans |
| Gap (number) | `gap` | Bind to a space variable |
| Gap: Auto → Between / Around / Evenly | `justify-content: space-between / space-around / space-evenly` | Around + Evenly added Aug 2026 |
| Padding | `padding` | Bind every side to variables |
| Hug contents | `width: fit-content` (`flex: none`) | Containers and text only |
| Fill container | main axis `flex: 1 1 0`; cross axis `align-self: stretch` | Children only, never top-level |
| Fixed | `width: <n>px` | |
| Min / max width, height | `min-width`, `max-width`, … | Accept number variables |
| Wrap (H/V flows only) | `flex-wrap: wrap` + `row-gap` | Not masonry: order is kept |
| Ignore auto layout (formerly "absolute position") | `position:absolute` inside a `relative` parent | Uses constraints |
| Canvas stacking (first / last on top) | DOM order, `z-index` | Matters for negative gap |
| Strokes included in layout | `box-sizing: border-box` | Inside strokes only |
| Align baseline (key `B`) | `align-items: baseline` | Icon + text rows, mixed sizes |
| Text max lines + truncate | `-webkit-line-clamp`, `text-overflow: ellipsis` | Max lines and max height are exclusive |

Rule: if you cannot say which CSS a frame produces, the frame is wrong or unnecessary.

## 2. Layout version (new engine, 2026)

Figma shipped a new auto layout version. Since July 2026 it is the default for new frames; the per-frame **Layout version** toggle (auto layout settings, or Actions → "Update layout version for selection/page") disappears in January 2027 and becomes an Update button.

| Changed behaviour (new version) | Consequence for you |
|---|---|
| Padding is always respected; a frame can never be narrower than its padding (overrides max width) | Old frames may grow after upgrade, reduce padding, don't fight it |
| Inside strokes count in layout by default; outside/center strokes never do | A 1→2 px border change between states shifts content; keep stroke width constant or use an outside stroke |
| Fill children split space by content box (CSS border-box) | Use a grid with `1fr` tracks when columns must be exactly equal |
| Auto gap never goes below 0 | No accidental overlap; overlap needs an explicit negative gap |
| A single child in Between aligns to start | Use Around/Evenly or alignment for centred lone items |

Instances cannot override the layout version: upgrade the main component, review shifts, republish. Check an inherited library's version before editing it.

## 3. Hug, Fill, Fixed, decide from content outward

Size flows from the innermost content: the label sizes the button, buttons size the toolbar, the viewport sizes the page.

| Use | When | Examples |
|---|---|---|
| **Hug** | The container's size should come from its content | Button, chip, tag, badge, menu item label, tooltip |
| **Fill** | The child should take the space its parent gives | Input in a form, card in a row, text block in a column, list row, divider |
| **Fixed** | The size is a design decision, not a result | Icon (16/20/24), avatar, thumbnail, top-level frame width (device/breakpoint) |
| **Hug + min** | Content-sized but must meet a floor | Button `min-width` 44 to 48 (touch target), tag min width |
| **Fill + max** | Stretch, but readable or bounded | Text column max 640 to 720 px (~65 ch), dialog max 560, content container max 1200 to 1440 |

- A Hug parent with a Fill child becomes Fixed on that axis, Figma does this silently; check it was intended.
- Fill on the main axis divides free space; on the cross axis it stretches. Two Fill children = equal shares of what is left, not equal widths.
- Heights: almost always Hug. A Fixed height on anything containing text is a clipping bug waiting for a translation.

## 4. Spacing: gap, padding, auto

| Need | Use | Why |
|---|---|---|
| Space between siblings | **Gap** bound to `space/*` | One source; survives reorder and hide |
| Space between a container's edge and content | **Padding** bound to `space/*` (inset) | Belongs to the container, not the child |
| Push groups to opposite edges (nav: logo ↔ actions) | **Auto gap → Between** on a parent with two child groups | Mirrors `space-between`; no spacer layers |
| Equal distribution (tab bar, segmented control) | **Evenly** / **Around**, or Fill children | Matches CSS spacing vocabulary |
| Overlap (avatar stack) | Explicit negative gap + canvas stacking set deliberately | The only legitimate negative gap |

- Never use spacer rectangles, empty frames or transparent padding to make space, the developer gets meaningless DOM.
- Never put padding on children to fake a gap between siblings; it doubles at the edges and breaks when one child hides.
- Bind gap and padding to **semantic** space variables (`space/inset-md`, `space/stack-lg`) or the scale (`space/4`), never raw numbers. Scope those variables to `GAP` (covers gap and padding). See `variables-and-tokens.md`.
- Gaps follow a rhythm: related items closer than unrelated (proximity). If every gap in a card is the same, hierarchy is missing.

## 5. Wrap

Use Wrap (horizontal flow) for collections that reflow: chips, tags, filter pills, card grids with a min width. Set the counter-axis spacing (row gap) separately, it often wants to be smaller or larger than the column gap. Give children a min width (or Fixed width) so the break point is predictable. Wrap is not masonry: items keep order and fill row by row. For true two-axis alignment (columns that line up across rows) use a grid.

## 6. Grid auto layout

Grid is the third flow: rows × columns of cells. Use it when items must align on **both** axes.

| Use grid for | Keep horizontal/vertical for |
|---|---|
| Dashboards, bento layouts, galleries, calendars | Stacks, toolbars, forms that are one column |
| Label/value forms with aligned columns | Rows whose items have no column relationship |
| Exactly equal columns (`1fr` each) | Content-sized sequences (chips) |

- Tracks are **Fixed** (px), **Fill** (`fr`, type `A`/"Auto" = `1fr`) or **Hug**. Rows default to an Auto count that grows with children.
- Children span cells with Row span / Column span; a child must be Fill to span.
- "Automatic positioning" is on by default; turn it off only when empty cells are intentional.
- Grid children do not wrap. Column count is **not** variable-bindable (row/column gaps are), so each breakpoint frame sets its own column count.
- Grid auto layout is a different feature from layout-guide grids (uniform/column guides). Use guides to *check* alignment; use grid auto layout to *produce* it.
- Dev Mode CSS output for grid tracks and spans (verify before promising developers exact CSS).

## 7. Ignore auto layout (absolute escapes)

Legitimate: notification dot on an avatar, close button in a dialog corner, focus ring that must not shift layout, decorative overlays, floating badges. The child stays in the frame, leaves the flow, and uses constraints (e.g. Top + Right).

Not legitimate: positioning real content. More than one or two absolute children in a frame means the structure is wrong, rebuild it as nested flows.

## 8. Nesting: every frame must earn its place

A frame exists only if it changes at least one of: direction, gap, padding, alignment, background/stroke/radius, clipping, or it is a semantic unit a developer will name (a `<header>`, a list item).

- Typical depth inside a component: 2 to 4 levels. Screens: page → section → container → group → item. Deeper than ~6 is usually wrapper soup.
- A frame with one child and no fill, padding or alignment change is a wrapper: remove it.
- Two sibling frames with identical settings next to each other usually want to be one frame with a gap.
- Name every frame for its role (`header`, `actions`, `body`, `meta`), never `Frame 427`. Layer names feed Dev Mode, Code Connect and `get_design_context`.

## 9. Text resizing

| Text role | Resizing | Plus |
|---|---|---|
| Single-line label in a Hug container (button, chip) | Auto width | Never wraps; container hugs it |
| Paragraph, description, any wrapping text | Fill width + Auto height | Bound text style; Hug parent height |
| Title in a constrained card/row | Fill width + max lines (1 to 2) + truncate | Test with 2× length |
| Fixed size | Almost never | Overlaps when content grows |

- Use the style's text styles with line height bound to variables; never set a frame height to "fit" text by eye.
- Vertical trim (cap height to baseline, Plugin API `leadingTrim`) gives optically centred labels in buttons; it maps to CSS `text-box` trimming, whose browser support you must check (verify).
- Baseline-align rows that mix sizes (price + unit, label + value).

## 10. Responsive behaviour across breakpoints

Figma Design has no media queries. Simulate them honestly:

1. One top-level frame per breakpoint, **Fixed** width (sizes from `../dimensions.md`), Hug height. Everything inside is Fill or Hug.
2. A `viewport` (or `dimension`) variable collection with modes (e.g. Mobile / Tablet / Desktop) for page margins, section gaps, grid gaps and type sizes. Set the mode once on each top-level frame; children inherit (Auto mode).
3. Content containers: Fill + max width + centred, so desktop never stretches a text column to 1600 px.
4. Structure changes (sidebar → bottom tabs, table → cards) are different components or variants, not squeezed layouts.
5. Stress test every frame: resize it narrower and wider, paste double-length strings, toggle every boolean, switch every mode. Nothing may clip, overlap or overflow. Confirm with `get_screenshot`.

## 11. Common professional mistakes

| Mistake | How to spot it | Fix |
|---|---|---|
| Frames with absolute x/y children | `get_metadata`: children with no layout mode parent | Wrap in auto layout; see figma-use Rule 12a |
| Spacer rectangles or empty frames | Layers named `spacer`, empty frames with fixed size | Delete; use gap/padding |
| Raw gap/padding numbers | `get_variable_defs` on the node returns no space variable | Bind to `space/*` |
| Fixed height on text containers | Text clipped after a longer string or mode switch | Hug height |
| Fixed-size text boxes | Text overlaps siblings when edited | Auto height + Fill width |
| Hug parent silently turned Fixed | Parent stops growing with content | Re-evaluate which child should Fill |
| Wrapper soup | Depth > 6, single-child frames | Unwrap; one frame per real change |
| Equal widths expected from Fill | Columns differ by content | Grid with `1fr` tracks |
| State changes that shift layout | Hover/focus variant jumps by 1 to 2 px | Constant stroke width; outside stroke or absolute ring for focus |
| Absolute-positioned content | Many "Ignore auto layout" children | Rebuild as nested flows |
| Gaps all identical | No grouping by proximity | Smaller gaps inside groups, larger between |
| Legacy layout version in a library | Layout version setting shows legacy | Upgrade main components, review, republish |

## 12. QA checklist

- [ ] Every container with related children uses auto layout; no absolute content.
- [ ] Every gap, padding, min/max and radius is bound to a variable; no raw numbers.
- [ ] Each frame's sizing (Hug/Fill/Fixed) is a stated decision; no Fixed heights around text.
- [ ] Text: Auto width for labels, Fill + Auto height for paragraphs, truncation where space is fixed.
- [ ] Min/max set for touch targets, readable measure and bounded containers.
- [ ] Two-axis alignment uses grid; one-axis uses flex flows; no fake grids from nested stacks.
- [ ] Absolute children only for overlays, badges, focus rings.
- [ ] No wrapper frames, spacers or `Frame 123` names.
- [ ] New layout version on every component; libraries republished after upgrade.
- [ ] Stress test passed: resized, long text, booleans toggled, every mode switched; screenshot checked.
