# Writing updates, guides and case studies

Set `name` and `description` in the root `site.json` using nonempty JSON strings. The builder uses them for site branding and discovery metadata, and adds the first character of `name` in the accent colour to the favicon background in `assets/favicon.svg`. Rebuild after changing these settings.

`skin` accepts `light` (the default reading design, including its system dark appearance) or `control`. `tagline` is a plain-text string shown below the wordmark on the control home page; it defaults to empty. On the light home page, a nonempty tagline follows the name heading. HTML in the tagline is escaped. The control home page uses a dark palette and a compact guides heading; contents and chapters use white reading surfaces and the same dark header. All skin tokens live in `assets/style.css`. Control uses local Noto Sans regular and semibold and Noto Sans Mono light, with their licence in `assets/fonts/OFL.txt`. Mint fills retain dark text, while mint-family links on white use a darker shade for contrast. Amber is reserved for warnings.

Create `content/your-guide/`. Use lowercase words separated by hyphens for the folder name. The guide slug `assets` is reserved for site assets. Add `index.md` with the guide title, description, and a short introduction. Add chapters named `01-your-chapter.md`, `02-next-chapter.md`, and so on. Chapter basenames must match `[0-9]{2}-[a-z0-9]+(?:-[a-z0-9]+)*\.md`: two digits, a hyphen, lowercase letters or digits separated by single hyphens, then `.md`. The folder contains only the contents source and chapters; there are no nested chapter folders. Invalid chapter names stop the build with the filename in the error.

Every source begins with simple front matter. Values are plain text on one line, without quotes or YAML features:

```
---
title: Read the response
description: Understand the shape before using the values.
order: 2
kind: guide
---
```

Use `title`, `description`, `kind`, and `order` on every `content/<slug>/index.md` contents source. `kind` is required and accepts only `update`, `guide` or `case-study`; chapters do not need it. Its `order` must be a positive integer unique within its kind: an update, a guide and a case study may share an order. Publish orders never change once published. Each section sorts by order. Updates have `Update NN` eyebrows and case studies have `Case study NN` eyebrows on cards and contents pages, preserving order gaps (for example, `Case study 01` and `Case study 02`). Guides have no numbered eyebrow. Home shows Updates, Guides, then Case studies (`id="case-studies"`), with peer h2 headings and singular or plural counts (`1 case study`, `2 case studies`), and omits empty sections. Card links read “Read the update”, “Explore the guide” or “Read the case study”; article metadata reads “<site> update”, “<site> guide” or “<site> case study”. Header links point only to existing Updates, Guides and Case studies home anchors; breadcrumbs start with Home. `llms.txt` and home Markdown group entries under Updates, Guides and Case studies, omitting empty groups. Missing or unknown kinds and missing, invalid, or duplicate orders stop the build with one error line and leave `dist/` untouched. Optional `series` on the contents source labels the breadcrumb and home card; optional `level` adds a label beside the chapter count and reading time. Omit either field to hide its label. The contents breadcrumb always includes the guide title. On chapters, `order` is a unique positive integer matching the two-digit filename prefix. The builder sorts by that number. The front matter title becomes the page's only h1. Use `##` for sections and `###` for subsections. Heading IDs come from lowercase words separated by hyphens; repeated headings receive numeric suffixes.

An update's `index.md` may set `logo: assets/what-is-traderswift/traderswift-wordmark-500.png`. The path starts at the site root with `assets/` and must resolve to an existing local PNG, JPEG or SVG supported by the image rules below. The builder renders it above the eyebrow and title and again immediately below the first “Start with chapter 01” button. Each image has intrinsic dimensions and a maximum displayed height of 112px to leave room for the title on a phone. Remove the corresponding image paragraph from the body: `logo` is omitted from published Markdown, and `llms.txt` links to that clean copy. Without `logo`, contents markup stays unchanged. `logo` belongs only on an update's contents source, not a chapter.

Chapters may set `part: Foundations` in their front matter. Repeat the same title on every chapter in that part. A title change begins a new h3 heading and ordered list in the table of contents. Titles are plain text and escaped for HTML. Chapter numbers, ordered-list starts, progress links and previous/next navigation remain continuous across parts. With no parts, the contents retain the original flat list. An omitted or empty part means an unlabelled group and ends any preceding named group. Once a named part ends, it cannot appear again within that contents page, even after an unlabelled group. A returning part stops the build with one error line and leaves `dist/` untouched. Part titles belong on chapters, not the contents source; published chapter Markdown retains them.

The optional `content/about.md` supplies a home About block after all populated content sections. Its front matter accepts exactly `title` and `description`, both nonempty, with no kind, order or chapters. The title becomes an h2; the description is metadata and is not repeated in the body. Write plain paragraphs separated by blank lines; inline links and emphasis work, while headings, images, lists, tables, quotes and fences are not allowed. The paragraphs also appear in home Markdown, reached through the existing home link in `llms.txt`. Without this file the home output is unchanged. For example:

```
---
title: About
description: A short introduction to the project.
---

The first paragraph introduces the project.

The second paragraph explains who it is for.
```

The Markdown subset supports paragraphs, headings, `*emphasis*`, `_emphasis_`, `**strong text**`, inline backticks, `[links](relative-page.html)`, flat numbered and bulleted lists, `> blockquotes`, and triple-backtick code fences with an optional language. Separate blocks with a blank line. Prose paragraphs, lists, blockquotes and figures have a 32px bottom gap, including one-sentence paragraphs on phones. Raw HTML is escaped. Nested lists, nested inline formatting, reference links, and multiline front matter are not supported.

Link to chapter `.html` pages with relative filenames. Anchor links work with the generated heading IDs. Markdown copies preserve the original source except for the contents source's `order` and `logo`, which are used only by the builder and omitted from published Markdown. The generated home and contents Markdown also link directly to chapter Markdown.

Put images in `assets/` as PNG, JPG/JPEG (baseline or progressive), or self-contained SVG. SVG needs positive numeric `width` and `height` attributes, with no scripts or external resources. PNG and JPEG dimensions come from their binary headers. Invalid or truncated image containers stop the build with a filename in the error; this is not a full JPEG pixel decoder.

Use a standalone image paragraph with descriptive alternative text. An optional double-quoted title becomes a visible, escaped caption:

```
![Describe the useful information in the image.](../assets/example.png "A caption explaining what to notice.")
```

The builder adds intrinsic dimensions, lazy loading, and asynchronous decoding. Images scale down to the reading column.

Pipe tables need a header, a separator with at least three hyphens per column, and matching cells in each row. Outer pipes are optional. Colons select left, center, or right alignment. Cells support the same flat inline formatting as paragraphs. Nested tables, multiline cells, and literal pipe characters inside cells are unsupported.

```
| Refusal reason | Example input | Next step |
| :--- | :---: | ---: |
| Missing price | `ask` is absent | Stop and check the response. |
```

Tables have column headers and a keyboard-focusable wrapper. On small screens, swipe within the table or focus it and use arrow keys to scroll horizontally. Code blocks also scroll independently of chapter swipes.

Use a prompt fence for text the reader can reuse:

```
::: prompt
Explain the response fields in plain language.
Keep the example local.
:::
```

A prompt becomes a labelled figure, visually distinct from code. Its Copy button copies the literal prompt text, including the final newline written to the adjacent `-prompt-N.txt` file. Each prompt has its own button, a keyboard focus indicator, an accessible “Copy prompt” label and a polite live region. Successful copying shows and announces “Copied” for two seconds. If clipboard access is unavailable or denied, the text is selected for manual copying, the button shows “Selected”, and the live region explains what to do. Without JavaScript, the plain-text link remains available. Prompt text is literal, not Markdown.

Copy controls use the existing same-origin `assets/reading.js`, loaded once per page; the Content-Security-Policy stays unchanged and no inline script is needed. The script reveals each button and hides its text link only after attaching the handler. Buttons use the prompt palette in both skins and themes, with AA text contrast and a minimum 44px tap target. A single timeout after each click resets that button's feedback after two seconds; there is no polling.

Use a notice fence for an announcement. Its body supports paragraphs, links and flat bullet lists:

```
::: notice
The guide has been updated. [Read the chapter](01-your-chapter.html).

Check the changes before continuing.

- Review the examples.
- Follow the updated steps.
:::
```

A notice becomes `<aside class="notice" role="note">` with a small uppercase “Announcement” label, a yellow background and a left border. It uses the prompt box's padding and 32px outer rhythm. Dedicated light and dark notice tokens keep body text, label and underlined links at WCAG AA contrast in both skins, including the control theme switch. Close the fence on its own line; an unclosed notice fails like an unclosed prompt, with one error line and no changes to `dist/`. Markdown copies keep the notice block as written; `llms.txt` continues linking to those copies.

Run `python3 build.py` after editing. The builder validates inputs and generates the complete site in a temporary folder before replacing `dist/`, copying assets and Markdown, and regenerating navigation and discovery indexes. Invalid input leaves the existing `dist/` untouched. If `content/` is missing, add `content/<guide>/index.md`; the builder exits with one error line and creates no output. Keep generated output with the sources. Set `base_url` in `site.json` to an absolute HTTP(S) site root, including any project subdirectory. `--base-url` overrides this setting. With neither supplied, the default is `https://example.com`, a placeholder for the sitemap and discovery indexes.
