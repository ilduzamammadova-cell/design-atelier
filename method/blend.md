# Blend, inventing a new style from genes

A new style is not an average of influences. Averages are bland; that is how generic design is made. Originality comes from **a few specific genes from sources that are far apart, held together by one person's taste and a small set of hard laws.**

## 0. Inputs

- The person's DNA profile (or, without one, the brief plus four quick questions, `discover.md` § Quick).
- The brief: what is being made, for whom, the one job it must do, constraints (platform, brand assets that must stay, accessibility needs, content).
- Whether cultural mixing is requested. Default: no.

## 1. Gather candidates

```bash
python3 <skill-dir>/scripts/atlas_match.py --profile ~/.design-atelier/profiles/<slug>/dna.md --top 8
python3 <skill-dir>/scripts/atlas_match.py --profile ... --vary          # a different draw from a wider pool, run it at least once
python3 <skill-dir>/scripts/atlas_match.py --profile ... --topic <subject>      # topic-weighted
python3 <skill-dir>/scripts/atlas_match.py --profile ... --section art,architecture   # cross-domain pull
```

Add `--include-cultures` only if the person asked for cultural mixing.

Sources used in earlier blends (`~/.design-atelier/recent-sources.json`) are pushed to the bottom of every list. Prefer fresh sources: a master that appears in every style becomes a new house default, which is the same failure as a trend. Reuse a recent source only when this person's evidence clearly calls for it, and say why.

Read only the cards you are seriously considering (8 to 12) with `atlas_match.py --genes id1,id2,…`, which prints just the essence, **Genes** table and **Don't copy**. Open a full card only for the sources you end up using.

## 2. Pick genes by role

Fill four roles. One or two genes per source, never more. The roles keep the blend coherent *and* new:

| Role | Comes from | Job | Typical gene |
|---|---|---|---|
| **Spine** | a KIN card (close to the person) | Structure: grid, type system, spacing logic. Makes it feel like *them*. | A grid discipline, a type hierarchy rule |
| **Voice** | a TENSION card (agrees mostly, diverges on 2 to 3 axes) | The one surprising quality people will remember. | A color behavior, a shape language, a typographic attitude |
| **Accent** | a FAR card, preferably outside graphic/UI (art, architecture, product, craft) | A single detail no other interface has. Cross-domain borrowing is what stops UI from looking like other UI. | A light slot from architecture, a texture from print, a joint detail from furniture |
| **Personal** | the person's own life (Discover Q1, Q3, Q6, Q10) | Grounds the style in something no one else has. | Their material, an object's proportions, a place's light |

Optional fifth: **Behavior**, one UX card gene that sets the interaction attitude (calm vs eager, modeless, progressive disclosure…). A style includes how it behaves.

Checks while picking:
- At least two disciplines among the sources. Four graphic designers in a row produce graphic design history, not a new style.
- Spine and Voice must not come from the same movement.
- If a gene is iconic enough that people would name its source on sight, transform it (change scale, medium, or context) or drop it.
- If a gene's UI translation lands on a saturated trend surface, backdrop blur, glass panels, glows, gradient meshes, gradient text, re-translate it into a non-trend material: translucency as overlapping flat tints (or `mix-blend-mode: multiply`), light as value steps, depth as overlap and seams. The idea survives; the cliché doesn't.

## 3. Write the laws

Translate the genes into **five to seven laws**, short, absolute, testable constraints. Laws are what make a style recognisable, and constraints are what force invention.

Good laws are specific and checkable:
- "Color is pigment, never light: no glows, no gradients, no transparency over color."
- "Only two type sizes per screen. Hierarchy comes from weight and position."
- "Every edge that meets another surface shows a 1px seam in `ink-30`. Joints are visible."
- "One full-bleed color field per view; everything else sits on paper."
- "Nothing moves unless the user moved it. State changes are cuts, not tweens."

Bad laws are vague ("clean and modern", "use whitespace"), a reader could not tell whether a screen obeys them.

Each law traces back to a gene. Write the source next to it; this is how the designer learns their own lineage.

## 4. Name it

Give the style a name that evokes its laws, not its category. "Ledger & Lamp", "Wet Ink Grid", "Quiet Machine". Never "Modern Minimal", "Clean SaaS", or a movement name with "neo-" in front.

## 5. Distance check

Score the new style on the 12 axes, then:

```bash
python3 <skill-dir>/scripts/atlas_match.py --vector "<style vector>" --include-trends --top 5
```

- **Nearest atlas card at distance < 3** → *inspect*, don't react mechanically. A close vector means the overall feeling resembles that source; it is a problem only if the style also reuses that source's recognisable genes (its grid, its signature form, its palette logic). If it does, push the Voice gene harder or swap the Accent. If the resemblance is only in mood, note it and move on, never swap a typeface or color just to move a number.
- **Any trend with saturation ≥ 7 within distance 6** (the script prints a WARNING) → drifting toward slop. Identify which law pulls it there and change it.
- **Distance from the person's own DNA > 9** → this is no longer their style. Pull the Spine closer.

Also check by eye against `atlas/trends/_saturation-map.md`: does any law accidentally recreate a trend surface?

## 6. Codify

Choose type with `references/typography.md` (derive from genes; check § 4 Model defaults). Size every frame, target and breakpoint from `references/dimensions.md`. Then fill `templates/style-spec.md` completely: tokens (color with light/dark, type, shape, spacing), layout grammar, icons (`references/icons.md`), motion (`references/motion.md`), signature moves, slop tells specific to *this* style, Figma variables, CSS/Tailwind tokens.

Contrast-check every text/background token pair (WCAG 2.2 AA: 4.5:1 body, 3:1 large text and UI components). An original palette that fails contrast is not finished.

Save to `~/.design-atelier/profiles/<slug>/styles/<style-slug>.md`, then record the sources so the next blend reaches further:

```bash
python3 <skill-dir>/scripts/atlas_match.py --record <spine-id>,<voice-id>,<accent-id>
```

## 7. Specimen

Prove the style on one specimen before applying it anywhere: a single page containing a hero/header with real imagery (photograph or illustration made for this style, `references/imagery.md`), body text, a card with an image, a form with error state, a data table or list, buttons in all states, a drawn icon set (`references/icons.md`, checked with `scripts/icon_check.py`), one empty state with a spot illustration, and one motion moment. Build it via `references/web.md` (or `figma.md`). Then critique the specimen against each law, fix, and only then show it.

Check numeric laws in code, both sides of the rule: if a law says "space between groups ≥ 3× space inside", list every gap pair in the CSS and confirm each one, not just the hero. A law the specimen breaks is either fixed or rewritten, never left.

The specimen is where a style stops being words. Most problems appear here.

## Three directions

When the person has not chosen a style, present three directions as **style boards** (`assets/style-board.html`), side by side and at equal depth. Defining the style is the deliverable; a product page comes after the choice.

Make them genuinely different. Keep the Spine if there is real evidence of who the person is; otherwise vary it too. Each board needs its own Voice and Accent genes, and the set must differ in at least two of: palette family, type classification, composition logic, imagery treatment. Build at least one board from a FAR source (`atlas_match.py --vary`). Check each board against `atlas/trends/_saturation-map.md` and the model-default lists; a board that lands on a familiar look (cream page, sepia photos, editorial serif) is replaced, not polished.

For each direction:

```
### [Name]
Laws: 1. … 2. … 3. … 4. … 5. …
Genes: Spine, [gene] ([source id]) · Voice, [gene] ([source id]) · Accent, [gene] ([source id]) · Personal, [gene]
Tokens: palette [4 to 5 hex] · type [display / text] · shape [radius, border, depth]
Feels like: one sentence a non-designer would understand.
Risk: the one way this direction could go wrong.
```

Fill one board per direction in `assets/style-board.html` (copy it to the project). Every board shows the same slots at real size, so the person compares styles, not layouts: hero composition, type pair in real copy, palette with roles, imagery treatment (a real photo graded to the style, or an illustration drawn for it), four icons from the style's set, a button and a card, five laws, and gene sources named plainly. Render the boards and look at them before showing them.

Then ask: pick one, merge two (say which parts), or reject all and say why. A rejection is useful data, record it in the journal.
