# Lumière — Luxury Beauty Giveaway

High-end **sweepstakes / giveaway** landing-page template (fictional): enter to
win a $500 beauty bundle, then claim a 20%-off coupon to shop. A distinct
giveaway archetype — not the cinematic or bento skeletons. Audience: elegant
middle-aged women.

Open `index.html`, or serve the repo and visit
`/templates/makeup-giveaway/index.html`. No build step.

## Highlights
- **Headline graphic** — "WIN THE GLOW" rose-gold typographic image, lifted with
  CSS drop-shadow/glow (the real `<h1>` is visually-hidden for SEO/AX).
- **One image CTA + CSS buttons** — only "Shop the Collection" is a generated
  image; "Enter to Win" and nav are premium CSS buttons.
- **Demo entry form** (first name + email) with a thank-you state; countdown to
  Sunday; count-up stats — all clearly fictional.
- Elegant luxe theme (Playfair Display + Inter), hero prize video, prize grid,
  3-step how-to-enter with rose-gold icons, parallax story band, reviews, coupon.

## How the art was made (fal.ai)
Built with the `entertainment-designer` skill. Stills: flux-pro/v1.1-ultra.
**Transparency via fal BiRefNet** (`fal.py bg` → `imgkit alpha`) — logo, headline,
the CTA, and icons. Logo is an icon+wordmark lockup; favicon cropped from it.
Hero video: Kling → `vidkit web` + poster. No emojis, no hand-authored SVG.
See `assets/prompts/manifest.json`; originals in `raw/`.
