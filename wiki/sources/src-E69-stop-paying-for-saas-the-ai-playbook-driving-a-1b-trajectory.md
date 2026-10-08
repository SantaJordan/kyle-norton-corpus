---
slug: src-E69-stop-paying-for-saas-the-ai-playbook-driving-a-1b-trajectory
type: source
lifecycle: validated
valid_from: 2026-05-13
invalid_at: null
superseded_by: null
sources: [raw/podcasts/own-show/E69-stop-paying-for-saas-the-ai-playbook-driving-a-1b-trajectory/transcript.md]
links: [kyle-norton, owner-com, revenue-leadership-podcast, person-ghazi-masood, saastr, build-vs-buy-software, ai-sales-stack, ai-in-gtm, gtm-engineering, revops, org-design, sales-hiring, hiring-scorecards, talent-density, comp-plans, ai-sdrs-and-agents, sales-coaching-and-enablement, cro-role-and-board, career-and-leadership]
tags: [own-show, host, replit, build-vs-buy, salesforce-headless, vibe-coding, non-traditional-hires, 15-minute-screen, 80-percent-bar, quotas-only-go-up, xdr-hiring-analysis, auto-research, openclaw, youtube-channel-move, scale-down]
---

# E69: Stop Paying For SaaS: The AI Playbook Driving A $1B Trajectory

**Show:** The Revenue Leadership Podcast · **Guest:** Ghazi Masood, CRO @ Replit (ex-Auth0, CRO at Retool; transcript spells "Massoud"/"Repl.it") · **Published:** 2026-05-13 · **Kyle's role:** host · **Raw:** `raw/podcasts/own-show/E69-stop-paying-for-saas-the-ai-playbook-driving-a-1b-trajectory/transcript.md`

**Attribution note.** No speaker labels. Below, a line counts as Kyle's only when it's his PSA, intro or question, it's first-person about Owner/OpenClaw/his hiring analysis, or the guest's reply makes the switch clear. Replit facts, the hiring process and the org design are Ghazi's. Lines marked *inferred Kyle* are very likely his but not airtight.

## TL;DR
- Replit grew from $2M to $150M+ in under a year and is tracking to a $1B run rate by end-2026. It keeps Salesforce as system of record (migrating off HubSpot) and vibe-codes everything on top: revenue copilot, "Repl.it book" (Gainsight-like health), CPQ/quote-to-cash, and forecasting. Kyle agrees: "we're not going to go vibe code Salesforce".
- Kyle pushes for a **build-vs-buy heuristic**: buy what's central, integration-heavy, governance/security-critical, or where downtime takes the team offline (dialers). Build peripheral tools (Owner rebuilt its LMS and a contest/recognition system). Weigh the incremental benefit over today's tool.
- Ghazi hires for mission and AI passion over pedigree (an ex-Marine and a school teacher became top sellers), with 15-minute CRO screens, mock panels and an "80% bar". Kyle shares his Claude-built XDR hiring analysis and bar-raiser copilot.

## What Kyle said
- **PSA:** the show moved to a new YouTube channel, youtube.com/@Kyle-Norton ("Kyle Norton, the Revenue Leadership Podcast"). Audio stays on Spotify, Apple and others @00:00–02:03. [[revenue-leadership-podcast]]
- Replit "was actually the first vibe coding experience I had ever used" via a "100 days of code course in like 2022" @02:03. [[career-and-leadership]]
- Quipped that Replit is "low-code, no-code on super steroids" @04:04.
- *Inferred Kyle:* "People don't send a dashboard or a spreadsheet anymore. Any spreadsheet is now an interactive web app." Many experiences he engages with are internally built @05:06–06:11 (Ghazi: "I am the perfect use case for that"). [[build-vs-buy-software]] [[ai-in-gtm]]
- He has "organically learned" to build his own automations but lacks clean principles for context engineering. He asked for advice for non-technical CROs, noting outputs often get "90 percent there" @07:13–08:16. [[ai-in-gtm]]
- His setup: "a context file that's local and in GitHub so that my open clock [OpenClaw] can get at it", covering business objectives and "how I decision make and problem solve", so it can be "the most effective AI chief of staff" @13:22–14:25. [[ai-sales-stack]] [[playbooks-and-documentation]]
- Wonders if he "overcooked" his setup: OpenClaw "in this like digital ocean droplet". It's "probably overbuilt because I wanted it early", and he "could get most of what I've been able to build" in a tool like Replit or Claude's @15:28. [[build-vs-buy-software]]
- Context: a handful of companies (Anthropic, OpenAI, Replit) are growing "like 50 X year over year, like 10 X year over year" at multi-hundred-million run rates @16:30–17:31. [[fundraising-and-investability]]
- On ARR per employee: "It says only 461 employees on LinkedIn" @28:53. [[metrics-and-forecasting]]
- "It's a law of startup physics. Quotas only go up... It's like gravity." If quotas start going down, "that's when you got to work" @29:55. [[comp-plans]]
- **Systems of record:** "we're not going to go vibe code Salesforce". Core systems that manage "governance and ecosystem and, uh, security" are "best bought". He sees Salesforce's headless/"Salesforce 360" direction matching Replit's approach @31:58–33:00. [[build-vs-buy-software]] [[revops]]
- **Build-vs-buy heuristics he proposes:** integrations and "centrality of the tool", and "Governance and security". Plus a downtime test: "should we vibe code sales loft?... I don't think we would vibe code a calling tool. Like you could vibe code your own thing and just API into Twilio. But like, what's sort of the point if that goes down at like your whole team is offline." He plans to talk about this at SaaStr @37:13–38:16. [[build-vs-buy-software]] [[ai-sales-stack]]
- Owner built **its own LMS** and "a recognition and a contest system" because they're "not that connected, they're not that central". If one goes down for a couple of hours, "you're not totally losing your mind" @38:16. [[build-vs-buy-software]] [[sales-coaching-and-enablement]]
- Adds **cost-benefit**: "what is the incremental benefit above the quality of the tool today that you unlock by doing it yourself?" ("how much better are you going to make a dialer?") @39:17. [[build-vs-buy-software]]
- Replit re-platforming to Salesforce "sort of confirms my prior": the CRM is a "hub and connection point" you don't live in @39:17. [[build-vs-buy-software]]
- Owner: "I at least have a bunch of people that have been with me three years now as we're, we're probably gonna hire like a hundred people in sales this year" @41:20. [[sales-hiring]] [[talent-density]]
- Summarized Ghazi's approach as "traits based decisions and then teaching a lot of the craft and specific knowledge" @45:28. [[sales-hiring]] [[hiring-scorecards]]
- **XDR hiring analysis** ("a few weekends ago"): pulled all Ashby scorecards, MetaView interview recordings, and in-role performance from Owner's BI tool, then had Claude analyze common traits and "who's good at identifying talent". The goal is a copilot that scores each candidate's likelihood of success. Kyle is the final "bar raiser" (a 30-minute interview for all market-facing roles). He runs it from a terminal tab and it writes a Notion page. Across "maybe five bar raisers" it has "been aligned with all of the recommendations". When unsure, he ran Karpathy's auto-research repo for about 45 minutes and it was "way better after then" @46:30–49:34. [[hiring-scorecards]] [[sales-hiring]] [[ai-in-gtm]]
- Founders building AI hiring tools felt "a little thin and a little like AI slop". You need deep in-role performance data, and he needs years to validate the scores @49:34. [[hiring-scorecards]]
- RevOps, GTM engineering, applied AI, data and BizOps "overlap so much now". With low technical barriers, "who owns that today is, is a big question" @55:47–56:48. [[org-design]] [[revops]] [[gtm-engineering]]
- "it seems insane now to think about how much time people spent building a lead list to call and updating their next steps" @58:57. [[ai-sales-stack]]
- *Inferred Kyle:* scaling down matters more now because you "can't rely on... working a couple of deals when you were a manager 18 months ago" @61:03. [[cro-role-and-board]]
- On vetting the CEO before joining: "You only need to learn that less, less than once" @63:05. [[career-and-leadership]]

## Guest's core ideas
- Mission: "democratizing software creation". The next billion builders sit outside engineering. "low-code, no-code is dead" without an AI pivot. He left Retool partly because it "could not pivot to AI fast enough" @04:04–05:06. [[ai-in-gtm]]
- He builds his own decks in Replit from his phone and ran the annual kickoff that way, with no enablement team needed @06:11–07:13. [[ai-in-gtm]]
- **Buy the system of record, build on top:** HubSpot → Salesforce. Built in Replit: a revenue copilot (funnel through closed-won, with Gong calls pulled in), "Repl.it book" (customer health, a Gainsight replacement, built by a field engineer in "less than a day"), CPQ/quote-to-cash/order forms, and Clari-like forecasting. Buys Nooks for the dialer. Big enterprises won't vibe-code ERP/CRM, though SMB customers vibe-code CRM, HCM and onboarding @08:16–37:13. [[build-vs-buy-software]] [[ai-sales-stack]]
- Hyper-growth CRO is hands-on: he does all first screens, opens London/EU, and runs a series of "very first time" rollouts (territories, comp plans, forecasting, post-sales) @17:31–19:34. [[cro-role-and-board]]
- **Hiring profile:** "We're not going to go automate salespeople". He optimizes for AI/mission passion over top-1% Oracle/Salesforce pedigree. The top seller was an ex-US Marine, and a top commercial seller was a school teacher. AEs carry demos to 80–90% without SEs, and great reps become the customer's "AI advocate" @19:34–24:43. [[sales-hiring]] [[talent-density]]
- **Process:** 15-minute CRO screens (down from 30) testing communication and a 0–10 AI self-ranking, then a role-specific mock-panel prompt with three panelists, then hire/no-hire. An explicit "80% bar" filled by enablement (onboarding in Foster City, role tracks run by Yo-Yo) @27:51–46:30. [[sales-hiring]] [[hiring-scorecards]] [[sales-coaching-and-enablement]]
- **Org:** GTM is about 60 people. 90% of pipeline was inbound. He's building outbound BDRs in Salt Lake City and plans fully agent-run inbound by end of Q2. Commercial (<2,000 employees) vs. enterprise AEs. No CSMs: "Repl.it customer advocates" plus forward-deployed field engineers. RevOps covers systems, deal desk, a generalist ops role and a planned AI GTM engineer. Data sits in product and BizOps in finance @25:44–56:48. [[org-design]] [[revops]] [[ai-sdrs-and-agents]]
- Quotas started only in January with half-year plans. Everyone is "smashing their quota", so H2 quotas go up. The first thing to break was RevOps (territories, comp, seat→usage pricing, CRM migration), not deal velocity @28:53–31:58. [[comp-plans]] [[revops]]
- Fully automated SDRs "didn't really work for us" (at his last company). Inbound can be automated. He's testing **self-serve Enterprise** for sub-$20–25K deals, which may shift the mix toward enterprise sellers @52:37–54:45. [[ai-sdrs-and-agents]] [[smb-sales-motion]]
- Agents won't just buy from agents. Complex regulated deals need humans, and AI frees reps from "back office crap" @57:54–58:57. [[ai-in-gtm]]
- Great CROs: customer-first, lead by example, own the whole lifecycle. Advice: leaders must be able to "scale down". Hardest lesson: back-channel the CEO/founder @60:00–63:05. [[cro-role-and-board]] [[career-and-leadership]]

## Key quotes
- "It was actually the first vibe coding experience I had ever used" (Kyle) @02:03
- "The big behemoth question is, hey, are we building our own CRM? No, we're not." (guest, cold open) @00:00
- "We're not going to go automate salespeople, right?" (guest) @19:34
- "It's a law of startup physics. Quotas only go up." (Kyle) @29:55
- "we're not going to go vibe code Salesforce" (Kyle) @31:58
- "I don't think we would vibe code a calling tool." (Kyle) @37:13
- "what is the incremental benefit above the quality of the tool today that you unlock by doing it yourself?" (Kyle) @39:17
- "we want an 80% bar." (guest) @43:26

## Numbers & facts
- Replit: revenue "$2 million to over $150 million in less than a year", tracking to "a billion-dollar run rate by the end of 2026", hiring "200-plus people over the next 12 months" (Kyle's intro) @02:03.
- Kyle: "only 461 employees on LinkedIn" @28:53.
- Guest: nearly three decades in GTM @03:04. Previous org of 300 people @17:31. GTM all-up "right around 60 ish" @25:44. 90% of pipeline inbound at arrival @25:44. Inbound automated "by the end of Q2" @25:44. Commercial <2,000 employees, enterprise >2,000 @26:47. Quotas since January, half-year plans @28:53. Screens cut from 30 to 15 minutes @41:20. 3-person mock panel @42:24. 80% bar @43:26. AEs take deals to "80, 90%" without SE @20:38–21:39. Self-serve Enterprise for "sub 20K, 25K" @53:45. Replit Book built in "less than a day" @34:04. Agent 4 is the current release @14:25. Flying 26 years (Angel Flight West) @63:05. Started at Replit officially in December @50:35.
- Kyle/Owner: ~100 sales hires "this year" @41:20. XDR analysis aligned on "maybe five" bar raisers. Auto-research ran about 45 minutes @48:32.

## Frameworks & named ideas
- **Buy the system of record, build the workflow layer** (guest; Kyle concurs). **Headless CRM** (Kyle).
- **Kyle's build-vs-buy tests:** centrality/integrations, governance/security, downtime blast radius (dialer/Twilio), incremental benefit over the incumbent tool. Build peripheral tools (LMS, contests).
- **Traits over pedigree + an 80% bar backed by enablement** (guest). **AI advocate** rep (guest).
- **Quotas only go up / law of startup physics** (Kyle, echoing [[src-E68-are-you-uninvestable-the-new-gtm-reality]]).
- **AI hiring copilot / bar-raiser second opinion** with Karpathy auto-research (Kyle).
- **Scale down** (guest's leadership advice).
- **Self-serve Enterprise** experiment (guest).

## Related sources
- [[src-substack-2026-05-17-stop-paying-for-saas-the-ai-playbook]]: Kyle's companion post (capacity creation, "AI makes bad infrastructure louder", RevOps-as-product).
- [[src-E68-are-you-uninvestable-the-new-gtm-reality]] (same XDR hiring analysis, quotas-only-go-up). [[src-E65-inside-our-ai-sales-stack-kyle-norton]] (Owner considering ripping out Salesloft).

## Concepts & entities
- [[kyle-norton]] · [[owner-com]] · [[revenue-leadership-podcast]] · [[person-ghazi-masood]] · [[saastr]]
- [[build-vs-buy-software]] · [[ai-sales-stack]] · [[ai-in-gtm]] · [[gtm-engineering]] · [[revops]] · [[org-design]]
- [[sales-hiring]] · [[hiring-scorecards]] · [[talent-density]] · [[comp-plans]] · [[ai-sdrs-and-agents]] · [[smb-sales-motion]]
- [[sales-coaching-and-enablement]] · [[playbooks-and-documentation]] · [[metrics-and-forecasting]] · [[cro-role-and-board]] · [[career-and-leadership]] · [[fundraising-and-investability]]
