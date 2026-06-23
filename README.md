# LP-Templates

Static HTML landing-page templates for premium, graphic-heavy sales pages.

## Quick start

Say **"Generate a template for X"** to an agent loaded in this repo (X = your
offer/niche). It runs `PROMPT.md` — the single fill-in brief + end-to-end playbook
— from brief → brand → mockup → assets → motion → QA, producing a finished
`templates/<slug>/` folder. Fill in the Brief block in `PROMPT.md` first for more
control; leave blanks and the agent infers + labels assumptions.

## Structure

- `PROMPT.md` - the "Generate a template for X" kickoff brief + playbook (start here).
- `CLAUDE.md` - the map for AI agents loaded into this repo.
- `DESIGN_GUIDELINES.md` - borrowed NabuKit UI/UX rules used as the baseline polish rubric.
- `skills/landing-page-design-process/` - repo-local skill; the four-stage process for building a template.
- `skills/entertainment-designer/` - elite art-director skill: high-fidelity fal.ai stills + looping video, layered animation, graphics-heavy marketing pages.
- `tools/fal.py` - fal.ai client: premium stills (FLUX ultra) + looping video (Kling). Reads `FAL_KEY` from gitignored `.env`.
- `tools/vidkit.py` - ffmpeg (via pip) video post: web-compress, poster frame, seamless loop.
- `tools/imgkit.py` - Pillow post-processor (transparent keyout, webp, favicon).
- `tools/IMAGE_PIPELINE.md` - fidelity tiers, fal + baseline engines, transparency workflow, known issues.
- `templates/_blank/` - copy-to-start scaffold (brand.json, manifest, folder shape).
- `templates/fishing-cinematic/` - flagship: dark cinematic, video-backed, host widget (fal).
- `templates/macaron-cinematic/` - light patisserie theme, video-backed, host widget (fal).
- `templates/saas-reelo/` - SaaS bento layout: mascot, vertical-video cards, pricing tiers, large accent graphics (fal).
- `templates/ai-profit-blueprint/` - lead-gen VSL squeeze: email opt-in for a free AI mini-course, Kennedy/Brunson copy, host VSL modal (fal).
- `templates/fishing-course-local-lake/` - earlier illustrated template (baseline engines, no key).

## How a template is built

Every template is its own brand. The four stages (see the skill):

0. **Brief & Brand** — define `brand/brand.json` (palette, type, seed, and the one
   `styleSignature` sentence). Generate logo, mark, favicon, style board, and
   `brand/styleguide.html`.
1. **Mockup & sales architecture** — full `index.html`, every image declared as a
   slot in `assets/prompts/manifest.json`.
2. **Asset generation & polish** — generate each asset as
   `styleSignature + subjectPrompt`, post-process with `tools/imgkit.py`.
3. **Motion, detail & QA** — at 360 / 768 / 1280.

The **style signature** is the consistency mechanism: it is prepended to every
image prompt, so logo, icons, backgrounds, and CTA buttons all look like one brand.

## Template Standard

Each template is a self-contained static folder that opens directly in a browser:

- `index.html`, `brand/`, `assets/` (css, js, `img/`, `prompts/`), `raw/`
- AI-generated brand assets (logo, icons, backgrounds, CTA) under the template folder
- responsive layout for phone, tablet, and desktop
- no external secrets or production integrations

## Current Templates

### `fishing-course-local-lake`

A fictional $28 video course landing page for local lake fishing tips and tricks. It uses a long-form sales-letter structure, offer stack, guarantee, FAQ, image-backed CTAs, responsive layout, and interaction polish.

