# Style DNA Axes

Twelve axes describe any visual sensibility, a designer's taste, a master's work, a movement, a trend, or a finished style. The same vector format is used everywhere, so a person's profile can be matched against the atlas numerically (`scripts/atlas_match.py`).

Each axis runs 0 to 10. Score what the work *feels like*, not what it is made of. A 5 means "balanced / not a defining trait", not "unknown". If an axis truly does not apply (rare, mostly UX cards), use 5.

| # | Axis | 0 means | 10 means | Anchors (0 · 5 · 10) |
|---|---|---|---|---|
| 1 | `order` | intuitive, free placement | strict system, everything on a grid | Carson · Paul Rand · Müller-Brockmann |
| 2 | `density` | sparse, lots of air | packed, information-rich | Kenya Hara · Swiss poster · Victorian broadsheet / Bloomberg Terminal |
| 3 | `ornament` | bare, nothing decorative | heavily decorated, pattern on pattern | Dieter Rams · Art Deco · Art Nouveau / William Morris wallpaper |
| 4 | `warmth` | cool, clinical, technical | warm, human, intimate | Wim Crouwel · Pentagram · Matisse cut-outs |
| 5 | `contrast` | soft, tonal, low contrast | stark, extreme contrast of scale/value | Morandi · Bauhaus · Russian Constructivism |
| 6 | `geometry` | organic, fluid, hand-curved | hard-edged, geometric, ruled | Art Nouveau · Saul Bass · De Stijl |
| 7 | `chroma` | monochrome or muted | saturated, many colors | Agnes Martin · Push Pin · Memphis |
| 8 | `typevoice` | type recedes, neutral carrier | type *is* the image | Muji · Vignelli · Paula Scher / Emigre |
| 9 | `energy` | still, calm, static | kinetic, agitated, diagonal, loud | Agnes Martin · Swiss · Futurism / Carson |
| 10 | `hand` | machine-precise, digital-clean | handmade, textured, imperfect | Apple · Push Pin · Basquiat / risograph zines |
| 11 | `play` | grave, serious, institutional | playful, witty, ironic | Swiss federal forms · Paul Rand · Memphis / Sagmeister |
| 12 | `era` | rooted in tradition, nostalgic | futurist, forward-looking | Kelmscott Press · Bauhaus · Y2K chrome / speculative UI |

## How to score

- Score against the anchors, not against personal preference. Two people scoring the same master should land within ±1.
- Extremes (0 to 1, 9 to 10) are rare and meaningful, use them only for defining traits.
- A movement's vector is its center of gravity; individual members may deviate.

## Vector notation

In card front matter, use a YAML flow map with all twelve keys in this order:

```yaml
axes: {order: 9, density: 5, ornament: 1, warmth: 3, contrast: 7, geometry: 9, chroma: 4, typevoice: 6, energy: 5, hand: 1, play: 2, era: 6}
```

## Reading a vector

- **Distance** between two vectors (Euclidean) = how different two sensibilities are. Close masters reinforce each other; distant masters create tension.
- **Novelty** comes from combining genes whose sources are far apart on 2 to 3 axes while agreeing on the rest. Total disagreement produces noise; total agreement produces a copy.
