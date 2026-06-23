# Think and Grow Rich — editorial art-deco book sales page

A premium, graphics-led landing page that **sells a book and links to Amazon**.
The offer is Napoleon Hill's 1937 classic *Think and Grow Rich*. The page leans
into a **vintage art-deco wealth** aesthetic — deep emerald-black, antique gold
foil, warm cream parchment — and an **editorial / long-form** architecture
distinct from every other template in this repo.

> No video, no host/mascot widget. Both are optional in this kit, and a book
> sales page reads better as a quiet, literary, gallery-grade experience. The
> design work is carried by typography, gold-foil deco artwork, and motion.

## What stands out

- **Editorial long-form archetype** — sticky deco nav → literary hero (floating
  book over a gold sunburst) → proof stat strip with count-ups → Carnegie origin
  story (Hill's vintage portrait, duotone, in a gold deco frame) → the 13
  Principles (6 pillar medallions + the full numbered list) → big gold pull-quote
  → what's inside (specs `<dl>` + takeaways) → reader acclaim → buy/offer →
  FAQ → final CTA. Gold-foil dividers between bands.
- **One art-directed image CTA** ("BUY ON AMAZON", embossed antique-gold deco
  pill) reused at the hero, offer, and final CTA. Every other button is a crafted
  CSS button. Dark ink on gold throughout — AA on the fill, not the page.
- **A cohesive gold deco icon set** — six matching medallion icons for the
  principles, generated from one shared art-direction descriptor, circle-cropped
  in CSS so they read as siblings.
- **Real source assets, treated** — the actual book cover (background removed via
  fal BiRefNet) and a vintage photograph of Napoleon Hill (sepia/gold duotone via
  CSS blend) anchor the page in the real product.
- **Restrained, expensive motion** — IntersectionObserver reveals with an
  immediate above-the-fold pass (no flash), hero parallax, gold count-ups, a
  condensing nav, a floating book, and an accordion FAQ. All 60fps
  (transform/opacity), all gated behind `prefers-reduced-motion`.

## How the art was made

All imagery is fal.ai + the repo tools (`tools/fal.py`, `tools/imgkit.py`). The
one `styleSignature` in `brand/brand.json` is prepended to every prompt for a
single coherent look; `seed 19370` across the set.

- **Scenes** (`hero-deco`): FLUX1.1 [pro] ultra → `imgkit webp`.
- **Cutouts** (book, emblem/logo-mark, seal, star, quote, the CTA button):
  generate → `fal.py bg` (BiRefNet matte) → `imgkit alpha`.
- **Icon set**: FLUX ultra, one shared deco descriptor → `imgkit webp`, circle-
  cropped in CSS.
- **CTA button**: Ideogram v3 (engraved deco lettering) → `fal.py bg` → `alpha`.
  Generated three candidates; kept the one with the label on a single legible line.
- **Sources**: the book cover and the Hill portrait are user-supplied real images,
  only matted/treated (not generated). Originals in `raw/`.
- `assets/img/noise.png` is a tiny procedural grain (Pillow) for the page overlay.

See `assets/prompts/manifest.json` for the per-asset prompt + post step.

## QA

```bash
python3 -m http.server 8771      # from repo root
# open http://localhost:8771/templates/think-grow-rich/index.html
```

Checked at 360 / 768 / 1280: no horizontal overflow, AA contrast (dark ink on
gold buttons, dark text on the seal, cream on emerald cards), reveals fire without
a flash, count-ups run, FAQ toggles, mobile hamburger drawer opens/closes
(Esc / × / link), favicon loads, all CTAs deep-link to Amazon search.

## Assumptions (labeled)

- **CTA target**: Amazon search for the book (`amazon.com/s?k=think+and+grow+rich…`)
  — swap for a specific ASIN/affiliate link in production.
- **Price** "from $9.99" and the **format chips** are representative; confirm
  against the live Amazon listing.
- **Reader testimonials** are illustrative (first names only) — see the footer
  disclaimer.

## Shape

```
brand/    brand.json, styleguide.html, logo-mark.png, favicon.png, style-board.webp
assets/
  styles.css, app.js
  img/    hero-deco, book, hill, ic-* (6), star, seal, quote, btn-cta, noise
  prompts/ manifest.json
raw/      full-res originals + source cover/portrait
index.html
LLM.md    repurposing brief for the next book/offer
```
