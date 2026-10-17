# Motion

Motion is part of a style's voice. Two products with identical static screens feel completely different if one snaps like a machine and the other settles like paper. Choose the motion personality from the style's DNA, then encode it as tokens so every animation agrees.

## Personalities

Pick one primary personality. Read it from `energy`, `geometry`, `hand` and the Behavior gene.

| Personality | Feels like | Durations | Easing | Fits DNA |
|---|---|---|---|---|
| **Still** | A printed page. Nothing moves except what must. | state feedback only, 80–120ms | linear or `ease-out` | energy ≤ 2, calm/quiet styles |
| **Mechanical** | A well-made machine: precise, quantised, confident | 100–200ms | sharp `cubic-bezier(.2,0,0,1)`, or `steps()` for deliberate tick motion | order ≥ 8, geometry ≥ 8, hand ≤ 2 |
| **Physical** | Objects with mass that settle | spring-based; settle ≈ 250–450ms | springs (stiffness/damping) rather than curves | product-led, tactile styles; warmth ≥ 6 |
| **Editorial** | Turning pages, slow reveals, cuts between scenes | 300–600ms | gentle `ease-in-out` | typevoice ≥ 7, density ≤ 5 |
| **Ink / organic** | Things that grow, bleed, unfurl | 400–900ms, staggered | asymmetric, long tails | hand ≥ 7, geometry ≤ 3 |
| **Kinetic** | Type and shape as performers | varies; choreographed sequences | expressive, often custom per sequence | energy ≥ 8, play ≥ 7 — use sparingly; best for brand moments, not product chrome |

A style may borrow a secondary personality for one moment (e.g. a Still product with one Kinetic hero) — name that moment explicitly in the spec.

## Tokens

Define these in every style spec; never write raw durations or curves in components.

```css
:root {
  --duration-instant: 0ms;
  --duration-fast: 120ms;    /* hover, press, toggle */
  --duration-base: 220ms;    /* small layout change, popover */
  --duration-slow: 400ms;    /* page/section transition, large reveal */
  --ease-standard: cubic-bezier(.2, 0, 0, 1);
  --ease-enter: cubic-bezier(0, 0, 0, 1);      /* decelerate into place */
  --ease-exit: cubic-bezier(.3, 0, 1, 1);      /* accelerate away */
}
@media (prefers-reduced-motion: reduce) {
  :root { --duration-fast: 0ms; --duration-base: 0ms; --duration-slow: 0ms; }
}
```

Adjust values to the personality; keep the names stable.

## What moves

Motion should explain something: where an element came from, where it went, what changed, what is responding. Before adding any animation, finish the sentence "This moves so the user understands that…". If you can't, cut it.

Good reasons:
- **Feedback** — press, toggle, success, error.
- **Continuity** — an element expands into its detail view instead of the screen jumping.
- **Hierarchy over time** — the most important element arrives first.
- **State** — loading, progress, completion.

Usually bad reasons (and saturated trends): scroll-jacking, parallax for its own sake, cursor followers, magnetic buttons, marquee tickers, everything fading up on scroll, looping background blobs.

## Implementation

- Animate `transform` and `opacity`. Avoid animating `width`, `height`, `top`, `left` (layout thrash). Never `transition: all`.
- Respect `prefers-reduced-motion`: replace movement with instant change or a short opacity fade; never remove the information the motion carried.
- Web: CSS transitions for state; the View Transitions API for page/element continuity where supported; Motion (`motion` / formerly Framer Motion) or GSAP for choreography; Rive or Lottie for illustrative animation.
- Figma: Smart Animate between variants; match durations and easing to the tokens so prototypes behave like the build.
- No animation may block input. Long sequences must be skippable.
- Nothing flashes more than three times per second (WCAG 2.3.1).
