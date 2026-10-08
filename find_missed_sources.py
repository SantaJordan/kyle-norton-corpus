#!/usr/bin/env python3
"""Coverage audit: search the web (Exa + Parallel) for Kyle Norton content we haven't collected.

Writes research/missed-sources-<date>.csv (+ raw JSON) with each hit classified as
  have      — already in kyle-norton-podcasts/ or writing/ (matched by YouTube ID, URL, or title)
  own-show  — an episode of his own podcast (RSS is authoritative; we pull those separately)
  gap       — already listed under README "Known gaps"
  NEW       — not seen before → review by hand

Keys (EXA_API_KEY, PARALLEL_API_KEY) are read from the environment, or from a .env file next to
this script (copy .env.example to .env).
Usage: python3 find_missed_sources.py [--no-task]
"""

import argparse
import csv
import json
import os
import re
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "research"
EPISODES = ROOT / "kyle-norton-podcasts" / "episodes"

QUERIES = [
    "Kyle Norton Owner.com podcast interview",
    "Kyle Norton CRO Owner.com guest episode",
    "Kyle Norton Owner.com webinar",
    "Kyle Norton Owner.com conference talk keynote",
    "Kyle Norton Owner.com interview article",
    "Kyle Norton Owner.com Q&A written interview",
    "Kyle Norton chief revenue officer Owner restaurant software sales",
    "Kyle Norton Owner.com AI sales team",
    "Kyle Norton Owner.com hiring sales reps",
    "Kyle Norton Owner.com revenue leadership",
    "Kyle Norton Shopify sales leader interview",
    "Kyle Norton League sales VP interview",
    "Kyle Norton Pavilion CRO school",
    "Kyle Norton SaaStr session Owner.com",
    "Kyle Norton GTM Fund Stage 2 Capital",
    "Kyle Norton Owner.com quoted",
    "Kyle Norton guest post newsletter sales",
    "Kyle Norton Owner.com YouTube",
    "Kyle Norton Owner.com Spotify podcast episode",
    "Kyle Norton Owner.com LinkedIn Live",
]
OBJECTIVE = ("Find every podcast episode, video interview, webinar, conference talk, written interview, "
             "guest article, newsletter feature or press piece where Kyle Norton (Chief Revenue Officer at "
             "Owner.com, formerly Shopify and League, host of The Revenue Leadership Podcast) speaks or is "
             "interviewed or quoted. Include older appearances too.")

TASK_SCHEMA = {
    "type": "object",
    "properties": {"appearances": {"type": "array", "items": {"type": "object", "properties": {
        "title": {"type": "string"}, "outlet": {"type": "string"}, "url": {"type": "string"},
        "date": {"type": "string", "description": "YYYY-MM-DD or YYYY-MM if known, else empty"},
        "format": {"type": "string", "description": "podcast | video | webinar | conference talk | written interview | article | newsletter | other"},
        "kyle_role": {"type": "string", "description": "guest | host | panelist | speaker | quoted | author"},
    }, "required": ["title", "outlet", "url", "date", "format", "kyle_role"], "additionalProperties": False}}},
    "required": ["appearances"], "additionalProperties": False,
}


def keys():
    k = {n: os.environ.get(n) for n in ("EXA_API_KEY", "PARALLEL_API_KEY")}
    env = ROOT / ".env"
    for line in (env.read_text().splitlines() if env.exists() else []):
        m = re.match(r"^(?:export\s+)?(EXA_API_KEY|PARALLEL_API_KEY)=(.*)$", line.strip())
        if m and not k[m.group(1)]:
            k[m.group(1)] = m.group(2).strip().strip("'\"")
    return k


def http(method, url, headers, body=None, timeout=180):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method,
                                 headers={"Content-Type": "application/json", **headers})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        return {"_error": e.code, "_body": e.read().decode()[:500]}


def exa(key, q):
    r = http("POST", "https://api.exa.ai/search", {"x-api-key": key},
             {"query": q, "numResults": 25, "type": "auto", "contents": {"text": {"maxCharacters": 400}}})
    return [{"engine": "exa", "query": q, "title": x.get("title") or "", "url": x.get("url"),
             "date": (x.get("publishedDate") or "")[:10], "snippet": (x.get("text") or "")[:300]}
            for x in r.get("results", [])]


def parallel_search(key, q):
    r = http("POST", "https://api.parallel.ai/v1beta/search",
             {"x-api-key": key, "parallel-beta": "search-extract-2025-10-10"},
             {"objective": OBJECTIVE, "search_queries": [q], "max_results": 20})
    return [{"engine": "parallel", "query": q, "title": x.get("title") or "", "url": x.get("url"),
             "date": x.get("publish_date") or "", "snippet": " ".join(x.get("excerpts") or [])[:300]}
            for x in r.get("results", [])]


def parallel_task(key):
    hdr = {"x-api-key": key}
    run = http("POST", "https://api.parallel.ai/v1/tasks/runs", hdr, {
        "input": OBJECTIVE, "processor": "ultra",
        "task_spec": {"output_schema": {"type": "json", "json_schema": TASK_SCHEMA}}})
    if "run_id" not in run:
        print("parallel task failed to start:", run)
        return []
    for _ in range(60):  # up to ~30 min
        res = http("GET", f"https://api.parallel.ai/v1/tasks/runs/{run['run_id']}/result", hdr, timeout=600)
        if res.get("output"):
            content = res["output"].get("content")
            content = json.loads(content) if isinstance(content, str) else content
            (OUT / f"parallel-task-{date.today()}.json").write_text(json.dumps(res, indent=2))
            return [{"engine": "parallel-task", "query": "deep research", "title": a["title"],
                     "url": a["url"], "date": a["date"], "snippet": f"{a['outlet']} · {a['format']} · {a['kyle_role']}"}
                    for a in content.get("appearances", [])]
        time.sleep(30)
    print("parallel task timed out")
    return []


def known():
    titles, ids, urls = [], set(), set()
    for m in EPISODES.glob("*/*/metadata.json"):
        d = json.loads(m.read_text())
        titles.append(d.get("title", ""))
        if d.get("youtube_id"):
            ids.add(d["youtube_id"])
    for p in (ROOT / "writing" / "substack").glob("*.md"):
        m = re.search(r"^url: (\S+)", p.read_text(), re.M)
        if m:
            urls.add(m.group(1).rstrip("/"))
        t = re.search(r'^title: "(.*)"', p.read_text(), re.M)
        if t:
            titles.append(t.group(1))
    gaps = set(re.findall(r"\|\s*([A-Za-z0-9_-]{11})\s*\|", (ROOT / "README.md").read_text()))
    return titles, ids, urls, gaps


def toks(s):
    stop = {"kyle", "norton", "owner", "com", "cro", "with", "the", "and", "for", "how", "podcast", "episode"}
    return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if len(w) > 2 and w not in stop}


def classify(hit, titles, ids, urls, gaps):
    url, title = (hit["url"] or "").rstrip("/"), hit["title"]
    yid = re.search(r"(?:v=|youtu\.be/|/shorts/)([A-Za-z0-9_-]{11})", url)
    if yid and yid.group(1) in ids:
        return "have"
    if yid and yid.group(1) in gaps:
        return "gap"
    if url in urls or "therevenueleadershippodcast.com" in url:
        return "have"
    if "revenue-leadership-podcast" in url or "Revenue Leadership Podcast" in title or "libsyn.com" in url:
        return "own-show"
    t = toks(title)
    if t and any(len(t & toks(k)) / len(t) >= 0.7 for k in titles):
        return "have"
    return "NEW"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-task", action="store_true", help="skip the Parallel deep-research task")
    args = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    k = keys()
    missing = [n for n, v in k.items() if not v]
    if missing:
        raise SystemExit(f"Missing {', '.join(missing)} — export them or put them in .env (see .env.example)")
    hits = []
    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = [ex.submit(exa, k["EXA_API_KEY"], q) for q in QUERIES]
        futs += [ex.submit(parallel_search, k["PARALLEL_API_KEY"], q) for q in QUERIES]
        task = None if args.no_task else ex.submit(parallel_task, k["PARALLEL_API_KEY"])
        for f in futs:
            hits += f.result()
        if task:
            hits += task.result()
    (OUT / f"search-raw-{date.today()}.json").write_text(json.dumps(hits, indent=1))

    titles, ids, urls, gaps = known()
    rows = {}
    for h in hits:
        if not h["url"]:
            continue
        key = h["url"].split("#")[0].rstrip("/").lower()
        if key in rows:
            rows[key]["engines"].add(h["engine"])
            continue
        rows[key] = {**h, "engines": {h["engine"]}, "domain": urlparse(h["url"]).netloc.replace("www.", ""),
                     "status": classify(h, titles, ids, urls, gaps)}
    path = OUT / f"missed-sources-{date.today()}.csv"
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["status", "date", "domain", "title", "url", "engines", "snippet"])
        for r in sorted(rows.values(), key=lambda r: (r["status"] != "NEW", r["date"] or "0"), reverse=False):
            w.writerow([r["status"], r["date"], r["domain"], r["title"], r["url"], "+".join(sorted(r["engines"])), r["snippet"].replace("\n", " ")])
    counts = {}
    for r in rows.values():
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    print(f"{len(hits)} hits → {len(rows)} unique URLs → {counts}\nwrote {path}")


if __name__ == "__main__":
    main()
