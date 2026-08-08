#!/usr/bin/env python3
"""Zero-dependency integrity checks for the static portfolio.

Validates local href/src targets, published writing/backlog consistency, and the
minimum head metadata required for GitHub Pages rendering. This does not claim to
replace a browser visual-regression suite; it catches the static failures that can
make a Pages deployment render without CSS/assets or lead to dead article links.
"""
from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
IGNORE_DIRS = {".git", ".github"}


class Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.targets: list[tuple[str, str]] = []
        self.title_seen = False
        self.viewport_seen = False
        self.charset_seen = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if tag == "a" and data.get("href"):
            self.targets.append(("href", data["href"] or ""))
        if tag in {"img", "script", "link", "source"}:
            for key in ("src", "href", "srcset"):
                if data.get(key):
                    value = data[key] or ""
                    if key == "srcset":
                        for part in value.split(","):
                            self.targets.append((key, part.strip().split(" ")[0]))
                    else:
                        self.targets.append((key, value))
        if tag == "title":
            self.title_seen = True
        if tag == "meta" and data.get("name", "").lower() == "viewport":
            self.viewport_seen = True
        if tag == "meta" and "charset" in data:
            self.charset_seen = True


def html_files() -> list[Path]:
    out: list[Path] = []
    for path in ROOT.rglob("*.html"):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        out.append(path)
    return sorted(out)


def local_target(source: Path, raw: str) -> Path | None:
    raw = raw.strip()
    if not raw or raw.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return None
    parts = urlsplit(raw)
    if parts.scheme or parts.netloc or raw.startswith("//"):
        return None
    path_text = unquote(parts.path)
    if not path_text:
        return None
    if path_text.startswith("/"):
        candidate = ROOT / path_text.lstrip("/")
    else:
        candidate = source.parent / path_text
    candidate = candidate.resolve()
    try:
        candidate.relative_to(ROOT.resolve())
    except ValueError:
        return candidate
    if path_text.endswith("/") or candidate.is_dir():
        candidate = candidate / "index.html"
    return candidate


def validate_html() -> list[str]:
    errors: list[str] = []
    for path in html_files():
        text = path.read_text(encoding="utf-8")
        parser = Links()
        try:
            parser.feed(text)
            parser.close()
        except Exception as exc:  # pragma: no cover - defensive CI path
            errors.append(f"{path.relative_to(ROOT)}: HTML parser error: {exc}")
            continue

        # HTMLParser doesn't surface <title> as a start tag in all malformed cases,
        # so use explicit checks for the minimum head contract.
        if not re.search(r"<title>.+?</title>", text, flags=re.I | re.S):
            errors.append(f"{path.relative_to(ROOT)}: missing non-empty <title>")
        if not re.search(r"<meta\s+[^>]*charset=", text, flags=re.I):
            errors.append(f"{path.relative_to(ROOT)}: missing charset meta")
        if not re.search(r"<meta\s+[^>]*name=[\"']viewport[\"']", text, flags=re.I):
            errors.append(f"{path.relative_to(ROOT)}: missing viewport meta")

        for kind, raw in parser.targets:
            target = local_target(path, raw)
            if target is None:
                continue
            if not target.exists():
                errors.append(
                    f"{path.relative_to(ROOT)}: broken local {kind}={raw!r} -> "
                    f"{target.relative_to(ROOT) if target.is_relative_to(ROOT) else target}"
                )
    return errors


def validate_writing_contract() -> list[str]:
    errors: list[str] = []
    backlog_path = ROOT / "writing" / "backlog.json"
    index_path = ROOT / "writing" / "index.html"
    backlog = json.loads(backlog_path.read_text(encoding="utf-8"))
    index = index_path.read_text(encoding="utf-8")

    unfinished = [
        item.get("slug", "<missing>")
        for item in backlog.get("items", [])
        if item.get("status") != "published"
    ]
    if unfinished:
        errors.append("writing backlog has unfinished items: " + ", ".join(unfinished))

    for item in backlog.get("items", []):
        path = item.get("published_path")
        if not path:
            errors.append(f"{item.get('slug')}: published item missing published_path")
            continue
        full = ROOT / path
        if not full.exists():
            errors.append(f"{item.get('slug')}: published_path does not exist: {path}")
            continue
        href = Path(path).name
        if href not in index:
            errors.append(f"{item.get('slug')}: writing index does not link {href}")

    return errors


def main() -> int:
    errors = validate_html() + validate_writing_contract()
    if errors:
        print("site integrity FAILED", file=sys.stderr)
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1
    print(f"site integrity OK: {len(html_files())} HTML pages")
    print("writing backlog OK: all items published and indexed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
