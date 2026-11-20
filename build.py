import argparse
import html
import json
import re
import shutil
import sys
from itertools import groupby
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.parse import urlsplit

from image_metadata import image_dimensions

site_directory = Path(__file__).resolve().parent
output_directory = site_directory / 'dist'
site_configuration = json.loads((site_directory / 'site.json').read_text(encoding='utf-8'))
if any(not isinstance(site_configuration.get(field), str) or not site_configuration[field].strip() for field in ('name', 'description')):
    raise ValueError('site.json requires nonempty name and description strings')
site_name = site_configuration['name']
site_description = site_configuration['description']
site_skin = site_configuration.get('skin', 'light')
site_tagline = site_configuration.get('tagline', '')
if site_skin not in ('light', 'control'):
    raise ValueError('site.json skin must be light or control')
if not isinstance(site_tagline, str):
    raise ValueError('site.json tagline must be a string')
link_pattern = r'!?\[([^\]]*)\]\(([^\s)]+)(?: "([^"\n]*)")?\)'
token_pattern = re.compile(r'(`[^`]+`|!?\[[^\]]*\]\([^\s)]+(?: "[^"\n]*")?\)|\*\*[^*]+\*\*|\*[^*]+\*|_[^_]+_)')
content_kinds = {
    'update': ('Updates', 'updates', 'update', 'Read the update'),
    'guide': ('Guides', 'guides', 'guide', 'Explore the guide'),
    'case-study': ('Case studies', 'case-studies', 'case study', 'Read the case study'),
}

def escape(value):
    return html.escape(str(value), quote=True)

def safe_link(address):
    if urlsplit(address).scheme not in ('', 'https', 'http', 'mailto') or address.startswith('//'):
        raise ValueError('Unsupported link: ' + address)
    return escape(address)

def inline_markdown(text):
    fragments = []
    for token in token_pattern.split(text):
        if token.startswith('`') and token.endswith('`'):
            fragments.append('<code>' + escape(token[1:-1]) + '</code>')
        elif link := re.fullmatch(link_pattern, token):
            label, address, caption = link.groups()
            if token.startswith('!'):
                asset_path = (site_directory / 'content' / address).resolve()
                if not asset_path.is_relative_to(site_directory / 'assets'):
                    raise ValueError('Images must be local assets: ' + address)
                width, height = image_dimensions(asset_path)
                fragments.append(f'<img src="{safe_link(address)}" alt="{escape(label)}" width="{width}" height="{height}" loading="lazy" decoding="async">')
            else:
                fragments.append(f'<a href="{safe_link(address)}">{escape(label)}</a>')
        elif token.startswith('**') and token.endswith('**'):
            fragments.append('<strong>' + escape(token[2:-2]) + '</strong>')
        elif len(token) > 2 and token[0] in '*_' and token[-1] == token[0]:
            fragments.append('<em>' + escape(token[1:-1]) + '</em>')
        else:
            fragments.append(escape(token))
    return ''.join(fragments)

def table_cells(line):
    return [cell.strip() for cell in line.strip().removeprefix('|').removesuffix('|').split('|')]
def table_start(lines, position):
    return position + 1 < len(lines) and '|' in lines[position] and all(re.fullmatch(r':?-{3,}:?', cell) for cell in table_cells(lines[position + 1]))
def render_table(lines, position):
    headers = table_cells(lines[position])
    separators = table_cells(lines[position + 1])
    if len(headers) != len(separators):
        raise ValueError('Table header and separator widths differ')
    alignments = ['center' if cell.startswith(':') and cell.endswith(':') else 'right' if cell.endswith(':') else 'left' for cell in separators]
    def row(cells, tag):
        if len(cells) != len(headers):
            raise ValueError('Table row width differs from header')
        return '<tr>' + ''.join(f'<{tag} class="align-{alignment}"' + (' scope="col"' if tag == 'th' else '') + f'>{inline_markdown(cell)}</{tag}>' for cell, alignment in zip(cells, alignments)) + '</tr>'
    heading = row(headers, 'th')
    rows = []
    position += 2
    while position < len(lines) and lines[position].strip() and '|' in lines[position]:
        rows.append(row(table_cells(lines[position]), 'td'))
        position += 1
    return '<div class="table-scroll" tabindex="0" role="region" aria-label="Scrollable table"><table><thead>' + heading + '</thead><tbody>' + ''.join(rows) + '</tbody></table></div>', position
def read_source(source_path):
    source = source_path.read_text(encoding='utf-8')
    lines = source.splitlines()
    if not lines or lines[0] != '---' or '---' not in lines[1:]:
        raise ValueError('Missing front matter: ' + source_path.name)
    closing_line = lines.index('---', 1)
    metadata = {}
    for line in lines[1:closing_line]:
        name, separator, value = line.partition(':')
        if not separator or name not in ('title', 'description', 'order', 'series', 'level', 'kind', 'logo', 'part') or name in metadata or (name == 'logo' and source_path.name != 'index.md') or (name == 'part' and source_path.name == 'index.md'):
            raise ValueError('Invalid front matter: ' + source_path.name)
        metadata[name] = value.strip()
    if not metadata.get('title') or not metadata.get('description'):
        raise ValueError('Title and description required: ' + source_path.name)
    return metadata, '\n'.join(lines[closing_line + 1:]).strip('\n'), source

def render_markdown(source, destination):
    lines = source.splitlines()
    fragments = []
    heading_identifiers = set()
    position = 0
    prompt_count = 0
    while position < len(lines):
        line = lines[position]
        if not line.strip():
            position += 1
            continue
        if line.startswith('```') or line.strip() in ('::: prompt', '::: notice'):
            prompt = line.strip() == '::: prompt'
            notice = line.strip() == '::: notice'
            language = '' if prompt or notice else line[3:].strip()
            if language and not re.fullmatch(r'[a-zA-Z0-9_+-]+', language):
                raise ValueError('Invalid code language')
            closing_fence = ':::' if prompt or notice else '```'
            collected = []
            position += 1
            while position < len(lines) and lines[position].strip() != closing_fence:
                collected.append(lines[position])
                position += 1
            if position == len(lines):
                raise ValueError('Unclosed Markdown fence')
            text = '\n'.join(collected)
            if notice:
                fragments.append('<aside class="notice" role="note"><div class="notice-label">Announcement</div>' + render_markdown(text, destination) + '</aside>')
            elif prompt:
                prompt_count += 1
                prompt_path = destination.with_name(f'{destination.stem}-prompt-{prompt_count}.txt')
                prompt_path.write_text(text + '\n', encoding='utf-8')
                fragments.append(f'<figure class="prompt"><figcaption><span>Try this prompt</span><button class="prompt-copy" type="button" aria-label="Copy prompt" hidden>Copy</button><a href="{escape(prompt_path.name)}" aria-label="Open plain prompt text to copy">Open text to copy ↗</a><span class="prompt-status" role="status" aria-live="polite" aria-atomic="true"></span></figcaption><blockquote><p>{escape(text)}</p></blockquote></figure>')
            else:
                fragments.append(f'<figure class="code-block"><figcaption>{escape(language or "Code")}</figcaption><pre tabindex="0"><code class="language-{escape(language or "text")}">{escape(text)}</code></pre></figure>')
        elif table_start(lines, position):
            rendered_table, position = render_table(lines, position)
            fragments.append(rendered_table)
            continue
        elif heading_match := re.fullmatch(r'(#{1,6})\s+(.+)', line):
            level = max(2, len(heading_match[1]))
            heading_slug = re.sub(r'[^a-z0-9]+', '-', heading_match[2].lower()).strip('-') or 'section'
            identifier = heading_slug
            suffix = 2
            while identifier in heading_identifiers:
                identifier = f'{heading_slug}-{suffix}'
                suffix += 1
            heading_identifiers.add(identifier)
            fragments.append(f'<h{level} id="{identifier}">{inline_markdown(heading_match[2])}</h{level}>')
        elif re.match(r'^(?:[-*]|\d+\.)\s+', line):
            ordered = bool(re.match(r'^\d+\.', line))
            list_tag = 'ol' if ordered else 'ul'
            pattern = r'^\d+\.\s+(.*)' if ordered else r'^[-*]\s+(.*)'
            items = []
            while position < len(lines) and (item := re.match(pattern, lines[position])):
                items.append('<li>' + inline_markdown(item[1]) + '</li>')
                position += 1
            fragments.append(f'<{list_tag}>' + ''.join(items) + f'</{list_tag}>')
            continue
        elif line.startswith('> '):
            collected = []
            while position < len(lines) and lines[position].startswith('> '):
                collected.append(lines[position][2:])
                position += 1
            fragments.append('<blockquote><p>' + inline_markdown(' '.join(collected)) + '</p></blockquote>')
            continue
        elif line.startswith('!['):
            image_match = re.fullmatch(link_pattern, line)
            if not image_match:
                raise ValueError('Invalid standalone image: ' + line)
            caption = '<figcaption>' + escape(image_match[3]) + '</figcaption>' if image_match[3] else ''
            fragments.append('<figure class="illustration">' + inline_markdown(line) + caption + '</figure>')
        else:
            collected = [line]
            position += 1
            while position < len(lines) and lines[position].strip() and not table_start(lines, position) and not re.match(r'^(#{1,6}\s|```|:::|> |!\[|[-*]\s|\d+\.\s)', lines[position]):
                collected.append(lines[position])
                position += 1
            fragments.append('<p>' + inline_markdown(' '.join(collected)) + '</p>')
            continue
        position += 1
    return '\n'.join(fragments)
def page_shell(title, description, body, section_kinds, depth=0):
    prefix = '../' * depth
    section_links = ''.join(f'<a href="{prefix}index.html#{content_kinds[kind][1]}">{content_kinds[kind][0]}</a>' for kind in section_kinds)
    theme_switch = '''<button class="theme-switch" type="button" aria-label="Switch to dark mode" hidden><svg viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><g class="theme-sun"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M5 5l1.5 1.5m11 11L19 19M5 19l1.5-1.5m11-11L19 5"/></g><path class="theme-moon" d="M20 15.5A9 9 0 0 1 8.5 4 9 9 0 1 0 20 15.5Z"/></svg></button>''' if site_skin == 'control' else ''
    return f'''<!doctype html>
<html lang="en" data-skin="{site_skin}" data-page="{"home" if depth == 0 else "reading"}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{escape(description)}">
<meta name="color-scheme" content="light dark">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'self'; script-src 'self'; img-src 'self'; font-src 'self'; base-uri 'none'; form-action 'none'">
<title>{escape(title)} · {escape(site_name)}</title>
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{prefix}assets/style.css">
<script src="{prefix}assets/reading.js" blocking="render"></script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header"><a class="wordmark" href="{prefix}index.html" aria-label="{escape(site_name)} home">{escape(site_name)}</a><nav aria-label="Site">{section_links}<a class="source-link" href="{prefix}llms.txt">For agents ↗</a>{theme_switch}</nav></header>
<main id="main">{body}</main>
<footer class="site-footer"><span>{escape(site_name)}</span><nav aria-label="Resources"><a href="{prefix}index.json">Index</a><a href="{prefix}llms.txt">Plain text</a><a href="{prefix}sitemap.xml">Sitemap</a></nav></footer>
</body>
</html>
'''

def write_page(output_directory, relative_path, title, description, body, markdown, section_kinds, depth=0):
    destination = output_directory / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(page_shell(title, description, body, section_kinds, depth), encoding='utf-8')
    destination.with_suffix('.md').write_text(markdown, encoding='utf-8')
    return {'title': title, 'description': description, 'url': relative_path, 'markdown': str(Path(relative_path).with_suffix('.md'))}

def build(base_url):
    if not isinstance(base_url, str) or urlsplit(base_url).scheme not in ('https', 'http') or not urlsplit(base_url).netloc or urlsplit(base_url).query or urlsplit(base_url).fragment:
        raise ValueError('Base URL must be an absolute HTTP(S) site root')
    base_url = base_url.rstrip('/')
    if not (site_directory / 'content').is_dir():
        raise ValueError('Missing content directory: add content/<guide>/index.md')
    with TemporaryDirectory(prefix='.build-', dir=site_directory) as temporary_directory:
        staged_output = Path(temporary_directory) / 'dist'
        page_count = render_site(base_url, staged_output)
        if output_directory.exists():
            shutil.rmtree(output_directory)
        shutil.move(staged_output, output_directory)
    print(f'Built {page_count} pages in dist/')

def read_guides():
    guides = []
    guide_orders = set()
    for tutorial_directory in sorted((site_directory / 'content').iterdir()):
        if not tutorial_directory.is_dir():
            continue
        tutorial_slug = tutorial_directory.name
        if tutorial_slug == 'assets':
            raise ValueError('Guide slug assets is reserved for site assets')
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', tutorial_slug):
            raise ValueError('Tutorial folder names must be lowercase slugs: ' + tutorial_slug)
        tutorial_metadata, tutorial_body, tutorial_source = read_source(tutorial_directory / 'index.md')
        kind = tutorial_metadata.get('kind')
        if kind not in content_kinds:
            raise ValueError('Kind must be update, guide or case-study: ' + tutorial_slug)
        guide_order = tutorial_metadata.get('order', '')
        if not re.fullmatch(r'[0-9]+', guide_order) or int(guide_order) < 1:
            raise ValueError('Content order must be a positive integer: ' + tutorial_slug)
        guide_number = int(guide_order)
        if (kind, guide_number) in guide_orders:
            raise ValueError(f'Duplicate {kind} order {guide_number}: {tutorial_slug}')
        guide_orders.add((kind, guide_number))
        tutorial_front_matter, separator, tutorial_body_source = tutorial_source.partition('\n---\n')
        tutorial_source = re.sub(r'^(?:order|logo):[^\r\n]*(?:\r?\n|$)', '', tutorial_front_matter, flags=re.MULTILINE).rstrip('\n') + separator + tutorial_body_source
        guides.append((guide_number, tutorial_directory, tutorial_metadata, tutorial_body, tutorial_source))
    return sorted(guides, key=lambda guide: (tuple(content_kinds).index(guide[2]['kind']), guide[0]))

def contents_logo(metadata):
    if 'logo' not in metadata:
        return ''
    address = metadata['logo']
    asset_path = (site_directory / address).resolve()
    if metadata['kind'] != 'update' or not address.startswith('assets/') or not asset_path.is_relative_to(site_directory / 'assets'):
        raise ValueError('Logo must be a local assets/ image on an update index')
    width, height = image_dimensions(asset_path)
    return f'<img class="contents-logo" src="../{safe_link(address)}" alt="{escape(site_name)}" width="{width}" height="{height}" decoding="async">'

def contents_list(chapters, rows):
    fragments, seen_parts = [], set()
    chapter_number = 1
    for part, group in groupby(zip(chapters, rows), key=lambda item: item[0][2].get('part', '')):
        if part and part in seen_parts:
            raise ValueError('Returning chapter part: ' + part)
        if part:
            seen_parts.add(part)
            fragments.append(f'<h3 class="part-heading">{escape(part)}</h3>')
        start = f' start="{chapter_number}"' if chapter_number > 1 else ''
        grouped_rows = [row for chapter, row in group]
        fragments.append(f'<ol class="chapter-list"{start}>' + ''.join(grouped_rows) + '</ol>')
        chapter_number += len(grouped_rows)
    return ''.join(fragments)

def home_about():
    about_path = site_directory / 'content' / 'about.md'
    if not about_path.exists():
        return '', ''
    metadata, body, source = read_source(about_path)
    if set(metadata) != {'title', 'description'} or '![' in body or any(re.match(r'^(?:#{1,6}\s|```|:::|> |!\[|[-*]\s|\d+\.\s)', line.strip()) or table_start(body.splitlines(), index) for index, line in enumerate(body.splitlines())):
        raise ValueError('About requires title and description only, and plain paragraphs')
    paragraphs = '\n'.join('<p>' + inline_markdown(' '.join(paragraph.splitlines())) + '</p>' for paragraph in re.split(r'\n\s*\n', body) if paragraph.strip())
    return f'<section id="about" aria-labelledby="about-heading"><div class="section-heading"><h2 id="about-heading">{escape(metadata["title"])}</h2></div><div class="about-copy prose">{paragraphs}</div></section>', f'\n## {metadata["title"]}\n\n{body}\n'

def render_site(base_url, output_directory):
    guides = read_guides()
    section_kinds = tuple(kind for kind in content_kinds if any(guide[2]['kind'] == kind for guide in guides))
    output_directory.mkdir()
    shutil.copytree(site_directory / 'assets', output_directory / 'assets')
    favicon_path = output_directory / 'assets' / 'favicon.svg'
    favicon_initial = f'<text x="20" y="29" text-anchor="middle" fill="#345c46" font-family="Georgia,serif" font-size="30">{escape(site_name[0])}</text>'
    favicon_path.write_text(favicon_path.read_text(encoding='utf-8').replace('</svg>', favicon_initial + '</svg>'), encoding='utf-8')
    indexed_pages = []
    tutorial_cards = {kind: [] for kind in content_kinds}
    grouped_markdown = {kind: [] for kind in content_kinds}
    grouped_pages = {kind: [] for kind in content_kinds}
    for guide_number, tutorial_directory, tutorial_metadata, tutorial_body, tutorial_source in guides:
        tutorial_slug = tutorial_directory.name
        kind = tutorial_metadata['kind']
        kind_label = content_kinds[kind][2]
        first_page = len(indexed_pages)
        series = tutorial_metadata.get('series', '')
        series_breadcrumb = f'<span>{escape(series)}</span><span aria-hidden="true">/</span>' if series else ''
        contents_eyebrow = f'<p class="eyebrow">{kind_label.capitalize()} {guide_number:02}</p>' if kind != 'guide' else ''
        card_eyebrow = contents_eyebrow
        if series:
            card_eyebrow += f'<p class="eyebrow">{escape(series)}</p>'
        card_link = content_kinds[kind][3]
        level = tutorial_metadata.get('level', '')
        level_label = f'<span>{escape(level)}</span>' if level else ''
        chapters = []
        for chapter_path in sorted(tutorial_directory.iterdir()):
            if chapter_path.name == 'index.md':
                continue
            if not chapter_path.is_file() or not re.fullmatch(r'[0-9]{2}-[a-z0-9]+(?:-[a-z0-9]+)*\.md', chapter_path.name):
                raise ValueError('Invalid chapter filename: ' + chapter_path.name + '; expected 01-lowercase-slug.md')
            metadata, body, source = read_source(chapter_path)
            order = int(metadata.get('order', '0'))
            if order < 1 or order != int(chapter_path.name[:2]):
                raise ValueError('Chapter order must match its positive filename prefix')
            chapters.append((order, chapter_path, metadata, body, source))
        chapters.sort(key=lambda chapter: chapter[0])
        if not chapters or len({chapter[0] for chapter in chapters}) != len(chapters):
            raise ValueError('A tutorial needs chapters with unique orders')
        total_minutes = sum(max(1, len(chapter[3].split()) // 180 + 1) for chapter in chapters)
        chapter_rows = []
        (output_directory / tutorial_slug).mkdir()
        for chapter_index, (order, source_path, metadata, markdown_body, source) in enumerate(chapters):
            filename = source_path.with_suffix('.html').name
            minutes = max(1, len(markdown_body.split()) // 180 + 1)
            chapter_rows.append(f'<li><a href="{escape(filename)}"><span class="chapter-number">{chapter_index + 1:02}</span><span><strong>{escape(metadata["title"])}</strong><span class="chapter-description">{escape(metadata["description"])}</span></span><span class="row-end">{minutes} min <span aria-hidden="true">↗</span></span></a></li>')
            previous_href = chapters[chapter_index - 1][1].with_suffix('.html').name if chapter_index else 'index.html'
            previous_title = chapters[chapter_index - 1][2]['title'] if chapter_index else 'Table of contents'
            navigation = f'<a rel="prev" href="{escape(previous_href)}"><span>← {"Previous chapter" if chapter_index else "Back to contents"}</span><strong>{escape(previous_title)}</strong></a>'
            if chapter_index + 1 < len(chapters):
                next_chapter = chapters[chapter_index + 1]
                navigation += f'<a rel="next" href="{escape(next_chapter[1].with_suffix(".html").name)}"><span>Next chapter →</span><strong>{escape(next_chapter[2]["title"])}</strong></a>'
            else:
                navigation += f'<a href="index.html"><span>{kind_label.capitalize()} complete ✓</span><strong>Return to the contents</strong></a>'
            progress_links = ''.join(f'<a href="{escape(chapter[1].with_suffix(".html").name)}" aria-label="Chapter {index + 1}: {escape(chapter[2]["title"])}"' + (' aria-current="page"' if index == chapter_index else '') + f'>{index + 1:02}</a>' for index, chapter in enumerate(chapters))
            rendered_body = render_markdown(markdown_body, output_directory / tutorial_slug / filename)
            body = f'''<div class="reading-layout"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="../index.html">Home</a><span aria-hidden="true">/</span><a href="index.html">{escape(tutorial_metadata['title'])}</a></nav>
<div class="reading-topline"><p class="eyebrow">Chapter {chapter_index + 1:02} <span>/ {len(chapters):02}</span></p><nav class="chapter-progress" aria-label="Chapters">{progress_links}</nav></div>
<article><header class="article-header"><h1>{escape(metadata['title'])}</h1><p class="standfirst">{escape(metadata['description'])}</p><div class="article-meta"><span>{escape(site_name)} {kind_label}</span><span>{minutes} min read</span><a href="{escape(source_path.name)}">Read Markdown ↗</a></div></header><div class="prose">{rendered_body}</div></article>
<nav class="chapter-navigation" aria-label="Chapter navigation">{navigation}</nav><p class="reading-hint">One chapter at a time. Use the links to keep reading, or swipe on touch screens.</p></div>'''
            indexed_pages.append(write_page(output_directory, f'{tutorial_slug}/{filename}', metadata['title'], metadata['description'], body, source, section_kinds, 1))
        contents_markdown = tutorial_source + '\n\n## Chapters\n\n' + '\n'.join(f'{index + 1}. [{chapter[2]["title"]}]({chapter[1].name})' for index, chapter in enumerate(chapters)) + '\n'
        logo = contents_logo(tutorial_metadata)
        grouped_contents = contents_list(chapters, chapter_rows)
        contents_intro = render_markdown(tutorial_body, output_directory / tutorial_slug / 'index.html')
        chapter_count = f'<span class="chapter-count">{len(chapters)}</span>' if site_skin == 'control' else str(len(chapters))
        contents_body = f'''<div class="contents-layout"><nav class="breadcrumb" aria-label="Breadcrumb"><a href="../index.html">Home</a><span aria-hidden="true">/</span>{series_breadcrumb}<span>{escape(tutorial_metadata['title'])}</span></nav>{logo}{contents_eyebrow}<h1>{escape(tutorial_metadata['title'])}</h1><p class="standfirst">{escape(tutorial_metadata['description'])}</p><div class="guide-meta"><span>{chapter_count} chapters</span><span>{total_minutes} min read</span>{level_label}</div><a class="button" rel="next" href="{escape(chapters[0][1].with_suffix('.html').name)}">Start with chapter 01 <span aria-hidden="true">→</span></a><div class="contents-intro prose">{contents_intro}</div><div class="section-heading"><h2>Table of contents</h2><a href="index.md">Markdown ↗</a></div>{grouped_contents}<a class="text-link" href="{escape(chapters[0][1].with_suffix('.html').name)}">Start with chapter 01 <span aria-hidden="true">→</span></a></div>'''
        indexed_pages.append(write_page(output_directory, f'{tutorial_slug}/index.html', tutorial_metadata['title'], tutorial_metadata['description'], contents_body, contents_markdown, section_kinds, 1))
        tutorial_cards[kind].append(f'<article class="guide-card"><div class="card-copy">{card_eyebrow}<h3><a href="{escape(tutorial_slug)}/index.html">{escape(tutorial_metadata["title"])}</a></h3><p>{escape(tutorial_metadata["description"])}</p><div class="card-bottom"><span>{chapter_count} chapters <span aria-hidden="true">·</span> {total_minutes} min read</span><a href="{escape(tutorial_slug)}/index.html">{card_link} <span aria-hidden="true">↗</span></a></div></div></article>')
        grouped_markdown[kind].append(f'- [{tutorial_metadata["title"]}]({tutorial_slug}/index.md): {tutorial_metadata["description"]}')
        grouped_pages[kind].extend(indexed_pages[first_page:])
    home_heading = f'<h1>{escape(site_name)}</h1>'
    tagline = f'<p class="tagline">{escape(site_tagline)}</p>' if site_tagline else ''
    sections = []
    home_markdown = f'# {site_name}\n'
    for kind, (title, section_id, kind_label, card_link) in content_kinds.items():
        cards = tutorial_cards[kind]
        if not cards:
            continue
        count_label = kind_label if len(cards) == 1 else title.lower()
        sections.append(f'<section id="{section_id}" aria-labelledby="{section_id}-heading"><div class="section-heading"><h2 id="{section_id}-heading">{title}</h2><span>{len(cards)} {count_label}</span></div>{"".join(cards)}</section>')
        home_markdown += f'\n## {title}\n\n' + '\n'.join(grouped_markdown[kind]) + '\n'
    about_html, about_markdown = home_about()
    home_markdown += about_markdown
    home_body = f'<div class="home-layout"><section class="home-hero">{home_heading}{tagline}</section>{"".join(sections)}{about_html}</div>'
    indexed_pages.insert(0, write_page(output_directory, 'index.html', 'Blog', site_description, home_body, home_markdown, section_kinds))
    (output_directory / 'index.json').write_text(json.dumps({'name': site_name, 'description': site_description, 'base_url': base_url.rstrip('/'), 'pages': indexed_pages}, indent=2) + '\n', encoding='utf-8')
    plain_index = f'# {site_name}\n\n{site_description}\n\nSite: {base_url}\n\nStatic HTML and Markdown.\n\n[Home](index.html) | Markdown: index.md\n'
    for kind, (title, section_id, kind_label, card_link) in content_kinds.items():
        if grouped_pages[kind]:
            plain_index += f'\n## {title}\n\n' + '\n'.join(f'- [{page["title"]}]({page["url"]}) | Markdown: {page["markdown"]} | {page["description"]}' for page in grouped_pages[kind]) + '\n'
    (output_directory / 'llms.txt').write_text(plain_index.rstrip() + '\n', encoding='utf-8')
    locations = ''.join(f'<url><loc>{escape(base_url.rstrip("/") + "/" + page["url"])}</loc></url>' for page in indexed_pages)
    (output_directory / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + locations + '</urlset>\n', encoding='utf-8')
    return len(indexed_pages)

if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser(description=f'Build {site_name} from local Markdown.')
    argument_parser.add_argument('--base-url', default=site_configuration.get('base_url', 'https://example.com'), help='Public site root, including any project subdirectory; defaults to site.json base_url or https://example.com.')
    arguments = argument_parser.parse_args()
    try:
        build(arguments.base_url)
    except (ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
