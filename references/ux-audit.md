# UX Audit

An audit answers three questions, in this order:
1. **Can people do what they came to do?** (usability, accessibility)
2. **Does it hold together?** (consistency with its own style, or with a style spec if one exists)
3. **Does it look chosen, or like everything else?** (originality / slop)

Most audits stop at a list of small visual nits. Lead with the problems that stop people from succeeding.

## Inputs

- What is being audited: URL, screenshots, Figma link, or code.
- The product's main jobs — ask, or infer and state the assumption: "I'm assuming the key job is booking a table."
- **Key job unknown and real users reachable?** Find it before auditing (after *The Mom Test*, `atlas/ux/the-mom-test.md`). Ask about past behaviour, never opinions: "The last time you opened it, what were you trying to get done?" / "What did you use before or alongside it, and what does that cost you?" / "What happened the last time it went wrong?" The key job is the one people already spend time or money on. Record it with its evidence; if no one can be reached, state the assumption and mark that task's findings provisional.
- The style spec, if the work belongs to a profile in `~/.design-atelier/profiles/`.

For a live URL, use the browser tools to walk the real flows (including mobile width ~375px and keyboard-only). For Figma, inspect frames and prototype links. For code, read the components and run it if possible.

## Method

### 1. Walk the key tasks
For each main job, go step by step as a first-time user. Record every point of hesitation, confusion, dead end, or extra step. This finds the problems that matter most.

At each step, apply the Norman lenses (`atlas/ux/don-norman.md`):
- **Discoverability:** in a still screenshot — no hover, no tutorial — can a newcomer point to every available action and say how to do it? Hover-only, gesture-only and unlabeled-icon actions fail.
- **Mapping:** is each control on or next to what it changes, laid out like its effect?
- **Feedback:** is every action acknowledged within ~100ms, with the resulting state in the user's terms (not "Success")? Can a slow action be submitted twice?
- **Conceptual model:** from the screen alone, could the user say where their data is, what is saved, and what happens next? Does any cue suggest a wrong model?
- **Gulfs:** name the step where the user can't tell what to do (execution) or whether it worked (evaluation). These are usually the severity 3–4 findings.

Classify every error before proposing a fix. A **slip** (right goal, wrong action — look-alike targets, hidden mode, habit) is fixed by making targets differ, separating them, showing the mode, making it reversible. A **mistake** (wrong goal or model) is fixed by a clearer system image, a preview before commit, or the missing information at the point of decision. A confirmation dialog fixes neither: people confirm the action, not the object.

### 2. Heuristic pass
Check against these ten questions (adapted from Nielsen's usability heuristics, in our words):
1. Does the interface always show what's happening?
2. Does it speak the user's language, not the system's?
3. Can people undo and escape easily?
4. Is the same thing always done the same way?
5. Does it prevent errors before they happen?
6. Can people recognise options instead of remembering them?
7. Are there shortcuts for frequent users without burdening new ones?
8. Is every element earning its place?
9. Are errors explained in plain language with a way forward?
10. Is help available where it's needed?

### 3. Accessibility pass
Contrast of every text/UI pair; visible focus; keyboard-only completion of key tasks; labels and error text; headings and landmarks; target sizes; zoom to 200%; reduced-motion behavior. (`references/principles.md` § Accessibility minimums.)

### 4. Style consistency pass
With a style spec: check each law, token use, component variants, icon set, motion tokens. List every place the work breaks a law — and whether the break looks intentional (a candidate for evolving the style) or accidental.
Without a spec: check internal consistency — how many type sizes, colors, radii, shadow styles and button variants exist versus how many are needed.

### 5. Originality pass
Compare against `atlas/trends/_saturation-map.md` and `references/anti-slop.md`. Name each generic pattern found and its saturation. Then answer honestly: if the logo were removed, could this be mistaken for a thousand other products? What is the one thing only this product does visually?

## Severity

| Level | Meaning | Example |
|---|---|---|
| **4 · Blocker** | Users can't complete a key task, or a group of users is excluded | Checkout button unreachable by keyboard; text contrast 2:1 |
| **3 · Major** | Task completes with significant friction, errors or confusion | Form clears all fields on one error |
| **2 · Minor** | Noticeable friction, easy workaround | Inconsistent button styles between pages |
| **1 · Polish** | Craft and detail | Uneven icon stroke weights |
| **◇ Identity** | Not a usability problem; the work looks generic or off-style | Purple gradient hero + three icon cards + logo strip |

## Report template

```markdown
# UX Audit — [Product], [date]

**Scope:** [what was reviewed, devices, flows] · **Assumed key jobs:** [1–3]

## Summary
Three sentences: overall state, the biggest risk, the biggest opportunity.

## Top 5 (fix first)
| # | Issue | Where | Severity | Fix |
|---|---|---|---|---|

## Findings by task
### [Task name]
- [Step] — issue — severity — evidence (screenshot / selector) — recommended fix

## Accessibility
[findings, each with the WCAG criterion]

## Style consistency
[law-by-law, or internal-consistency counts]

## Identity / originality
[generic patterns with saturation; what is distinctive and should be protected; one concrete move that would make it unmistakable]

## What works
[things to keep — an audit that only criticises is not trusted]
```

Every finding needs evidence (where exactly) and a concrete fix. "Improve the hierarchy" is not a fix; "make the price the largest element on the card and move the SKU under the title in `ink-muted`" is.
