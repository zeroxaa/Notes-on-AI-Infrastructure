#!/usr/bin/env python3
"""Check coverage, navigation, local links, and translation source freshness."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import quote, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "translations.json"
START = "<!-- bilingual-navigation:start -->"
END = "<!-- bilingual-navigation:end -->"
NAV = re.compile(r"\A" + re.escape(START) + r".*?" + re.escape(END) + r"\n\n", re.S)
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")
FIGURE = re.compile(r"<!-- translated-figure: (.+?) -->")


def body(text):
    return NAV.sub("", text, count=1)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def relative_link(current, target):
    return quote(os.path.relpath(ROOT / target, (ROOT / current).parent), safe="/-._~")


def navigation(pages, index, language):
    page = pages[index]
    current = page[language]
    toc = "README.md" if language == "source" else "en/README.md"
    links = [
        f"[中文原文]({relative_link(current, page['source'])})",
        f"[English]({relative_link(current, page['translation'])})",
        f"[{'目录' if language == 'source' else 'Contents'}]({relative_link(current, toc)})",
    ]
    if index:
        links.append(f"[{'上一页' if language == 'source' else 'Previous'}]({relative_link(current, pages[index - 1][language])})")
    if index + 1 < len(pages):
        links.append(f"[{'下一页' if language == 'source' else 'Next'}]({relative_link(current, pages[index + 1][language])})")
    note = ("本版仅为中文正文添加双语导航；英文译本及维护说明见 "
            if language == "source" else
            "English translation of Wang Honglei's Chinese original. Edition and maintenance notes: ")
    punctuation = "。" if language == "source" else "."
    return (START + "\n" + " | ".join(links) + "\n\n" + note
            + f"[TRANSLATIONS.md]({relative_link(current, 'TRANSLATIONS.md')})"
            + punctuation + "\n" + END + "\n\n")


def source_state(page):
    path = ROOT / page["source"]
    text = body(path.read_text(encoding="utf-8"))
    assets = {}
    for target in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text):
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            continue
        asset = (path.parent / unquote(parsed.path)).resolve()
        name = asset.relative_to(ROOT).as_posix()
        assets[name] = digest(asset.read_bytes())
    return digest(text.encode("utf-8")), assets


def without_fences(text, name, errors):
    outside = []
    opened = None
    for line in text.splitlines():
        match = re.match(r"^\s*(" + chr(96) + r"{3,}|~{3,})", line)
        if match:
            fence = match.group(1)
            if opened is None:
                opened = fence
            elif fence[0] == opened[0] and len(fence) >= len(opened):
                opened = None
        elif opened is None:
            outside.append(line)
    if opened:
        errors.append(f"{name}: unclosed code fence")
    return "\n".join(outside)


def check(data):
    errors = []
    pages = data["pages"]
    sources = [p["source"] for p in pages]
    translations = [p["translation"] for p in pages]
    expected_sources = {"序言.md", "后记.md"} | {
        p.relative_to(ROOT).as_posix() for p in ROOT.glob("第*辑*/*.md")
    }
    expected_translations = {
        p.relative_to(ROOT).as_posix() for p in (ROOT / "en").rglob("*.md")
        if p != ROOT / "en/README.md"
    }
    for label, recorded, actual in [
        ("Chinese pages", sources, expected_sources),
        ("English pages", translations, expected_translations),
    ]:
        if len(recorded) != len(set(recorded)):
            errors.append(f"{label}: duplicate manifest entry")
        if set(recorded) != actual:
            errors.append(f"{label}: manifest/files differ: {sorted(set(recorded) ^ actual)}")
    for index, page in enumerate(pages):
        texts = {}
        for language in ("source", "translation"):
            name = page[language]
            path = ROOT / name
            if not path.is_file():
                errors.append(f"Missing page: {name}")
                continue
            text = path.read_text(encoding="utf-8")
            texts[language] = text
            if not text.startswith(navigation(pages, index, language)):
                errors.append(f"{name}: navigation needs --write-navigation")
            if re.search(r"<!-- (?:diagram|source-code):", text):
                errors.append(f"{name}: unfinished translation placeholder")
        if len(texts) < 2:
            continue
        sections = []
        for language in ("source", "translation"):
            plain = without_fences(body(texts[language]), page[language], errors)
            sections.append(re.findall(r"^#{2,4}\s+(\d+(?:\.\d+)+)(?=\s)", plain, re.M))
        if sections[0] != sections[1]:
            errors.append(f"{page['translation']}: numbered sections differ from source")
        try:
            checksum, assets = source_state(page)
        except (OSError, ValueError) as exc:
            errors.append(f"{page['source']}: cannot read source assets: {exc}")
            continue
        if checksum != page.get("source_sha256") or assets != page.get("assets"):
            errors.append(f"{page['source']}: source or images changed; update English, then --refresh-source")
        translated_figures = FIGURE.findall(texts["translation"])
        if sorted(translated_figures) != sorted(assets):
            errors.append(f"{page['translation']}: English figure coverage differs from source images")
    for path in [ROOT / "README.md", ROOT / "en/README.md", ROOT / "TRANSLATIONS.md",
                 *[ROOT / p for p in sources + translations]]:
        if not path.is_file():
            errors.append(f"Missing document: {path.relative_to(ROOT)}")
            continue
        plain = without_fences(path.read_text(encoding="utf-8"), path.relative_to(ROOT), errors)
        for match in LINK.finditer(plain):
            target = match.group(1).strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken local link: {target}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-navigation", action="store_true", help="Regenerate language, contents, and previous/next links.")
    parser.add_argument("--refresh-source", action="append", default=[], metavar="CHINESE_PATH",
                        help="Record source and image hashes AFTER updating its English translation; repeat for multiple pages.")
    args = parser.parse_args()
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if args.write_navigation:
        for index, page in enumerate(data["pages"]):
            for language in ("source", "translation"):
                path = ROOT / page[language]
                path.write_text(navigation(data["pages"], index, language) + body(path.read_text(encoding="utf-8")), encoding="utf-8")
    selected = set(args.refresh_source)
    unknown = selected - {p["source"] for p in data["pages"]}
    if unknown:
        parser.error(f"Unknown Chinese paths: {sorted(unknown)}")
    if selected:
        for page in data["pages"]:
            if page["source"] in selected:
                page["source_sha256"], page["assets"] = source_state(page)
        MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    errors = check(data)
    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print(f"OK: {len(data['pages'])} bilingual page pairs, "
          f"{sum(len(p['assets']) for p in data['pages'])} translated figures; "
          "section coverage, navigation, local links, and source hashes match.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
