#!/usr/bin/env python3
"""Build a single-page HTML site from README.md for the awesome-python website."""

import json
import re
import shutil
import xml.etree.ElementTree as ET
from collections.abc import Sequence
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader
from readme_parser import ParsedGroup, ParsedSection, parse_readme, parse_sponsors, slugify

GITHUB_REPO_URL_RE = re.compile(r"^https?://github\.com/([^/]+/[^/]+?)(?:\.git)?/?$")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)\s]+)\)")
BULLET_LINE_RE = re.compile(r"^\s*-\s")
SITE_URL = "https://awesome-python.com/"
SITEMAP_URL = f"{SITE_URL}sitemap.xml"
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"

SOURCE_TYPE_DOMAINS = {
    "docs.python.org": "Built-in",
    "gitlab.com": "GitLab",
    "bitbucket.org": "Bitbucket",
}


def detect_source_type(url: str) -> str | None:
    """Detect source type from URL domain. Returns None for GitHub URLs."""
    if GITHUB_REPO_URL_RE.match(url):
        return None
    for domain, source_type in SOURCE_TYPE_DOMAINS.items():
        if domain in url:
            return source_type
    if "github.com" not in url:
        return "External"
    return None


def extract_github_repo(url: str) -> str | None:
    """Extract owner/repo from a GitHub repo URL. Returns None for non-GitHub URLs."""
    m = GITHUB_REPO_URL_RE.match(url)
    return m.group(1) if m else None


def load_stars(path: Path) -> dict[str, dict]:
    """Load star data from JSON. Returns empty dict if file doesn't exist or is corrupt."""
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def sort_entries(entries: list[dict]) -> list[dict]:
    """Sort entries by stars descending, then name ascending.

    Three tiers: starred entries first, stdlib second, other non-starred last.
    """

    def sort_key(entry: dict) -> tuple[int, int, int, str]:
        stars = entry["stars"]
        name = entry["name"].lower()
        if stars is not None:
            builtin = 1 if entry.get("source_type") == "Built-in" else 0
            return (0, -stars, builtin, name)
        if entry.get("source_type") == "Built-in":
            return (1, 0, 0, name)
        return (2, 0, 0, name)

    return sorted(entries, key=sort_key)


def build_robots_txt() -> str:
    return (
        "User-agent: *\n"
        "Content-Signal: search=yes, ai-input=yes, ai-train=yes\n"
        "Allow: /\n"
        "\n"
        f"Sitemap: {SITEMAP_URL}\n"
    )


def category_path(category: ParsedSection) -> str:
    return f"/categories/{category['slug']}/"


def category_public_url(category: ParsedSection) -> str:
    return f"{SITE_URL}categories/{category['slug']}/"


def group_public_url(group_slug: str) -> str:
    return f"{SITE_URL}categories/{group_slug}/"


def subcategory_path(category_slug: str, subcategory_slug: str) -> str:
    return f"/categories/{category_slug}/{subcategory_slug}/"


def subcategory_public_url(category_slug: str, subcategory_slug: str) -> str:
    return f"{SITE_URL}categories/{category_slug}/{subcategory_slug}/"


def write_sitemap_xml(path: Path, urls: Sequence[tuple[str, str]]) -> None:
    ET.register_namespace("", SITEMAP_NS)
    urlset = ET.Element(f"{{{SITEMAP_NS}}}urlset")
    for url, lastmod in urls:
        url_el = ET.SubElement(urlset, f"{{{SITEMAP_NS}}}url")
        loc_el = ET.SubElement(url_el, f"{{{SITEMAP_NS}}}loc")
        loc_el.text = url
        lastmod_el = ET.SubElement(url_el, f"{{{SITEMAP_NS}}}lastmod")
        lastmod_el.text = lastmod

    ET.ElementTree(urlset).write(path, encoding="utf-8", xml_declaration=True)
    with path.open("ab") as f:
        f.write(b"\n")


def top_level_heading_text(line: str) -> str | None:
    stripped = line.strip()
    if not stripped.startswith("# "):
        return None
    return stripped.removeprefix("#").strip().strip("#").strip().strip("*").strip()


LLMS_CATEGORIES_PLACEHOLDER = "{{ categories_md }}"


def extract_categories_body(markdown: str) -> str:
    """Return content under the `# Categories` heading, excluding the heading line itself."""
    lines = markdown.splitlines(keepends=True)
    start_idx = None
    end_idx = len(lines)
    for i, line in enumerate(lines):
        heading = top_level_heading_text(line)
        if heading is None:
            continue
        if start_idx is None and heading.lower() == "categories":
            start_idx = i + 1
            while start_idx < len(lines) and lines[start_idx].strip() == "":
                start_idx += 1
        elif start_idx is not None and i >= start_idx:
            end_idx = i
            break
    if start_idx is None:
        return ""
    return "".join(lines[start_idx:end_idx]).rstrip() + "\n"


def build_llms_txt(template_text: str, readme_text: str, stars_data: dict[str, dict]) -> str:
    """Render the llms.txt template by injecting the README's Categories body, then annotate stars."""
    body = extract_categories_body(readme_text).rstrip()
    rendered = template_text.replace(LLMS_CATEGORIES_PLACEHOLDER, body)
    return annotate_entries_with_stars(rendered, stars_data, format_stars=str)


def annotate_entries_with_stars(
    markdown: str,
    stars_data: dict[str, dict],
    *,
    format_stars=None,
) -> str:
    """Append the star count to bullet entry lines whose first GitHub link has known star data.

    `format_stars` controls the parenthesized text. Defaults to "{N} GitHub stars".
    Pass `str` for a bare number.
    """
    if format_stars is None:
        format_stars = lambda n: f"{n} GitHub stars"  # noqa: E731 lambda-assignment
    lines = markdown.splitlines(keepends=True)
    out: list[str] = []
    for line in lines:
        if not BULLET_LINE_RE.match(line):
            out.append(line)
            continue
        annotated = line
        for match in MARKDOWN_LINK_RE.finditer(line):
            repo_key = extract_github_repo(match.group(1))
            if not repo_key:
                continue
            entry = stars_data.get(repo_key)
            if not entry or "stars" not in entry:
                continue
            stripped = line.rstrip("\n")
            ending = line[len(stripped):]
            annotated = f"{stripped} ({format_stars(entry['stars'])}){ending}"
            break
        out.append(annotated)
    return "".join(out)


def remove_sponsors_section(markdown: str) -> str:
    lines = markdown.splitlines(keepends=True)
    start_idx = None
    for i, line in enumerate(lines):
        heading = top_level_heading_text(line)
        if heading and heading.lower() == "sponsors":
            start_idx = i
            break

    if start_idx is None:
        return markdown

    end_idx = len(lines)
    for i, line in enumerate(lines[start_idx + 1 :], start=start_idx + 1):
        if top_level_heading_text(line):
            end_idx = i
            break

    return "".join(lines[:start_idx] + lines[end_idx:])


def extract_entries(
    categories: list[ParsedSection],
    groups: list[ParsedGroup],
) -> list[dict]:
    """Flatten categories into individual library entries for table display.

    Entries appearing in multiple categories are merged into a single entry
    with lists of categories and groups.
    """
    cat_to_group = {cat["name"]: group["name"] for group in groups for cat in group["categories"]}

    seen: dict[tuple[str, str], dict[str, Any]] = {}  # (url, name) -> entry
    entries: list[dict[str, Any]] = []
    for cat in categories:
        group_name = cat_to_group.get(cat["name"], "Other")
        for entry in cat["entries"]:
            key = (entry["url"], entry["name"])
            existing: dict[str, Any] | None = seen.get(key)
            if existing is None:
                existing = {
                    "name": entry["name"],
                    "url": entry["url"],
                    "description": entry["description"],
                    "categories": [],
                    "groups": [],
                    "subcategories": [],
                    "stars": None,
                    "owner": None,
                    "last_commit_at": None,
                    "source_type": detect_source_type(entry["url"]),
                    "also_see": entry["also_see"],
                }
                seen[key] = existing
                entries.append(existing)
            if cat["name"] not in existing["categories"]:
                existing["categories"].append(cat["name"])
            if group_name not in existing["groups"]:
                existing["groups"].append(group_name)
            subcat = entry["subcategory"]
            if subcat:
                scoped = f"{cat['name']} > {subcat}"
                if not any(s["value"] == scoped for s in existing["subcategories"]):
                    sub_slug = slugify(subcat)
                    existing["subcategories"].append({
                        "name": subcat,
                        "value": scoped,
                        "slug": sub_slug,
                        "url": f"/categories/{cat['slug']}/{sub_slug}/",
                    })
    return entries


def build(repo_root: Path) -> None:
    """Main build: parse README, render single-page HTML via Jinja2 templates."""
    website = repo_root / "website"
    readme_text = (repo_root / "README.md").read_text(encoding="utf-8")

    subtitle = ""
    for line in readme_text.split("\n"):
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            subtitle = stripped
            break

    parsed_groups = parse_readme(readme_text)
    sponsors = parse_sponsors(readme_text)

    categories = [cat for g in parsed_groups for cat in g["categories"]]
    cat_slugs = [cat["slug"] for cat in categories]
    group_slugs = [g["slug"] for g in parsed_groups]
    all_top_level_slugs = cat_slugs + group_slugs
    duplicates = {s for s in all_top_level_slugs if all_top_level_slugs.count(s) > 1}
    if duplicates:
        raise ValueError(
            f"slug collision in /categories/ namespace: {sorted(duplicates)}. "
            "Rename a category or group so their slugs differ."
        )
    total_entries = sum(c["entry_count"] for c in categories)
    entries = extract_entries(categories, parsed_groups)
    build_date = datetime.now(UTC)

    stars_data = load_stars(website / "data" / "github_stars.json")

    repo_self = stars_data.get("vinta/awesome-python", {})
    repo_stars = None
    if "stars" in repo_self:
        stars_val = repo_self["stars"]
        repo_stars = f"{stars_val // 1000}k" if stars_val >= 1000 else str(stars_val)

    for entry in entries:
        repo_key = extract_github_repo(entry["url"])
        if not repo_key and entry.get("source_type") == "Built-in":
            repo_key = "python/cpython"
        if repo_key and repo_key in stars_data:
            sd = stars_data[repo_key]
            entry["stars"] = sd["stars"]
            entry["owner"] = sd["owner"]
            entry["last_commit_at"] = sd.get("last_commit_at", "")

    entries = sort_entries(entries)
    category_urls = {cat["name"]: category_path(cat) for cat in categories}

    env = Environment(
        loader=FileSystemLoader(website / "templates"),
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )

    site_dir = website / "output"
    if site_dir.exists():
        shutil.rmtree(site_dir)
    site_dir.mkdir(parents=True)

    tpl_index = env.get_template("index.html")
    (site_dir / "index.html").write_text(
        tpl_index.render(
            categories=categories,
            subtitle=subtitle,
            entries=entries,
            total_entries=total_entries,
            total_categories=len(categories),
            repo_stars=repo_stars,
            build_date=build_date.strftime("%B %d, %Y"),
            sponsors=sponsors,
            category_urls=category_urls,
        ),
        encoding="utf-8",
    )

    tpl_category = env.get_template("category.html")
    categories_dir = site_dir / "categories"
    for category in categories:
        category_entries = [entry for entry in entries if category["name"] in entry["categories"]]
        page_dir = categories_dir / category["slug"]
        page_dir.mkdir(parents=True, exist_ok=True)
        (page_dir / "index.html").write_text(
            tpl_category.render(
                category=category,
                category_url=category_public_url(category),
                entries=category_entries,
                total_categories=len(categories),
                page_kind="category",
            ),
            encoding="utf-8",
        )

    for group in parsed_groups:
        group_entries = [entry for entry in entries if group["name"] in entry["groups"]]
        page_dir = categories_dir / group["slug"]
        page_dir.mkdir(parents=True, exist_ok=True)
        synthetic = {
            "name": group["name"],
            "slug": group["slug"],
            "description": "",
            "description_html": "",
        }
        (page_dir / "index.html").write_text(
            tpl_category.render(
                category=synthetic,
                category_url=group_public_url(group["slug"]),
                entries=group_entries,
                total_categories=len(categories),
                page_kind="group",
            ),
            encoding="utf-8",
        )

    seen_subcats: set[tuple[str, str]] = set()
    for category in categories:
        cat_url_prefix = f"/categories/{category['slug']}/"
        for entry in entries:
            for sub in entry.get("subcategories", []):
                if not sub["url"].startswith(cat_url_prefix):
                    continue
                key = (category["slug"], sub["slug"])
                if key in seen_subcats:
                    continue
                seen_subcats.add(key)
                sub_entries = [
                    e for e in entries
                    if any(s["value"] == sub["value"] for s in e.get("subcategories", []))
                ]
                page_dir = categories_dir / category["slug"] / sub["slug"]
                page_dir.mkdir(parents=True, exist_ok=True)
                synthetic = {
                    "name": sub["name"],
                    "slug": sub["slug"],
                    "description": "",
                    "description_html": "",
                }
                (page_dir / "index.html").write_text(
                    tpl_category.render(
                        category=synthetic,
                        category_url=subcategory_public_url(category["slug"], sub["slug"]),
                        entries=sub_entries,
                        total_categories=len(categories),
                        page_kind="subcategory",
                        parent_category=category,
                    ),
                    encoding="utf-8",
                )

    static_src = website / "static"
    static_dst = site_dir / "static"
    if static_src.exists():
        shutil.copytree(static_src, static_dst, dirs_exist_ok=True)

    markdown_index = annotate_entries_with_stars(
        remove_sponsors_section(readme_text), stars_data
    )
    llms_template = (website / "templates" / "llms.txt").read_text(encoding="utf-8")
    llms_txt = build_llms_txt(llms_template, readme_text, stars_data)
    (site_dir / "robots.txt").write_text(build_robots_txt(), encoding="utf-8")
    sitemap_date = build_date.date().isoformat()
    sitemap_urls = [(SITE_URL, sitemap_date)] + [
        (category_public_url(category), sitemap_date) for category in categories
    ]
    write_sitemap_xml(site_dir / "sitemap.xml", sitemap_urls)
    (site_dir / "index.md").write_text(markdown_index, encoding="utf-8")
    (site_dir / "llms.txt").write_text(llms_txt, encoding="utf-8")

    print(f"Built site with {len(parsed_groups)} groups, {len(categories)} categories")
    print(f"Total entries: {total_entries}")
    print(f"Output: {site_dir}")


if __name__ == "__main__":
    build(Path(__file__).parent.parent)
