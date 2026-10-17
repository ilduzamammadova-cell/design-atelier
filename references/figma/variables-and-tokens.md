# Variables and tokens

Load before creating, renaming, binding or exporting any variable or style in Figma. This file is the professional *what and why*. The Plugin API *how* (creating collections and modes, `VARIABLE_ALIAS`, `scopes`, `setVariableCodeSyntax`, binding paints, text and effect styles) lives in `figma:figma-generate-library` → `references/token-creation.md` and in `figma:figma-use` → `references/variable-patterns.md`, `text-style-patterns.md`, `effect-style-patterns.md`.

Related: [auto-layout.md](auto-layout.md) · [components.md](components.md) · [file-structure-and-naming.md](file-structure-and-naming.md) · [handoff.md](handoff.md) · CSS names in `../web.md`, motion values in `../motion.md`.

Checked against help.figma.com, Figma's Schema 2025 recap, the plugin changelog, the Plugin API typings and the W3C DTCG reports (October 2026). "(verify)" marks anything not confirmed in a primary source.

## 1. Architecture: primitive → semantic → component

| Tier | Holds | Example | Bound to layers? | Scope | Publish |
|---|---|---|---|---|---|
| **Primitive** | Raw values: palettes, scales, font families | `color/blue/500 = #2963ED`, `space/4 = 16` | Never | `[]` (hidden from pickers) | Hide from publishing, or publish unscoped |
| **Semantic** | Decisions by role; carries the modes | `color/accent → color/blue/500` (Light), `→ color/blue/300` (Dark) | Yes, the default | Specific | Yes |
| **Component** (optional) | One component's decision | `button/bg/primary/rest → color/accent` | Only inside that component | Specific | Yes |

- Semantic tokens never hold raw values; every value in every mode is an alias. A raw value there survives a mode switch but cannot follow a palette change.
- Add the component tier only when a component must diverge from the semantic layer or be themed on its own (multi-brand). Figma's own guidance: many systems need only primitives + semantics.
- Fonts and motion rarely need aliasing; a single semantic tier is fine for them.

## 2. Collections and modes

One collection per **independent mode axis**: a frame sets one mode per collection, so independent axes (theme × density × viewport) combine freely without multiplying modes.

| Collection | Modes | Contains |
|---|---|---|
| `[style]/primitives` | one (`Value`) | Color ramps, the space/radius/size scales, font families and sizes |
| `[style]/color` | `Light`, `Dark` (+ `High contrast` if required) | Semantic colors |
| `[style]/dimension` | one, or `Compact` / `Default`, or `Mobile` / `Desktop` | Semantic space, radius, size, border widths |
| `[style]/type` | one, or `Mobile` / `Desktop` | Font sizes, line heights, tracking, bound inside text styles |
| `[style]/motion` | one, or `Standard` / `Reduced` | Durations (TIMING) and easings (EASING) |

This refines the two-collection layout in `../figma.md`: a single `[style]/semantic` collection with Light/Dark is fine while color is the only thing that changes; split it the moment a second axis (density, viewport) appears.

- **Limits:** modes per collection, Professional 10, Organization 20 (Schema 2025); Enterprise higher (verify); Starter has no modes. Up to 5,000 variables per collection.
- **Inheritance:** layers default to Auto and take the nearest parent's explicit mode; with none set, the collection's default (leftmost) mode applies. Set modes on top-level frames or pages, never layer by layer.
- **Brands:** on Enterprise, use **extended collections**, a brand extends the base collection, inherits its variables and modes, and overrides only the values it changes; untouched values keep following the parent. Extensions override values; per the Plugin API type they cannot add modes of their own (verify). Elsewhere: brand modes in the color collection, or one library file per brand.
- **Variants driven by modes:** a string (or number) variable bound to an instance's variant property switches the variant when the mode changes; values must match the variant values exactly.
- Mode names are labels, so Title Case is fine. Never create a mode per screen or per component.
- **Prototype variables** (cart count, signed-in, selected tab) go in their own `_prototype` collection, hidden from publishing and never aliased into design tokens, they are app state, not design decisions.

## 3. Aliasing rules

| Rule | Why |
|---|---|
| Alias downward only: component → semantic → primitive | A skipped tier is a value the theme switch silently misses |
| Same type only (color → color, number → number) | Figma enforces it; mixed meanings break export |
| Chains ≤ 3 hops, no cycles | Debuggable in Dev Mode; DTCG tools must reject cycles |
| Cross-collection aliases are fine within a file | The normal primitive → semantic link |
| Library variables must be subscribed/imported before aliasing | The Plugin API cannot alias across files directly |
| Never duplicate a primitive's value in a semantic token | One change must propagate everywhere |

## 4. Scoping: show each variable only where it belongs

Never leave `ALL_SCOPES` (the default). Scopes filter the UI pickers; they do not block binding through the API, so scope **and** review bindings.

| Variable | Scopes |
|---|---|
| Primitives (any type) | `[]` |
| `color/bg`, `color/surface` | `FRAME_FILL`, `SHAPE_FILL` |
| `color/ink*` (text) | `TEXT_FILL` |
| Icon color | `SHAPE_FILL`, `STROKE_COLOR` |
| `color/line`, `color/focus` | `STROKE_COLOR` (+ `EFFECT_COLOR` if the focus ring is a spread shadow) |
| Shadow / scrim color | `EFFECT_COLOR` |
| `space/*` (gap and padding) | `GAP` |
| `radius/*` | `CORNER_RADIUS` |
| `size/*`, min/max widths | `WIDTH_HEIGHT` |
| `border/*` widths | `STROKE_FLOAT` |
| `opacity/*` | `OPACITY` |
| Blur radius | `EFFECT_FLOAT` |
| Font size / line height / tracking / paragraph spacing | `FONT_SIZE` / `LINE_HEIGHT` / `LETTER_SPACING` / `PARAGRAPH_SPACING` |
| Font family / style name / numeric weight | `FONT_FAMILY` / `FONT_STYLE` / `FONT_WEIGHT` |
| Localised copy (string) | `TEXT_CONTENT` |
| Boolean | no scopes exist |

`ALL_FILLS` covers frame, shape and text fills at once and excludes the individual fill scopes, prefer the individual ones.

## 5. Code syntax

Set Web, iOS and Android code syntax explicitly on every semantic and component variable; Dev Mode then shows CSS, SwiftUI and Compose snippets with the real names. Do not rely on Dev Mode's automatic slash-to-hyphen names (digit-handling bugs have been reported). Use the codebase's actual names when they exist.

| Figma variable | Web | iOS | Android |
|---|---|---|---|
| `color/ink-muted` | `var(--color-ink-muted)` | `Color.inkMuted` | `colorInkMuted` |
| `space/inset-md` | `var(--space-inset-md)` | `Spacing.insetMd` | `spaceInsetMd` |

Web syntax includes the `var()` wrapper (figma-generate-library rule). Renaming a variable does not change its code syntax, update both deliberately.

## 6. Naming grammar

- `/` makes a group in the Variables panel; segments are lowercase kebab-case. `.`, `{`, `}` and `$` are rejected by Figma and forbidden by DTCG, write `space/half`, not `space/0.5`.
- Order from broad to narrow: **category / property / variant / state**. Omit slots you do not need; never reorder them.
- A name is never both a token and a group (`color/accent` *and* `color/accent/hover`): DTCG would need `$root` and most tools break.
- One name, mechanically transformed everywhere: Figma `color/ink-muted` ↔ CSS `--color-ink-muted` ↔ DTCG `color.ink-muted` ↔ alias `{color.ink-muted}`.
- No values or brand names in semantic names (`color/blue-text` ✗); primitives use scale steps (`space/4`), not pixels, so the scale can be retuned without renames. Prefer full words; keep short forms (`bg`, `md`) only where code already uses them.
- Kebab-case in Figma and CSS; camelCase only in iOS/Android code syntax, or where the codebase is camel (Primer's `bgColor`).

Two grammars, pick one per file:
- **Compact** (a personal style, under ~100 tokens): `category/role[-variant][-state]`. It is the style-spec vocabulary and produces exactly the CSS names in `../web.md`.
- **Full** (multi-product system): `category/property/variant/state`, with an explicit `rest` state on anything stateful (as Primer does): `color/bg/accent/rest`, `color/bg/accent/hover`.

| Category | Primitive | Semantic (compact) | Full / component |
|---|---|---|---|
| Color | `color/blue/500`, `color/neutral/900` | `color/bg`, `color/surface`, `color/ink`, `color/ink-muted`, `color/accent`, `color/accent-hover`, `color/on-accent`, `color/line`, `color/focus`, `color/danger` | `color/text/muted`, `color/bg/accent/hover`, `button/bg/primary/rest` |
| Space | `space/1` … `space/12` | `space/inset-md`, `space/stack-lg`, `space/inline-sm`, `space/gutter`, `space/section` | `card/padding` |
| Radius | `radius/sm`, `radius/md`, `radius/full` | `radius/control`, `radius/card` | `button/radius` |
| Size | `size/4` … `size/12` | `size/icon-sm`, `size/icon-md`, `size/control-md`, `size/touch-min` | `avatar/size/lg` |
| Border | `border/sm`, `border/md`, `border/lg` | `border/hairline`, `border/focus` | `input/border/error` |
| Typography | `font/family/display`, `font/size/1` … `font/size/8`, `font/weight/regular` | text styles `display/lg`, `heading/md`, `body/md`, `label/sm`, `mono/sm` (fields bound to variables) | `button/label/size` |
| Motion | none | `duration/fast`, `duration/base`, `ease/standard`, `ease/enter`, `ease/exit` | `dialog/duration/enter` |
| Opacity | none | `opacity/disabled`, `opacity/scrim` | none |

## 7. Styles or variables

| Need | Use | Why |
|---|---|---|
| A single color, number, string or boolean that may change by context | Variable | Modes, scopes, code syntax, aliasing |
| Typography (family + size + weight + line height + tracking) | Text style, each field bound to variables | No composite variable type; the style becomes mode-aware through its bound fields |
| Shadow, elevation, blur | Effect style; color, offsets, radius and spread bound to variables | Composite value |
| Gradient | Paint style; each stop bound to a color variable | Variables cannot hold gradients |
| Several fills, image fills | Paint style | Composite value |
| Layout guides | Grid style; count, gutter, offset bound to variables | Composite value |
| Duration and easing | TIMING (seconds) and EASING variables, Plugin API since Aug 2026; check the Variables UI and prototype binding in your account (verify) | Matches the motion tokens in `../motion.md` |

Styles have no modes, scopes or code syntax of their own. Line-height variables are absolute numbers, not percentages, store a value per size and per mode (verify).

## 8. One vocabulary in Figma and code (DTCG)

The W3C Design Tokens Format Module **2025.10** (28 Oct 2025) is the first stable version of the format; theming lives in the companion **Resolver Module 2025.10**. Neither is a W3C Standard, but tools converge on them, and Figma's native variable export follows DTCG (announced at Schema 2025, rolled out per account from Nov 2025, check availability; early exports dropped descriptions) (verify).

| Figma | DTCG | CSS |
|---|---|---|
| Collection | File or top-level group | none |
| Mode | Resolver modifier context (`theme`: `light` / `dark`) | `:root`, `@media (prefers-color-scheme: dark)`, `[data-theme="dark"]` |
| Group `color/` | Group `"color": {}`, `$type` inherited by children | Name prefix |
| Variable `color/blue/500` | Token `color.blue.500` with `$value` | `--color-blue-500` |
| Alias | `"{color.blue.500}"` (or JSON Pointer `$ref`) | `var(--color-blue-500)` |
| COLOR / FLOAT / STRING | `color` / `dimension` or `number` or `fontWeight` / `fontFamily` | value |
| TIMING (seconds) / EASING | `duration` (`ms`/`s`) / `cubicBezier` | `ms` / `cubic-bezier()` |
| Text / effect / gradient style | `typography` / `shadow` / `gradient` composite | several properties |
| Description, scopes, code syntax | `$description`; tool data under `$extensions` (reverse-domain keys) | comment |

```json
{
  "color": {
    "$type": "color",
    "blue": { "500": { "$value": { "colorSpace": "srgb", "components": [0.16, 0.39, 0.93], "hex": "#2963ed" } } },
    "accent": { "$value": "{color.blue.500}", "$description": "Primary action fill" }
  },
  "space": { "$type": "dimension", "4": { "$value": { "value": 16, "unit": "px" } } },
  "duration": { "$type": "duration", "fast": { "$value": { "value": 120, "unit": "ms" } } }
}
```

```css
:root { --color-blue-500: #2963ed; --color-accent: var(--color-blue-500); --space-4: 16px; --duration-fast: 120ms; }
```

DTCG details to respect: dimensions are objects with `px` or `rem`; colors carry `colorSpace` + `components` with optional `alpha` and `hex` fallback; `$type` is never inferred from the value; names are case-sensitive; files use `.tokens.json`. Figma TIMING stores seconds, convert to `ms` on export. The Variables REST API is Enterprise-only (verify); export through `use_figma` (Plugin API) works on every plan.

## 9. Versioning and deprecation

- Version the token set with semver and say it in the library publish message: **major** = rename, removal or change of meaning; **minor** = new tokens or modes; **patch** = value tuning within the same meaning.
- Renaming a Figma variable keeps layer bindings (they are by ID) but breaks code names and DTCG paths, treat it as major and update code syntax on purpose.
- Deprecate before deleting (unlike components, do not move variables into a `Deprecated/` group, that is a rename): keep the name, start the description with `Deprecated v2.0, use color/ink-muted`, set scopes to `[]` so it leaves the pickers while existing bindings still resolve, and emit `"$deprecated": "Use {color.ink-muted}"` in DTCG.
- Delete at the next major only when usage is zero (scan bindings with `use_figma`; spot-check screens with `get_variable_defs`; Check designs / library analytics on Organization and Enterprise (verify)).
- Make large token changes on a branch where the plan allows it, and never change a token's meaning while keeping its name.

## 10. QA checklist

- [ ] Three tiers respected: primitives unscoped and unbound; semantics alias primitives in every mode; component tokens alias semantics.
- [ ] One collection per mode axis; modes set on top-level frames or pages; mode count within the plan limit.
- [ ] No `ALL_SCOPES`; every variable scoped to the properties it belongs to.
- [ ] Web/iOS/Android code syntax set on every semantic and component variable, matching code names.
- [ ] Names follow one grammar; no `.` `{` `}` `$`; no name is both a token and a group; no values or brand names in semantic names.
- [ ] Text styles, effect styles and gradients bind their fields to variables; no raw hex or px inside them.
- [ ] `get_variable_defs` on representative nodes shows only semantic or component variables, no raw values, no primitives.
- [ ] Both modes contrast-checked: text ≥ 4.5:1, large text and UI parts ≥ 3:1.
- [ ] DTCG export (or CSS) round-trips with the same names; motion converted from seconds to ms.
- [ ] Deprecated tokens described, unscoped and listed in the changelog; no meaning changed under an old name.
