---
slug: src-outbound-kitchen-scale-outbound-sales
type: source
lifecycle: validated
valid_from: 2024-11-19
invalid_at: null
superseded_by: null
sources: [raw/podcasts/guest-appearances/outbound-kitchen-scale-outbound-sales/transcript.md]
links: [kyle-norton, owner-com, outbound-kitchen, person-elric-legloire, person-jonathan-shankman, person-brett-bombach, pavilion, outbound-at-scale, smb-sales-motion, icp-and-saying-no, revops, gtm-engineering, org-design, sales-hiring, sales-coaching-and-enablement, ai-sales-stack, ai-sdrs-and-agents, talent-density, career-and-leadership, src-outbound-kitchen-ai-sdrs-dead-wrong]
tags: [podcast, guest-appearance, outbound-kitchen, outbound, bdr-ratio, lead-scoring, data-enrichment, revops-ratio]
---

# Outbound Kitchen: How to Scale Your Outbound Sales Without Losing Efficiency

**Show / host:** Outbound Kitchen / Elric Legloire · **Published:** 2024-11-19 (YouTube upload date) · **Kyle's role:** guest · **Raw:** `raw/podcasts/guest-appearances/outbound-kitchen-scale-outbound-sales/transcript.md` · **YouTube:** https://www.youtube.com/watch?v=z2s88Phez2I

Part 1 of two; part 2 is [[src-outbound-kitchen-ai-sdrs-dead-wrong]]. The intro claims ("scaled a sales team from 4 to 50 in under 2 years", "72,000 RR monthly with a 0.13 CAG ratio") are the host's framing (@00:00), not Kyle's words.

## TL;DR
- Kyle built Owner's outbound from zero (first BDR Nov 1, 2022) into a ~26-BDR machine at a 2:1 BDR-to-AE ratio, justified from first principles: if each BDR closes ~70–80K ARR/month against a ~70–80K cost, more BDRs per rep is better.
- The engine is data and ops: a central data team builds ML-scored, enriched account lists (BDRs never pick their own accounts), RevOps runs at ~1:20 support ratio, and Momentum/Avara automate CRM fill and practice. No AI-BDR outbound.
- Decision-maker-to-book conversion went from ~4% to ~16% via scripting iteration, rigorous one-thing-at-a-time coaching ("biggest needle mover"), lead quality, and talent selected on DNA over craft.

## What Kyle argued
- Properly built outbound can match inbound CAC and lets you target higher-value customers; plus channel redundancy because demand gen is volatile (@01:05–@03:07). See [[outbound-at-scale]], [[smb-sales-motion]].
- Fix deal quality / ICP before spinning up demand: sales intentionally declined in his first two full months (@03:07–@04:07). See [[icp-and-saying-no]].
- The BDR:AE ratio is a math question, not a norm: "You, you want as arguably as many BDRs per rep as possible" as long as BDRs produce (@07:16).
- Use pods and round-robin rather than 1:1 BDR–AE pairing, which is brittle in a high-promotion org (@08:16–@09:21).
- Split inbound SDRs (speed to first touch + meeting confirmation, critical for blue-collar buyers with high no-show) from outbound BDRs (cold-call craft) (@10:25–@11:31).
- Dedicated BDRs beat full-cycle AEs because people avoid the hardest part of the job, and AE hours cost ~2x for prospecting (@12:33–@15:45). Enterprise AEs should prospect through networks, not cold calls (@16:45).
- Under-investment in RevOps/enablement explains why "50% of your reps don't work out" (@20:56); first-time sales heads lack systems/spreadsheet skills their career never required (@22:00–@25:07). See [[revops]], [[career-and-leadership]].
- ML lead scoring (regression on digital footprint, trained on closed won/lost and GPV) beats deterministic point scoring (@28:10–@30:16). See [[gtm-engineering]].
- Account selection must be top-down even in enterprise — reps add perspective on a list delivered "on a platter" (@31:20–@33:22).
- AI is used internally (Momentum custom prompts for CRM fill, "still more accurate than a rep"; Avara sims), not for AI BDR outbound (@33:22–@37:32). See [[ai-sales-stack]], [[ai-sdrs-and-agents]].
- Talent is "like 80% of the battle"; hire BDRs on DNA (mindset, habits, intelligence, character) over craft (@44:47, @46:51–@47:53). See [[sales-hiring]], [[talent-density]].

## Key quotes
- "I am a believer that a properly constructed outbound motion, you can have comparable CAC" (@01:05–@02:06)
- "I joke that like the number one objective for any BDR is to stop being a BDR as fast as possible." (@12:33)
- "it's only inefficient if your BDRs aren't producing much." (@08:16)
- "You wouldn't, you don't want your data scientists selling deals. Why do you want your sales reps doing data work?" (@31:20–@32:21)
- "even without any correction, it's still more accurate than a rep, interestingly enough." (@34:26)
- "And then we don't do any AI outbound, like no, like AI BDR spam or anything." (@37:32)
- "And, and like the, the talent is like 80% of the battle." (@44:47)
- "I haven't made a cold outbound dial in like forever." (@45:49)

## Numbers & facts he cited
- Joined Owner June 2022; sales team was 4 reps + a manager, two reps moved on (@00:00). Sales team now "close to 50 people" (@01:05).
- First outbound BDR hired November 1, 2022 (his birthday), Brayden (@03:07).
- Mix: outbound went from ~0% to a peak of ~70%; growth leader hired ~June/July 2023; now inbound ~60–70%, outbound ~30–40%, partner ~5–10% (@05:08–@06:13).
- Partner motion launched "less than 90 days ago" via a channel relationship with one of the largest US food distributors (@06:13).
- ~26 BDRs (≈6–7 inbound SDRs, rest outbound), four managers, new director Ryan Berner; 16–17 AEs (@06:13, @11:31).
- 2:1 outbound BDR-to-AE ratio (@06:13). BDRs produce ~70–80K closed-won ARR per month; average BDR cost ~70–80K (@07:16).
- BDR success rate "might be like 15 to 20%"; typical BDR tenure ~24 months (@12:33–@13:36).
- AE cost per prospecting hour is about double a BDR's (@15:45).
- RevOps/GTM ops: 3 full-time + 2 contractors (+ consultants) supporting ~100 people; ~1:20 ratio (@19:55–@20:56).
- Demand-gen spend "hundreds of thousands of dollars" per month; a ramping SDR "might be costing you tens of thousands of dollars" (@36:28).
- DM conversation-to-book rate ~4% → ~16% (figures stated by host; Kyle explains the drivers) (@40:37–@42:42).

## Frameworks & named ideas
- **Formers** — re-prospecting former inbound leads as the first outbound motion (@05:08).
- **Pods + round-robin rotator** (single-location / multi-location pods) (@08:16).
- **Golden script** — learn the core before "you color outside the lines"; shape pitch by third-party marketplace use (@43:45).
- **Local name drop** — nearest Owner customer surfaced in Salesloft; adherence checked by a Momentum prompt (@37:32–@39:35).
- **Coaching mastery** (his Substack guide): questions-based, focused, data-driven, one thing at a time (@41:38).
- **Biggest needle mover** — Brett Bombach's weekly rep/manager doc on one conversion lever (@41:38–@42:42).
- **Hiring framework: DNA / craft / specialized knowledge**; Brad Stulberg's "rugged flexibility" (@46:51–@47:53).

## Stories / anecdotes
- One of the earliest Salesloft Cadence customers; as global BDR director at Vision Critical, tooling gave ~3x activity volume; learned RevOps from Navin (now RevOps at 1Password) (@17:47–@18:49).
- Jonathan Shankman ("the wizard") built the data/scoring system — "I didn't build any of this stuff" (@26:07–@27:08).
- Avara came via a fund he's involved in; Owner was an early design partner (@34:26).
- His daughter walked into the recording (@13:36).
- First BDR came via referral — cousin of a BDR who worked for him ~8 years earlier; years of LinkedIn brand building fed early hiring (@44:47).

## Concepts & entities
- [[outbound-at-scale]] · [[smb-sales-motion]] · [[icp-and-saying-no]] · [[revops]] · [[gtm-engineering]] · [[org-design]]
- [[sales-hiring]] · [[talent-density]] · [[sales-coaching-and-enablement]] · [[ai-sales-stack]] · [[ai-sdrs-and-agents]] · [[career-and-leadership]]
- [[kyle-norton]] · [[owner-com]] · [[outbound-kitchen]] · [[pavilion]] · [[person-elric-legloire]] · [[person-jonathan-shankman]] · [[person-brett-bombach]]
- Related source: [[src-outbound-kitchen-ai-sdrs-dead-wrong]]
