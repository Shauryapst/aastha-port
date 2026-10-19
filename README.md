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
- Desktop: scroll through the pages; click any page to open the magnifier, click again to close.
  `+` / `−` (or Shift + scroll) change the zoom. Arrow keys go page by page. "Index" jumps to a project.
- Phones held upright: each page fills the screen height — swipe sideways to read it,
  press and hold anywhere to magnify.
- No entrance animations — every page is a plain image, loaded as you approach it.
- Each page has its own link, e.g. `/#p12` opens Fables of Mithila.

## Updating
- **Changed a page in Canva?** Download it as PNG and replace `img/NN.webp` and `img/xl/NN.webp`
  (2400 px and 4200 px wide, WebP). Or ask Claude to redo the conversion.
- **Added or removed pages / renamed a section?** Edit the lists at the top of `_edit/build.py`,
  then run `python3 _edit/build.py` — it rewrites `index.html`.
- **Clickable email/Behance/LinkedIn areas** on pages 2 and 45 are set in `HOTSPOTS` in `_edit/build.py`.
