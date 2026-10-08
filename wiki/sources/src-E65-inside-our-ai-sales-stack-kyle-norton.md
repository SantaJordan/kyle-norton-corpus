---
slug: src-E65-inside-our-ai-sales-stack-kyle-norton
type: source
lifecycle: validated
valid_from: 2026-03-25
invalid_at: null
superseded_by: null
sources: [raw/podcasts/own-show/E65-inside-our-ai-sales-stack-kyle-norton/transcript.md]
links: [kyle-norton, owner-com, revenue-leadership-podcast, clay, person-everett-berry, ai-sales-stack, ai-in-gtm, gtm-engineering, ai-sdrs-and-agents, outbound-at-scale, smb-sales-motion, build-vs-buy-software, org-design, revops, sales-coaching-and-enablement, playbooks-and-documentation, metrics-and-forecasting, career-and-leadership, sales-hiring]
tags: [own-show, interviewed, clay-cro-summit, ai-pre-call-research, pcrios, econnect, local-name-drop, applied-ai, experimentation, waterfall-enrichment, personal-brand, writing-skills, podcast-workflow, momentum, salesloft]
---

# E65: Inside Our AI Sales Stack - Kyle Norton | CRO @ Owner.com

**Show:** The Revenue Leadership Podcast · **Guest:** Kyle Norton himself, interviewed by Everett Berry (Clay's head of GTM engineering; transcript spells "Everett Barry") at the closed-door Clay CRO Summit · **Published:** 2026-03-25 · **Kyle's role:** interviewed · **Raw:** `raw/podcasts/own-show/E65-inside-our-ai-sales-stack-kyle-norton/transcript.md`

**Attribution note.** A narrator intro (@00:00) frames the episode; Everett asks the questions and introduces it as "part three of Kyle and I's podcast series on GTM engineering" @01:00. Audience members (including "Stevie", surname not given) ask questions at the end. Everything below under "What Kyle said" is Kyle answering. The transcript is short (~30 min) and the speaker turns are clear.

## TL;DR
- Owner points almost all its AI effort at **pipeline generation** ("RGAs over everything"). ML scoring (deal size, win rate, eConnect pick-up likelihood) feeds AI pre-call research. The research sits inside Salesloft and fills a rigid cold-call script (PCRIOS). Email is centralized. BDRs now make 150–200 dials a day and reach 20–30 decision makers, about 5x where they started.
- Experiments run through a small central team: the VP RevOps, VP Data/BizOps, Kyle, and the applied AI lead "YG". A pilot uses 2–3 reps plus one manager, with tracking set up in advance. Winners must be statistically significant before they become an enablement ticket. Kyle prefers deterministic flows over "an agent at every single step".
- Kyle's own leverage stack: writing "skills" built from a 150-page doc of his posts, a Clay table that researches podcast guests and drafts the docket, and a transcript-to-newsletter-to-LinkedIn pipeline with human choice points. If he restarted, he'd use Clay instead of internally built waterfall enrichment, and he'd stop pushing managers to learn AI.

## What Kyle said
- Slogan "RGAs over everything" (revenue-generating activities). He ran his first time-series study of rep time 10–12 years ago, and his early fix was Salesforce reports with trigger words that he screenshotted as "don't call these" @02:01. [[ai-in-gtm]] [[metrics-and-forecasting]]
- "Most of our AI efforts" go to pipeline generation: "if you can just generate way more pipeline, everything else gets better", and pipeline is easier to move than conversion rates @02:01–03:02. [[ai-in-gtm]] [[outbound-at-scale]]
- Top-of-funnel ML scores estimate how big the deal will be and the win rate. **eConnect** predicts whether the person will pick up, which produced a 2.3x lift in decision-maker connects @03:02. [[ai-sales-stack]] [[revops]]
- The pipeline is scoring, then enrichment, then **AI pre-call research (AI PCR)** that delivers "on a platter" what the rep should say. The cold-call structure is rigid @03:02. [[ai-sales-stack]] [[playbooks-and-documentation]]
- **PCRIOS** ("Pocrios, the Greek goddess of cold calling"): pattern interrupt, credibility, relevance, intrigue, offer of value, steps @03:02. [[playbooks-and-documentation]] [[outbound-at-scale]]
- Pattern interrupt = **local name drop**. For each prospect, Owner takes the zip code, finds the nearest customer, and enriches that into a Salesforce field. The rep opens with "I actually work with Stevie's Pizza over on Fifth Street" @04:06. [[smb-sales-motion]]
- AI PCR is a window Owner injected into the Salesloft UI. They're "thinking about ripping out sales loft and building natively on top of Salesforce" @04:06. [[build-vs-buy-software]] [[ai-sales-stack]]
- The "I noticed" line is the second personalized element. A workflow pulls in the prospect's whole digital presence and ranks "what is the thing that's most broken" (e.g. off-domain online ordering hurting search rank). That creates the intrigue @04:06–05:11. [[ai-sales-stack]] [[smb-sales-motion]]
- Follow-up workflows and "sell between" automation (send videos, AI cold email) run between the call and the meeting. All emailing is moving off BDRs/SDRs to a central team, and BDRs are told which leads to call based on central orchestration @05:11. [[ai-sdrs-and-agents]] [[gtm-engineering]]
- BDRs make 150–200 calls a day and talk to 20–30 decision makers, "probably 5X" the original level @05:11–06:12. [[outbound-at-scale]]
- **Experimentation, early phase:** "just me and the VP of BizOps and data cooking up weird stuff" and they'd "YOLO it to the whole entire team" @06:12. **Now:** Kyle, the VP RevOps, the VP Data, and the applied AI leader brainstorm "where is the most lift" about once a month, and they "know the next six things" @06:12–07:18. [[gtm-engineering]] [[org-design]]
- They want more ideas coming up from the team because "we're very centralized right now" @07:18. [[gtm-engineering]]
- **Pilot mechanics:** YG (applied AI lead, based in New York) builds a prototype and flies to Toronto for three days to sit beside the team. The pilot uses 2–3 reps plus one manager, and it's their only non-quota project at a time. The data team sets up tracking in advance. The manager runs the cadence and writes a daily update. If the result is a stat-sig winner, it becomes an enablement ticket and gets rolled out @07:18–08:20. [[sales-coaching-and-enablement]] [[gtm-engineering]]
- Current pilot: **time shift**. Four reps start at 10 a.m. instead of 8 a.m. because data shows the best call window is 5:00–6:30 @07:18. [[outbound-at-scale]]
- **Org:** YG reports to the VP of Data in BizOps, not to Kyle, though it was Kyle's headcount. It was the first headcount he added after the Series C, inspired by Stevie's applied AI team. The rule is sales-only work for the first 12 months. There's a separate applied AI leader for growth marketing. The team is mostly data science/data engineering plus applied AI, and everyone must be "massively AI-pilled" @08:20–09:28. [[org-design]] [[gtm-engineering]]
- On fully automating SMB sales: "If you can, you should." PLG is already that, but Owner's mom-and-pop buyers struggle to get on a Google Meet, so its agentic bottom-of-market experience has had "mediocre success so far". Technical buyers "would rather talk to a robot" @09:28–10:32. [[smb-sales-motion]] [[ai-sdrs-and-agents]]
- ACV is one input to unit economics. "if your ACV is 10k and you're closing at 80%, that's way better than if you were at 12k closing at 40%" @10:32–11:38. [[metrics-and-forecasting]]
- He's looking at LATAM reps for the bottom of the market (transcript: "a core of the cost of our North American reps", probably a mis-transcription). An earlier attempt to hire LATAM sales talent "was really tough", so the launch team is another option @11:38. [[sales-hiring]] [[org-design]]
- AI is often "a hammer looking for a nail". Start from the business problem. Use AI where you must ingest data and make a non-deterministic reasoned decision, or for pattern recognition. Otherwise use deterministic flows, because an agent at every step "leads to sloppy outputs" @11:38–12:43. [[ai-in-gtm]] [[ai-sdrs-and-agents]]
- Pushes back on Everett's idea that GTM collapses into two roles (GTM engineers plus reps), calling it "a little reductive". Owner calls the role "applied AI" ("Some people say GTME, like tomato, tomato"). He wants many more of them, and they're hiring "as fast as we can" @13:45. [[gtm-engineering]] [[org-design]]
- Argues for **more specialization**, not less: unbundle the job description into discrete tasks, move them to agents, workflows or a central team, and what's left is a highly specialized role. "There is no way that any of my AEs could cold call the way my BDRs call now." He sees convergence at the leadership level, not on the front line @13:45–14:50. [[org-design]] [[outbound-at-scale]]
- **Personal brand:** semi-purposeful, inspired by Naval Ravikant (compounding assets) and Seth Godin. The purpose was "always recruiting to start." Owner has never used outsourced recruiters or done outbound recruiting. "Kyle writes a LinkedIn post and then 1,600 people apply", saving "hundreds and hundreds of thousands of dollars." He doesn't monetize the brand for Owner because customers aren't on LinkedIn. His advice: do it only if you're excited about it @15:54–18:02. [[career-and-leadership]] [[sales-hiring]]
- **Writing skills:** he fed a 150-page Google Doc of every LinkedIn post into a meta-prompt that wrote a prompt, which then produced a detailed style description. He now has newsletter, LinkedIn and email skills. The email skill says "never say hello. Only write one line" @18:02–19:03. [[ai-in-gtm]] [[career-and-leadership]]
- **Podcast workflow:** a Superhuman invite template leads to a Tally intake form (LinkedIn, topics, contrarian views). That feeds a Clay table where every column is a research prompt: everything the guest has said online, then themes and what's unique, then leadership vs. systems-building views. Kyle picks three topics by hand, and the last column writes the docket (research, summary, intro, questions). He spends 10–15 minutes editing the questions @19:03–21:10. [[clay]] [[ai-in-gtm]]
- The transcript goes into the newsletter writer, which carries the Wikipedia "AI Writing Giveaways" list (em dash, "it's not just this, it's that") in its style file. He now only does "a light edit", then it writes a LinkedIn post @21:10. [[playbooks-and-documentation]]
- **Human checkpoints matter:** the newsletter skill offers 5 hook options, then 10 stack-ranked takeaways that he edits (e.g. "I don't like three, use seven"), and then it "basically one-shots the output" @22:12. [[ai-in-gtm]]
- **Personal OS:** he has workflows for anything repeated, and the weekly update is an AI workflow (context handling is "the thing that I'm still figuring out"). He records the podcast for 90 minutes and spends another 30–45 per week. He learns after the kids sleep with an AirPod in, watching YouTube/Twitter @23:14. [[executive-performance-and-mindset]]
- Starting cold today means you "basically waste 20 hours building a vibe-coded app that never really works" to build "taste and an intuition". Learning make.com was "sort of a waste" but taught him decomposition. In Claude Code he "yap[s] away" and asks for a PRD @24:19–25:25. [[gtm-engineering]] [[career-and-leadership]]
- Leaders need enough understanding to design the system but probably don't need "Cloud Code Terminal and have a GitHub repo"; "where the line is, I'm not totally sure yet" @25:25–26:26. [[cro-role-and-board]]
- **Start-over answer 1:** Owner built waterfall enrichment in late 2022 "before clay was a thing". Today he'd "just use clay", because only two people can operate the internal system and RevOps and his BDR leader can't. Clay would democratize access (though not down to reps). Foundations: "first party and third party data" @26:26–27:29. [[clay]] [[build-vs-buy-software]] [[revops]]
- **Start-over answer 2:** he pushed managers too hard on AI (two ~six-hour Andrej Karpathy videos as "required watching by Monday", a big AI memo like Toby's and Duolingo's). Managers just need to know which problems to solve, and the applied AI team solves them. He'd keep them on "hiring, coaching, managing to the number." "I've changed my stance there" @27:29. [[sales-coaching-and-enablement]] [[org-design]]
- Learning tip: ask Claude to break the problem down and "explain what we're doing as we go" (e.g. why Vercel or Supabase). That now teaches him more than YouTube @28:29–29:34. [[career-and-leadership]]

## Key quotes
- "We have this slogan, RGAs over everything." (Kyle) @02:01
- "It's much easier to generate pipeline than it is to move conversion" [rates] (Kyle) @02:01
- "which led to a 2.3x lift in decision-maker connects" (Kyle, on eConnect) @03:02
- "My BDRs make 150 to 200 calls a day" (Kyle) @05:11
- "You don't need an agent at every single step of the way. Oftentimes, that leads to sloppy outputs." (Kyle) @12:43
- "There is no way that any of my AEs could cold call the way my BDRs call now." (Kyle) @14:50
- "Kyle writes a LinkedIn post and then 1,600 people apply" (Kyle) @16:59
- "I would just use clay" (Kyle) @26:26

## Numbers & facts
- eConnect: "2.3x lift in decision-maker connects" @03:02.
- BDR output: 150–200 calls a day, 20–30 decision-maker conversations, "probably 5X" the starting level @05:11–06:12.
- Experiment planning about monthly, with a visible queue of "the next six things" @06:12–07:18.
- Pilot size: 2–3 reps plus 1 manager. The time-shift pilot moves 4 reps from an 8 a.m. to a 10 a.m. start, and the best call window is "5 o'clock to 6.30" @07:18.
- Applied AI lead: first headcount after the **Series C**, sales-only for the first 12 months. Based in New York, while the sales team is in Toronto @07:18–08:20.
- First rep-time study 10–12 years ago @02:01.
- ACV illustration: 10k at 80% close beats 12k at 40% @11:38.
- Recruiting: "1,600 people apply" to a post, saving "hundreds and hundreds of thousands of dollars" @16:59.
- Writing corpus: a 150-page Google Doc @18:02–19:03.
- Podcast time: 90 minutes recording plus 30–45 minutes per week. Question editing takes 10–15 minutes @20:04, @23:14.
- Waterfall enrichment built in late 2022, and only two people can operate it @26:26.
- Karpathy videos "like six hours long" @27:29.
- Learning curve: "waste 20 hours building a vibe-coded app" @24:19.

## Frameworks & named ideas
- **RGAs over everything** (revenue-generating activities).
- **Pipeline-first AI**: put AI at pipe gen before conversion.
- **Funnel stack**: ML scoring (deal size, win rate, **eConnect**), then enrichment, then **AI PCR**, then a rigid script, then central follow-up/"sell between" automation, then centrally orchestrated call lists.
- **PCRIOS cold-call structure** (pattern interrupt, credibility, relevance, intrigue, offer of value, steps), with the **local name drop** and the **"I noticed"** line as the personalized parts.
- **Pilot → stat sig → enablement ticket** experimentation loop.
- **Applied AI ≈ GTME** ("tomato, tomato"), housed under Data/BizOps.
- **Unbundle the JD** → more specialization on the front line, convergence at leadership level.
- **Deterministic first, AI where reasoning or pattern recognition is needed.**
- **Human-in-the-loop checkpoints** (pick 3 topics, pick hook, pick takeaways).
- **Personal brand as recruiting engine** (Naval's compounding assets).
- **Ask the model to teach you as it builds.**

### Tools named
Salesforce (system of record), Salesloft (dialer/sequence UI, may be ripped out), Momentum (sponsor read: "we ripped out Gong", writes back to Salesforce @01:00), internal waterfall enrichment (2022), Clay (podcast research table, recommended for enrichment), Superhuman, Tally, Google Docs, make.com (abandoned), Claude/Claude Code (PRDs), Vercel/Supabase (as examples).

## Related sources
- Same people, same theme: [[src-kyle-nortons-bets-for-gtm-domination]] (data-first GTM AI, deterministic constraints, personal brand for recruiting).
- Later companions that refer back to the centralized model: [[src-substack-2026-04-30-your-buyers-ai-is-pitching-your-product]], [[src-substack-2026-05-13-are-you-uninvestable-cassie-young]].

## Concepts & entities
- [[kyle-norton]] · [[owner-com]] · [[revenue-leadership-podcast]] · [[clay]] · [[person-everett-berry]]
- [[ai-sales-stack]] · [[ai-in-gtm]] · [[gtm-engineering]] · [[ai-sdrs-and-agents]] · [[outbound-at-scale]] · [[smb-sales-motion]]
- [[build-vs-buy-software]] · [[org-design]] · [[revops]] · [[sales-coaching-and-enablement]] · [[playbooks-and-documentation]]
- [[metrics-and-forecasting]] · [[sales-hiring]] · [[career-and-leadership]] · [[executive-performance-and-mindset]] · [[cro-role-and-board]]
