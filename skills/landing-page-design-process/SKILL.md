---
name: landing-page-design-process
description: Build or polish premium graphic-heavy static HTML landing-page templates. Use when creating LP-Templates pages, long-form sales letters, offer pages, static HTML funnels, image-rich CTA sections, favicon/icon/image assets, responsive landing pages, animation polish, or final QA for desktop, tablet, and mobile.
---

# Landing Page Design Process

Use this skill for LP-Templates work. The output should be a finished static HTML template folder, not a marketing explanation of a template.

## Required Inputs

Confirm or infer:

- Product or offer
- Price and primary CTA
- Audience and pain points
- Desired persuasion style
- Template slug under `templates/`

If details are missing, make conservative fictional assumptions and label them in the template copy only when legally or ethically needed.

## Step 1: Mockup And Sales Architecture

Build the full page with all sections before visual polish.

- Create `index.html` and any initial `assets/` files.
- Write the sales page as a complete long-form argument: hook, problem, story, mechanism, proof-style elements, offer stack, bonuses, guarantee, FAQ, final CTA.
- Use persuasive direct-response copy inspired by classic funnel structure, without copying protected copy or naming a real marketer in public page text.
- Keep every CTA wired to a real target section such as `#order`.
- Include realistic placeholder proof, testimonials, and stats only if the fictional nature is clear in metadata/comments or the template context.
- Design sections for 360px, 768px, and 1280px from the start.

Step 1 acceptance:

- The whole page reads in order.
- No lorem ipsum remains.
- Every section has a purpose.
- The main CTA exists in the hero, middle, offer stack, and final section.

## Step 2: Visual Polish And Asset Build

Turn the mockup into a premium graphic-heavy template.

- Apply `DESIGN_GUIDELINES.md` as the layout, contrast, typography, mobile, and button rubric.
- Generate or create local background images, product/scene images, icons, favicon, and CTA button images.
- Use Codex image generation when available for hero/background/product art. If unavailable, create deterministic raster assets with ImageMagick or repo-native SVG/CSS, and state the fallback.
- Use image-backed primary CTA buttons with a hover-state image or sprite when the design calls for a high-end sales-page feel.
- Add favicon files and ensure the page references them.
- Avoid fragile external image dependencies; project-bound assets must live under the template folder.

Step 2 acceptance:

- The first viewport has strong product/offer imagery.
- CTA buttons have visible hover/focus states.
- Icons and imagery feel cohesive.
- The page still works when opened from disk.

## Step 3: Motion, Detail Polish, And QA

Add final behavior and inspect the template like a shippable page.

- Add restrained scroll reveal, hover, parallax, sticky bar, countdown, accordions, or section highlighting only when they improve the sales experience.
- Polish typography, text wrapping, scrollbar styling, focus rings, selection color, and reduced-motion behavior.
- Verify no horizontal overflow at 360px, 768px, and 1280px.
- Check CTA links, FAQ toggles, animations, asset paths, favicon path, and image loading.
- Keep animations subtle and fast; the page should feel expensive, not busy.

Step 3 acceptance:

- Desktop, tablet, and mobile are readable and polished.
- No overlapping UI, clipped text, broken images, dead buttons, or accidental horizontal scrolling.
- The template folder can be copied as a standalone static design.

## File Pattern

Use this folder shape:

```text
templates/<template-slug>/
├── index.html
└── assets/
    ├── styles.css
    ├── script.js
    ├── favicon.png
    ├── hero-*.webp
    └── cta-*.png
```

## Copy Notes

For a long-form sales letter, prefer these beats:

1. Specific promise
2. Painful current state
3. New mechanism
4. Personal or local story
5. What the buyer gets
6. Why it works
7. Offer stack
8. Risk reversal
9. Urgency or reason to act now
10. FAQ and final CTA

Do not fabricate real endorsements, real credentials, real scarcity, or real legal claims. Fictional templates can use clearly fictional names and demo proof.

