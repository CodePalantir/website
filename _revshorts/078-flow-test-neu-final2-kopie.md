---
layout: revshort
title: "Flow_Test_NEW_final2_COPY"
description: "Open your automation list. Not the process documentation, which doesn't exist anyway. The actual list in the system."
date: 2026-05-30
read_time: "2 min read"
category: "AI"
hero_icon: "sparkles"
lang: en
translation: /de/revshorts/078-flow-test-neu-final2-kopie/
---

Open your automation list. Not the process documentation, which doesn't exist anyway. The actual list in the system.

In there you'll find things like "Lead Update," "Lead Update 2," "Flow_Test_NEW_final2_COPY," and a workflow named "Michael please do not delete." Michael left the company in 2023. Nobody knows what the thing does, but everyone is afraid to touch it.

That's not an anecdote, that's the normal state. In almost every org we audit, the automations are anonymous. They have names, sure, but names that reveal nothing: not which object they touch, not what triggers them, not whether they're even still actively needed. And then the thing happens that always happens. A field suddenly gets overwritten, a lead lands with the wrong team, an email goes out twice. Now the search begins.

With clean names, the search takes ten minutes. You filter by object, read the names, have your candidate. Without clean names it takes three days, because you have to open 47 flows one by one, click through them, and reconstruct in your head what they do. Three days during which the field keeps getting overwritten. We've been in debugging sessions where half the time went not into the problem but into archaeology: what even is this?

Naming conventions are documentation at zero cost. That's the real point. Prose documentation in a wiki goes stale the moment it's written, because it lives next to the system and nobody keeps it current. A name lives in the system itself. "Lead_BeforeSave_SetRegion" tells you object, timing, and purpose without you opening the flow. Costs five seconds of thought at creation. Saves hours on every single incident.

The convention itself barely matters. Object first or purpose first, underscores or not, you can argue about that, but you don't have to for long. All that matters: one rule, applied consistently, by everyone. Including the admin who's just quickly testing something. Especially him, because "just quickly testing something" becomes "final2_COPY," and "final2_COPY" becomes production logic that your routing hangs on three years later.

You can tell pretty precisely how an org is run by the state of its automation list. Not the culture slides, the list. How many of your flows could you identify by name without opening them?
