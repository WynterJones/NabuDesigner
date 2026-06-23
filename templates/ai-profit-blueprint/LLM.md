# Repurpose this template for a new lead-magnet — LLM brief

You are an **elite art director + direct-response copywriter**. Repurpose this
**lead-gen VSL squeeze** template for a **new free offer / niche** (a free guide,
challenge, webinar, mini-course, checklist, quiz funnel) while preserving its
structure, motion, and premium graphics-led feel.

Read the `entertainment-designer` and `landing-page-design-process` skills first.
Everything uses the repo tools (fal.ai + Pillow + ffmpeg); `FAL_KEY` is in `.env`.

## What this template IS (keep it)

- **Lead generation, not checkout.** The conversion is an **email opt-in form**
  (hero + mid + final), with a JS thank-you state. No price, no cart.
- **Dan Kennedy / Russell Brunson direct response.** Big-promise headline → pain
  agitation → future-pacing → fascination/curiosity bullets → host authority →
  "Secret #N" stack → proof → value stack → reason-why urgency → P.S. close.
- Section architecture, animation system, and component classes (see `BRIEF.md`):
  sticky nav, hero opt-in + VSL play-card → YouTube modal, agitation cards,
  future-pace scene, 5 module/day cards, host authority, secret bullets + mid
  opt-in, proof (stat strip + testimonials), value stack with seal, FAQ accordion,
  final opt-in (urgency + P.S.), footer. Sticky host widget hidden on phones.
- **Graphics-heavy, low-text, one promise per section, full-image buttons, no
  emojis, no invented SVG icon art, no orphan words.**

## Inputs to collect (ask or infer + label)

- The free offer + its one promise; audience + core pain; the primary CTA label.
- Niche & mood → drives the **two style signatures** and palette.
- Host/creator name + look (the on-page authority + VSL).

## Steps

### 1. Rebrand `brand/brand.json`
Set `name`, `tagline`, `seed`, palette (real hexes), and **both** signatures:
`styleSignature` (scenes — can specify a dark/colored background) and
`styleSignatureWhiteBg` (the keyout variant — pure-white background, used for
logo/icons/chrome/host/avatars/seal). Both end with "No text, no words, no letters."
The right signature is prepended to every prompt.

### 2. Regenerate every asset from `assets/prompts/manifest.json`
Each entry lists its engine, signature choice, subjectPrompt, and post step. Keep
the **same filenames** (the HTML/CSS reference them as a contract). Rules learned:
- **Scenes** (hero, future, module, host-scene, style-board): navy `styleSignature`
  → `imgkit webp`.
- **Keyout assets** (logo, mark, icons ×6, chrome ×5, host, avatars ×3, seal):
  `styleSignatureWhiteBg` + "no cast shadow, no reflection" → `imgkit keyout`.
  Generate the icon set with one shared descriptor so they read as a family.
- **CTA buttons** (`fal-ai/ideogram/v3`, no signature, prompt has the exact label):
  Ideogram is inconsistent — it wraps, adds stray punctuation/nav text, or boxes
  the button into a square. **Generate 2–3 candidates per button, Read each, keep
  the clean single-line one, and key out at `--fuzz ~46 --trim --pad 8`.** Prompt
  "ONLY a single isolated button on a plain pure-white empty background, nothing
  else, one horizontal line, no drop shadow."
- **Hero video**: `fal.py video` from `raw/hero.jpg` → `vidkit web` + `poster`.
- **Always Read each generated file and regenerate duds** (generic, washed-out,
  cluttered, wrong background, striped/two-tone/wrapped/typo'd buttons).

### 3. Rewrite the copy in `index.html`
Short, punchy, direct-response. One promise per section. Replace eyebrows,
headlines, lede, the 5 day cards + fascination one-liners, the "Secret #N" bullets,
stat-strip numbers (`data-count` + `data-suffix`), testimonials, value stack, FAQ,
urgency reason-why, and the host P.S. Keep headlines orphan-free.

### 4. Recolor `assets/styles.css`
Update the `:root` variables to the new palette. Don't restructure.

### 5. QA (serve + browser, at 360 / 768 / 1280)
```bash
python3 -m http.server 8771      # from repo root
```
Check: no horizontal overflow; hero video autoplays/loops with poster; **count-up
stats land on real numbers** (a `setTimeout` fallback covers throttled tabs); all
three opt-in forms validate + show the success state; FAQ accordion toggles; VSL
modal opens and **Esc/×/click-outside close it and clear the iframe `src`**; the
host widget is hidden on phones; buttons are crisp single-line; no orphan words.

## Bar
Every asset passes the glance test — instant impact, strong focal point, rich
color, readable silhouette. If it looks generic, washed-out, cluttered, or a button
is inconsistent, regenerate it. The page must read as a premium, graphics-led
direct-response squeeze page, not a document.
