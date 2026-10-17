# Developer hand-off

Use when a flow, screen or component moves from design to engineering, or when the person asks for "specs", "redlines", "dev-ready" or "hand-off". This file defines what the **Figma file** must contain and how to verify the build. To generate a written spec sheet from it, run the `design:design-handoff` skill (if installed) on the ready section; to build it in code, `figma:figma-design-to-code`; motion in code, `figma:figma-implement-motion`. File layout: [file-structure-and-naming.md](file-structure-and-naming.md). Tokens and code syntax: [variables-and-tokens.md](variables-and-tokens.md). Component states and properties: [components.md](components.md). Resizing behaviour: [auto-layout.md](auto-layout.md). Frames, pixels, export details: [canvas-craft.md](canvas-craft.md).

**Check access first:** Dev Mode, annotations, measurements and compare changes need a **Full or Dev seat** on a paid plan. A developer on a view-only seat will not see your annotations, confirm seats before hand-off, or the annotations go nowhere.

## 1. When a design is "ready for dev"

Mark nothing ready until every gate passes:

| Gate | Pass when |
|---|---|
| Content | Final copy, or every placeholder `[bracketed]` and listed in the note |
| Coverage | All states and edge cases in § 2 drawn, every breakpoint drawn |
| System | Only library instances, nothing detached; every fill, stroke, gap, padding, radius and text bound to variables or styles |
| Annotations | Behaviour, accessibility and content annotations complete (§ 3) |
| Review | Design critique done; engineering lead has seen it once *before* ready; open comments resolved |

Then mark the **section** (not each frame) *Ready for dev*: select it → *Mark as ready for dev* next to its label.

| Status | Plans | Meaning |
|---|---|---|
| Ready for dev | All paid plans | Developers who opened the file in Dev Mode are notified; the design appears in the *Ready for dev* view (left sidebar) |
| Changed | Automatic | Set by any edit after marking; cannot be set manually |
| Completed | Organization, Enterprise | Development finished; notifies viewers |

- **Edits that do not trigger Changed**: accepting a library instance update, changing the value of an already-applied variable or style, temporary hover nudges. Everything else does.
- **Close every change with a reason**: *Ready for dev* → *Done with changes* → one sentence ("Error copy shortened after legal review"). The reason lands in version history and in the notification, silent edits to ready work are the fastest way to lose engineering trust.
- **Developers inspect** in focus view (Organization/Enterprise; one design at a time with its own version history and mode switcher) and with **Compare changes** (all paid plans): side by side, overlay, edited/added/deleted layers, property diff and code diff, plus instance-with-overrides vs main component.

## 2. What every hand-off includes

| Item | Show | Why |
|---|---|---|
| Component states | Default, hover, pressed, focus-visible, disabled, loading, selected, error, success, whichever the component has | Undrawn states get invented during build |
| Screen states | Empty (first use and no results), loading (skeleton or spinner, with delay rule), error (recoverable and fatal), partial data, success | These are where products feel unfinished |
| Content extremes | Longest realistic string and a translated-length version, 0 / 1 / many items, missing image or avatar, very large numbers | Text and data break layouts, not pixels |
| Permissions and connectivity | Read-only, no permission, offline, slow (what shows after 1 s, after 10 s) | Real conditions, not the happy path |
| Responsive | One frame per breakpoint from [../dimensions.md](../dimensions.md), plus annotations for behaviour *between* them: what fills, hugs, wraps, reflows, hides | Devs build the in-between widths you didn't draw |
| RTL (if the product ships an RTL language) | Mirrored key screens; which icons mirror (directional arrows) and which don't (play, checkmarks, logos) | Mirroring is a design decision, not a CSS flag |
| Interactions | Prototype for the flow; trigger → result for every interactive element | Clicks without outcomes are guesses |
| Motion | Trigger, property, duration token, easing token, reduced-motion fallback | Durations in ms get rounded wrong; tokens don't |
| Accessibility | § 4 | Cheapest to fix in design |
| Assets | Export settings on every asset layer (§ 6) | Assets download from Dev Mode with the right names and scales |
| Note | The hand-off note (§ 7) | Context the canvas can't hold |

## 3. Annotate in Dev Mode

Use **native annotations** (all paid plans; Full seat with edit access to add, Full or Dev seat to view; Shift T) instead of sticky-note frames, they stay attached to layers, show in Dev Mode by default and can be filtered by category.

| Category (Figma defaults) | Put here | Example |
|---|---|---|
| Development | Data source, validation, truncation, breakpoint behaviour, anything code must decide | "List paginates at 50; 'Load more' button, not infinite scroll" |
| Interaction | Triggers, outcomes, motion with token names | "Tap card → detail sheet; `duration-base`, `ease-enter`; reduced motion: fade only" |
| Accessibility | Focus order, roles, names, announcements, keyboard | "Focus moves to sheet heading on open; Esc closes, focus returns to card" |
| Content | Copy rules, character limits, localisation | "Title max 2 lines then ellipsis; never truncate prices" |

- **Pin properties instead of typing values** (*+ Property*), pinned values stay current when the design changes; typed ones rot.
- **One behaviour per annotation, one category each**: devs filter by category; mixed notes get half-read.
- **Measurements** (Shift M) only where spacing is *not* a token or the relationship isn't obvious (optical alignment, overlap); tokens already answer the rest.
- **Custom categories are per file** (*Edit categories…*); add `Analytics` or `Edge case` only if the team will filter by them.
- **Dev resources**: attach the ticket, Storybook page or GitHub file to the section or component, resources on a component propagate to every instance.

## 4. Accessibility annotations

Annotate in the Accessibility category, or use a stamp kit: GitHub's open-source **Annotation Toolkit** (2025) and CVS Health's annotation kits cover focus order, landmarks, headings, labels, tables and image descriptions. Minimums from [../principles.md](../principles.md) and [../dimensions.md](../dimensions.md):

| Annotate | Rule (WCAG 2.2 AA unless stated) |
|---|---|
| Focus order | Numbered stamps on every interactive element per screen and per open overlay; where focus goes on open and on close |
| Roles and names | Role (button, link, tab, dialog…) and the accessible name source for every control, especially icon-only buttons |
| Headings and landmarks | Heading levels and header/nav/main/footer regions |
| Contrast | Text 4.5:1, large text 3:1, UI components and focus indicators 3:1 against adjacent colours, in Light **and** Dark |
| Target size | Never below 24×24 CSS px (2.5.8); the style's platform targets (44 pt iOS, 48 dp Android) from dimensions |
| Alt text | Written alt for informative images; "decorative" flagged for the rest |
| Announcements | Status messages, errors, loading completion: what a screen reader hears and when |
| Keyboard | Keys per custom widget (arrows in tabs and menus, Esc for overlays), no keyboard traps |
| Motion | Reduced-motion behaviour for every animation |

## 5. Tokens, names and code links

- **Tokens, not values**: bind everything, and give every variable code syntax so Dev Mode shows `var(--color-ink)` instead of a hex ([variables-and-tokens.md](variables-and-tokens.md)). Dev Mode can *suggest* a variable for a raw value (exact value and matching scope), treat each raw value as a bug to fix before ready, not a suggestion for devs.
- **In notes, write the token, value in brackets only if it helps**: `space/4 (16)`, `duration-fast`, `ease-standard`.
- **Code Connect** maps library components to real code so Dev Mode and the MCP server return `<Button variant="primary">` instead of generated markup, set up via `figma:figma-code-connect` ([design-system.md](design-system.md) § 8 for UI vs CLI and plans).
- **No detached instances in ready work**: detaching cuts the Code Connect link and the update path; Compare changes shows instance overrides against the main component.
- **Component playground** (Dev Mode → *Explore component behavior*) lets developers try properties and variable modes without editing the design, point them to it instead of drawing every combination.
- **Motion in Figma Motion** (open beta): devs open the Inspect panel's *Motion* tab for a read-only timeline and copy CSS, React or JSON; the MCP server returns keyframes, timing and easing (`get_motion_context`). Still name the tokens in an annotation, exported curves are values.

## 6. Export settings

Full per-format settings (stroke handling, colour profile, scale syntax) live in [canvas-craft.md](canvas-craft.md) § 10; for hand-off, enforce these:

| Asset | Hand off as | Why |
|---|---|---|
| Icons | SVG at 1x (Figma exports SVG and PDF at 1x only), delivered from the icon library package rather than per screen | One source of truth; code tints them via `currentColor` |
| Logos, simple illustrations | SVG, *Outline text* on for wordmarks | Renders without the font |
| Photos, complex raster | JPG (PNG if transparent): web 1x + `@2x`; iOS `@2x` + `@3x`; Android 1, 1.5, 2, 3, 4x density folders | Matches each platform's asset pipeline; Figma has no WebP/AVIF export, so convert in the build |
| Gradients, borders, shadows, text | Not exported | They are code, built from tokens |

- **Put export settings on the asset layer itself**: it then appears as a downloadable asset in Dev Mode with the intended formats, so developers don't guess.
- **Name the layer as the file**: the layer name becomes the file name, and the suffix field adds nothing automatically, type `@2x` yourself.

## 7. Hand-off note template

Put the note next to the section, as an embedded **Figma spec** (open beta on paid plans; check `whoami` → `specs_enabled` and use `figma:figma-spec`), or a text frame, and link it in the ticket.

```markdown
# [Feature], hand-off
Status: Ready for dev · [date] · Designer: [name] · Eng lead: [name]
Figma: [section link] · Ticket: [link] · Library: [name] v[x.y.z]

## Goal
[One paragraph: user problem, success measure.]

## Scope
In: [screens/flows] · Out: [explicitly not included] · Placeholders still open: [list]

## Flows and screens
| Screen | Frame | States drawn | Notes |
|---|---|---|---|

## Behaviour
- Responsive: [breakpoints and what changes between them]
- Interactions: [trigger → result, motion tokens]
- Data: [sources, validation rules, limits, pagination]

## Accessibility
- Focus order: [see annotations / summary] · Announcements: [list]
- Contrast checked in Light and Dark: [yes/no + exceptions]

## Components
| Component | Library or new | Code Connect | Notes |
|---|---|---|---|

## New or changed tokens
| Token | Value (Light / Dark) | Why |
|---|---|---|

## Assets
[list with export formats; where they live]

## Open questions
- [question], owner, due
```

## 8. Design QA after build

Review the implementation against the design before the ticket closes; do it on a real build, not a screenshot sent over chat.

1. **Side by side at every breakpoint**: `get_screenshot` of the frame vs a browser or simulator screenshot at the same width; for close calls, overlay the build screenshot at 50 % on the frame in a `QA` section.
2. **Tokens**: inspect computed styles, values must resolve from the token variables, no raw hex or px in components.
3. **States and edge cases**: trigger every state from § 2 in the build, including long text, empty, error, offline.
4. **Accessibility**: keyboard-only pass, screen-reader names and announcements, contrast in both modes, target sizes, reduced motion (`design:accessibility-review` if installed).
5. **Motion and assets**: timings feel like the prototype; images crisp at 2x; icons crisp and aligned.
6. **Log findings** with the severity scale from [../ux-audit.md](../ux-audit.md) (4 Blocker … 1 Polish, ◇ Identity for off-style work), each with a screenshot pair and the design link; blockers and majors reopen the ticket.
7. **Close the loop**: mark the section *Completed* (Organization/Enterprise) or note it in the file; add a journal entry ([../../method/evolve.md](../../method/evolve.md)) for anything the build taught about the style.

## QA checklist

- [ ] Developers have Full or Dev seats and access to the file and its libraries
- [ ] All gates in § 1 passed; status set on the section, not frame by frame
- [ ] Every component and screen state from § 2 drawn, including empty, loading, error and long text
- [ ] Every breakpoint drawn; in-between behaviour annotated; RTL covered if shipped
- [ ] Annotations in the right categories; properties pinned, not typed; dev resources linked
- [ ] Focus order, roles/names, headings, alt text, announcements and keyboard annotated; contrast and target sizes pass
- [ ] No raw values, no detached instances; Code Connect mapped for library components
- [ ] Motion specified with token names and a reduced-motion fallback
- [ ] Export settings on every asset layer; names match the code's asset convention
- [ ] Hand-off note complete, linked in the ticket; open questions have owners
- [ ] After build: design QA run at every breakpoint, findings logged with severity, status moved to Completed

## Sources (checked 2026-10)

help.figma.com: Dev Mode statuses and notifications (26781702258583) · Dev Mode focus view (23919923330455) · Compare changes in Dev Mode (15023193382935) · Add measurements and annotate designs (20774752502935) · Guide to Dev Mode (15023124644247) · Export formats and settings (13402894554519) · Variables in Dev Mode (27882809912471) · Link Dev resources to layers (15023231995927) · Code Connect (23920389749655) · Hand off animations to development (41296356954263). developers.figma.com: MCP server, Structure your Figma file. figma.com/blog: Build by design (Specs, Oct 2026). github.com/github/annotation-toolkit · github.com/cvs-health/annotations. W3C: WCAG 2.2.
