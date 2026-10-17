# Figma pre-delivery QA

Run this on every Figma deliverable (screen, flow, library or prototype) before it is shown or marked ready. Run it read-only first: `get_metadata` for structure and names, `get_screenshot` per breakpoint and mode, `get_variable_defs` on sample nodes, the precision audit (`canvas-craft.md` § 11) and the reactions audit (`prototyping.md` § 6). Fix what fails, then run `../anti-slop.md` § Pre-delivery check. Report only the failures, one line each with the fix. Each group links to its detailed rules.

## Structure & naming → [file-structure-and-naming.md](file-structure-and-naming.md)
- [ ] Pages ordered and separated for the file type; no screens inside library files.
- [ ] Every flow sits in a named section; frames are named `Screen · State · Width`.
- [ ] No default layer names (`Frame 12`, `Group 5`, `Vector`) in delivered frames or components.
- [ ] Explorations and rejected directions live on Explorations/Archive pages, not hidden on screens.
- [ ] Cover shows owner, status and version; thumbnail set.

## Auto layout & resizing → [auto-layout.md](auto-layout.md)
- [ ] Every container of related children uses auto layout; absolute position only for deliberate overlaps.
- [ ] Hug / Fill / Fixed chosen per layer, with min/max widths where content varies.
- [ ] Each screen survives resizing to its breakpoint's narrowest and widest width, the longest strings and empty content.
- [ ] Padding and gaps are spacing variables and line up with the layout guide's margins and gutters.
- [ ] Every absolute-positioned layer has deliberate constraints (`canvas-craft.md` § 3).

## Components & instances → [components.md](components.md)
- [ ] Every repeated element is a library instance; zero detached instances.
- [ ] Every component has its full state set (default, hover, pressed, focus, disabled; loading/error where relevant).
- [ ] Instances are changed only through component properties, never by editing their insides.
- [ ] Icons come from one set, swapped via instance swap, sized by optical-size variants.
- [ ] Main components carry a description and status line.

## Variables & tokens → [variables-and-tokens.md](variables-and-tokens.md)
- [ ] No raw hex, spacing, radius or font values on delivered layers (spot-check with `get_variable_defs`).
- [ ] Every variable is scoped; semantic variables alias primitives.
- [ ] Light and Dark modes are complete; switching modes changes color only, never layout.
- [ ] Code syntax is set; variable names match the CSS custom properties in `../web.md`.
- [ ] Prototype-state variables are isolated in `proto/*` and hidden from publishing.

## Typography → [canvas-craft.md § 6](canvas-craft.md), [../typography.md](../typography.md)
- [ ] Every text node uses a text style; no Auto line height in styles; letter spacing in %.
- [ ] Truncation and max lines tested with the longest real string and a ~30% longer translation.
- [ ] Tabular figures wherever numbers update or align; every OpenType feature listed for code.
- [ ] Type sizes meet the platform minimums in `../dimensions.md`.
- [ ] Each typeface choice is recorded with the gene it came from.

## Color & contrast, both modes → [canvas-craft.md § 9](canvas-craft.md), [../principles.md](../principles.md)
- [ ] Body text ≥ 4.5:1; large text, icons, input borders and focus indicators ≥ 3:1, checked in Light *and* Dark.
- [ ] Contrast measured on real pairs (text on its actual surface, icon on its fill), not on swatches.
- [ ] Color is never the only signal: errors and statuses also carry text or an icon.
- [ ] Elevation still reads in Dark (surface steps or mode-bound shadow variables).
- [ ] File color profile checked, stated in the handoff note, tokens given in the code's color space.

## Sizes, targets & safe areas → [../dimensions.md](../dimensions.md)
- [ ] Frames at preset widths in points, one per breakpoint the product supports.
- [ ] Every interactive element meets the platform target minimum (WCAG 2.2 floor 24×24 CSS px), even when the glyph is smaller.
- [ ] Nothing essential under the status bar, notch/island, home indicator or on-screen keyboard.
- [ ] Scrolling content clears fixed bars plus safe areas.
- [ ] Precision audit clean: whole-pixel x, y, width, height.

## Accessibility annotations → [handoff.md](handoff.md), [../principles.md](../principles.md)
- [ ] Native annotations in the Accessibility category (visible in Dev Mode), not loose sticky notes.
- [ ] Heading levels and landmarks marked on every screen.
- [ ] Focus order and keyboard behavior (Tab, Shift+Tab, Esc, arrows, Enter) annotated for every interactive screen.
- [ ] Accessible names for icon-only controls; alt text or "decorative" for every image.
- [ ] Error, status and live-update announcements described; reduced-motion alternative stated for each animation.

## Prototype → [prototyping.md](prototyping.md)
- [ ] Each flow has a goal-named starting point and a description; device set; no dead ends.
- [ ] Every duration and easing is a motion token; reactions audit clean; no default curves.
- [ ] States wired once inside component sets; Smart Animate pairs share names and hierarchy.
- [ ] Tested on the target device via Mirror at true size.

## Handoff readiness → [handoff.md](handoff.md), [canvas-craft.md § 10](canvas-craft.md)
- [ ] Finished sections marked Ready for dev; work in progress clearly excluded.
- [ ] All states present: empty, loading, error, success, long content, missing image, offline where relevant.
- [ ] Export settings on every asset layer; names kebab-case by meaning; SVG icons single-color.
- [ ] Placeholders bracketed and listed with exactly what must be supplied.
- [ ] Rules Figma can't express are annotated: truncation, OpenType, vertical trim, motion, breakpoint behavior.
- [ ] Developers have view access to the file and every library it uses.

## File hygiene & performance → [canvas-craft.md § 11](canvas-craft.md)
- [ ] No hidden abandoned layers, empty frames or stray off-canvas objects.
- [ ] Images no larger than about 2× display size; decorative effect stacks flattened; at most one blurred layer per screen.
- [ ] Memory meter checked on large files; explorations split into their own file.
- [ ] Named version saved at delivery, matching the handoff note.
- [ ] Final `get_screenshot` of each delivered frame compared against the style laws.
