---
id: ivan-sutherland
name: Ivan Sutherland
type: designer
discipline: [ux, ui]
era: 1962 to 1970s (Sketchpad 1962 to 63; head-mounted display 1968)
origin: MIT Lincoln Laboratory, Massachusetts; University of Utah, Salt Lake City, USA
lineage: []
tags:
  mood: [direct, precise, constructive, visionary]
  topics: [creative tools, CAD, design software, spatial computing, graphics engines]
axes: {order: 8, density: 4, ornament: 0, warmth: 3, contrast: 7, geometry: 9, chroma: 0, typevoice: 1, energy: 4, hand: 2, play: 4, era: 9}
---

# Ivan Sutherland (b. 1938)

**Essence:** Draw on the machine and let it keep your intentions, you state relationships, the computer maintains them, and the screen becomes a window you can step through.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Draw where the thing is | Sketchpad (PhD thesis, MIT, 1963) let a person draw straight onto the TX-2's display with a light pen, graphics as a conversation with the machine, not a batch job. | Every object on a canvas is selected, moved and resized where it is drawn; the inspector panel is secondary and mirrors the direct edit. While dragging, geometry updates every frame with no "apply" step. |
| G2 · Constraints, not coordinates | Users declared conditions, these lines parallel, this length equal to that, and the program solved the drawing to satisfy them; conditions could be combined and applied in one step. | Layout and diagram tools where the user pins relationships ("same width as", "centred on", "16px from", "parallel to") instead of typing x/y. Selected objects show constraint badges; relations survive content changes and can be saved as reusable composite rules. |
| G3 · Master and instances | Define a symbol once and place it many times; change the definition and every occurrence updates. | Component/instance model throughout: repeated elements are instances with explicit, visible overrides (a dot on overridden properties); "edit master" propagates; "detach" is deliberate and logged. |
| G4 · The ultimate display | His 1965 essay imagined a display as a window into a world whose physics the computer controls, including physics that does not exist. | In spatial or canvas products, decide which real-world rules to keep (inertia, occlusion, gravity) and which to break for clarity (pass-through objects, infinite zoom, undoable time). Write the rule list down as part of the design spec. |
| G5 · View follows the body | The 1968 head-mounted display (built with students including Bob Sproull) redrew wireframe scenes as the wearer's head moved, content fixed in the world, not on the glass. | In AR/VR and large canvases, anchor content to world or document coordinates, not to the viewport; only system chrome is screen-locked. Navigation by moving the viewpoint (pan, zoom, head pose), never by paging. |

## Visual facts

- **Color:** none by choice, phosphor line on black: CRT black ≈ #050807, phosphor ≈ #CFE8D8, dim construction lines ≈ #4F6B5E.
- **Type:** almost none; labels and numbers only → free: IBM Plex Mono or JetBrains Mono.
- **Form:** thin vector lines, points, arcs, constraint marks, wireframe solids; no fills.
- **Composition:** a drawing surface larger than the screen, explored by zoom and pan; the instrument disappears around the drawing.

## Attitude

Sutherland treated the computer as a partner in making things, and the display as a way into a world rather than a printout. He valued working systems over speculation, then let the systems provoke bigger speculation. Through his Utah students (among them John Warnock, Jim Clark and Ed Catmull) his ideas became PostScript, graphics workstations and computer animation; he received the Turing Award in 1988.

## Blends

- **Amplifies:** `douglas-engelbart`, `alan-kay`, `bret-victor`, direct manipulation, augmentation and live, explorable systems.
- **Productive tension with:** `charles-and-ray-eames`, constraint-driven precision animated by the Eameses' warmth and curiosity: tools that feel like toys but compute like CAD.
- **Clashes with:** `ios-skeuomorphism`, Sketchpad's power lies in abstract, editable structure; dressing it as leather and paper hides the relationships the user is meant to manipulate.

## Don't copy

The Sketchpad and head-mounted display photographs and film footage (MIT Lincoln Laboratory, University of Utah) as interface imagery; the 1968 apparatus as a product silhouette. Take constraints, instances and world-anchoring.

## Study

- *Sketchpad: A Man-Machine Graphical Communication System* (thesis, 1963); reissued as Cambridge Computer Laboratory Technical Report UCAM-CL-TR-574 (2003), with a preface by Alan Blackwell and Kerry Rodden: https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-574.html
- "The Ultimate Display" (Proceedings of the IFIP Congress, 1965).
- "A head-mounted three dimensional display" (AFIPS Fall Joint Computer Conference, 1968).
- ACM A.M. Turing Award profile (1988): https://amturing.acm.org
- Alan Kay's lectures demonstrating Sketchpad footage, e.g. "Doing with Images Makes Symbols" (1987).
