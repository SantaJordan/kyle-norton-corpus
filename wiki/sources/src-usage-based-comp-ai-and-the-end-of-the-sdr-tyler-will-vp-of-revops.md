---
slug: src-usage-based-comp-ai-and-the-end-of-the-sdr-tyler-will-vp-of-revops
type: source
lifecycle: validated
valid_from: 2025-12-31
invalid_at: null
superseded_by: null
sources: [raw/podcasts/own-show/usage-based-comp-ai-and-the-end-of-the-sdr-tyler-will-vp-of-revops/transcript.md]
links: [kyle-norton, owner-com, shopify, revenue-leadership-podcast, person-tyler-will, person-jason-lemkin, comp-plans, revops, metrics-and-forecasting, churn-and-retention, ai-in-gtm, ai-sdrs-and-agents, gtm-engineering, personal-ai-stack, context-harness-and-memory, ai-operating-model, sales-coaching-and-enablement, cro-role-and-board, operating-rhythm]
tags: [own-show, intercom, fin, usage-based-pricing, outcome-pricing, mrr-comp, input-metrics, forward-deployed-engineer, claude-code, revops-scaling, sdr-agent, comp-change-management, writing-style-skill]
---

# E59: Usage-Based Comp, AI, and the End of the SDR
**Show:** The Revenue Leadership Podcast · **Guest:** Tyler Will, VP of RevOps @ Intercom · **Published:** 2025-12-31 (RSS) · **Kyle's role:** host · **Raw:** `raw/podcasts/own-show/usage-based-comp-ai-and-the-end-of-the-sdr-tyler-will-vp-of-revops/transcript.md`

## TL;DR
- Intercom's AI agent Fin ($0.99 per resolution) forced a rethink of comp, pricing, ICP, forecasting and especially post-sales. Onboarding now means writing the customer's documentation. Expansion means raising Fin's "involvement rate". New roles include R&D services (forward-deployed engineers) and split pre- and post-sales SEs.
- Comp evolved in two phases. First, AEs got monthly credit for uncontracted overage usage. Then account managers moved to pure summed MRR over a semiannual period. Every plan follows four rules: simple, fair, rewards the right behavior, and instrumentable. Plans should be overhauled at most annually, triggered by a pricing or product change.
- RevOps is becoming more generalist and opinionated. Claude Code queries Snowflake directly, and "If you're showing up in the forecast meeting to take notes, you are going to lose your job". Kyle adds Owner details: his VP RevOps building in Salesforce from Claude Code, a Claude writing-style skill, and the message that roles which only relay documents mean "we have failed".

## What Kyle said
- Owner uses Fin: "We're a Finn customer actually." @02:00 ([[owner-com]])
- **AI depth for CROs:** he referenced the previous episode with Jason Lemkin as one end of the pendulum (a CRO/CMO should "implement one AI tool soup to nuts on their own"). His own bar: "if you don't understand the difference between pre-training and post- training. If you don't understand like recursive learning and like ingestion versus and like tuning ... you're probably going to struggle". @06:05–08:08 ([[ai-in-gtm]], [[person-jason-lemkin]])
- **Systems engineering:** "in the AI world this systems engineering mindset is going to be more important than ever and and this is what's going to differentiate you know good to great CRO". @05:04 ([[cro-role-and-board]])
- **Metric pressure:** "if you just like breathe down everybody's neck and you make it all about dials, then you invariably see dials go up and decision maker connect rate go down because people are just doing ghost dials". "every strength is a weakness". @13:12–14:13 ([[metrics-and-forecasting]], [[sales-coaching-and-enablement]])
- **Coaching posture:** "if a rep doesn't have a lot of calls. I don't send them a Slack message being like, 'Hey, go make them more make more calls.' I'm like, 'Hey, go figure out what's what's broken.'" And: "people want to do a good job ... You just oftentimes there's things in the way." @17:17–18:18 ([[sales-coaching-and-enablement]])
- **Honest comp rollouts:** the worst rollouts try to sell a bad change as good. "At the end of the day, we are all agents of capitalism here". "quotas go up because that's how startups work and there's it's a you know a law of startup physics." @41:36 ([[comp-plans]])
- **Product and GTM roadmap alignment:** "the thing we're trying to get better at is is aligning product roadmap with go to market roadmap". Sometimes "we've got three major initiatives all lined up and we can't put a fourth in front of the for the in front of the reps without massively diluting it". He asked what the "minimum effective dosage" of process is. @44:39–45:40 ([[operating-rhythm]])
- **Owner RevOps in Claude Code:** "my VP of Rev ops and I were like texting all weekend cuz we were both cooking in cloud code". The VP RevOps was "building into our um sandbox Salesforce from the cloud code terminal like at a very high level of of proficiency". Business requirements go to Claude, which writes the technical spec and implements it, so "we don't need to do the grinded out like Salesforce development". @58:56 (VP RevOps unnamed in the episode; Owner's VP RevOps is [[person-steve-dinner]]) ([[revops]], [[gtm-engineering]])
- **Roles must move up:** a RevOps team member who was one of Owner's first BDRs is moving into a cross-functional coordination role. His words to her: "if your role ends up being writing documents and just telling one thing from one person to another we have failed. So like the the AI tooling should be able to do all that. You need to like pull the strings and build that AI system". @59:58 ([[revops]], [[ai-operating-model]])
- He asked whether the RevOps-to-rep ratio is higher now. @60:59
- **Probable Kyle (not certain):** "it's just all the people all the people doing the junior number crunching grinded out work all have to move up one level of abstraction and AI has to do all that." @63:03. A first-person account follows of setting up Fireflies to push every call into one Notion page and a Claude Code skill that reviews a week of meeting notes for commitments missing from task lists. @63:03–64:05. He likely cited Karpathy ("computers allowed you to automate anything that is specifiable and now AI can let you automate anything that's verifiable"). @65:06. He also mentioned a vendor PRD where Claude flagged "13 of them" fabrications. @66:06–67:08. ([[personal-ai-stack]])
- **Writing-style skill:** "I basically like put 150 pages of my writing into originally it was chatbt. like tell me my writing style in excruciating detail ... and then it marries that with a bunch of context about owner and that's now in like a clot skill". It replaced a TextExpander snippet ("Zstyle"). @75:13–76:14 ([[personal-ai-stack]], [[context-harness-and-memory]])
- **T-shaped CROs:** "Toby from Shopify would call it being T-shaped." @78:14 ([[shopify]], [[cro-role-and-board]])

## Guest's core ideas
- Leaders over-index on success metrics. Instrument the whole machine with a few key input metrics, bounded by guardrails (e.g., 10–50 calls), and inspect some metrics at the manager or exec level rather than per rep (pipeline quality, pacing). @04:02–17:17 ([[metrics-and-forecasting]])
- On AI depth, Tyler sits "twothirds of the way toward toward Jason's position". Anyone selling an AI product must be fluent in it (RAG, model tuning, Fin's analyze-test-train-deploy loop). @07:07–10:09 ([[ai-in-gtm]])
- Everything got rethought: comp, pricing, discounting, ICP, forecasting. Post-sales changed most. Onboarding is about getting the customer's documentation AI-ready. Growth means unlocking more conversations ("involvement rate") and new channels, which turns into a recurring commercial conversation. @19:21–27:26 ([[churn-and-retention]])
- Team design: AE hunters, plus relationship managers and CSMs on co-sales. CSMs are now more technical and commercial. A new R&D services team ("like the forward deployed engineer") is about 8 months old. SEs are split into pre- and post-sales. Upskilling runs through "Finn University". @27:26–30:28 ([[org-design]])
- Comp phase 1: the contract retires quota, plus monthly credit (not annualized) for uncontracted usage, given to the landing AE for 12 months and to the RM while they own the account. Phase 2: RMs on summed MRR across their book each semiannual period. A temporary 2x credit on Fin deals drove adoption. @30:28–35:33, @42:38 ([[comp-plans]])
- Comp rules: two metrics (one plan has three), "simple enough you can explain it in five minutes on a whiteboard", fair, rewards the desired behavior, and visible throughout the period. Tweak every six months and overhaul at most annually. Bring managers in months early. In hindsight, he says, they lost engagement before launch and got "too cute". @35:33–52:49 ([[comp-plans]])
- RevOps: the first GTM engineer was hired "like a month ago". Solutions ops was split off for post-sales. Generalists are coming back. Tyler queries Snowflake via Claude Code and Glean, so analytics moves from ticket-driven dashboards to embedded investigation. Headcount (about 45 against 250 sellers) is up for now, and the goal is no new RevOps hires next year. @53:50–63:03 ([[revops]], [[gtm-engineering]])
- The "SDR agent is going to be one of the first things that goes". Outbound gets easier and better. AE productivity rises somewhat. Post-sales success needs more people, not fewer. @67:08–70:10 ([[ai-sdrs-and-agents]])
- Internal AI uses: Fin answering RevOps questions in Slack (adoption is the blocker), a post-sales "cockpit" (built on Snowflake), Gong forecasting, and auto-filled MEDDPICC fields. The SVP of sales "used quad code and found $9 million of pipeline" that turned out to be a mistake. @66:06, @71:11–74:13
- A great CRO is a "porpus": surface-level breadth with the ability to dive deep, plus business-generalist fluency. Advice for RevOps leaders: "have an opinion". Hardest lesson: give tough feedback early. Book: Ethan Mollick's *Co-Intelligence*. @77:14–83:17

## Key quotes
- Guest: "If you're showing up in the forecast meeting to take notes, you are going to lose your job to Gemini or whatever it is that is on that call very quickly." @00:00
- Guest: "that SDR agent is going to be one of the first things that goes" @68:09
- Kyle: "you invariably see dials go up and decision maker connect rate go down because people are just doing ghost dials" @14:13
- Kyle: "we are all agents of capitalism here" @41:36
- Kyle: "if your role ends up being writing documents and just telling one thing from one person to another we have failed." @59:58

## Numbers & facts
- Fin pricing: "99 cents per resolution". A resolution is a customer confirmation or a "soft resolution" (no follow-up). @21:22–22:23
- Intercom: 250 sellers. Tyler's team will be about 45 people early next year. @07:07
- Comp example: a $60K contract plus $5K/month overage in two months gives $70K of quota credit. @32:31–33:31
- Owner: Kyle's writing-style skill was built from about 150 pages of his writing. @75:13

## Concepts & entities
[[kyle-norton]] · [[owner-com]] · [[shopify]] · [[revenue-leadership-podcast]] · [[person-tyler-will]] · [[person-jason-lemkin]] · [[person-steve-dinner]] · [[comp-plans]] · [[revops]] · [[metrics-and-forecasting]] · [[churn-and-retention]] · [[org-design]] · [[ai-in-gtm]] · [[ai-sdrs-and-agents]] · [[gtm-engineering]] · [[personal-ai-stack]] · [[context-harness-and-memory]] · [[ai-operating-model]] · [[sales-coaching-and-enablement]] · [[cro-role-and-board]] · [[operating-rhythm]]
