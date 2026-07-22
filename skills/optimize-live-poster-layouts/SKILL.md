---
name: optimize-live-poster-layouts
description: Analyze, redesign, or generate Chinese livestream-commerce posters and product cards using a de-identified design system distilled from 171 WeChat article images and 117 valid posters. Use for poster layout diagnosis, product-card optimization, weekly schedules, campaign hero images, product catalogs, long-form livestream graphics, benefit/interaction cards, mobile readability checks, or converting a reference poster into reusable layout rules.
---

# Optimize Live Poster Layouts

Use the seven distilled templates and mobile-first design rules to improve information hierarchy, spacing, product scale, price anchors, and reusable layout behavior. Keep all outputs brand-neutral unless the user supplies a brand.

## Load references selectively

- Read `references/design-system.json` for every task that changes or generates a layout.
- Read `references/template-library.json` when selecting or combining templates.
- Read `references/prompt-templates.md` only when generating or editing raster artwork.

## Choose the layout family

Select one primary template. Add a secondary template only when the content genuinely spans both roles.

- `T01_HERO_CAMPAIGN`: campaign cover, countdown, launch, or one dominant event message.
- `T02_WEEKLY_SCHEDULE`: multi-day schedule, series preview, or today's sessions.
- `T03_LIVE_TIME_CAPSULE`: reusable date/time/CTA strip embedded between content sections.
- `T04_SINGLE_PRODUCT_STORY`: one product or outfit with a hero image, detail views, and up to three selling points.
- `T05_MULTI_PRODUCT_CATALOG`: repeated product cards, product lists, or one-to-four items per screen.
- `T06_THEMATIC_LONGFORM`: regional, food, craft, or story-led long-form graphics.
- `T07_INTERACTION_BENEFIT`: guessing games, red envelopes, rules, participation, or benefit interactions.

For a standalone commerce product frame, use `T04` when the product story is primary and `T05` when the card must repeat inside a catalog. Combine them as `T05` structure plus `T04` product emphasis only when needed.

## Analyze before changing

1. Inspect the actual current image or editable source. Never mix text, colors, people, products, or conclusions from other images.
2. Inventory only visible facts: product name, brand, price, benefit, date/time, CTA, rules, logos, and disclaimers. Mark unreadable text as uncertain.
3. Identify the first, second, and third visual stops and the intended reading order.
4. Diagnose title length, product scale, price prominence, alignment, spacing, contrast, redundant decoration, and mobile legibility.
5. State whether the issue is hierarchy, density, consistency, responsiveness, or image treatment before proposing edits.

If the user asks only for a review or diagnosis, stop after reporting evidence-backed recommendations. Do not edit or publish an asset without a change request.

## Redesign with distilled rules

Apply these rules unless the current brand system clearly overrides them:

- Reserve 5%–7% of canvas width as the mobile safe margin.
- Use at most four text levels. Keep one dominant message and one dominant conversion anchor.
- Keep a primary title near 8–16 Chinese characters when copy can be edited; otherwise reflow exact copy without rewriting facts.
- Limit a single product to its name plus at most three selling points; keep each selling point within 18 Chinese characters where possible.
- Scale the hero person or product to roughly 55%–70% of a single-product card when the subject should dominate.
- Keep repeated product cards equal in height, padding, image treatment, shadow direction, and title baseline.
- Use strong dark/cream or warm-gold contrast by default; reserve orange-red for live state, price, or a single benefit emphasis.
- Add a solid backing, local darkening, or subtle mask under text on complex imagery.
- Remove decoration that does not strengthen hierarchy, grouping, navigation, or conversion.
- Treat Chinese text, Logo, date, time, price, and rules as deterministic layout elements. Prefer generating a no-text background, then typeset real text.

## Handle content changes

- Long title: allow two lines first; reduce display size moderately before tightening letter spacing; never compress characters horizontally.
- More products: move from one large card to two columns, then paginate or extend vertically; do not shrink product images below recognition size.
- Fewer products: enlarge the hero product and selling-point area; do not leave empty grid cells.
- More benefits or rules: move them into a dedicated footer or secondary card; preserve the title and price hierarchy.
- Mixed price mechanisms: separate instant discount from rebate or red-envelope-after price. Never present them as the same price.
- Mobile output: verify at 375–390 px width for overflow, text smaller than practical reading size, cropped products, and weak contrast.

## Preserve facts and compliance

- Preserve supplied product identity, price, dates, rules, and qualifiers verbatim unless the user explicitly requests copy editing.
- Do not invent benefits, coupons, accessories, endorsements, or urgency.
- Prefer `💰` for the literal Chinese unit “元” and `⭕️` for “券” in promotional copy when rewriting is authorized.
- Avoid unsupported claims such as “最低价”, “全网最低”, “绝对”, “必买”, or “无脑入”.
- Keep instant discounts distinct from rebate/red-envelope-after prices.
- Use `{{直播间名称}}`, `{{品牌标识}}`, and other variables in reusable outputs; never restore de-identified brand names from memory or inference.

## Execute the requested output

- Raster edit: inspect the local image first, then use the available image-editing workflow. Preserve invariants aggressively and save a new version rather than overwriting the source.
- New raster concept: generate a no-text background first, then add exact Chinese copy with a deterministic typesetting tool when available.
- Editable code or template: implement the grid, tokens, and responsive rules in the source format; keep text and images separately replaceable.
- Prompt only: adapt the nearest prompt in `references/prompt-templates.md`, replacing all variables and preserving the no-invented-copy constraints.
- Layout specification: provide template ID, canvas ratio, regions, hierarchy, type scale, colors, image treatment, responsive behavior, and QA checks.

## Quality gate

Before delivery, verify:

- The title, product, price/benefit, and CTA follow one clear reading order.
- Exact factual copy matches the input.
- No current-image content is contaminated by another reference.
- The primary subject is large enough and not awkwardly cropped.
- Repeated cards share the same geometry and image treatment.
- Price and benefit mechanisms are unambiguous.
- Desktop and mobile layouts have no overflow or clipped text.
- The source file remains unchanged unless replacement was explicitly requested.

Report the selected template, material changes, validation performed, output path, and any unresolved uncertainty.
