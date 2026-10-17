---
id: trajan
name: Trajan
type: typeface
discipline: [graphic, ui]
era: 1989 (model: inscription of AD 113)
origin: California, USA (Adobe); model in Rome, Italy
lineage: []
tags:
  mood: [monumental, solemn, classical, epic]
  topics: [film, institutions, memorials, luxury, heritage]
axes: {order: 8, density: 2, ornament: 2, warmth: 4, contrast: 4, geometry: 6, chroma: 1, typevoice: 7, energy: 2, hand: 3, play: 1, era: 1}
---

# Trajan

**Essence:** Roman imperial capitals turned into a font. The proportions are carved for stone and eternity, which is why the face fits monuments, and why it became cinema's shorthand for "important".

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Capitals only | Monumental Roman inscriptions had no lowercase, so Trajan offers capitals and small caps and nothing else. | Titles ≤ 5 words, letterspaced +8 to 15%; never sentences or paragraphs. Pair with a full lowercase text face for everything readable. |
| G2 · Proportion classes | Roman capitals vary in width by design: round and wide letters (*O, C, D, M*) beside narrow ones (*E, F, L, S*), so spacing has to be judged by eye. | In letterspaced caps, kern optically: start from `font-kerning: normal`, then hand-tune pairs like *LA, AV, TO* in wordmarks and hero titles. Equal tracking alone is never enough. |
| G3 · Lettering as architecture | The source inscription is part of a building; letters, margins and the stone plane form one composition. | Ceremony surfaces (memorial pages, awards, certificates, donor walls): caps centred on a vertical axis, line spacing ≥ 1.6× cap height, margins ≥ 15% of width, and a single flat plane behind with no gradients. |
| G4 · Monument becomes cliché | From 1992, film posters adopted it so widely that by the 2000s it was the default "prestige drama" voice. | Run a cliché test before shipping: if the title looks like a 1990s movie poster, change one variable, such as a different weight (Trajan Pro 3 light) or Roman proportions carried by another face. |

## Visual facts

- **Classification:** inscriptional / glyphic Roman capitals (titling).
- **Origin:** Carol Twombly, Adobe, 1989, adapted from the inscription at the base of Trajan's Column, Rome (AD 113). The digital release added a bold weight, which the Romans never had.
- **Main digital versions:** Trajan Pro (OpenType, small caps and Central European support). Trajan Pro 3 (2012, revised by Robert Slimbach: six weights plus Greek and Cyrillic). Trajan Sans companion. All commercial (Adobe).
- **Anatomy:** capitals only, classical width classes, modest stroke contrast, sharp bracketed serifs, generous proportions.
- **Free / open alternatives:** Cinzel (Natanael Gama, OFL; first-century inscription proportions, three weights plus Decorative). Marcellus SC (Astigmatic, OFL; a flared, inscription-inspired titling style).

## Attitude

The source letters were made to outlast an empire. They carry authority by proportion, not by ornament. Borrowing them means borrowing permanence, so the occasion must deserve it.

## Using it today

- **Signals:** film posters from the early 1990s (*The Bodyguard*, *Scent of a Woman*, 1992, and many after), TV dramas, book covers, universities and wineries. It is extremely saturated: the face now reads as "epic drama, circa 1995" more than as Rome.
- **Robotic ↔ humane: 5/10.** Varied widths and stroke modulation from the brush and chisel are human. The monumental formality and all-caps distance are not intimate.
- **UI fitness:** display only, as caps ≥ 18px with tracking. Small-cap navigation is possible ≥ 13px for very short labels. Never body, never form fields. Coverage: Trajan Pro 3 has Latin, Greek and Cyrillic.
- **Pairs with:** a Renaissance lowercase text face (EB Garamond): Roman capitals with humanist minuscules, the historical marriage. Optima for UI and subheads, since both descend from inscriptional letters. A quiet neutral sans for controls.

## Blends

- **Amplifies:** `optima`: inscriptional capitals and their sans-serif descendant share proportions.
- **Productive tension with:** `punk-graphics`: imperial capitals on xerox grit and collage give authority under attack, which is useful for activism.
- **Clashes with:** `memphis`: monumental gravity beside squiggles and confetti cancels both.

## Don't copy

Trajan outlines without an Adobe licence; specific film poster title treatments; photographic tracings of the column inscription sold as a font.

## Study

- Edward M. Catich, *The Origin of the Serif* (1968): how brush and chisel shaped these letters.
- Adobe, Trajan Pro 3 specimen (blog.typekit.com, 2013 PDF).
- The A.V. Club, "Here's how a single font came to dominate movie posters" (2018).
- Cinzel specimen: fonts.google.com/specimen/Cinzel
