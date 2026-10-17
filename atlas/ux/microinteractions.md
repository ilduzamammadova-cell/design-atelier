---
id: microinteractions
name: Microinteractions
type: principle
discipline: [ux, ui]
era: 2013–present
origin: San Francisco, California, USA
lineage: [don-norman]
tags:
  mood: [precise, responsive, crafted, tactile, witty]
  topics: [mobile apps, devices, settings, form inputs, consumer software, wearables]
axes: {order: 6, density: 3, ornament: 2, warmth: 6, contrast: 5, geometry: 5, chroma: 5, typevoice: 3, energy: 5, hand: 2, play: 6, era: 6}
---

# Microinteractions

**Essence:** Products are judged by their smallest moments — a toggle, a save, a refresh — so each single-purpose interaction deserves deliberate design of what starts it, how it behaves, how it answers, and how it changes over time.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Four-part anatomy | Dan Saffer (2013): trigger → rules → feedback → loops & modes | Every small feature is specified in four lines: what starts it (user or system), what it does and doesn't allow, how it reports, and how it behaves over repeated use; reviews check all four |
| G2 · The trigger shows the data | A trigger can display state before it is touched | Buttons carry their state: a download button fills with progress then becomes "Open"; a bell shows the count; a toggle's label states the current value; tabs show unread dots |
| G3 · Don't start from zero | Use what is already known to make the first use smarter | Remember the last choice; prefill by context (location, time, previous order); the first-time state is tailored, not empty |
| G4 · Feedback where the action is | Feedback should appear at the point of the trigger, proportional to the action | Response within 100ms at the control itself; micro-motion 150–250ms ease-out; a haptic tick for toggles; never a modal or page change to confirm a micro-action |
| G5 · Rules made visible by constraint | Users learn rules from feedback and limits, not instructions | Password rules shown as live ticks while typing; sliders snap to valid steps; impossible next states disabled; character counters appear near the limit, not from the start |
| G6 · Long loops | Behaviour can evolve with use | Hints show for the first 2–3 uses, then disappear; frequently used options rise; labels can shorten to icons after the user demonstrates familiarity |

## Visual facts

- **Color:** state changes carried by small colour shifts on the control itself (fill, ring, icon tint); one success hue, one error hue.
- **Type:** tiny, precise status text beside controls ("Saved", "Copied") that fades after 1.5–2s.
- **Form:** morphing icons (menu → close, play → pause), progress inside buttons, springy but brief motion.
- **Composition:** feedback co-located with its trigger; nothing jumps across the screen to report a small event.

## Attitude

Saffer, an interaction designer who worked at Smart Design, argued in *Microinteractions: Designing with Details* (O'Reilly, 2013) that features are built from micro-moments and that a single well-made one can become a product's signature — as pull-to-refresh, introduced by Loren Brichter in his Tweetie app, became a platform convention. The belief: care in the details is where users feel respect.

## Blends

- **Amplifies:** `don-norman`, `kano-model`, `persuasive-technology` (ethical use) — feedback, delight and celebration done right.
- **Productive tension with:** `calm-technology` — forcing expressive feedback down to whisper level yields precise, tiny, satisfying cues.
- **Clashes with:** `psychedelic` — constant motion everywhere destroys the signal value of feedback.

## Don't copy

Branded signature moments: a specific social network's like-heart burst, Apple's slide-to-unlock, Tweetie's exact pull-to-refresh animation and sound, any app mascot's celebration. Invent your own signature moment.

## Study

- Dan Saffer, *Microinteractions: Designing with Details* (O'Reilly, 2013); https://microinteractions.com
- Dan Saffer, *Designing for Interaction* (2006; 2nd ed. 2009)
- Val Head, *Designing Interface Animation* (Rosenfeld, 2016)
