# Reelo — SaaS (cinematic, original layout)

High-fidelity SaaS landing-page template (fictional): **Reelo**, an AI
short-video studio. Deliberately a **different architecture** from the
cinematic-photo templates — a dark, glassmorphic **bento layout** with a mascot,
large accent graphics, and vertical-video cards.

Open `index.html`, or serve the repo and visit
`/templates/saas-reelo/index.html`. No build step (Lenis loads from CDN).

## What makes it distinct
- **Bento hero** — editor UI tile, a vertical-video tile, a stat, the mascot, a
  feature tile — instead of a full-bleed cinematic hero.
- **Mascot** — a glossy play-button creature, recurring large (hero, value
  section, final CTA) with a gentle bob.
- **Vertical-video cards** — four phone-framed 9:16 loops of *diverse real
  content* (creator, food, travel, fitness) in an angled row.
- **Large accent graphics** — gradient orbs (CSS) + generated 3D glass blob/ring.
- **Pricing tiers** (Free / Pro / Studio) and a YouTube **demo modal**.

## How the art was made (fal.ai)
Built with the `entertainment-designer` skill.
- Stills: `flux-pro/v1.1-ultra`. **Cutouts use fal BiRefNet bg-removal**
  (`fal.py bg` → `imgkit alpha`) — clean alpha, no colour-keying.
- **Logo = icon + wordmark lockup** (`ideogram/v3`) → bg-removed → `imgkit crop`
  lifts the icon for the favicon. White wordmark for the dark theme.
- Buttons: `ideogram/v3` style A (sleek glassy gradient) → bg-removed.
- Vertical videos: Kling i2v → `vidkit web` + posters.
See `assets/prompts/manifest.json`; full-res originals in `raw/`.

## Effects
Lenis smooth scroll (CDN) + vanilla JS: reveals, 3D tilt on tiles, parallax,
count-up, lazy video, marquee, glow. GSAP/ScrollTrigger, Swiper, SplitType,
tsParticles are recommended in the skill for deeper choreography. No emojis, no
hand-authored SVG — all icons/checks/play badges are generated image assets.
Honors `prefers-reduced-motion`.
