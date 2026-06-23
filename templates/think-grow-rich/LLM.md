# Repurpose this template for a new book / product — LLM brief

You are an **elite entertainment art director + conversion copywriter**. Repurpose
this **editorial art-deco book sales page** for a new offer — most naturally
another **book or info-product that links out to a retailer (Amazon, etc.)** —
while preserving its structure, motion, and premium graphics-led feel.

Read the `entertainment-designer` and `landing-page-design-process` skills and
`DESIGN_GUIDELINES.md` first. Everything uses the repo tools (fal.ai + Pillow);
`FAL_KEY` is already in the repo-root `.env`.

## What this template is

A **long-form editorial** archetype (no video, no host widget — both optional in
this kit). Sticky deco nav → literary hero (floating product + signature backdrop)
→ stat strip with count-ups → origin/story split with a duotone portrait →
principles/features (icon medallions + numbered list) → pull-quote → what's inside
(spec `<dl>` + takeaways) → reader acclaim → buy/offer → FAQ → final CTA → footer.
**One image CTA** (reused), CSS buttons for the rest.

## What NOT to change

- The section architecture, the reveal/parallax/count-up/FAQ motion system, and
  the component classes (`.hero`, `.split`, `.pillars`, `.thirteen`, `.pull`,
  `.inside`, `.reviews`, `.offer`, `.faq`, `.final`).
- The ethos: graphics-led, low-text, one promise per section, one CTA per zone,
  one image CTA + CSS buttons, no emojis, no invented SVG icon art, no orphan words.
- **Contrast discipline:** label colour comes from the *fill* (dark ink on gold/
  pastel; light on deep), card text reads on the card, the logo/seal text reads on
  both light and dark. See DESIGN_GUIDELINES §2.

## Steps

### 1. Rebrand `brand/brand.json`
Set `name`, `tagline`, `seed`, the new niche **palette** (real hexes), and a new
one-sentence **`styleSignature`** (medium, lighting, exact palette, texture, mood;
end with "No text, no words, no letters."). This string is prepended to every
image prompt. Recolor `assets/styles.css` `:root` to match — don't restructure.

### 2. Regenerate assets from `assets/prompts/manifest.json`
Keep the same filenames so HTML/CSS keep working. Per entry, generate
`styleSignature + subjectPrompt` (rewritten for the new niche) then the post step:

```bash
# signature backdrop (FLUX ultra) -> webp
python3 tools/fal.py image --prompt "<sig + backdrop>" --aspect 16:9 --seed <SEED> --out raw/hero-deco.jpg
python3 tools/imgkit.py webp raw/hero-deco.jpg assets/img/hero-deco.webp --max 1920

# cutouts: generate -> fal bg (BiRefNet) -> imgkit alpha   (book/product, seal, star, quote, emblem)
python3 tools/fal.py bg --image raw/<x>.jpg --out raw/<x>-cut.png
python3 tools/imgkit.py alpha raw/<x>-cut.png assets/img/<x>.png --size <N>

# icon set: ONE shared descriptor across all -> webp, circle-cropped in CSS
python3 tools/fal.py image --prompt "<sig + ONE shared deco descriptor + subject>" --aspect 1:1 --seed <SEED> --out raw/ic-x.jpg
python3 tools/imgkit.py webp raw/ic-x.jpg assets/img/ic-x.webp --max 480
```

- **Product image**: if you have the real cover/product, just `fal.py bg` it (like
  the book here). Otherwise generate it.
- **Portrait/author**: a real photo treated to duotone in CSS (`.portrait img`
  filter + `mix-blend-mode`) reads as authentic — reuse that treatment.

### 3. Regenerate the ONE image CTA (`assets/img/btn-cta.png`)
Ideogram v3, short label on **one line**, finish derived from the brand. Generate
2–3 candidates, keep the best; regenerate any that wraps, goes two-tone, or whose
lettering doesn't read against its own material. Update every `alt` to match.

```bash
python3 tools/fal.py image --model fal-ai/ideogram/v3 --aspect 3:1 \
  --prompt "<brand-styled wide pill, engraved same-material lettering reading exactly '<LABEL>', one line, plain white background, no wrap/stripes/seam/emoji/icons>" \
  --out raw/btn.jpg
python3 tools/fal.py bg --image raw/btn.jpg --out raw/btn-cut.png
python3 tools/imgkit.py alpha raw/btn-cut.png assets/img/btn-cta.png --pad 6
```

### 4. Rewrite the copy in `index.html`
Short, benefit-led, one promise per section. Replace: nav, hero eyebrow/headline/
lede/ribbon, stat-strip numbers + `data-count`/`data-suffix`, the origin story +
portrait caption + signature, the pillar cards + the numbered list, the pull-quote
+ attribution, the spec `<dl>` + takeaways, reviews, offer chips/price, FAQ, final
CTA, footer + disclaimer. Wire every CTA `href` to the new retailer link. Keep
headlines orphan-free (`&nbsp;` trailing phrases, intentional `<br>`).

### 5. Rebuild `brand/styleguide.html` and this template's `README.md`
Update palette swatches, type specimens, icon grid, CTA, scene to the new brand.

### 6. QA (serve + browser, 360/768/1280)
```bash
python3 -m http.server 8771      # from repo root
# open http://localhost:8771/templates/<slug>/index.html
```
No horizontal overflow; AA contrast on every button label / card / seal / logo;
reveals fire without a flash; count-ups run; FAQ toggles; mobile drawer opens and
closes (Esc / × / link); favicon loads; all CTAs hit the retailer.

## Bar
Every asset passes the glance test — instant impact, strong focal point, rich
color, readable silhouette, **legible label/text contrast**. If anything looks
generic, washed-out, cluttered, low-contrast, or a button is inconsistent,
regenerate it. The page reads as a premium, graphics-led marketing experience —
a gallery, not a document.
