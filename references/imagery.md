# Imagery — photography and illustration

Every design this skill delivers carries real visual material: photographs, illustrations, product images, diagrams. A grey box with "Image" in it is not a design, it is a wireframe. Images are also where a style becomes recognisable fastest — and where generic stock and trend illustration undo everything else.

Decide imagery from the style, the same way as type and color: each image choice traces to a law or gene.

## 1. Choose the kind of image

| The page needs to… | Use |
|---|---|
| Show a real product, place, person or result | **Photography** (the client's own first) |
| Explain an idea, process or something that doesn't exist yet | **Illustration** or **diagram** |
| Carry mood where nothing literal fits | **Illustration**, texture, or a type-as-image moment |
| Prove something (data, before/after) | **Diagram / chart** in the style, never decoration |

Mixing photography and illustration on one page is fine when each has a clear job; the style spec says which job belongs to which.

## 2. Sourcing order

1. **The person's own assets** — product shots, team, places, past work. Ask for them early; list exactly what is needed (subject, orientation, minimum size).
2. **Generated images** when an image-generation tool is available in the session (an MCP image generator, Figma's image tools, etc.). Build prompts from the style spec (§ 4). Label generated stand-ins for real things — a product, a team, a venue — as `[placeholder: replace with real photo of …]`; never present them as the real thing.
3. **Licensed stock** — Unsplash and Pexels allow free commercial use under their own licences; check the licence page for each source and keep a credits list. Choose images that obey the art direction (§ 3), then grade them to the palette.
4. **Hand-built illustration / SVG** — when no generator is available, or when the style's laws call for drawn, geometric or diagrammatic imagery (§ 5).

Never ship a page with empty image frames. When the person's real photos are missing, fill every photo slot with a **stand-in** — stock or generated, graded to the art direction — and mark it visibly and in the alt text as a stand-in ("sample photo — replace with your own bread"). The stand-in shows what the real photo should look like; the label keeps it honest. Use a styled empty placeholder only when no stock or generation is possible at all (offline), and list the missing assets either way.

## 3. Art direction (write it into the style spec)

Define these once per style; every image must obey them:

- **Subject matter:** what is shown and what never is (e.g. "hands and tools, never faces at desks").
- **Light:** time of day, hard or soft, direction, warm or cool — derived from the palette.
- **Color grade:** shift photos toward the palette (a duotone, a shared tint, lifted blacks, restrained saturation). One grade for all images.
- **Composition & crop:** distance (close detail vs wide context), horizon placement, negative space for type, crops that snap to grid columns, consistent aspect ratios (pick 2–3: e.g. 4:5, 3:2, 16:9).
- **Texture & finish:** grain or clean, matte or glossy — consistent with the style's `hand` axis.
- **People:** real diversity of age, body, skin and ability that fits the audience; candid over posed; consent and rights for any real person.
- **Avoid:** the stock clichés — pointing at laptops, handshake, headset smile, lightbulb, puzzle pieces, glowing brains, abstract 3D blobs.

## 4. Generating images from the style

Build every prompt from one fixed skeleton so the set stays consistent:

```
[subject, specific and concrete], [setting],
[light: from art direction], [lens/viewpoint: e.g. 50mm eye level / overhead flat lay],
[palette: 3–5 named colors from tokens], [material/texture: from the style's genes],
[composition: where empty space must be for type], [aspect ratio]
Avoid: [the style's slop tells + generic stock clichés + any saturated trend surfaces]
```

- Generate a small batch, pick the one that obeys the art direction best, and reuse its seed or pass it as a reference image for the rest, when the tool supports it.
- Check every generated image for artefacts (hands, text, logos, distorted objects) and for anything resembling a real brand or a living artist's signature work. Regenerate rather than retouch heavily.
- Never generate imagery in the manner of a named living artist; describe the visual qualities instead (the genes).
- Record the final prompts in the style spec so future images match.

## 5. Illustration system

An illustration style is a small design system. Derive it from the style's genes — not from what illustration currently looks like on the internet.

| Decide | From | Examples of decisions |
|---|---|---|
| **Construction** | `geometry`, `hand` axes; Spine gene | ruler-and-compass shapes only / cut-paper edges / single continuous line / pixel grid |
| **Line** | type stem weight, icon stroke | one stroke weight shared with icons; or no outlines, only fills |
| **Color** | palette tokens | max 3 colors + paper; no gradients unless a law allows them |
| **Figures** | audience, `play` axis | none / abstract figures with real proportions / objects instead of people |
| **Space** | `order`, `density` | flat frontal / one-point perspective / diagram space — never isometric by default |
| **Detail** | `ornament` axis | what disappears at small sizes |

Saturated illustration trends to avoid unless deliberately transformed: corporate-Memphis figures (`atlas/trends/corporate-memphis-illustration.md`), 3D clay and blob renders, isometric scenes, gradient mesh blobs.

**Producing illustrations:**
- **SVG by hand or by code** for geometric, diagrammatic or cut-paper styles: build on the spacing grid, use token colors as `fill`/`stroke`, keep `viewBox` clean, name groups by meaning. Generative SVG (patterns, scatter, noise) is fine when its rules come from a gene.
- **Generated raster** for painterly, photographic or textured styles (§ 4).
- **In Figma:** build illustrations as components when reused (spot illustrations for empty states, onboarding, errors), with color bound to variables so they follow light/dark modes.

**Where illustrations are typically needed** — produce them, don't leave them blank: hero or key visual, empty states, onboarding steps, error and success states, feature explanations, 404.

## 6. Images in code

- Serve AVIF/WebP with a fallback; `srcset` and `sizes` for responsive images; set `width`/`height` or `aspect-ratio` to prevent layout shift; `loading="lazy"` below the fold.
- Every meaningful image has `alt` describing its content and purpose; decorative images have `alt=""`.
- SVG illustrations inline when they need to follow the theme (`currentColor`, CSS variables); otherwise as files.
- Keep credits and licences in the repository (`/credits.md` or similar).

## 7. Check

- [ ] No empty or grey image frames anywhere.
- [ ] Every image obeys the art direction: subject, light, grade, crop, texture.
- [ ] Generated stand-ins for real things are labelled as placeholders.
- [ ] Stock images have a recorded source and licence.
- [ ] Illustrations share construction, line and palette with the icons and the style laws.
- [ ] No stock clichés, no saturated illustration trends, nothing imitating a living artist.
- [ ] Alt text written; responsive formats and sizes set.
