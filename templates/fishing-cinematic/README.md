# Local Lake Secrets — Cinematic

High-fidelity, graphics-led, video-backed landing-page template (fictional $28
fishing course). The cinematic successor to `fishing-course-local-lake`.

Open `index.html` in a browser (or serve the repo and visit
`/templates/fishing-cinematic/index.html`). No build step.

## What makes it stand out

- **Looping video backgrounds** — hero (trophy bass) and the offer band (ambient
  lake) are muted autoplay `<video>` loops with poster fallbacks.
- **Graphics-heavy, low-text** — one promise per section, big imagery, one CTA
  per zone. Marketing-led, not a document.
- **Motion** — drifting particle field over the hero, scroll parallax on every
  scene band, reveal-on-scroll, count-up stats, glowing CTAs, sticky nav, mobile
  drawer. All honor `prefers-reduced-motion`.

## How the art was made (fal.ai)

Built with the `entertainment-designer` skill. Every asset = the `styleSignature`
in `brand/brand.json` + a subject prompt, seed 73412.

- Stills: `tools/fal.py image` (FLUX1.1 [pro] ultra) → `tools/imgkit.py webp`.
- Logo: FLUX on white → `tools/imgkit.py keyout` → transparent + favicon.
- Video: `tools/fal.py video` (Kling v2.5) → `tools/vidkit.py web` + `poster`
  (a ~20 MB clip compresses to <1 MB).

`assets/prompts/manifest.json` records the exact prompt + post step for every
asset; full-res originals are in `raw/`.

## Shape

```
brand/        brand.json, logo.png, favicon.png
assets/
  styles.css, script.js
  img/        hero, cast, underwater, lake  (webp scenes)
  video/      hero.mp4 + hero-poster.jpg, lake.mp4 + lake-poster.jpg
  prompts/    manifest.json
raw/          full-res stills + original Kling mp4s
index.html
```
