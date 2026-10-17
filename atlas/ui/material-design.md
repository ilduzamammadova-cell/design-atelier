---
id: material-design
name: Material Design (2014 → M3 → M3 Expressive)
type: system
discipline: [ui, ux]
era: 2014 to present
origin: Mountain View / New York, USA (Google)
lineage: [webos, swiss-international, metro-design-language]
tags:
  mood: [bold, tactile, systematic, optimistic]
  topics: [mobile, productivity, cross-platform products, design systems]
axes: {order: 9, density: 5, ornament: 2, warmth: 5, contrast: 6, geometry: 7, chroma: 7, typevoice: 5, energy: 5, hand: 0, play: 5, era: 7}
---

# Material Design (2014 → M3 → M3 Expressive)

**Essence:** Interface as sheets of digital paper and ink with physics, elevations, shadows and motion that start from your touch, later tuned by your own wallpaper and, since 2025, by springy, shape-shifting expressiveness.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Paper with physics | Surfaces are sheets at defined elevations; they cast shadows, slide over each other and never pass through one another. | Elevation scale (0, 1, 3, 6, 8, 12 dp) with each level mapped to a paired shadow token (key light + ambient). Overlap order follows elevation strictly; no element changes depth without motion. |
| G2 · Print-poster boldness | The 2014 spec borrowed from print and Swiss posters: big colour fields, large type, full-bleed imagery, deliberate whitespace. | App bar in a bold primary; one accent colour for actions; display type 34 to 56 px; imagery full-bleed to the edges; keylines on an 8 dp grid (4 dp for type and icons). |
| G3 · Motion that starts from touch | Press feedback radiated from the touch point (ripple); tapped cards expanded into the next screen (container transform). | Press ripple originates at exact pointer coordinates; shared-element transitions grow the tapped container into the destination page so the user never loses the object. |
| G4 · One floating primary action | A circular floating action button carried the screen's single most important verb. | One prominent floating action per screen, bottom-trailing, labelled by icon (or extended with a verb); if there is no single primary action, there is no FAB. |
| G5 · Colour from the person | Material You (2021, Android 12) derived the whole theme from the user's wallpaper using tonal palettes in the HCT colour space. | From one seed colour, generate five tonal palettes (primary, secondary, tertiary, neutral, neutral variant), tones 0 to 100; map roles (e.g. primary = tone 40 light / 80 dark). Theme is personal; contrast is guaranteed by tone distance. |
| G6 · Expressive shape and springs | M3 Expressive (May 2025), backed by 46 studies with 18,000+ participants, added a 35-shape library with shape morphing, spring-based motion physics and emphasized type. | Shape tokens from 4 dp to fully round plus a set of playful shapes; buttons morph shape on press (round → squircle); motion tokens defined as springs (stiffness/damping), not durations; one emphasized type style per screen. |

## Visual facts

- **Color:** 2014 swatch system (red `#F44336`, indigo `#3F51B5`, teal `#009688`, amber `#FFC107` and their 50 to 900 tints); M3 baseline seed purple `#6750A4`; dynamic schemes from wallpaper.
- **Type:** Roboto (Christian Robertson, 2011), Roboto Flex, Google Sans; Google Sans Flex (open-sourced in late 2025) underlies newer rounded styles. Free: **Roboto**, **Roboto Flex**, **Material Symbols** (variable icon font).
- **Form:** 2014, square-ish cards with 2 dp radius and soft shadows; M3, large radii (12 to 28 dp), tonal surfaces instead of heavy shadows; Expressive, morphing blobs, scallops, pill clusters.
- **Composition:** 8 dp grid, responsive layout grid with columns and margins, app bars, navigation rails/bars, bottom sheets.

## Attitude

Announced at Google I/O in June 2014 under Matías Duarte (who had led `webos`), Material set out to unify Google's sprawling products with a metaphor grounded in physics and print rigour. Each later phase widened the aim: Theming (2018) for brands, Material You (2021) for personal expression, Expressive (2025) for emotion validated by research. The constant: a documented, tokenised system that anyone can build.

## Blends

- **Amplifies:** `swiss-international`, `webos`, `metro-design-language`, grid, colour fields, cards.
- **Productive tension with:** `memphis`, Expressive's shape library already leans playful; Memphis pattern and clashing colour inside strict tokens yields a disciplined exuberance.
- **Clashes with:** `ios-skeuomorphism`, literal textures fight Material's abstract paper and its shadow logic.

## Don't copy

- Google logos and product icons (Gmail, Drive, etc.), Google's illustration styles, Android wallpapers; shipping the default M3 baseline purple theme unchanged as "your" style.

## Study

- m3.material.io (current spec, including Expressive) and the archived 2014 guidelines (material.io/archive).
- Google Design, "Expressive Material Design: Google research" (design.google, 2025).
- Material Color Utilities (open source), HCT colour space and tonal palette generation.
