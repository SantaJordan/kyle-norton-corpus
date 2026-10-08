---
slug: src-E19-architecting-systems-for-hypergrowth-with-nate-follen-of-ram
type: source
lifecycle: validated
valid_from: 2025-02-05
invalid_at: null
superseded_by: null
sources: [raw/podcasts/own-show/E19-architecting-systems-for-hypergrowth-with-nate-follen-of-ram/transcript.md]
links: [kyle-norton, owner-com, momentum, clay, revenue-leadership-podcast, person-jonathan-shankman, revops, ai-sales-stack, ai-in-gtm, build-vs-buy-software, gtm-engineering, outbound-at-scale, org-design, personal-ai-stack, prioritization-5p, churn-and-retention]
tags: [own-show, ramp, business-systems, momentum, gong-cancelled, crm-autofill, iroute, lead-scoring, datalane, dispositions, slope, pilots, reasoning-models, kg-buyer-alert, agile-revops]
---

# E19: Architecting Systems for Hypergrowth with Nate Follen of Ramp
**Show:** The Revenue Leadership Podcast · **Guest:** Nate Follen, head of business systems operations @ Ramp; ex-Intercom, BentoBox (transcript spells "Follin") · **Published:** 2025-02-05 (RSS pubDate) · **Kyle's role:** host · **Raw:** `raw/podcasts/own-show/E19-architecting-systems-for-hypergrowth-with-nate-follen-of-ram/transcript.md`

## TL;DR
- Ramp runs GTM systems like a product org: small, funnel-aligned pods (MarTech/SDR/AE), two-week sprints, tiger-team experiments before rollout, a "revenue Drake's equation" to prioritize, and vendors chosen for "slope."
- AI use cases centre on [[momentum]]: deal-risk "KG buyer" alerts, win/loss context windows, CSM handoff dossiers, and prompt-driven CRM fields. Build vs buy is often "both," decided by pilots and adoption.
- This is one of Kyle's most detailed early descriptions of Owner's AI/RevOps stack: Gong cancelled for Momentum, Snowflake-scored "iRoute" lead routing into SalesLoft, Datalane mobile enrichment, a 5%-fee compliance prompt, and auto-fill over rep approval.

## What Kyle said
- Owner and Ramp are both Redpoint portfolio companies and "very excited customers of Momentum"; Owner is also a Ramp customer. @03:08, @47:05 ([[owner-com]], [[momentum]])
- Org: Owner is moving RevOps to Agile, aligned to "sales, launch, CS as the key stakeholders." At ~200 employees it is "one product owner for each of those functional areas," and "most of our development is done on contract, both onshore and offshore." @09:19–10:27 ([[revops]], [[org-design]])
- "My head of RevOps was a former sales leader" (second-line BDR leader, sales manager). Purely technical partners give answers with "no hope of adoption" ("slap some more required fields"). SMB reps won't fill six fields, so automate with Momentum. @11:28–12:29 ([[revops]])
- "Just canceled Gong" after "seven, eight years": "if you had told me 24 months ago that I was going to cancel Gong, I would have thought you were nuts... with generative AI, all of that is commoditized now." Call recording is moving into Momentum. @18:57 ([[ai-sales-stack]], [[build-vs-buy-software]])
- Consolidation vs best-of-breed: he once put everything in SalesLoft (including call recording), then brought in Gong. Interoperability is better now, and you can build integrations via Zapier or APIs; Owner pipes Snowflake directly into SalesLoft. @21:01–22:04 ([[ai-sales-stack]])
- Lead scoring and routing: two Snowflake models, "eGMB and eWin" (deal value, propensity), power "iRoute." It runs at night and tops a BDR up from "60 do-call steps" to "100 do-call steps" with the highest-scored leads, which is "not possible with any off-the-shelf tooling." @22:04–23:08 ([[gtm-engineering]], [[outbound-at-scale]])
- Enrichment: data-ops leader [[person-jonathan-shankman]] built a scraping/enrichment/AI-confidence system, and Owner now uses Datalane. "Our mobile phone enrichment rate is like 95%"; with a restaurant owner's mobile, reaching them is "easy." Uses the People Data Labs API. @24:09–25:10 ([[gtm-engineering]], [[outbound-at-scale]])
- Disposition taxonomy (connected? gatekeeper vs owner? which number? outcome) makes it easy for reps and yields "high quality data." @25:10–26:12 ([[revops]])
- Vendor selection by "slope" is "my number one criteria." Owner was ~"15 million ARR when we started using Momentum," and he "might have been their first full paying customer." He was also early with Avara (AI sim), a "first 10 customer" of SalesLoft, and early with Chorus and Chili Piper. He chose Momentum for custom prompts into custom Salesforce fields over a vendor that "filled out medic... only medic." "I'm much too opinionated about how I want to run things." @34:35–36:41 ([[build-vs-buy-software]], [[ai-sales-stack]])
- Owner's AI use case: "we charge a 5% service fee to the guest." If owners learn it at onboarding "they're going to be pissed," so a Momentum prompt checks whether the rep mentioned it, sets a checkbox on the opportunity, and flags misses to managers. @52:18–53:21 ([[ai-in-gtm]], [[churn-and-retention]])
- Auto-fill experiment: reps often skipped click-to-accept, and "just having it fill in the fields automatically every time... We got a larger volume of high quality data." @54:26–55:26 ([[ai-sales-stack]])
- Advice: "just push the vendor to pilot... it's the ultimate way to just like de-risk like crazy." Much AI is vaporware ("hallucinating gobbledygook"). @60:39–61:40 ([[build-vs-buy-software]])
- Momentum compounds: a lead attracts talent and money to experiment, and "the gulf seems to be widening" between Ramp and competitors. @62:40–63:43
- AI so far has been "the world's hardest working intern"; reasoning models widen the aperture. He tested o1 on his own symptoms with stored memory, and it was "night and day" vs 4o and "far better than what the like telemedicine call I had was." Deal-advice products were "pretty lame" until now. @66:54–67:54 ([[personal-ai-stack]], [[ai-in-gtm]])
- "AI is going to replace a bunch of the parts of the sales process that aren't sales... the craft of sales will make a big comeback." @71:04–72:09 ([[ai-in-gtm]], [[ai-sdrs-and-agents]])

## Guest's core ideas
- "Ramp years" are like dog years. Speed of change is a "quiet superpower," enabled by a flat, Slack-heavy org; hacky builds are accepted only as named debt. @04:13–07:19 ([[culture-and-high-standards]])
- Lean teams (GTM systems team of five plus 3–4 Apex engineers), aligned to funnel stages so each owner acts as a product manager for that role's workflows. @08:19–09:19 ([[org-design]], [[revops]])
- Hire for slope and curiosity. Test ideas (e.g., gifting) with a tiger team before rollout. @14:40–15:45
- Momentum AI: "KG buyer" / deal-risk alerts from calls and emails (long prompts with examples), win/loss context windows, and CSM handoff group DMs in Slack. @16:49–18:57, @49:09–52:18 ([[ai-sales-stack]])
- Prefer best-of-breed modules over consolidation. Re-evaluate build vs buy at each renewal; call recording is now "a pretty easy build." @20:00–21:01 ([[build-vs-buy-software]])
- Biggest systems landmine: confusing or frequently changing pricing that is hard to contract quickly. At Ramp-speed, hiring too slowly also leaves money on the table. @30:19–33:28
- Prioritize with the "revenue Drake's equation" (leads × conversion × deal size − churn), weighted by team size. Run two-week sprints, half-year roadmaps, daily standups, and "jam sessions"/shadowing with reps. @39:48–42:52 ([[prioritization-5p]])
- Other tools: Actively (outbound scoring that retrains itself), Clay, Rox, Atrium (anomaly tracking), Perplexity, and an in-house Slack "AI sales engineer." @43:55–47:05, @56:26–58:32, @68:56 ([[ai-sales-stack]], [[clay]])

## Key quotes
- Kyle: "if you had told me 24 months ago that I was going to cancel Gong, I would have thought you were nuts" @18:57
- Kyle: "Our mobile phone enrichment rate is like 95%." @24:09
- Kyle: "I'm much too opinionated about how I want to run things." @36:41
- Kyle: "We got a larger volume of high quality data running it that way." @54:26
- Kyle: "AI is going to replace a bunch of the parts of the sales process that aren't sales." @71:04
- Guest: "speed of change is actually one of the quiet superpowers that's not talked about quite as much." @06:18

## Numbers & facts
- Ramp (Kyle's intro): "fastest company ever to 100 million ARR"; Keith Rabois called it "best run private company on the planet"; valuation "over $8 billion." @00:00, @03:08
- Ramp: day 2,131 since founding; Follen ~1,000 days; sales team tripled to "upwards of around 400"; 1,000+ employees; 5+ products. @04:13, @06:18, @12:29, @28:15
- Owner (Kyle): ~200 employees @10:27; Gong used 7–8 years @18:57; iRoute 60→100 daily call steps @23:08; 95% mobile enrichment @24:09; ~$15M ARR when Momentum was adopted @34:35; 5% guest service fee @52:18.

## Concepts & entities
[[kyle-norton]] · [[owner-com]] · [[momentum]] · [[clay]] · [[revenue-leadership-podcast]] · [[person-jonathan-shankman]] · guest Nate Follen (`person-nate-follen`, no entity page yet) · [[revops]] · [[ai-sales-stack]] · [[ai-in-gtm]] · [[ai-sdrs-and-agents]] · [[build-vs-buy-software]] · [[gtm-engineering]] · [[outbound-at-scale]] · [[org-design]] · [[personal-ai-stack]] · [[prioritization-5p]] · [[churn-and-retention]] · [[culture-and-high-standards]]
