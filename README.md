# LP-Templates

**An AI system for generating premium, graphics-heavy landing pages.**

Not just a folder of templates — a repeatable pipeline. Point an AI agent at this
repo, name an offer, and it produces a finished, animated, single-folder landing
page with original art, looping video, and a cohesive brand — built from the same
skills, tools, and quality bar every time.

---

## Quick start

Open the repo in an AI agent (Claude Code / Codex / Cursor) and say:

> **"Generate a template for `<your offer or niche>`."**

The agent runs [`PROMPT.md`](PROMPT.md) — a single brief + end-to-end playbook —
through five stages (brief → brand → mockup → assets → motion/QA) and drops a
finished `templates/<slug>/` you can open in a browser. Fill in the Brief block in
`PROMPT.md` for control, or leave blanks and the agent infers and labels its
assumptions.

**One-time setup** — add your fal.ai key to a gitignored `.env` at the repo root:

```bash
echo "FAL_KEY=your-fal-key" > .env
python3 -m pip install Pillow imageio-ffmpeg   # installed on first use anyway
```

Preview any template locally:

```bash
python3 -m http.server 8771      # from the repo root
# open http://localhost:8771/templates/<slug>/index.html
```

---

## Templates

| Template | Niche | Look |
|---|---|---|
| [`fishing-cinematic`](templates/fishing-cinematic/) | $28 video course | Dark cinematic · hero video · host widget |
| [`macaron-cinematic`](templates/macaron-cinematic/) | $97 maker course | Light patisserie · video · host widget |
| [`saas-reelo`](templates/saas-reelo/) | AI SaaS app | Bento layout · mascot · vertical-video cards · pricing tiers |
| [`ai-profit-blueprint`](templates/ai-profit-blueprint/) | Free lead magnet | VSL squeeze · direct-response copy |
| [`makeup-giveaway`](templates/makeup-giveaway/) | Beauty giveaway | Light luxe · enter-to-win · headline graphic · coupon close |
| [`fishing-course-local-lake`](templates/fishing-course-local-lake/) | $28 video course | Baseline (no fal key needed) |
| [`_blank`](templates/_blank/) | — | Copy-to-start scaffold |

Each is a self-contained static folder (`index.html`, `brand/`, `assets/`,
`raw/`) that opens directly in a browser — no build step, no external services.
Every template ships an `LLM.md` brief so an agent can repurpose it for a new
offer in minutes.

---

## How it works

Every template is its own brand, built in five stages (see the skills):

0. **Brief & Brand** — `brand/brand.json`: palette, type, seed, and one
   `styleSignature` sentence that is prepended to every image prompt for one
   coherent look.
1. **Mockup & architecture** — `index.html`, with every image declared as a slot
   in `assets/prompts/manifest.json`. Layout archetype varies per niche.
2. **Asset generation** — each asset = `styleSignature + subjectPrompt`, generated
   with fal and post-processed locally.
3. **Motion & effects** — scroll reveals, parallax, particles, smooth scroll,
   micro-interactions.
4. **QA** — checked at 360 / 768 / 1280.

---

## What's inside

**Skills** (the process)
- `skills/landing-page-design-process/` — the five-stage method + brand system.
- `skills/entertainment-designer/` — high-fidelity art direction: fal stills,
  looping/vertical video, mascots, headline graphics, the button strategy, and
  the effects-library toolkit.

**Tools** (the engine — Python, no framework)
- `tools/fal.py` — fal.ai client: stills (FLUX ultra), text graphics
  (Ideogram v3), video (Kling), and background removal (BiRefNet).
- `tools/imgkit.py` — Pillow: `alpha` (trim transparent), `crop`, `webp`,
  `favicon`.
- `tools/vidkit.py` — ffmpeg (bundled via pip): web-compress, poster, loop.
- `tools/IMAGE_PIPELINE.md` — engines, transparency workflow, known issues.

**Guides**
- `CLAUDE.md` — the map for an agent loaded into the repo.
- `PROMPT.md` — the "Generate a template for X" kickoff brief.
- `DESIGN_GUIDELINES.md` — the layout / UX / QA rubric.

---

## The bar

Graphics-led and low-text · large accent graphics · varied layout per niche ·
one premium image CTA backed by clean CSS buttons · headline graphics for impact ·
generated icons (no emoji, no hand-drawn SVG) · video for variety, not wallpaper ·
clean alpha cutouts via fal background removal · no orphan words · AA contrast ·
no horizontal overflow at any breakpoint · honors reduced-motion.

> The templates are fictional demos for design purposes — no real offers,
> endorsements, or checkout integrations.
