# Building a style in Figma

Use when the person works in Figma, shares a figma.com link, or asks for the design "in Figma". Work like a senior product designer: every value bound to a variable, every layout in auto layout, every reusable part a component, every layer named for what it is, and a file a developer can build from without asking questions.

This file is the route. The practice lives in `references/figma/`:

| File | Read when |
|---|---|
| `figma/file-structure-and-naming.md` | Starting or reorganising any file; naming pages, sections, frames, layers |
| `figma/variables-and-tokens.md` | Creating the style's tokens: collections, modes, aliasing, scoping, code syntax, DTCG export |
| `figma/auto-layout.md` | Building any frame or component (hug/fill/fixed, min/max, grid auto layout, spacing) |
| `figma/components.md` | Making components: variants, properties, slots, nested instances, states |
| `figma/canvas-craft.md` | Frames, layout guides, pixel precision, icons and vectors, text, images, effects, color profile, export |
| `figma/prototyping.md` | Interactions, Smart Animate, motion tokens, variables and conditions in prototypes |
| `figma/design-system.md` | Turning the style into a library: foundations, documentation, governance, code sync |
| `figma/handoff.md` | Preparing frames for developers: states, specs, annotations, Dev Mode, Code Connect |
| `figma/qa-checklist.md` | Before showing or handing off anything |
| `references/dimensions.md` | Frame sizes, safe areas, targets, platform type sizes, breakpoints |

## Before any write

- The Figma MCP server provides the tools (`use_figma`, `get_design_context`, `get_metadata`, `get_screenshot`, `get_variable_defs`, `search_design_system`, `create_new_file`, Code Connect tools).
- **Load the `figma:figma-use` skill before any `use_figma` call** — it carries the Plugin API rules. Also: `figma:figma-generate-library` for building variables and components as a library, `figma:figma-generate-design` for full screens, `figma:figma-create-new-file` before `create_new_file`, `figma:figma-code-connect` for mapping components to code.
- Writing into someone's Figma account is outward-facing: confirm which file (or that a new file is wanted) before the first write.
- Some settings can't be changed through the Plugin API (for example the file's color profile and some prototype overlay settings — see `figma/canvas-craft.md`). Tell the person exactly what to set by hand.
- If the Figma tools aren't connected, say so and offer the web route (`references/web.md`) or a spec-only deliverable.

## Read first

If the person shares an existing file:
1. `get_metadata` and `get_screenshot` to see structure and state.
2. `get_variable_defs` and `search_design_system` to find existing variables, styles and components.
3. If a design system exists, **adopt it**: map the style onto existing variables, add only what's missing, follow its naming. Never create a second, parallel visual language in one file.

## Build order

Each step depends on the previous one.

1. **File structure** — pages and sections (`figma/file-structure-and-naming.md`), plus a Cover and a *Laws & lineage* page that explains why the style looks the way it does.
2. **Variables** — primitives, then semantic tokens with Light/Dark modes (and density or brand modes if needed), scoped and given code syntax (`figma/variables-and-tokens.md`). Values come from the style spec § 11.
3. **Text styles** for every step of the type scale; **effect styles** only if the style uses depth.
4. **Layout guides** per breakpoint frame, sized from `references/dimensions.md`.
5. **Icons** — the style's monochrome set as components with size variants (`references/icons.md`, `figma/canvas-craft.md`).
6. **Components** — atoms to patterns, every state, auto layout throughout, every fill/stroke/gap/padding/radius bound to a variable (`figma/components.md`, `figma/auto-layout.md`).
7. **Imagery** — real photographs and illustrations placed with the style's art direction; spot illustrations as components (`references/imagery.md`).
8. **Specimen** — one page built only from the components and variables (`method/blend.md` § 7).
9. **Screens** at the stated frame sizes, checked at the smallest and largest targets.
10. **Prototype** key flows with motion matched to the motion tokens (`figma/prototyping.md`).
11. **Hand-off** — mark ready for dev, annotate, link code (`figma/handoff.md`).

Take a `get_screenshot` after each major step and compare it with the style laws; fix before moving on.

## Done means

Run `figma/qa-checklist.md`, then the pre-delivery check in `references/anti-slop.md`. Report to the person in plain language: what was built, where it is in the file, what they must set by hand, and what is still missing (assets, decisions).
