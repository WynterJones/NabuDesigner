# Local Lake Secrets

Fictional static landing-page template for a `$28` local lake fishing video course.

Open `index.html` directly in a browser. No build step is required.

## Brand

The template's visual identity lives in `brand/`:

- `brand.json` — the single source of truth: palette, type, seed, and the **style signature** that anchors every generated image.
- `styleguide.html` — open this to see the logo, palette, type, icons, scenes, and CTA buttons together.
- `logo.png`, `logo-mark.png`, `favicon.png`, `style-board.webp` — generated brand assets.

## Assets

All imagery is AI-generated from the style signature in `brand.json`, then post-processed with `tools/imgkit.py`:

- `assets/img/hero.webp`, `scene-deep.webp` — scenes (Gemini → webp).
- `assets/img/icon-*.png` — module icons (Gemini on white → transparent via `imgkit keyout`).
- `assets/img/cta.webp`, `cta-hover.webp` — CTA button textures; the label is HTML over the texture.
- The checklist tick is an inline SVG (crisp at any size), not a raster.

`assets/prompts/manifest.json` records the exact prompt and post step for every asset, so any single image can be regenerated. Original full-resolution generations are kept in `raw/`.
