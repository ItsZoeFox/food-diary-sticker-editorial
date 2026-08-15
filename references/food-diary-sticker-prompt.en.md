# Food Diary Sticker Image-Editing Prompt

Use the user's original image as the sole source for the real food. Produce one finished editorial food-diary photograph. Default to the source photograph's exact pixel dimensions and aspect ratio. Default to one clean watercolor sticker; use original pixel art only when explicitly requested.

Before editing, ask whether the user also wants a top/bottom comparison image unless they already specified it. The default deliverable is the processed image only. When requested, create the comparison after the edit: untouched original above, final processed image below, equal-size panels, thin neutral divider, and no labels unless requested.

## Core Direction

Treat the image as documentary evidence of a specific meal, especially when it was cooked by the user or someone important to them. Preserve the exact photographic food and lock every visible ingredient's original shape, roughness, count, scale, position, orientation, overlap, unevenness, surface color, sauce coverage, and natural imperfection. Do not regenerate, redraw, beautify, round, enlarge, duplicate, delete, move, separate, untangle, standardize, reorganize, or re-plate any real food. Do not make homemade pieces more uniform or commercially styled.

Preserve the original vessel, food mass, hand, serving gesture, and meaningful dining context by default. Permit only mild whole-image framing or perspective correction. Never reshape the plate, bowl, rim, handles, or the food inside it. Replace dishware only when explicitly requested. In that exception, generate the new vessel around the locked food footprint and preserve the exact liquid boundary, contact relationships, perspective, and all ingredient geometry; never re-plate the food. Use subtractive cleanup only for obvious drips, crumbs, or scraps physically stuck on empty vessel areas above the food line. Do not clean within the food, reduce sauce among ingredients, clarify broth, separate crowded pieces, or modify quantities. Then rebuild only the surroundings as needed.

Grade the complete food-and-background composite together only after cleanup and scene construction. Match the background to the original food's existing illumination rather than relighting the food to match an invented set. Make the image gently inviting through global finishing only:

- slightly warmer, softer light;
- balanced exposure and natural color separation;
- restrained saturation;
- subtle highlights on caramel, sauce, cream, glaze, or crisp surfaces;
- low sharpening and low clarity;
- realistic texture, moisture, crumbs, and shadows.

Do not locally repaint, smooth, reshape, recolor, relight, gloss, or add highlights to individual ingredients.

Use one coherent light direction, softness, white balance, exposure family, contact-shadow logic, perspective, and depth of field across food, vessel, table, and props. Preserve the dish's own appetizing cue rather than applying a universal warm-orange filter: clear soup should remain translucent, glaze should shine only where physically expected, fried surfaces should retain browned texture, and fresh greens should remain natural.

Do not create HDR contrast, edge halos, crunchy micro-detail, plastic gloss, waxy surfaces, excessive saturation, artificial steam, fake cheese pulls, or invented garnishes.

## Scene Adaptation

Choose one setting from the visible evidence and user context:

- **Home savory:** refined but lived-in home table, warm wood or coordinated cloth, quiet ceramics, natural window light, at most two subtle props.
- **Dessert/tea:** airy dessert-table or café-at-home mood, pale stone or light wood, delicate linen, soft daylight, color accents derived from fruit, tea, caramel, chocolate, or cream.
- **Restaurant shared meal:** preserve all principal dishes and communal energy. Simplify the table surface and remove phones, bags, empty dishes, wrappers, and visually loud clutter. Keep hands or diners only when they support the moment.
- **Street food:** keep the handheld food and authentic street ambience, with soft night-market bokeh or a simple street table. Remove intrusive plastic clutter where possible while preserving truthful context.

When the food's cuisine or region is unambiguous, echo it subtly through material, cloth, ceramics, and palette. Avoid costume-like clichés, decorative stereotypes, and excessive props. When cuisine is uncertain, choose a neutral scene based on the food's dominant color and occasion.

Match the new background to the original subject's camera angle, focal length, perspective, light direction, color temperature, depth of field, and contact shadows. The result must feel like one photograph, not a cutout pasted onto a set.

## Sticker

Add exactly one sticker in the clearest available negative-space area, about 15–20% of the canvas. Lower-right is only a default: first map every important dish and meaningful gesture, then choose the corner or edge zone where the sticker is prominent, compositionally balanced, and does not cover food. Leave breathing room from the frame.

Derive the sticker from the dish's most memorable visual trait rather than copying the whole photograph. Examples include a caramelized ramekin top, one green ice-cream scoop with mango cubes, a representative fish slice with sauce and scallions, a crisp pork-belly cube, or the layered cross-section of a stuffed bun.

Preserve a recognizable silhouette and amplify three to five decisive cues such as construction, cross-section, filling, toppings, sauce, garnish, crust, or layers. The result must read as the specific dish type rather than a generic bowl, bun, cube, or scoop. Use brighter, more appetizing color than the real-food grade through moderately high saturation, clean ingredient separation, and readable light-dark grouping—not through stronger gloss or brown shading.

Choose one style:

- **Clean transparent watercolor (default):** translucent washes, reserved-paper highlights, controlled pigment edges, sparse fine contour accents, bright clean ingredient colors, and ample visual breathing room. Use only minimal paper texture.
- **Original pixel art (when requested):** chunky, deliberate square pixel clusters; crisp nearest-neighbor edges; compact sprite readability; limited cheerful palette; clean internal pixel outlines; no antialiasing, smooth vector curves, or 3D rendering. It may evoke the broad language of cozy life-simulation or colorful food-adventure games, but must not copy any named game's characters, assets, UI, palette, composition, or exact style.

In both styles, avoid muddy brown masses, greasy highlights, oil-film effects, sauce puddles, dirt-like speckles, random grain, dense pigment clumps, stained paper, heavy opaque impasto, photorealistic meat texture, and noisy micro-detail. Evaluate the sticker as if enlarged: it must remain clean and fresh. Add an irregular warm-white die-cut border—or a pixel-stepped version for pixel art—and a tiny clean contact shadow. No face, mascot, words, label, speech bubble, arrow, logo, or watermark.

For several dishes, keep every major dish photographic and choose only one sticker motif. If the user did not name the hero, select by centrality, size, visual distinctiveness, then narrative importance.

## Food-Derived Accent Marks

When clean negative space exists, create one coherent motion system derived from the food. Use one primary thin incomplete flow-line and optionally one shorter secondary line. Let them follow the vessel's ellipse, the dominant ingredient direction, sauce flow, or serving gesture without touching the real food or forming a complete enclosing ring. Attach at most three small flat accents to these paths.

The line and accents must read as a single orbital or directional gesture, not as independent symbols scattered around the frame. Every element must be nonrepresentational, flat, incomplete, and shadowless. Do not draw complete miniature leaves, fruits, meatballs, chilies, herbs, vegetables, or any other recognizable ingredient. Do not add volume, internal food detail, realistic texture, cast shadows, sauce splatter, crumbs, stains, or dirt-like dots. Reduce or omit the system if it competes with the subject or sticker.

## Negative Constraints

No text. No artistic title. No callout. No arrow. No outline around the real subject. No collage panel. No poster frame. No multiple stickers. No recursive editing from earlier generated versions. No removal, duplication, relocation, reshaping, standardization, re-plating, local repainting, or material change to real food.

Return the first version that is faithful, appetizing, coherent, clean, and charming.
