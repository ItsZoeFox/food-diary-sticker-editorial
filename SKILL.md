---
name: food-diary-sticker-editorial
description: "Transform one original food photograph into a faithful, warm personal food-diary image: preserve the real homemade dish's exact shapes, quantities, positions, overlaps, imperfections, and unoutlined photographic identity; gently improve global color and context without re-plating; clean or rebuild only the surroundings; and add one clean recognizable watercolor or original pixel-art sticker plus integrated food-derived flow lines. Use for sentimental homemade-meal records, desserts, restaurant spreads, street food, cluttered dining-table photos, or creative food edits where authenticity matters more than commercial perfection."
---

# Food Diary Sticker Editorial

Create one polished food photograph with one restrained illustrated sticker. The result should feel newly art-directed without turning the food into an illustration or advertisement.

## Preflight Defaults

Before editing, ask one concise question unless the user has already answered it: **“是否还需要一张原图与处理图并排展示的前后对照版？”**

- Default deliverable: the processed image only. Create the comparison version only when requested.
- Default processed-image size: exactly the same pixel dimensions and aspect ratio as the source photograph. Change size or crop only when the user asks. If the generator cannot emit the exact pixel dimensions, request the same aspect ratio and perform one deterministic final resize/crop from the first successful edit; never regenerate merely to change dimensions.
- Default sticker style: clean watercolor. Use original pixel art only when the user requests it.
- When a comparison is requested, choose its direction from the source orientation: for a portrait source, place the untouched original on the left and the final processed image on the right; for a landscape or square source, place the untouched original above and the final processed image below. Keep both panels at the source dimensions, separate them with a thin neutral divider, and add no labels unless requested. Prefer `scripts/compose_food_comparison.py`, whose `auto` layout applies this EXIF-aware rule. Honor an explicitly requested direction instead.

## Workflow

1. Always begin from the user's original photograph. Never use a previously generated edit as the source unless the user explicitly requests it.
2. Inspect the image and identify:
   - the food subject or complete set of major dishes;
   - the most appetizing visual cues: crisp crust, caramel crackle, creaminess, steam, sauce, layers, char, fresh garnish, or contrasting ingredients;
   - clutter that can be removed without falsifying the meal;
   - a plausible scene family: home savory, dessert/tea, restaurant shared meal, or street food;
   - one sticker motif that can summarize the strongest food memory.
3. Treat personal homemade food as documentary evidence. Lock every visible ingredient's shape, count, scale, position, orientation, overlap, surface, sauce coverage, and natural imperfection. Do not regenerate, move, separate, standardize, enlarge, duplicate, delete, or re-plate real food.
4. Preserve the vessel, hand, and meaningful dining context by default. Permit only mild whole-image framing or perspective correction; never reshape the plate, bowl, rim, handles, or the food inside it.
   - **Explicit vessel-replacement exception:** replace dishware only when the user asks. Choose a vessel whose material, color, silhouette, and regional cues support the food, but keep the food footprint, liquid boundary, food-to-vessel contact, camera angle, and all ingredient geometry locked. Replace the vessel around the food; never re-plate the food to fit the new vessel.
5. Use subtractive cleanup only outside the food mass: remove obvious rim drips, crumbs, or scraps physically stuck above the food line. Do not clean inside the dish, reduce sauce among ingredients, untangle herbs, clarify broth, or improve ingredient arrangement.
6. Clean or rebuild the surrounding table scene to complement the food. Infer cuisine or region only from strong visible evidence or user-provided information; otherwise use a neutral setting matched to color, texture, and occasion.
7. Grade the complete food-and-background scene together, after composition and cleanup. Use one light direction, one white balance, coherent contrast, matching contact shadows, and consistent depth. Apply only a gentle global grade: natural warmth, a small midtone lift, restrained saturation, and low sharpening/clarity. Never locally repaint ingredients.
8. Keep the real subject integrated with the scene. Do not outline or cut out the food or vessel.
9. Add exactly one small sticker in the clearest available negative-space area. Default to clean transparent watercolor; use original pixel art when requested. Keep it vivid through clean color separation—not grease, muddy shadow, or noisy texture—and add an irregular warm-white die-cut border with a faint contact shadow.
10. Build food-derived effects as one coherent flow system: one or two incomplete lines that follow the vessel contour or dominant ingredient direction, plus at most three small attached accents. Avoid scattered marks.
11. Run the quality gates below and return the first successful version. Do not automatically generate a more polished or stylized version.

## Multiple-Dish Rule

Keep all major dishes photographic. Choose exactly one sticker subject.

Use this priority unless the user names a focal dish:

1. centrality and visual dominance;
2. apparent serving size;
3. distinctive shape, texture, or color;
4. narrative importance to the meal.

The sticker may depict one representative serving, ingredient relationship, or signature texture. Never make a sticker for every dish and never remove secondary dishes merely to simplify the composition.

## Scene Routing

- **Home savory:** choose a food-matched surface from stone, terrazzo, tile, lacquer, glass/metal, fine textile, or wood rather than defaulting to wood plus coarse linen. Use soft natural light and at most two quiet household props. Remove computers, cables, packaging, and unrelated work objects.
- **Dessert or tea:** lighter and more delicate. Favor pale stone, light oak, fine linen, restrained café or afternoon-tea cues, and colors derived from the dessert. Avoid rustic cooking props unless the dessert itself calls for them.
- **Restaurant shared meal:** retain the sense of people eating together and the restaurant's cuisine. Clean phones, bags, empty bowls, packaging, and loud printed clutter when they compete with the food. Preserve hands or diners when they add life without blocking dishes.
- **Street food:** retain an authentic street or night-market atmosphere, handheld gesture, and ambient light. Remove distracting plastic clutter when possible, but do not force the food into a pristine home-table scene.

When rebuilding a background, read [references/background-routing.md](references/background-routing.md). Select one primary surface family from the food and vessel, then vary lighting and one minor prop. Within a batch, do not repeat the same primary surface family, textile treatment, or lighting motif unless the food genuinely requires it.

## Stable Food Grade

- Grade the full composite only after perspective correction, food cleanup, and background placement.
- Match light direction, softness, white balance, exposure, contrast, contact shadow, and depth across food, vessel, table, and props.
- Keep midtones gently lifted and highlights controlled. Use medium-low contrast, moderate natural saturation, low sharpening, and low clarity by default.
- Preserve category-specific appetizing cues: clear golden broth, restrained glaze, browned crust, fresh greens, creamy softness, or crisp caramel. Do not apply one universal orange or high-clarity filter.
- Use global correction only on the real dish. Do not repaint, smooth, reshape, recolor, relight, or add highlights to individual ingredients.
- Avoid HDR, halos, crushed shadows, neon greens, gray broth, orange cast, plastic sauce, oily film, waxiness, and crunchy microcontrast.

## Sticker Design

- Choose its position from available negative space after mapping every major dish. Prefer lower-right only when it remains visible and unobstructive; otherwise use another corner or edge zone that balances the composition.
- Never cover a major dish, diner gesture, or important vessel edge. Keep safe breathing room from the frame.
- Target roughly 15–20% of the canvas. Prioritize immediate visibility and dish recognition over making the sticker tiny.
- Choose one coherent style per image:
  - **Clean watercolor (default):** translucent washes, reserved-paper highlights, controlled pigment edges, minimal fine contour accents, and generous breathing room.
  - **Original pixel art (on request):** deliberate 16-bit-like square pixel clusters, crisp nearest-neighbor edges, compact sprite readability, limited cheerful palette, and a pixel-stepped white border. Borrow only broad genre language; never copy a named game's assets, characters, UI, palette, or exact style.
- Use brighter, more appetizing color than the real-food grade through moderately high saturation, clean ingredient separation, and strong light-dark grouping without neon color.
- Keep saturation independent from gloss and texture. A colorful sticker must still have low grease cues, clean shadows, and a fresh surface.
- Keep a recognizable silhouette and three to five decisive cues. Amplify the signature construction, cross-section, ingredient contrast, sauce, garnish, crust, or layers so a viewer can tell what kind of dish it represents without a label.
- Simplify secondary detail, but do not simplify away the food category. If the first motif reads as a generic bowl, bun, cube, or scoop, restore the characteristic filling, toppings, layers, or serving form.
- Exclude muddy brown masses, oily film, sauce puddles, dirt-like speckles, gritty pigment clumps, stained paper, heavy impasto, photorealistic meat texture, and noisy micro-detail. Judge the sticker at enlarged viewing size; it must remain clean.
- Outline only the sticker with a warm-white irregular cut edge.
- Use no text, face, mascot, speech bubble, arrow, label, logo, or watermark.

## Food-Derived Accent Marks

- Extract the palette and motion logic from the real dish: bowl ellipse, herb direction, sauce curve, ingredient axis, or serving gesture.
- Use one primary incomplete line and optionally one shorter secondary line. Let them follow the vessel contour or dominant ingredient flow without touching or enclosing the real food completely.
- Attach no more than three small flat accents to the lines. The line and accents must read as one continuous visual system rather than independent decorations scattered around the frame.
- Make every element flat and incomplete. It should read as graphic motion, not as a tiny leaf, fruit, meatball, chili, or other complete ingredient.
- Use no volume, internal food detail, realistic texture, cast shadow, splatter, crumbs, stains, or dirt-like dots.
- Reduce or omit marks when the scene lacks clean negative space.

## Quality Gates

Before returning, confirm all of the following:

- The viewer immediately recognizes the dish or meal.
- Direct comparison with the original confirms the same ingredient shapes, count, scale, positions, orientation, overlaps, quantity, sauce coverage, and homemade imperfections.
- The real food remains the hero and has no outline.
- The food looks believable, warm, and appetizing—not crunchy from sharpening, waxy, plastic, HDR, or oversaturated.
- The plate or bowl is intentionally aligned; its rim and handles are clean, while the food still looks naturally homemade.
- The background supports the food category and does not contain distracting electronics, bags, packaging, or unrelated clutter.
- The background uses one intentional primary material and does not fall back to wood plus coarse linen without a food- or context-based reason.
- In a multi-image batch, each image has a distinct surface family or clearly different scene logic while the set remains stylistically related.
- The subject and new background share coherent light direction, color temperature, contact shadow, and perspective.
- There is exactly one vivid white-bordered sticker, clearly visible in a non-obstructive negative-space area.
- The sticker communicates the dish category through silhouette plus at least three characteristic visual cues; it is not a generic food icon.
- Enlarging the sticker reveals clean color shapes rather than grease, dirt-like texture, muddy shadows, or random noise.
- Food-derived effects form one integrated orbital or directional line system; they are not scattered symbols, miniature ingredients, or realistic food debris.
- No artistic title, food name, annotation, arrow, logo, or watermark appears unless the user explicitly asks for text.
- No major dish has been invented, deleted, duplicated, or materially changed.
- The processed standalone has the source image's exact pixel dimensions unless the user requested another size.
- If a comparison was requested, a portrait source uses untouched original left and final processed image right; a landscape or square source uses untouched original above and final processed image below. Neither panel is stretched, cropped differently, or mislabeled.

## Priority Order

When goals conflict, use this order:

1. faithful and recognizable food
2. natural appetizing appearance
3. coherent food-specific scene
4. clean composition
5. charming sticker character
6. decorative effects

## Full Prompt Reference

Read [references/food-diary-sticker-prompt.en.md](references/food-diary-sticker-prompt.en.md) before generating or editing the image. The equivalent Chinese prompt is available at [references/food-diary-sticker-prompt.zh-CN.md](references/food-diary-sticker-prompt.zh-CN.md). Adapt the scene section to the actual food and supplied context; do not invent a specific cuisine when the evidence is weak.
