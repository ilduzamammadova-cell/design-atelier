# Design system file

Use when a named style (`templates/style-spec.md`) becomes a reusable Figma library, or when the person asks for "a design system", "a UI kit" or "a library" in their style. This file says **what a professional system contains and how it is run**. How to build it with the Plugin API, in what order, with which helper scripts: load `figma:figma-use` + `figma:figma-generate-library` together. File and page layout: [file-structure-and-naming.md](file-structure-and-naming.md). Variables, modes, scopes, code syntax, token pipeline: [variables-and-tokens.md](variables-and-tokens.md). Component properties, variants, slots: [components.md](components.md). Layout behaviour: [auto-layout.md](auto-layout.md).

## 1. Scope before building

| Situation | Build | Skip for now |
|---|---|---|
| Personal style, one product | One library file: foundations, 8 to 12 core components, specimen, Getting started with the laws | Separate libraries, analytics, formal contribution flow |
| Team product, several designers | Foundations + Components libraries, documentation per component, changelog, Code Connect | Multi-brand theming |
| Several brands or platforms | Above + theme modes; extended collections for brand overrides (Enterprise plan) | none |

Agree the v1 inventory with the person before the first write, `figma:figma-generate-library` treats an unagreed full library as scope creep, and so should you.

## 2. Mapping the style spec onto the system

Every section of the person's style spec has one home in Figma. Nothing in the spec is left only in Markdown, and nothing in Figma lacks a line in the spec.

| Style spec (`templates/style-spec.md`) | Figma artifact | Page |
|---|---|---|
| Essence sentence, owner, version | Cover frame | Cover |
| § 1 Laws, § 9 Signature moves, § 10 Slop tells | Principles frames with do/don't pairs; also a library **guidelines file** for the Figma agent (open beta, see § 8) | Getting started |
| § 2 Lineage | "Where this style comes from" frame: gene, source, transformation | Getting started |
| § 4 Color | Primitive + semantic variables, Light/Dark modes | Color |
| § 4 Typography | Text styles (bound to variables where the file uses typography variables) | Typography |
| § 4 Shape, depth, space | `space/*`, `radius/*`, `border/*` variables; effect styles or a documented "no shadows" rule | Spacing & radius · Elevation |
| § 4 Grid | Layout grid styles per breakpoint from [../dimensions.md](../dimensions.md) | Grid |
| § 5 Layout grammar | Patterns and templates that obey it | Patterns · Templates |
| § 6 Components | Components with every state | One page each |
| § 7 Icons | Icon components on the style's grid and stroke ([../icons.md](../icons.md)) | Icons |
| § 8 Motion | Duration/easing tokens; animation styles if the team uses Figma Motion (open beta) | Motion |
| § 8b Imagery | Art-direction frames, crop ratios, do/don't images | Imagery (optional) |
| § 11 Implementation | Code syntax on every variable; token JSON export | (in the variables) |
| § 12 Specimen | Specimen page built only from library instances | Specimen |

## 3. Foundations: what each page must show

Document with **instances and bound swatches, never pasted values**, documentation then updates itself when a token changes.

| Foundation | Figma asset | The page shows | Why |
|---|---|---|---|
| Color | Primitives (hidden from publishing) + semantic aliases with modes | Semantic swatches bound to variables, each with name, code syntax, usage, contrast pair results in both modes | Designers pick roles, not hues; contrast is proven, not assumed |
| Typography | Text styles `Display/*`, `Heading/*`, `Body/*`, `Label/*`, `Code/*` | One specimen line per style: size / line-height / tracking / weight, usage, the longest realistic string | Shows hierarchy and wrap behaviour, not just a font name |
| Space | Number variables `space/1…n` | Scale bars with token name and value; where each step is used | Ends "8 or 12?" debates |
| Radius & border | `radius/*`, `border/width/*` | Shapes per token, which components use which | Keeps shape language consistent |
| Elevation | Effect styles or none | Each level on the real surface colour in both modes, with use cases | Shadows that fail in dark mode are caught here |
| Motion | `duration/*`, easing tokens ([../motion.md](../motion.md)) | Live demo frames or prototype, reduced-motion rule | Motion is part of the style, not a dev afterthought |
| Iconography | Icon components, sizes 16/20/24 | Grid, keylines, stroke, naming, the full set | Contributors draw new icons that fit |
| Grid & breakpoints | Layout grid styles | Columns, gutters, margins per breakpoint | Templates and product screens share one skeleton |

## 4. Component documentation page

Every component page uses the same frames, top to bottom. Main components live on the page; documentation uses **instances** of them.

| Frame | Contents | Why |
|---|---|---|
| Header | Name, status (`Stable`/`Beta`/`Deprecated`), version added, one-line purpose, links to code and Storybook | The first five seconds answer "can I use this?" |
| Anatomy | Numbered parts mapped to named layers and sub-components | Shared vocabulary for design reviews and code |
| Properties | Table of variant/boolean/text/instance-swap/slot properties and their code prop names | Proves Figma API = code API |
| States | Default, hover, pressed, focus, disabled, loading, error, selected, as instances | No state is invented during build |
| Usage | Do/don't pairs side by side, one reason each | Rules stick when the wrong version is visible |
| Content | Label length, truncation, wrapping, pluralisation, long-text example, RTL if supported | Copy breaks components more often than pixels do |
| Accessibility | Role, accessible name source, keyboard map, focus order, contrast pairs, min target size | Accessibility is specified once, inherited everywhere |
| Specs | Spacing, sizing and tokens per part (the EightShapes *Specs* plugin can generate anatomy and layout frames) | Developers measure tokens, not pixels |
| Code | Code Connect status, code component name and path | Shows how far design and code are in sync |

Also put a short version on the component itself: **description** (first line = purpose and status) and a **documentation link**, they appear in Dev Mode Inspect, the Assets panel and search.

## 5. Patterns and templates

- **Patterns** solve a recurring problem with several components: form with validation, empty → loading → populated, list/detail, filter and sort, destructive confirmation. Document the rule ("errors appear under the field after blur, summary on submit"), not only the picture, the rule is what product designers reuse.
- **Templates** are page skeletons per breakpoint (app shell, settings, dashboard, article) built only from instances, with `[bracketed]` content. Publish them as components so product files start from them instead of copying frames.
- **Specimen** stays separate: it proves the style ([../../method/blend.md](../../method/blend.md) § 7); templates prove the system.

## 6. Governance

Even a one-person system needs a written process, it is how a style survives its second contributor.

| Change | Path | Version bump |
|---|---|---|
| Bug or visual fix | Issue → branch → owner review → merge → publish | PATCH |
| New variant, property or token | Proposal with use cases from ≥2 screens → branch → review → publish | MINOR |
| New component or pattern | Proposal → design review with engineering → build in branch → documentation page → Code Connect → publish | MINOR |
| Removal, rename, restructure | Deprecation path ([file-structure-and-naming.md](file-structure-and-naming.md) § 8) | MAJOR |

- **One owner (DRI) per library** who reviews branches and publishes, Primer runs its Figma library exactly like a protected `main`: contributors branch, the DRI reviews, a maintainer merges and publishes.
- **Contribution review checklist**: built from foundations only (no raw values), every state present, properties match code names, layers named, description and link set, accessible, light and dark checked, documentation page updated.
- **A style law outranks a contribution.** If a request breaks a law, change the law deliberately (journal entry, [../../method/evolve.md](../../method/evolve.md)) or decline, never let it drift in.

## 7. Adoption metrics

Library analytics (Organization and Enterprise plans; file menu → *Library analytics*, or right-click the file in the browser):

| Signal | Reading | Action |
|---|---|---|
| Insertions over 30/60/90/365 days | Which components carry the product | Invest documentation and Code Connect there first |
| Detaches (instances, styles, variables) | The asset doesn't fit real needs | Interview the detachers; add a property or slot, or a pattern |
| Teams using / files using | Reach | Low reach → onboarding problem, not a design problem |
| Zero insertions for 90+ days | Dead weight | Candidate for deprecation |

Caveats: data refreshes daily and keeps one year; style and variable tracking started 10 Oct 2024; nested components don't count as insertions; other people's drafts aren't tracked; CSV export appears only when more than five teams use the library; the Library Analytics REST API is Enterprise-only. On Professional, sample product files by hand each quarter.

## 8. Keeping Figma and code in sync

| Layer | Mechanism | Rule |
|---|---|---|
| Tokens | Variables with code syntax; native DTCG JSON *Export modes* / *Import mode* in the Variables modal | Decide one direction of truth (code → Figma or Figma → code) and never edit both; pipeline in [variables-and-tokens.md](variables-and-tokens.md) |
| Components | **Code Connect** | Every published component that exists in code gets a mapping; Dev Mode and the MCP server then return real component code instead of generated markup |
| Docs | Description + documentation link + Dev resources (Storybook, GitHub) | Links propagate from components to all instances |
| Drift | Periodic reconciliation | Run `figma:figma-generate-library` in *reconciliation* scope: diff, update in place, keep IDs |

Code Connect choice (Professional, Organization, Enterprise; Full or Dev seat; on Professional only one library and one framework are active at a time):

| | Code Connect UI | Code Connect CLI |
|---|---|---|
| Runs | In Figma (Dev Mode → library menu → *Connect components to code*); GitHub optional | In the repo; publishes from the terminal |
| Maps | Component → code path and name; one design component to several frameworks | Properties → props, dynamic code examples (React, Web Components, SwiftUI, Compose parsers) |
| Best for | Designers starting the mapping | Engineering teams wanting exact snippets |

One connection type per component; both kinds coexist in one system and both feed the MCP server. Write templates with `figma:figma-code-connect`.

Newer Figma features worth adopting when available (status as of Oct 2026):

- **Guidelines files for libraries** (open beta; Professional+): up to 200 KB of `.md`/`.txt`/`.json` rules the Figma agent reads whenever the library is enabled (file menu → *Library → Manage guidelines*). Export the style laws, signature moves and slop tells here, it keeps AI-generated screens inside the style.
- **Slots** (open beta per help center): flexible content areas in instances; reduce variant explosion and detaches. Details in [components.md](components.md).
- **Extended collections** (Enterprise): brand themes that inherit the parent system and override selected variables.
- **Check designs** linter that flags raw values before hand-off (announced Schema 2025 as early access; verify availability).
- **Centralized design systems** with system map and gap check (announced Oct 2026 as a preview; verify).

## QA checklist

- [ ] Scope and v1 inventory agreed; nothing outside it built
- [ ] Every style-spec section has a Figma home (§ 2 table); laws on Getting started and in a guidelines file if available
- [ ] Foundations documented with bound swatches and instances, no pasted hex or px
- [ ] Contrast pairs pass WCAG 2.2 AA in Light and Dark ([../principles.md](../principles.md))
- [ ] Every component page has Header, Anatomy, Properties, States, Usage, Content, Accessibility, Specs, Code
- [ ] Every published component has a description (purpose + status) and a documentation link
- [ ] Patterns state their rule; templates built only from instances
- [ ] Owner named; contribution path and review checklist written on Getting started
- [ ] Code Connect mapped for every component that exists in code; variable code syntax set
- [ ] One direction of token truth recorded; last reconciliation date on the Changelog
- [ ] Library analytics (or manual sample) reviewed this quarter; detach hotspots have an action
- [ ] Pre-delivery check in [../anti-slop.md](../anti-slop.md) passed on the specimen and templates

## Sources (checked 2026-10)

help.figma.com: View and explore library analytics (360039238353) · Code Connect (23920389749655) · Modes for variables (15343816063383) · Add guidelines files to a design library (43509372175511) · Use slots to build flexible components (38231200344599) · Extended collections (36346281624471) · Add descriptions (7938814091287) · Guide to Dev Mode (15023124644247). developers.figma.com: Comparing Code Connect UI and CLI. figma.com/blog: Schema 2025 design systems recap · Build by design (Config India, Oct 2026) · release notes. primer.style: Contributing to Figma. github.com/figma/sds (Simple Design System, Code Connect reference implementation).
