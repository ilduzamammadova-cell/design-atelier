---
id: game-ui
name: Game UI (diegetic HUDs & expressive menus)
type: movement
discipline: [ui, ux, graphic]
era: 1980s to present
origin: Worldwide, Japan, USA, Europe
lineage: []
tags:
  mood: [immersive, kinetic, dramatic, responsive]
  topics: [games, fitness, onboarding, gamified tools, AR/VR, maps]
axes: {order: 6, density: 6, ornament: 6, warmth: 5, contrast: 8, geometry: 6, chroma: 7, typevoice: 7, energy: 8, hand: 3, play: 9, era: 7}
---

# Game UI (diegetic HUDs & expressive menus)

**Essence:** Interfaces that live inside the fiction and the feel, health worn on a character's spine, menus that strike poses, feedback you can almost feel in your hands.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Diegetic status | Information placed inside the world: *Dead Space* (2008) showed health on the suit's spine; *Metroid Prime* (2002) framed the HUD as the inside of a visor; *Fallout 3*'s Pip-Boy was a device on the wrist. | Show status on the object it belongs to: upload progress filling the file's own thumbnail, battery on the device illustration, deadline as the card's colour. Avoid separate status panels. |
| G2 · Menus with attitude | *Persona 5* (2016; menus by Masayoshi Suto) made every menu kinetic and stylised, tilted panels, red/black/white, cut-out mixed typography inspired by punk ransom notes. | Menu items at alternating angles (−8°/+6°), selection snaps with a 120 ms overshoot; three-colour palette; headings collaged from 2 to 3 contrasting faces. Personality lives in navigation itself. |
| G3 · Juice | Game feel: amplified feedback, hit-stop, screen shake, particles, sound, haptics, makes every action satisfying. | For success actions: 60 ms hold, scale punch 1 → 1.12 → 1 with spring, a small particle burst, a haptic tick. Grade intensity by importance; respect reduced-motion settings. |
| G4 · World-anchored markers | Spatial UI pins labels and waypoints to objects, with edge arrows when they go off-screen. | In maps, canvases and 3D views, annotations attach to objects and show distance; off-screen items clamp to the viewport edge as arrows. |
| G5 · HUD that gets out of the way | Many games fade HUD elements when idle and bring them back when values change. | Secondary chrome fades to 0 after ~3 s idle and returns on input or when its value changes; critical alerts never fade. |
| G6 · Glanceable under stress | Big numbers, colour-coded states, unmistakable silhouettes and TV-safe margins let players read status in a fraction of a second. | Critical values ≥24 px with tabular numerals; strict colour semantics (red = danger only); 5% safe margin on all edges; each icon recognisable by silhouette alone. |

## Visual facts

- **Color:** varies by fiction, Persona 5's red (~`#E60012`), black and white; Pip-Boy phosphor green (~`#1AFF80`) on black; cool hologram blues (~`#6AD3FF`) in sci-fi HUDs.
- **Type:** condensed display grotesques for numbers, bitmap faces for retro games, collaged mixed type for stylised menus. Free: **Bebas Neue**, **Anton**, **Rubik Mono One**, **Press Start 2P**.
- **Form:** angled panels, brackets, radial meters, glowing lines, comic-style bursts.
- **Composition:** corners and edges hold persistent HUD; centre kept clear for action; full-screen menus with strong diagonal composition.

## Attitude

Game designers treat interface as part of the experience, not a layer on top of it. Erik Fagerholt and Magnus Lorentzon's thesis *Beyond the HUD* (2009) mapped the field as diegetic, non-diegetic, spatial and meta interfaces. The belief to borrow: feedback and feel are as important as information, and an interface can carry emotion.

## Blends

- **Amplifies:** `flash-era-web`, `constructivism`, `demoscene-and-tracker-ui`, diagonals, energy, technical showmanship.
- **Productive tension with:** `swiss-international`, rational grid and data tables animated with game juice: dashboards that feel alive but stay legible.
- **Clashes with:** `kenya-hara`, emptiness and silence cannot coexist with juice and shake; the blend reads as noise.

## Don't copy

- Persona 5's menus, calling cards and logo; the Pip-Boy device and its mascot; the Dead Space RIG; any game's characters, logos and HUD artwork.

## Study

- Game UI Database (gameuidatabase.com, Edd Coates, 2020, ), thousands of searchable game screens.
- Erik Fagerholt & Magnus Lorentzon, *Beyond the HUD* (Chalmers University of Technology, 2009).
- GDC talks on game feel and UI (gdcvault.com); Steve Swink, *Game Feel* (2008).
