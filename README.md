# design-atelier

A Claude skill that helps a designer discover, invent and grow their own original visual style, the way a painter's style emerges, instead of following trends.

It keeps an atlas of masters, movements, typefaces and traditions across graphic, product, UI and UX design, art, architecture and world crafts. Each entry is broken into transplantable "genes". The skill blends genes from distant sources through a person's taste profile into a new, named style, then builds it in Figma or as live web code.

## What's inside

| Path | Contents |
|---|---|
| `SKILL.md` | Entry point: modes, profiles, guardrails, file map |
| `method/` | Discover (taste interview), Blend (genes → laws → style), Evolve (journal, signature moves) |
| `atlas/` | ~380 gene cards: graphic, product, ui, ux, art, architecture, cultures, type, trends (anti-references) |
| `references/` | Visual principles, dimensions, typography, icons, imagery, motion, UX audit, anti-slop, web, Figma (9 files) |
| `templates/` | DNA profile, style spec, journal entry, gene card |
| `scripts/` | `atlas_match.py` (match a taste vector to the atlas), `icon_check.py` (validate SVG icon sets) |
| `assets/` | `taste-test.html` (A/B taste test → 12-axis Style DNA vector), `style-board.html` (three style boards to choose from) |
| `evals/` | Test prompts and assertions used to evaluate the skill |

## Install

**Claude Code**: put the folder in your skills directory:

```bash
git clone https://github.com/ilduzamammadova-cell/design-atelier.git ~/.claude/skills/design-atelier
```

Then call it with `/design-atelier`, or just ask for help finding a design style.

**Claude.ai**: zip the folder (or package it as a `.skill` file) and upload it under Settings → Capabilities → Skills.

## Notes

- Profiles and journals are stored per person in `~/.design-atelier/profiles/`.
- Atlas text is original analysis written for this skill; it does not reproduce source books.
- The scripts need only Python 3 (no dependencies).

## License

MIT. See [LICENSE](LICENSE). Use it, change it, share it.
