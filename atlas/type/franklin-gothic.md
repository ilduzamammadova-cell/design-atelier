---
id: franklin-gothic
name: Franklin Gothic
type: typeface
discipline: [graphic, ui]
era: 1902 to present
origin: Jersey City / New York, USA, American Type Founders (Morris Fuller Benton)
lineage: []
tags:
  mood: [muscular, urgent, civic, newsy]
  topics: [news, museums, campaigns, government, sports]
axes: {order: 6, density: 7, ornament: 1, warmth: 5, contrast: 7, geometry: 6, chroma: 4, typevoice: 6, energy: 6, hand: 2, play: 3, era: 3}
---

# Franklin Gothic (1902)

**Essence:** The American gothic, heavy, slightly irregular, built for headlines that have to be read from across the street.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Weight as volume | Benton's family began with one heavy weight; its authority comes from dark, dense letters with the stroke thinning where curves meet stems so counters stay open. | Use one heavy weight (700 to 800) for headlines and calls to action and keep everything else regular; avoid four or five near-identical weights. Headline sizes 28 to 64px at 0 to −1% tracking; never heavier than 800 in dark mode. |
| G2 · Condensed for urgency | Condensed and extra-condensed members let long headlines fit narrow newspaper columns without shrinking. | Use a condensed width for headlines in narrow viewports (≤ 480px) instead of reducing size; keep body text at normal width. Define `headline-condensed` as a separate token, not ad-hoc `letter-spacing`. |
| G3 · Vernacular irregularity | Double-storey g, a slightly uneven rhythm and ink-trap-like thinning give the face a printed, human roughness compared to neo-grotesques. | When a product needs to feel civic or editorial rather than corporate, prefer American-gothic cuts (double-storey g, thinned joins) for headings; pair with clean UI text so the roughness stays at the top of the hierarchy. |
| G4 · Institution in one logotype | MoMA has used Franklin Gothic No. 2 for its name since 1964 and, since 2004, Matthew Carter's MoMA Gothic built from it for all typography, a museum identity made almost entirely of one gothic. | Make the wordmark simply the name set in the house face at a fixed weight and tracking; document that exact setting (weight, tracking, case) as the logo spec. |

## Visual facts

- **Classification:** grotesque (American gothic).
- **Designer · year · foundry:** Morris Fuller Benton, American Type Founders, 1902 (family extended through the 1910s with italic, condensed and extra-condensed).
- **Digital versions & licences:** ITC Franklin Gothic (Victor Caruso, 1980: Book, Medium, Demi, Heavy with larger x-height; condensed/compressed by David Berlow, 1991); Franklin Gothic Medium bundled with Windows; MoMA Gothic (custom, Matthew Carter, 2004). Commercial (ITC/Monotype).
- **Proportions:** medium-large x-height (larger in ITC), moderate apertures, noticeable thinning at joins, double-storey g with an ear, slightly condensed text widths.
- **Free / open alternatives (keep the gene):** Libre Franklin (Impallari Type, OFL); Public Sans (US Web Design System; based on Libre Franklin, slightly more regular and looser-spaced, variable since 2022).

## Attitude

Franklin Gothic was made to sell and to announce, not to disappear. Its belief is that public type should have physical weight, a headline is an act of speaking up.

## Using it today

- **Signals:** American newspapers and campaigns, MoMA, public-sector UI through Public Sans; reads "civic, journalistic, slightly old-school". Moderately used; less saturated in product UI than geometric sans.
- **Robotic ↔ humane:** 5/10, monoline but irregular; thinning joins, double-storey g and heavy, warm colour feel printed rather than machined. ITC italics are sloped with some cursive hints.
- **UI fitness:** heavy and demi weights for headlines and buttons; Book/regular OK for body at 16px+. For dense UI use Public Sans (designed for interfaces). Libre Franklin/Public Sans cover Latin (Public Sans adds Vietnamese); check Cyrillic needs.
- **Pairs with:** Century Schoolbook or Caslon for article body, the classic American newspaper pairing; Public Sans for small UI labels (same gothic root, built for interfaces); Courier Prime (OFL) for typewritten captions and data.

## Blends

- **Amplifies:** `chermayeff-and-geismar`, `lester-beall`, American graphic punch.
- **Productive tension with:** `kenya-hara`, a loud gothic used once, very large, inside a quiet, empty layout.
- **Clashes with:** `art-nouveau`, whiplash ornament against a blunt gothic reads as two unrelated posters.

## Don't copy

ITC Franklin Gothic and MoMA Gothic outlines; the MoMA logotype; campaign wordmarks set in Franklin.

## Study

- MoMA Inside/Out, "From the Archives: A Brief Homage to Franklin Gothic" (2010) and "One Typeface Fits All at MoMA" (2013): https://www.moma.org/explore/inside_out/
- US Web Design System, Public Sans: https://public-sans.digital.gov
- Klim Type Foundry, "American Grotesk design information", on the American gothic lineage.
