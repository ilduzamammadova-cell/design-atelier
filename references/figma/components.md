# Components

Load before creating, changing or reviewing any component, variant set or instance in Figma. This file is the professional *what and why*. The Plugin API *how* (`combineAsVariants`, grid-laying variants, `addComponentProperty`, `componentPropertyReferences`, `preferredValues`) lives in the `figma:figma-generate-library` skill — `references/component-creation.md` and `references/naming-conventions.md` — and in `figma:figma-use` → `references/component-patterns.md`. Map finished components to code with `figma:figma-code-connect`.

Related: [auto-layout.md](auto-layout.md) · [variables-and-tokens.md](variables-and-tokens.md) · state wiring in [prototyping.md](prototyping.md) § 9 · publishing and component deprecation in [file-structure-and-naming.md](file-structure-and-naming.md).

Checked against help.figma.com, the Figma plugin changelog and the Plugin API typings (October 2026). "(verify)" marks anything not confirmed in a primary source.

## 1. What deserves to be a component

| Make it a component when… | Keep it a frame of instances when… |
|---|---|
| It appears twice, or will | It is a one-off composition (a landing-page hero) |
| It has interactive states | It is a page section whose content always differs |
| A code component of that name exists or will | It only arranges other components (a screen) |
| It encodes a style law that must not drift (a signature border, a seam) | Making it reusable would need 10+ properties to cover its uses |

Brad Frost's vocabulary sorts the rest: **components** live in the core library (Button, Field, Card); **recipes** are product-specific compositions of them (ProductCard, AddressForm) and live in the product file; **snowflakes** are one-offs and stay frames. Promote a snowflake only when it repeats.

## 2. Structure: build from the inside out

| Tier | Contents | Rule |
|---|---|---|
| 0 · parts | Icons, spinner, focus ring, `_Button/Base`, `_Tabs/Tab` | Private unless designers place them directly |
| 1 · controls | Button, IconButton, Checkbox, Radio, Switch, Input, Select, Avatar, Badge | One component set each |
| 2 · composites | Field (label + input + help), ListItem, Card, Menu, Tabs, Toast | Built from tier 0–1 instances only |
| 3 · patterns | Dialog, Navigation, Table, Empty/Loading/Error states | Slots for the parts that vary |

Never build a parent before its children exist; never redraw a child inside a parent — nest the instance, so one fix propagates everywhere. Every component is auto layout (see `auto-layout.md`) with every fill, stroke, gap, padding and radius bound to a variable (see `variables-and-tokens.md`).

## 3. Naming

| Thing | Convention | Example |
|---|---|---|
| Published component / set | Same name as the code component, PascalCase | `Button`, `TextField`, `ListItem` |
| Internal part (base, sub-part) | `_` prefix **plus** right-click → Hide when publishing. `_` tells designers "don't place this"; the explicit hide makes exclusion reliable — a 2025 forum report says `_` alone no longer hides components (verify) | `_Button/Base`, `_Parts/FocusRing` |
| Documentation helper | `.` prefix — the prefix Figma's help documents for keeping a component out of the library | `.Doc/SpecLabel` |
| Layers inside | lowercase kebab, named after the code part | `container`, `icon-leading`, `label`, `icon-trailing`, `focus-ring` |
| Variant layer | Generated `Property=Value, Property=Value` — never rename by hand | `Type=Primary, Size=Md, State=Hover` |

Private parts still work nested inside published components: edit `_Button/Base`, republish, and every published parent that contains it updates. Layer names are read by Dev Mode, Code Connect and `get_design_context`; `Frame 12` is a defect.

## 4. Pick the right property for each difference

Figma has five property types: **Variant, Boolean, Text, Instance swap, Slot** (slots GA June 2026, all plans). Use one property per named difference — never one "Style" property that changes three things.

| The difference is… | Use | Why |
|---|---|---|
| A visual or structural alternative a code prop selects (type, size, tone) | **Variant** | Each combination is drawn; maps 1:1 to the prop |
| An interaction state (hover, pressed, focus, disabled) | **Variant** `State` | Figma has no pseudo-classes; tell Code Connect these are CSS states, not props |
| Show / hide one layer | **Boolean** | Booleans only control layer visibility |
| Editable copy | **Text** | Label stays editable without diving into layers |
| Exactly one swappable nested component (icon, avatar) | **Instance swap** + preferred instances | Fixed position and size; curated choices |
| A region holding variable content (dialog body, card content, menu items) | **Slot** | Designers add, reorder and resize without detaching |
| A nested component's own options | **Expose nested instances** | Reuses the child's API instead of re-declaring it |
| Density or size that follows context (compact tables) | Variable **modes** on number variables | Only when code also switches it by context, not by prop |
| Light/dark, brand, locale | Variable **modes** — never variants | A `Theme=Dark` variant doubles every set and drifts |

## 5. Variant matrix conventions

- **Property names:** Title Case nouns, named after the code prop: `Type` (or `Variant` if code says `variant`), `Size`, `State`, `Tone`. One vocabulary across the whole library.
- **Values:** one style library-wide — Title Case words, or the code's literal values. Never `Variant 7`, never an empty value.
- **Order in the panel:** most impactful first — `Type` → `Size` → `State` → toggles.
- **Two-state variants:** values `true` / `false` (lowercase). Figma shows them as a toggle and boolean variables can bind to them; `Yes/No` reportedly breaks boolean-variable binding.
- Every variant carries every property. Figma does not need impossible combinations — omit them only when code forbids them too.
- Lay the set out as a labelled grid (rows = Type × Size, columns = State) so a reviewer reads it like a spec sheet.

| Property | Default value set |
|---|---|
| `Type` | `Primary`, `Secondary`, `Tertiary`, `Danger` |
| `Size` | `Sm`, `Md`, `Lg` |
| `State` | `Default`, `Hover`, `Pressed`, `Focus`, `Disabled` (+ `Loading`, `Error` where they apply) |
| `Tone` | `Neutral`, `Accent`, `Success`, `Warning`, `Danger` |
| `Selected`, `Checked`, `Open` | `true`, `false` |

## 6. States every interactive component needs

| Component | Required states | Notes |
|---|---|---|
| Button, IconButton | Default, Hover, Pressed, Focus, Disabled, Loading | Loading keeps the width: hide label, centre an absolute spinner |
| Input, Select, Textarea | Default, Hover, Focus, Filled, Disabled, Read-only, Error | Error = border + icon + message text, never colour alone |
| Checkbox, Radio, Switch | `Checked` × (Default, Hover, Pressed, Focus, Disabled); Checkbox also `Indeterminate` | Label is part of the hit area |
| Tab, Nav item, Segment | `Selected` × (Default, Hover, Pressed, Focus, Disabled) | Selected is persistent, Pressed is transient — never merge them |
| ListItem, Menu item | Default, Hover, Pressed, Focus, Selected, Disabled | Destructive items use the danger tone, not a new layout |
| Link | Default, Hover, Focus, Visited (if the product shows it) | Underline or equivalent, not colour only |

- **Focus** is the one most often missing. Draw it as an outside stroke or an absolute `focus-ring` layer so it never shifts layout; ring ≥ 3:1 against adjacent colours (WCAG 1.4.11).
- **Disabled** uses `opacity/disabled` or dedicated disabled colours from tokens — not ad-hoc greys.
- Hover does not exist on touch; still draw it for pointer platforms, and never hide information behind it.
- Wire states for prototypes on the set: While hovering → `State=Hover`, While pressing → `State=Pressed`, Smart Animate with the motion tokens' duration and easing (`../motion.md`).

## 7. Avoiding variant explosion

Count the set: the product of value counts. Above ~30 variants the set is slow to use and hard to maintain (the `figma-generate-library` cap). Reduce in this order:

1. Icons → **instance swap**. Never `Icon=ChevronRight` variants.
2. Labels → **text** properties; optional parts → **booleans**.
3. Variable content → **slots**.
4. Theme, brand, density, locale → variable **modes**.
5. Sub-elements with their own state machine (tab, segment, table cell) → a private building-block set (`_Tabs/Tab`) nested in a lean parent.
6. Split the set only where code has separate components (`IconButton` vs `Button`), never to dodge a count.

A **base component** (`_Button/Base`, one master drawing that every variant instances and overrides with tokens) does not reduce the count, but it makes structural edits happen once. Use it for sets above ~12 variants; skip it for small sets where the extra nesting costs more than it saves.

## 8. Nested instances, instance swap and slots

| Need | Tool | Set up |
|---|---|---|
| Edit a child's props from the parent panel | Expose nested instances | Parent → Properties `+` → Nested instances. Exposes all of the child's props, so keep children lean |
| One swappable item in a fixed place | Instance swap | Default = a real component; add **preferred instances** (components or whole sets) so the picker shows the right family first |
| N items of a known kind (actions, menu items, chips) | Slot + preferred instances + min/max layers | Turn on "Only allow preferred instances" when the system must stay strict |
| Arbitrary content region | Slot, unrestricted | Name it for its role: `content`, `actions`, `media` |

Slot facts (help.figma.com, Plugin API June 2026):
- Create by right-click → Convert to slot (⌘/Ctrl + ⇧ + S) on a nested frame, Wrap in new slot on other layers, or Create property → Slot. Apply across variants with multi-edit.
- Settings: name, description, documentation, preferred instances, only-allow-preferred, min/max layers (guidance, not a hard block), display empty slots by default, fill items on the counter axis.
- The slot's flow, position and constraints come from the main component; instances cannot change them. Design the slot's auto layout carefully.
- A slot cannot be the component's top-level layer. Moving a layer that carries a component property into a slot removes that property. Deleting a slot property resets every instance's slot content — do it on a branch.
- Code Connect supports slot content; Figma MCP support for slots was "coming soon" in the help article — check what `get_design_context` returns before relying on it (verify).
- Older libraries that faked slots with placeholder "Slot" components should migrate (help: "Migrate a library to using slots").

"Simplified instances" was deprecated from 23 March 2026; instances now show all properties and layers. Design a clean property panel instead of hiding layers.

## 9. Descriptions and documentation

Set the description on the component set (or the single component) — never on variants or instances. Three short sentences:

> Primary action button. Use for the single most important action in a view; use Secondary for the rest. Enter/Space activates; Loading keeps width and blocks repeat clicks.

- Add a documentation link (Storybook, spec page, the style's Laws & lineage page) on every published component.
- Write slot descriptions: what belongs there and how many.
- Property names must read well to a designer *and* map to code; if they diverge, Code Connect records the mapping.

## 10. Detaching

- Never detach a library instance in product work: it cuts off every future fix, and Check designs (Organization/Enterprise) flags detached instances (verify).
- A wish to detach means the component lacks a property, variant or slot. Add it to the component, or propose it.
- Allowed only in labelled exploration files, or to start a snowflake — then rename it so nobody mistakes it for the component.
- Override through the API the component offers (text, booleans, swaps, slot content, variable modes). Manual fill/stroke overrides on instances block future updates of that property; do not use them.

## 11. QA checklist

- [ ] Each component maps to one code component (same name) or is a documented recipe; one-offs stay frames.
- [ ] Children are nested instances, never redrawn; parts carry `_` + Hide when publishing, doc helpers `.`, both verified absent from the publish modal.
- [ ] One property per difference; icons via instance swap; variable content via slots; theme/density via modes.
- [ ] Variant names follow `Property=Value`, shared vocabulary, `true/false` toggles; set ≤ ~30 variants or justified.
- [ ] All required states present, including Focus, Disabled, Loading, Error; state changes do not shift layout.
- [ ] Every visual value bound to a variable; text uses text styles; no raw hex or px.
- [ ] Preferred instances set on every instance swap and restricted slot.
- [ ] Description and documentation link on every published set; layers named semantically.
- [ ] No detached instances in product files; no manual fill overrides on instances.
- [ ] Component set laid out as a labelled grid; `get_screenshot` shows no clipped labels at any size.
