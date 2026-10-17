---
id: segoe-ui
name: Segoe UI
type: typeface
discipline: [graphic, ui]
era: 2006–present (Segoe UI Variable 2021)
origin: Redmond, USA — Microsoft, designed by Steve Matteson at Agfa Monotype
lineage: [metro-design-language, fluent-design]
tags:
  mood: [open, calm, businesslike, familiar]
  topics: [operating-systems, productivity, enterprise, forms, dashboards]
axes: {order: 8, density: 5, ornament: 0, warmth: 6, contrast: 3, geometry: 5, chroma: 4, typevoice: 1, energy: 2, hand: 1, play: 2, era: 6}
---

# Segoe UI (Windows Vista, 2006–07)

**Essence:** Windows' humanist voice — an open, unshowy sans that later became the typographic backbone of Metro's "content over chrome" and of Fluent.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Humanist system face | Segoe UI replaced Tahoma as the Windows UI font from Vista: open apertures and gentle modulation for long hours of interface reading. | Default UI text in an open humanist sans at 14px/20px; labels 12px/16px; never set UI chrome in a display face. |
| G2 · Type as the interface (Metro) | Windows Phone 7 and Windows 8 used large, light Segoe headings as primary navigation — typography replaced buttons and frames. | Use oversized, light headings (light/semilight, 32–46px) as tappable section switchers in pivot-style nav; let whitespace and type size, not boxes, define hierarchy. |
| G3 · Optical sizing in the system font | Segoe UI Variable (Windows 11) uses a variable optical-size axis so captions and titles get size-appropriate shapes and spacing. | Use `font-optical-sizing: auto` with an opsz-capable face; Microsoft's guidance for Windows 11: Regular for most text, Semibold for titles, minimum 12px Regular and 14px Semibold. |
| G4 · Open fallback by design | Microsoft released Selawik (Aaron Bell, OFL, 2015) as an open-source, metric-friendly fallback for Segoe UI. | Ship a metrically matched open fallback for any proprietary system face you reference: `font-family: "Segoe UI Variable", "Segoe UI", Selawik, system-ui, sans-serif`. |

## Visual facts

- **Classification:** humanist sans (system UI).
- **Designer · year · foundry:** Steve Matteson (Agfa Monotype); Segoe licensed by Microsoft in 2003 as a brand face replacing Franklin Gothic; Segoe UI became the Windows UI font with Vista. Light/Semibold added in Windows 7, Semilight in Windows 8; the 2012 Microsoft wordmark is set in Segoe.
- **Digital versions & licences:** Segoe UI, Segoe UI Variable (Windows 11, with optical sizes), Segoe UI Symbol/Emoji; bundled with Windows, not redistributable. Often compared with Frutiger and Myriad.
- **Proportions:** medium-large x-height, open apertures, slight modulation, true italic; Variable adds text/display optical sizes.
- **Free / open alternatives (keep the gene):** Selawik (Microsoft, Aaron Bell, OFL — Segoe UI fallback, five weights); Open Sans (Steve Matteson, OFL — same designer, similar humanist openness).

## Attitude

Segoe embodies Microsoft's shift from decorated chrome to typographic interface: the belief that clear, open letters at generous sizes can carry an operating system's personality on their own.

## Using it today

- **Signals:** Windows Vista to Windows 11, Office, Xbox-era Metro, Microsoft's 2012 logo; reads "Windows, productivity, enterprise". Saturation: ubiquitous on Windows, invisible elsewhere.
- **Robotic ↔ humane:** 7/10 — open apertures, humanist modulation and a true italic; its businesslike evenness makes it calm rather than warm.
- **UI fitness:** body, labels and headings in Windows-native UI; for cross-platform web, reference it only through a system stack. Wide script coverage (Latin, Greek, Cyrillic, Arabic, Hebrew and more) on Windows.
- **Pairs with:** Cascadia Code or another clear mono for developer UI; a sturdy, large-x-height screen serif (Georgia class) for long-form reading views, so documents get a second voice; Segoe Fluent Icons for matched stroke and metrics.

## Blends

- **Amplifies:** `metro-design-language`, `fluent-design` — typography-led system UI.
- **Productive tension with:** `swiss-international` — Metro's own roots in transit signage and Swiss grids.
- **Clashes with:** `ios-skeuomorphism` — flat typographic chrome vs simulated materials.

## Don't copy

Segoe outlines and Microsoft wordmark; don't embed bundled Windows font files in apps or websites.

## Study

- Microsoft Learn, Windows app typography: https://learn.microsoft.com/windows/apps/design/style/typography
- Microsoft Typography, Selawik: https://learn.microsoft.com/typography/font-list/selawik
- Mike Kruzeniski, "From Transportation to Pixels" (2011) — Metro's typographic roots.
