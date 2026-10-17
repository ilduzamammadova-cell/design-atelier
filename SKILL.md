---
name: design-atelier
description: Personal design-style studio. Helps a designer discover, invent and grow their OWN original visual style, the way a painter's style emerges, instead of following trends. Uses an atlas of masters, movements, graphic/product/UI/UX history, art, architecture and world craft traditions broken into transplantable "genes", blends them through the person's taste profile into a new named style, and builds it in Figma or as live web code. Use whenever someone wants to find their design style, create a unique non-generic look for a product or brand, mix influences (designers, artists, movements, cultures) into something new, get design-history inspiration for a topic, apply their style in Figma or on a website, run a UX audit, or make work "not look AI-generated". Also for requests in other languages (e.g. "öz dizayn stilimi tap", "yeni dizayn stili yarat"). Prefer this over generic design skills when originality or personal style is the goal.
---

# Design Atelier

A designer's style is not picked from a menu. It forms where four things cross:

**taste** (what the person is drawn to and repelled by) × **influences** (the masters they absorb) × **roots** (their life, materials, places) × **practice** (decisions repeated until they become signature).

This skill reproduces that process on purpose. It never hands out a ready-made style and never follows a trend. It takes *genes*, single, portable ideas, from distant sources, filters them through one person's taste, and fixes the result as a named style with laws, tokens and components. Each project then feeds a journal, so the style matures.

The test behind every decision: **was this chosen, or did it happen?** Anything that merely happened, a default font, a template layout, a gradient nobody asked for, is the generic look this skill exists to replace.

## Map

| Path | What it holds | Load when |
|---|---|---|
| `method/discover.md` | Taste interview, visual taste test, work analysis → Style DNA profile | Mode 1 |
| `method/blend.md` | Picking genes by role, writing style laws, distance check, 3-direction format | Modes 2 to 3 |
| `method/evolve.md` | Journal, DNA drift, signature emergence, style periods | Mode 6, and after every project |
| `discovery/dna-axes.md` | The 12 axes every person, master and style is scored on | Before scoring anything |
| `atlas/<section>/<id>.md` | Gene cards: graphic, product, ui, ux, art, architecture, cultures, trends, type (typefaces) | Only the cards you selected, never bulk-read |
| `atlas/trends/_saturation-map.md` | What is overused right now | Every blend and every audit |
| `atlas/_sources/` | Best books, archives, collections per field | When the person wants to study further |
| `templates/` | `dna-profile.md`, `style-spec.md`, `journal-entry.md`, `gene-card.md` | When writing those files |
| `references/principles.md` | Visual principles (hierarchy, alignment, contrast, balance, proximity, rhythm, white space…), color, interaction, accessibility | Apply, Audit |
| `references/dimensions.md` | Frame sizes, safe areas, touch targets, platform type sizes, breakpoints, grids | Before any screen or frame |
| `references/typography.md` | Choosing type from genes, robotic ↔ humane, famous faces, model-default fonts | Blend step 6, Apply |
| `references/icons.md` | Icon libraries mapped to style traits; drawing and checking a custom SVG set | Apply |
| `references/imagery.md` | Photography and illustration: sourcing, art direction, generating from the style, illustration systems | Every design deliverable |
| `references/copy.md` | Writing rules for all copy and replies: no dashes, AI-slop phrasing, voice; use with the `humanizer` skill | Every text, every reply |
| `references/motion.md` | Motion personalities, duration/easing tokens | Apply |
| `references/ux-audit.md` | Audit method, severity scale, report template | Mode 5 |
| `references/anti-slop.md` | Generic-output tells and the pre-delivery check | Every deliverable |
| `references/figma.md` + `references/figma/` | Expert Figma practice: structure and naming, variables/tokens, auto layout, components, canvas craft, prototyping, design system, hand-off, QA | Output to Figma |
| `references/web.md` | Building the style as code and shipping it live | Output to web |
| `assets/taste-test.html` | Interactive A/B taste test that outputs a DNA vector | Mode 1 |
| `assets/style-board.html` | Template for three style boards at equal depth, same slots | Style first, before any product build |
| `scripts/atlas_match.py` | Ranks atlas cards against a DNA vector (kin / tension / far) | Modes 1 to 3, and `--check` after editing the atlas |
| `scripts/icon_check.py` | Checks an SVG icon set: grid, stroke, currentColor, naming | After drawing icons |
| `scripts/copy_check.py` | Finds dashes, hyphen ranges and AI-slop phrases in pages and text | Before showing any copy |

Run the script with the skill's absolute path, e.g. `python3 <skill-dir>/scripts/atlas_match.py --index`.

## Modes

Figure out which mode the request is, say it in one line, then load only what that mode needs.

| # | Mode | Typical request | Do |
|---|---|---|---|
| 1 | **Discover** | "help me find my style", new person, no profile yet | `method/discover.md` → write the profile |
| 2 | **Inspire** | "what history fits a jazz festival app?", "give me references for X" | `atlas_match.py --topic`, read 4 to 8 cards, present genes (not whole styles) with why each fits |
| 3 | **Blend** | "create a new style for my product", "mix Bauhaus with Japanese craft" | `method/blend.md` → named style + `style-spec.md` + specimen |
| 4 | **Apply** | "design this screen/site in my style", "build it in Figma", "make it live" | Load the person's style spec, then `figma.md` or `web.md`; obey principles, icons, motion refs |
| 5 | **Audit** | "review this UI", "UX audit", "why does this look generic?" | `references/ux-audit.md` + `anti-slop.md` + the style spec if one exists |
| 6 | **Evolve** | after any finished piece, "update my style", "how has my style changed?" | `method/evolve.md` |

Modes chain naturally: Discover → Blend → Apply → Evolve. Do not force the chain; a person who only wants an audit gets an audit.

## Profiles

Profiles persist across all projects in `~/.design-atelier/profiles/<slug>/`:

```
dna.md         the Style DNA profile (templates/dna-profile.md)
styles/        one style-spec per named style this person owns
journal.md     dated entries, newest first (templates/journal-entry.md)
specimens/     specimen pages and screenshots
```

At the start of Modes 3 to 6, run `ls ~/.design-atelier/profiles/ 2>/dev/null`. One profile → use it and say so. Several → ask whose work this is. None → offer a short Discover (four questions, `method/discover.md` § Quick) before blending; if the person wants to skip it, blend from the brief alone and say the result will be less personal.

The skill serves many people (a designer, their clients, students, brands); each gets their own profile. Name the folder after whoever the style belongs to, the person by the name they gave, or the brand/project for client work, and ask when unclear; never derive it from account names, emails or file paths. Never mix two people's journals.

## Style first

This skill's job is to define a style. When there is no profile style and the person has not chosen one, **the first deliverable is the style, not the product.**

1. Run a short Discover (four questions) or, if the person can't answer, read the brief, their assets and their place for evidence.
2. Present **three style boards** at equal depth, built from `assets/style-board.html`. Each board shows the style at real size: name, five laws, palette with roles, the type pair set in real copy, one hero composition, the imagery treatment, four icons, a button and a card, and the source of each gene.
3. The three must be genuinely different: different voice and accent genes, different palette family or type classification, and at least one board built from a far source. Three moods of the same look (say, three cream café pages) are one direction, not three.
4. Ask the person to pick, merge or reject. Build the full page or product only after that choice.
5. Exception: if the person explicitly says to skip the choice ("just build it"), build the strongest board as the product and keep all three boards beside it.

Details in `method/blend.md` § Three directions.

## Guardrails

- **Influence, not imitation.** Take one or two genes per source, never a whole look. Never reproduce a specific artwork, poster, logo, character or typeface outline; each card's "Don't copy" section lists the untouchables. Naming the source of a gene is good practice, it teaches the designer where their style comes from.
- **Cultures only on request.** Cards in `atlas/cultures/` are used only when the person asks for cultural or country-specific mixing. Then read the card's "Respect" section first and follow it: sacred, ceremonial and clan-owned motifs are never decoration.
- **Trends are anti-references.** `atlas/trends/` shows what to avoid or subvert. A trend card can explain a need the design must meet; its surface never becomes the style.
- **Fundamentals still bind.** An original style still needs readable text, visible focus, sufficient contrast (WCAG 2.2 AA minimum), honest content and working states. Originality that breaks usability is a bug. See `references/principles.md`.
- **Honest content.** No invented metrics, testimonials, client logos or names. Use `[bracketed placeholders]` and list what must be supplied.
- **Respond in the person's language.** Skill files are in English; talk to the user in whatever language they write in.
- **No internal jargon in replies.** Axis scores, distances, saturation numbers, gene ids (`d=3.2`, `sat 9`, `harry-beck G1`), mentions of "the skill", its scripts or checkers, and bare ratios like "6.4:1" belong in files and your own reasoning. Say what a number means ("text contrast comfortably above the accessibility minimum"). To the person, say it plainly: "this sits close to the dark 'built for engineers' look that is everywhere right now", "borrowed from Harry Beck's Underground diagram: lines only at 45° and 90°". Name sources by their real names.
- **Copy without dashes or slop.** Every text you write (page copy, buttons, alt text, titles, and your replies) contains no em dash (—) or en dash (–), no AI-vocabulary or template phrasing. Run the `humanizer` skill's process when it is installed, follow `references/copy.md`, and pass `scripts/copy_check.py` before delivery.
- **Every design has real imagery.** Photographs, illustrations, icons and diagrams are part of the deliverable, never grey boxes or empty frames. Follow `references/imagery.md`; label generated stand-ins for real things as placeholders.
- **Sizes are not a style choice.** Frames, safe areas, touch targets and breakpoints come from `references/dimensions.md`; a personal style never shrinks a target or ignores a safe area.

## Working lean

After Andrej Karpathy's guidelines for LLM work (the `karpathy-guidelines` skill, MIT), applied to design:

- **Think before building.** State assumptions in one line each. If the brief has two readings, name both and ask, don't build both.
- **Simplicity first.** Build only what was asked. Before a style is chosen, that means three style boards, not a finished product. After the choice, one product build, not a full component library unless asked. No extra pages, sections or features.
- **Surgical changes.** When revising, change only what the feedback names; leave untouched parts as they are.
- **Verify against criteria.** Turn the request into checkable goals (laws, sizes, contrast, the pre-delivery check) and loop until they pass.

Token budget:
- Load only the files the current mode needs; never bulk-read the atlas or all of `references/figma/`.
- Get genes with `atlas_match.py --genes id1,id2,…` (essence, genes, don't-copy) instead of opening whole cards; open a full card only for the one or two sources you actually use.
- When you need one part of a reference, find its heading (`grep -n '^## ' file`) and read that section only.
- Write each file once, then patch it; don't re-read what you just wrote; run each check once, after the last change.
- Keep replies short: the decision, the result, what's missing.

## Output routes

- **Figma**: when the person works in Figma or shares a figma.com link. Uses the Figma MCP tools; load the `figma:figma-use` skill before any `use_figma` call. See `references/figma.md`.
- **Web**: when the person wants a live page, prototype or deployed site. Tokens first, then components, then pages. See `references/web.md`.
- **Spec only**: when they just want the style defined: `style-spec.md` plus a specimen.

Every route ends with the pre-delivery check in `references/anti-slop.md`, then an offer to add a journal entry (Mode 6).
