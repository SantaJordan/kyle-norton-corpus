#!/usr/bin/env python3
"""Incremental update: pull everything Kyle Norton said/wrote after the last collection.

Sources:
  - Own show: libsyn RSS enclosures (audio) -> OpenAI Whisper
  - Guest appearances: YouTube audio via yt-dlp -> OpenAI Whisper
  - Writing: Substack posts (therevenueleadershippodcast.com) -> markdown

OPENAI_API_KEY is read from the environment, or from a .env file next to this script
(copy .env.example to .env). Never hardcode a key.
Usage: python3 fetch_new_content.py [--since 2026-03-06]
"""

import argparse
import html
import json
import os
import re
import subprocess
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date
from email.utils import parsedate_to_datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EPISODES = ROOT / "kyle-norton-podcasts" / "episodes"
OWN_DIR, GUEST_DIR = EPISODES / "own-show", EPISODES / "guest-appearances"
WRITING_DIR = ROOT / "writing" / "substack"
AUDIO_DIR = Path(os.environ.get("TMPDIR", "/tmp")) / "kyle_norton_audio"
RSS_URL = "https://rss.libsyn.com/shows/546792/destinations/4716112.xml"
SUBSTACK = "https://www.therevenueleadershippodcast.com"
UA = {"User-Agent": "Mozilla/5.0"}
MAX_BYTES = 24 * 1024 * 1024

# Own-show episodes missed by the first (2026-03-06) collection, by RSS episode number.
BACKFILL_OWN = {52}

GUEST_EPISODES = [
    ("otTvdQ8d7cA", "firmable-best-practice-killing-sales", "Firmable", "Episode 10: Why \"Best Practice\" Is Killing Your Sales Team"),
    ("tX5lb-vx_Bw", "gtmshift-your-gtm-worked-live", "The GTMshift", "Kyle Norton - Your GTM Worked Live"),
    ("9ppK03I-Hy0", "caliber-outbound-objection-navigation", "Caliber", "Introducing the Outbound Objection Navigation System"),
    ("BzA8bTjFIgk", "saastr-2m-arr-per-rep-with-ai", "SaaStr AI", "How Owner.com's CRO Closes $2M+ ARR Per Rep With AI"),
    ("vjEE3ku_stE", "ivey-future-of-sales-irreplaceable", "Ivey Business School", "The Future of Sales: How to Stay Irreplaceable in the Age of AI"),
    ("naK3Rb2H5v8", "union-square-cro-stories-60m-arr", "Union Square Consulting (CRO Stories)", "The Investments and Priorities That Took Owner.com to $60M ARR"),
    ("CIu_Cjql9Do", "captivate-talent-stop-vibe-hiring", "Captivate Talent", "How to Stop Vibe Hiring and Build a Sales Team That Actually Scales"),
    ("-1w3tRUX0JI", "topline-world-class-ai-in-gtm", "Topline (Pavilion)", "What World-Class AI in GTM Looks Like"),
    ("xLSkTfmB-e8", "crew-podcast-how-best-cros-hire", "The Crew Podcast", "How The Best CROs Actually Hire Salespeople"),
    # Backfill 2026-10-05 — README "Known gaps" + coverage audit (find_missed_sources.py)
    ("YiNv22b0Lxc", "gtmshift-lessons-in-scaling-2025", "The GTMshift", "Lessons in Scaling with Kyle Norton"),
    ("G5oEN3vVy1U", "polaris-lodestar-s1e1", "Polaris Ops (LodeStar)", "LodeStar S1 EP 1: Kyle Norton"),
    ("evrLRF1v-do", "whispered-hiring", "Whispered", "Whispered Hiring with Kyle Norton"),
    ("9oLxWRF9Uys", "saastr-ai-sales-gtm-2026-lemkin", "SaaStr AI", "AI, Sales + GTM in 2026: This Changes Everything (with Jason Lemkin)"),
    ("acDTXCZmoGg", "coffee-scaling-smarter", "Coffee", "Scaling Smarter: Building High-Velocity Sales Teams for Long-Term Growth"),
    ("RSEW5vyyQYA", "topline-e99-operationalizing-ai", "Topline (Pavilion)", "E99: How GTM Revenue Leaders Are Operationalizing AI for Growth"),
    ("qrd0pfxow0c", "getaccept-change-management", "GetAccept (On the Record #14)", "Change management made simple"),
    ("pNnUxp8Nufk", "bravado-scaling-smb-30m", "Bravado", "Scaling SMB to $30M, Investing in RevOps Early, and Stage-appropriate Sales Hiring"),
    ("IcWaOtvDImo", "saastr-ai-revops-playbook", "SaaStr AI", "The RevOps Playbook: Owner.com CRO's Secrets to Scaling"),
    ("IxJwD9_6vGs", "revenue-diaries-ep4", "Revenue Diaries", "Episode 4: The Raw DNA of a Competitive Psycho & Loving Father"),
    ("6nHa3Gxk0og", "topline-e78-executive-fear-boards", "Topline (Pavilion)", "E78: CRO Kyle Norton on Executive Fear, Boards, and the CRO Journey"),
    ("ZM59pcrW0I4", "top-founders-latka-5m-arr-cro", "Top Founders (Nathan Latka)", "$5m in ARR? Your CRO Should Be Focused on These 3 Things"),
    ("c6U2KVbpk28", "startwell-cro-tells-founders", "StartWell", "The CRO Who Tells Founders Exactly What They Don't Want to Hear About Sales"),
    ("aama2OEZ9Tg", "signal-learn-build-scale", "The Signal (AI x GTM Summit)", "Learn, Build, Scale: A Revenue Leader's AI Transformation Roadmap"),
    ("RznL6-oauPE", "momentum-planning-2025-ai-strategy", "Momentum (AI Advantage webinar)", "Planning Your 2025 AI Strategy"),
    ("pTYKzeeh_lE", "dmz-chat-shopify-2020", "DMZ", "Chat with Kyle Norton, Head of Revenue, Retail at Shopify"),
    ("TE4rfMz48Zw", "shopify-head-of-revenue-retail-2020", "YouTube", "Kyle Norton, Head of Revenue, Retail at Shopify"),
    ("ThT_QwkdZmY", "reprise-revenue-leadership-ep03", "Reprise", "Revenue Leadership Series Ep 03"),
]

# Non-YouTube backfill: (audio or page URL, slug, podcast, title, publish date)
AUDIO_BACKFILL = [
    ("https://traffic.libsyn.com/secure/thetwentyminutevc/Kyle_Norton__Owner.com.mp3", "20vc-20sales-2m-to-40m-arr", "20VC (20Sales)", "From $2M ARR to $40M ARR: The Playbook", "2025-05-30"),
    ("https://anchor.fm/s/db885b68/podcast/play/104967034/https%3A%2F%2Fd3ctxlq1ktw2nl.cloudfront.net%2Fstaging%2F2025-6-3%2F403229363-44100-2-63291141cc886.mp3", "pocus-scaling-3m-to-21m", "Pocus Unlocking Revenue", "Secrets for scaling $3M to $21M", "2025-07-03"),
    ("https://anchor.fm/s/a2f07060/podcast/play/97491509/https%3A%2F%2Fd3ctxlq1ktw2nl.cloudfront.net%2Fstaging%2F2025-0-24%2F393623057-44100-2-4bfdb0ad91f27.mp3", "elite-selling-pov-selling", "Elite Selling Podcast", "PoV selling with Kyle Norton", "2025-01-24"),
    ("https://api.spreaker.com/download/episode/62278336/kyle_norton_trimmed.mp3", "chief-revenue-podcast-063", "13 Jobs - The Chief Revenue Podcast", "063 - Kyle Norton's Revenue Leadership Framework", "2024-10-08"),
    ("https://anchor.fm/s/f3bf9a70/podcast/play/87556021/https%3A%2F%2Fd3ctxlq1ktw2nl.cloudfront.net%2Fstaging%2F2024-5-3%2F5ef665a0-bdf5-8914-b328-7dbbf8175bc6.mp3", "the-simmer-owner-cro", "The Simmer", "Kyle Norton, Chief Revenue Officer, Owner.com", "2024-06-04"),
    ("https://www.buzzsprout.com/2301388/episodes/14555449-navigating-sales-leadership-with-kyle-norton.mp3", "pillar-talk-navigating-sales-leadership", "Pillar Talk (Rick Smolen)", "Navigating Sales Leadership with Kyle Norton", "2024-02-23"),
    ("https://thegtmnewsletter.substack.com/p/gtm-5-slow-is-smooth-smooth-is-fast-d19", "gtmnow-5-slow-is-smooth", "GTMnow", "GTM 5: Slow is Smooth; Smooth is Fast", "2022-11-01"),
    ("https://salesleaderpodcast.fireside.fm/15", "sales-leadership-podcast-15-league", "Sales Leadership Podcast", "#15: Kyle Norton of League — Slow is Smooth...Smooth is Fast", "2018-09-25"),
    ("https://feeds.soundcloud.com/stream/225891967-hunterandcraft-kyle-norton-vision-critical.m4a", "hunter-craft-radio-vision-critical", "Hunter & Craft Radio", "Radio Episode #12: Kyle Norton of Vision Critical", "2015-09-28"),
]


def load_key():
    if os.environ.get("OPENAI_API_KEY"):
        return os.environ["OPENAI_API_KEY"]
    env = Path(__file__).resolve().parent / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            m = re.match(r"^(?:export\s+)?OPENAI_API_KEY=(.*)$", line.strip())
            if m:
                return m.group(1).strip().strip("'\"")
    raise SystemExit("OPENAI_API_KEY not set — export it or put it in .env (see .env.example)")


def slugify(s, n=64):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")[:n].rstrip("-")


def fetch(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r:
        return r.read()


def compress(src, dst):
    for kbps in (48, 32, 24):
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-ac", "1", "-ar", "16000",
                        "-b:a", f"{kbps}k", str(dst)], check=True)
        if dst.stat().st_size <= MAX_BYTES:
            return dst
    raise RuntimeError(f"{src.name} still >24MB at 24kbps")


def transcribe(client, audio):
    with open(audio, "rb") as f:
        r = client.audio.transcriptions.create(model="whisper-1", file=f, response_format="verbose_json")
    return [{"start": round(s.start, 2), "duration": round(s.end - s.start, 2), "text": s.text.strip()} for s in r.segments]


def write_episode(folder, meta, segments):
    folder.mkdir(parents=True, exist_ok=True)
    meta["transcript_segments"] = len(segments)
    (folder / "metadata.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False))
    (folder / "transcript.json").write_text(json.dumps(segments, indent=2, ensure_ascii=False))
    lines, next_marker = [f"# {meta['title']}", "", f"*{meta.get('date', '')} · {meta.get('podcast_name', '')}*", ""], 60
    para = []
    for s in segments:
        if s["start"] >= next_marker:
            lines += [" ".join(para), "", f"**[{int(s['start'] // 60):02d}:{int(s['start'] % 60):02d}]**", ""]
            para, next_marker = [], s["start"] + 60
        para.append(s["text"])
    lines.append(" ".join(para))
    (folder / "transcript.md").write_text("\n".join(lines) + "\n")


def process(client, job):
    folder, meta, source = job["folder"], job["meta"], job["source"]
    if (folder / "transcript.json").exists():
        return f"skip {folder.name}"
    raw = AUDIO_DIR / f"{folder.name}.raw"
    if job.get("direct"):
        raw.write_bytes(fetch(source))
    else:
        subprocess.run(["yt-dlp", "-q", "-x", "--audio-format", "mp3", "-o", str(raw.with_suffix(".%(ext)s")),
                        "--", source], check=True, timeout=900)
        raw = raw.with_suffix(".mp3")
    small = compress(raw, AUDIO_DIR / f"{folder.name}.small.mp3")
    write_episode(folder, meta, transcribe(client, small))
    return f"done {folder.name}"


def own_show_jobs(since):
    root = ET.fromstring(fetch(RSS_URL))
    jobs = []
    for it in root.iter("item"):
        title = it.findtext("title")
        d = parsedate_to_datetime(it.findtext("pubDate")).date()
        m = re.match(r"E(\d+):\s*(.*)", title)
        num = int(m.group(1)) if m else None
        if d <= since and num not in BACKFILL_OWN:
            continue
        guest = title.split("|", 1)[1].strip() if "|" in title else None
        meta = {"title": title, "host": "Kyle Norton", "guest_name": guest, "episode_num": num,
                "topic": m.group(2).split("|")[0].strip() if m else title, "date": d.isoformat(),
                "audio_url": it.find("enclosure").get("url"), "podcast_name": "The Revenue Leadership Podcast",
                "source": "revenue-leadership-podcast", "transcript_source": "openai-whisper-api (rss audio)"}
        folder = OWN_DIR / f"E{num:02d}-{slugify(meta['topic'])}"
        jobs.append({"folder": folder, "meta": meta, "source": meta["audio_url"], "direct": True})
    return jobs


def backfill_jobs():
    jobs = []
    for source, slug, pod, title, d in AUDIO_BACKFILL:
        meta = {"title": f"{pod}: {title}", "host": pod, "guest_name": "Kyle Norton", "podcast_name": pod,
                "date": d, "audio_url": source, "source": slug.split("-")[0],
                "transcript_source": "openai-whisper-api (podcast feed audio)"}
        direct = bool(re.search(r"\.(mp3|m4a)(\?|$)|anchor\.fm/.*/play/|spreaker\.com/download|soundcloud\.com/stream", source))
        jobs.append({"folder": GUEST_DIR / slug, "meta": meta, "source": source, "direct": direct})
    return jobs


def guest_jobs():
    jobs = []
    for yid, slug, pod, title in GUEST_EPISODES:
        if (GUEST_DIR / slug / "transcript.json").exists():
            continue
        r = subprocess.run(["yt-dlp", "--dump-json", "--skip-download", "--", yid], capture_output=True, text=True)
        if r.returncode != 0:
            print(f"FAIL {slug}: video unavailable ({r.stderr.strip().splitlines()[-1][:120] if r.stderr.strip() else 'no detail'})")
            continue
        info = json.loads(r.stdout)
        d = info["upload_date"]
        meta = {"title": f"{pod}: {title}", "host": info.get("channel"), "guest_name": "Kyle Norton",
                "podcast_name": pod, "date": f"{d[:4]}-{d[4:6]}-{d[6:]}", "youtube_id": yid,
                "youtube_url": f"https://www.youtube.com/watch?v={yid}", "source": slug.split("-")[0],
                "transcript_source": "openai-whisper-api"}
        jobs.append({"folder": GUEST_DIR / slug, "meta": meta, "source": yid})
    return jobs


def html_to_md(h):
    h = re.sub(r"<(h[1-4])[^>]*>(.*?)</\1>", lambda m: "\n\n## " + m.group(2) + "\n\n", h, flags=re.S)
    h = re.sub(r"<li[^>]*>(.*?)</li>", r"\n- \1", h, flags=re.S)
    h = re.sub(r"<(strong|b)>(.*?)</\1>", r"**\2**", h, flags=re.S)
    h = re.sub(r"<(em|i)>(.*?)</\1>", r"*\2*", h, flags=re.S)
    h = re.sub(r"<br\s*/?>|</p>|</blockquote>", "\n\n", h)
    h = html.unescape(re.sub(r"<[^>]+>", "", h))
    return re.sub(r"\n{3,}", "\n\n", h).strip()


def fetch_substack(since):
    WRITING_DIR.mkdir(parents=True, exist_ok=True)
    posts = json.loads(fetch(f"{SUBSTACK}/api/v1/archive?sort=new&limit=50"))
    out = []
    for p in posts:
        if p["post_date"][:10] <= since.isoformat():
            continue
        full = json.loads(fetch(f"{SUBSTACK}/api/v1/posts/{p['slug']}"))
        paywalled = full.get("audience") == "only_paid"
        body = html_to_md(full.get("body_html") or full.get("truncated_body_text") or "")
        front = (f"---\ntitle: \"{p['title'].replace(chr(34), chr(39))}\"\ndate: {p['post_date'][:10]}\n"
                 f"url: {p['canonical_url']}\nwordcount: {p.get('wordcount')}\n"
                 f"paywalled: {str(paywalled).lower()}\n---\n\n")
        note = "> **Paywalled — only the free preview below was retrievable.**\n\n" if paywalled else ""
        path = WRITING_DIR / f"{p['post_date'][:10]}-{p['slug'][:60]}.md"
        path.write_text(front + f"# {p['title']}\n\n" + note + body + "\n")
        out.append(f"{path.name} ({len(body.split())} words{', PAYWALLED preview' if paywalled else ''})")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", default="2026-03-06")
    args = ap.parse_args()
    since = date.fromisoformat(args.since)
    AUDIO_DIR.mkdir(exist_ok=True)

    for line in fetch_substack(since):
        print("substack", line)

    from openai import OpenAI
    client = OpenAI(api_key=load_key())
    jobs = own_show_jobs(since) + guest_jobs() + backfill_jobs()
    print(f"{len(jobs)} audio jobs")
    with ThreadPoolExecutor(max_workers=5) as ex:
        futs = {ex.submit(process, client, j): j["folder"].name for j in jobs}
        for f in as_completed(futs):
            try:
                print(f.result(), flush=True)
            except Exception as e:
                print(f"FAIL {futs[f]}: {e}", flush=True)


if __name__ == "__main__":
    main()
