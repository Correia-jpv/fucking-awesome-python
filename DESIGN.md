# awesome-python.com DESIGN.md

awesome-python.com is a searchable, filterable index of ~650 curated Python projects. It is a reference tool, not a landing page and not a GitHub README mirror.

This file follows the [Google Stitch DESIGN.md format](https://stitch.withgoogle.com/docs/design-md/overview/). The source of truth for token values lives in `website/static/style.css`. Color tokens here are written in OKLCH because the project mandates OKLCH over hex, which is a deliberate divergence from the spec's hex-only token requirement.

## Overview

Three words: **opinionated, confident, dense**.

Working Python developers (mid to senior) are the target reader. They write Python daily and arrive with a specific question in mind: "what's a good HTTP client these days", "is there still a maintained ORM for X", "what are people using for task queues now". Secondary readers: polyglot developers evaluating Python's ecosystem, and curious browsers.

Jobs to be done:

1. Find a library for a specific need fast (search + tag filter).
2. Compare candidates at a glance (stars, last commit, tags, one-line description).
3. Confirm a project is alive before clicking through.

These users skim. They reward density and terse copy. They penalize marketing fluff.

Voice:

- Editorial. Every word earns its place.
- Confident, not combative. "This is the list" energy, not "check out these cool projects".
- No hype. The content is what's interesting.
- Calm authority. Closer to a well-edited technical reference (O'Reilly index, The Economist briefing, a good man page) than a blog or product site.

Emotional goals: trust, efficiency, craft. The reader should feel the list was edited by someone with taste, find what they need in seconds, and notice the typographic care as a signal that the curation is careful too.

Reference points (stay close to these):

- **https://www.placestoread.xyz** is the primary visual model for the table, expand row, sorting, and footer. "Like placestoread" means dense single-page list, inline click-to-expand rows that indent under the Name column, sortable headers, minimum decoration. When in doubt about a table or row treatment, check placestoread first.
- Magazine reference pages (The Economist, FT Weekend, Monocle).
- Field-guide books. Curated, functional, hand-made.
- Library card catalogs. Dense tabular information, excellent typography, no decoration for decoration's sake.

Anti-references (avoid strictly):

- Generic dark developer-tool look. No cyan on near-black, neon gradients, VSCode-palette dashboards, terminal-green monospace branding.
- Other awesome-* sites. No plain README dumps, bare lists of links, no voice.
- SaaS marketing pages. No big metric counters, testimonial cards, feature grids, pricing tiers, or "join 10,000+ developers" social proof bands.

Design principles:

1. **The list is the hero.** Hero, sponsor band, and CTA exist, but they must not compete with the table for attention.
2. **Density is a feature.** Prefer tables and tight rhythm over giant cards with one fact each. Mid-senior developers want to see more at once.
3. **Editorial typography over decoration.** Visual interest comes from the serif/sans pairing, type hierarchy, and whitespace. Not from gradients, shadows, badges, or icon boxes above headings.
4. **Warm, not cool.** Neutrals tint toward warm hues (roughly 55 to 80 in OKLCH). Pure grays and cool blues do not belong.
5. **One point of view.** No dark mode, no theme picker, no alternate palettes. Consistency signals curation.

## Colors

Warm editorial palette. Light theme only (`color-scheme: light`). OKLCH only.

Surfaces:

- `--bg-page` `oklch(96.8% 0.018 80)`. Cream/ivory canvas. The default page background.
- `--bg-paper` `oklch(98.6% 0.01 80)`. Warm white for the content shell.
- `--bg-paper-strong` `oklch(95.7% 0.016 76)`. Tinted paper for sponsor band, CTA backgrounds, static decoration.
- `--hero-bg-start` → `--hero-bg-end` `oklch(14% 0.03 32)` → `oklch(28% 0.05 42)`. Dark earthy hero gradient.
- `--footer-bg` `oklch(16% 0.025 35)`. Dark warm charcoal footer, part of the same system.

Ink:

- `--ink` `oklch(22% 0.02 55)`. Body text.
- `--ink-soft` `oklch(38% 0.018 55)`. Secondary copy.
- `--ink-muted` `oklch(52% 0.02 55)`. Meta rows, captions, static labels.
- `--line` / `--line-strong`. Hairlines and dividers.

Accent (warm brown-red, reserved for interactive):

- `--accent` `oklch(58% 0.16 45)`. Primary accent.
- `--accent-deep` `oklch(44% 0.15 42)`. Link text, hover.
- `--accent-soft` `oklch(92% 0.045 55)`. Tinted background for filter tags.
- `--accent-underline` `oklch(58% 0.16 45 / 0.4)`. Subtle text-decoration-color.

Rules:

- Use OKLCH for any new color. Not HSL, not hex.
- Accent tokens (`--accent`, `--accent-deep`, `--accent-soft`) are reserved for interactive elements. Clickable filter tags (`.tag`) correctly use `--accent-soft` background with `--accent-deep` text. Interactive link states (`.col-name > a:hover`, `.sponsor-link:hover`, `.hero-action-primary`, `.back-to-top`, CTAs) use accent tokens.
- Non-interactive elements (inline code, `.source-badge`, static labels, decorative pills) must use `--ink-muted`, `--ink-soft`, or `--bg-paper-strong`. Never the accent. Users should not mistake static decoration for something clickable.
- Same role uses the same token everywhere. No one-off inline `color: oklch(...)` buried in a rule.

Aversions:

- **No green.** The user rejected it when picking the palette. Warm brown-red, ivory, and dark earthy tones are the established system. Do not introduce green even for success states or ancillary accents.
- No cyan, no neon gradients, no pure grays, no cool blues.

## Typography

Pairing (do not swap):

- **Display**: `Cormorant Garamond` (serif, 600 only).
- **Body**: `Manrope` (sans, 400 / 600 / 700 / 800).

Scale tokens (`:root`):

- `--text-xs` `0.8rem` (12.8px). The smallest token. Pills, badges, tags, captions, footnotes.
- `--text-sm` `0.95rem`. Meta rows, secondary copy.
- `--text-base` `1rem` (16px). Body floor.
- `--text-lg` `1.125rem`. Content-heavy passages.
- Magazine-cover scale for the main headline: `clamp(4.5rem, 11vw, 8.5rem)`. Then a tight modular scale for the rest.

Hard-won sizing rules (do not relax):

- **Body type floor is 16px.** Do not go smaller.
- **Absolute minimum font size is 12px (`0.75rem`) for ANY text**, including pills, badges, tags, captions, footnotes. Anything smaller hits Chrome's default minimum-font-size floor and renders inconsistently across browsers and user accessibility settings. Use `var(--text-xs)` (`0.8rem`) as the smallest token in code.
- **When in doubt, pick one step larger** than what generic scale references suggest. The user has corrected sizes upward 11+ times across 8 sessions. Footer, meta rows, expand content, labels, and headings all trend too small by default. **Never reduce an existing size unprompted.**
- Adjacent heading levels differ by at least 0.25rem of rendered size.
- Row numbers in the table: left-align, no leading zeros. Zero-padding was tried and rejected.
- **Never `text-transform`.** Write the casing in the markup.

## Layout

- **Single width cap: `--shell-max: 84rem` (~1344px) applied via `.section-shell`.** This is the ONLY width cap in the project. Widescreen monitors are the default viewing context.
- **Do NOT add `max-width`** to sections, cards, table cells, table rows, expanded rows, CTA backgrounds, sponsor descriptions, hero subcopy, paragraphs, or list items. The user has removed narrow inner caps repeatedly (`56ch`, `65-75ch`, etc.). Default is no inner cap.
- The "cap line length at ~65-75ch" rule does NOT apply here. Ignore it. Readability at wide widths is carried by vertical rhythm, leading, and the modular type scale instead.
- If a width cap is genuinely necessary for a specific element, ask first with a concrete reason before adding it.
- Shell padding: `--shell-pad: clamp(1.25rem, 3vw, 2.5rem)`. Symmetric gutters: logo left-gap equals logo right-gap, column paddings match across header and body.
- `gap` over child margins in flex and grid.
- Logical properties (`margin-inline`, `padding-block`) over physical (`margin-left`, `padding-top`).
- `rem` for spacing and type. `px` only for borders and shadows.
- CSS custom properties for all colors and repeated values.
- Sibling components (card lists, grid items) share identical spacing.
- Never `!important`. Fix specificity instead.

## Elevation & Depth

Depth comes from **tonal layers**, not heavy shadows.

- The page is a quiet warm canvas (`--bg-page`). The content shell is slightly brighter paper (`--bg-paper`). The sponsor band, CTA backgrounds, and inline decorative blocks step up to `--bg-paper-strong`.
- The hero is the one place that uses real atmosphere: subtle grid, slow sheen, warm radial gradients on a dark earthy ground (`--hero-bg-start` → `--hero-bg-end`). The sheen and any other motion respect `prefers-reduced-motion`.
- The footer is a single tonal block in `--footer-bg`, no internal gradients.
- Box shadows, when used at all, are 1px soft inset/outset for separation only. No drop-shadows-as-decoration.
- No glassmorphism as default decoration.
- No bounce or elastic easing. Real objects decelerate smoothly.

## Shapes

The shape language is overwhelmingly **pill on small, zero radius on large**.

- **Pills** (`border-radius: 999px`) for tags, search, sponsor logo chip, source badges, back-to-top, and primary CTA buttons.
- **`0.4rem`** is used in one expand-row callout. Do not introduce a tokenized radius scale. The project does not need one.
- Containers use the page surface itself, not rounded panels. When a panel is needed, prefer pill on small chips and zero radius on large surfaces.
- **No `border-left` or `border-right` greater than 1px as a colored accent stripe** on cards, list items, callouts, or alerts. Use a different structure.

## Components

The component vocabulary is small and table-led. Source of truth: `website/static/style.css`.

- **Table-driven index** (the hero of the page). Sticky header, sortable columns, click-to-expand rows that indent under the Name column. Modeled on placestoread.xyz. Not a card grid.
- **Filter tags** (`.tag`). `--accent-soft` background with `--accent-deep` text. Pill shape. Hover lifts border to `--tag-hover-border`. Active state uses the warm `--tag-active-start` → `--tag-active-end` gradient. Tag variants (`group`, `subcat`, `source`, `built-in`) inherit the base `.tag` style and differ only where a real difference is needed.
- **Hero**. Magazine-cover headline, dark earthy ground, kicker and proof microcopy, primary CTA button using `--hero-btn-start` / `--hero-btn-end`. Subtle grid plus slow sheen. Respects `prefers-reduced-motion`.
- **Sponsor band**. Sits in the README header on `--bg-paper-strong`. Editorial layout, not a logo wall. Sponsor links share the global accent treatment.
- **CTA**. Warm `--cta-bg`, full-bleed within shell. The button itself uses accent tokens.
- **Footer**. Dark warm charcoal, part of the same system. Footer links share the global hover and focus treatment.
- **Search**. Pill input with `--search-inset` interior and `--search-focus-ring` focus ring. Focus shadow uses `--search-focus-shadow`.
- **Source badge / inline code**. Static decoration on `--bg-paper-strong` with `--ink-muted` text. Never the accent.

Peer-consistency check (run before shipping any visual change):

- Hover and focus states: if one link type gets a treatment, peer links (hero topbar, footer, project names, sponsor names, expand-meta) share it.
- Tag variants inherit the base `.tag` style. Differ only where a real difference is needed.
- Typography tiers: labels that play the same role share size, weight, and letter-spacing.
- Symmetric gutters: logo left-gap equals logo right-gap, column paddings match across header and body.
- Role-based color tokens: same role uses the same token everywhere.

## Do's and Don'ts

- **Do** keep the table the focal point. Hero, sponsor band, and CTA must not compete.
- **Do** use accent tokens only on interactive elements.
- **Do** prefer density over whitespace expansion.
- **Do** check peer elements before shipping a visual change.
- **Do** use OKLCH for every new color.
- **Don't** add inner `max-width` to anything. The shell handles width.
- **Don't** introduce green, cyan, neon, pure gray, or cool blue.
- **Don't** add a dark mode, theme picker, or alternate palette.
- **Don't** use gradient text (`background-clip: text` on gradients). Solid color only.
- **Don't** use `!important`. Fix specificity instead.
- **Don't** use `text-transform`. Write the casing in markup.
- **Don't** use a `border-left` or `border-right` greater than 1px as an accent stripe.
- **Don't** use bounce or elastic easing.
- **Don't** use glassmorphism as default decoration.
- **Don't** mimic generic dark developer-tool sites, other awesome-* sites, or SaaS marketing pages.

## Narrow-Screen Behavior

The user actively tests `< 960px` and `< 680px`. Narrow screens must stay functional.

- Do not drop features the user might want (sort affordance, filter chips, sticky header where reasonable). Hiding is a last resort and requires justification.
- Always run the `playwright-cli` skill at a narrow viewport after any layout change.

## Verification

After any frontend change, use the `playwright-cli` skill to visually verify in a real browser. Check layout, responsiveness, and interactive behavior. Do not claim a UI change works based on code alone.
