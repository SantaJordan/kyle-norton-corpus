---
slug: src-E71-the-most-efficient-marketing-org-in-the-world-35-people-350m
type: source
lifecycle: validated
valid_from: 2026-07-01
invalid_at: null
superseded_by: null
sources: [raw/podcasts/own-show/E71-the-most-efficient-marketing-org-in-the-world-35-people-350m/transcript.md]
links: [kyle-norton, owner-com, revenue-leadership-podcast, person-tim-rutten, ai-in-gtm, gtm-engineering, build-vs-buy-software, ai-sales-stack, org-design, marketing-alignment, icp-and-saying-no, revops, metrics-and-forecasting, ai-sdrs-and-agents]
tags: [own-show, backbase, cmo, gtm-os, ai-native, vercel, landing-zone, gtm-architect, signal-engine, abm, love-letters, podcast-as-abm, banking]
---

# E71: The Most Efficient Marketing Org In The World? (35 People, $350M)
**Show:** The Revenue Leadership Podcast · **Guest:** Tim Rutten, CMO @ Backbase (spelled "Tim Bruton" in the cold-open transcription) · **Published:** 2026-07-01 · **Kyle's role:** host · **Raw:** `raw/podcasts/own-show/E71-the-most-efficient-marketing-org-in-the-world-35-people-350m/transcript.md`

## TL;DR
- "AI native" means redesigning the org as a system from day zero. Rutten and his CRO went "all in," seeded Claude Code to leaders for 2–4 weeks to create buy-in, then halted the free-for-all and built a governed in-house "GTMOS" on Vercel. Six months in, they're "30 to 40%" of the way to automating how they operate.
- The model needs a strong "landing zone," a GTM *architect* who owns the harness, and 5–8 business-owner builders. A standalone GTM engineering team becomes a bottleneck. Kyle notes this differs from his own centralized-team approach.
- Results: 35 marketing FTEs on $350M+ ARR. Bespoke signal engine replaced 6sense. Fully automated QBR decks. One-to-one ABM plans in 15 minutes. Exec "love letters" get ~40% response. A C-suite-only podcast works as an ABM channel.

## What Kyle said
- Cold open: "as you know, I'm massively AI-pilled... I took a ton of notes." @00:00 ([[ai-in-gtm]])
- Same YouTube channel-move PSA as E70. @00:00–02:04 ([[revenue-leadership-podcast]])
- Framing: "why individual co-pilots are table stakes and why we're really past them now," plus redesigning a revenue org that combines agents and humans. @02:04 ([[ai-in-gtm]], [[org-design]])
- "AI native" is "the buzzword du jour. Every founder wants an AI native revenue leader." @03:04 ([[career-and-leadership]])
- On change management, he frames resistance as "change is being done to them and not with them." @11:14 ([[org-design]])
- Pushed on the structural pillars needed once everyone has terminal access ("invariably they hit a bunch of these roadblocks"). @14:21
- His contrasting approach: "a centralized version of AI and go-to-market." Giving everyone a Claude license leaves "a ton of skills locked in people's individual" instances with no scale. He has "preferred to build with a centralized team" that deploys to the whole rep population. He calls Rutten's harness-enabled business-owner builders "a different version," and questions how builders get qualified or certified. @35:01–36:09 ([[gtm-engineering]], [[ai-sales-stack]])
- Thesis: "If you want to know where go-to-market is going, you just have to look at where product development is today. That's where go-to-market is going to be in 18 months." He maps the engineering "dark factory"/harness/loops conversation to GTM, and names Ramp (with Glass) as the other company he knows building a harness with headless Salesforce and replacing BI with homegrown tools. @55:41–56:42 ([[ai-in-gtm]], [[build-vs-buy-software]])
- Asked where the ROI shows up (pipe, conversion, per-rep efficiency) and whether pipegen per person rose. @56:42, @60:50 ([[metrics-and-forecasting]])
- His own podcast method: he used to send a docket ahead, but guests pre-wrote answers "and those episodes were the worst." Now he refuses to send outlines: 10 minutes of framing, then go. "I do this job every day. So I don't need to do a bunch of research to know what interesting questions to ask." @71:14–72:18 ([[revenue-leadership-podcast]])
- Closing: "I haven't seen a lot of people that have built this level of sophistication... I have a ton of notes that I'm going to be taking back to my team." @75:21–76:23
- Ad read for Granola (code TheRevenue). @38:11

## Guest's core ideas
- AI native is "systems thinking by design from day zero." Individual GPT use helps the person, not the org. It takes a top-down mandate to "throw away the org chart" and rebuild around work. @04:06–06:07 ([[ai-in-gtm]], [[org-design]])
- "You either go all in or you don't go at all." He and the CRO treated GTM (sales, marketing, partners, CS) as one system on one context foundation, which became GTMOS. @06:07–08:10 ([[marketing-alignment]])
- Seeding: in late Q3 last year his CTO pushed him into Claude Code. He gave his marketing leadership and RevOps premium seats with "no target on it, no ROI," and 20–30 people were building within weeks. He halted it after 2–4 weeks because it doesn't scale (data consistency, Salesforce CRUD rights). @11:14–16:21
- GTMOS: an in-house landing zone with enterprise auth, guardrailed and metered connectors (Salesforce, Exa, etc.) and swappable tools. It runs on the Vercel stack (Next.js, AI Gateway with zero-data-retention LLMs, AI SDK, Workflows). Built in Cursor/Claude Code with a GitHub PR → checks → auto-deploy pipeline. "70% to 80% of GTMOS is not LLM-based." "A hundred percent of the GTMOS code is generated." @17:22–26:45, @33:58 ([[build-vs-buy-software]], [[ai-sales-stack]])
- Staffing: one full-time GTM engineer, plus part-time builders (Rutten, the RevOps director, the content-marketing director). The goal is to "make non-engineers dangerous." @26:45–28:48 ([[gtm-engineering]])
- GTM engineering as a standalone function "will become the bottleneck" because engineers don't know the business. Invest instead in a senior "GTM architect" who governs the harness, plus a circle of 5–8 business builders. @32:56–36:09 ([[gtm-engineering]], [[org-design]])
- The RevOps director rebuilt the whole reporting and pipeline cadence natively in GTMOS in three months. "Nobody's in Salesforce anymore." @36:09–37:09 ([[revops]], [[metrics-and-forecasting]])
- Marketing org is collapsing into logical units of work: brand/creative and product marketing (evolving into a customer-facing "go-to-market portfolio" function), plus a single merged digital + content + ABM "demand engine." The BDM role is being "hollowed out" toward strategic account penetration. Desk research is redundant. @09:12–10:13, @42:17–45:25 ([[org-design]], [[marketing-alignment]])
- Outside-in demand gen: scan the 3,000-bank TAM continuously, score against an ICP rubric (strong / moderate / cooling / no fit), research board-level "thematic investments," and campaign to ~30-account thematic clusters, hitting one bank from multiple persona angles. @45:25–52:36 ([[icp-and-saying-no]], [[outbound-at-scale]])
- ICP as an engine: parameters with qualifiers and disqualifiers (e.g., just bought a competitor, or being acquired means out), retuned as the market or product changes (the Casisto acquisition). Solve the hardest problems first (signal engine, ICP engine) before agentic outreach, which "can hurt your brand incredibly fast." @61:54–66:02 ([[icp-and-saying-no]], [[ai-sdrs-and-agents]])
- C-suite tactics: public "love letters" championing a bank's exec team (human-written, AI-researched), and the Banking Reinvented podcast restricted to C-suite guests. @66:02–72:18 ([[marketing-alignment]])

## Key quotes
- Kyle: "as you know, I'm massively AI-pilled and Tim really knows his stuff." @00:00
- Guest: "certain parts are being hollowed out and that is not the career anymore." @10:13
- Guest: "make sure you have a landing zone, a good architecture, really understand how to do this so you can make non-engineers dangerous." @27:47
- Guest: "A hundred percent of the GTMOS code is generated, which already on its own is a crazy fact." @33:58
- Kyle: "It's a different riff on our approach and what I've been espousing, which is a centralized version of AI and go-to-market." @35:01
- Guest: "Nobody's in Salesforce anymore. It took him three months in total." @37:09
- Kyle: "If you want to know where go-to-market is going, you just have to look at where product development is today. That's where go-to-market is going to be in 18 months." @55:41
- Kyle: "I do this job every day. So I don't need to do a bunch of research to know what interesting questions to ask." @72:18

## Numbers & facts
- Backbase: 2,000–2,200 employees. Marketing is "35 FT in total, running a book of business of 350 million and up ARR." @38:11
- Magic number (TTM new ARR ÷ S&M spend): 80 cents per dollar. With ARR valued over five years, "a nice 4x impact." @38:11
- GTMOS: "30 to 40%" of operations automated/rewritten, about six months in. @22:31. "70% to 80%" of it is deterministic, not LLM. @24:35
- Tools cut: one 15K/yr tool last week; 6sense not renewed (replaced by the signal engine built in ~2 months); "at least 100K extra" to cut by year end. @24:35–25:40, @42:17
- Staffing: 1 full-time GTM engineer plus 2–3 part-time builders; target 5–8 builders. @26:45, @36:09
- RevOps reporting rebuild took 3 months. @37:09
- TAM: 3,000 mid-to-large banks, each with a C-suite of 5–8. Weekly scan costs about $500, with a target near $50. Campaigns go to ~30-account clusters. @45:25–48:33, @72:18
- 14 regional ABM managers. One-to-one account plans take 15 minutes (previously "weeks"). Reps can now work ~50 accounts in parallel. QBR prep used to take 2–3 weeks and is now automated. @57:45–60:50
- Love letters: ~40% of executives respond, running ~6 months. @67:04
- Banking Reinvented: called "the fastest growing podcast of 2025" (guest claim). @68:08

## Frameworks & named ideas
- GTMOS / landing zone. GTM architect vs GTM engineer. Five-to-eight business builders ("make non-engineers dangerous"). "All in or not at all." Logical units of work. Outside-in demand gen with thematic clusters. ICP engine (qualifiers, disqualifiers, dissatisfiers). Engagement matrix (engagement × opportunity stage). White-box signal engine. Love letters. Podcast-as-ABM. Tiago Forte's second brain (projects + areas).
- Kyle: "co-pilots are table stakes." Centralized AI-in-GTM team (his model) vs harness-enabled builders. "GTM is where product development was, 18 months later." The dark-factory analogy. No-docket podcast prep.

## Concepts & entities
[[kyle-norton]] · [[owner-com]] · [[revenue-leadership-podcast]] · [[person-tim-rutten]] · [[ai-in-gtm]] · [[gtm-engineering]] · [[build-vs-buy-software]] · [[ai-sales-stack]] · [[org-design]] · [[marketing-alignment]] · [[icp-and-saying-no]] · [[revops]] · [[metrics-and-forecasting]] · [[ai-sdrs-and-agents]] · [[outbound-at-scale]] · [[career-and-leadership]]
