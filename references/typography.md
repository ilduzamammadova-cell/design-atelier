# Typography

Type is the style's voice: people read it before they read the words. It is also where generated design collapses fastest into defaults. Choose typefaces from the style's genes, test them against the robotic ↔ humane spectrum, and check the result against the model-default list in § 4.

## 1. Derive type from the genes

1. Read the **Type** line under "Visual facts" in every source card of the style. The gene often implies a typographic consequence (Johnston's calligraphic proportions, Bodoni's vertical stress, a signage gene's open apertures).
2. Match the style's vector against typeface cards:
   ```bash
   python3 <skill-dir>/scripts/atlas_match.py --vector "<style vector>" --section type --top 8
   ```
3. Read the shortlisted cards in `atlas/type/` — especially **Using it today** (what the face signals, how saturated it is, UI fitness, pairings).
4. Assign roles: **display**, **text**, and optionally **utility** (mono or numerals). Two families is the norm; a third only for a clear utility role.
5. Write the reason for each choice in the style spec, tied to a gene. "It looks clean" is not a reason.

## 2. Robotic ↔ humane

People call a typeface "friendly" or "cold" for anatomical reasons. Read them, then choose on purpose.

| Trait | Reads robotic | Reads humane |
|---|---|---|
| **Apertures** (openings of c, e, a, s) | Closed, curling in | Open, letting light in |
| **Stroke** | Monolinear, mechanically even | Slight modulation; stress follows a pen |
| **Construction** | Compass circles, ruler lines, uniform widths | Handwriting proportions: round o, narrower e and s |
| **Terminals** | Flat horizontal or vertical cuts | Angled or softened cuts |
| **Italic** | Slanted roman (oblique) | True cursive italic |
| **Spacing** | Tight and uniform | Slightly generous, rhythmic |
| **Numerals** | Only tabular lining | Proportional and oldstyle also available |
| **x-height** | Extreme (shouting or tiny) | Moderately large |

Robotic is not wrong. A data-dense trading tool or an engineering brand may want mechanical precision; Eurostile or DIN can be exactly right there. For products whose job is care, calm or everyday use, a humanist sans or a warm text serif usually reads friendlier than a geometric or neo-grotesque face.

**Friendly is not childish.** Rounded, bouncy, hand-lettered faces signal play, not warmth. Reserve them for audiences and moments that actually want play.

Humane starting points in the atlas (read the cards before choosing): humanist sans such as Frutiger, Gill Sans (display), Myriad, Source Sans, Johnston; screen-born faces such as Verdana and Georgia; warm text serifs such as Century Schoolbook; legibility-first Atkinson Hyperlegible (mind § 4).

## 3. Famous typefaces — what they say

A famous face carries its history into every product that uses it. The card for each lists its associations and saturation; the short version:

| Typeface | Carries | Card |
|---|---|---|
| Helvetica | Corporate modernism, neutrality, "no opinion" | `atlas/type/helvetica.md` |
| Arial | Helvetica's metric stand-in; the system default — rarely chosen, often defaulted | `atlas/type/arial.md` |
| Futura | Geometric modernism, the space age, fashion | `atlas/type/futura.md` |
| Gotham | American civic vernacular; political campaign confidence | `atlas/type/gotham.md` |
| Bodoni, Didot | Fashion, luxury, high contrast — display sizes only | `atlas/type/bodoni.md`, `atlas/type/didot.md` |
| Garamond | Literary, bookish, humane classicism | `atlas/type/garamond.md` |
| Times New Roman | Newspapers, academia, the document default | `atlas/type/times-new-roman.md` |
| Roboto | Android and Google products | `atlas/type/roboto.md` |
| SF Pro | Apple's system voice — licensed for Apple platforms only | `atlas/type/sf-pro.md` |
| DIN | Engineering, road signs, technical precision | `atlas/type/din.md` |

If a card is missing, the type agents may not have written it yet; check `ls atlas/type/`.

Using a famous face is fine when its associations serve the style. Using it because it is familiar makes the style borrow someone else's voice.

## 4. Model defaults — the faces generated design reaches for

Asked for something "original", models drift to a short list of characterful-but-safe open fonts. In this skill's own testing, independent runs chose the same faces for the same brief. These are not banned; they are **unexamined**:

- **Trend sans:** Inter, Geist, DM Sans, Space Grotesk, Manrope, Plus Jakarta Sans, Poppins (see `atlas/trends/inter-and-geometric-sans-default.md`).
- **The second reflex** — what models pick when told to avoid the above: IBM Plex Sans, Archivo, Schibsted Grotesk, Hanken Grotesk, Work Sans, Public Sans — and, once those are flagged too, Libre Franklin, Fira Sans, Source Sans 3, Literata. The list will keep growing; the cure is deriving type from the gene and browsing beyond the first page of any catalogue (§ 5), not memorising bans.
- **Serifs:** Instrument Serif, Fraunces, Newsreader, Playfair Display, EB Garamond, Source Serif.
- **Mono:** JetBrains Mono, IBM Plex Mono, Geist Mono.
- **Accessibility reflex:** Atkinson Hyperlegible for everything.
- **Cultural reflex:** Shippori Mincho or Noto Serif JP whenever the brief says "Japanese".

**Rule:** if your first pick is on this list, write down three alternatives from different routes — the source card's original face or its open revival; an independent foundry from § 5; a face from a different classification that keeps the gene. Choose by the gene and record the reason. Keeping the first pick is allowed when the reason is specific.

The same reflex applies to motifs: an ensō-style gap for anything wabi-sabi, amber "safelight" for anything nocturnal, one vermilion accent on black and white. Check `references/anti-slop.md` § Model defaults.

## 5. Finding well-made, less-used open fonts

- **Google Fonts** — browse by classification and sort by newest or trending, not most popular.
- **Fontshare** (Indian Type Foundry) — free families with commercial-use terms.
- **Velvetyne** — libre, often experimental display faces.
- **Collletttivo** — a collective releasing free typefaces.
- **Use & Modify** — a curated selection of libre fonts.
- **Uncut.wtf** — a catalogue of free contemporary typefaces.
- **The League of Moveable Type** and **Badass Libre Fonts by Womxn** — open-source catalogues.

Before committing to any font: read its licence (OFL or the foundry's own terms; web, app and logo use can differ), check glyph coverage for every language the product ships in (Latin Extended diacritics, Cyrillic, Greek, Vietnamese, CJK), and confirm the weights, true italics and OpenType features you need exist.

## 6. Setting type for screens

- **Scale:** derive the ratio from the style's laws; six sizes or fewer in product UI.
- **Body:** 16px+, line-height 1.4–1.6, measure 45–80 characters (`references/principles.md`).
- **Tracking:** tighten large display sizes (−1% to −3%); add +5% to +10% to all-caps labels; never track lowercase body text.
- **Numerals:** `font-variant-numeric: tabular-nums` in tables and data; proportional or oldstyle in prose where the face has them.
- **OpenType:** real small caps (`font-variant-caps`), case-sensitive forms for all-caps, ligatures as the face intends.
- **Numerals in UI:** faces with oldstyle default figures make "1" look like "ı" or "I" in prices and counts. Set `font-variant-numeric: lining-nums tabular-nums` on buttons, prices, times and tables — and set it *after* any `font:` shorthand, which resets it.
- **Loading:** `font-display: swap`, a fallback stack with similar metrics, `size-adjust` on the fallback to avoid layout shift.
- **Licences:** a web licence does not cover app embedding; SF Pro is for Apple platforms only; brand logos may need a separate licence.
