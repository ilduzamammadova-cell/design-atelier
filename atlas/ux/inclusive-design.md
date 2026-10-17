---
id: inclusive-design
name: Inclusive Design
type: principle
discipline: [ux, ui, product]
era: 1990s to present (Microsoft toolkit mid-2010s)
origin: Toronto, Canada / Redmond, Washington, USA
lineage: [universal-design]
tags:
  mood: [humane, flexible, welcoming, adaptable, clear]
  topics: [public services, education, health, consumer apps, gaming, media]
axes: {order: 6, density: 4, ornament: 1, warmth: 8, contrast: 7, geometry: 5, chroma: 5, typevoice: 4, energy: 3, hand: 3, play: 4, era: 6}
---

# Inclusive Design

**Essence:** Exclusion is a mismatch between a person and a design, not a property of the person, so design with people at the margins, solve for one, and the result works better for many.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Persona spectrum | Microsoft's toolkit maps a permanent disability to temporary and situational versions (one arm → arm injury → holding a baby) | Every core flow is completable with one thumb, with keyboard only, and with a screen reader; primary actions within one-handed reach; voice and keyboard parity tested each release |
| G2 · Solve for one, extend to many | Designing for a specific excluded person yields features everyone ends up using (captions in a noisy bar) | Captions on by default for autoplaying video; transcripts for audio; a high-contrast theme shipped as a first-class theme, not a hidden setting |
| G3 · Recognise exclusion | Exclusion happens when designers solve with their own abilities and biases as the default | Audit each flow for single-modality requirements (drag-only, colour-only, audio-only, time-limited) and add an alternative path for each |
| G4 · Honour the person's settings | People already told the system what they need | Respect `prefers-reduced-motion`, `prefers-contrast`, `prefers-color-scheme` and OS text size; layouts reflow cleanly at 200% text and 320px width; never lock zoom |
| G5 · Learn from diversity | Co-design with people who experience exclusion; treat their adaptations as innovation | Name fields accept any script and a single name; gender optional and free-text; recruit at least one participant with a disability in every usability round |
| G6 · Pace belongs to the person | Time pressure excludes people who read, move or process differently | No auto-advancing carousels; timeouts warn and extend; animations pausable; long forms save progress automatically |

## Visual facts

- **Color:** text contrast ≥ 4.5:1 (WCAG AA), UI components ≥ 3:1; state never carried by colour alone. Example: text #1B1B1F on #FFFFFF, accent #0B57D0.
- **Type:** body 16 to 18px minimum, generous line height (1.5); Atkinson Hyperlegible (Braille Institute, free) or Lexend; clear distinction of I/l/1 and O/0.
- **Form:** visible 2 to 3px focus rings with offset; large, clearly bounded targets; icons always paired with text labels.
- **Composition:** single-column flows that reflow; predictable placement; no hover-only content.

## Attitude

The Inclusive Design Research Centre (Jutta Treviranus, Toronto, from 1993) framed inclusion as designing for human diversity in all its variety. Kat Holmes led Microsoft's inclusive design work and its toolkit, whose three principles are recognise exclusion, learn from diversity, solve for one and extend to many; her book *Mismatch* (2018) argues that disability arises from mismatched interactions. Products like the Xbox Adaptive Controller (2018) showed the approach at mainstream scale.

## Blends

- **Amplifies:** `universal-design`, `calm-technology`, `jakob-nielsen`, fit for all, low strain, convention.
- **Productive tension with:** `edward-tufte`, high density against large, scalable type; the result is dense layouts that reflow and zoom without breaking.
- **Clashes with:** `deconstructivist-type`, illegibility as an aesthetic excludes by design.

## Don't copy

Microsoft's Inclusive Design toolkit illustrations and activity cards, its persona spectrum graphic, and the Xbox Adaptive Controller's industrial design. Build your own spectrum from your own research.

## Study

- Kat Holmes, *Mismatch: How Inclusion Shapes Design* (MIT Press, 2018)
- Microsoft Inclusive Design toolkit: https://inclusive.microsoft.design
- Inclusive Design Research Centre, OCAD University: https://idrc.ocadu.ca
- W3C, Web Content Accessibility Guidelines (WCAG) 2.2 (2023): https://www.w3.org/TR/WCAG22/
- Heydon Pickering, *Inclusive Design Patterns* (2016); Sara Hendren, *What Can a Body Do?* (2020)
