# Principles

A personal style changes how things look and behave. It does not change how people read, see and act. These are the fundamentals every style must still satisfy, the floor under originality, not a style of their own.

## Visual principles

Every screen is judged on these, whatever the style. A style changes *how* each is satisfied, Swiss alignment and Memphis alignment look nothing alike, never *whether*. Each principle ends with a check you can run on a screenshot.

| Principle | What it means | Apply | Check |
|---|---|---|---|
| **Hierarchy** | One thing is seen first, one second, the rest after | Decide the reading order before styling. Build it with size, weight, position, contrast and space, using as few of these as the job needs | Squint or blur the screenshot: the intended first element still wins |
| **Alignment** | Every element sits on a shared line with something else | Align to grid columns, the baseline, or a strong edge; use one alignment per group (left *or* centered, not both) | Draw vertical lines through every left edge: few lines = calm, many = noise. No element is off by 1 to 3px |
| **Contrast** | Difference that signals importance or category | Contrast in size (≥ 1.5× steps), weight, value, color, shape, or density, strong enough to read as intentional | Every contrast is either clearly different or identical; "almost the same" (15px vs 16px, two near greys) is a bug |
| **Balance** | Visual weight distributed so the layout feels stable, symmetrical (formal), asymmetrical (dynamic), or radial | Visual weight grows with size, darkness, saturation, texture, isolation and faces. Counter a heavy element with space or a smaller dark one on the other side | Cover each half of the screen in turn: neither side feels empty by accident. Asymmetry is a decision, not a leftover |
| **Proximity** | Things near each other read as related | Space between groups visibly larger than space inside them (roughly 2× or more) | Every label is closer to its own field than to the next one |
| **Repetition / consistency** | Same thing, same look, same place | Reuse tokens and components; repeat a few distinctive moves so they become the style's signature | Count distinct type sizes, colors, radii, shadows, button styles, each count matches the spec |
| **Emphasis / focal point** | One clear point of attention per view | Give the primary action or message the single strongest contrast; everything else steps down | Exactly one element per view uses the accent at full strength |
| **Proportion & scale** | Sizes relate to each other through a system | Use a modular type scale and a spacing scale (4- or 8-based); size images by column spans | Every size on screen exists in the scale; no ad-hoc values |
| **Rhythm** | Repeated intervals that the eye can follow, with deliberate breaks | Consistent vertical spacing between sections; break the rhythm once to create emphasis | Section gaps form a pattern; the one exception is the intended moment |
| **White space** | Empty space as an active element, macro (between sections) and micro (inside components, line-height, letter spacing) | Give important elements more surrounding space; never fill space because it is empty | Removing any decorative element makes the screen better or no worse |
| **Figure-ground** | Clear separation between content and background | Surfaces, borders or value steps that make layers obvious without effects | Every interactive surface is distinguishable from the background in greyscale |
| **Gestalt (similarity, continuity, closure, common region)** | The eye groups by likeness, follows lines, completes shapes, and reads enclosed areas as units | Use these instead of extra boxes and dividers; let alignment carry continuity | Remove one border or divider: the grouping still reads |
| **Unity** | Everything looks like it belongs to one system | Every element traces back to the style's laws and tokens | Cover the logo: the screen still reads as one product, not a collage |
| **Movement / eye path** | The route the eye takes through the layout (often Z on sparse pages, F on text-heavy ones) | Place the next step where the path naturally goes; use direction in imagery and diagonals deliberately | Trace the path with a finger: it reaches the primary action without backtracking |

### Grid

Every layout sits on a grid, even when the style hides it.
- Choose columns, gutters and margins per breakpoint (`references/dimensions.md`).
- Snap element edges to columns and vertical positions to the baseline or spacing unit.
- Breaking the grid is a tool for emphasis; break it once, on purpose, and keep everything else on it.

## Typography

- Body text 16px+ on screen (14px only in dense professional tools, with care), line length 45 to 80 characters, line-height 1.4 to 1.6 for body.
- Limit type sizes per screen; a modular or baseline-derived scale beats arbitrary sizes.
- Pair typefaces by contrast in role, not similarity (two similar sans-serifs look like a mistake).
- Use real typographic characters: curly quotes, proper dashes, ellipsis, non-breaking spaces where needed.

## Color

- Color carries meaning (state, action, category) before decoration. Never rely on color alone to convey meaning, add text, icon or shape.
- Contrast (WCAG 2.2 AA): text 4.5:1, large text (≥ 24px, or ≥ 18.66px bold) 3:1, UI components and focus indicators 3:1 against adjacent colors.
- Design dark mode as its own palette, not an inversion: lower saturation, avoid pure black/white extremes, re-check every contrast pair.

## Interaction

- **Visibility of state and feedback:** the user always knows what is happening (loading, saved, failed, selected). Every action is acknowledged within ~100ms and shows its result in the user's terms ("Sent to 3 people", not "Success"). Pending buttons ignore repeat presses.
- **Signifiers:** every action has a visible cue for what it does and how, fill or outline plus a verb, a drag grip, a field edge, without hover and without a tutorial. Non-interactive things don't borrow those cues.
- **Mapping:** controls sit on or next to what they change, arranged like their effect (row actions in the row, up moves up).
- **Constraints before error messages:** make invalid input impossible (pickers, masks, disabled options with a one-line reason) rather than rejecting it after submit.
- **Forgiveness:** prefer undo over "Are you sure?", people confirm the action, not the object, so dialogs catch neither slips nor mistakes. Make frequent and destructive controls look different and sit apart; preview outcomes. If an action truly can't be undone, name the object and the consequence.
- **Truthful model:** what the screen shows must let people form the right model of where things are and what happens next. Never show a cue that implies a false one (a sync badge on local-only files).
- **Consistency:** same thing, same look, same place, same behavior.
- **Recognition over recall:** show options; don't make people remember them.
- **Progressive disclosure:** show what most people need; reveal the rest on demand.
- **Targets:** at least 24×24 CSS px (WCAG 2.2), 44×44 for touch.
- **Focus:** visible keyboard focus on everything interactive; logical tab order.

## Honest design

Borrowing the spirit of Dieter Rams' principles, in our own words: good design is useful before it is beautiful, understandable without instruction, unobtrusive, honest about what the product does, long-lasting rather than fashionable, thorough in details, considerate of resources, and as little design as the job requires. A personal style decides *how* to be these things; it never opts out.

Never use deceptive patterns: hidden costs, confirm-shaming, pre-checked consent, fake urgency, roach-motel cancellation, disguised ads. See `atlas/ux/dark-patterns.md` when available.

## Accessibility minimums (non-negotiable in every style)

- Semantic structure: real headings, landmarks, lists, buttons, labels.
- Every input has a visible label; errors are described in text, next to the field.
- Images have meaningful `alt` (or empty `alt` if decorative).
- Content works at 200% zoom and 320px width without horizontal scrolling.
- Motion respects `prefers-reduced-motion`; nothing flashes > 3×/second.
- Test with keyboard only, and with a screen reader for key flows.
