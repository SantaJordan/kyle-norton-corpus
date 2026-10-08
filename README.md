# Kyle Norton — Everything He's Said, Ready for Claude

Every podcast, interview, Substack post and public post we could find from **Kyle Norton**, CRO at *Lassie AI* (AI back-office automation for dental practices), previously CRO at Owner.com, and host of *The Revenue Leadership Podcast*. It's organized so Claude (or any LLM) can answer "what does Kyle think about X?" with a timestamped citation. It also includes the scripts to pull in his newest material.

Published with Kyle's permission. Collected through 2026-10-05, so the material covers his Owner.com years. His Lassie role is newer than anything here.

## What's inside

| Folder / file | What it is |
|---|---|
| `wiki/` | **Start here.** An LLM-written wiki: topic pages (`concepts/`), people and companies (`entities/`), one page per recording or post (`sources/`). Every claim cites a source and timestamp. Catalog: [`wiki/index.md`](wiki/index.md). Rules: [`wiki/SCHEMA.md`](wiki/SCHEMA.md). |
| `kyle-norton-podcasts/episodes/` | Raw transcripts: 74 episodes of his own show and 55 guest appearances (2015 → 2026-09). Each has `metadata.json`, `transcript.json` (timestamped segments) and `transcript.md`. |
| `writing/substack/` | His Substack posts (2 paywalled posts are previews only). |
| `writing/web/` | Written interviews, articles and LinkedIn posts (text capped at 6,000 characters each). |
| `kyle-norton-all-transcripts.md` | Every transcript in one file, for dropping into a long-context chat. |
| `fetch_new_content.py` | Pulls new material: new own-show episodes, new Substack posts, and any guest appearances you add. |
| `find_missed_sources.py` | Searches the web for appearances the collection is missing. |
| `wiki/lint.py` | Checks the wiki for broken links and quotes that don't match the transcripts. |

## Using it with Claude

Open this folder in Claude Code (or upload the wiki to a Claude Project) and ask questions. Examples: "What's Kyle's current view on AI SDRs, and how has it changed?" "What Owner.com numbers has he shared, and do they agree?" `CLAUDE.md` tells Claude how the folder is laid out.

## Updating it yourself

You need Python 3, `yt-dlp` and `ffmpeg` (`brew install yt-dlp ffmpeg` on a Mac), plus your own API keys:

| Key | Needed for | Rough cost |
|---|---|---|
| `OPENAI_API_KEY` | Transcribing audio with Whisper (`fetch_new_content.py`) | ~$0.36 per hour of audio |
| `EXA_API_KEY`, `PARALLEL_API_KEY` | Optional: the missed-sources web search (`find_missed_sources.py`) | under $1 per run |

Copy `.env.example` to `.env` and fill in your keys, or export them in your shell. `.env` is git-ignored, so it never gets committed.

1. **Find gaps (every few months, optional):** `python3 find_missed_sources.py`. This writes a spreadsheet to `research/`. Rows marked `NEW` haven't been collected yet. Add the real ones to `GUEST_EPISODES` in `fetch_new_content.py`.
2. **Pull new material:** `python3 fetch_new_content.py --since 2026-10-05`. It reads his show's RSS feed and his Substack, and downloads anything in `GUEST_EPISODES`. Anything already transcribed is skipped.
3. **Update the wiki:** ask Claude to "ingest the new sources into the wiki, following wiki/SCHEMA.md". That means one source page per new item, then updates to the topic and people pages it touches.
4. **Check it:** `python3 wiki/lint.py`. It should report 0 broken links and 0 non-verbatim quotes.

If YouTube downloads fail with HTTP 403, update `yt-dlp` (`brew upgrade yt-dlp`).

## Things to know

- **Transcripts have no speaker labels.** On his own show the guest does most of the talking, so the wiki credits a line to Kyle only when it's clearly him. His own views mostly come from his guest appearances.
- **Publish date ≠ record date.** An episode that aired in April can quote numbers from months earlier. Check the date before treating a figure as current.
- **His numbers vary by venue** (ARR per rep, research lift and others). `wiki/entities/owner-com.md` keeps a reconciliation section.
- **Duplicates:** `kyle-nortons-bets-for-gtm-domination` is a rebroadcast of GTMnow 163, `saastr-gtm-efficiency-owner` is an edited cut of `saastr-gtm-efficiency-smb`, and `grow-and-tell-selling-skeptical-icp` is a clip. Count each once.
- **Transcript quality:** own-show E31–E64 come from YouTube auto-captions (no punctuation, occasional errors). Everything else is OpenAI Whisper.
- **The old YouTube playlist is stale.** The show moved to a new YouTube channel in 2026, so the RSS feed is the source of truth for episodes.

## Known gaps (as of 2026-10-05)

- **Unreachable:** Reprise Revenue Leadership Series Ep 03 (private video); "Score-carding for Success" (page 404); OwnerTube "Building Owner" interview (page 404).
- **Partial text:** web pages are capped at 6,000 characters; 2 Substack posts are paywalled previews.
- **Not yet searched exhaustively:** his full LinkedIn history (about 50 posts captured), and appearances he mentions with no recording found: Sales Reframed (~Mar 2026), Boardroom RevOps (Oct 2025), Trig webinar (Apr 2026), Accord panel (Mar 2026), Salesforce Startup Summit panel (Apr 2026), AI Fluent Revenue Leader (Jul 2026).
- Short clips (under 7 minutes) that excerpt longer episodes were skipped.
