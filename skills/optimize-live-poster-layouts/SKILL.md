---
name: optimize-live-poster-layouts
description: Analyze, distill, redesign, or generate Chinese livestream-commerce posters, Xiaohongshu 3:4 graphics, WeChat long-form visuals, campaign covers, schedules, product cards, catalogs, and benefit-interaction posts. Use when Codex must diagnose hierarchy or aesthetics, preserve exact Chinese copy while changing a layout, convert reference images into reusable design rules, select one of seven commerce-poster structures, generate a no-text visual background, specify deterministic typesetting, or run mobile-readability and anti-AI-slop QA.
---

# Optimize Live Poster Layouts

Build commerce posters from two independent decisions:

1. **Structure**: choose the information architecture from `references/template-library.json`.
2. **Aesthetic direction**: derive the visual language from the user's brand/reference or `references/aesthetic-system.md`.

Never treat a template as a fixed visual style. Preserve supplied facts and brand assets exactly.

## Load only what the task needs

- Read `references/design-system.json` for every redesign, generation, or layout specification.
- Read `references/template-library.json` when selecting or combining T01-T07.
- Read `references/aesthetic-system.md` when judging style, matching references, or generating a new direction.
- Read `references/prompt-templates.md` only for raster generation or editing.
- Read `references/quality-rubric.md` before delivering any changed or generated artifact.
- Read `references/evaluation-cases.json` only when testing or maintaining this skill.
- Do not load `references/dataset-manifest.json` during ordinary poster work; it contains aggregate provenance only.

## Classify the request

Choose one mode before acting:

- `AUDIT`: diagnose the current poster and stop after evidence-backed recommendations.
- `REDESIGN`: preserve facts and required assets while changing structure or style.
- `GENERATE`: create a new poster, background, editable template, or layout specification.
- `DISTILL`: turn one or more references into reusable rules without copying protected artwork.
- `PROMPT`: return a filled generation prompt and typesetting specification only.

Do not edit or publish an asset in `AUDIT` mode. Do not rewrite copy unless the user requests copy editing.

## Inspect before designing

1. Inspect every supplied image or editable source separately.
2. Inventory only visible or user-supplied facts: title, brand, product, price, benefit, date/time, CTA, rules, logos, disclaimers, people, and required imagery.
3. Mark unreadable text as `识别不确定`; never complete it from context.
4. Record invariants that must not change.
5. Identify the current first, second, and third visual stops.
6. Diagnose the dominant problem: hierarchy, density, consistency, composition, image treatment, aesthetic mismatch, factual contamination, or mobile readability.

When several references are supplied, assign each a role such as `content source`, `style source`, `character source`, or `layout source`. Never mix their roles implicitly.

## Select structure and output profile

Choose one primary template from T01-T07. Add one secondary template only when the content genuinely spans both roles. State the choice internally before generating.

Use these output defaults unless the user specifies otherwise:

- Xiaohongshu feed: `3:4`, recommended `1080x1440`.
- Instagram feed: `4:5`, recommended `1080x1350`.
- Story/video cover: `9:16`, recommended `1080x1920`.
- WeChat article: content-led long image or the source width; avoid forcing a social-feed ratio.

Do not stretch an existing design to a new ratio. Recompose it.

## Derive the aesthetic direction

Use this priority order:

1. Explicit brand guidelines and supplied assets.
2. User-designated style reference.
3. Category, audience, campaign goal, and channel context.
4. A suitable profile from `references/aesthetic-system.md`.

Before creating, produce a compact internal design read:

`<artifact> for <audience>, communicating <primary message>, using <aesthetic direction>, with density <1-5> and commercial intensity <1-5>.`

Avoid generic AI defaults unless the brief requires them: purple-blue mesh gradients, floating glass cards, equal three-card layouts, meaningless sparkles, excessive stickers, fake 3D chrome, random English microcopy, and decoration without an information role.

## Build protected reading zones

Classify every visible element:

- `CRITICAL`: title, date/time, price or primary benefit, CTA, safety/compliance statement. Never crop, obscure, or place on uncontrolled visual noise.
- `SUPPORT`: product name, selling points, labels, secondary rules. Keep readable at intended mobile size.
- `GRAPHIC`: people, products, giant numerals, patterns, textures, decorative type. May overlap or crop when it does not damage critical reading.

Give every critical block a controlled local contrast field. Keep one dominant message and one dominant conversion anchor. Use no more than four text levels.

## Execute without contaminating facts

- Preserve product identity, dates, prices, rules, qualifiers, people, and logos verbatim unless explicitly authorized to change them.
- Never invent benefits, coupons, accessories, endorsements, urgency, or missing text.
- Keep instant discounts distinct from rebates, red-envelope-after prices, and conditional prices.
- When promotional copy editing is authorized, prefer `💰` for the literal Chinese unit `元` and `⭕️` for `券` only if this matches the requested channel convention.
- Avoid unsupported claims such as `最低价`, `全网最低`, `绝对`, `必买`, or `无脑入`.

For raster generation, separate production into two contracts:

1. **Visual background**: generate composition, subject, lighting, materials, and reserved text fields. Request no letters, numerals, logos, watermarks, or fake UI.
2. **Typesetting specification**: place exact Chinese copy, numbers, Logo, price mechanisms, and rules with deterministic text tools when available.

If deterministic typesetting is unavailable, disclose the risk and verify all rendered text visually.

## Adapt content safely

- Long title: use two lines before reducing size; never horizontally compress Chinese characters.
- More products: move from one card to two columns, then paginate or extend vertically; preserve recognition size.
- Fewer products: enlarge the hero subject and selling-point area; do not leave dead grid cells.
- More benefits/rules: move them to a dedicated footer or secondary card; preserve title and conversion hierarchy.
- Complex imagery: add a solid field, controlled local darkening, or mask under critical text.
- Repeated cards: keep height, padding, title baseline, image treatment, and shadow direction consistent.

## Validate before delivery

Apply `references/quality-rubric.md`. Required gates:

- Exact factual copy matches the input.
- No content from another reference contaminates the current artifact.
- The title, key fact/date, price or benefit, and CTA form one obvious reading path.
- Critical text has a protected contrast channel.
- The primary subject is recognizable and intentionally cropped.
- The result works at thumbnail scale and at 375-390 px mobile width.
- No generated gibberish, clipped text, overflow, or ambiguous price mechanism remains.
- The visual direction is specific to the brief rather than a generic AI style.
- The source remains unchanged unless replacement was explicitly requested.

Report the selected mode, template, aesthetic direction, material changes, validation result, output path, and unresolved uncertainty.
