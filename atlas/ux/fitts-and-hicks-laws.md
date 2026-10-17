---
id: fitts-and-hicks-laws
name: Fitts's Law and the Hick–Hyman Law
type: principle
discipline: [ux, ui, product]
era: 1952–1954 (applied to pointing devices from 1978)
origin: Columbus, Ohio, USA (Fitts) and Cambridge, UK (Hick)
lineage: []
tags:
  mood: [efficient, physical, direct, decisive]
  topics: [mobile apps, toolbars, checkout, kiosks, games, pro tools]
axes: {order: 7, density: 4, ornament: 1, warmth: 3, contrast: 6, geometry: 7, chroma: 4, typevoice: 3, energy: 4, hand: 1, play: 2, era: 5}
---

# Fitts's Law and the Hick–Hyman Law

**Essence:** Interaction is bodily work with a measurable cost: reaching a target costs more the farther and smaller it is, and choosing costs more the more options compete — so good layout spends the user's milliseconds like money.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Big and near | Fitts (1954): movement time grows with distance and shrinks with target width (a logarithmic trade-off) | Touch targets ≥ 44×44pt (iOS) / 48dp (Android); never below WCAG 2.2's 24×24 CSS px minimum. The primary action is the largest target and sits nearest the resting thumb or cursor |
| G2 · Edges are infinite | A pointer stops at the screen edge, so edge and corner targets are effectively endless in one direction | Pin global menus and toolbars to the screen edge with zero inset hit area; put the most frequent desktop commands in corners; on phones, keep primary navigation and the main action in the bottom third |
| G3 · Act where you look | Distance is the expensive term, so bring commands to the object instead of sending the hand to a distant toolbar | Contextual toolbar appears 8px from the current selection; right-click and long-press menus open at the pointer; radial menus place every option at equal distance |
| G4 · Choice is cheap only when sorted | Hick–Hyman (1952–53): decision time grows with the log of the number of equally likely options — when the user can subdivide them | ≤ 5–7 unsorted top-level actions. Longer sets are alphabetised or grouped and always type-to-filter; never present an unordered list of 20 choices |
| G5 · A default ends the debate | Unequal probabilities speed decisions; a recommended path removes most of the choice cost | One primary button per view, visually dominant; pre-select the most common safe option; mark the recommended plan rather than presenting tiers as equals |
| G6 · Danger is far and small | Inverse Fitts: what should be rare should be hard to hit by accident | Destructive actions are never adjacent to frequent ones — at least one full target width of space, different shape or colour, often one level deeper (overflow menu) |

## Visual facts

- **Color:** usually a strong accent for the one primary target and quiet neutrals elsewhere, because hierarchy of colour reinforces hierarchy of reach.
- **Type:** labels sized for the target, often 15–17px on touch; type never shrinks to fit more buttons.
- **Form:** generous hit areas (padding counts as target), full-width mobile buttons, bottom sheets, floating action points.
- **Composition:** frequency maps to proximity — the most used things gravitate to edges, corners and thumb zones.

## Attitude

Paul Fitts studied pilots' hands; William Hick and Ray Hyman studied reaction time. When Card, English and Burr tested the mouse at Xerox PARC (1978), Fitts's law fit it closely, and the HCI field gained its first quantitative design rule. The belief underneath: comfort is measurable, and a designer's taste must answer to the user's body.

## Blends

- **Amplifies:** `jef-raskin`, `progressive-disclosure`, `universal-design` — efficiency, staged choice and physical accessibility point the same way.
- **Productive tension with:** `edward-tufte` — dense small-multiple displays combined with large invisible hit zones give information density without tiny targets.
- **Clashes with:** `postmodern-new-wave` — scattered, layered, tiny typographic targets make a layout impossible to operate; keep that energy for non-interactive zones.

## Don't copy

No visual artifacts to protect, but avoid lifting specific researchers' charts (Steven Hoober's thumb-zone heat maps, MacKenzie's plots) as UI decoration. Measure your own targets.

## Study

- P. M. Fitts, "The information capacity of the human motor system in controlling the amplitude of movement" (*Journal of Experimental Psychology*, 1954)
- W. E. Hick, "On the rate of gain of information" (1952); R. Hyman, "Stimulus information as a determinant of reaction time" (1953)
- S. Card, W. English, B. Burr, mouse vs. other devices study (*Ergonomics*, 1978)
- I. Scott MacKenzie, "Fitts' law as a research and design tool in HCI" (1992)
- W3C WCAG 2.2, SC 2.5.8 Target Size (Minimum): https://www.w3.org/TR/WCAG22/
