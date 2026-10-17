---
id: gestalt-principles
name: Gestalt Principles of Perception
type: principle
discipline: [ux, ui, graphic]
era: 1910s–1930s (Berlin school); extended 1990s
origin: Berlin and Frankfurt, Germany
lineage: []
tags:
  mood: [ordered, legible, quiet, coherent]
  topics: [dashboards, forms, settings, data-heavy apps, navigation]
axes: {order: 7, density: 5, ornament: 1, warmth: 4, contrast: 5, geometry: 6, chroma: 3, typevoice: 3, energy: 3, hand: 2, play: 3, era: 5}
---

# Gestalt Principles of Perception

**Essence:** The eye groups before it reads, so layout is the art of arranging what perception will do anyway: space, likeness, alignment and shared motion carry meaning before a single word is parsed.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Space is the divider | Proximity: items close together read as one unit, faster and more reliably than boxes or rules | Two spacing tokens do the grouping: inside a group 8px, between groups at least 24px (ratio ≥ 3:1). Label sits 4–6px above its field. Delete dividers and card borders wherever the gap already separates |
| G2 · One shared plane | Common region (Palmer, 1992): a shared background binds items even when spacing is equal | When space is not enough, use a single tinted surface (one tonal step off the page). Never border + shadow + tint together; never nest regions more than two deep |
| G3 · Likeness means sameness | Similarity: things that look alike are assumed to act alike | One visual treatment per interactive role. Link colour is reserved for things that navigate and never used for emphasis; every destructive action shares one red; non-interactive text never borrows a control style |
| G4 · One figure per moment | Figure–ground: perception settles on one figure and lets the rest recede | Each screen state has exactly one focal layer. Sheets and dialogs dim the ground to ~50% and stop it from moving; selected rows rise by value, not by adding a border |
| G5 · Lines of travel | Continuity and alignment: elements on a common path read as a sequence | Max 2–3 vertical alignment axes per screen. Steppers, timelines and breadcrumbs sit on one baseline; a card peeking 16–24px past the viewport edge signals "more this way" |
| G6 · Move together, belong together | Common fate: elements sharing direction and timing are seen as a group | Grouped items animate with the same easing, duration and direction; multi-selected items lift together; unrelated elements never animate in the same beat |

## Visual facts

- **Color:** neutral by necessity; colour is spent on role (G3), not decoration. A typical result: grey scale plus one accent and one danger hue.
- **Type:** recedes; hierarchy comes from spacing and weight more than from size jumps.
- **Form:** few strokes, few boxes; grouping is carried by gaps and tonal planes.
- **Composition:** clusters separated by deliberate air; strong shared left edges; one clear focal layer.

## Attitude

The Berlin school (Wertheimer, Koffka, Köhler) argued that we perceive organised wholes, not piles of sensations. For a designer this turns layout into honesty: if two things are related, they must look related, and if they are not, perception must be allowed to pull them apart. Later researchers added common region and uniform connectedness, which is why the principle set keeps growing rather than ossifying.

## Blends

- **Amplifies:** `swiss-international`, `josef-muller-brockmann`, `edward-tufte` — grid discipline and data-ink thinking are applied Gestalt.
- **Productive tension with:** `deconstructivist-type` — deliberately breaking grouping in one hero zone, while the working UI obeys it, creates designed friction instead of noise.
- **Clashes with:** `brutalism` (web brutalism) — raw stacking that ignores grouping mixed with careful grouping reads as neither rigorous nor raw.

## Don't copy

No single artifact belongs to the theory, but avoid the clichés: the Rubin vase, Kanizsa triangle and dot-grid demos used as decoration, and the illustrated principle cards sold by lawsofux.com or NN/g. Take the perceptual rule, not someone's diagram of it.

## Study

- Max Wertheimer, "Laws of Organization in Perceptual Forms" (1923; English in W. D. Ellis, *A Source Book of Gestalt Psychology*, 1938)
- Kurt Koffka, *Principles of Gestalt Psychology* (1935); Rudolf Arnheim, *Art and Visual Perception* (1954)
- Stephen Palmer, common region (1992) and, with Irvin Rock, uniform connectedness (1994); *Vision Science* (1999)
- Jeff Johnson, *Designing with the Mind in Mind* (3rd ed., 2020)
- Nielsen Norman Group articles on proximity, similarity and common region: https://www.nngroup.com/topic/visual-design/
