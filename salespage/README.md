# DragonForge — sales page

The marketing/landing page that **sells the whole LP-Templates kit** as a one-time
$28 download. Dark obsidian + molten-gold dragon theme, over-the-top fantasy game
key-art, and a signature **slot-machine template reel** for the included templates.

Built with the same pipeline it sells (brand → mockup → fal art/video → motion → QA),
so it doubles as the most maximal reference build in the repo.

```bash
python3 -m http.server 8771        # from repo root
# open http://localhost:8771/salespage/index.html
```

## What stands out
- **Slot-reel template showcase** — the 5 included templates as glowing collectible
  reels in an ornate gold machine with chase-lights and a working pull-lever (auto-
  spins on scroll, re-spins on click). Mobile: horizontal scroll-snap.
- **Forged-ember image CTA** — a full AI-generated button (Ideogram v3, text rendered
  *in* the image, matted with fal `bg`). Reused in hero / pricing / final.
- **Cinematic dragon hero** with a ping-pong looping forge video, particle embers,
  parallax mascot, and a molten headline graphic.
- **Host widget** — a baby-dragon mascot FAB opening a YouTube tour modal.
- Five-stage timeline, feature grid, count-up stats, deliverables checklist, an
  offer card with an `INSTANT DOWNLOAD` seal, FAQ accordion, ember-field final CTA.

## ⚙️ Set up checkout + delivery (REQUIRED before launch)

The page is static, so payment + ZIP delivery runs through **Gumroad** (it hosts the
file and delivers it instantly after the $28 clears).

1. **Build the product ZIP** — zip the repo so buyers get the whole kit:
   ```bash
   # from the repo root, exclude secrets + scratch
   zip -r dragonforge-kit.zip . \
     -x '.env' -x '.git/*' -x 'salespage/raw/*' -x '*/raw/*' \
     -x '.farmwork/*' -x 'outputs/*' -x 'salespage/gen.sh'
   ```
   (Keep `.env` OUT of the zip — it holds your fal key.)
2. **Create the Gumroad product** — gumroad.com → new product → *Digital product* →
   price **$28** → upload `dragonforge-kit.zip`. Gumroad emails + serves the download
   automatically on purchase. Copy the product URL
   (e.g. `https://yourname.gumroad.com/l/dragonforge`).
3. **Wire the buttons** — open `assets/script.js` and set the one constant:
   ```js
   var BUY_URL = "https://yourname.gumroad.com/l/dragonforge";
   ```
   Every `[data-buy]` link (nav, hero, pricing, final, modal) points there and opens
   in a new tab.
4. *(Optional)* **On-page overlay checkout** — append `?wanted=true` to `BUY_URL` and
   uncomment the `gumroad.js` `<script>` at the bottom of `index.html`. Note: the
   Gumroad overlay injects its own button chrome, which is why the default uses clean
   direct links instead.

> Swap Gumroad for **Lemon Squeezy / Stripe Payment Link** by pointing `BUY_URL` at
> that checkout instead — the rest of the page is identical.

## Folder
```
salespage/
  index.html              # the page
  assets/styles.css       # dragon theme, slot machine, all surfaces
  assets/script.js        # reveals, parallax, slot spin, modal, ember canvas, BUY_URL
  assets/img/             # hero, headline, button, mascot, 5 slot cards, icons, seal, coil
  assets/video/           # hero.mp4 + forge.mp4 (ping-pong loops) + posters
  brand/                  # brand.json, logo, logo-mark, favicon, og-image
  assets/prompts/manifest.json   # every image slot declared
  raw/                    # original fal generations (pre-processing)
  gen.sh                  # the asset-generation driver used to build this page
```

## Notes / assumptions
- Copy, stats, and the guarantee are marketing for the real kit; the modal uses a
  placeholder YouTube ID — swap in your tour video (`data-src` on `#player`).
- All art was generated with fal (`tools/fal.py`), matted with fal `bg` (BiRefNet),
  and post-processed with `imgkit` / `vidkit`. Videos use the new `vidkit pingpong`
  boomerang loop for seam-free idle motion.
