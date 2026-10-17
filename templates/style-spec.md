---
style: [Style Name]
slug: [style-slug]
owner: [profile slug]
version: 1
created: YYYY-MM-DD
axes: {order: 5, density: 5, ornament: 5, warmth: 5, contrast: 5, geometry: 5, chroma: 5, typevoice: 5, energy: 5, hand: 5, play: 5, era: 5}
---

# [Style Name]

> One sentence a non-designer would understand: what using something in this style feels like.

## 1. Laws

Five to seven absolute, testable constraints. Each traces to a gene.

| # | Law | Gene · source |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

## 2. Lineage

| Role | Gene | Source id | How it was transformed |
|---|---|---|---|
| Spine | | | |
| Voice | | | |
| Accent | | | |
| Personal | | (person's life) | |
| Behavior (opt.) | | | |

Distance check: nearest atlas card `[id]` at d=[x]; nearest trend `[id]` at d=[x] (saturation [n]).

## 3. Fit

- **Strong for:** [product types, contexts]
- **Weak for:** [where it strains, and the adaptation to use there]

## 4. Tokens

### Color
| Token | Light | Dark | Use | Contrast |
|---|---|---|---|---|
| `bg` | | | page | — |
| `surface` | | | cards, panels | — |
| `ink` | | | body text | x:1 on bg |
| `ink-muted` | | | secondary text | x:1 on bg |
| `accent` | | | [where exactly] | x:1 |
| `on-accent` | | | text on accent | x:1 |
| `line` | | | borders, seams | x:1 (UI ≥ 3:1) |
| `danger` / `success` | | | states | x:1 |

Rules: [how much accent per view, forbidden combinations, how color behaves]

### Typography
- **Display:** [family] — weights, tracking, case
- **Text:** [family] — weights, size/line-height
- **Mono / utility (opt.):** [family]
- **Scale:** [steps in px/rem and the logic behind them]
- **Licensing / free alternative:** [Google Fonts or open fallback]

### Shape, depth, space
- **Radius:** [values + where]
- **Border / seam:** [width, color, where]
- **Depth:** [shadow values, or "none — depth comes from …"]
- **Spacing scale:** [base unit and steps]
- **Grid:** [columns, gutters, margins per breakpoint]

## 5. Layout grammar

How a screen is composed in this style: alignment, density, where the eye lands first, image treatment, how sections end.

## 6. Components

For each: what makes it *this style's* version, not the default.
- **Button** (default / hover / active / focus / disabled / loading)
- **Input & form** (label, help, error)
- **Card / list item**
- **Navigation**
- **Table / data**
- **Empty / loading / error states**

## 7. Icons

- **Library or custom:** [choice] — why (see `references/icons.md`)
- **Grid / stroke / corners / fill:** [values matched to the type]

## 8. Motion

- **Personality:** [from `references/motion.md`]
- **Tokens:** `duration-fast` / `duration-base` / `duration-slow`, `ease-standard` / `ease-enter` / `ease-exit`
- **Moves:** [what may move] · **Never moves:** [what may not]
- **Reduced motion:** [fallback]

## 8b. Imagery

- **Photography art direction:** subject · light · color grade · crop & aspect ratios · texture · people · never-show list
- **Illustration system:** construction · line (shared with icons) · colors · figures · space · detail
- **Generation prompt skeleton:** the fixed prompt (from `references/imagery.md` § 4) with this style's values filled in
- **Sources & credits:** client assets needed / generated / stock with licences

## 9. Signature moves

The 3–5 details that make this style recognisable. Without them it collapses into generic UI.

## 10. Slop tells for this style

How this particular style would look if done cheaply. Check every output against this list.

## 11. Implementation

### Figma variables
```
Collection: [style-slug]/primitives   modes: —
Collection: [style-slug]/semantic     modes: light, dark
  color/bg, color/surface, color/ink, …
  space/1…n, radius/…, type/…
```

### CSS custom properties
```css
:root { }
@media (prefers-color-scheme: dark) { :root { } }
```

### Tailwind v4
```css
@theme { }
```

## 12. Specimen

Link or path to the specimen page and its critique notes.
