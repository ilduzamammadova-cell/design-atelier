# Building a style for the web (and shipping it live)

Use when the person wants a live page, a coded prototype, components for an existing codebase, or a deployed site.

## Detect first

- **Existing codebase?** Read its stack (`package.json`, framework, CSS approach, component library). Build the style *into* it: map tokens onto the existing theme system (Tailwind theme, CSS variables, styled-system, shadcn theme) rather than adding a parallel one. Ask before replacing a component library.
- **Nothing yet?** Default to the smallest thing that works: a single `index.html` with inline CSS for a specimen or landing page; Vite + React (or the person's preferred framework) for an app.
- **Existing design system or brand?** Adopt it; the personal style then operates through layout, type use, motion and the details the brand leaves open.

## Build order

1. **Tokens** — CSS custom properties, generated from the style spec (§ 11). Light and dark. These are the only place raw values live.
2. **Base** — reset, root type (font loading with `font-display: swap`, real fallbacks), focus styles, selection color, reduced-motion handling.
3. **Components** — each with every state. Components reference tokens only; a raw hex or px in a component is a bug.
4. **Specimen** — the page from `method/blend.md` § 7. Get it right before any product page.
5. **Pages / product screens.**

```css
/* tokens.css — names match the Figma variables */
:root {
  --color-bg: …; --color-surface: …; --color-ink: …; --color-ink-muted: …;
  --color-accent: …; --color-on-accent: …; --color-line: …;
  --font-display: "…", fallback-stack; --font-text: "…", fallback-stack;
  --space-1: …; /* … the scale from the spec */
  --radius-…: …;
  --duration-fast: …; --ease-standard: …;
}
@media (prefers-color-scheme: dark) { :root { /* dark values */ } }
```

With Tailwind v4, expose the same tokens through `@theme` so utilities and custom CSS share one source.

## Fonts

- Prefer fonts with clear web licences: Google Fonts, Fontshare, open-source foundry releases, or the person's licensed fonts.
- Self-host when possible; subset; preload only the one or two files used above the fold.
- If the style's chosen face can't be licensed for the project, pick the closest alternative that keeps the gene (stem contrast, width, terminals) and record the substitution in the spec.

## Quality bar before anything is called done

- Works at 375px, 768px, 1280px+, no horizontal scroll.
- Keyboard-only: every interactive element reachable, visible focus, logical order.
- Contrast pairs pass AA in light and dark.
- `prefers-reduced-motion` respected.
- Lighthouse (or equivalent) accessibility ≥ 95; no layout shift from fonts or images (reserve space).
- Real states: empty, loading, error, long content, missing images.
- Pre-delivery check from `references/anti-slop.md`.

Verify in a browser (the built-in browser tools or a local preview), take screenshots at mobile and desktop widths, and compare them against the style laws before showing them. Code checks alone miss what the eye catches at once: a heading indented twice, content scrolling under the status bar, a numeral that reads as a letter, two buttons competing for attention.

## Shipping it live

Deployment is an outward-facing action: confirm with the person before publishing anything publicly.

- **Already has hosting / CI?** Use their existing pipeline (and any deploy skill or tooling the person already uses).
- **Static page or specimen:** any static host works — Vercel, Netlify, Cloudflare Pages, GitHub Pages. A single HTML file can also be published as an artifact when that tool is available.
- **App builders** (e.g. Lovable) when the person works there: send the style spec's tokens and laws as part of the brief so the builder doesn't fall back to its defaults.

After deploy, open the live URL, re-check mobile and desktop, and send the person the link plus a screenshot.
