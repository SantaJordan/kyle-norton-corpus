---
slug: src-replacing-your-sales-team-with-ai-agents-jason-lemkin-founder-ceo
type: source
lifecycle: validated
valid_from: 2025-12-17
invalid_at: null
superseded_by: null
sources: [raw/podcasts/own-show/replacing-your-sales-team-with-ai-agents-jason-lemkin-founder-ceo/transcript.md]
links: [kyle-norton, owner-com, shopify, saastr, momentum, revenue-leadership-podcast, person-jason-lemkin, smb-sales-motion, ai-sdrs-and-agents, ai-in-gtm, ai-sales-stack, gtm-engineering, outbound-at-scale, context-harness-and-memory, ai-operating-model, build-vs-buy-software, revops, personal-ai-stack, talent-density, sales-hiring, comp-plans, fundraising-and-investability, executive-performance-and-mindset, career-and-leadership]
tags: [own-show, saastr, ai-agents, agentforce, salesforce, artisan, qualified, forward-deployed-engineers, vendor-bakeoff, incognito-test, inbound, guru, token-rationing, t2d3, jevons-paradox]
---

# E58: Replacing Your Sales Team with AI Agents
**Show:** The Revenue Leadership Podcast · **Guest:** Jason Lemkin, Founder & CEO @ SaaStr · **Published:** 2025-12-17 · **Kyle's role:** host · **Raw:** `raw/podcasts/own-show/replacing-your-sales-team-with-ai-agents-jason-lemkin-founder-ceo/transcript.md`

## TL;DR
- In May 2025, after two highly paid reps quit without notice, SaaStr went "all in on agents." It now runs about 20 agents, with Agentforce, Artisan and Qualified each working a slice of the Salesforce database. Lemkin says agents now beat "a midpack AE or SDR," so mid-pack GTM jobs are "in terminal decline."
- His playbook: the executive deploys the first agent personally (about 30 days, 20–30 hours), picks the vendor by the quality of its forward-deployed engineer, runs a two-vendor bake-off rather than ten, and starts with inbound and support (an incognito test of your own website).
- Kyle shares a lot of Owner.com detail in first person: about 3x bookings per dollar per AE, nine production AI use cases, about 25 sales hires in 75 days, an in-house cold outbound engine sending 1,800 emails a day, Guru beating AI-native startups, and a shift back toward Salesforce/Agentforce as the orchestration hub.

## What Kyle said
- Intro: he learned "all about uh tech" from SaaStr when he broke into the space "over 10 years ago". Lemkin led Owner's seed, and "Jason's been incredibly helpful for me personally". @01:01–03:04 ([[saastr]], [[person-jason-lemkin]], [[owner-com]])
- Owner's agent stack and the context question: "we've got one mind and we've got like an SMS follow-up agent that we're building." He asked whether to "build one mega model of our own to power all of the customer journey from AI BDR all the way through to AI support" or connect many tools that share insight. @14:17–15:17 ([[context-harness-and-memory]], [[ai-operating-model]], [[ai-sdrs-and-agents]])
- Jevons paradox of sales: Owner has "like nine high impact production use cases of AI". Bookings per dollar per AE is "3x any team I've ever managed before". Yet "I'm hiring like 25 people in sales over like a 75day period". He concedes "it's not like for like because we do month-to-month contracts and it's SMB." (Lemkin pushes back: at a true 3x you could run a team 30–40% smaller.) @25:22–26:25 ([[ai-in-gtm]], [[sales-hiring]], [[smb-sales-motion]])
- Who runs agents: "probably like a growth PM or a data science turned GTME." @30:29 ([[gtm-engineering]])
- Owner's GTM AI lead: the role was hard to fill with people who had enough "business acumen and and sales savvy". They hired someone from Atomico's venture studio who had started companies. He built the cold outbound email infrastructure "in like three weeks" (others said it was "a multi-month project") on "prompt layer and a bunch of models" plus custom code. Owner was then "sending 1,800 cold outbound emails every single day", with outside help on domain infrastructure. @31:30–32:30 ([[gtm-engineering]], [[outbound-at-scale]], [[build-vs-buy-software]])
- Budget pushback: he is surprised by friends at good companies who say they lack budget for AI ("what are you talking about?"). @34:33 ([[ai-in-gtm]])
- He did it himself first. [[momentum]] was "one of our first AI implementations". He wrote the prompts and custom Salesforce fields himself (he had implemented Salesforce "on my own way back in the day") and checked the fields at night "after the kids went to sleep". He also took a Replit "100 days of code" course. Now an AI lead and an "incredibly AI savvy" head of RevOps own it. He still takes demos but is "not anywhere near as close." @40:39–41:39 ([[revops]], [[personal-ai-stack]], [[ai-operating-model]])
- Sales team size: "100." @43:42
- He fields reference requests by dictating short answers ("whisper flow") rather than taking calls. @54:54 ([[personal-ai-stack]])
- Incumbent vs startup: in an AI knowledge-base bake-off, two AI-native startups lost to Guru ("Who would have known the like stodgy incumbent would have actually had the better AI tooling"). Guru now runs across Owner's whole GTM org. @56:56–57:57 ([[build-vs-buy-software]], [[ai-sales-stack]])
- His hypothesis: weak incumbent AI comes from "crappy models" and token-constraining ("it feels like I'm using GPT 3.5 here"). Leaders need hands-on taste to tell the difference. He learned this as a consumer: the Oura ring advisor gave superficial answers, so he dumped his data into Gemini 3 for "fascinating insights". @57:57–61:59 ([[personal-ai-stack]], [[ai-in-gtm]])
- Salesforce reversal: at [[shopify]] he stopped a Salesforce Einstein pitch mid-meeting ("don't try to hoodwig me with Einstein"). Now Owner is "leaning into Salesforce more than ever which I am personally surprised by". Looking at tool sprawl and a "master orchestrator agent", he thinks "maybe this is actually rolling back into Salesforce", partly for "security and the data and and the governance" at Owner's scale. @63:00, @68:04 ([[ai-sales-stack]], [[ai-operating-model]])
- Workload: "still working as hard as I ever have", but "I'm actually having a blast." Closing advice: if you sign up for growth beyond triple-triple-double-double, "be ready to work harder than you ever have"; if not, take a different path. @77:12, @80:15 ([[executive-performance-and-mindset]], [[career-and-leadership]])

## Guest's core ideas
- "Inning one" of AI GTM is cloning your best human at scale. Today's "hyperpersonalized" emails use roughly one to three data fields. Token cost and latency block true one-to-one. @10:12–14:17 ([[ai-sdrs-and-agents]], [[outbound-at-scale]])
- Don't design meta-agents until you have three or four agents working in production for three or four months. SaaStr's agents share learnings only by writing back to Salesforce. Most companies need "a nerdy human managing your agents," not a home-built orchestration layer. @15:17–18:19 ([[context-harness-and-memory]], [[ai-operating-model]])
- Pick vendors on the "2 by 2" of product quality and forward-deployed-engineer quality: "don't sign the contract until you talk to your forward deployed engineer". Every GTM agent needs weeks of training. @21:19–23:21 ([[build-vs-buy-software]])
- Mid-pack AEs, SDRs and BDRs are in "terminal decline". Truly elite operators, such as one human managing 20 agents, should earn 2–3x, with 10x productivity expected. Find the internal "GTM nerd" rather than posting for an AI executive. @24:22–33:30 ([[talent-density]], [[comp-plans]], [[gtm-engineering]])
- Executives must deploy the first tool themselves. Agencies won't get it right "not today". Training means uploading docs, iterating sample outputs, and reading results daily. Lemkin trained a digital-clone agent ("Deli" in transcript, likely Delphi) every morning for a month. @34:33–46:46 ([[ai-in-gtm]])
- Start with inbound and support: run the "incognito" test on your own site and fix "the one that breaks your heart". AI should answer questions and qualify instantly instead of routing buyers through a 21-year-old SDR. @46:46–52:52 ([[ai-sdrs-and-agents]])
- Two-vendor bake-off (an incumbent add-on plus one hot startup with real references). Leaders converge within weeks. Co-pilot add-ons are mediocre when AI isn't core to the vendor. @53:53–61:59 ([[build-vs-buy-software]])
- Salesforce "renaissance": not mainly Agentforce, but Salesforce as "the hub for your agents". Agentforce is more work to set up but as good or better in production thanks to native data. @63:00–69:05 ([[ai-sales-stack]])
- Triple-triple-double-double still builds a multi-billion-dollar company but no longer reliably gets venture funding. Revenue leaders face a bifurcated choice: high intensity or slow-growth "lifestyle" roles. The 2020–21 "magical middle ground" is gone. @70:06–81:15 ([[fundraising-and-investability]], [[career-and-leadership]])

## Key quotes
- Kyle: "do we build one mega model of our own to power all of the customer journey from AI BDR all the way through to AI support" @15:17
- Kyle: "we have like nine high impact production use cases of AI" @25:22
- Kyle: "He built the infrastructure in like three weeks and and like everybody else told us that was like a multi-month project" @31:30
- Kyle: "Who would have known the like stodgy incumbent would have actually had the better AI tooling" @57:57
- Guest: "I am done paying an SDR $150,000 a year, an AE $500,000 a year for basically inbound spoonfed leads and renewals and quitting on me." @21:19
- Guest: "Our AI agents are better than a midpack AE or SDR or BDR." @24:22
- Guest: "If you don't roll up your sleeves in the age of AI and AIGM, you will become obsolete." @37:37

## Numbers & facts
- Owner (Kyle): about 3x bookings per dollar per AE versus his prior teams; 9 high-impact production AI use cases; hiring about 25 sales people over about 75 days; sales team of "100"; 1,800 cold outbound emails a day; outbound infrastructure built in about 3 weeks. @25:22–26:25, @32:30, @43:42
- Lemkin estimates Kyle spends "probably 30 or 40% of your time" recruiting. @18:19
- SaaStr: 70,000 AI emails versus about 7,000 sent by humans before, driving "15% of the revenue for Saster London". @11:14, @36:35
- SaaStr went all in on agents in May 2025 and now runs about 20 agents. Its pay was $150K for an SDR, $500K for an AE, and up to $200K for a senior SDR. @21:19–24:22
- First agent tool costs "50k 60k or 100k" and takes about 30 days, of which 20–30 hours are the executive's own. Agent products are "30, 40, 50K and up". @35:35–36:35, @65:02
- Gorgias board approved about $4M of incremental token costs for next year. @58:57
- Agentforce: "Mark has 2,000 people working on it". Salesforce is a "$45 billion company". FDE can promise production in 45 days. @67:03, @69:05
- Venture: about 50% of VCs would have funded triple-triple-double three to four years ago, versus about 10% now. SaaStr's AI VC tool gave one founder a 38% chance of raising. @71:07–74:10

## Concepts & entities
[[kyle-norton]] · [[owner-com]] · [[shopify]] · [[saastr]] · [[momentum]] · [[revenue-leadership-podcast]] · [[person-jason-lemkin]] · [[ai-sdrs-and-agents]] · [[ai-in-gtm]] · [[ai-sales-stack]] · [[gtm-engineering]] · [[outbound-at-scale]] · [[context-harness-and-memory]] · [[ai-operating-model]] · [[build-vs-buy-software]] · [[revops]] · [[personal-ai-stack]] · [[talent-density]] · [[sales-hiring]] · [[smb-sales-motion]] · [[comp-plans]] · [[fundraising-and-investability]] · [[executive-performance-and-mindset]] · [[career-and-leadership]]
