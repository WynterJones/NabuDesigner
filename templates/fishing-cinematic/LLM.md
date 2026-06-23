# Repurpose this template for a new offer — LLM brief

You are an **elite entertainment art director + conversion copywriter**. Your job
is to repurpose this cinematic landing-page template for a **new offer/niche**
while preserving its structure, motion, and premium graphics-led feel.

Read the `entertainment-designer` and `landing-page-design-process` skills first.
Everything generated here uses the repo tools (fal.ai + Pillow + ffmpeg). The
`FAL_KEY` is already in the repo-root `.env`.

## Inputs to collect (ask the user, or infer + label assumptions)

- Offer / product and price; audience + core pain; the one promise.
- Niche & mood → drives the **style signature** and palette.
- Host/creator name + look (the on-page character), if any.

## What NOT to change

- The section architecture, animation system, and component classes
  (hero video, stat strip, parallax bands, "what you get" kit, offer with
  ambient video, guarantee seal, final CTA, Bob-style host widget + modal).
- The ethos: **graphics-heavy, low-text, marketing-focused**, one promise per
  section, one CTA per zone, full-image buttons, no orphan words.

## Steps

### 1. Rebrand `brand/brand.json`
Set `name`, `tagline`, `seed`, palette (real hexes for the new niche), and a new
one-sentence **`styleSignature`** (medium, lighting, exact palette, texture, mood;
end with "No text, no words"). This string is prepended to every image prompt.

### 2. Regenerate every asset from the manifest
`assets/prompts/manifest.json` is the asset list. For each entry, generate with
`styleSignature + subjectPrompt` (rewritten for the new niche), then run its post
step. Keep the same filenames so the HTML/CSS keep working.

```bash
# scenes / backgrounds (FLUX ultra) -> webp
python3 tools/fal.py image --prompt "<styleSignature + subject>" --aspect 16:9 --seed <SEED> --out raw/hero.jpg
python3 tools/imgkit.py webp raw/hero.jpg assets/img/hero.webp --max 1920

# looping video backgrounds (Kling) -> web-weight + poster   (run in background; 1-5 min)
python3 tools/fal.py video --image raw/hero.jpg --duration 5 --aspect 16:9 \
  --prompt "<looping idle: subjects that move + parallax, seamless loop>" --out raw/hero.mp4
python3 tools/vidkit.py web raw/hero.mp4 assets/video/hero.mp4 --max 1280
python3 tools/vidkit.py poster raw/hero.mp4 assets/video/hero-poster.jpg

# logo + icons + seal: generate on SOLID WHITE, then key to transparent
python3 tools/imgkit.py keyout raw/logo.jpg brand/logo.png --fuzz 30 --trim --pad 40 --size 640
python3 tools/imgkit.py keyout raw/ic-x.jpg assets/img/ic-x.png --fuzz 30 --trim --pad 24 --size 256

# product/deliverables render (the "what you get" bundle) -> webp on dark
python3 tools/fal.py image --prompt "<new product bundle render>, dark background, no readable text" --aspect 4:3 --out raw/bundle.jpg
python3 tools/imgkit.py webp raw/bundle.jpg assets/img/bundle.webp --max 1400
```

### 3. Regenerate the full-image CTA buttons (literal AI graphics)
Generate each button with `fal-ai/ideogram/v3`, then `imgkit keyout`. Keep labels
SHORT (one line), force an ultra-wide single-line button, recolour to the brand.
Update each `alt` to match. **Read every result and regenerate any that wraps,
goes two-tone, recolours, or has a typo** (Ideogram is inconsistent).
```bash
python3 tools/fal.py image --model fal-ai/ideogram/v3 --aspect 3:1 \
  --prompt "An ultra-wide glossy 3D <BRANDCOLOR> game button, one continuous gradient (no two-tone, no seam), thick bevel + top gloss + soft glow, ONE single line of bold white outlined text reading exactly '<LABEL>', plain white background, no wrapping, no stars." \
  --out raw/btn-hero.jpg
python3 tools/imgkit.py keyout raw/btn-hero.jpg assets/img/btn-hero.png --fuzz 44 --trim --pad 8
# repeat for btn-nav, btn-kit, btn-offer, btn-final
```

### 4. Regenerate the host (the "Bob" widget)
Generate the new host on solid white → keyout → `assets/img/bob.png` (corner
cutout). Generate a scene version → `fal.py video` → `vidkit web`/`poster` →
`assets/video/bob.mp4` + `bob-poster.jpg`. Update the modal copy.

### 5. Rewrite the copy in `index.html`
Short, punchy, benefit-led. One promise per section. Replace: eyebrows, headlines,
lede, stat strip numbers, method steps, kit list, offer value stack + price,
guarantee, FAQ-style lines, footer. Keep headlines orphan-free (`&nbsp;` trailing
phrases; intentional `<br>`; `text-wrap: balance` is already global).

### 6. Recolor `assets/styles.css` from the new palette
Update the `:root` variables to the new `brand.json` palette. Don't restructure.

### 7. QA (serve + browser)
```bash
python3 -m http.server 8771 --directory .    # from repo root
```
Open `/templates/<slug>/index.html`. Check at 360 / 768 / 1280:
no horizontal overflow, videos autoplay/loop, buttons crisp, Bob modal opens
(Esc/×/click-outside close), icons/seal clean, no orphan words, AA contrast.

## Bar
Every asset passes the glance test — instant impact, strong focal point, rich
color, readable silhouette. If it looks generic, washed-out, or cluttered, or any
button text is inconsistent, regenerate it. The page must read as a premium,
graphics-led marketing experience, not a document.
