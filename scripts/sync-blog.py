#!/usr/bin/env python3
"""Fetch Mataroa RSS and write posts.json. Stdlib only."""
import json
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path

RSS_URL = "https://august.mataroa.blog/rss/"
OUT = Path(__file__).resolve().parent.parent / "posts.json"
MAX_POSTS = 10
EXCERPT_CHARS = 220


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)

    def text(self):
        return "".join(self.parts)


def strip_html(html):
    p = TextExtractor()
    p.feed(html)
    return " ".join(p.text().split())


def main():
    req = urllib.request.Request(RSS_URL, headers={"User-Agent": "abhinavmir.github.io sync"})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = r.read()
    root = ET.fromstring(data)
    posts = []
    for it in root.findall("./channel/item")[:MAX_POSTS]:
        title = (it.findtext("title") or "").strip()
        link = (it.findtext("link") or "").strip()
        pub = (it.findtext("pubDate") or "").strip()
        desc = it.findtext("description") or ""
        excerpt = strip_html(desc)
        if len(excerpt) > EXCERPT_CHARS:
            excerpt = excerpt[:EXCERPT_CHARS].rsplit(" ", 1)[0] + "…"
        posts.append({"title": title, "url": link, "published": pub, "excerpt": excerpt})
    OUT.write_text(json.dumps(posts, indent=2) + "\n")
    print(f"wrote {len(posts)} posts to {OUT}")


if __name__ == "__main__":
    main()
