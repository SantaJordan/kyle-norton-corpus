---
slug: src-E74-your-agent-isn-t-broken-its-foundation-is
type: source
lifecycle: validated
valid_from: 2026-09-02
invalid_at: null
superseded_by: null
sources: [raw/podcasts/own-show/E74-your-agent-isn-t-broken-its-foundation-is/transcript.md]
links: [kyle-norton, owner-com, revenue-leadership-podcast, person-jonathan-moss, pavilion, saastr, ai-in-gtm, gtm-engineering, build-vs-buy-software, ai-sales-stack, ai-sdrs-and-agents, revops, org-design, cro-role-and-board, metrics-and-forecasting, sales-hiring]
tags: [own-show, experity, health-tech, hipaa, company-brain, meta-harness, six-layer-stack, agentcore, snowflake, revops-as-product, gtm-pods, ai-maturity-levels, personal-ai-stack, openclaw, agent-payments]
---

# E74: Your Agent Isn't Broken. Its Foundation Is.
**Show:** The Revenue Leadership Podcast · **Guest:** Jonathan Moss ("J Moss"), EVP Growth & Partnerships @ Experity ("Xperity" in transcript) · **Published:** 2026-09-02 · **Kyle's role:** host · **Raw:** `raw/podcasts/own-show/E74-your-agent-isn-t-broken-its-foundation-is/transcript.md`

## TL;DR
- GTM AI fails as a "soup" of disconnected pilots. Moss's six-layer system: data → "brain" (semantic layer of policies, IP and decisions) → intelligence (models) → orchestration → agents → interface. Build the system and the workflows in parallel, start from a business outcome, and redesign the work instead of bolting AI onto it. Build and own the harness; a vendor almost got Experity's "AI brain."
- Kyle pushes back that big companies should first win with a few use cases to earn credibility. He lays out his SaaStr maturity model (L1 chat-as-search → L2 working agents/workflows → L3 AI as infrastructure → L4 recursive self-improvement) and says he once traded headcount to get data work done.
- Org: RevOps becomes "revenue product," organized as cross-functional pods (acquisition, expansion, retention, value realization). Hire generalists with agency, and contract the specialists. The revenue leader must own revenue end to end and understand the system, or a system owner must sit at the C-suite table. The episode closes with a long comparison of Kyle's and Moss's personal AI stacks.

## What Kyle said
- Intro: Moss is co-dean of the AI in GTM school at [[pavilion]] and leads the RevOps practice for Winning by Design's Growth Institute. Kyle recommends his GTM AI podcast and Substack. @01:00
- Most GTM AI transformation is "a bunch of disconnected pilots... thrown into a soup" with little ROI. He cites the McKinsey-style "90% of implementations have no ROI" stat, "directionally very accurate." @02:08 ([[ai-in-gtm]])
- "I've talked a lot about building this company meta harness." Pushback: at a big public company with "50 cooks in the kitchen," starting with the system "doesn't work." You "get a couple interesting use cases up and running, build some value, demonstrate and build momentum" until you can say "I can't do the next thing without the infrastructure." Fix data first, but not all of orchestration. @05:19–06:19 ([[ai-in-gtm]], [[gtm-engineering]])
- Building workflows "tells you where the system is broken": missing context, identity that doesn't reconcile across systems, missing access. @08:28
- RevOps as product: "user behavior... jobs to be done... building a PRD... build your MVP... iterate and loop... We're all product thinkers." @11:48 ([[revops]])
- Build vs buy for intelligence: "I've written extensively about like you should be building your own intelligence." A platform (Vasco came up "on my last podcast") is fine if you can see the intelligence and "still take it out." An MCP-wired Claude "lies to you... it fills in the gaps... that's the RL." He calls the brain "that compounding asset that is the brain of your company." @21:10–23:14 ([[build-vs-buy-software]], [[metrics-and-forecasting]])
- Data team buy-in: he has also traded headcount. "When we raised our series, see the first role that I put into the new headcount plan was an applied leader for sales," and that headcount ultimately went to the data and BizOps team: "I just needed the work to get done." Non-revenue stakeholders don't see why revenue's asks outrank the VP of product's or the CFO's. @29:26–31:29 ([[org-design]], [[revops]])
- Agent sprawl: RevOps, growth marketing and sales leaders all build, some on personal Vercel accounts "with their company credit card." Agents collide and send customers duplicate emails. He cites Ramp's Glass write-up and Cursor's platform. @31:29–33:38 ([[ai-sdrs-and-agents]], [[gtm-engineering]])
- Regulated industries: at a Winning by Design event he told a skeptic "I don't know. Like, I sold the restaurants like we are very much not doing what you're doing", but "you can. It just takes a different level of... coordination." @37:47–38:54
- SaaStr talk maturity model: level 1 chat as a Google replacement; level 2 successful agents and AI workflows; level 3 "AI as infrastructure" (people build inside a governed platform instead of vibe coding with their own MCPs and "a monster skill file"); level 4 a "recursive self-improving loop," with agents watching, building and improving agents. His "Grok bot" (as transcribed) inspection bot monitors his other bots. "The best companies are getting here like sort of now." @42:00–44:14 ([[ai-in-gtm]], [[saastr]])
- Asked whether the future revenue leader "might not just come from sales." Building leadership teams is like a basketball team ("you don't want five centers"). Does everyone need to be "super A.I. Pilled"? @45:16, @54:52 ([[cro-role-and-board]], [[org-design]])
- Moss says Kyle sits on his agent "GTM panel." @58:58
- Kyle's personal AI stack: on OpenClaw, migrating to "Grok bot" because OpenClaw crons "just stop firing." He keeps separate channels per job (podcast production vs podcast outreach). Crons check 48h before recording whether the docket is created and shared. He builds in Cursor, writes everything back to a GitHub repo of skill files so multiple surfaces share them, and has a setup agent porting OpenClaw over. Memory experiments include Garry Tan's "G brain" and "Toby's QMD." @63:08–67:19 ([[ai-sales-stack]])
- "Kai, K-A-I... my digital chief of staff" has its own email and logins via a 1Password agent vault, so he doesn't hand over his own passwords. He mentions "AI FOMO." @68:20–70:26
- Hot tip: Robinhood banking virtual cards for agents. His has a $500 monthly limit with approvals off. Its first successful purchase was reordering a particular sock. He wants agentic Amazon purchasing. @74:31–79:37

## Guest's core ideas
- The six-layer system. Moss "started at the agent and interface" and kept hitting missing context, so he rebuilt from the bottom up. That's his "lesson learned." @03:08–05:19 ([[ai-in-gtm]])
- System and workflows should run in parallel, not in sequence. @07:28
- Workflow method: business outcome first, then map handoffs, exceptions, data and where "context drop[s]" (meetings), then redesign (remove, automate, augment), then change management, measurement and a learning loop. Treat it like a product launch. "AI is not something that you add into an existing process." @09:36–10:45 ([[revops]])
- GTM intelligence center: decentralized self-serve analytics instead of a RevOps ticket queue, built on Snowflake, a semantic layer, LLMs and a chat UI. "Three year trends... in less than 30 minutes." Users must "teach the system" when output is bad, so every use improves the data (vs CRMs, where use makes data worse). @15:00–19:08, @24:19 ([[metrics-and-forecasting]])
- Stack: Snowflake, a GitHub-repo "brain" running on AWS, AgentCore for orchestration, observability, evals and permissions, and a homegrown chat UI or Teams (headless). @19:08–20:08, @36:45–42:00 ([[ai-sales-stack]])
- Own the harness: Experity nearly put its brain into a third party. Lock-in plus data exposure make portability "the most important factor." @20:08–23:14 ([[build-vs-buy-software]])
- Getting data-team priority: the pitch (revenue is what "feeds all of us") failed. What worked was moving 2–3 budgeted revenue FTEs into the data team. @27:24–29:26
- Avoid sprawl by giving everyone access to connected AI tools (gating access "pissed a bunch of people off") and running weekly "show us what you did with AI" sessions. "The agent is the easiest thing to build of all this." @33:38–36:45 ([[ai-sdrs-and-agents]])
- In GTM, regulated data (PHI) rarely appears. The work is getting people to stop treating everything as regulated. @38:54–39:54
- Org: RevOps silos (marketing/sales/CS ops) give way to product-style pods (PM, builder/engineer, process SME, data) per outcome: acquisition, expansion, retention, value realization. Hire generalists with revenue-architecture fluency and agency, and contract specialists (e.g., HubSpot work) via agencies or Upwork. @46:27–54:52 ([[org-design]], [[sales-hiring]])
- The revenue leader needs P&L fluency, agency to build, and end-to-end ownership of revenue and the system beneath it. Otherwise a growth/RevOps system owner needs a C-suite seat (like the CPO/CTO split). @54:52–57:57 ([[cro-role-and-board]])
- Personal stack: 121 agents in team hierarchies (including a GTM panel and a personal board), 57 skill files, a smart-routing agent behind Telegram, "Let's Cook" (thousands of markdown docs in a brain), Langtrace for decision tracking, a watchdog, and a Mac mini runtime. 52 cron jobs, "at least four of them break every day almost." @58:58–74:31

## Key quotes
- Guest: "if you're not thinking about the system that you're building, you're not going to be able to scale it." @04:17
- Kyle: "I've talked a lot about building this company meta harness." @05:19
- Guest: "A.I. is not something that you add into an existing process because then all you're typically doing is you're just adding one extra step or one extra layer." @09:36
- Kyle: "We're all product thinkers." @11:48
- Kyle: "MCP your cloud code instance or your cloud desktop instance into a bunch of things and ask it questions, it's lies. It lies to you." @22:10
- Kyle: "I just needed the work to get done." @30:29
- Kyle: "level three is AI as infrastructure." @42:00
- Guest: "The agent is the easiest thing to build of all this." @34:42

## Numbers & facts
- Moss: 20 years of GTM systems at Verizon, T-Mobile, OYO, REEF, Booster. Joined Experity in 2024. His role changed "a few months ago" after building RevOps over about 2.5 years. @01:00, @50:41
- "90% of implementations have no ROI" (Kyle citing a McKinsey-type survey, hedged). @02:08
- 3-year trend analysis in under 30 minutes. @18:06
- 2–3 revenue FTEs reallocated to the data team. @29:26
- Kyle: Owner's first post-Series C headcount was an "applied leader for sales," placed in data/BizOps. @30:29
- Moss personal: 121 agents, 57 skills, 52 crons (about four break daily). @58:58–67:19
- Kyle: Robinhood agent card with a $500 limit. @79:37

## Frameworks & named ideas
- Moss: six-layer agent stack. Brain/semantic layer. GTM intelligence center. "Teach the system." Parallel system+workflow build. RevOps-as-revenue-product. Outcome pods (acquisition, expansion, retention, value realization). Generalists plus contracted specialists. System owner at the C-suite table. Agent vs skill distinction.
- Kyle: company meta harness. Momentum-first for big orgs. Four-level AI maturity model (SaaStr talk), with level 4 being recursive self-improvement. Headcount trade to unblock data. Agent sprawl. Basketball-team leadership mix. Personal stack (OpenClaw → "Grok bot", Kai chief of staff, 1Password agent vault, Robinhood agent card).

## Concepts & entities
[[kyle-norton]] · [[owner-com]] · [[revenue-leadership-podcast]] · [[person-jonathan-moss]] · [[pavilion]] · [[saastr]] · [[ai-in-gtm]] · [[gtm-engineering]] · [[build-vs-buy-software]] · [[ai-sales-stack]] · [[ai-sdrs-and-agents]] · [[revops]] · [[org-design]] · [[cro-role-and-board]] · [[metrics-and-forecasting]] · [[sales-hiring]]
