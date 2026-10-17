---
id: islamic-calligraphy
name: Arabic-script calligraphy in the Islamic world
type: tradition
discipline: [graphic, art, architecture]
era: 7th century-present; proportioned scripts systematised 10th century (Ibn Muqla, refined by Ibn al-Bawwab and Yaqut al-Musta'simi)
origin: cross-regional: Arabian Peninsula, Iraq, Egypt, Maghreb, Anatolia, Iran, South Asia
lineage: []
tags:
  mood: [rhythmic, elevated, disciplined, fluent]
  topics: [publishing, culture, education, bilingual products, identity]
axes: {order: 8, density: 6, ornament: 7, warmth: 6, contrast: 7, geometry: 6, chroma: 3, typevoice: 10, energy: 6, hand: 8, play: 3, era: 2}
---

# Arabic-script calligraphy

**Essence:** Writing raised to the highest visual art, governed by proportions measured in the dot of the reed pen.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Proportion from the pen's dot | The proportioned script (al-khatt al-mansub) measures letters in rhombic dots made by the nib: the alif is a set number of dots tall, and a circle with the alif as diameter governs the other letters. | Derive the type and spacing scale from a stroke unit n (e.g. 8px): stem = n, x-height = 5n, line-height = 7n, paddings in multiples of n. Publish the unit as the root token. |
| G2 · Script registers by purpose | Kufic is angular and monumental, Naskh a clear book hand, Thuluth grand display, Nasta'liq sloped and poetic, Diwani a chancery hand, Maghribi the western tradition. | Define type roles by purpose, each with its own voice: display (grand, Thuluth-like), text (Naskh clarity), meta (geometric Kufic). Arabic UI fonts: Amiri, Noto Naskh Arabic, Reem Kufi, Aref Ruqaa, Noto Nastaliq Urdu. |
| G3 · Justify by stretching, not spacing | Lines are justified by lengthening letter connections (kashida) and reshaping words, never by spreading letters apart. | In Arabic layouts, never letterspace; use kashida-aware justification where the font supports it. In Latin layouts, borrow the idea: justify a headline by extending a rule or bar, not by tracking. |
| G4 · Square Kufic as pixel grid | Square Kufic builds letters from square units on an orthogonal grid, often laid in brick or tile. | Wordmarks and icon glyphs constructed on an 8×8 or 12×12 square grid; ideal for pixel, LED and small-size UI marks. Use only text you can read and verify. |
| G5 · Text as architectural band | Inscription bands frame doors, domes and borders; the text is ornament and message at once. | One static text band (a real, meaningful line, e.g. the product's principle) as a frame around a hero; legible size, no marquee motion. |
| G6 · Composition inside a shape | Calligraphers compose words into circles, mirrored pairs (müsenna) and monograms such as the Ottoman tughra. | Monogram construction: letters of a name stacked into a bounded shape for avatars and seals, keeping stroke contrast consistent. |

## Visual facts

- **Color:** carbon ink #141414 on burnished paper #EFE4C8; gold illumination #B8913A; lapis #26428B; white script on cobalt tile #1F4FA0.
- **Type:** see G2; Scheherazade New and Lateef (SIL) also strong for text.
- **Form:** modulated reed-pen strokes, diamond dots, sweeping descenders; vowel and decorative marks as a secondary layer.
- **Composition:** main text plus diacritic layer; margins with illumination; strict baselines or deliberate stacking.

## Attitude

Calligraphy carried revelation, so its craft was held in the highest esteem; masters certified students with an ijaza, a licence to sign. The same script writes Arabic, Persian, Urdu and other languages and serves poetry, law and commerce. Its lesson for designers: rigorous proportion and expressive freedom are not opposites.

## Blends

- **Amplifies:** `islamic-geometric-pattern`, script bands and geometric fields belong together.
- **Productive tension with:** `swiss-international`, bilingual Arabic-Latin systems where a modulated reed stroke meets a rational grotesk grid.
- **Clashes with:** `punk-graphics`, ransom-note cutting breaks letter joining and reads as disrespect.

## Don't copy

The Blue Qur'an (9th to 10th century); the tughra of Süleyman the Magnificent (Met); compositions by named calligraphers past and present (e.g. Hassan Massoudy, eL Seed).

## Respect

Qur'anic verses, the name of God, the name of the Prophet and the shahada must never be used decoratively, and never on floors, rugs, footwear, lower garments, disposable packaging or bathroom goods. In 1997 Nike recalled about 38,000 pairs of shoes because a flame logo resembled "Allah" in Arabic script. Never fake Arabic: letters must join and shape correctly right-to-left (many tools break this); have a fluent reader check every word. Caricature is Latin "Arabian" display fonts that bend letters into pseudo-script. Credit script style and calligrapher; remember Christians, Jews and secular writers also use the script.

## Study

- Sheila S. Blair, *Islamic Calligraphy* (2006)
- Huda Smitshuijzen AbiFarès, *Arabic Typography* (2001); Khatt Foundation (Amsterdam)
- Chester Beatty Library (Dublin); Aga Khan Museum (Toronto); British Library
- Met: the tughra of Süleyman the Magnificent
