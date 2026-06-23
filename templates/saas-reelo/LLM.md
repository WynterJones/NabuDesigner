# Repurpose this template for a new offer — LLM brief

You are an **elite entertainment art director + conversion copywriter**.
Repurpose this **SaaS bento template** for a new product while keeping its
structure, motion, and premium feel. Read the `entertainment-designer` and
`landing-page-design-process` skills first. `FAL_KEY` is in the repo-root `.env`.

## Keep
- The bento architecture and components: bento hero, marquee, vertical-video card
  row, feature bento, mascot value section, pricing tiers, YouTube demo modal,
  final CTA. Motion: Lenis smooth scroll, reveals, tilt, parallax, count-up.
- Ethos: graphics-led, low-text, large accent graphics, a recurring **mascot**.
  **No emojis. No hand-authored/invented SVG** — generate every icon/check/play
  badge as an image asset. **Modal = YouTube embed**, not a generated clip.

## Steps
1. **Rebrand `brand/brand.json`** — name, palette (real hexes), `seed`, and the
   one `styleSignature` sentence. Recolour the theme (`:root` in `styles.css`).
2. **Regenerate every asset from `assets/prompts/manifest.json`** with
   `styleSignature + subjectPrompt`, keeping filenames. Transparency via
   **`fal.py bg` → `imgkit alpha`** (BiRefNet matting, never colour-key).
   - Logo: `ideogram/v3` icon+wordmark lockup → `fal.py bg` → `imgkit alpha`
     (logo) + `imgkit crop --box "0,0,0.26,1"` (favicon). White wordmark for dark
     themes, dark for light.
   - Mascot: flux on plain bg → `fal.py bg` → `imgkit alpha`. Recur it large.
   - Buttons: `ideogram/v3`, art-directed (style A sleek gradient or fit the
     brand), ultra-wide ONE line → `fal.py bg`. Read each; regenerate any
     striped/two-tone/wrapped/typo'd. Recolour to the brand.
   - Vertical videos: 9:16 stills of *diverse real content* for the niche → Kling
     i2v → `vidkit web` + poster.
   - UI/product mockup + accent shapes (blob/ring) + icon set (generated).
3. **Rewrite the copy** in `index.html` — short, benefit-led, one promise per
   section, orphan-free (`&nbsp;`, `text-wrap: balance`). Update button `alt` text
   and the pricing tiers. Swap the YouTube `data-src` video id.
4. **Polish pass** — optionally add GSAP/ScrollTrigger, SplitType, Swiper,
   tsParticles (see skill). Keep `prefers-reduced-motion` paths.
5. **QA** — `python3 -m http.server 8771` from repo root; open the page; check
   360/768/1280: no horizontal overflow, videos autoplay/loop, modal closes on
   Esc/×/click-outside, clean cutouts, no emojis/SVG, AA contrast.

## Bar
Every asset passes the glance test. Clean alpha edges (use `fal.py bg`).
Distinct layout — don't converge on a sibling template's skeleton. If it looks
generic or a button is off, regenerate it.
