# Prototyping

A prototype answers one question: can people find it, does it feel right, will the team commit to it. Build exactly enough to answer that question, wire it so it behaves like the build, and test it on the device it is for.

Load `figma:figma-use` before writing interactions via MCP. Reactions are set with `await node.setReactionsAsync([...])`. **Durations are seconds in the API (`0.22`) and milliseconds in the UI (220).** Motion values come from `../motion.md`; component states from `components.md`; prototype variables from `variables-and-tokens.md`; device sizes and safe areas from `../dimensions.md`.

## 1. Decide what to prototype

| Prototype | Leave static (show as frames in the state matrix) |
|---|---|
| The primary task, end to end | Every edge state of every screen |
| The most likely error on that path, and its recovery | Platform-standard behavior (system sheets, pickers, permission dialogs) unless the design changes it |
| The navigation model: tabs, back, modals, deep entry points | Settings lists, legal pages, long static content |
| Novel interactions and gestures, anything costly to get wrong in code | Marketing pages: build them in code (`../web.md`) |
| Transitions that carry meaning (continuity, hierarchy) | Decorative motion |
| State-heavy controls, through interactive components | Data variety beyond what variables can fake |

- **Fidelity follows the question.** A navigation test needs no Smart Animate; a motion review needs no forty screens.
- **No dead ends.** Every screen has a way forward and a way back; every flow ends on a success state or returns to its start.

## 2. Flows and starting points

- **One flow per user goal.** Name the starting point as the goal (`Pay with saved card`, not `Flow 1`) and write its description: goal, start state, what is *not* prototyped. Descriptions appear in the presentation sidebar.
- Figma creates a starting point on the first connection; rename it immediately. A page can hold several.
- **Prototype settings (device, background, starting points) belong to the page**, so keep one prototype per page and set the device to match the frame width.
- Lay flows out left → right in sections (`file-structure-and-naming.md` § 3), so the canvas reads like the prototype.
- Via MCP: the page's `flowStartingPoints` (`[{ nodeId, name }]`) is writable.

## 3. Triggers

| Trigger | Use for | Behavior to know |
|---|---|---|
| On click / On tap | Actions, navigation | The default; covers most needs |
| On drag | Drag-to-dismiss sheets, swipe cards | The drag scrubs through the transition; for carousels use horizontal scroll overflow instead |
| While hovering | Tooltips, hover feedback (desktop only) | Reverts when the cursor leaves. For component hover, use a Hover variant (§ 9) |
| While pressing | Press feedback, long-press previews | Reverts on release |
| Mouse enter / Mouse leave | Menus that stay open until dismissed | Fire once per entry/exit (since November 2023); pair them |
| Mouse down / Mouse up | Press-and-release menus | Open on down, choose on up |
| Key / Gamepad | Shortcuts, Esc to close, Enter to submit, arrow keys in lists | Single keys or combinations |
| After delay | Splash → home, toast auto-dismiss, loading → loaded | Milliseconds; fires after the viewer stays on the frame |
| When video hits / ends | Video players | Only on connections from a video layer |

Touch screens have no hover: never put meaning only in a hover trigger.

## 4. Actions and transitions

- **Actions:** Navigate to, Back, Scroll to, Open link, Open / Swap / Close overlay, Change to (variants only), Set variable, Set variable mode, Conditional. One trigger can run several actions, top to bottom; the order changes the outcome.
- **Pick the transition from the spatial model**, not taste, so motion explains the structure:
  - Drill-in hierarchy → **Push** / **Slide** (right to left on iOS).
  - Sheets and modals → **Move in** from the bottom, **Move out** to dismiss.
  - Unrelated destinations (tabs, top-level sections) → **Dissolve** or **Instant**.
  - One element becoming the next screen → **Smart Animate**.
  - Material's patterns map cleanly: container transform ≈ Smart Animate; shared axis ≈ Push/Slide; fade through ≈ Dissolve.
- **Decide what navigation preserves.** Navigate actions can reset or keep scroll position and interactive-component state (API: `resetScrollPosition`, `resetInteractiveComponents`; verify UI labels). Tabs usually keep their state; a fresh flow resets it.

## 5. Smart Animate requirements

- **Layers match when they share the same name, the same parent names and the same position in the hierarchy.** Top-level frame names may differ. Text layers you renamed match by name; auto-named text layers match by text style.
- **Duplicate the frame, then edit**, so names stay identical. Name new layers deliberately; hover a layer in the Prototype tab to see what it matches.
- **Hide with opacity 0, not visibility**, so the layer fades instead of popping. Layers that exist only in the destination dissolve in.
- **Animates:** position, size, rotation, opacity, and fills (solid, gradient, image). Auto layout reflow animates too, expanding a row moves its neighbors.
- **Falls back to dissolve:** layers with drop or inner shadows, and morphs between different shapes. Layers with noise, texture or blur do animate, but only between duplicated frames.
- **Overlays:** Open overlay can't Smart Animate; Swap overlay between overlays with matching layers can.
- **Shared-element transitions:** use Push/Slide/Move with "Smart animate matching layers", matched layers (header, image) animate while the rest slides. Put a solid-fill rectangle behind the content, or Slide and Move show both screens overlapping.

## 6. Motion matched to the style's tokens

Prototype motion is a spec developers copy; it must use the same numbers as the code tokens in `../motion.md`.

| Token | Figma interaction setting | Typical use |
|---|---|---|
| `--duration-fast` (e.g. 120ms) | Duration 120 | Hover, press, toggle (Change to) |
| `--duration-base` (e.g. 220ms) | Duration 220 | Popover, small layout change |
| `--duration-slow` (e.g. 400ms) | Duration 400 | Screen transition, large reveal |
| `--ease-standard` `cubic-bezier(.2,0,0,1)` | Custom bezier 0.2, 0, 0, 1 | Movement within the screen |
| `--ease-enter` `cubic-bezier(0,0,0,1)` | Custom bezier 0, 0, 0, 1 | Arrivals: Move in, overlays opening |
| `--ease-exit` `cubic-bezier(.3,0,1,1)` | Custom bezier 0.3, 0, 1, 1 | Departures: Move out, close |
| Spring (Physical personality) | Custom spring: stiffness, damping, mass | Sheets, cards, drag release |

- **Never leave the default curve.** It is a decision nobody made.
- **Use Custom values, not presets, for anything that ships.** The Gentle / Quick / Bouncy / Slow springs and the Ease and Back presets have no published parameters, so code can't match them. Custom springs (stiffness, damping, mass) map 1:1 to motion.dev (`type: "spring", stiffness, damping, mass`) and SwiftUI `.interpolatingSpring(mass:stiffness:damping:)`.
- **Custom prototype curves can't be saved**, and prototype transitions take raw values with no variable binding in the Plugin API. The file's TIMING/EASING variables (`variables-and-tokens.md` § 7) therefore stay the source of truth, but you copy their values by hand. Keep the exact numbers on the Motion foundations page (`design-system.md`) and paste them, or set them in one `use_figma` script from a token table: `{ type: 'CUSTOM_CUBIC_BEZIER', easingFunctionCubicBezier: { x1, y1, x2, y2 } }` and `{ type: 'CUSTOM_SPRING', easingFunctionSpring: { mass, stiffness, damping, initialVelocity } }`.
- **Audit:** read every node's `reactions` and list the distinct (transition, easing, duration) combinations; anything not in the token table is a bug.
- **Back easings (overshoot) and Bouncy springs** only when the style's personality is Physical or Kinetic.
- **Reduced motion:** prototypes have no reduced-motion switch (verify). To show the alternative, add a boolean `proto/reduceMotion` and a Conditional that runs an Instant or Dissolve version of the same Navigate.
- **Figma Motion** (open beta since Config 2026, any plan, edit access): a timeline with keyframes, preset and composite animation styles, custom animation styles you can publish, a Hold easing, and custom curves and springs saveable as variables. Use it for authored animation that Smart Animate can't express: loaders, illustration, staged reveals. Author with `figma:figma-use-motion`; implement with `get_motion_context` and `figma:figma-implement-motion`. Developer handoff of Motion: `handoff.md` § 5. Whether Motion timelines play inside prototypes, verify.

## 7. Overlays

- **Use for** menus, popovers, dialogs, bottom sheets, toasts and tooltips, anything that sits above the current screen without replacing it.
- **Size the overlay frame to the component** (a sheet is device width and its own height), not a full-screen frame with an empty area: that breaks "Close when clicking outside".
- **Settings live on the overlay frame**, not the connection: position (seven presets or manual), Close when clicking outside, and Add background behind overlay (set color and opacity to the scrim token). These are read-only in the Plugin API (`overlayPositionType`, `overlayBackground`), so specify them for the person or ask them to set them.
- Multi-step dialogs: **Swap overlay** (Smart Animate works between matching overlays). Dismiss with Close overlay or Back.
- Every overlay has a visible close control and, on desktop, Esc (Key trigger) closes it.
- **Toast:** Open overlay → on the toast, After delay (e.g. 4000ms) → Close overlay.

## 8. Scroll and fixed elements

- **Scrolling needs overflow**: set the frame's overflow (vertical, horizontal, both, none), and let content exceed the frame. Top-level frames taller than the device scroll on their own.
- **Positions:** Scroll with parent (default), **Fixed** (status bar, nav bar, tab bar, floating action button), **Sticky** (sticks to the top edge of its scroll container: section headers, filter bars).
- **Auto layout frames accept Fixed only on absolute-positioned children**, so make nav and tab bars absolute children, or keep them outside the content stack.
- **Carousels:** an inner frame with clip content and horizontal overflow; fixed height.
- **Scroll to** for anchor links and "back to top"; it can animate.
- **Content must clear fixed bars:** bottom padding = tab bar height + home-indicator safe area (`../dimensions.md`); otherwise the last item hides.

## 9. Interactive components for states

- **Wire the states from `components.md` § 6 inside the component set once**, and every instance in every prototype behaves, no duplicate screens per state. Typical wiring: While hovering → Hover; While pressing (or Mouse down / up) → Pressed; On click → Change to Checked / Expanded / Selected.
- **Change to works only between variants of the same set**; a nested instance can switch its parent's variant (an accordion row's chevron expanding the row).
- **Same layer names across variants** make Smart Animate move the parts (a switch knob slides instead of blinking), at `--duration-fast`.
- **After delay** between a Loading and a Loaded variant shows async behavior; loop two variants for a spinner.
- **Disabled variants carry no interactions**, so the prototype respects disabled states.
- Variant structure and properties: `components.md`. Focus order and keyboard behavior go into annotations (`handoff.md`), not into a hand-wired Tab flow.

## 10. Variables, conditionals and modes

Available on paid plans to anyone with edit access.

- **Set variable** makes one frame behave like many: a number for cart count or progress width, a string for a name or total, a boolean for "error shown" or "signed in", a color for selection.
- **Expressions:** number math, string joins and boolean logic, `cartCount + 1`, `"Hi, " + firstName`.
- **Conditional (if/else)** for validation and branching: if `proto/emailValid` is false, show the error variant; else navigate.
- **Set variable mode** switches the page's mode live, Light/Dark, locale, brand. Objects with an explicit mode ignore it, so leave screens on Auto when they should follow.
- **Keep prototype state in its own collection** (`proto/*`), hidden from publishing: it is state, not design tokens (`variables-and-tokens.md`).
- **Typing is faked:** prototypes don't accept real text input (verify), so a tap sets the "typed" value.
- Via MCP: `setReactionsAsync` takes `SET_VARIABLE`, `SET_VARIABLE_MODE` and `CONDITIONAL` actions; bind properties with `setBoundVariable` (patterns in `figma:figma-use`).

## 11. Test on the device

- **Figma mobile app:** in the **Mirror** tab, the phone shows whatever top-level frame is selected on the desktop, scaled to the device width and tappable. Use the same account on both devices; Wi-Fi or cellular both work; mirroring needs edit access. The app's presentation view plays from the flow starting point.
- **Check on the real device:** thumb reach and target size, type legibility at true size, safe areas (notch, island, home indicator), the keyboard covering inputs, fixed bars during scroll, and motion timing, durations that feel right on a monitor often feel slow in the hand.
- **Desktop and web:** present at Actual size (100%) at each breakpoint width; Fit width hides real type sizes.

## 12. Present

- **Scaling:** Actual size, Fit width, Fit width and height, Fill screen (Z cycles them); device frame on or off; background from the prototype settings.
- **Stakeholder demo:** share with "Hide UI" (it adds a URL parameter), start from a named flow, walk the happy path, then the error path.
- **Usability test:** turn off "Show hints on click" so hotspot highlights don't give answers away. Give each task its own starting point; R restarts the current flow.
- **While building**, use the inline preview (Shift+Space); edits show live.

## QA, prototype

- [ ] Each flow answers a stated question; its starting point is named as a user goal and has a description.
- [ ] Device and background set in the page's prototype settings; device matches the frame width.
- [ ] No dead ends: every screen has forward and back paths; the main error path is wired.
- [ ] Transitions follow the spatial model (push for depth, move-in for sheets, dissolve for siblings).
- [ ] Every duration and curve is a motion token; the reactions audit finds no stray values; no default curves.
- [ ] Smart Animate pairs share names and hierarchy; nothing pops; no shadow layers relied on to animate.
- [ ] Overlays sized to content, close on outside click or a visible control, Esc on desktop, scrim from tokens.
- [ ] Fixed and sticky elements behave; content clears bars and safe areas.
- [ ] States wired once inside component sets, not duplicated as screens.
- [ ] Prototype variables live in `proto/*`, hidden from publishing; Light/Dark switching works through Set variable mode.
- [ ] Tested on the target device via Mirror at true size; findings noted.
- [ ] Usability-test links have hotspot hints off; demo links use Hide UI.
