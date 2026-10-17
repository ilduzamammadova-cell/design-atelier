---
id: laws-of-ux
name: Laws of UX
type: principle
discipline: [ux, ui]
era: compiled 2017–2018 onward (laws dating from 1920s–1990s)
origin: USA
lineage: [gestalt-principles, fitts-and-hicks-laws, jakob-nielsen]
tags:
  mood: [evidence-based, clear, efficient, considerate]
  topics: [checkout, onboarding, forms, performance, any digital product]
axes: {order: 7, density: 4, ornament: 1, warmth: 5, contrast: 5, geometry: 5, chroma: 4, typevoice: 3, energy: 3, hand: 1, play: 3, era: 5}
---

# Laws of UX

**Essence:** A compact canon of psychological findings — about speed, memory, attention and motivation — turned into rules of thumb that make interfaces feel fast, memorable and humane. (Gestalt, Fitts/Hick and Jakob's Law have their own cards; this card holds the rest.)

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Doherty threshold | Productivity soars when system response stays under about 400ms (Doherty & Thadani, IBM, 1982) | Optimistic UI for saves, likes and moves; skeletons appear only after 400ms (avoids flash); anything longer shows determinate progress; perceived speed budget written into specs |
| G2 · Tesler's law | Every task has irreducible complexity; the only question is who carries it — the system or the user | Absorb complexity in the product: address autocomplete, auto-detected file formats, timezone inference, smart defaults; never push parsing or conversion onto the user |
| G3 · Peak–end rule | People judge an experience mostly by its most intense moment and its ending (Kahneman et al., 1993) | Design the completion screen as carefully as the start: clear summary, what happens next, one useful action; never end a flow on an upsell, an error or a survey wall |
| G4 · Von Restorff effect | The one item that differs is the one remembered | One accent element per view; the primary call to action is the only thing in the accent colour; never two "highlighted" plans or badges competing |
| G5 · Goal-gradient and Zeigarnik | Effort rises as the goal nears; unfinished tasks stay in mind | Setup checklists show completed steps first and remaining ones honestly (no fake pre-filled progress); "2 steps left" copy near the end; resumable drafts visibly waiting |
| G6 · Postel's law | Be liberal in what you accept and conservative in what you send | Inputs accept any reasonable format (spaces in card numbers, +44 or 0 prefixes, any date order with confirmation); outputs are always formatted consistently |

## Visual facts

- **Color:** neutral systems with a single unmistakable accent (G4).
- **Type:** clear hierarchy so that chunked information scans quickly; numbers grouped (card numbers in 4s, codes in 3s) for memory.
- **Form:** progress indicators, checklists, skeleton states, inline validation.
- **Composition:** linear flows with a designed ending; one focal action per step.

## Attitude

Jon Yablonski gathered these findings on lawsofux.com and in *Laws of UX* (O'Reilly, 2020; 2nd ed. 2024) so designers could ground decisions in psychology rather than taste. They are heuristics, not physics: Miller's "seven plus or minus two" concerns short-term memory, not a cap on menu items, and the aesthetic–usability effect warns that beauty can hide problems in testing. The same laws can be weaponised, so they come with an ethical duty.

## Blends

- **Amplifies:** `jakob-nielsen`, `microinteractions`, `progressive-disclosure` — evidence, feedback and staged complexity.
- **Productive tension with:** `bret-victor` — laws optimise known patterns, Victor invents new media; together: novel interfaces tested against human limits.
- **Clashes with:** `dark-patterns` — goal-gradient, scarcity and peak–end used against the user become manipulation.

## Don't copy

The lawsofux.com illustrations, posters and card-deck artwork. Cite the original research and draw your own.

## Study

- Jon Yablonski, *Laws of UX* (O'Reilly, 2020; 2nd ed. 2024); https://lawsofux.com
- W. J. Doherty & A. J. Thadani, "The Economic Value of Rapid Response Time" (IBM, 1982)
- D. Kahneman et al., "When More Pain Is Preferred to Less" (*Psychological Science*, 1993)
- G. A. Miller, "The Magical Number Seven, Plus or Minus Two" (1956)
- M. Kurosu & K. Kashimura, aesthetic–usability study (CHI 1995)
