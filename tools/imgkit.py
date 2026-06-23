#!/usr/bin/env python3
"""imgkit - post-process AI-generated images for LP-Templates.

The image-gen MCP engines cannot reliably output transparency or sized webp:
- Gemini "fakes" a transparent background by painting a gray checkerboard.
- gpt-image-1 is currently broken in the MCP server (bad response_format param).

So we always generate on a SOLID flat background and clean up here, locally,
with Pillow. This keeps asset production deterministic and engine-agnostic.

Commands
--------
keyout  IN OUT [--color FFFFFF] [--fuzz 14] [--trim] [--pad 24] [--size 512]
    Flood-fill the flat background colour inwards from the four corners and make
    it transparent (preserves same-colour pixels INSIDE the artwork). Optionally
    trim the transparent border, pad, and fit into a square of --size.

webp    IN OUT [--max 1600] [--quality 82]
    Convert/downscale to web-ready webp (longest edge <= --max).

favicon IN OUT [--size 256]
    Square-crop center and resize to a favicon PNG.

Examples
--------
    python3 tools/imgkit.py keyout raw/logo.png brand/logo.png --trim --pad 40 --size 640
    python3 tools/imgkit.py webp  raw/hero.png assets/img/hero.webp --max 1800
    python3 tools/imgkit.py favicon brand/logo-mark.png brand/favicon.png --size 256
"""
import argparse
import sys
from collections import deque

from PIL import Image


def _hex(c):
    c = c.lstrip("#")
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def keyout(args):
    img = Image.open(args.IN).convert("RGBA")
    px = img.load()
    w, h = img.size
    target = _hex(args.color)
    tol = args.fuzz * args.fuzz * 3  # squared-distance threshold

    def near(p):
        return (p[0] - target[0]) ** 2 + (p[1] - target[1]) ** 2 + (p[2] - target[2]) ** 2 <= tol

    visited = bytearray(w * h)
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            q.append((x, y))
    for y in range(h):
        for x in (0, w - 1):
            q.append((x, y))
    while q:
        x, y = q.popleft()
        if x < 0 or y < 0 or x >= w or y >= h:
            continue
        i = y * w + x
        if visited[i]:
            continue
        visited[i] = 1
        r, g, b, a = px[x, y]
        if not near((r, g, b)):
            continue
        px[x, y] = (r, g, b, 0)
        q.extend(((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)))

    if args.trim:
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)

    if args.pad:
        w2, h2 = img.size
        canvas = Image.new("RGBA", (w2 + 2 * args.pad, h2 + 2 * args.pad), (0, 0, 0, 0))
        canvas.paste(img, (args.pad, args.pad), img)
        img = canvas

    if args.size:
        img.thumbnail((args.size, args.size), Image.LANCZOS)
        canvas = Image.new("RGBA", (args.size, args.size), (0, 0, 0, 0))
        canvas.paste(img, ((args.size - img.width) // 2, (args.size - img.height) // 2), img)
        img = canvas

    img.save(args.OUT)
    print(f"keyout -> {args.OUT} {img.size}")


def webp(args):
    img = Image.open(args.IN).convert("RGB")
    w, h = img.size
    if max(w, h) > args.max:
        s = args.max / max(w, h)
        img = img.resize((round(w * s), round(h * s)), Image.LANCZOS)
    img.save(args.OUT, "WEBP", quality=args.quality, method=6)
    print(f"webp -> {args.OUT} {img.size} q{args.quality}")


def favicon(args):
    img = Image.open(args.IN).convert("RGBA")
    w, h = img.size
    s = min(w, h)
    img = img.crop(((w - s) // 2, (h - s) // 2, (w + s) // 2, (h + s) // 2))
    img = img.resize((args.size, args.size), Image.LANCZOS)
    img.save(args.OUT)
    print(f"favicon -> {args.OUT} {img.size}")


def alpha(args):
    """Trim transparent border, pad, and optionally fit a square — for images
    that already have an alpha channel (e.g. the output of `fal.py bg`)."""
    img = Image.open(args.IN).convert("RGBA")
    bbox = img.getchannel("A").getbbox()
    if bbox:
        img = img.crop(bbox)
    if args.pad:
        w, h = img.size
        c = Image.new("RGBA", (w + 2 * args.pad, h + 2 * args.pad), (0, 0, 0, 0))
        c.paste(img, (args.pad, args.pad), img)
        img = c
    if args.size:
        img.thumbnail((args.size, args.size), Image.LANCZOS)
        if args.square:
            c = Image.new("RGBA", (args.size, args.size), (0, 0, 0, 0))
            c.paste(img, ((args.size - img.width) // 2, (args.size - img.height) // 2), img)
            img = c
    img.save(args.OUT)
    print(f"alpha -> {args.OUT} {img.size}")


def crop(args):
    """Crop a fractional box (left,top,right,bottom as 0-1) — e.g. lift the icon
    out of a horizontal logo lockup for a favicon/mark."""
    img = Image.open(args.IN).convert("RGBA")
    w, h = img.size
    l, t, r, b = [float(x) for x in args.box.split(",")]
    img = img.crop((int(w * l), int(h * t), int(w * r), int(h * b)))
    bbox = img.getchannel("A").getbbox()
    if bbox:
        img = img.crop(bbox)
    if args.size:
        img.thumbnail((args.size, args.size), Image.LANCZOS)
    img.save(args.OUT)
    print(f"crop -> {args.OUT} {img.size}")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    k = sub.add_parser("keyout")
    k.add_argument("IN"); k.add_argument("OUT")
    k.add_argument("--color", default="FFFFFF")
    k.add_argument("--fuzz", type=int, default=14)
    k.add_argument("--trim", action="store_true")
    k.add_argument("--pad", type=int, default=0)
    k.add_argument("--size", type=int, default=0)
    k.set_defaults(func=keyout)

    wv = sub.add_parser("webp")
    wv.add_argument("IN"); wv.add_argument("OUT")
    wv.add_argument("--max", type=int, default=1600)
    wv.add_argument("--quality", type=int, default=82)
    wv.set_defaults(func=webp)

    f = sub.add_parser("favicon")
    f.add_argument("IN"); f.add_argument("OUT")
    f.add_argument("--size", type=int, default=256)
    f.set_defaults(func=favicon)

    a = sub.add_parser("alpha")
    a.add_argument("IN"); a.add_argument("OUT")
    a.add_argument("--pad", type=int, default=0)
    a.add_argument("--size", type=int, default=0)
    a.add_argument("--square", action="store_true")
    a.set_defaults(func=alpha)

    c = sub.add_parser("crop")
    c.add_argument("IN"); c.add_argument("OUT")
    c.add_argument("--box", default="0,0,1,1", help="left,top,right,bottom as 0-1 fractions")
    c.add_argument("--size", type=int, default=0)
    c.set_defaults(func=crop)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    sys.exit(main())
