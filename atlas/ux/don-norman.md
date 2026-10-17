---
id: don-norman
name: Don Norman
type: designer
discipline: [ux, product]
era: 1980s to present
origin: San Diego, California, USA
lineage: [gestalt-principles]
tags:
  mood: [clear, humane, explanatory, forgiving]
  topics: [physical products, appliances, enterprise software, onboarding, automotive, any interface]
axes: {order: 6, density: 4, ornament: 1, warmth: 6, contrast: 5, geometry: 5, chroma: 4, typevoice: 3, energy: 3, hand: 3, play: 4, era: 5}
---

# Don Norman

**Essence:** When people struggle with a thing, the thing is at fault, good design lets a newcomer discover what is possible, see what just happened and recover from the error that will certainly come.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Discoverable through signifiers | Discoverability: can a newcomer tell which actions exist, where and how? An affordance is a relationship (what a thing permits this person to do); a signifier is the perceivable cue that announces it. He added the second term because designers kept saying "affordance" when they meant a cue. A simple thing that needs a label or manual has failed | Still-screenshot test: with no hover and no tutorial, a first-timer can point to every action. No hover-only controls on touch; buttons have a fill or outline plus a verb; draggable rows show a grip; editable text shows a field edge; every swipe or long-press action also sits in a visible menu |
| G2 · Map, then constrain | Natural mapping lays controls out like the things they control (his four-burner stove). A good mapping is itself a logical constraint, alongside physical (fits one way only), semantic (the situation's meaning) and cultural (convention) ones. Forcing functions, interlock, lock-in, lockout, are the strongest constraint and annoy people in everyday use, so keep them for real danger | Controls sit on or beside what they change, in the same arrangement (row actions in the row; layer list ordered like the canvas stack; drag up = move up). Wrong input is made impossible, not reported (greyed dates, input masks, disabled options with a one-line reason). Interlock: Publish stays disabled and lists what is missing; lock-in: leaving keeps the draft; lockout: destructive admin behind a deliberate second step |
| G3 · Bridge both gulfs, stage by stage | Seven stages of action: a goal, three execution stages (plan, specify, perform) and three evaluation stages (perceive, interpret, compare). The gulf of execution is the gap between intention and the actions offered; the gulf of evaluation is the effort needed to work out the system's current state. Feedback must be immediate and informative, late or missing feedback makes people repeat commands and invent false causes | Walk each key screen as questions: what can I do, how, what happened, is that what I wanted? Acknowledge every input within 100ms; a pressed button goes busy and ignores repeats; show the resulting state in the user's terms ("Shared with 3 people" with avatars, not "Success"); long jobs show progress and stay cancellable; one prioritised message at a time, never a stack of toasts |
| G4 · Slips ≠ mistakes | Slips: right goal, wrong execution, a habitual routine captures the action, a similar-looking target gets hit, a mode changes what a gesture means. Mistakes: wrong goal or plan, from a wrong model or missing information. "Are you sure?" catches neither, because people confirm the action, not the object. Treat each error as an approximation of what the person meant | Classify every error seen in testing. Slips → make frequent and destructive controls look different and sit apart, remove or show modes, make actions reversible (trash with restore, undo, version history). Mistakes → preview the outcome before commit, name the object and consequence ("Delete 'Q3 invoices', 14 files"), and explain the model at the point of decision. Error messages say what happened and offer the next step |
| G5 · A truthful system image | Designer and user never talk directly: the user builds a mental model only from the system image, what the product shows, says and does, plus its docs. Knowledge in the world needs no learning but is slower; knowledge in the head is fast but must be learned. Make the *correct* things visible, or people invent wrong explanations | One honest overview of how the system works (where data lives, what syncs, what happens next, e.g. a sync panel drawn device → cloud → shared). Rarely used knowledge stays in the world (visible options, inline hints); frequent actions may move into the head (shortcuts printed beside menu items). Never show a cue that implies a false model (a cloud badge on files that are local only) |
| G6 · Design for the activity, with people | Designers are not typical users, and people's accounts of their own behaviour are after-the-fact rationalisations, so observe. Human-centred design iterates observe → ideate → prototype → test; the Double Diamond (UK Design Council, 2005), which he adopted, diverges and converges first on the right problem, then on the right solution. Activity-centred design serves the whole activity, not isolated tasks | Each feature spec opens with the activity it serves and its real task sequence; tools appear where that sequence needs them (export where the task ends, not in Settings). Test key flows with 3 to 5 real users per iteration; don't freeze the problem statement until observation has tested it |

## Visual facts

- **Color:** Norman has no visual signature; products built on his ideas use colour semantically, one success, one warning, one error hue, never decorative reuse.
- **Type:** label-forward; verbs on buttons ("Send invoice", not "OK"); object names inside confirmations.
- **Form:** visible edges on interactive things; depth and shading used only as signifiers; a visible state for everything that can change.
- **Composition:** controls placed by mapping, not by grid symmetry alone; layout follows the order of the activity.

## Attitude

Trained as a cognitive scientist, Norman argued that "human error" is usually design error, and his 1988 book made usability a public concern; he asked designers to assume every possible error will be made and to support the person rather than fight them. At Apple in the 1990s he took the title User Experience Architect, helping popularise the phrase. *Emotional Design* added that attractive things work better (visceral, behavioural, reflective levels); his recent work pushes toward humanity-centred, sustainable design.

## Blends

- **Amplifies:** `jakob-nielsen`, `steve-krug`, `microinteractions`, `the-mom-test`, evaluation, plainness, feedback, and evidence from what people actually do.
- **Productive tension with:** `dieter-rams`, minimal surfaces tend to hide signifiers; forcing Rams-level reduction to keep every signifier gives "flat but legible" products.
- **Clashes with:** `postmodern-new-wave`, ambiguity as an aesthetic goal fights mapping and clear system images in working UI.

## Don't copy

The cover of *The Design of Everyday Things* (Jacques Carelman's "coffeepot for masochists"), the much-shared "Norman door" photographs, and his stove, refrigerator-control and action-cycle diagrams reproduced as decoration.

## Study

- *The Psychology of Everyday Things* (1988), retitled *The Design of Everyday Things* for the paperback; the revised and expanded edition (2013) adds signifiers, the Double Diamond and design-thinking chapters
- "Human-Centered Design Considered Harmful" (*interactions*, 2005) and "Signifiers, Not Affordances" (*interactions*, 2008)
- *User Centered System Design* (ed. with Stephen Draper, 1986)
- *Emotional Design* (2004); *Living with Complexity* (2010); *Design for a Better World* (2023)
- Essays and archive: https://jnd.org · Nielsen Norman Group, co-founded with Jakob Nielsen in 1998: https://www.nngroup.com
