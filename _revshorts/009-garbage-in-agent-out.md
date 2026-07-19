---
layout: revshort
title: "Garbage in, agent out"
description: "The board saw Agentforce at a conference, now AI has to go into the CRM. Understandable wish. Except: an AI agent on a broken data model produces the..."
date: 2026-03-22
read_time: "2 min read"
category: "AI"
hero_icon: "sparkles"
lang: en
translation: /de/revshorts/009-garbage-in-agent-out/
---

The board saw Agentforce at a conference, now AI has to go into the CRM. Understandable wish. Except: an AI agent on a broken data model produces the same nonsense your processes did before, just faster, around the clock, and confidently worded.

A concrete example from the field. An agent is supposed to automatically assign incoming inquiries to the right account owner. Sounds like a two-day project. But in the org, Müller GmbH exists four times: once as Müller GmbH, once as Mueller GmbH & Co. KG, once as MÜLLER (imported from the old system), and once as a test account somebody created in 2022 and never deleted. The agent routes the inquiry to the owner of the wrong duplicate, that colleague left a year ago, the inquiry sits in an orphaned queue for twelve days. Before, a human would have caught it. The agent gets it wrong flawlessly.

Or the customer history. Ask a copilot for the history of an account whose activities are scattered across four duplicates and two legacy systems, and you get a fluently worded summary of a quarter of the truth. The model isn't even hallucinating in the technical sense. It correctly summarizes what's there. There's just almost nothing there.

Same mechanics with scoring. AI scoring on fields that are 60 percent empty, because they were never required and nobody maintains them, mainly learns one thing: which reps document properly. That correlates with likelihood to close about as well as the font size in the proposal.

The uncomfortable truth is that the unsexy groundwork makes up about 80 percent of a serious AI project. Merging duplicates. Defining and enforcing required fields. Deciding what an active customer is and when an opportunity is dead. Building processes so data gets created as a byproduct of work instead of as an extra chore. Only then do Agentforce, Breeze, or the Dynamics Copilot pay off, and then they actually do, because they're working on a model that reflects reality.

The vendors won't tell you this, by the way, because data hygiene demos poorly on a keynote stage. An agent writing an email live looks better than a dedupe job merging 3,000 accounts overnight. The dedupe job is still worth more.

Anyone selling you an AI project without having seen your data model first is selling you a turbocharger for a car with a flat tire. It goes faster. Just not where you want to go.
