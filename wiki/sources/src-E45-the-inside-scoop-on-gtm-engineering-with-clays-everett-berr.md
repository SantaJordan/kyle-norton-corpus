---
slug: src-E45-the-inside-scoop-on-gtm-engineering-with-clays-everett-berr
type: source
lifecycle: validated
valid_from: 2025-09-03
invalid_at: null
superseded_by: null
sources: [raw/podcasts/own-show/E45-the-inside-scoop-on-gtm-engineering-with-clays-everett-berr/transcript.md]
links: [kyle-norton, owner-com, shopify, clay, momentum, revenue-leadership-podcast, person-everett-berry, person-jason-lemkin, gtm-engineering, ai-in-gtm, ai-sdrs-and-agents, ai-sophistication-ladder, context-harness-and-memory, revops, org-design, outbound-at-scale, icp-and-saying-no, build-vs-buy-software, ai-sales-stack, personal-ai-stack, point-of-view-positioning, sales-hiring, career-and-leadership]
tags: [own-show, clay, gtm-engineering, forward-deployed-engineers, data-quality, snowflake, lossiness, ai-sdr, account-scoring, gtme-org-placement]
---

# E45: The Inside Scoop on GTM Engineering with Clay's Everett Berry
**Show:** The Revenue Leadership Podcast · **Guest:** Everett Berry, head of GTM engineering @ Clay (transcript: "Everert Barry") · **Published:** 2025-09-03 · **Kyle's role:** host · **Raw:** `raw/podcasts/own-show/E45-the-inside-scoop-on-gtm-engineering-with-clays-everett-berr/transcript.md`

## TL;DR
- Clay runs its sales team as forward-deployed GTM engineers who scope and implement Clay inside customers. Berry says that fits a consumption, no-code product for ops and expert users.
- Why AI pilots fail: AI SDRs get too much end-to-end scope and miss hidden context, AI gets put in feedback loops a human should own, and chained prompts compound "confidently wrong" outputs. Kyle calls the compounding "lossiness".
- Kyle's thesis, which Berry shares: do the boring data work first. At Owner, Snowflake (not Salesforce) is the system of record, the data team owns GTM data, and Kyle says Owner is talking to Clay about "converging on Clay".

## What Kyle said
- Shopify once called its reps "sales hackers". It "was cute and funny for a while and then we're like, let's just call them account executives." He compared Clay's model to Palantir's embedded engineers. @06:07 ([[shopify]], [[gtm-engineering]])
- Unsure whether AI will make reps more expert or more relationship-driven: "I don't have a strong sense on where we're going." Owner is "automating as much of the grunt work as humanly possible um through a set of different tools." @09:10 ([[ai-in-gtm]], [[ai-sales-stack]])
- He called the MIT "95% of AI deployments" study a selective sample and "clickbaity". Both Owner and Clay are examples of getting "tremendous amount of value" from AI. @10:11–11:12 ([[ai-in-gtm]])
- Lossiness (from his "half-written Substack post"): problems that are too broad, chained prompts or agents with no human in the loop or deterministic check, and slight hallucination at each step add up to "slop". @16:17–18:20 ([[context-harness-and-memory]], [[ai-sdrs-and-agents]])
- Owner positioning: Owner is "so thoughtful" about its positioning language, so he would never let a tool generate a target-account plan from a domain. He wants to put the positioning, banned words and tone into the prompt ("this is the context engineering thing"). @18:20–19:21 ([[point-of-view-positioning]], [[context-harness-and-memory]])
- His own Clay use: guests fill in a Tally intake form, which webhooks into "my personal clay research table". Agents summarize the guest's background and content, then add his questions. Getting the output right took many rounds of prompt rewriting, and "trial and error" felt "silly". @22:24–23:27 ([[personal-ai-stack]], [[clay]])
- An AI-lead candidate he interviewed described a "mouth feel" for where each model is strong. Kyle also prefers Anthropic models for writing ("Yeah, same."). @23:27, @25:29 ([[personal-ai-stack]], [[sales-hiring]])
- He framed AI foundations as infrastructure, people and strategy. @27:31
- Advice he gives "the most most commonly" is to start with data quality and get buy-in from the data team. A 6sense example (Snowflake to Clay) is "not really the realm of revops anymore". People skip to "carpet bombing their market with AISR" when they should "spend four to six months" fixing baseline data quality. @34:42–35:42 ([[revops]], [[ai-sdrs-and-agents]])
- GTM25 talk thesis, "do the boring stuff first": first-party data via [[momentum]] and third-party data via [[clay]]. On Owner: "we built a bunch of this in-house because it was before Clay like exploded" and is now talking to Clay's team about "converging on Clay". He says the two products are "like 80% of your AI roadmap". @37:44–38:47 ([[build-vs-buy-software]], [[ai-sales-stack]])
- Owner data: Owner has hundreds of thousands of target accounts, so GTM data is "fairly exclusively" the data team's job. "our system of record is Snowflake not Salesforce". Owner pushes into Salesforce, but scoring is built on Snowflake. @43:52–44:54 ([[revops]], [[owner-com]])
- Asked whether a GTME should report "direct into the CRO or through RevOps", when to hire one ("5 million AR, 10 million AR?"), and suggested you could have several GTMEs across the CMO's team and RevOps. @46:57, @50:02–51:02 ([[org-design]], [[gtm-engineering]])
- "You're eating glass." He connected this to his last episode with "Dr. Michael Derase" on purpose-driven leadership. @64:17 ([[career-and-leadership]])

## Guest's core ideas
- Forward-deployed model: 30 people and five GTM-engineering teams. A sales leader is joining. Internal GTMEs build Clay's own pipeline systems. @04:03–07:08 ([[gtm-engineering]], [[clay]])
- Future reps are experts "surrounded by automation". Clay already automates pre-call research, follow-up and Salesforce stage updates. He contrasts this with [[person-jason-lemkin]]'s companion-SE vision. @07:08–10:11 ([[ai-in-gtm]])
- AI SDRs fail when they are handed a broad ICP and an account list without the hidden context SDRs learn, for example targeting backend/DevOps engineering leaders. Keep humans on the feedback loop for messaging. @11:12–16:17 ([[ai-sdrs-and-agents]])
- Break up prompts and gut-check web-agent output against database data (for example, Clearbit revenue). Read the metaprompter's output before trusting it. Starter task: classify CRM industries with ChatGPT, and write copy with Anthropic. @19:21–25:29 ([[context-harness-and-memory]])
- CRO order of operations: (1) put AI licenses in everyone's hands, (2) centralize what the best reps build through GTMEs and orchestration (metric: leads worked per rep, headcount curves bending), (3) only then build net-new agentic workflows. @28:32–33:40 ([[ai-in-gtm]], [[ai-sophistication-ladder]])
- High-volume or PLG markets put enrichment with the data team (warehouse/dbt). Lower-volume enterprise markets keep it with ops in Clay and Salesforce. @40:48–43:52 ([[revops]])
- GTMEs are IC builders paired with a strategy-side RevOps role. Centralize them under the CRO (via RevOps), next to marketing ops under a CMO, or near business systems under the CIO/CTO. Variants include an experiment GTME and a data-systems GTME. @44:54–51:02 ([[org-design]], [[gtm-engineering]])
- Early stage: one RevOps/sales-ops lead, one GTME, and an agency for outbound. Clay uses a Clay agency for its own outbound. Biggest ROI is account scoring and segmentation, which means matching ready accounts to reps instead of chasing logos like Figma. @52:05–59:11 ([[outbound-at-scale]], [[icp-and-saying-no]])
- Rapid fire: systems thinking separates great CROs. Spend time recruiting. Explain why behind policies. Book: *Stoner* by John Williams. @60:11–64:17 ([[career-and-leadership]])

## Key quotes
- Kyle: "We're doing similar things, automating as much of the grunt work as humanly possible um through a set of different tools." @09:10
- Kyle: "That's where the slop comes down in my mind" @18:20
- Kyle: "dude you just got to spend four to six months on making sure the baseline data quality is good and using AI to do that." @35:42
- Kyle: "do the boring stuff first. You have to get first-party data in a good spot" @38:47
- Kyle: "We our system of record is Snowflake not Salesforce." @44:54
- Guest: "anytime you're kind of introducing an AI into like a system that has a feedback loop, I actually think the the back part of that" @15:16
- Guest: "it's kind of why I think this go to market engineer role is a legitimate role because this detail is just not captured in most other roles." @25:29

## Numbers & facts
- Owner: "hundreds of thousands of of target accounts". The system of record is Snowflake, and scoring is built on Snowflake. @43:52–44:54
- Clay: GTM engineering is "30 30 people later and five go to market engineering teams later". @07:08
- Clay: assessed "150 odd data providers" and ranks its waterfalls by quality. @39:47
- Clay community Slack: "about 20,000". Job board at clay.com/job-board, plus a talent directory. @54:06–56:08
- MIT study claim, as Kyle cited it: "95% of AI deployments are failing to produce ROI". @10:11
- Berry found Clay at a Brooklyn growth meetup in early 2022 while at Vantage. His earlier company Archetype ("archype") was acquired by ClickHouse. @03:02–04:03

## Concepts & entities
[[kyle-norton]] · [[owner-com]] · [[shopify]] · [[clay]] · [[momentum]] · [[revenue-leadership-podcast]] · [[person-everett-berry]] · [[person-jason-lemkin]] · [[gtm-engineering]] · [[ai-in-gtm]] · [[ai-sdrs-and-agents]] · [[ai-sophistication-ladder]] · [[context-harness-and-memory]] · [[revops]] · [[org-design]] · [[outbound-at-scale]] · [[icp-and-saying-no]] · [[build-vs-buy-software]] · [[ai-sales-stack]] · [[personal-ai-stack]] · [[point-of-view-positioning]] · [[sales-hiring]] · [[career-and-leadership]]
