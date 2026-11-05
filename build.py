#!/usr/bin/env python3
"""Build a static HTML site from Markdown docs.

Reads every Markdown file in docs/, converts it to a complete
standalone HTML page with shared navigation and styling, and writes
the result to site/. No network access, no dependencies beyond the
Python standard library plus the `markdown` package.
"""

import re
import shutil
import textwrap
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"
ASSETS = ROOT / "assets"

# Pages in reading order. Each entry: (md filename, nav label)
PAGES = [
    ("index.md", "Start here"),
    ("01-what-you-need.md", "1. What you need"),
    ("02-run-ollama-on-the-main-computer.md", "2. Install Ollama"),
    ("03-open-it-to-your-network.md", "3. Open to family"),
    ("04-firewall-basics.md", "4. Firewall"),
    ("05-phone-access.md", "5. Phones"),
    ("06-when-this-is-a-bad-idea.md", "6. When not to"),
    ("setup-day-checklist.md", "Setup day"),
    ("troubleshooting.md", "Troubleshooting"),
    ("glossary.md", "Glossary"),
]

TITLE = "Share Your Local AI"
SUBTITLE = "One household, one main computer, every device. No cloud."
COPYRIGHT = "Copyright (c) 2026 Asdale Dynamics, LLC"
HUB_URL = "https://dylanasdale.github.io"

MD_KEYWORDS = re.compile(r"\[(.*?)\]\((?!http)([^)#]+)(#[^)]*)?\)")


def md_to_html(path: Path) -> str:
    text = path.read_text(encoding="utf-8")

    def rewrite(match: re.Match) -> str:
        label, target, anchor = match.group(1), match.group(2), match.group(3) or ""
        if target.endswith(".md"):
            return f"[{label}]({Path(target).stem}.html{anchor})"
        return match.group(0)

    text = MD_KEYWORDS.sub(rewrite, text)
    return markdown.markdown(text, extensions=["tables", "fenced_code", "toc"])


def page_template(body: str, title: str, active: str) -> str:
    nav_items = "".join(
        f'<a class="{"active" if fname == active else ""}" href="{Path(fname).stem}.html">{label}</a>\n'
        for fname, label in PAGES
    )
    return textwrap.dedent(f"""\
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="{SUBTITLE} A beginner manual by Asdale Dynamics, LLC.">
        <title>{title} — {TITLE}</title>
        <link rel="stylesheet" href="style.css">
        </head>
        <body>
        <header class="site-header">
          <a class="brand" href="index.html">{TITLE}</a>
          <span class="tagline">{SUBTITLE}</span>
        </header>
        <nav class="site-nav">
        {nav_items}</nav>
        <main>
        {body}
        </main>
        <footer class="site-footer">
          <p>{COPYRIGHT} · {TITLE} is free documentation under the MIT license · <a href="{HUB_URL}">{HUB_URL}</a></p>
          <p>Educational guide only — not medical, legal, or security advice.</p>
        </footer>
        </body>
        </html>
        """)


def extract_h1(html: str, fallback: str) -> str:
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
    if not m:
        return fallback
    return re.sub(r"<.*?>", "", m.group(1)).strip()


def build() -> None:
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir()

    if (ASSETS / "style.css").is_file():
        shutil.copy(ASSETS / "style.css", SITE / "style.css")

    built = []
    for fname, _label in PAGES:
        src = DOCS / fname
        if not src.is_file():
            raise SystemExit(f"Missing doc file: {src}")
        html = md_to_html(src)
        out_name = src.stem + ".html"
        title = extract_h1(html, fname)
        page = page_template(html, title, fname)
        (SITE / out_name).write_text(page, encoding="utf-8")
        built.append(out_name)

    print(f"Built {len(built)} pages into site/:")
    for name in built:
        print(f"  site/{name}")


if __name__ == "__main__":
    build()
