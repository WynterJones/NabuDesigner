#!/usr/bin/env bash
# Asset generation driver for the DragonForge sales page.
# Usage: bash salespage/gen.sh <group>   (run several groups in parallel as bg jobs)
set -u
cd "$(dirname "$0")/.."          # repo root
R=salespage/raw
IMG=salespage/assets/img
VID=salespage/assets/video
BR=salespage/brand
SEED=88231
SS="cinematic premium fantasy concept art, dark obsidian and molten-gold dragon theme, dramatic ember-orange and gold rim lighting against near-black backgrounds, glowing forge embers and floating sparks, jade-green dragon-scale accents and deep crimson, volcanic atmosphere with smoke and god rays, ornate gold filigree, layered depth, shallow depth of field, hyper-detailed, professional AAA fantasy game key-art quality, strong focal point, rich saturated color. No text, no words, no letters."
ICONSS="minimal premium emblem icon on a solid pure white background, glossy molten-gold and jade two-tone (#f4c044 gold and #36c08a jade), even medium stroke, subtle inner glow, matching a cohesive fantasy game icon set, centered, no text, no words, no letters."
img(){ python3 tools/fal.py image --seed "$SEED" "$@"; }

case "${1:-}" in

hero)
  img --aspect 16:9 --out $R/hero.jpg --prompt "$SS
An immense majestic dragon perched over a molten forge of glowing landing-page screens and golden UI panels, breathing a stream of ember sparks that forge into bright web layouts, obsidian volcanic cavern, towering scale, dramatic ember and gold rim light, floating sparks and smoke, cinematic depth, generous dark negative space on the lower-left for copy, epic AAA fantasy game key art."
  python3 tools/imgkit.py webp $R/hero.jpg $IMG/hero.webp --max 1920 --quality 84
  img --aspect 16:9 --out $R/og.jpg --prompt "$SS
A colossal golden dragon coiled around a glowing volcanic blacksmith forge anvil, molten gold and ember sparks erupting upward, obsidian cavern, dramatic god rays, wide cinematic hero composition with dark negative space on the left, epic AAA fantasy key art."
  python3 tools/imgkit.py webp $R/og.jpg $BR/og-image.png --max 1200 --quality 88
  # videos (long pole)
  python3 tools/fal.py video --image $R/hero.jpg --duration 5 --aspect 16:9 --out $R/hero.mp4 \
    --prompt "Create a seamless looping animation. Preserve the original artwork. Ember sparks drift upward, the dragon breathes faint glowing embers, forge light pulses, smoke rolls slowly, gentle parallax push-in. No large body movement, no scene changes, no camera cuts. Premium game-quality idle animation. 5-second seamless loop."
  python3 tools/vidkit.py web    $R/hero.mp4 $VID/hero.mp4 --max 1280
  python3 tools/vidkit.py poster $R/hero.mp4 $VID/hero-poster.jpg
  python3 tools/fal.py video --image $R/og.jpg --duration 5 --aspect 16:9 --out $R/forge.mp4 \
    --prompt "Create a seamless looping animation. Preserve the original artwork. Molten gold shimmer, ember sparks rise, forge glow pulses, slow smoke drift, gentle parallax. No large body movement, no cuts. 5-second seamless loop."
  python3 tools/vidkit.py web    $R/forge.mp4 $VID/forge.mp4 --max 1280
  python3 tools/vidkit.py poster $R/forge.mp4 $VID/forge-poster.jpg
  ;;

cutouts)
  # logo lockup
  img --model fal-ai/ideogram/v3 --aspect 16:9 --out $R/logo.jpg --prompt "Horizontal logo lockup on a plain flat MID-GRAY background: a glossy ornate golden dragon-head emblem fused with a blacksmith anvil on the LEFT, the bold wordmark 'DragonForge' in molten gold on ONE single line to its right. Only that one word, correct spelling, no tagline, no extra icons."
  python3 tools/fal.py bg $R/logo.jpg $R/logo-cut.png
  python3 tools/imgkit.py alpha $R/logo-cut.png $BR/logo.png --pad 8
  python3 tools/imgkit.py crop  $R/logo-cut.png $BR/logo-mark.png --box "0,0,0.26,1" --size 320
  python3 tools/imgkit.py favicon $BR/logo-mark.png $BR/favicon.png --size 256
  # headline graphic
  img --model fal-ai/ideogram/v3 --aspect 16:9 --out $R/hl.jpg --prompt "Epic 3D fantasy logo title text reading exactly 'DRAGONFORGE' on ONE single line, carved from molten gold metal with glowing ember edges and a forged-steel bevel, dragon-scale texture, dramatic rim light, plain pure white background, no other objects, perfect spelling."
  python3 tools/fal.py bg $R/hl.jpg $R/hl-cut.png
  python3 tools/imgkit.py alpha $R/hl-cut.png $IMG/hl-forge.png --pad 6
  # primary CTA button
  img --model fal-ai/ideogram/v3 --aspect 3:1 --out $R/btn.jpg --prompt "A premium 3D call-to-action button, wide rounded-rectangle filling the frame, rich molten-gold to ember-orange gradient with a glossy top sheen, crisp bright highlight along the top edge, soft golden outer glow, dragon-scale micro-texture, tactile pressable feel, high-end fantasy-game UI. Bold clean white sans-serif text on ONE single line reading exactly 'GET DRAGONFORGE', strong contrast, subtle dark shadow under the text. One continuous gold colour, no stripes, no two-tone, no seam, no emoji, no extra icons. Plain pure white background."
  python3 tools/fal.py bg $R/btn.jpg $R/btn-cut.png
  python3 tools/imgkit.py alpha $R/btn-cut.png $IMG/btn-cta.png --pad 6
  # mascot
  img --aspect 1:1 --out $R/mascot.jpg --prompt "$SS
An adorable yet fierce small golden baby dragon mascot, friendly expressive eyes, glossy gold and jade scales, tiny ember glow at the nostrils, perched and looking toward the viewer, full body, centered, clean plain background, premium 3D collectible mascot quality."
  python3 tools/fal.py bg $R/mascot.jpg $R/mascot-cut.png
  python3 tools/imgkit.py alpha $R/mascot-cut.png $IMG/mascot.png --size 760
  # coil divider
  img --aspect 16:9 --out $R/coil.jpg --prompt "$SS
An ornate golden dragon coiling in an elegant horizontal S-curve, glowing ember outline, isolated on a plain dark background, decorative section-divider accent."
  python3 tools/fal.py bg $R/coil.jpg $R/coil-cut.png
  python3 tools/imgkit.py alpha $R/coil-cut.png $IMG/coil.png --size 1400
  # seal medallion (empty center)
  img --aspect 1:1 --out $R/seal.jpg --prompt "$SS
An ornate empty circular golden dragon medallion coin seal with filigree dragon border and a blank smooth polished center, centered on plain background."
  python3 tools/fal.py bg $R/seal.jpg $R/seal-cut.png
  python3 tools/imgkit.py alpha $R/seal-cut.png $IMG/seal.png --size 360
  # play badge
  img --aspect 1:1 --out $R/play.jpg --prompt "$ICONSS A glossy gold circular play button with a forward triangle and an ember glow."
  python3 tools/imgkit.py keyout $R/play.jpg $IMG/play-badge.png --fuzz 30 --trim --pad 24 --size 220
  # check coin
  img --aspect 1:1 --out $R/check.jpg --prompt "$ICONSS A bold rounded checkmark inside a glowing gold dragon-scale coin."
  python3 tools/imgkit.py keyout $R/check.jpg $IMG/ic-check.png --fuzz 30 --trim --pad 28 --size 200
  ;;

cards)
  for c in \
    "card-fishing|A trophy bass leaping from teal dawn water, cinematic fishing scene, framed inside a luminous ornate golden slot-reel emblem, centered collectible game symbol." \
    "card-macaron|A tower of pastel French macarons glowing like treasure, soft patisserie light, framed inside a luminous ornate golden slot-reel emblem, centered collectible game symbol." \
    "card-saas|A floating neon SaaS app dashboard with glowing UI cards and a cute mascot, framed inside a luminous ornate golden slot-reel emblem, centered collectible game symbol." \
    "card-leadgen|A glowing email-capture play button with rising profit charts on a neon tech grid, framed inside a luminous ornate golden slot-reel emblem, centered collectible game symbol." \
    "card-wild|A radiant cracked golden dragon egg erupting with ember light, the ultimate jackpot WILD symbol with the most ornate gold filigree frame, framed inside a luminous slot-reel emblem, centered collectible game symbol." ; do
    id="${c%%|*}"; pr="${c#*|}"
    img --aspect 1:1 --out $R/$id.jpg --prompt "$SS
$pr"
    python3 tools/imgkit.py webp $R/$id.jpg $IMG/$id.webp --max 900 --quality 86
  done
  ;;

icons)
  for c in \
    "ic-anvil|a blacksmith anvil with a single rising flame" \
    "ic-spark|a four-point AI magic spark star" \
    "ic-terminal|a code terminal window with angle brackets inside" \
    "ic-chest|an open treasure chest overflowing with gold coins" \
    "ic-scroll|a fanned stack of three glowing template cards" \
    "ic-motion|a swirling motion vortex with trailing sparks" ; do
    id="${c%%|*}"; pr="${c#*|}"
    img --aspect 1:1 --out $R/$id.jpg --prompt "$ICONSS $pr."
    python3 tools/imgkit.py keyout $R/$id.jpg $IMG/$id.png --fuzz 30 --trim --pad 36 --size 256
  done
  ;;

*) echo "groups: hero | cutouts | cards | icons"; exit 1;;
esac
echo "DONE group ${1}"
