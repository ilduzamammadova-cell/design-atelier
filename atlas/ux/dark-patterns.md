---
id: dark-patterns
name: Dark Patterns (Deceptive Patterns), anti-gene card
type: principle
discipline: [ux]
era: 2010 to present
origin: London, UK
lineage: []
tags:
  mood: [manipulative, coercive, deceptive, urgent]
  topics: [subscriptions, e-commerce, consent banners, social feeds, games, travel booking]
axes: {order: 4, density: 7, ornament: 4, warmth: 3, contrast: 7, geometry: 5, chroma: 6, typevoice: 5, energy: 8, hand: 1, play: 3, era: 4}
---

# Dark Patterns (Deceptive Patterns)

**Essence:** ANTI-GENE CARD, never blend. Interfaces deliberately designed to trick or pressure people into choices they would not otherwise make. Use this card as a checklist of what a personal style must never contain, and adopt the inverse rules below. (The axis vector describes how these products feel, only so the matcher can warn when a style drifts toward it.)

## Genes

Each row is an *anti-gene*: the pattern, why it harms, and the inverse rule to adopt.

| Gene | The idea | In UI / product terms |
|---|---|---|
| AG1 · Hard to cancel / obstruction | Easy in, hard out ("roach motel"); barriers make leaving costly | Cancel in the same channel and the same number of steps as signup; at most one retention screen, shown once, with "Cancel subscription" as an equal-weight button |
| AG2 · Confirmshaming | Guilt-laden decline copy ("No, I prefer paying full price") | Decline labels are neutral and specific ("No thanks", "Not now"), same size, weight and style as the accept option |
| AG3 · Sneaking & preselection | Extras slipped into baskets, pre-ticked boxes, costs revealed at the end | No pre-checked add-ons, consents or newsletters; total price including fees visible from the first step; nothing enters a basket without an explicit tap |
| AG4 · Fake urgency & scarcity | Countdown timers and "only 2 left" messages that are not true | Timers only for real, server-verified deadlines; stock counts only from live inventory; no "X people are looking at this" unless measured and meaningful |
| AG5 · Trick wording & visual interference | Double negatives, accept buttons bright and reject buttons grey or hidden | Consent choices symmetrical (same component, same prominence, same level); button labels state the outcome ("Share my data" / "Don't share"); no double negatives anywhere |
| AG6 · Nagging & addictive design | Repeated asks after a "no"; endless feeds and autoplay engineered for compulsion | A "no" is remembered for at least 90 days; feeds show a natural end ("You're all caught up"); autoplay off by default; usage summaries offered, not hidden |

## Visual facts

- **Color:** the tell is asymmetry, saturated accept vs. grey decline, red countdowns, tiny low-contrast close buttons.
- **Type:** fine print for the important parts, huge type for the bait.
- **Form:** interstitials, fake system dialogs, disguised ads styled as content or navigation.
- **Composition:** the "right" choice placed where Fitts and habit make it hard to reach. The inverse style: symmetric, honest, calm.

## Attitude

Harry Brignull, a UK user-experience consultant, coined "dark patterns" in 2010 and later renamed the field "deceptive patterns" (deceptive.design, book 2023). His point is that these are deliberate business decisions, not accidents. Regulators now agree: the EU Digital Services Act bans deceptive interface design for online platforms; the US FTC's 2022 report catalogued the practice; and in September 2025 Amazon agreed to a US$2.5 billion settlement with the FTC over Prime enrolment and cancellation flows.

## Blends

- **Amplifies:** (the cure) `don-norman`, `inclusive-design`, `calm-technology`, honest signifiers, respect for all users, protected attention.
- **Productive tension with:** `persuasive-technology`, the same mechanics; the line is the user's own goal, transparency and easy exit.
- **Clashes with:** every card in the atlas, never blend; only invert.

## Don't copy

The real-company screenshots in the deceptive.design hall of shame and the book's illustrations. Never reproduce any of the patterns themselves, even "ironically" in a prototype that might ship.

## Study

- Deceptive pattern types and hall of shame: https://www.deceptive.design
- Harry Brignull, *Deceptive Patterns: Exposing the Tricks Tech Companies Use to Control You* (2023)
- US FTC staff report, *Bringing Dark Patterns to Light* (September 2022)
- Mathur et al., "Dark Patterns at Scale: Findings from a Crawl of 11K Shopping Websites" (CSCW 2019)
- Gray et al., "The Dark (Patterns) Side of UX Design" (CHI 2018)
- EU Digital Services Act, Article 25 (online interface design and organisation)
