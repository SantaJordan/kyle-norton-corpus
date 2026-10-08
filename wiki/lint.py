#!/usr/bin/env python3
"""Wiki lint: broken [[links]], orphan pages, and quotes not found verbatim in the raw sources.

Usage: python3 wiki/lint.py   (run from anywhere)
"""
import glob
import os
import re

WIKI = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(WIKI)
DIRS = ["sources", "concepts", "entities", "syntheses"]


def q(s):
    return (s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
             .replace("…", "...").replace("—", "-").replace("–", "-"))


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"\*\*\[\d+:\d+\]\*\*", "", q(s))).lower()


pages = {os.path.basename(f)[:-3]: f for d in DIRS for f in glob.glob(f"{WIKI}/{d}/*.md")}
print({d: len(glob.glob(f"{WIKI}/{d}/*.md")) for d in DIRS})

# Links + orphans (index.md counts as an inbound reference)
index = open(f"{WIKI}/index.md").read() if os.path.exists(f"{WIKI}/index.md") else ""
inbound = {k: int(f"[[{k}]]" in index) for k in pages}
broken = {}
for k, f in pages.items():
    for link in set(re.findall(r"\[\[([^\]|#]+)", open(f).read())):
        link = link.strip()
        if link in pages:
            inbound[link] += link != k
        else:
            broken.setdefault(link, []).append(k)
print(f"broken links: {len(broken)}")
for link, src in sorted(broken.items()):
    print(f"  [[{link}]] <- {', '.join(src[:3])}")
orphans = [k for k, v in inbound.items() if v == 0]
print(f"orphans: {orphans or 'none'}")

# Quotes in derived pages must appear verbatim in source pages / transcripts / posts
corpus = norm(" ".join(open(f).read() for f in
                       glob.glob(f"{WIKI}/sources/*.md")
                       + glob.glob(f"{ROOT}/kyle-norton-podcasts/episodes/*/*/transcript.md")
                       + glob.glob(f"{ROOT}/writing/*/*.md")))
total, misses = 0, []
for d in ["concepts", "entities", "syntheses"]:
    for f in sorted(glob.glob(f"{WIKI}/{d}/*.md")):
        for line in open(f):
            line = q(re.sub(r"\[\[[^\]]*\]\]", "", line))
            for s in re.findall(r'"([^"\n]*)"', line):
                if len(s) < 12:
                    continue
                total += 1
                parts = [re.sub(r"\s+", " ", p.strip(" .,;:!?'")) for p in re.split(r"\.\.\.|\[[^\]]*\]", s.lower())]
                parts = [p for p in parts if len(p) > 3]
                if parts and not all(p in corpus for p in parts):
                    misses.append(f"{os.path.basename(f)}: {s[:100]}")
print(f"quotes checked: {total}, not verbatim: {len(misses)}")
for m in misses:
    print("  " + m)
