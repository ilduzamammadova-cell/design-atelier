---
id: windows-95
name: Windows 95
type: system
discipline: [ui, ux]
era: 1995 to 2001
origin: Redmond, USA
lineage: [nextstep, classic-macintosh]
tags:
  mood: [utilitarian, sturdy, plainspoken, nostalgic]
  topics: [productivity, admin tools, forms, retro products, games]
axes: {order: 8, density: 6, ornament: 2, warmth: 4, contrast: 6, geometry: 9, chroma: 2, typevoice: 2, energy: 2, hand: 1, play: 3, era: 4}
---

# Windows 95

**Essence:** Mass-market computing in chiselled grey: every control a bevelled block, every task one labelled click from a single Start button.

## Genes

| Gene | The idea | In UI / product terms |
|---|---|---|
| G1 · Chiselled bevel | Controls are raised grey blocks with a two-step bevel (white + light grey on top/left, black + dark grey on bottom/right); pressing inverts the bevel and nudges content 1 px. | Bevel tokens: `--hi: #FFF; --hi2: #DFDFDF; --lo: #808080; --lo2: #000`. Pressed state swaps them and translates the label `1px 1px`. No blur shadows, no radius, tactility from edges alone. |
| G2 · One labelled front door | The Start button, a word plus a logo, bottom-left, was added because usability tests showed new users did not know where to begin. | One persistent, text-labelled launcher in a corner that opens a cascading hierarchical menu of everything. The label is a plain verb, never just an icon. |
| G3 · Taskbar of open things | Every open window becomes an equal-width button in a strip; the active one looks pressed in. | A persistent strip listing open documents/tabs as labelled buttons; active item rendered inset (inverted bevel). Users always see what is open. |
| G4 · Everything has Properties | Right-click on any object gives a context menu whose last entry is Properties. | Secondary click works on every object; its menu ends with "Properties…" opening a tabbed sheet with OK / Cancel / Apply bottom-right. |
| G5 · Dense bitmap type and dotted focus | MS Sans Serif at 8 point, non-antialiased, bold for titles; keyboard focus shown by a 1 px dotted rectangle around the label. | 11 px UI type, row heights ~18 to 20 px; focus = `outline: 1px dotted` hugging the text, not a glow ring. Keyboard access to everything. |
| G6 · Solid title bars, square controls | The active window has a solid navy title bar with white bold text; minimise/maximise/close are small bevelled squares at the right. | Window headers in one dark accent with white 11 px bold label; three 16×14 square controls; inactive headers drop to mid-grey. |

## Visual facts

- **Color:** face grey `#C0C0C0`, shadow `#808080`, highlight `#FFFFFF`, title navy `#000080`, desktop teal `#008080` (the standard VGA values of the default scheme).
- **Type:** MS Sans Serif (bitmap) for UI; Marlett for window-control glyphs. Free: **Pixelify Sans** for display; open-source pixel recreations used by the **98.css** project for faithful UI.
- **Form:** rectangles only; 1 px etched separators (dark line + white line); sunken white fields for inputs; scroll bars with bevelled arrow buttons.
- **Composition:** taskbar at bottom, desktop icons in a left column, dialogs with tabs and right-aligned button rows.

## Attitude

Windows 95 was designed through repeated usability testing for people who had never used a mouse (documented by Kent Sullivan, CHI 1996). Virginia Howlett's team gave it its 3D visual language. Its ethic: discoverability over elegance, explicit labels over clever metaphors. Borrow it when you want an interface that looks *operable*, every affordance visibly pressable.

## Blends

- **Amplifies:** `web-1-vernacular`, `brutalist-web`, `bloomberg-terminal`, honest, utilitarian chrome.
- **Productive tension with:** `swiss-international`, bevelled tactility locked to a rigorous typographic grid gives a crisp "operable Swiss" interface.
- **Clashes with:** `ios-7-flat`, hairline glyphs and translucent bars next to chunky bevels look broken rather than mixed.

## Don't copy

- The Windows logo/flag, the Start button artwork, the "Clouds" wallpaper, the system icon set (My Computer, Recycle Bin, etc.), the startup sound.

## Study

- Kent Sullivan, "The Windows 95 User Interface: A Case Study in Usability Engineering," CHI 1996.
- Microsoft, *The Windows Interface Guidelines for Software Design* (Microsoft Press, 1995).
- GUIdebook gallery, Windows 95 screenshots; 98.css (Jordan Scales), open-source CSS recreation, useful for studying bevel tokens.
