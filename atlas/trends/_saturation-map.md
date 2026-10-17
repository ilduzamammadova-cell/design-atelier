# Saturation map — slop check

Load this to check a design (or generated code) for the visual defaults of 2020–2026. Saturation is scored as of **October 2026**: 0 = fresh, 10 = everywhere. Each row links to a card in `atlas/trends/<id>.md` with the full "Why it reads as slop now" and "Subvert" sections.

**How to use**
- Any match at **9–10** → replace that element; keep the need, change the surface (see the card's Subvert).
- Any match at **6–8** → allowed only if it is a deliberate, transformed choice the style spec can justify in one sentence.
- **3+ matches at ≥8 on one screen** → the design reads as generic / AI-generated; redesign from the style DNA, not by patching.
- A low score (≤5) is not an endorsement — it means "dated" more than "fresh".

## Table

| id | sat | Tell-tale sign | Underlying need (keep this) |
|---|---|---|---|
| `purple-blue-gradient-saas` | 10 | Indigo→violet gradient on a headline word + indigo button on white | An ownable brand hue; a primary action that stands out |
| `inter-and-geometric-sans-default` | 10 | Inter (or Geist/DM Sans/Space Grotesk) for everything, wordmark included | Legible small UI text; a neutral carrier for content |
| `shadcn-tailwind-default-look` | 10 | Zinc borders, `rounded-md`, `shadow-sm`, lucide icons, black primary button | Accessible primitives; consistent, fast-to-build components |
| `centered-hero-three-cards-template` | 10 | Pill badge → centered H1 → 2 buttons → logos → 3 icon cards | State the value fast; scannable benefits; one path to action |
| `ai-sparkle-iconography` | 10 | Gradient ✨ on every AI button, chip and badge | Disclose machine involvement; set expectations for AI actions |
| `bento-grid` | 9 | Mosaic of rounded tiles of arbitrary sizes in the Features section | Summarise many items at a glance; size = importance |
| `linear-style-dark-ui` | 9 | Near-black page, white→gray gradient headline, tilted glowing app screenshot | Low-glare focus for pros; hierarchy by luminance; product as hero |
| `gradient-mesh-and-aurora` | 9 | Blurred violet/pink/cyan blobs drifting behind content | Atmosphere when there is nothing literal to picture |
| `dot-grid-and-line-grid-backgrounds` | 9 | Radially masked dot or 1px grid behind the hero | Signal precision; canvas affordance in real editors |
| `pill-buttons-with-arrows` | 9 | "Get started →" capsule with arrow nudge + announcement pill badge | Forward motion; friendly, tappable targets; announce news |
| `trusted-by-logo-strip` | 9 | Row/carousel of grayscale logos under "Trusted by teams at" | Borrowed trust; evidence of scale and relevance |
| `glassmorphism` | 8 | Frosted white panels with `backdrop-blur` over colored blobs | Show layering; keep context visible behind focus |
| `liquid-glass-imitation` | 8 | Glossy refractive pill nav with rainbow rim on a non-Apple site | Chrome that defers to content; continuous, physical transitions |
| `dark-mode-neon-glow` | 8 | Animated glowing border beams, violet glow, cursor spotlight | One point of attention on dark; glow as live state |
| `oversized-grotesk-hero` | 8 | Viewport-wide tight-tracked grotesk slogan, letters staggering in | One message at maximum scale; type as image |
| `emoji-as-icons` | 8 | 🚀 ⚡ 🔒 heading feature cards and H2s | Quick visual anchors; friendliness |
| `marquee-tickers` | 8 | Tilted band of looping words or an endless logo carousel | Liveness; abundance; a break in vertical rhythm |
| `editorial-serif-revival` | 7 | Light condensed serif H1 with one italic word on cream #F5F1EA | Human, literate voice; reading-first rhythm |
| `grain-and-noise-overlay` | 7 | Full-page noise at 8–15% over gradients and text | Tactility; analog warmth; de-banding gradients |
| `kinetic-type-everywhere` | 7 | Every heading splits and flies in; rotating-word hero | Time-based hierarchy; voice through motion |
| `corporate-memphis-illustration` | 6 | Flat purple-skinned figures with tiny heads and bendy limbs | Representation without stereotype; humanise abstract services |
| `3d-clay-and-blob-renders` | 6 | Pastel inflated padlock/rocket/coin floating above a card | Friendly tactility; object metaphor; delight moments |
| `neo-brutalism-web` | 6 | 3px black borders + `6px 6px 0 #000` shadows on candy fills | Visible structure; unmistakable affordance; cheap personality |
| `scroll-jacking-and-parallax` | 6 | Smooth-scroll inertia, pinned sections, wheel turns that barely move | Narrative pacing; depth; explaining a transformation |
| `cursor-followers-and-magnetic-buttons` | 6 | Lagging blend-mode circle cursor; buttons leaning toward pointer | Responsive presence; easier targeting |
| `spline-3d-hero` | 6 | Iridescent blob/torus spinning in the hero, following the cursor | Tangible product metaphor; proof of craft |
| `y2k-chrome-and-acid` | 5 | Liquid-chrome logo, acid-green starburst, pixel type | Material optimism; maximal energy for culture/events |
| `neumorphism` | 3 | Gray-on-gray controls with paired light/dark soft shadows | Physical affordance; one-material calm |
| `isometric-illustration` | 3 | 30° diorama of servers and phones with tiny faceless people | Explain systems spatially; modular diagrams |

## Code fingerprints (for scanning generated code)

| Fingerprint | Points to |
|---|---|
| `bg-indigo-500`, `from-purple-500 to-blue-500`, `bg-clip-text text-transparent` | `purple-blue-gradient-saas` |
| `font-family: Inter`, `font-sans` with Inter/Geist only, `Space Grotesk` | `inter-and-geometric-sans-default` |
| `lucide-react`, `rounded-md border shadow-sm`, zinc/slate tokens untouched | `shadcn-tailwind-default-look` |
| `backdrop-filter: blur(...)` + `rgba(255,255,255,.1–.25)` | `glassmorphism` |
| `feDisplacementMap`, "liquid-glass" component names | `liquid-glass-imitation` |
| `filter: blur(80px+)` on absolutely positioned circles | `gradient-mesh-and-aurora` |
| `radial-gradient(... 1px, transparent 1px)` + `mask-image: radial-gradient` | `dot-grid-and-line-grid-backgrounds` |
| `border-beam`, `shine-border`, `meteors`, `spotlight`, `0 0 40px` violet shadows | `dark-mode-neon-glow` |
| `rounded-full` button + `ArrowRight` + `group-hover:translate-x-1` | `pill-buttons-with-arrows` |
| `grid-cols-3` of icon cards directly after the hero | `centered-hero-three-cards-template` |
| `Sparkles` icon, ✨ in labels | `ai-sparkle-iconography` |
| `animate-marquee`, duplicated logo arrays, `-rotate-2` bands | `marquee-tickers`, `trusted-by-logo-strip` |
| `mix-blend-mode: difference` cursor div, magnetic hover handlers | `cursor-followers-and-magnetic-buttons` |
| `@splinetool/react-spline`, `<Canvas>` with a lone mesh in the hero | `spline-3d-hero` |
| Lenis / Locomotive Scroll, `ScrollTrigger` `pin: true` everywhere | `scroll-jacking-and-parallax` |
| `SplitText`, per-character stagger on every heading | `kinetic-type-everywhere` |
| `4px 4px 0 #000` + 2–3px black borders on every card | `neo-brutalism-web` |
| Paired shadows like `9px 9px 16px #a3b1c6, -9px -9px 16px #fff` | `neumorphism` |
| `feTurbulence` / noise PNG fixed over the whole body | `grain-and-noise-overlay` |
| Emoji as the first character of headings and card titles | `emoji-as-icons` |

## Known slop stacks

- **The AI SaaS default:** `inter-and-geometric-sans-default` + `purple-blue-gradient-saas` + `centered-hero-three-cards-template` + `pill-buttons-with-arrows` + `ai-sparkle-iconography` + `trusted-by-logo-strip`.
- **The dev-tool default:** `linear-style-dark-ui` + `dot-grid-and-line-grid-backgrounds` + `dark-mode-neon-glow` + `bento-grid` + `shadcn-tailwind-default-look`.
- **The "futuristic" dashboard:** `glassmorphism` / `liquid-glass-imitation` + `gradient-mesh-and-aurora` + `grain-and-noise-overlay`.
- **The agency portfolio:** `oversized-grotesk-hero` + `kinetic-type-everywhere` + `marquee-tickers` + `cursor-followers-and-magnetic-buttons` + `scroll-jacking-and-parallax`.
- **The friendly startup (2018–2022):** `corporate-memphis-illustration` + `isometric-illustration` + `3d-clay-and-blob-renders` + `emoji-as-icons`.
