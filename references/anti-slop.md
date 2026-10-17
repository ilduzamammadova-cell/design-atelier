# Anti-slop

"Slop" is design that happened instead of being chosen: the statistical average of everything already online. It is what a model produces when it reaches for the most likely answer at every decision. Each default is harmless alone; together they make work instantly recognisable as generic.

This skill's main defence is structural, a personal DNA, genes from far-apart sources, hard laws. This file is the final check.

## The tells

### Composition
- Centered hero → three feature cards with icons → testimonial carousel → pricing table → logo strip → FAQ accordion → footer. The template, in the template's order.
- Every section the same height and padding; no rhythm change anywhere.
- Symmetry by default, never by decision.
- "Trusted by" strip of logos the product doesn't have.

### Color
- Purple/indigo/blue gradient as the brand, regardless of the brand's actual hue.
- Gradient text on headlines.
- Glows, neon shadows on dark backgrounds; aurora/mesh blobs behind content.
- Accent applied everywhere, so it marks nothing.

### Type
- Inter (or another neutral geometric sans) for everything, at default tracking, because nothing was chosen.
- Huge headline + small grey subline + two buttons ("Get started" / "Learn more →").
- Headlines in Title Case With Every Word Capitalised for no reason.

### Surface
- Glass cards with backdrop blur over gradients.
- Uniform 12 to 16px radius on every element; uniform soft shadow on every card.
- Dot-grid or line-grid backgrounds as filler.
- Grain/noise overlay applied to "add texture" without a reason.

### Icons & imagery
- Default outline icon set at default size in a tinted circle, one per feature card.
- ✨ for anything AI. Emoji as icons.
- 3D clay blobs, isometric illustrations, faceless flat people with oversized limbs.
- Stock photos of people pointing at laptops.
- Grey boxes or empty frames labelled "Image", a design without imagery is a wireframe.

### Copy
- "Unlock", "supercharge", "seamless", "elevate", "revolutionise", "effortless", "all-in-one".
- Fabricated numbers ("10,000+ teams"), fake testimonials, invented logos.
- Three-adjective rhythm everywhere ("Fast, secure, and reliable").

### Motion
- Every element fades up on scroll. Magnetic buttons. Cursor followers. Marquees. Scroll-jacking.

Each has a card with saturation and a "Subvert" section in `atlas/trends/`. When a tell is present, the fix is rarely to delete, it is to meet the same need with a gene from the style.

## Model defaults

These rules govern *your* unprompted choices. The person's own evidence outranks them: if their proudest work, their references or their journal show a move repeatedly (say, black and white with one orange accent), that move is their signature, keep it and build on it; never strip it because it also appears on this list.

Trend slop is what the internet repeats. Model slop is what *Claude* repeats: the second-order defaults it reaches for when told to be original. In this skill's own tests, separate runs given the same brief converged on the same typefaces and motifs. They are not banned, they are unexamined. If a choice below came to mind first, write two alternatives from the atlas, choose by the gene, and record why.

- **Type:** the faces in `references/typography.md` § 4, e.g. IBM Plex, Archivo, Schibsted/Hanken Grotesk, Atkinson Hyperlegible everywhere, Instrument Serif/Fraunces/Newsreader for "editorial", Shippori Mincho for anything Japanese.
- **Palette:** black and white with one vermilion/orange accent; amber "safelight" for anything nocturnal; warm paper + ink + one accent as the universal "tasteful" answer.
- **Motifs:** an ensō-style gap or brush circle for anything wabi-sabi or Zen (also a religious symbol, see the culture card's Respect section); a transit-map diagram for anything about flows; a tick-marked dial for anything about measurement.
- **Skill defaults:** this atlas has its own gravity. Across unrelated briefs, tests kept reaching for the same few sources, Anni Albers' weave and threads, Carlo Scarpa's joints, Edward Tufte, Ladislav Sutnar, James Turrell's light, and the same faces (Libre Franklin, Fira Sans, Source Sans 3, Literata). Use `--vary` and the recent-sources memory; if one of these comes first, look again.
- **Venue and food clichés:** opening hours drawn as a 12-cell clock or lit windows; the brand's initial or a special letter turned into a cup or plate; a cream or limestone page with sepia photos for any café. Independent runs on the same café brief produced all three.
- **Structure:** exactly three directions that differ only in palette; seven laws when five would do; every direction recommending a blend of A and C.

## Pre-delivery check

Run on every deliverable before showing it. Answer each in one line in your own working; fix anything that fails.

1. **Chosen?** For the palette, type pair, layout of the first viewport, icon set and motion: can I name the gene or law each came from? If one "just happened", replace it. If it is on the § Model defaults list, show the two alternatives you rejected.
2. **Laws:** does the work obey every law in the style spec? List violations.
3. **Signature:** are at least two of the style's signature moves visible on this screen?
4. **Saturation:** compare against `atlas/trends/_saturation-map.md`. Any trend at saturation ≥ 7 visible? Justify or subvert it.
5. **Logo test:** cover the logo. Could this be any other product? Name the one thing that makes it this one.
6. **Content:** no invented metrics, quotes, logos or names. Placeholders are bracketed and listed.
7. **Fundamentals:** contrast pairs pass AA; focus visible; labels present; works at 375px; reduced motion handled.
8. **Copy:** `scripts/copy_check.py` reports no dashes and no slop phrases; headlines say something specific to this product (`references/copy.md`).

Report the check result to the person briefly, one line per failed item and what you did about it. Passing items don't need narrating.
