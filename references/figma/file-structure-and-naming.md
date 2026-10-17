# Figma file structure and naming

Use when creating, reorganising or publishing any Figma file that carries the person's style: a library, a product file, or a single feature file. Load `figma:figma-use` before every `use_figma` write; inspect existing conventions first (`get_metadata`, or `inspectFileStructure.js` from `figma:figma-generate-library`) and **match them** if the file already has a consistent scheme.

Related: variant and property naming → [components.md](components.md) · variable and style naming, code syntax → [variables-and-tokens.md](variables-and-tokens.md) · resizing behaviour → [auto-layout.md](auto-layout.md) · frames, pixels, export → [canvas-craft.md](canvas-craft.md) · what the system contains → [design-system.md](design-system.md) · hand-off → [handoff.md](handoff.md).

## 1. Library files vs product files

| File | Holds | Publishes? | Example name |
|---|---|---|---|
| Foundations library | Variables, text/effect styles, layout grids | Yes | `Atelier · Foundations` |
| Components library | Components built only from Foundations | Yes | `Atelier · Components` |
| Icons library (optional) | Icon components, one size set | Yes | `Atelier · Icons` |
| Product / feature file | Flows, screens, explorations for one product area | No | `Billing · Invoices` |
| Sandbox | Experiments, contribution drafts | Never | `Sandbox · [name]` |

- **Start with one library file** for a personal style and one product; split Foundations from Components when a second product, brand or platform consumes it, consumers can then take the tokens without the components. Primer splits *Primer Primitives* (color, type, spacing) from *Primer Web* (components); Carbon separates its core kit from IBM Design Language libraries (type, color, icons, pictograms).
- **Never build screens inside a library file**: every publish would then carry noise, and library analytics would count your own test instances.
- **Projects cannot hold subfolders** (Figma help: files and projects), keep one project per product plus one `Design system` project, and let file names carry the rest.
- **No version numbers or "final" in file names**: they go stale; versions live in publish notes and named versions (§ 7).
- **Set a thumbnail** (right-click the Cover frame → *Set as thumbnail*), teammates find files by sight in the file browser.

## 2. Page structure

### Library file

```
Cover                    name, one-line essence, owner, current version, status legend
Getting started          how to enable the library, principles (style laws), who to ask
Changelog                one frame per release, newest first (§ 7)
---
Color · Typography · Spacing & radius · Elevation · Motion · Grid · Icons
---
Button
Input
Select
…                        one page per component family, alphabetical
---
Patterns                 forms, empty states, list/detail, filtering
Templates                page-level layouts per breakpoint
---
_Utilities               doc components, specimen helpers (hidden from publishing)
Deprecated               main components on their way out (§ 8)
```

- **Foundations before components, utilities and deprecated last**: the page list reads as a dependency order.
- **One page per component family** (Button and IconButton may share), a page is a link target, keeps Dev Mode navigation short and loads faster.
- **Separators are pages named `---`**: the convention in Figma's Simple Design System, Material 3 and Polaris files (catalogued in `figma:figma-generate-library` → `references/naming-conventions.md`).

### Product file

```
Cover
Brief & decisions        problem, links, decisions log (or an embedded Figma spec, see handoff.md)
---
Onboarding               one page per flow or feature area
Checkout
Settings
---
Explorations             divergent ideas, never marked ready
Archive                  superseded work kept for history
```

- **Pages say *what*; dev statuses say *readiness*.** Figma's own handoff guide suggests separate WIP / feedback / ready pages, but the *Ready for dev* status on sections is what Dev Mode filters and notifies on, prefer it, and keep readiness out of page names (see [handoff.md](handoff.md) § 1).
- **Archive, don't delete**: version history covers mistakes, but an Archive page keeps rejected directions visible to the next designer.

## 3. Sections and frames

| Rule | Why |
|---|---|
| Wrap each flow or sub-flow in a **section** named like the flow: `Checkout / Payment` | Sections are the unit you mark *Ready for dev*, link to, and use as prototype destinations |
| Flows run **left → right**, states of one screen stack **top → bottom** | Reviewers and developers scan every file the same way |
| One breakpoint per row or per section, labelled with its width | Responsive behaviour is compared at a glance |
| Name frames `Screen · State · Width`: `Payment · Error · 375` | Sorts in the layers panel and reads in Dev Mode; no `/`, which creates folders on export and groups if the frame becomes a component |
| Use top-level frames for screens, never groups | Groups have no layout intent and cannot be marked ready or compared in Dev Mode |
| Keep the canvas lean: delete leftovers instead of hiding them | Hidden layers still appear in the layers panel and invite questions during inspection |

Sections sit at the top level, can contain other sections, and cannot live inside frames or groups (Figma help: sections).

## 4. Layer naming

Developers, Dev Mode and the Figma MCP server all read layer names; Figma's MCP guidance explicitly asks to replace `Frame1268` / `Group5` with intent names because default names produce unstructured code.

| Do | Don't | Why |
|---|---|---|
| Name every surviving layer by role: `Header`, `PriceRow`, `PrimaryAction` | `Frame 1268`, `Group 5`, `Rectangle 12` | Role names become component and class names in generated code |
| Use the names engineers use: `CardContainer`, `ProductImage`, `Toolbar` | Visual names: `Blue box`, `Big text` | Shared vocabulary removes a translation step |
| Name text layers by the data they hold: `title`, `price`, `helperText` | The literal copy: `Pay €49 now` | Copy changes; overrides survive instance swaps only when layer names match (Primer) |
| Name action layers by the action: `Submit`, `Dismiss` | `Button copy 3` | Tells devs and screen-reader labels what it does |
| Keep one casing per file (PascalCase containers, camelCase text) | Mixed `card_header`, `Card Header`, `cardHeader` | Searchable and diff-friendly |
| Name exportable assets in the code's asset convention: `icon-arrow-right` | `Vector`, `Union` | The layer name becomes the exported file name |

## 5. Component and style naming (summary)

Full rules live in [components.md](components.md) and [variables-and-tokens.md](variables-and-tokens.md); the file-level essentials:

- **Component name = code component name, PascalCase**: `Button`, `ActionList`, `DatePicker`, Primer's rule; exact code identifiers go into Code Connect and variable code syntax, not into layer clutter.
- **Slash = hierarchy in the Assets panel**: `Icon/Arrow/Right`, `Avatar/Group`. Two or three levels; deeper paths hide assets.
- **Internal parts: `_` prefix + Hide when publishing**: `_Button/IconSlot`. The `_` signals "don't use directly"; the explicit *Hide when publishing* makes it reliable, Figma's help confirms the `.` prefix for components and `_`/`.` for whole variable collections; a 2025 forum report says `_` alone no longer hides components (verify).
- **Doc-only components: `.` prefix**: `.Doc/Header`, `.Doc/DoDont`, kept out of the library.
- **Styles and variables**: `Heading/1`, `Body/Medium`, `color/bg/surface`, `space/4`, names for designers, code syntax for developers.

## 6. Status conventions

| Where | Convention | Why |
|---|---|---|
| Sections / frames | Dev status: *Ready for dev* → *Changed* (automatic) → *Completed* | The only status Dev Mode filters and notifies on |
| Component description, first line | `Stable` · `Beta` · `Deprecated, use X, removal v3.0` | Shown in Dev Mode Inspect, Assets panel and search |
| Library page names (large multi-team systems only) | Colour-circle prefix for design status, `[beta]` / `[future]` suffix for code status, the pattern of Figma's own UI3 library | Lifecycle at a glance; overkill for a personal system |
| Product page names (optional) | A small emoji legend (Figma's handoff guide shows 🏗️ 💭 🚢), defined on the Cover | Visual aid only; never the sole carrier of readiness |

## 7. Versioning, branching, changelog

**Semantic versions in every publish note**: Figma has no version field, but it asks for a description on every publish and shows it when consumers accept updates and in version history.

| Bump | When | Examples |
|---|---|---|
| MAJOR | Consumers' instances or code mappings break | Component, variant, property, style or variable removed or renamed; layers with children added/removed so overrides reset (Primer warns about this) |
| MINOR | Additive and backwards-compatible | New component, variant, property, token, mode |
| PATCH | Visual fix, same API | Corrected padding, icon redraw, description fix |

Publish note format, mirrored as a frame on the Changelog page (publish descriptions are hard to find later):

```
v2.4.0 to 2026-10-16
Added: Select (size sm/md), color/feedback/info
Changed: Button focus ring now uses color/focus (was accent)
Deprecated: Dropdown, use Select; removal in v3.0.0
Migration: swap Dropdown instances for Select; props map 1:1 except `placement`
```

- **Save a named version with the same number** (*Save to version history*), autosave checkpoints arrive every 30 minutes and are unnamed, so releases get lost among them.
- **Branch anything that changes an API or tokens** (Organization and Enterprise plans; Full seat). Name branches `TICKET-123: Select component` or `@user/select-component`, request review from the library owner, merge, then publish, **you can only publish from the main file**.
- **Skip branching** for a ground-up rebuild (new file), side-by-side concepts (pages), or a tiny urgent fix (edit main), Figma's branching guidance.
- **Undoing a merge means restoring a version**: merged branches are archived; name a version before merging large branches.
- **No branching on your plan?** Work in a `Sandbox` duplicate or a WIP page and untick unready assets in the publish modal.

## 8. Deprecation path

Figma has no native "deprecated" flag for components (none found as of Oct 2026; verify). Run deprecation as a two-release process:

1. **Ship the replacement** (MINOR) and write the migration in the publish note.
2. **Mark the old asset while still published**: description first line `Deprecated in v2.4, use Select. Removal v3.0.`, rename to `Deprecated/Dropdown`, move the main component to the *Deprecated* page, publish. Renames of already-hidden components may not propagate (forum reports), so rename *before* hiding.
3. **Watch usage** in library analytics (Organization/Enterprise) or by sampling product files; give at least one release cycle.
4. **Remove** (MAJOR): *Hide when publishing* or delete, publish. Existing instances keep rendering but stop receiving updates.

## 9. Library publishing hygiene

- **Publish from a clean main file only**, after the QA checklist below, every publish shows an update badge to every consumer.
- **Read the publish modal line by line**: it lists added, modified and removed assets; untick anything accidental (one stray nudge = a modified component for everyone).
- **Batch releases** (weekly or per milestone), not every tweak, consumers stop reading notes that arrive daily.
- **Description and documentation link on every published component, style and variable**: they surface in Dev Mode Inspect, the Assets panel and search; a Storybook/GitHub link gets a branded button.
- **Hide internal parts, doc components and specimen helpers** before publishing.
- **Share the library file with developers** (at least *can view*), otherwise "go to main component" leads to an access error (Figma's handoff guide).

## QA checklist

- [ ] File type is clear (library / product / sandbox); no screens in library files
- [ ] Page order: Cover → Getting started → Changelog → Foundations → Components → Patterns → Templates → utilities/deprecated; separators `---`
- [ ] Thumbnail set; Cover shows owner, version, status legend
- [ ] Every flow in a named section; frames named `Screen · State · Width`
- [ ] Zero default layer names (`Frame`, `Group`, `Rectangle`, `Vector`) in components and ready-for-dev frames
- [ ] Component names match code; internal parts `_`-prefixed and hidden; doc parts `.`-prefixed
- [ ] Publish note has a semver number, Added/Changed/Deprecated/Removed, and migration steps; Changelog frame and named version match it
- [ ] Deprecated assets carry description, `Deprecated/` prefix and a removal version
- [ ] Publish modal reviewed asset by asset; nothing accidental ticked
- [ ] Developers have view access to every library the file uses

## Sources (checked 2026-10)

help.figma.com: Guide to files and projects (1500005554982) · Organize your canvas with sections (9771500257687) · Publish a library (360025508373) · Hide styles, components and variables when publishing (360039238193) · Guide to branching (360063144053) · Version history (360038006754) · Add descriptions to styles, components and variables (7938814091287). figma.com: Guide to developer handoff (best-practices) · Best practices for branching (scaling-design). developers.figma.com: MCP server, Structure your Figma file. primer.style: Contributing to Figma. carbondesignsystem.com: Figma kits.
