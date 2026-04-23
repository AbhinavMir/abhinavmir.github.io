#!/usr/bin/env python3
"""Fetch Mataroa RSS and write posts.json. Stdlib only."""
import json
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

RSS_URL = "https://august.mataroa.blog/rss/"
OUT = Path(__file__).resolve().parent.parent / "posts.json"


def main():
    req = urllib.request.Request(RSS_URL, headers={"User-Agent": "abhinavmir.github.io sync"})
    with urllib.request.urlopen(req, timeout=20) as r:
        data = r.read()
    root = ET.fromstring(data)
    posts = []
    for it in root.findall("./channel/item"):
        posts.append({
            "title": (it.findtext("title") or "").strip(),
            "url": (it.findtext("link") or "").strip(),
            "published": (it.findtext("pubDate") or "").strip(),
        })
    OUT.write_text(json.dumps(posts, indent=2) + "\n")
    print(f"wrote {len(posts)} posts to {OUT}")


if __name__ == "__main__":
    main()
