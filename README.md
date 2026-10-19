# Aastha Rajput — Portfolio (v2)

The Canva pages shown one after another, full width, with a magnifier.

## Deploy
Drag this whole folder onto https://app.netlify.com/drop — done. (Or push it to GitHub and
connect the repo in Netlify; no build command, publish directory `.`.)

## What's in here
- `index.html` — the site (all the code is in this one file)
- `img/01.webp … 45.webp` — the 45 Canva pages, 2400 px wide
- `img/xl/` — the same pages at 4200 px, used by the magnifier and on retina screens
- `og.jpg` — preview image when the link is shared
- `_edit/` — only needed if you change page titles or chapters (see below)

## How it behaves
- Pages sit as cards with space around and between them.
- Loading screen: the name writes itself in letter by letter, then the screen splits open onto the cover.
- Scrolling (mouse/trackpad) is smoothed; arrow keys, the ‹ › buttons and the right-hand rail glide to land each page centred.
- Every page gently zooms as it reaches the middle of the screen; project title pages drift slightly slower (parallax).
- Entering a new project flashes its name in the middle of the screen for a moment.
- Magnifier: click a page, then scroll to zoom in/out (or `+` / `−`); click again to close. The lens wobbles as it moves.
  On phones: press and hold a page.
- The cursor ring labels what you're over (Zoom, Open, Copy…) and snaps onto buttons.
- Index: project thumbnails tilt in 3D under the mouse.
- Thank-you page: the email and Behance lines underline themselves and a "Back to top" button rises in.
- Motion is switched off for visitors who have "reduce motion" turned on. No animation ever hides a page.
- Each page has its own link, e.g. `/#p12` opens Fables of Mithila.

## Updating
- **Changed a page in Canva?** Download it as PNG and replace `img/NN.webp` and `img/xl/NN.webp`
  (2400 px and 4200 px wide, WebP). Or ask Claude to redo the conversion.
- **Added or removed pages / renamed a section?** Edit the lists at the top of `_edit/build.py`,
  then run `python3 _edit/build.py` — it rewrites `index.html`.
- **Clickable email/Behance/LinkedIn areas** on pages 2 and 45 are set in `HOTSPOTS` in `_edit/build.py`.
