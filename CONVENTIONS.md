# Writing a guide

Set `name` and `description` in the root `site.json` using nonempty JSON strings. The builder uses them for site branding and discovery metadata, and adds the first character of `name` in the accent colour to the favicon background in `assets/favicon.svg`. Rebuild after changing these settings.

`skin` accepts `light` (the default reading design, including its system dark appearance) or `control`. `tagline` is a plain-text string shown below the wordmark on the control home page; it defaults to empty. On the light home page, a nonempty tagline follows the name heading. HTML in the tagline is escaped. The control home page uses a dark palette and a compact guides heading; contents and chapters use white reading surfaces and the same dark header. All skin tokens live in `assets/style.css`. Control uses local Noto Sans regular and semibold and Noto Sans Mono light, with their licence in `assets/fonts/OFL.txt`. Mint fills retain dark text, while mint-family links on white use a darker shade for contrast. Amber is reserved for warnings.

Create `content/your-guide/`. Use lowercase words separated by hyphens for the folder name. The guide slug `assets` is reserved for site assets. Add `index.md` with the guide title, description, and a short introduction. Add chapters named `01-your-chapter.md`, `02-next-chapter.md`, and so on. Chapter basenames must match `[0-9]{2}-[a-z0-9]+(?:-[a-z0-9]+)*\.md`: two digits, a hyphen, lowercase letters or digits separated by single hyphens, then `.md`. The folder contains only the contents source and chapters; there are no nested chapter folders. Invalid chapter names stop the build with the filename in the error.

Every source begins with simple front matter. Values are plain text on one line, without quotes or YAML features:

```
---
title: Read the response
description: Understand the shape before using the values.
order: 2
---
```

Use `title` and `description` on the contents source; omit `order`. Optional `series` on the contents source labels the breadcrumb and home card; optional `level` adds a label beside the chapter count and reading time. Omit either field to hide its label. The contents breadcrumb always includes the guide title. On chapters, `order` is a unique positive integer matching the two-digit filename prefix. The builder sorts by that number. The front matter title becomes the page's only h1. Use `##` for sections and `###` for subsections. Heading IDs come from lowercase words separated by hyphens; repeated headings receive numeric suffixes.

The Markdown subset supports paragraphs, headings, `*emphasis*`, `_emphasis_`, `**strong text**`, inline backticks, `[links](relative-page.html)`, flat numbered and bulleted lists, `> blockquotes`, and triple-backtick code fences with an optional language. Separate blocks with a blank line. Raw HTML is escaped. Nested lists, nested inline formatting, reference links, and multiline front matter are not supported.

Link to chapter `.html` pages with relative filenames. Anchor links work with the generated heading IDs. Markdown copies preserve the original source. The generated home and contents Markdown also link directly to chapter Markdown.

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

A prompt becomes a labelled figure, visually distinct from code. Its link opens an adjacent plain-text file so readers can select and copy it without JavaScript. Prompt text is literal, not Markdown.

Run `python3 build.py` after editing. The builder validates inputs and generates the complete site in a temporary folder before replacing `dist/`, copying assets and Markdown, and regenerating navigation and discovery indexes. Invalid input leaves the existing `dist/` untouched. If `content/` is missing, add `content/<guide>/index.md`; the builder exits with one error line and creates no output. Keep generated output with the sources. Set `base_url` in `site.json` to an absolute HTTP(S) site root, including any project subdirectory. `--base-url` overrides this setting. With neither supplied, the default is `https://example.com`, a placeholder for the sitemap and discovery indexes.
