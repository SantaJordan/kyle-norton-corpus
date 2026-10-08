# Kyle Norton Wiki — Schema

The rulebook for this wiki (the "schema" layer in Karpathy's LLM-wiki pattern). Every LLM session that reads or writes this wiki follows it.

## What this wiki is

A compounding knowledge base of **what Kyle Norton (CRO @ Owner.com) has said and written**: his own show (*The Revenue Leadership Podcast*), his guest appearances on other shows, and his Substack. The LLM writes and maintains every page. A human drops sources and asks questions.

## Three layers

| Layer | Path | Who writes | Rule |
|---|---|---|---|
| Raw sources | `raw/` (symlinks to `../kyle-norton-podcasts/episodes/`, `../writing/substack/`) | Scripts (`../fetch_new_content.py`) | **Immutable.** Never edit a transcript. |
| Wiki pages | `sources/`, `entities/`, `concepts/`, `syntheses/` | LLM | Rewrite freely; never delete (see lifecycle). |
| Schema | this file | LLM + maintainer | Change deliberately. |

## Page types

- **`sources/src-<slug>.md`**: one page per podcast episode or post. It covers what was said, with timestamps, verbatim quotes, and numbers. It is the only page type that cites transcripts directly.
- **`entities/<slug>.md`**: a person, company, or show. Each has a "Timeline" and a "What Kyle has said about it" section.
- **`concepts/<slug>.md`**: one topic Kyle has a view on. It holds his **current position**, how that position **evolved** (dated), supporting quotes, and contradictions or tensions. Every claim cites a `[[src-...]]` page.
- **`syntheses/<slug>.md`**: cross-cutting analyses (e.g., "what changed since March 2026", "Kyle's operating playbook").

## Frontmatter (every page)

```yaml
---
slug: <filename without .md>
type: source | entity | concept | synthesis
lifecycle: emergent | validated | canonical   # emergent = 1 source; validated = 2+ sources; canonical = maintainer-promoted
valid_from: YYYY-MM-DD        # for sources: publish date; otherwise first-evidence date
invalid_at: null              # set (never delete) when superseded
superseded_by: null
sources: [relative/paths/to/raw]   # source pages: raw transcript path; others: [[src-...]] slugs
links: [slug, slug]
tags: [tag, tag]
---
```

## Citation rules

- **Verify, don't guess.** Every quote must be verbatim from the transcript. Every number must appear in a source. Cite as `[[src-slug]] @mm:ss`.
- Transcripts have **no speaker labels**. On Kyle's own show, attribute a line to Kyle only when context makes it unambiguous (he's asking, framing, or speaking of Owner.com in the first person). Otherwise write "the guest said". On guest appearances, Kyle is the main speaker. The host's questions are not Kyle's views.
- Older YouTube-caption transcripts (own-show E31–E46 era) have no punctuation and some mis-transcriptions (e.g., "Sastr" = SaaStr). Normalize spelling inside quotes only when the meaning is unambiguous.
- Paywalled Substack posts carry only a preview. Mark any claim from them `(preview only)`.

## Canonical slugs (link to these; create new ones only when nothing fits)

**Entities:** `kyle-norton`, `owner-com`, `revenue-leadership-podcast`, `pavilion`, `shopify`, `clay`, `saastr`, `momentum`, `person-yg` (Owner applied-AI lead), `person-steve-dinner` (Owner VP RevOps), plus `person-<first-last>` for recurring people (e.g. `person-kevin-bailey`, `person-jason-lemkin`, `person-everett-berry`).

**Concepts:**
`ai-in-gtm` · `ai-sales-stack` · `gtm-engineering` · `ai-sdrs-and-agents` · `build-vs-buy-software` · `buyer-ai-aeo-geo` · `talent-density` · `sales-hiring` · `hiring-scorecards` · `sales-coaching-and-enablement` · `playbooks-and-documentation` · `smb-sales-motion` · `outbound-at-scale` · `icp-and-saying-no` · `revops` · `metrics-and-forecasting` · `comp-plans` · `capacity-planning` · `churn-and-retention` · `org-design` · `cro-role-and-board` · `career-and-leadership` · `executive-performance-and-mindset` · `fundraising-and-investability` · `marketing-alignment` · `culture-and-high-standards` · `point-of-view-positioning` · `ai-operating-model` (centralized vs decentralized) · `ai-sophistication-ladder` · `context-harness-and-memory` · `personal-ai-stack` · `sales-methodology` (PROFIT, PCRIOS, NASCAR, 4i) · `operating-rhythm` · `prioritization-5p` · `office-vs-remote` · `recognition-and-motivation`

## Operations

- **Ingest:** a new raw source becomes one `sources/` page. Then update every touched `concepts/` and `entities/` page: add new evidence, revise "current position", and record evolution with dates. Update `index.md` and append to `log.md`.
- **Query:** answer from wiki pages first. Fall back to raw transcripts only to verify. If an answer is worth keeping, file it in `syntheses/`.
- **Lint:** find orphans, concepts with no `[[src-]]` citations, stale "current position" claims, and contradictions not yet called out.

## Log format

`YYYY-MM-DD HH:MM <type> <action> [[slug]] <one-line summary>` (append-only).
