# Dimensions

Wrong frame sizes, small targets and invented breakpoints are the fastest way to make original work look amateur. A personal style changes color, type, shape and rhythm; it never changes the sizes below. Use this file whenever a screen, frame, breakpoint, icon or share image gets a number. Checked against primary sources on 2026-10-16. Values marked **(verify)** could not be confirmed from a primary source; check them in the device simulator or the platform's current UI kit before relying on them. When Apple or Google ship new hardware or a new design language, re-check this file.

## 1. Units & grid

Design in logical units at 1x, never in device pixels. In Figma, 1 unit = 1 pt = 1 dp = 1 CSS px; export with the multipliers that follow the unit table.

| Unit | Where | What it is | Use for |
|---|---|---|---|
| **pt** | iOS, iPadOS | Logical point. @2x screens draw 1 pt with 2×2 px, @3x with 3×3 px | All iOS layout and type |
| **dp** | Android | ≈ 1 px on a 160 dpi screen; `px = dp × (dpi / 160)` | Android layout |
| **sp** | Android | Same as dp by default, but scales with the user's text size | Text only, never layout |
| **CSS px** | Web | 1/96 in; not a device pixel, one CSS px can span several physical pixels | Web layout |
| **rem** | Web | Root (`html`) font size; browser default is usually 16px | Type, spacing, breakpoints |

| Platform | Export multipliers |
|---|---|
| iOS / iPadOS | @2x (all iPads, iPhone SE 4.7", iPhone 11/XR) and @3x (every other current iPhone). Prefer SVG/PDF vectors |
| Android | mdpi 1x · hdpi 1.5x · xhdpi 2x · xxhdpi 3x · xxxhdpi 4x (a 48×48 mdpi asset is 192×192 at xxxhdpi). Prefer vector drawables |
| Web | SVG for icons; raster images at 1x and 2x via `srcset` |

**The 4/8 system.** Material's spacing scale is built on 8 dp (`space100` = 8 dp) with nested steps of 2, 4, 6 and 10 dp inside components. Its token scale: 0, 2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 32, 36, 40, 48, 56, 64, 72. Material 2 put components on an 8 dp grid and icons and type on a 4 dp grid. Apple publishes no grid rule, but its own numbers (44, 28, 24, 12 pt) are all multiples of 4. Choose like this:

- **Base unit 4, layout steps in 8.** Margins, section gaps, card padding and touch-UI spacing: 8, 16, 24, 32, 48, 64. Inside components (icon-to-label gap, chip padding, badge offset, dense tables): 4, 8, 12.
- **Go 8-only** for spacious, calm, expressive styles and marketing pages.
- **Lean on 4** for dense, data-heavy or desktop-tool styles.
- **Line heights in multiples of 4** so text sits on the same grid as boxes (every M3 line height already is).
- Never mix a 5/10 system with 4/8 in one product. Off-grid values (13, 15, 18 px spacing) read as accidental.

## 2. Figma frame presets

Design one frame per breakpoint, not one per device. Test at the extremes.

| Target | Design at | Test at (smallest / largest) | Notes |
|---|---|---|---|
| **iPhone** | **402×874 pt** (iPhone 17, 17 Pro, 18 Pro) | 375×667 (iPhone SE 4.7", shortest) and 360×780 (iPhone 13 mini, narrowest) / 440×956 (Pro Max) | Drop the 360/375 checks only if analytics show you can |
| iPhone, other current sizes | none | 390×844 (16e/17e) · 393×852 (15/16) · 420×912 (Air) · 430×932 (16 Plus) | Spot-check the one closest to your audience |
| **Android phone** | **411×891 dp** (Android Studio reference phone) | 360×800 dp (a top mobile viewport worldwide) / largest supported phone | Window size, not device, drives layout |
| Foldable | 673×841 dp (reference unfolded foldable) | Folded (compact) and unfolded, both orientations | iPhone Duo: see § 3 |
| **Tablet** | **820×1180 pt** (iPad, iPad Air 11") | 744×1133 (iPad mini) / 1032×1376 (iPad Pro 13"), portrait and landscape | Android reference tablet: 1280×800 dp landscape |
| **Web, mobile** | **390** wide | 320 (WCAG reflow minimum) / 440 | Height grows with content |
| **Web, laptop/desktop** | **1440** wide | 1280 (small laptops; 1280×720, 1366×768, 1536×864 are all common) / 1920 (most common desktop screen, ~28%) | Check 1024 for tablets in landscape and split windows |

Rules: keep the frame at the device's portrait size in points/dp; show the status bar, home indicator and system bars in the frame; never scale a frame to "fit" a different device.

## 3. iOS / iPadOS

### Screen sizes (portrait, points)

The HIG Layout page dropped its device table in its 2026-09-09 update. The values below come from the last published HIG table (July 2026) and Apple's tech-spec pages. For any newer device, read the size in Xcode's Device Hub or the Simulator.

| Device | Points | Pixels |
|---|---|---|
| iPhone 18 Pro Max · 17 Pro Max · 16 Pro Max | 440×956 | 1320×2868 @3x |
| iPhone Air | 420×912 | 1260×2736 @3x |
| iPhone 18 Pro · 17 Pro · 17 · 16 Pro | 402×874 | 1206×2622 @3x |
| iPhone 16 Plus · 15 Pro Max · 15 Plus | 430×932 | 1290×2796 @3x |
| iPhone 16 · 15 Pro · 15 | 393×852 | 1179×2556 @3x |
| iPhone 17e · 16e | 390×844 | 1170×2532 @3x |
| iPhone 13 mini · 12 mini | 360×780 | 1080×2340 @3x |
| iPhone SE 4.7" | 375×667 | 750×1334 @2x |
| iPhone Duo, outer display (5.4") | ≈466×678 **(verify)** | 1398×2034 device pixels (also the App Store screenshot size) |
| iPhone Duo, inner display (7.6", folding) | ≈626×890 **(verify)** | 1878×2670 device pixels; App Store screenshots use 2007×2853 |
| iPad mini 8.3" | 744×1133 | 1488×2266 @2x |
| iPad 11" · iPad Air 11" | 820×1180 | 1640×2360 @2x |
| iPad Pro 11" (M4 and later) | 834×1210 | 1668×2420 @2x |
| iPad Air 13" | 1024×1366 | 2048×2732 @2x |
| iPad Pro 13" | 1032×1376 | 2064×2752 @2x |

iPhone 18 Pro / Pro Max and 17e points are Apple's published pixels ÷ 3 (same pixel grids as the models they're listed with). iPhone Duo points are device pixels ÷ 3 (Apple specs page, checked 2026-10-16); confirm against the HIG before relying on them. On iPhone Duo, toolbars and tab bars move to the side of the outer display and of the inner display in landscape; build with size classes and safe areas, never fixed widths.

### Layout, safe areas and bars

| Item | Value | Rule |
|---|---|---|
| Size classes | iPhone portrait = compact width, regular height. iPad full screen = regular/regular. Max/Plus/Air landscape = regular width, compact height | Lay out by size class, not by device or orientation |
| Safe area | Top (status bar, Dynamic Island) and bottom (home indicator) vary by model; typical top ≈ 47 to 62 pt, bottom 34 pt on Face ID iPhones **(verify)** | Read the safe area; never hardcode. Backgrounds bleed under bars; controls and text stay inside |
| Side margins | System layout margins: 16 pt on most iPhones, 20 pt on larger/regular widths **(verify)** | Align content to layout margins. Avoid full-width buttons; inset them |
| Navigation bar | Standard title, or Large Title (34 pt text style) that collapses on scroll | Use the system bar from Apple's current (Liquid Glass) UI kit. Legacy UIKit heights: 44 pt nav bar, 49 pt tab bar **(verify; Liquid Glass bars float and differ)** |
| Tab bar | iOS: floats over content at the bottom. iPadOS: near the top, can convert to a sidebar | Navigation only, never actions. Short single-word labels. Avoid overflow: extra tabs collapse into a "More" tab. On iPad, default to five or fewer |
| Toolbar | Actions for the current view | One primary action with the prominent style, on the trailing side |
| Hit target | **44×44 pt** default · **28×28 pt** absolute minimum | Leave ~12 pt around bezeled controls, ~24 pt around borderless ones |
| Text size | Default 17 pt · minimum 11 pt | Support enlargement to at least 200% |

### Dynamic Type, Large (default) size, SF Pro

| Style | Weight | Size / leading (pt) | Emphasized |
|---|---|---|---|
| Large Title | Regular | 34 / 41 | Bold |
| Title 1 | Regular | 28 / 34 | Bold |
| Title 2 | Regular | 22 / 28 | Bold |
| Title 3 | Regular | 20 / 25 | Semibold |
| Headline | Semibold | 17 / 22 | Semibold |
| Body | Regular | 17 / 22 | Semibold |
| Callout | Regular | 16 / 21 | Semibold |
| Subhead | Regular | 15 / 20 | Semibold |
| Footnote | Regular | 13 / 18 | Semibold |
| Caption 1 | Regular | 12 / 16 | Semibold |
| Caption 2 | Regular | 11 / 13 | Semibold |

Body runs from 14 pt (xSmall) to 23 pt (xxxLarge) and 53 pt (AX5). With a custom typeface, start from these sizes and make it scale with Dynamic Type too. Test at xxxLarge and AX5: stack inline items, let rows grow, keep truncation to a minimum.

### App icons

| Platform | Canvas | Mask | Notes |
|---|---|---|---|
| iOS, iPadOS, macOS | 1024×1024 px, square, layered | System rounds the corners | Build in Icon Composer. Provide default, dark, clear and tinted appearances (the system generates missing ones) |
| watchOS | 1088×1088 px | Circular | Avoid a pure black background |
| visionOS | 1024×1024 px, layered (3D) | Circular | Background plus one or two layers |
| tvOS | 800×480 px, 2 to 5 parallax layers | Rounded rectangle | Keep a safe zone; focus scaling crops edges |

Never pre-round corners or pre-apply masks, shadows or glows; the system adds them. Keep the motif centered. Color: sRGB or Display P3.

## 4. Android / Material 3

### Breakpoints (formerly window size classes)

| Class | Width (dp) | Typical | Panes | Navigation | Margin · spacer |
|---|---|---|---|---|---|
| **Compact** | < 600 | Phone portrait | 1 | Navigation bar (or modal expanded rail) | 16 dp |
| **Medium** | 600 to 839 | Tablet portrait, unfolded foldable portrait | 1 (2 only for low-density content, 50/50) | Rail for 1 pane; bar for 2 panes | 24 · 24 dp |
| **Expanded** | 840 to 1199 | Phone or tablet landscape, unfolded foldable landscape | 1 or 2 (2 recommended) | Collapsed or expanded rail | 24 · 24 dp; fixed pane 360 dp |
| **Large** | 1200 to 1599 | Large tablet, desktop | 2 recommended | Rail | 24 · 24 dp; fixed pane 412 dp |
| **Extra-large** | ≥ 1600 | Desktop, ultra-wide | 1 to 3 (third = side sheet, ≤ 400 dp) | Expanded rail | 24 · 24 dp |

Height classes: compact < 480 dp, medium 480 to 899 dp, expanded ≥ 900 dp. Most scrolling layouts never need them. Keep text at 40 to 60 characters per line at every breakpoint. M3 no longer fixes column counts; it places rails and panes on rulers. When a column grid helps, use the Material 2 grid: 4 columns below 600 dp (16 dp margins), 8 columns at 600 to 904 (32 dp margins), 12 columns from 905 (840 dp body, then flexible margins up to 200 dp; 1040 dp body from 1440).

### Components (M3 Expressive, current)

| Component | Size (dp) | Notes |
|---|---|---|
| Top app bar, small | 64 high | Leading or centered title (center-aligned bar merged into small) |
| Top app bar, medium flexible | 112 expanded (136 with subtitle) → 64 collapsed | Replaces baseline medium (112) |
| Top app bar, large flexible | 120 expanded (152 with subtitle) → 64 collapsed | Replaces baseline large (152) |
| Navigation bar (flexible) | 64 high | Baseline bar was 80. 3 to 5 equal destinations; compact and medium |
| Navigation rail, collapsed | 96 wide (narrow 80) | Medium and up |
| Navigation rail, expanded | 220 to 360 wide | Replaces the navigation drawer (360 wide, no longer recommended) |
| FAB | 56 (icon 24) | Most important action on the screen |
| Medium FAB | 80 (icon 28) | New in Expressive |
| Large FAB | 96 (icon 32) | Small FAB (40) is no longer recommended |
| Touch target | **≥ 48×48** | Visual can be smaller (a 24 dp icon) if the target is 48; keep targets separated |
| Adaptive launcher icon | 108×108 layers | Logo 48 to 66 dp; only the inner 66×66 is never masked |

### Type scale (Roboto baseline, sp)

| Role | Large | Medium | Small | Weight |
|---|---|---|---|---|
| Display | 57 / 64 | 45 / 52 | 36 / 44 | Regular |
| Headline | 32 / 40 | 28 / 36 | 24 / 32 | Regular |
| Title | 22 / 28 | 16 / 24 | 14 / 20 | Regular (L), Medium (M, S) |
| Body | 16 / 24 | 14 / 20 | 12 / 16 | Regular |
| Label | 14 / 20 | 12 / 16 | 11 / 16 | Medium |

Size / line height. Map a custom style's faces onto these roles instead of inventing a parallel scale; keep text in sp so it follows the user's font size.

## 5. Web

### Breakpoints

Set breakpoints where the content breaks, not where devices are: start at 320, widen until the layout strains, add a breakpoint there. Write them in rem, mobile-first (`min-width`). Use container queries for components that live in different-width slots (Tailwind's run from `@3xs` 16rem/256 to `@7xl` 80rem/1280). If the project already uses one of these systems, keep its breakpoints; never mix two sets.

| System | sm | md | lg | xl | 2xl / xxl |
|---|---|---|---|---|---|
| Tailwind v4 | 40rem (640) | 48rem (768) | 64rem (1024) | 80rem (1280) | 96rem (1536) |
| Bootstrap 5.3 | 576 | 768 | 992 | 1200 | 1400 |
| Material 3 | none | 600 | 840 | 1200 | 1600 |

### Containers and columns

- **Tailwind `container`:** `width: 100%` plus a `max-width` equal to the current breakpoint (640 → 1536). It neither centers nor pads: add `mx-auto px-4` (or the style's margin token).
- **Bootstrap `.container`:** 540 / 720 / 960 / 1140 / 1320 px at sm-xxl; gutter 1.5rem (24px).
- **Your own:** derive the max width from the content. Long-form text caps at the measure; app shells and grids usually stop between 1200 and 1440.

Typical column grid (Material 2 grid, Material 3 margins, Bootstrap gutter); keep gutters clearly narrower than columns:

| Range | Columns | Outer margin | Gutter |
|---|---|---|---|
| Mobile (< 600) | 4 | 16 | 16 |
| Tablet (600 to 904) | 8 | 24 to 32 | 24 |
| Desktop (≥ 905) | 12 | Flexible; body capped (~1040 to 1320) | 24 |

### Viewport and safe areas

- Use `<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">`.
- Never add `user-scalable=no` or `maximum-scale=1`: it blocks zoom, and WCAG requires text to resize to 200%.
- `viewport-fit=cover` lets the page fill the display under notches and the home indicator; then pad fixed and edge UI with the insets:

```css
.top-bar    { padding-top: env(safe-area-inset-top, 0px); }
.bottom-nav { padding-bottom: max(16px, env(safe-area-inset-bottom, 0px)); }
.full-bleed { padding-inline: max(16px, env(safe-area-inset-left, 0px)) max(16px, env(safe-area-inset-right, 0px)); }
```

### Text and measure

- Body text 1rem (16px, the browser default) or larger; size type in rem so user font settings apply.
- Measure: at most 80 characters per line (WCAG 1.4.8); 40 to 60 for UI text (Material). Set `max-width` in `ch` on text blocks, then count real characters at the widest breakpoint. No horizontal scrolling at 320 CSS px (WCAG 1.4.10 Reflow).

### Tap targets

| Level | Size | Source |
|---|---|---|
| Minimum (AA) | **24×24 CSS px**, or an undersized target whose 24 px circle doesn't overlap another target | WCAG 2.2 SC 2.5.8 |
| Enhanced (AAA) | 44×44 CSS px | WCAG 2.2 SC 2.5.5 |
| Recommended for touch | **44 to 48 px** for every primary control | Apple 44 pt, Material 48 dp |

Enlarge the hit area with padding or a pseudo-element; keep the visual size the style wants.

### Responsive images

```html
<img src="hero-800.jpg"
     srcset="hero-480.jpg 480w, hero-800.jpg 800w, hero-1600.jpg 1600w"
     sizes="(width <= 600px) 100vw, 50vw"
     width="1600" height="900" alt="[describe the image]">
```

- `w` descriptors give each file's real width; `sizes` gives the slot width (lengths like `100vw`, never `%`); the browser picks the file. Order `sizes` conditions carefully: the first match wins.
- Always set `width` and `height` attributes, or reserve the box with CSS `aspect-ratio`, so nothing shifts on load (good CLS is ≤ 0.1). Provide at least 2× the slot width for high-density screens.

## 6. Assets

### Favicons and web app icons

| File | Size | Purpose |
|---|---|---|
| `favicon.ico` | 32×32 (16/32/48 inside, optional) | Fallback for browsers that don't use SVG icons |
| `favicon.svg` | Vector | Modern browsers |
| `apple-touch-icon.png` | 180×180 | iOS home screen; Apple's touch-icon size for @3x iPhones |
| Manifest icon | 192×192 PNG | Required by Chromium |
| Manifest icon | 512×512 PNG | Required by Chromium; install and splash |
| Maskable manifest icon | 512×512 PNG, `"purpose": "maskable"` | Keep the motif inside the center circle (radius 40% of the width); fill the rest with background. Ship it as its own entry, not the 512 `any` icon |

```html
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/manifest.webmanifest">
```

### Social share images

| Platform | Size | Notes |
|---|---|---|
| Open Graph (Facebook, most link previews) | **1200×630** (1.91:1) | Minimum 600×315 for the large preview, 200×200 absolute; ≤ 8 MB |
| X `summary_large_image` | Reuse the 1200×630 image **(verify current spec)** | Keep focal content centered; edges crop |
| LinkedIn | 1200×627 is the commonly cited size **(verify)** | Same 1.91:1 image works |

Declare `og:image:width`, `og:image:height` and `og:image:alt`. Keep text large, centered and away from the edges; previews render small.

### App store graphics

| Store | Asset | Size |
|---|---|---|
| App Store | iPhone screenshots (required: Dynamic Island medium) | 1206×2622 or 1179×2556 portrait (landscape: same numbers swapped, for every row) |
| App Store | iPhone, Dynamic Island large | 1320×2868, 1290×2796 or 1260×2736 |
| App Store | iPhone, Face ID large (needed if you skip Dynamic Island large) | 1284×2778 or 1242×2688 |
| App Store | iPad 13" (required if the app runs on iPad) | 2064×2752 or 2048×2732 |
| App Store | iPhone Duo, outer / inner (optional now; required from April 2027 for apps built with the iOS 27.1 SDK or later) | 1398×2034 / 2007×2853 |
| App Store | Count and format | 1 to 10 per size; JPEG or PNG; no alpha or transparency |
| Google Play | App icon | 512×512, 32-bit PNG, ≤ 1024 KB |
| Google Play | Feature graphic | 1024×500, JPEG or 24-bit PNG, no alpha |
| Google Play | Screenshots | 320 to 3840 px per side, long side ≤ 2× short side, 2 to 8 per device type; for recommendation slots, ≥ 4 at 1080×1920 (9:16) or 1920×1080 (16:9) |

## 7. Checklist before delivering a screen

1. Frame is the stated design size in pt/dp/CSS px at 1x (iPhone 402×874, Android 411×891, iPad 820×1180, web 390 and 1440).
2. Checked at the smallest and largest targets: iPhone 360/375 and 440; Android 360 dp and the next breakpoint; web 320 and 1920.
3. Nothing interactive or readable sits under the status bar, Dynamic Island, home indicator, notch or fold; backgrounds bleed edge to edge.
4. Every touch target is ≥ 44 pt (iOS) / 48 dp (Android) / 44 px for primary web controls, never below 24 px, with space between neighbors.
5. Type comes from the platform scale; body ≥ 17 pt iOS, 16 sp Android, 16 px web; nothing below 11 pt; layout survives AX5 Dynamic Type and 200% browser zoom.
6. Spacing, sizes and line heights sit on the 4/8 grid; no stray odd values.
7. Margins match the platform: 16 compact / 24 medium and up (Material), system layout margins (iOS), container padding (web).
8. Breakpoints come from one system and from where the content breaks; no horizontal scroll at 320.
9. Text blocks stay under 80 characters per line at the widest breakpoint.
10. Images have dimensions or `aspect-ratio` and 2× sources; icons and share images exported at the sizes in § 6.

**Sources:** https://developer.apple.com/design/human-interface-guidelines/layout (current, and archived 2026-07-02 at https://web.archive.org/web/20260702060104/https://developer.apple.com/tutorials/data/design/human-interface-guidelines/layout.json) · https://developer.apple.com/design/human-interface-guidelines/typography · https://developer.apple.com/design/human-interface-guidelines/accessibility · https://developer.apple.com/design/human-interface-guidelines/tab-bars · https://developer.apple.com/design/human-interface-guidelines/toolbars · https://developer.apple.com/design/human-interface-guidelines/app-icons · https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo · https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications · https://www.apple.com/iphone-18-pro/specs/ · https://www.apple.com/iphone-17e/specs/ · https://www.apple.com/iphone-duo/specs/ · https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/ConfiguringWebApplications/ConfiguringWebApplications.html · https://m3.material.io/foundations/layout/breakpoints/overview · https://m3.material.io/foundations/layout/grids-spacing/grids · https://m3.material.io/styles/spacing/tokens · https://m3.material.io/components/app-bars/specs · https://m3.material.io/components/navigation-bar/overview · https://m3.material.io/components/navigation-drawer/overview · https://m3.material.io/components/floating-action-button/overview · https://m3.material.io/foundations/designing/structure · https://github.com/androidx/androidx/tree/androidx-main/compose/material3/material3/src/commonMain/kotlin/androidx/compose/material3/tokens · https://m2.material.io/design/layout/responsive-layout-grid.html · https://m2.material.io/design/layout/spacing-methods.html · https://developer.android.com/develop/ui/compose/layouts/adaptive/use-window-size-classes · https://developer.android.com/training/multiscreen/screendensities · https://developer.android.com/guide/topics/ui/accessibility/apps · https://developer.android.com/develop/ui/views/launch/icon_design_adaptive · https://developer.android.com/reference/kotlin/androidx/compose/ui/tooling/preview/PreviewScreenSizes · https://support.google.com/googleplay/android-developer/answer/9866151 · https://www.w3.org/TR/WCAG22/ · https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html · https://developer.mozilla.org/en-US/docs/Web/CSS/env · https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport · https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Responsive_images · https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Manifest/Reference/icons · https://web.dev/articles/add-manifest · https://web.dev/articles/maskable-icon · https://web.dev/articles/optimize-cls · https://tailwindcss.com/docs/responsive-design · https://tailwindcss.com/docs/max-width · https://getbootstrap.com/docs/5.3/layout/breakpoints/ · https://getbootstrap.com/docs/5.3/layout/containers/ · https://developers.facebook.com/docs/sharing/webmasters/images/ · https://gs.statcounter.com/screen-resolution-stats
