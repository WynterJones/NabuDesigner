# AI Profit Blueprint — lead-gen VSL squeeze

High-fidelity, graphics-led **email lead-generation** landing page for a fictional
**free 5-day AI mini-course**. Direct-response (Dan Kennedy / Russell Brunson)
copy wrapped around a premium dark-cinematic tech brand. Built with the LP-Templates
system via a team of agents.

Open `index.html` in a browser (or serve the repo and visit
`/templates/ai-profit-blueprint/index.html`). No build step.

## What makes it stand out

- **Lead-gen, not checkout** — the primary action is an email opt-in form
  (hero, mid-page, and final), with a thank-you state. No price, no cart.
- **A distinct archetype** — a VSL opt-in *squeeze* (hero capture + video-modal
  VSL → agitation → future-pace → 5 fascination-bullet day cards → host authority
  → "Secret #N" stack → proof → value stack → FAQ → urgency + P.S. close). Not the
  cinematic/bento/light skeletons of its siblings.
- **Brunson/Kennedy copy** — big-promise headline, pain agitation, future-pacing,
  curiosity bullets, reason-why urgency (weekly cohort cap), and a host P.S.
- **Generated art, one brand** — every scene, icon, glyph, avatar, host, and CTA
  button is an AI asset sharing one `styleSignature` (midnight-navy + electric-blue/
  cyan + gold). Full-image CTA buttons (Ideogram), a 6-icon family, chrome glyphs,
  and a host (Marcus Vale) cutout + VSL modal (real YouTube embed).
- **Motion** — hero video loop + canvas particle fields, scroll reveals, count-up
  stats, FAQ accordion, sticky nav, mobile drawer. All honor `prefers-reduced-motion`.

## How the art was made (fal.ai)

Every asset = the `styleSignature` in `brand/brand.json` + a subject prompt, seed
50824. Keyout assets use the `styleSignatureWhiteBg` variant (pure-white background
so transparency keys cleanly — the navy signature fights keyout).

- Stills: `tools/fal.py image` (FLUX1.1 [pro] ultra) → `tools/imgkit.py webp`.
- Logo/icons/chrome/host/avatars: FLUX on white → `tools/imgkit.py keyout`.
- CTA buttons: `fal-ai/ideogram/v3` (in-image text) → `keyout`.
- Hero video: `tools/fal.py video` (Kling v2.5) → `tools/vidkit.py web` + `poster`
  (~18 MB → ~0.5 MB).

`BRIEF.md` is the locked build brief; `assets/prompts/manifest.json` records the
prompt + post step for every asset; full-res originals are in `raw/`.

## Shape

```
BRIEF.md      locked build brief (offer, palette, section architecture)
brand/        brand.json (+ styleSignatureWhiteBg), logo, logo-mark, favicon,
              style-board.webp, styleguide.html
assets/
  styles.css, script.js
  img/        hero, scenes, 6-icon set, chrome glyphs, host, avatars, CTA buttons, seal
  video/      hero.mp4 + hero-poster.jpg
  prompts/    manifest.json
raw/          full-res stills + original Kling mp4
index.html
```

## Notes

Fictional demo template — all names, testimonials, stats, and results are
illustrative and flagged as not real in the page and footer.
