---
id: conversational-and-ai-ux
name: Conversational and AI / Agent UX
type: system
discipline: [ux, ui]
era: 2019–present (LLM and agent patterns 2023–2026; roots in 1960s chatbots)
origin: USA (Microsoft Research, Google PAIR, independent pattern libraries)
lineage: [ben-shneiderman, progressive-disclosure, jakob-nielsen]
tags:
  mood: [conversational, transparent, collaborative, provisional, steerable]
  topics: [assistants, agents, copilots, search, creative tools, customer support, coding tools]
axes: {order: 5, density: 4, ornament: 1, warmth: 7, contrast: 4, geometry: 4, chroma: 3, typevoice: 5, energy: 4, hand: 2, play: 4, era: 9}
---

# Conversational and AI / Agent UX

**Essence:** A probabilistic collaborator must be legible and steerable: say what it can do, show its work, ask before consequential acts, stop when told, accept correction gracefully — and hand precise work back to direct manipulation.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Set expectations, identify the AI | Microsoft's Human-AI guidelines (Amershi et al., CHI 2019) open with: make clear what the system can do and how well | Empty state shows 3–4 example requests spanning real capability; a plain capability line ("Can search the web · Can't send email without asking"); AI-made content labelled; memory and data use disclosed with an incognito option |
| G2 · Show work, collapsed by default | Streaming output plus inspectable reasoning and sources build calibrated trust | Answers stream token by token; tool calls and steps collapse into one summary row ("Searched 6 sources · 40s") that expands; claims carry numbered inline citations linking to sources |
| G3 · Plan → approve → act | Consequential agent actions need a reviewable plan and a human checkpoint | Agent presents a numbered plan with predicted effects; reversible steps run with undo; irreversible ones (send, pay, delete, publish) pause for explicit approval naming the exact object |
| G4 · Always interruptible | People must be able to stop or redirect a running system at any moment | While generating, Send becomes Stop in the same spot; new messages can be queued or interject mid-run; the user can edit the plan and the agent resumes from there |
| G5 · Efficient correction and dismissal | When AI is wrong (it will be), fixing it must be cheaper than starting over | Inline edit of any output; regenerate one section, not all; Esc dismisses suggestions; feedback is granular (this sentence, this source) rather than a single thumbs-down |
| G6 · Intent in words, precision in widgets | AI enables intent-based outcome specification (Nielsen, 2023), but words are poor at fine adjustment | The conversation produces a structured artifact (table, form, canvas, slider set) that the user manipulates directly; never make people type what a slider does better |

## Visual facts

- **Color:** soft neutral surfaces, low-chroma; a single accent for the user's turn or for actionable proposals; avoid the overused "AI gradient" and sparkle-as-brand.
- **Type:** comfortable reading measure (60–75 characters, ~680–760px column); a mono for tool output and code; system or humanist sans for prose.
- **Form:** message turns, collapsible step logs, citation chips, approval cards with explicit verbs, side-panel artifacts.
- **Composition:** conversation column plus an artifact pane; status and controls (Stop, model, permissions) fixed near the input.

## Attitude

The field learned early lessons from ELIZA (1966), which showed how readily people attribute understanding to a program, and from Microsoft's Office Assistant, which showed the cost of unrequested help. Google's People + AI Guidebook (2019) and pattern libraries such as Emily Campbell's Shape of AI (wayfinders, inputs, tuners, governors, trust builders, identifiers) codified the field; conversation design borrows Grice's cooperative maxims — say enough, say what is true, stay relevant, be clear. The governing belief: design for error, calibrated trust and human control.

## Blends

- **Amplifies:** `ben-shneiderman`, `progressive-disclosure`, `calm-technology` — human control, layered detail, low-interruption agents.
- **Productive tension with:** `bret-victor` — opaque generation against visible, manipulable models; push outputs to arrive as explorable structures.
- **Clashes with:** `persuasive-technology` — engagement-optimised companions (flattery, endless follow-up bait) corrode trust in the assistant's honesty.

## Don't copy

Any vendor's chat interface screen-for-screen, assistant logos and sparkle marks, named personas and avatars, and the Shape of AI illustrations (licensed CC BY-NC-SA, non-commercial). Take the interaction patterns, not the product skins.

## Study

- S. Amershi et al., "Guidelines for Human-AI Interaction" (CHI 2019): https://www.microsoft.com/en-us/research/project/guidelines-for-human-ai-interaction/
- Google PAIR, *People + AI Guidebook* (2019; updated 2021): https://pair.withgoogle.com/guidebook
- Emily Campbell, Shape of AI pattern library: https://www.shapeof.ai
- Jakob Nielsen, "AI: First New UI Paradigm in 60 Years" (NN/g, 2023)
- Erika Hall, *Conversational Design* (2018); Ben Shneiderman, *Human-Centered AI* (2022)
- Joseph Weizenbaum, *Computer Power and Human Reason* (1976)
