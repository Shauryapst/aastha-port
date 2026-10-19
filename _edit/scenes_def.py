"""Process scenes: scroll-driven animations placed after a page (used by build.py)."""
import json, pathlib, html
esc = html.escape
SCENE_META = json.loads((pathlib.Path(__file__).resolve().parent.parent / "img" / "scene" / "scenes.json").read_text())

UNBUILT_NOTE = ("The design aims to translate the microscopic beauty of algae into modern surface techniques. "
                "The focus is on capturing the textures, forms and translucency seen in algae strands and colonies — "
                "celebrating the balance between nature's simplicity and its complex patterns, and showing how unseen "
                "ecosystems can inspire creative design.")

# (after_page, id, type, chapter no., project, title, subtitle, spec, steps, cfg)
# steps: (from, to, name, detail) in scene progress 0..1
SCENES = [
    (4, "unbuilt", "moodboard", "01", "Unbuilt", "The moodboard",
     "Algae, coral and underwater textures for Sarita Handa's home textiles.",
     "Client: Sarita Handa · bedding, cushions, soft furnishings",
     [(0, .34, "Inspiration gathers", "Images, textures and samples arrive, each at its own pace."),
      (.34, .6, "Colour board", "Eight Pantone TCX colours, drawn from the algae."),
      (.6, .7, "Keywords", "Growth · organic · natural rhythm · underwater textures."),
      (.7, 1, "Concept", "The note that ties the board together.")],
     {}),
    (12, "fables", "sketch", "02", "Fables of Mithila", "Sketch to garment",
     "A Madhubani-printed kaftan, from the first pen line to the finished coordinate set.",
     "Madhubani line work · print repeat 15 × 15 in",
     [(0, .34, "Sketch", "The flat sketch is drawn line by line."),
      (.34, .64, "Colour & print", "Colour and the Panchatantra print fill the silhouette."),
      (.64, .8, "The garment", "The finished kaftan."),
      (.8, 1, "Coordinates", "The full set of print coordinates.")],
     {"figure": "img/scene/fables-figure.webp", "lineup": "img/scene/fables-lineup.webp"}),
    (19, "saandra", "motif", "03", "Saandra", "Motif to print",
     "A jharokha-inspired motif, repeated and rotated into a dense, detailed print.",
     "Repeat 12 × 12 in · Spring / Summer ready-to-wear",
     [(0, .2, "One hand-drawn motif", "Starting from a single motif."),
      (.2, .5, "Duplicate & rotate", "Copies turn and settle into a half-drop."),
      (.5, .78, "Repeat unit", "The 12 × 12 in unit tiles seamlessly."),
      (.78, 1, "The finished print", "Saandra on its marigold ground.")],
     {"motif": "img/scene/saandra-motif.webp", "print": "img/scene/saandra-print.webp", "ground": "#f8b931",
      "rotate": "alt", "unit": "Repeat 12 × 12 in", "cardLabel": "Saandra — final print", "zoomTo": .4, "gapX": 1.12, "gapY": 1.04}),
    (25, "seed", "motif", "04", "Seed Scriptures", "Motif to print",
     "The pomegranate — from an ink sketch to a final motif to a repeating print.",
     "Repeat 8 × 8 in · half-drop",
     [(0, .2, "From sketch to motif", "An ink sketch becomes the final coloured motif."),
      (.2, .5, "Duplicate", "The pomegranate is repeated in a half-drop."),
      (.5, .78, "Repeat unit", "The 8 × 8 in unit on a cream ground."),
      (.78, 1, "The finished print", "As it appears on the collection.")],
     {"motif": "img/scene/seed-motif.webp", "sketch": "img/scene/seed-motif-sketch.webp", "print": "img/scene/seed-print.webp",
      "ground": "#fbf6cf", "rotate": "none", "unit": "Repeat 8 × 8 in", "cardLabel": "Seed Scriptures — final print", "zoomTo": .36, "gapX": 1.06, "gapY": 1.0}),
    (33, "roundup", "weave", "05", "Roundup", "Weave formation",
     "Woody's cowboy world in yarn — bold yellow, denim blue and ivory in a twill check.",
     "Acrylic yarn · 30s count · 24 reed · ~384 ends · 2/2 twill",
     [(0, .2, "Warp", "Lengthwise threads are set on the loom."),
      (.2, .48, "Weft", "The crosswise thread travels over, under, over…"),
      (.48, .7, "Twill & check", "Diagonal ribs and colour blocks appear."),
      (.7, 1, "The finished muffler", "Woven, finished and worn.")],
     {"pattern": "twill", "band": 4, "warp": ["#fffbec", "#04345c", "#fffbec", "#2a8fe6", "#ffd230", "#2a8fe6"],
      "weft": ["#ffd230", "#fffbec", "#04345c", "#fffbec", "#2a8fe6"], "photo": "img/scene/roundup-photo.webp"}),
    (38, "kargha", "weave", "06", "Kargha", "Weave formation",
     "Colour blocks and geometric diamonds, woven into a waist belt.",
     "Woven belt · geometry · repetition · colour",
     [(0, .2, "Warp", "Bands of red, marigold, pink and olive are set up."),
      (.2, .48, "Weft", "The weft travels over and under the warp."),
      (.48, .7, "Diamonds", "Floating threads lift into diamond motifs."),
      (.7, 1, "The finished belt", "Kargha, off the loom.")],
     {"pattern": "kargha", "band": 12, "warp": ["#d8322a", "#e8c22a", "#f1a0ae", "#55691f", "#e8c22a"],
      "weft": ["#f3ead2", "#f3ead2", "#55691f"], "photo": "img/scene/kargha-photo.webp"}),
]
AFTER = {sc[0]: sc for sc in SCENES}


def moodboard_html():
    mb = SCENE_META["moodboard"]
    # file, left%, top%, width%, rotation, enter-from dx%, dy%, start, end
    layout = [("mb-algae.webp", 0, 4, 44, -3, -150, 10, .02, .2), ("mb-radial.webp", 36, 0, 40, 4, 0, -170, .05, .28),
              ("mb-coral.webp", 70, 8, 30, 3, 150, -40, .03, .22), ("mb-cells.webp", 54, 34, 24, -2, 170, 30, .1, .34),
              ("mb-lines.webp", 26, 46, 32, -5, -20, 170, .12, .3), ("mb-weed.webp", 2, 58, 40, 2, -160, 80, .16, .36)]
    pieces = "".join(
        f'<figure class="mb-piece" style="left:{l}%;top:{t}%;width:{w}%" data-r="{r}" data-dx="{dx}" data-dy="{dy}" data-a="{a}" data-b="{b}">'
        f'<img data-src="img/scene/{f}" alt="" width="{mb[f]["w"]}" height="{mb[f]["h"]}"></figure>'
        for f, l, t, w, r, dx, dy, a, b in layout)
    chips = "".join(f'<span class="mb-chip" style="--c:{c["hex"]}"><i></i><small>{c["code"]}</small></span>'
                    for c in SCENE_META["unbuiltPalette"])
    words = "".join(f'<span class="mb-word">{w}</span>' for w in ["Growth", "Organic", "Natural rhythm", "Underwater textures"])
    return (f'<div class="mb"><div class="mb-collage">{pieces}</div><div class="mb-info">'
            f'<div class="mb-pal" aria-label="Colour board">{chips}</div><p class="mb-words">{words}</p>'
            f'<div class="mb-note"><h3>Concept</h3><p class="mb-note-text">{esc(UNBUILT_NOTE)}</p></div></div></div>')


def scene_html(sc):
    after, sid, typ, no, proj, title, sub, spec, steps, cfg = sc
    lis = "".join(f'<li data-a="{a}" data-b="{b}"><b>{k + 1:02d}</b><span>{esc(n)}</span><em>{esc(d)}</em></li>'
                  for k, (a, b, n, d) in enumerate(steps))
    stage = moodboard_html() if typ == "moodboard" else ""
    return (f'  <section class="scene" id="s-{sid}" data-scene="{typ}" data-title="{esc(title)}" '
            f"data-cfg='{json.dumps(cfg)}' aria-label=\"{esc(proj)} — {esc(title)}\">\n"
            f'    <div class="sc-pin">\n      <div class="sc-cap">\n'
            f'        <span class="sc-kick">{no} · {esc(proj)}</span>\n'
            f'        <h2 class="sc-title">{esc(title)}</h2>\n        <p class="sc-sub">{esc(sub)}</p>\n'
            f'        <ol class="sc-steps">{lis}</ol>\n        <div class="sc-bar"><i></i></div>\n'
            f'        <p class="sc-spec">{esc(spec)}</p>\n      </div>\n'
            f'      <div class="sc-stage">{stage}</div>\n    </div>\n  </section>')


def scene_data():
    return json.dumps({k: SCENE_META[k] for k in ("fablesFigure", "fablesLineup", "fablesLines")}, separators=(",", ":"))
