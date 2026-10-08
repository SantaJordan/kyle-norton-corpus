# Kyle Norton corpus — guide for Claude

This folder holds everything Kyle Norton (CRO @ Owner.com, host of *The Revenue Leadership Podcast*) has said or written publicly, plus an LLM-maintained wiki built on top of it.

## Answering questions

1. Start at `wiki/index.md`. Topic pages are in `wiki/concepts/`, people and companies in `wiki/entities/`, one page per recording or post in `wiki/sources/`.
2. Give Kyle's **current** position first, then how it changed, citing source pages and timestamps (`[[src-...]] @mm:ss`).
3. If you need a verbatim quote, check the raw transcript in `kyle-norton-podcasts/episodes/.../transcript.md`.
4. Transcripts have no speaker labels. On his own show the guest does most of the talking, so only attribute a line to Kyle when it's unambiguous.
5. Publish date ≠ record date, and his numbers vary by venue. See the reconciliation section in `wiki/entities/owner-com.md` before calling a figure current.

## Adding new material

Read `wiki/SCHEMA.md` before writing any wiki page. The refresh steps are in `README.md` → "Updating it yourself". When you're done, `python3 wiki/lint.py` must report 0 broken links and 0 non-verbatim quotes.

API keys come from the environment or a git-ignored `.env` file (see `.env.example`). Never write a key into a script or a committed file.
