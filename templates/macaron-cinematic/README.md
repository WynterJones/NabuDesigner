# The Macaron Method — Cinematic

High-fidelity, graphics-led, video-backed landing-page template (fictional $97
course: making + selling macarons from a certified home kitchen via Shopify and
social). A **light, pastel patisserie** counterpart to `fishing-cinematic` —
proof the system handles a bright theme as well as a dark one.

Open `index.html` in a browser, or serve the repo and visit
`/templates/macaron-cinematic/index.html`. No build step.

## Highlights
- **Looping video backgrounds** — pastel macaron hero + ambient flatlay loop,
  muted autoplay with poster fallbacks.
- **Graphics-led, low-text** — one promise per section, big imagery, one CTA/zone.
- **Full-image rose-pink CTA buttons** (Ideogram, keyed) — juicy, not flat/CSS.
- **Alysha host widget** — bottom-right character cutout + play button opening a
  video modal (her kitchen intro) with a CTA under the video.
- Motion: pink particle field, scroll parallax, reveals, count-up stats, glow
  CTAs, sticky nav, mobile drawer — all honour `prefers-reduced-motion`.

## How the art was made (fal.ai)
Built with the `entertainment-designer` skill. Every asset = the `styleSignature`
in `brand/brand.json` + a subject prompt, seed 88231. Stills: flux-pro ultra →
`imgkit webp`. Logo/icons/seal/character: flux on white → `imgkit keyout`.
Buttons: `ideogram/v3` → `imgkit keyout`. Video: Kling → `vidkit web` + poster.
See `assets/prompts/manifest.json`; full-res originals in `raw/`.

## Shape
```
brand/   brand.json, logo.png, favicon.png
assets/  styles.css, script.js, img/ (scenes, icons, buttons, bundle, alysha),
         video/ (hero, ambient, alysha + posters), prompts/manifest.json
raw/     full-res stills + original mp4s
index.html · LLM.md (repurpose brief)
```
