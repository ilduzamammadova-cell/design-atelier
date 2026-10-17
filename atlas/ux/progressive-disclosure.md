---
id: progressive-disclosure
name: Progressive Disclosure
type: principle
discipline: [ux, ui]
era: 1980s to present
origin: Yorktown Heights, New York, USA (IBM Watson Research Center)
lineage: []
tags:
  mood: [calm, layered, focused, unhurried]
  topics: [settings, pro tools, long forms, onboarding, AI agents, checkout]
axes: {order: 7, density: 3, ornament: 1, warmth: 5, contrast: 4, geometry: 5, chroma: 3, typevoice: 3, energy: 2, hand: 1, play: 3, era: 5}
---

# Progressive Disclosure

**Essence:** Show what most people need now, and let the rest unfold on request, complexity is welcome as long as it arrives in layers, at the moment it becomes relevant.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Two layers, rarely three | A primary layer covering the common case and one secondary layer; a third level signals a design problem | "Advanced" collapsed with a count ("Advanced · 6 options"); disclosure is never nested more than once; if a tertiary layer appears, the IA gets redesigned |
| G2 · Training wheels | Carroll and Carrithers (IBM, 1984) blocked advanced functions for new users and saw faster learning with fewer errors | New accounts start with a reduced command set that expands after first success or by a persistent "Show all features" switch; the expansion is announced once, not repeatedly |
| G3 · Disclose at the moment of relevance | Options mean most when the context that needs them exists | Contextual toolbars appear on selection; field-specific options appear after the field has a value; "more" controls reachable by keyboard focus, not hover alone |
| G4 · Strong scent on the trigger | Users open a disclosure only if its label predicts what's inside | Label the content, not the mechanism: "Shipping options (3)" instead of "More"; chevron direction matches the expansion; the collapsed row summarises current values ("Quality: Auto · 1080p") |
| G5 · Defaults carry the weight | Deferred options must be safe untouched, or disclosure becomes a trap | Every hidden option has a sensible default shown in the summary; nothing required lives behind a disclosure; validation errors inside a collapsed section force it open |
| G6 · Staged disclosure for rare, linear tasks | Wizards suit infrequent tasks with a fixed order; they punish frequent ones | Multi-step flows only for one-off setup: 3 to 5 fields per step, visible step count, Back that keeps entries; frequent tasks get one editable page instead |

## Visual facts

- **Color:** quiet; disclosure controls are secondary in weight (text buttons, subtle chevrons).
- **Type:** section summaries in a muted secondary style beneath the label.
- **Form:** accordions, disclosure triangles, "show more" rows, contextual popovers, collapsed reasoning blocks in AI tools ("Worked for 2 min · 6 steps").
- **Composition:** a short, calm first layer with clearly signposted depth beneath.

## Attitude

John Carroll's training-wheels and minimalist-instruction research at IBM gave early evidence for staging features; Jakob Nielsen later made progressive disclosure a household term in usability, and now applies it to long-running AI agents, whose steps must be summarised by default and inspectable on demand. The belief: attention is scarce, but people are capable, so stage the complexity rather than deleting it.

## Blends

- **Amplifies:** `calm-technology`, `alan-cooper`, `fitts-and-hicks-laws`, protected attention, perpetual intermediates, fewer choices at once.
- **Productive tension with:** `edward-tufte`, Tufte wants everything visible at once; the hybrid is a dense overview with detail drawers rather than hidden settings.
- **Clashes with:** `brutalism`, web brutalism's show-everything rawness and staged revelation cancel each other out.

## Don't copy

No signature artifact, but do not clone a platform's settings screens wholesale (e.g. a specific OS's preferences layout). Take the layering logic.

## Study

- J. M. Carroll & C. Carrithers, "Training Wheels in a User Interface" (*Communications of the ACM*, 1984)
- John M. Carroll, *The Nurnberg Funnel* (MIT Press, 1990)
- Jakob Nielsen, "Progressive Disclosure" (NN/g, 2006): https://www.nngroup.com/articles/progressive-disclosure/
- Jenifer Tidwell, Charles Brewer & Aynne Valencia, *Designing Interfaces* (3rd ed., 2020)
- Jakob Nielsen, "Progressive Disclosure: From Training Wheels to Week-Long AI Agents" (UX Tigers)
